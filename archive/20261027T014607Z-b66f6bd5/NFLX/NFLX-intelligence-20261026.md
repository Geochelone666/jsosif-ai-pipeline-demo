# NFLX Intelligence Report

- ticker: **NFLX**
- Report as_of: **2026-10-26**
- Market data as_of: **2026-10-26**
- Quant sources: https://finance.yahoo.com/quote/NFLX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NFLX/key-statistics/
- AI analysis snapshot as_of: **2026-10-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-27T01:47:35.018934+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 8, 'ai': 13, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 1, 'positive_sentiment_in_headwinds': 1}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 7 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 60.87%; oldest publication 2026-10-21

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 63.9000 |
| Return 1D (%) | -2.9613 |
| Return 1W (%) | -8.5182 |
| Return 1M (%) | -10.1897 |
| Return YTD (%) | -31.8473 |
| Return 1Y (%) | -41.6273 |
| Annualized volatility (%) | 35.9398 |
| Beta vs SPY | 0.2168 |
| Max drawdown (%) | -44.7948 |
| Sharpe (rf=0) | -1.3296 |
| Downside deviation (rf=0, %) | 26.4132 |
| Sortino (rf=0) | -1.8091 |
| Historical VaR 95% (1D, %) | 3.5205 |
| Historical ES 95% (1D, %) | 5.1308 |
| Correlation vs SPY | 0.0767 |
| Tracking error vs SPY (%) | 37.1921 |
| P/E (trailing) | 18.47 |
| P/B | 8.96 |
| EV/EBITDA | 17.03 |
| Revenue growth (%) | 11.80 |
| Forward P/E (estimate) | 16.95 |
| Gross margin (%) | 50.69 |
| Operating margin (%) | 34.63 |
| Return on equity (%) | 53.46 |
| Free cash flow yield (%) | 9.57 |
| MA50 | 73.9828 |
| Close vs MA50 (%) | -13.6286 |
| MA200 | 82.1418 |
| Close vs MA200 (%) | -22.2077 |
| RSI (14, Wilder) | 33.4634 |
| MACD (12,26) | -1.9830 |
| MACD signal (9) | -1.6231 |
| MACD histogram | -0.3599 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NFLX': 268, 'SPY': 268}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 63.9000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.9613 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -8.5182 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -10.1897 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -31.8473 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -41.6273 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 35.9398 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.4132 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -1.8091 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.5205 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1308 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0767 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.1921 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.2168 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -44.7948 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -1.3296 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.9500 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 50.6850 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 34.6320 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 53.4630 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 9.5746 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 18.4682 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 33.4634 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.3599 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -13.6286 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -22.2077 -> Clearly below the moving-average trend level.

## TAILWINDS

### Netflix (NFLX) Stock Stays Cheap After Its 58% Three Year Gain
- Summary: Netflix (NFLX) Stock Stays Cheap After Its 58% Three Year Gain
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOVmpXNWh4OWZNOUI5d0lnd1NGYzBBU2tLSFhPeDY3UFpFM1ZXODVVdzNuMy1CM1pMelUxdFZEQ25XVW5NMHlPYnZ1WFZ3RXZXbXB6aDg2eFpWNUF5RC1KWUFJc2dmMHlkbkJQY1k2Z2JLb25RY0J6cURXR2hxV1AzZDZMM0dvWW84WHFIalR2Q05pbDZzMlBpekhKdw?oc=5>

### Netflix: The Ad Miss Is Offset By Record Buybacks
- Summary: Record buybacks counteract ad revenue miss, supporting financial health.
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxOQUVBS2FkdDBjMEpaN2tqRm00OG1WOEJFUnFTMHctQWVVamxSOFdhUkdnLWhqVi1wZ1VOUXRuNGNJOTV2LUpmcW9OSXdFTVRfcFJUb19CWEl1ek1MU1RXcTlhRzU1M0cxWnRWbzh3dGk0S2VIcXh0STRiRkRiVHdfN0hncFFpVHVuXzlTRjgwcTAtMG8?oc=5>

## HEADWINDS

### Netflix Drops 4% as Engagement Worries Outweigh Earnings Beat; Disney and Spotify Slip
- Summary: Netflix Drops 4% as Engagement Worries Outweigh Earnings Beat; Disney and Spotify Slip
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxNQkpSSVcwbDQyLUs4clU0dV9mUGdRZkpabnpJNTNLbmZucTIycF9nWDNFZjdValFmODFYOVJ6VWphQmlhaW1GWDBpTXRMTU9udXZCZ2JZRjRfajM2VXRsbHV0S20zdnNBOGQ4VHliZEU4eEFiTl9NdU5hNkRZaUdjd0FET2JZR0NsS2VzdTc1cDlnWnlkMW1xYlRGRmluSUd4VVNqQ0tBNEFjTUx1VlM4ZzZQeWkyT0s0eW53akhOc29kSkJzUGNV?oc=5>

### Netflix (NFLX) Stock Price Falls As Q3 Earnings Stir Valuation Doubts
- Summary: Netflix (NFLX) Stock Price Falls As Q3 Earnings Stir Valuation Doubts
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOVmRBaFZXZGZad2d5SGVQS2J4c2xPOTdpNjNqRmlQWXliMWpIVFdpV2RsSlZ1NHRiUFBtZ0hQbGxDS2U3bjBSNE5pR2hlUFNPY3Y4YVp2LUhsRHlvZ1dhemdCc2twWXJYX2JBZm1ELU5fRGJVWnpFOTlQcU5sOGlGZl9qazJhajZTaFRqWnQ4X3kxVTBqWXFyMDdKRQ?oc=5>

### NFLX Stock Tumbles Overnight: Co-CEO Wants Netflix To Be Last Service Customers 'Ever Cancel', Says Live Events 'Drive New Membership'
- Summary: NFLX Stock Tumbles Overnight: Co-CEO Wants Netflix To Be Last Service Customers 'Ever Cancel', Says Live Events 'Drive New Membership'
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNVTBxOTVRYmtvSHVoYlluTGwyQjZNR3ZEeHZ2Nno3SzNmaHFPQ2YxMTU1enN6aExMMW1rRVg2dC1oQ1Z1WjJCcGNHVDhVUUJpWWJEOVFfZnRpUXpKYWVYTmRsclE3ZjJiY2dNZ0NxSGswb25zTy1xSzBHRmNKWjlzOVduNTRKRXRXeEtBS3RCRG81RTg4VXNPMHBKWTg?oc=5>

### NFLX Stock Slips More Than 6% Premarket: Morningstar Sees 'Best Buying Opportunity' For Netflix Amid Negative Sentiment
- Summary: NFLX Stock Slips More Than 6% Premarket: Morningstar Sees 'Best Buying Opportunity' For Netflix Amid Negative Sentiment
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNYXVuTzRUeVNQZHhoTUpSZzg5aEE4VnhPYWh5YVQ4UmplQ1B4T1ktSDN5aHpMVFY2cm01QnRGS2FWWWxSMmlOTmYxS2kyaWVCZHdDZ0Q0NC1Bd1JGWG54cVdBdDktWnJKMEJZVldCOGRaUVhCQkdNYjBMTVNxakdjYjRyZFVSRUNrX3BrbERTUXJmdw?oc=5>

### NFLX Stock Heads For 26-Month Low After Needham Downgrade, Wall Street Price Target Cuts — YouTube Threat Grows, Content Problem ‘Seems Clear’
- Summary: NFLX Stock Heads For 26-Month Low After Needham Downgrade, Wall Street Price Target Cuts — YouTube Threat Grows, Content Problem ‘Seems Clear’
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOSTNsWGs5VllLU09RdWlFcGkySkh6UTRaTUVCRFplcm5GamFZQnFhVFhvQnJzU3JMQkRFT3NuVjJCNThrX0s5X0pYeW9TT1p4RWNpUGtja0hNYy1nUXhUZjlCYklKN3RjNzhpS3NtN2F2dVVOY0R2OXhLNXF0UUp2VkNrdVVxMVVQeHR1cFdnOEx5Q2dn?oc=5>

### Netflix Stock Drops Over 6% Following Expected Revenue Numbers
- Summary: Netflix Stock Drops Over 6% Following Expected Revenue Numbers
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxORFVyZ3JGNEJIdWMyYndUX1d5MTZwX1h2VmxmakJ0TEphU0RVLUt3RHJRMlBlQ1QtLU12eFV6eE5GN0JSdWRIWXJVNl9NX0JqVlJBVDZyZEN6akdUb1pReWk4TUpiWmNuakdkVVVmaUVCR0tFc3lfTC1uTmNTYUd5SzBUUVgtcVA4bHZrMkpjY2E3VG4tV3c?oc=5>

### Netflix Is Down 51% From Its High. History Suggests This Is What Happens Next.
- Summary: Stock fell 51% from peak, suggesting potential decline.
- Date: 2026-10-25 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNeW5MLXZUaEFoNFJQeElyX2JzWnlHc1hRS3V2YV9GOFpSLV9La0JJTFdCOUtXaDU1VG05UUhrWXB2M2RzbXgtOTJNVVlPZmpXd3VYOVcwd1Zoc2FlNHhrcGgxMGRFbGxINEU1ZG1fOThTZ2s1WlE4Y1kxb00wZXhqTkdSaHZtS0F6a2RzdjY2TUtiWHV4RzBoXw?oc=5>

### Netflix Q3: An Opportunity Hiding In Plain Sight (NASDAQ:NFLX)
- Summary: Q3 earnings may reveal hidden upside.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxQUTBjcy1lMWVqMHEwVzJ6dmNJYmJuM011ZG5pUXFlQTRWbGs3MkpEYlhzSmp5ajJhcWUzYnQyQkQwV2ZuZllmOFZlYm5lYWRITHZHcS1rS201OWg4ZElvSU1jVFdMeHhsck9qZkZtN0IyWWFkZndsSHVoUDRYclczaVNCTWVsanVLTUUxS285U3NQdw?oc=5>

### Netflix Is Now Down 29% This Year: Is NFLX Stock Hopeless or Ready for a Rebound?
- Summary: Year-to-date decline of 29% raises doubt on rebound.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxQLUd5d2xvbWNXbkpvYmY3VmhEYUtsbU83V2VIMnptYW5WbUNMZ1dibkJmZEwxYUg0RXhmOWRQZ0t6aW5RaTNoUkQ4Y3ZEZ3FaU2FGSjl2VC1uQlE3bkNnVUtaNi1DY1RzS05zeE55ZGNuS2UtYmlSbTR2ZDlqRXNvaTF1V3QyalNmNkdYN3JsTU50bDZwNXFvR0FVajlpODFvWlZrSGlpYmhDRTg0a0RkWTRLWXFFdzg1YmxZc3RFSQ?oc=5>

### Netflix's Higher Spending Fails To Lift Engagement, Says Wolfe In Downgrade — But Argus Still Sees 46% Upside Potential
- Summary: Increased spending did not boost engagement, leading to a downgrade.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxPMzE0ZS11V251a2V2ZVR2UmxfU2RsWlloVUVpSVR0cklncGpBdkxJVV8wc1lweHEzUDhWZzU1b2JkOTRpRkVKRV92UnFkc2M3S181Vkt3RHFZVEtodHNHbmE4R3Jyb2dNeU81V0MyWUx1SkJOdVFQRWw3ZkJrWUxfcjVTOS1LQTBxMzhUbGlrNkcwdVhQTWtjU0dDdW9QZVBQZnc?oc=5>

### As Netflix’s Slowdown Becomes More Palpable, I’m Still Not Giving Up on NFLX Stock
- Summary: Netflix’s slowdown is evident, raising concerns for investors.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxNV25PMTdvVEpvR1hmVFVSc1AyTjRURjZtb21qTDQxUHllWDdHaVdmRF9mY1JIU2RsQ191T3NhOUFuaW5PZlFtOHVKTTlZNmpaZ3N2RmJ6cnJyNXAwT3R5bV8ya19pb2pFYXVQT2lURW0yNk9OOUlLT3NIeHdzWDNZRW9mTUt1bk9WSEt4WHQyTFgxdS1EWHUxVFAyVDVNYUgyaVp0VE1DY0xnSXZpVlVWY3BuT01vczQxcjVJYUhLZEQ?oc=5>

### Down Roughly 50% From Its Highs, Is Netflix Stock Finally a Buy?
- Summary: Stock price has dropped 50%, questioning buy potential.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPaUxsUFM0YmRJeEtMU3VUTG1kT0FEMVpHckhVenVyMXZ5Y25YZFlhWGc5SklnZWJJNHljMzA0NmlGTGdTU3VYTUtlenBKcFhLcXhYN0MxdGVyQkk4eDZfQU9WZ3hOelJoU01ocnQ3UEQ0R0ZNWWRiSEZIOERkaTBoMnMtY3Jnam9CaTlKMk41OGpPMVdl?oc=5>

### Netflix Stock Has Always Overcome the Odds. Has It Finally Hit a Wall?
- Summary: Investors wonder if Netflix has reached a performance ceiling.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPMlEtcTktT2NrV1BGT2V2UVhMVFE5OE9sQVFPMmhfdUh5dlF3SzI5QXdmTF9JODNXZFFIY2IyQy1uemZYZ2NIdENSOWktblBtY3RvMHlRaFR5aDRsQzl3b0JFM1ByRHpDOGhxODBwc3E5ekVpamtvTTlNVVhfNnVyOEVROGpGcno2NjZINmVwLWU3SENkN2hR?oc=5>

## CATALYSTS

### Netflix (NFLX) Stock Fair Value Falls After Cautious Q3 Analyst Revisions
- Summary: Netflix (NFLX) Stock Fair Value Falls After Cautious Q3 Analyst Revisions
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQSE1oLXBDN2dSRUZabVZhbzJvTDZpSVV3NmNVQ2VlYjJJQVVRSTBfQmJHT2FhWGt6LUl4NjFBMElxaVFGajh2eWlIRm1abUp2cFVoekg1VGdZN0pmbGV2ckZjWXB2ZzcwRWV2RkZ6S1pqVTBFNjRuamREVk5RMkoxZUw5ZjZyQXg1SDNHdzRIWDhweXJYTGpacC1R?oc=5>

### NFLX Stock Breaks $65 Support as Engagement Concerns and Advertising Outlook Disappoint Netflix Investors
- Summary: Netflix shares fell below $65 amid concerns over engagement and advertising prospects, prompting a sell‑off.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi4AFBVV95cUxPamR5dml1d0NnLXBfQi1majRZQ1poc1pDU0NQc2F0c294SlVfekZ0QklrR0Yzdi00dnU0a0k5dFBLaC1McjZENzZ2V05PbWk1amRyOXAzQzE2TFNZTlZWcHNSUm5XUXZlRmJWYzJIcTBSU1VOTzRQYk9FZ0E5VW9VOC1xS1B0UjZCUHl5T3gzQUdKaTh0WDBTSXJZRWVZeG9ZVjhGMWNfQnc5WjlKRHE2bjd4U3ZSQU1tS0FJOVZFSTV1YlNPS3paR3lYc0VfZUE1LXhhRTRFdEQzOTNQYmJ6cg?oc=5>

### Should You Buy Netflix Stock After Its 51% Plunge?
- Summary: The article questions buying Netflix after a 51% drop, highlighting potential risks.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOS0JnUml0VTFqcjdudFhjaW55d3M3cnpzMjFDby1iODYyUFJiZzN5TkExMFhHVEFjb0JjRDFuSVJEaE03MWUtdkJrcXN6LWRtS01WYmtFWHI5U0Y5dFhqbUdXYS1KVkJhdE5CY2tQN0thdC01UVRUeWJLVlNUY2VKa0NMSXlka0p5MFBzZ1lxa3hydU5tVVdF?oc=5>

### Why Netflix (NFLX) shares are falling today
- Summary: Explains factors behind today's decline in Netflix stock price.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQMi1rUzE5c3J6OEZESUJ3RmhEZkNsYldiRXMxRDRBX1g1eFRLd2pZQ3dHUl9ZZDFlVF9KYlk0OThYS3Q2bG9mVGtYWUIxTUhYdFNRVF83bUtFemNmQ29xSk1vd1ZQUURvbWJVMjEtdnEzUWl1cW0yRmE1LVNWYUZzamNCbEVDamFZeFczblY0ZHdzU0JZLXRBNEM0RjQ?oc=5>

### Why Netflix Stock Dropped Today
- Summary: Details reasons for the recent drop in Netflix shares.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQVW92S2lTTzBKRUp2ejdoX1MzMGVGZTQzTFJ0Qk51WFI2SEVIMEJDQ25SUm8xcTZaZ0ROaml0WVF5RHptLUM2UDI3Wmg0SXowX2Rhazd0X1BUSWUwLXpMemxwc09mTUtMQmFrUWUwQmxkZW5CcmFjYl9DVVJYZEJyRmMxV1htWm5oVEwyVU8tYjNIZXp0VzN0UlZKb0s?oc=5>

### 1 Reason Why Netflix Stock Looks Oversold
- Summary: Identifies a single factor suggesting Netflix shares may be oversold.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOd1o1cTIzd25kckM1eDdzeTJBRkYycXRlZzBLd19NS1FVTThIME5maVhYamNtcjVrU0pPTWpHVVZBUXRhNzU2a1NnQXpDcnhJQ282aFJiY3hwVzhnOEZOaDdCMDkwUXlKN05IN1JWT284ZExXVGNfZXpQb2VKTTYzSzBvNHFoTEZjRGZBT2hjV3R5ZXlzU1E?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NFLX** | **18.47** | **8.96** | **17.03** | **11.80** | **266,075,750,400.00 USD** | **-41.63** |
| DIS | 22.76 | 1.74 | 11.37 | 6.80 | 190,626,234,368.00 USD | 0.29 |
| WBD | N/A | 2.36 | 13.79 | -11.20 | 77,595,885,568.00 USD | N/A |
| CMCSA | 6.98 | 0.85 | 4.72 | -6.10 | 78,299,684,864.00 USD | -15.34 |

Peers fetched as_of: 2026-10-26; NFLX reuses existing data (market data as_of: 2026-10-26); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-20
- Next expected earnings: 2027-01-19 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-26

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 12,874,176,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 3,663,927,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimwFBVV95cUxOVmpXNWh4OWZNOUI5d0lnd1NGYzBBU2tLSFhPeDY3UFpFM1ZXODVVdzNuMy1CM1pMelUxdFZEQ25XVW5NMHlPYnZ1WFZ3RXZXbXB6aDg2eFpWNUF5RC1KWUFJc2dmMHlkbkJQY1k2Z2JLb25RY0J6cURXR2hxV1AzZDZMM0dvWW84WHFIalR2Q05pbDZzMlBpekhKdw?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxOQUVBS2FkdDBjMEpaN2tqRm00OG1WOEJFUnFTMHctQWVVamxSOFdhUkdnLWhqVi1wZ1VOUXRuNGNJOTV2LUpmcW9OSXdFTVRfcFJUb19CWEl1ek1MU1RXcTlhRzU1M0cxWnRWbzh3dGk0S2VIcXh0STRiRkRiVHdfN0hncFFpVHVuXzlTRjgwcTAtMG8?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxNQkpSSVcwbDQyLUs4clU0dV9mUGdRZkpabnpJNTNLbmZucTIycF9nWDNFZjdValFmODFYOVJ6VWphQmlhaW1GWDBpTXRMTU9udXZCZ2JZRjRfajM2VXRsbHV0S20zdnNBOGQ4VHliZEU4eEFiTl9NdU5hNkRZaUdjd0FET2JZR0NsS2VzdTc1cDlnWnlkMW1xYlRGRmluSUd4VVNqQ0tBNEFjTUx1VlM4ZzZQeWkyT0s0eW53akhOc29kSkJzUGNV?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOVmRBaFZXZGZad2d5SGVQS2J4c2xPOTdpNjNqRmlQWXliMWpIVFdpV2RsSlZ1NHRiUFBtZ0hQbGxDS2U3bjBSNE5pR2hlUFNPY3Y4YVp2LUhsRHlvZ1dhemdCc2twWXJYX2JBZm1ELU5fRGJVWnpFOTlQcU5sOGlGZl9qazJhajZTaFRqWnQ4X3kxVTBqWXFyMDdKRQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNVTBxOTVRYmtvSHVoYlluTGwyQjZNR3ZEeHZ2Nno3SzNmaHFPQ2YxMTU1enN6aExMMW1rRVg2dC1oQ1Z1WjJCcGNHVDhVUUJpWWJEOVFfZnRpUXpKYWVYTmRsclE3ZjJiY2dNZ0NxSGswb25zTy1xSzBHRmNKWjlzOVduNTRKRXRXeEtBS3RCRG81RTg4VXNPMHBKWTg?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNYXVuTzRUeVNQZHhoTUpSZzg5aEE4VnhPYWh5YVQ4UmplQ1B4T1ktSDN5aHpMVFY2cm01QnRGS2FWWWxSMmlOTmYxS2kyaWVCZHdDZ0Q0NC1Bd1JGWG54cVdBdDktWnJKMEJZVldCOGRaUVhCQkdNYjBMTVNxakdjYjRyZFVSRUNrX3BrbERTUXJmdw?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOSTNsWGs5VllLU09RdWlFcGkySkh6UTRaTUVCRFplcm5GamFZQnFhVFhvQnJzU3JMQkRFT3NuVjJCNThrX0s5X0pYeW9TT1p4RWNpUGtja0hNYy1nUXhUZjlCYklKN3RjNzhpS3NtN2F2dVVOY0R2OXhLNXF0UUp2VkNrdVVxMVVQeHR1cFdnOEx5Q2dn?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxORFVyZ3JGNEJIdWMyYndUX1d5MTZwX1h2VmxmakJ0TEphU0RVLUt3RHJRMlBlQ1QtLU12eFV6eE5GN0JSdWRIWXJVNl9NX0JqVlJBVDZyZEN6akdUb1pReWk4TUpiWmNuakdkVVVmaUVCR0tFc3lfTC1uTmNTYUd5SzBUUVgtcVA4bHZrMkpjY2E3VG4tV3c?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNeW5MLXZUaEFoNFJQeElyX2JzWnlHc1hRS3V2YV9GOFpSLV9La0JJTFdCOUtXaDU1VG05UUhrWXB2M2RzbXgtOTJNVVlPZmpXd3VYOVcwd1Zoc2FlNHhrcGgxMGRFbGxINEU1ZG1fOThTZ2s1WlE4Y1kxb00wZXhqTkdSaHZtS0F6a2RzdjY2TUtiWHV4RzBoXw?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxPZTg4c2VtT2d1SV9meTFhZFpzN2ItRk85YXlQWnAwQUxDRm5VMmhBU0RrVXAyRWROcWk4RUpFdk4yWlhkc3dlUjFyU3hkVDVkaklFNC0zTmRPRmJZNHQxN2xvYmQtMVlDVm9Bd2VJdkZIOEI1Mnh0blZMNEJ4d0FGOXBvY25ic1UwV2NYa2ZPcw?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxQUTBjcy1lMWVqMHEwVzJ6dmNJYmJuM011ZG5pUXFlQTRWbGs3MkpEYlhzSmp5ajJhcWUzYnQyQkQwV2ZuZllmOFZlYm5lYWRITHZHcS1rS201OWg4ZElvSU1jVFdMeHhsck9qZkZtN0IyWWFkZndsSHVoUDRYclczaVNCTWVsanVLTUUxS285U3NQdw?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxQLUd5d2xvbWNXbkpvYmY3VmhEYUtsbU83V2VIMnptYW5WbUNMZ1dibkJmZEwxYUg0RXhmOWRQZ0t6aW5RaTNoUkQ4Y3ZEZ3FaU2FGSjl2VC1uQlE3bkNnVUtaNi1DY1RzS05zeE55ZGNuS2UtYmlSbTR2ZDlqRXNvaTF1V3QyalNmNkdYN3JsTU50bDZwNXFvR0FVajlpODFvWlZrSGlpYmhDRTg0a0RkWTRLWXFFdzg1YmxZc3RFSQ?oc=5
- https://news.google.com/rss/articles/CBMid0FVX3lxTE11RzNQdUxJc2pOaVNJdC1nbjF3SnFMTHhyYXdzRzQ4UzVqdzZ1dU5aUmdHMjVxWW1GLWFsbVh5VExYXzB5M3hjYVhCR05abVl0VkNpNXdLUl9kWkpfYVBEZzEtdks4cGpMRHIyM0k2NnhSNlBXamxr?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxPMzE0ZS11V251a2V2ZVR2UmxfU2RsWlloVUVpSVR0cklncGpBdkxJVV8wc1lweHEzUDhWZzU1b2JkOTRpRkVKRV92UnFkc2M3S181Vkt3RHFZVEtodHNHbmE4R3Jyb2dNeU81V0MyWUx1SkJOdVFQRWw3ZkJrWUxfcjVTOS1LQTBxMzhUbGlrNkcwdVhQTWtjU0dDdW9QZVBQZnc?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxNV25PMTdvVEpvR1hmVFVSc1AyTjRURjZtb21qTDQxUHllWDdHaVdmRF9mY1JIU2RsQ191T3NhOUFuaW5PZlFtOHVKTTlZNmpaZ3N2RmJ6cnJyNXAwT3R5bV8ya19pb2pFYXVQT2lURW0yNk9OOUlLT3NIeHdzWDNZRW9mTUt1bk9WSEt4WHQyTFgxdS1EWHUxVFAyVDVNYUgyaVp0VE1DY0xnSXZpVlVWY3BuT01vczQxcjVJYUhLZEQ?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPaUxsUFM0YmRJeEtMU3VUTG1kT0FEMVpHckhVenVyMXZ5Y25YZFlhWGc5SklnZWJJNHljMzA0NmlGTGdTU3VYTUtlenBKcFhLcXhYN0MxdGVyQkk4eDZfQU9WZ3hOelJoU01ocnQ3UEQ0R0ZNWWRiSEZIOERkaTBoMnMtY3Jnam9CaTlKMk41OGpPMVdl?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPMlEtcTktT2NrV1BGT2V2UVhMVFE5OE9sQVFPMmhfdUh5dlF3SzI5QXdmTF9JODNXZFFIY2IyQy1uemZYZ2NIdENSOWktblBtY3RvMHlRaFR5aDRsQzl3b0JFM1ByRHpDOGhxODBwc3E5ekVpamtvTTlNVVhfNnVyOEVROGpGcno2NjZINmVwLWU3SENkN2hR?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQSE1oLXBDN2dSRUZabVZhbzJvTDZpSVV3NmNVQ2VlYjJJQVVRSTBfQmJHT2FhWGt6LUl4NjFBMElxaVFGajh2eWlIRm1abUp2cFVoekg1VGdZN0pmbGV2ckZjWXB2ZzcwRWV2RkZ6S1pqVTBFNjRuamREVk5RMkoxZUw5ZjZyQXg1SDNHdzRIWDhweXJYTGpacC1R?oc=5
- https://news.google.com/rss/articles/CBMi4AFBVV95cUxPamR5dml1d0NnLXBfQi1majRZQ1poc1pDU0NQc2F0c294SlVfekZ0QklrR0Yzdi00dnU0a0k5dFBLaC1McjZENzZ2V05PbWk1amRyOXAzQzE2TFNZTlZWcHNSUm5XUXZlRmJWYzJIcTBSU1VOTzRQYk9FZ0E5VW9VOC1xS1B0UjZCUHl5T3gzQUdKaTh0WDBTSXJZRWVZeG9ZVjhGMWNfQnc5WjlKRHE2bjd4U3ZSQU1tS0FJOVZFSTV1YlNPS3paR3lYc0VfZUE1LXhhRTRFdEQzOTNQYmJ6cg?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOS0JnUml0VTFqcjdudFhjaW55d3M3cnpzMjFDby1iODYyUFJiZzN5TkExMFhHVEFjb0JjRDFuSVJEaE03MWUtdkJrcXN6LWRtS01WYmtFWHI5U0Y5dFhqbUdXYS1KVkJhdE5CY2tQN0thdC01UVRUeWJLVlNUY2VKa0NMSXlka0p5MFBzZ1lxa3hydU5tVVdF?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQMi1rUzE5c3J6OEZESUJ3RmhEZkNsYldiRXMxRDRBX1g1eFRLd2pZQ3dHUl9ZZDFlVF9KYlk0OThYS3Q2bG9mVGtYWUIxTUhYdFNRVF83bUtFemNmQ29xSk1vd1ZQUURvbWJVMjEtdnEzUWl1cW0yRmE1LVNWYUZzamNCbEVDamFZeFczblY0ZHdzU0JZLXRBNEM0RjQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQVW92S2lTTzBKRUp2ejdoX1MzMGVGZTQzTFJ0Qk51WFI2SEVIMEJDQ25SUm8xcTZaZ0ROaml0WVF5RHptLUM2UDI3Wmg0SXowX2Rhazd0X1BUSWUwLXpMemxwc09mTUtMQmFrUWUwQmxkZW5CcmFjYl9DVVJYZEJyRmMxV1htWm5oVEwyVU8tYjNIZXp0VzN0UlZKb0s?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOd1o1cTIzd25kckM1eDdzeTJBRkYycXRlZzBLd19NS1FVTThIME5maVhYamNtcjVrU0pPTWpHVVZBUXRhNzU2a1NnQXpDcnhJQ282aFJiY3hwVzhnOEZOaDdCMDkwUXlKN05IN1JWT284ZExXVGNfZXpQb2VKTTYzSzBvNHFoTEZjRGZBT2hjV3R5ZXlzU1E?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
