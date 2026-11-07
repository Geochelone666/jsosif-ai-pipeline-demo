# BRK-B Intelligence Report

- ticker: **BRK-B**
- Report as_of: **2026-11-06**
- Market data as_of: **2026-11-06**
- Quant sources: https://finance.yahoo.com/quote/BRK-B/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/BRK-B/key-statistics/
- AI analysis snapshot as_of: **2026-11-06**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-07T04:40:16.789173+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 6, 'ai': 12, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **11** exact headline/source/date matches; prior report **20261106T045829Z-1db1e5a7/BRK-B** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 12 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 39.13%; oldest publication 2026-11-02

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 570.8900 |
| Return 1D (%) | -0.2516 |
| Return 1W (%) | 5.2351 |
| Return 1M (%) | 12.9268 |
| Return YTD (%) | 13.5761 |
| Return 1Y (%) | 15.7640 |
| Annualized volatility (%) | 15.1508 |
| Beta vs SPY | 0.0447 |
| Max drawdown (%) | -9.4218 |
| Sharpe (rf=0) | 1.0458 |
| Downside deviation (rf=0, %) | 10.0840 |
| Sortino (rf=0) | 1.5713 |
| Historical VaR 95% (1D, %) | 1.4122 |
| Historical ES 95% (1D, %) | 2.0016 |
| Correlation vs SPY | 0.0400 |
| Tracking error vs SPY (%) | 19.9180 |
| P/E (trailing) | 14.36 |
| P/B | 0.00 |
| EV/EBITDA | -1.79 |
| Revenue growth (%) | 10.00 |
| Forward P/E (estimate) | 25.45 |
| Gross margin (%) | 30.33 |
| Operating margin (%) | 32.56 |
| Return on equity (%) | 12.12 |
| Free cash flow yield (%) | 5.89 |
| MA50 | 521.5604 |
| Close vs MA50 (%) | 9.4581 |
| MA200 | 497.7229 |
| Close vs MA200 (%) | 14.7004 |
| RSI (14, Wilder) | 73.6025 |
| MACD (12,26) | 14.2126 |
| MACD signal (9) | 11.4312 |
| MACD histogram | 2.7814 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'BRK-B': 277, 'SPY': 277}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 570.8900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.2516 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 5.2351 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 12.9268 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 13.5761 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 15.7640 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 15.1508 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 10.0840 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.5713 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.4122 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.0016 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0400 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 19.9180 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.0447 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -9.4218 -> Shallow peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.0458 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 25.4504 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 30.3320 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 32.5610 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 12.1200 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 5.8894 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 14.3584 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 73.6025 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 2.7814 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 9.4581 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 14.7004 -> Clearly above the moving-average trend level.

## TAILWINDS

### Berkshire Hathaway Stock (BRK.B) Hits All-Time High as Market Tanks
- Summary: Berkshire Hathaway Stock (BRK.B) Hits All-Time High as Market Tanks
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQY0FyNElEb0JXNUptbU1IRnJjWHEtekVkVHFZbTA2RmxBcG9ncmxpSWQxeEtmeHltc3hjZFluTGd4eUh4MEZWRUp6VWRmZ0FhcjJXRV9HTGN5Mm5hMlF0a1VFOGxjS3E0dkFUQWN4OGlEdmRBWTR6aFZlVlZBaFZmUEtNZVotYnVhSjBLN1ppUy1vZGNxQ2JkRXEybw?oc=5>

### Berkshire Hathaway Shares Are Up 11% This Year. Is the Stock a Buy Ahead of Earnings?
- Summary: Berkshire Hathaway Shares Are Up 11% This Year. Is the Stock a Buy Ahead of Earnings?
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxQRm5DaTN3NmRadmh5LVczYXBueVBlUnhtaDZrQ2FGRGtmS0J1WnRkOWcwQ1FmT1pLN0dwQUV2ajRWZENUTGRFRmRBMEpJdjBMbUVmcnB0ZGxRWTNDRWV6RlItbjBfWndhNWVhVVZuWkxWdUY5RnZmU3h5dVlfaXItdEs4NDN5RVdnTFF6RnNBWXZMTExSRUoyS3B6UTNiSE9qbWx2X3VHNVZYRENl?oc=5>

### Berkshire Hathaway Stock Has Surged. Can Earnings Keep the Rally Going?
- Summary: Berkshire Hathaway Stock Has Surged. Can Earnings Keep the Rally Going?
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxQaFk0ektfOWtITzBVYXRoYXVjVTZub3gyclBPS05TNDR1N1lPSm80Y2lid1dJclQxY2Z6VmpSVGpRTk9NSHFUdzl5M0NHX0phWFUzOXJOV0FNWlJsdnJ0UmhEZU9PSXVLQ1h0UGdlaml5dVJnSml4NVZCRmV3dDdfQzFiWUUySHVLd1pUcQ?oc=5>

### Berkshire Hathaway Inc (BRK.B) Shares Surge 4.0% -- What GF Scor
- Summary: Berkshire Hathaway Inc (BRK.B) Shares Surge 4.0% -- What GF Scor
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxOc0w4a19pY1htemludV9nRkY5RnVOcmNxRUoxQzdOakxSUnpYYzFNQU42M29VUjh5ODk3MTZueVpEMUtuZEs4Y3pySnM4TXFUeWxqTzgtQzYxMnFwRmh3S3dKYTlHblJ2em5FNkVlTkZ4TEYyOUI3SGRLenZod3hpSGM3b3d4NW9jZjZnTWctUjZrWjQ4N0dzOVlLeHBuV1pOSlhPTlNWREI3cmUxMzZaM0cta1g4d25kVHc?oc=5>

### Berkshire Hathaway's Stock Portfolio Is Worth About 3 Times What It Paid. The Gains Alone Equal About 19% of the Company.
- Summary: Portfolio value tripled, gains 19% of company, indicating strong asset performance.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPWmxkMW4tQXR5X09YUWJIXy1QMFE2VTA1NjkyTEx0MTBmZHRhQUJiTzAxMnBBR0Q0dUhpNVB5VHBrWTJ3N0g2b3RvYkZybnlmM0IyYmpXMHlhNHZQLVM4b0VhOXhxYmNSaEZCRF83WVFiQXVjZDN6bWJQSE9MSFR3TE04akxPWWhzOWtGMC03bVlOei1qeFVWLTBVeVh4QjZFWmtNajNKWGpxZw?oc=5>

### Berkshire Has Gained 16% in About 5 Weeks
- Summary: Berkshire’s stock rose 16% over roughly five weeks, indicating strong market performance.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxQWDVzSlBjckRRN2JXTjRubUVLb1BCOENjMV9PZzNPQzREZVBNUzd0emhtOHRhQ21MTlkzY21qVXktNEticzJRVFpZdEVrUWZ0MEM5R3gzTlFDbjdLLV9IZ2VzWDZERklMcjJ5UFllMFQyVGJtYmdSS2l4Sm9tVy1HUE82c1pLUzlUeWFrXw?oc=5>

### Warren Buffett's 3 Longest-Held Stocks Average a 3,757% Gain and Collectively Deliver $1.53 Billion in Annual Dividend Income for Berkshire Hathaway
- Summary: Three long‑held stocks yielded huge gains and $1.53B in dividends, boosting Berkshire’s income.
- Date: 2026-11-04 | Impact: high | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOV1FIelB2WWcybVl2OE1MblZFWlBQVXhGUEFqcGhOenRiYndFNVFkaUpST3dtTUxoam13N3g2Zm90S1pLSm9XaWMxYXhMWEtYb19Hd3RyUkNhQ0d2cGwtZVJuNTdBT3lWb3J2WGFVbFJWeFJlUHpKd1I3SnROZWx6Z0ZrazhTRWNXVHlMbmFHWlFtbEIycHMxT2VpZw?oc=5>

### Berkshire Hathaway Reports Nov. 7 With Its Stock at a Record. Its Cash Pile Is the Number to Watch.
- Summary: Berkshire’s stock hit a record; its cash reserves remain a key metric.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxQRTFYN1AwWVpyUUxvMWF3R004djZQc0ljZFpSUmtzckhuU1hTX0dhZnBzNkk2UUw4d0VjTHBBbXUwTlUwUFhReGt2TmdIUVhnZzVpbjY5cy1XeTRnWi10MTlubVhxdDIxS2s0bExjWmQ0U3VhYmpfOFYzUWdTXzU4dElmUUJVcl85VUJiS2w3c0c3TTg5Q1plYzVPcnJjTGQ3OEFHTDJyNHVoZDNXTkNuZk1xRko5eXFMQXdjclR0OWp5ZUtNR0FwUFJoRmxpR2xIYkxOVVF3?oc=5>

### Warren Buffett's Successor, Greg Abel, Has 71% of Berkshire Hathaway's $362 Billion Portfolio Invested in 7 Standout Stocks
- Summary: Greg Abel’s portfolio heavily concentrated in seven stocks, reflecting strategic focus.
- Date: 2026-11-06 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4gFBVV95cUxNdlk5ZDQyTU43VDFLV01oUEFrWWpVSWRINV9tZUhibGgtRlllbzdjOE9fVWlHNGc5TjYyTlRjUkdoMllrRG81c01UNDJZUUtkb09vSHQ1N1I5dFU1YzlwZm8zZm1LVGhGc0pFYVRjMEUxQmZ0S0JSeXp6RDJDTWF2SHY5SkRRUWMzS204dVRvUFE5N3NyenV3UlRmd0JIejBmTl95S2RISUV2VHpCSDN1SG90Q2hCa3pRWjhkaDN5RDYzVkR3bU5mdFNSN01QS2d4V2FzeUNJZUVHdzNMZk82Y1VR?oc=5>

### History Says Berkshire Hathaway Stock Rewards Patience: It Rose in 50 of the Last 61 Years
- Summary: Berkshire Hathaway stock has historically performed well, rising in 50 of the last 61 years, indicating long-term resilience.
- Date: 2026-11-02 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPWEpBZDRaVGZiU1gyRXdOQ0IwYkFINklhcXpIT1RNVmNHWnFWY2VWNkNFc0N4NDZrSTdmQTREQVFReTJlaV84VUlDOFFIY25hLW1yaGFtamJnQTQyVkxoUkp4ZlN0aGExeTdKLTZNOXNqUUdOTnctQ0dTZldSaFNiY281RTlUY05HRTQtUjBnU0ZKVmpzRzA0M181N3I4VDJHLUY2bA?oc=5>

## HEADWINDS

### Berkshire After Buffett: Steady Hands, Big Bets In The Greg Abel Era
- Summary: Berkshire shifts strategy under Greg Abel, continuing steady leadership and significant bets.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxOc1FqWWVkbUpRTGV3cVpaa1VnN3N0dk5zYnF6LVhBd1NjczU0UEJmV014ZUdBYno2akE5NTB6cC1XY2VMVnlUeVRoNnJqQ01Qbk5KRll2SlRQZVg2V1JGZDdOaVdmSEFxNWRZeVBCM2QtOUlnRnktM0pyU2FaWGh1dXoyN2Y0U1J6QWpSZmlSWEZSdDV2ODFodjA4QUx2V1p1MkE?oc=5>

## CATALYSTS

### Berkshire Hathaway Q3 earnings on deck with focus on buybacks, investments, cash (BRK.A:NYSE)
- Summary: Berkshire Hathaway Q3 earnings on deck with focus on buybacks, investments, cash (BRK.A:NYSE)
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxOd3V0aFlwV3dzZ2JpdmFOUFFzQUtWS0MxRGpScEE5ZlRCejVaellmaERmQ1NTbVZmajRrOFA5bVY3aXQ4MHYxQk5VRWZNd0gxbXNvSldldnhfeHhzTnlDRkY2VHlpeWItS3FfWENQTlpRVHRPcjhwaVpldW1lRG1sdHlPZ096MU1CMjVfR3VkZ0gyaG5EYnEtSXl5aHlRbV9wOXh0SEQzYjc0QWxvOXVqSzZLTEk0VTA?oc=5>

### Berkshire Hathaway Q3 earnings on deck with focus on buybacks, investments, cash
- Summary: Berkshire Hathaway Q3 earnings on deck with focus on buybacks, investments, cash
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxQZmpBLXAydEQwNGpEZi01Q3ZLeFREaVVkR2QtWVh3UzUwU3FTVjd3ckwwbkIyd1dDTWVhck5LS0pfWWtCX0Nsd2xaNUZIX3BGQ3FheHpLMmVoT0VicFFwUmlKUWtvbHNFdGRTdnh3NDljaGhMeW1YUWt5MkFZZ2NZR2p6dkZySmxwY2NlVTlQNWlRWU0wejFla0tReTUyNGJJSlBSMjMteDJISTVBUVhyUVE3b1ZudWtPVTJpU3lWUGRCVHlZNzFVeDM4SDNiTWg1b1JFVGtMa3k?oc=5>

### Berkshire Hathaway Is Buying More Sirius XM. Here’s What It May See
- Summary: Berkshire Hathaway is increasing its stake in Sirius XM, potentially expanding its media portfolio.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNNmFRR3dWNThYNkVNZUl0SnhGS3JaQ3J3Q2hsN2pseHlNRDJVWTV1dEs1MHRBQUtVNDNJZjg1aHNJTDNfcFhQX2dUcTc1VF9kTFJwbzBWdm1Sd0p0WnRTbTFpZDBEV2dseEhxdVJsZjJyTFBnNHZFN3JGc2U3dVJDTkdkMVBtamNKWENuQmhUdm9UUVB0cDFkQkNnQ0JmMzdmUVRjaA?oc=5>

### Greg Abel’s Next 13F Lands November 16, and 1 Question About Berkshire Hathaway’s $299 Billion Portfolio Looms Larger Than Any Other
- Summary: Upcoming 13F filing may reveal portfolio changes, potential impact on holdings.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxNNEVVcjVzM2U2T1lJaThYTlZWZUJJdDFGYlVYTWtPNzhUZ2ROcHFsN3JnMXhWWTNMaTlibUVjMldLTGh0RElpdTd6TExzSDFJSEtxR1RmNmQyXzBYSEQ4Uzl1bmdOYW5lQkw2MzB6Z3ExY2kzSGFQYVU3UnF3YV9BcWNhbkFWVW1EQ2t5dEQzY3pHdk0?oc=5>

### 2 Berkshire Hathaway Holdings to Buy After Record Third Quarters
- Summary: Berkshire Hathaway plans to acquire two holdings following record third-quarter performance.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQUzc5U0lRWFB3UWhTdEEzazg2SU5tekdwVTNXWTY1M3MyM0lWbXhiUFpBVUF2MUtBcEFVblN6a3pENzcybFJyNGhWcnZXTU91aHhtZS04QklkelJjZ09qS01RQjFhNUQxQmZNWVI2UUUwei13VzVkM3RGX0ZRUVhEelZBTDg0QkNyamJMVkd2WEM2TUU0dkZfeE1Fd05xeGc?oc=5>

### Berkshire Hathaway Bought Back Its Own Stock at About $488 a Share in June. Should You Buy It Near $557?
- Summary: Berkshire executed a share buyback at $488, signaling confidence in its valuation.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQbG5zTjdicEpSQWo0VmpoOENFWFF3ZGpjcVZpT3NoNlhCUlAtSmJjZ2tmSC1udEw3VllhcDR5RlFVZUVtWmJ5Q3gwVFMwOW5GMUYxQnZGd1l2aGdBQi1zNEZ4NGhoTUU4YXRlOEJySjJMVHdyTU9qWEo2OTNrRzAwLWp0dHFFUXFqSlpEeVg0dTBvWHdj?oc=5>

## RISKS

### Berkshire Hathaway: The Easy Re-Rating Is Gone (NYSE:BRK.A)
- Summary: Berkshire's easy re-rating has disappeared, indicating potential credit risk changes.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxPSGUzZzN3eG1yME1RSXRweXlLR3NxLTlqcVYzSDFDd19fN2tJQUdIaWlYNXYyTXVxc1dkSnlvVlFyaVBpcW01a1piYl83SkJuMVVKTWM1RGZ2STVQck9LRVZFNlA5Ykd4XzY1RmVkWGx4dW5FZ3lPeWE1Q1NuY01lZGplUEwtS0RLLXdPbE1Xbw?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **BRK-B** | **14.36** | **0.00** | **-1.79** | **10.00** | **1,222,109,822,976.00 USD** | **15.76** |
| MKL | 13.80 | 1.28 | 7.93 | -11.20 | 23,713,228,800.00 USD | -3.49 |
| FFH.TO | 9.87 | 1.41 | 8.66 | 1.90 | 57,459,585,024.00 CAD | 21.78 |
| L | 15.17 | 1.22 | 8.61 | 1.90 | 22,186,129,408.00 USD | 8.20 |

Peers fetched as_of: 2026-11-06; BRK-B reuses existing data (market data as_of: 2026-11-06); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-08
- Next expected earnings: 2026-11-07 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-06

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-10
- Revenue (latest available single quarter): 101,808,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): 25,667,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1067983/000119312526341032/brka-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimwFBVV95cUxQY0FyNElEb0JXNUptbU1IRnJjWHEtekVkVHFZbTA2RmxBcG9ncmxpSWQxeEtmeHltc3hjZFluTGd4eUh4MEZWRUp6VWRmZ0FhcjJXRV9HTGN5Mm5hMlF0a1VFOGxjS3E0dkFUQWN4OGlEdmRBWTR6aFZlVlZBaFZmUEtNZVotYnVhSjBLN1ppUy1vZGNxQ2JkRXEybw?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxQRm5DaTN3NmRadmh5LVczYXBueVBlUnhtaDZrQ2FGRGtmS0J1WnRkOWcwQ1FmT1pLN0dwQUV2ajRWZENUTGRFRmRBMEpJdjBMbUVmcnB0ZGxRWTNDRWV6RlItbjBfWndhNWVhVVZuWkxWdUY5RnZmU3h5dVlfaXItdEs4NDN5RVdnTFF6RnNBWXZMTExSRUoyS3B6UTNiSE9qbWx2X3VHNVZYRENl?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxQak5Sd0pMYUk0aERTSUVoOXlTMXpCdk90V0dWSDVySW5HcEpyOVFQNUtUM2pDdTBKM2I3OERlbDRJcWk4OHVtdWdZazZEOXBfVDJzbk1RbmlaR3JMUmRnVUQ1bmpZVUdtVDNUUkJnTDhaZmtRaXdjci1CUklzVkE4RTc3TTZBMEkxNzYzWG5Qejk2anFWR3BESk11al9KWkVsMXNsRGlNeF9VRG5UMzFVcnlRbXdUa1oz?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxQaFk0ektfOWtITzBVYXRoYXVjVTZub3gyclBPS05TNDR1N1lPSm80Y2lid1dJclQxY2Z6VmpSVGpRTk9NSHFUdzl5M0NHX0phWFUzOXJOV0FNWlJsdnJ0UmhEZU9PSXVLQ1h0UGdlaml5dVJnSml4NVZCRmV3dDdfQzFiWUUySHVLd1pUcQ?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxOc0w4a19pY1htemludV9nRkY5RnVOcmNxRUoxQzdOakxSUnpYYzFNQU42M29VUjh5ODk3MTZueVpEMUtuZEs4Y3pySnM4TXFUeWxqTzgtQzYxMnFwRmh3S3dKYTlHblJ2em5FNkVlTkZ4TEYyOUI3SGRLenZod3hpSGM3b3d4NW9jZjZnTWctUjZrWjQ4N0dzOVlLeHBuV1pOSlhPTlNWREI3cmUxMzZaM0cta1g4d25kVHc?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPWmxkMW4tQXR5X09YUWJIXy1QMFE2VTA1NjkyTEx0MTBmZHRhQUJiTzAxMnBBR0Q0dUhpNVB5VHBrWTJ3N0g2b3RvYkZybnlmM0IyYmpXMHlhNHZQLVM4b0VhOXhxYmNSaEZCRF83WVFiQXVjZDN6bWJQSE9MSFR3TE04akxPWWhzOWtGMC03bVlOei1qeFVWLTBVeVh4QjZFWmtNajNKWGpxZw?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxQWDVzSlBjckRRN2JXTjRubUVLb1BCOENjMV9PZzNPQzREZVBNUzd0emhtOHRhQ21MTlkzY21qVXktNEticzJRVFpZdEVrUWZ0MEM5R3gzTlFDbjdLLV9IZ2VzWDZERklMcjJ5UFllMFQyVGJtYmdSS2l4Sm9tVy1HUE82c1pLUzlUeWFrXw?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOV1FIelB2WWcybVl2OE1MblZFWlBQVXhGUEFqcGhOenRiYndFNVFkaUpST3dtTUxoam13N3g2Zm90S1pLSm9XaWMxYXhMWEtYb19Hd3RyUkNhQ0d2cGwtZVJuNTdBT3lWb3J2WGFVbFJWeFJlUHpKd1I3SnROZWx6Z0ZrazhTRWNXVHlMbmFHWlFtbEIycHMxT2VpZw?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxQRTFYN1AwWVpyUUxvMWF3R004djZQc0ljZFpSUmtzckhuU1hTX0dhZnBzNkk2UUw4d0VjTHBBbXUwTlUwUFhReGt2TmdIUVhnZzVpbjY5cy1XeTRnWi10MTlubVhxdDIxS2s0bExjWmQ0U3VhYmpfOFYzUWdTXzU4dElmUUJVcl85VUJiS2w3c0c3TTg5Q1plYzVPcnJjTGQ3OEFHTDJyNHVoZDNXTkNuZk1xRko5eXFMQXdjclR0OWp5ZUtNR0FwUFJoRmxpR2xIYkxOVVF3?oc=5
- https://news.google.com/rss/articles/CBMi4gFBVV95cUxNdlk5ZDQyTU43VDFLV01oUEFrWWpVSWRINV9tZUhibGgtRlllbzdjOE9fVWlHNGc5TjYyTlRjUkdoMllrRG81c01UNDJZUUtkb09vSHQ1N1I5dFU1YzlwZm8zZm1LVGhGc0pFYVRjMEUxQmZ0S0JSeXp6RDJDTWF2SHY5SkRRUWMzS204dVRvUFE5N3NyenV3UlRmd0JIejBmTl95S2RISUV2VHpCSDN1SG90Q2hCa3pRWjhkaDN5RDYzVkR3bU5mdFNSN01QS2d4V2FzeUNJZUVHdzNMZk82Y1VR?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPWEpBZDRaVGZiU1gyRXdOQ0IwYkFINklhcXpIT1RNVmNHWnFWY2VWNkNFc0N4NDZrSTdmQTREQVFReTJlaV84VUlDOFFIY25hLW1yaGFtamJnQTQyVkxoUkp4ZlN0aGExeTdKLTZNOXNqUUdOTnctQ0dTZldSaFNiY281RTlUY05HRTQtUjBnU0ZKVmpzRzA0M181N3I4VDJHLUY2bA?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOc1FqWWVkbUpRTGV3cVpaa1VnN3N0dk5zYnF6LVhBd1NjczU0UEJmV014ZUdBYno2akE5NTB6cC1XY2VMVnlUeVRoNnJqQ01Qbk5KRll2SlRQZVg2V1JGZDdOaVdmSEFxNWRZeVBCM2QtOUlnRnktM0pyU2FaWGh1dXoyN2Y0U1J6QWpSZmlSWEZSdDV2ODFodjA4QUx2V1p1MkE?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxOd3V0aFlwV3dzZ2JpdmFOUFFzQUtWS0MxRGpScEE5ZlRCejVaellmaERmQ1NTbVZmajRrOFA5bVY3aXQ4MHYxQk5VRWZNd0gxbXNvSldldnhfeHhzTnlDRkY2VHlpeWItS3FfWENQTlpRVHRPcjhwaVpldW1lRG1sdHlPZ096MU1CMjVfR3VkZ0gyaG5EYnEtSXl5aHlRbV9wOXh0SEQzYjc0QWxvOXVqSzZLTEk0VTA?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxQZmpBLXAydEQwNGpEZi01Q3ZLeFREaVVkR2QtWVh3UzUwU3FTVjd3ckwwbkIyd1dDTWVhck5LS0pfWWtCX0Nsd2xaNUZIX3BGQ3FheHpLMmVoT0VicFFwUmlKUWtvbHNFdGRTdnh3NDljaGhMeW1YUWt5MkFZZ2NZR2p6dkZySmxwY2NlVTlQNWlRWU0wejFla0tReTUyNGJJSlBSMjMteDJISTVBUVhyUVE3b1ZudWtPVTJpU3lWUGRCVHlZNzFVeDM4SDNiTWg1b1JFVGtMa3k?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNNmFRR3dWNThYNkVNZUl0SnhGS3JaQ3J3Q2hsN2pseHlNRDJVWTV1dEs1MHRBQUtVNDNJZjg1aHNJTDNfcFhQX2dUcTc1VF9kTFJwbzBWdm1Sd0p0WnRTbTFpZDBEV2dseEhxdVJsZjJyTFBnNHZFN3JGc2U3dVJDTkdkMVBtamNKWENuQmhUdm9UUVB0cDFkQkNnQ0JmMzdmUVRjaA?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxNNEVVcjVzM2U2T1lJaThYTlZWZUJJdDFGYlVYTWtPNzhUZ2ROcHFsN3JnMXhWWTNMaTlibUVjMldLTGh0RElpdTd6TExzSDFJSEtxR1RmNmQyXzBYSEQ4Uzl1bmdOYW5lQkw2MzB6Z3ExY2kzSGFQYVU3UnF3YV9BcWNhbkFWVW1EQ2t5dEQzY3pHdk0?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQUzc5U0lRWFB3UWhTdEEzazg2SU5tekdwVTNXWTY1M3MyM0lWbXhiUFpBVUF2MUtBcEFVblN6a3pENzcybFJyNGhWcnZXTU91aHhtZS04QklkelJjZ09qS01RQjFhNUQxQmZNWVI2UUUwei13VzVkM3RGX0ZRUVhEelZBTDg0QkNyamJMVkd2WEM2TUU0dkZfeE1Fd05xeGc?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQbG5zTjdicEpSQWo0VmpoOENFWFF3ZGpjcVZpT3NoNlhCUlAtSmJjZ2tmSC1udEw3VllhcDR5RlFVZUVtWmJ5Q3gwVFMwOW5GMUYxQnZGd1l2aGdBQi1zNEZ4NGhoTUU4YXRlOEJySjJMVHdyTU9qWEo2OTNrRzAwLWp0dHFFUXFqSlpEeVg0dTBvWHdj?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxPSGUzZzN3eG1yME1RSXRweXlLR3NxLTlqcVYzSDFDd19fN2tJQUdIaWlYNXYyTXVxc1dkSnlvVlFyaVBpcW01a1piYl83SkJuMVVKTWM1RGZ2STVQck9LRVZFNlA5Ykd4XzY1RmVkWGx4dW5FZ3lPeWE1Q1NuY01lZGplUEwtS0RLLXdPbE1Xbw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
