"""Private spreadsheet import drives personal subscriptions without sending email."""
from copy import deepcopy
import json
from pathlib import Path
import shutil
import stat
import subprocess
import sys

import pytest

from prepare_subscriptions import prepare
from subscriptions import import_members_csv, research_tickers, tickers_for, validate


HEADER = 'id,name,email,groups,tickers,enabled,timezone,send_weekday,send_time\r\n'
ROSTER = HEADER + (
    'member-001,"Alice, Example",alice@example.com,research,CSCO;JPM,yes,America/Toronto,2,09:00\r\n'
    'member-002,Bob Example,bob@example.com,research,COST,no,America/Toronto,4,17:00\r\n')


def test_spreadsheet_creates_groups_and_preserves_personal_choices():
    base = {'groups': {}, 'members': [], 'max_report_age_days': 3}
    config = import_members_csv(base, '\ufeff' + ROSTER)
    assert base == {'groups': {}, 'members': [], 'max_report_age_days': 3}
    alice, bob = config['members']
    assert alice['id'] == 'member-001' and alice['name'] == 'Alice, Example'
    assert tickers_for(config, alice) == ['CSCO', 'JPM']
    assert tickers_for(config, bob) == ['COST']
    assert tickers_for(config) == ['CSCO', 'JPM']
    assert config['groups']['research']['tickers'] == ['COST', 'CSCO', 'JPM']
    assert research_tickers(config) == ['COST', 'CSCO', 'JPM']
    assert config['max_report_age_days'] == 3


def test_blank_personal_holdings_inherit_group_defaults():
    config = import_members_csv({'groups': {'research': {'tickers': ['ENB']}}, 'members': []},
                                ROSTER.replace('CSCO;JPM', ''))
    assert tickers_for(config, config['members'][0]) == ['ENB']
    assert config['groups']['research']['tickers'] == ['ENB']


def test_personal_holdings_can_be_used_without_groups():
    config = import_members_csv({'groups': {}, 'members': []}, ROSTER.replace(',research,', ',,'))
    assert config['groups'] == {}
    assert tickers_for(config, config['members'][0]) == ['CSCO', 'JPM']


def test_opt_out_affects_email_only():
    config = import_members_csv({'groups': {}, 'members': []}, ROSTER)
    for member in config['members']:
        member['enabled'] = False
    assert tickers_for(config) == []
    assert research_tickers(config) == ['COST', 'CSCO', 'JPM']


@pytest.mark.parametrize('text', [
    HEADER, '', HEADER.replace('email,', ''), HEADER.replace('tickers,', 'unexpected,'),
    ROSTER.replace(',yes,', ',maybe,'), ROSTER.replace(',2,09:00', ',Monday,09:00'),
    ROSTER.replace('CSCO;JPM', 'UNKNOWN'), ROSTER.replace('member-002', 'member-001'),
    ROSTER.replace('bob@example.com', 'alice@example.com'),
    HEADER + 'member-001,"Unclosed quote', ROSTER.replace('CSCO;JPM,yes', 'CSCO,JPM,yes'),
])
def test_invalid_spreadsheet_cannot_mutate_configuration(text):
    base = {'groups': {}, 'members': []}
    original = deepcopy(base)
    with pytest.raises(ValueError):
        import_members_csv(base, text)
    assert base == original


def test_legacy_csv_without_personal_holdings_is_supported():
    old = 'id,name,email,groups,enabled,timezone,send_weekday,send_time\n'
    old += 'one,Alice,alice@example.com,research,false,UTC,0,09:00\n'
    config = import_members_csv({'groups': {'research': {'tickers': ['CSCO']}}}, old)
    assert tickers_for(config, config['members'][0]) == ['CSCO']


def test_private_environment_table_is_loaded_atomically(tmp_path, monkeypatch):
    monkeypatch.delenv('SUBSCRIPTIONS_JSON', raising=False)
    monkeypatch.setenv('MEMBERS_CSV', ROSTER)
    target = tmp_path / 'subscriptions.json'
    assert prepare(target, required=True)
    config = validate(json.loads(target.read_text()))
    assert len(config['members']) == 2
    assert stat.S_IMODE(target.stat().st_mode) == 0o600
    previous = target.read_bytes()
    monkeypatch.setenv('MEMBERS_CSV', HEADER)
    with pytest.raises(ValueError):
        prepare(target, required=True)
    assert target.read_bytes() == previous
    assert list(tmp_path.iterdir()) == [target]


def test_json_settings_survive_table_replacement(tmp_path, monkeypatch):
    monkeypatch.setenv('SUBSCRIPTIONS_JSON', json.dumps({
        'groups': {'research': {'tickers': ['ENB']}}, 'members': [],
        'max_report_age_days': 2, 'allow_degraded': False}))
    monkeypatch.setenv('MEMBERS_CSV', ROSTER)
    target = tmp_path / 'subscriptions.json'
    prepare(target)
    config = json.loads(target.read_text())
    assert config['max_report_age_days'] == 2
    assert not config['allow_degraded']
    assert config['groups']['research']['tickers'] == ['ENB']


def test_missing_table_does_not_enable_delivery(tmp_path, monkeypatch):
    monkeypatch.delenv('SUBSCRIPTIONS_JSON', raising=False)
    monkeypatch.delenv('MEMBERS_CSV', raising=False)
    target = tmp_path / 'subscriptions.json'
    assert not prepare(target)
    with pytest.raises(ValueError):
        prepare(target, required=True)
    assert not target.exists()


def test_csv_cli_creates_a_private_configuration_without_a_json_template(tmp_path):
    root = Path(__file__).resolve().parents[1]
    csv = tmp_path / 'members.csv'; csv.write_text(ROSTER)
    target = tmp_path / 'config/subscriptions.local.json'
    subprocess.run([sys.executable, str(root / 'scripts/subscriptions.py'), str(target),
                    '--import-csv', str(csv)], check=True, capture_output=True)
    assert len(validate(json.loads(target.read_text()))['members']) == 2


def test_browser_csv_roundtrip_matches_the_actual_importer(tmp_path):
    node = shutil.which('node')
    if not node:
        pytest.skip('Node required for browser spreadsheet validation')
    root = Path(__file__).resolve().parents[1]
    script = (root / 'docs/members.html').read_text().split('<script>', 1)[1].split('</script>', 1)[0]
    target = tmp_path / 'spreadsheet.js'
    target.write_text(script + '''
const fs = require('node:fs');
const text = fs.readFileSync(0, 'utf8');
const config = JSOSIFConfig.importMembersCsv(text);
const exported = JSOSIFConfig.membersCsv(config);
process.stdout.write(JSON.stringify({config, exported}));
''')
    result = subprocess.run([node, str(target)], input=ROSTER, capture_output=True, text=True, check=True)
    browser = json.loads(result.stdout)
    python = import_members_csv({'groups': {}, 'members': []}, ROSTER)
    assert browser['config'] == python
    reimported = import_members_csv({'groups': {}, 'members': []}, browser['exported'])
    for member in reimported['members']:
        for field in ('preferred_frequency', 'preferred_weekdays', 'preferred_time', 'content_preferences', 'feedback'):
            assert member.pop(field) == ''
    assert reimported == python
