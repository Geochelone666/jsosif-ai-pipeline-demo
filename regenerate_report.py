#!/usr/bin/env python3
"""Regenerate the NVDA intelligence report with quant + AI results."""
import json

quant = json.load(open("quant.json", encoding="utf-8"))
q = quant["metrics"]
ai = json.load(open("ai-intel.json", encoding="utf-8"))
rss = json.load(open("rss-items.json", encoding="utf-8"))

# map rss links by headline for sources
link_by_headline = {}
for it in rss:
    link_by_headline[it["headline"]] = it["link"]

def section(name, items):
    out = [f"## {name}\n"]
    if not items:
        out.append("(No items in this run)\n")
        return "\n".join(out)
    for it in items:
        srcs = " ".join(f"<{u}>" for u in it.get("sources", []) if u)
        if not srcs:
            u = link_by_headline.get(it["headline"], "")
            srcs = f"<{u}>" if u else ""
        out.append(
            f"### {it['headline']}\n"
            f"- Summary: {it['summary']}\n"
            f"- Date: {it['date']} | Impact: {it['impact']} | Horizon: {it['horizon']} | Confidence: {it['confidence']}\n"
            + (f"- Sources: {srcs}\n" if srcs else "")
        )
    return "\n".join(out)

def fmt(v, d=4):
    if v is None:
        return "N/A"
    return f"{v:.{d}f}"

q = q  # metrics dict
quant_table = f"""## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | {fmt(q.get('Close'))} |
| Return 1D (%) | {fmt(q.get('Return 1D (%)'))} |
| Return 1W (%) | {fmt(q.get('Return 1W (%)'))} |
| Return 1M (%) | {fmt(q.get('Return 1M (%)'))} |
| Return YTD (%) | {fmt(q.get('Return YTD (%)'))} |
| Return 1Y (%) | {fmt(q.get('Return 1Y (%)'))} |
| Annualized volatility (%) | {fmt(q.get('Annualized volatility (%)'))} |
| Beta vs SPY | {fmt(q.get('Beta vs SPY'))} |
| Max drawdown (%) | {fmt(q.get('Max drawdown (%)'))} |
| Sharpe (rf=0) | {fmt(q.get('Sharpe (rf=0)'))} |
| P/E (trailing) | {fmt(q.get('P/E (trailing)'), 2)} |
| P/B | {fmt(q.get('P/B'), 2)} |
| EV/EBITDA | {fmt(q.get('EV/EBITDA'), 2)} |
| Revenue growth (%) | {fmt(q.get('Revenue growth (%)'), 2)} |
| MA50 | {fmt(q.get('MA50'))} |
| Close vs MA50 (%) | {fmt(q.get('Close vs MA50 (%)'))} |
| MA200 | {fmt(q.get('MA200'))} |
| Close vs MA200 (%) | {fmt(q.get('Close vs MA200 (%)'))} |
| RSI (14, Wilder) | {fmt(q.get('RSI (14, Wilder)'))} |
| MACD (12,26) | {fmt(q.get('MACD (12,26)'))} |
| MACD signal (9) | {fmt(q.get('MACD signal (9)'))} |
| MACD histogram | {fmt(q.get('MACD histogram'))} |
"""

all_sources = []
seen = set()
for sec in ("tailwinds", "headwinds", "catalysts", "risks"):
    for it in ai[sec]:
        for u in it.get("sources", []):
            if u and u not in seen:
                seen.add(u); all_sources.append(u)
        u = link_by_headline.get(it["headline"], "")
        if u and u not in seen:
            seen.add(u); all_sources.append(u)

report = f"""# NVDA Intelligence Demo

- ticker: **NVDA**
- Report as_of: **2026-10-03**
- Market data as_of: **{quant.get('as_of','2026-10-02')}**
- Quant sources: yfinance (NVDA/SPY daily prices + info fundamentals)
- AI model: **gemini-3.5-flash-lite** (25 Google News RSS headlines -> AI extraction and classification; free-tier grounding unavailable, using RSS + AI)

{quant_table}
Methodology: yfinance daily closes with auto_adjust=True; 1Y return independently recomputed from raw CSV using Decimal and verified.
Market data sample: 252 trading days each for NVDA/SPY.

{section('TAILWINDS', ai['tailwinds'])}
{section('HEADWINDS', ai['headwinds'])}
{section('CATALYSTS', ai['catalysts'])}
{section('RISKS', ai['risks'])}
## SOURCES

""" + "\n".join(f"- {u}" for u in all_sources) + """

## Demo notes and limitations

- Single-asset, one-off local demo; AI items require human spot checks; RSS coverage is not guaranteed.
- Free-tier Gemini grounding (google_search tool) returned 429; the demo uses Google News RSS + plain-text AI extraction.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
"""

with open("NVDA-intelligence-20261003.md", "w", encoding="utf-8") as f:
    f.write(report)
print("report regenerated,", len(report), "chars")

from data_utils import ROOT, number

REPORT = ROOT / 'NVDA-intelligence-20261003.md'

def load(name):
    with (ROOT / name).open(encoding='utf-8') as stream:
        return json.load(stream)

def fmt(value, percent=False):
    value = number(value)
    return 'N/A' if value is None else f'{value * (100 if percent else 1):,.2f}'

def amount(data):
    if data is None:
        return 'N/A'
    return f'{fmt(data.get("value"))} {data.get("unit", "N/A")}; period {data.get("period", "N/A")}; fiscal year/reporting period {data.get("fiscal_year", "N/A")}/{data.get("fiscal_period", "N/A")}'

def append_free_source_sections():
    peers, earnings, macro, edgar = [load(name + '.json') for name in ('comparables', 'earnings', 'fred', 'edgar')]
    quant, info = load('quant.json'), load('info.json')
    q = quant['metrics']
    growth, ret = number(q.get('Revenue growth (%)')), number(q.get('Return 1Y (%)'))
    nvda = {'ticker': 'NVDA', 'pe': q.get('P/E (trailing)'), 'pb': q.get('P/B'), 'ev_ebitda': q.get('EV/EBITDA'), 'revenue_growth': growth / 100 if growth is not None else None, 'mktcap': info.get('marketCap'), 'ret_1y': ret / 100 if ret is not None else None}
    out = ['## PEER COMPARABLES', '', '| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (USD) | 1Y return (%) |', '|---|---:|---:|---:|---:|---:|---:|']
    for row in [nvda] + peers['peers']:
        cells = [row['ticker'], fmt(row['pe']), fmt(row['pb']), fmt(row['ev_ebitda']), fmt(row['revenue_growth'], True), fmt(row['mktcap']), fmt(row['ret_1y'], True)]
        if row['ticker'] == 'NVDA':
            cells = [f'**{cell}**' for cell in cells]
        out.append('| ' + ' | '.join(cells) + ' |')
    out += ['', f'Peers fetched as_of: {peers["as_of"]}; NVDA reuses existing data (market data as_of: {quant.get("as_of")}); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.', '', '## EARNINGS CALENDAR', '', f'- Last reported earnings: {earnings["last_earnings"] or "N/A"}', f'- Next expected earnings: {earnings["next_earnings"] or "N/A"} (yfinance; expected dates may change)', '', '## MACRO (FRED)', '']
    if not macro['available']:
        out.append('No FRED API key configured; skipped')
    else:
        out += [f'Fetched as_of: {macro["as_of"]}', '', '| Metric | series_id | Latest value | Observation date |', '|---|---|---:|---|']
        out += [f'| {row["name"]} | {row["series_id"]} | {fmt(row["value"])} | {row["date"] or "N/A"} |' for row in macro['indicators']]
    filing = edgar['latest_filing'] or {}
    out += ['', '## LATEST FILING (EDGAR)', '', f'- Form: {filing.get("form", "N/A")}', f'- Filing date: {filing.get("filing_date", "N/A")}', f'- Revenue (latest available single quarter): {amount(edgar["revenue"])}', f'- Net income (latest available single quarter): {amount(edgar["net_income"])}', f'- SEC link: {filing.get("url", "N/A")}', '', 'SEC requests use the demo placeholder contact email contact@example.com. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.', '', 'API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).', '']
    original = REPORT.read_text(encoding='utf-8')
    marker = '## SOURCES\n'
    assert original.count(marker) == 1
    REPORT.write_text(original.replace(marker, '\n'.join(out) + '\n' + marker), encoding='utf-8')
    print(f'report: {REPORT}; {len(REPORT.read_text(encoding="utf-8").splitlines())} lines')


append_free_source_sections()
