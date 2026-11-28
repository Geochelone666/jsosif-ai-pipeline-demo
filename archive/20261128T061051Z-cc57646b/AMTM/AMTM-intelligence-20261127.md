# AMTM Intelligence Report

- ticker: **AMTM**
- Report as_of: **2026-11-27**
- Market data as_of: **2026-11-27**
- Quant sources: https://finance.yahoo.com/quote/AMTM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMTM/key-statistics/
- AI analysis snapshot as_of: **2026-11-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-28T06:13:35.682623+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 20, 'rule': 9, 'ai': 5, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261127T063646Z-c0c26981/AMTM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 20 unique headlines; 10 named publishers; 1 exact duplicates; 20 HTTPS source links; largest publisher share 30.0%; oldest publication 2026-11-22

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 24.7100 |
| Return 1D (%) | -0.6034 |
| Return 1W (%) | 21.4848 |
| Return 1M (%) | 13.6092 |
| Return YTD (%) | -14.7931 |
| Return 1Y (%) | -15.7518 |
| Annualized volatility (%) | 44.3841 |
| Beta vs SPY | 0.7688 |
| Max drawdown (%) | -51.7186 |
| Sharpe (rf=0) | -0.1164 |
| Downside deviation (rf=0, %) | 29.8591 |
| Sortino (rf=0) | -0.1730 |
| Historical VaR 95% (1D, %) | 3.8360 |
| Historical ES 95% (1D, %) | 5.9321 |
| Correlation vs SPY | 0.2602 |
| Tracking error vs SPY (%) | 42.9957 |
| P/E (trailing) | 17.91 |
| P/B | 1.24 |
| EV/EBITDA | 9.46 |
| Revenue growth (%) | -7.80 |
| Forward P/E (estimate) | 8.18 |
| Gross margin (%) | 10.45 |
| Operating margin (%) | 4.25 |
| Return on equity (%) | 7.07 |
| Free cash flow yield (%) | 7.35 |
| MA50 | 20.6168 |
| Close vs MA50 (%) | 19.8537 |
| MA200 | 23.2428 |
| Close vs MA200 (%) | 6.3123 |
| RSI (14, Wilder) | 68.2894 |
| MACD (12,26) | 0.7327 |
| MACD signal (9) | 0.4751 |
| MACD histogram | 0.2575 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMTM': 291, 'SPY': 291}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 24.7100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.6034 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 21.4848 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 13.6092 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -14.7931 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -15.7518 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 44.3841 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 29.8591 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.1730 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.8360 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.9321 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2602 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 42.9957 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.7688 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -51.7186 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.1164 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 8.1802 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 10.4520 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 4.2530 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 7.0690 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 7.3455 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 17.9058 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 68.2894 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.2575 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 19.8537 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 6.3123 -> Clearly above the moving-average trend level.

## TAILWINDS

### Amentum Holdings (AMTM) Q4 Earnings Top Estimates
- Summary: Amentum Holdings (AMTM) Q4 Earnings Top Estimates
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNYmthQ0g1M0FCOWt5UnpxQUpURFVsWTh2XzVCR1BIazVBVU5qQnBVdFRUMW5nVnlrMHFPTDFFRHlYSzhERE1pcXZiTGN1NFY4dGdYdXVFdzFONzl2VW5MdXlJM1ljaVRLWUJRSnZ0dlNTYldUVXppemJBVzEzMjVkNWU1ZUVUbHNvcWxaeXpWdk9xOExCTF9xenlDMzNpWDQ?oc=5>

### Amentum (AMTM) Stock Is Up 14.5% Today: Earnings Beat, FY27 Guid
- Summary: Amentum (AMTM) Stock Is Up 14.5% Today: Earnings Beat, FY27 Guid
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAJBVV95cUxPNDB0VkswNU9EV2xVb1NzQldHNVdfWmVjVFd4c01fOUhhb2pabHQ0V0Y3OUo4dHF3cHdOTDFpb1JVd19jZWlsUVFuRUhCaGM0Y2RDdEtpdE5pRXFUMmVzUGJxZGdRbTVBd1VUajZNTlZoUnkxeVAtUGNCTnFZaENhemJ6bTZDTXNKSzJVdW5PVWhlOVdFN3V2Ny1SbnI0NWd6MFhHeC1GUUFjVEhkV2RwRjFwWnoxNFFsdmVUS2dXZEM2akdueEdOUUU5Q1VuV3lSdWRFdVRzdHhnMHdUS1U0VFJnWEh6aXpRSnhIS1RHVnhzMEZfUENwY0JOUjlYWlFLODRwUnFSNFVTWFZSR2NRS0draHIteF9FbTh1VDRmWmt2cFpfcDFNblFpU0s5Slox?oc=5>

### Amentum Holdings (AMTM) Board Approves $500 Million Stock Buybac
- Summary: Amentum’s board approved a $500M stock buyback, signaling confidence and potentially boosting share value.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxONDRoOVJvRTg1YUJKdEtoX2dkLUdsd05VMGhEUFB5NHJ0VU83Si1pRUpzMDVUbTNpLWFXdTI1WEFRZHB0bzdUemNzdHFmRzBBQTRCelhGb1A1S0tDbUJxeVlKaVdOZGVOWjBvYnRYaFd2TTlYUFI5WXYzdzRyeHNWcGw5VFNiSEgyb1l2Uy1CM3p3Y28tcDNyLWV3ZUd5Z1RLVjAyQkF4YUpVdUVZMkE?oc=5>

## HEADWINDS

### Amentum Holdings (AMTM) Stock Looks Cheap Despite Its 19% Slide
- Summary: Amentum Holdings (AMTM) Stock Looks Cheap Despite Its 19% Slide
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPRmVfa19mZzBnNU82UDdtd1hQY016MG1IY3I0S0Nial9zZUlFZXBOcnBSb3dxcGRsNENxZ0cwTDF4SEJnYlk0S3JUcHJ5RUNYRkEyUEZWV2txSVpGYmJDOGVma0duTzNaWFZsSXUyeW13azF2d3dBdWFqeG9ZT2hWNGZxSmJtT01rVktMNXByanNWLWh4X2F3eGprOGpweTg?oc=5>

### Amentum (AMTM) Reports Q4 Revenue Slightly Below Expectations, E
- Summary: Amentum (AMTM) Reports Q4 Revenue Slightly Below Expectations, E
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxOVkw3X3lzdWFxaGNfRmVRWUppMVJhOEs2aU5KQlJHTzdhcENzMkVpeWpSSUJPQm5JTHgtUU91TEdtMWIwc3FtTG15VWVIdXplTTZPdjFvMXFiRURZUkd4b05Ha1BLbGNsV05xRDZFWnotaDhQaU01R2pTSldUWEJzdFRhRjZCQ2V5cXZadkFGclkyMGdRa19jaFZSdlJGT0c0NDZFRG9sYmZwVGtaZ3g4NHBZb01JaXVJOUtfZGdZTGtwTnBiRzBmcDJJV1hxUQ?oc=5>

## CATALYSTS

### Amentum Holdings climbs 16% on earnings beat, buyback plan (AMTM:NYSE)
- Summary: Amentum Holdings climbs 16% on earnings beat, buyback plan (AMTM:NYSE)
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxOTXc1QWZkYVNkWFQwM0NYeWo0eXJ3c0N3RkROc2hPLUdYSVVhYW1idFB5azVSaVJYRlRJYm9RSG1pUHpWOUFRczdKZmtTd3JXcjA4TFNlY1F2ZldaYnkwWGpXb1owU0pCUGU1TFNUVURjQWFBTHlxWlRSTW4wRzBIa1JFSHIybXpvMF84NmR1MWFpd1k4T3pBWkpqUmtQSVl3R0RVVQ?oc=5>

### Amentum Stock Jumps 20% as First Buyback of Up to $500 Million Overshadows Revenue Miss
- Summary: Amentum Stock Jumps 20% as First Buyback of Up to $500 Million Overshadows Revenue Miss
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMidkFVX3lxTFBTRzJfT3N3MG00NmZXbjFZanl0TmJpRVZ1aDFjT2pSank0MENQM2puNGdJOVdrN2xPVV9sUU9UeDBkOG5SZkpMN3ZGZnRLU3hWa1ZoUDlwMFZJbEdsaUpzTkx5czYzWXRuakxCMTZLRDBodXl5T2c?oc=5>

### Amentum Holdings Stock Gains Attention After Earnings Beat And $500 Million Buyback
- Summary: Amentum Holdings Stock Gains Attention After Earnings Beat And $500 Million Buyback
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNVDVKUlFGejFqWlV1X1ptMmlFbjIyeWVlRG9MOHFsaXhiY2VWMUxGMkZ1NGpWLVhxdG8zdEVZOHJPa1Y2X1F6T3lJN1dodmFJRlBqb18xbkVMdUpoUjh6VDNSVEJJZlRHMGFYSDF4NC1PdWlIVW9BSGhJX2RkMFZucFRBVm1HUVU2aV9Bb0htZEZFckFyOFMtN1l2TFN0Y3B1ZG1YSlZ3?oc=5>

### Amentum (AMTM) Q4 Earnings: Taking a Look at Key Metrics Versus Estimates
- Summary: Amentum (AMTM) Q4 Earnings: Taking a Look at Key Metrics Versus Estimates
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNQ0hkUlFVZDk1dHNBNE9fNC0zd0c5Yl9makZZZm1vQUNHVVZocmtNbTMyVVZwX21lVThiVVhHMFFxVlZRTno4aGtYM0tuWEZoblc5UFZRRjA4Y18yZm5iOGRla0tYZnVDZDcweXVJN2hSYVFwemlIU2FITjdPM2RJZGlkRjktUzBNNy1qaUdMd3FLQldjMmp4UWdVVWQ?oc=5>

### Amentum (AMTM) Launches $500 Million Share Buyback Program Amid Mixed Valuation Signals
- Summary: Amentum (AMTM) Launches $500 Million Share Buyback Program Amid Mixed Valuation Signals
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxNV0RMVUozcDlZZ01MODlHNEZqVTZ5bnc3ZEs4ZVZMaXJwRVdKTkJjd2dwMzJzbFN6ZDZVMmRscUYzS0FMUVFLSUhqanJMREIzNmJST05BOHBhSk5ReHFVN0tSbXYwanhfVzBFUEtEbUw3YlYxYXlIV2Q0d2g0cWZWMWVveHR1UWhGQVBWTllxM2pTTmRPTmtKNEtKTkVzU2JIM0d1Z01BWXhXbFhBVGdrNmt6ZFpzMEZwSVAyTDNIUTI?oc=5>

### Amentum Holdings (AMTM) Issues Fresh Guidance And Buyback, Is It Still 15% Below Fair Value?
- Summary: Amentum releases new guidance and announces a share buyback program, potentially impacting short-term stock performance.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxNd3VWZEdRVng3V3RDUlVTVjA0b1dneklJOW85bVhwam1Ob21rZkhuSUkxQ0pVM0F0bUNDR2U2SUtGYWVHZ09WYV9WVXpRT2k4SGdMTDBvSVF4R0NPcWEyMGg3ME05TUxsaUh3aVVPM00xTE1IUnhYT2I3LUxjNjBlQ2NSWnlVRThhOVFNenZPVi00LVlGXzV4MFAwdFZ3bUF0?oc=5>

### What Amentum (AMTM) Said on Its Q4 Earnings Call
- Summary: Amentum discussed Q4 financial results and outlook.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQNHVtRkxIN25JbFV6NEpFSUJzWDNZOTlpcWV3TGI0RmN4UjZBOFBjQ2JlT0ViRGxMUG0wbUhIRjgwcGVlY01pRmFaMTQ3ZlFxYW9pLUlZYjZlUGdBWUlYY0xQZ3JBUlU4RmUtdnBuZG1tZndSUzBPS3JFRDFleEtiWWxJSHduQ1ZERnYySlVBVWZ0cUkwV3JGVjZR?oc=5>

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
| **AMTM** | **17.91** | **1.24** | **9.46** | **-7.80** | **6,049,642,496.00 USD** | **-15.75** |
| LDOS | 11.78 | 3.11 | 9.15 | 3.60 | 16,076,461,056.00 USD | -29.97 |
| CACI | 25.92 | 3.02 | 15.23 | 8.20 | 14,022,776,832.00 USD | 2.60 |
| SAIC | 17.62 | 4.42 | 11.84 | 6.30 | 6,335,760,384.00 USD | 78.84 |

Peers fetched as_of: 2026-11-27; AMTM reuses existing data (market data as_of: 2026-11-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-23
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-27

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-11-24
- Revenue (latest available single quarter): 3,490,000,000.00 USD; period 2026-04-04/2026-07-03; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 66,000,000.00 USD; period 2026-04-04/2026-07-03; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/2011286/000162828026075740/amtm-20261002.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMinwFBVV95cUxNYmthQ0g1M0FCOWt5UnpxQUpURFVsWTh2XzVCR1BIazVBVU5qQnBVdFRUMW5nVnlrMHFPTDFFRHlYSzhERE1pcXZiTGN1NFY4dGdYdXVFdzFONzl2VW5MdXlJM1ljaVRLWUJRSnZ0dlNTYldUVXppemJBVzEzMjVkNWU1ZUVUbHNvcWxaeXpWdk9xOExCTF9xenlDMzNpWDQ?oc=5
- https://news.google.com/rss/articles/CBMisAJBVV95cUxPNDB0VkswNU9EV2xVb1NzQldHNVdfWmVjVFd4c01fOUhhb2pabHQ0V0Y3OUo4dHF3cHdOTDFpb1JVd19jZWlsUVFuRUhCaGM0Y2RDdEtpdE5pRXFUMmVzUGJxZGdRbTVBd1VUajZNTlZoUnkxeVAtUGNCTnFZaENhemJ6bTZDTXNKSzJVdW5PVWhlOVdFN3V2Ny1SbnI0NWd6MFhHeC1GUUFjVEhkV2RwRjFwWnoxNFFsdmVUS2dXZEM2akdueEdOUUU5Q1VuV3lSdWRFdVRzdHhnMHdUS1U0VFJnWEh6aXpRSnhIS1RHVnhzMEZfUENwY0JOUjlYWlFLODRwUnFSNFVTWFZSR2NRS0draHIteF9FbTh1VDRmWmt2cFpfcDFNblFpU0s5Slox?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxONDRoOVJvRTg1YUJKdEtoX2dkLUdsd05VMGhEUFB5NHJ0VU83Si1pRUpzMDVUbTNpLWFXdTI1WEFRZHB0bzdUemNzdHFmRzBBQTRCelhGb1A1S0tDbUJxeVlKaVdOZGVOWjBvYnRYaFd2TTlYUFI5WXYzdzRyeHNWcGw5VFNiSEgyb1l2Uy1CM3p3Y28tcDNyLWV3ZUd5Z1RLVjAyQkF4YUpVdUVZMkE?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPRmVfa19mZzBnNU82UDdtd1hQY016MG1IY3I0S0Nial9zZUlFZXBOcnBSb3dxcGRsNENxZ0cwTDF4SEJnYlk0S3JUcHJ5RUNYRkEyUEZWV2txSVpGYmJDOGVma0duTzNaWFZsSXUyeW13azF2d3dBdWFqeG9ZT2hWNGZxSmJtT01rVktMNXByanNWLWh4X2F3eGprOGpweTg?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxOVkw3X3lzdWFxaGNfRmVRWUppMVJhOEs2aU5KQlJHTzdhcENzMkVpeWpSSUJPQm5JTHgtUU91TEdtMWIwc3FtTG15VWVIdXplTTZPdjFvMXFiRURZUkd4b05Ha1BLbGNsV05xRDZFWnotaDhQaU01R2pTSldUWEJzdFRhRjZCQ2V5cXZadkFGclkyMGdRa19jaFZSdlJGT0c0NDZFRG9sYmZwVGtaZ3g4NHBZb01JaXVJOUtfZGdZTGtwTnBiRzBmcDJJV1hxUQ?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxOTXc1QWZkYVNkWFQwM0NYeWo0eXJ3c0N3RkROc2hPLUdYSVVhYW1idFB5azVSaVJYRlRJYm9RSG1pUHpWOUFRczdKZmtTd3JXcjA4TFNlY1F2ZldaYnkwWGpXb1owU0pCUGU1TFNUVURjQWFBTHlxWlRSTW4wRzBIa1JFSHIybXpvMF84NmR1MWFpd1k4T3pBWkpqUmtQSVl3R0RVVQ?oc=5
- https://news.google.com/rss/articles/CBMidkFVX3lxTFBTRzJfT3N3MG00NmZXbjFZanl0TmJpRVZ1aDFjT2pSank0MENQM2puNGdJOVdrN2xPVV9sUU9UeDBkOG5SZkpMN3ZGZnRLU3hWa1ZoUDlwMFZJbEdsaUpzTkx5czYzWXRuakxCMTZLRDBodXl5T2c?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNVDVKUlFGejFqWlV1X1ptMmlFbjIyeWVlRG9MOHFsaXhiY2VWMUxGMkZ1NGpWLVhxdG8zdEVZOHJPa1Y2X1F6T3lJN1dodmFJRlBqb18xbkVMdUpoUjh6VDNSVEJJZlRHMGFYSDF4NC1PdWlIVW9BSGhJX2RkMFZucFRBVm1HUVU2aV9Bb0htZEZFckFyOFMtN1l2TFN0Y3B1ZG1YSlZ3?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNQ0hkUlFVZDk1dHNBNE9fNC0zd0c5Yl9makZZZm1vQUNHVVZocmtNbTMyVVZwX21lVThiVVhHMFFxVlZRTno4aGtYM0tuWEZoblc5UFZRRjA4Y18yZm5iOGRla0tYZnVDZDcweXVJN2hSYVFwemlIU2FITjdPM2RJZGlkRjktUzBNNy1qaUdMd3FLQldjMmp4UWdVVWQ?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxNV0RMVUozcDlZZ01MODlHNEZqVTZ5bnc3ZEs4ZVZMaXJwRVdKTkJjd2dwMzJzbFN6ZDZVMmRscUYzS0FMUVFLSUhqanJMREIzNmJST05BOHBhSk5ReHFVN0tSbXYwanhfVzBFUEtEbUw3YlYxYXlIV2Q0d2g0cWZWMWVveHR1UWhGQVBWTllxM2pTTmRPTmtKNEtKTkVzU2JIM0d1Z01BWXhXbFhBVGdrNmt6ZFpzMEZwSVAyTDNIUTI?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxNd3VWZEdRVng3V3RDUlVTVjA0b1dneklJOW85bVhwam1Ob21rZkhuSUkxQ0pVM0F0bUNDR2U2SUtGYWVHZ09WYV9WVXpRT2k4SGdMTDBvSVF4R0NPcWEyMGg3ME05TUxsaUh3aVVPM00xTE1IUnhYT2I3LUxjNjBlQ2NSWnlVRThhOVFNenZPVi00LVlGXzV4MFAwdFZ3bUF0?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQNHVtRkxIN25JbFV6NEpFSUJzWDNZOTlpcWV3TGI0RmN4UjZBOFBjQ2JlT0ViRGxMUG0wbUhIRjgwcGVlY01pRmFaMTQ3ZlFxYW9pLUlZYjZlUGdBWUlYY0xQZ3JBUlU4RmUtdnBuZG1tZndSUzBPS3JFRDFleEtiWWxJSHduQ1ZERnYySlVBVWZ0cUkwV3JGVjZR?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxOUl9zYXkyLTBBUVpHQ3A3TGY1YmNJNjdWRWNZcEpfRGZ6SlNZLU1kcTZLZ0pVQkxGSG9RSXlhR3pMdWZIdW10MVdnUmpQQ2NsbDhWSGYyTm42WEFUNVE3UWhNTHR1LUVQVUdVc0NlQ01wMElwTU9SdnR4dFA2MjUya2l2al9aV25rQzZva1ozcklUVjZ0aThpSzBuSktVOWE3enRCRQ?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxPSklRUUE2RmlwVmlFNndVSlg5YUNtRUVQMmdXSzNhRV96V2haN2ZBb19JdWNLeU8zVjMwdGYwaHkxdm0wQnp2ekF1U0ZrSkxBVEp1XzNVRU5SMjY3UUhHNWdJRWVDOUhkMVFUeDZGU2lzMHpBc3ZFNTBUOHVsMFJISWVLWVJRUDZ1dTZ5YUFhSFc1Z0tTTWZKZU1hZ0t2QUNFcnJmbXhaUXBJQmIzUmc?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
