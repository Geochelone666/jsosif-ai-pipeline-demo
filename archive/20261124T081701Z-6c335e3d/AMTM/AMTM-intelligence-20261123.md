# AMTM Intelligence Report

- ticker: **AMTM**
- Report as_of: **2026-11-23**
- Market data as_of: **2026-11-23**
- Quant sources: https://finance.yahoo.com/quote/AMTM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMTM/key-statistics/
- AI analysis snapshot as_of: **2026-11-23**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-24T08:29:43.918322+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 7, 'rule': 4, 'ai': 2, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261123T053847Z-45053549/AMTM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 7 unique headlines; 4 named publishers; 0 exact duplicates; 7 HTTPS source links; largest publisher share 42.86%; oldest publication 2026-11-22

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 20.6500 |
| Return 1D (%) | 1.5241 |
| Return 1W (%) | -3.8193 |
| Return 1M (%) | -5.1011 |
| Return YTD (%) | -28.7931 |
| Return 1Y (%) | -14.8805 |
| Annualized volatility (%) | 43.6835 |
| Beta vs SPY | 0.8883 |
| Max drawdown (%) | -51.7186 |
| Sharpe (rf=0) | -0.2592 |
| Downside deviation (rf=0, %) | 30.0328 |
| Sortino (rf=0) | -0.3769 |
| Historical VaR 95% (1D, %) | 3.8360 |
| Historical ES 95% (1D, %) | 5.9321 |
| Correlation vs SPY | 0.3045 |
| Tracking error vs SPY (%) | 41.6426 |
| P/E (trailing) | 24.88 |
| P/B | 1.07 |
| EV/EBITDA | 8.46 |
| Revenue growth (%) | -2.00 |
| Forward P/E (estimate) | 7.00 |
| Gross margin (%) | 10.49 |
| Operating margin (%) | 4.01 |
| Return on equity (%) | 4.29 |
| Free cash flow yield (%) | 9.59 |
| MA50 | 20.3336 |
| Close vs MA50 (%) | 1.5560 |
| MA200 | 23.3662 |
| Close vs MA200 (%) | -11.6245 |
| RSI (14, Wilder) | 45.1199 |
| MACD (12,26) | 0.0917 |
| MACD signal (9) | 0.3683 |
| MACD histogram | -0.2767 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMTM': 288, 'SPY': 288}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 20.6500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.5241 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -3.8193 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -5.1011 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -28.7931 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -14.8805 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 43.6835 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 30.0328 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.3769 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.8360 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.9321 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3045 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 41.6426 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.8883 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -51.7186 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.2592 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 6.9974 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 10.4880 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 4.0130 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 4.2870 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 9.5909 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 24.8795 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 45.1199 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.2767 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 1.5560 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -11.6245 -> Clearly below the moving-average trend level.

## TAILWINDS

### Amentum Holdings (AMTM) Q4 Earnings Top Estimates
- Summary: Amentum Holdings (AMTM) Q4 Earnings Top Estimates
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNYmthQ0g1M0FCOWt5UnpxQUpURFVsWTh2XzVCR1BIazVBVU5qQnBVdFRUMW5nVnlrMHFPTDFFRHlYSzhERE1pcXZiTGN1NFY4dGdYdXVFdzFONzl2VW5MdXlJM1ljaVRLWUJRSnZ0dlNTYldUVXppemJBVzEzMjVkNWU1ZUVUbHNvcWxaeXpWdk9xOExCTF9xenlDMzNpWDQ?oc=5>

## HEADWINDS

### Amentum (AMTM) Reports Q4 Revenue Slightly Below Expectations, E
- Summary: Amentum (AMTM) Reports Q4 Revenue Slightly Below Expectations, E
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxOVkw3X3lzdWFxaGNfRmVRWUppMVJhOEs2aU5KQlJHTzdhcENzMkVpeWpSSUJPQm5JTHgtUU91TEdtMWIwc3FtTG15VWVIdXplTTZPdjFvMXFiRURZUkd4b05Ha1BLbGNsV05xRDZFWnotaDhQaU01R2pTSldUWEJzdFRhRjZCQ2V5cXZadkFGclkyMGdRa19jaFZSdlJGT0c0NDZFRG9sYmZwVGtaZ3g4NHBZb01JaXVJOUtfZGdZTGtwTnBiRzBmcDJJV1hxUQ?oc=5>

## CATALYSTS

### Amentum (AMTM) Q4 Earnings: Taking a Look at Key Metrics Versus Estimates
- Summary: Amentum (AMTM) Q4 Earnings: Taking a Look at Key Metrics Versus Estimates
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNQ0hkUlFVZDk1dHNBNE9fNC0zd0c5Yl9makZZZm1vQUNHVVZocmtNbTMyVVZwX21lVThiVVhHMFFxVlZRTno4aGtYM0tuWEZoblc5UFZRRjA4Y18yZm5iOGRla0tYZnVDZDcweXVJN2hSYVFwemlIU2FITjdPM2RJZGlkRjktUzBNNy1qaUdMd3FLQldjMmp4UWdVVWQ?oc=5>

### Amentum (AMTM) Launches $500 Million Share Buyback Program Amid Mixed Valuation Signals
- Summary: Amentum (AMTM) Launches $500 Million Share Buyback Program Amid Mixed Valuation Signals
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxNV0RMVUozcDlZZ01MODlHNEZqVTZ5bnc3ZEs4ZVZMaXJwRVdKTkJjd2dwMzJzbFN6ZDZVMmRscUYzS0FMUVFLSUhqanJMREIzNmJST05BOHBhSk5ReHFVN0tSbXYwanhfVzBFUEtEbUw3YlYxYXlIV2Q0d2g0cWZWMWVveHR1UWhGQVBWTllxM2pTTmRPTmtKNEtKTkVzU2JIM0d1Z01BWXhXbFhBVGdrNmt6ZFpzMEZwSVAyTDNIUTI?oc=5>

### What to expect from Amentum’s Q3 earnings
- Summary: Analysts discuss anticipated Q3 earnings, revenue, and guidance for Amentum.
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxOUl9zYXkyLTBBUVpHQ3A3TGY1YmNJNjdWRWNZcEpfRGZ6SlNZLU1kcTZLZ0pVQkxGSG9RSXlhR3pMdWZIdW10MVdnUmpQQ2NsbDhWSGYyTm42WEFUNVE3UWhNTHR1LUVQVUdVc0NlQ01wMElwTU9SdnR4dFA2MjUya2l2al9aV25rQzZva1ozcklUVjZ0aThpSzBuSktVOWE3enRCRQ?oc=5>

### Revenue fell 4% at Amentum (AMTM) in fiscal 2026, but net income rose.
- Summary: Revenue declined 4% in FY2026, yet net income increased, indicating improved profitability.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxPSklRUUE2RmlwVmlFNndVSlg5YUNtRUVQMmdXSzNhRV96V2haN2ZBb19JdWNLeU8zVjMwdGYwaHkxdm0wQnp2ekF1U0ZrSkxBVEp1XzNVRU5SMjY3UUhHNWdJRWVDOUhkMVFUeDZGU2lzMHpBc3ZFNTBUOHVsMFJISWVLWVJRUDZ1dTZ5YUFhSFc1Z0tTTWZKZU1hZ0t2QUNFcnJmbXhaUXBJQmIzUmc?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMTM** | **24.88** | **1.07** | **8.46** | **-2.00** | **5,049,057,280.00 USD** | **-14.88** |
| LDOS | 11.03 | 2.91 | 8.73 | 3.60 | 15,062,685,696.00 USD | -33.03 |
| CACI | 24.23 | 2.82 | 14.50 | 8.20 | 13,112,536,064.00 USD | -1.60 |
| SAIC | 16.68 | 4.18 | 11.38 | 6.30 | 5,989,476,864.00 USD | 70.10 |

Peers fetched as_of: 2026-11-23; AMTM reuses existing data (market data as_of: 2026-11-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-23
- Next expected earnings: N/A (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-23

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-11
- Revenue (latest available single quarter): 3,490,000,000.00 USD; period 2026-04-04/2026-07-03; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 66,000,000.00 USD; period 2026-04-04/2026-07-03; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/2011286/000162828026055727/amtm-20260703.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMinwFBVV95cUxNYmthQ0g1M0FCOWt5UnpxQUpURFVsWTh2XzVCR1BIazVBVU5qQnBVdFRUMW5nVnlrMHFPTDFFRHlYSzhERE1pcXZiTGN1NFY4dGdYdXVFdzFONzl2VW5MdXlJM1ljaVRLWUJRSnZ0dlNTYldUVXppemJBVzEzMjVkNWU1ZUVUbHNvcWxaeXpWdk9xOExCTF9xenlDMzNpWDQ?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxOVkw3X3lzdWFxaGNfRmVRWUppMVJhOEs2aU5KQlJHTzdhcENzMkVpeWpSSUJPQm5JTHgtUU91TEdtMWIwc3FtTG15VWVIdXplTTZPdjFvMXFiRURZUkd4b05Ha1BLbGNsV05xRDZFWnotaDhQaU01R2pTSldUWEJzdFRhRjZCQ2V5cXZadkFGclkyMGdRa19jaFZSdlJGT0c0NDZFRG9sYmZwVGtaZ3g4NHBZb01JaXVJOUtfZGdZTGtwTnBiRzBmcDJJV1hxUQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNQ0hkUlFVZDk1dHNBNE9fNC0zd0c5Yl9makZZZm1vQUNHVVZocmtNbTMyVVZwX21lVThiVVhHMFFxVlZRTno4aGtYM0tuWEZoblc5UFZRRjA4Y18yZm5iOGRla0tYZnVDZDcweXVJN2hSYVFwemlIU2FITjdPM2RJZGlkRjktUzBNNy1qaUdMd3FLQldjMmp4UWdVVWQ?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxNV0RMVUozcDlZZ01MODlHNEZqVTZ5bnc3ZEs4ZVZMaXJwRVdKTkJjd2dwMzJzbFN6ZDZVMmRscUYzS0FMUVFLSUhqanJMREIzNmJST05BOHBhSk5ReHFVN0tSbXYwanhfVzBFUEtEbUw3YlYxYXlIV2Q0d2g0cWZWMWVveHR1UWhGQVBWTllxM2pTTmRPTmtKNEtKTkVzU2JIM0d1Z01BWXhXbFhBVGdrNmt6ZFpzMEZwSVAyTDNIUTI?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxOUl9zYXkyLTBBUVpHQ3A3TGY1YmNJNjdWRWNZcEpfRGZ6SlNZLU1kcTZLZ0pVQkxGSG9RSXlhR3pMdWZIdW10MVdnUmpQQ2NsbDhWSGYyTm42WEFUNVE3UWhNTHR1LUVQVUdVc0NlQ01wMElwTU9SdnR4dFA2MjUya2l2al9aV25rQzZva1ozcklUVjZ0aThpSzBuSktVOWE3enRCRQ?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxPSklRUUE2RmlwVmlFNndVSlg5YUNtRUVQMmdXSzNhRV96V2haN2ZBb19JdWNLeU8zVjMwdGYwaHkxdm0wQnp2ekF1U0ZrSkxBVEp1XzNVRU5SMjY3UUhHNWdJRWVDOUhkMVFUeDZGU2lzMHpBc3ZFNTBUOHVsMFJISWVLWVJRUDZ1dTZ5YUFhSFc1Z0tTTWZKZU1hZ0t2QUNFcnJmbXhaUXBJQmIzUmc?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
