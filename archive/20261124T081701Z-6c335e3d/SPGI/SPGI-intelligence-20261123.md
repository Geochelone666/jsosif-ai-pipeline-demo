# SPGI Intelligence Report

- ticker: **SPGI**
- Report as_of: **2026-11-23**
- Market data as_of: **2026-11-23**
- Quant sources: https://finance.yahoo.com/quote/SPGI/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SPGI/key-statistics/
- AI analysis snapshot as_of: **2026-11-23**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-24T08:23:42.061185+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 9, 'rule': 0, 'ai': 4, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261123T053847Z-45053549/SPGI** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 9 unique headlines; 8 named publishers; 0 exact duplicates; 9 HTTPS source links; largest publisher share 22.22%; oldest publication 2026-11-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 451.9600 |
| Return 1D (%) | 2.8187 |
| Return 1W (%) | -4.1625 |
| Return 1M (%) | 0.3664 |
| Return YTD (%) | -7.9538 |
| Return 1Y (%) | -2.3561 |
| Annualized volatility (%) | 31.3828 |
| Beta vs SPY | 0.4122 |
| Max drawdown (%) | -28.4781 |
| Sharpe (rf=0) | 0.1104 |
| Downside deviation (rf=0, %) | 23.4759 |
| Sortino (rf=0) | 0.1475 |
| Historical VaR 95% (1D, %) | 2.9322 |
| Historical ES 95% (1D, %) | 4.7258 |
| Correlation vs SPY | 0.1967 |
| Tracking error vs SPY (%) | 32.0038 |
| P/E (trailing) | 27.00 |
| P/B | 6.65 |
| EV/EBITDA | 17.57 |
| Revenue growth (%) | 6.80 |
| Forward P/E (estimate) | 22.40 |
| Gross margin (%) | 70.99 |
| Operating margin (%) | 44.09 |
| Return on equity (%) | 17.88 |
| Free cash flow yield (%) | 4.61 |
| MA50 | 432.0370 |
| Close vs MA50 (%) | 4.6114 |
| MA200 | 414.3018 |
| Close vs MA200 (%) | 9.0895 |
| RSI (14, Wilder) | 50.1759 |
| MACD (12,26) | 3.5915 |
| MACD signal (9) | 8.5735 |
| MACD histogram | -4.9820 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SPGI': 288, 'SPY': 288}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 451.9600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.8187 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -4.1625 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 0.3664 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -7.9538 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -2.3561 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 31.3828 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 23.4759 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.1475 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9322 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.7258 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1967 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.0038 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.4122 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.4781 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1104 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 22.4022 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 70.9940 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 44.0930 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 17.8760 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.6090 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 26.9988 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 50.1759 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -4.9820 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 4.6114 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 9.0895 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

### S&P Global Inc Stock (SPGI) Moved Down by 3.38% on Nov 17: Drivers Behind the Movement
- Summary: Stock fell 3.38% on Nov 17, indicating short‑term negative market sentiment.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxPQVJhZjVzSkFPMFdROWtfajY2QWFPTlBYQnlURTVoTzFTa2Rhbnl1dGhPOGEwMTdhcG54dldITWV6czBjODFBWjZUbjAyd2gyclNzWUwwUi1jeUEweTdHYVk1TU92N2c2dndKSXV6Yy1SWE90dHBjaWpaVHBBQnVYcC0tcERtTkYzMlpN?oc=5>

### S&P Global (SPGI) Stock Looks Reasonable Even After New Debt
- Summary: New debt issuance may weigh on SPGI's financials.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxOQXU1eUlmQ2xRVnVNOEdVT2hDTHVvR1EySFR0Z0xiSm1FODN5LVNyczliV1hMNUVrQWUxcFVXQnY0U0dsSE02RnpxOVJUdkV4YmhZYVlHbFVGdFZLUDlvTC1HNng0Umh0YVpKdW14bnItWk9WN0lUSm5kTXI3anE0WGQ0WS1SdjhhNkRtdlhCd1VJWjJmRTFqbnFZVjdEcl8tYTZaYmZxbHdYQUxMeXI3eTd1NVI1NXNvNUoySkZxekZHajlBWWZKby13Nmtub0ZEZ2Nj0gHYAUFVX3lxTE9SRTVSYXhXUFI2T3dMY0Q0LWNPaUQ5MnNSVXl0cjdFUkZXOHhhTW1nNlBRU2tFWW9hVXZORXVzMGxjYmlRNy1qamh5M19Rc1pBRnJmUzQ2dWJhYWRmZmNxY3NEdmpOMkcxSzJNUUNUS2JkbUtNd1U3NWY1SmthajhWZ0Nhb3VwZU9kaHpqcWxCRllQcEQ5N210bmlVb3lSano0VThCS21RZTRuZnJDS3AyS0g1VFhNUE9HSjlNOTRXN2UxSTJVSjFuRHQ5RmdNYjZna2dhOURiUw?oc=5>

## CATALYSTS

### Are Wall Street Analysts Bullish on S&P Global Stock?
- Summary: Analysts express bullish sentiment toward SPGI, potentially influencing investor perception.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPeTZnUnVzVkFRclp1SkJYTzdJbXU1U25IcFN6ZDE3M0hTM2dERnI0MVNvazNlTGxrYnpEVlF5cFBlSm10NjNZWUh6bHI3aUp2b2cwVlQxU29vQlp0ZXN6dEZ0Rk9nb0dicHVESmxGdGFYYm9wVnhweG00X1pJUVh3YnE4eU5tTy1yRk5SOEZpOTAzeFRGMF9zeXM2dw?oc=5>

## RISKS

### S&P Global (SPGI) Stock Dropped, So What Is Driving Attention Now?
- Summary: SPGI shares fell, raising concerns about market reaction and potential underlying issues.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxNcEk5X3ZQM1dMM05YVFc1Y0szMEl6eW5nb0pCYl8xd2dTYlBMNVRtYm9lTWtDYmZsWjBEQm1wWjRNekExNldtRjI3Qkp0dFFBb3JwdWpKZzc5NFJGRWZwQjlEa2tUS1ZHUkwxX2l5YXJNcVJ3YjdSTldyaF9uZ2l6Q011SGtraTN3cnVxbEVzaFVOU01heW1Mc0JldmxBT0dJVlloSktIVmt2N3kzVWp6bjdOWEdzSHFHdk15cHRVN2x4WVlNNEo1Ny01NjYzcHVmcklfMzk1QdIB3AFBVV95cUxNSjh5bXZkUVJudjhjdkxrNk9BcWlxeWI3U0FBbm03Ylo1NWVWdk1zRW9wNzlXaFZxUEQwODZjeUllV2Z6VUN3d0JtNnhpZEVmMThuYmU2cndWVjNiWnRHeFZaNG81YTNLdlo4NGFNR2tPVXJCWTY3ZmFOUG9LRzdLNHNuZXQ2UDI5RTJZOUtJQ1JZdG1PNS1sV2ZfaFdyM1VjRWhRbzJLSlRBMklCSk8xQzctaGd4aUtoVE11dkJ1bVNiVVVMRVg3WC1yTnRJamEwaHNPbkE3djBEWG5Z?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SPGI** | **27.00** | **6.65** | **17.57** | **6.80** | **131,023,200,256.00 USD** | **-2.36** |
| MCO | 29.32 | 25.36 | 21.98 | 0.80 | 82,865,291,264.00 USD | 1.09 |
| MSCI | 33.19 | -14.92 | 25.52 | 12.40 | 44,876,259,328.00 USD | 13.29 |
| FDS | 21.45 | 5.50 | 13.65 | 6.30 | 11,017,040,896.00 USD | 14.82 |

Peers fetched as_of: 2026-11-23; SPGI reuses existing data (market data as_of: 2026-11-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-27
- Next expected earnings: 2027-02-09 (yfinance; expected dates may change)

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
- Filing date: 2026-10-28
- Revenue (latest available single quarter): 1,567,000,000.00 USD; period 2018-01-01/2018-03-31; fiscal year/reporting period 2018/Q1
- Net income (latest available single quarter): 1,240,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/64040/000006404026000058/spgi-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiiwFBVV95cUxPQVJhZjVzSkFPMFdROWtfajY2QWFPTlBYQnlURTVoTzFTa2Rhbnl1dGhPOGEwMTdhcG54dldITWV6czBjODFBWjZUbjAyd2gyclNzWUwwUi1jeUEweTdHYVk1TU92N2c2dndKSXV6Yy1SWE90dHBjaWpaVHBBQnVYcC0tcERtTkYzMlpN?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxOQXU1eUlmQ2xRVnVNOEdVT2hDTHVvR1EySFR0Z0xiSm1FODN5LVNyczliV1hMNUVrQWUxcFVXQnY0U0dsSE02RnpxOVJUdkV4YmhZYVlHbFVGdFZLUDlvTC1HNng0Umh0YVpKdW14bnItWk9WN0lUSm5kTXI3anE0WGQ0WS1SdjhhNkRtdlhCd1VJWjJmRTFqbnFZVjdEcl8tYTZaYmZxbHdYQUxMeXI3eTd1NVI1NXNvNUoySkZxekZHajlBWWZKby13Nmtub0ZEZ2Nj0gHYAUFVX3lxTE9SRTVSYXhXUFI2T3dMY0Q0LWNPaUQ5MnNSVXl0cjdFUkZXOHhhTW1nNlBRU2tFWW9hVXZORXVzMGxjYmlRNy1qamh5M19Rc1pBRnJmUzQ2dWJhYWRmZmNxY3NEdmpOMkcxSzJNUUNUS2JkbUtNd1U3NWY1SmthajhWZ0Nhb3VwZU9kaHpqcWxCRllQcEQ5N210bmlVb3lSano0VThCS21RZTRuZnJDS3AyS0g1VFhNUE9HSjlNOTRXN2UxSTJVSjFuRHQ5RmdNYjZna2dhOURiUw?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPeTZnUnVzVkFRclp1SkJYTzdJbXU1U25IcFN6ZDE3M0hTM2dERnI0MVNvazNlTGxrYnpEVlF5cFBlSm10NjNZWUh6bHI3aUp2b2cwVlQxU29vQlp0ZXN6dEZ0Rk9nb0dicHVESmxGdGFYYm9wVnhweG00X1pJUVh3YnE4eU5tTy1yRk5SOEZpOTAzeFRGMF9zeXM2dw?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxNcEk5X3ZQM1dMM05YVFc1Y0szMEl6eW5nb0pCYl8xd2dTYlBMNVRtYm9lTWtDYmZsWjBEQm1wWjRNekExNldtRjI3Qkp0dFFBb3JwdWpKZzc5NFJGRWZwQjlEa2tUS1ZHUkwxX2l5YXJNcVJ3YjdSTldyaF9uZ2l6Q011SGtraTN3cnVxbEVzaFVOU01heW1Mc0JldmxBT0dJVlloSktIVmt2N3kzVWp6bjdOWEdzSHFHdk15cHRVN2x4WVlNNEo1Ny01NjYzcHVmcklfMzk1QdIB3AFBVV95cUxNSjh5bXZkUVJudjhjdkxrNk9BcWlxeWI3U0FBbm03Ylo1NWVWdk1zRW9wNzlXaFZxUEQwODZjeUllV2Z6VUN3d0JtNnhpZEVmMThuYmU2cndWVjNiWnRHeFZaNG81YTNLdlo4NGFNR2tPVXJCWTY3ZmFOUG9LRzdLNHNuZXQ2UDI5RTJZOUtJQ1JZdG1PNS1sV2ZfaFdyM1VjRWhRbzJLSlRBMklCSk8xQzctaGd4aUtoVE11dkJ1bVNiVVVMRVg3WC1yTnRJamEwaHNPbkE3djBEWG5Z?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
