"""Validate report sections and rounding against ticker snapshots."""
from decimal import Decimal
import csv
import json
import re
import os
from datetime import date
from data_utils import DATA, REPORTS, ROOT, save, SUPPORTED, as_of_date


def build_health(results):
    """Machine-readable summary of validation results.

    Pure function: derives pass/fail/skip per item from the results dict
    without changing any original validation judgment. A ticker passes only
    when its sections and quant checks passed and neither market nor AI
    errors are recorded; an item marked skipped (or None) counts as skip.
    """
    items = {}
    for key, item in results.items():
        if key == '_health':
            continue
        if item is None or (isinstance(item, dict) and item.get('skipped')):
            items[key] = 'skip'
        elif key.startswith('independent_'):
            items[key] = 'pass' if isinstance(item, dict) and item.get('passed') is True else 'fail'
        elif (isinstance(item, dict) and item.get('sections_passed')
              and item.get('quant_matches_json')
              and not item.get('ai_error') and not item.get('market_errors')):
            items[key] = 'pass'
        else:
            items[key] = 'fail'
    passed = sum(1 for v in items.values() if v == 'pass')
    failed = sum(1 for v in items.values() if v == 'fail')
    skipped = sum(1 for v in items.values() if v == 'skip')
    if failed:
        status = 'fail'
    elif items:
        status = 'pass'
    else:
        status = 'skip'
    return {'status': status, 'total': len(items), 'passed': passed,
            'failed': failed, 'skipped': skipped, 'items': items}


AS_OF = as_of_date().isoformat()
STAMP = AS_OF.replace("-", "")

sections = ('QUANTITATIVE', 'TAILWINDS', 'HEADWINDS', 'CATALYSTS', 'RISKS', 'PEER COMPARABLES', 'EARNINGS CALENDAR', 'MACRO (FRED)', 'LATEST FILING (EDGAR)', 'SOURCES')
results = {}
index = ['# Intelligence reports', '', f'Snapshot date: {AS_OF}. Missing data is N/A. Report-date daily prices may be intraday and provisional. News and other non-market sections retain existing snapshots.', '']
for ticker in SUPPORTED:
    report_name = f'{ticker}-intelligence-{STAMP}.md'
    report = (REPORTS / report_name).read_text()
    quant = json.loads((DATA / f'{ticker.lower()}-quant.json').read_text())
    ai = json.loads((DATA / f'{ticker.lower()}-ai-intel.json').read_text())
    assert all(f'## {section}\n' in report for section in sections)
    table = report.split('## QUANTITATIVE\n', 1)[1].split('Methodology:', 1)[0]
    for key, value in quant['metrics'].items():
        digits = 2 if key in ('P/E (trailing)', 'P/B', 'EV/EBITDA', 'Revenue growth (%)') else 4
        expected = 'N/A' if value is None else f'{value:.{digits}f}'
        assert f'| {key} | {expected} |' in table, (ticker, key)
    count = sum(len(ai[k]) for k in ('tailwinds', 'headwinds', 'catalysts', 'risks'))
    close = quant['metrics'].get('Close')
    ret = quant['metrics'].get('Return 1Y (%)')
    close_text = 'N/A' if close is None else f'${close:.4f}'
    ret_text = 'N/A' if ret is None else f'{ret:.4f}%'
    count_text = 'N/A' if ai.get('error') else str(count)
    index.append(f'- [{ticker}](reports/{report_name}): close {close_text}; 1Y return {ret_text}; AI items {count_text}.')
    results[ticker] = {'sections_passed': True, 'quant_matches_json': True, 'ai_items': count_text, 'market_errors': quant['errors'], 'ai_error': ai.get('error')}
# Recompute each available raw CSV independently.
for ticker in SUPPORTED:
    quant = json.loads((DATA / f'{ticker.lower()}-quant.json').read_text())
    v = quant.get('verification')
    raw = DATA / f'{ticker}-yfinance.csv'
    if not v or not raw.exists():
        continue
    with raw.open() as stream:
        rows = list(csv.DictReader(stream))
    base = next(Decimal(row['Close']) for row in rows if row['Date'].startswith(v['base_date']))
    end = next(Decimal(row['Close']) for row in rows if row['Date'].startswith(quant['as_of']))
    computed = (end - base) / base * 100
    assert abs(computed - Decimal(str(quant['metrics']['Return 1Y (%)']))) < Decimal('1e-10')
    results[f'independent_{ticker}_1Y'] = {'passed': True, 'return_pct': str(computed)}
(ROOT / 'INDEX.md').write_text('\n'.join(index) + '\n')
results['_health'] = build_health(results)
save('phase1-validation.json', results)
print(json.dumps(results, indent=2))
