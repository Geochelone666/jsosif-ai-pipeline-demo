# CAT Intelligence Report

- ticker: **CAT**
- Report as_of: **2026-11-16**
- Market data as_of: **2026-11-16**
- Quant sources: https://finance.yahoo.com/quote/CAT/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CAT/key-statistics/
- AI analysis snapshot as_of: **2026-11-16**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-17T06:53:40.604195+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 3, 'ai': 19, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261116T043911Z-b81cfeb4/CAT** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **7**; {'directional_claim_without_event_type': 3, 'low_uncalibrated_model_confidence': 2, 'short_term_price_move_in_structural_risks': 2}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 15 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 24.0%; oldest publication 2026-11-09

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 570.4900 |
| Return 1D (%) | -4.9500 |
| Return 1W (%) | -4.7405 |
| Return 1M (%) | -21.7463 |
| Return YTD (%) | 0.4314 |
| Return 1Y (%) | 3.8466 |
| Annualized volatility (%) | 41.7443 |
| Beta vs SPY | 1.8518 |
| Max drawdown (%) | -47.7898 |
| Sharpe (rf=0) | 0.3081 |
| Downside deviation (rf=0, %) | 29.6148 |
| Sortino (rf=0) | 0.4343 |
| Historical VaR 95% (1D, %) | 4.3559 |
| Historical ES 95% (1D, %) | 5.8406 |
| Correlation vs SPY | 0.6107 |
| Tracking error vs SPY (%) | 35.0734 |
| P/E (trailing) | 22.39 |
| P/B | 12.15 |
| EV/EBITDA | 17.65 |
| Revenue growth (%) | 17.30 |
| Forward P/E (estimate) | 17.73 |
| Gross margin (%) | 29.54 |
| Operating margin (%) | 18.76 |
| Return on equity (%) | 56.14 |
| Free cash flow yield (%) | 1.52 |
| MA50 | 734.6221 |
| Close vs MA50 (%) | -22.3424 |
| MA200 | 803.9534 |
| Close vs MA200 (%) | -29.0394 |
| RSI (14, Wilder) | 31.4456 |
| MACD (12,26) | -46.9858 |
| MACD signal (9) | -48.0893 |
| MACD histogram | 1.1035 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CAT': 283, 'SPY': 283}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 570.4900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -4.9500 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -4.7405 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -21.7463 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 0.4314 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 3.8466 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 41.7443 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 29.6148 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4343 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.3559 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.8406 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6107 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 35.0734 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.8518 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -47.7898 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3081 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.7295 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 29.5420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 18.7610 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 56.1350 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.5220 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 22.3897 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 31.4456 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.1035 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -22.3424 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -29.0394 -> Clearly below the moving-average trend level.

## TAILWINDS

### Caterpillar (CAT) Stock Looks Like A Bargain On Its 222% Run
- Summary: Positive view on CAT stock, suggesting a bargain after a 222% run.
- Date: 2026-11-11 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQZHVXQm5YSjNZLU9OdHJaU3E2blFWOEI2LUM1ajR0eTlOOVNxVlAtcERmRmp1c0hZYXJEZl8zVkhYLUlHV2wxUk5OZmVqN044UmROeklfV1NHRWwwZV81amJCdEZKNDFGcXdyODc0T2thTkR6a0tLSV9faVg3dWpVYlhKSk9CY29OLVZSRWl6RnJhbzFWeHNRZURXeWZYMWtwSmc?oc=5>

### Why Is Caterpillar (CAT) In Focus After A $3.4 Billion AI Power Order?
- Summary: Caterpillar secured a $3.4 billion AI power order, boosting revenue prospects.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxPd1dlc2g0VjBPM0lPNTVkc0Nsa05jQ1hfd0ZiQklZVXBURW9hczBiaHFGSkF5M2NuWDBRa3podnlnbHgwby0xRDNsUDJFLTMwcjBwdzlPeFRYY1VnZHJSQkxXYlBQNk85MGF5SUtvaG42TnFSQVBVbVdKMjNJNmNrX1hGbkNHQXRseldEZllaWVVFY1Z0aDF0QklZVzRtMngyNDg0bW1tZFVDcC1WSzY4aWJiUVNaU0lkZmNsYmQzMDZoUlllYW44N2dEa9IB0AFBVV95cUxPX3NlWS1va3VicDZxUnNCWUhxRENldXhydUl5SXhzdjN0VHdRVFl4NkZqS21STWsyeEtxZ1J0REkyMXJUV29WNTNBN2l6M195dDE1WFYwd3ByUFd6eVowclRFdjdKMFZlWVo2VFBOWDJRNUUtYzJlYzVjM1NTOUhKTUNLeEJHQzFTTDQzZy1LQnBhMGl0MXdlaDlXLW5PbkpIMjlLUVZYUUlpeE1ZMHhYTEFBMGswUHBhWGhpMjhrYXdIRi1OSEtTc3A4Q082aElr?oc=5>

### Caterpillar Stocks Jump 6.61% as Anthropic Takes Over $3.4 Billion Generator Order
- Summary: Caterpillar shares rise after securing a $3.4B generator contract with Anthropic, boosting revenue prospects.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPeHNqTHAxVnZNSjZwbkNvYVRQSGpZTjFfUUhyOGRvVmswVl9Fb2NqaWtSQzc4bWFjb25fZzl3VmhyS0lhV2pHdkNYM3JTdHd4RVEyMkdRa0xPOUdBaFFEXzdDWFVnd1ZMSmtmUURSOTkzaEUtYTEtOVNGNGEzR2VfbG12ci1YeWlENXRDcmlialo5UUQwWW9RYg?oc=5>

### Caterpillar Stock Offers a Backdoor Route to a Potential AI Recovery
- Summary: Speculation that Caterpillar could benefit from AI trends, suggesting future upside.
- Date: 2026-11-16 | Impact: medium | Horizon: medium | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxQbndQdmY0Rld2RzhjdFZEM3dac3l0NHN4OXlWTlRxRzZsT3hZM0VWb2JNMWFpRVk3MmtBS2pMdnZXM1hfS2NSYUw5YjVOcUY1TEV6NTVGVVZJYTN5ZVQxaGdxX0pkRlRrd1A0MWp2cGF0Qi1DaDFSMXhtWE5rNGFJbHlRb05kSFpLUDFWYVdQWHhEV3JYcDVfcHhzR3BBX0IyV2ZwZmFCYUFuR1lNdk9Tbnh3?oc=5>

### Kevin Simpson Is Buying More Caterpillar as an AI Trade That Isn’t Just AI
- Summary: Investor buying more Caterpillar shares.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNZ01vSll2ay1obGVvUFhneVdTbDJUY1hWeFFuSU5xY0hIZFhtVXJvdnU1SGdpVlk4ZHYzSlpfSjV1Vkw3b2lwQUk2VkVxYThkX2Z3WjZMLTlQSW1uU19SN2VqODUxQ2s1d1RVS1k1anpTMXYzaU5JLUl1c2VkOXZMSHR4SUZndmdrYjB4SFZvOEpnbU9nVElBRV9IRXMtbXRjd0sxTw?oc=5>

### Michael Burry trims Caterpillar bearish bet after puts nearly quadruple (CAT:NYSE)
- Summary: Investor reducing bearish position in Caterpillar.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxNenhDZnVjT3I5TWg4b2pELVpBZUl0OXRHTTZFdWs0bVotNmRhcnF0QlpUcmJoR0s1U1I3M0JidEtvU0Rqemh6VXBRZ2NsV3lYOFdIMUViMVJkZlUyZ1BZWk5scTNhc090YlVFUjhsY095c3c5Wl9ZbDB3S3dPRW9vS3ZIdzg0SUVCeFhIQ1ByZUpQUmxaY3M5QUprb0w1RDktbTZTTTdHZkpKV09UZUE?oc=5>

## HEADWINDS

### Caterpillar shares technical analysis: Downward price move highlights seller pressure
- Summary: Caterpillar shares technical analysis: Downward price move highlights seller pressure
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQYTlzS0NlZFhxYVZEamdlU3B3ME5zRm53ZEpSaV9vNEdJVlZBNFJJLVFFNFFGdTlmTmRtQzI4MFpBbU9xVE1hakpHQjU2MjgwLVFxTHloX2hEQUd3S3ZJTU5sVkw2RUhSOGJWa0NLMDhwT082OWRxb3Jpb01qNVotbHRpWURtR0tubEF6NnN5bE9uWFlPY2c?oc=5>

### Caterpillar Shares Slide 10% in Worst Week Since 2025 as Burry Exits Bearish Bet
- Summary: Caterpillar Shares Slide 10% in Worst Week Since 2025 as Burry Exits Bearish Bet
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMidkFVX3lxTFB6U3BIcEFrVmhLS3gxajV6U2VjM1cwVW83a0c2SXVvNVotaURhSjRkeUs5eFltWGpKZksxeUQxN2k0N1VfOFMxc3NyNTNSUC12MWZfZFNJS1l5dUU2Sm5Cc1pHWkVBVG5seW4xTWpqU09sNkZSaHc?oc=5>

### Michael Burry Cashes In On Caterpillar Puts After 4X Gain — Is CAT Stock Still Overvalued?
- Summary: Burry’s puts suggest bearish sentiment.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNWlFPd3JLaXpOZVZXUHJYOF9tOVFIS3lJUFNjSi1maUZnRFNCN3hNWjRpSXI0a0lla05ibDhiYWlDbXRlUnF6WmtHUzhmVFhDUGZ1WWxCeXNvTXE1TGNNTDl5WjdmVFlyb0RGbG1EM3BWeWIxY0gtbnVhTlNTQkZvQVBwOXpTQ3RzQ1BnZUJObWtzejhHVFlDWDY5RXVhMVNZTkt0cQ?oc=5>

### Caterpillar stock stalls below resistance as rebound odds stay low: weekly forecast
- Summary: Technical stall below resistance, low rebound odds for CAT.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOOU9QcGNnMmxuTElXU1RkQkpXdjJ4YjB0ZElXUHN1SGlJS3RyaWV0Uy1nNkJHeEFjM1ZhUFkwVjZacUpXaGgtbnFVaUJRZHk2dkpJRWFZOWctNmg4SU93RklrWTdMcXBwel9abElmZXUwTkN5bzQyc3Nkd2VMZDhmcEpIQ0NoaXVwT0JjWS1uNmxmWWd4?oc=5>

### Michael Burry Cashed In Caterpillar Puts After a Nearly 4x Gain Even as CAT Stock Fell 10% in Its Worst Week in 18 Months. Is Caterpillar Still Overvalued, or Did Burry Just Lock In the Easy Money?
- Summary: Burry’s exit signals potential overvaluation concerns, adding downside pressure.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi1wJBVV95cUxQRzlMOWd6Y3BEaDZVeDkyWG9Jd2xuMlltLVFyRnJ1cVhsR2RDcjdSZ0FtRXNnZDloOEF3TlUyTWZpQVk0Q2xaXzBBUEhHN2l1VmVEZk1Ob0FPOE11MFMwc0E0LXpuR3VLYzY2dVBpcDhnRW1iMHlLUkJ2elQxQkc1YmNQTlgtMVJ0RTZnTWZGUkIxd0x2LXhfbklHVnJEZm1taE9vVlJ3SEk4Q3lPRGlZYlRiTzI4bm5KNUxoQ3NGQ0tubmRsRUE4RjF4UGNUQzQ2bk5IdU1qTTZRY1B5UkN3X21qT2k5OHJhc0pyUU1ndUsyXzlOTDJ5QVhpWDRUVWdQZVFLRlBja2lCelV6Tl85aVlPajROUFAtSWpfM1l6N09ncVVIcnhKX1dZMF9oZFh0MDZIQXN0T3VlelNCUmV4ODcyTHdzZUM4el9hdjg4X3JodExGVVdn?oc=5>

### What Has Changed In Caterpillar’s Story?
- Summary: General inquiry into changes within Caterpillar.
- Date: 2026-11-16 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPOTh3QWM3QXRrNERSNmV3bG9oWnM2eGxCSHBDbXpPNWctTUw1bms3RjhVNlZhNGZTaEdQdk9hYmFtV3ZtT0Npb2lJbEZwSXhWN1U3OV9Pand0Z3k2aEpiWUFnSHhNcjNSM2dvQVFObTFkSHhXQTc5ZGhSZ2l0bzNUemxCRFA4c0lyeW95b1UxZlZNZlByX3JYcnc3U1JoWG8?oc=5>

## CATALYSTS

### Caterpillar (CAT) Stock Fair Value Falls As Analysts Cut Targets And Lift Rates
- Summary: Caterpillar (CAT) Stock Fair Value Falls As Analysts Cut Targets And Lift Rates
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxNTFZpMTVKelRubDFSaEtOVUthOG5RcDc3a3FjZFg5U1FoeGRNMTAza1J5aThiazUtaV9jcXMwU2FXMnRYQkNMNGd0MjBkWjhlcGFtUUNlNGFZQ08zS2dVdzRtWk1McVJqdDFuQi0zZnd0aTh6aDdwdVVjc2JYQ0JwSVRsNUktWWhQ?oc=5>

### Can Caterpillar Stock Hit $820?
- Summary: Speculation on future price target for CAT shares.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxORWs4Q3hRZGdKWVNuNTRqWUlwNWtTcEllc1ptbW9UcUxtM1N0N2FpRllKSjJ6UTZraFNmcFBldEwxNXNVQlljNDZOY2JaaUdMNmJmTHNCM2F2MTlyWXhaYTlwSnJvWV9RM0Q3b2JlTWJpeUpHT1p0dTEwbDFKbjFVLXkyaE9zM2twQWtoSk5uUGpIdmc?oc=5>

### Caterpillar Inc Stock (CAT) Moved Up by 3.21% on Nov 11: What Investors Need To Know
- Summary: CAT shares rose 3.21% on Nov 11, indicating positive market movement.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxQSHI1YWlVYzNfZlFhcHNOQ1Q4XzBhU1dRbkZfeHVZLUp0aU9uakZQR3FLWkxqMHZsUmVvNkJjQmZITThudHh1SHRucXF2dUlOcWlydHE1OFRHRm5lZjg3UEZLRXhXNUZLWm1JckdabEJHcl96SkhmM2hsdWVCR0pCc0V2VHN5bnBTWWc?oc=5>

### Caterpillar's 34% Slump Over 6 Months: Wall Street Desk Says It Sets Up 90% Gains Within a Year
- Summary: Despite a 34% decline, analysts forecast a 90% rebound, indicating a potential upside catalyst.
- Date: 2026-11-16 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxPU1VwX0s1M0w0NFViODIwbDMzeWZURWJOdThhNjdKMWJiYUJQQzJES2ZmWW56VFE0a19YTl9LU25lR3daOUNyeHRRZzVCYk5ZM3dTTzFCanVCY3RQTmg1M0U5UmVScmgzcWE4NWNubkRqSnZsRUhyTlJMT2tyT21aV0c1UjdYV1hSNmNNS2F5b3JVTkhaaGtfb19VOVBSS2RKeHJvSFBQN0VYN3ZNSkgxYjJBNnBVQktXX0xNOEcxVVN6WnhWMUlCem5kc0xrRjV4?oc=5>

### Caterpillar’s 34% Slump Over 6 Months: Wall Street Desk Says It Sets Up 90% Gains Within a Year
- Summary: Duplicate of previous forecast, reinforcing potential upside.
- Date: 2026-11-16 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOR3RwVnFOZ0M3eWlCbjUybklZQ3BqRDBxVmY0ZE5lb1RKYWY5dW40M0UtV0lMNkM3c1V6VkI3VXhMU1U0TXFRTzZMdWdjek95ZFlGRG1TNVotVDlZRjE5MGV6aVRfQWNrQXFRTHE4T3VUMlRvTi1WQTRQSmRYNDV4V2toRUhzakYxVVJBNFF5QjlGVEtqWDlZ?oc=5>

### Is Trending Stock Caterpillar Inc. (CAT) a Buy Now?
- Summary: Analyst question about whether to buy Caterpillar stock.
- Date: 2026-11-16 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxOVDF5OFhjanZXNEFXN1ViWTNMMElYc2JOUmx2WkxXSnlNRzhlRVhTeHp2TE1xVUxFOFA3YjZPOHdGWnVlVy1GYjdpdThaYUIxbXRtd1M4V0ZvOFVnd0d1bGNlU19kcnlXNUJxdFRadGJxakRTdHR1ZVF2eXBGYlc1dy1ZX1pNZU9xWUtN?oc=5>

### Caterpillar Makes Advanced Safety Technologies Standard on Construction Equipment
- Summary: Caterpillar standardizes advanced safety tech across its construction equipment lineup, enhancing safety and efficiency.
- Date: 2026-11-16 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxNWVFoNXBMWU1WYk9NU1pTSTJKeXFMY2IyZ3RLSVF3eEJQNEdvcFZqNFp0ZDdGZWp4V1ZaVnJ0UjlPSk1oekJXY1Bad0k4dkhXU0xmV2lSTEFFNUFlVzlxMHZmUjJEMTJ5YnBCZWFDdFZBdjZJRGFQb2loZlA4RHhzMUpiZG8wT0ZULXBCcHVWMm5hUDJINGdURm5kWkh2ZDZ1RWZJWHBNcG5RcTlfMnZNcmtR?oc=5>

### Michael Burry just made a big move on Caterpillar stock
- Summary: Investor Michael Burry has taken a significant position in Caterpillar shares.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxPNjNSWWZwMzh1LUlsNXBWZzNKM3pDWGhHT1RVX0FKSGNHY1dRakNoVmlDUmJvSDFvbjl1aExGYl9CNHBmNlEzSmw3a2xia3FVNHduanYzdDRVczJFUEthMlRQXzNmTDJWVHEyc3pQX2hWQVpwMVg3WEtzWlp2Vk1JOGNyR0M?oc=5>

## RISKS

### Caterpillar Inc Stock (CAT) Moved Down by 3.37% on Nov 16: Facts Behind the Movement
- Summary: Stock price decline on Nov 16.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxQamsyUm54NFFaQ2o5NjRxNkhCeHY5NWtkOVpVUjlTMlV6YmdISjJ0OTJ6ajFTNE1mVWczOXFMNjhNMnVCekdueDktY1RveGdpdnNEbTYwUXgxRS13dFNvRElUdExqeUhmekRFQnlUM1d5NHk4RFNFQkVtWUdiREdJa3EyREFMc3ZkNEE?oc=5>

### Caterpillar Slides as AI-Linked Industrial Trade Remains Under Pressure
- Summary: Caterpillar shares fell amid pressure on AI-linked industrial trade, impacting investor sentiment.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxQVXJCOEhNZ2xRLXZ2bE83c0NkWmVDdUp3Z0gwbjRreEQ3Y0NWdm96U3NvZ1FrLUduaDhjZWw4bDNHWXlIZ2UxcGxUQmR0YU5jaE9GcFhvQ0JQZlN4QmFybHNQdVZrWFlDNDVmVU1RUlc1dk8yRk5jakZuNjljMkppdUx6Wl9YUG8yX1RnelVGWlFkMzVoYnIwa1NjTlJ2RHdqdDFpdGs0Yw?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CAT** | **22.39** | **12.15** | **17.65** | **17.30** | **261,052,891,136.00 USD** | **3.85** |
| DE | 36.35 | 6.30 | 27.21 | 4.90 | 176,332,324,864.00 USD | 38.89 |
| CNH | 54.57 | 1.82 | 35.49 | -1.00 | 18,403,000,320.00 USD | 15.13 |
| CMI | 18.05 | 4.45 | 11.99 | 13.50 | 59,282,640,896.00 USD | -5.09 |

Peers fetched as_of: 2026-11-16; CAT reuses existing data (market data as_of: 2026-11-16); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-29
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-16

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 20,682,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 1,141,000,000.00 USD; period 2011-07-01/2011-09-30; fiscal year/reporting period 2011/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/18230/000001823026000057/cat-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiogFBVV95cUxQZHVXQm5YSjNZLU9OdHJaU3E2blFWOEI2LUM1ajR0eTlOOVNxVlAtcERmRmp1c0hZYXJEZl8zVkhYLUlHV2wxUk5OZmVqN044UmROeklfV1NHRWwwZV81amJCdEZKNDFGcXdyODc0T2thTkR6a0tLSV9faVg3dWpVYlhKSk9CY29OLVZSRWl6RnJhbzFWeHNRZURXeWZYMWtwSmc?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxPd1dlc2g0VjBPM0lPNTVkc0Nsa05jQ1hfd0ZiQklZVXBURW9hczBiaHFGSkF5M2NuWDBRa3podnlnbHgwby0xRDNsUDJFLTMwcjBwdzlPeFRYY1VnZHJSQkxXYlBQNk85MGF5SUtvaG42TnFSQVBVbVdKMjNJNmNrX1hGbkNHQXRseldEZllaWVVFY1Z0aDF0QklZVzRtMngyNDg0bW1tZFVDcC1WSzY4aWJiUVNaU0lkZmNsYmQzMDZoUlllYW44N2dEa9IB0AFBVV95cUxPX3NlWS1va3VicDZxUnNCWUhxRENldXhydUl5SXhzdjN0VHdRVFl4NkZqS21STWsyeEtxZ1J0REkyMXJUV29WNTNBN2l6M195dDE1WFYwd3ByUFd6eVowclRFdjdKMFZlWVo2VFBOWDJRNUUtYzJlYzVjM1NTOUhKTUNLeEJHQzFTTDQzZy1LQnBhMGl0MXdlaDlXLW5PbkpIMjlLUVZYUUlpeE1ZMHhYTEFBMGswUHBhWGhpMjhrYXdIRi1OSEtTc3A4Q082aElr?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPeHNqTHAxVnZNSjZwbkNvYVRQSGpZTjFfUUhyOGRvVmswVl9Fb2NqaWtSQzc4bWFjb25fZzl3VmhyS0lhV2pHdkNYM3JTdHd4RVEyMkdRa0xPOUdBaFFEXzdDWFVnd1ZMSmtmUURSOTkzaEUtYTEtOVNGNGEzR2VfbG12ci1YeWlENXRDcmlialo5UUQwWW9RYg?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxQbndQdmY0Rld2RzhjdFZEM3dac3l0NHN4OXlWTlRxRzZsT3hZM0VWb2JNMWFpRVk3MmtBS2pMdnZXM1hfS2NSYUw5YjVOcUY1TEV6NTVGVVZJYTN5ZVQxaGdxX0pkRlRrd1A0MWp2cGF0Qi1DaDFSMXhtWE5rNGFJbHlRb05kSFpLUDFWYVdQWHhEV3JYcDVfcHhzR3BBX0IyV2ZwZmFCYUFuR1lNdk9Tbnh3?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNZ01vSll2ay1obGVvUFhneVdTbDJUY1hWeFFuSU5xY0hIZFhtVXJvdnU1SGdpVlk4ZHYzSlpfSjV1Vkw3b2lwQUk2VkVxYThkX2Z3WjZMLTlQSW1uU19SN2VqODUxQ2s1d1RVS1k1anpTMXYzaU5JLUl1c2VkOXZMSHR4SUZndmdrYjB4SFZvOEpnbU9nVElBRV9IRXMtbXRjd0sxTw?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxNenhDZnVjT3I5TWg4b2pELVpBZUl0OXRHTTZFdWs0bVotNmRhcnF0QlpUcmJoR0s1U1I3M0JidEtvU0Rqemh6VXBRZ2NsV3lYOFdIMUViMVJkZlUyZ1BZWk5scTNhc090YlVFUjhsY095c3c5Wl9ZbDB3S3dPRW9vS3ZIdzg0SUVCeFhIQ1ByZUpQUmxaY3M5QUprb0w1RDktbTZTTTdHZkpKV09UZUE?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQYTlzS0NlZFhxYVZEamdlU3B3ME5zRm53ZEpSaV9vNEdJVlZBNFJJLVFFNFFGdTlmTmRtQzI4MFpBbU9xVE1hakpHQjU2MjgwLVFxTHloX2hEQUd3S3ZJTU5sVkw2RUhSOGJWa0NLMDhwT082OWRxb3Jpb01qNVotbHRpWURtR0tubEF6NnN5bE9uWFlPY2c?oc=5
- https://news.google.com/rss/articles/CBMidkFVX3lxTFB6U3BIcEFrVmhLS3gxajV6U2VjM1cwVW83a0c2SXVvNVotaURhSjRkeUs5eFltWGpKZksxeUQxN2k0N1VfOFMxc3NyNTNSUC12MWZfZFNJS1l5dUU2Sm5Cc1pHWkVBVG5seW4xTWpqU09sNkZSaHc?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNWlFPd3JLaXpOZVZXUHJYOF9tOVFIS3lJUFNjSi1maUZnRFNCN3hNWjRpSXI0a0lla05ibDhiYWlDbXRlUnF6WmtHUzhmVFhDUGZ1WWxCeXNvTXE1TGNNTDl5WjdmVFlyb0RGbG1EM3BWeWIxY0gtbnVhTlNTQkZvQVBwOXpTQ3RzQ1BnZUJObWtzejhHVFlDWDY5RXVhMVNZTkt0cQ?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOOU9QcGNnMmxuTElXU1RkQkpXdjJ4YjB0ZElXUHN1SGlJS3RyaWV0Uy1nNkJHeEFjM1ZhUFkwVjZacUpXaGgtbnFVaUJRZHk2dkpJRWFZOWctNmg4SU93RklrWTdMcXBwel9abElmZXUwTkN5bzQyc3Nkd2VMZDhmcEpIQ0NoaXVwT0JjWS1uNmxmWWd4?oc=5
- https://news.google.com/rss/articles/CBMi1wJBVV95cUxQRzlMOWd6Y3BEaDZVeDkyWG9Jd2xuMlltLVFyRnJ1cVhsR2RDcjdSZ0FtRXNnZDloOEF3TlUyTWZpQVk0Q2xaXzBBUEhHN2l1VmVEZk1Ob0FPOE11MFMwc0E0LXpuR3VLYzY2dVBpcDhnRW1iMHlLUkJ2elQxQkc1YmNQTlgtMVJ0RTZnTWZGUkIxd0x2LXhfbklHVnJEZm1taE9vVlJ3SEk4Q3lPRGlZYlRiTzI4bm5KNUxoQ3NGQ0tubmRsRUE4RjF4UGNUQzQ2bk5IdU1qTTZRY1B5UkN3X21qT2k5OHJhc0pyUU1ndUsyXzlOTDJ5QVhpWDRUVWdQZVFLRlBja2lCelV6Tl85aVlPajROUFAtSWpfM1l6N09ncVVIcnhKX1dZMF9oZFh0MDZIQXN0T3VlelNCUmV4ODcyTHdzZUM4el9hdjg4X3JodExGVVdn?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPOTh3QWM3QXRrNERSNmV3bG9oWnM2eGxCSHBDbXpPNWctTUw1bms3RjhVNlZhNGZTaEdQdk9hYmFtV3ZtT0Npb2lJbEZwSXhWN1U3OV9Pand0Z3k2aEpiWUFnSHhNcjNSM2dvQVFObTFkSHhXQTc5ZGhSZ2l0bzNUemxCRFA4c0lyeW95b1UxZlZNZlByX3JYcnc3U1JoWG8?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxNTFZpMTVKelRubDFSaEtOVUthOG5RcDc3a3FjZFg5U1FoeGRNMTAza1J5aThiazUtaV9jcXMwU2FXMnRYQkNMNGd0MjBkWjhlcGFtUUNlNGFZQ08zS2dVdzRtWk1McVJqdDFuQi0zZnd0aTh6aDdwdVVjc2JYQ0JwSVRsNUktWWhQ?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxORWs4Q3hRZGdKWVNuNTRqWUlwNWtTcEllc1ptbW9UcUxtM1N0N2FpRllKSjJ6UTZraFNmcFBldEwxNXNVQlljNDZOY2JaaUdMNmJmTHNCM2F2MTlyWXhaYTlwSnJvWV9RM0Q3b2JlTWJpeUpHT1p0dTEwbDFKbjFVLXkyaE9zM2twQWtoSk5uUGpIdmc?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxQSHI1YWlVYzNfZlFhcHNOQ1Q4XzBhU1dRbkZfeHVZLUp0aU9uakZQR3FLWkxqMHZsUmVvNkJjQmZITThudHh1SHRucXF2dUlOcWlydHE1OFRHRm5lZjg3UEZLRXhXNUZLWm1JckdabEJHcl96SkhmM2hsdWVCR0pCc0V2VHN5bnBTWWc?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxPU1VwX0s1M0w0NFViODIwbDMzeWZURWJOdThhNjdKMWJiYUJQQzJES2ZmWW56VFE0a19YTl9LU25lR3daOUNyeHRRZzVCYk5ZM3dTTzFCanVCY3RQTmg1M0U5UmVScmgzcWE4NWNubkRqSnZsRUhyTlJMT2tyT21aV0c1UjdYV1hSNmNNS2F5b3JVTkhaaGtfb19VOVBSS2RKeHJvSFBQN0VYN3ZNSkgxYjJBNnBVQktXX0xNOEcxVVN6WnhWMUlCem5kc0xrRjV4?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOR3RwVnFOZ0M3eWlCbjUybklZQ3BqRDBxVmY0ZE5lb1RKYWY5dW40M0UtV0lMNkM3c1V6VkI3VXhMU1U0TXFRTzZMdWdjek95ZFlGRG1TNVotVDlZRjE5MGV6aVRfQWNrQXFRTHE4T3VUMlRvTi1WQTRQSmRYNDV4V2toRUhzakYxVVJBNFF5QjlGVEtqWDlZ?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxOVDF5OFhjanZXNEFXN1ViWTNMMElYc2JOUmx2WkxXSnlNRzhlRVhTeHp2TE1xVUxFOFA3YjZPOHdGWnVlVy1GYjdpdThaYUIxbXRtd1M4V0ZvOFVnd0d1bGNlU19kcnlXNUJxdFRadGJxakRTdHR1ZVF2eXBGYlc1dy1ZX1pNZU9xWUtN?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxNWVFoNXBMWU1WYk9NU1pTSTJKeXFMY2IyZ3RLSVF3eEJQNEdvcFZqNFp0ZDdGZWp4V1ZaVnJ0UjlPSk1oekJXY1Bad0k4dkhXU0xmV2lSTEFFNUFlVzlxMHZmUjJEMTJ5YnBCZWFDdFZBdjZJRGFQb2loZlA4RHhzMUpiZG8wT0ZULXBCcHVWMm5hUDJINGdURm5kWkh2ZDZ1RWZJWHBNcG5RcTlfMnZNcmtR?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxPNjNSWWZwMzh1LUlsNXBWZzNKM3pDWGhHT1RVX0FKSGNHY1dRakNoVmlDUmJvSDFvbjl1aExGYl9CNHBmNlEzSmw3a2xia3FVNHduanYzdDRVczJFUEthMlRQXzNmTDJWVHEyc3pQX2hWQVpwMVg3WEtzWlp2Vk1JOGNyR0M?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxQamsyUm54NFFaQ2o5NjRxNkhCeHY5NWtkOVpVUjlTMlV6YmdISjJ0OTJ6ajFTNE1mVWczOXFMNjhNMnVCekdueDktY1RveGdpdnNEbTYwUXgxRS13dFNvRElUdExqeUhmekRFQnlUM1d5NHk4RFNFQkVtWUdiREdJa3EyREFMc3ZkNEE?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxQVXJCOEhNZ2xRLXZ2bE83c0NkWmVDdUp3Z0gwbjRreEQ3Y0NWdm96U3NvZ1FrLUduaDhjZWw4bDNHWXlIZ2UxcGxUQmR0YU5jaE9GcFhvQ0JQZlN4QmFybHNQdVZrWFlDNDVmVU1RUlc1dk8yRk5jakZuNjljMkppdUx6Wl9YUG8yX1RnelVGWlFkMzVoYnIwa1NjTlJ2RHdqdDFpdGs0Yw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
