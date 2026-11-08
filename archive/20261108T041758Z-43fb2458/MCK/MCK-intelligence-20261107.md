# MCK Intelligence Report

- ticker: **MCK**
- Report as_of: **2026-11-07**
- Market data as_of: **2026-11-06**
- Quant sources: https://finance.yahoo.com/quote/MCK/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MCK/key-statistics/
- AI analysis snapshot as_of: **2026-11-07**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-08T04:24:29.047747+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 9, 'ai': 10, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **11** exact headline/source/date matches; prior report **20261107T043155Z-acc5f41d/MCK** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 10 named publishers; 1 exact duplicates; 22 HTTPS source links; largest publisher share 27.27%; oldest publication 2026-11-02

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 1060.8400 |
| Return 1D (%) | -1.0410 |
| Return 1W (%) | 6.6621 |
| Return 1M (%) | 15.0998 |
| Return YTD (%) | 29.7133 |
| Return 1Y (%) | 24.0396 |
| Annualized volatility (%) | 31.6655 |
| Beta vs SPY | -0.1701 |
| Max drawdown (%) | -27.1691 |
| Sharpe (rf=0) | 0.8367 |
| Downside deviation (rf=0, %) | 18.3829 |
| Sortino (rf=0) | 1.4413 |
| Historical VaR 95% (1D, %) | 2.5988 |
| Historical ES 95% (1D, %) | 3.6083 |
| Correlation vs SPY | -0.0728 |
| Tracking error vs SPY (%) | 35.3379 |
| P/E (trailing) | 27.36 |
| P/B | -30.85 |
| EV/EBITDA | 17.82 |
| Revenue growth (%) | 7.60 |
| Forward P/E (estimate) | 20.37 |
| Gross margin (%) | 3.65 |
| Operating margin (%) | 1.47 |
| Return on equity (%) | N/A |
| Free cash flow yield (%) | 6.04 |
| MA50 | 937.6546 |
| Close vs MA50 (%) | 13.1376 |
| MA200 | 866.7029 |
| Close vs MA200 (%) | 22.3995 |
| RSI (14, Wilder) | 70.2208 |
| MACD (12,26) | 31.9015 |
| MACD signal (9) | 27.1123 |
| MACD histogram | 4.7892 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MCK': 277, 'SPY': 277}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 1060.8400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.0410 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 6.6621 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 15.0998 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 29.7133 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 24.0396 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 31.6655 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 18.3829 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.4413 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.5988 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.6083 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.0728 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 35.3379 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1701 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.1691 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.8367 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 20.3716 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 3.6530 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 1.4750 -> No interpretation rule is available for this metric.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 6.0439 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 27.3624 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 70.2208 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 4.7892 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 13.1376 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 22.3995 -> Clearly above the moving-average trend level.

## TAILWINDS

### McKesson (MCK) Beats Q2 Earnings and Revenue Estimates
- Summary: McKesson (MCK) Beats Q2 Earnings and Revenue Estimates
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNc29vZHBpLVRRSnRWX1c2SmtZVEszOFF4aWtxcTlGZ1c0ZHFJWGRDU0JxRENBVlZuQmpVM21YbWh3TEdfMmdFRXU3UHJpaDlKTUJHRXpNSXc0clN6c0hmcWRVVnFmNWZZNldWMUE0WmM3aXRmUHhDVTJfbmQ0ZGlzNzJlbWVFSGM0Mk9tMlZDZWsyclpoQ09acU9zZw?oc=5>

### McKesson’s (NYSE:MCK) Q3 CY2026 adjusted EPS top estimates
- Summary: McKesson’s (NYSE:MCK) Q3 CY2026 adjusted EPS top estimates
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxOMGNPRHJ5YUhOOW9Jc25sX3RhQW9neXpvZjBCXzVZc2NrUkIzcmhycVdadXJDM25yYWNZa1YtTmxoRUtnWEZvOVdYb29MQWQ3OG9xd1pCQWR6Z3cwaVcxZE1pcmtmVW9pVEJjUG1ELTIwY1ZPU3l4Y3M3U1JaejVIVHVIS0VucXh4bklGWjNfTC1xUS1NVGVUVWdTaWF4cnUwQ2NWd1JJamo4SGdxUGpwLVVQd2w0czNm?oc=5>

### MCK Q2 Earnings Beat Estimates on Specialty Growth, Outlook Raised
- Summary: MCK Q2 Earnings Beat Estimates on Specialty Growth, Outlook Raised
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxQUDAxR1dQVjZyNGc5bmIyWEN3OExkOW9LQURMdjdnX0dZWnZ6TXdLR3lRNnNIMHAzX2lkTmdtMlU5d1poVXk0LVk1dE9VQUJBdGJkbmd1M3JXN2daOWNYaEVZVUlhcVlQVjVJSWxBOFM3REptYmxUMF9wQlhzUmlNYXZFcFBlMVhWTTh2QUQ5YTA4aFdncE1SckFoaXB4bWxJUHdwcWg4aW1sWGdPcU02OVJTWTBfdkkyRGIzWEdR?oc=5>

### MCK Q2 Earnings Call Highlights Raised Outlook and Specialty Growth
- Summary: MCK Q2 Earnings Call Highlights Raised Outlook and Specialty Growth
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxORlA3d2h2czB1N21TaXJQLXROMmU4bGNYcUNfQjBEWDNOQUx3TnlZVlNZVEZ4TjRpLXFBcmY0cmZ2Ym50bENBaTQxaG1KQkE2QnJhazN5Nk50blJlelp5YmIzZkxVU0RoVGpIZm1TWDJfUExGU3Z3Q1Vkd2V0VF84c3JrM1I4S0twRDVKLXVwd0l5V3hIaXExc0laaFZwbHZjOFFCenFlMmlDbHhuaHM0MFFadlg1dTFYREkzdUt1eTE?oc=5>

### McKesson (MCK) Earnings Beat Raises The Question Of Whether The Stock Is Fully Valued
- Summary: McKesson (MCK) Earnings Beat Raises The Question Of Whether The Stock Is Fully Valued
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxOcVA3M1lKMWV4Yzh1WkFfVThiSFljM2hlSmxtSjI3MU9TQmd2VXVDemZ6NHp0UllKQW1oeUs3d0Q5ZFpmSXAzQk5lRU83RWxTeTBsOXNKMG9iMWwwTXVVRmIyRWhqN1d0Rnh0QkVXdUpEeFlXc1JqclJERmRuYmpsSE9NR1phMkJnbm1IT0JCZGszU0o1eFRRZGtZYVB1bXphLU1mUVY0UmQ4QU9BWkdENlZHUll1SE5MRkVBckFuQ0JBQVo20gHKAUFVX3lxTE5wbXNseUlMSDNPVWN0aEJfZUsyMlNRV2NfS3dyMVVCeWdRZDBnaU5zMm9YTTFydHVJTXoyYm0xVTBvUGNXdE5NVmJIc1RtZ1RGcmNpRlA5cmRuVWR1RnZNazJRSzhpa3JTaDBrTXlRYnhkczNWY2NyYXZPWnVjeV94eE9qQzNxVjNKOGU4czBjY3VrTXBHY181ckhGS1lzaFRIYkVROXFIdGNQeHQzN0FJRFRJa0tnMDJMQjgxVXo0dks1UlFhUGgwcGc?oc=5>

### McKesson Reports Fiscal 2027 Second Quarter Results and Raises Full Year Adjusted EPS Guidance
- Summary: McKesson Reports Fiscal 2027 Second Quarter Results and Raises Full Year Adjusted EPS Guidance
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxQVC1sY044cHJDV3AwTnVjX3prLWM2LVpfU0lQODlKVG54NktyVWY4SzAxZlliUDdwR2Q0R082UmVuRVpqQmw0M2JkS190aEx5U1h2dFN2V0ZHTWZhUldoaWM2Q0lDSm5DMUNPRlZVRzhfQm1EUnZTb0g1WFZoZlM5aUZKTFBWWENNZDB4NHFaNjBxNy02QjdyYVB6elhvVGtrdFFwbFBtQ0RnNGZHNmpKWVpHQnBWRVNpZFg0ZlNrNA?oc=5>

### McKesson (MCK) Stock May Be 37% Undervalued On Raised Full Year Guidance
- Summary: Guidance raised, stock undervalued, positive outlook.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxOMjJiZm1TQzFkNjBDSlBfTXowMTZOREI3blhmTk1ESzNZZl9QcG5oTDVPMHQtSW5MOUVOSG9CQjFETTVHMC0tMGZ1aUt4UHpxeld5NVBoa0pYdU1JbkxpWUllVGRIcVNiZ1dQQk1SaHBJTVIwOXItTGhrWUhGSTFqWFV3MEx4RW9lbzhMUGtJaVAxWEFIT2QtTlRiRW9lWDhVcjJTSTdBSFc4RUhPMXI5ekxKYWUtQ3FKTUtMV2pCNF8ybDlN0gHKAUFVX3lxTE9GWlY4ZURyWG5tVm15RV8tdGxjemp3YUgxaFp5N2s0V1ZvT184ckdvUy04MktKSnJsZ1BjbVRqZnBpd1hjcDBWUFdPcl81S2oxOUNvQVNxUjdaWmFQMEx1ck1sWHBPVzZiYVlqcmhRNjFldnhxdm5oNHl1TXhzUVNuUDRfWkdtUmNnOW1tbGhnWkxNNU9qZ2xjQUdGNmlyOU8zakpmUmpDb3N2Ni0zeVBHRTJkNlpUdS1obmhXLXFsOHY3U1lvUUZBQnc?oc=5>

## HEADWINDS

### Will MCK's Pharma & Specialty Demand Offset Pricing Headwind in Q2?
- Summary: McKesson may see demand offset pricing headwinds in Q2, potentially impacting earnings.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxOaTVrUjVHZkY1aEJOdU1lTXMyQ2JYbWJhNVVzOV9OdFlheEk3VXNCRXZXN2NfeGdBSzBUSDNwajlydk1fSFRMN3lXSi1PVnk1SHlkOEZfa2JnbXdGdjBjZ1hLdnFzX0ZYQnNReTFvVTFmaGdNZ05iYlROMVVjVkxmNWVHeHFWaVNTNFptWkEtaTdNOXI3dlZfdXRTeXFHaS1mQ0EwNjA0N3JXTllyak9NQ2xXUG5KV2RQNVlIZw?oc=5>

### McKesson (MCK) CTO Fraga sold 600 shares for $630K at $1,050.00 under a 10b5-1 plan
- Summary: Insider sale may signal negative sentiment.
- Date: 2026-11-05 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxNSERoSnVuWUZPb3J1V2l3M2ZGa0pwdlhuaU1LYjNYcUlkczBBMmJneEYzUy1ob24wT0piZWxXZDlHMFQtaG5pU3pubWJQYVo1Ymd3clNPaWhaeUdrRFNRQ2Z6bjF4dnRGTFdleVZYRVJocVF3ZG1leGZRZEdVX3dNV1FWeGpsa0lVMlZWNjN4WElVcEI3clZocFVSSTNzcnhjQVJz?oc=5>

## CATALYSTS

### McKesson Corp.: Normalized Earnings Suggest Attractive Valuation (MCK)
- Summary: McKesson Corp.: Normalized Earnings Suggest Attractive Valuation (MCK)
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOT2VzOTZScDhOR3JFZGpFVGdNMlgxWTQ1RS1hSkJJMUJVU2s0VC11bGRDMXU3MmROaGdIcnNLMGw2LUlXcmt5WWhVRDVsOUtEczBTRENGakQ0bXo4bkJMU0lmb245cXZaVU1FbFljX0ZlUnhUOGU3ZHJjVWFyN1Z2WlQ3RE04SHlSancxUU9UaU94YUhGaWNwMVNhNy1WS292TlBfQ2V3?oc=5>

### McKesson (MCK) Reports Q2 Revenue Growth and Raises Earnings Gui
- Summary: McKesson (MCK) Reports Q2 Revenue Growth and Raises Earnings Gui
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxOSVFoLVZ6eWZ6WnBoQ0xDMWp3STJxZUptUjBSRGl4OFZaWE84azJVUGRyZU9wVFFSYW1DVGdvelBHZXVTN0duOFh6djRhN3dVZ2owVzN0ZXN6ZTBoSXd2ZE1FSHZOTWhPV2tQcWVvLXV5QlBLMVpNRklSQ2ptQTQ5bWNlbUtGT21BVUc5RWYtMnFwYldhOHNkSG1sRFlrb01QMFFrZHk3Y1Q1dV9iS2pCNEhrZlRZVjBPcV8xenV5bTRnUWhTdGlj?oc=5>

### McKesson (MCK) Q3 earnings report preview: what to look for
- Summary: McKesson (MCK) Q3 earnings report preview: what to look for
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxQb0lLQThNR2NyV0J0OTNyQklUR1R2OGlBOEg4dHB2eUh6SXVnRk5mM3poQTBOQzRDblVmSmh3ZGVSb2txNFMwTmFIa1VJZmJkOXdvcFB1ZV9JSUpKRmgyQUhsU3lyZlB0NU01ZlpfUFNTWDRqcnhOZjlBVGxaUDBUWnU5aFRPZ0lDcmR6Y2tubzJQTDVPdnM1WmQxSlFNUXJzMGVxVXdqOXh3MWZFOWF2RHd3?oc=5>

### Here's What Key Metrics Tell Us About McKesson (MCK) Q2 Earnings
- Summary: Analysis of McKesson's Q2 earnings metrics and performance indicators.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQV3VxdlpheEw3LW92SmJNSHkyRHpWbXJwdzlEbkp3Y3JtUVc4MEhCOFVNX2NLZFdQTzQzQ3VPdUpHNWZHVmdQLWZBMGdpeUdweTNVUElNV3A4MVdaZElMX0FLaDE4eUxCTlYyMjdJdXp1SEU0eE9TTnJ1MHVxOUdSVGhjalBTMjUweTBUMHRUbVVTMlVo?oc=5>

### McKesson Corporation (MCK) Stock Forecasts
- Summary: McKesson releases stock price forecasts for the upcoming period.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxPWUZxUnpUcnRpMFN0NWN4WDVHZmY3X1hBZ3I0WGlxN3N5cTloSjBCNmJiV2xQLVFIeUw0OExLNU5fVzdEMjFvdzZ4MTdTd1poZlFxbU8xUDByMVJEVW1Ic1dxdE14X3FQRjRHc1o0YWU5RFVkSnNEYldXMXR6azAtWGh0WEtlSE9IQm40Ug?oc=5>

### McKesson (MCK) Surged 13% Following Strong Q3 Results
- Summary: McKesson’s Q3 earnings beat expectations, driving a 13% stock jump.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOXzZNN0F1OVZZdVNGVVM0eUNNQ29vQ2lqZWlpRXN0QkpZQ1B0d0xMZlkxdE9oZm5hanhEZy16dU9lT1ZWQldzdFdhUmlYMl9PMUFkSHU2aEFtdllOcW1TWmFQcFRwOVdIQ0t1NmlIOWdLY0Z3U0pDTU9rUFJIMEkwdmhBOS15ck8zNVNoXzVFeTZ6WldFSkZRVg?oc=5>

### McKesson: Fiscal Q2 Earnings Snapshot
- Summary: Snapshot of McKesson's fiscal Q2 earnings results and key figures.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPaC1NYzc2dXBxa1R4YWcxZVdpZEpVbVNINC0zV3gxUGtjWDZQbE1XY05UY2pRZ1lPLWtId3U1bVFRVUkwTzZSdmd0V0xySmZpRDhXUzZMemllTWswOUZXNzY5cDZNMlZFYmNMNWI3a0pmczFEOWEyU0MtVWlKcWhjZlVvTml4cVFaa3ZfTTBWWGY0Mkdmbk42NURkbG9ldjBTWlFr?oc=5>

### 5 insightful analyst questions from McKesson’s Q3 CY2026 earnings call
- Summary: Earnings call provides new information.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxPVHkxS1pGeU9kWGlVdDlKbU9NdHBZMWphQnBfZVo4a1JfbC1fcWpyUS00dzRVYWIwR3hienZIWUViU09hQVlKRHJ2SDh2UzdfOVY2UW9jdjJpakZpQ2hRTXFNYktZc0lVSWMwdmFSenVvYlhfbHJjcGIxUExEY2NSNkQ3Y1djSkMtTzZvTXhDeGJOV1JOYVQxcUR6NnNMZXZoQVRGNC1sYl8yQzN6dzU5VnNST2RTWmI5N3p6elhCc1YzYkl4Qml4R0JTZw?oc=5>

### Officer Francisco Fraga proposes selling 600 shares of McKesson (MCK).
- Summary: Officer Francisco Fraga proposes selling 600 shares of McKesson, indicating a potential ownership change.
- Date: 2026-11-04 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPbDFkVFBxcXZUNkc4eGhzdG9VdFlHeUxpQjg3RjdXNUxuYzhNeEdpZzVWUXYyTEdfRC1WSEhxTkhUX0NvLV9zOWhRQ3BIMWFIc0dSMFc0NTQzQ2xORl82enJJMVhtQjRoMDNmNzBoUVM1S3FZZ2VXYlQxR2RWYm55dUJMdXNMXzVjUlgtTi1fSi04RlE?oc=5>

## RISKS

### Is McKesson Stock Increasing Your Market Risk?
- Summary: Potential increase in market risk for investors.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxNQVpTYzNPcmZRVFlvclIzdWJiQW4xVGRMSmFZMENfalFBOGxnSWZ4Q29yUWl5clNCcHk0eUhCaXcya0NuWkFGVHFnZGYycWdMSmZFcUktYWtaRGp4VHpwUHY5TlFmczh0dVNVRS1CYkV1SF9DaTN1Z3VsQWFmQVA4QTV1Tlhzd0wxMHpHSnBXTXNpUV9Lc2J0eEx4R29ha2R4UFlHWFhNNlo?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MCK** | **27.36** | **-30.85** | **17.82** | **7.60** | **122,481,041,408.00 USD** | **24.04** |
| COR | 18.58 | 17.29 | 12.25 | 5.50 | 63,652,311,040.00 USD | -6.70 |
| CAH | 35.15 | -20.84 | 15.16 | 5.50 | 62,804,451,328.00 USD | 38.54 |
| CNC | 23.97 | 1.55 | 5.67 | 0.20 | 34,526,040,064.00 USD | 87.98 |

Peers fetched as_of: 2026-11-07; MCK reuses existing data (market data as_of: 2026-11-06); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-04
- Next expected earnings: 2027-02-03 (yfinance; expected dates may change)

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
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 29,980,000,000.00 USD; period 2011-04-01/2011-06-30; fiscal year/reporting period 2011/Q1
- Net income (latest available single quarter): 1,218,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2027/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/927653/000092765326000281/mck-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimwFBVV95cUxNc29vZHBpLVRRSnRWX1c2SmtZVEszOFF4aWtxcTlGZ1c0ZHFJWGRDU0JxRENBVlZuQmpVM21YbWh3TEdfMmdFRXU3UHJpaDlKTUJHRXpNSXc0clN6c0hmcWRVVnFmNWZZNldWMUE0WmM3aXRmUHhDVTJfbmQ0ZGlzNzJlbWVFSGM0Mk9tMlZDZWsyclpoQ09acU9zZw?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxOMGNPRHJ5YUhOOW9Jc25sX3RhQW9neXpvZjBCXzVZc2NrUkIzcmhycVdadXJDM25yYWNZa1YtTmxoRUtnWEZvOVdYb29MQWQ3OG9xd1pCQWR6Z3cwaVcxZE1pcmtmVW9pVEJjUG1ELTIwY1ZPU3l4Y3M3U1JaejVIVHVIS0VucXh4bklGWjNfTC1xUS1NVGVUVWdTaWF4cnUwQ2NWd1JJamo4SGdxUGpwLVVQd2w0czNm?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQVkRURThFQXlfakZQbVBKVjVTYWtvalZsZmhpckk5aUlzXy0ySDFmU0JWN3pRT2R5aEtzVXRFVWlKenROQ3JwblE2dENUMDFKZU1DVmNYQndnd2lwd2VFVEZzN1JfRkpwUTduZW14d2t5VEZySWRVeDc2Mnp6eVh0dXNvR2pkbnJtTVRza0I5LUtSMjVjU1hlSHZOOFZoYUw0V1Vjb2Z3?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxQUDAxR1dQVjZyNGc5bmIyWEN3OExkOW9LQURMdjdnX0dZWnZ6TXdLR3lRNnNIMHAzX2lkTmdtMlU5d1poVXk0LVk1dE9VQUJBdGJkbmd1M3JXN2daOWNYaEVZVUlhcVlQVjVJSWxBOFM3REptYmxUMF9wQlhzUmlNYXZFcFBlMVhWTTh2QUQ5YTA4aFdncE1SckFoaXB4bWxJUHdwcWg4aW1sWGdPcU02OVJTWTBfdkkyRGIzWEdR?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxORlA3d2h2czB1N21TaXJQLXROMmU4bGNYcUNfQjBEWDNOQUx3TnlZVlNZVEZ4TjRpLXFBcmY0cmZ2Ym50bENBaTQxaG1KQkE2QnJhazN5Nk50blJlelp5YmIzZkxVU0RoVGpIZm1TWDJfUExGU3Z3Q1Vkd2V0VF84c3JrM1I4S0twRDVKLXVwd0l5V3hIaXExc0laaFZwbHZjOFFCenFlMmlDbHhuaHM0MFFadlg1dTFYREkzdUt1eTE?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxOcVA3M1lKMWV4Yzh1WkFfVThiSFljM2hlSmxtSjI3MU9TQmd2VXVDemZ6NHp0UllKQW1oeUs3d0Q5ZFpmSXAzQk5lRU83RWxTeTBsOXNKMG9iMWwwTXVVRmIyRWhqN1d0Rnh0QkVXdUpEeFlXc1JqclJERmRuYmpsSE9NR1phMkJnbm1IT0JCZGszU0o1eFRRZGtZYVB1bXphLU1mUVY0UmQ4QU9BWkdENlZHUll1SE5MRkVBckFuQ0JBQVo20gHKAUFVX3lxTE5wbXNseUlMSDNPVWN0aEJfZUsyMlNRV2NfS3dyMVVCeWdRZDBnaU5zMm9YTTFydHVJTXoyYm0xVTBvUGNXdE5NVmJIc1RtZ1RGcmNpRlA5cmRuVWR1RnZNazJRSzhpa3JTaDBrTXlRYnhkczNWY2NyYXZPWnVjeV94eE9qQzNxVjNKOGU4czBjY3VrTXBHY181ckhGS1lzaFRIYkVROXFIdGNQeHQzN0FJRFRJa0tnMDJMQjgxVXo0dks1UlFhUGgwcGc?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxQVC1sY044cHJDV3AwTnVjX3prLWM2LVpfU0lQODlKVG54NktyVWY4SzAxZlliUDdwR2Q0R082UmVuRVpqQmw0M2JkS190aEx5U1h2dFN2V0ZHTWZhUldoaWM2Q0lDSm5DMUNPRlZVRzhfQm1EUnZTb0g1WFZoZlM5aUZKTFBWWENNZDB4NHFaNjBxNy02QjdyYVB6elhvVGtrdFFwbFBtQ0RnNGZHNmpKWVpHQnBWRVNpZFg0ZlNrNA?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxOMjJiZm1TQzFkNjBDSlBfTXowMTZOREI3blhmTk1ESzNZZl9QcG5oTDVPMHQtSW5MOUVOSG9CQjFETTVHMC0tMGZ1aUt4UHpxeld5NVBoa0pYdU1JbkxpWUllVGRIcVNiZ1dQQk1SaHBJTVIwOXItTGhrWUhGSTFqWFV3MEx4RW9lbzhMUGtJaVAxWEFIT2QtTlRiRW9lWDhVcjJTSTdBSFc4RUhPMXI5ekxKYWUtQ3FKTUtMV2pCNF8ybDlN0gHKAUFVX3lxTE9GWlY4ZURyWG5tVm15RV8tdGxjemp3YUgxaFp5N2s0V1ZvT184ckdvUy04MktKSnJsZ1BjbVRqZnBpd1hjcDBWUFdPcl81S2oxOUNvQVNxUjdaWmFQMEx1ck1sWHBPVzZiYVlqcmhRNjFldnhxdm5oNHl1TXhzUVNuUDRfWkdtUmNnOW1tbGhnWkxNNU9qZ2xjQUdGNmlyOU8zakpmUmpDb3N2Ni0zeVBHRTJkNlpUdS1obmhXLXFsOHY3U1lvUUZBQnc?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxOaTVrUjVHZkY1aEJOdU1lTXMyQ2JYbWJhNVVzOV9OdFlheEk3VXNCRXZXN2NfeGdBSzBUSDNwajlydk1fSFRMN3lXSi1PVnk1SHlkOEZfa2JnbXdGdjBjZ1hLdnFzX0ZYQnNReTFvVTFmaGdNZ05iYlROMVVjVkxmNWVHeHFWaVNTNFptWkEtaTdNOXI3dlZfdXRTeXFHaS1mQ0EwNjA0N3JXTllyak9NQ2xXUG5KV2RQNVlIZw?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxNSERoSnVuWUZPb3J1V2l3M2ZGa0pwdlhuaU1LYjNYcUlkczBBMmJneEYzUy1ob24wT0piZWxXZDlHMFQtaG5pU3pubWJQYVo1Ymd3clNPaWhaeUdrRFNRQ2Z6bjF4dnRGTFdleVZYRVJocVF3ZG1leGZRZEdVX3dNV1FWeGpsa0lVMlZWNjN4WElVcEI3clZocFVSSTNzcnhjQVJz?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOT2VzOTZScDhOR3JFZGpFVGdNMlgxWTQ1RS1hSkJJMUJVU2s0VC11bGRDMXU3MmROaGdIcnNLMGw2LUlXcmt5WWhVRDVsOUtEczBTRENGakQ0bXo4bkJMU0lmb245cXZaVU1FbFljX0ZlUnhUOGU3ZHJjVWFyN1Z2WlQ3RE04SHlSancxUU9UaU94YUhGaWNwMVNhNy1WS292TlBfQ2V3?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxOSVFoLVZ6eWZ6WnBoQ0xDMWp3STJxZUptUjBSRGl4OFZaWE84azJVUGRyZU9wVFFSYW1DVGdvelBHZXVTN0duOFh6djRhN3dVZ2owVzN0ZXN6ZTBoSXd2ZE1FSHZOTWhPV2tQcWVvLXV5QlBLMVpNRklSQ2ptQTQ5bWNlbUtGT21BVUc5RWYtMnFwYldhOHNkSG1sRFlrb01QMFFrZHk3Y1Q1dV9iS2pCNEhrZlRZVjBPcV8xenV5bTRnUWhTdGlj?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxQb0lLQThNR2NyV0J0OTNyQklUR1R2OGlBOEg4dHB2eUh6SXVnRk5mM3poQTBOQzRDblVmSmh3ZGVSb2txNFMwTmFIa1VJZmJkOXdvcFB1ZV9JSUpKRmgyQUhsU3lyZlB0NU01ZlpfUFNTWDRqcnhOZjlBVGxaUDBUWnU5aFRPZ0lDcmR6Y2tubzJQTDVPdnM1WmQxSlFNUXJzMGVxVXdqOXh3MWZFOWF2RHd3?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQV3VxdlpheEw3LW92SmJNSHkyRHpWbXJwdzlEbkp3Y3JtUVc4MEhCOFVNX2NLZFdQTzQzQ3VPdUpHNWZHVmdQLWZBMGdpeUdweTNVUElNV3A4MVdaZElMX0FLaDE4eUxCTlYyMjdJdXp1SEU0eE9TTnJ1MHVxOUdSVGhjalBTMjUweTBUMHRUbVVTMlVo?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxPWUZxUnpUcnRpMFN0NWN4WDVHZmY3X1hBZ3I0WGlxN3N5cTloSjBCNmJiV2xQLVFIeUw0OExLNU5fVzdEMjFvdzZ4MTdTd1poZlFxbU8xUDByMVJEVW1Ic1dxdE14X3FQRjRHc1o0YWU5RFVkSnNEYldXMXR6azAtWGh0WEtlSE9IQm40Ug?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOXzZNN0F1OVZZdVNGVVM0eUNNQ29vQ2lqZWlpRXN0QkpZQ1B0d0xMZlkxdE9oZm5hanhEZy16dU9lT1ZWQldzdFdhUmlYMl9PMUFkSHU2aEFtdllOcW1TWmFQcFRwOVdIQ0t1NmlIOWdLY0Z3U0pDTU9rUFJIMEkwdmhBOS15ck8zNVNoXzVFeTZ6WldFSkZRVg?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPaC1NYzc2dXBxa1R4YWcxZVdpZEpVbVNINC0zV3gxUGtjWDZQbE1XY05UY2pRZ1lPLWtId3U1bVFRVUkwTzZSdmd0V0xySmZpRDhXUzZMemllTWswOUZXNzY5cDZNMlZFYmNMNWI3a0pmczFEOWEyU0MtVWlKcWhjZlVvTml4cVFaa3ZfTTBWWGY0Mkdmbk42NURkbG9ldjBTWlFr?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxPVHkxS1pGeU9kWGlVdDlKbU9NdHBZMWphQnBfZVo4a1JfbC1fcWpyUS00dzRVYWIwR3hienZIWUViU09hQVlKRHJ2SDh2UzdfOVY2UW9jdjJpakZpQ2hRTXFNYktZc0lVSWMwdmFSenVvYlhfbHJjcGIxUExEY2NSNkQ3Y1djSkMtTzZvTXhDeGJOV1JOYVQxcUR6NnNMZXZoQVRGNC1sYl8yQzN6dzU5VnNST2RTWmI5N3p6elhCc1YzYkl4Qml4R0JTZw?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPbDFkVFBxcXZUNkc4eGhzdG9VdFlHeUxpQjg3RjdXNUxuYzhNeEdpZzVWUXYyTEdfRC1WSEhxTkhUX0NvLV9zOWhRQ3BIMWFIc0dSMFc0NTQzQ2xORl82enJJMVhtQjRoMDNmNzBoUVM1S3FZZ2VXYlQxR2RWYm55dUJMdXNMXzVjUlgtTi1fSi04RlE?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxNQVpTYzNPcmZRVFlvclIzdWJiQW4xVGRMSmFZMENfalFBOGxnSWZ4Q29yUWl5clNCcHk0eUhCaXcya0NuWkFGVHFnZGYycWdMSmZFcUktYWtaRGp4VHpwUHY5TlFmczh0dVNVRS1CYkV1SF9DaTN1Z3VsQWFmQVA4QTV1Tlhzd0wxMHpHSnBXTXNpUV9Lc2J0eEx4R29ha2R4UFlHWFhNNlo?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
