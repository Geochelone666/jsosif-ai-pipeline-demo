# BRK-B Intelligence Report

- ticker: **BRK-B**
- Report as_of: **2026-11-20**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/BRK-B/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/BRK-B/key-statistics/
- AI analysis snapshot as_of: **2026-11-20**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-21T05:44:20.170559+00:00**
- AI status: **Partial: 2 headlines remain unclassified and excluded from research conclusions**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 2, 'ai': 14, 'unknown': 2, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261120T053808Z-e360129e/BRK-B** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 1, 'positive_sentiment_in_headwinds': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 11 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 40.0%; oldest publication 2026-11-16

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 570.0000 |
| Return 1D (%) | -0.3566 |
| Return 1W (%) | -3.8689 |
| Return 1M (%) | 5.5908 |
| Return YTD (%) | 13.3990 |
| Return 1Y (%) | 13.7452 |
| Annualized volatility (%) | 15.1459 |
| Beta vs SPY | 0.0876 |
| Max drawdown (%) | -9.4218 |
| Sharpe (rf=0) | 0.9294 |
| Downside deviation (rf=0, %) | 10.2423 |
| Sortino (rf=0) | 1.3744 |
| Historical VaR 95% (1D, %) | 1.4206 |
| Historical ES 95% (1D, %) | 2.0519 |
| Correlation vs SPY | 0.0827 |
| Tracking error vs SPY (%) | 19.9489 |
| P/E (trailing) | 16.01 |
| P/B | 0.00 |
| EV/EBITDA | -2.04 |
| Revenue growth (%) | 11.20 |
| Forward P/E (estimate) | 24.98 |
| Gross margin (%) | 26.60 |
| Operating margin (%) | 26.60 |
| Return on equity (%) | 10.57 |
| Free cash flow yield (%) | 4.33 |
| MA50 | 536.8642 |
| Close vs MA50 (%) | 6.1721 |
| MA200 | 502.5689 |
| Close vs MA200 (%) | 13.4173 |
| RSI (14, Wilder) | 56.6048 |
| MACD (12,26) | 12.7999 |
| MACD signal (9) | 15.1127 |
| MACD histogram | -2.3128 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'BRK-B': 287, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 570.0000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.3566 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -3.8689 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 5.5908 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 13.3990 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 13.7452 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 15.1459 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 10.2423 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.3744 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.4206 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.0519 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0827 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 19.9489 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.0876 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -9.4218 -> Shallow peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9294 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 24.9818 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 26.6020 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 26.6020 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 10.5740 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.3332 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 16.0067 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 56.6048 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -2.3128 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 6.1721 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 13.4173 -> Clearly above the moving-average trend level.

## TAILWINDS

### Berkshire Hathaway Is Up 18% in Its First Year Without Buffett as CEO. Can BRK.B Stock Hit $700 by 2027?
- Summary: Berkshire’s stock rose 18% in its first year post-Buffett, suggesting strong momentum toward a $700 target by 2027.
- Date: 2026-11-17 | Impact: medium | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxPM1dENGVxMWdITEZQTWNILUFtSGRGaUVmWF9tOEhzRXVncFJvLTAtSzFFdGlGVjNobUxzSTZhZUYyYVl0VFJTOTFNa1VjdnpJeHRRX2dUamk3QzN5VXZzaE5kQmM5MmY4dWdia3NPZG93TDY2WWE2MDBzOHY5bXdfc0ZvNHV0dE5uSUY3SU5Md0k2RzlzUHpMTXdXZk5HX05OSHc?oc=5>

### Berkshire Hathaway: A Sure Long-Term Winner, But A Much Better Buy If It Drops 15%
- Summary: Positive outlook; suggests Berkshire is a strong long-term investment, especially if price falls 15%.
- Date: 2026-11-20 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxOQjZfQ1c3c0ZReVlQR1Q0Ry1fem9OdDcwZUtEZG9TU3BJdTQ1ZlB1ZUVsRWY5a3F3XzlnV2RDSlRsME53aFFPZjhMYlZES2syRnBRX2FkYkZ3amJoQjRyYkNpSm8yS215d056dHB5ZlAtcG9BSFhDQmpIZWZOMXY5bURnMTRVaF9kVkJEU2RsdG94YkVHZWc2MFR2UkgwNDY2Z0wzU0JaSjRQck5GMDB5aHM0THNwNWZ4bzFGQXdwcjJuYV81WDNZ?oc=5>

### Warren Buffett Stopped Giving Bill Gates's Foundation Berkshire Shares. It Just Sold $1 Billion More and Bought a Dollar Store. Here's When the Rest Runs Out
- Summary: Berkshire sold an additional $1B of shares and purchased a dollar store chain, indicating portfolio rebalancing.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogJBVV95cUxPMDV2NFVXb1VsQmVXTnd5bW5YcjZ5eXVzQXJ0OElqMXV3T3I4OUJsdTRPZmdPc3B0TG4xenBwWGU3cFA2eERhSDJJdUFHT0xLOG5NR0F1T2lOb1BUazRGcUE0OFdUV3QyN184X2hvTm8tVGdndGZ0ZDdzUjA4aGxHQUd0ajhMY3phOUllRFZEX25EWHI4V2V3V0ZqcUp0SmlqQUM4SHZ5M0hVZUgzOHQ3YW0wVjZ5V2R0ek91c3J2XzZWTHNmSnBBbllvZ3JwZUQ2emxJOW1zdkF2UTlRaFN2ZjF2TVpPTHV5NnkwcHU5VjE5LUdpNUg4ZFdHM2tWMG1sa3ZZT2JTcFM0Um4zS09XWnltQl81WVllX01mdXFra0xhUQ?oc=5>

### Kraft Heinz still has Berkshire Hathaway as its top investor (KHC:NYSE)
- Summary: Berkshire remains the largest shareholder in Kraft Heinz, maintaining significant influence in the company.
- Date: 2026-11-17 | Impact: low | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNWFB6eHVqN2hvOEZwNDB0bXBtU20xVk5hQlJkdDlmLVU0a04yUUdsYUZEY0Z5bG4zQXdlZ0xsQ2dZSm9xdWprdjR2bDBpT2xid1dYcXhWWElfOFhfQWpnYnFVeHgxZncxem5sU2ZXdVRHVmo4SVA3NnBYbkRTVFVYM2ZxMi1LVzlRUnRkS3FCTm56NWZ2QzFjM3FPOXUtd1U?oc=5>

### Tracking Berkshire Hathaway Portfolio – Q3 2026 Update (NYSE:BRK.A)
- Summary: Quarterly portfolio update shows Berkshire’s current holdings and recent changes.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQM19sV01OdFRtLUprWElVYlNtcVE5bG1YMjBpNmU2Z1RXU2VNMFlUNEF1Tk1CV2E2NXFlRC14eUZxTHlpb1pjRlhxczBhVEstRHlDU0FlY1IxODlhZFNYM3oyb3RucXJCYWtLRmNQRW54RnFiTkpqNU91dnM2UEN3cGZmc09BcGJ3c3hadXpqNVFsVk1ILUFvRg?oc=5>

## HEADWINDS

### Berkshire almost doubles stake in tumbling housing stock
- Summary: Berkshire almost doubles stake in tumbling housing stock
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxOMERPMWdJQlAwVjFiTXVsd294dVUxeTQzdXh1WjhIX0hnMjJxNFJyN0hJaTBNLUVPMkd3MHZJVFpuejFIMnNodmM3azd5d0tNb0hOR3E0ZnJQYUFfR05jSmUyN1hkbzlsak0wRkh3UHpVQ2VGYjNKQlFCNUVsbEswc29relZlVm40d1o1ekVwMUI5Z1hDZG42eElWN2I1MFNaNGNqVUpoUXM4RUU?oc=5>

### Berkshire Hathaway downgraded by Argus
- Summary: Berkshire Hathaway downgraded by Argus
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxORGgzRU5GV2RRVXZhVTVzamV4eU9FTTl5ZkRWX3ZJSkMwOEk4TGtFemFtdmlMYVNjeWJham1XYWV1OXA1VkFHVWlzMUpxcUpmVkh1OW1waDFKMTNtLV9NUjFMZHNidjJpekJYUTZRWGJXRFZIc24wTHhXYWZtYlRoN3J3VjhWUjFX?oc=5>

### Warren Buffett Says Berkshire Will Never Prefer Cash Over Good Businesses. History Says Your Portfolio Shouldn't Either.
- Summary: Buffett’s statement reinforces long-term value focus, but may be viewed as a strategic stance rather than a direct event.
- Date: 2026-11-19 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxOandVMkcyYUwwQWtUZVNvQWM3WFV3TnhOVlFqZ1ZjWF9nYlNuS1lyUDNFYjlic3B0SmdFX2U4T1oyTXdGdnV5cm5xVk45ckxDQkJmNWw3OEtKenNVVXBkUjNId29mUFplbXRLRF9nVDMtb0NvNWtORmNxUzJ4a3l4VTZBYUkta0g1VlpYc2RQNXVVbDNaQ3QtYkV4T1RFdklFVFE?oc=5>

## CATALYSTS

### Berkshire reveals new $689 million stake in major tech stock
- Summary: Berkshire announced a $689M stake in a major tech company, expanding its portfolio.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQcHNSX3ZyWGhORWM3UjJpeG9sblZJR3dFVXRCYzhRLXZlMnd3M2RyVGVDdW0xLVdBb0lXTmt0RG1ZMUVQS1NNb1VVWXZjTWtRcWdwdWxsSXRtdG1sTHN3MGJuYkJ5V3laY0F4Z2xjeHRLeHBJSmdnekw5cUc5OUk5bFdRUlFHU2RNdTlydHA0ZThyTUJiSGpVOWFvaG1pRFh1NGc?oc=5>

### Berkshire Hathaway (BRK.B) Reveals New Stake And Nearly Doubles One Holding
- Summary: Berkshire doubles a holding, adding a significant stake to its holdings.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPdVhDY2h0djVhZ3dwUXNPSHg3TFFhT1NFUnVvNWpHanZ5M1kzS3JrSENsdlQzNmhHZUJJUjdNc2NXam1LSTdjV0VEZXNneS1Vc2RrZTR2Q1dvREUwUHUxUmJheDJjY1lQTV9zOFlfQ0Z1ZXJiTDJueGdXRnRobzNWQ3pVRmpWcW9tYnY4d0dwZjhuU1dGYUpFQ0VBbDVWQQ?oc=5>

### Warren Buffett Just Gave Away $5.5 Billion of Berkshire Stock. He Says His Confidence in Berkshire Is "As Strong as Ever."
- Summary: Buffett distributes $5.5B of Berkshire shares, signaling strong confidence.
- Date: 2026-11-18 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPZWE3aFRHaTlWWkdRRUxteUdMX1pOSVRBc1NlNmZTMFZlMEdMeHVQRDdSY1JfNlZHMVRZaHJNdkthM3ByYm1udHVFMVROVHhuVk82eGJtcFVXS3pDOTdrQmRfa0dEQ0lTUlNGcW1GenlDQ2QyWGt5dGVuaFNMRmNIQzBaMkt4c1JoenBsQlhEeTBXMmxNR3l0cFlR?oc=5>

### Here's What Berkshire Hathaway Bought and Sold in Q3
- Summary: Summary of Berkshire's Q3 acquisitions and divestitures.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNODdJLV9XbG85V0RTTi1lT2lZTm1KaWFVa2h6MnhXT21UWUlVenZWZFFnVW51Nk9LYWx4V2VPeW1TYlBzbUF6OGpTbWxSNGYtMVBGQklwMFUtenA0VFBRendROW9GRXNudnJGUlhubUhOZ2tPVDBTZ1dDeHFDOXg0ZXNaazlnajNGbnpwY3AzLWF0dw?oc=5>

### Berkshire Hathaway has been a popular 'anti-AI trade.' One firm says it’s too expensive now
- Summary: A firm views Berkshire as overpriced, labeling it an anti-AI trade.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxPOXBfRjdkSEpHSTJ3b2o3dUttNFRyRU1OVVExLWVSWmV6M2FDUWNKVFl1dERwUFFoSGdiUkIwZk9UODRaQjEzbFpaODJnYmRiZXVlcjJKMFBkdGhvcUpLcHFjMVBIX19tLXNZS2NCanJXN2FzQmQ5RlRrREtzN1dZMGFIUDRfYjVWS0oySnFQdjVRbEZhZUp2bnlTZzZPUTVDdXJKSGhfUV9ZQVVXWmRDUkE3cm1JVDgzRzlFbmRuZkVWQQ?oc=5>

### Warren Buffett Expects Berkshire Hathaway (BRKA, BRKB) Stock to Drop About 50% Again Someday. Here's What He Says to Do Then.
- Summary: Buffett predicts a future 50% drop and advises actions.
- Date: 2026-11-19 | Impact: high | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxQV1FWcTNHWTNfd3pnSmZ2MUJYWXpaWm0taXI3TFE5bmRyV041UjVRSUFiYmF6SENLYVV3ZWZiM2pZZ3FISlNUeS13MDhSaWdOVW10M09XVWVJVDllSkFaby1YYm9hZElMM1huZlU1OEJINmc4Z29QZC12Ri1hUThsWmc3TmdueXNoN3dYWlc0TTRHcDMyX1FjVVA1a21jelVzVmJmZU9LTTZwUQ?oc=5>

### Warren Buffett's Successor, Greg Abel, Has 31% of Berkshire Hathaway's $363 Billion Portfolio Invested in 3 Game-Changing AI Stocks
- Summary: Abel’s portfolio heavily weighted in AI stocks.
- Date: 2026-11-20 | Impact: medium | Horizon: medium | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxPTmlyN21KMGdKcXZYMVlvM0hRR2xKUmNKNEMzVHo1cUdjZ3Nqc1E2c2tudFBfLVFVT2ZjNUFyeF9kMmRWb2xvRkV1WVhUTWhtbG44SGdObWhjWTRVbHJlaHJ2MWxXUmNBa0dhNDFuTEdudlBHUlVaMWFXQ1NYRGM3UFA3UWdVakx0MjNKeW9rMDFza2I2OUxPZklmNHlvRDJuZHJmckI1RHFxc0ltaGZjSVl3VXhLc0VCSEhjNjJiOGkteEVES3ZrcGhzTmk4MW9xUnc?oc=5>

### Forget Apple. Warren Buffett’s Berkshire Is Pouring Nearly $1 Billion Into This Little-Known Tech Stock.
- Summary: Berkshire Hathaway invests ~$1B in a small tech company, expanding its portfolio.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3AFBVV95cUxNNkJQLVk5VVlHT1dtNGdncEF5NURIQ01zRFE5VmV6c0NUYTM5N0dlOXJqOWxlaUt2dVBkUEtkZ2VWS1M3Yk1SRXllVnNQZEtmcTQwclhTTS12dmhoOE1nNXNyc0FOS2ZNNmlQSUl6bnVBMC1ER0MwMW1acnhRSC1SWXZ5WVNMekVURm11aHFQYy1nOHMtYnFIbmFlZThqeE1Cb1lNbnY5eHdUeUstWFBNMGhHMzdQQUFLdllqU3dJX0dhbEo0dDk2WjRmbzVrRVN1elp1TlM3UTlvYzl6?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **BRK-B** | **16.01** | **0.00** | **-2.04** | **11.20** | **1,210,976,043,008.00 USD** | **13.75** |
| MKL | 13.89 | 1.28 | 7.92 | -11.20 | 23,683,143,680.00 USD | -5.08 |
| FFH.TO | 9.59 | 1.39 | 8.54 | 1.90 | 54,538,334,208.00 CAD | 12.10 |
| L | 15.17 | 1.21 | 8.59 | 1.90 | 22,123,440,128.00 USD | 4.49 |

Peers fetched as_of: 2026-11-20; BRK-B reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-07
- Next expected earnings: 2027-03-01 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-20

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-09
- Revenue (latest available single quarter): 105,647,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 22,112,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1067983/000119312526452412/brka-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiogFBVV95cUxPM1dENGVxMWdITEZQTWNILUFtSGRGaUVmWF9tOEhzRXVncFJvLTAtSzFFdGlGVjNobUxzSTZhZUYyYVl0VFJTOTFNa1VjdnpJeHRRX2dUamk3QzN5VXZzaE5kQmM5MmY4dWdia3NPZG93TDY2WWE2MDBzOHY5bXdfc0ZvNHV0dE5uSUY3SU5Md0k2RzlzUHpMTXdXZk5HX05OSHc?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxOQjZfQ1c3c0ZReVlQR1Q0Ry1fem9OdDcwZUtEZG9TU3BJdTQ1ZlB1ZUVsRWY5a3F3XzlnV2RDSlRsME53aFFPZjhMYlZES2syRnBRX2FkYkZ3amJoQjRyYkNpSm8yS215d056dHB5ZlAtcG9BSFhDQmpIZWZOMXY5bURnMTRVaF9kVkJEU2RsdG94YkVHZWc2MFR2UkgwNDY2Z0wzU0JaSjRQck5GMDB5aHM0THNwNWZ4bzFGQXdwcjJuYV81WDNZ?oc=5
- https://news.google.com/rss/articles/CBMiogJBVV95cUxPMDV2NFVXb1VsQmVXTnd5bW5YcjZ5eXVzQXJ0OElqMXV3T3I4OUJsdTRPZmdPc3B0TG4xenBwWGU3cFA2eERhSDJJdUFHT0xLOG5NR0F1T2lOb1BUazRGcUE0OFdUV3QyN184X2hvTm8tVGdndGZ0ZDdzUjA4aGxHQUd0ajhMY3phOUllRFZEX25EWHI4V2V3V0ZqcUp0SmlqQUM4SHZ5M0hVZUgzOHQ3YW0wVjZ5V2R0ek91c3J2XzZWTHNmSnBBbllvZ3JwZUQ2emxJOW1zdkF2UTlRaFN2ZjF2TVpPTHV5NnkwcHU5VjE5LUdpNUg4ZFdHM2tWMG1sa3ZZT2JTcFM0Um4zS09XWnltQl81WVllX01mdXFra0xhUQ?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNWFB6eHVqN2hvOEZwNDB0bXBtU20xVk5hQlJkdDlmLVU0a04yUUdsYUZEY0Z5bG4zQXdlZ0xsQ2dZSm9xdWprdjR2bDBpT2xid1dYcXhWWElfOFhfQWpnYnFVeHgxZncxem5sU2ZXdVRHVmo4SVA3NnBYbkRTVFVYM2ZxMi1LVzlRUnRkS3FCTm56NWZ2QzFjM3FPOXUtd1U?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQM19sV01OdFRtLUprWElVYlNtcVE5bG1YMjBpNmU2Z1RXU2VNMFlUNEF1Tk1CV2E2NXFlRC14eUZxTHlpb1pjRlhxczBhVEstRHlDU0FlY1IxODlhZFNYM3oyb3RucXJCYWtLRmNQRW54RnFiTkpqNU91dnM2UEN3cGZmc09BcGJ3c3hadXpqNVFsVk1ILUFvRg?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxOMERPMWdJQlAwVjFiTXVsd294dVUxeTQzdXh1WjhIX0hnMjJxNFJyN0hJaTBNLUVPMkd3MHZJVFpuejFIMnNodmM3azd5d0tNb0hOR3E0ZnJQYUFfR05jSmUyN1hkbzlsak0wRkh3UHpVQ2VGYjNKQlFCNUVsbEswc29relZlVm40d1o1ekVwMUI5Z1hDZG42eElWN2I1MFNaNGNqVUpoUXM4RUU?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxORGgzRU5GV2RRVXZhVTVzamV4eU9FTTl5ZkRWX3ZJSkMwOEk4TGtFemFtdmlMYVNjeWJham1XYWV1OXA1VkFHVWlzMUpxcUpmVkh1OW1waDFKMTNtLV9NUjFMZHNidjJpekJYUTZRWGJXRFZIc24wTHhXYWZtYlRoN3J3VjhWUjFX?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOandVMkcyYUwwQWtUZVNvQWM3WFV3TnhOVlFqZ1ZjWF9nYlNuS1lyUDNFYjlic3B0SmdFX2U4T1oyTXdGdnV5cm5xVk45ckxDQkJmNWw3OEtKenNVVXBkUjNId29mUFplbXRLRF9nVDMtb0NvNWtORmNxUzJ4a3l4VTZBYUkta0g1VlpYc2RQNXVVbDNaQ3QtYkV4T1RFdklFVFE?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQcHNSX3ZyWGhORWM3UjJpeG9sblZJR3dFVXRCYzhRLXZlMnd3M2RyVGVDdW0xLVdBb0lXTmt0RG1ZMUVQS1NNb1VVWXZjTWtRcWdwdWxsSXRtdG1sTHN3MGJuYkJ5V3laY0F4Z2xjeHRLeHBJSmdnekw5cUc5OUk5bFdRUlFHU2RNdTlydHA0ZThyTUJiSGpVOWFvaG1pRFh1NGc?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPdVhDY2h0djVhZ3dwUXNPSHg3TFFhT1NFUnVvNWpHanZ5M1kzS3JrSENsdlQzNmhHZUJJUjdNc2NXam1LSTdjV0VEZXNneS1Vc2RrZTR2Q1dvREUwUHUxUmJheDJjY1lQTV9zOFlfQ0Z1ZXJiTDJueGdXRnRobzNWQ3pVRmpWcW9tYnY4d0dwZjhuU1dGYUpFQ0VBbDVWQQ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPZWE3aFRHaTlWWkdRRUxteUdMX1pOSVRBc1NlNmZTMFZlMEdMeHVQRDdSY1JfNlZHMVRZaHJNdkthM3ByYm1udHVFMVROVHhuVk82eGJtcFVXS3pDOTdrQmRfa0dEQ0lTUlNGcW1GenlDQ2QyWGt5dGVuaFNMRmNIQzBaMkt4c1JoenBsQlhEeTBXMmxNR3l0cFlR?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNODdJLV9XbG85V0RTTi1lT2lZTm1KaWFVa2h6MnhXT21UWUlVenZWZFFnVW51Nk9LYWx4V2VPeW1TYlBzbUF6OGpTbWxSNGYtMVBGQklwMFUtenA0VFBRendROW9GRXNudnJGUlhubUhOZ2tPVDBTZ1dDeHFDOXg0ZXNaazlnajNGbnpwY3AzLWF0dw?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxPOXBfRjdkSEpHSTJ3b2o3dUttNFRyRU1OVVExLWVSWmV6M2FDUWNKVFl1dERwUFFoSGdiUkIwZk9UODRaQjEzbFpaODJnYmRiZXVlcjJKMFBkdGhvcUpLcHFjMVBIX19tLXNZS2NCanJXN2FzQmQ5RlRrREtzN1dZMGFIUDRfYjVWS0oySnFQdjVRbEZhZUp2bnlTZzZPUTVDdXJKSGhfUV9ZQVVXWmRDUkE3cm1JVDgzRzlFbmRuZkVWQQ?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxQV1FWcTNHWTNfd3pnSmZ2MUJYWXpaWm0taXI3TFE5bmRyV041UjVRSUFiYmF6SENLYVV3ZWZiM2pZZ3FISlNUeS13MDhSaWdOVW10M09XVWVJVDllSkFaby1YYm9hZElMM1huZlU1OEJINmc4Z29QZC12Ri1hUThsWmc3TmdueXNoN3dYWlc0TTRHcDMyX1FjVVA1a21jelVzVmJmZU9LTTZwUQ?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxPTmlyN21KMGdKcXZYMVlvM0hRR2xKUmNKNEMzVHo1cUdjZ3Nqc1E2c2tudFBfLVFVT2ZjNUFyeF9kMmRWb2xvRkV1WVhUTWhtbG44SGdObWhjWTRVbHJlaHJ2MWxXUmNBa0dhNDFuTEdudlBHUlVaMWFXQ1NYRGM3UFA3UWdVakx0MjNKeW9rMDFza2I2OUxPZklmNHlvRDJuZHJmckI1RHFxc0ltaGZjSVl3VXhLc0VCSEhjNjJiOGkteEVES3ZrcGhzTmk4MW9xUnc?oc=5
- https://news.google.com/rss/articles/CBMi3AFBVV95cUxNNkJQLVk5VVlHT1dtNGdncEF5NURIQ01zRFE5VmV6c0NUYTM5N0dlOXJqOWxlaUt2dVBkUEtkZ2VWS1M3Yk1SRXllVnNQZEtmcTQwclhTTS12dmhoOE1nNXNyc0FOS2ZNNmlQSUl6bnVBMC1ER0MwMW1acnhRSC1SWXZ5WVNMekVURm11aHFQYy1nOHMtYnFIbmFlZThqeE1Cb1lNbnY5eHdUeUstWFBNMGhHMzdQQUFLdllqU3dJX0dhbEo0dDk2WjRmbzVrRVN1elp1TlM3UTlvYzl6?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
