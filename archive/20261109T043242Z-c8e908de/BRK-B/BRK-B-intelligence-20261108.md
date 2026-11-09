# BRK-B Intelligence Report

- ticker: **BRK-B**
- Report as_of: **2026-11-08**
- Market data as_of: **2026-11-06**
- Quant sources: https://finance.yahoo.com/quote/BRK-B/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/BRK-B/key-statistics/
- AI analysis snapshot as_of: **2026-11-08**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-09T04:45:39.644010+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 8, 'ai': 14, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261108T041758Z-43fb2458/BRK-B** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 9 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 37.5%; oldest publication 2026-11-04

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

### Berkshire shares surge as Wall Street swoons amid AI fears
- Summary: Berkshire shares surge as Wall Street swoons amid AI fears
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPQXgyQmpJT1lzSWhTZ01uZWJoRngzWm44N2hQT2lRcUNLWVZONlZQa3lHOTN0VE1zNEZvSjNzUEk4aThrNk1DbTZpazdtTm43TmJUYWNwYWlnTDJocHM3T3BybUpWSlM1ZElKTExkRTBoQy1NVy1zZDRCWHNPZDJFcXJReDR2OF81MkxPS282anN1UzRlUzNBb0tWTQ?oc=5>

### Berkshire Hathaway Shares Are Up 11% This Year. Is the Stock a Buy Ahead of Earnings?
- Summary: Berkshire Hathaway Shares Are Up 11% This Year. Is the Stock a Buy Ahead of Earnings?
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxQVjhPR3hqVG9yeXF2YXNxOVVIUzBtR2xabkdtczY5MzhCZWkweHJfMjk0OUJITFZWNTRjZTNCNWl6VHRkbEtrb21pU1FkWFVwTFEyZjNVeVduLVdiUjlrTWRQdGtJT0JicjY0S2dPT09TM0dOQ2tpTm1sSGJQdWs2ODBSUDV5T051U29OXzh1WmRlLWEwYVpyZnlOOG9icmNWNXdxcGFHVHB4bXBQYm1XRTRzZUhzamRV?oc=5>

### Berkshire Hathaway Reports Nov. 7 With Its Stock at a Record. Its Cash Pile Is the Number to Watch.
- Summary: Berkshire’s stock hit a record; its cash reserves remain a key metric.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxQRTFYN1AwWVpyUUxvMWF3R004djZQc0ljZFpSUmtzckhuU1hTX0dhZnBzNkk2UUw4d0VjTHBBbXUwTlUwUFhReGt2TmdIUVhnZzVpbjY5cy1XeTRnWi10MTlubVhxdDIxS2s0bExjWmQ0U3VhYmpfOFYzUWdTXzU4dElmUUJVcl85VUJiS2w3c0c3TTg5Q1plYzVPcnJjTGQ3OEFHTDJyNHVoZDNXTkNuZk1xRko5eXFMQXdjclR0OWp5ZUtNR0FwUFJoRmxpR2xIYkxOVVF3?oc=5>

### Forget the AI Friday Rally: Why Big Money Is Still Fleeing to Warren Buffett's Berkshire Hathaway
- Summary: Investors are moving capital toward Berkshire, indicating confidence in its stability.
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxQbDBVSXNTeVRMa0xqaWxjNFNodVpKai1ZOEdNNFRzTzdNS1dvNmU2Y1dxMzJsYzBQUWN5a0R0dmotNnoyX2tEZXAxMTlKVDVFMElleHBuajNrUW5aUE01akViLXg5ci05Mk9naktWVWpCb1F2ckFKakc0RFhpQ1RlVkYtZkJJdUkwUUdOdXdPUTdXOEFhWjdycXJSajluMkFzWmtUWUVOQUV5M0lmLXFYbjFNQXp0cl85ZTNHTFZLV3BESHoyQjVxbWQ1alF0Q3dwbmxTYUlR?oc=5>

### Berkshire Hathaway's Stock Portfolio Is Worth About 3 Times What It Paid. The Gains Alone Equal About 19% of the Company.
- Summary: Portfolio value tripled, gains 19% of company, indicating strong asset performance.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPWmxkMW4tQXR5X09YUWJIXy1QMFE2VTA1NjkyTEx0MTBmZHRhQUJiTzAxMnBBR0Q0dUhpNVB5VHBrWTJ3N0g2b3RvYkZybnlmM0IyYmpXMHlhNHZQLVM4b0VhOXhxYmNSaEZCRF83WVFiQXVjZDN6bWJQSE9MSFR3TE04akxPWWhzOWtGMC03bVlOei1qeFVWLTBVeVh4QjZFWmtNajNKWGpxZw?oc=5>

### This Warren Buffett Dividend Stock Is the One I'd Buy With $1,000 in November
- Summary: Positive recommendation to buy Buffett’s dividend stock.
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQeWNYVVdULV9FeUxCTzZnTEI3dHU0SjZvRV82QTd4ZnRDeHZZYVVnMXJadEpHeVkzV29LbDd1Wmt1NGdxQmtQbGptUmtRYktvbVNjTXRwQ0dQNkc4OG9GaXZKQjBtMk1vbWVwbFRZbmdPQXpSVkRkcjd5YnRMQ0JGaE1nNmtKUHEwdmJ3OHh6ZHE3QXVMZ3BpZU4wMUZMRUE?oc=5>

### Warren Buffett's Coca-Cola Shares Now Pay Back Two-Thirds of What He Paid, Every Single Year
- Summary: Coca‑Cola dividends now exceed two‑thirds of Buffett’s purchase price, indicating strong cash returns.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisgJBVV95cUxQcEdjdy03RmlrUTMzaFlndXRIcUlKdnJhUmdDUUxxYzNhZFRYUzZtRDctdG5DanowMFBNejZ5NFlJdm1EWWZyMHpTTVBjbk5ac1gtUGZvRkw5dHZlSm9ySUZBVE9DR2UxWm0tNm5GU0ZSczM4UXdrNHRzMFAwUUttdXEyVWFtZ2ZqczFyQ1JDY1phb3psTFZuYzhEZGRXSlNhdjlkUWV3Xy1OTm9WMUk2NnVuVEFSVGgwcW1pNXpFdFB3b0RnOGFTTjFUWXBLWG1mZ3hRRUhSWm43UU5mODJUQUxPWE40WU1kaGF6cUVMZEpKYjc0WWJWSW5XV3ptdUJOT1ZzMUxpTXJtbXVqYS03YU5fRE9GdUpoempCSW1hN0ZlNjN3M1IweFluM1pnYzBQM2c?oc=5>

## HEADWINDS

### Berkshire Hathaway Earnings: Cash Levels Retreat Again as Acquisitions and Share Buybacks Pick Up
- Summary: Berkshire Hathaway Earnings: Cash Levels Retreat Again as Acquisitions and Share Buybacks Pick Up
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxNU3k5QnhncjJEWEVxWGlGZm9DRnBxTGRBQ29fZHBfV3VrRnVkWEs5bzFSZnZhcURvdzBHVmdiOG5zOGJSdjZRMzVpZGQtY1RKRVBTS0dsa2ZmYWliSEIzUHctdEEtVVo1MHZNU2NsMzFaTHZ5eWxNQ0JWZnp0SWNwQjNIM2IxUmFrX0hvSFBmRzdkOUJ0UFBsUF9HbjlqamcxNDF0T2huUldUSndCQ0I2S2ZQLXdvbU1QTGFNSWZuazdWQQ?oc=5>

### Berkshire’s Operating Earnings Fell 6% to $12.7 Billion in 3Q; Stock Buybacks Hit $9.6 Billion
- Summary: Berkshire’s Operating Earnings Fell 6% to $12.7 Billion in 3Q; Stock Buybacks Hit $9.6 Billion
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxOLTRIamMySU9hMmxlaXZDaExNaVg5N2xJY0t0a2lTOWF2Tmc5QTRnbzkyMUFEcklKRmVHN3UyRzNPTWF0VWdENE12eU5CTkh1WUVCUjFyRnVyODdqajZQR3VyTWVfakctbzZrc293MF9vb2NfZFI2QmdabGE1a2syV2Q1WHM0U1Zk?oc=5>

### Berkshire Hathaway (BRK.A) Formalizes Greg Abel Succession After Earnings Slip And $9.6 Billion Repurchase
- Summary: Berkshire Hathaway (BRK.A) Formalizes Greg Abel Succession After Earnings Slip And $9.6 Billion Repurchase
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOb28zSUxaNTBMVXp0WS1UZ0JtTUU1REZtWUNhUHVnaElEMXpNOVZ4a2lqRk9nVWZwblRjeFduS2NPTnU4ZWRHQXVSY2hnNnFxbXUzZzZhSF9jYjhkOXhLTE41SzdkNlotNmstVko2RFJvY1lHbUM4TUxTcEtmUkQ2UzA5NWJxSVlwMjVJOHlXM2pVeXFSX1dIUGJKOEl6cEI2N3lxN3Fn?oc=5>

### Berkshire Hathaway’s Operating Earnings Fall, Buybacks Rise
- Summary: Operating earnings decline, offset by increased buybacks.
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxQMGduc3dBZWxiNEFiNnBVc0E5SFlZbFJuMDN3UHczaHkwQnVTTWRWeEh1TmdFNTBfZC1uTjU4NEVLc1FQUG5oZk82TzRBbEN6S0kySGxNRVhzb1RVemlNdkZZcV96WVFVZVRUM3VDaWpGd3JPaTJmaG1CSTAzWWZLM0hPdWtzSXN6cnhMdm9zMy12WnFhRnRPT1E5Vm5JdzdzMTJvcFVuV0ZtWlE?oc=5>

### Berkshire Hathaway (BRK.A) Stock Faces Q3 Earnings Profit Decline Forecast
- Summary: Forecast predicts a decline in Q3 earnings profit for Berkshire Hathaway.
- Date: 2026-11-08 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOdGpudktybjBqOEZRSnBSOWxDcE5UU3EzZ0dzVU5qcVplaHhSLWRyVGphNTB0T2RqTk9TWEU2cklNcnd2a1NxeklZYWpNMnRYSEFUc0YtazdnbFdFRExNRWdrempuUy12VlV5LWxQVEpFZFNubklGWkJOemJ3NTBoel9QT2dIV2pqVnBKWVZZTHdJVmhCelpGT1Y2VW5XanNo?oc=5>

## CATALYSTS

### Berkshire Hathaway Inc. News Release
- Summary: Berkshire Hathaway Inc. News Release
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxPdFdZRkFBTThXWTJ4aHNRaTQwYXM4T3pORXVadmQ4NzRJN3ctYWZ5OGU3dHd0M0pZZjBMbnhmbklreXVHeFY4cHY4cFNzNzFaV2Z4TWR3bHh0TTFUUFkwenowZ2xwZlVRUF9aNzVDc2taQm9WSG1WSlpDUlBDdGxqcUU3M211OTEwaER2S0RpNlZTa0tzam8yUjFvMG9TR09iR1E?oc=5>

### Berkshire Hathaway buys back $9.6 billion of its own stock but its profits declined
- Summary: Berkshire Hathaway buys back $9.6 billion of its own stock but its profits declined
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNekhIdFlna0VmeDEwU1BIOFl2OS1tb1l1czNfZWt5b2l2aHIzQmVEVEVIUHFaTV9SVkdYaDlOcVc0Wl9zTTNzdUtkUlJMU3gxRFNJWnpPYy0wMUFSd24wSUdkSlVJNGFWV2VLT3ZBM1hrMmZhSXo1ZlRXTllvcExLRGhMYkxwQUp2ckc5dVg5N19vOHBieHk1ZnFMVQ?oc=5>

### Berkshire improves Q3 buybacks while profits dip (BRK.A:NYSE)
- Summary: Berkshire improves Q3 buybacks while profits dip (BRK.A:NYSE)
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigwFBVV95cUxPblVZQjExbGQ5VlpOcW1aTkxTWDBmNm1ESkxydzd6NDJpNThBdHZ2M1QweEdYR1o3N0dFU244ZFM3ekYySHVoT0JYd3ByT3FYZ2VybHZQUFlHZ1ZuUFBzV2tid2lueUdCT3ltdW9CclRqOHBIZlUtMHB1Rm1rSHZHdzRDYw?oc=5>

### Berkshire Hathaway’s Quarterly Profit Falls After Investment Gains Shrink
- Summary: Berkshire Hathaway reports a decline in quarterly profit due to reduced investment gains.
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQSlRmcnB2bWtXOHV1MEJucmRMSFpiMjUtM1dMUnVRbnBybWxCSWJ0YU02QVczWERwbDlNQzJSeThHVnRNUmEtd3dOQzRUQnJhT2V5WlhQczRYdVVGaUV3YVpaNUdvUkNqRDB0aWpDQW5IV0xtbF8zQjdGNm9xYlllMDRSYTZTLXNHMTJGLUNXYXhCMGx2R2drclQ5amZocWJndlE?oc=5>

### Berkshire Hathaway: Abel Just Made The Biggest Buyback In History (NYSE:BRK.A)
- Summary: Abel executed the largest share buyback in Berkshire Hathaway history.
- Date: 2026-11-07 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxPaEZpWkxwNlN4U1d1UmxzMEVHWWJxOVYtSkhRYUdhekpOVjJuaTVsd1MwMDRNalhrRXhhbTJtMkdCd3J0SWplcEVjSHgtbFVKUGU2bmh3c00tN0d6Vmk3Nmk5bGJuQ1FkVzZWb3dnMURsUVJnQ1hRQTMwMnZmOWs3WXZYZkZ1Tm1mNkJxXzE2ekU3UXlKdnJfQjQ0ME5VRVFGTjdySVhQczk?oc=5>

## RISKS

### Berkshire Hathaway: The Easy Re-Rating Is Gone (NYSE:BRK.A)
- Summary: Berkshire's easy re-rating has disappeared, indicating potential credit risk changes.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxPSGUzZzN3eG1yME1RSXRweXlLR3NxLTlqcVYzSDFDd19fN2tJQUdIaWlYNXYyTXVxc1dkSnlvVlFyaVBpcW01a1piYl83SkJuMVVKTWM1RGZ2STVQck9LRVZFNlA5Ykd4XzY1RmVkWGx4dW5FZ3lPeWE1Q1NuY01lZGplUEwtS0RLLXdPbE1Xbw?oc=5>

### Berkshire Hathaway: BNSF And Energy Steal The Show In Q3 (Rating Downgrade)
- Summary: BNSF and Energy sectors received a rating downgrade, impacting Berkshire Hathaway.
- Date: 2026-11-08 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPNjVIWGhXeEl0aF9saUJhMWk3Y3E1VXN4X3dxaElKdk1tUkd6ZjA3NVNrOGd6UDI2UDhnS1NmcDV3QnJYZXFmOXlQS2pJbk9QYXlvWEhpTS1lREk0MzluTzV1QkJReGFUOWw3NEVkQUYtbVFkNWhXYVZ1WEZ5aXgxek0yeFBBT1BSWi1IaDJQVFJiOW1kS1ZpM3I2Q2U?oc=5>

### Is a Market Crash Coming? Warren Buffett's Warning Is Ringing Loud and Clear.
- Summary: Buffett warns of imminent market crash, signaling potential downturn.
- Date: 2026-11-08 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNb3g4SklKVjFSZmppYlVTU2dyd2ZpWkVnaWNmdUw0TE5haW05S1lxWlpZYlJJR3RjT0JBbUp2TkMxTURuVjJrZDBwcUx2Mi05SW9EcjBEaUhfMDE1Sm85ZDM1T3N2VU00VEFJbXo0ZmtPd1M0UXZEOVJocWhXUnAzaGxwZFZHUU5hTEtoU2wwVEFIQTNDbzYyc1NHUjFZeEV0OEE?oc=5>

### Warren Buffett and Greg Abel Just Sent Shockwaves Through Wall Street With This $377 Billion Warning
- Summary: Buffett and Abel issue warning that could trigger market volatility.
- Date: 2026-11-08 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxPWDJUeGR3dEw0Z2lqQ2VIaXN2UG9rZjdWbjdub3Nqa1NHei1qWU5ZWC1zUkRQTFQwSncwZEMzTlZjcVFxRjZ0ZGg0TEozRS1YVDVULTN6Zmo5S0dIQW1YNGtzN0ZPX1ZyeGhhamlRWFlqczJGWmFSZVgzQU5EUkFGbElFMVZIbzBVUXV2RlF3N0t6c0paeWJ5UlROSGJsTUY0Q1QzUUFBb3AyT2I3djRnazdqZ0VOV2dPTGVfbmo0RDBxTVFxb2FneVFZUDROUQ?oc=5>

### Warren Buffett's Successor, Greg Abel, Has 71% of Berkshire Hathaway's $362 Billion Portfolio Invested in 7 Standout Stocks
- Summary: Abel's concentrated portfolio may expose Berkshire to sector risk.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4gFBVV95cUxNdlk5ZDQyTU43VDFLV01oUEFrWWpVSWRINV9tZUhibGgtRlllbzdjOE9fVWlHNGc5TjYyTlRjUkdoMllrRG81c01UNDJZUUtkb09vSHQ1N1I5dFU1YzlwZm8zZm1LVGhGc0pFYVRjMEUxQmZ0S0JSeXp6RDJDTWF2SHY5SkRRUWMzS204dVRvUFE5N3NyenV3UlRmd0JIejBmTl95S2RISUV2VHpCSDN1SG90Q2hCa3pRWjhkaDN5RDYzVkR3bU5mdFNSN01QS2d4V2FzeUNJZUVHdzNMZk82Y1VR?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **BRK-B** | **14.36** | **0.00** | **-1.79** | **10.00** | **1,222,109,822,976.00 USD** | **15.76** |
| MKL | 13.80 | 1.28 | 7.93 | -11.20 | 23,713,228,800.00 USD | -3.49 |
| FFH.TO | 9.87 | 1.41 | 8.66 | 1.90 | 55,458,017,280.00 CAD | 21.78 |
| L | 15.17 | 1.22 | 8.61 | 1.90 | 22,186,129,408.00 USD | 8.20 |

Peers fetched as_of: 2026-11-08; BRK-B reuses existing data (market data as_of: 2026-11-06); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-07
- Next expected earnings: 2027-03-01 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-08

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

- https://news.google.com/rss/articles/CBMimwFBVV95cUxPQXgyQmpJT1lzSWhTZ01uZWJoRngzWm44N2hQT2lRcUNLWVZONlZQa3lHOTN0VE1zNEZvSjNzUEk4aThrNk1DbTZpazdtTm43TmJUYWNwYWlnTDJocHM3T3BybUpWSlM1ZElKTExkRTBoQy1NVy1zZDRCWHNPZDJFcXJReDR2OF81MkxPS282anN1UzRlUzNBb0tWTQ?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxQVjhPR3hqVG9yeXF2YXNxOVVIUzBtR2xabkdtczY5MzhCZWkweHJfMjk0OUJITFZWNTRjZTNCNWl6VHRkbEtrb21pU1FkWFVwTFEyZjNVeVduLVdiUjlrTWRQdGtJT0JicjY0S2dPT09TM0dOQ2tpTm1sSGJQdWs2ODBSUDV5T051U29OXzh1WmRlLWEwYVpyZnlOOG9icmNWNXdxcGFHVHB4bXBQYm1XRTRzZUhzamRV?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxQRTFYN1AwWVpyUUxvMWF3R004djZQc0ljZFpSUmtzckhuU1hTX0dhZnBzNkk2UUw4d0VjTHBBbXUwTlUwUFhReGt2TmdIUVhnZzVpbjY5cy1XeTRnWi10MTlubVhxdDIxS2s0bExjWmQ0U3VhYmpfOFYzUWdTXzU4dElmUUJVcl85VUJiS2w3c0c3TTg5Q1plYzVPcnJjTGQ3OEFHTDJyNHVoZDNXTkNuZk1xRko5eXFMQXdjclR0OWp5ZUtNR0FwUFJoRmxpR2xIYkxOVVF3?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxQbDBVSXNTeVRMa0xqaWxjNFNodVpKai1ZOEdNNFRzTzdNS1dvNmU2Y1dxMzJsYzBQUWN5a0R0dmotNnoyX2tEZXAxMTlKVDVFMElleHBuajNrUW5aUE01akViLXg5ci05Mk9naktWVWpCb1F2ckFKakc0RFhpQ1RlVkYtZkJJdUkwUUdOdXdPUTdXOEFhWjdycXJSajluMkFzWmtUWUVOQUV5M0lmLXFYbjFNQXp0cl85ZTNHTFZLV3BESHoyQjVxbWQ1alF0Q3dwbmxTYUlR?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPWmxkMW4tQXR5X09YUWJIXy1QMFE2VTA1NjkyTEx0MTBmZHRhQUJiTzAxMnBBR0Q0dUhpNVB5VHBrWTJ3N0g2b3RvYkZybnlmM0IyYmpXMHlhNHZQLVM4b0VhOXhxYmNSaEZCRF83WVFiQXVjZDN6bWJQSE9MSFR3TE04akxPWWhzOWtGMC03bVlOei1qeFVWLTBVeVh4QjZFWmtNajNKWGpxZw?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQeWNYVVdULV9FeUxCTzZnTEI3dHU0SjZvRV82QTd4ZnRDeHZZYVVnMXJadEpHeVkzV29LbDd1Wmt1NGdxQmtQbGptUmtRYktvbVNjTXRwQ0dQNkc4OG9GaXZKQjBtMk1vbWVwbFRZbmdPQXpSVkRkcjd5YnRMQ0JGaE1nNmtKUHEwdmJ3OHh6ZHE3QXVMZ3BpZU4wMUZMRUE?oc=5
- https://news.google.com/rss/articles/CBMisgJBVV95cUxQcEdjdy03RmlrUTMzaFlndXRIcUlKdnJhUmdDUUxxYzNhZFRYUzZtRDctdG5DanowMFBNejZ5NFlJdm1EWWZyMHpTTVBjbk5ac1gtUGZvRkw5dHZlSm9ySUZBVE9DR2UxWm0tNm5GU0ZSczM4UXdrNHRzMFAwUUttdXEyVWFtZ2ZqczFyQ1JDY1phb3psTFZuYzhEZGRXSlNhdjlkUWV3Xy1OTm9WMUk2NnVuVEFSVGgwcW1pNXpFdFB3b0RnOGFTTjFUWXBLWG1mZ3hRRUhSWm43UU5mODJUQUxPWE40WU1kaGF6cUVMZEpKYjc0WWJWSW5XV3ptdUJOT1ZzMUxpTXJtbXVqYS03YU5fRE9GdUpoempCSW1hN0ZlNjN3M1IweFluM1pnYzBQM2c?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxNU3k5QnhncjJEWEVxWGlGZm9DRnBxTGRBQ29fZHBfV3VrRnVkWEs5bzFSZnZhcURvdzBHVmdiOG5zOGJSdjZRMzVpZGQtY1RKRVBTS0dsa2ZmYWliSEIzUHctdEEtVVo1MHZNU2NsMzFaTHZ5eWxNQ0JWZnp0SWNwQjNIM2IxUmFrX0hvSFBmRzdkOUJ0UFBsUF9HbjlqamcxNDF0T2huUldUSndCQ0I2S2ZQLXdvbU1QTGFNSWZuazdWQQ?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxOLTRIamMySU9hMmxlaXZDaExNaVg5N2xJY0t0a2lTOWF2Tmc5QTRnbzkyMUFEcklKRmVHN3UyRzNPTWF0VWdENE12eU5CTkh1WUVCUjFyRnVyODdqajZQR3VyTWVfakctbzZrc293MF9vb2NfZFI2QmdabGE1a2syV2Q1WHM0U1Zk?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOb28zSUxaNTBMVXp0WS1UZ0JtTUU1REZtWUNhUHVnaElEMXpNOVZ4a2lqRk9nVWZwblRjeFduS2NPTnU4ZWRHQXVSY2hnNnFxbXUzZzZhSF9jYjhkOXhLTE41SzdkNlotNmstVko2RFJvY1lHbUM4TUxTcEtmUkQ2UzA5NWJxSVlwMjVJOHlXM2pVeXFSX1dIUGJKOEl6cEI2N3lxN3Fn?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxQMGduc3dBZWxiNEFiNnBVc0E5SFlZbFJuMDN3UHczaHkwQnVTTWRWeEh1TmdFNTBfZC1uTjU4NEVLc1FQUG5oZk82TzRBbEN6S0kySGxNRVhzb1RVemlNdkZZcV96WVFVZVRUM3VDaWpGd3JPaTJmaG1CSTAzWWZLM0hPdWtzSXN6cnhMdm9zMy12WnFhRnRPT1E5Vm5JdzdzMTJvcFVuV0ZtWlE?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOdGpudktybjBqOEZRSnBSOWxDcE5UU3EzZ0dzVU5qcVplaHhSLWRyVGphNTB0T2RqTk9TWEU2cklNcnd2a1NxeklZYWpNMnRYSEFUc0YtazdnbFdFRExNRWdrempuUy12VlV5LWxQVEpFZFNubklGWkJOemJ3NTBoel9QT2dIV2pqVnBKWVZZTHdJVmhCelpGT1Y2VW5XanNo?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxPdFdZRkFBTThXWTJ4aHNRaTQwYXM4T3pORXVadmQ4NzRJN3ctYWZ5OGU3dHd0M0pZZjBMbnhmbklreXVHeFY4cHY4cFNzNzFaV2Z4TWR3bHh0TTFUUFkwenowZ2xwZlVRUF9aNzVDc2taQm9WSG1WSlpDUlBDdGxqcUU3M211OTEwaER2S0RpNlZTa0tzam8yUjFvMG9TR09iR1E?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNekhIdFlna0VmeDEwU1BIOFl2OS1tb1l1czNfZWt5b2l2aHIzQmVEVEVIUHFaTV9SVkdYaDlOcVc0Wl9zTTNzdUtkUlJMU3gxRFNJWnpPYy0wMUFSd24wSUdkSlVJNGFWV2VLT3ZBM1hrMmZhSXo1ZlRXTllvcExLRGhMYkxwQUp2ckc5dVg5N19vOHBieHk1ZnFMVQ?oc=5
- https://news.google.com/rss/articles/CBMihgFBVV95cUxOV1MzYnhvUVFDNy1XSFJMMlU0RHhFNkFyTmM2Y0xqdVhUNmtNSUVsSkJtV0lIRjlKaFZWNGRuVTJkaWl6ZTNXYUNSVlMxdTNsNDlaN2RqU01RLVN5UHJKdXZmZGZKVW13amE4d2xsZmxRUmdISUhPQXc5ajYyOTRNd1lDTTczZw?oc=5
- https://news.google.com/rss/articles/CBMigwFBVV95cUxPblVZQjExbGQ5VlpOcW1aTkxTWDBmNm1ESkxydzd6NDJpNThBdHZ2M1QweEdYR1o3N0dFU244ZFM3ekYySHVoT0JYd3ByT3FYZ2VybHZQUFlHZ1ZuUFBzV2tid2lueUdCT3ltdW9CclRqOHBIZlUtMHB1Rm1rSHZHdzRDYw?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQSlRmcnB2bWtXOHV1MEJucmRMSFpiMjUtM1dMUnVRbnBybWxCSWJ0YU02QVczWERwbDlNQzJSeThHVnRNUmEtd3dOQzRUQnJhT2V5WlhQczRYdVVGaUV3YVpaNUdvUkNqRDB0aWpDQW5IV0xtbF8zQjdGNm9xYlllMDRSYTZTLXNHMTJGLUNXYXhCMGx2R2drclQ5amZocWJndlE?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxPaEZpWkxwNlN4U1d1UmxzMEVHWWJxOVYtSkhRYUdhekpOVjJuaTVsd1MwMDRNalhrRXhhbTJtMkdCd3J0SWplcEVjSHgtbFVKUGU2bmh3c00tN0d6Vmk3Nmk5bGJuQ1FkVzZWb3dnMURsUVJnQ1hRQTMwMnZmOWs3WXZYZkZ1Tm1mNkJxXzE2ekU3UXlKdnJfQjQ0ME5VRVFGTjdySVhQczk?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxPSGUzZzN3eG1yME1RSXRweXlLR3NxLTlqcVYzSDFDd19fN2tJQUdIaWlYNXYyTXVxc1dkSnlvVlFyaVBpcW01a1piYl83SkJuMVVKTWM1RGZ2STVQck9LRVZFNlA5Ykd4XzY1RmVkWGx4dW5FZ3lPeWE1Q1NuY01lZGplUEwtS0RLLXdPbE1Xbw?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPNjVIWGhXeEl0aF9saUJhMWk3Y3E1VXN4X3dxaElKdk1tUkd6ZjA3NVNrOGd6UDI2UDhnS1NmcDV3QnJYZXFmOXlQS2pJbk9QYXlvWEhpTS1lREk0MzluTzV1QkJReGFUOWw3NEVkQUYtbVFkNWhXYVZ1WEZ5aXgxek0yeFBBT1BSWi1IaDJQVFJiOW1kS1ZpM3I2Q2U?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNb3g4SklKVjFSZmppYlVTU2dyd2ZpWkVnaWNmdUw0TE5haW05S1lxWlpZYlJJR3RjT0JBbUp2TkMxTURuVjJrZDBwcUx2Mi05SW9EcjBEaUhfMDE1Sm85ZDM1T3N2VU00VEFJbXo0ZmtPd1M0UXZEOVJocWhXUnAzaGxwZFZHUU5hTEtoU2wwVEFIQTNDbzYyc1NHUjFZeEV0OEE?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxPWDJUeGR3dEw0Z2lqQ2VIaXN2UG9rZjdWbjdub3Nqa1NHei1qWU5ZWC1zUkRQTFQwSncwZEMzTlZjcVFxRjZ0ZGg0TEozRS1YVDVULTN6Zmo5S0dIQW1YNGtzN0ZPX1ZyeGhhamlRWFlqczJGWmFSZVgzQU5EUkFGbElFMVZIbzBVUXV2RlF3N0t6c0paeWJ5UlROSGJsTUY0Q1QzUUFBb3AyT2I3djRnazdqZ0VOV2dPTGVfbmo0RDBxTVFxb2FneVFZUDROUQ?oc=5
- https://news.google.com/rss/articles/CBMi4gFBVV95cUxNdlk5ZDQyTU43VDFLV01oUEFrWWpVSWRINV9tZUhibGgtRlllbzdjOE9fVWlHNGc5TjYyTlRjUkdoMllrRG81c01UNDJZUUtkb09vSHQ1N1I5dFU1YzlwZm8zZm1LVGhGc0pFYVRjMEUxQmZ0S0JSeXp6RDJDTWF2SHY5SkRRUWMzS204dVRvUFE5N3NyenV3UlRmd0JIejBmTl95S2RISUV2VHpCSDN1SG90Q2hCa3pRWjhkaDN5RDYzVkR3bU5mdFNSN01QS2d4V2FzeUNJZUVHdzNMZk82Y1VR?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
