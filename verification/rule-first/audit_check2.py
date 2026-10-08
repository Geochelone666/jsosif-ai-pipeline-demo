"""Independent checks of this run's raw CSV, source linkage and rendered data."""
import csv
import json
import math
from datetime import date, timedelta
from pathlib import Path
from email.utils import parsedate_to_datetime
import numpy as np

ROOT = Path(__file__).parent
def load(name):
    return json.loads((ROOT / name).read_text())
def closes(ticker):
    with (ROOT / f'{ticker}-yfinance.csv').open() as stream:
        return {date.fromisoformat(r['Date'][:10]): float(r['Close']) for r in csv.DictReader(stream)}
results = {}
for ticker in ('NVDA', 'MSFT', 'AAPL', 'GOOGL', 'AMZN', 'TSLA'):
    prefix = ticker.lower()
    q = load(f'{prefix}-quant.json')
    m = q['metrics']
    assert not q['errors'], (ticker, q['errors'])
    assert len(m) == 22 and all(v is not None and math.isfinite(v) for v in m.values())
    raw = closes(ticker)
    days = sorted(raw)
    end = days[-1]
    close = raw[end]
    expected = {'Close': close}
    boundaries = {'Return 1D (%)': days[-2], 'Return 1W (%)': end-timedelta(days=7),
                  'Return 1M (%)': end.replace(month=end.month-1), 'Return YTD (%)': date(end.year-1, 12, 31),
                  'Return 1Y (%)': end.replace(year=end.year-1)}
    for key, boundary in boundaries.items():
        base = raw[max(d for d in days if d <= boundary)]
        expected[key] = (close-base)/base*100
    window = [raw[d] for d in days if d >= end.replace(year=end.year-1)]
    returns = np.diff(window)/np.asarray(window[:-1])
    expected['Annualized volatility (%)'] = np.std(returns, ddof=1)*math.sqrt(252)*100
    expected['Sharpe (rf=0)'] = np.mean(returns)/np.std(returns, ddof=1)*math.sqrt(252)
    expected['Max drawdown (%)'] = min(v/max(window[:i+1])-1 for i,v in enumerate(window))*100
    for n in (50,200):
        expected[f'MA{n}'] = sum(raw[d] for d in days[-n:])/n
        expected[f'Close vs MA{n} (%)'] = (close/expected[f'MA{n}']-1)*100
    for key,value in expected.items():
        assert math.isclose(value,m[key],rel_tol=1e-9,abs_tol=1e-9), (ticker,key,value,m[key])
    ai = load(f'{prefix}-ai-intel.json')
    assert not ai.get('error')
    rss = load(f'{prefix}-rss-items.json')
    assert len(rss)==25
    sources = {i['headline']:i for i in rss}
    report = (ROOT/f'{ticker}-intelligence-20261003.md').read_text()
    items = [i for key in ('tailwinds','headwinds','catalysts','risks') for i in ai[key]]
    assert items
    for item in items:
        src = sources[item['headline']]
        assert item['date'] == parsedate_to_datetime(src['pubDate']).date().isoformat() <= '2026-10-03'
        assert item['headline'] in report and item['summary'] in report and src['link'] in report
    peers = load(f'{prefix}-comparables.json')['peers']
    assert len(peers)==4
    missing = {p['ticker']:[k for k,v in p.items() if v is None] for p in peers}
    earnings = load(f'{prefix}-earnings.json')
    assert earnings['last_earnings'] <= '2026-10-04' < earnings['next_earnings']
    for key in ('last_earnings','next_earnings'):
        assert earnings[key] in report
    edgar = load(f'{prefix}-edgar.json')
    assert all(edgar[k] is not None for k in ('latest_filing','revenue','net_income'))
    assert edgar['latest_filing']['url'] in report
    for key in ('revenue','net_income'):
        assert f"{edgar[key]['value']:,.2f}" in report and edgar[key]['period'] in report
    results[ticker] = {'market_as_of':q['as_of'], 'numeric_metrics':len(m), 'independent_metrics_passed':list(expected),
                       'rss_items':len(rss),'ai_items':len(items),'ai_sources_and_report_match':True,
                       'peer_missing_fields':missing,'earnings':earnings,'edgar_fields_present':3,'report_data_match':True}
(ROOT/'stage-audit-check2.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
