import json
from email import policy
from email.parser import BytesParser
from pathlib import Path
import socket
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import distribute_team_reports as team


def test_team_dry_run(tmp_path, monkeypatch):
    def forbidden(*args, **kwargs):
        pytest.fail('Dry-run attempted network access')
    monkeypatch.setattr(socket, 'create_connection', forbidden)
    monkeypatch.setattr(socket.socket, 'connect', forbidden)
    monkeypatch.setenv('SEND_LEDGER_PATH', str(tmp_path / 'ledger.jsonl'))
    team.main(['--dry-run', '--output-dir', str(tmp_path)])
    expected = json.loads((team.ROOT / 'config/team_recipients.json').read_text())['assignments']
    files = list(tmp_path.glob('*.eml'))
    assert len(files) == len(expected)
    for path in files:
        message = BytesParser(policy=policy.default).parsebytes(path.read_bytes())
        ticker = expected[str(message['To'])]
        assert f'Holding: {ticker}' in message.get_body(preferencelist=('plain',)).get_content()
        assert message.get_content_type() == 'multipart/alternative'
        assert str(message['Subject']).count(';') == 0


def test_batch_validation_and_send_gate(tmp_path, monkeypatch):
    config = tmp_path / 'team.json'
    config.write_text(json.dumps({'assignments': {'a@example.com': 'CNQ.TO', 'b@example.com': 'CSCO'}}))
    (tmp_path / 'CNQ.TO-intelligence-20261008.md').write_text('# CNQ\n')
    with pytest.raises(ValueError, match='No common report date'):
        team.prepare(config, tmp_path)
    with pytest.raises(ValueError, match='Missing report'):
        team.prepare(config, tmp_path, '20261008')
    monkeypatch.delenv('JSOSIF_APPROVED_SEND', raising=False)
    with pytest.raises(SystemExit):
        team.main(['--send'])


def test_send_routes_separate_messages(tmp_path, monkeypatch):
    sent = []
    expected = json.loads((team.ROOT / 'config/team_recipients.json').read_text())['assignments']
    monkeypatch.setenv('SEND_LEDGER_PATH', str(tmp_path / 'ledger.jsonl'))
    monkeypatch.setenv('JSOSIF_APPROVED_SEND', '1')
    monkeypatch.setattr(team, 'send', sent.append)
    team.main(['--send'])
    assert len(sent) == len(expected)
    assert len({str(message['To']) for message in sent}) == len(expected)


@pytest.mark.parametrize('assignments', [{}, {'a@example.com': 'UNKNOWN'},
    {'a@example.com': 'CSCO', 'b@example.com': 'CSCO'}, {'bad': 'CSCO'}])
def test_invalid_assignments(tmp_path, assignments):
    config = tmp_path / 'team.json'
    config.write_text(json.dumps({'assignments': assignments}))
    with pytest.raises(ValueError):
        team.prepare(config, tmp_path)


def _ledger_rows(path):
    return [json.loads(line) for line in Path(path).read_text().splitlines() if line.strip()]


def test_send_ledger_records_sent_attempts(tmp_path, monkeypatch):
    ledger = tmp_path / 'ledger.jsonl'
    monkeypatch.setenv('SEND_LEDGER_PATH', str(ledger))
    monkeypatch.setenv('JSOSIF_APPROVED_SEND', '1')
    monkeypatch.setattr(team, 'send', lambda message: None)
    team.main(['--send'])
    expected = json.loads((team.ROOT / 'config/team_recipients.json').read_text())['assignments']
    rows = _ledger_rows(ledger)
    assert len(rows) == len(expected)
    assert {row['status'] for row in rows} == {'sent'}
    assert all(row['dry_run'] is False for row in rows)
    assert {row['recipients'][0] for row in rows} == set(expected)


def test_send_ledger_records_failed_attempt(tmp_path, monkeypatch):
    ledger = tmp_path / 'ledger.jsonl'
    monkeypatch.setenv('SEND_LEDGER_PATH', str(ledger))
    monkeypatch.setenv('JSOSIF_APPROVED_SEND', '1')

    def boom(message):
        raise RuntimeError('smtp down')

    monkeypatch.setattr(team, 'send', boom)
    with pytest.raises(RuntimeError, match='smtp down'):
        team.main(['--send'])
    rows = _ledger_rows(ledger)
    assert len(rows) == 1
    assert rows[0]['status'] == 'failed'
    assert 'smtp down' in rows[0]['error']
    assert rows[0]['dry_run'] is False


def test_send_ledger_records_dry_run(tmp_path, monkeypatch):
    ledger = tmp_path / 'ledger.jsonl'
    monkeypatch.setenv('SEND_LEDGER_PATH', str(ledger))
    team.main(['--dry-run', '--output-dir', str(tmp_path / 'eml')])
    rows = _ledger_rows(ledger)
    assert rows
    assert {row['status'] for row in rows} == {'dry-run'}
    assert all(row['dry_run'] is True for row in rows)
