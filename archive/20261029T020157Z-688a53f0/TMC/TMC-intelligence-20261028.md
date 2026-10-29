# TMC Intelligence Report

- ticker: **TMC**
- Report as_of: **2026-10-28**
- Market data as_of: **2026-10-28**
- Quant sources: https://finance.yahoo.com/quote/TMC/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TMC/key-statistics/
- AI analysis snapshot as_of: **2026-10-28**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-29T02:05:30.308765+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 2, 'rule': 1, 'ai': 1, 'unknown': 0})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 2 unique headlines; 2 named publishers; 0 exact duplicates; 2 HTTPS source links; largest publisher share 50.0%; oldest publication 2026-10-25

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 2.8000 |
| Return 1D (%) | 1.8182 |
| Return 1W (%) | 5.6604 |
| Return 1M (%) | -27.4611 |
| Return YTD (%) | -54.6191 |
| Return 1Y (%) | -59.9428 |
| Annualized volatility (%) | 91.6878 |
| Beta vs SPY | 3.4764 |
| Max drawdown (%) | -74.6822 |
| Sharpe (rf=0) | -0.5496 |
| Downside deviation (rf=0, %) | 61.5852 |
| Sortino (rf=0) | -0.8182 |
| Historical VaR 95% (1D, %) | 8.7111 |
| Historical ES 95% (1D, %) | 11.6409 |
| Correlation vs SPY | 0.4816 |
| Tracking error vs SPY (%) | 86.2911 |
| P/E (trailing) | N/A |
| P/B | -44.44 |
| EV/EBITDA | -5.53 |
| Revenue growth (%) | N/A |
| Forward P/E (estimate) | N/A |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 0.00 |
| Return on equity (%) | -1123.19 |
| Free cash flow yield (%) | 1.68 |
| MA50 | 3.7398 |
| Close vs MA50 (%) | -25.1297 |
| MA200 | 4.9449 |
| Close vs MA200 (%) | -43.3763 |
| RSI (14, Wilder) | 40.0303 |
| MACD (12,26) | -0.3413 |
| MACD signal (9) | -0.3618 |
| MACD histogram | 0.0205 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TMC': 270, 'SPY': 270}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 2.8000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.8182 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 5.6604 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -27.4611 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -54.6191 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -59.9428 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 91.6878 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 61.5852 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.8182 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 8.7111 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 11.6409 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4816 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 86.2911 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.4764 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -74.6822 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.5496 -> Negative risk-adjusted return.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: -1123.1911 -> Adjusted price fell over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.6826 -> No interpretation rule is available for this metric.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 40.0303 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.0205 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -25.1297 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -43.3763 -> Clearly below the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### The Metals Company Trades at $2.65. Analysts See It at $10. Here's What Would Need to Go Right for It to Close That Gap.
- Summary: The Metals Company Trades at $2.65. Analysts See It at $10. Here's What Would Need to Go Right for It to Close That Gap.
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPRERZUHVZemxqckRSS3BMMHlSNnk1cEJDX1p5X0xDWk1nSm4wcWRNREE0Mzg2bVFUend2b1pLYjlpVHFudjdhQUdnbmZ3VzZITTdIOWZsRkM3R3NYNHZoSEJfVFQ2Q3M3Tl9qa21wQi1vQ20zMEJtSWJUM0pOY1p2Ni1ITjR4UHcyNVQxM2JuaEZVQkU?oc=5>

### USA Rare Earth Soars 13%, Critical Metals Up 12%, TMC Up 11% as Critical Minerals Stocks Rally
- Summary: TMC shares surged 11% amid a rally in critical minerals stocks, reflecting positive market sentiment.
- Date: 2026-10-28 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxOU2ZrVWRDdHlrdjF4TlN5OW1OSzFvN3lMZ1RoLUtweWJ1R0NHLTB1RjNobG1QUnRJd3VJY2hpQ2hhRmU0cWduRV8teWVxWlhSTUF0dWgzOVNrS0J5YURMOXN0OWUxWmFqTUNKV0o0YV9Ib3ZnZGxZZGxCYW5vM0swMUU0TGdOUHI0YjJEbjdTSm9PZTVwQ3d5MWNDT0NDekxsRkRvN2hRSXdZYzVZSnZ6Y2VqM3AwUGs?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TMC** | **N/A** | **-44.44** | **-5.53** | **N/A** | **1,235,179,392.00 USD** | **-59.94** |
| MP | N/A | 3.74 | 178.37 | 119.70 | 7,312,851,456.00 USD | -36.77 |
| LAC | N/A | 0.55 | -25.66 | N/A | 787,803,200.00 USD | -62.59 |
| VALE | 22.94 | 1.25 | 1.73 | 6.40 | 48,813,600,768.00 USD | 6.90 |

Peers fetched as_of: 2026-10-28; TMC reuses existing data (market data as_of: 2026-10-28); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-13
- Next expected earnings: 2026-11-12 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-28

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-13
- Revenue (latest available single quarter): 410,000.00 USD; period 2024-04-01/2024-06-30; fiscal year/reporting period 2024/Q2
- Net income (latest available single quarter): -60,123,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1798562/000110465926096051/tmc-20260630x10q.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMikwFBVV95cUxPRERZUHVZemxqckRSS3BMMHlSNnk1cEJDX1p5X0xDWk1nSm4wcWRNREE0Mzg2bVFUend2b1pLYjlpVHFudjdhQUdnbmZ3VzZITTdIOWZsRkM3R3NYNHZoSEJfVFQ2Q3M3Tl9qa21wQi1vQ20zMEJtSWJUM0pOY1p2Ni1ITjR4UHcyNVQxM2JuaEZVQkU?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxOU2ZrVWRDdHlrdjF4TlN5OW1OSzFvN3lMZ1RoLUtweWJ1R0NHLTB1RjNobG1QUnRJd3VJY2hpQ2hhRmU0cWduRV8teWVxWlhSTUF0dWgzOVNrS0J5YURMOXN0OWUxWmFqTUNKV0o0YV9Ib3ZnZGxZZGxCYW5vM0swMUU0TGdOUHI0YjJEbjdTSm9PZTVwQ3d5MWNDT0NDekxsRkRvN2hRSXdZYzVZSnZ6Y2VqM3AwUGs?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
