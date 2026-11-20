# NVDA Intelligence Report

- ticker: **NVDA**
- Report as_of: **2026-11-19**
- Market data as_of: **2026-11-19**
- Quant sources: https://finance.yahoo.com/quote/NVDA/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVDA/key-statistics/
- AI analysis snapshot as_of: **2026-11-19**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-20T05:47:48.784804+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 5, 'ai': 12, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261118T054934Z-e0d070d9/NVDA** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 1, 'positive_sentiment_in_headwinds': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 14 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 36.0%; oldest publication 2026-11-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 145.9800 |
| Return 1D (%) | -3.2989 |
| Return 1W (%) | -12.1608 |
| Return 1M (%) | -32.7560 |
| Return YTD (%) | -21.5434 |
| Return 1Y (%) | -21.5474 |
| Annualized volatility (%) | 38.8298 |
| Beta vs SPY | 1.7658 |
| Max drawdown (%) | -38.9818 |
| Sharpe (rf=0) | -0.4334 |
| Downside deviation (rf=0, %) | 28.1885 |
| Sortino (rf=0) | -0.5971 |
| Historical VaR 95% (1D, %) | 4.1932 |
| Historical ES 95% (1D, %) | 5.1243 |
| Correlation vs SPY | 0.6321 |
| Tracking error vs SPY (%) | 31.9168 |
| P/E (trailing) | 16.22 |
| P/B | 13.20 |
| EV/EBITDA | 14.22 |
| Revenue growth (%) | 103.20 |
| Forward P/E (estimate) | 8.79 |
| Gross margin (%) | 74.92 |
| Operating margin (%) | 66.08 |
| Return on equity (%) | 117.36 |
| Free cash flow yield (%) | 2.82 |
| MA50 | 208.8556 |
| Close vs MA50 (%) | -30.1048 |
| MA200 | 203.3151 |
| Close vs MA200 (%) | -28.2001 |
| RSI (14, Wilder) | 19.6448 |
| MACD (12,26) | -17.7572 |
| MACD signal (9) | -14.0405 |
| MACD histogram | -3.7168 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVDA': 286, 'SPY': 286}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 145.9800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -3.2989 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -12.1608 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -32.7560 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -21.5434 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -21.5474 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 38.8298 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 28.1885 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.5971 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.1932 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1243 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6321 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.9168 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.7658 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -38.9818 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.4334 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 8.7912 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.9210 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 66.0820 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 117.3640 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.8154 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 16.2200 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 19.6448 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.7168 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -30.1048 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -28.2001 -> Clearly below the moving-average trend level.

## TAILWINDS

### Nvidia stock erases earnings pop as investors face life after Jensen Huang
- Summary: Nvidia stock erases earnings pop as investors face life after Jensen Huang
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxQUzhvYkxzRld1VG11TlpOSE5wWjE5WE94RkMwVkJJWnRReDFRTUZ1X1FQWU55Rnh5b1hqU0VvTzBCay10WE5iVzJYWHdtVWJ0dlU5aFhhX2Yxa09Ub0otUkVUQ0hCTC1OUHBhRTU5UDBlRVZfNEx4cUtoVXRRanEwazFaQTBwYmpBREc2MVlsaVlDNWptenNNZkpDNzd2blFtS3pJX0oxWDl2RlcyMFNucDRILTRlRF9iUWFPRTA3VFo5NGRVZUJTaDkyTmpYcF9xcGJtMw?oc=5>

### Is Nvidia Stock a Once-in-a-Decade Buying Opportunity After Its Latest Earnings?
- Summary: Analysis of post-earnings buying potential for NVDA.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxOSWE3SDhVLURnMWI2MzhzdHlPX1pYcTlDeURlYTNNbkZ2X2E5dS1qb3dtNFh6bUdFSlpDWGkyY0djeW04SVBDQjZJeWZlN2R0N2ZiNXZ2OEFQZlZpMk10ZzU0d0pxTHl2eDlIVGcwazYzcUJSWHk2YktyWGdTVFZ3UVNsaXdXT1pTalY0blc3aURQQklUY0NtZV9aRTNfWWdyelRycW00Zl84QTJhTmppTHhteU9RQUlHTmFXdUxkbw?oc=5>

## HEADWINDS

### NVDA Stock Alert: What to Know as Moody's Cuts Nvidia's Outlook Rating
- Summary: NVDA Stock Alert: What to Know as Moody's Cuts Nvidia's Outlook Rating
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxQQmI0cjQ4cUVpYjVTeXNuNFdNRmE4bHFJTDBsbDBNLS1LZGEzeFhsUVRvYzltRjA0YUU4RnYzS1htMkNHTDRDcHdfQXk4QjdRYloyQVRJWGtlLXhHNmJiMmVQMVhJNTduQXNZdld6ald5SmN0bUVHWUJpbmRBR2RIN2tVdEI2cG9hcXNMeExDd1JWNFBtS0JLQlkzWERheDhVSWZVZ3Z1RUNsc21zRjVQNWg4cw?oc=5>

### Nvidia (NVDA) Stock Drops Despite Q3 Results Showing Huge AI Earnings
- Summary: Nvidia (NVDA) Stock Drops Despite Q3 Results Showing Huge AI Earnings
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPWHNRcEVuR1ViVWpUY0p5RnIyekVpWDRTVUFLXzhLYnFDZ2tfeGctTGFkcENyRFliRXVRSktrc3hiTU01ZW9oY1dzaVJ2dzBNcTBxLWZienhFM0I0dVFDYXp3NTVjM3lZNGhxMXpuZUhuLXdUd1o0RTN2VVR0bzRDNnE0LXByUDJvWFl3VUFra1JDQXZmbV9FejNKdEI?oc=5>

### Nvidia’s stock falls further. It has lost $669 billion in six trading days.
- Summary: Nvidia’s stock falls further. It has lost $669 billion in six trading days.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxNVEJ3VzdMRnFXV3ZlNU1Kc0NHZ0toc2w3aFRGSFF5QkFCYmRTQUVGOW9YVE52UE9nLWR4U1JSZmF0R0h6aUNjREs4VGVyZ1NaZkhOdGhzQ0ZQbEdHQTlrU1VuaEFMMDlQdE1YdVdRYTdtaVp2UWQtX3hZMjBVLXQ4Z1VuTDRabnRRTnl4Zy1GZlA5QW52cTJIcGw1SnBZZ2VmQ01GYVUxQWNzSzEzelctbkhWX2w?oc=5>

### Nvidia’s Kress tells CNBC's Jim Cramer that 'customers continue to be with us’
- Summary: Positive customer sentiment reported by Nvidia executive.
- Date: 2026-11-18 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMifEFVX3lxTE9iM3pFNTMyc0NDSXdVbjV1RFhtMjMybWRUcWtGOGRsVllWSS1Yd2Y0emU4MXNVbUpoUUUxTVZ5ck8xem1nNjVuNUl2VVFzLXNMZU1nZlRPNDJTRG9uaFhkbXpSdzNhQW9lWDZQbUtHUnRZeDBlaUl2Y3pDcErSAYIBQVVfeXFMTXV5dkdmRTlzLVlhbUdHREtUSWs2M09MRm8yYldyTkhnZllMWUdFZHh4cVo1Z0FlUmRld3ZnUmVuMV9OanU0em9oTmF2MjNoNGZ0T282eDZialBxU3g1Nkt5aFVrSzdHbmh0Y1I5aFZhRDZjQWdWX0Q3aXNVaV9DeFA2UQ?oc=5>

### Nvidia: The Worst Is Yet To Come (NASDAQ:NVDA)
- Summary: Critical outlook on Nvidia’s future prospects.
- Date: 2026-11-19 | Impact: high | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMifEFVX3lxTE5PQVk0Zkc2enRNbFBEaThQMVdVQXQ1X1pTdm11LWgwNkE0Q3BVd1Y0R0gxTnVzZjdPdUVDWEJxcDVfSk16QWJmSWFXMUpMTEJQMnh4d2N2SFpNQmRqUWJ0c0ZUMFpxRFdfS1k4UU5jXzI0Z3l1V2VoS3NvTGQ?oc=5>

### Why Is Nvidia (NVDA) Stock Falling After Record Earnings?
- Summary: Stock decline following record earnings.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTFBFOVFHRlJnRTd1eTF3aG9HVUJzLVpJZVJIand2T2dFMzk3QU5mRkhwNXU5aXdzYmREWFk1dEdvR0ZOS1pQYWNJTk5CWGM1akFQTjQxbV82U0pEQVRTZUEzbXNFUkpObTJvU2NQb28zeVBPRFZLeDg5NW1JOTVfdw?oc=5>

### QUICK SPARK: Nvidia Stock Is Bleeding Like It's 2008
- Summary: NVIDIA shares decline sharply, echoing 2008 market conditions.
- Date: 2026-11-19 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOc3RRaGlXbTlWZ1pyYW1tc0hrRXBlV0xRTjVrTGU0UDhDTUhJbEFYZTdacGtQd0ZRdjhJQ2Zqbm9Qbk1HSmVxTjFkX1NVa0MyZkZsNkhsdkIwb29mLXpZRXFqM3M3ZzJyY21obFE1MTlocnVLU2lCUlVMOVJJWmRsRVc3SC13SE1QYzZqT2pLdG5jODJzdzY0ZkhxTWw?oc=5>

## CATALYSTS

### NVIDIA Doubled Its Revenue in Its First Quarter Without Huang. Here’s Our Price Target.
- Summary: NVIDIA Doubled Its Revenue in Its First Quarter Without Huang. Here’s Our Price Target.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxNMnc5TjJWdmVlZ255ZjJOaUpXa3FzWVJYdXVrQjRoRWVxTmtpRXptS21fX3h3a3ZXMXZIQjVNYnd6N25XSURjYzlKV3JOMkE0Yk9LanRZcGZLelgxSzc3YkVOZk9UYnJCSmxuVUVqSDNpNXBIdUdvODl2VmJKdUNRR0FyM0pVbFpGYmVLbm5IUWNkbkVIb0s5MFRRdmhKWWhoQ013?oc=5>

### Nvidia’s Third-Quarter Earnings, Outlook Top Wall Street Expectations
- Summary: Nvidia reported Q3 earnings surpassing analyst expectations, with strong revenue and guidance, indicating robust performance.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxOd09QMUxzbVhUclZQOE5JTDY0VjRCUU80amJ3S0lHZnd2MERNWkthb0VHY0JpLWw5Q2xwTXM1ZlBGRERERlFVeXlxeUtTTFU1YzNuVS1UeEV1Y21TZTVrQkZidTF3N1NBOWhmZjFrTlhUNjNVSnBJVmcyRVNvQ256cTRPX091MFRGVy11bjVaTG16QWRJTjVic1VNZ3NfZnFrWmo0bVk1bW5jMWtGTXVyR3BVUlJHRzA1ZHlCZmR3?oc=5>

### Wedbush Lifts Nvidia Stock (NVDA) Price Target to $293. Here’s Why
- Summary: Wedbush raises NVDA price target to $293, citing strong growth prospects and robust earnings outlook.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPRllSN2RmXzJSQjJjQ2F5WmxTWUhGd0dETkZzRWdVMjNmc0g2NVVmdFMyOUpJd3Ffd3d4akxjdUVOYWFsT2lCeVN3ZV83YVEyNjluV0tfOUJwUllIUWVIZzBual9VWFBDZnFRZjlCc2pTS1V6Ri1zVjlITFJrU1lLcmk0YVdrc0tUMzlobEZpVEZ4TkFUVFE?oc=5>

### Nvidia earnings live: Nvidia posts Q3 beat as revenue rose 103% YOY to $115.8B, board says it will not reinstate Jensen Huang as CEO
- Summary: NVDA beats Q3 earnings expectations, revenue up 103% YoY to $115.8B; board confirms no CEO reinstatement.
- Date: 2026-11-18 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMi5gFBVV95cUxPTGswLW45X25uQXNodGZiZnNWeFk1dTdSWm5SRktfUXBTaTY3QlA2dFR3U3hFNnpDX2dwa3VHYllDS3Roa1VyWGFEMk16alc1dHRXR1p0eUVsRk1LMEliNDJyYlJIczVmam1OT25jMjRKbUZ2UE05bGtKLWUtdldySHpvOWMyRUdmenJUaFk0eTYtalRlZll0RkkzdGdzcnMwYkR1eWpKZTdqU3VRYXpLY1BSU2MwM04yMEJmbW9YOWZvZlRleUpqd3BseDhrTE5GVEFNN0FTM0hjUjdDTFBGUUQyOWVfUQ?oc=5>

### Nvidia Is Financing Its Own Demand, And The Fed Noticed (NASDAQ:NVDA)
- Summary: NVDA’s self-financing of demand attracts Fed attention, indicating significant liquidity use and market impact.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPSWY1d2ItZkhENElDOVhFeHBYYXpQcU0zdjZTbG4yV0Z2RHM1eGF5ZG5FTFo4YklUTUItMnNJZVd4b1gzMGZoeE9PRzhnZ3pwREQxYVBMVDNFRVo4bWNhcktfZUlBZkRacldEQUZRSG84eEJGM3Y0YWc0eEU2VUV3MVREMHJBWE1UaUk2d0tpaEY0SDFxZXN5bkZTVQ?oc=5>

### Nvidia Stock Can’t Shake Post-Huang Hangover. Anthropic Debut Also Not Providing a Boost.
- Summary: NVIDIA shares remain weak after CEO departure; Anthropic launch fails to lift sentiment.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxOM0V3d1ZlZG04SEFmUFJDc1lRZDRWMkZMMkVULVc2SlZqMmI2VUlfUW9sWS1UOFAydWxxdDBVZDZVU2FRODNxMUtTdGdKSnh1Z0tnOF90VDNzMThFUkk2dFE0Y0ZwenFLSWl5TFNKUDhod1pOU0VHT2lEbE0tUUtKN3hQNjk?oc=5>

### Nvidia Beat Again. Why Is The Stock Still Down?
- Summary: NVDA reported earnings beat, yet shares remain down, indicating market skepticism about future growth.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPdkFIWjA0UXlkc3l0NnBYTzNxUklMY0piNjVnZlZGMXVJYWk5cHRpcnF0OFAtYV9lY2p4dTRuMnNwNjRuSlJNOHlhcURTZk4xcm5uYnFNWkVibWd1c2R6ZUNoTmdwT19kdkxQdmw0OF9fcDV3ekNCN0xBcUQyS0c3eUFlTnRER3Y2RzdpYjBueElrR2JRTlRr?oc=5>

## RISKS

### Jensen Huang Stepped Away From Nvidia. The Stock Has Crashed. Instead of Rushing to Buy the Dip, Here Are 2 AI Stocks Down More Than 15% to Buy Instead.
- Summary: Leadership change with CEO departure and stock crash raises concerns about company direction.
- Date: 2026-11-19 | Impact: high | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOcHQxY0U0UnFWS3Nhb3dHdUxJZVlqNmZBVko1X3hUcWkyZlNsVmljSF9JRVUtWGd0Qm9MdTlfSWk1RFpaZ1NXaHRTd1Nma21pOFNiOUpCUFh2eWtSVUtkNmlia2lESUVrZWEtZFV6YkFHdHpQLUJrbjhmbmphT1hfRHhSakRTT3ZLbkx3NXVIaHdaYkQ1ZndBOTg5cl9jdw?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVDA** | **16.22** | **13.20** | **14.22** | **103.20** | **3,524,978,802,688.00 USD** | **-21.55** |
| AMD | 113.24 | 11.73 | 71.41 | 44.70 | 809,641,574,400.00 USD | 118.83 |
| AVGO | 44.27 | 16.60 | 32.34 | 85.50 | 1,654,778,757,120.00 USD | -1.47 |
| INTC | N/A | 2.57 | 16.14 | 20.90 | 296,151,810,048.00 USD | 58.70 |

Peers fetched as_of: 2026-11-19; NVDA reuses existing data (market data as_of: 2026-11-19); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-17
- Next expected earnings: 2027-02-24 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-19

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-26
- Revenue (latest available single quarter): 96,221,000,000.00 USD; period 2026-04-27/2026-07-26; fiscal year/reporting period 2027/Q2
- Net income (latest available single quarter): 59,688,000,000.00 USD; period 2026-04-27/2026-07-26; fiscal year/reporting period 2027/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi1AFBVV95cUxQUzhvYkxzRld1VG11TlpOSE5wWjE5WE94RkMwVkJJWnRReDFRTUZ1X1FQWU55Rnh5b1hqU0VvTzBCay10WE5iVzJYWHdtVWJ0dlU5aFhhX2Yxa09Ub0otUkVUQ0hCTC1OUHBhRTU5UDBlRVZfNEx4cUtoVXRRanEwazFaQTBwYmpBREc2MVlsaVlDNWptenNNZkpDNzd2blFtS3pJX0oxWDl2RlcyMFNucDRILTRlRF9iUWFPRTA3VFo5NGRVZUJTaDkyTmpYcF9xcGJtMw?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxOSWE3SDhVLURnMWI2MzhzdHlPX1pYcTlDeURlYTNNbkZ2X2E5dS1qb3dtNFh6bUdFSlpDWGkyY0djeW04SVBDQjZJeWZlN2R0N2ZiNXZ2OEFQZlZpMk10ZzU0d0pxTHl2eDlIVGcwazYzcUJSWHk2YktyWGdTVFZ3UVNsaXdXT1pTalY0blc3aURQQklUY0NtZV9aRTNfWWdyelRycW00Zl84QTJhTmppTHhteU9RQUlHTmFXdUxkbw?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxQQmI0cjQ4cUVpYjVTeXNuNFdNRmE4bHFJTDBsbDBNLS1LZGEzeFhsUVRvYzltRjA0YUU4RnYzS1htMkNHTDRDcHdfQXk4QjdRYloyQVRJWGtlLXhHNmJiMmVQMVhJNTduQXNZdld6ald5SmN0bUVHWUJpbmRBR2RIN2tVdEI2cG9hcXNMeExDd1JWNFBtS0JLQlkzWERheDhVSWZVZ3Z1RUNsc21zRjVQNWg4cw?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPWHNRcEVuR1ViVWpUY0p5RnIyekVpWDRTVUFLXzhLYnFDZ2tfeGctTGFkcENyRFliRXVRSktrc3hiTU01ZW9oY1dzaVJ2dzBNcTBxLWZienhFM0I0dVFDYXp3NTVjM3lZNGhxMXpuZUhuLXdUd1o0RTN2VVR0bzRDNnE0LXByUDJvWFl3VUFra1JDQXZmbV9FejNKdEI?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxNVEJ3VzdMRnFXV3ZlNU1Kc0NHZ0toc2w3aFRGSFF5QkFCYmRTQUVGOW9YVE52UE9nLWR4U1JSZmF0R0h6aUNjREs4VGVyZ1NaZkhOdGhzQ0ZQbEdHQTlrU1VuaEFMMDlQdE1YdVdRYTdtaVp2UWQtX3hZMjBVLXQ4Z1VuTDRabnRRTnl4Zy1GZlA5QW52cTJIcGw1SnBZZ2VmQ01GYVUxQWNzSzEzelctbkhWX2w?oc=5
- https://news.google.com/rss/articles/CBMifEFVX3lxTE9iM3pFNTMyc0NDSXdVbjV1RFhtMjMybWRUcWtGOGRsVllWSS1Yd2Y0emU4MXNVbUpoUUUxTVZ5ck8xem1nNjVuNUl2VVFzLXNMZU1nZlRPNDJTRG9uaFhkbXpSdzNhQW9lWDZQbUtHUnRZeDBlaUl2Y3pDcErSAYIBQVVfeXFMTXV5dkdmRTlzLVlhbUdHREtUSWs2M09MRm8yYldyTkhnZllMWUdFZHh4cVo1Z0FlUmRld3ZnUmVuMV9OanU0em9oTmF2MjNoNGZ0T282eDZialBxU3g1Nkt5aFVrSzdHbmh0Y1I5aFZhRDZjQWdWX0Q3aXNVaV9DeFA2UQ?oc=5
- https://news.google.com/rss/articles/CBMifEFVX3lxTE5PQVk0Zkc2enRNbFBEaThQMVdVQXQ1X1pTdm11LWgwNkE0Q3BVd1Y0R0gxTnVzZjdPdUVDWEJxcDVfSk16QWJmSWFXMUpMTEJQMnh4d2N2SFpNQmRqUWJ0c0ZUMFpxRFdfS1k4UU5jXzI0Z3l1V2VoS3NvTGQ?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTFBFOVFHRlJnRTd1eTF3aG9HVUJzLVpJZVJIand2T2dFMzk3QU5mRkhwNXU5aXdzYmREWFk1dEdvR0ZOS1pQYWNJTk5CWGM1akFQTjQxbV82U0pEQVRTZUEzbXNFUkpObTJvU2NQb28zeVBPRFZLeDg5NW1JOTVfdw?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOc3RRaGlXbTlWZ1pyYW1tc0hrRXBlV0xRTjVrTGU0UDhDTUhJbEFYZTdacGtQd0ZRdjhJQ2Zqbm9Qbk1HSmVxTjFkX1NVa0MyZkZsNkhsdkIwb29mLXpZRXFqM3M3ZzJyY21obFE1MTlocnVLU2lCUlVMOVJJWmRsRVc3SC13SE1QYzZqT2pLdG5jODJzdzY0ZkhxTWw?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxNMnc5TjJWdmVlZ255ZjJOaUpXa3FzWVJYdXVrQjRoRWVxTmtpRXptS21fX3h3a3ZXMXZIQjVNYnd6N25XSURjYzlKV3JOMkE0Yk9LanRZcGZLelgxSzc3YkVOZk9UYnJCSmxuVUVqSDNpNXBIdUdvODl2VmJKdUNRR0FyM0pVbFpGYmVLbm5IUWNkbkVIb0s5MFRRdmhKWWhoQ013?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxOd09QMUxzbVhUclZQOE5JTDY0VjRCUU80amJ3S0lHZnd2MERNWkthb0VHY0JpLWw5Q2xwTXM1ZlBGRERERlFVeXlxeUtTTFU1YzNuVS1UeEV1Y21TZTVrQkZidTF3N1NBOWhmZjFrTlhUNjNVSnBJVmcyRVNvQ256cTRPX091MFRGVy11bjVaTG16QWRJTjVic1VNZ3NfZnFrWmo0bVk1bW5jMWtGTXVyR3BVUlJHRzA1ZHlCZmR3?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPRllSN2RmXzJSQjJjQ2F5WmxTWUhGd0dETkZzRWdVMjNmc0g2NVVmdFMyOUpJd3Ffd3d4akxjdUVOYWFsT2lCeVN3ZV83YVEyNjluV0tfOUJwUllIUWVIZzBual9VWFBDZnFRZjlCc2pTS1V6Ri1zVjlITFJrU1lLcmk0YVdrc0tUMzlobEZpVEZ4TkFUVFE?oc=5
- https://news.google.com/rss/articles/CBMi5gFBVV95cUxPTGswLW45X25uQXNodGZiZnNWeFk1dTdSWm5SRktfUXBTaTY3QlA2dFR3U3hFNnpDX2dwa3VHYllDS3Roa1VyWGFEMk16alc1dHRXR1p0eUVsRk1LMEliNDJyYlJIczVmam1OT25jMjRKbUZ2UE05bGtKLWUtdldySHpvOWMyRUdmenJUaFk0eTYtalRlZll0RkkzdGdzcnMwYkR1eWpKZTdqU3VRYXpLY1BSU2MwM04yMEJmbW9YOWZvZlRleUpqd3BseDhrTE5GVEFNN0FTM0hjUjdDTFBGUUQyOWVfUQ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPSWY1d2ItZkhENElDOVhFeHBYYXpQcU0zdjZTbG4yV0Z2RHM1eGF5ZG5FTFo4YklUTUItMnNJZVd4b1gzMGZoeE9PRzhnZ3pwREQxYVBMVDNFRVo4bWNhcktfZUlBZkRacldEQUZRSG84eEJGM3Y0YWc0eEU2VUV3MVREMHJBWE1UaUk2d0tpaEY0SDFxZXN5bkZTVQ?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxOM0V3d1ZlZG04SEFmUFJDc1lRZDRWMkZMMkVULVc2SlZqMmI2VUlfUW9sWS1UOFAydWxxdDBVZDZVU2FRODNxMUtTdGdKSnh1Z0tnOF90VDNzMThFUkk2dFE0Y0ZwenFLSWl5TFNKUDhod1pOU0VHT2lEbE0tUUtKN3hQNjk?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPdkFIWjA0UXlkc3l0NnBYTzNxUklMY0piNjVnZlZGMXVJYWk5cHRpcnF0OFAtYV9lY2p4dTRuMnNwNjRuSlJNOHlhcURTZk4xcm5uYnFNWkVibWd1c2R6ZUNoTmdwT19kdkxQdmw0OF9fcDV3ekNCN0xBcUQyS0c3eUFlTnRER3Y2RzdpYjBueElrR2JRTlRr?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOcHQxY0U0UnFWS3Nhb3dHdUxJZVlqNmZBVko1X3hUcWkyZlNsVmljSF9JRVUtWGd0Qm9MdTlfSWk1RFpaZ1NXaHRTd1Nma21pOFNiOUpCUFh2eWtSVUtkNmlia2lESUVrZWEtZFV6YkFHdHpQLUJrbjhmbmphT1hfRHhSakRTT3ZLbkx3NXVIaHdaYkQ1ZndBOTg5cl9jdw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
