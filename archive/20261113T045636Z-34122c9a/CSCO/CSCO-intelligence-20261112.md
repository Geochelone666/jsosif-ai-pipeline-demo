# CSCO Intelligence Report

- ticker: **CSCO**
- Report as_of: **2026-11-12**
- Market data as_of: **2026-11-12**
- Quant sources: https://finance.yahoo.com/quote/CSCO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CSCO/key-statistics/
- AI analysis snapshot as_of: **2026-11-12**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-13T05:09:43.965624+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 11, 'ai': 9, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261112T054014Z-6c47e7f9/CSCO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 2}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 13 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 40.0%; oldest publication 2026-11-06

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 102.0100 |
| Return 1D (%) | 1.2406 |
| Return 1W (%) | 6.5713 |
| Return 1M (%) | -11.5571 |
| Return YTD (%) | 34.8806 |
| Return 1Y (%) | 40.4794 |
| Annualized volatility (%) | 36.7886 |
| Beta vs SPY | 1.2419 |
| Max drawdown (%) | -27.2567 |
| Sharpe (rf=0) | 1.1122 |
| Downside deviation (rf=0, %) | 25.4279 |
| Sortino (rf=0) | 1.6091 |
| Historical VaR 95% (1D, %) | 3.0714 |
| Historical ES 95% (1D, %) | 5.3408 |
| Correlation vs SPY | 0.4637 |
| Tracking error vs SPY (%) | 32.7639 |
| P/E (trailing) | 27.13 |
| P/B | 8.01 |
| EV/EBITDA | 22.39 |
| Revenue growth (%) | 17.60 |
| Forward P/E (estimate) | 18.14 |
| Gross margin (%) | 64.52 |
| Operating margin (%) | 25.39 |
| Return on equity (%) | 27.32 |
| Free cash flow yield (%) | 2.78 |
| MA50 | 107.8481 |
| Close vs MA50 (%) | -5.4132 |
| MA200 | 101.6502 |
| Close vs MA200 (%) | 0.3539 |
| RSI (14, Wilder) | 45.2937 |
| MACD (12,26) | -2.9484 |
| MACD signal (9) | -2.5834 |
| MACD histogram | -0.3650 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CSCO': 281, 'SPY': 281}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 102.0100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.2406 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 6.5713 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -11.5571 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 34.8806 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 40.4794 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 36.7886 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 25.4279 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.6091 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.0714 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.3408 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4637 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.7639 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.2419 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.2567 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1122 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 18.1385 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 64.5240 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 25.3910 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 27.3190 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.7805 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 27.1303 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 45.2937 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.3650 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -5.4132 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 0.3539 -> Slightly above the moving-average trend level.

## TAILWINDS

### Cisco Stock (CSCO) Jumps 5% as Financial Results Top Wall Street Estimates
- Summary: Cisco Stock (CSCO) Jumps 5% as Financial Results Top Wall Street Estimates
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPeWVsTjlzSXpZZ0p2Vy05QV9DSXZBNlAyVktuSC1OWTB4UXRwQ1l3Vjh3cGx6STV0TllUS0U0by1IdGY4M1FqVWpzQUsxbGNTNEE0b05HZThfdTAzMmtqQzRhRlRNajJvTk11Ry14OXQ5ZXRIWER3WlZSVE01YWVfUElreVVmNEg4NkU2NFM4dnpyZmlGbDRZZ3A1bUNiRXNHcTVZ?oc=5>

### Cisco stock rises after hours as earnings beat forecasts and its AI revenue outlook climbs to $9 billion
- Summary: Cisco stock rises after hours as earnings beat forecasts and its AI revenue outlook climbs to $9 billion
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxNbTY3eFZkZzlxcGFEN2p2Ump0TU41c1AtaWQ1QThmWWNpT3podHNxY094Z24ydHYxVkFpb2lfOGhNUVFDTFlUZDNhbi1FOGxzT3dPVkZxMHpqQjd5cUxQcjRfLU5Yei1HVEg0OGtWV21aTXJKUXJMUUdaSURVODFuRlBnYjJUX2NwWWl2TWNKUjVKbW9nTXBybkZJUVVncGdsSDVuQU5QTzVCTzMw?oc=5>

### Cisco Tops Q1 Estimates, Raises FY27 Outlook During Multi-Year Networking 'Supercycle'
- Summary: Cisco Tops Q1 Estimates, Raises FY27 Outlook During Multi-Year Networking 'Supercycle'
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxQMi0ySDZkbkRUeTVIb2ZsN3VrbzY3TC00UEozVDAyUzMzeklOVnRxTUpkMW5qOURWUW55TmtwWm8tS1pRcnZ0UDhUSnloY0RVaVdwMnNGTE0tNG93TUlvOEV3SlZkQThuZFZQZ2FWS2RYZm1nNkFlRmNSYjBuUkVqTDQ0R3I5VzZfR2V3ekF5TmwxeTNsdmNDT1dWTXhWWmxUN3E5LUY0UGRZT0swN0VCaHl5R3lrWlloaVhGbUNLSXFXSm5UQVNJd0VaYlhrcVl6bUlLc0ZtSQ?oc=5>

### Cisco Systems (CSCO) Q1 Earnings and Revenues Beat Estimates
- Summary: Cisco Systems (CSCO) Q1 Earnings and Revenues Beat Estimates
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQc3NMbXh0VkFHZnEtalpOX055M2haeWpleW5zdFlYVHlpQjJzS2JLY1A1OVBhUzFfbUhQWUlqWHY2U1JEb3hZTTZDR0hqUW9TVkUxNWpFZmlMckRfZS05TUZIRjBRT3NFTjh2OXpQRUdqRFVFemNlOVdHa0pIalJ6VVRkWWs1ejM1RkdnZ25SZ2FGMU5vSVNBZzF3OA?oc=5>

### Cisco (NASDAQ:CSCO) Earnings Beat: Revenue Surges 24% as AI Outlook Hits $9 Billion
- Summary: Cisco (NASDAQ:CSCO) Earnings Beat: Revenue Surges 24% as AI Outlook Hits $9 Billion
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMidkFVX3lxTE5nVl9zUnJ6djVKNG1TZTE2bUsycF82TThESVkxMUFBSERNQUpwSFh5ck14RUJpTGdoTXNYd3NFWXBrWTBwRUZNd0JoOUwzUm0wWUs2Zk1ZYWpya2djOS1XcGtRZ1FZMV9vc2t0eHkyaVdsdHVJTEE?oc=5>

### Cisco Systems (CSCO) Could Be 15% Undervalued As AI Earnings Focus Builds
- Summary: Investors see Cisco undervalued amid AI earnings focus, suggesting potential upside.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNaUZoNjY4Sy13SHlPSFN1Mno0cWtaWFVDMDhDWm90TDRVcmpTSGc3dzh3M09GZ1g0bGRDdnpGVHk0WFlDUFc0WDNkaW9DYy11b2dhV2RuUEVOTTJpa3F2ZUhOdTVFaTJyUnZvWjY0Nmp1eTBWOWdldWJqOU1heXF0MlJvcUR4T1BLTDEwdXo0OEdsbXJJOGdZ?oc=5>

### Dear Cisco Stock Fans, Mark Your Calendars for November 12
- Summary: Upcoming event on November 12 for Cisco shareholders.
- Date: 2026-11-11 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPNE9oNF9IX2t6RlhjMm51ZW0yTnZtaldGNDZSWHFoMjF3dTJXdHU5SGxKUGJNOUJBSjY1MEJXNmItbGhLREZoa1BxckZGcVRxcnAxanlrUUZaOHdTbEFIN2I1OV9zZWM5SzFvdzhxVmFfdGhxZVdGUExpMXJwQWtfQTN5a0tXUUNHa1Q0UHhoamV6amdhYlZUWF9iam15eUtDaGxF?oc=5>

### Cisco beats on earnings, says AI infrastructure revenue will double this fiscal year
- Summary: Cisco exceeded earnings expectations, projecting AI infrastructure revenue to double this fiscal year.
- Date: 2026-11-12 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMickFVX3lxTFBXZ1VHS3FlM0xwR1ctNVZGd255am4zdHdQUUhBVjdyRmVoRy05RkZPcGQ2RUgzUFVsSlk1YTQ5aUZTM1lhZmFPT2lXUXY4NzcwanBweWVNN3RMSklUdzBfdDg5MUtfMzY0Qi1FMmpHT19sZ9IBd0FVX3lxTFB0dFNlWHZZSG04enVwQmRHZ3J3LUtIT3ZUdF9ESkVzZExBaWJFSTVjcGZxbkFxUVl2VFZ3dkFBTVFVc0dWTG5INTRlMDBqT1VudEJYZ0xOX0NiUzVPSEtoUzhfRlh5bmlMMWZjaHExV0dPTVBra2hv?oc=5>

## HEADWINDS

### Cisco Stock Retests $101.60 Ahead of Q1 Results, With AI Orders in Focus
- Summary: Cisco shares retested $101.60 level before Q1 results, indicating market sensitivity to AI order updates.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxOVmliNHE0all0VXZ5VTgxaG9oZVFSc0VKWXRiaXFzdkhydlJkQzU0bnNTNUpCLURPNDk4Tm84M2wyMkRjbC1BMHByZHdfVjRMcHJMM0E2bllCVnRxX0NZZlhIV2EwVFpBZHRPSnNreDY5VmgxRjljcWFBeENqN0pUc1JuMWZGazNMNEk2elE3dExmREJKcm1HNXRQcmNsaHBVOHZ4UXFQTXlMWngzRWJOVVpXdS1mOVNVMlhuRU5tSVRWcXJkaGYyMFBOWEpsU2dWMnp2QUtR?oc=5>

## CATALYSTS

### Cisco Q1 Earnings – Here’s What Analysts Expect from CSCO Stock amid AI Trade Concerns
- Summary: Cisco Q1 Earnings – Here’s What Analysts Expect from CSCO Stock amid AI Trade Concerns
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOajdxTFFHUlRraWFsc0pSekZYRktYRFZVRnVEZDZWc0p0clZaRUNYMjFaMjVHVU9UQzZ0X1cwcE9hWFBLWjBuSGdiSFZ4dmMtcklIUG1YVzgyU19mVm13UnA2OXdZTVNlY2JDVGZMREVfUlVfTGtscTRLVlFhN1hBR2YyejZTLWhsakJSWktCZ09wQ0ZrbV9RVmZseGNZdG8?oc=5>

### Cisco Reports First Quarter Earnings
- Summary: Cisco Reports First Quarter Earnings
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPRmNKTkMxYlRJT0c0eUtObVRzYnhtWmdESUtIdF9nRmxyVldJM2k1b0N6Nmo2LWVndlNKckI3YnAtVWpJSHI1WnlyMVhsVDYwU2FYZ3JQM19DRmtXWGRubjNKdGhNYmc3ZDd6QVlOQ0EwRWh0MmJ4MXl1SVgtaWZGX1RCbXp6QzlOdEJHVUZJQXBPNWpWWUtfWHFGT3B3MXNt?oc=5>

### Cisco’s 16-Year Revenue Growth High Raises the Stakes for Fiscal 2027 Earnings
- Summary: Cisco’s 16-Year Revenue Growth High Raises the Stakes for Fiscal 2027 Earnings
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxQM1FKc3pISEF0elVQVVpoTnVPTUlwQk5IY0tPY01GWkdwRS1BLVF3VTBwZlpyRVBoQkU0dF9mRDhhc0k5eEtSYU9DRWUtRXM3YjQ2dURrWFE1U2RaUWtXblZlOGx0YlN1WkdlOV9kWjRTTFk0cEpwRXRiTFRaQi1uNlh2UnVhd2gyMTZTRWlQSDFIUW91bkQ4TEJRa1ZHRGpjb2dHY3c1UEljbURpVks2Qi1tQlpOQVNPY0VSVnBB?oc=5>

### Cisco Earnings Due Thursday: Here’s What Investors Need to Know
- Summary: Cisco Earnings Due Thursday: Here’s What Investors Need to Know
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxQSDBTUEs5SjE0ODhMeVFvZHpuN0d4a1ppZXRLOENtaDBySGxEUkNpR29aVzVNdmliSGFva0YtM2ZURmRZNEYtVzFWa2ZXdTg0WF9yN2phN2NDOExITzJyTklxdzB0bUgzMDlTSGlIRWl4WEhidkRncXBlWnc5UkJIdTU4X1IxLVFhV0pFVGNzeDZKOHJiOWE0ZzZnd2tJWDBjYWN5ZmNteFNhbHpnQ3lJSzR4dF9sc0JFbzdjdzR3VQ?oc=5>

### Cisco (CSCO) Reports Q1 Earnings: What Key Metrics Have to Say
- Summary: Cisco (CSCO) Reports Q1 Earnings: What Key Metrics Have to Say
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOTFIyN2F2c28zSndhdFk0UUtQcHlpZTNEbkpYdFdsSmpsYzZLZDFOVk0wZzdMWmU5MUhoQnBlUllpbnA2R044dlVhSVd6QXhzQWhZN0FYLVVHRVp5ZloxQ2VrcXUyam1DbF9nMkFwQlJMYXNQQjNacEhJV3NRTk0yRU5qanlQd1pHRjdmd2NmeXh3SXp2T3lNZFRlVQ?oc=5>

### CISCO SYSTEMS ($CSCO) Releases Q1 2027 Earnings
- Summary: CISCO SYSTEMS ($CSCO) Releases Q1 2027 Earnings
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxPVUhtbzgzcE9xOWdUOWQwSXNBUnA1bDVnZmlsYzNkZXVzOVFpdmlWa1JHY0U3aTh4d3lPMVYtNHVpOTR6SjA0OExpd0l6X0t2blNZMWtoUkJSYmFJaHBHRC1ZVGRTX2ZBS0lqMXY5VGcxWnhKQ3pXZll1RVlnQk9hQWdSNEgxQ0Q4NzJzQlVBMA?oc=5>

### Ahead of Cisco Earnings, Here's What Barchart Data Says Comes Next for CSCO Stock
- Summary: Market data predicts post-earnings movement.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQOTA3ZmRSaHdoS2dnM1JoMnRtSHVoU01iR25wLWVTN3JXZ1psVWRld2wxeGJDMy1lQnhpTXdEUnBCWjRRbzhHOFlVekx4VmNUUFB6eTdCQnNpcWNFa3BQMzJodU1XRlltM1B4M3BaWW9FWHBDV0hfc05ndnhPXzZ1MnQtMVRsWVliNnp1UUZWem5tTi0yaEJhTm5CSnd5WnljNEE?oc=5>

### Will Cisco (CSCO) Beat Estimates Again in Its Next Earnings Report?
- Summary: Questioning Cisco's ability to exceed earnings estimates.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNRGJRSG9SOERDYW9PNnVvRXdCY0haNHB3MDVwM0hXMmhERnVrOHBRTElLRTkxQUNtRF9RSk5DOXZhS09FMTE3c0pNLXFnV04xWmZMUXVjYXRCMXNvM00zX2k3c1pxcExOQ3U0QzhDcm5YbDN4TGd2c3NrdVE3d3V4dTg0RGo1MmlGQTgwZEV4YkZDdm81S1FIMzJ3ZEc?oc=5>

### Cisco (CSCO) vs. ANET and HPE: Can AI Networking Turn Strong Orders Into Lasting Earnings Growth?
- Summary: Questioning whether AI networking can convert strong orders into sustained earnings growth.
- Date: 2026-11-12 | Impact: medium | Horizon: medium | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxQSGozWEcxNGh2Nk0zaHFIbnFXSTg1UGNpWEdSUDdMUHFWdzRreV9meUprdGpHZWpMZTRHdmd2QzVTMXhfWjl6VlhBX3Z4RW5oRGFlT3VqZkV5WUlLbmYyVHppSnlxR0pUbVdfZEFqdlRORHRrcUlaeW1OWlZoMHN5VjNpN0hMdnhQaG5qQXpBTGM?oc=5>

### Will Cisco Systems (CSCO) Deliver the Strong Results the Market Needs to See?
- Summary: Querying Cisco's ability to meet market expectations for strong results.
- Date: 2026-11-09 | Impact: medium | Horizon: medium | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQSjRuWWVZQzNFa3hnMzB4U0VKc21CcHZPeXE0OTc4dVgzdHRycVpOYXJrbWpPanRiTTVUOXBDRTZFMk9WZlNIVFY3UW5hOXpzMFhqOFlxRUVPV0dFN2FrdVFWZU1XdFJyVXFCU0tuM0huMUU1VG8tdmhQOEh0OGx0dDlDVUJCS1I2NHpsSGFmWlIzQnZpZFpsR0ZGcERmNmc?oc=5>

### 48 ETFs Add to Cisco (CSCO) Holdings on Nov. 10
- Summary: 48 ETFs increased their Cisco holdings on Nov. 10, indicating growing institutional interest.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxOdlZVMnQ0SkpReExZSW9ocmIzelZpa2k1aE5hYnVoSHZRbFowaHZ1cDBKZzlvQ3YxSkhoX0JEa01MTG8tel9vRWhjd3V2aXhJM3k4R0xTcTNIU3lzMEVFdENjZWhMNUpLVGtGazhGSnZKVTFJVVJxU3d4QTVNR2NVVWZ6enRsNDQ1NkRGWDR3ZEU?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CSCO** | **27.13** | **8.01** | **22.39** | **17.60** | **402,183,290,880.00 USD** | **40.48** |
| ANET | 55.40 | 15.87 | 46.51 | 58.50 | 261,056,839,680.00 USD | 53.08 |
| FFIV | 25.55 | 4.51 | 18.01 | 13.30 | 18,045,446,144.00 USD | 32.26 |
| HPE | 25.86 | 2.51 | 11.72 | 33.70 | 66,585,636,864.00 USD | 117.48 |

Peers fetched as_of: 2026-11-12; CSCO reuses existing data (market data as_of: 2026-11-12); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-12
- Next expected earnings: N/A (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-12

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
- https://news.google.com/rss/articles/CBMirAFBVV95cUxNbTY3eFZkZzlxcGFEN2p2Ump0TU41c1AtaWQ1QThmWWNpT3podHNxY094Z24ydHYxVkFpb2lfOGhNUVFDTFlUZDNhbi1FOGxzT3dPVkZxMHpqQjd5cUxQcjRfLU5Yei1HVEg0OGtWV21aTXJKUXJMUUdaSURVODFuRlBnYjJUX2NwWWl2TWNKUjVKbW9nTXBybkZJUVVncGdsSDVuQU5QTzVCTzMw?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxQMi0ySDZkbkRUeTVIb2ZsN3VrbzY3TC00UEozVDAyUzMzeklOVnRxTUpkMW5qOURWUW55TmtwWm8tS1pRcnZ0UDhUSnloY0RVaVdwMnNGTE0tNG93TUlvOEV3SlZkQThuZFZQZ2FWS2RYZm1nNkFlRmNSYjBuUkVqTDQ0R3I5VzZfR2V3ekF5TmwxeTNsdmNDT1dWTXhWWmxUN3E5LUY0UGRZT0swN0VCaHl5R3lrWlloaVhGbUNLSXFXSm5UQVNJd0VaYlhrcVl6bUlLc0ZtSQ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQc3NMbXh0VkFHZnEtalpOX055M2haeWpleW5zdFlYVHlpQjJzS2JLY1A1OVBhUzFfbUhQWUlqWHY2U1JEb3hZTTZDR0hqUW9TVkUxNWpFZmlMckRfZS05TUZIRjBRT3NFTjh2OXpQRUdqRFVFemNlOVdHa0pIalJ6VVRkWWs1ejM1RkdnZ25SZ2FGMU5vSVNBZzF3OA?oc=5
- https://news.google.com/rss/articles/CBMidkFVX3lxTE5nVl9zUnJ6djVKNG1TZTE2bUsycF82TThESVkxMUFBSERNQUpwSFh5ck14RUJpTGdoTXNYd3NFWXBrWTBwRUZNd0JoOUwzUm0wWUs2Zk1ZYWpya2djOS1XcGtRZ1FZMV9vc2t0eHkyaVdsdHVJTEE?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNaUZoNjY4Sy13SHlPSFN1Mno0cWtaWFVDMDhDWm90TDRVcmpTSGc3dzh3M09GZ1g0bGRDdnpGVHk0WFlDUFc0WDNkaW9DYy11b2dhV2RuUEVOTTJpa3F2ZUhOdTVFaTJyUnZvWjY0Nmp1eTBWOWdldWJqOU1heXF0MlJvcUR4T1BLTDEwdXo0OEdsbXJJOGdZ?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPNE9oNF9IX2t6RlhjMm51ZW0yTnZtaldGNDZSWHFoMjF3dTJXdHU5SGxKUGJNOUJBSjY1MEJXNmItbGhLREZoa1BxckZGcVRxcnAxanlrUUZaOHdTbEFIN2I1OV9zZWM5SzFvdzhxVmFfdGhxZVdGUExpMXJwQWtfQTN5a0tXUUNHa1Q0UHhoamV6amdhYlZUWF9iam15eUtDaGxF?oc=5
- https://news.google.com/rss/articles/CBMickFVX3lxTFBXZ1VHS3FlM0xwR1ctNVZGd255am4zdHdQUUhBVjdyRmVoRy05RkZPcGQ2RUgzUFVsSlk1YTQ5aUZTM1lhZmFPT2lXUXY4NzcwanBweWVNN3RMSklUdzBfdDg5MUtfMzY0Qi1FMmpHT19sZ9IBd0FVX3lxTFB0dFNlWHZZSG04enVwQmRHZ3J3LUtIT3ZUdF9ESkVzZExBaWJFSTVjcGZxbkFxUVl2VFZ3dkFBTVFVc0dWTG5INTRlMDBqT1VudEJYZ0xOX0NiUzVPSEtoUzhfRlh5bmlMMWZjaHExV0dPTVBra2hv?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxOVmliNHE0all0VXZ5VTgxaG9oZVFSc0VKWXRiaXFzdkhydlJkQzU0bnNTNUpCLURPNDk4Tm84M2wyMkRjbC1BMHByZHdfVjRMcHJMM0E2bllCVnRxX0NZZlhIV2EwVFpBZHRPSnNreDY5VmgxRjljcWFBeENqN0pUc1JuMWZGazNMNEk2elE3dExmREJKcm1HNXRQcmNsaHBVOHZ4UXFQTXlMWngzRWJOVVpXdS1mOVNVMlhuRU5tSVRWcXJkaGYyMFBOWEpsU2dWMnp2QUtR?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOajdxTFFHUlRraWFsc0pSekZYRktYRFZVRnVEZDZWc0p0clZaRUNYMjFaMjVHVU9UQzZ0X1cwcE9hWFBLWjBuSGdiSFZ4dmMtcklIUG1YVzgyU19mVm13UnA2OXdZTVNlY2JDVGZMREVfUlVfTGtscTRLVlFhN1hBR2YyejZTLWhsakJSWktCZ09wQ0ZrbV9RVmZseGNZdG8?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPRmNKTkMxYlRJT0c0eUtObVRzYnhtWmdESUtIdF9nRmxyVldJM2k1b0N6Nmo2LWVndlNKckI3YnAtVWpJSHI1WnlyMVhsVDYwU2FYZ3JQM19DRmtXWGRubjNKdGhNYmc3ZDd6QVlOQ0EwRWh0MmJ4MXl1SVgtaWZGX1RCbXp6QzlOdEJHVUZJQXBPNWpWWUtfWHFGT3B3MXNt?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxQM1FKc3pISEF0elVQVVpoTnVPTUlwQk5IY0tPY01GWkdwRS1BLVF3VTBwZlpyRVBoQkU0dF9mRDhhc0k5eEtSYU9DRWUtRXM3YjQ2dURrWFE1U2RaUWtXblZlOGx0YlN1WkdlOV9kWjRTTFk0cEpwRXRiTFRaQi1uNlh2UnVhd2gyMTZTRWlQSDFIUW91bkQ4TEJRa1ZHRGpjb2dHY3c1UEljbURpVks2Qi1tQlpOQVNPY0VSVnBB?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxQSDBTUEs5SjE0ODhMeVFvZHpuN0d4a1ppZXRLOENtaDBySGxEUkNpR29aVzVNdmliSGFva0YtM2ZURmRZNEYtVzFWa2ZXdTg0WF9yN2phN2NDOExITzJyTklxdzB0bUgzMDlTSGlIRWl4WEhidkRncXBlWnc5UkJIdTU4X1IxLVFhV0pFVGNzeDZKOHJiOWE0ZzZnd2tJWDBjYWN5ZmNteFNhbHpnQ3lJSzR4dF9sc0JFbzdjdzR3VQ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOTFIyN2F2c28zSndhdFk0UUtQcHlpZTNEbkpYdFdsSmpsYzZLZDFOVk0wZzdMWmU5MUhoQnBlUllpbnA2R044dlVhSVd6QXhzQWhZN0FYLVVHRVp5ZloxQ2VrcXUyam1DbF9nMkFwQlJMYXNQQjNacEhJV3NRTk0yRU5qanlQd1pHRjdmd2NmeXh3SXp2T3lNZFRlVQ?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxPVUhtbzgzcE9xOWdUOWQwSXNBUnA1bDVnZmlsYzNkZXVzOVFpdmlWa1JHY0U3aTh4d3lPMVYtNHVpOTR6SjA0OExpd0l6X0t2blNZMWtoUkJSYmFJaHBHRC1ZVGRTX2ZBS0lqMXY5VGcxWnhKQ3pXZll1RVlnQk9hQWdSNEgxQ0Q4NzJzQlVBMA?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQOTA3ZmRSaHdoS2dnM1JoMnRtSHVoU01iR25wLWVTN3JXZ1psVWRld2wxeGJDMy1lQnhpTXdEUnBCWjRRbzhHOFlVekx4VmNUUFB6eTdCQnNpcWNFa3BQMzJodU1XRlltM1B4M3BaWW9FWHBDV0hfc05ndnhPXzZ1MnQtMVRsWVliNnp1UUZWem5tTi0yaEJhTm5CSnd5WnljNEE?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNRGJRSG9SOERDYW9PNnVvRXdCY0haNHB3MDVwM0hXMmhERnVrOHBRTElLRTkxQUNtRF9RSk5DOXZhS09FMTE3c0pNLXFnV04xWmZMUXVjYXRCMXNvM00zX2k3c1pxcExOQ3U0QzhDcm5YbDN4TGd2c3NrdVE3d3V4dTg0RGo1MmlGQTgwZEV4YkZDdm81S1FIMzJ3ZEc?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxQSGozWEcxNGh2Nk0zaHFIbnFXSTg1UGNpWEdSUDdMUHFWdzRreV9meUprdGpHZWpMZTRHdmd2QzVTMXhfWjl6VlhBX3Z4RW5oRGFlT3VqZkV5WUlLbmYyVHppSnlxR0pUbVdfZEFqdlRORHRrcUlaeW1OWlZoMHN5VjNpN0hMdnhQaG5qQXpBTGM?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQSjRuWWVZQzNFa3hnMzB4U0VKc21CcHZPeXE0OTc4dVgzdHRycVpOYXJrbWpPanRiTTVUOXBDRTZFMk9WZlNIVFY3UW5hOXpzMFhqOFlxRUVPV0dFN2FrdVFWZU1XdFJyVXFCU0tuM0huMUU1VG8tdmhQOEh0OGx0dDlDVUJCS1I2NHpsSGFmWlIzQnZpZFpsR0ZGcERmNmc?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxOdlZVMnQ0SkpReExZSW9ocmIzelZpa2k1aE5hYnVoSHZRbFowaHZ1cDBKZzlvQ3YxSkhoX0JEa01MTG8tel9vRWhjd3V2aXhJM3k4R0xTcTNIU3lzMEVFdENjZWhMNUpLVGtGazhGSnZKVTFJVVJxU3d4QTVNR2NVVWZ6enRsNDQ1NkRGWDR3ZEU?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
