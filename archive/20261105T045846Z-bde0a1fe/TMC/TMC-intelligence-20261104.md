# TMC Intelligence Report

- ticker: **TMC**
- Report as_of: **2026-11-04**
- Market data as_of: **2026-11-04**
- Quant sources: https://finance.yahoo.com/quote/TMC/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TMC/key-statistics/
- AI analysis snapshot as_of: **2026-11-04**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-05T04:59:13.226395+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 2, 'rule': 0, 'ai': 1, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261103T051441Z-8b1c85d8/TMC** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 2 unique headlines; 2 named publishers; 0 exact duplicates; 2 HTTPS source links; largest publisher share 50.0%; oldest publication 2026-11-01

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 2.3100 |
| Return 1D (%) | 0.0000 |
| Return 1W (%) | -17.5000 |
| Return 1M (%) | -39.0501 |
| Return YTD (%) | -62.5608 |
| Return 1Y (%) | -61.4357 |
| Annualized volatility (%) | 91.8753 |
| Beta vs SPY | 3.5129 |
| Max drawdown (%) | -75.5297 |
| Sharpe (rf=0) | -0.5878 |
| Downside deviation (rf=0, %) | 61.9570 |
| Sortino (rf=0) | -0.8716 |
| Historical VaR 95% (1D, %) | 8.7111 |
| Historical ES 95% (1D, %) | 11.7053 |
| Correlation vs SPY | 0.4909 |
| Tracking error vs SPY (%) | 86.3005 |
| P/E (trailing) | N/A |
| P/B | -36.67 |
| EV/EBITDA | -4.48 |
| Revenue growth (%) | N/A |
| Forward P/E (estimate) | N/A |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 0.00 |
| Return on equity (%) | -1123.19 |
| Free cash flow yield (%) | 2.04 |
| MA50 | 3.5391 |
| Close vs MA50 (%) | -34.7292 |
| MA200 | 4.8220 |
| Close vs MA200 (%) | -52.0948 |
| RSI (14, Wilder) | 30.1403 |
| MACD (12,26) | -0.3155 |
| MACD signal (9) | -0.3272 |
| MACD histogram | 0.0117 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TMC': 275, 'SPY': 275}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 2.3100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.0000 -> Unchanged adjusted price over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -17.5000 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -39.0501 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -62.5608 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -61.4357 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 91.8753 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 61.9570 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.8716 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 8.7111 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 11.7053 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4909 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 86.3005 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.5129 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -75.5297 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.5878 -> Negative risk-adjusted return.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: -1123.1911 -> Adjusted price fell over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.0396 -> No interpretation rule is available for this metric.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 30.1403 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.0117 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -34.7292 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -52.0948 -> Clearly below the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

No items in this run

## RISKS

### The Metals Company: Offshore Engineering Advances as Losses Widen and Permitting Takes Longer
- Summary: Losses widen and permitting delays threaten offshore engineering progress, signaling operational challenges for TMC.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxQTGd3UVJFeHp6S1RCbjNfcHRuQ2h1eExnY3pIU213SnExbVNzTlA5R1h4WFg3N1c2WGtPbXdUTzM5c25kcndBMFRJM1hYUTZfeU1rRU1rbngtU0VUMHR4dlZrM3RsM3l5VHFadVRoSFlBMWZtVk1tbTZ5VWNjVVZhMzRjNXE0S0hURzFIZG1IaXY1d1VxU2JiTy1FdWdVN2Vta0RIZ0Z3dEJBSEVGVWZ4dXRVZ1doTUNXQW5PelVjbFBabTNJWUFfZ2NtWQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TMC** | **N/A** | **-36.67** | **-4.48** | **N/A** | **1,019,022,976.00 USD** | **-61.44** |
| MP | N/A | 3.27 | 155.82 | 119.70 | 6,395,628,032.00 USD | -34.59 |
| LAC | N/A | 0.50 | -24.42 | N/A | 707,933,760.00 USD | -57.79 |
| VALE | 67.24 | 1.26 | 1.96 | -3.90 | 48,643,366,912.00 USD | 3.67 |

Peers fetched as_of: 2026-11-04; TMC reuses existing data (market data as_of: 2026-11-04); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-13
- Next expected earnings: 2026-11-12 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-04

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMiywFBVV95cUxQTGd3UVJFeHp6S1RCbjNfcHRuQ2h1eExnY3pIU213SnExbVNzTlA5R1h4WFg3N1c2WGtPbXdUTzM5c25kcndBMFRJM1hYUTZfeU1rRU1rbngtU0VUMHR4dlZrM3RsM3l5VHFadVRoSFlBMWZtVk1tbTZ5VWNjVVZhMzRjNXE0S0hURzFIZG1IaXY1d1VxU2JiTy1FdWdVN2Vta0RIZ0Z3dEJBSEVGVWZ4dXRVZ1doTUNXQW5PelVjbFBabTNJWUFfZ2NtWQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
