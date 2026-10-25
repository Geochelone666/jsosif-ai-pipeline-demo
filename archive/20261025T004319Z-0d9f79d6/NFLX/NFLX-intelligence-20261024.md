# NFLX Intelligence Report

- ticker: **NFLX**
- Report as_of: **2026-10-24**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/NFLX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NFLX/key-statistics/
- AI analysis snapshot as_of: **2026-10-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-25T01:20:23.218104+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 14, 'ai': 5, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 9 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 66.67%; oldest publication 2026-10-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 65.8500 |
| Return 1D (%) | -1.7897 |
| Return 1W (%) | -6.6355 |
| Return 1M (%) | -7.7214 |
| Return YTD (%) | -29.7675 |
| Return 1Y (%) | -40.8669 |
| Annualized volatility (%) | 35.7921 |
| Beta vs SPY | 0.2203 |
| Max drawdown (%) | -43.8099 |
| Sharpe (rf=0) | -1.2946 |
| Downside deviation (rf=0, %) | 26.2481 |
| Sortino (rf=0) | -1.7653 |
| Historical VaR 95% (1D, %) | 3.5133 |
| Historical ES 95% (1D, %) | 5.1308 |
| Correlation vs SPY | 0.0784 |
| Tracking error vs SPY (%) | 37.0402 |
| P/E (trailing) | 19.03 |
| P/B | 9.23 |
| EV/EBITDA | 17.53 |
| Revenue growth (%) | 11.80 |
| Forward P/E (estimate) | 17.47 |
| Gross margin (%) | 50.69 |
| Operating margin (%) | 34.63 |
| Return on equity (%) | 53.46 |
| Free cash flow yield (%) | 9.29 |
| MA50 | 74.2680 |
| Close vs MA50 (%) | -11.3346 |
| MA200 | 82.2750 |
| Close vs MA200 (%) | -19.9635 |
| RSI (14, Wilder) | 37.1202 |
| MACD (12,26) | -1.7364 |
| MACD signal (9) | -1.5331 |
| MACD histogram | -0.2033 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NFLX': 267, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 65.8500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.7897 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -6.6355 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -7.7214 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -29.7675 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -40.8669 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 35.7921 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.2481 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -1.7653 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.5133 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1308 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0784 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.0402 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.2203 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -43.8099 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -1.2946 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.4705 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 50.6850 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 34.6320 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 53.4630 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 9.2911 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 19.0318 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 37.1202 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.2033 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -11.3346 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -19.9635 -> Clearly below the moving-average trend level.

## TAILWINDS

### Netflix Beats Q3 Earnings Estimates But Braces Wall Street for 2026 Ad Sales Whiff
- Summary: Netflix Beats Q3 Earnings Estimates But Braces Wall Street for 2026 Ad Sales Whiff
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxQV2xrakJTS3dXNzdZd3JzWWpodUd4Z1A3SlVoalJkQWMzTUpOYU9yNXBFMm5IN3p3RHdBbk9QZWZxbVUxSnBXRXFzUlk2bFozTUtnVEtpT3RIQUU5c3RqamYzd0ZRcVFvMlZZTjhwT09fM0k2U0gzdmlDWVRuUlBiRm9KY0JLajBfYmVJV2p3R01fQk9aa1FYUVBVNjRBbVpYajVJM3VaX1RDZ040bkZ5b0tLSjhDY2YtV1RtZ3hpWXlwYjJW?oc=5>

### Netflix (NFLX) Stock Stays Cheap After Its 58% Three Year Gain
- Summary: Netflix (NFLX) Stock Stays Cheap After Its 58% Three Year Gain
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOVmpXNWh4OWZNOUI5d0lnd1NGYzBBU2tLSFhPeDY3UFpFM1ZXODVVdzNuMy1CM1pMelUxdFZEQ25XVW5NMHlPYnZ1WFZ3RXZXbXB6aDg2eFpWNUF5RC1KWUFJc2dmMHlkbkJQY1k2Z2JLb25RY0J6cURXR2hxV1AzZDZMM0dvWW84WHFIalR2Q05pbDZzMlBpekhKdw?oc=5>

## HEADWINDS

### Netflix stock sinks as Wall Street lowers price targets following Q4 revenue forecast miss
- Summary: Netflix stock sinks as Wall Street lowers price targets following Q4 revenue forecast miss
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7gFBVV95cUxQNEJkYUJaMXNVbEhiRTVINEhQZEptTkdWWFpkQkhDc2hDMkREQVRteGxITEZGVlYwcnZzSUdmd1ltclFkM2hBTnp2OGVWSVJEaWlub29QdHVMVC15eTRISWRPUGZLT3NaS2FiZHhwNGxtOExtUDBQUUpHejhDOFRmQ2pFQXhKRUNuN1JnM3RiR281VjlfT1ZvS1IxX2FWZ0tZQ3VjMTAzRERHQnowczhMNGJRUU1YeUFPdGNxVDNOWFFrZ0FOckdkNDdZNDFwaXhtaF81VXhJSzRLb1hVVW5JVks2Q09vVVViQ3dVN21n?oc=5>

### Netflix Is Now Down 29% This Year: Is NFLX Stock Hopeless or Ready for a Rebound?
- Summary: Netflix Is Now Down 29% This Year: Is NFLX Stock Hopeless or Ready for a Rebound?
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxQLUd5d2xvbWNXbkpvYmY3VmhEYUtsbU83V2VIMnptYW5WbUNMZ1dibkJmZEwxYUg0RXhmOWRQZ0t6aW5RaTNoUkQ4Y3ZEZ3FaU2FGSjl2VC1uQlE3bkNnVUtaNi1DY1RzS05zeE55ZGNuS2UtYmlSbTR2ZDlqRXNvaTF1V3QyalNmNkdYN3JsTU50bDZwNXFvR0FVajlpODFvWlZrSGlpYmhDRTg0a0RkWTRLWXFFdzg1YmxZc3RFSQ?oc=5>

### Netflix has 2 problems behind the stock slide — and they aren't YouTube, co-CEO Ted Sarandos says
- Summary: Netflix has 2 problems behind the stock slide — and they aren't YouTube, co-CEO Ted Sarandos says
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7wFBVV95cUxOSmVJUnB4azRpbkpPRmxaNmVSRjlld0Y3TUpvcEx0Q3kydjNVTE13VEdaTHBCRGhQYWhVa1lTUlhFR3FUX1lJZ05QZUtDaUt2b2h4OTA1bHp2U0ZPQ2VYNHhEU1RqWkF6NUR6Q2FUOGZ2RTdmdE1GYnBBLUxkT0wzaXA5V2tidExCeC1Id1pwTVY2WjBKQUZnYzdUSkw5eDh6d2hkbExyVVEzeklrY3JDZW9vUjE2Uk11Q2JTX1pxTmsyNEtZWGpLVnoyeEc0d193QW53QkQzd0RFckRtWjJQcmhYSFNkeVA5OXdlSFhmMA?oc=5>

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

### Netflix Stock Drops After-Hours As Revenue Growth Slows Further And Q4 Sales Miss Expectations
- Summary: Netflix Stock Drops After-Hours As Revenue Growth Slows Further And Q4 Sales Miss Expectations
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQTl9SOU1QMWZOYk1qN3dScWN6aFhKcU1sWEM0emhlUmwza29LY05TTW5zRjB5NHFDYkxTMmo5VVIyQzBLd1RNOVR0MEhvSm1PU0doaGg4VHRsZF9MUGxkNE55ZXNDUE41aTF1aXVDeXM2OVVyWFgtdmd6M2FSUEN0M3JyLVNHUWlyNVVpRnpwSmNDdkpTbGk0QVh5TllOQ28?oc=5>

### NFLX Stock Heads For 26-Month Low After Needham Downgrade, Wall Street Price Target Cuts — YouTube Threat Grows, Content Problem ‘Seems Clear’
- Summary: NFLX Stock Heads For 26-Month Low After Needham Downgrade, Wall Street Price Target Cuts — YouTube Threat Grows, Content Problem ‘Seems Clear’
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOSTNsWGs5VllLU09RdWlFcGkySkh6UTRaTUVCRFplcm5GamFZQnFhVFhvQnJzU3JMQkRFT3NuVjJCNThrX0s5X0pYeW9TT1p4RWNpUGtja0hNYy1nUXhUZjlCYklKN3RjNzhpS3NtN2F2dVVOY0R2OXhLNXF0UUp2VkNrdVVxMVVQeHR1cFdnOEx5Q2dn?oc=5>

### Netflix posts third-quarter earnings beat, but shares fall on advertising and revenue guidance
- Summary: Netflix posts third-quarter earnings beat, but shares fall on advertising and revenue guidance
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMidEFVX3lxTE4zWGVPQmxpYk9aQUgxT2szTmtmSnpJQlpGcTRWcWpiZGVQQ3JzZnNQNElCNlRiQmxQNjhFN3ljZWVfRVVrUEYzdlp6VUw2bHlQUUJiUlNWcDJEeFUzLVhCcFVVa3BrOTl1aXVVQ05yVlJYSTV60gF6QVVfeXFMTlA0cW56QmhrZk5uWlJ1VWllY3hMMnRUYVc5REx0Wi1ZZXJYeThtWW9jVGJmaGVPNzFlaGVtQVZGeXFWMm93Y0xIVkJTRkZEeVJhMHpLdGE1cXpVWE1YU1JWWWxTRXFZclN5MGJaU2JDNmN2WmlpMzg0eWc?oc=5>

### Netflix Stock Drops Over 6% Following Expected Revenue Numbers
- Summary: Netflix Stock Drops Over 6% Following Expected Revenue Numbers
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxORFVyZ3JGNEJIdWMyYndUX1d5MTZwX1h2VmxmakJ0TEphU0RVLUt3RHJRMlBlQ1QtLU12eFV6eE5GN0JSdWRIWXJVNl9NX0JqVlJBVDZyZEN6akdUb1pReWk4TUpiWmNuakdkVVVmaUVCR0tFc3lfTC1uTmNTYUd5SzBUUVgtcVA4bHZrMkpjY2E3VG4tV3c?oc=5>

## CATALYSTS

### Netflix (NFLX) Stock Fair Value Falls After Cautious Q3 Analyst Revisions
- Summary: Netflix (NFLX) Stock Fair Value Falls After Cautious Q3 Analyst Revisions
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQSE1oLXBDN2dSRUZabVZhbzJvTDZpSVV3NmNVQ2VlYjJJQVVRSTBfQmJHT2FhWGt6LUl4NjFBMElxaVFGajh2eWlIRm1abUp2cFVoekg1VGdZN0pmbGV2ckZjWXB2ZzcwRWV2RkZ6S1pqVTBFNjRuamREVk5RMkoxZUw5ZjZyQXg1SDNHdzRIWDhweXJYTGpacC1R?oc=5>

### NFLX Stock Flat Overnight: Netflix's ‘Largest Content Deal’ With Brazil Media Giant Globo Fails To Sway Retail Ahead Of Earnings
- Summary: NFLX Stock Flat Overnight: Netflix's ‘Largest Content Deal’ With Brazil Media Giant Globo Fails To Sway Retail Ahead Of Earnings
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxNd3JSQU1waGFseE0tTlZyUDd1eWpEbDJCbm9HajJ3bmxxT1poZkNCWlRrc3RmWnlaZDMtR2hwMlNuYzBacWQ2REtQNHc2SHF6d2NmQ21pUzBoVE9DTUhDWEV4dzJlYmRxX0I0NTZucGhhWlQ0U2t1NGZoSGpiVEs1akwzSGhzRHZ0WkMyUGtmMl84ZFlJSDZ0LWQ3UVJOdFM3?oc=5>

### Netflix's Apocalypse Fears Overly Done - Cash Cow With Renewal Prospects (NASDAQ:NFLX)
- Summary: Shares drop amid concerns over renewal prospects, despite cash flow strength.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxQaFJVVVgyWXRXY2dpWlBLUkVzZVN3S3N0Z19xMlRwa2NWMEZ3Q3h2WUR4SnMwRkUybFhxWXczUkxMTUh4SmVpTUY2R1dsalJCMmJGQmhkcXZ6cV9JNGdUblFNeHhHczVHb2VJMHNVa01ENjEwTWw3OXlvenVya3BrLXVqVFFaMWhyNlNXVENYSUZDWVdnT0NVcXhzWm5mRHNrUk9jSEhPRE82ZGVGT2xv?oc=5>

### Why Netflix (NFLX) shares are falling today
- Summary: Stock declines today due to market sentiment and recent performance concerns.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQMi1rUzE5c3J6OEZESUJ3RmhEZkNsYldiRXMxRDRBX1g1eFRLd2pZQ3dHUl9ZZDFlVF9KYlk0OThYS3Q2bG9mVGtYWUIxTUhYdFNRVF83bUtFemNmQ29xSk1vd1ZQUURvbWJVMjEtdnEzUWl1cW0yRmE1LVNWYUZzamNCbEVDamFZeFczblY0ZHdzU0JZLXRBNEM0RjQ?oc=5>

### Why Is Netflix Stock Falling Over 5% Despite Beating Third-Quarter Earnings Estimates?
- Summary: Shares fall despite earnings beat, reflecting broader market worries.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPQ1J0SmtscmZVQV9zTUlRODdtVm96NFF2SnhUbkUtNi1halVJMDc3bkRfc2thX1JyeXkyeDUtOF9jMzhOWmU0UDRTbGZtWWNwbXctbkRGejZjVFEwdEV2THFvQ1FVQm1DOWZYYTFlazJXeWVteV9qNXdBdDk3V2ZxcURiUWtZQ0J1X3RNQ0tRN0JqQ0c5cEZod2RDRQ?oc=5>

### Why Netflix Stock Dropped Today
- Summary: Stock dropped today amid negative market sentiment.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQVW92S2lTTzBKRUp2ejdoX1MzMGVGZTQzTFJ0Qk51WFI2SEVIMEJDQ25SUm8xcTZaZ0ROaml0WVF5RHptLUM2UDI3Wmg0SXowX2Rhazd0X1BUSWUwLXpMemxwc09mTUtMQmFrUWUwQmxkZW5CcmFjYl9DVVJYZEJyRmMxV1htWm5oVEwyVU8tYjNIZXp0VzN0UlZKb0s?oc=5>

### 1 Reason Why Netflix Stock Looks Oversold
- Summary: Stock appears oversold, leading to a decline.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOd1o1cTIzd25kckM1eDdzeTJBRkYycXRlZzBLd19NS1FVTThIME5maVhYamNtcjVrU0pPTWpHVVZBUXRhNzU2a1NnQXpDcnhJQ282aFJiY3hwVzhnOEZOaDdCMDkwUXlKN05IN1JWT284ZExXVGNfZXpQb2VKTTYzSzBvNHFoTEZjRGZBT2hjV3R5ZXlzU1E?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NFLX** | **19.03** | **9.23** | **17.53** | **11.80** | **274,195,415,040.00 USD** | **-40.87** |
| DIS | 23.20 | 1.77 | 11.54 | 6.80 | 194,286,796,800.00 USD | 0.99 |
| WBD | N/A | 2.36 | 13.79 | -11.20 | 77,595,885,568.00 USD | N/A |
| CMCSA | 7.18 | 0.87 | 4.79 | -6.10 | 80,572,334,080.00 USD | -12.95 |

Peers fetched as_of: 2026-10-24; NFLX reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-20
- Next expected earnings: 2027-01-19 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-24

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

- https://news.google.com/rss/articles/CBMixAFBVV95cUxQV2xrakJTS3dXNzdZd3JzWWpodUd4Z1A3SlVoalJkQWMzTUpOYU9yNXBFMm5IN3p3RHdBbk9QZWZxbVUxSnBXRXFzUlk2bFozTUtnVEtpT3RIQUU5c3RqamYzd0ZRcVFvMlZZTjhwT09fM0k2U0gzdmlDWVRuUlBiRm9KY0JLajBfYmVJV2p3R01fQk9aa1FYUVBVNjRBbVpYajVJM3VaX1RDZ040bkZ5b0tLSjhDY2YtV1RtZ3hpWXlwYjJW?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOVmpXNWh4OWZNOUI5d0lnd1NGYzBBU2tLSFhPeDY3UFpFM1ZXODVVdzNuMy1CM1pMelUxdFZEQ25XVW5NMHlPYnZ1WFZ3RXZXbXB6aDg2eFpWNUF5RC1KWUFJc2dmMHlkbkJQY1k2Z2JLb25RY0J6cURXR2hxV1AzZDZMM0dvWW84WHFIalR2Q05pbDZzMlBpekhKdw?oc=5
- https://news.google.com/rss/articles/CBMi7gFBVV95cUxQNEJkYUJaMXNVbEhiRTVINEhQZEptTkdWWFpkQkhDc2hDMkREQVRteGxITEZGVlYwcnZzSUdmd1ltclFkM2hBTnp2OGVWSVJEaWlub29QdHVMVC15eTRISWRPUGZLT3NaS2FiZHhwNGxtOExtUDBQUUpHejhDOFRmQ2pFQXhKRUNuN1JnM3RiR281VjlfT1ZvS1IxX2FWZ0tZQ3VjMTAzRERHQnowczhMNGJRUU1YeUFPdGNxVDNOWFFrZ0FOckdkNDdZNDFwaXhtaF81VXhJSzRLb1hVVW5JVks2Q09vVVViQ3dVN21n?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxQLUd5d2xvbWNXbkpvYmY3VmhEYUtsbU83V2VIMnptYW5WbUNMZ1dibkJmZEwxYUg0RXhmOWRQZ0t6aW5RaTNoUkQ4Y3ZEZ3FaU2FGSjl2VC1uQlE3bkNnVUtaNi1DY1RzS05zeE55ZGNuS2UtYmlSbTR2ZDlqRXNvaTF1V3QyalNmNkdYN3JsTU50bDZwNXFvR0FVajlpODFvWlZrSGlpYmhDRTg0a0RkWTRLWXFFdzg1YmxZc3RFSQ?oc=5
- https://news.google.com/rss/articles/CBMi7wFBVV95cUxOSmVJUnB4azRpbkpPRmxaNmVSRjlld0Y3TUpvcEx0Q3kydjNVTE13VEdaTHBCRGhQYWhVa1lTUlhFR3FUX1lJZ05QZUtDaUt2b2h4OTA1bHp2U0ZPQ2VYNHhEU1RqWkF6NUR6Q2FUOGZ2RTdmdE1GYnBBLUxkT0wzaXA5V2tidExCeC1Id1pwTVY2WjBKQUZnYzdUSkw5eDh6d2hkbExyVVEzeklrY3JDZW9vUjE2Uk11Q2JTX1pxTmsyNEtZWGpLVnoyeEc0d193QW53QkQzd0RFckRtWjJQcmhYSFNkeVA5OXdlSFhmMA?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOVmRBaFZXZGZad2d5SGVQS2J4c2xPOTdpNjNqRmlQWXliMWpIVFdpV2RsSlZ1NHRiUFBtZ0hQbGxDS2U3bjBSNE5pR2hlUFNPY3Y4YVp2LUhsRHlvZ1dhemdCc2twWXJYX2JBZm1ELU5fRGJVWnpFOTlQcU5sOGlGZl9qazJhajZTaFRqWnQ4X3kxVTBqWXFyMDdKRQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNVTBxOTVRYmtvSHVoYlluTGwyQjZNR3ZEeHZ2Nno3SzNmaHFPQ2YxMTU1enN6aExMMW1rRVg2dC1oQ1Z1WjJCcGNHVDhVUUJpWWJEOVFfZnRpUXpKYWVYTmRsclE3ZjJiY2dNZ0NxSGswb25zTy1xSzBHRmNKWjlzOVduNTRKRXRXeEtBS3RCRG81RTg4VXNPMHBKWTg?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNYXVuTzRUeVNQZHhoTUpSZzg5aEE4VnhPYWh5YVQ4UmplQ1B4T1ktSDN5aHpMVFY2cm01QnRGS2FWWWxSMmlOTmYxS2kyaWVCZHdDZ0Q0NC1Bd1JGWG54cVdBdDktWnJKMEJZVldCOGRaUVhCQkdNYjBMTVNxakdjYjRyZFVSRUNrX3BrbERTUXJmdw?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQTl9SOU1QMWZOYk1qN3dScWN6aFhKcU1sWEM0emhlUmwza29LY05TTW5zRjB5NHFDYkxTMmo5VVIyQzBLd1RNOVR0MEhvSm1PU0doaGg4VHRsZF9MUGxkNE55ZXNDUE41aTF1aXVDeXM2OVVyWFgtdmd6M2FSUEN0M3JyLVNHUWlyNVVpRnpwSmNDdkpTbGk0QVh5TllOQ28?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOSTNsWGs5VllLU09RdWlFcGkySkh6UTRaTUVCRFplcm5GamFZQnFhVFhvQnJzU3JMQkRFT3NuVjJCNThrX0s5X0pYeW9TT1p4RWNpUGtja0hNYy1nUXhUZjlCYklKN3RjNzhpS3NtN2F2dVVOY0R2OXhLNXF0UUp2VkNrdVVxMVVQeHR1cFdnOEx5Q2dn?oc=5
- https://news.google.com/rss/articles/CBMidEFVX3lxTE4zWGVPQmxpYk9aQUgxT2szTmtmSnpJQlpGcTRWcWpiZGVQQ3JzZnNQNElCNlRiQmxQNjhFN3ljZWVfRVVrUEYzdlp6VUw2bHlQUUJiUlNWcDJEeFUzLVhCcFVVa3BrOTl1aXVVQ05yVlJYSTV60gF6QVVfeXFMTlA0cW56QmhrZk5uWlJ1VWllY3hMMnRUYVc5REx0Wi1ZZXJYeThtWW9jVGJmaGVPNzFlaGVtQVZGeXFWMm93Y0xIVkJTRkZEeVJhMHpLdGE1cXpVWE1YU1JWWWxTRXFZclN5MGJaU2JDNmN2WmlpMzg0eWc?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxORFVyZ3JGNEJIdWMyYndUX1d5MTZwX1h2VmxmakJ0TEphU0RVLUt3RHJRMlBlQ1QtLU12eFV6eE5GN0JSdWRIWXJVNl9NX0JqVlJBVDZyZEN6akdUb1pReWk4TUpiWmNuakdkVVVmaUVCR0tFc3lfTC1uTmNTYUd5SzBUUVgtcVA4bHZrMkpjY2E3VG4tV3c?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQSE1oLXBDN2dSRUZabVZhbzJvTDZpSVV3NmNVQ2VlYjJJQVVRSTBfQmJHT2FhWGt6LUl4NjFBMElxaVFGajh2eWlIRm1abUp2cFVoekg1VGdZN0pmbGV2ckZjWXB2ZzcwRWV2RkZ6S1pqVTBFNjRuamREVk5RMkoxZUw5ZjZyQXg1SDNHdzRIWDhweXJYTGpacC1R?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxQd3l6VmgwRS1MajB3OEh4cktucTlSczdEd0FOZlhoNE15dEpkOEx4VElhb2lUaFJUX1hTNDBQeXFjMFJkVC1qSFRxWUxkV2dBT003ejlWNFR0QlFXSHU4aVNzemdKSEhtU2dxVUdPZ3k5a2hIblp3anlpVEFDRUpiMTUyUDQ?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxNd3JSQU1waGFseE0tTlZyUDd1eWpEbDJCbm9HajJ3bmxxT1poZkNCWlRrc3RmWnlaZDMtR2hwMlNuYzBacWQ2REtQNHc2SHF6d2NmQ21pUzBoVE9DTUhDWEV4dzJlYmRxX0I0NTZucGhhWlQ0U2t1NGZoSGpiVEs1akwzSGhzRHZ0WkMyUGtmMl84ZFlJSDZ0LWQ3UVJOdFM3?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxQaFJVVVgyWXRXY2dpWlBLUkVzZVN3S3N0Z19xMlRwa2NWMEZ3Q3h2WUR4SnMwRkUybFhxWXczUkxMTUh4SmVpTUY2R1dsalJCMmJGQmhkcXZ6cV9JNGdUblFNeHhHczVHb2VJMHNVa01ENjEwTWw3OXlvenVya3BrLXVqVFFaMWhyNlNXVENYSUZDWVdnT0NVcXhzWm5mRHNrUk9jSEhPRE82ZGVGT2xv?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQMi1rUzE5c3J6OEZESUJ3RmhEZkNsYldiRXMxRDRBX1g1eFRLd2pZQ3dHUl9ZZDFlVF9KYlk0OThYS3Q2bG9mVGtYWUIxTUhYdFNRVF83bUtFemNmQ29xSk1vd1ZQUURvbWJVMjEtdnEzUWl1cW0yRmE1LVNWYUZzamNCbEVDamFZeFczblY0ZHdzU0JZLXRBNEM0RjQ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPQ1J0SmtscmZVQV9zTUlRODdtVm96NFF2SnhUbkUtNi1halVJMDc3bkRfc2thX1JyeXkyeDUtOF9jMzhOWmU0UDRTbGZtWWNwbXctbkRGejZjVFEwdEV2THFvQ1FVQm1DOWZYYTFlazJXeWVteV9qNXdBdDk3V2ZxcURiUWtZQ0J1X3RNQ0tRN0JqQ0c5cEZod2RDRQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQVW92S2lTTzBKRUp2ejdoX1MzMGVGZTQzTFJ0Qk51WFI2SEVIMEJDQ25SUm8xcTZaZ0ROaml0WVF5RHptLUM2UDI3Wmg0SXowX2Rhazd0X1BUSWUwLXpMemxwc09mTUtMQmFrUWUwQmxkZW5CcmFjYl9DVVJYZEJyRmMxV1htWm5oVEwyVU8tYjNIZXp0VzN0UlZKb0s?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOd1o1cTIzd25kckM1eDdzeTJBRkYycXRlZzBLd19NS1FVTThIME5maVhYamNtcjVrU0pPTWpHVVZBUXRhNzU2a1NnQXpDcnhJQ282aFJiY3hwVzhnOEZOaDdCMDkwUXlKN05IN1JWT284ZExXVGNfZXpQb2VKTTYzSzBvNHFoTEZjRGZBT2hjV3R5ZXlzU1E?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
