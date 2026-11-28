"""Build an offline, retrospective stock-versus-candidate benchmark review."""
import argparse
from datetime import datetime
import hashlib
import json
from pathlib import Path

from benchmark_prices import MAX_BYTES, load_bundle as load_capture, validate_capture
from report_store import resolve_file
from research_data import PriceObservation, relative_performance
from shared_research_pack import ROOT, canonical, digest, exact_date, teams


def build(capture):
    validate_capture(capture)
    configured = teams(ROOT / 'config/research_teams.json')
    series = {row['symbol']: row for row in capture['series']}
    start, end = (exact_date(capture[k]) for k in ('start', 'end'))

    def observations(symbol):
        row = series.get(symbol)
        if row is None or row['status'] != 'observed': return []
        return [PriceObservation(symbol, exact_date(cell['observed_on']), cell['value'], row['currency'],
                                 datetime.fromisoformat(row['retrieved_at']), row['source_url'],
                                 adjustment_basis=row['adjustment_basis'])
                for cell in row['observations'] if cell['value'] is not None]

    groups = []
    for team in configured:
        pairs = []
        for stock in team['tickers']:
            for candidate in team['benchmark_candidates']:
                benchmark = candidate['ticker']
                a, b = series.get(stock), series.get(benchmark)
                result = relative_performance(observations(stock), observations(benchmark), start=start, end=end)
                reason = None
                for label, row in (('Stock', a), ('Candidate benchmark', b)):
                    if row is None:
                        reason = label + ' series was not captured'; break
                    if row['status'] != 'observed':
                        reason = label + ' series: ' + row['reason']; break
                if reason is None and b['currency'] != candidate['currency']:
                    reason = 'Candidate currency differs from configured currency'
                if reason:
                    result = {'status': 'missing', 'start': capture['start'], 'end': capture['end'],
                              'stock_return_pct': None, 'benchmark_return_pct': None,
                              'relative_return_pp': None, 'reason': reason}
                pairs.append({'stock': stock, 'benchmark': benchmark, 'benchmark_status': 'proposed',
                              'stock_series_id': digest(a) if a else None,
                              'benchmark_series_id': digest(b) if b else None, 'result': result})
        groups.append({'id': team['id'], 'name': team['name'], 'pairs': pairs})
    pairs = [pair for group in groups for pair in group['pairs']]
    available = sum(p['result']['status'] == 'available' for p in pairs)
    payload = {'schema_version': 1, 'kind': 'candidate_benchmark_review', 'delivery_ready': False,
               'point_in_time_eligible': False, 'capture': capture, 'configuration': configured,
               'configuration_id': digest(configured), 'groups': groups,
               'coverage': {'stocks': sum(len(t['tickers']) for t in configured), 'groups': len(groups),
                            'pairs': len(pairs), 'available_pairs': available, 'missing_pairs': len(pairs)-available,
                            'captured_series': len(series)}}
    return {'review_id': digest(payload), **payload}


def validate(value):
    if not isinstance(value, dict) or 'capture' not in value or canonical(value) != canonical(build(value['capture'])):
        raise ValueError('Review differs from recomputed capture evidence and current configuration')
    return value


def markdown(value):
    validate(value)
    capture, coverage = value['capture'], value['coverage']
    lines = ['# Candidate benchmark review — retrospective draft', '',
             ('**Synthetic/injected fixture — not provider observations.**' if capture['capture_mode'] == 'injected_fetcher'
              else 'Evidence mode: provider capture (retrospective observations).'), '',
             f"Observation window: {capture['start']} through {capture['end']} (inclusive).",
             f"Captured at: {capture['finished_at']}. Provider: yfinance. Capture: `{capture['capture_id']}`.",
             f"Review: `{value['review_id']}`. Configuration: `{value['configuration_id']}`.", '',
             f"Coverage: {coverage['available_pairs']} / {coverage['pairs']} comparable pairs; "
             f"{coverage['missing_pairs']} missing across {coverage['stocks']} stocks and {coverage['groups']} groups.", '',
             'All ETF benchmarks remain proposed. Delivery ready: false. Point-in-time eligible: false.',
             'Each pair uses exact common endpoints, one currency and adjusted close prices. No forward fill, '
             'currency conversion, sector average or Consumer ETF blend is applied.',
             'Returns are adjusted-price changes, not a certified total-return methodology. Historical values may '
             'be revised by the provider. Provider symbol metadata is not verified exchange/MIC identity.',
             'Hashes detect inconsistent retained content; they do not authenticate the provider. '
             'Use the accompanying JSON for retained prices, metadata, source URLs and retrieval times.', '']
    def percent(number): return 'missing' if number is None else f'{number:.4f}'
    for group in value['groups']:
        lines += ['## '+group['name'], '',
                  '| Stock | Proposed ETF | Currency | Stock % | ETF % | Difference (pp) | Evidence / gap |',
                  '| --- | --- | --- | ---: | ---: | ---: | --- |']
        for pair in group['pairs']:
            result = pair['result']
            fields = [pair['stock'], pair['benchmark'], result.get('currency', 'missing'),
                      percent(result['stock_return_pct']), percent(result['benchmark_return_pct']),
                      percent(result['relative_return_pp']), result.get('reason', 'Exact endpoints available')]
            lines.append('| '+' | '.join(fields)+' |')
        lines.append('')
    lines += ['## Retained series', '', '| Symbol | Currency | Status | Source |', '| --- | --- | --- | --- |']
    for row in capture['series']:
        lines.append(f"| {row['symbol']} | {row['currency'] or 'missing'} | {row['reason'] or row['status']} | "
                     f"[Price history]({row['source_url']}) |")
    return '\n'.join(lines)+'\n'


def write_bundle(value, output):
    validate(value); output = Path(output)
    if output.resolve().is_relative_to(ROOT): raise ValueError('Review output must be outside the repository')
    files = {'benchmark-review.json': (json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False)+'\n').encode(),
             'benchmark-review.md': markdown(value).encode()}
    if any(len(raw) > MAX_BYTES for raw in files.values()): raise ValueError('Review exceeds size limit')
    manifest = {'schema_version': 1, 'kind': value['kind'], 'review_id': value['review_id'],
                'files': {name: hashlib.sha256(raw).hexdigest() for name, raw in files.items()}}
    output.mkdir(parents=False, exist_ok=False)
    files['manifest.json'] = (json.dumps(manifest, indent=2)+'\n').encode()
    for name, raw in files.items():
        with (output/name).open('xb') as stream: stream.write(raw)
    return manifest


def load_bundle(root):
    def read(name, limit=MAX_BYTES):
        with resolve_file(root, name).open('rb') as stream: raw = stream.read(limit+1)
        if len(raw) > limit: raise ValueError('Review input exceeds size limit')
        return raw
    manifest = json.loads(read('manifest.json', 65536))
    if (not isinstance(manifest, dict) or set(manifest) != {'schema_version', 'kind', 'review_id', 'files'}
            or type(manifest['schema_version']) is not int or manifest['schema_version'] != 1
            or manifest['kind'] != 'candidate_benchmark_review' or not isinstance(manifest['files'], dict)
            or set(manifest['files']) != {'benchmark-review.json', 'benchmark-review.md'}):
        raise ValueError('Invalid review manifest')
    files = {name: read(name) for name in manifest['files']}
    if any(hashlib.sha256(raw).hexdigest() != manifest['files'][name] for name, raw in files.items()):
        raise ValueError('Review checksum mismatch')
    value = validate(json.loads(files['benchmark-review.json']))
    if value['review_id'] != manifest['review_id'] or files['benchmark-review.md'] != markdown(value).encode():
        raise ValueError('Review identity or rendered content mismatch')
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--capture', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.output.resolve().is_relative_to(args.capture.resolve()):
            raise ValueError('Review output must not modify the capture bundle')
        value = build(load_capture(args.capture)); write_bundle(value, args.output)
    except (OSError, ValueError, TypeError, KeyError, AttributeError):
        parser.error('Review failed; use an intact capture and a new output directory outside inputs and repository')
    print('Benchmark review saved: ' + str(value['coverage']['available_pairs']) + '/' +
          str(value['coverage']['pairs']) + ' comparable pairs; delivery_ready=false')


if __name__ == '__main__': main()
