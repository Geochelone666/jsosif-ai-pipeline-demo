# PEP Intelligence Report

- ticker: **PEP**
- Report as_of: **2026-11-09**
- Market data as_of: **2026-11-09**
- Quant sources: https://finance.yahoo.com/quote/PEP/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/PEP/key-statistics/
- AI analysis snapshot as_of: **2026-11-09**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-10T06:14:03.168066+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 6, 'ai': 5, 'unknown': 0, 'irrelevant': 13})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **11** exact headline/source/date matches; prior report **20261109T043242Z-c8e908de/PEP** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 9 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 29.17%; oldest publication 2026-11-03

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 141.8800 |
| Return 1D (%) | 0.3821 |
| Return 1W (%) | 1.0397 |
| Return 1M (%) | 12.6300 |
| Return YTD (%) | 1.8666 |
| Return 1Y (%) | 3.2731 |
| Annualized volatility (%) | 21.6517 |
| Beta vs SPY | -0.1952 |
| Max drawdown (%) | -25.2176 |
| Sharpe (rf=0) | 0.2682 |
| Downside deviation (rf=0, %) | 14.3317 |
| Sortino (rf=0) | 0.4051 |
| Historical VaR 95% (1D, %) | 2.2001 |
| Historical ES 95% (1D, %) | 2.6412 |
| Correlation vs SPY | -0.1234 |
| Tracking error vs SPY (%) | 27.0080 |
| P/E (trailing) | 17.85 |
| P/B | 8.68 |
| EV/EBITDA | 12.22 |
| Revenue growth (%) | 5.60 |
| Forward P/E (estimate) | 16.42 |
| Gross margin (%) | 54.33 |
| Operating margin (%) | 16.88 |
| Return on equity (%) | 52.19 |
| Free cash flow yield (%) | 4.68 |
| MA50 | 133.2277 |
| Close vs MA50 (%) | 6.4944 |
| MA200 | 143.6877 |
| Close vs MA200 (%) | -1.2581 |
| RSI (14, Wilder) | 63.3169 |
| MACD (12,26) | 2.7861 |
| MACD signal (9) | 1.9117 |
| MACD histogram | 0.8745 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'PEP': 278, 'SPY': 278}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 141.8800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.3821 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.0397 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 12.6300 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 1.8666 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 3.2731 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 21.6517 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.3317 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4051 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.2001 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.6412 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1234 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 27.0080 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1952 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -25.2176 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2682 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.4236 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.3270 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 16.8830 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 52.1870 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.6778 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 17.8465 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 63.3169 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.8745 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 6.4944 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -1.2581 -> Slightly below the moving-average trend level.

## TAILWINDS

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

### PepsiCo Has Raised Its Dividend 54 Straight Years, but $1,000 in Coca-Cola Finished $1,296 Ahead Over the Past Decade
- Summary: PepsiCo Has Raised Its Dividend 54 Straight Years, but $1,000 in Coca-Cola Finished $1,296 Ahead Over the Past Decade
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxPREZNWVpQWFR3bmZjcUZJQTAwQUdTa1hCQnVpaEJuN19xMjNfMmVhSW1xNjI0U2JXRnA5LXlySjB0bDNvak5ZX0ZzU2t4U0J0bkNJUHZBZEJNdmVqSVFLVUZqZTRTZnM2WVdaN1JuS1psaWJ1WHZic05Vc1Njc05CT2RoTXF4SjZ1Sk5OVXdZZXVhRWxiU0ljb1c4Um1GdEVKR3dhLUpxd3hvQWQ0TlVpcmh2VkRLNEE3MGRrSFZtY0Q3VjVZRzdud3JqTDZDbnQ3eW5kYXFZbklnVjEtLW5tdEhxVGV3SlVqUmhveg?oc=5>

### PepsiCo Extends KFC Beverage Partnership Across Eight International Markets
- Summary: PepsiCo Extends KFC Beverage Partnership Across Eight International Markets
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxOaFJTajBVaXltQzNFcXlnSVl2V1Z5R0hVcDJPVjVHYUhibVhHR3UwRV9hOXV6MzN3bFZhazE2Z0Y2c0dHVVJsUHFPaGpvcFlHbjMzMk5tUmRZMDFERFV3ODZXVzRqNVZlb2diU2lnR0dGenY3RzJYTmc3ZHBvdGtadWZ5SjZBUVZGUjRaamxkMjlLOG5SYWJORWxiWlZOSGVTcmRBWm1fX2g?oc=5>

### PepsiCo Remains a Popular Choice for Dividend Investors
- Summary: PepsiCo Remains a Popular Choice for Dividend Investors
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxQcDl3MFM0YUd4eFlzVVVlRjJQVG9ocjlRMFFNcEEwTFJ3Z2MtNVdqWXoxOWI1ZElrQW5oYlVUdHpJT3FYclNmejQ2MndrYy1PSnZaQVhubHdOVE5pbkZRTlNraTQ4RnhnczNUODlGUW5yWWxvLWRVWks4ZF92LWc5ZW10SjN5UFNXWjhQOEEyUThBRmMweGY2bHQ1OEtKX25FWGtGamhkZw?oc=5>

### PepsiCo, Inc. $PEP Stock Sold by Brighton Jones LLC
- Summary: PepsiCo, Inc. $PEP Stock Sold by Brighton Jones LLC
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxQcXF2dHM3ZUtuTWJzeXpuTElqbzM1YXZQeXl2eXVxTzBLSFhyN1lRMXJTZHVtLU1nclZ6Qkp0ajJ5dnZnS3F1YVdSTFFVRmZiQkctaHgzY0VkZUFBUXVHamxBendUUV84bHktcXo0SkJhdGk1QVUyR0dzbEVjNElKQTZiQnZSYTJ6djYzSF9KU0VPQkhqR3pQalY5aEV1Wm1sa2duYTVpa0VjdVNFd1E?oc=5>

### PepsiCo, Inc. $PEP Stock: Lindsell Train Ltd Reduces Stake
- Summary: PepsiCo, Inc. $PEP Stock: Lindsell Train Ltd Reduces Stake
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxQeGY2TmxKcm1TWXpkcDA0NDMwS0xmMzd4WmxsdURQVTFxT2lZOXF3Z1JvMEhyc2g1aGZvQ09rRHFPZGhiQUpTWG81MHcwd2ptRGp6bzdUd0NPaWZYUHJfUjE5em05NXN3V1lLSHBlVFdydlAxX3hnRlZoa3RNQVkzaEVjVllQZ19aZXBzSkFnRHNlT2pnU3AwZG56WFZhMldUZWZvMENGN3VPd1Z2S1B1TTYzckQ4Zw?oc=5>

### PepsiCo (PEP) Could Be 29% Undervalued Following Its KFC Deal Renewal
- Summary: Speculation that PepsiCo may be undervalued after renewing its KFC franchise agreement.
- Date: 2026-11-06 | Impact: low | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOTTZVbW1pRWl3aU9seF8zT2ZCZ2hrUFcwXzltSUNOUlYxSmJvWWp2V2l3cF9veVdfVTU5Q3V1VTNNYWtmem5GWHo2bzUwRTJRa2xBX2FTRDBrX2xNUGJQQWktcWJ0SVdMYW9xOWRyM2RsNWU4SmNoMXV1dnZNaDlQVmN6N1Z3MHZLeEtSZXNJbU5ObnNoSkliblphQmJFdw?oc=5>

### KFC pairs chicken tenders with Doritos on select menus as PepsiCo renews its drink deal in 8 countries.
- Summary: PepsiCo renews its drink partnership with KFC in eight countries, pairing drinks with new menu items.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxNMWdkU0gzZGtHMzFwQUxfZ1VrRjdfQXctbnlleE1JMkJGQ1lFeWZfVUZrOTVLbmhTYW5DVklLVEU3MUVJdWxKRXQzdDVsOFRPenRRWFByM211SWQ5TzhuRFlvdmJiRWc5WXZTUElWZzVRbzg0N0dGVTlzU3V6OW5peDZkUTlPTlRCaDBFZGxUWmZHSVIwT2Mzd0J4TFoyZHptSzJ4R09nZndHeWRpUGJj?oc=5>

### Learn Why The Bull Case For PepsiCo (PEP) Could Change Following KFC Deal Renewal
- Summary: KFC deal renewal may alter PepsiCo’s bullish outlook.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxQamxqV0M3YXdmNS1FOENuc3ExX1VQT29XaWRXZmZEYkJVdE0zampyUWRnZWFDay1jcTQta3VDeUI5SGprNGNjbFhoVE9xTmZ0VEFIMG1zdjhiM040Y2JpVWN4NDd1OTBXVW5RV05JY0ZkZDFoUkxWWllKNTdkUmZwYnQzWTJscXVKTGoxUHFGLUtpUnpUSUVpd2IwX1FxVEtQb2VhTkZyWmpPaGJnSjc2UXZIWU1YMnR5WnVGYXh6YmVkem1JQ2Jsbm9WbzRqcllIMzhfWNIB2gFBVV95cUxOR3lTd2U0eXVlZE5IOWkwdFB2blNOVkNEZ2JWWlc2a3F3T21zMjhuWTZCN3BiZHRzWkwwRUluZ1VibS05cW1JOVZ4U0FXT3RXUTVVdWxsbm4tQkFWU0RRNWtHcHlrLW9JbkpQU3ZyUFVpem5YSk1fd09hT1YzMi16dVZnUWQtLVB3RDRGWHpTbFprRDR2ZFhvdXFLVlZydzdSTG9pY19aajM4bVVhNEFBbFJhV0RvM0plVmFMT1VOM3AzY19UNDgzVGJ3WE9WM29pTlhTbTVQbUY1UQ?oc=5>

## RISKS

### PepsiCo reshapes North American business with 1,000 job reductions (PEP:NASDAQ)
- Summary: PepsiCo cuts 1,000 jobs in North America, signaling cost-cutting and potential operational impact.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNbFFHVHlsLWJnOWIta3lIQnBNdE9DVkhZbVJkM0NJbHFIUlpTeVJoSzhNODZadFI4WGNabEdxd29LeUh4ZEdFTmZRdU91Nm5hbGl2SlJHMWdVU2lSc3d5Mno3dlZILTRxSTVDMlNOVHBxTjJpU0ppUk9GNndIaTZIT0FmQ0dWRnFDU3l4VDhmUFlJZ2p3NjZLM053SGhFN29EVHhBTFRn?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **PEP** | **17.85** | **8.68** | **12.22** | **5.60** | **193,345,716,224.00 USD** | **3.27** |
| KO | 28.33 | 11.05 | 25.29 | 7.40 | 413,111,681,024.00 USD | 39.73 |
| MNST | 41.49 | 9.08 | 28.78 | 16.70 | 89,340,846,080.00 USD | 30.90 |
| KDP | 33.28 | 1.98 | 17.27 | 70.60 | 50,273,128,448.00 USD | 46.83 |

Peers fetched as_of: 2026-11-09; PEP reuses existing data (market data as_of: 2026-11-09); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-08
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

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
- Filing date: 2026-10-08
- Revenue (latest available single quarter): 25,274,000,000.00 USD; period 2026-06-14/2026-09-05; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 3,048,000,000.00 USD; period 2026-06-14/2026-09-05; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/77476/000007747626000048/pep-20260905.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMipAFBVV95cUxPQ3hPZnVmajhPcHpxbFhNU1VsOW53aHFQN0JreWVWRncwR2Q3c3g3aXVJQ2dOZjluZDBHQ1l0cXRKWXlyRzB2QnQwYlFnSml6YjRqYW5paHdodllxbzdVMkJUclVpbVFXVmN1RERoaWFxZ3hDVkx1T1prNmIzX05HS1JvWEZQOWtuZlRBZVp4M29YeUpKSE5FYzZhS0tfdlV6NjFlRw?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxPNkdqTmktOGdTWVVWUFowZnVxYzkxNG5jMjd5MzQ4aWJoRXQ1QnZZVVcwaE94NVJuLVZRT2xsQV9GZUNXc3FsWUxmUVdQamJfTzJ1RnYxU3hRSEdtSUJQQnY0dERvc3hWMzM3cVFpd3E2Z2VkS2ktV2xIdkdoUVZGNEVSU29iTlFudTZjLXJsQi1uLVY3SF90OHlLS2tXeDJNdzUwZFlJMWdsbW9rNkNlYUxkdFd0cDI3YXQ2Z3NGRQ?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxPREZNWVpQWFR3bmZjcUZJQTAwQUdTa1hCQnVpaEJuN19xMjNfMmVhSW1xNjI0U2JXRnA5LXlySjB0bDNvak5ZX0ZzU2t4U0J0bkNJUHZBZEJNdmVqSVFLVUZqZTRTZnM2WVdaN1JuS1psaWJ1WHZic05Vc1Njc05CT2RoTXF4SjZ1Sk5OVXdZZXVhRWxiU0ljb1c4Um1GdEVKR3dhLUpxd3hvQWQ0TlVpcmh2VkRLNEE3MGRrSFZtY0Q3VjVZRzdud3JqTDZDbnQ3eW5kYXFZbklnVjEtLW5tdEhxVGV3SlVqUmhveg?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxOaFJTajBVaXltQzNFcXlnSVl2V1Z5R0hVcDJPVjVHYUhibVhHR3UwRV9hOXV6MzN3bFZhazE2Z0Y2c0dHVVJsUHFPaGpvcFlHbjMzMk5tUmRZMDFERFV3ODZXVzRqNVZlb2diU2lnR0dGenY3RzJYTmc3ZHBvdGtadWZ5SjZBUVZGUjRaamxkMjlLOG5SYWJORWxiWlZOSGVTcmRBWm1fX2g?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxQcDl3MFM0YUd4eFlzVVVlRjJQVG9ocjlRMFFNcEEwTFJ3Z2MtNVdqWXoxOWI1ZElrQW5oYlVUdHpJT3FYclNmejQ2MndrYy1PSnZaQVhubHdOVE5pbkZRTlNraTQ4RnhnczNUODlGUW5yWWxvLWRVWks4ZF92LWc5ZW10SjN5UFNXWjhQOEEyUThBRmMweGY2bHQ1OEtKX25FWGtGamhkZw?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxQcXF2dHM3ZUtuTWJzeXpuTElqbzM1YXZQeXl2eXVxTzBLSFhyN1lRMXJTZHVtLU1nclZ6Qkp0ajJ5dnZnS3F1YVdSTFFVRmZiQkctaHgzY0VkZUFBUXVHamxBendUUV84bHktcXo0SkJhdGk1QVUyR0dzbEVjNElKQTZiQnZSYTJ6djYzSF9KU0VPQkhqR3pQalY5aEV1Wm1sa2duYTVpa0VjdVNFd1E?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxQeGY2TmxKcm1TWXpkcDA0NDMwS0xmMzd4WmxsdURQVTFxT2lZOXF3Z1JvMEhyc2g1aGZvQ09rRHFPZGhiQUpTWG81MHcwd2ptRGp6bzdUd0NPaWZYUHJfUjE5em05NXN3V1lLSHBlVFdydlAxX3hnRlZoa3RNQVkzaEVjVllQZ19aZXBzSkFnRHNlT2pnU3AwZG56WFZhMldUZWZvMENGN3VPd1Z2S1B1TTYzckQ4Zw?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOTTZVbW1pRWl3aU9seF8zT2ZCZ2hrUFcwXzltSUNOUlYxSmJvWWp2V2l3cF9veVdfVTU5Q3V1VTNNYWtmem5GWHo2bzUwRTJRa2xBX2FTRDBrX2xNUGJQQWktcWJ0SVdMYW9xOWRyM2RsNWU4SmNoMXV1dnZNaDlQVmN6N1Z3MHZLeEtSZXNJbU5ObnNoSkliblphQmJFdw?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxNMWdkU0gzZGtHMzFwQUxfZ1VrRjdfQXctbnlleE1JMkJGQ1lFeWZfVUZrOTVLbmhTYW5DVklLVEU3MUVJdWxKRXQzdDVsOFRPenRRWFByM211SWQ5TzhuRFlvdmJiRWc5WXZTUElWZzVRbzg0N0dGVTlzU3V6OW5peDZkUTlPTlRCaDBFZGxUWmZHSVIwT2Mzd0J4TFoyZHptSzJ4R09nZndHeWRpUGJj?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxQamxqV0M3YXdmNS1FOENuc3ExX1VQT29XaWRXZmZEYkJVdE0zampyUWRnZWFDay1jcTQta3VDeUI5SGprNGNjbFhoVE9xTmZ0VEFIMG1zdjhiM040Y2JpVWN4NDd1OTBXVW5RV05JY0ZkZDFoUkxWWllKNTdkUmZwYnQzWTJscXVKTGoxUHFGLUtpUnpUSUVpd2IwX1FxVEtQb2VhTkZyWmpPaGJnSjc2UXZIWU1YMnR5WnVGYXh6YmVkem1JQ2Jsbm9WbzRqcllIMzhfWNIB2gFBVV95cUxOR3lTd2U0eXVlZE5IOWkwdFB2blNOVkNEZ2JWWlc2a3F3T21zMjhuWTZCN3BiZHRzWkwwRUluZ1VibS05cW1JOVZ4U0FXT3RXUTVVdWxsbm4tQkFWU0RRNWtHcHlrLW9JbkpQU3ZyUFVpem5YSk1fd09hT1YzMi16dVZnUWQtLVB3RDRGWHpTbFprRDR2ZFhvdXFLVlZydzdSTG9pY19aajM4bVVhNEFBbFJhV0RvM0plVmFMT1VOM3AzY19UNDgzVGJ3WE9WM29pTlhTbTVQbUY1UQ?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNbFFHVHlsLWJnOWIta3lIQnBNdE9DVkhZbVJkM0NJbHFIUlpTeVJoSzhNODZadFI4WGNabEdxd29LeUh4ZEdFTmZRdU91Nm5hbGl2SlJHMWdVU2lSc3d5Mno3dlZILTRxSTVDMlNOVHBxTjJpU0ppUk9GNndIaTZIT0FmQ0dWRnFDU3l4VDhmUFlJZ2p3NjZLM053SGhFN29EVHhBTFRn?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
