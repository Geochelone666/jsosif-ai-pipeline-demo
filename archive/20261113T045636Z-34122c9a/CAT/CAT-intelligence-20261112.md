# CAT Intelligence Report

- ticker: **CAT**
- Report as_of: **2026-11-12**
- Market data as_of: **2026-11-12**
- Quant sources: https://finance.yahoo.com/quote/CAT/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CAT/key-statistics/
- AI analysis snapshot as_of: **2026-11-12**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-13T04:56:43.019510+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 2, 'ai': 15, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **13** exact headline/source/date matches; prior report **20261111T043601Z-d14951e6/CAT** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **3**; {'directional_claim_without_event_type': 2, 'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 12 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 20.0%; oldest publication 2026-11-06

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 605.2800 |
| Return 1D (%) | 0.6100 |
| Return 1W (%) | 9.3274 |
| Return 1M (%) | -24.1003 |
| Return YTD (%) | 6.5560 |
| Return 1Y (%) | 6.5281 |
| Annualized volatility (%) | 41.4940 |
| Beta vs SPY | 1.8324 |
| Max drawdown (%) | -47.7898 |
| Sharpe (rf=0) | 0.3600 |
| Downside deviation (rf=0, %) | 29.3250 |
| Sortino (rf=0) | 0.5094 |
| Historical VaR 95% (1D, %) | 4.2437 |
| Historical ES 95% (1D, %) | 5.7878 |
| Correlation vs SPY | 0.6065 |
| Tracking error vs SPY (%) | 34.9149 |
| P/E (trailing) | 23.76 |
| P/B | 12.89 |
| EV/EBITDA | 18.59 |
| Revenue growth (%) | 17.30 |
| Forward P/E (estimate) | 18.77 |
| Gross margin (%) | 29.54 |
| Operating margin (%) | 18.76 |
| Return on equity (%) | 56.14 |
| Free cash flow yield (%) | 1.43 |
| MA50 | 743.4134 |
| Close vs MA50 (%) | -18.5810 |
| MA200 | 804.6726 |
| Close vs MA200 (%) | -24.7793 |
| RSI (14, Wilder) | 36.4280 |
| MACD (12,26) | -49.3473 |
| MACD signal (9) | -48.7079 |
| MACD histogram | -0.6394 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CAT': 281, 'SPY': 281}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 605.2800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.6100 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 9.3274 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -24.1003 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 6.5560 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 6.5281 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 41.4940 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 29.3250 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.5094 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.2437 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.7878 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6065 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 34.9149 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.8324 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -47.7898 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3600 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 18.7701 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 29.5420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 18.7610 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 56.1350 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.4345 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 23.7551 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 36.4280 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.6394 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -18.5810 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -24.7793 -> Clearly below the moving-average trend level.

## TAILWINDS

### Caterpillar stock rallies as Anthropic generator order and record results boost sentiment
- Summary: Caterpillar stock rallies as Anthropic generator order and record results boost sentiment
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNX2JxV0djQ3diY0o5amlwWW5xMVhnTS1MSXhENGQxel9JY00tNThkamk0TUh0bUZMYTdkcm9vNWJJY25kWFRGX1RUV3l1VllzMjc3bVhlMm5hdWJMU1YxTndLQndrSFItQWRxeU05RlN2N0paZDNPVktRTlRUcHdHWktNdmJJdGhhNlFXbFFNYjFnbC02VUxxdEVKOXA?oc=5>

### Caterpillar Stock Jumps 7% on Anthropic's $3.4 Billion Deal, With $628.70 Next
- Summary: Caterpillar Stock Jumps 7% on Anthropic's $3.4 Billion Deal, With $628.70 Next
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi-gFBVV95cUxQZ3N5d2hOR2ZJLTYzX2NKUGYzVnRqZ0c5RWJNMUFobWR1Z2xCdlRiaXNpNjBzZWp3U0tRWmF3aTZSZUZPMmxzSTMzcmk3dTRsVGdudmFpSkhjU3MtVmFVcXNza2N6UmExQzJJRGxnMnNvSWQtdklRYnJLYU9JQXNMTVJ1VmRmY2JKOWZBZ3AtWUxlM1V3akpVUTNOV3JjUGpVTzJVdzV0TnNlUk1MQXFSazhNX3NxV0RHcE9NTnNRN2Vfd28zSXpmNUVuYnpIOHJlaktoLVlDd3dDOGJKR1VGUXhvRkRBdGJUbUd6clJkS0FyOHlLYzUyNU93?oc=5>

### Caterpillar (CAT) Is Amongst The Notable Names Insiders Are Loading Up On After the Recent Crash
- Summary: Insider buying after crash signals potential upside.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNUy1ZR3NCUUJ3bVh4R3lpOFBkVlAxa0hkaE1peWdVUHR6SXFPZVg3bC1hRldCc1ZWS0xrLTdfSkRoaWxUMzEwcldURzlmMDFSTnllakpmYlRyY0t5Mi1xQjllV1JkY2dkbkVJbGtfNUYzZXJNOVVJbHMzSWRGcWxMRWtyd25oUFR3MnN4YXJIZzJPa2o1Mmp4QkxtSGxlS0doRXFlbw?oc=5>

### Caterpillar (CAT) Stock Looks Like A Bargain On Its 222% Run
- Summary: Positive view on CAT stock, suggesting a bargain after a 222% run.
- Date: 2026-11-11 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQZHVXQm5YSjNZLU9OdHJaU3E2blFWOEI2LUM1ajR0eTlOOVNxVlAtcERmRmp1c0hZYXJEZl8zVkhYLUlHV2wxUk5OZmVqN044UmROeklfV1NHRWwwZV81amJCdEZKNDFGcXdyODc0T2thTkR6a0tLSV9faVg3dWpVYlhKSk9CY29OLVZSRWl6RnJhbzFWeHNRZURXeWZYMWtwSmc?oc=5>

## HEADWINDS

### Michael Burry Cashes In On Caterpillar Puts After 4X Gain — Is CAT Stock Still Overvalued?
- Summary: Burry’s puts suggest bearish sentiment.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNWlFPd3JLaXpOZVZXUHJYOF9tOVFIS3lJUFNjSi1maUZnRFNCN3hNWjRpSXI0a0lla05ibDhiYWlDbXRlUnF6WmtHUzhmVFhDUGZ1WWxCeXNvTXE1TGNNTDl5WjdmVFlyb0RGbG1EM3BWeWIxY0gtbnVhTlNTQkZvQVBwOXpTQ3RzQ1BnZUJObWtzejhHVFlDWDY5RXVhMVNZTkt0cQ?oc=5>

### Caterpillar Inc Stock (CAT) Opened Down by 3.21% on Nov 10: What Investors Need To Know
- Summary: Opening decline indicates short‑term downside pressure.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxNQlM1U25JV09KYWxJRkU1cTV4RFFOZmUyS3FHNlhSYmlOSldQM1hxZ0pZZFJfNDlLQzFXbkstaHRuSTBQR3llNEM2WUNfaGV1bmV4TTBmN1JaNVI2elZieHZqZzNXeFBfc2ZwcURndkdRVW52YlRkUlBhdnRHMnA3a0J5MUlZajh0OEE?oc=5>

### Caterpillar stock stalls below resistance as rebound odds stay low: weekly forecast
- Summary: Technical stall below resistance, low rebound odds for CAT.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOOU9QcGNnMmxuTElXU1RkQkpXdjJ4YjB0ZElXUHN1SGlJS3RyaWV0Uy1nNkJHeEFjM1ZhUFkwVjZacUpXaGgtbnFVaUJRZHk2dkpJRWFZOWctNmg4SU93RklrWTdMcXBwel9abElmZXUwTkN5bzQyc3Nkd2VMZDhmcEpIQ0NoaXVwT0JjWS1uNmxmWWd4?oc=5>

## CATALYSTS

### Caterpillar Stocks Jump 6.61% as Anthropic Takes Over $3.4 Billion Generator Order
- Summary: Caterpillar’s stock surged after Anthropic secured a $3.4B generator contract, signaling a significant product win.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPeHNqTHAxVnZNSjZwbkNvYVRQSGpZTjFfUUhyOGRvVmswVl9Fb2NqaWtSQzc4bWFjb25fZzl3VmhyS0lhV2pHdkNYM3JTdHd4RVEyMkdRa0xPOUdBaFFEXzdDWFVnd1ZMSmtmUURSOTkzaEUtYTEtOVNGNGEzR2VfbG12ci1YeWlENXRDcmlialo5UUQwWW9RYg?oc=5>

### Caterpillar Inc Stock (CAT) Moved Up by 6.33% on Nov 9: Facts Behind the Movement
- Summary: CAT shares rose 6.33% on Nov 9, reflecting positive market sentiment and potential underlying catalysts.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxPYWhHMi1yN2MyUnhlZmlPdFdLOTNjeURLWFlFWEc1THo3Y2JRUllZVWNIcG5PbVU2SVVIWXFQb3c5WHJxTnpPT2tmYVNxSzZXb3QyME91X2lmdXVUOHl0eW91UFA5WXBtN0dPSWlIbHVybkU2ZENISENkMTJ4WUJwaGtfMXMwbTVaRmc?oc=5>

### A Look at Caterpillar Inc (CAT) After 7.2% Gain -- GF Value $504
- Summary: CAT experienced a 7.2% gain, boosting its GF value to $504 and indicating strong investor confidence.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxNTnRjQmJITUVpQkcyejM3NEppdUJyRldHaXJfOUZiZEd0RElCXzgyMGRYb0FQUzBnOFRaU0J2NEUwZUFXRW43Nkl0MElPOXBwQVVWN2hMMzg4SDRZaDNwVmxEWllHSDg4VmZmREc4ak9YRS0wQ0k1Z3JkSjlhckEwOG9mZ1ZHT0c3RVpvLUJseHg1em12eFVCRnE3M015UXNIWHIwVXV4WHAxV0l4RnVOVW1R?oc=5>

### Michael Burry just made a big move on Caterpillar stock
- Summary: Burry's significant position change in CAT stock.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxPNjNSWWZwMzh1LUlsNXBWZzNKM3pDWGhHT1RVX0FKSGNHY1dRakNoVmlDUmJvSDFvbjl1aExGYl9CNHBmNlEzSmw3a2xia3FVNHduanYzdDRVczJFUEthMlRQXzNmTDJWVHEyc3pQX2hWQVpwMVg3WEtzWlp2Vk1JOGNyR0M?oc=5>

### Michael Burry trims Caterpillar bearish bet after puts nearly quadruple (CAT:NYSE)
- Summary: Burry reduces bearish bet after large put activity.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxNenhDZnVjT3I5TWg4b2pELVpBZUl0OXRHTTZFdWs0bVotNmRhcnF0QlpUcmJoR0s1U1I3M0JidEtvU0Rqemh6VXBRZ2NsV3lYOFdIMUViMVJkZlUyZ1BZWk5scTNhc090YlVFUjhsY095c3c5Wl9ZbDB3S3dPRW9vS3ZIdzg0SUVCeFhIQ1ByZUpQUmxaY3M5QUprb0w1RDktbTZTTTdHZkpKV09UZUE?oc=5>

### Can Caterpillar Stock Hit $820?
- Summary: Speculation on future price target for CAT shares.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxORWs4Q3hRZGdKWVNuNTRqWUlwNWtTcEllc1ptbW9UcUxtM1N0N2FpRllKSjJ6UTZraFNmcFBldEwxNXNVQlljNDZOY2JaaUdMNmJmTHNCM2F2MTlyWXhaYTlwSnJvWV9RM0Q3b2JlTWJpeUpHT1p0dTEwbDFKbjFVLXkyaE9zM2twQWtoSk5uUGpIdmc?oc=5>

### Caterpillar Inc Stock (CAT) Moved Up by 3.21% on Nov 11: What Investors Need To Know
- Summary: CAT shares rose 3.21% on Nov 11, indicating positive market movement.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxQSHI1YWlVYzNfZlFhcHNOQ1Q4XzBhU1dRbkZfeHVZLUp0aU9uakZQR3FLWkxqMHZsUmVvNkJjQmZITThudHh1SHRucXF2dUlOcWlydHE1OFRHRm5lZjg3UEZLRXhXNUZLWm1JckdabEJHcl96SkhmM2hsdWVCR0pCc0V2VHN5bnBTWWc?oc=5>

### Caterpillar stock support and resistance levels after 5.8% rebound
- Summary: Technical analysis of CAT support/resistance following a 5.8% rebound.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxNZkE4aGxDRDhTaU1ZMUhLdHduaXpUaW5HV1daM2hKTElfN3JDT0RvYU9lNU1iX3dVSGd2SXhNNEJLa1d1by02LUozVlg0YmhDRFpnMG1Lb21Bc3BMNnRYaW1iS0VtbUdYRzVZVlpsNTNteFpBX0hIM1o3SWljcXNUYUVNZkg0MHhtekVPd3hlWVBmbTdTZVN4S0RHUEdoSFE4RUxNNlk3ekJCandNdHM5ZFQ4RW5EenBZcTgwNDdLOF9sLWE3?oc=5>

### Gas Generator Deal Could Be A Game Changer For Caterpillar (CAT)
- Summary: New gas generator deal positions CAT as a potential market leader.
- Date: 2026-11-12 | Impact: high | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxNamRVaFVFZ1E3Y3F6QXhVSndqREttSEFlOFM4NEtfc0Z4SXhUVEc5UzZyNmhWa002cUh2VVhFNzdPbG5FX19UNGFPN0pEWFVIeThoZEhOci1mT1k2MUFQclV4aGdfTFY4QWdJQnRzbGNULWFvenE5Y0dWQW9sVXV0blJxYlh5ZzJXU0VJQzV5MjZYanh3MFExZ1l3VWFpZkFNaHR0VDhsRVJwTVFZeWp3UHN5bW96QW9LVm5mQ1EzUWtqVkdhLXEzSW9NdzPSAdIBQVVfeXFMUGtOWWxDcWMxMnFGWUd1aVVGU0hMTXU0WV92QmJxQnlMcU1CQzJ3RXd3SS1MVm9LYkhDV0J0bGRNeWZ5Q0xPaGRhYmFRcExGdEtkeUFHV3N6MGJUSUdHTjdQeEtucG13cnQwWE1KM1p4SnAwUFNqdkZjTnpFbENYdWluLWtmcURuU2hUUHJXUTJpNk4xZ2g4UTA2bzFHZGRPTktGZVFBT2oxT3ZfbjMxUEJZb0lKSGcwX0I2SHJRUjB2cFFHRXVZTUROSlZZRHd4YTVn?oc=5>

### Terex, Titan International, Caterpillar, AGCO, and AeroVironment shares skyrocket, what you need to know
- Summary: CAT shares surged alongside competitors, indicating a broader market rally.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwJBVV95cUxNakgxTXNwMlRFcVNOWmJTanY0MnBsR05CeWdnMVE0YjR1RWx5aFYyM0YxV1dLU2czNUdqWjg5WFV3NTVaUjl2OXFYeWZXcVMtejVBV3N0UWtjT0YxbjFMMEEyQWFwZzF0SFNfSHZmY2NCMzNBNUJLTmwxeU5VZlVrdGRyeHZ1R1ZKUHN6NjNqTXpncHNGY1pCUHJmWkctM2I1MlJGM05VbVd0eVhPTFI2Umx1TGt1bWgxOXpvS1hYM292ZzllQ1Y1QUZSUDA3SGtZbVlhWEZXQjA3WFNUdTVnSkxOUHR6QTRJOHN6NHQya0tBM1ZoN0IwRnBtWFFwMUw0Z0syLWwtZ1NzaVM0emFoNXdQWQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CAT** | **23.76** | **12.89** | **18.59** | **17.30** | **276,972,601,344.00 USD** | **6.53** |
| DE | 37.73 | 6.54 | 27.99 | 4.90 | 183,019,028,480.00 USD | 42.80 |
| CNH | 57.00 | 1.90 | 18.43 | -1.00 | 19,221,983,232.00 USD | 16.99 |
| CMI | 19.00 | 4.68 | 12.57 | 13.50 | 62,389,800,960.00 USD | -3.64 |

Peers fetched as_of: 2026-11-12; CAT reuses existing data (market data as_of: 2026-11-12); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-29
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-12

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

- https://news.google.com/rss/articles/CBMinAFBVV95cUxNX2JxV0djQ3diY0o5amlwWW5xMVhnTS1MSXhENGQxel9JY00tNThkamk0TUh0bUZMYTdkcm9vNWJJY25kWFRGX1RUV3l1VllzMjc3bVhlMm5hdWJMU1YxTndLQndrSFItQWRxeU05RlN2N0paZDNPVktRTlRUcHdHWktNdmJJdGhhNlFXbFFNYjFnbC02VUxxdEVKOXA?oc=5
- https://news.google.com/rss/articles/CBMi-gFBVV95cUxQZ3N5d2hOR2ZJLTYzX2NKUGYzVnRqZ0c5RWJNMUFobWR1Z2xCdlRiaXNpNjBzZWp3U0tRWmF3aTZSZUZPMmxzSTMzcmk3dTRsVGdudmFpSkhjU3MtVmFVcXNza2N6UmExQzJJRGxnMnNvSWQtdklRYnJLYU9JQXNMTVJ1VmRmY2JKOWZBZ3AtWUxlM1V3akpVUTNOV3JjUGpVTzJVdzV0TnNlUk1MQXFSazhNX3NxV0RHcE9NTnNRN2Vfd28zSXpmNUVuYnpIOHJlaktoLVlDd3dDOGJKR1VGUXhvRkRBdGJUbUd6clJkS0FyOHlLYzUyNU93?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNUy1ZR3NCUUJ3bVh4R3lpOFBkVlAxa0hkaE1peWdVUHR6SXFPZVg3bC1hRldCc1ZWS0xrLTdfSkRoaWxUMzEwcldURzlmMDFSTnllakpmYlRyY0t5Mi1xQjllV1JkY2dkbkVJbGtfNUYzZXJNOVVJbHMzSWRGcWxMRWtyd25oUFR3MnN4YXJIZzJPa2o1Mmp4QkxtSGxlS0doRXFlbw?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQZHVXQm5YSjNZLU9OdHJaU3E2blFWOEI2LUM1ajR0eTlOOVNxVlAtcERmRmp1c0hZYXJEZl8zVkhYLUlHV2wxUk5OZmVqN044UmROeklfV1NHRWwwZV81amJCdEZKNDFGcXdyODc0T2thTkR6a0tLSV9faVg3dWpVYlhKSk9CY29OLVZSRWl6RnJhbzFWeHNRZURXeWZYMWtwSmc?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNWlFPd3JLaXpOZVZXUHJYOF9tOVFIS3lJUFNjSi1maUZnRFNCN3hNWjRpSXI0a0lla05ibDhiYWlDbXRlUnF6WmtHUzhmVFhDUGZ1WWxCeXNvTXE1TGNNTDl5WjdmVFlyb0RGbG1EM3BWeWIxY0gtbnVhTlNTQkZvQVBwOXpTQ3RzQ1BnZUJObWtzejhHVFlDWDY5RXVhMVNZTkt0cQ?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxNQlM1U25JV09KYWxJRkU1cTV4RFFOZmUyS3FHNlhSYmlOSldQM1hxZ0pZZFJfNDlLQzFXbkstaHRuSTBQR3llNEM2WUNfaGV1bmV4TTBmN1JaNVI2elZieHZqZzNXeFBfc2ZwcURndkdRVW52YlRkUlBhdnRHMnA3a0J5MUlZajh0OEE?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOOU9QcGNnMmxuTElXU1RkQkpXdjJ4YjB0ZElXUHN1SGlJS3RyaWV0Uy1nNkJHeEFjM1ZhUFkwVjZacUpXaGgtbnFVaUJRZHk2dkpJRWFZOWctNmg4SU93RklrWTdMcXBwel9abElmZXUwTkN5bzQyc3Nkd2VMZDhmcEpIQ0NoaXVwT0JjWS1uNmxmWWd4?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPeHNqTHAxVnZNSjZwbkNvYVRQSGpZTjFfUUhyOGRvVmswVl9Fb2NqaWtSQzc4bWFjb25fZzl3VmhyS0lhV2pHdkNYM3JTdHd4RVEyMkdRa0xPOUdBaFFEXzdDWFVnd1ZMSmtmUURSOTkzaEUtYTEtOVNGNGEzR2VfbG12ci1YeWlENXRDcmlialo5UUQwWW9RYg?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxPYWhHMi1yN2MyUnhlZmlPdFdLOTNjeURLWFlFWEc1THo3Y2JRUllZVWNIcG5PbVU2SVVIWXFQb3c5WHJxTnpPT2tmYVNxSzZXb3QyME91X2lmdXVUOHl0eW91UFA5WXBtN0dPSWlIbHVybkU2ZENISENkMTJ4WUJwaGtfMXMwbTVaRmc?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxNTnRjQmJITUVpQkcyejM3NEppdUJyRldHaXJfOUZiZEd0RElCXzgyMGRYb0FQUzBnOFRaU0J2NEUwZUFXRW43Nkl0MElPOXBwQVVWN2hMMzg4SDRZaDNwVmxEWllHSDg4VmZmREc4ak9YRS0wQ0k1Z3JkSjlhckEwOG9mZ1ZHT0c3RVpvLUJseHg1em12eFVCRnE3M015UXNIWHIwVXV4WHAxV0l4RnVOVW1R?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxPNjNSWWZwMzh1LUlsNXBWZzNKM3pDWGhHT1RVX0FKSGNHY1dRakNoVmlDUmJvSDFvbjl1aExGYl9CNHBmNlEzSmw3a2xia3FVNHduanYzdDRVczJFUEthMlRQXzNmTDJWVHEyc3pQX2hWQVpwMVg3WEtzWlp2Vk1JOGNyR0M?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxNenhDZnVjT3I5TWg4b2pELVpBZUl0OXRHTTZFdWs0bVotNmRhcnF0QlpUcmJoR0s1U1I3M0JidEtvU0Rqemh6VXBRZ2NsV3lYOFdIMUViMVJkZlUyZ1BZWk5scTNhc090YlVFUjhsY095c3c5Wl9ZbDB3S3dPRW9vS3ZIdzg0SUVCeFhIQ1ByZUpQUmxaY3M5QUprb0w1RDktbTZTTTdHZkpKV09UZUE?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxORWs4Q3hRZGdKWVNuNTRqWUlwNWtTcEllc1ptbW9UcUxtM1N0N2FpRllKSjJ6UTZraFNmcFBldEwxNXNVQlljNDZOY2JaaUdMNmJmTHNCM2F2MTlyWXhaYTlwSnJvWV9RM0Q3b2JlTWJpeUpHT1p0dTEwbDFKbjFVLXkyaE9zM2twQWtoSk5uUGpIdmc?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxQSHI1YWlVYzNfZlFhcHNOQ1Q4XzBhU1dRbkZfeHVZLUp0aU9uakZQR3FLWkxqMHZsUmVvNkJjQmZITThudHh1SHRucXF2dUlOcWlydHE1OFRHRm5lZjg3UEZLRXhXNUZLWm1JckdabEJHcl96SkhmM2hsdWVCR0pCc0V2VHN5bnBTWWc?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxNZkE4aGxDRDhTaU1ZMUhLdHduaXpUaW5HV1daM2hKTElfN3JDT0RvYU9lNU1iX3dVSGd2SXhNNEJLa1d1by02LUozVlg0YmhDRFpnMG1Lb21Bc3BMNnRYaW1iS0VtbUdYRzVZVlpsNTNteFpBX0hIM1o3SWljcXNUYUVNZkg0MHhtekVPd3hlWVBmbTdTZVN4S0RHUEdoSFE4RUxNNlk3ekJCandNdHM5ZFQ4RW5EenBZcTgwNDdLOF9sLWE3?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxNamRVaFVFZ1E3Y3F6QXhVSndqREttSEFlOFM4NEtfc0Z4SXhUVEc5UzZyNmhWa002cUh2VVhFNzdPbG5FX19UNGFPN0pEWFVIeThoZEhOci1mT1k2MUFQclV4aGdfTFY4QWdJQnRzbGNULWFvenE5Y0dWQW9sVXV0blJxYlh5ZzJXU0VJQzV5MjZYanh3MFExZ1l3VWFpZkFNaHR0VDhsRVJwTVFZeWp3UHN5bW96QW9LVm5mQ1EzUWtqVkdhLXEzSW9NdzPSAdIBQVVfeXFMUGtOWWxDcWMxMnFGWUd1aVVGU0hMTXU0WV92QmJxQnlMcU1CQzJ3RXd3SS1MVm9LYkhDV0J0bGRNeWZ5Q0xPaGRhYmFRcExGdEtkeUFHV3N6MGJUSUdHTjdQeEtucG13cnQwWE1KM1p4SnAwUFNqdkZjTnpFbENYdWluLWtmcURuU2hUUHJXUTJpNk4xZ2g4UTA2bzFHZGRPTktGZVFBT2oxT3ZfbjMxUEJZb0lKSGcwX0I2SHJRUjB2cFFHRXVZTUROSlZZRHd4YTVn?oc=5
- https://news.google.com/rss/articles/CBMikwJBVV95cUxNakgxTXNwMlRFcVNOWmJTanY0MnBsR05CeWdnMVE0YjR1RWx5aFYyM0YxV1dLU2czNUdqWjg5WFV3NTVaUjl2OXFYeWZXcVMtejVBV3N0UWtjT0YxbjFMMEEyQWFwZzF0SFNfSHZmY2NCMzNBNUJLTmwxeU5VZlVrdGRyeHZ1R1ZKUHN6NjNqTXpncHNGY1pCUHJmWkctM2I1MlJGM05VbVd0eVhPTFI2Umx1TGt1bWgxOXpvS1hYM292ZzllQ1Y1QUZSUDA3SGtZbVlhWEZXQjA3WFNUdTVnSkxOUHR6QTRJOHN6NHQya0tBM1ZoN0IwRnBtWFFwMUw0Z0syLWwtZ1NzaVM0emFoNXdQWQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
