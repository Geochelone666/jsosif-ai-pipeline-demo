# SPGI Intelligence Report

- ticker: **SPGI**
- Report as_of: **2026-11-27**
- Market data as_of: **2026-11-27**
- Quant sources: https://finance.yahoo.com/quote/SPGI/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SPGI/key-statistics/
- AI analysis snapshot as_of: **2026-11-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-28T06:31:50.727075+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 9, 'rule': 1, 'ai': 4, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261127T063646Z-c0c26981/SPGI** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 9 unique headlines; 8 named publishers; 0 exact duplicates; 9 HTTPS source links; largest publisher share 22.22%; oldest publication 2026-11-23

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 461.2400 |
| Return 1D (%) | 0.1085 |
| Return 1W (%) | 5.1539 |
| Return 1M (%) | 2.9615 |
| Return YTD (%) | -5.8632 |
| Return 1Y (%) | -0.7386 |
| Annualized volatility (%) | 31.3927 |
| Beta vs SPY | 0.3995 |
| Max drawdown (%) | -28.4781 |
| Sharpe (rf=0) | 0.1139 |
| Downside deviation (rf=0, %) | 23.4759 |
| Sortino (rf=0) | 0.1523 |
| Historical VaR 95% (1D, %) | 2.9322 |
| Historical ES 95% (1D, %) | 4.7258 |
| Correlation vs SPY | 0.1912 |
| Tracking error vs SPY (%) | 32.1069 |
| P/E (trailing) | 27.55 |
| P/B | 6.78 |
| EV/EBITDA | 17.89 |
| Revenue growth (%) | 6.80 |
| Forward P/E (estimate) | 22.86 |
| Gross margin (%) | 70.99 |
| Operating margin (%) | 44.09 |
| Return on equity (%) | 17.88 |
| Free cash flow yield (%) | 4.52 |
| MA50 | 434.2243 |
| Close vs MA50 (%) | 6.2216 |
| MA200 | 414.5055 |
| Close vs MA200 (%) | 11.2748 |
| RSI (14, Wilder) | 55.9472 |
| MACD (12,26) | 3.7044 |
| MACD signal (9) | 6.1027 |
| MACD histogram | -2.3982 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SPGI': 291, 'SPY': 291}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 461.2400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.1085 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 5.1539 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 2.9615 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -5.8632 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -0.7386 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 31.3927 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 23.4759 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.1523 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9322 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.7258 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1912 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.1069 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3995 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.4781 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1139 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 22.8622 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 70.9940 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 44.0930 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 17.8760 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.5163 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 27.5532 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 55.9472 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -2.3982 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 6.2216 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 11.2748 -> Clearly above the moving-average trend level.

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

### Cognizant in talks for S&P Global's India-based Capital IQ operations - report (CTSH:NASDAQ)
- Summary: Cognizant seeks to acquire or partner with S&P Global’s Capital IQ India unit, potentially expanding its analytics footprint.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxNbWtnOWNkTVRZU01JRElhTmZSdTJiUDR5RlNoVjdBQkxDSWUteU9KZlRTbTBnUmdBcUswNG95Wk5fOG1WWl85UEh1TXZUdERMWnRadW1BVFRKZEVzdzRmTGNQSXN1UjZwQl83cnEzcFVjNXhacTV1VnZDODFpQnRGakh1b2JmS1VQdTlfRVZCU0JiQnlwN0l2cE1hVGNPUFJOZmZrRXIzNm1MTng2SGp1LVpLWDA?oc=5>

### Centuri Holdings Set to Join S&P SmallCap 600
- Summary: Centuri Holdings will be added to the S&P SmallCap 600 index, potentially increasing visibility and liquidity for the company.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxQQUNWRVpnQlRVcTNlVWNsdHRkSzI1VEZyaS01YnI1b0hXbE9KVTBPV3ZXNFlqMzFJUzlGR19aSThDcW9fUEFodW5ZM0hTbXFTaEVzWmVqTHFZQnFQcHliWXV0UnAxUVdmSFFwR1VPN1N1MXdvOXc0OXoxSDhlZUZZd1lBcE5hTXc3YU5qcnA1clA?oc=5>

### Cognizant in talks for S&P Global's India-based Capital IQ operations - report
- Summary: Cognizant is negotiating to acquire S&P Global’s India-based Capital IQ operations, potentially expanding its analytics footprint.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxQRmRTVVVxaE9tZ3RMYzcyV1lMRUNSc1BaaWUzWExsT1c5cjhycWpHT3djdWZKcjdsTDZiV1BTd19OY2ZVSE1XQ242aU9yY0pyTEYzNWVsdFJ6NWU0NERZa01RZWNVRW1KT0M2ZEhtZm9abURzb1RWUGU0aUlhOTVZaW1QdHdtSlVGNnZ1NWV5dENzN3dXUmFxOE5JaXR3ZFdKQTZ1dHhKVm1ZQUItWUlCWnhiYndQWW5WWmtybW1fN2kyVmE4OHRHYVJ5UUxhVVpTRVRIUTRB?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SPGI** | **27.55** | **6.78** | **17.89** | **6.80** | **133,713,469,440.00 USD** | **-0.74** |
| MCO | 29.77 | 25.74 | 22.30 | 0.80 | 84,132,610,048.00 USD | 1.06 |
| MSCI | 33.71 | -15.15 | 25.86 | 12.40 | 45,574,811,648.00 USD | 14.90 |
| FDS | 22.18 | 5.69 | 14.07 | 6.30 | 11,391,808,512.00 USD | 18.56 |

Peers fetched as_of: 2026-11-27; SPGI reuses existing data (market data as_of: 2026-11-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-27
- Next expected earnings: 2027-02-09 (yfinance; expected dates may change)

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
- Filing date: 2026-10-28
- Revenue (latest available single quarter): 1,567,000,000.00 USD; period 2018-01-01/2018-03-31; fiscal year/reporting period 2018/Q1
- Net income (latest available single quarter): 1,240,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/64040/000006404026000058/spgi-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi0wFBVV95cUxOQXU1eUlmQ2xRVnVNOEdVT2hDTHVvR1EySFR0Z0xiSm1FODN5LVNyczliV1hMNUVrQWUxcFVXQnY0U0dsSE02RnpxOVJUdkV4YmhZYVlHbFVGdFZLUDlvTC1HNng0Umh0YVpKdW14bnItWk9WN0lUSm5kTXI3anE0WGQ0WS1SdjhhNkRtdlhCd1VJWjJmRTFqbnFZVjdEcl8tYTZaYmZxbHdYQUxMeXI3eTd1NVI1NXNvNUoySkZxekZHajlBWWZKby13Nmtub0ZEZ2Nj0gHYAUFVX3lxTE9SRTVSYXhXUFI2T3dMY0Q0LWNPaUQ5MnNSVXl0cjdFUkZXOHhhTW1nNlBRU2tFWW9hVXZORXVzMGxjYmlRNy1qamh5M19Rc1pBRnJmUzQ2dWJhYWRmZmNxY3NEdmpOMkcxSzJNUUNUS2JkbUtNd1U3NWY1SmthajhWZ0Nhb3VwZU9kaHpqcWxCRllQcEQ5N210bmlVb3lSano0VThCS21RZTRuZnJDS3AyS0g1VFhNUE9HSjlNOTRXN2UxSTJVSjFuRHQ5RmdNYjZna2dhOURiUw?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOTlRWSE12TmM4LUt5VWhRNHBPak9oUHJubFdKYU5lQUlTaEttMHJuQkhIZmlfY0pnbzlaUTk1RDA3QWdIUGI0ZVdhNHdKODZCeWMzWW4ySTRaUFQtb1d1aDI2dGRUcHJQYXpkalFOYV9xalVEcGdpdUNlbU5sVnFHcG1NT1o3WjBtZmEyUFVzcXpxMnI0?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxNbWtnOWNkTVRZU01JRElhTmZSdTJiUDR5RlNoVjdBQkxDSWUteU9KZlRTbTBnUmdBcUswNG95Wk5fOG1WWl85UEh1TXZUdERMWnRadW1BVFRKZEVzdzRmTGNQSXN1UjZwQl83cnEzcFVjNXhacTV1VnZDODFpQnRGakh1b2JmS1VQdTlfRVZCU0JiQnlwN0l2cE1hVGNPUFJOZmZrRXIzNm1MTng2SGp1LVpLWDA?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxQQUNWRVpnQlRVcTNlVWNsdHRkSzI1VEZyaS01YnI1b0hXbE9KVTBPV3ZXNFlqMzFJUzlGR19aSThDcW9fUEFodW5ZM0hTbXFTaEVzWmVqTHFZQnFQcHliWXV0UnAxUVdmSFFwR1VPN1N1MXdvOXc0OXoxSDhlZUZZd1lBcE5hTXc3YU5qcnA1clA?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxQRmRTVVVxaE9tZ3RMYzcyV1lMRUNSc1BaaWUzWExsT1c5cjhycWpHT3djdWZKcjdsTDZiV1BTd19OY2ZVSE1XQ242aU9yY0pyTEYzNWVsdFJ6NWU0NERZa01RZWNVRW1KT0M2ZEhtZm9abURzb1RWUGU0aUlhOTVZaW1QdHdtSlVGNnZ1NWV5dENzN3dXUmFxOE5JaXR3ZFdKQTZ1dHhKVm1ZQUItWUlCWnhiYndQWW5WWmtybW1fN2kyVmE4OHRHYVJ5UUxhVVpTRVRIUTRB?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
