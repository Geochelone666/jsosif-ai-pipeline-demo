import json
from pathlib import Path
from email.utils import parsedate_to_datetime
import pandas as pd
import numpy as np

root = Path(__file__).resolve().parent
result = {}
for ticker in ('NVDA', 'MSFT', 'AAPL', 'GOOGL', 'AMZN', 'TSLA'):
    def read(name):
        return json.loads((root / f'{ticker.lower()}-{name}.json').read_text())
    q, ai, peers, earnings, edgar, rss = [read(n) for n in ('quant', 'ai-intel', 'comparables', 'earnings', 'edgar', 'rss-items')]
    assert not q['errors'] and not ai.get('error')
    assert all(v is not None and np.isfinite(v) for v in q['metrics'].values())
    c = pd.read_csv(root / f'{ticker}-yfinance.csv', index_col=0, parse_dates=True)['Close']
    c.index = pd.to_datetime(c.index, utc=True).tz_convert('America/New_York').tz_localize(None).normalize()
    c = c.loc[:q['as_of']]
    end = c.index[-1]
    targets = {'Return 1D (%)': c.index[-2], 'Return 1W (%)': end-pd.Timedelta(days=7), 'Return 1M (%)': end-pd.DateOffset(months=1), 'Return YTD (%)': pd.Timestamp('2025-12-31'), 'Return 1Y (%)': end-pd.DateOffset(years=1)}
    checks = {}
    for key, boundary in targets.items():
        value = (c.iloc[-1]-c.loc[:boundary].iloc[-1])/c.loc[:boundary].iloc[-1]*100
        assert abs(value-q['metrics'][key]) < 1e-10
        checks[key] = float(value)
    for n in (50, 200):
        assert abs(c.iloc[-n:].mean()-q['metrics'][f'MA{n}']) < 1e-10
    window = c.loc[end-pd.DateOffset(years=1):]
    returns = window.pct_change().dropna()
    assert abs(returns.std(ddof=1)*np.sqrt(252)*100-q['metrics']['Annualized volatility (%)']) < 1e-10
    assert abs((window/window.cummax()-1).min()*100-q['metrics']['Max drawdown (%)']) < 1e-10
    assert len(rss) == 25
    dates = {x['headline']: parsedate_to_datetime(x['pubDate']).date().isoformat() for x in rss}
    assert all(d <= '2026-10-03' for d in dates.values())
    report = (root / f'{ticker}-intelligence-20261003.md').read_text()
    count = 0
    for key in ('tailwinds', 'headwinds', 'catalysts', 'risks'):
        for item in ai[key]:
            assert item['date'] == dates[item['headline']]
            assert item['headline'] in report and item['summary'] in report
            assert any(x['link'] in report for x in rss if x['headline']==item['headline'])
            count += 1
    assert count > 0
    assert len(peers['peers']) == 4
    missing = {row['ticker']: [k for k in ('pe','pb','ev_ebitda','revenue_growth','mktcap','ret_1y') if row[k] is None] for row in peers['peers']}
    assert all(not fields or (symbol in ('F', 'RIVN', 'LCID') and fields == ['pe']) for symbol, fields in missing.items())
    assert earnings['last_earnings'] and earnings['next_earnings']
    assert all(edgar[k] for k in ('latest_filing','revenue','net_income'))
    assert edgar['latest_filing']['url'] in report
    assert earnings['last_earnings'] in report and earnings['next_earnings'] in report
    result[ticker] = {'passed': True, 'market_as_of': q['as_of'], 'close': q['metrics']['Close'], 'independent_returns': checks, 'ma_volatility_drawdown_passed': True, 'rss_items': len(rss), 'ai_items': count, 'ai_dates_headlines_sources_match': True, 'peer_missing_fields': missing, 'earnings_date_fields': '2/2', 'edgar_fields': '3/3', 'report_matches': True}
(root / 'stage-audit-check3.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
