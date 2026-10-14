"""Build frozen email payloads from supplied data without refreshing sources."""
from copy import deepcopy
import json

try:
    if __package__:
        from .snapshot_contract import CONTRACT_VERSION, validate_snapshot
    else:
        from snapshot_contract import CONTRACT_VERSION, validate_snapshot
except ModuleNotFoundError as exc:
    if exc.name != (__package__ + '.snapshot_contract' if __package__ else 'snapshot_contract'):
        raise
    # Allow the builder to ship before the shared contract module is available.
    CONTRACT_VERSION = '1.0'
    validate_snapshot = None


NO_REFRESH_NOTE = ('Report date is not a guarantee of data freshness. '
                   'No data is refreshed by email generation.')


def emit_frozen_snapshot(*, ticker, as_of, quant_metrics: dict, ai: dict,
                         freshness: dict, disclaimer: str,
                         availability_reasons: dict | None = None) -> dict:
    """Assemble the fixed contract so missing inputs retain explicit placeholders.

    Only None marks a missing metric; zero and empty strings remain available.
    Copy nested assumptions so later upstream edits cannot alter this snapshot.
    When installed, the shared validator is authoritative and errors raise ValueError.
    """
    reasons = availability_reasons or {}
    quant = []
    for metric, value in quant_metrics.items():
        quant.append({
            'metric': metric,
            'value': None if value is None else str(value),
            'availability': 'missing' if value is None else 'ok',
            'reason': (reasons.get(metric) or 'N/A') if value is None else None,
        })
    frozen_freshness = {
        field: freshness.get(field, 'N/A')
        for field in ('report_as_of', 'market_data_as_of', 'market_data_fetched_at',
                      'ai_snapshot_as_of', 'snapshot_note', 'assumptions_version')
    }
    frozen_freshness['assumptions_checked'] = deepcopy(freshness.get('assumptions_checked', {}))
    frozen_freshness['no_refresh_note'] = NO_REFRESH_NOTE
    payload = {
        'contract_version': CONTRACT_VERSION,
        'identity': {'ticker': ticker, 'as_of': as_of, 'report_stamp': as_of.replace('-', '')},
        'quant': quant,
        'ai_summary': {
            'status': ai.get('status') or ai.get('error') or 'N/A',
            'sections': {key: value for key, value in (ai.get('sections') or {}).items()
                         if isinstance(value, str)},
        },
        'freshness': frozen_freshness,
        'disclaimer': disclaimer,
    }
    if validate_snapshot is not None:
        errors = validate_snapshot(payload)
        if errors:
            raise ValueError('Invalid frozen snapshot:\n' + '\n'.join(errors))
    return payload


def snapshot_to_json(payload) -> str:
    """Serialize deterministically so identical snapshots have identical bytes."""
    return json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)
