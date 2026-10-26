# T Intelligence Report

- ticker: **T**
- Report as_of: **2026-10-25**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/T/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/T/key-statistics/
- AI analysis snapshot as_of: **2026-10-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-26T01:00:25.330766+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 8, 'ai': 12, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 10 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 52.17%; oldest publication 2026-10-21

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 20.9300 |
| Return 1D (%) | -7.9595 |
| Return 1W (%) | -10.7082 |
| Return 1M (%) | -16.3375 |
| Return YTD (%) | -11.7205 |
| Return 1Y (%) | -10.9316 |
| Annualized volatility (%) | 28.7575 |
| Beta vs SPY | -0.3751 |
| Max drawdown (%) | -28.8854 |
| Sharpe (rf=0) | -0.2589 |
| Downside deviation (rf=0, %) | 22.1335 |
| Sortino (rf=0) | -0.3364 |
| Historical VaR 95% (1D, %) | 2.8546 |
| Historical ES 95% (1D, %) | 4.6484 |
| Correlation vs SPY | -0.1663 |
| Tracking error vs SPY (%) | 33.3371 |
| P/E (trailing) | 11.19 |
| P/B | 1.33 |
| EV/EBITDA | 7.16 |
| Revenue growth (%) | 5.30 |
| Forward P/E (estimate) | 8.07 |
| Gross margin (%) | 59.74 |
| Operating margin (%) | 24.65 |
| Return on equity (%) | 11.61 |
| Free cash flow yield (%) | 8.48 |
| MA50 | 24.5298 |
| Close vs MA50 (%) | -14.6751 |
| MA200 | 24.4921 |
| Close vs MA200 (%) | -14.5439 |
| RSI (14, Wilder) | 31.6518 |
| MACD (12,26) | -0.6732 |
| MACD signal (9) | -0.4982 |
| MACD histogram | -0.1750 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'T': 267, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 20.9300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -7.9595 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -10.7082 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -16.3375 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -11.7205 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -10.9316 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 28.7575 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 22.1335 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.3364 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8546 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.6484 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1663 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 33.3371 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.3751 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.8854 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.2589 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 8.0704 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 59.7420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 24.6520 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 11.6130 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 8.4838 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 11.1925 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 31.6518 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.1750 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -14.6751 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -14.5439 -> Clearly below the moving-average trend level.

## TAILWINDS

### AT&T Sinks 5% Despite Q3 Beat and Raised Outlook; Verizon and T-Mobile Drop 3%
- Summary: AT&T Sinks 5% Despite Q3 Beat and Raised Outlook; Verizon and T-Mobile Drop 3%
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxOaUJKUGstUVhON1ptalVFRWExNk9fR3NkZVNuYmxuMkF4NGxlbkJBYkxUeW1idVQzS3ZOeXJRdlpMbk50RFc5Y2dXVk52eXhaemp4dWJTVlFvVUV5d1FfVUNvb0JINGlxcDZrS2QwOWpJbzRCZzh6QXo5MGotN0tBTGRScW9xNUs4MTk3RW9B?oc=5>

## HEADWINDS

### AT&T Stock Drops as Starlink Fears Overshadow Earnings. What It Means for the Dividend.
- Summary: AT&T Stock Drops as Starlink Fears Overshadow Earnings. What It Means for the Dividend.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMidEFVX3lxTE1jUTBjWEpVOVlBLV9RWGVLaE9GT3BRaDFLcFJHR1l6Z1pWZDVlUkNfT0w5NVRacmlqRjJiSjhtUUVOSEZubmI1QUp3QTVrUzAyMUJpb25mcTZGSXFUV1dITHllSGxCbzQyU2tuSEVpamFuRzBn?oc=5>

### AT&T, Verizon, T-Mobile Shares Slip As SpaceX Reportedly Holds Cell Tower Talks For Starlink Mobile
- Summary: AT&T, Verizon, T-Mobile Shares Slip As SpaceX Reportedly Holds Cell Tower Talks For Starlink Mobile
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi5AFBVV95cUxORzZ2YUxFVlR5V2dHMHVudTZwZ2w1QS1aS1YxR3ZXZUtjZnZXYzd1VTJCYWFfU05JNlNkemVjZ2hGRjBGQ1NtT2ZWYmhsNzRVbVVicU81LUlOYS04cFBzWHVXUXpmUzJSbmEwUDRrUjA3QUdVQVE3dThIdnBrZEd6dzg3N2YxTFZCWko1WGtzLTJoU292LVZBVnczblkxaGFQa1RYWVdKbEo3WkRkRkszMTJIYWFaWjRTc2xiVEE0bEw1WncyNXFDU2tfTHJBR3FjdV9Dd2VoVjJwSy1sc195dHkwTk0?oc=5>

### AT&T (T) Stock Price Sinks As Q3 Results Spotlight Debt Tension
- Summary: AT&T (T) Stock Price Sinks As Q3 Results Spotlight Debt Tension
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxQWXhZbTZGcV9ZcWRjbWtnYzhUaTVHS3I2ZWUzU1BHNnFucjVIQjlLTHJfZEV2dzNWbERqVWhiMVNwZk1iMVVtR3BuY0JuQ3lTd0oxN0xfWGJ4NDcxdTZNSjFNRTdvZWpmcUNORWl3RkhRcloyb0p4STEzNmF5SHBHZXRmUTYzb19oblBzcXR4WQ?oc=5>

### AT&T Stock Sinks on Subscriber and SpaceX Worries. Is the Stock a Buy on the Dip?
- Summary: AT&T Stock Sinks on Subscriber and SpaceX Worries. Is the Stock a Buy on the Dip?
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOWUIwNUc2YTBxbDJBeXA5ZHhXV1lfUGlhd3RPYTdhWDRmQmtoMzQ3dEtzZ3Rzd2dRMktWMDRJVGdHVDVkdC1qbE0wWVhNTFVMRV9OVk14aWZ0UFcyUXhzUXlqbGpYS3JjTHo4dWFnZUtuZXpudlJDOW5TSHUtSHVWOVZmbEMyYzAtYkhGMU5feEVQQnk4dUR3aGdGeGI?oc=5>

### AT&T Stock Falls 13.4% in a Month. Is the Drop a Buying Opportunity?
- Summary: AT&T Stock Falls 13.4% in a Month. Is the Drop a Buying Opportunity?
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxPbldsRmVsWnpnTkZ0WWx1aHB1cFlXaEZGUlpPbENiUlNQR2wxMG91d09xYlkwczVTRWVTdHlDRkhfV3VGNGNpX3c2UkdwV3FSOGZGSjVHWWRNYWcwX3FkbGFyTXFZN21EZDB3ZFIyT0owbWxySjREa0R6SzRXR2ZKVThIeG9LLWZyVjdLUEs2VUZMdkJGS1Brb2FQWWs5WjBpM0hsVGZ4em84NkdnN3ZfMi1iTU5JUEVodkJ4Vw?oc=5>

### Why AT&T Stock Plunged on Friday
- Summary: AT&T shares fell sharply on Friday due to market concerns.
- Date: 2026-10-24 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOeDZaZ0RBRUZ2aDQ0TV9lUWtzWkNuUk81RFhOSUVZSVYtcExFazBhRlR5LXdVR1BESjdyTXlsekh3azNJRERnU0hINGpBdEFFRFhWZHoxOXVFY0JBbDlfUXRfakFPaG5rMy1Ub2JaVlVxTlJJQzhGcG53SkliNUl2a01UTUR0UGE1RWxzVFhpLV9aSGVZY2c?oc=5>

### T-Mobile, Verizon, and AT&T Stocks Are Falling After Hours — What Spooked Investors and What Wall Street Sees Next
- Summary: AT&T, T-Mobile, and Verizon stocks dropped after hours amid investor unease.
- Date: 2026-10-22 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxQdkFsUWEwRlYySENJSmdvWElsVUJ4WlFSV1lEU056VVZKSGtrajhreUFZR0V6b1pkUXFlTGh4aGowa0dGUkx3ellCbWdqemt6U0xaVnpLUWFTUTIyd3RGWEtMc21IVDhBdThCWU1PQWJXLVR5RUdQOVpiVmhxb1dVT1pqTVphRHREb0hOLXlSdzlONU9IUThaX3lTczZlN3BNWmJYRGdrdDRwV0xlVzhWcFdnVTBkYjBxVXJ0Sk1CMDZHNUdKSGxGSFF4ajM2eFVaems0ZG9n?oc=5>

### AT&T (T) stock trades down, here is why
- Summary: AT&T shares declined, with analysts citing recent factors.
- Date: 2026-10-21 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxNYUJRRlhFV2lBa3k1R2N2ZVhJbGRkOHptTFd0bkZ6X3puT1RjS2JUUl9abkVVY25xdXNjWmcxTUw3UUxsNnNxMFIwUG5EeUVNbXFEdWtpc3VibzBtU25vaWFvalpkVVYyUjFzSGxiYTY0cENjVFVJSWpRSng0emotd3lUOGlaOEN5RFlidERPNA?oc=5>

### What Just Happened To AT&T Stock?
- Summary: AT&T stock experienced a sudden drop, prompting questions.
- Date: 2026-10-25 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxQTXFZWnp5RUtLRTdjVDNjVkp5OHJoVEd0bW9MdXVLX0QzWkgxOFU0R2dQZWdhT0hYa0o5VWRkTW9xX0FZOE9JSGljVzNKSW9sZkxpcXpFd0FROE5YWjhJazVmbmVMMEl5ZlBjdVp0anlObjNhc2FqNEZFZHFZam0xZ3Z6bERqSk4ybTc3eE14S1R6SEU?oc=5>

### AT&T extends recent slump with another 8% retreat (T:NYSE)
- Summary: Stock price fell 8%, extending slump.
- Date: 2026-10-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxOYVlUZjJnTXBSZ3R0LVBzejFUcDQ5MklPeURDajNjR3BNLV96dXlDYU92U0QxTnlIVG92WE1oTlNOQW5ub0NNN2tRSzRzcGo2NUREdk51cFo2UW1oajN0akNBWWFuNFBZREhTdUg4d1BrTjgwb3Bua3U4Z2JVektQeG04NEVzNS1NS1VaR0Jn?oc=5>

### Stock Market Today, Oct. 23: AT&T Slides on SpaceX Cell-Site Talks
- Summary: Stock slid due to SpaceX cell-site talks.
- Date: 2026-10-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxOd05hZV9CR1JuTWw5ZUE3Q0pyU2gyaHp0cEFGQXYtS3MwSUdaV2JpN2E3a3E0VjlmUldBNWpjLVFyeDNiY3JnX1haTjhsY28xa2VpbFdXLU9TMk1RazhkOVRqX296dFZKNFVkWE84dnFWcVNicEhKcFFualpFS0pYSnpwWXI3QlVpdkhVQ2trckJQcUhIemp0aWV0MGxNQk91a0dpd0llVFJrdy1BVmJWcWtORU4zNUVmQ2VBY29nWGYtdkZXNzZV?oc=5>

### AT&T and Telecom Stocks Tumble as Musk Muscles In
- Summary: Stocks tumbled amid Musk’s involvement.
- Date: 2026-10-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMigwFBVV95cUxPeWRuQk5fMUpGNC1oSGdHcFdnSWtHMVJzRDZWZTJTblpwdXZoWFlZVmsxVU0xRzl1TTN3a2EtRVoxeG5kRzR3SWljdWp6Y01RaHZmZGlHMmNKU1hCdXY5dGoyMWtaeVc3Z3prVVVrSXNZQ2dkMzJVLWhYcDgxV3RTZkJBWQ?oc=5>

## CATALYSTS

### AT&T Wireless Subscriber Growth Underwhelms. Will It Spark iPhone 18 Battle?
- Summary: AT&T Wireless Subscriber Growth Underwhelms. Will It Spark iPhone 18 Battle?
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQY2tmVXBIMjFza1JXOUJkNFlkemtsY1dTY01kdXZYUGJTb1NZQUlMY1J5ZHI4VnNfXzJFbThRX2dwRG4yZkd3dU9WbnJKQzI5MGgxSXdmZDRFb04xZFRTX3ZleVB3dlpTXzFUcHhSWkpXa0FRanhZQWMwWlRZTldWNXk4a0dFbEI3XzBhdEhMTXJvWTdZM3FzNQ?oc=5>

### AT&T Froze Its Dividend After a 2022 Cut. Is Verizon the Better Income Stock?
- Summary: AT&T Froze Its Dividend After a 2022 Cut. Is Verizon the Better Income Stock?
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOZEY3UnREczR3LXNPRE00YkFzcFNLUV9EWk5vbE42RVVIbHFnYThud1ZnMVRKR1lZcUVfM21lanhqUXc4Y2dIeXBpZzU2QWJYRVN0VE10NUJfWjdQeEN5RXNpRFRIT3c2YjU5aU5hcl9wdU9NaHc3SHlxeVhIa05hWEppTnhtUE9XQ2xwcXZlV3JXallR?oc=5>

### Why Is AT&T Stock Falling Despite Beating Third-Quarter Earnings Estimates?
- Summary: AT&T beat Q3 earnings but stock fell, indicating market concerns beyond earnings.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOaFN0WUh2T2gyMFFWMDhDYm9KNEFoMkNyZTBjTGVQLWJaekp3dThYWVlyZmtaMXJ0Y0d6RFZwTWh4TFBsSXhwQjQwQUNBM19WNFo5UGRkU1JpbGowWDFaMW9zVTVXbk1FcVotMTdWck1CVUJZYXlVVVBQTTVmMTFHY04tcnJacnJnUHRJR25KaFU5VldzTWZz?oc=5>

### Why AT&T Stock is Tumbling Today
- Summary: AT&T stock dropped today despite recent earnings, reflecting investor uncertainty.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNNU5iLTdRbzFnTXlZNEgtOHA4RU9qRi05elJQR3kzMHlVMGVFaWZrVTRocURNTWVwSEJfX0lQRVRERjJVaTAya3dwTjVLTGJjYi1lTkY0eEtZUk91SXpuMjhNemx1dmphV3U3MjJUVkdoQjc2ZWVfQTRzdF8wQ0lTbHBjOEpFOEwxRXJNZkhXdkRVNWlkNGc?oc=5>

### What Should AT&T Stock Holders Take From Its Third Quarter?
- Summary: Analysis of AT&T's Q3 results for shareholders.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOaE9nY0dGMVFGQW5WRjJ1UjhmQlIybVBSUm5XRHRCY0F2VFFnMDc0MXVsT19jM1hOeG40dVlWdUh1NGNxdzY1YUloR0t6TUVQMkxGMVZnUUNRel9TT3lyMHdBWHFUOG5ia2thdk9ETDhlR2htZHRoS280b1h6M0NNME9ZOXQ3QjJGSUpNeXMtZjlST3REUGlEU25R?oc=5>

### Is AT&T Worth Buying as Fiber Growth Offsets Rising Leverage Risks?
- Summary: Analyst question on buying amid fiber growth and leverage risks.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxORWZjaThaczlMUEpPdEU2bG53VVhKb2VMNmRMc2h4eEtubVEzWHo2bk90aGxaZUc0b3dNWW51LUJWTjRwX3g4WC1hLUpiUXNoSzBCZkxzZjlQM050UF93bWM0eWRpbUtHQVZKU0l0Y1BuQ2hlV2VELVEyTWN4ZXhSclJOTmYzTXhoS3k5MmxHYXVVWG9CSjZV?oc=5>

### Telecom Stocks Fall as SpaceX Eyes 80,000 Cell Sites: T-Mobile Sinks 5%, AT&T Drops 4%, Verizon Slides 3%
- Summary: AT&T shares fell 4% amid broader telecom sell‑off linked to SpaceX’s cell‑site plans.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQeW9YX2JfMVZfN2FVVGZXWmdNS181YzFZaWU5elRHeFlpMmNWZGJ3eWUtcmtPWnl1cFEzZE1aa3lZYkMxM1lYWW93WWw4dzgyQUVuRUd3ZTZiSjdhRVh0Wk0xVndjU2hLdmJHR1FrMExCdFVubWM3QXJubnpXX2NJcUpJQnB0VDFYVlo2STBjYlJ3YUtDdU1vM1Ezb1Y?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **T** | **11.19** | **1.33** | **7.16** | **5.30** | **140,994,396,160.00 USD** | **-10.93** |
| VZ | 11.63 | 1.79 | 7.41 | -0.70 | 185,552,257,024.00 USD | 24.04 |
| TMUS | 15.31 | 2.80 | 8.00 | 7.90 | 157,189,292,032.00 USD | -31.98 |
| BCE | 4.18 | 1.29 | 7.34 | 1.50 | 19,023,525,888.00 USD | -9.92 |

Peers fetched as_of: 2026-10-25; T reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-25

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 32,322,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 891,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/732717/000073271726000372/t-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMijgFBVV95cUxOaUJKUGstUVhON1ptalVFRWExNk9fR3NkZVNuYmxuMkF4NGxlbkJBYkxUeW1idVQzS3ZOeXJRdlpMbk50RFc5Y2dXVk52eXhaemp4dWJTVlFvVUV5d1FfVUNvb0JINGlxcDZrS2QwOWpJbzRCZzh6QXo5MGotN0tBTGRScW9xNUs4MTk3RW9B?oc=5
- https://news.google.com/rss/articles/CBMidEFVX3lxTE1jUTBjWEpVOVlBLV9RWGVLaE9GT3BRaDFLcFJHR1l6Z1pWZDVlUkNfT0w5NVRacmlqRjJiSjhtUUVOSEZubmI1QUp3QTVrUzAyMUJpb25mcTZGSXFUV1dITHllSGxCbzQyU2tuSEVpamFuRzBn?oc=5
- https://news.google.com/rss/articles/CBMi5AFBVV95cUxORzZ2YUxFVlR5V2dHMHVudTZwZ2w1QS1aS1YxR3ZXZUtjZnZXYzd1VTJCYWFfU05JNlNkemVjZ2hGRjBGQ1NtT2ZWYmhsNzRVbVVicU81LUlOYS04cFBzWHVXUXpmUzJSbmEwUDRrUjA3QUdVQVE3dThIdnBrZEd6dzg3N2YxTFZCWko1WGtzLTJoU292LVZBVnczblkxaGFQa1RYWVdKbEo3WkRkRkszMTJIYWFaWjRTc2xiVEE0bEw1WncyNXFDU2tfTHJBR3FjdV9Dd2VoVjJwSy1sc195dHkwTk0?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxQWXhZbTZGcV9ZcWRjbWtnYzhUaTVHS3I2ZWUzU1BHNnFucjVIQjlLTHJfZEV2dzNWbERqVWhiMVNwZk1iMVVtR3BuY0JuQ3lTd0oxN0xfWGJ4NDcxdTZNSjFNRTdvZWpmcUNORWl3RkhRcloyb0p4STEzNmF5SHBHZXRmUTYzb19oblBzcXR4WQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOWUIwNUc2YTBxbDJBeXA5ZHhXV1lfUGlhd3RPYTdhWDRmQmtoMzQ3dEtzZ3Rzd2dRMktWMDRJVGdHVDVkdC1qbE0wWVhNTFVMRV9OVk14aWZ0UFcyUXhzUXlqbGpYS3JjTHo4dWFnZUtuZXpudlJDOW5TSHUtSHVWOVZmbEMyYzAtYkhGMU5feEVQQnk4dUR3aGdGeGI?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOdWdQQUNjMEM4M0xWVENjSVJmUFF4emdjd0NOcFEtTVV6dGxKZ3FPWDBZRjZMZm9iTDBOZnN5QV81aktkWTV2eW5IaTMwSUVIOE4yaTltZ0VmSzZFcGZJdjlXWkNnWEU4UFBCbHROOWZvN2xUalBQMlo1ak5iajhSSExLV1VLaWphRWlxZ1JneXVxUXVZSnJfRQ?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxPbldsRmVsWnpnTkZ0WWx1aHB1cFlXaEZGUlpPbENiUlNQR2wxMG91d09xYlkwczVTRWVTdHlDRkhfV3VGNGNpX3c2UkdwV3FSOGZGSjVHWWRNYWcwX3FkbGFyTXFZN21EZDB3ZFIyT0owbWxySjREa0R6SzRXR2ZKVThIeG9LLWZyVjdLUEs2VUZMdkJGS1Brb2FQWWs5WjBpM0hsVGZ4em84NkdnN3ZfMi1iTU5JUEVodkJ4Vw?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOeDZaZ0RBRUZ2aDQ0TV9lUWtzWkNuUk81RFhOSUVZSVYtcExFazBhRlR5LXdVR1BESjdyTXlsekh3azNJRERnU0hINGpBdEFFRFhWZHoxOXVFY0JBbDlfUXRfakFPaG5rMy1Ub2JaVlVxTlJJQzhGcG53SkliNUl2a01UTUR0UGE1RWxzVFhpLV9aSGVZY2c?oc=5
- https://news.google.com/rss/articles/CBMif0FVX3lxTFBqeWRleVNIT3JOR2duMEJ4T0xfZjZ4Y1ppMEpHSTlnajNvZzI5aUxYbWh6eDBwWFhmdlgydk0yT1NrSHdQY3NLemJrdE5uc1d6MkZuQ2VXa3htN183TjVHS1lSSUpKOTFxRkxuMGZPVmo0a3V4VHVQNVdPYnZlNEk?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxQdkFsUWEwRlYySENJSmdvWElsVUJ4WlFSV1lEU056VVZKSGtrajhreUFZR0V6b1pkUXFlTGh4aGowa0dGUkx3ellCbWdqemt6U0xaVnpLUWFTUTIyd3RGWEtMc21IVDhBdThCWU1PQWJXLVR5RUdQOVpiVmhxb1dVT1pqTVphRHREb0hOLXlSdzlONU9IUThaX3lTczZlN3BNWmJYRGdrdDRwV0xlVzhWcFdnVTBkYjBxVXJ0Sk1CMDZHNUdKSGxGSFF4ajM2eFVaems0ZG9n?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxNYUJRRlhFV2lBa3k1R2N2ZVhJbGRkOHptTFd0bkZ6X3puT1RjS2JUUl9abkVVY25xdXNjWmcxTUw3UUxsNnNxMFIwUG5EeUVNbXFEdWtpc3VibzBtU25vaWFvalpkVVYyUjFzSGxiYTY0cENjVFVJSWpRSng0emotd3lUOGlaOEN5RFlidERPNA?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxQTXFZWnp5RUtLRTdjVDNjVkp5OHJoVEd0bW9MdXVLX0QzWkgxOFU0R2dQZWdhT0hYa0o5VWRkTW9xX0FZOE9JSGljVzNKSW9sZkxpcXpFd0FROE5YWjhJazVmbmVMMEl5ZlBjdVp0anlObjNhc2FqNEZFZHFZam0xZ3Z6bERqSk4ybTc3eE14S1R6SEU?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxOYVlUZjJnTXBSZ3R0LVBzejFUcDQ5MklPeURDajNjR3BNLV96dXlDYU92U0QxTnlIVG92WE1oTlNOQW5ub0NNN2tRSzRzcGo2NUREdk51cFo2UW1oajN0akNBWWFuNFBZREhTdUg4d1BrTjgwb3Bua3U4Z2JVektQeG04NEVzNS1NS1VaR0Jn?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxOd05hZV9CR1JuTWw5ZUE3Q0pyU2gyaHp0cEFGQXYtS3MwSUdaV2JpN2E3a3E0VjlmUldBNWpjLVFyeDNiY3JnX1haTjhsY28xa2VpbFdXLU9TMk1RazhkOVRqX296dFZKNFVkWE84dnFWcVNicEhKcFFualpFS0pYSnpwWXI3QlVpdkhVQ2trckJQcUhIemp0aWV0MGxNQk91a0dpd0llVFJrdy1BVmJWcWtORU4zNUVmQ2VBY29nWGYtdkZXNzZV?oc=5
- https://news.google.com/rss/articles/CBMigwFBVV95cUxPeWRuQk5fMUpGNC1oSGdHcFdnSWtHMVJzRDZWZTJTblpwdXZoWFlZVmsxVU0xRzl1TTN3a2EtRVoxeG5kRzR3SWljdWp6Y01RaHZmZGlHMmNKU1hCdXY5dGoyMWtaeVc3Z3prVVVrSXNZQ2dkMzJVLWhYcDgxV3RTZkJBWQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQY2tmVXBIMjFza1JXOUJkNFlkemtsY1dTY01kdXZYUGJTb1NZQUlMY1J5ZHI4VnNfXzJFbThRX2dwRG4yZkd3dU9WbnJKQzI5MGgxSXdmZDRFb04xZFRTX3ZleVB3dlpTXzFUcHhSWkpXa0FRanhZQWMwWlRZTldWNXk4a0dFbEI3XzBhdEhMTXJvWTdZM3FzNQ?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOZEY3UnREczR3LXNPRE00YkFzcFNLUV9EWk5vbE42RVVIbHFnYThud1ZnMVRKR1lZcUVfM21lanhqUXc4Y2dIeXBpZzU2QWJYRVN0VE10NUJfWjdQeEN5RXNpRFRIT3c2YjU5aU5hcl9wdU9NaHc3SHlxeVhIa05hWEppTnhtUE9XQ2xwcXZlV3JXallR?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOaFN0WUh2T2gyMFFWMDhDYm9KNEFoMkNyZTBjTGVQLWJaekp3dThYWVlyZmtaMXJ0Y0d6RFZwTWh4TFBsSXhwQjQwQUNBM19WNFo5UGRkU1JpbGowWDFaMW9zVTVXbk1FcVotMTdWck1CVUJZYXlVVVBQTTVmMTFHY04tcnJacnJnUHRJR25KaFU5VldzTWZz?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNNU5iLTdRbzFnTXlZNEgtOHA4RU9qRi05elJQR3kzMHlVMGVFaWZrVTRocURNTWVwSEJfX0lQRVRERjJVaTAya3dwTjVLTGJjYi1lTkY0eEtZUk91SXpuMjhNemx1dmphV3U3MjJUVkdoQjc2ZWVfQTRzdF8wQ0lTbHBjOEpFOEwxRXJNZkhXdkRVNWlkNGc?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOaE9nY0dGMVFGQW5WRjJ1UjhmQlIybVBSUm5XRHRCY0F2VFFnMDc0MXVsT19jM1hOeG40dVlWdUh1NGNxdzY1YUloR0t6TUVQMkxGMVZnUUNRel9TT3lyMHdBWHFUOG5ia2thdk9ETDhlR2htZHRoS280b1h6M0NNME9ZOXQ3QjJGSUpNeXMtZjlST3REUGlEU25R?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxORWZjaThaczlMUEpPdEU2bG53VVhKb2VMNmRMc2h4eEtubVEzWHo2bk90aGxaZUc0b3dNWW51LUJWTjRwX3g4WC1hLUpiUXNoSzBCZkxzZjlQM050UF93bWM0eWRpbUtHQVZKU0l0Y1BuQ2hlV2VELVEyTWN4ZXhSclJOTmYzTXhoS3k5MmxHYXVVWG9CSjZV?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQeW9YX2JfMVZfN2FVVGZXWmdNS181YzFZaWU5elRHeFlpMmNWZGJ3eWUtcmtPWnl1cFEzZE1aa3lZYkMxM1lYWW93WWw4dzgyQUVuRUd3ZTZiSjdhRVh0Wk0xVndjU2hLdmJHR1FrMExCdFVubWM3QXJubnpXX2NJcUpJQnB0VDFYVlo2STBjYlJ3YUtDdU1vM1Ezb1Y?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
