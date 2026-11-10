# BRK-B Intelligence Report

- ticker: **BRK-B**
- Report as_of: **2026-11-09**
- Market data as_of: **2026-11-09**
- Quant sources: https://finance.yahoo.com/quote/BRK-B/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/BRK-B/key-statistics/
- AI analysis snapshot as_of: **2026-11-09**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-10T05:59:55.853876+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 8, 'ai': 12, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261109T043242Z-c8e908de/BRK-B** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'negative_sentiment_in_tailwinds': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 19 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 20.0%; oldest publication 2026-11-07

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 575.2500 |
| Return 1D (%) | 0.7637 |
| Return 1W (%) | 3.4418 |
| Return 1M (%) | 11.5647 |
| Return YTD (%) | 14.4435 |
| Return 1Y (%) | 15.2667 |
| Annualized volatility (%) | 15.1469 |
| Beta vs SPY | 0.0564 |
| Max drawdown (%) | -9.4218 |
| Sharpe (rf=0) | 1.0490 |
| Downside deviation (rf=0, %) | 10.0955 |
| Sortino (rf=0) | 1.5740 |
| Historical VaR 95% (1D, %) | 1.4125 |
| Historical ES 95% (1D, %) | 2.0016 |
| Correlation vs SPY | 0.0509 |
| Tracking error vs SPY (%) | 19.8938 |
| P/E (trailing) | 16.10 |
| P/B | 0.00 |
| EV/EBITDA | -2.04 |
| Revenue growth (%) | 11.20 |
| Forward P/E (estimate) | 25.60 |
| Gross margin (%) | 26.60 |
| Operating margin (%) | 26.05 |
| Return on equity (%) | 10.57 |
| Free cash flow yield (%) | 4.62 |
| MA50 | 522.9654 |
| Close vs MA50 (%) | 9.9977 |
| MA200 | 498.2043 |
| Close vs MA200 (%) | 15.4647 |
| RSI (14, Wilder) | 75.2586 |
| MACD (12,26) | 14.7675 |
| MACD signal (9) | 12.0985 |
| MACD histogram | 2.6690 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'BRK-B': 278, 'SPY': 278}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 575.2500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.7637 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 3.4418 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 11.5647 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 14.4435 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 15.2667 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 15.1469 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 10.0955 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.5740 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.4125 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.0016 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0509 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 19.8938 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.0564 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -9.4218 -> Shallow peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.0490 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 25.6009 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 26.6020 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 26.0550 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 10.5740 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.6232 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 16.0999 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 75.2586 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 2.6690 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 9.9977 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 15.4647 -> Clearly above the moving-average trend level.

## TAILWINDS

### Berkshire shares surge as Wall Street swoons amid AI fears
- Summary: Berkshire shares surge as Wall Street swoons amid AI fears
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPQXgyQmpJT1lzSWhTZ01uZWJoRngzWm44N2hQT2lRcUNLWVZONlZQa3lHOTN0VE1zNEZvSjNzUEk4aThrNk1DbTZpazdtTm43TmJUYWNwYWlnTDJocHM3T3BybUpWSlM1ZElKTExkRTBoQy1NVy1zZDRCWHNPZDJFcXJReDR2OF81MkxPS282anN1UzRlUzNBb0tWTQ?oc=5>

### Warren Buffett’s Successor Is Doubling Down on Berkshire Hathaway Stock. You Probably Shouldn’t
- Summary: Company’s successor buying more shares, a bullish move but cautioned by headline.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxPUTVUZVZydnZ2U240TUxLcW9CbVdQV0kxWEkwdzNLNExLeXNrUTg0cFhWYzdTbzd5c3ozWEZJQkdCWGo3U0dXNjFUNTNuRk5qUVBXUzFZWG4yVXdKN0JIbEJFS085eW9mWGZLaTBvTUszNVdUWEJabUFkQVdMVFZ3WkhzbDJRRW5mRVJnLVFkazRyd0ZpdWRsSm9VVU8wVUQzNWVDQ3lRa3F5VUtYZ2R1dnN0aEJsdkhLZjBWMFZiSmFIbE96blM5aUtfTEUxS1V5enc?oc=5>

### Warren Buffett's Rule for Stock Buybacks Is Very Specific. Berkshire Spent a Record $9.6 Billion on Them Last Quarter.
- Summary: Record $9.6B buyback last quarter signals strong capital allocation.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNZ2x4aFRuSTUzYXFaQTc5S3E3N2xiRm9ZU0Npb3Q2RmFYN21JcUxfQld6MUZ0OUQ5ZkNtMzY5MDNXM2FQV0VwSlBWX0NDdi1uemdhdWFzcWVMSF9tUzhmSFA2Yl8xUWVtcUR4X0NrV090V2dTWE9MbjBCZ3VFY1NpOUVpSWNzSTRGTHpZNjVXZ1FqQ1JjU3I1alczTGpBZkswNnc?oc=5>

## HEADWINDS

### Berkshire Hathaway Earnings: Cash Levels Retreat Again as Acquisitions and Share Buybacks Pick Up
- Summary: Berkshire Hathaway Earnings: Cash Levels Retreat Again as Acquisitions and Share Buybacks Pick Up
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxNU3k5QnhncjJEWEVxWGlGZm9DRnBxTGRBQ29fZHBfV3VrRnVkWEs5bzFSZnZhcURvdzBHVmdiOG5zOGJSdjZRMzVpZGQtY1RKRVBTS0dsa2ZmYWliSEIzUHctdEEtVVo1MHZNU2NsMzFaTHZ5eWxNQ0JWZnp0SWNwQjNIM2IxUmFrX0hvSFBmRzdkOUJ0UFBsUF9HbjlqamcxNDF0T2huUldUSndCQ0I2S2ZQLXdvbU1QTGFNSWZuazdWQQ?oc=5>

### Berkshire Hathaway speeds up stock buybacks, though profit falls
- Summary: Berkshire Hathaway speeds up stock buybacks, though profit falls
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxPa29SbTRWcFpWdFpiekRVRjRvNmZjM1BnNzhOeVY3ajB5S25PaGgxVFAyTTItcjRDZkRmcHROSkJIZ3lNdXZkaGp0R2hOZE51eHBzR1U3MXlFRXhGOUhzV1pJR0I2RWtUZnRrQU1MVXZaSm1haDUtTHo3NEJvNGJhLU1rM2N4a240NWp2VFh5Vkd5LW1DOTd6emN0S1QyengzS1ZjdE04LVluRGppX19oSkxtVktEcDdoWXVIVk93?oc=5>

### Berkshire Hathaway (BRK.B) Q3 Earnings: Revenue Beats, but Profits Fall 28%
- Summary: Berkshire Hathaway (BRK.B) Q3 Earnings: Revenue Beats, but Profits Fall 28%
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNQWV5Uk0tX0J5bG1mMVB5cVpEVVFlWHVrNG9LUE1pT3lQbDIyR3J1aU9YMVJLVjRPOXJ1VWpXaHFOcUJOQU9PenVMN3cxMWFwclU0ZDMyeGNoaVJDTldZSzNZa1VtUFFON2lXRHRpSGRBdThPUTR2ZW1iODBaWDZmQzgtRExpSlVERVJXNmlKd0RZNzBJci0ydzNFM09mV0FqWWc?oc=5>

### Why Is Berkshire Hathaway Stock Trading Lower Monday?
- Summary: Stock price decline indicates market pressure.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxNRVdFQkxVZDB4a3N3NkdiWWtxMGxWeVdzMDU3VnRTLU9zRmhWSG13NmJOSWs4RUZxQXVhWGpNeHNDam5aOFdrSS1yblNJSnREWHQxdzVTeFpRVmV1aGRwb3EwRS1CWXJJNG9rT2JUX3JsbURFNmoyZDQ1ZlB2U19pNzBKWGNCVVVaNkk4RzM3WFBvbGRBMUp0SWJTbXZzNklPck05ODFrZ29BeGFZNnc?oc=5>

### Berkshire Hathaway’s Operating Earnings Fall, Buybacks Rise
- Summary: Operating earnings decline despite rising buybacks.
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxOc2ZtOW9LNl81SlBjQ3dkekluZDI1WmhWV1Znckw0MGlnWUF6WWF4cjd5MFlVTWQ4MTRjc1lWbWRrSzZ5RkY5SnIzQUpKcGZ4Y09rOGxqQ2FNNzRwaE90aExSOENLa2dGd1BrY2xKYVRwNW9nV2Rtckx2LTJlaGNrME5nT3JYVlo4cmNRaXVoZ0RnVGFnZnpDWXVGOUVodWtpWTQ5WEN1eXBtdEZuOUE?oc=5>

### Warren Buffett’s Berkshire Rose 5% in the Market’s Worst Week Since April 2025
- Summary: Stock fell 5% during market worst week.
- Date: 2026-11-07 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxQR2gtQ0swRGJjaU5OTDIyM2pXN3J1b1g1MFpfNXg2TFNFTkliZi1TdzBmZGxFS0VJUzN2Q0Q3Szc2MHJBdm1EUFBhSXBOcjhvWml0QmpQekZqTnluak9nSGozZWZncXZCVmxSYnE3VHJ0ZEFhOXFzck1jVm5nbjBtRU50VldUd2VHODJzQ1NManJUZUp3RXlsUUdnQkJ1RTFxWVNGNWdmWFZlQ2EwYVNUX05sdjBnYi1JRU80?oc=5>

### BRK.B Q3 Earnings Decline Year Over Year, Revenues Top Estimates
- Summary: Q3 earnings down YoY, revenues beat estimates.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPV1MxNnk5dVFqOExmUlBLNWhFS04zU1VQZHAwSWpyckJEQUgxdmFjSWJuQlBYbS1RcnJuSVlZejREcGtuR3ZacFlRSmEwOXFrdWlBTFlXRGRCRkhBRV9oWU5rRV9MOVMyZ0lfRXdyX25lR3ctSWdYVnM0dnIzMnlXVXJkMXVBUktpQW5OOVVWaEZkVDAw?oc=5>

### Berkshire Hathaway: This Isn't Going In The Right Direction (NYSE:BRK.A)
- Summary: Negative outlook on Berkshire’s performance.
- Date: 2026-11-09 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOZkRQbUtwVUlGV045NGRiMG45eTJ1NFlSMzROUHM2ZDhvalhuS2lmR2dCRWtuSkIxT3VSVHcybUwyMGR5Z0JMMmJQVUxEWU9rYVVIa1VnUUtPSUxJRldpSG1vU0RXS2YxMElVemJXVHJHaUxnd2EyNkNJelFpdV9Qd1J3WDhlYVh0T0Fmd1lzR1hqbzZjMkZpYmFSSUpHZW8?oc=5>

## CATALYSTS

### Berkshire Hathaway latest: Q3 earnings, top 5 holdings, record stock buyback, & more
- Summary: Berkshire Hathaway latest: Q3 earnings, top 5 holdings, record stock buyback, & more
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxQZ2loVTdsMFF4Z2F5WWdnOHprakxBVGlGcUJ1YWkxNm1uOFltRmNDbU9ISWsySWplc296c1lWWU5DUzBITEN3Zm1xT1pHR1pDQUhUemhGdEdTcVFXdlNCeTRNVDFxeTQ3b1BpbV9SdnQyRjM4S3M2cjBaTE1xRnhXLXlVRzh6Mmd1dkY0LXFGRXotWnhvdjZIeXBaZTE0WnY5MDUtUkVWYWNXa2xvQ2hiMUVmZHFJT054QTB1Z3JDbzR3cDdP?oc=5>

### Berkshire Hathaway buys back $9.6 billion of its own stock but its profits declined - ABC News
- Summary: Berkshire Hathaway buys back $9.6 billion of its own stock but its profits declined - ABC News
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNVDRseVNGNHdzbmNUUkpNSGtnM3V2dDh0RHFIdEJwT3FBclN5aU5qMUZXT1ljLTdfZmp3MFg0eUJfN3lkUWRoaXVIQWlFeTUwR202Qnd3cm9xZ0tsRGwwTTVNdE1zOGs1dGVxTW5SelhCRFk3bjNtajRxTXpURm51c3pKdlQ5a0lRZ1NnaG43dUZiazRkNDVZcEl1X0V0WDgwSXlhOdIBqgFBVV95cUxQNFMtU05xOWM4WVdIY1ZOalJqN1ZnREF2SVBWekVOOUFkZzZPMjlLQy00RWhJei0xS2R2MjIxcTQxMzlSejk0eklLTzVmYmYxT01uY1FfV0d5RzVHd21mU2VpU2lNeUdkaTZZcDI1N3JMMzktTTh1cUdnRlF4djk1Ulp1UVBzMHA4bE92OXNVZWlCVS1tNEJTak5hWkQ1REZITEtqNGw5a3h4dw?oc=5>

### Berkshire Hathaway earnings expose unexpected problem beneath strong economy
- Summary: Berkshire Hathaway earnings expose unexpected problem beneath strong economy
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxPR2NfZzl0UUlGcm1GSHZ3M1dOeldXYmFDdU84MDB6SHQxVXZUMklXRWpCV1FzSThuTDNZWElEQmlqSDdDandIR0ZwOE5wN0JtNkctc0lob19NbzBnTHEtYWV5ektaV240bEdqeDd2SnJTMkpod0ZZblNLSDd5OTRGbVJKNVhzR28?oc=5>

### Berkshire Hathaway Q3 Earnings Miss On Insurance, Not On Strategy
- Summary: Berkshire Hathaway Q3 Earnings Miss On Insurance, Not On Strategy
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxObUlKZVllVlVCdXlfa2VfbnY5a2ljTHI0ZV9QakR1aUExeGNzczkzZDdOamxKQm9DZW5mTnhUd0N0MnRtRGZybDlzNUJwUnNYaWY0MDV2aVFtOWk2dDRaS3IzVFBqemtna1lVbVVtYVE0bkw1bWJEeFVxbGhkNTN2SkFOOU5NU01iWWRBb1RDS1FwYUlXV1VYc2E1bnJwOHViZWNFcXZLd3pPbFVBQlJEcFZ0bFFxQTQ?oc=5>

### Berkshire Hathaway’s Quarterly Profit Falls After Investment Gains Shrink
- Summary: Berkshire Hathaway reports a decline in quarterly profit due to reduced investment gains.
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQSlRmcnB2bWtXOHV1MEJucmRMSFpiMjUtM1dMUnVRbnBybWxCSWJ0YU02QVczWERwbDlNQzJSeThHVnRNUmEtd3dOQzRUQnJhT2V5WlhQczRYdVVGaUV3YVpaNUdvUkNqRDB0aWpDQW5IV0xtbF8zQjdGNm9xYlllMDRSYTZTLXNHMTJGLUNXYXhCMGx2R2drclQ5amZocWJndlE?oc=5>

### The biggest takeaway from Berkshire Hathaway’s latest quarter isn’t the $357 billion cash or its stock buybacks
- Summary: Quarter results highlight factors beyond cash and buybacks.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi5gFBVV95cUxNOURBSlE3MGE0bFVPWWU3b0Z3dlpUaVQ0WG9JZGJQdDBnWXozSjcxUjhlaTJTOFNsOUt5dTBBOElEX3RMUHZaa0N3ei1rNTVsR242MDFaTGxZaWNZanMyNjNlbng1b2syTUpBYXEzUHVmTFo4RXZHVWt2UlByTHJtSGw1cENlSUJaem84UzE3Tk5SUGJoOVEtdGJOYl9xM0hyVHFtSkRrVDhSUTNPVXZSbFM1ZTl2YXUyYndWTzdvQkIydWQyVGN2YjVKZHYyMV9PNGlRcWozQ3V6cUtYLW5tbUVScjVvdw?oc=5>

### US Stock Futures Mixed as Investors Assess Berkshire Hathaway Earnings, Nvidia Reports and AI Regulation Plans: Dow Jones, S&P, Nasdaq, Wall Street
- Summary: Investors evaluating Berkshire earnings amid market mix.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNMVh6MTZGNjR5STJGM05veFRUWEppT1d4X0U4RFhwR1RfTFA2UFhXZVhRdEw5OUJocGQ1emFZanhXbDVuREwtcjV0d2NjbXplNW5rajVCMzJXbnMtenRvaTU5YUVoVWJNX0hkb29ydDhGU0tWdDlfZWNTaEFMOGs1ODEwSWZCRm8wdXhlbTZCbUEtc2tlRERYa1drejQzZw?oc=5>

## RISKS

### Warren Buffett and Greg Abel Just Sent Shockwaves Through Wall Street With This $377 Billion Warning
- Summary: Buffett and Abel issue warning that could trigger market volatility.
- Date: 2026-11-08 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxPWDJUeGR3dEw0Z2lqQ2VIaXN2UG9rZjdWbjdub3Nqa1NHei1qWU5ZWC1zUkRQTFQwSncwZEMzTlZjcVFxRjZ0ZGg0TEozRS1YVDVULTN6Zmo5S0dIQW1YNGtzN0ZPX1ZyeGhhamlRWFlqczJGWmFSZVgzQU5EUkFGbElFMVZIbzBVUXV2RlF3N0t6c0paeWJ5UlROSGJsTUY0Q1QzUUFBb3AyT2I3djRnazdqZ0VOV2dPTGVfbmo0RDBxTVFxb2FneVFZUDROUQ?oc=5>

### Berkshire Hathaway: The Margin Of Safety Has Evaporated (Rating Downgrade) (NYSE:BRK.A)
- Summary: Credit rating downgrade signals increased risk.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxPVG5Zd21HMzR5TWpzbzFac1RSOTJzQWRWTzZqSTNYVUZBMzFuWW9TeHNQTzBXZDlOamdnYjB1VlNNdXJMd29sRnpVZFEybjZWZXJfUHBhTlJ0bFhueE83UEstTFRiTWk1am9MZXNvbWd1UTI2b2t0MzU5OW9pRlJ2WmtJN2FkeG1vc1Q4Rzc0dFdhRTZQSzU3NEZzaXdSd3BOMGNtOGh5aVdOQXV3UmFpMm5B?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **BRK-B** | **16.10** | **0.00** | **-2.04** | **11.20** | **1,231,443,329,024.00 USD** | **15.27** |
| MKL | 13.89 | 1.29 | 7.98 | -11.20 | 23,862,671,360.00 USD | -4.22 |
| FFH.TO | 10.11 | 1.43 | 8.75 | 1.90 | 56,136,220,672.00 CAD | 23.40 |
| L | 15.21 | 1.22 | 8.63 | 1.90 | 22,232,641,536.00 USD | 7.41 |

Peers fetched as_of: 2026-11-09; BRK-B reuses existing data (market data as_of: 2026-11-09); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-07
- Next expected earnings: 2027-03-01 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-09

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMimwFBVV95cUxPQXgyQmpJT1lzSWhTZ01uZWJoRngzWm44N2hQT2lRcUNLWVZONlZQa3lHOTN0VE1zNEZvSjNzUEk4aThrNk1DbTZpazdtTm43TmJUYWNwYWlnTDJocHM3T3BybUpWSlM1ZElKTExkRTBoQy1NVy1zZDRCWHNPZDJFcXJReDR2OF81MkxPS282anN1UzRlUzNBb0tWTQ?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxPUTVUZVZydnZ2U240TUxLcW9CbVdQV0kxWEkwdzNLNExLeXNrUTg0cFhWYzdTbzd5c3ozWEZJQkdCWGo3U0dXNjFUNTNuRk5qUVBXUzFZWG4yVXdKN0JIbEJFS085eW9mWGZLaTBvTUszNVdUWEJabUFkQVdMVFZ3WkhzbDJRRW5mRVJnLVFkazRyd0ZpdWRsSm9VVU8wVUQzNWVDQ3lRa3F5VUtYZ2R1dnN0aEJsdkhLZjBWMFZiSmFIbE96blM5aUtfTEUxS1V5enc?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNZ2x4aFRuSTUzYXFaQTc5S3E3N2xiRm9ZU0Npb3Q2RmFYN21JcUxfQld6MUZ0OUQ5ZkNtMzY5MDNXM2FQV0VwSlBWX0NDdi1uemdhdWFzcWVMSF9tUzhmSFA2Yl8xUWVtcUR4X0NrV090V2dTWE9MbjBCZ3VFY1NpOUVpSWNzSTRGTHpZNjVXZ1FqQ1JjU3I1alczTGpBZkswNnc?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxNU3k5QnhncjJEWEVxWGlGZm9DRnBxTGRBQ29fZHBfV3VrRnVkWEs5bzFSZnZhcURvdzBHVmdiOG5zOGJSdjZRMzVpZGQtY1RKRVBTS0dsa2ZmYWliSEIzUHctdEEtVVo1MHZNU2NsMzFaTHZ5eWxNQ0JWZnp0SWNwQjNIM2IxUmFrX0hvSFBmRzdkOUJ0UFBsUF9HbjlqamcxNDF0T2huUldUSndCQ0I2S2ZQLXdvbU1QTGFNSWZuazdWQQ?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxPa29SbTRWcFpWdFpiekRVRjRvNmZjM1BnNzhOeVY3ajB5S25PaGgxVFAyTTItcjRDZkRmcHROSkJIZ3lNdXZkaGp0R2hOZE51eHBzR1U3MXlFRXhGOUhzV1pJR0I2RWtUZnRrQU1MVXZaSm1haDUtTHo3NEJvNGJhLU1rM2N4a240NWp2VFh5Vkd5LW1DOTd6emN0S1QyengzS1ZjdE04LVluRGppX19oSkxtVktEcDdoWXVIVk93?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNQWV5Uk0tX0J5bG1mMVB5cVpEVVFlWHVrNG9LUE1pT3lQbDIyR3J1aU9YMVJLVjRPOXJ1VWpXaHFOcUJOQU9PenVMN3cxMWFwclU0ZDMyeGNoaVJDTldZSzNZa1VtUFFON2lXRHRpSGRBdThPUTR2ZW1iODBaWDZmQzgtRExpSlVERVJXNmlKd0RZNzBJci0ydzNFM09mV0FqWWc?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxNRVdFQkxVZDB4a3N3NkdiWWtxMGxWeVdzMDU3VnRTLU9zRmhWSG13NmJOSWs4RUZxQXVhWGpNeHNDam5aOFdrSS1yblNJSnREWHQxdzVTeFpRVmV1aGRwb3EwRS1CWXJJNG9rT2JUX3JsbURFNmoyZDQ1ZlB2U19pNzBKWGNCVVVaNkk4RzM3WFBvbGRBMUp0SWJTbXZzNklPck05ODFrZ29BeGFZNnc?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxOc2ZtOW9LNl81SlBjQ3dkekluZDI1WmhWV1Znckw0MGlnWUF6WWF4cjd5MFlVTWQ4MTRjc1lWbWRrSzZ5RkY5SnIzQUpKcGZ4Y09rOGxqQ2FNNzRwaE90aExSOENLa2dGd1BrY2xKYVRwNW9nV2Rtckx2LTJlaGNrME5nT3JYVlo4cmNRaXVoZ0RnVGFnZnpDWXVGOUVodWtpWTQ5WEN1eXBtdEZuOUE?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxQR2gtQ0swRGJjaU5OTDIyM2pXN3J1b1g1MFpfNXg2TFNFTkliZi1TdzBmZGxFS0VJUzN2Q0Q3Szc2MHJBdm1EUFBhSXBOcjhvWml0QmpQekZqTnluak9nSGozZWZncXZCVmxSYnE3VHJ0ZEFhOXFzck1jVm5nbjBtRU50VldUd2VHODJzQ1NManJUZUp3RXlsUUdnQkJ1RTFxWVNGNWdmWFZlQ2EwYVNUX05sdjBnYi1JRU80?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPV1MxNnk5dVFqOExmUlBLNWhFS04zU1VQZHAwSWpyckJEQUgxdmFjSWJuQlBYbS1RcnJuSVlZejREcGtuR3ZacFlRSmEwOXFrdWlBTFlXRGRCRkhBRV9oWU5rRV9MOVMyZ0lfRXdyX25lR3ctSWdYVnM0dnIzMnlXVXJkMXVBUktpQW5OOVVWaEZkVDAw?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOZkRQbUtwVUlGV045NGRiMG45eTJ1NFlSMzROUHM2ZDhvalhuS2lmR2dCRWtuSkIxT3VSVHcybUwyMGR5Z0JMMmJQVUxEWU9rYVVIa1VnUUtPSUxJRldpSG1vU0RXS2YxMElVemJXVHJHaUxnd2EyNkNJelFpdV9Qd1J3WDhlYVh0T0Fmd1lzR1hqbzZjMkZpYmFSSUpHZW8?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxQZ2loVTdsMFF4Z2F5WWdnOHprakxBVGlGcUJ1YWkxNm1uOFltRmNDbU9ISWsySWplc296c1lWWU5DUzBITEN3Zm1xT1pHR1pDQUhUemhGdEdTcVFXdlNCeTRNVDFxeTQ3b1BpbV9SdnQyRjM4S3M2cjBaTE1xRnhXLXlVRzh6Mmd1dkY0LXFGRXotWnhvdjZIeXBaZTE0WnY5MDUtUkVWYWNXa2xvQ2hiMUVmZHFJT054QTB1Z3JDbzR3cDdP?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNVDRseVNGNHdzbmNUUkpNSGtnM3V2dDh0RHFIdEJwT3FBclN5aU5qMUZXT1ljLTdfZmp3MFg0eUJfN3lkUWRoaXVIQWlFeTUwR202Qnd3cm9xZ0tsRGwwTTVNdE1zOGs1dGVxTW5SelhCRFk3bjNtajRxTXpURm51c3pKdlQ5a0lRZ1NnaG43dUZiazRkNDVZcEl1X0V0WDgwSXlhOdIBqgFBVV95cUxQNFMtU05xOWM4WVdIY1ZOalJqN1ZnREF2SVBWekVOOUFkZzZPMjlLQy00RWhJei0xS2R2MjIxcTQxMzlSejk0eklLTzVmYmYxT01uY1FfV0d5RzVHd21mU2VpU2lNeUdkaTZZcDI1N3JMMzktTTh1cUdnRlF4djk1Ulp1UVBzMHA4bE92OXNVZWlCVS1tNEJTak5hWkQ1REZITEtqNGw5a3h4dw?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxPR2NfZzl0UUlGcm1GSHZ3M1dOeldXYmFDdU84MDB6SHQxVXZUMklXRWpCV1FzSThuTDNZWElEQmlqSDdDandIR0ZwOE5wN0JtNkctc0lob19NbzBnTHEtYWV5ektaV240bEdqeDd2SnJTMkpod0ZZblNLSDd5OTRGbVJKNVhzR28?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxObUlKZVllVlVCdXlfa2VfbnY5a2ljTHI0ZV9QakR1aUExeGNzczkzZDdOamxKQm9DZW5mTnhUd0N0MnRtRGZybDlzNUJwUnNYaWY0MDV2aVFtOWk2dDRaS3IzVFBqemtna1lVbVVtYVE0bkw1bWJEeFVxbGhkNTN2SkFOOU5NU01iWWRBb1RDS1FwYUlXV1VYc2E1bnJwOHViZWNFcXZLd3pPbFVBQlJEcFZ0bFFxQTQ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQSlRmcnB2bWtXOHV1MEJucmRMSFpiMjUtM1dMUnVRbnBybWxCSWJ0YU02QVczWERwbDlNQzJSeThHVnRNUmEtd3dOQzRUQnJhT2V5WlhQczRYdVVGaUV3YVpaNUdvUkNqRDB0aWpDQW5IV0xtbF8zQjdGNm9xYlllMDRSYTZTLXNHMTJGLUNXYXhCMGx2R2drclQ5amZocWJndlE?oc=5
- https://news.google.com/rss/articles/CBMi5gFBVV95cUxNOURBSlE3MGE0bFVPWWU3b0Z3dlpUaVQ0WG9JZGJQdDBnWXozSjcxUjhlaTJTOFNsOUt5dTBBOElEX3RMUHZaa0N3ei1rNTVsR242MDFaTGxZaWNZanMyNjNlbng1b2syTUpBYXEzUHVmTFo4RXZHVWt2UlByTHJtSGw1cENlSUJaem84UzE3Tk5SUGJoOVEtdGJOYl9xM0hyVHFtSkRrVDhSUTNPVXZSbFM1ZTl2YXUyYndWTzdvQkIydWQyVGN2YjVKZHYyMV9PNGlRcWozQ3V6cUtYLW5tbUVScjVvdw?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxNMVh6MTZGNjR5STJGM05veFRUWEppT1d4X0U4RFhwR1RfTFA2UFhXZVhRdEw5OUJocGQ1emFZanhXbDVuREwtcjV0d2NjbXplNW5rajVCMzJXbnMtenRvaTU5YUVoVWJNX0hkb29ydDhGU0tWdDlfZWNTaEFMOGs1ODEwSWZCRm8wdXhlbTZCbUEtc2tlRERYa1drejQzZw?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxPWDJUeGR3dEw0Z2lqQ2VIaXN2UG9rZjdWbjdub3Nqa1NHei1qWU5ZWC1zUkRQTFQwSncwZEMzTlZjcVFxRjZ0ZGg0TEozRS1YVDVULTN6Zmo5S0dIQW1YNGtzN0ZPX1ZyeGhhamlRWFlqczJGWmFSZVgzQU5EUkFGbElFMVZIbzBVUXV2RlF3N0t6c0paeWJ5UlROSGJsTUY0Q1QzUUFBb3AyT2I3djRnazdqZ0VOV2dPTGVfbmo0RDBxTVFxb2FneVFZUDROUQ?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxPVG5Zd21HMzR5TWpzbzFac1RSOTJzQWRWTzZqSTNYVUZBMzFuWW9TeHNQTzBXZDlOamdnYjB1VlNNdXJMd29sRnpVZFEybjZWZXJfUHBhTlJ0bFhueE83UEstTFRiTWk1am9MZXNvbWd1UTI2b2t0MzU5OW9pRlJ2WmtJN2FkeG1vc1Q4Rzc0dFdhRTZQSzU3NEZzaXdSd3BOMGNtOGh5aVdOQXV3UmFpMm5B?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
