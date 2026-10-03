"""Validate report sections and rounding against ticker snapshots."""
from decimal import Decimal
import csv
import json
import re
from data_utils import ROOT, save

sections = ('QUANTITATIVE', 'TAILWINDS', 'HEADWINDS', 'CATALYSTS', 'RISKS', 'PEER COMPARABLES', 'EARNINGS CALENDAR', 'MACRO (FRED)', 'LATEST FILING (EDGAR)', 'SOURCES')
results = {}
index = ['# Intelligence reports', '', 'Snapshot date: 2026-10-03. Missing data is N/A.', '']
for ticker in ('NVDA', 'MSFT', 'AAPL'):
    report_name = f'{ticker}-intelligence-20261003.md'
    report = (ROOT / report_name).read_text()
    quant = json.loads((ROOT / f'{ticker.lower()}-quant.json').read_text())
    ai = json.loads((ROOT / f'{ticker.lower()}-ai-intel.json').read_text())
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
    index.append(f'- [{ticker}]({report_name}): close {close_text}; 1Y return {ret_text}; AI items {count_text}.')
    results[ticker] = {'sections_passed': True, 'quant_matches_json': True, 'ai_items': count_text, 'market_errors': quant['errors'], 'ai_error': ai.get('error')}
# Independent arithmetic from raw NVDA CSV, using the recorded boundary date.
quant = json.loads((ROOT / 'nvda-quant.json').read_text())
v = quant['verification']
if v:
    with (ROOT / 'NVDA-yfinance.csv').open() as stream:
        rows = list(csv.DictReader(stream))
    base = next(Decimal(row['Close']) for row in rows if row['Date'].startswith(v['base_date']))
    end = next(Decimal(row['Close']) for row in rows if row['Date'].startswith(quant['as_of']))
    computed = (end - base) / base * 100
    assert abs(computed - Decimal(str(quant['metrics']['Return 1Y (%)']))) < Decimal('1e-10')
    results['independent_nvda_1Y'] = {'base_close': str(base), 'end_close': str(end), 'return_pct': str(computed), 'passed': True}
else:
    results['independent_nvda_1Y'] = {'passed': False, 'reason': 'N/A: market data unavailable'}
(ROOT / 'INDEX.md').write_text('\n'.join(index) + '\n')
save('phase1-validation.json', results)
print(json.dumps(results, indent=2))
