# TD.TO Intelligence Report

- ticker: **TD.TO**
- Report as_of: **2026-11-27**
- Market data as_of: **2026-11-27**
- Quant sources: https://finance.yahoo.com/quote/TD.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TD.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-28T06:32:40.334926+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 4, 'rule': 1, 'ai': 0, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261127T063646Z-c0c26981/TD.TO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 4 unique headlines; 3 named publishers; 0 exact duplicates; 4 HTTPS source links; largest publisher share 50.0%; oldest publication 2026-11-24

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 166.2300 |
| Return 1D (%) | 0.4107 |
| Return 1W (%) | 2.5794 |
| Return 1M (%) | -5.8560 |
| Return YTD (%) | 32.3781 |
| Return 1Y (%) | 46.2876 |
| Annualized volatility (%) | 18.2508 |
| Beta vs SPY | 0.7034 |
| Max drawdown (%) | -9.4339 |
| Sharpe (rf=0) | 2.1854 |
| Downside deviation (rf=0, %) | 12.6980 |
| Sortino (rf=0) | 3.1411 |
| Historical VaR 95% (1D, %) | 1.9575 |
| Historical ES 95% (1D, %) | 2.7608 |
| Correlation vs SPY | 0.5771 |
| Tracking error vs SPY (%) | 15.6691 |
| P/E (trailing) | 17.87 |
| P/B | 2.20 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 11.50 |
| Forward P/E (estimate) | 14.85 |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 35.14 |
| Return on equity (%) | 12.83 |
| Free cash flow yield (%) | N/A |
| MA50 | 170.3810 |
| Close vs MA50 (%) | -2.4363 |
| MA200 | 156.0848 |
| Close vs MA200 (%) | 6.4998 |
| RSI (14, Wilder) | 42.3415 |
| MACD (12,26) | -1.9678 |
| MACD signal (9) | -1.0268 |
| MACD histogram | -0.9410 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TD.TO': 291, 'SPY': 291}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 166.2300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.4107 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.5794 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -5.8560 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 32.3781 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 46.2876 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 18.2508 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 12.6980 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 3.1411 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.9575 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.7608 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5771 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 15.6691 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.7034 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -9.4339 -> Shallow peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 2.1854 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 14.8464 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 35.1440 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 12.8280 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 17.8742 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 42.3415 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.9410 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -2.4363 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 6.4998 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### TD Bank stock: analysts reset targets ahead of Q4 results
- Summary: TD Bank stock: analysts reset targets ahead of Q4 results
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxNeEtXVjFNLUM5Yjh6a2kwNzNiSTNkNDhvc1hWQ09nNEU2Tko0Vm54T0FMSzNVREFkU3Ziam1lbjRCV1NpVDhCMmpkQlNZOWZ3QW5OaFZuTVJuYTY4VjhrY3puXzY4VWxjOVBaTURjNUREdTRnZUtMZERDV0NLYUdrQ1A5bm5FQm0zT3VZYnFpS01faF9aM3BrSGtROTk1OWdpZlhxY2xVUkthem5wTHFZcXdiU3VFcHh5Vktz?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TD.TO** | **17.87** | **2.20** | **N/A** | **11.50** | **271,456,354,304.00 CAD** | **46.29** |
| RY.TO | 16.89 | 2.77 | N/A | 8.90 | 370,957,975,552.00 CAD | 27.69 |
| BMO.TO | 18.25 | 1.85 | N/A | 12.00 | 156,882,305,024.00 CAD | 32.26 |
| BNS.TO | 15.80 | 1.65 | N/A | 11.70 | 146,966,511,616.00 CAD | 29.56 |

Peers fetched as_of: 2026-11-27; TD.TO reuses existing data (market data as_of: 2026-11-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-27
- Next expected earnings: 2026-12-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-27

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: N/A
- Filing date: N/A
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: N/A

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiuwFBVV95cUxNeEtXVjFNLUM5Yjh6a2kwNzNiSTNkNDhvc1hWQ09nNEU2Tko0Vm54T0FMSzNVREFkU3Ziam1lbjRCV1NpVDhCMmpkQlNZOWZ3QW5OaFZuTVJuYTY4VjhrY3puXzY4VWxjOVBaTURjNUREdTRnZUtMZERDV0NLYUdrQ1A5bm5FQm0zT3VZYnFpS01faF9aM3BrSGtROTk1OWdpZlhxY2xVUkthem5wTHFZcXdiU3VFcHh5Vktz?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
