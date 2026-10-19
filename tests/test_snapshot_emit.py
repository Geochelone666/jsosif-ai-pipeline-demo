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
        ai={'status': 'ok', 'sections': {'TAILWINDS': 'Growth ↑'}},
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
    assert 'Growth ↑' in first
    assert first == json.dumps(json.loads(first), ensure_ascii=False, indent=2, sort_keys=True)


@pytest.mark.parametrize('ai, expected', [
    ({'status': 'ok', 'error': 'failed'}, 'ok'),
    ({'status': '', 'error': 'failed'}, 'failed'),
    ({'status': None, 'error': ''}, 'N/A'),
])
def test_ai_status_precedence_and_section_filter(inputs, ai, expected):
    inputs['ai'] = dict(ai, sections={'text': 'Retained ✓', 'empty': '', 'number': 2, 'null': None})
    assert emit_frozen_snapshot(**inputs)['ai_summary'] == {
        'status': expected, 'sections': {'text': 'Retained ✓', 'empty': ''}}


def test_falsey_metrics_are_available(inputs):
    inputs['quant_metrics'] = {'Zero': 0, 'False': False, 'Empty': ''}
    rows = emit_frozen_snapshot(**inputs)['quant']
    assert [row['value'] for row in rows] == ['0', 'False', '']
    assert all(row['availability'] == 'ok' and row['reason'] is None for row in rows)


@pytest.mark.parametrize('reason', [None, ''])
def test_empty_missing_reason_uses_placeholder(inputs, reason):
    payload = emit_frozen_snapshot(**inputs, availability_reasons={'Growth': reason})
    assert payload['quant'][1]['reason'] == 'N/A'


def test_fixed_note_and_detached_assumptions(inputs):
    inputs['freshness']['no_refresh_note'] = 'upstream note'
    payload = emit_frozen_snapshot(**inputs)
    inputs['freshness']['assumptions_checked']['freshness']['status'] = 'changed'
    assert payload['freshness']['assumptions_checked']['freshness']['status'] == 'uncheckable'
    assert payload['freshness']['no_refresh_note'] == (
        'Report date is not a guarantee of data freshness. '
        'No data is refreshed by email generation.')
    assert inputs['freshness']['no_refresh_note'] == 'upstream note'


def test_shared_validation_errors_are_not_ignored(inputs, monkeypatch):
    import snapshot_emit

    monkeypatch.setattr(snapshot_emit, 'validate_snapshot', lambda payload: ['contract error'])
    with pytest.raises(ValueError, match='contract error'):
        emit_frozen_snapshot(**inputs)
