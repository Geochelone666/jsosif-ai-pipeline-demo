# TMC Intelligence Report

- ticker: **TMC**
- Report as_of: **2026-11-09**
- Market data as_of: **2026-11-09**
- Quant sources: https://finance.yahoo.com/quote/TMC/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TMC/key-statistics/
- AI analysis snapshot as_of: **2026-11-09**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-10T05:52:02.395115+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 6, 'rule': 0, 'ai': 5, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'directional_claim_without_event_type': 1, 'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 6 unique headlines; 6 named publishers; 0 exact duplicates; 6 HTTPS source links; largest publisher share 16.67%; oldest publication 2026-11-02

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 2.6200 |
| Return 1D (%) | 15.4185 |
| Return 1W (%) | 12.4464 |
| Return 1M (%) | -21.9076 |
| Return YTD (%) | -57.5365 |
| Return 1Y (%) | -54.2757 |
| Annualized volatility (%) | 94.0196 |
| Beta vs SPY | 3.4808 |
| Max drawdown (%) | -78.0720 |
| Sharpe (rf=0) | -0.4094 |
| Downside deviation (rf=0, %) | 62.4579 |
| Sortino (rf=0) | -0.6163 |
| Historical VaR 95% (1D, %) | 8.9088 |
| Historical ES 95% (1D, %) | 11.8344 |
| Correlation vs SPY | 0.5069 |
| Tracking error vs SPY (%) | 87.8755 |
| P/E (trailing) | N/A |
| P/B | -41.59 |
| EV/EBITDA | -5.14 |
| Revenue growth (%) | N/A |
| Forward P/E (estimate) | N/A |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 0.00 |
| Return on equity (%) | -1123.19 |
| Free cash flow yield (%) | 1.80 |
| MA50 | 3.3801 |
| Close vs MA50 (%) | -22.4875 |
| MA200 | 4.7272 |
| Close vs MA200 (%) | -44.5758 |
| RSI (14, Wilder) | 45.4611 |
| MACD (12,26) | -0.2881 |
| MACD signal (9) | -0.3196 |
| MACD histogram | 0.0315 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TMC': 278, 'SPY': 278}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 2.6200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 15.4185 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 12.4464 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -21.9076 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -57.5365 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -54.2757 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 94.0196 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 62.4579 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.6163 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 8.9088 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 11.8344 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5069 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 87.8755 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.4808 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -78.0720 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.4094 -> Negative risk-adjusted return.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: -1123.1911 -> Adjusted price fell over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.7983 -> No interpretation rule is available for this metric.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 45.4611 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.0315 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -22.4875 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -44.5758 -> Clearly below the moving-average trend level.

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

### Form 8K TMC the metals Co Inc. For: 9 November By Investing.com
- Summary: SEC Form 8-K filed for 9 November.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxOVmRuV3doaDVMblBmZXd5MzFxN2VYNUVzMzdEVUs5R2xEbXJtZUtvRnh2cVRmWnhlbFg1RUZ3c2w5QndNRmRCZXgxR05vRHRlRkUwUDhnTVR6b1RrUE1jMGlJWGEzSW1BTnFMMFg4WWhncGZqOW81aVZqNW9IRkV1SktzbGpJSEh6SzYzNFBCRDRsUzhnRlJUbV94dGRWOU1FVTh4cHNic28?oc=5>

### NOAA to decide on TMC the metals Co Inc. permit application by mid-December By Investing.com
- Summary: NOAA pending permit decision.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxPV0drMFJqcU1OQ1BZTHJaN0hDcXZVQTU2Mm9VejJQYkh6WGl1TGdVdWNhMXZJT2c1dV8xbnYtYktTRmtqd19maXRwOXJaMHYxQ3lSQUtjQ3hPb2g5NFRnM2I3ZkdTOHk1LWJITmpOLWVwdVZGeVIzQS13QXJFUnpCVXdWbkFMU2I3dVBndFphWW5zVTB4ODBGZS04dFNoVWlNWEVjM1FBaDU1YTk0bmNncV9hYkE1MmRiakVuQmxrZnYwaVJzLTJpVjAwb2ZjeUk?oc=5>

### TMC stock hits 52-week low at 2.33 USD
- Summary: Stock price falls to 52‑week low.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNSlo3QWZYMzVTa25OT2kweXVSYzdYVjhUbmoxU3dfNFVUbktVV2lIOHA3TnhSZ0wycWlPOFhKaVZxOTFZMXBwaHFzLUVubnV6WlBveHZrZlJQSzFncElXci1rcktlQmNiNG01NUZZV2ZTMUEwM1R2NlFSUDk5TkhlTTRyR3JwaE9JUU5oMTZ2QU9YTDhRWVpjcQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TMC** | **N/A** | **-41.59** | **-5.14** | **N/A** | **1,155,774,976.00 USD** | **-54.28** |
| MP | N/A | 3.45 | 108.93 | 190.90 | 6,729,615,872.00 USD | -35.58 |
| LAC | N/A | 0.52 | -24.82 | N/A | 733,346,752.00 USD | -58.61 |
| VALE | 74.81 | 1.31 | 2.00 | -3.90 | 50,941,480,960.00 USD | 6.69 |

Peers fetched as_of: 2026-11-09; TMC reuses existing data (market data as_of: 2026-11-09); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-13
- Next expected earnings: 2026-11-12 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-09

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMiuwFBVV95cUxNWnBteDlONHNON0RqVmhlVnduVjBrTlJ2Mm1uYV9jT2FrTTJ5VWFEbjg0TWsyVW9hV2ZGMjRiN1A3dnhkcnJOVVNkeVVma1hwa2tOXzFMTGg3M05CVFhKUjFpZTlWOVF5LXhNNlIyQUl3NHhsbHc2U2ZDby1wWUxKMmdWZW9MR1dFMVVTQ0VtRjlSbl9DS3R1dWJmWkZ2VG40LUJRcTMzUzAyVk1OQmNDV0hKZTVJWmM1dFRZ?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPeHdGQldEN3F1Z2ZEWlBoQkFGWEJBUkNNUmwyNFJRWmRZbjJ1UHhzekp5UTNrX3NkSVZJQzRzdWROYUllODlJa1NQQ0JIaDkwYVd0dmJEZmVOd0lRbU1NNXdKYzNzS21KMnhrVEhVclNFX3lMc0RDZzUxNG9DZ1VoVUFoVUJpSC1CODNSdnRZRTRnQUtNN3k4X1JQYW1iUFp5?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxOVmRuV3doaDVMblBmZXd5MzFxN2VYNUVzMzdEVUs5R2xEbXJtZUtvRnh2cVRmWnhlbFg1RUZ3c2w5QndNRmRCZXgxR05vRHRlRkUwUDhnTVR6b1RrUE1jMGlJWGEzSW1BTnFMMFg4WWhncGZqOW81aVZqNW9IRkV1SktzbGpJSEh6SzYzNFBCRDRsUzhnRlJUbV94dGRWOU1FVTh4cHNic28?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxPV0drMFJqcU1OQ1BZTHJaN0hDcXZVQTU2Mm9VejJQYkh6WGl1TGdVdWNhMXZJT2c1dV8xbnYtYktTRmtqd19maXRwOXJaMHYxQ3lSQUtjQ3hPb2g5NFRnM2I3ZkdTOHk1LWJITmpOLWVwdVZGeVIzQS13QXJFUnpCVXdWbkFMU2I3dVBndFphWW5zVTB4ODBGZS04dFNoVWlNWEVjM1FBaDU1YTk0bmNncV9hYkE1MmRiakVuQmxrZnYwaVJzLTJpVjAwb2ZjeUk?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNSlo3QWZYMzVTa25OT2kweXVSYzdYVjhUbmoxU3dfNFVUbktVV2lIOHA3TnhSZ0wycWlPOFhKaVZxOTFZMXBwaHFzLUVubnV6WlBveHZrZlJQSzFncElXci1rcktlQmNiNG01NUZZV2ZTMUEwM1R2NlFSUDk5TkhlTTRyR3JwaE9JUU5oMTZ2QU9YTDhRWVpjcQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
