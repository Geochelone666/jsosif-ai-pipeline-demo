# ENB Intelligence Report

- ticker: **ENB**
- Report as_of: **2026-11-27**
- Market data as_of: **2026-11-27**
- Quant sources: https://finance.yahoo.com/quote/ENB/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ENB/key-statistics/
- AI analysis snapshot as_of: **2026-11-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-28T06:20:52.254257+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 13, 'rule': 6, 'ai': 3, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261127T063646Z-c0c26981/ENB** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 13 unique headlines; 8 named publishers; 0 exact duplicates; 13 HTTPS source links; largest publisher share 23.08%; oldest publication 2026-11-23

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 47.0300 |
| Return 1D (%) | 0.1704 |
| Return 1W (%) | 2.9328 |
| Return 1M (%) | -1.3967 |
| Return YTD (%) | 3.7681 |
| Return 1Y (%) | 3.3145 |
| Annualized volatility (%) | 18.3388 |
| Beta vs SPY | -0.0862 |
| Max drawdown (%) | -19.8462 |
| Sharpe (rf=0) | 0.1866 |
| Downside deviation (rf=0, %) | 12.9814 |
| Sortino (rf=0) | 0.2636 |
| Historical VaR 95% (1D, %) | 1.8097 |
| Historical ES 95% (1D, %) | 2.5127 |
| Correlation vs SPY | -0.0706 |
| Tracking error vs SPY (%) | 24.5129 |
| P/E (trailing) | 22.61 |
| P/B | 2.42 |
| EV/EBITDA | 13.03 |
| Revenue growth (%) | 44.00 |
| Forward P/E (estimate) | 21.18 |
| Gross margin (%) | 30.20 |
| Operating margin (%) | 12.82 |
| Return on equity (%) | 9.85 |
| Free cash flow yield (%) | N/A |
| MA50 | 46.8561 |
| Close vs MA50 (%) | 0.3712 |
| MA200 | 50.6990 |
| Close vs MA200 (%) | -7.2369 |
| RSI (14, Wilder) | 50.8081 |
| MACD (12,26) | -0.2431 |
| MACD signal (9) | -0.2012 |
| MACD histogram | -0.0420 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ENB': 291, 'SPY': 291}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 47.0300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.1704 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.9328 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -1.3967 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 3.7681 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 3.3145 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 18.3388 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 12.9814 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.2636 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.8097 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.5127 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.0706 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.5129 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.0862 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -19.8462 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1866 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 21.1781 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 30.1950 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 12.8210 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.8490 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 22.6106 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 50.8081 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.0420 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 0.3712 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -7.2369 -> Clearly below the moving-average trend level.

## TAILWINDS

### Enbridge stock rises as buyer demand builds amid C$1.5 billion Line 3 stake sale talks
- Summary: Enbridge stock rises as buyer demand builds amid C$1.5 billion Line 3 stake sale talks
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQMHh6RkFtaDBfWUZrUVdXZlhlOEhKaTUyVUllVHdRdUhnWkQ4U2o3LXVlZlB3VEFod1laTmNybWNyV05JSHdoMWtNMjd2ZGZEalhRZnBLb0ctWjhVUXJsWlh2ZGVJSnFnLU5GV2MwR2d3cEVDbm1yeEFQVWJfMVN6N0JXN2NTQmVQRTk0V3g4cEpSS044?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Enbridge sees large fund acquisition: ENB remains range-bound
- Summary: Enbridge sees large fund acquisition: ENB remains range-bound
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPS0FoRnJaaGtLakkxeTNhYTRQNjU1VC1VanpYYlRmWnlpNzZWNEtER05GR1BOR1VHMXJUNTRmczFPaTNBTEJZM1ZYM04zb0oyWE5mNEFjUmZPZ01xWlIzcjdlN0dJY2NXMVIyUEdkLUhPX1NBREtRU3pRbm80bVU4eVFlSWYtOWVtTjZWd0tycVMtWDg?oc=5>

### Enbridge in talks for C$1.5B pipeline deal with indigenous communities- report (ENB:NYSE)
- Summary: Enbridge in talks for C$1.5B pipeline deal with indigenous communities- report (ENB:NYSE)
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxOdmhESDhiblBaUmxaanpMaG80VnkwQ0t6NDl3VnBtdVI1ejBuYWw5TjdLSllJQ01sV2Q0bFczQXdDSU5jcktwRFdpdGpndzhLdkY3cnlmbUN2Q2JvUURJTFlTSmhaSDM2NUw3VDRJQ0QwdlNwckV6bWE0b0RZZnJla2JwQ3E5aGc3R0d2OVhaVnZkOE9PWFoyVTdmVkRMZmtQNGdPSXNnRjg4am5manJ2N0VoWWk?oc=5>

### Enbridge reaffirms 2026 guidance and raises dividend: ENB tests C$65.94 resistance
- Summary: Enbridge reaffirms 2026 guidance and raises dividend: ENB tests C$65.94 resistance
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQaTRha1ljQjNDVHRGQkVwdDJ2bTVLeG11clk5cE4za2E5V284c3ZzWUpQWlc0cUtvRnRwTDFkYlFCYURkOFFyVU1Lc1hCTk5aZ2tIcnZOY2R1amJhTko0SDFGUFBOcjdKXzBxNTJtZWx4eWpWdHJUTm8yWHZ0dlAxc2w0bUVDdXJVQ2pNaUtPRU5KV2Nza0E?oc=5>

### Enbridge Inc (NYSE:ENB) Stock Has Consensus Price Target of $65.88 According to Brokerages
- Summary: Enbridge Inc (NYSE:ENB) Stock Has Consensus Price Target of $65.88 According to Brokerages
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi5AFBVV95cUxOWWFTMEo5QjRsaHZNTDBwYTdfNVZXaDhzbmJSRE5RY0pSNmNzU1RyUnJsU1lVNExoT29HWHctNnFNNUZxbXpBY1NJVEdnMXgyV2FGdHpCdzZhMHEtcUVqVmVVdExpQmNmT1pXTDRzRmdBMThYNkMwSHJxN1RGQS1oZW93MzZMUjBnVVdUZm54d05XNTAxRUVTLWxsRUJSMzVBMGJSdUdIY25qQTlLLVFXaHR0Q1RKcUFQQk9UdU9heWxWOTdsRmJ3NDdlS0FoOFBKLTlsc2k1VWs5TElYdGJZcllMLVI?oc=5>

### Enbridge Inc $ENB Shares Newly Acquired by Marshall Wace LLP
- Summary: Enbridge Inc $ENB Shares Newly Acquired by Marshall Wace LLP
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxPSDlPM3BDc1Vxd2pibWtUSkpSazktejBvaHl4SHp3N0NBTEh1YzQ0UWtRQlQydTl6RFNlWmFUWmkxSENWM0tNRG15czhMd3BUY0JfemZuR0RhWHljd3lzOXc5N1BqRDJfQWd3U2l2aVQ2bEFibjU2ZjFfcU1UbG4wamRZUUVUQ3NDYlVNQzJUa3JYOEx0ZjVnUUZ6U1k3REQ1RXpicy1LZWItb01nbmxaV2JrYnhYZVFielJSWA?oc=5>

### Enbridge Inc (ENB) is Attracting Investor Attention: Here is What You Should Know
- Summary: Investor focus on Enbridge’s stable cash flows and growth outlook.
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxObVVfb2FJNHFLZUlERUtVTTMwZzc5Y3MwcnVDQTFBQlc2ZGdDRlBsN1R6c054NEE1MEd1UktiaXdMRXVFandidkRPZmtvaVVpV3dTVE9ZX0NyOWxYcW5tNmdKelFWems4WXdsQXU0a0EzZEJjcTBXaE8zUWJ5YWpRLXpZMklaa0V6Tk1XbVdn?oc=5>

### Enbridge: Yield Is Very Attractive, But Performance Is Underwhelming (NYSE:ENB)
- Summary: Analyst notes attractive dividend yield but weak performance, suggesting cautious investment.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxQWENkQ3JydFBJb2JlejRXUFhHYjRzRjdBczRzSWdfU1NEVENHQkVXNzllczNKN1ZodXptakZiZnZxa0I4OU5oVWpGendfai1tT2Z3OTBqSzdlU2xKQzBObzIwVXY5NzdNTm5LSmJwWU5xRkY4S3JYT3JsY3VrQUZMMzhLdFliWkVjSDRqTWctcUNYaDU0SUE3LUthaG9SQm1xUmYyVkFOYmFkdUk?oc=5>

## RISKS

### Enbridge stock could be at risk of falling to $61.5 despite strong revenue growth
- Summary: Enbridge shares may drop to $61.5 amid strong revenue growth.
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxQTS1lSTJlSlgwanBmSkVZaDZ6ekRCdU04YjVXNE5vUnR1VENzRmZUOFZ5WjM4Und3c1RpZUdjZExhVkEwTWFYTEM3WWo5SDFIZk5NZVkzbXd3eDgwWXJoRGdHYVNLVFUyWEpIdGhXWk1VTzFZWHFHbnFyZ2FKYldnOF9QdmJmUjBjYW02R2VOaDFaaVJWaW9RMmdfaTY5QmotZG5IT1BPUWRETmN5ckE3d094dkYxM0dnV29qQWdkYVN6dGhGekFYVlEwaWZrLW9JZ0hZeFNYR1JpNkpQZGZtaEYzNVdHTGtQLUdIZw?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ENB** | **22.61** | **2.42** | **13.03** | **44.00** | **104,824,602,624.00 USD** | **3.31** |
| TRP.TO | 24.28 | 3.66 | 16.50 | 8.80 | 93,592,338,432.00 CAD | 23.43 |
| KMI | 19.80 | 2.26 | 13.69 | 9.30 | 71,442,833,408.00 USD | 23.48 |
| EPD | 12.01 | 2.58 | 10.69 | 49.30 | 78,241,628,160.00 USD | 18.40 |

Peers fetched as_of: 2026-11-27; ENB reuses existing data (market data as_of: 2026-11-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-06
- Next expected earnings: 2027-02-12 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-27

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-06
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: https://www.sec.gov/Archives/edgar/data/895728/000119312526450714/enb-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMilAFBVV95cUxQMHh6RkFtaDBfWUZrUVdXZlhlOEhKaTUyVUllVHdRdUhnWkQ4U2o3LXVlZlB3VEFod1laTmNybWNyV05JSHdoMWtNMjd2ZGZEalhRZnBLb0ctWjhVUXJsWlh2ZGVJSnFnLU5GV2MwR2d3cEVDbm1yeEFQVWJfMVN6N0JXN2NTQmVQRTk0V3g4cEpSS044?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPS0FoRnJaaGtLakkxeTNhYTRQNjU1VC1VanpYYlRmWnlpNzZWNEtER05GR1BOR1VHMXJUNTRmczFPaTNBTEJZM1ZYM04zb0oyWE5mNEFjUmZPZ01xWlIzcjdlN0dJY2NXMVIyUEdkLUhPX1NBREtRU3pRbm80bVU4eVFlSWYtOWVtTjZWd0tycVMtWDg?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxOdmhESDhiblBaUmxaanpMaG80VnkwQ0t6NDl3VnBtdVI1ejBuYWw5TjdLSllJQ01sV2Q0bFczQXdDSU5jcktwRFdpdGpndzhLdkY3cnlmbUN2Q2JvUURJTFlTSmhaSDM2NUw3VDRJQ0QwdlNwckV6bWE0b0RZZnJla2JwQ3E5aGc3R0d2OVhaVnZkOE9PWFoyVTdmVkRMZmtQNGdPSXNnRjg4am5manJ2N0VoWWk?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQaTRha1ljQjNDVHRGQkVwdDJ2bTVLeG11clk5cE4za2E5V284c3ZzWUpQWlc0cUtvRnRwTDFkYlFCYURkOFFyVU1Lc1hCTk5aZ2tIcnZOY2R1amJhTko0SDFGUFBOcjdKXzBxNTJtZWx4eWpWdHJUTm8yWHZ0dlAxc2w0bUVDdXJVQ2pNaUtPRU5KV2Nza0E?oc=5
- https://news.google.com/rss/articles/CBMi5AFBVV95cUxOWWFTMEo5QjRsaHZNTDBwYTdfNVZXaDhzbmJSRE5RY0pSNmNzU1RyUnJsU1lVNExoT29HWHctNnFNNUZxbXpBY1NJVEdnMXgyV2FGdHpCdzZhMHEtcUVqVmVVdExpQmNmT1pXTDRzRmdBMThYNkMwSHJxN1RGQS1oZW93MzZMUjBnVVdUZm54d05XNTAxRUVTLWxsRUJSMzVBMGJSdUdIY25qQTlLLVFXaHR0Q1RKcUFQQk9UdU9heWxWOTdsRmJ3NDdlS0FoOFBKLTlsc2k1VWs5TElYdGJZcllMLVI?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxPSDlPM3BDc1Vxd2pibWtUSkpSazktejBvaHl4SHp3N0NBTEh1YzQ0UWtRQlQydTl6RFNlWmFUWmkxSENWM0tNRG15czhMd3BUY0JfemZuR0RhWHljd3lzOXc5N1BqRDJfQWd3U2l2aVQ2bEFibjU2ZjFfcU1UbG4wamRZUUVUQ3NDYlVNQzJUa3JYOEx0ZjVnUUZ6U1k3REQ1RXpicy1LZWItb01nbmxaV2JrYnhYZVFielJSWA?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxObVVfb2FJNHFLZUlERUtVTTMwZzc5Y3MwcnVDQTFBQlc2ZGdDRlBsN1R6c054NEE1MEd1UktiaXdMRXVFandidkRPZmtvaVVpV3dTVE9ZX0NyOWxYcW5tNmdKelFWems4WXdsQXU0a0EzZEJjcTBXaE8zUWJ5YWpRLXpZMklaa0V6Tk1XbVdn?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxQWENkQ3JydFBJb2JlejRXUFhHYjRzRjdBczRzSWdfU1NEVENHQkVXNzllczNKN1ZodXptakZiZnZxa0I4OU5oVWpGendfai1tT2Z3OTBqSzdlU2xKQzBObzIwVXY5NzdNTm5LSmJwWU5xRkY4S3JYT3JsY3VrQUZMMzhLdFliWkVjSDRqTWctcUNYaDU0SUE3LUthaG9SQm1xUmYyVkFOYmFkdUk?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxQTS1lSTJlSlgwanBmSkVZaDZ6ekRCdU04YjVXNE5vUnR1VENzRmZUOFZ5WjM4Und3c1RpZUdjZExhVkEwTWFYTEM3WWo5SDFIZk5NZVkzbXd3eDgwWXJoRGdHYVNLVFUyWEpIdGhXWk1VTzFZWHFHbnFyZ2FKYldnOF9QdmJmUjBjYW02R2VOaDFaaVJWaW9RMmdfaTY5QmotZG5IT1BPUWRETmN5ckE3d094dkYxM0dnV29qQWdkYVN6dGhGekFYVlEwaWZrLW9JZ0hZeFNYR1JpNkpQZGZtaEYzNVdHTGtQLUdIZw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
