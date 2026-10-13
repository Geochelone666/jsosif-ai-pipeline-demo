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
    with pytest.raises(NotImplementedError, match='发送需 Lucas 明确批准'):
        mail.main([str(snapshot), '--send'])


def test_identity_conflict(snapshot):
    snapshot.with_suffix('.json').write_text('{"ticker": "COST", "as_of": "2026-10-08"}')
    with pytest.raises(ValueError):
        mail.build_email([snapshot], ['a@example.com'])
