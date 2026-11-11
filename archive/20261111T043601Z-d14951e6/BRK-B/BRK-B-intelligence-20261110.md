# BRK-B Intelligence Report

- ticker: **BRK-B**
- Report as_of: **2026-11-10**
- Market data as_of: **2026-11-10**
- Quant sources: https://finance.yahoo.com/quote/BRK-B/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/BRK-B/key-statistics/
- AI analysis snapshot as_of: **2026-11-10**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-11T04:56:12.740394+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 5, 'ai': 17, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261110T055129Z-abd33250/BRK-B** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 12 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 40.0%; oldest publication 2026-11-07

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 583.3400 |
| Return 1D (%) | 1.4063 |
| Return 1W (%) | 4.7157 |
| Return 1M (%) | 13.1337 |
| Return YTD (%) | 16.0529 |
| Return 1Y (%) | 17.3770 |
| Annualized volatility (%) | 15.1764 |
| Beta vs SPY | 0.0533 |
| Max drawdown (%) | -9.4218 |
| Sharpe (rf=0) | 1.1359 |
| Downside deviation (rf=0, %) | 10.0753 |
| Sortino (rf=0) | 1.7110 |
| Historical VaR 95% (1D, %) | 1.4122 |
| Historical ES 95% (1D, %) | 2.0016 |
| Correlation vs SPY | 0.0480 |
| Tracking error vs SPY (%) | 19.9321 |
| P/E (trailing) | 16.10 |
| P/B | 0.00 |
| EV/EBITDA | -2.04 |
| Revenue growth (%) | 11.20 |
| Forward P/E (estimate) | 25.96 |
| Gross margin (%) | 26.60 |
| Operating margin (%) | 26.05 |
| Return on equity (%) | 10.57 |
| Free cash flow yield (%) | 4.23 |
| MA50 | 524.5516 |
| Close vs MA50 (%) | 11.2074 |
| MA200 | 498.7037 |
| Close vs MA200 (%) | 16.9713 |
| RSI (14, Wilder) | 78.0148 |
| MACD (12,26) | 15.6793 |
| MACD signal (9) | 12.8146 |
| MACD histogram | 2.8647 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'BRK-B': 279, 'SPY': 279}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 583.3400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.4063 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 4.7157 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 13.1337 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 16.0529 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 17.3770 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 15.1764 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 10.0753 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.7110 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.4122 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.0016 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0480 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 19.9321 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.0533 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -9.4218 -> Shallow peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1359 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 25.9609 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 26.6020 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 26.0550 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 10.5740 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.2341 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 16.0966 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 78.0148 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 2.8647 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 11.2074 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 16.9713 -> Clearly above the moving-average trend level.

## TAILWINDS

### Berkshire shares surge as Wall Street swoons amid AI fears
- Summary: Berkshire shares surge as Wall Street swoons amid AI fears
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPQXgyQmpJT1lzSWhTZ01uZWJoRngzWm44N2hQT2lRcUNLWVZONlZQa3lHOTN0VE1zNEZvSjNzUEk4aThrNk1DbTZpazdtTm43TmJUYWNwYWlnTDJocHM3T3BybUpWSlM1ZElKTExkRTBoQy1NVy1zZDRCWHNPZDJFcXJReDR2OF81MkxPS282anN1UzRlUzNBb0tWTQ?oc=5>

### Warren Buffett's Rule for Stock Buybacks Is Very Specific. Berkshire Spent a Record $9.6 Billion on Them Last Quarter.
- Summary: Record $9.6B buyback last quarter signals strong capital allocation.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNZ2x4aFRuSTUzYXFaQTc5S3E3N2xiRm9ZU0Npb3Q2RmFYN21JcUxfQld6MUZ0OUQ5ZkNtMzY5MDNXM2FQV0VwSlBWX0NDdi1uemdhdWFzcWVMSF9tUzhmSFA2Yl8xUWVtcUR4X0NrV090V2dTWE9MbjBCZ3VFY1NpOUVpSWNzSTRGTHpZNjVXZ1FqQ1JjU3I1alczTGpBZkswNnc?oc=5>

### Forget the AI Friday Rally: Why Big Money Is Still Fleeing to Warren Buffett’s Berkshire Hathaway
- Summary: Investors are moving money into Berkshire Hathaway, indicating a positive market move.
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOT250cWpQVTRuclhwa1c5THVjelFjeEt3c042eVBSdVpzUTB3S0wtMUUxMWhOWHRQS2Z5VTFoYV9zb0xEekVsQ2d1WE1LZ01JYVVlYzF0eV9rZTR0ckt4ZE1PNF9qaGhuWmUxR1BLeDVHQk45UHk1OXNDUXNMc3p3QnhkOC1aeF85NWdmNktWWGlvUUhfWUE?oc=5>

### Berkshire Hathaway stock is a haven again as investors flee AI bloodbath while its own portfolio takes a hit amid reshuffling
- Summary: Stock is seen as a safe haven amid market turbulence, though portfolio losses occur.
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPd0ZwYVhqTGEwb1ZkSWcta2tKbExWN2lZY2pFdXk3VmNiN0lHZzZpV2FNRWFIQnYta3cxRDk0dFlXVjFoUmp0Y3ZBdnh0Rl9vMmxyVXZieWJhYk1uYlpCWGRhTVdEZTNSVnYzWUptSk95NG9jazB3cmxYTnFUdjd0eFIxQjhOLVF4QmUxYklwY2tSajNDZmVkTFNUcmhqblFSeEh3?oc=5>

### Berkshire May Be Buying Class A Stock Directly From Holders to Boost Repurchases
- Summary: Berkshire Hathaway may purchase Class A shares directly from holders, increasing repurchase activity.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxPTXJ5cHQ5R0NicjVZUDlMSnBZVmk5VlozOTVQYzFSWUxHVW1ZYjNkUVNzbUthT01uLUR1NEhsVGtZMGJHZVBJM2o0TVBHNWJxazdMYXA5VFVfQ3ZFWWRXMFk5cE5KR0pvZE4yeFhpQW53QTNIUjNGNlBneDQ1VDBOTXBjSklWR2FSS2c?oc=5>

### Warren Buffett’s Successor Is Doubling Down on Berkshire Hathaway Stock. You Probably Shouldn’t
- Summary: Successor intensifies Berkshire stock buybacks, potentially signaling confidence in the company’s value.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOZlhDenNoR3FMdmtnWUtUYkpwU2RWS1YzNnZ5UVhsN0FqTi1YWXRnbDhmRlJSNGxxMGNyRzR2ZUVJY3FhZjZMY3RGR2RKSlNJcjBhd1BUcDEwb05NOGM0bmN2NjZoWWxNTEhwczgzQXRsYm5SMk5lU0o0UTV0VUtJdm5UNENhY1hoX3hoMS00NGRRM0ZVVnR1N2hZeUJDaFBQZ1dHM3Vn?oc=5>

### Berkshire Hathaway (BRK.B) Might Be Buying Back More Stock than Investors Realize. Here’s What’s Happening
- Summary: Berkshire may be conducting larger buybacks than previously known, indicating strong capital allocation strategy.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxQUjJfcy0tSjZBR1djcnBNbDVnVkI5am9lV2V4Mmh5QlJ1N2s4TFRJdWZNUmx6NzdmZVlJYU9vTHBkVDNWNW9NUUdTSFI3UnZCTUt5MHhVYjgtc3pGcnQzZFhaUzI5a3dMLVNlbDhGeWxtV2Y0N0pGbnVwajlnOXN5dXJBa2hqbm1wYUVOb1FDM2p2dzJrM1RXQUtQeU02QUp4RC1DYkRDN3lIY2VsMzBIQlFGaWxTdkYzWUpEamVTMFRjbDBBYU5VWkMwUQ?oc=5>

## HEADWINDS

### Berkshire Hathaway Earnings: Cash Levels Retreat Again as Acquisitions and Share Buybacks Pick Up
- Summary: Berkshire Hathaway Earnings: Cash Levels Retreat Again as Acquisitions and Share Buybacks Pick Up
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxNU3k5QnhncjJEWEVxWGlGZm9DRnBxTGRBQ29fZHBfV3VrRnVkWEs5bzFSZnZhcURvdzBHVmdiOG5zOGJSdjZRMzVpZGQtY1RKRVBTS0dsa2ZmYWliSEIzUHctdEEtVVo1MHZNU2NsMzFaTHZ5eWxNQ0JWZnp0SWNwQjNIM2IxUmFrX0hvSFBmRzdkOUJ0UFBsUF9HbjlqamcxNDF0T2huUldUSndCQ0I2S2ZQLXdvbU1QTGFNSWZuazdWQQ?oc=5>

### Why Is Berkshire Hathaway Stock Trading Lower Monday?
- Summary: Stock price decline indicates market pressure.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxNRVdFQkxVZDB4a3N3NkdiWWtxMGxWeVdzMDU3VnRTLU9zRmhWSG13NmJOSWs4RUZxQXVhWGpNeHNDam5aOFdrSS1yblNJSnREWHQxdzVTeFpRVmV1aGRwb3EwRS1CWXJJNG9rT2JUX3JsbURFNmoyZDQ1ZlB2U19pNzBKWGNCVVVaNkk4RzM3WFBvbGRBMUp0SWJTbXZzNklPck05ODFrZ29BeGFZNnc?oc=5>

### BRK.B Q3 Earnings Decline Year Over Year, Revenues Top Estimates
- Summary: Q3 earnings down YoY, revenues beat estimates.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPV1MxNnk5dVFqOExmUlBLNWhFS04zU1VQZHAwSWpyckJEQUgxdmFjSWJuQlBYbS1RcnJuSVlZejREcGtuR3ZacFlRSmEwOXFrdWlBTFlXRGRCRkhBRV9oWU5rRV9MOVMyZ0lfRXdyX25lR3ctSWdYVnM0dnIzMnlXVXJkMXVBUktpQW5OOVVWaEZkVDAw?oc=5>

### Berkshire Hathaway: This Isn't Going In The Right Direction (NYSE:BRK.A)
- Summary: Negative outlook on Berkshire’s performance.
- Date: 2026-11-09 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOZkRQbUtwVUlGV045NGRiMG45eTJ1NFlSMzROUHM2ZDhvalhuS2lmR2dCRWtuSkIxT3VSVHcybUwyMGR5Z0JMMmJQVUxEWU9rYVVIa1VnUUtPSUxJRldpSG1vU0RXS2YxMElVemJXVHJHaUxnd2EyNkNJelFpdV9Qd1J3WDhlYVh0T0Fmd1lzR1hqbzZjMkZpYmFSSUpHZW8?oc=5>

### Berkshire Hathaway: BNSF And Energy Steal The Show In Q3 (Rating Downgrade)
- Summary: A rating downgrade signals increased risk for Berkshire Hathaway.
- Date: 2026-11-08 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPNjVIWGhXeEl0aF9saUJhMWk3Y3E1VXN4X3dxaElKdk1tUkd6ZjA3NVNrOGd6UDI2UDhnS1NmcDV3QnJYZXFmOXlQS2pJbk9QYXlvWEhpTS1lREk0MzluTzV1QkJReGFUOWw3NEVkQUYtbVFkNWhXYVZ1WEZ5aXgxek0yeFBBT1BSWi1IaDJQVFJiOW1kS1ZpM3I2Q2U?oc=5>

### Berkshire Hathaway Stocks Slip 1.01% Despite $9.6 Billion Buyback Surge
- Summary: Stock price fell despite a large buyback, indicating a negative short‑term move.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQWk93cHB4ZzdfR3N6OGQ5Rm04b3EwZTlOVmJEb3FZRElYWDhRTmxkTXRQMkVBLUM4YnRrTV95T25SdXVpbzBncFJGbFVLUk5ITkNVUk5KNE95ZXNNVHBYelgzWFQwTHVjZVRxZHJqdlhvSDd5WFQzQXdzWTFTM19MdjVXWTNYX0ZkNGsxMS1TbERFUVBBVFlLcVZMclBDQQ?oc=5>

## CATALYSTS

### Berkshire Hathaway earnings expose unexpected problem beneath strong economy
- Summary: Berkshire Hathaway earnings expose unexpected problem beneath strong economy
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxPR2NfZzl0UUlGcm1GSHZ3M1dOeldXYmFDdU84MDB6SHQxVXZUMklXRWpCV1FzSThuTDNZWElEQmlqSDdDandIR0ZwOE5wN0JtNkctc0lob19NbzBnTHEtYWV5ektaV240bEdqeDd2SnJTMkpod0ZZblNLSDd5OTRGbVJKNVhzR28?oc=5>

### Berkshire Hathaway Q3 Earnings Miss On Insurance, Not On Strategy
- Summary: Berkshire Hathaway Q3 Earnings Miss On Insurance, Not On Strategy
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxObUlKZVllVlVCdXlfa2VfbnY5a2ljTHI0ZV9QakR1aUExeGNzczkzZDdOamxKQm9DZW5mTnhUd0N0MnRtRGZybDlzNUJwUnNYaWY0MDV2aVFtOWk2dDRaS3IzVFBqemtna1lVbVVtYVE0bkw1bWJEeFVxbGhkNTN2SkFOOU5NU01iWWRBb1RDS1FwYUlXV1VYc2E1bnJwOHViZWNFcXZLd3pPbFVBQlJEcFZ0bFFxQTQ?oc=5>

### Berkshire Hathaway latest: Q3 earnings, top 5 holdings, record stock buyback, & more
- Summary: Berkshire Hathaway latest: Q3 earnings, top 5 holdings, record stock buyback, & more
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxQZ2loVTdsMFF4Z2F5WWdnOHprakxBVGlGcUJ1YWkxNm1uOFltRmNDbU9ISWsySWplc296c1lWWU5DUzBITEN3Zm1xT1pHR1pDQUhUemhGdEdTcVFXdlNCeTRNVDFxeTQ3b1BpbV9SdnQyRjM4S3M2cjBaTE1xRnhXLXlVRzh6Mmd1dkY0LXFGRXotWnhvdjZIeXBaZTE0WnY5MDUtUkVWYWNXa2xvQ2hiMUVmZHFJT054QTB1Z3JDbzR3cDdP?oc=5>

### The biggest takeaway from Berkshire Hathaway’s latest quarter isn’t the $357 billion cash or its stock buybacks
- Summary: Quarter results highlight factors beyond cash and buybacks.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi5gFBVV95cUxNOURBSlE3MGE0bFVPWWU3b0Z3dlpUaVQ0WG9JZGJQdDBnWXozSjcxUjhlaTJTOFNsOUt5dTBBOElEX3RMUHZaa0N3ei1rNTVsR242MDFaTGxZaWNZanMyNjNlbng1b2syTUpBYXEzUHVmTFo4RXZHVWt2UlByTHJtSGw1cENlSUJaem84UzE3Tk5SUGJoOVEtdGJOYl9xM0hyVHFtSkRrVDhSUTNPVXZSbFM1ZTl2YXUyYndWTzdvQkIydWQyVGN2YjVKZHYyMV9PNGlRcWozQ3V6cUtYLW5tbUVScjVvdw?oc=5>

### Warren Buffett's Successor, Greg Abel, Just Added Another Tech Stock to Berkshire's Portfolio. Here's What He Sees.
- Summary: New tech investment indicates portfolio diversification and potential growth opportunities.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPOS0tVEUtMkVvMmoydEJNRks4SEcwUUZEQnpmM05sZUpmWVdlcDJzTzREX25GR19HWkczRExwc1FFemNjNllyd3BoaGlTd0czMS1Va1BQdmZOMnR1VU13TFpzUExzOHlvNWdIa0VXUm5ha3VBRFJOUjZoaUl1ZW8xTm9xYlV5bHRTOXpyXzVhaVlsT2tVVFB1dQ?oc=5>

### Warren Buffett's Successor, Greg Abel, Just Plowed $27 Million Into a Virtual Monopoly (No, Not Alphabet!)
- Summary: Greg Abel invested $27M in a virtual monopoly, a new product investment.
- Date: 2026-11-09 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQWjlWbUxIMHhnWnEzVEZIZEx0MTQ2Z0p5ekh3RnR5VEZsOWh4REhnd2dlTjN6UHkwbWdJMlEyaHdlMnY2aUpZaml4MEFDMEdJaG9wTGNYY3JuVVMzdTE2RUt4a3VnSE5ybjloYklNc0Z0ZWlCaldaWmtNdHJGa1lzTEJhekVHWTNtVUE4UU9GUkJ1U1NaRHo4OUc0OUxPZ1ZjbUE?oc=5>

### Berkshire Hathaway’s Quarterly Profit Falls After Investment Gains Shrink
- Summary: Berkshire Hathaway reports a decline in quarterly profit due to reduced investment gains.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQSlRmcnB2bWtXOHV1MEJucmRMSFpiMjUtM1dMUnVRbnBybWxCSWJ0YU02QVczWERwbDlNQzJSeThHVnRNUmEtd3dOQzRUQnJhT2V5WlhQczRYdVVGaUV3YVpaNUdvUkNqRDB0aWpDQW5IV0xtbF8zQjdGNm9xYlllMDRSYTZTLXNHMTJGLUNXYXhCMGx2R2drclQ5amZocWJndlE?oc=5>

## RISKS

### Berkshire Hathaway: The Margin Of Safety Has Evaporated (Rating Downgrade) (NYSE:BRK.A)
- Summary: Credit rating downgrade signals increased risk.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxPVG5Zd21HMzR5TWpzbzFac1RSOTJzQWRWTzZqSTNYVUZBMzFuWW9TeHNQTzBXZDlOamdnYjB1VlNNdXJMd29sRnpVZFEybjZWZXJfUHBhTlJ0bFhueE83UEstTFRiTWk1am9MZXNvbWd1UTI2b2t0MzU5OW9pRlJ2WmtJN2FkeG1vc1Q4Rzc0dFdhRTZQSzU3NEZzaXdSd3BOMGNtOGh5aVdOQXV3UmFpMm5B?oc=5>

### Berkshire Hathaway Remains Attractive Even If Its Valuation Is Becoming Stretched (BRK.A)
- Summary: Valuation stretch may pose a risk to Berkshire’s attractiveness, suggesting potential overvaluation concerns.
- Date: 2026-11-10 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxQUVo4RktsemNtcXRGcngxbWgxVUFtcmRiQi1JOFQ5QlpiUzVVNVF0b296N3pJRW5saGthRlFQdVRuMEh2c1hNTURQcm9qOUZ5RGZvRDlobTZjU1pYT1lmajJuaUw3V1IwVVAtWTNBSWg4bFNpZjFrM20tdzJBcmZyUG95RzRZdlZObWg4SzRHYWc5TmpLeEZUMDg0RGhTeU02b1h1UDhkUHNGVkJNNUREZWVXVnNrOGt3dS1J?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **BRK-B** | **16.10** | **0.00** | **-2.04** | **11.20** | **1,239,317,086,208.00 USD** | **17.38** |
| MKL | 13.89 | 1.31 | 8.08 | -11.20 | 24,146,268,160.00 USD | -4.17 |
| FFH.TO | 10.24 | 1.46 | 8.93 | 1.90 | 57,536,188,416.00 CAD | 25.94 |
| L | 15.20 | 1.23 | 8.70 | 1.90 | 22,432,845,824.00 USD | 7.93 |

Peers fetched as_of: 2026-11-10; BRK-B reuses existing data (market data as_of: 2026-11-10); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-07
- Next expected earnings: 2027-03-01 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-10

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

- https://news.google.com/rss/articles/CBMimwFBVV95cUxPQXgyQmpJT1lzSWhTZ01uZWJoRngzWm44N2hQT2lRcUNLWVZONlZQa3lHOTN0VE1zNEZvSjNzUEk4aThrNk1DbTZpazdtTm43TmJUYWNwYWlnTDJocHM3T3BybUpWSlM1ZElKTExkRTBoQy1NVy1zZDRCWHNPZDJFcXJReDR2OF81MkxPS282anN1UzRlUzNBb0tWTQ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNZ2x4aFRuSTUzYXFaQTc5S3E3N2xiRm9ZU0Npb3Q2RmFYN21JcUxfQld6MUZ0OUQ5ZkNtMzY5MDNXM2FQV0VwSlBWX0NDdi1uemdhdWFzcWVMSF9tUzhmSFA2Yl8xUWVtcUR4X0NrV090V2dTWE9MbjBCZ3VFY1NpOUVpSWNzSTRGTHpZNjVXZ1FqQ1JjU3I1alczTGpBZkswNnc?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOT250cWpQVTRuclhwa1c5THVjelFjeEt3c042eVBSdVpzUTB3S0wtMUUxMWhOWHRQS2Z5VTFoYV9zb0xEekVsQ2d1WE1LZ01JYVVlYzF0eV9rZTR0ckt4ZE1PNF9qaGhuWmUxR1BLeDVHQk45UHk1OXNDUXNMc3p3QnhkOC1aeF85NWdmNktWWGlvUUhfWUE?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPd0ZwYVhqTGEwb1ZkSWcta2tKbExWN2lZY2pFdXk3VmNiN0lHZzZpV2FNRWFIQnYta3cxRDk0dFlXVjFoUmp0Y3ZBdnh0Rl9vMmxyVXZieWJhYk1uYlpCWGRhTVdEZTNSVnYzWUptSk95NG9jazB3cmxYTnFUdjd0eFIxQjhOLVF4QmUxYklwY2tSajNDZmVkTFNUcmhqblFSeEh3?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxPTXJ5cHQ5R0NicjVZUDlMSnBZVmk5VlozOTVQYzFSWUxHVW1ZYjNkUVNzbUthT01uLUR1NEhsVGtZMGJHZVBJM2o0TVBHNWJxazdMYXA5VFVfQ3ZFWWRXMFk5cE5KR0pvZE4yeFhpQW53QTNIUjNGNlBneDQ1VDBOTXBjSklWR2FSS2c?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOZlhDenNoR3FMdmtnWUtUYkpwU2RWS1YzNnZ5UVhsN0FqTi1YWXRnbDhmRlJSNGxxMGNyRzR2ZUVJY3FhZjZMY3RGR2RKSlNJcjBhd1BUcDEwb05NOGM0bmN2NjZoWWxNTEhwczgzQXRsYm5SMk5lU0o0UTV0VUtJdm5UNENhY1hoX3hoMS00NGRRM0ZVVnR1N2hZeUJDaFBQZ1dHM3Vn?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxQUjJfcy0tSjZBR1djcnBNbDVnVkI5am9lV2V4Mmh5QlJ1N2s4TFRJdWZNUmx6NzdmZVlJYU9vTHBkVDNWNW9NUUdTSFI3UnZCTUt5MHhVYjgtc3pGcnQzZFhaUzI5a3dMLVNlbDhGeWxtV2Y0N0pGbnVwajlnOXN5dXJBa2hqbm1wYUVOb1FDM2p2dzJrM1RXQUtQeU02QUp4RC1DYkRDN3lIY2VsMzBIQlFGaWxTdkYzWUpEamVTMFRjbDBBYU5VWkMwUQ?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxNU3k5QnhncjJEWEVxWGlGZm9DRnBxTGRBQ29fZHBfV3VrRnVkWEs5bzFSZnZhcURvdzBHVmdiOG5zOGJSdjZRMzVpZGQtY1RKRVBTS0dsa2ZmYWliSEIzUHctdEEtVVo1MHZNU2NsMzFaTHZ5eWxNQ0JWZnp0SWNwQjNIM2IxUmFrX0hvSFBmRzdkOUJ0UFBsUF9HbjlqamcxNDF0T2huUldUSndCQ0I2S2ZQLXdvbU1QTGFNSWZuazdWQQ?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxNRVdFQkxVZDB4a3N3NkdiWWtxMGxWeVdzMDU3VnRTLU9zRmhWSG13NmJOSWs4RUZxQXVhWGpNeHNDam5aOFdrSS1yblNJSnREWHQxdzVTeFpRVmV1aGRwb3EwRS1CWXJJNG9rT2JUX3JsbURFNmoyZDQ1ZlB2U19pNzBKWGNCVVVaNkk4RzM3WFBvbGRBMUp0SWJTbXZzNklPck05ODFrZ29BeGFZNnc?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPV1MxNnk5dVFqOExmUlBLNWhFS04zU1VQZHAwSWpyckJEQUgxdmFjSWJuQlBYbS1RcnJuSVlZejREcGtuR3ZacFlRSmEwOXFrdWlBTFlXRGRCRkhBRV9oWU5rRV9MOVMyZ0lfRXdyX25lR3ctSWdYVnM0dnIzMnlXVXJkMXVBUktpQW5OOVVWaEZkVDAw?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOZkRQbUtwVUlGV045NGRiMG45eTJ1NFlSMzROUHM2ZDhvalhuS2lmR2dCRWtuSkIxT3VSVHcybUwyMGR5Z0JMMmJQVUxEWU9rYVVIa1VnUUtPSUxJRldpSG1vU0RXS2YxMElVemJXVHJHaUxnd2EyNkNJelFpdV9Qd1J3WDhlYVh0T0Fmd1lzR1hqbzZjMkZpYmFSSUpHZW8?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPNjVIWGhXeEl0aF9saUJhMWk3Y3E1VXN4X3dxaElKdk1tUkd6ZjA3NVNrOGd6UDI2UDhnS1NmcDV3QnJYZXFmOXlQS2pJbk9QYXlvWEhpTS1lREk0MzluTzV1QkJReGFUOWw3NEVkQUYtbVFkNWhXYVZ1WEZ5aXgxek0yeFBBT1BSWi1IaDJQVFJiOW1kS1ZpM3I2Q2U?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQWk93cHB4ZzdfR3N6OGQ5Rm04b3EwZTlOVmJEb3FZRElYWDhRTmxkTXRQMkVBLUM4YnRrTV95T25SdXVpbzBncFJGbFVLUk5ITkNVUk5KNE95ZXNNVHBYelgzWFQwTHVjZVRxZHJqdlhvSDd5WFQzQXdzWTFTM19MdjVXWTNYX0ZkNGsxMS1TbERFUVBBVFlLcVZMclBDQQ?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxPR2NfZzl0UUlGcm1GSHZ3M1dOeldXYmFDdU84MDB6SHQxVXZUMklXRWpCV1FzSThuTDNZWElEQmlqSDdDandIR0ZwOE5wN0JtNkctc0lob19NbzBnTHEtYWV5ektaV240bEdqeDd2SnJTMkpod0ZZblNLSDd5OTRGbVJKNVhzR28?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxObUlKZVllVlVCdXlfa2VfbnY5a2ljTHI0ZV9QakR1aUExeGNzczkzZDdOamxKQm9DZW5mTnhUd0N0MnRtRGZybDlzNUJwUnNYaWY0MDV2aVFtOWk2dDRaS3IzVFBqemtna1lVbVVtYVE0bkw1bWJEeFVxbGhkNTN2SkFOOU5NU01iWWRBb1RDS1FwYUlXV1VYc2E1bnJwOHViZWNFcXZLd3pPbFVBQlJEcFZ0bFFxQTQ?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxQZ2loVTdsMFF4Z2F5WWdnOHprakxBVGlGcUJ1YWkxNm1uOFltRmNDbU9ISWsySWplc296c1lWWU5DUzBITEN3Zm1xT1pHR1pDQUhUemhGdEdTcVFXdlNCeTRNVDFxeTQ3b1BpbV9SdnQyRjM4S3M2cjBaTE1xRnhXLXlVRzh6Mmd1dkY0LXFGRXotWnhvdjZIeXBaZTE0WnY5MDUtUkVWYWNXa2xvQ2hiMUVmZHFJT054QTB1Z3JDbzR3cDdP?oc=5
- https://news.google.com/rss/articles/CBMi5gFBVV95cUxNOURBSlE3MGE0bFVPWWU3b0Z3dlpUaVQ0WG9JZGJQdDBnWXozSjcxUjhlaTJTOFNsOUt5dTBBOElEX3RMUHZaa0N3ei1rNTVsR242MDFaTGxZaWNZanMyNjNlbng1b2syTUpBYXEzUHVmTFo4RXZHVWt2UlByTHJtSGw1cENlSUJaem84UzE3Tk5SUGJoOVEtdGJOYl9xM0hyVHFtSkRrVDhSUTNPVXZSbFM1ZTl2YXUyYndWTzdvQkIydWQyVGN2YjVKZHYyMV9PNGlRcWozQ3V6cUtYLW5tbUVScjVvdw?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPOS0tVEUtMkVvMmoydEJNRks4SEcwUUZEQnpmM05sZUpmWVdlcDJzTzREX25GR19HWkczRExwc1FFemNjNllyd3BoaGlTd0czMS1Va1BQdmZOMnR1VU13TFpzUExzOHlvNWdIa0VXUm5ha3VBRFJOUjZoaUl1ZW8xTm9xYlV5bHRTOXpyXzVhaVlsT2tVVFB1dQ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQWjlWbUxIMHhnWnEzVEZIZEx0MTQ2Z0p5ekh3RnR5VEZsOWh4REhnd2dlTjN6UHkwbWdJMlEyaHdlMnY2aUpZaml4MEFDMEdJaG9wTGNYY3JuVVMzdTE2RUt4a3VnSE5ybjloYklNc0Z0ZWlCaldaWmtNdHJGa1lzTEJhekVHWTNtVUE4UU9GUkJ1U1NaRHo4OUc0OUxPZ1ZjbUE?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQSlRmcnB2bWtXOHV1MEJucmRMSFpiMjUtM1dMUnVRbnBybWxCSWJ0YU02QVczWERwbDlNQzJSeThHVnRNUmEtd3dOQzRUQnJhT2V5WlhQczRYdVVGaUV3YVpaNUdvUkNqRDB0aWpDQW5IV0xtbF8zQjdGNm9xYlllMDRSYTZTLXNHMTJGLUNXYXhCMGx2R2drclQ5amZocWJndlE?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxPVG5Zd21HMzR5TWpzbzFac1RSOTJzQWRWTzZqSTNYVUZBMzFuWW9TeHNQTzBXZDlOamdnYjB1VlNNdXJMd29sRnpVZFEybjZWZXJfUHBhTlJ0bFhueE83UEstTFRiTWk1am9MZXNvbWd1UTI2b2t0MzU5OW9pRlJ2WmtJN2FkeG1vc1Q4Rzc0dFdhRTZQSzU3NEZzaXdSd3BOMGNtOGh5aVdOQXV3UmFpMm5B?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxQUVo4RktsemNtcXRGcngxbWgxVUFtcmRiQi1JOFQ5QlpiUzVVNVF0b296N3pJRW5saGthRlFQdVRuMEh2c1hNTURQcm9qOUZ5RGZvRDlobTZjU1pYT1lmajJuaUw3V1IwVVAtWTNBSWg4bFNpZjFrM20tdzJBcmZyUG95RzRZdlZObWg4SzRHYWc5TmpLeEZUMDg0RGhTeU02b1h1UDhkUHNGVkJNNUREZWVXVnNrOGt3dS1J?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
