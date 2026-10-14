"""Exercise the freeze gate offline so malformed snapshots cannot pass release checks."""
import json
from pathlib import Path
import random
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import snapshot_freeze_check as gate


@pytest.fixture
def payload():
    return {
        'contract_version': '1.0',
        'identity': {'ticker': 'TEST', 'as_of': '2026-10-14', 'report_stamp': '20261014'},
        'quant': {}, 'ai_summary': {}, 'freshness': {},
        'disclaimer': 'Not investment advice.',
    }


@pytest.fixture
def reports(tmp_path, payload, monkeypatch):
    # Isolate the minimum contract from concurrent changes in the optional module.
    monkeypatch.setattr(gate, 'validate_snapshot', None)
    for ticker in ('TEST', 'DEMO'):
        payload['identity']['ticker'] = ticker
        (tmp_path / f'{ticker}-intelligence-20261014.json').write_text(json.dumps(payload))
    return tmp_path


def test_reports_pass(reports):
    assert gate.check_reports_dir(reports) == {'checked': 2, 'passed': 2, 'failed': []}


def test_missing_disclaimer_identifies_file(reports):
    path = reports / 'TEST-intelligence-20261014.json'
    payload = json.loads(path.read_text())
    del payload['disclaimer']
    path.write_text(json.dumps(payload))
    result = gate.check_reports_dir(reports)
    assert (result['checked'], result['passed']) == (2, 1)
    assert len(result['failed']) == 1
    assert result['failed'][0]['file'] == str(path)
    assert 'disclaimer' in ' '.join(result['failed'][0]['errors'])


def test_determinism():
    assert gate.determinism_check(lambda value, *, scale: {'value': value * scale}, 2, scale=3)
    noise = random.Random(42)
    assert not gate.determinism_check(lambda: {'noise': noise.random()})


def test_main_bad_directory(tmp_path, capsys):
    with pytest.raises(SystemExit) as caught:
        gate.main([str(tmp_path / 'missing')])
    assert caught.value.code == 1
    assert 'failed=1' in capsys.readouterr().out
