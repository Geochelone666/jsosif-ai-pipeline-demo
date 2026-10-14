"""Pin the shared snapshot schema so email producers cannot silently drift."""
import importlib
from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))


@pytest.fixture
def contract():
    return importlib.import_module('snapshot_contract')


def test_frozen_schema(contract):
    assert contract.CONTRACT_VERSION == '1.0'
    assert contract.REQUIRED_TOP_LEVEL == [
        'contract_version', 'identity', 'quant', 'ai_summary', 'freshness', 'disclaimer']
    assert contract.REQUIRED_IDENTITY == ['ticker', 'as_of', 'report_stamp']
    assert contract.REQUIRED_FRESHNESS == [
        'report_as_of', 'market_data_as_of', 'market_data_fetched_at',
        'ai_snapshot_as_of', 'snapshot_note', 'assumptions_version',
        'assumptions_checked', 'no_refresh_note']


@pytest.fixture
def payload():
    return {
        'contract_version': '1.0',
        'identity': {'ticker': 'AAPL', 'as_of': '2026-10-14', 'report_stamp': '20261014'},
        'quant': [
            {'metric': 'price', 'value': '200', 'availability': 'ok', 'reason': None},
            {'metric': 'pe', 'value': None, 'availability': 'missing', 'reason': 'No EPS'},
        ],
        'ai_summary': {'status': 'ok', 'sections': {'overview': 'Summary'}},
        'freshness': {
            'report_as_of': '2026-10-14', 'market_data_as_of': '2026-10-13',
            'market_data_fetched_at': '2026-10-14T00:00:00Z',
            'ai_snapshot_as_of': '2026-10-13', 'snapshot_note': '',
            'assumptions_version': '1', 'assumptions_checked': {},
            'no_refresh_note': '邮件生成不刷新任何数据',
        },
        'disclaimer': 'For research only.',
    }


def test_valid_payload(contract, payload):
    from copy import deepcopy
    before = deepcopy(payload)
    assert contract.validate_snapshot(payload) == []
    assert payload == before


@pytest.mark.parametrize('group, fields', [
    (None, ['contract_version', 'identity', 'quant', 'ai_summary', 'freshness', 'disclaimer']),
    ('identity', ['ticker', 'as_of', 'report_stamp']),
    ('freshness', ['report_as_of', 'market_data_as_of', 'market_data_fetched_at',
                   'ai_snapshot_as_of', 'snapshot_note', 'assumptions_version',
                   'assumptions_checked', 'no_refresh_note']),
    ('ai_summary', ['status', 'sections']),
])
def test_required_fields(contract, payload, group, fields):
    target = payload if group is None else payload[group]
    for field in fields:
        original = target.pop(field)
        assert any(field in error for error in contract.validate_snapshot(payload))
        target[field] = original


@pytest.mark.parametrize('field', ['metric', 'value', 'availability', 'reason'])
def test_required_quant_fields(contract, payload, field):
    del payload['quant'][0][field]
    assert any(field in error for error in contract.validate_snapshot(payload))


@pytest.mark.parametrize('path, value', [
    (('contract_version',), '2.0'), (('contract_version',), 1.0),
    (('identity',), None), (('quant',), []), (('quant',), {}),
    (('quant',), [None]), (('ai_summary',), []), (('freshness',), None),
    (('disclaimer',), ''), (('disclaimer',), '  '), (('disclaimer',), 12),
    (('identity', 'ticker'), ' '), (('identity', 'report_stamp'), None),
    (('identity', 'as_of'), '2026-02-29'), (('identity', 'as_of'), '2026-13-01'),
    (('identity', 'as_of'), '20261014'), (('identity', 'as_of'), '2026-1-01'),
    (('identity', 'as_of'), 20261014),
    (('ai_summary', 'status'), ''), (('ai_summary', 'status'), None),
    (('ai_summary', 'sections'), []), (('ai_summary', 'sections'), {'x': 1}),
    (('freshness', 'assumptions_checked'), []),
    (('freshness', 'report_as_of'), None),
    (('freshness', 'no_refresh_note'), 'Data refreshed'),
])
def test_invalid_fields(contract, payload, path, value):
    target = payload
    for key in path[:-1]:
        target = target[key]
    target[path[-1]] = value
    assert any(path[-1] in error for error in contract.validate_snapshot(payload))


@pytest.mark.parametrize('field, value', [
    ('metric', ''), ('metric', 1), ('value', 12), ('reason', []),
    ('availability', 'unknown'), ('availability', []), ('availability', None),
])
def test_invalid_quant_fields(contract, payload, field, value):
    payload['quant'][0][field] = value
    assert any(field in error for error in contract.validate_snapshot(payload))


@pytest.mark.parametrize('reason', [None, '', '  ', 42])
def test_missing_needs_reason(contract, payload, reason):
    payload['quant'][1]['reason'] = reason
    assert any('reason' in error for error in contract.validate_snapshot(payload))


@pytest.mark.parametrize('value', [None, [], 'snapshot', 42])
def test_invalid_payload_type(contract, value):
    assert contract.validate_snapshot(value)


def test_leap_day_and_empty_sections(contract, payload):
    payload['identity']['as_of'] = '2024-02-29'
    payload['identity']['report_stamp'] = '20240229'
    payload['ai_summary']['sections'] = {}
    assert contract.validate_snapshot(payload) == []


def test_collects_multiple_errors(contract, payload):
    del payload['identity']['ticker']
    payload['disclaimer'] = ''
    errors = contract.validate_snapshot(payload)
    assert any('ticker' in error for error in errors)
    assert any('disclaimer' in error for error in errors)
