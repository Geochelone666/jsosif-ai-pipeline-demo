# MG.TO Intelligence Report

- ticker: **MG.TO**
- Report as_of: **2026-11-02**
- Market data as_of: **2026-11-02**
- Quant sources: https://finance.yahoo.com/quote/MG.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MG.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-02**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-03T05:16:03.240434+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 5, 'rule': 0, 'ai': 1, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261102T041627Z-c84a7052/MG.TO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 5 unique headlines; 2 named publishers; 0 exact duplicates; 5 HTTPS source links; largest publisher share 60.0%; oldest publication 2026-10-29

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 91.5700 |
| Return 1D (%) | 2.9918 |
| Return 1W (%) | 2.2215 |
| Return 1M (%) | -0.5106 |
| Return YTD (%) | 28.0165 |
| Return 1Y (%) | 42.7669 |
| Annualized volatility (%) | 36.5447 |
| Beta vs SPY | 1.1476 |
| Max drawdown (%) | -22.7904 |
| Sharpe (rf=0) | 1.0369 |
| Downside deviation (rf=0, %) | 20.9945 |
| Sortino (rf=0) | 1.8049 |
| Historical VaR 95% (1D, %) | 2.7500 |
| Historical ES 95% (1D, %) | 3.9845 |
| Correlation vs SPY | 0.4009 |
| Tracking error vs SPY (%) | 33.8204 |
| P/E (trailing) | 21.50 |
| P/B | 1.48 |
| EV/EBITDA | 7.21 |
| Revenue growth (%) | -3.90 |
| Forward P/E (estimate) | 8.30 |
| Gross margin (%) | 14.27 |
| Operating margin (%) | 5.49 |
| Return on equity (%) | N/A |
| Free cash flow yield (%) | N/A |
| MA50 | 91.2488 |
| Close vs MA50 (%) | 0.3520 |
| MA200 | 86.3339 |
| Close vs MA200 (%) | 6.0649 |
| RSI (14, Wilder) | 51.6125 |
| MACD (12,26) | -0.4445 |
| MACD signal (9) | -0.3361 |
| MACD histogram | -0.1084 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MG.TO': 272, 'SPY': 273}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 91.5700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.9918 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.2215 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -0.5106 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 28.0165 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 42.7669 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 36.5447 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 20.9945 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.8049 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.7500 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.9845 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4009 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 33.8204 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.1476 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -22.7904 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.0369 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 8.3031 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 14.2730 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 5.4880 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 21.4953 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 51.6125 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.1084 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 0.3520 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 6.0649 -> Clearly above the moving-average trend level.

## TAILWINDS

### Canada-U.S. Trade Talks Are Back: This TSX Stock Could Benefit If Tariffs Ease
- Summary: Potential tariff easing could improve MG.TO’s export prospects, boosting demand for its automotive parts.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMif0FVX3lxTE04dlE2bUdPbDJtRy11dG9VNEUtMkhWaWQxYjZqUWZwQkU5Yk43ZFExMmtiVXVoNW5RV1hsTjdIc25hM3N3al8tX1hGMjNEYmJINUJtU2VyREtHTDJzOGZvRDhGMnVCcjdOQVZwdmZhRzE1d1VSVlRZZDhPZ1E4SjQ?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

No items in this run

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MG.TO** | **21.50** | **1.48** | **7.21** | **-3.90** | **23,776,768,000.00 CAD** | **42.77** |
| APTV | 43.36 | 1.05 | 4.36 | 2.30 | 9,183,622,144.00 USD | -45.46 |
| BWA | 21.84 | 1.83 | 6.01 | -2.90 | 10,392,127,488.00 USD | 21.91 |
| LEA | 10.32 | 1.18 | 5.10 | 1.60 | 5,893,404,672.00 USD | 19.81 |

Peers fetched as_of: 2026-11-02; MG.TO reuses existing data (market data as_of: 2026-11-02); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-30
- Next expected earnings: 2027-02-12 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-02

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMif0FVX3lxTE04dlE2bUdPbDJtRy11dG9VNEUtMkhWaWQxYjZqUWZwQkU5Yk43ZFExMmtiVXVoNW5RV1hsTjdIc25hM3N3al8tX1hGMjNEYmJINUJtU2VyREtHTDJzOGZvRDhGMnVCcjdOQVZwdmZhRzE1d1VSVlRZZDhPZ1E4SjQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
