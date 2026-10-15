"""Exercise SMTP over loopback with temporary credentials and a local TLS CA."""
import base64
from email import policy
from email.parser import BytesParser
import json
from pathlib import Path
import socket
import socketserver
import ssl
import subprocess
import sys
import threading
from contextlib import contextmanager

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import email_delivery as mail
import send_ledger


@pytest.fixture(autouse=True)
def isolate(tmp_path, monkeypatch):
    monkeypatch.setattr(mail, 'ROOT', tmp_path)
    monkeypatch.setenv('SEND_LEDGER_PATH', str(tmp_path / 'ledger.jsonl'))
    monkeypatch.delenv('JSOSIF_APPROVED_SEND', raising=False)
    resolve = socket.getaddrinfo

    def local_resolve(host, *args, **kwargs):
        assert host == '127.0.0.1', 'Non-loopback DNS forbidden'
        return resolve(host, *args, **kwargs)

    monkeypatch.setattr(socket, 'getaddrinfo', local_resolve)
    original = socket.socket.connect

    def loopback_only(sock, address):
        assert address[0] == '127.0.0.1', 'Non-loopback connection forbidden'
        return original(sock, address)

    monkeypatch.setattr(socket.socket, 'connect', loopback_only)


@pytest.fixture
def message(tmp_path):
    snapshot = tmp_path / 'ACN-intelligence-20261015.md'
    snapshot.write_text('# ACN\n## TAILWINDS\nLocal test 中文\n')
    pdf = tmp_path / 'report.pdf'
    pdf.write_bytes(b'%PDF-1.4 fake attachment')
    return mail.build_email([snapshot], ['reader@example.com'], pdf_path=pdf)


@pytest.fixture
def config(tmp_path):
    path = tmp_path / 'config' / 'gmail.json'
    path.parent.mkdir()
    path.write_text(json.dumps({'address': 'sender@example.com', 'app_password': 'fake-password'}))
    return path


@contextmanager
def fake_smtp(tmp_path, reject=False):
    cert, key = tmp_path / 'cert.pem', tmp_path / 'key.pem'
    subprocess.run(['openssl', 'req', '-x509', '-newkey', 'rsa:2048', '-nodes',
                    '-keyout', str(key), '-out', str(cert), '-days', '1',
                    '-subj', '/CN=localhost', '-addext', 'subjectAltName=IP:127.0.0.1'],
                   check=True, capture_output=True)
    server_tls = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    server_tls.load_cert_chain(cert, key)
    events, messages, errors = [], [], []

    class Handler(socketserver.StreamRequestHandler):
        def handle(self):
            try:
                self.connection.settimeout(5)
                self.wfile.write(b'220 local test\r\n')
                encrypted = False
                while line := self.rfile.readline():
                    verb = line.split()[0].decode()
                    events.append(verb)
                    if verb == 'EHLO':
                        self.wfile.write(b'250-localhost\r\n' +
                                         (b'250 AUTH PLAIN\r\n' if encrypted else b'250 STARTTLS\r\n'))
                    elif verb == 'STARTTLS':
                        self.wfile.write(b'220 ready\r\n')
                        self.rfile.close()
                        self.connection = server_tls.wrap_socket(self.connection, server_side=True)
                        self.rfile = self.connection.makefile('rb')
                        self.wfile = self.connection.makefile('wb', buffering=0)
                        encrypted = True
                    elif verb == 'AUTH':
                        assert encrypted
                        assert base64.b64decode(line.split()[2]) == b'\0sender@example.com\0fake-password'
                        self.wfile.write(b'235 authenticated\r\n')
                    elif verb in ('MAIL', 'RCPT', 'RSET'):
                        self.wfile.write(b'250 ok\r\n')
                    elif verb == 'DATA':
                        self.wfile.write(b'354 continue\r\n')
                        data = []
                        while (part := self.rfile.readline()) != b'.\r\n':
                            assert part
                            data.append(part[1:] if part.startswith(b'..') else part)
                        messages.append(b''.join(data))
                        self.wfile.write(b'550 fake-password rejected\r\n' if reject else b'250 accepted\r\n')
                    elif verb == 'QUIT':
                        self.wfile.write(b'221 bye\r\n')
                        break
                    else:
                        raise AssertionError(verb)
            except Exception as exc:
                errors.append(exc)

    with socketserver.TCPServer(('127.0.0.1', 0), Handler) as server:
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            yield server.server_address[1], ssl.create_default_context(cafile=str(cert)), events, messages
        finally:
            server.shutdown()
            thread.join(timeout=6)
            assert not thread.is_alive()
            assert not errors


@pytest.mark.parametrize('reject', [False, True])
def test_smtp_round_trip(tmp_path, config, message, reject):
    with fake_smtp(tmp_path, reject) as (port, context, events, messages):
        backend = mail.GmailSmtpBackend(config, host='127.0.0.1', port=port, tls_context=context)
        if reject:
            with pytest.raises(RuntimeError, match='SMTPDataError') as error:
                backend.deliver(message)
            assert 'fake-password' not in str(error.value)
        else:
            backend.deliver(message)
    assert events == ['EHLO', 'STARTTLS', 'EHLO', 'AUTH', 'MAIL', 'RCPT', 'DATA', 'QUIT']
    parsed = BytesParser(policy=policy.default).parsebytes(messages[0])
    assert parsed['From'] == 'sender@example.com'
    assert parsed['To'] == 'reader@example.com'
    assert 'ACN' in parsed['Subject']
    assert parsed.get_content_type() == 'multipart/mixed'
    for subtype in ('plain', 'html'):
        assert 'Local test 中文' in parsed.get_body(preferencelist=(subtype,)).get_content()
    attachment, = parsed.iter_attachments()
    assert attachment.get_content_type() == 'application/pdf'
    assert attachment.get_filename() == 'report.pdf'
    assert attachment.get_payload(decode=True) == b'%PDF-1.4 fake attachment'
    row, = send_ledger.query()
    assert row['dry_run'] is False
    assert row['status'] == ('failed' if reject else 'sent')
    assert row['recipients'] == ['reader@example.com']
    assert row['snapshot_id'] == 'ACN-2026-10-15'
    assert 'fake-password' not in json.dumps(row)
    assert bool(row['error']) == reject


@pytest.mark.parametrize('approval', [None, '', '0', 'true'])
def test_unapproved_cli_stops_before_config(monkeypatch, approval):
    if approval is not None:
        monkeypatch.setenv('JSOSIF_APPROVED_SEND', approval)
    def forbidden(*args, **kwargs):
        pytest.fail('Unapproved path read a file')
    monkeypatch.setattr(Path, 'read_text', forbidden)
    with pytest.raises(NotImplementedError, match='发送需 Lucas 明确批准'):
        mail.main(['missing.md', '--send'])


@pytest.mark.parametrize('payload', [None, 'bad json', '[]', '{}',
    '{"address": "sender@example.com"}',
    '{"address": "sender@example.com", "app_password": 123}',
    '{"address": "sender@example.com", "app_password": "  "}',
    '{"address": "sender@example.com", "app_password": "FILL_IN_TEST"}',
    '{"address": "bad", "app_password": "fake-password"}'])
def test_approved_cli_config_fail_closed(tmp_path, monkeypatch, message, payload):
    monkeypatch.setenv('JSOSIF_APPROVED_SEND', '1')
    monkeypatch.setattr(mail, 'load_recipients', lambda _: ['reader@example.com'])
    monkeypatch.setattr(mail, 'build_email', lambda *a, **k: message)
    path = tmp_path / 'config' / 'gmail.json'
    path.parent.mkdir()
    if payload is not None:
        path.write_text(payload)
    with pytest.raises(ValueError, match='Gmail config'):
        mail.main(['unused.md', '--send'])
    row, = send_ledger.query()
    assert row['status'] == 'failed' and row['dry_run'] is False
    assert row['error'] and 'fake-password' not in row['error']
