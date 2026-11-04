# PEP Intelligence Report

- ticker: **PEP**
- Report as_of: **2026-11-03**
- Market data as_of: **2026-11-03**
- Quant sources: https://finance.yahoo.com/quote/PEP/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/PEP/key-statistics/
- AI analysis snapshot as_of: **2026-11-03**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-04T05:07:02.622514+00:00**
- AI status: **Partial: 1 headline remains unclassified and excluded from research conclusions**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 18, 'rule': 6, 'ai': 7, 'unknown': 1, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261103T051441Z-8b1c85d8/PEP** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'positive_sentiment_in_headwinds': 1}
- RSS source audit (metadata only, not article fact-checking): 18 unique headlines; 6 named publishers; 2 exact duplicates; 18 HTTPS source links; largest publisher share 27.78%; oldest publication 2026-10-27

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 137.2700 |
| Return 1D (%) | -2.2433 |
| Return 1W (%) | 2.8240 |
| Return 1M (%) | 9.0396 |
| Return YTD (%) | -1.4433 |
| Return 1Y (%) | -0.5347 |
| Annualized volatility (%) | 21.3022 |
| Beta vs SPY | -0.2498 |
| Max drawdown (%) | -25.2176 |
| Sharpe (rf=0) | 0.0805 |
| Downside deviation (rf=0, %) | 14.3092 |
| Sortino (rf=0) | 0.1199 |
| Historical VaR 95% (1D, %) | 2.1996 |
| Historical ES 95% (1D, %) | 2.6412 |
| Correlation vs SPY | -0.1501 |
| Tracking error vs SPY (%) | 26.4467 |
| P/E (trailing) | 17.67 |
| P/B | 8.40 |
| EV/EBITDA | 11.89 |
| Revenue growth (%) | 5.60 |
| Forward P/E (estimate) | 15.89 |
| Gross margin (%) | 54.33 |
| Operating margin (%) | 16.88 |
| Return on equity (%) | 52.19 |
| Free cash flow yield (%) | 4.83 |
| MA50 | 133.0462 |
| Close vs MA50 (%) | 3.1747 |
| MA200 | 143.6767 |
| Close vs MA200 (%) | -4.4591 |
| RSI (14, Wilder) | 58.1125 |
| MACD (12,26) | 1.7211 |
| MACD signal (9) | 0.9328 |
| MACD histogram | 0.7883 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'PEP': 274, 'SPY': 274}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 137.2700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.2433 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.8240 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 9.0396 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -1.4433 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -0.5347 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 21.3022 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.3092 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.1199 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.1996 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.6412 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1501 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.4467 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.2498 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -25.2176 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.0805 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.8899 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.3270 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 16.8830 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 52.1870 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.8349 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 17.6667 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 58.1125 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.7883 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 3.1747 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -4.4591 -> Slightly below the moving-average trend level.

## TAILWINDS

### PepsiCo (NASDAQ:PEP) Stock Price Up 2.2% - What's Next?
- Summary: PepsiCo (NASDAQ:PEP) Stock Price Up 2.2% - What's Next?
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxOX0V0QmNORTZKUmdFaW93WUdXYURCLVhQSkxjNlIxOEQ1SEdOQnRoZjRsOXRZeWtWMmVja3AwaF9yUmpPc2Z2dGxCWFFUMS1mTUo0SHdsVkxNQkl5WUtCVHF2WEU1QmkwVDMzODZxWmhvU0JudUp0LXl1Z0FCYW9jY01QejhyZzN1QkJzS1ZvN0duTm41UkljMi12ajhfbUpoRW1XbXMyLVVXZ1U?oc=5>

### Is PepsiCo Stock Stronger Than It Looks?
- Summary: Questioning PepsiCo’s stock strength suggests potential undervaluation and future upside for investors.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQdGI1al9tWm5HV2dzcWcxOWtxbWg5Rm9rMlFSWldnZG9tb3Nib2VNZXAxa0RXVVlxcnp3am9DN1J6TmFYNzBVazVaUmh0cnAyZlJSVWRyNVhuVHhpaXJKVURfWGllQjVmZnhhM09OUkVVdTFHWDBfcmIxRUIwd0FKNTFiNV9fZ2VQU2NGcncyYnRCV2dsNTQyQ1E4RVI3UUxS?oc=5>

### Coca-Cola Yields Just 2.2% Compared to 4.3% for PepsiCo. Here's the Better Dividend King Stock for Generating Long-Term Passive Income.
- Summary: PepsiCo offers a higher dividend yield than Coca-Cola, positioning it as a more attractive income stock for long-term investors.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxON0NhSHRndFp3TWVQZlFmNWU2Yy13LThiTmd5OUdqRFllLTI1UXR0aEJBVVhXeVVmSDlTb0F4M19lR3prYVVvRHFpZGh0OXNGbk9Qc01FRWIybVJyTFhpMlJwa1YxUUpZQmVKSnl5ZG1lRTYwQUoyY0I0QTNMTG92Z3hndmFZbUZ3dGdiUnRCdlJ5Z1E?oc=5>

### What Is PepsiCo (PEP) Gaining From Its Expanded Beverage Partnership?
- Summary: PepsiCo benefits from a new beverage partnership, potentially boosting product reach and revenue.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPQ3hPZnVmajhPcHpxbFhNU1VsOW53aHFQN0JreWVWRncwR2Q3c3g3aXVJQ2dOZjluZDBHQ1l0cXRKWXlyRzB2QnQwYlFnSml6YjRqYW5paHdodllxbzdVMkJUclVpbVFXVmN1RERoaWFxZ3hDVkx1T1prNmIzX05HS1JvWEZQOWtuZlRBZVp4M29YeUpKSE5FYzZhS0tfdlV6NjFlRw?oc=5>

## HEADWINDS

### PepsiCo (NASDAQ:PEP) Shares Down 2.2% - What's Next?
- Summary: PepsiCo (NASDAQ:PEP) Shares Down 2.2% - What's Next?
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxPSTIwYkc5R3VLa295NE1GM2VxdE45cXowaHBCRjFUOGtlZWc4WU50OHVyem4yNEN3cFplWlpkS1FxWHNJTXdUT3BuNnRrMlNKSnRrUXFoSzVvcHBXUHM5VjZ1SHlYb2dNYU1PVEFqclZLVzFJZnBSTjltNE8yaWpHcnI4dWh4TVNEN2IyLVUtV2xHUDdhaU82SDNlZW1IUWVaQnBENWZXdw?oc=5>

### How Did Coca-Cola Stock Leave PepsiCo Behind?
- Summary: PepsiCo stock lagged behind Coca-Cola, indicating weaker market performance.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxObFVqeTlwMWlvWTI0bi1uT0EyZFRZNzQtUUVoUWE1ZHVtQXZKSDMweUxtRVJDeHktQUFEVU1zTV84VndmUnU5M3FtZVExTlhPSlNnZXZweDVINURLcDhFWnRhM0plS2ktTEFPYTMyaFN0NldmVkRGckcyTGhOLXhpZndBOXZWYWJ4bnlNa0V1NUhRdk1WWkx2MW9STlgzWVZxRG9wWTlTWQ?oc=5>

### Why Is PepsiCo Stock Falling, and Is It a Buying Opportunity?
- Summary: PepsiCo shares declined, raising concerns about short-term valuation.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxQZnptbTE5THpPQURPOTIwZEhMbTdLdjg2RTl6Skd5LUo4MjBfU04xNi13dDdCSEViOU1xV2laWmpzdGNrU3d0aVg2UV9MYmxINm1XVUs4NmFLNEhMdTczX185N3RCU0I3dDhTREtxVGlnNHpSVjRMajhmamw5ZHhVTmpHUm51VFU2LVdWRk1aZV8?oc=5>

### Why PepsiCo (PEP) Stock Is Up Today
- Summary: PepsiCo shares rose today, reflecting positive market sentiment.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMifEFVX3lxTE11WUN4TGlJNGpMSmo2NmVfelgxTGdHb0paSnNUQWdhTi1sVHdUUzByYTJZNHlFci0wdTNDenR6Rk04RnlNTkJNTlNueGZTaElZMFlYUlpUSTVJczJUMVl5NGxLWVVCcWZiTUlsT0RfaXFFNFVCaXZRRmdaVzE?oc=5>

## CATALYSTS

### PepsiCo Remains a Popular Choice for Dividend Investors
- Summary: PepsiCo Remains a Popular Choice for Dividend Investors
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxQcDl3MFM0YUd4eFlzVVVlRjJQVG9ocjlRMFFNcEEwTFJ3Z2MtNVdqWXoxOWI1ZElrQW5oYlVUdHpJT3FYclNmejQ2MndrYy1PSnZaQVhubHdOVE5pbkZRTlNraTQ4RnhnczNUODlGUW5yWWxvLWRVWks4ZF92LWc5ZW10SjN5UFNXWjhQOEEyUThBRmMweGY2bHQ1OEtKX25FWGtGamhkZw?oc=5>

### PepsiCo, Inc. $PEP Stock Sold by Summit Global Investments
- Summary: PepsiCo, Inc. $PEP Stock Sold by Summit Global Investments
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxOUlVzM3l5ejBhRmxQcXhNaGp0UGQ5T0Y1VWJKVk5VZE9sa3lvNno4V1BNZFBIS1pYdkhEb1dydEY4cUhnR2VXOS00QlZ3eHFubVZ1eHhJSGJWdmswU2FQT0xQZmxaWXdZT3p3eXY0THVER0djWU9LSWJZZlJkdC1OV3RPYVI5X1RoY1A5SF9YN0cxcnhvdlp0RDNrSHlXTXdCR2pYd2h6SkZvUXRpNWFybDU4OXZMU28?oc=5>

### PepsiCo Hasn't Been This Cheap Relative to Earnings in 6 Years. Here's Why That's the Signal to Buy.
- Summary: PepsiCo Hasn't Been This Cheap Relative to Earnings in 6 Years. Here's Why That's the Signal to Buy.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPMklRamY4NTlwSXBhcnNLbjVrWjU0VnVPYTc3WG9NY1NianJJZVN4b2JRWmpHcktGYm5rVHJiU3h6dk9DTVhqLTVleEd3LTZqWmozQlQ2WWxsYkc3d2piTVVfel9VMF9qdjA3YmNveTdKRVlyOFc0TDk3cDMxSnZudEU3SzRKdG92UE16ZVNHYlUxTFB4N3Uw?oc=5>

### PepsiCo, Inc. $PEP Stock Sold by Heritage Investors Management Corp
- Summary: PepsiCo, Inc. $PEP Stock Sold by Heritage Investors Management Corp
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxQdzQzOGNNVGNELW5xaXFyLWw5Q1gydHdJcG5mRFFGemIxV2hzSk9tekZlMmlHNEM1REhsbkM0ZG5jczZBbDktaEsxMERhbDR5Ym15cjNhTFNmLV90QVo4all0OEFJMjdiUDBWMllNajFFQzJqNUpCbTA5M0pZOUhKYlRUVTNRcjRLSVZEMWRoS3pYSl9faHhmLTlrYVJhUEFlcGt1TXJZUDVGOHBmSGd5bng5YTl0dmlkamIzX3NOZkZ1Z3c?oc=5>

### PepsiCo, Inc. $PEP Stake Increased by GRIMES & Co WEALTH MANAGEMENT LLC
- Summary: Wealth management firm GRIMES & Co increases stake in PepsiCo.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxNZW4wd3l5dE9GbUVIWktOLXlLR292MDM3OUpDTXNILWJvZlZtcnhzVU9zTEppU1Z2RndqMGVJdWtaTG9fWjFLc0REV3VHRzV0SUUxUU9fUEhKSUZIekFBd2tBZzJiTHVLQVpQV3lIX2g1S3FfUXFIYmZTUWZQUnJqQ0tRS21uMWJJWUF4cDNjQlVUUF9VYWNXTnBkODNJaFhfalpEa19SWXBYV1YzVFV5Rm5zTDVkVS04RFE0Uy1iZmZia0VBUlE?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **PEP** | **17.67** | **8.40** | **11.89** | **5.60** | **187,063,484,416.00 USD** | **-0.53** |
| KO | 28.30 | 10.91 | 24.99 | 7.40 | 407,820,369,920.00 USD | 43.18 |
| MNST | 44.51 | 9.87 | 30.38 | 20.20 | 92,428,066,816.00 USD | 41.87 |
| KDP | 37.35 | 1.85 | 18.28 | 75.60 | 47,275,098,112.00 USD | 34.56 |

Peers fetched as_of: 2026-11-03; PEP reuses existing data (market data as_of: 2026-11-03); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-08
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-03

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-08
- Revenue (latest available single quarter): 25,274,000,000.00 USD; period 2026-06-14/2026-09-05; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 3,048,000,000.00 USD; period 2026-06-14/2026-09-05; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/77476/000007747626000048/pep-20260905.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiqwFBVV95cUxOX0V0QmNORTZKUmdFaW93WUdXYURCLVhQSkxjNlIxOEQ1SEdOQnRoZjRsOXRZeWtWMmVja3AwaF9yUmpPc2Z2dGxCWFFUMS1mTUo0SHdsVkxNQkl5WUtCVHF2WEU1QmkwVDMzODZxWmhvU0JudUp0LXl1Z0FCYW9jY01QejhyZzN1QkJzS1ZvN0duTm41UkljMi12ajhfbUpoRW1XbXMyLVVXZ1U?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQdGI1al9tWm5HV2dzcWcxOWtxbWg5Rm9rMlFSWldnZG9tb3Nib2VNZXAxa0RXVVlxcnp3am9DN1J6TmFYNzBVazVaUmh0cnAyZlJSVWRyNVhuVHhpaXJKVURfWGllQjVmZnhhM09OUkVVdTFHWDBfcmIxRUIwd0FKNTFiNV9fZ2VQU2NGcncyYnRCV2dsNTQyQ1E4RVI3UUxS?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxON0NhSHRndFp3TWVQZlFmNWU2Yy13LThiTmd5OUdqRFllLTI1UXR0aEJBVVhXeVVmSDlTb0F4M19lR3prYVVvRHFpZGh0OXNGbk9Qc01FRWIybVJyTFhpMlJwa1YxUUpZQmVKSnl5ZG1lRTYwQUoyY0I0QTNMTG92Z3hndmFZbUZ3dGdiUnRCdlJ5Z1E?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPQ3hPZnVmajhPcHpxbFhNU1VsOW53aHFQN0JreWVWRncwR2Q3c3g3aXVJQ2dOZjluZDBHQ1l0cXRKWXlyRzB2QnQwYlFnSml6YjRqYW5paHdodllxbzdVMkJUclVpbVFXVmN1RERoaWFxZ3hDVkx1T1prNmIzX05HS1JvWEZQOWtuZlRBZVp4M29YeUpKSE5FYzZhS0tfdlV6NjFlRw?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPSTIwYkc5R3VLa295NE1GM2VxdE45cXowaHBCRjFUOGtlZWc4WU50OHVyem4yNEN3cFplWlpkS1FxWHNJTXdUT3BuNnRrMlNKSnRrUXFoSzVvcHBXUHM5VjZ1SHlYb2dNYU1PVEFqclZLVzFJZnBSTjltNE8yaWpHcnI4dWh4TVNEN2IyLVUtV2xHUDdhaU82SDNlZW1IUWVaQnBENWZXdw?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxObFVqeTlwMWlvWTI0bi1uT0EyZFRZNzQtUUVoUWE1ZHVtQXZKSDMweUxtRVJDeHktQUFEVU1zTV84VndmUnU5M3FtZVExTlhPSlNnZXZweDVINURLcDhFWnRhM0plS2ktTEFPYTMyaFN0NldmVkRGckcyTGhOLXhpZndBOXZWYWJ4bnlNa0V1NUhRdk1WWkx2MW9STlgzWVZxRG9wWTlTWQ?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxQZnptbTE5THpPQURPOTIwZEhMbTdLdjg2RTl6Skd5LUo4MjBfU04xNi13dDdCSEViOU1xV2laWmpzdGNrU3d0aVg2UV9MYmxINm1XVUs4NmFLNEhMdTczX185N3RCU0I3dDhTREtxVGlnNHpSVjRMajhmamw5ZHhVTmpHUm51VFU2LVdWRk1aZV8?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQZ3pMSk05S3QyZ2QyMkpGOUZ4VjlaMmtxV3BZVVBHTE13Z2xLcUI2WTYzS2xOeHk3WW5pcV9SQVoyLVQ2Zm5CaXdqQmJhaWdMRWFFUGhNR0hQOEdzbHZtMFRIX1Q5VFhYdDJiRS05SWdLLU5jVjlzbk9rWFpIaTYwQzlMdzFkTlBYdFpMR08tSXotTjFJd2xkeWVRTTVkdw?oc=5
- https://news.google.com/rss/articles/CBMifEFVX3lxTE11WUN4TGlJNGpMSmo2NmVfelgxTGdHb0paSnNUQWdhTi1sVHdUUzByYTJZNHlFci0wdTNDenR6Rk04RnlNTkJNTlNueGZTaElZMFlYUlpUSTVJczJUMVl5NGxLWVVCcWZiTUlsT0RfaXFFNFVCaXZRRmdaVzE?oc=5
- https://news.google.com/rss/articles/CBMid0FVX3lxTE5kTDdJNXFzYXQ5Q0JOTFBTb0Jva2JaMlBJWGZVaWV4ckxjSEpJQy0tMjVCV0tzanhsTDVrRUFOOU9UQTNXQ2o4VTJTcFJYaE9uTHBVYUNYM2FHY0wydDV2MUE0MHNWVVUzd1E2Y042Y3dzSm9jR1h3?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxQcDl3MFM0YUd4eFlzVVVlRjJQVG9ocjlRMFFNcEEwTFJ3Z2MtNVdqWXoxOWI1ZElrQW5oYlVUdHpJT3FYclNmejQ2MndrYy1PSnZaQVhubHdOVE5pbkZRTlNraTQ4RnhnczNUODlGUW5yWWxvLWRVWks4ZF92LWc5ZW10SjN5UFNXWjhQOEEyUThBRmMweGY2bHQ1OEtKX25FWGtGamhkZw?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxOUlVzM3l5ejBhRmxQcXhNaGp0UGQ5T0Y1VWJKVk5VZE9sa3lvNno4V1BNZFBIS1pYdkhEb1dydEY4cUhnR2VXOS00QlZ3eHFubVZ1eHhJSGJWdmswU2FQT0xQZmxaWXdZT3p3eXY0THVER0djWU9LSWJZZlJkdC1OV3RPYVI5X1RoY1A5SF9YN0cxcnhvdlp0RDNrSHlXTXdCR2pYd2h6SkZvUXRpNWFybDU4OXZMU28?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPMklRamY4NTlwSXBhcnNLbjVrWjU0VnVPYTc3WG9NY1NianJJZVN4b2JRWmpHcktGYm5rVHJiU3h6dk9DTVhqLTVleEd3LTZqWmozQlQ2WWxsYkc3d2piTVVfel9VMF9qdjA3YmNveTdKRVlyOFc0TDk3cDMxSnZudEU3SzRKdG92UE16ZVNHYlUxTFB4N3Uw?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxQdzQzOGNNVGNELW5xaXFyLWw5Q1gydHdJcG5mRFFGemIxV2hzSk9tekZlMmlHNEM1REhsbkM0ZG5jczZBbDktaEsxMERhbDR5Ym15cjNhTFNmLV90QVo4all0OEFJMjdiUDBWMllNajFFQzJqNUpCbTA5M0pZOUhKYlRUVTNRcjRLSVZEMWRoS3pYSl9faHhmLTlrYVJhUEFlcGt1TXJZUDVGOHBmSGd5bng5YTl0dmlkamIzX3NOZkZ1Z3c?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxNZW4wd3l5dE9GbUVIWktOLXlLR292MDM3OUpDTXNILWJvZlZtcnhzVU9zTEppU1Z2RndqMGVJdWtaTG9fWjFLc0REV3VHRzV0SUUxUU9fUEhKSUZIekFBd2tBZzJiTHVLQVpQV3lIX2g1S3FfUXFIYmZTUWZQUnJqQ0tRS21uMWJJWUF4cDNjQlVUUF9VYWNXTnBkODNJaFhfalpEa19SWXBYV1YzVFV5Rm5zTDVkVS04RFE0Uy1iZmZia0VBUlE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
