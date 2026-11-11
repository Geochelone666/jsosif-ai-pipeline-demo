# TMC Intelligence Report

- ticker: **TMC**
- Report as_of: **2026-11-10**
- Market data as_of: **2026-11-10**
- Quant sources: https://finance.yahoo.com/quote/TMC/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TMC/key-statistics/
- AI analysis snapshot as_of: **2026-11-10**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-11T04:50:00.289043+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 8, 'rule': 0, 'ai': 4, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261110T055129Z-abd33250/TMC** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'directional_claim_without_event_type': 1}
- RSS source audit (metadata only, not article fact-checking): 8 unique headlines; 8 named publishers; 0 exact duplicates; 8 HTTPS source links; largest publisher share 12.5%; oldest publication 2026-11-05

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 2.4200 |
| Return 1D (%) | -7.6336 |
| Return 1W (%) | 4.7619 |
| Return 1M (%) | -27.8689 |
| Return YTD (%) | -60.7780 |
| Return 1Y (%) | -59.0525 |
| Annualized volatility (%) | 94.1303 |
| Beta vs SPY | 3.4943 |
| Max drawdown (%) | -78.0720 |
| Sharpe (rf=0) | -0.4887 |
| Downside deviation (rf=0, %) | 62.8009 |
| Sortino (rf=0) | -0.7325 |
| Historical VaR 95% (1D, %) | 8.8909 |
| Historical ES 95% (1D, %) | 11.8344 |
| Correlation vs SPY | 0.5075 |
| Tracking error vs SPY (%) | 87.9848 |
| P/E (trailing) | N/A |
| P/B | -38.41 |
| EV/EBITDA | -4.71 |
| Revenue growth (%) | N/A |
| Forward P/E (estimate) | N/A |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 0.00 |
| Return on equity (%) | -1123.19 |
| Free cash flow yield (%) | 1.95 |
| MA50 | 3.3331 |
| Close vs MA50 (%) | -27.3949 |
| MA200 | 4.7004 |
| Close vs MA200 (%) | -48.5153 |
| RSI (14, Wilder) | 41.1113 |
| MACD (12,26) | -0.2718 |
| MACD signal (9) | -0.3101 |
| MACD histogram | 0.0383 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TMC': 279, 'SPY': 279}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 2.4200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -7.6336 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 4.7619 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -27.8689 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -60.7780 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -59.0525 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 94.1303 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 62.8009 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.7325 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 8.8909 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 11.8344 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5075 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 87.9848 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.4943 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -78.0720 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.4887 -> Negative risk-adjusted return.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: -1123.1911 -> Adjusted price fell over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.9469 -> No interpretation rule is available for this metric.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 41.1113 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.0383 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -27.3949 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -48.5153 -> Clearly below the moving-average trend level.

## TAILWINDS

### TMC Receives NOAA Letter on Seabed Permit Application Certification
- Summary: TMC received a NOAA letter confirming certification of its seabed permit application, supporting its expansion plans.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxNWnBteDlONHNON0RqVmhlVnduVjBrTlJ2Mm1uYV9jT2FrTTJ5VWFEbjg0TWsyVW9hV2ZGMjRiN1A3dnhkcnJOVVNkeVVma1hwa2tOXzFMTGg3M05CVFhKUjFpZTlWOVF5LXhNNlIyQUl3NHhsbHc2U2ZDby1wWUxKMmdWZW9MR1dFMVVTQ0VtRjlSbl9DS3R1dWJmWkZ2VG40LUJRcTMzUzAyVk1OQmNDV0hKZTVJWmM1dFRZ?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### TMC: TMC the metals company Inc. filed SEC Form 8-K: Regulation FD Disclosure, Financial Statements and Exhibits
- Summary: SEC filing discloses financial statements and exhibits.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPeHdGQldEN3F1Z2ZEWlBoQkFGWEJBUkNNUmwyNFJRWmRZbjJ1UHhzekp5UTNrX3NkSVZJQzRzdWROYUllODlJa1NQQ0JIaDkwYVd0dmJEZmVOd0lRbU1NNXdKYzNzS21KMnhrVEhVclNFX3lMc0RDZzUxNG9DZ1VoVUFoVUJpSC1CODNSdnRZRTRnQUtNN3k4X1JQYW1iUFp5?oc=5>

### A third-quarter update from The Metals Company is scheduled for Nov. 12
- Summary: Scheduled third‑quarter update to be announced on Nov. 12.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxQMl9BODdEbGFLVnNVWExPT09EWEdEakI1RFowTXFOQ3plUHFBSTl1dUZ1UmJMdDVxTTdBbm9DcWo5VmUxeFcwOGxxMjlBQk1EajFsVE5OWnI0M1A1MWpMZ3h6NUM2QUpSUk9WdnlRazJ3Yk90R0w5NDd3eGkyNDVXcGdHeTRCcFZvc3JSTnAwTnNueW9Ga3hFMHY0TXBka0VMLVljbnhnNGc5Ty0za28xLWxNenpmeFNwNHc?oc=5>

## RISKS

### NOAA to decide on TMC the metals Co Inc. permit application by mid-December
- Summary: NOAA will decide on TMC's permit application by mid‑December, potentially delaying operations.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxQa0FsV1FSZGxfSVVoT3RlSFQyOEd3X25TQjVsZU5qbDlIRmxpYUhHbjdfZjlBNkh6WHRsSDI4bDQtS3NZbkpoX2xNTjM4LTQ2aDduVncxWjd1TzVnRWhPRlJJczlsNXJWWExHWnFINGUzTW5hWW45NjVDTWRCeXVPS3JjNl9VQnhTQ0RaLTNfY2dhdzM0a1VENWh5Z3JnQVZNQUF6WW5FaTlJRkZKbVFrNXlXMWpsLXRwbm1pRzVrZlNobzVUb01DRmQ4aUszcm8?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TMC** | **N/A** | **-38.41** | **-4.71** | **N/A** | **1,067,547,904.00 USD** | **-59.05** |
| MP | N/A | 3.33 | 105.24 | 190.90 | 6,499,650,048.00 USD | -43.19 |
| LAC | N/A | 0.48 | -24.09 | N/A | 686,151,168.00 USD | -62.94 |
| VALE | 72.38 | 1.27 | 1.97 | -3.90 | 49,281,744,896.00 USD | 1.96 |

Peers fetched as_of: 2026-11-10; TMC reuses existing data (market data as_of: 2026-11-10); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-13
- Next expected earnings: 2026-11-12 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-10

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMiuwFBVV95cUxNWnBteDlONHNON0RqVmhlVnduVjBrTlJ2Mm1uYV9jT2FrTTJ5VWFEbjg0TWsyVW9hV2ZGMjRiN1A3dnhkcnJOVVNkeVVma1hwa2tOXzFMTGg3M05CVFhKUjFpZTlWOVF5LXhNNlIyQUl3NHhsbHc2U2ZDby1wWUxKMmdWZW9MR1dFMVVTQ0VtRjlSbl9DS3R1dWJmWkZ2VG40LUJRcTMzUzAyVk1OQmNDV0hKZTVJWmM1dFRZ?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPeHdGQldEN3F1Z2ZEWlBoQkFGWEJBUkNNUmwyNFJRWmRZbjJ1UHhzekp5UTNrX3NkSVZJQzRzdWROYUllODlJa1NQQ0JIaDkwYVd0dmJEZmVOd0lRbU1NNXdKYzNzS21KMnhrVEhVclNFX3lMc0RDZzUxNG9DZ1VoVUFoVUJpSC1CODNSdnRZRTRnQUtNN3k4X1JQYW1iUFp5?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxQMl9BODdEbGFLVnNVWExPT09EWEdEakI1RFowTXFOQ3plUHFBSTl1dUZ1UmJMdDVxTTdBbm9DcWo5VmUxeFcwOGxxMjlBQk1EajFsVE5OWnI0M1A1MWpMZ3h6NUM2QUpSUk9WdnlRazJ3Yk90R0w5NDd3eGkyNDVXcGdHeTRCcFZvc3JSTnAwTnNueW9Ga3hFMHY0TXBka0VMLVljbnhnNGc5Ty0za28xLWxNenpmeFNwNHc?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxQa0FsV1FSZGxfSVVoT3RlSFQyOEd3X25TQjVsZU5qbDlIRmxpYUhHbjdfZjlBNkh6WHRsSDI4bDQtS3NZbkpoX2xNTjM4LTQ2aDduVncxWjd1TzVnRWhPRlJJczlsNXJWWExHWnFINGUzTW5hWW45NjVDTWRCeXVPS3JjNl9VQnhTQ0RaLTNfY2dhdzM0a1VENWh5Z3JnQVZNQUF6WW5FaTlJRkZKbVFrNXlXMWpsLXRwbm1pRzVrZlNobzVUb01DRmQ4aUszcm8?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
