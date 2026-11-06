# PEP Intelligence Report

- ticker: **PEP**
- Report as_of: **2026-11-05**
- Market data as_of: **2026-11-05**
- Quant sources: https://finance.yahoo.com/quote/PEP/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/PEP/key-statistics/
- AI analysis snapshot as_of: **2026-11-05**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-06T05:06:16.255895+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 5, 'ai': 7, 'unknown': 0, 'irrelevant': 12})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261105T045846Z-bde0a1fe/PEP** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 9 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-10-29

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 142.7100 |
| Return 1D (%) | 0.2036 |
| Return 1W (%) | 6.6672 |
| Return 1M (%) | 13.5774 |
| Return YTD (%) | 2.4625 |
| Return 1Y (%) | 3.9427 |
| Annualized volatility (%) | 21.6248 |
| Beta vs SPY | -0.1965 |
| Max drawdown (%) | -25.2176 |
| Sharpe (rf=0) | 0.2869 |
| Downside deviation (rf=0, %) | 14.3009 |
| Sortino (rf=0) | 0.4338 |
| Historical VaR 95% (1D, %) | 2.1996 |
| Historical ES 95% (1D, %) | 2.6412 |
| Correlation vs SPY | -0.1235 |
| Tracking error vs SPY (%) | 26.9266 |
| P/E (trailing) | 17.95 |
| P/B | 8.73 |
| EV/EBITDA | 12.28 |
| Revenue growth (%) | 5.60 |
| Forward P/E (estimate) | 16.52 |
| Gross margin (%) | 54.33 |
| Operating margin (%) | 16.88 |
| Return on equity (%) | 52.19 |
| Free cash flow yield (%) | 4.65 |
| MA50 | 133.1197 |
| Close vs MA50 (%) | 7.2043 |
| MA200 | 143.6738 |
| Close vs MA200 (%) | -0.6709 |
| RSI (14, Wilder) | 65.8984 |
| MACD (12,26) | 2.5266 |
| MACD signal (9) | 1.4501 |
| MACD histogram | 1.0765 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'PEP': 276, 'SPY': 276}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 142.7100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.2036 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 6.6672 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 13.5774 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 2.4625 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 3.9427 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 21.6248 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.3009 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4338 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.1996 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.6412 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1235 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.9266 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1965 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -25.2176 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2869 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.5196 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.3270 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 16.8830 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 52.1870 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.6506 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 17.9509 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 65.8984 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.0765 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 7.2043 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -0.6709 -> Slightly below the moving-average trend level.

## TAILWINDS

### PepsiCo (NASDAQ:PEP) Stock Price Up 2.2% - What's Next?
- Summary: PepsiCo (NASDAQ:PEP) Stock Price Up 2.2% - What's Next?
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxOX0V0QmNORTZKUmdFaW93WUdXYURCLVhQSkxjNlIxOEQ1SEdOQnRoZjRsOXRZeWtWMmVja3AwaF9yUmpPc2Z2dGxCWFFUMS1mTUo0SHdsVkxNQkl5WUtCVHF2WEU1QmkwVDMzODZxWmhvU0JudUp0LXl1Z0FCYW9jY01QejhyZzN1QkJzS1ZvN0duTm41UkljMi12ajhfbUpoRW1XbXMyLVVXZ1U?oc=5>

### What Is PepsiCo (PEP) Gaining From Its Expanded Beverage Partnership?
- Summary: PepsiCo expands beverage partnership, potentially boosting product mix and market reach.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPQ3hPZnVmajhPcHpxbFhNU1VsOW53aHFQN0JreWVWRncwR2Q3c3g3aXVJQ2dOZjluZDBHQ1l0cXRKWXlyRzB2QnQwYlFnSml6YjRqYW5paHdodllxbzdVMkJUclVpbVFXVmN1RERoaWFxZ3hDVkx1T1prNmIzX05HS1JvWEZQOWtuZlRBZVp4M29YeUpKSE5FYzZhS0tfdlV6NjFlRw?oc=5>

### PepsiCo Jumps 15.1% in a Month as Investors Weigh What Comes Next
- Summary: PepsiCo shares surged 15.1% over a month, reflecting investor optimism.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxOYlhuTVc3aHp1YW9RZVVDdnRQcUZIT1p2LVI4ZDlGbjVkQkk0cmV0Njl6M2pkb2swV24wUjhCc2xXS1JWUXZUQnBSNk42anBJQjJaOU1WOFBUNnlVY2djZmQyLTAtS3o3Y05KQ3otMDhvSmY0Q1RtRlZJRUFOTktGV3psYU5KZ0pNSlZYQTFjZmhiNGJxeE9UdzBDOXlTQnd0bUZaWFV0VG13LURjeG53bUZiUk5Na3dCQXk2Rg?oc=5>

### Golden Cross Formed, PEP Stock Gains 3.75% on Wednesday
- Summary: A golden cross formed, leading to a 3.75% rise in PEP shares on Wednesday, indicating bullish momentum.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNQmJ1UDFyM0x1T1ZTbDFTSDJ1ZnVzVFVTVnEwYW1uUjR3ZW1WMERBcUg0MjI4c0VqT2JvN1huTElSYkNMTi1LMUJ5SEk0LWhJbnYzZC1sNU02WncyRnNKdUh4MFk4UWN6T3QxNGZYTWd6UV9xZGtVaVRXMTVHYUpUUnVxVUpFX0R5U0NHdms0LTJtZ01IR1Vj?oc=5>

## HEADWINDS

### PepsiCo Lowers 2026 EPS Outlook as North America Pressures Margins
- Summary: PepsiCo Lowers 2026 EPS Outlook as North America Pressures Margins
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxPNkdqTmktOGdTWVVWUFowZnVxYzkxNG5jMjd5MzQ4aWJoRXQ1QnZZVVcwaE94NVJuLVZRT2xsQV9GZUNXc3FsWUxmUVdQamJfTzJ1RnYxU3hRSEdtSUJQQnY0dERvc3hWMzM3cVFpd3E2Z2VkS2ktV2xIdkdoUVZGNEVSU29iTlFudTZjLXJsQi1uLVY3SF90OHlLS2tXeDJNdzUwZFlJMWdsbW9rNkNlYUxkdFd0cDI3YXQ2Z3NGRQ?oc=5>

## CATALYSTS

### PepsiCo Remains a Popular Choice for Dividend Investors
- Summary: PepsiCo Remains a Popular Choice for Dividend Investors
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxQcDl3MFM0YUd4eFlzVVVlRjJQVG9ocjlRMFFNcEEwTFJ3Z2MtNVdqWXoxOWI1ZElrQW5oYlVUdHpJT3FYclNmejQ2MndrYy1PSnZaQVhubHdOVE5pbkZRTlNraTQ4RnhnczNUODlGUW5yWWxvLWRVWks4ZF92LWc5ZW10SjN5UFNXWjhQOEEyUThBRmMweGY2bHQ1OEtKX25FWGtGamhkZw?oc=5>

### PepsiCo, Inc. $PEP Stock Sold by Summit Global Investments
- Summary: PepsiCo, Inc. $PEP Stock Sold by Summit Global Investments
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxOUlVzM3l5ejBhRmxQcXhNaGp0UGQ5T0Y1VWJKVk5VZE9sa3lvNno4V1BNZFBIS1pYdkhEb1dydEY4cUhnR2VXOS00QlZ3eHFubVZ1eHhJSGJWdmswU2FQT0xQZmxaWXdZT3p3eXY0THVER0djWU9LSWJZZlJkdC1OV3RPYVI5X1RoY1A5SF9YN0cxcnhvdlp0RDNrSHlXTXdCR2pYd2h6SkZvUXRpNWFybDU4OXZMU28?oc=5>

### PepsiCo, Inc. $PEP Stock Sold by Heritage Investors Management Corp
- Summary: PepsiCo, Inc. $PEP Stock Sold by Heritage Investors Management Corp
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxQdzQzOGNNVGNELW5xaXFyLWw5Q1gydHdJcG5mRFFGemIxV2hzSk9tekZlMmlHNEM1REhsbkM0ZG5jczZBbDktaEsxMERhbDR5Ym15cjNhTFNmLV90QVo4all0OEFJMjdiUDBWMllNajFFQzJqNUpCbTA5M0pZOUhKYlRUVTNRcjRLSVZEMWRoS3pYSl9faHhmLTlrYVJhUEFlcGt1TXJZUDVGOHBmSGd5bng5YTl0dmlkamIzX3NOZkZ1Z3c?oc=5>

### PepsiCo: 4.2% Yield And 53 Years Of Dividend Growth In An Anti-Bubble (NASDAQ:PEP)
- Summary: PepsiCo reports a 4.2% dividend yield with a 53‑year growth record, reinforcing its dividend stability.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxOazFqTmZsZE5RUVNybUtpYXRFekhRNV9hc3RvREdkdnhLZGJjQ3d5ekZGbmw1dlNLaXpyNU42QjAtUGRKcWNrVUFfT284OFBtcTJjeEZqWGRjSzdrS2k1a0l2b21FbUkxaWtvWnBRbEJNQUNSUDVEUUd3dlM3cVgxM2RyTzlRcG1BbTZ0eWJxVVI5R0xHZmlUNVhuRXVBUTFLV2IxZW9EVmRZNnJFNWVkMzNhdFo?oc=5>

### PepsiCo (PEP) Stock May Be 50% Undervalued As Partnership Deal Extends
- Summary: PepsiCo’s partnership deal extension may signal continued growth, potentially undervaluing the stock by 50%.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxNc3JKbUhRcDNaWXVXNDE4UFR0Qkp5Sy0zMkVWSmQxbi00M2Jxc0R0eFRGWE9VcW9DRGtSeThQaTl0OVBOZHFMbkpzT2FTbjJlbVNtWThkcXdmZC12eU1TRVBhUUoyQ0VzVlYyTmttak1aWGM1Q2gxUENFUHhvUnZJRWF1SEc3VmE4R0dNMFJZZVcySTA0UmJVS1RGZ1ZvVHBzT1lZVzVsQTRUV3Y0NzZhcVd6cDlyMEdxb1RsYmRUaTF2eTV2WmlBam5sVURnQ1o0RHZB0gHYAUFVX3lxTE1YZnFieXhwUnN6YWlHejNZZExONTRLWmtYTzZ3MWtPTEhwZ1poQmtSUnUxamFwTEY5MWdTanpnUTR6ZGJiTDBKVjB4WWNpUWxROFZVN1lJWHp4aU8zS3lOeHI3VmVIZmk2bV9fVTRRcTh2MFNKS0Vsdk9Qalp6U1NIelY2UVRNVlNpRGhZY2RqQ21rNTVrZ09GTkNTcVVKSGo2N29SWFpwSjdhT3BXd1p2LS1BdkREQmlReEJTbTNQc3c0ZVZhUmZ6RjR1Nm5tcUhUS0ZpazNjVw?oc=5>

### Can PepsiCo's Snack Pricing Strategy Drive Volume Growth?
- Summary: Explores how PepsiCo’s snack pricing could boost sales volume, indicating potential product strategy impact.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxPcENldTM3SHJHWmxTcnVFSXBrQVJnQl82S0UxWnBGajZscWNFenRTSWJoVGhZdHZoSjFPb0djcVRsMlJ1QThwcmN2anEyVUZFaEItR2RRQmcxLW5RSVVkNnhnWXNEbDJKc1BXdENKRk5OdC1xUGZMTnhISWNqRXNZdEpOVUh6MzlSd3JuYkRVRGZpcTBudmNGWnAzYTNNVWZCcGFFR29LbEh1enV5bTNIMWdB?oc=5>

### Can PepsiCo (NASDAQ:PEP) Protect Its Dividend Amid Slower Growth?
- Summary: PepsiCo seeks to maintain dividend despite slower growth.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQUUkzVDdET1F5VjFYNnJxbGdwY0ZjWjhWLWxaeURHZXRpUzBUcXhPdEhWa0dpTjZlQXJ3T09FYzFrdnNTOEVlaWphcmdndW9wdml5OXZWa3dSODFNZ0pJWUdMeGhZQV9ockZPV01Vd3ppWjBYV0lXSlB2bWlacFotYjNYRUdWQU1JWnR2eG1NRjVTaU01aC05WUhvUFd5VEYzcTg2TVE1WUQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **PEP** | **17.95** | **8.73** | **12.28** | **5.60** | **194,476,802,048.00 USD** | **3.94** |
| KO | 28.24 | 11.02 | 25.22 | 7.40 | 411,821,113,344.00 USD | 43.45 |
| MNST | 45.12 | 10.01 | 30.81 | 20.20 | 93,701,447,680.00 USD | 40.95 |
| KDP | 33.23 | 1.97 | 17.26 | 70.60 | 50,205,081,600.00 USD | 42.46 |

Peers fetched as_of: 2026-11-05; PEP reuses existing data (market data as_of: 2026-11-05); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-08
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-05

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
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPQ3hPZnVmajhPcHpxbFhNU1VsOW53aHFQN0JreWVWRncwR2Q3c3g3aXVJQ2dOZjluZDBHQ1l0cXRKWXlyRzB2QnQwYlFnSml6YjRqYW5paHdodllxbzdVMkJUclVpbVFXVmN1RERoaWFxZ3hDVkx1T1prNmIzX05HS1JvWEZQOWtuZlRBZVp4M29YeUpKSE5FYzZhS0tfdlV6NjFlRw?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxOYlhuTVc3aHp1YW9RZVVDdnRQcUZIT1p2LVI4ZDlGbjVkQkk0cmV0Njl6M2pkb2swV24wUjhCc2xXS1JWUXZUQnBSNk42anBJQjJaOU1WOFBUNnlVY2djZmQyLTAtS3o3Y05KQ3otMDhvSmY0Q1RtRlZJRUFOTktGV3psYU5KZ0pNSlZYQTFjZmhiNGJxeE9UdzBDOXlTQnd0bUZaWFV0VG13LURjeG53bUZiUk5Na3dCQXk2Rg?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNQmJ1UDFyM0x1T1ZTbDFTSDJ1ZnVzVFVTVnEwYW1uUjR3ZW1WMERBcUg0MjI4c0VqT2JvN1huTElSYkNMTi1LMUJ5SEk0LWhJbnYzZC1sNU02WncyRnNKdUh4MFk4UWN6T3QxNGZYTWd6UV9xZGtVaVRXMTVHYUpUUnVxVUpFX0R5U0NHdms0LTJtZ01IR1Vj?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxPNkdqTmktOGdTWVVWUFowZnVxYzkxNG5jMjd5MzQ4aWJoRXQ1QnZZVVcwaE94NVJuLVZRT2xsQV9GZUNXc3FsWUxmUVdQamJfTzJ1RnYxU3hRSEdtSUJQQnY0dERvc3hWMzM3cVFpd3E2Z2VkS2ktV2xIdkdoUVZGNEVSU29iTlFudTZjLXJsQi1uLVY3SF90OHlLS2tXeDJNdzUwZFlJMWdsbW9rNkNlYUxkdFd0cDI3YXQ2Z3NGRQ?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxQcDl3MFM0YUd4eFlzVVVlRjJQVG9ocjlRMFFNcEEwTFJ3Z2MtNVdqWXoxOWI1ZElrQW5oYlVUdHpJT3FYclNmejQ2MndrYy1PSnZaQVhubHdOVE5pbkZRTlNraTQ4RnhnczNUODlGUW5yWWxvLWRVWks4ZF92LWc5ZW10SjN5UFNXWjhQOEEyUThBRmMweGY2bHQ1OEtKX25FWGtGamhkZw?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxOUlVzM3l5ejBhRmxQcXhNaGp0UGQ5T0Y1VWJKVk5VZE9sa3lvNno4V1BNZFBIS1pYdkhEb1dydEY4cUhnR2VXOS00QlZ3eHFubVZ1eHhJSGJWdmswU2FQT0xQZmxaWXdZT3p3eXY0THVER0djWU9LSWJZZlJkdC1OV3RPYVI5X1RoY1A5SF9YN0cxcnhvdlp0RDNrSHlXTXdCR2pYd2h6SkZvUXRpNWFybDU4OXZMU28?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxQdzQzOGNNVGNELW5xaXFyLWw5Q1gydHdJcG5mRFFGemIxV2hzSk9tekZlMmlHNEM1REhsbkM0ZG5jczZBbDktaEsxMERhbDR5Ym15cjNhTFNmLV90QVo4all0OEFJMjdiUDBWMllNajFFQzJqNUpCbTA5M0pZOUhKYlRUVTNRcjRLSVZEMWRoS3pYSl9faHhmLTlrYVJhUEFlcGt1TXJZUDVGOHBmSGd5bng5YTl0dmlkamIzX3NOZkZ1Z3c?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxOazFqTmZsZE5RUVNybUtpYXRFekhRNV9hc3RvREdkdnhLZGJjQ3d5ekZGbmw1dlNLaXpyNU42QjAtUGRKcWNrVUFfT284OFBtcTJjeEZqWGRjSzdrS2k1a0l2b21FbUkxaWtvWnBRbEJNQUNSUDVEUUd3dlM3cVgxM2RyTzlRcG1BbTZ0eWJxVVI5R0xHZmlUNVhuRXVBUTFLV2IxZW9EVmRZNnJFNWVkMzNhdFo?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxNc3JKbUhRcDNaWXVXNDE4UFR0Qkp5Sy0zMkVWSmQxbi00M2Jxc0R0eFRGWE9VcW9DRGtSeThQaTl0OVBOZHFMbkpzT2FTbjJlbVNtWThkcXdmZC12eU1TRVBhUUoyQ0VzVlYyTmttak1aWGM1Q2gxUENFUHhvUnZJRWF1SEc3VmE4R0dNMFJZZVcySTA0UmJVS1RGZ1ZvVHBzT1lZVzVsQTRUV3Y0NzZhcVd6cDlyMEdxb1RsYmRUaTF2eTV2WmlBam5sVURnQ1o0RHZB0gHYAUFVX3lxTE1YZnFieXhwUnN6YWlHejNZZExONTRLWmtYTzZ3MWtPTEhwZ1poQmtSUnUxamFwTEY5MWdTanpnUTR6ZGJiTDBKVjB4WWNpUWxROFZVN1lJWHp4aU8zS3lOeHI3VmVIZmk2bV9fVTRRcTh2MFNKS0Vsdk9Qalp6U1NIelY2UVRNVlNpRGhZY2RqQ21rNTVrZ09GTkNTcVVKSGo2N29SWFpwSjdhT3BXd1p2LS1BdkREQmlReEJTbTNQc3c0ZVZhUmZ6RjR1Nm5tcUhUS0ZpazNjVw?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxPcENldTM3SHJHWmxTcnVFSXBrQVJnQl82S0UxWnBGajZscWNFenRTSWJoVGhZdHZoSjFPb0djcVRsMlJ1QThwcmN2anEyVUZFaEItR2RRQmcxLW5RSVVkNnhnWXNEbDJKc1BXdENKRk5OdC1xUGZMTnhISWNqRXNZdEpOVUh6MzlSd3JuYkRVRGZpcTBudmNGWnAzYTNNVWZCcGFFR29LbEh1enV5bTNIMWdB?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQUUkzVDdET1F5VjFYNnJxbGdwY0ZjWjhWLWxaeURHZXRpUzBUcXhPdEhWa0dpTjZlQXJ3T09FYzFrdnNTOEVlaWphcmdndW9wdml5OXZWa3dSODFNZ0pJWUdMeGhZQV9ockZPV01Vd3ppWjBYV0lXSlB2bWlacFotYjNYRUdWQU1JWnR2eG1NRjVTaU01aC05WUhvUFd5VEYzcTg2TVE1WUQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
