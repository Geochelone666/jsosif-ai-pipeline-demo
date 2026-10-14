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
        'quant': [{'metric': 'Close', 'value': '1.00', 'availability': 'ok', 'reason': None}],
        'ai_summary': {'status': 'Unavailable', 'sections': {}},
        'freshness': {
            'report_as_of': '2026-10-14', 'market_data_as_of': 'N/A',
            'market_data_fetched_at': 'N/A', 'ai_snapshot_as_of': 'N/A',
            'snapshot_note': 'Retained snapshot', 'assumptions_version': '1',
            'assumptions_checked': {}, 'no_refresh_note': '邮件生成不刷新任何数据',
        },
        'disclaimer': 'Not investment advice.',
    }


@pytest.fixture
def reports(tmp_path, payload):
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


@pytest.mark.parametrize('key', gate.REQUIRED_TOP_LEVEL)
def test_fallback_required_keys(payload, monkeypatch, key):
    monkeypatch.setattr(gate, 'validate_snapshot', None)
    del payload[key]
    assert any(key in error for error in gate.check_snapshot_payload(payload))


@pytest.mark.parametrize('key', gate.REQUIRED_IDENTITY)
@pytest.mark.parametrize('value', [None, '', '  ', 0])
def test_fallback_identity(payload, monkeypatch, key, value):
    monkeypatch.setattr(gate, 'validate_snapshot', None)
    payload['identity'][key] = value
    assert any(f'identity.{key}' in error for error in gate.check_snapshot_payload(payload))


@pytest.mark.parametrize('value', [None, '', '  ', 0])
def test_fallback_disclaimer(payload, monkeypatch, value):
    monkeypatch.setattr(gate, 'validate_snapshot', None)
    payload['disclaimer'] = value
    assert any('disclaimer' in error for error in gate.check_snapshot_payload(payload))


@pytest.mark.parametrize('payload', [None, [], 'text', 1, {'identity': []}])
def test_fallback_bad_structure(payload, monkeypatch):
    monkeypatch.setattr(gate, 'validate_snapshot', None)
    assert gate.check_snapshot_payload(payload)


def test_shared_validator_is_authoritative(payload, monkeypatch):
    seen = []

    def validate(value):
        seen.append(value)
        return ['quant: shared contract error']

    monkeypatch.setattr(gate, 'validate_snapshot', validate)
    assert gate.check_snapshot_payload(payload) == ['quant: shared contract error']
    assert seen == [payload]


def test_fallback_valid(payload, monkeypatch):
    monkeypatch.setattr(gate, 'validate_snapshot', None)
    assert gate.check_snapshot_payload(payload) == []


@pytest.mark.parametrize('content', [b'{broken', b'\xff', b'null'])
def test_bad_json_does_not_stop_scan(reports, content):
    path = reports / 'BAD-intelligence-20261014.json'
    path.write_bytes(content)
    (reports / 'unrelated.json').write_text('{broken')
    (reports / 'DIR-intelligence-20261014.json').mkdir()
    result = gate.check_reports_dir(reports)
    assert (result['checked'], result['passed']) == (3, 2)
    assert len(result['failed']) == 1
    assert result['failed'][0]['file'] == str(path)
    assert result['failed'][0]['errors']


def test_main_reports_errors(reports, capsys):
    path = reports / 'TEST-intelligence-20261014.json'
    path.write_text('{}')
    with pytest.raises(SystemExit) as caught:
        gate.main([str(reports)])
    assert caught.value.code == 1
    output = capsys.readouterr().out
    assert 'checked=2 passed=1 failed=1' in output
    assert str(path) in output and 'disclaimer' in output


def test_main_success(reports, capsys):
    assert gate.main([str(reports)]) == 0
    assert 'checked=2 passed=2 failed=0' in capsys.readouterr().out


def test_empty_directory(tmp_path):
    assert gate.check_reports_dir(tmp_path) == {'checked': 0, 'passed': 0, 'failed': []}


def test_determinism_ignores_mapping_order():
    results = iter([{'a': 1, 'b': {'c': 2, 'd': 3}}, {'b': {'d': 3, 'c': 2}, 'a': 1}])
    assert gate.determinism_check(lambda: next(results))


def test_determinism_catches_reused_mutable_output():
    output = {'build': 0}

    def emit():
        output['build'] += 1
        return output

    assert not gate.determinism_check(emit)


def test_import_without_contract(payload, monkeypatch):
    import importlib
    import runpy

    original = importlib.import_module

    def without_contract(name, *args, **kwargs):
        if name == 'snapshot_contract':
            raise ModuleNotFoundError(name=name)
        return original(name, *args, **kwargs)

    monkeypatch.setattr(importlib, 'import_module', without_contract)
    module = runpy.run_path(str(Path(gate.__file__)))
    assert module['validate_snapshot'] is None
    assert module['check_snapshot_payload'](payload) == []
    del payload['disclaimer']
    assert module['check_snapshot_payload'](payload)


def test_optional_emitter_repeat_build(payload, monkeypatch):
    emitter = pytest.importorskip('snapshot_emit')
    emit = getattr(emitter, 'emit_frozen_snapshot', None)
    if emit is None:
        pytest.skip('Optional emitter is not available yet')
    # Test repeatability independently of the concurrently developed contract.
    monkeypatch.setattr(emitter, 'validate_snapshot', None)
    assert gate.determinism_check(
        emit, ticker='TEST', as_of='2026-10-14', quant_metrics={'Close': 1},
        ai=payload['ai_summary'], freshness=payload['freshness'],
        disclaimer=payload['disclaimer'])
