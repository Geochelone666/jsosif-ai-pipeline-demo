# CSU.TO Intelligence Report

- ticker: **CSU.TO**
- Report as_of: **2026-10-27**
- Market data as_of: **2026-10-27**
- Quant sources: https://finance.yahoo.com/quote/CSU.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CSU.TO/key-statistics/
- AI analysis snapshot as_of: **2026-10-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-28T02:21:30.955200+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 2, 'rule': 0, 'ai': 1, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261027T014607Z-b66f6bd5/CSU.TO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 2 unique headlines; 2 named publishers; 0 exact duplicates; 2 HTTPS source links; largest publisher share 50.0%; oldest publication 2026-10-21

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 3303.8201 |
| Return 1D (%) | -1.7147 |
| Return 1W (%) | 1.9698 |
| Return 1M (%) | 14.9963 |
| Return YTD (%) | 0.2325 |
| Return 1Y (%) | -13.8851 |
| Annualized volatility (%) | 45.1194 |
| Beta vs SPY | 0.1153 |
| Max drawdown (%) | -41.2334 |
| Sharpe (rf=0) | -0.1083 |
| Downside deviation (rf=0, %) | 31.0935 |
| Sortino (rf=0) | -0.1571 |
| Historical VaR 95% (1D, %) | 4.5246 |
| Historical ES 95% (1D, %) | 5.7867 |
| Correlation vs SPY | 0.0323 |
| Tracking error vs SPY (%) | 46.8311 |
| P/E (trailing) | 52.73 |
| P/B | 12.07 |
| EV/EBITDA | 31.79 |
| Revenue growth (%) | 17.30 |
| Forward P/E (estimate) | 17.83 |
| Gross margin (%) | 37.27 |
| Operating margin (%) | 15.11 |
| Return on equity (%) | 23.28 |
| Free cash flow yield (%) | N/A |
| MA50 | 3016.3497 |
| Close vs MA50 (%) | 9.5304 |
| MA200 | 2765.7594 |
| Close vs MA200 (%) | 19.4544 |
| RSI (14, Wilder) | 62.7040 |
| MACD (12,26) | 111.5213 |
| MACD signal (9) | 83.5177 |
| MACD histogram | 28.0036 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CSU.TO': 268, 'SPY': 269}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 3303.8201 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.7147 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.9698 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 14.9963 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 0.2325 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -13.8851 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 45.1194 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 31.0935 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.1571 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.5246 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.7867 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0323 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 46.8311 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.1153 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -41.2334 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.1083 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.8271 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 37.2680 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 15.1120 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 23.2810 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 52.7261 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 62.7040 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 28.0036 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 9.5304 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 19.4544 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### I’d Keep Constellation Software Stock Despite its 3% Organic Growth: Here’s Why
- Summary: Shares remain attractive despite modest growth, citing strong fundamentals and future upside.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxOTmdtaVJLbUt5R3pqSy1JMklpNWZmbnB5Tl9XTGxNMEZsN2RabzQtSGN5OHlmR1M3Y0tGTDJnOWMwNTU4Nzc4UkRqNDVfOGdnQkVfbWZOS2hEdm1XeTltUG5BM01waUVEZjhSUmRlX2V3UnpnU1kycDZLNnp3elVFaVlsR0lwcnpfanRmNA?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CSU.TO** | **52.73** | **12.07** | **31.79** | **17.30** | **70,013,001,728.00 CAD** | **-13.89** |
| DSG.TO | 43.41 | 4.79 | 32.27 | 11.80 | 11,067,415,552.00 CAD | -3.30 |
| OTEX.TO | 10.70 | 1.61 | 8.62 | 2.90 | 9,272,128,512.00 CAD | -27.70 |
| TOI.V | 139.00 | 9.22 | 25.66 | 17.50 | 20,149,837,824.00 CAD | -39.07 |

Peers fetched as_of: 2026-10-27; CSU.TO reuses existing data (market data as_of: 2026-10-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-10
- Next expected earnings: 2026-11-06 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-27

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMijAFBVV95cUxOTmdtaVJLbUt5R3pqSy1JMklpNWZmbnB5Tl9XTGxNMEZsN2RabzQtSGN5OHlmR1M3Y0tGTDJnOWMwNTU4Nzc4UkRqNDVfOGdnQkVfbWZOS2hEdm1XeTltUG5BM01waUVEZjhSUmRlX2V3UnpnU1kycDZLNnp3elVFaVlsR0lwcnpfanRmNA?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
