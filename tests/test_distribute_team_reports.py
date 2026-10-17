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
    team.main(['--dry-run', '--output-dir', str(tmp_path)])
    expected = json.loads((team.ROOT / 'config/team_recipients.json').read_text())['assignments']
    files = list(tmp_path.glob('*.eml'))
    assert len(files) == len(expected) == 5
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


def test_send_routes_separate_messages(monkeypatch):
    sent = []
    monkeypatch.setenv('JSOSIF_APPROVED_SEND', '1')
    monkeypatch.setattr(team, 'send', sent.append)
    team.main(['--send'])
    assert len(sent) == 5
    assert len({str(message['To']) for message in sent}) == 5


@pytest.mark.parametrize('assignments', [{}, {'a@example.com': 'UNKNOWN'},
    {'a@example.com': 'CSCO', 'b@example.com': 'CSCO'}, {'bad': 'CSCO'}])
def test_invalid_assignments(tmp_path, assignments):
    config = tmp_path / 'team.json'
    config.write_text(json.dumps({'assignments': assignments}))
    with pytest.raises(ValueError):
        team.prepare(config, tmp_path)


def test_two_members_same_stock_keep_separate_previews(tmp_path):
    config = tmp_path / 'team.json'
    config.write_text(json.dumps({'assignments': {
        'alice@example.com': 'CSCO', 'bob@example.com': 'CSCO'}}))
    output = tmp_path / 'previews'
    team.main(['--config', str(config), '--date', '20261008', '--output-dir', str(output)])
    files = list(output.glob('*.eml'))
    assert len(files) == 2
    assert {str(BytesParser(policy=policy.default).parsebytes(p.read_bytes())['To'])
            for p in files} == {'alice@example.com', 'bob@example.com'}

