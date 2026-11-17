# CSCO Intelligence Report

- ticker: **CSCO**
- Report as_of: **2026-11-16**
- Market data as_of: **2026-11-16**
- Quant sources: https://finance.yahoo.com/quote/CSCO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CSCO/key-statistics/
- AI analysis snapshot as_of: **2026-11-16**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-17T06:26:06.820515+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 6, 'ai': 11, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **11** exact headline/source/date matches; prior report **20261116T043911Z-b81cfeb4/CSCO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 8 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 72.0%; oldest publication 2026-11-09

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 94.5200 |
| Return 1D (%) | -1.1711 |
| Return 1W (%) | -4.1865 |
| Return 1M (%) | -11.9844 |
| Return YTD (%) | 24.9771 |
| Return 1Y (%) | 23.4229 |
| Annualized volatility (%) | 37.1591 |
| Beta vs SPY | 1.3078 |
| Max drawdown (%) | -27.2567 |
| Sharpe (rf=0) | 0.7648 |
| Downside deviation (rf=0, %) | 26.2635 |
| Sortino (rf=0) | 1.0821 |
| Historical VaR 95% (1D, %) | 3.2248 |
| Historical ES 95% (1D, %) | 5.5834 |
| Correlation vs SPY | 0.4845 |
| Tracking error vs SPY (%) | 32.7806 |
| P/E (trailing) | 25.14 |
| P/B | 7.23 |
| EV/EBITDA | 18.71 |
| Revenue growth (%) | 24.40 |
| Forward P/E (estimate) | 15.67 |
| Gross margin (%) | 64.07 |
| Operating margin (%) | 27.17 |
| Return on equity (%) | 30.38 |
| Free cash flow yield (%) | 2.91 |
| MA50 | 107.3119 |
| Close vs MA50 (%) | -11.9203 |
| MA200 | 101.8274 |
| Close vs MA200 (%) | -7.1763 |
| RSI (14, Wilder) | 35.9175 |
| MACD (12,26) | -3.4657 |
| MACD signal (9) | -2.8600 |
| MACD histogram | -0.6057 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CSCO': 283, 'SPY': 283}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 94.5200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.1711 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -4.1865 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -11.9844 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 24.9771 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 23.4229 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 37.1591 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.2635 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.0821 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.2248 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.5834 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4845 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.7806 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.3078 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.2567 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.7648 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.6738 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 64.0660 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 27.1660 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 30.3800 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.9073 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 25.1383 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 35.9175 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.6057 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -11.9203 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -7.1763 -> Clearly below the moving-average trend level.

## TAILWINDS

### Cisco Raised Its Earnings Outlook 8%. The Stock Fell 6% Anyway
- Summary: Cisco Raised Its Earnings Outlook 8%. The Stock Fell 6% Anyway
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxOVjM1UkllWHBNT1lVUjRmSVVIMmhCYnhobEc0VTRtcGZpOWVyaVM4WTRkYXR0VkJ4MTJjLWlJMjZ4SjRPYVZXcV9ScGVZT1RhcUFZQk5YM25qUzQ2QkNDYU1abUlhWDNkRFkwd3ZFRVlXSENwT2MxNTZBZkV5b2swYkVBSUY4bUUxdHR6ZHJB?oc=5>

### Cisco Systems Delivers Record Q1 Results, Raises FY27 Outlook
- Summary: Cisco Systems Delivers Record Q1 Results, Raises FY27 Outlook
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNRVcxQXB4NnpKcjdLV2NnTHNveFFIUnllVU9ZSDdReG9iSnJMRTJKRExTSmhWNDNRLTloM1g0MjZYaXh0S2NfdjlMeWNxdnUwRnlTaTg1czdsZTF5Z2tkOVg2RkJ5U19qR0ZVRVJOWDlWTFE2cG1wSlR2Q2ZOODcwcnFvb2V0ZU9mSTFKV1NtelFhWnlEWHlPZEhzdTNRdw?oc=5>

### Cisco Systems (CSCO) Q1 Earnings and Revenues Beat Estimates
- Summary: Cisco Systems (CSCO) Q1 Earnings and Revenues Beat Estimates
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQc3NMbXh0VkFHZnEtalpOX055M2haeWpleW5zdFlYVHlpQjJzS2JLY1A1OVBhUzFfbUhQWUlqWHY2U1JEb3hZTTZDR0hqUW9TVkUxNWpFZmlMckRfZS05TUZIRjBRT3NFTjh2OXpQRUdqRFVFemNlOVdHa0pIalJ6VVRkWWs1ejM1RkdnZ25SZ2FGMU5vSVNBZzF3OA?oc=5>

### Cisco beats on earnings, says AI infrastructure revenue will double this fiscal year
- Summary: Cisco exceeded earnings expectations, projecting AI infrastructure revenue to double this fiscal year.
- Date: 2026-11-12 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMickFVX3lxTFBXZ1VHS3FlM0xwR1ctNVZGd255am4zdHdQUUhBVjdyRmVoRy05RkZPcGQ2RUgzUFVsSlk1YTQ5aUZTM1lhZmFPT2lXUXY4NzcwanBweWVNN3RMSklUdzBfdDg5MUtfMzY0Qi1FMmpHT19sZ9IBd0FVX3lxTFB0dFNlWHZZSG04enVwQmRHZ3J3LUtIT3ZUdF9ESkVzZExBaWJFSTVjcGZxbkFxUVl2VFZ3dkFBTVFVc0dWTG5INTRlMDBqT1VudEJYZ0xOX0NiUzVPSEtoUzhfRlh5bmlMMWZjaHExV0dPTVBra2hv?oc=5>

### The Zacks Analyst Blog Highlights Cisco Systems and Cloudflare
- Summary: Zacks analyst blog spotlights Cisco, suggesting positive analyst sentiment and potential upside.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxOaXdpYl9uYko2SDlBcjhRejd2QWdWNjlTcV9zejNXUlY2a3FKMHMwR1RyN2phc0ZjX0ladUN6eFEyYjZCVHNkOVcxN1BMVGpxZWl4UjlrSnhJUEZDWHlicWdTaUROdkxKU2FZOGZQRm9wSnV6QThGY093SnROUzh1MzI0azZsaDdKQjNpRHRqalhUaGlzZzNSTzRHLXV2N3NrdkE?oc=5>

### Cisco Systems (CSCO) stock price forecast: AI growth lifts 2027 outlook
- Summary: Cisco forecasts higher 2027 revenue driven by AI networking demand.
- Date: 2026-11-13 | Impact: high | Horizon: long | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNREc4d3FjZnNwdHpRWlE1djNlenBtYzZJbkFieTNWcVhuXzMxamVyeDJlQTQ5ZVg2UjI1YWcyUENfU3A1QklrZHR0TVJBY0pqUElxNUduNjhpZzNRbmM2WEhUeFhmTmxCS2M2X2dVVG9HNWl4TjNLQmNMUG8zLTE0MTJiWEFIdGYzU1FyVWcxQTEzQWZzT180M3ZoNA?oc=5>

## HEADWINDS

### Cisco Stocks Fall 5.29% as AI Networking Mix Squeezes Gross Margins
- Summary: Cisco Stocks Fall 5.29% as AI Networking Mix Squeezes Gross Margins
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxOTHpSRFcxQ044ZXdXUDR6TkJYWDU4Z2hoMjJLSk9XTm9NN3hVYTBqY3hiUW5OTjNUVWlLcWZPU0lMYTBlSlowbHhSVFQ3SExOY0dQcUF6X2ppWkI1U09YTzdqeW8zS1o4VEZaQzdZTXoyOFd4OGdOWnpTNTRFa2tEOGlmU1J0MFVRQ2F0Zld0aVU?oc=5>

## CATALYSTS

### Cisco Q1 Earnings – Here’s What Analysts Expect from CSCO Stock amid AI Trade Concerns
- Summary: Cisco Q1 Earnings – Here’s What Analysts Expect from CSCO Stock amid AI Trade Concerns
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOajdxTFFHUlRraWFsc0pSekZYRktYRFZVRnVEZDZWc0p0clZaRUNYMjFaMjVHVU9UQzZ0X1cwcE9hWFBLWjBuSGdiSFZ4dmMtcklIUG1YVzgyU19mVm13UnA2OXdZTVNlY2JDVGZMREVfUlVfTGtscTRLVlFhN1hBR2YyejZTLWhsakJSWktCZ09wQ0ZrbV9RVmZseGNZdG8?oc=5>

### Cisco (CSCO) Reports Q1 Earnings: What Key Metrics Have to Say
- Summary: Cisco (CSCO) Reports Q1 Earnings: What Key Metrics Have to Say
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOTFIyN2F2c28zSndhdFk0UUtQcHlpZTNEbkpYdFdsSmpsYzZLZDFOVk0wZzdMWmU5MUhoQnBlUllpbnA2R044dlVhSVd6QXhzQWhZN0FYLVVHRVp5ZloxQ2VrcXUyam1DbF9nMkFwQlJMYXNQQjNacEhJV3NRTk0yRU5qanlQd1pHRjdmd2NmeXh3SXp2T3lNZFRlVQ?oc=5>

### Cisco (CSCO) vs. ANET and HPE: Can AI Networking Turn Strong Orders Into Lasting Earnings Growth?
- Summary: Questioning whether AI networking can convert strong orders into sustained earnings growth.
- Date: 2026-11-12 | Impact: medium | Horizon: medium | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxQSGozWEcxNGh2Nk0zaHFIbnFXSTg1UGNpWEdSUDdMUHFWdzRreV9meUprdGpHZWpMZTRHdmd2QzVTMXhfWjl6VlhBX3Z4RW5oRGFlT3VqZkV5WUlLbmYyVHppSnlxR0pUbVdfZEFqdlRORHRrcUlaeW1OWlZoMHN5VjNpN0hMdnhQaG5qQXpBTGM?oc=5>

### Ahead of Cisco Earnings, Here's What Barchart Data Says Comes Next for CSCO Stock
- Summary: Market data predicts post-earnings movement.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQOTA3ZmRSaHdoS2dnM1JoMnRtSHVoU01iR25wLWVTN3JXZ1psVWRld2wxeGJDMy1lQnhpTXdEUnBCWjRRbzhHOFlVekx4VmNUUFB6eTdCQnNpcWNFa3BQMzJodU1XRlltM1B4M3BaWW9FWHBDV0hfc05ndnhPXzZ1MnQtMVRsWVliNnp1UUZWem5tTi0yaEJhTm5CSnd5WnljNEE?oc=5>

### 48 ETFs Add to Cisco (CSCO) Holdings on Nov. 10
- Summary: 48 ETFs increased their Cisco holdings on Nov. 10, indicating growing institutional interest.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxOdlZVMnQ0SkpReExZSW9ocmIzelZpa2k1aE5hYnVoSHZRbFowaHZ1cDBKZzlvQ3YxSkhoX0JEa01MTG8tel9vRWhjd3V2aXhJM3k4R0xTcTNIU3lzMEVFdENjZWhMNUpLVGtGazhGSnZKVTFJVVJxU3d4QTVNR2NVVWZ6enRsNDQ1NkRGWDR3ZEU?oc=5>

### Will Cisco (CSCO) Beat Estimates Again in Its Next Earnings Report?
- Summary: Questioning Cisco's ability to exceed earnings estimates.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNRGJRSG9SOERDYW9PNnVvRXdCY0haNHB3MDVwM0hXMmhERnVrOHBRTElLRTkxQUNtRF9RSk5DOXZhS09FMTE3c0pNLXFnV04xWmZMUXVjYXRCMXNvM00zX2k3c1pxcExOQ3U0QzhDcm5YbDN4TGd2c3NrdVE3d3V4dTg0RGo1MmlGQTgwZEV4YkZDdm81S1FIMzJ3ZEc?oc=5>

### Cisco lifts annual revenue forecast on strong AI networking demand
- Summary: Cisco raises annual revenue outlook due to AI demand.
- Date: 2026-11-12 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxPcDgteG5IeXZjU1k1UDdhbFkyZlVCaHI1d0pPdGp2elFReVRRclN6dWhTM2NuSUk3cGdUSnRRU2c4aWpCcS14blFsN3hLTTNCSktQbXpTUVgxRjVJV1R1YldHdEVYMXJvVHg3TzJiOXhEM0owM08ySlI1bmNkMG5GQXhnQl9iVExNWlN1Z0ZweFk3YldGWDltNFpnekdDZWpVcTJ3QTFlUUxNWXlLX0NjLUhvTjRtNzlrYnlXdXJiTmc?oc=5>

### US AI Data Centers ‘Are Going to Get Built’ Despite Political Pushback, Says Cisco CEO: ‘Too Important to Our Country’
- Summary: Cisco CEO announces plans to build AI data centers despite political pushback, emphasizing their national importance.
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNckJ4NmZvWFF5RVVvbHZJYTRnR2p0aGdEWElXeDR1VEJia2lNcDkyR0luMEoyU0dMd2JKdTZLOFRZVE4xakhwaURfYldpSm1qRmpzbEREbHQ1NmcteDNjR1JyWFdJbnhhTy0zanhGaDRpQTBqeHc0SjFCODJGQ09tWTlPVDlQVi1CRmpmc2lOdXVQUQ?oc=5>

### Cisco: Better Earnings, Cheaper Stock (NASDAQ:CSCO)
- Summary: Cisco reports improved earnings and a lower stock price, indicating stronger financial performance and potential upside for investors.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxOQW1JNjZlRklwSUJiX3pwLW13UG5WZF9NbTc3Mlk4dmhTeUNReWlfLWloUFNrbG5GY3ZfczdIZ0tHbUI0VGZ4dGFub252Z3dfMTdGX0ZDQi1LRVVxYW1wdkhlLXRhbzAyMXhsMHVUcXExRWlHbW52N2EyRlQ0OThlOWhB?oc=5>

## RISKS

### Cisco Systems (CSCO) Tied To FAA Ground Stop After Router Failures Hit Flights
- Summary: Router failures linked to FAA ground stop, impacting flight operations.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNOUtrNHlJcnBPQU5yVmpMeENvZG14bThqM2UzRmFsWEd2VUpEa21JWEduak84czByeUJpNkFaNWxrbEtnQlI0SDlyTEVpZUxELV9vdTdBYkt0VmhaNFcxX0xLRTRMSkxkWllwZ0lRaU9hV0VhcUZIR2FJNjAtT2ItQ1RPRGFPTnJSb09nQUZyN1JZdw?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CSCO** | **25.14** | **7.23** | **18.71** | **24.40** | **372,123,369,472.00 USD** | **23.42** |
| ANET | 52.83 | 14.37 | 41.84 | 58.50 | 236,281,511,936.00 USD | 42.36 |
| FFIV | 24.34 | 4.32 | 17.21 | 13.30 | 17,309,175,808.00 USD | 30.21 |
| HPE | 24.90 | 2.33 | 11.03 | 33.70 | 61,820,035,072.00 USD | 107.66 |

Peers fetched as_of: 2026-11-16; CSCO reuses existing data (market data as_of: 2026-11-16); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-12
- Next expected earnings: 2027-02-10 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-16

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-09-02
- Revenue (latest available single quarter): 12,844,000,000.00 USD; period 2018-04-29/2018-07-28; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 3,373,000,000.00 USD; period 2026-01-25/2026-04-25; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/858877/000085887726000132/csco-20260725.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMijgFBVV95cUxOVjM1UkllWHBNT1lVUjRmSVVIMmhCYnhobEc0VTRtcGZpOWVyaVM4WTRkYXR0VkJ4MTJjLWlJMjZ4SjRPYVZXcV9ScGVZT1RhcUFZQk5YM25qUzQ2QkNDYU1abUlhWDNkRFkwd3ZFRVlXSENwT2MxNTZBZkV5b2swYkVBSUY4bUUxdHR6ZHJB?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxNRVcxQXB4NnpKcjdLV2NnTHNveFFIUnllVU9ZSDdReG9iSnJMRTJKRExTSmhWNDNRLTloM1g0MjZYaXh0S2NfdjlMeWNxdnUwRnlTaTg1czdsZTF5Z2tkOVg2RkJ5U19qR0ZVRVJOWDlWTFE2cG1wSlR2Q2ZOODcwcnFvb2V0ZU9mSTFKV1NtelFhWnlEWHlPZEhzdTNRdw?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQc3NMbXh0VkFHZnEtalpOX055M2haeWpleW5zdFlYVHlpQjJzS2JLY1A1OVBhUzFfbUhQWUlqWHY2U1JEb3hZTTZDR0hqUW9TVkUxNWpFZmlMckRfZS05TUZIRjBRT3NFTjh2OXpQRUdqRFVFemNlOVdHa0pIalJ6VVRkWWs1ejM1RkdnZ25SZ2FGMU5vSVNBZzF3OA?oc=5
- https://news.google.com/rss/articles/CBMickFVX3lxTFBXZ1VHS3FlM0xwR1ctNVZGd255am4zdHdQUUhBVjdyRmVoRy05RkZPcGQ2RUgzUFVsSlk1YTQ5aUZTM1lhZmFPT2lXUXY4NzcwanBweWVNN3RMSklUdzBfdDg5MUtfMzY0Qi1FMmpHT19sZ9IBd0FVX3lxTFB0dFNlWHZZSG04enVwQmRHZ3J3LUtIT3ZUdF9ESkVzZExBaWJFSTVjcGZxbkFxUVl2VFZ3dkFBTVFVc0dWTG5INTRlMDBqT1VudEJYZ0xOX0NiUzVPSEtoUzhfRlh5bmlMMWZjaHExV0dPTVBra2hv?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOaXdpYl9uYko2SDlBcjhRejd2QWdWNjlTcV9zejNXUlY2a3FKMHMwR1RyN2phc0ZjX0ladUN6eFEyYjZCVHNkOVcxN1BMVGpxZWl4UjlrSnhJUEZDWHlicWdTaUROdkxKU2FZOGZQRm9wSnV6QThGY093SnROUzh1MzI0azZsaDdKQjNpRHRqalhUaGlzZzNSTzRHLXV2N3NrdkE?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNREc4d3FjZnNwdHpRWlE1djNlenBtYzZJbkFieTNWcVhuXzMxamVyeDJlQTQ5ZVg2UjI1YWcyUENfU3A1QklrZHR0TVJBY0pqUElxNUduNjhpZzNRbmM2WEhUeFhmTmxCS2M2X2dVVG9HNWl4TjNLQmNMUG8zLTE0MTJiWEFIdGYzU1FyVWcxQTEzQWZzT180M3ZoNA?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxOTHpSRFcxQ044ZXdXUDR6TkJYWDU4Z2hoMjJLSk9XTm9NN3hVYTBqY3hiUW5OTjNUVWlLcWZPU0lMYTBlSlowbHhSVFQ3SExOY0dQcUF6X2ppWkI1U09YTzdqeW8zS1o4VEZaQzdZTXoyOFd4OGdOWnpTNTRFa2tEOGlmU1J0MFVRQ2F0Zld0aVU?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOajdxTFFHUlRraWFsc0pSekZYRktYRFZVRnVEZDZWc0p0clZaRUNYMjFaMjVHVU9UQzZ0X1cwcE9hWFBLWjBuSGdiSFZ4dmMtcklIUG1YVzgyU19mVm13UnA2OXdZTVNlY2JDVGZMREVfUlVfTGtscTRLVlFhN1hBR2YyejZTLWhsakJSWktCZ09wQ0ZrbV9RVmZseGNZdG8?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOTFIyN2F2c28zSndhdFk0UUtQcHlpZTNEbkpYdFdsSmpsYzZLZDFOVk0wZzdMWmU5MUhoQnBlUllpbnA2R044dlVhSVd6QXhzQWhZN0FYLVVHRVp5ZloxQ2VrcXUyam1DbF9nMkFwQlJMYXNQQjNacEhJV3NRTk0yRU5qanlQd1pHRjdmd2NmeXh3SXp2T3lNZFRlVQ?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxQSGozWEcxNGh2Nk0zaHFIbnFXSTg1UGNpWEdSUDdMUHFWdzRreV9meUprdGpHZWpMZTRHdmd2QzVTMXhfWjl6VlhBX3Z4RW5oRGFlT3VqZkV5WUlLbmYyVHppSnlxR0pUbVdfZEFqdlRORHRrcUlaeW1OWlZoMHN5VjNpN0hMdnhQaG5qQXpBTGM?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQOTA3ZmRSaHdoS2dnM1JoMnRtSHVoU01iR25wLWVTN3JXZ1psVWRld2wxeGJDMy1lQnhpTXdEUnBCWjRRbzhHOFlVekx4VmNUUFB6eTdCQnNpcWNFa3BQMzJodU1XRlltM1B4M3BaWW9FWHBDV0hfc05ndnhPXzZ1MnQtMVRsWVliNnp1UUZWem5tTi0yaEJhTm5CSnd5WnljNEE?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxOdlZVMnQ0SkpReExZSW9ocmIzelZpa2k1aE5hYnVoSHZRbFowaHZ1cDBKZzlvQ3YxSkhoX0JEa01MTG8tel9vRWhjd3V2aXhJM3k4R0xTcTNIU3lzMEVFdENjZWhMNUpLVGtGazhGSnZKVTFJVVJxU3d4QTVNR2NVVWZ6enRsNDQ1NkRGWDR3ZEU?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNRGJRSG9SOERDYW9PNnVvRXdCY0haNHB3MDVwM0hXMmhERnVrOHBRTElLRTkxQUNtRF9RSk5DOXZhS09FMTE3c0pNLXFnV04xWmZMUXVjYXRCMXNvM00zX2k3c1pxcExOQ3U0QzhDcm5YbDN4TGd2c3NrdVE3d3V4dTg0RGo1MmlGQTgwZEV4YkZDdm81S1FIMzJ3ZEc?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxPcDgteG5IeXZjU1k1UDdhbFkyZlVCaHI1d0pPdGp2elFReVRRclN6dWhTM2NuSUk3cGdUSnRRU2c4aWpCcS14blFsN3hLTTNCSktQbXpTUVgxRjVJV1R1YldHdEVYMXJvVHg3TzJiOXhEM0owM08ySlI1bmNkMG5GQXhnQl9iVExNWlN1Z0ZweFk3YldGWDltNFpnekdDZWpVcTJ3QTFlUUxNWXlLX0NjLUhvTjRtNzlrYnlXdXJiTmc?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNckJ4NmZvWFF5RVVvbHZJYTRnR2p0aGdEWElXeDR1VEJia2lNcDkyR0luMEoyU0dMd2JKdTZLOFRZVE4xakhwaURfYldpSm1qRmpzbEREbHQ1NmcteDNjR1JyWFdJbnhhTy0zanhGaDRpQTBqeHc0SjFCODJGQ09tWTlPVDlQVi1CRmpmc2lOdXVQUQ?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxOQW1JNjZlRklwSUJiX3pwLW13UG5WZF9NbTc3Mlk4dmhTeUNReWlfLWloUFNrbG5GY3ZfczdIZ0tHbUI0VGZ4dGFub252Z3dfMTdGX0ZDQi1LRVVxYW1wdkhlLXRhbzAyMXhsMHVUcXExRWlHbW52N2EyRlQ0OThlOWhB?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNOUtrNHlJcnBPQU5yVmpMeENvZG14bThqM2UzRmFsWEd2VUpEa21JWEduak84czByeUJpNkFaNWxrbEtnQlI0SDlyTEVpZUxELV9vdTdBYkt0VmhaNFcxX0xLRTRMSkxkWllwZ0lRaU9hV0VhcUZIR2FJNjAtT2ItQ1RPRGFPTnJSb09nQUZyN1JZdw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
