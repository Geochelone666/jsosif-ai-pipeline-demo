"""Freeze an assembled Markdown report into the shared snapshot contract."""
import json
from datetime import date, timedelta
from build_review_bundle import snapshot_payload
from snapshot_contract import validate_snapshot
from data_utils import number


def news_evidence(ai):
    """Account for every RSS headline without promoting incomplete AI evidence."""
    stats = ai.get('extraction_stats')
    keys = ('unique_headlines', 'rule', 'ai', 'unknown', 'irrelevant')
    if not isinstance(stats, dict):
        return {'count_reconciled': False, 'coverage_pct': None}
    counts = {key: stats.get(key, 0 if key == 'irrelevant' else None) for key in keys}
    valid = all(type(value) is int and value >= 0 for value in counts.values())
    if not valid:
        return {'count_reconciled': False, 'coverage_pct': None}
    unique = counts['unique_headlines']
    resolved = counts['rule'] + counts['ai'] + counts['irrelevant']
    return {**counts, 'resolved_headlines': resolved,
            'coverage_pct': round(100 * resolved / unique, 2) if unique else 100.0,
            'count_reconciled': resolved + counts['unknown'] == unique}


def freeze(path, quant, ai):
    metadata = json.loads(path.with_suffix('.json').read_text(encoding='utf-8'))
    payload = snapshot_payload(path, from_markdown=True)
    if quant.get('ticker', payload['identity']['ticker']) != payload['identity']['ticker']:
        raise ValueError('Quant ticker and report identity disagree')
    payload.update(ticker=quant.get('ticker', payload['identity']['ticker']), as_of=payload['identity']['as_of'],
                   assumptions_version=quant.get('assumptions_version', metadata.get('assumptions_version', 'N/A')),
                   assumptions_checked=quant.get('assumptions_checked', payload['freshness']['assumptions_checked']))
    payload['freshness'].update(
        assumptions_version=str(payload['assumptions_version']),
        assumptions_checked=payload['assumptions_checked'])
    report_date = date.fromisoformat(payload['as_of'])
    try:
        market_date = date.fromisoformat(quant.get('as_of'))
    except (TypeError, ValueError):
        market_date = None
    close = number(quant.get('metrics', {}).get('Close'))
    evidence = news_evidence(ai)
    payload['source_evidence'] = {'news': evidence,
                                  'market': {'observed_as_of': quant.get('as_of'),
                                             'history_count': quant.get('history_count', {})}}
    payload['source_status'] = {
        'market': 'ok' if market_date is not None and close is not None and close > 0 and
                  report_date - timedelta(days=4) <= market_date <= report_date
                  else 'failed',
        'news': 'degraded' if ai.get('error') or
                ai.get('ticker') != payload['identity']['ticker'] or
                ai.get('as_of') != payload['as_of'] or
                ai.get('fetch_status', {}).get('status', 'ok') != 'ok' or
                (not ai.get('extraction_stats', {}).get('unique_headlines') and
                 ai.get('fetch_status', {}).get('status') != 'ok') or
                not evidence['count_reconciled'] or evidence.get('unknown', 0) > 0 else 'ok'}
    payload['extraction_stats'] = ai.get('extraction_stats', {})
    payload['quality'] = 'ready' if all(v == 'ok' for v in payload['source_status'].values()) else 'degraded'
    errors = validate_snapshot(payload)
    if errors:
        raise ValueError('Invalid report snapshot: ' + '; '.join(errors))
    target = path.with_suffix('.json')
    tmp = target.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2, allow_nan=False) + '\n', encoding='utf-8')
    tmp.replace(target)
    return payload
