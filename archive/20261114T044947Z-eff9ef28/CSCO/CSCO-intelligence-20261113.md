# CSCO Intelligence Report

- ticker: **CSCO**
- Report as_of: **2026-11-13**
- Market data as_of: **2026-11-13**
- Quant sources: https://finance.yahoo.com/quote/CSCO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CSCO/key-statistics/
- AI analysis snapshot as_of: **2026-11-13**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-14T04:53:38.218014+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 6, 'ai': 13, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261113T045636Z-34122c9a/CSCO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 2}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 7 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 72.0%; oldest publication 2026-11-09

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 95.6400 |
| Return 1D (%) | -6.2445 |
| Return 1W (%) | 1.9073 |
| Return 1M (%) | -16.8854 |
| Return YTD (%) | 26.4580 |
| Return 1Y (%) | 25.8860 |
| Annualized volatility (%) | 37.0707 |
| Beta vs SPY | 1.3164 |
| Max drawdown (%) | -27.2567 |
| Sharpe (rf=0) | 0.8094 |
| Downside deviation (rf=0, %) | 26.1863 |
| Sortino (rf=0) | 1.1458 |
| Historical VaR 95% (1D, %) | 3.2126 |
| Historical ES 95% (1D, %) | 5.5834 |
| Correlation vs SPY | 0.4841 |
| Tracking error vs SPY (%) | 32.7220 |
| P/E (trailing) | 27.09 |
| P/B | 7.51 |
| EV/EBITDA | 22.39 |
| Revenue growth (%) | 17.60 |
| Forward P/E (estimate) | 16.12 |
| Gross margin (%) | 64.52 |
| Operating margin (%) | 25.39 |
| Return on equity (%) | 27.32 |
| Free cash flow yield (%) | 2.97 |
| MA50 | 107.5971 |
| Close vs MA50 (%) | -11.1128 |
| MA200 | 101.7414 |
| Close vs MA200 (%) | -5.9969 |
| RSI (14, Wilder) | 37.1415 |
| MACD (12,26) | -3.2089 |
| MACD signal (9) | -2.7085 |
| MACD histogram | -0.5003 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CSCO': 282, 'SPY': 282}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 95.6400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -6.2445 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.9073 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -16.8854 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 26.4580 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 25.8860 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 37.0707 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.1863 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.1458 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.2126 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.5834 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4841 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.7220 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.3164 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.2567 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.8094 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.1229 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 64.5240 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 25.3910 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 27.3190 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.9657 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 27.0935 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 37.1415 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.5003 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -11.1128 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -5.9969 -> Clearly below the moving-average trend level.

## TAILWINDS

### Cisco Stock (CSCO) Jumps 5% as Financial Results Top Wall Street Estimates
- Summary: Cisco Stock (CSCO) Jumps 5% as Financial Results Top Wall Street Estimates
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPeWVsTjlzSXpZZ0p2Vy05QV9DSXZBNlAyVktuSC1OWTB4UXRwQ1l3Vjh3cGx6STV0TllUS0U0by1IdGY4M1FqVWpzQUsxbGNTNEE0b05HZThfdTAzMmtqQzRhRlRNajJvTk11Ry14OXQ5ZXRIWER3WlZSVE01YWVfUElreVVmNEg4NkU2NFM4dnpyZmlGbDRZZ3A1bUNiRXNHcTVZ?oc=5>

### Cisco Systems (CSCO) Q1 Earnings and Revenues Beat Estimates
- Summary: Cisco Systems (CSCO) Q1 Earnings and Revenues Beat Estimates
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQc3NMbXh0VkFHZnEtalpOX055M2haeWpleW5zdFlYVHlpQjJzS2JLY1A1OVBhUzFfbUhQWUlqWHY2U1JEb3hZTTZDR0hqUW9TVkUxNWpFZmlMckRfZS05TUZIRjBRT3NFTjh2OXpQRUdqRFVFemNlOVdHa0pIalJ6VVRkWWs1ejM1RkdnZ25SZ2FGMU5vSVNBZzF3OA?oc=5>

### Cisco beats on earnings, says AI infrastructure revenue will double this fiscal year
- Summary: Cisco exceeded earnings expectations, projecting AI infrastructure revenue to double this fiscal year.
- Date: 2026-11-12 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMickFVX3lxTFBXZ1VHS3FlM0xwR1ctNVZGd255am4zdHdQUUhBVjdyRmVoRy05RkZPcGQ2RUgzUFVsSlk1YTQ5aUZTM1lhZmFPT2lXUXY4NzcwanBweWVNN3RMSklUdzBfdDg5MUtfMzY0Qi1FMmpHT19sZ9IBd0FVX3lxTFB0dFNlWHZZSG04enVwQmRHZ3J3LUtIT3ZUdF9ESkVzZExBaWJFSTVjcGZxbkFxUVl2VFZ3dkFBTVFVc0dWTG5INTRlMDBqT1VudEJYZ0xOX0NiUzVPSEtoUzhfRlh5bmlMMWZjaHExV0dPTVBra2hv?oc=5>

### Cisco Systems (CSCO) stock price forecast: AI growth lifts 2027 outlook
- Summary: Cisco forecasts higher 2027 revenue driven by AI networking demand.
- Date: 2026-11-13 | Impact: high | Horizon: long | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNREc4d3FjZnNwdHpRWlE1djNlenBtYzZJbkFieTNWcVhuXzMxamVyeDJlQTQ5ZVg2UjI1YWcyUENfU3A1QklrZHR0TVJBY0pqUElxNUduNjhpZzNRbmM2WEhUeFhmTmxCS2M2X2dVVG9HNWl4TjNLQmNMUG8zLTE0MTJiWEFIdGYzU1FyVWcxQTEzQWZzT180M3ZoNA?oc=5>

### The Zacks Analyst Blog Highlights Cisco Systems and Cloudflare
- Summary: Zacks analyst blog spotlights Cisco, suggesting positive analyst sentiment and potential upside.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxOaXdpYl9uYko2SDlBcjhRejd2QWdWNjlTcV9zejNXUlY2a3FKMHMwR1RyN2phc0ZjX0ladUN6eFEyYjZCVHNkOVcxN1BMVGpxZWl4UjlrSnhJUEZDWHlicWdTaUROdkxKU2FZOGZQRm9wSnV6QThGY093SnROUzh1MzI0azZsaDdKQjNpRHRqalhUaGlzZzNSTzRHLXV2N3NrdkE?oc=5>

## HEADWINDS

### Cisco Stocks Fall 5.29% as AI Networking Mix Squeezes Gross Margins
- Summary: Cisco Stocks Fall 5.29% as AI Networking Mix Squeezes Gross Margins
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxOTHpSRFcxQ044ZXdXUDR6TkJYWDU4Z2hoMjJLSk9XTm9NN3hVYTBqY3hiUW5OTjNUVWlLcWZPU0lMYTBlSlowbHhSVFQ3SExOY0dQcUF6X2ppWkI1U09YTzdqeW8zS1o4VEZaQzdZTXoyOFd4OGdOWnpTNTRFa2tEOGlmU1J0MFVRQ2F0Zld0aVU?oc=5>

### Cisco shares down as focus turns to margins (CSCO:NASDAQ)
- Summary: Cisco shares down as focus turns to margins (CSCO:NASDAQ)
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxOMjNzZmpCMl9uenRQcVhPd2FCdTVNQnZka3J1dE9ZN1l0NElLckxiZTRJdVhGd0Z1MnBfUFFTUjBkN0xITGtJYV8yWGlndVRoQWNLM3RuREx2VjNPOFpVSmpJMmJYbVIyTGFMQTRtWVhvNTdERUltOFFnVlR4YmxrSDhtZGFNX281?oc=5>

### What Cisco Systems (CSCO) Said on Its Q1 Earnings Call
- Summary: Details from Cisco's Q1 earnings call.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNR2dtSnNvQVpZSWNvTjRodmZ1Q1phWkhicVM4Wjd1VE5BWTRwNjZkX2dCdnpfLV8za2NMU3AzWHlCb3h6NEtwRjZuV1pOanlCYU1uM2x0ZFZFcmo0T25oN21iZjlNekJWZ1U0YUVXdEo0QXZGUFpuTGpBZjdsNVpPZjM5elNDa2Y0b091X1ZpanNRV2ZRbUE?oc=5>

### Cisco’s Growth May Have Peaked Despite Raised AI Revenue Outlook, Says Citi — Barclays Sees Margins Holding Up
- Summary: Citi signals growth peak; mixed outlook may dampen investor enthusiasm.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQU296WWh2dWhYa0dscGY4S1J1NXctalp4YmhOQWFpOS1id1dORzEyM3B2czB2SjVGWjlQTzIxN2hOMHJTYzFZUFNOR29ZRjY0OVRLalZTdDVQUjhkOTJ3c0JGaVFoc2E1aFFLN3JfTEtzc2JBQUFhZkw3b3l2WEdGQXpEdk0xOWdESEx6aXdrNFkxM2o1OGZmUGZuWDk?oc=5>

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

### Will Cisco Systems (CSCO) Deliver the Strong Results the Market Needs to See?
- Summary: Querying Cisco's ability to meet market expectations for strong results.
- Date: 2026-11-09 | Impact: medium | Horizon: medium | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQSjRuWWVZQzNFa3hnMzB4U0VKc21CcHZPeXE0OTc4dVgzdHRycVpOYXJrbWpPanRiTTVUOXBDRTZFMk9WZlNIVFY3UW5hOXpzMFhqOFlxRUVPV0dFN2FrdVFWZU1XdFJyVXFCU0tuM0huMUU1VG8tdmhQOEh0OGx0dDlDVUJCS1I2NHpsSGFmWlIzQnZpZFpsR0ZGcERmNmc?oc=5>

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

### ‘Still Early In Networking Super Cycle’: Cisco Delivers Beat And Raise Quarter But Shares Drop Amid Nvidia-Linked Volatility
- Summary: Cisco beats earnings and raises outlook, but shares fall due to broader market volatility.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOY19wcldBYlMxclFIWE8zTzY3OEVzWHZKXzRTQjNnNnhIS2Q5M2JySEd2RldMbVJQY2U5bHJKb192Nnp4ZU1jMmlNMkthblBNSWJyUG14NGNDY1FHNW1BMEp1eU5OOC1TYVk4TVMyZTZhVENfUVRfM1djWXBzM0o2S3JvTjU4MFU0dDctVnhNR1RYWlpYajJnMWlxMlU5VTdJ?oc=5>

### Cisco: Accelerating Growth Drives Big Earnings Beat (NASDAQ:CSCO)
- Summary: Cisco reports earnings that exceed expectations, driven by accelerated growth across its portfolio.
- Date: 2026-11-13 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOWUNacVM1Tjc2MWdsZE8yNzc1V0hkUGtFOVVraER6ZTBzZFZVNUItVUZXNk5pUTZNRkVRQUF6QXNTZ1ZqSEQyYUxFSzRhbjljQldXWEdkdzFUQ2FDd2tvMkRsVmdKc2Y1eTV1VG9sMmhsUTJNUzB6Q0ZodVM0bTNvMklKb3FrdXRVNWotVjdaenBrR2hFdVE?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CSCO** | **27.09** | **7.51** | **22.39** | **17.60** | **377,069,010,944.00 USD** | **25.89** |
| ANET | 55.42 | 15.16 | 44.28 | 58.50 | 249,256,640,512.00 USD | 51.41 |
| FFIV | 25.38 | 4.38 | 17.49 | 13.30 | 17,562,554,368.00 USD | 29.42 |
| HPE | 25.82 | 2.42 | 11.36 | 33.70 | 64,103,276,544.00 USD | 114.39 |

Peers fetched as_of: 2026-11-13; CSCO reuses existing data (market data as_of: 2026-11-13); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-12
- Next expected earnings: 2027-02-10 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-13

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

- https://news.google.com/rss/articles/CBMiowFBVV95cUxPeWVsTjlzSXpZZ0p2Vy05QV9DSXZBNlAyVktuSC1OWTB4UXRwQ1l3Vjh3cGx6STV0TllUS0U0by1IdGY4M1FqVWpzQUsxbGNTNEE0b05HZThfdTAzMmtqQzRhRlRNajJvTk11Ry14OXQ5ZXRIWER3WlZSVE01YWVfUElreVVmNEg4NkU2NFM4dnpyZmlGbDRZZ3A1bUNiRXNHcTVZ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQc3NMbXh0VkFHZnEtalpOX055M2haeWpleW5zdFlYVHlpQjJzS2JLY1A1OVBhUzFfbUhQWUlqWHY2U1JEb3hZTTZDR0hqUW9TVkUxNWpFZmlMckRfZS05TUZIRjBRT3NFTjh2OXpQRUdqRFVFemNlOVdHa0pIalJ6VVRkWWs1ejM1RkdnZ25SZ2FGMU5vSVNBZzF3OA?oc=5
- https://news.google.com/rss/articles/CBMickFVX3lxTFBXZ1VHS3FlM0xwR1ctNVZGd255am4zdHdQUUhBVjdyRmVoRy05RkZPcGQ2RUgzUFVsSlk1YTQ5aUZTM1lhZmFPT2lXUXY4NzcwanBweWVNN3RMSklUdzBfdDg5MUtfMzY0Qi1FMmpHT19sZ9IBd0FVX3lxTFB0dFNlWHZZSG04enVwQmRHZ3J3LUtIT3ZUdF9ESkVzZExBaWJFSTVjcGZxbkFxUVl2VFZ3dkFBTVFVc0dWTG5INTRlMDBqT1VudEJYZ0xOX0NiUzVPSEtoUzhfRlh5bmlMMWZjaHExV0dPTVBra2hv?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNREc4d3FjZnNwdHpRWlE1djNlenBtYzZJbkFieTNWcVhuXzMxamVyeDJlQTQ5ZVg2UjI1YWcyUENfU3A1QklrZHR0TVJBY0pqUElxNUduNjhpZzNRbmM2WEhUeFhmTmxCS2M2X2dVVG9HNWl4TjNLQmNMUG8zLTE0MTJiWEFIdGYzU1FyVWcxQTEzQWZzT180M3ZoNA?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOaXdpYl9uYko2SDlBcjhRejd2QWdWNjlTcV9zejNXUlY2a3FKMHMwR1RyN2phc0ZjX0ladUN6eFEyYjZCVHNkOVcxN1BMVGpxZWl4UjlrSnhJUEZDWHlicWdTaUROdkxKU2FZOGZQRm9wSnV6QThGY093SnROUzh1MzI0azZsaDdKQjNpRHRqalhUaGlzZzNSTzRHLXV2N3NrdkE?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxOTHpSRFcxQ044ZXdXUDR6TkJYWDU4Z2hoMjJLSk9XTm9NN3hVYTBqY3hiUW5OTjNUVWlLcWZPU0lMYTBlSlowbHhSVFQ3SExOY0dQcUF6X2ppWkI1U09YTzdqeW8zS1o4VEZaQzdZTXoyOFd4OGdOWnpTNTRFa2tEOGlmU1J0MFVRQ2F0Zld0aVU?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxOMjNzZmpCMl9uenRQcVhPd2FCdTVNQnZka3J1dE9ZN1l0NElLckxiZTRJdVhGd0Z1MnBfUFFTUjBkN0xITGtJYV8yWGlndVRoQWNLM3RuREx2VjNPOFpVSmpJMmJYbVIyTGFMQTRtWVhvNTdERUltOFFnVlR4YmxrSDhtZGFNX281?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNR2dtSnNvQVpZSWNvTjRodmZ1Q1phWkhicVM4Wjd1VE5BWTRwNjZkX2dCdnpfLV8za2NMU3AzWHlCb3h6NEtwRjZuV1pOanlCYU1uM2x0ZFZFcmo0T25oN21iZjlNekJWZ1U0YUVXdEo0QXZGUFpuTGpBZjdsNVpPZjM5elNDa2Y0b091X1ZpanNRV2ZRbUE?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQU296WWh2dWhYa0dscGY4S1J1NXctalp4YmhOQWFpOS1id1dORzEyM3B2czB2SjVGWjlQTzIxN2hOMHJTYzFZUFNOR29ZRjY0OVRLalZTdDVQUjhkOTJ3c0JGaVFoc2E1aFFLN3JfTEtzc2JBQUFhZkw3b3l2WEdGQXpEdk0xOWdESEx6aXdrNFkxM2o1OGZmUGZuWDk?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOajdxTFFHUlRraWFsc0pSekZYRktYRFZVRnVEZDZWc0p0clZaRUNYMjFaMjVHVU9UQzZ0X1cwcE9hWFBLWjBuSGdiSFZ4dmMtcklIUG1YVzgyU19mVm13UnA2OXdZTVNlY2JDVGZMREVfUlVfTGtscTRLVlFhN1hBR2YyejZTLWhsakJSWktCZ09wQ0ZrbV9RVmZseGNZdG8?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOTFIyN2F2c28zSndhdFk0UUtQcHlpZTNEbkpYdFdsSmpsYzZLZDFOVk0wZzdMWmU5MUhoQnBlUllpbnA2R044dlVhSVd6QXhzQWhZN0FYLVVHRVp5ZloxQ2VrcXUyam1DbF9nMkFwQlJMYXNQQjNacEhJV3NRTk0yRU5qanlQd1pHRjdmd2NmeXh3SXp2T3lNZFRlVQ?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxQSGozWEcxNGh2Nk0zaHFIbnFXSTg1UGNpWEdSUDdMUHFWdzRreV9meUprdGpHZWpMZTRHdmd2QzVTMXhfWjl6VlhBX3Z4RW5oRGFlT3VqZkV5WUlLbmYyVHppSnlxR0pUbVdfZEFqdlRORHRrcUlaeW1OWlZoMHN5VjNpN0hMdnhQaG5qQXpBTGM?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQSjRuWWVZQzNFa3hnMzB4U0VKc21CcHZPeXE0OTc4dVgzdHRycVpOYXJrbWpPanRiTTVUOXBDRTZFMk9WZlNIVFY3UW5hOXpzMFhqOFlxRUVPV0dFN2FrdVFWZU1XdFJyVXFCU0tuM0huMUU1VG8tdmhQOEh0OGx0dDlDVUJCS1I2NHpsSGFmWlIzQnZpZFpsR0ZGcERmNmc?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQOTA3ZmRSaHdoS2dnM1JoMnRtSHVoU01iR25wLWVTN3JXZ1psVWRld2wxeGJDMy1lQnhpTXdEUnBCWjRRbzhHOFlVekx4VmNUUFB6eTdCQnNpcWNFa3BQMzJodU1XRlltM1B4M3BaWW9FWHBDV0hfc05ndnhPXzZ1MnQtMVRsWVliNnp1UUZWem5tTi0yaEJhTm5CSnd5WnljNEE?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxOdlZVMnQ0SkpReExZSW9ocmIzelZpa2k1aE5hYnVoSHZRbFowaHZ1cDBKZzlvQ3YxSkhoX0JEa01MTG8tel9vRWhjd3V2aXhJM3k4R0xTcTNIU3lzMEVFdENjZWhMNUpLVGtGazhGSnZKVTFJVVJxU3d4QTVNR2NVVWZ6enRsNDQ1NkRGWDR3ZEU?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNRGJRSG9SOERDYW9PNnVvRXdCY0haNHB3MDVwM0hXMmhERnVrOHBRTElLRTkxQUNtRF9RSk5DOXZhS09FMTE3c0pNLXFnV04xWmZMUXVjYXRCMXNvM00zX2k3c1pxcExOQ3U0QzhDcm5YbDN4TGd2c3NrdVE3d3V4dTg0RGo1MmlGQTgwZEV4YkZDdm81S1FIMzJ3ZEc?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxPcDgteG5IeXZjU1k1UDdhbFkyZlVCaHI1d0pPdGp2elFReVRRclN6dWhTM2NuSUk3cGdUSnRRU2c4aWpCcS14blFsN3hLTTNCSktQbXpTUVgxRjVJV1R1YldHdEVYMXJvVHg3TzJiOXhEM0owM08ySlI1bmNkMG5GQXhnQl9iVExNWlN1Z0ZweFk3YldGWDltNFpnekdDZWpVcTJ3QTFlUUxNWXlLX0NjLUhvTjRtNzlrYnlXdXJiTmc?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOY19wcldBYlMxclFIWE8zTzY3OEVzWHZKXzRTQjNnNnhIS2Q5M2JySEd2RldMbVJQY2U5bHJKb192Nnp4ZU1jMmlNMkthblBNSWJyUG14NGNDY1FHNW1BMEp1eU5OOC1TYVk4TVMyZTZhVENfUVRfM1djWXBzM0o2S3JvTjU4MFU0dDctVnhNR1RYWlpYajJnMWlxMlU5VTdJ?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOWUNacVM1Tjc2MWdsZE8yNzc1V0hkUGtFOVVraER6ZTBzZFZVNUItVUZXNk5pUTZNRkVRQUF6QXNTZ1ZqSEQyYUxFSzRhbjljQldXWEdkdzFUQ2FDd2tvMkRsVmdKc2Y1eTV1VG9sMmhsUTJNUzB6Q0ZodVM0bTNvMklKb3FrdXRVNWotVjdaenBrR2hFdVE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
