"""Offline contracts for the frozen v1 email snapshot."""
import json
from email import policy
from email.parser import BytesParser
from pathlib import Path
import socket
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import email_delivery as mail


@pytest.fixture
def snapshot(tmp_path):
    path = tmp_path / 'ACN-intelligence-20261008.md'
    path.write_text('''# ACN Intelligence Demo
- Report as_of: **2026-10-08**
- Market data as_of: **2026-10-07**
- AI analysis snapshot as_of: **2026-10-03** (retained)
- AI status: **Unavailable**
## QUANTITATIVE
| Metric | Value |
|---|---:|
| Close | 196.6400 |
## TAILWINDS
Growth <script>alert(1)</script>
''')
    path.with_suffix('.json').write_text(json.dumps({
        'ticker': 'ACN', 'as_of': '2026-10-08', 'assumptions_version': 1,
        'assumptions_checked': {'freshness': {'status': 'uncheckable', 'detail': 'No evidence'}}}))
    return path


def test_fields_and_missing_sections(snapshot):
    message = mail.build_email([snapshot], ['analyst@example.com'])
    assert 'ACN' in str(message['Subject']) and '2026-10-08' in str(message['Subject'])
    plain = message.get_body(preferencelist=('plain',)).get_content()
    html = message.get_body(preferencelist=('html',)).get_content()
    for field in ('196.6400', '2026-10-07', '2026-10-03', 'uncheckable', 'HEADWINDS', 'N/A', 'Not investment advice', 'Unavailable'):
        assert field in plain and field in html
    assert '<table>' in html and '<script>' not in html
    assert '&lt;script&gt;' in html


@pytest.mark.parametrize('payload', [{}, {'recipients': []}, {'recipients': 'a@example.com'},
    {'recipients': [None]}, {'recipients': ['bad']}, {'recipients': ['a@example.com\nBcc: b@example.com']},
    {'recipients': ['Name <a@example.com>']}, {'recipients': ['a@example.com', 'a@example.com']}])
def test_invalid_recipients(tmp_path, payload):
    path = tmp_path / 'recipients.json'
    path.write_text(json.dumps(payload))
    with pytest.raises(ValueError):
        mail.load_recipients(path)


def test_valid_recipients(tmp_path):
    path = tmp_path / 'recipients.json'
    path.write_text('{"recipients": ["a@example.com", "b@example.org"]}')
    assert mail.load_recipients(path) == ['a@example.com', 'b@example.org']


def test_sidecar_only_and_deduplication(snapshot):
    message = mail.build_email([snapshot, snapshot.with_suffix('.json')], ['a@example.com'])
    assert str(message['Subject']).count('ACN') == 1
    snapshot.unlink()
    plain = mail.build_email([snapshot.with_suffix('.json')], ['a@example.com']).get_body().get_content()
    assert 'N/A' in plain and 'uncheckable' in plain


def test_multiple_snapshots(snapshot, tmp_path):
    other = tmp_path / 'COST-intelligence-20261009.md'
    other.write_text('# COST Intelligence Demo\n')
    message = mail.build_email([snapshot, other], ['a@example.com'])
    for value in ('ACN', 'COST', '2026-10-08', '2026-10-09'):
        assert value in str(message['Subject'])


def test_dry_run_cli_no_network(snapshot, tmp_path, monkeypatch, capsys):
    def forbidden(*args, **kwargs):
        pytest.fail('Network call attempted')
    monkeypatch.setattr(socket.socket, 'connect', forbidden)
    monkeypatch.setattr(socket, 'create_connection', forbidden)
    monkeypatch.setattr(socket, 'getaddrinfo', forbidden)
    config = tmp_path / 'recipients.json'
    config.write_text('{"recipients": ["a@example.com"]}')
    target = tmp_path / 'preview.eml'
    mail.main([str(snapshot), '--recipients', str(config), '--output', str(target)])
    parsed = BytesParser(policy=policy.default).parsebytes(target.read_bytes())
    assert parsed.get_content_type() == 'multipart/alternative'
    assert [p.get_content_type() for p in parsed.iter_parts()] == ['text/plain', 'text/html']
    mail.main([str(snapshot), '--recipients', str(config), '--dry-run'])
    assert 'Subject:' in capsys.readouterr().out
    with pytest.raises(NotImplementedError, match='Explicit approval is required for email delivery'):
        mail.main([str(snapshot), '--send'])


def test_brief_format(snapshot, tmp_path):
    message = mail.build_email([snapshot], ['zhou6u@uwindsor.ca'], brief=True)
    plain = message.get_body(preferencelist=('plain',)).get_content()
    html = message.get_body(preferencelist=('html',)).get_content()
    for body in (plain, html):
        assert 'Hi Zhou6u,' in body
        assert 'ACN' in body and '2026-10-08' in body
        assert 'Best,' in body and 'Tech Team' in body
    # Brief format must not contain the full report dump
    assert '196.6400' not in plain


def test_brief_multiple_reports_and_pdfs(snapshot, tmp_path):
    other = tmp_path / 'COST-intelligence-20261008.md'
    other.write_text('# COST Intelligence Demo\n- Report as_of: **2026-10-08**\n')
    other.with_suffix('.json').write_text(json.dumps({'ticker': 'COST', 'as_of': '2026-10-08'}))
    pdf1 = tmp_path / 'ACN-intelligence-20261008.pdf'
    pdf2 = tmp_path / 'COST-intelligence-20261008.pdf'
    pdf1.write_bytes(b'%PDF-1.4 fake1')
    pdf2.write_bytes(b'%PDF-1.4 fake2')
    message = mail.build_email([snapshot, other], ['rodrick1@uwindsor.ca'],
                               brief=True, pdf_path=[pdf1, pdf2])
    plain = message.get_body(preferencelist=('plain',)).get_content()
    assert 'Hi Rodrick1,' in plain
    assert 'ACN' in plain and 'COST' in plain
    attachments = list(message.iter_attachments())
    assert len(attachments) == 2
    assert sorted(p.get_filename() for p in attachments) == [
        'ACN-intelligence-20261008.pdf', 'COST-intelligence-20261008.pdf']


def test_single_pdf_still_works(snapshot, tmp_path):
    pdf = tmp_path / 'ACN-intelligence-20261008.pdf'
    pdf.write_bytes(b'%PDF-1.4 fake')
    message = mail.build_email([snapshot], ['a@example.com'], pdf_path=pdf)
    assert len(list(message.iter_attachments())) == 1


def test_identity_conflict(snapshot):
    snapshot.with_suffix('.json').write_text('{"ticker": "COST", "as_of": "2026-10-08"}')
    with pytest.raises(ValueError):
        mail.build_email([snapshot], ['a@example.com'])
