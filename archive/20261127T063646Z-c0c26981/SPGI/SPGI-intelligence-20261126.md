# SPGI Intelligence Report

- ticker: **SPGI**
- Report as_of: **2026-11-26**
- Market data as_of: **2026-11-25**
- Quant sources: https://finance.yahoo.com/quote/SPGI/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SPGI/key-statistics/
- AI analysis snapshot as_of: **2026-11-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-27T06:39:30.515393+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 11, 'rule': 2, 'ai': 4, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261126T064454Z-dbdd6f45/SPGI** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 11 unique headlines; 7 named publishers; 0 exact duplicates; 11 HTTPS source links; largest publisher share 27.27%; oldest publication 2026-11-23

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 460.7400 |
| Return 1D (%) | 1.4399 |
| Return 1W (%) | 3.4374 |
| Return 1M (%) | 2.5347 |
| Return YTD (%) | -5.9652 |
| Return 1Y (%) | -0.5613 |
| Annualized volatility (%) | 31.3374 |
| Beta vs SPY | 0.4044 |
| Max drawdown (%) | -28.4781 |
| Sharpe (rf=0) | 0.1402 |
| Downside deviation (rf=0, %) | 23.4291 |
| Sortino (rf=0) | 0.1875 |
| Historical VaR 95% (1D, %) | 2.9286 |
| Historical ES 95% (1D, %) | 4.7258 |
| Correlation vs SPY | 0.1927 |
| Tracking error vs SPY (%) | 32.0100 |
| P/E (trailing) | 27.52 |
| P/B | 6.78 |
| EV/EBITDA | 17.87 |
| Revenue growth (%) | 6.80 |
| Forward P/E (estimate) | 22.84 |
| Gross margin (%) | 70.99 |
| Operating margin (%) | 44.09 |
| Return on equity (%) | 17.88 |
| Free cash flow yield (%) | 4.52 |
| MA50 | 433.0644 |
| Close vs MA50 (%) | 6.3906 |
| MA200 | 414.0311 |
| Close vs MA200 (%) | 11.2815 |
| RSI (14, Wilder) | 55.6722 |
| MACD (12,26) | 3.5154 |
| MACD signal (9) | 6.7022 |
| MACD histogram | -3.1869 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SPGI': 290, 'SPY': 290}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 460.7400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.4399 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 3.4374 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 2.5347 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -5.9652 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -0.5613 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 31.3374 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 23.4291 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.1875 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9286 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.7258 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1927 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.0100 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.4044 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.4781 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1402 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 22.8374 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 70.9940 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 44.0930 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 17.8760 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.5212 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 27.5233 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 55.6722 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.1869 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 6.3906 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 11.2815 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

### S&P Global (SPGI) Stock Looks Reasonable Even After New Debt
- Summary: New debt issuance may weigh on SPGI's financials.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxOQXU1eUlmQ2xRVnVNOEdVT2hDTHVvR1EySFR0Z0xiSm1FODN5LVNyczliV1hMNUVrQWUxcFVXQnY0U0dsSE02RnpxOVJUdkV4YmhZYVlHbFVGdFZLUDlvTC1HNng0Umh0YVpKdW14bnItWk9WN0lUSm5kTXI3anE0WGQ0WS1SdjhhNkRtdlhCd1VJWjJmRTFqbnFZVjdEcl8tYTZaYmZxbHdYQUxMeXI3eTd1NVI1NXNvNUoySkZxekZHajlBWWZKby13Nmtub0ZEZ2Nj0gHYAUFVX3lxTE9SRTVSYXhXUFI2T3dMY0Q0LWNPaUQ5MnNSVXl0cjdFUkZXOHhhTW1nNlBRU2tFWW9hVXZORXVzMGxjYmlRNy1qamh5M19Rc1pBRnJmUzQ2dWJhYWRmZmNxY3NEdmpOMkcxSzJNUUNUS2JkbUtNd1U3NWY1SmthajhWZ0Nhb3VwZU9kaHpqcWxCRllQcEQ5N210bmlVb3lSano0VThCS21RZTRuZnJDS3AyS0g1VFhNUE9HSjlNOTRXN2UxSTJVSjFuRHQ5RmdNYjZna2dhOURiUw?oc=5>

## CATALYSTS

### S&P Global (SPGI) Stock Looks Fully Valued Based On Earnings Power
- Summary: S&P Global (SPGI) Stock Looks Fully Valued Based On Earnings Power
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOTlRWSE12TmM4LUt5VWhRNHBPak9oUHJubFdKYU5lQUlTaEttMHJuQkhIZmlfY0pnbzlaUTk1RDA3QWdIUGI0ZVdhNHdKODZCeWMzWW4ySTRaUFQtb1d1aDI2dGRUcHJQYXpkalFOYV9xalVEcGdpdUNlbU5sVnFHcG1NT1o3WjBtZmEyUFVzcXpxMnI0?oc=5>

### S&P Global (SPGI) After November Updates Still Looks Undervalued To Analysts
- Summary: S&P Global (SPGI) After November Updates Still Looks Undervalued To Analysts
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxOZFo4ZURobWVzcTJRYnVtSlNkRi1BMGZySWNCOW1tVXBlQUYyVDl6bXloM2JSZW5oMTRJX0F0ODk1ZVhZOXR3bU1VUVJLXzE3WEJLdU9lNXhRbmpTYXhicW5GMFlRdzVEWHJBNDduaUg4Z2FfZ0VzX1V4ZlM1VFEwVXdlaEVxdGQ1anNvTE80MU5XWU9mRFpBSEJGN0Z1Mk5NU0VYa2ZXOVhiX3dQVlFpWHYteFpBSXcyb2VQSEV2Zm9hNHA0NWpwQzE0Y1dNSGE3amhEU3BSTdIB3AFBVV95cUxOLU9RU2VabmRQTkpmNTAwaUowVkt3NU11ME1vZ0MtenNLMmdQZ3ZoMlMxVDJiSUhWZWtIQ05iNEhVTWRvTHdBNTdTc0ZLMGl0ZDFIOUhVbXA3RlpHVDhhaV81empFOC1UcUZxelplTmNYV1hHYThaWGkzcC1xdDZnS1F4bDA0dGQwZFJ3VFJYdlFEM18yN3l4clFQM09jOGU5NGFEZ0t0VVB6emxuNWRQbTZWQ1BKSVgzYzdNRU8xLU1UdUwtQjh3SWRsTlZYbW8xSXBlU0VYS3VNUy1k?oc=5>

### Cognizant in talks for S&P Global's India-based Capital IQ operations - report (CTSH:NASDAQ)
- Summary: Cognizant seeks to acquire or partner with S&P Global’s Capital IQ India unit, potentially expanding its analytics footprint.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxNbWtnOWNkTVRZU01JRElhTmZSdTJiUDR5RlNoVjdBQkxDSWUteU9KZlRTbTBnUmdBcUswNG95Wk5fOG1WWl85UEh1TXZUdERMWnRadW1BVFRKZEVzdzRmTGNQSXN1UjZwQl83cnEzcFVjNXhacTV1VnZDODFpQnRGakh1b2JmS1VQdTlfRVZCU0JiQnlwN0l2cE1hVGNPUFJOZmZrRXIzNm1MTng2SGp1LVpLWDA?oc=5>

### Why Is S&P Global (SPGI) Up 2.5% Since Last Earnings Report?
- Summary: S&P Global shares rose 2.5% since the last earnings report, reflecting positive investor sentiment.
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxPT0pSWnU3MTN4M2Jfc0J2RW56WlAySC1sWHhrcGVGSFlxYl9pUGxMU2pBbXgtclJZcmp6V3FYWXJqTFd6VkZUY2xxY2c3WHEyd3R0NWdkNFNUMHF0UUwxSDFnUlVMOHFtMHI4bnB0c203Vk9KLXBmZVdTR1JLWW1CdG1YU3o1MGd4LUpZYQ?oc=5>

### How Is S&P Global (NYSE:SPGI) Building Its Digital Finance Capabilities?
- Summary: S&P Global is enhancing its digital finance tools to improve efficiency and client services.
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxNcGN0TjFxVzVCNUNKdTlSWW9Oai0xdllRUDlONDdybnlfdUliN0QtNnlTMWJUZkRjX3VWaDc2cDQ5WGtPaVVfcDR3YkhwenJnSW10SmoyVDRPYXhEVzRQUFpsbUUzbktFZzJTU3paUmpNREpBTlZuWlF3YW1HT0lyU0NpaW53VmMtWmk4M1lpSnpsbVJhdGZwdWc5QUtyQUJUcDNzRXpObnVvejNmM29DT3FB?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SPGI** | **27.52** | **6.78** | **17.87** | **6.80** | **133,568,520,192.00 USD** | **-0.56** |
| MCO | 29.63 | 25.63 | 22.20 | 0.80 | 83,744,653,312.00 USD | 0.89 |
| MSCI | 33.47 | -15.05 | 25.71 | 12.40 | 45,259,501,568.00 USD | 14.06 |
| FDS | 22.28 | 5.72 | 14.13 | 6.30 | 11,442,224,128.00 USD | 18.52 |

Peers fetched as_of: 2026-11-26; SPGI reuses existing data (market data as_of: 2026-11-25); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-27
- Next expected earnings: 2027-02-09 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-26

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-28
- Revenue (latest available single quarter): 1,567,000,000.00 USD; period 2018-01-01/2018-03-31; fiscal year/reporting period 2018/Q1
- Net income (latest available single quarter): 1,240,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/64040/000006404026000058/spgi-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi0wFBVV95cUxOQXU1eUlmQ2xRVnVNOEdVT2hDTHVvR1EySFR0Z0xiSm1FODN5LVNyczliV1hMNUVrQWUxcFVXQnY0U0dsSE02RnpxOVJUdkV4YmhZYVlHbFVGdFZLUDlvTC1HNng0Umh0YVpKdW14bnItWk9WN0lUSm5kTXI3anE0WGQ0WS1SdjhhNkRtdlhCd1VJWjJmRTFqbnFZVjdEcl8tYTZaYmZxbHdYQUxMeXI3eTd1NVI1NXNvNUoySkZxekZHajlBWWZKby13Nmtub0ZEZ2Nj0gHYAUFVX3lxTE9SRTVSYXhXUFI2T3dMY0Q0LWNPaUQ5MnNSVXl0cjdFUkZXOHhhTW1nNlBRU2tFWW9hVXZORXVzMGxjYmlRNy1qamh5M19Rc1pBRnJmUzQ2dWJhYWRmZmNxY3NEdmpOMkcxSzJNUUNUS2JkbUtNd1U3NWY1SmthajhWZ0Nhb3VwZU9kaHpqcWxCRllQcEQ5N210bmlVb3lSano0VThCS21RZTRuZnJDS3AyS0g1VFhNUE9HSjlNOTRXN2UxSTJVSjFuRHQ5RmdNYjZna2dhOURiUw?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOTlRWSE12TmM4LUt5VWhRNHBPak9oUHJubFdKYU5lQUlTaEttMHJuQkhIZmlfY0pnbzlaUTk1RDA3QWdIUGI0ZVdhNHdKODZCeWMzWW4ySTRaUFQtb1d1aDI2dGRUcHJQYXpkalFOYV9xalVEcGdpdUNlbU5sVnFHcG1NT1o3WjBtZmEyUFVzcXpxMnI0?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxOZFo4ZURobWVzcTJRYnVtSlNkRi1BMGZySWNCOW1tVXBlQUYyVDl6bXloM2JSZW5oMTRJX0F0ODk1ZVhZOXR3bU1VUVJLXzE3WEJLdU9lNXhRbmpTYXhicW5GMFlRdzVEWHJBNDduaUg4Z2FfZ0VzX1V4ZlM1VFEwVXdlaEVxdGQ1anNvTE80MU5XWU9mRFpBSEJGN0Z1Mk5NU0VYa2ZXOVhiX3dQVlFpWHYteFpBSXcyb2VQSEV2Zm9hNHA0NWpwQzE0Y1dNSGE3amhEU3BSTdIB3AFBVV95cUxOLU9RU2VabmRQTkpmNTAwaUowVkt3NU11ME1vZ0MtenNLMmdQZ3ZoMlMxVDJiSUhWZWtIQ05iNEhVTWRvTHdBNTdTc0ZLMGl0ZDFIOUhVbXA3RlpHVDhhaV81empFOC1UcUZxelplTmNYV1hHYThaWGkzcC1xdDZnS1F4bDA0dGQwZFJ3VFJYdlFEM18yN3l4clFQM09jOGU5NGFEZ0t0VVB6emxuNWRQbTZWQ1BKSVgzYzdNRU8xLU1UdUwtQjh3SWRsTlZYbW8xSXBlU0VYS3VNUy1k?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxNbWtnOWNkTVRZU01JRElhTmZSdTJiUDR5RlNoVjdBQkxDSWUteU9KZlRTbTBnUmdBcUswNG95Wk5fOG1WWl85UEh1TXZUdERMWnRadW1BVFRKZEVzdzRmTGNQSXN1UjZwQl83cnEzcFVjNXhacTV1VnZDODFpQnRGakh1b2JmS1VQdTlfRVZCU0JiQnlwN0l2cE1hVGNPUFJOZmZrRXIzNm1MTng2SGp1LVpLWDA?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxPT0pSWnU3MTN4M2Jfc0J2RW56WlAySC1sWHhrcGVGSFlxYl9pUGxMU2pBbXgtclJZcmp6V3FYWXJqTFd6VkZUY2xxY2c3WHEyd3R0NWdkNFNUMHF0UUwxSDFnUlVMOHFtMHI4bnB0c203Vk9KLXBmZVdTR1JLWW1CdG1YU3o1MGd4LUpZYQ?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxNcGN0TjFxVzVCNUNKdTlSWW9Oai0xdllRUDlONDdybnlfdUliN0QtNnlTMWJUZkRjX3VWaDc2cDQ5WGtPaVVfcDR3YkhwenJnSW10SmoyVDRPYXhEVzRQUFpsbUUzbktFZzJTU3paUmpNREpBTlZuWlF3YW1HT0lyU0NpaW53VmMtWmk4M1lpSnpsbVJhdGZwdWc5QUtyQUJUcDNzRXpObnVvejNmM29DT3FB?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
