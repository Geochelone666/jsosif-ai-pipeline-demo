"""Pin the email payload so upstream omissions cannot change its shape."""
import json
from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from snapshot_emit import NO_REFRESH_NOTE, emit_frozen_snapshot, snapshot_to_json


@pytest.fixture
def inputs():
    return dict(
        ticker='ACN', as_of='2026-10-08',
        quant_metrics={'Close': 196.64, 'Growth': None},
        ai={'status': 'ok', 'sections': {'TAILWINDS': '增长'}},
        freshness={
            'report_as_of': '2026-10-08', 'market_data_as_of': '2026-10-07',
            'market_data_fetched_at': '2026-10-08T12:00:00Z',
            'ai_snapshot_as_of': '2026-10-03', 'snapshot_note': 'retained',
            'assumptions_version': '1',
            'assumptions_checked': {'freshness': {'status': 'uncheckable'}},
        },
        disclaimer='Not investment advice.',
    )


def test_complete_payload(inputs):
    payload = emit_frozen_snapshot(**inputs)
    assert set(payload) == {
        'contract_version', 'identity', 'quant', 'ai_summary', 'freshness', 'disclaimer'}
    assert payload['contract_version'] == '1.0'
    assert payload['identity'] == {
        'ticker': 'ACN', 'as_of': '2026-10-08', 'report_stamp': '20261008'}
    assert payload['quant'] == [
        {'metric': 'Close', 'value': '196.64', 'availability': 'ok', 'reason': None},
        {'metric': 'Growth', 'value': None, 'availability': 'missing', 'reason': 'N/A'},
    ]
    assert payload['ai_summary'] == inputs['ai']
    assert payload['freshness'] == dict(inputs['freshness'], no_refresh_note=NO_REFRESH_NOTE)
    assert payload['disclaimer'] == inputs['disclaimer']
    try:
        from snapshot_contract import validate_snapshot
    except ModuleNotFoundError as exc:
        if exc.name != 'snapshot_contract':
            raise
    else:
        assert validate_snapshot(payload) == []


def test_missing_metrics(inputs):
    inputs['quant_metrics'] = {'Close': None, 'Growth': None}
    payload = emit_frozen_snapshot(**inputs, availability_reasons={'Close': 'No source'})
    assert [row['reason'] for row in payload['quant']] == ['No source', 'N/A']
    assert all(row['availability'] == 'missing' and row['value'] is None
               for row in payload['quant'])


def test_missing_ai_and_freshness(inputs):
    inputs.update(ai={}, freshness={})
    payload = emit_frozen_snapshot(**inputs)
    assert payload['ai_summary'] == {'status': 'N/A', 'sections': {}}
    assert payload['freshness'] == {
        'report_as_of': 'N/A', 'market_data_as_of': 'N/A',
        'market_data_fetched_at': 'N/A', 'ai_snapshot_as_of': 'N/A',
        'snapshot_note': 'N/A', 'assumptions_version': 'N/A',
        'assumptions_checked': {}, 'no_refresh_note': NO_REFRESH_NOTE,
    }


def test_stable_json(inputs):
    first = snapshot_to_json(emit_frozen_snapshot(**inputs))
    second = snapshot_to_json(emit_frozen_snapshot(**inputs))
    assert first.encode('utf-8') == second.encode('utf-8')
    assert '增长' in first
    assert first == json.dumps(json.loads(first), ensure_ascii=False, indent=2, sort_keys=True)
