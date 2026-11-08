# PEP Intelligence Report

- ticker: **PEP**
- Report as_of: **2026-11-07**
- Market data as_of: **2026-11-06**
- Quant sources: https://finance.yahoo.com/quote/PEP/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/PEP/key-statistics/
- AI analysis snapshot as_of: **2026-11-07**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-08T04:19:26.159845+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 8, 'ai': 6, 'unknown': 0, 'irrelevant': 11})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261106T045829Z-1db1e5a7/PEP** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 11 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 36.0%; oldest publication 2026-11-01

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 141.3400 |
| Return 1D (%) | -0.9600 |
| Return 1W (%) | 2.9125 |
| Return 1M (%) | 12.4334 |
| Return YTD (%) | 1.4789 |
| Return 1Y (%) | 3.8756 |
| Annualized volatility (%) | 21.6276 |
| Beta vs SPY | -0.2049 |
| Max drawdown (%) | -25.2176 |
| Sharpe (rf=0) | 0.2839 |
| Downside deviation (rf=0, %) | 14.3050 |
| Sortino (rf=0) | 0.4292 |
| Historical VaR 95% (1D, %) | 2.1996 |
| Historical ES 95% (1D, %) | 2.6412 |
| Correlation vs SPY | -0.1284 |
| Tracking error vs SPY (%) | 26.9554 |
| P/E (trailing) | 17.78 |
| P/B | 8.65 |
| EV/EBITDA | 12.18 |
| Revenue growth (%) | 5.60 |
| Forward P/E (estimate) | 16.36 |
| Gross margin (%) | 54.33 |
| Operating margin (%) | 16.88 |
| Return on equity (%) | 52.19 |
| Free cash flow yield (%) | 4.70 |
| MA50 | 133.1817 |
| Close vs MA50 (%) | 6.1257 |
| MA200 | 143.6799 |
| Close vs MA200 (%) | -1.6285 |
| RSI (14, Wilder) | 62.5182 |
| MACD (12,26) | 2.6650 |
| MACD signal (9) | 1.6931 |
| MACD histogram | 0.9719 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'PEP': 277, 'SPY': 277}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 141.3400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.9600 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.9125 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 12.4334 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 1.4789 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 3.8756 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 21.6276 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.3050 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4292 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.1996 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.6412 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1284 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.9554 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.2049 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -25.2176 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2839 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.3610 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.3270 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 16.8830 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 52.1870 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.6956 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 17.7786 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 62.5182 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.9719 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 6.1257 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -1.6285 -> Slightly below the moving-average trend level.

## TAILWINDS

### PepsiCo (NASDAQ:PEP) Stock Price Up 2.2% - What's Next?
- Summary: PepsiCo (NASDAQ:PEP) Stock Price Up 2.2% - What's Next?
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxOX0V0QmNORTZKUmdFaW93WUdXYURCLVhQSkxjNlIxOEQ1SEdOQnRoZjRsOXRZeWtWMmVja3AwaF9yUmpPc2Z2dGxCWFFUMS1mTUo0SHdsVkxNQkl5WUtCVHF2WEU1QmkwVDMzODZxWmhvU0JudUp0LXl1Z0FCYW9jY01QejhyZzN1QkJzS1ZvN0duTm41UkljMi12ajhfbUpoRW1XbXMyLVVXZ1U?oc=5>

### What Is PepsiCo (PEP) Gaining From Its Expanded Beverage Partnership?
- Summary: PepsiCo expands beverage partnership, potentially boosting product mix and market reach.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPQ3hPZnVmajhPcHpxbFhNU1VsOW53aHFQN0JreWVWRncwR2Q3c3g3aXVJQ2dOZjluZDBHQ1l0cXRKWXlyRzB2QnQwYlFnSml6YjRqYW5paHdodllxbzdVMkJUclVpbVFXVmN1RERoaWFxZ3hDVkx1T1prNmIzX05HS1JvWEZQOWtuZlRBZVp4M29YeUpKSE5FYzZhS0tfdlV6NjFlRw?oc=5>

## HEADWINDS

### PepsiCo Lowers 2026 EPS Outlook as North America Pressures Margins
- Summary: PepsiCo Lowers 2026 EPS Outlook as North America Pressures Margins
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxPNkdqTmktOGdTWVVWUFowZnVxYzkxNG5jMjd5MzQ4aWJoRXQ1QnZZVVcwaE94NVJuLVZRT2xsQV9GZUNXc3FsWUxmUVdQamJfTzJ1RnYxU3hRSEdtSUJQQnY0dERvc3hWMzM3cVFpd3E2Z2VkS2ktV2xIdkdoUVZGNEVSU29iTlFudTZjLXJsQi1uLVY3SF90OHlLS2tXeDJNdzUwZFlJMWdsbW9rNkNlYUxkdFd0cDI3YXQ2Z3NGRQ?oc=5>

## CATALYSTS

### PepsiCo Extends KFC Beverage Partnership Across Eight International Markets
- Summary: PepsiCo Extends KFC Beverage Partnership Across Eight International Markets
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxOaFJTajBVaXltQzNFcXlnSVl2V1Z5R0hVcDJPVjVHYUhibVhHR3UwRV9hOXV6MzN3bFZhazE2Z0Y2c0dHVVJsUHFPaGpvcFlHbjMzMk5tUmRZMDFERFV3ODZXVzRqNVZlb2diU2lnR0dGenY3RzJYTmc3ZHBvdGtadWZ5SjZBUVZGUjRaamxkMjlLOG5SYWJORWxiWlZOSGVTcmRBWm1fX2g?oc=5>

### PepsiCo Remains a Popular Choice for Dividend Investors
- Summary: PepsiCo Remains a Popular Choice for Dividend Investors
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxQcDl3MFM0YUd4eFlzVVVlRjJQVG9ocjlRMFFNcEEwTFJ3Z2MtNVdqWXoxOWI1ZElrQW5oYlVUdHpJT3FYclNmejQ2MndrYy1PSnZaQVhubHdOVE5pbkZRTlNraTQ4RnhnczNUODlGUW5yWWxvLWRVWks4ZF92LWc5ZW10SjN5UFNXWjhQOEEyUThBRmMweGY2bHQ1OEtKX25FWGtGamhkZw?oc=5>

### PepsiCo, Inc. $PEP Shares Purchased by Kestra Advisory Services LLC
- Summary: PepsiCo, Inc. $PEP Shares Purchased by Kestra Advisory Services LLC
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxQY3UwclhpOC1JcmVTRU0zM3doSWx6bFR3QlhCc0lPMjF4Z0VBSkRVV3BJR2swTU1QMHE0WnI4Q2tva2MzSldTZjI0VXBVd0ZoR2RqQ1lCVm52bWZUNnhiVG5TUnliLXE4TzhKS1RmNlFkWW1LUFQ0eWxFN0hhTW5DMEp3MFFzN25pUUhXYWFNVW9wU1NOZ2szb0lzZG52RlkyT2ZPdXo2UzFNMFY4RXU5Mk12ZTlrR0w5X0tGOGt4Vk5MRDA?oc=5>

### PepsiCo, Inc. $PEP Stock: Lindsell Train Ltd Reduces Stake
- Summary: PepsiCo, Inc. $PEP Stock: Lindsell Train Ltd Reduces Stake
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxQeGY2TmxKcm1TWXpkcDA0NDMwS0xmMzd4WmxsdURQVTFxT2lZOXF3Z1JvMEhyc2g1aGZvQ09rRHFPZGhiQUpTWG81MHcwd2ptRGp6bzdUd0NPaWZYUHJfUjE5em05NXN3V1lLSHBlVFdydlAxX3hnRlZoa3RNQVkzaEVjVllQZ19aZXBzSkFnRHNlT2pnU3AwZG56WFZhMldUZWZvMENGN3VPd1Z2S1B1TTYzckQ4Zw?oc=5>

### PepsiCo, Inc. $PEP Stock Sold by Heritage Investors Management Corp
- Summary: PepsiCo, Inc. $PEP Stock Sold by Heritage Investors Management Corp
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxQdzQzOGNNVGNELW5xaXFyLWw5Q1gydHdJcG5mRFFGemIxV2hzSk9tekZlMmlHNEM1REhsbkM0ZG5jczZBbDktaEsxMERhbDR5Ym15cjNhTFNmLV90QVo4all0OEFJMjdiUDBWMllNajFFQzJqNUpCbTA5M0pZOUhKYlRUVTNRcjRLSVZEMWRoS3pYSl9faHhmLTlrYVJhUEFlcGt1TXJZUDVGOHBmSGd5bng5YTl0dmlkamIzX3NOZkZ1Z3c?oc=5>

### PepsiCo, Inc. $PEP Shares Purchased by Rakuten Investment Management Inc.
- Summary: PepsiCo, Inc. $PEP Shares Purchased by Rakuten Investment Management Inc.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxQMmxVNWNDZTBfRmhMbzVaY2RJalkyQXhLT21scUM1d19fNFQyenVwVEZvTW0weVVOQ3FRNzVjN1VueGxZUThrdVBSd2dhNlJGU29mdUZBS2xCOXpNOUgtQUVLd0ZPeG9GaDE5emtkODZIN21nY0VVUXYxM1NBWE4zUS1KcHhjWkRmVVNkTDd4MDh3UUVFRm0xaGgxTUpnNDVBQ2R2azdNM25ZQVRzRGNJeGl6eDc3aWk4NXFXa0pLanhaSW96Q1ZTelNB?oc=5>

### PepsiCo: 4.2% Yield And 53 Years Of Dividend Growth In An Anti-Bubble (NASDAQ:PEP)
- Summary: PepsiCo reports a 4.2% dividend yield with a 53‑year growth record, reinforcing its dividend stability.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxOazFqTmZsZE5RUVNybUtpYXRFekhRNV9hc3RvREdkdnhLZGJjQ3d5ekZGbmw1dlNLaXpyNU42QjAtUGRKcWNrVUFfT284OFBtcTJjeEZqWGRjSzdrS2k1a0l2b21FbUkxaWtvWnBRbEJNQUNSUDVEUUd3dlM3cVgxM2RyTzlRcG1BbTZ0eWJxVVI5R0xHZmlUNVhuRXVBUTFLV2IxZW9EVmRZNnJFNWVkMzNhdFo?oc=5>

### Can PepsiCo's Snack Pricing Strategy Drive Volume Growth?
- Summary: Explores how PepsiCo’s snack pricing could boost sales volume, indicating potential product strategy impact.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxPcENldTM3SHJHWmxTcnVFSXBrQVJnQl82S0UxWnBGajZscWNFenRTSWJoVGhZdHZoSjFPb0djcVRsMlJ1QThwcmN2anEyVUZFaEItR2RRQmcxLW5RSVVkNnhnWXNEbDJKc1BXdENKRk5OdC1xUGZMTnhISWNqRXNZdEpOVUh6MzlSd3JuYkRVRGZpcTBudmNGWnAzYTNNVWZCcGFFR29LbEh1enV5bTNIMWdB?oc=5>

### KFC pairs chicken tenders with Doritos on select menus as PepsiCo renews its drink deal in 8 countries.
- Summary: PepsiCo renews its drink partnership with KFC in eight countries, pairing drinks with new menu items.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxNMWdkU0gzZGtHMzFwQUxfZ1VrRjdfQXctbnlleE1JMkJGQ1lFeWZfVUZrOTVLbmhTYW5DVklLVEU3MUVJdWxKRXQzdDVsOFRPenRRWFByM211SWQ5TzhuRFlvdmJiRWc5WXZTUElWZzVRbzg0N0dGVTlzU3V6OW5peDZkUTlPTlRCaDBFZGxUWmZHSVIwT2Mzd0J4TFoyZHptSzJ4R09nZndHeWRpUGJj?oc=5>

### What PepsiCo (PEP)'s Taco Bell Renewal Means For Shareholders
- Summary: PepsiCo renews its partnership with Taco Bell, potentially boosting brand synergy and shareholder value.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxQUHJLQXc1b2xhR28yWV8zb1NwM0FpVFJKbEpJY083T2w2OXU2WENIX0R4UG1PUTdtMFkzWnkxMldNb04wOWNIWXJNR1I3UnRoSmZaeWIxQ0I0NGwzcHV1U0R2S0pEZFFDX3pGbHZKb0lCM1VrcGcwMmloUmxJNUJVcUJvOGQ4ckZaLUtYdV96SmpfbXdWcWxxNG9UTFU1c2NjLUVCSXVReXRObXRlLWJfOWM1STB5dG80XzROYnlMcy1uaE42SEtaLTNhX1NHYnV5dEHSAdcBQVVfeXFMT1U0LTFBdUZIelU2SU5xTzZJdGt2Yy12bDZfNVZBREROekx4dnd2Y0p2MmkyVUFRSjVHMUpzLWZrQXVoZEJtaEpOMFlfNWxta3dqMk5JcF9yTlFTQnNIUE5FRDYtWXdYS3ZfcnNsU21veEVKNzJxbTNQY1ZLaDZ3cjJzRU5yUW1VMlNDT195TmJOX25yUVp0VHJsazNGcXpXdmc5T1NDd1lrVDRoUkZJU3FmUzVWWXlUdHFzT0xSa2tWbmFKODhUYmVCN2FRTjdWdW5ucmhnZDQ?oc=5>

### PepsiCo, Inc. $PEP Stake Increased by GRIMES & Co WEALTH MANAGEMENT LLC
- Summary: Grimes & Co Wealth Management increased its stake in PepsiCo, indicating confidence in the company.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxNZW4wd3l5dE9GbUVIWktOLXlLR292MDM3OUpDTXNILWJvZlZtcnhzVU9zTEppU1Z2RndqMGVJdWtaTG9fWjFLc0REV3VHRzV0SUUxUU9fUEhKSUZIekFBd2tBZzJiTHVLQVpQV3lIX2g1S3FfUXFIYmZTUWZQUnJqQ0tRS21uMWJJWUF4cDNjQlVUUF9VYWNXTnBkODNJaFhfalpEa19SWXBYV1YzVFV5Rm5zTDVkVS04RFE0Uy1iZmZia0VBUlE?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **PEP** | **17.78** | **8.65** | **12.18** | **5.60** | **192,609,828,864.00 USD** | **3.88** |
| KO | 28.22 | 11.01 | 25.20 | 7.40 | 411,562,999,808.00 USD | 42.21 |
| MNST | 41.56 | 9.09 | 29.04 | 16.70 | 89,497,444,352.00 USD | 37.90 |
| KDP | 33.00 | 1.96 | 17.19 | 70.60 | 49,851,240,448.00 USD | 43.39 |

Peers fetched as_of: 2026-11-07; PEP reuses existing data (market data as_of: 2026-11-06); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-08
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-07

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
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
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPQ3hPZnVmajhPcHpxbFhNU1VsOW53aHFQN0JreWVWRncwR2Q3c3g3aXVJQ2dOZjluZDBHQ1l0cXRKWXlyRzB2QnQwYlFnSml6YjRqYW5paHdodllxbzdVMkJUclVpbVFXVmN1RERoaWFxZ3hDVkx1T1prNmIzX05HS1JvWEZQOWtuZlRBZVp4M29YeUpKSE5FYzZhS0tfdlV6NjFlRw?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxPNkdqTmktOGdTWVVWUFowZnVxYzkxNG5jMjd5MzQ4aWJoRXQ1QnZZVVcwaE94NVJuLVZRT2xsQV9GZUNXc3FsWUxmUVdQamJfTzJ1RnYxU3hRSEdtSUJQQnY0dERvc3hWMzM3cVFpd3E2Z2VkS2ktV2xIdkdoUVZGNEVSU29iTlFudTZjLXJsQi1uLVY3SF90OHlLS2tXeDJNdzUwZFlJMWdsbW9rNkNlYUxkdFd0cDI3YXQ2Z3NGRQ?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxOaFJTajBVaXltQzNFcXlnSVl2V1Z5R0hVcDJPVjVHYUhibVhHR3UwRV9hOXV6MzN3bFZhazE2Z0Y2c0dHVVJsUHFPaGpvcFlHbjMzMk5tUmRZMDFERFV3ODZXVzRqNVZlb2diU2lnR0dGenY3RzJYTmc3ZHBvdGtadWZ5SjZBUVZGUjRaamxkMjlLOG5SYWJORWxiWlZOSGVTcmRBWm1fX2g?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxQcDl3MFM0YUd4eFlzVVVlRjJQVG9ocjlRMFFNcEEwTFJ3Z2MtNVdqWXoxOWI1ZElrQW5oYlVUdHpJT3FYclNmejQ2MndrYy1PSnZaQVhubHdOVE5pbkZRTlNraTQ4RnhnczNUODlGUW5yWWxvLWRVWks4ZF92LWc5ZW10SjN5UFNXWjhQOEEyUThBRmMweGY2bHQ1OEtKX25FWGtGamhkZw?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxQY3UwclhpOC1JcmVTRU0zM3doSWx6bFR3QlhCc0lPMjF4Z0VBSkRVV3BJR2swTU1QMHE0WnI4Q2tva2MzSldTZjI0VXBVd0ZoR2RqQ1lCVm52bWZUNnhiVG5TUnliLXE4TzhKS1RmNlFkWW1LUFQ0eWxFN0hhTW5DMEp3MFFzN25pUUhXYWFNVW9wU1NOZ2szb0lzZG52RlkyT2ZPdXo2UzFNMFY4RXU5Mk12ZTlrR0w5X0tGOGt4Vk5MRDA?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxQeGY2TmxKcm1TWXpkcDA0NDMwS0xmMzd4WmxsdURQVTFxT2lZOXF3Z1JvMEhyc2g1aGZvQ09rRHFPZGhiQUpTWG81MHcwd2ptRGp6bzdUd0NPaWZYUHJfUjE5em05NXN3V1lLSHBlVFdydlAxX3hnRlZoa3RNQVkzaEVjVllQZ19aZXBzSkFnRHNlT2pnU3AwZG56WFZhMldUZWZvMENGN3VPd1Z2S1B1TTYzckQ4Zw?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxQdzQzOGNNVGNELW5xaXFyLWw5Q1gydHdJcG5mRFFGemIxV2hzSk9tekZlMmlHNEM1REhsbkM0ZG5jczZBbDktaEsxMERhbDR5Ym15cjNhTFNmLV90QVo4all0OEFJMjdiUDBWMllNajFFQzJqNUpCbTA5M0pZOUhKYlRUVTNRcjRLSVZEMWRoS3pYSl9faHhmLTlrYVJhUEFlcGt1TXJZUDVGOHBmSGd5bng5YTl0dmlkamIzX3NOZkZ1Z3c?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxQMmxVNWNDZTBfRmhMbzVaY2RJalkyQXhLT21scUM1d19fNFQyenVwVEZvTW0weVVOQ3FRNzVjN1VueGxZUThrdVBSd2dhNlJGU29mdUZBS2xCOXpNOUgtQUVLd0ZPeG9GaDE5emtkODZIN21nY0VVUXYxM1NBWE4zUS1KcHhjWkRmVVNkTDd4MDh3UUVFRm0xaGgxTUpnNDVBQ2R2azdNM25ZQVRzRGNJeGl6eDc3aWk4NXFXa0pLanhaSW96Q1ZTelNB?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxOazFqTmZsZE5RUVNybUtpYXRFekhRNV9hc3RvREdkdnhLZGJjQ3d5ekZGbmw1dlNLaXpyNU42QjAtUGRKcWNrVUFfT284OFBtcTJjeEZqWGRjSzdrS2k1a0l2b21FbUkxaWtvWnBRbEJNQUNSUDVEUUd3dlM3cVgxM2RyTzlRcG1BbTZ0eWJxVVI5R0xHZmlUNVhuRXVBUTFLV2IxZW9EVmRZNnJFNWVkMzNhdFo?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxPcENldTM3SHJHWmxTcnVFSXBrQVJnQl82S0UxWnBGajZscWNFenRTSWJoVGhZdHZoSjFPb0djcVRsMlJ1QThwcmN2anEyVUZFaEItR2RRQmcxLW5RSVVkNnhnWXNEbDJKc1BXdENKRk5OdC1xUGZMTnhISWNqRXNZdEpOVUh6MzlSd3JuYkRVRGZpcTBudmNGWnAzYTNNVWZCcGFFR29LbEh1enV5bTNIMWdB?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxNMWdkU0gzZGtHMzFwQUxfZ1VrRjdfQXctbnlleE1JMkJGQ1lFeWZfVUZrOTVLbmhTYW5DVklLVEU3MUVJdWxKRXQzdDVsOFRPenRRWFByM211SWQ5TzhuRFlvdmJiRWc5WXZTUElWZzVRbzg0N0dGVTlzU3V6OW5peDZkUTlPTlRCaDBFZGxUWmZHSVIwT2Mzd0J4TFoyZHptSzJ4R09nZndHeWRpUGJj?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxQUHJLQXc1b2xhR28yWV8zb1NwM0FpVFJKbEpJY083T2w2OXU2WENIX0R4UG1PUTdtMFkzWnkxMldNb04wOWNIWXJNR1I3UnRoSmZaeWIxQ0I0NGwzcHV1U0R2S0pEZFFDX3pGbHZKb0lCM1VrcGcwMmloUmxJNUJVcUJvOGQ4ckZaLUtYdV96SmpfbXdWcWxxNG9UTFU1c2NjLUVCSXVReXRObXRlLWJfOWM1STB5dG80XzROYnlMcy1uaE42SEtaLTNhX1NHYnV5dEHSAdcBQVVfeXFMT1U0LTFBdUZIelU2SU5xTzZJdGt2Yy12bDZfNVZBREROekx4dnd2Y0p2MmkyVUFRSjVHMUpzLWZrQXVoZEJtaEpOMFlfNWxta3dqMk5JcF9yTlFTQnNIUE5FRDYtWXdYS3ZfcnNsU21veEVKNzJxbTNQY1ZLaDZ3cjJzRU5yUW1VMlNDT195TmJOX25yUVp0VHJsazNGcXpXdmc5T1NDd1lrVDRoUkZJU3FmUzVWWXlUdHFzT0xSa2tWbmFKODhUYmVCN2FRTjdWdW5ucmhnZDQ?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxNZW4wd3l5dE9GbUVIWktOLXlLR292MDM3OUpDTXNILWJvZlZtcnhzVU9zTEppU1Z2RndqMGVJdWtaTG9fWjFLc0REV3VHRzV0SUUxUU9fUEhKSUZIekFBd2tBZzJiTHVLQVpQV3lIX2g1S3FfUXFIYmZTUWZQUnJqQ0tRS21uMWJJWUF4cDNjQlVUUF9VYWNXTnBkODNJaFhfalpEa19SWXBYV1YzVFV5Rm5zTDVkVS04RFE0Uy1iZmZia0VBUlE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
