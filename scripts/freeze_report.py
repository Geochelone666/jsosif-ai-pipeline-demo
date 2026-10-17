"""Freeze an assembled Markdown report into the shared snapshot contract."""
import json
from datetime import date, timedelta
from build_review_bundle import snapshot_payload
from snapshot_contract import validate_snapshot


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
    payload['source_status'] = {
        'market': 'ok' if quant.get('as_of') and quant['metrics'].get('Close') is not None and
                  date.fromisoformat(quant['as_of']) >= date.fromisoformat(payload['as_of']) - timedelta(days=4)
                  else 'failed',
        'news': 'degraded' if ai.get('error') or
                not ai.get('extraction_stats', {}).get('unique_headlines') or
                (ai.get('extraction_stats', {}).get('unknown', 0) > 0 and
                 ai.get('extraction_stats', {}).get('ai', 0) == 0) else 'ok'}
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
