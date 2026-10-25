#!/usr/bin/env python3
"""Regenerate the selected ticker intelligence report with quant + AI results."""
import json
import os
import sys
from datetime import date
from metric_interpretation import build_interpretation_section
from ai_extract import analysis_status
from data_utils import DATA, REPORTS, ticker_arg, ticker_file, as_of_date
from assumptions import VERSION, AssumptionViolation, check_all, checked_mapping, required_paths
TICKER = ticker_arg()
AS_OF = as_of_date().isoformat()
STAMP = AS_OF.replace('-', '')
# Save a JSON sidecar even when preflight fails, before touching the report.
violation = None
try:
    checks = check_all({'ticker': TICKER, 'as_of': AS_OF,
                        'required_paths': required_paths(DATA, TICKER)})
except AssumptionViolation as exc:
    checks, violation = exc.results, exc
metadata = {'ticker': TICKER, 'as_of': AS_OF, 'assumptions_version': VERSION,
            'assumptions_checked': checked_mapping(checks)}
(REPORTS / f'{TICKER}-intelligence-{STAMP}.json').write_text(
    json.dumps(metadata, indent=2) + '\n', encoding='utf-8')
if violation is not None:
    print(str(violation), file=sys.stderr)
    raise SystemExit(2)

def read_snapshot(name):
    return json.loads((DATA / ticker_file(TICKER, name)).read_text(encoding="utf-8"))

quant = read_snapshot("quant.json")
q = quant["metrics"]
ai = read_snapshot("ai-intel.json")
rss = read_snapshot("rss-items.json")

# map rss links by headline for sources
link_by_headline = {}
for it in rss:
    link_by_headline[it["headline"]] = it["link"]

def section(name, items):
    out = [f"## {name}\n"]
    if not items:
        out.append(f"{('N/A: ' + ai['error']) if ai.get('error') else 'No items in this run'}\n")
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
| Downside deviation (rf=0, %) | {fmt(q.get('Downside deviation (rf=0, %)'))} |
| Sortino (rf=0) | {fmt(q.get('Sortino (rf=0)'))} |
| Historical VaR 95% (1D, %) | {fmt(q.get('Historical VaR 95% (1D, %)'))} |
| Historical ES 95% (1D, %) | {fmt(q.get('Historical ES 95% (1D, %)'))} |
| Correlation vs SPY | {fmt(q.get('Correlation vs SPY'))} |
| Tracking error vs SPY (%) | {fmt(q.get('Tracking error vs SPY (%)'))} |
| P/E (trailing) | {fmt(q.get('P/E (trailing)'), 2)} |
| P/B | {fmt(q.get('P/B'), 2)} |
| EV/EBITDA | {fmt(q.get('EV/EBITDA'), 2)} |
| Revenue growth (%) | {fmt(q.get('Revenue growth (%)'), 2)} |
| Forward P/E (estimate) | {fmt(q.get('Forward P/E (estimate)'), 2)} |
| Gross margin (%) | {fmt(q.get('Gross margin (%)'), 2)} |
| Operating margin (%) | {fmt(q.get('Operating margin (%)'), 2)} |
| Return on equity (%) | {fmt(q.get('Return on equity (%)'), 2)} |
| Free cash flow yield (%) | {fmt(q.get('Free cash flow yield (%)'), 2)} |
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

ai_status = analysis_status(ai)
report = f"""# {TICKER} Intelligence Report

- ticker: **{TICKER}**
- Report as_of: **{AS_OF}**
- Market data as_of: **{quant.get('as_of') or 'N/A'}**
- Quant sources: {', '.join(quant.get('sources', [])) or 'N/A'}
- AI analysis snapshot as_of: **{ai.get('as_of', 'N/A')}**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **{quant.get('fetched_at', 'N/A')}**
- AI status: **{ai_status}**
- AI model (configured): **{ai.get('model', 'legacy snapshot / rules')}** (RSS headlines; rule and AI item counts: {ai.get('extraction_stats', {})})
- AI model(s) actually used: **{', '.join(ai.get('models_used', [])) or 'N/A (no successful AI classification call)'}**
- Verified recent classification reuse: **{ai.get('ai_reuse', {}).get('reused_headlines', 0)}** exact headline/source/date matches; prior report **{ai.get('ai_reuse', {}).get('from_report', 'N/A')}** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **{ai.get('decision_audit', {}).get('flag_count', 'not audited')}**; {ai.get('decision_audit', {}).get('by_reason', {})}
- RSS source audit (metadata only, not article fact-checking): {ai.get('rss_audit', {}).get('unique_headlines', 'N/A')} unique headlines; {ai.get('rss_audit', {}).get('unique_publishers', 'N/A')} named publishers; {ai.get('rss_audit', {}).get('duplicates_excluded', 'N/A')} exact duplicates; {ai.get('rss_audit', {}).get('https_link_headlines', 'N/A')} HTTPS source links; largest publisher share {ai.get('rss_audit', {}).get('largest_publisher_share_pct', 'N/A')}%; oldest publication {ai.get('rss_audit', {}).get('oldest_publication_date', 'N/A')}

{quant_table}
Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {quant.get('history_count', {})}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

{build_interpretation_section(q)}{section('TAILWINDS', ai['tailwinds'])}
{section('HEADWINDS', ai['headwinds'])}
{section('CATALYSTS', ai['catalysts'])}
{section('RISKS', ai['risks'])}
## SOURCES

""" + "\n".join(f"- {u}" for u in all_sources) + """

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
"""

with (REPORTS / f"{TICKER}-intelligence-{STAMP}.md").open("w", encoding="utf-8") as f:
    f.write(report)
print("report regenerated,", len(report), "chars")

from data_utils import DATA, REPORTS, number

REPORT = REPORTS / f'{TICKER}-intelligence-{STAMP}.md'

def load(name):
    with (DATA / (name if name == 'fred.json' else ticker_file(TICKER, name))).open(encoding='utf-8') as stream:
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
    nvda = {'ticker': TICKER, 'pe': q.get('P/E (trailing)'), 'pb': q.get('P/B'), 'ev_ebitda': q.get('EV/EBITDA'), 'revenue_growth': growth / 100 if growth is not None else None, 'mktcap': info.get('marketCap'), 'ret_1y': ret / 100 if ret is not None else None, 'currency': info.get('currency')}
    out = ['## PEER COMPARABLES', '', '| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |', '|---|---:|---:|---:|---:|---:|---:|']
    for row in [nvda] + peers['peers']:
        cells = [row['ticker'], fmt(row['pe']), fmt(row['pb']), fmt(row['ev_ebitda']), fmt(row['revenue_growth'], True), fmt(row['mktcap']) + ' ' + (row.get('currency') or 'unknown currency'), fmt(row['ret_1y'], True)]
        if row['ticker'] == TICKER:
            cells = [f'**{cell}**' for cell in cells]
        out.append('| ' + ' | '.join(cells) + ' |')
    out += ['', f'Peers fetched as_of: {peers["as_of"]}; {TICKER} reuses existing data (market data as_of: {quant.get("as_of")}); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.', '', '## EARNINGS CALENDAR', '', f'- Last reported earnings: {earnings["last_earnings"] or "N/A"}', f'- Next expected earnings: {earnings["next_earnings"] or "N/A"} (yfinance; expected dates may change)', '', '## MACRO (FRED)', '']
    if not macro['available']:
        out.append('N/A: FRED observations unavailable (API key missing, request failed, or no numeric observations); see collection logs')
    else:
        out += [f'Fetched as_of: {macro["as_of"]}', '', '| Metric | series_id | Latest value | Observation date |', '|---|---|---:|---|']
        out += [f'| {row["name"]} | {row["series_id"]} | {fmt(row["value"])} | {row["date"] or "N/A"} |' for row in macro['indicators']]
    filing = edgar['latest_filing'] or {}
    out += ['', '## LATEST FILING (EDGAR)', '', f'- Form: {filing.get("form", "N/A")}', f'- Filing date: {filing.get("filing_date", "N/A")}', f'- Revenue (latest available single quarter): {amount(edgar["revenue"])}', f'- Net income (latest available single quarter): {amount(edgar["net_income"])}', f'- SEC link: {filing.get("url", "N/A")}', '', 'SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.', '', 'API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).', '']
    original = REPORT.read_text(encoding='utf-8')
    marker = '## SOURCES\n'
    assert original.count(marker) == 1
    REPORT.write_text(original.replace(marker, '\n'.join(out) + '\n' + marker), encoding='utf-8')
    print(f'report: {REPORT}; {len(REPORT.read_text(encoding="utf-8").splitlines())} lines')


append_free_source_sections()

from freeze_report import freeze
freeze(REPORT, quant, ai)

