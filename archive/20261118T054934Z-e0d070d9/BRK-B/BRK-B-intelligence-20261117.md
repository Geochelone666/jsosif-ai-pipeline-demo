# BRK-B Intelligence Report

- ticker: **BRK-B**
- Report as_of: **2026-11-17**
- Market data as_of: **2026-11-17**
- Quant sources: https://finance.yahoo.com/quote/BRK-B/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/BRK-B/key-statistics/
- AI analysis snapshot as_of: **2026-11-17**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-18T06:11:17.162032+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 1, 'ai': 20, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **12** exact headline/source/date matches; prior report **20261117T062519Z-6171f6c2/BRK-B** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 16 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-11-15

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 586.7600 |
| Return 1D (%) | -1.0272 |
| Return 1W (%) | 0.5863 |
| Return 1M (%) | 10.2891 |
| Return YTD (%) | 16.7333 |
| Return 1Y (%) | 16.5918 |
| Annualized volatility (%) | 14.9962 |
| Beta vs SPY | 0.0755 |
| Max drawdown (%) | -9.4218 |
| Sharpe (rf=0) | 1.1028 |
| Downside deviation (rf=0, %) | 10.0329 |
| Sortino (rf=0) | 1.6483 |
| Historical VaR 95% (1D, %) | 1.4122 |
| Historical ES 95% (1D, %) | 2.0016 |
| Correlation vs SPY | 0.0694 |
| Tracking error vs SPY (%) | 19.6499 |
| P/E (trailing) | 16.59 |
| P/B | 0.00 |
| EV/EBITDA | -2.04 |
| Revenue growth (%) | 11.20 |
| Forward P/E (estimate) | 25.72 |
| Gross margin (%) | 26.60 |
| Operating margin (%) | 26.60 |
| Return on equity (%) | 10.57 |
| Free cash flow yield (%) | 4.21 |
| MA50 | 533.0128 |
| Close vs MA50 (%) | 10.0837 |
| MA200 | 501.4929 |
| Close vs MA200 (%) | 17.0026 |
| RSI (14, Wilder) | 73.0920 |
| MACD (12,26) | 17.5714 |
| MACD signal (9) | 16.0181 |
| MACD histogram | 1.5533 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'BRK-B': 284, 'SPY': 284}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 586.7600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.0272 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.5863 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 10.2891 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 16.7333 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 16.5918 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 14.9962 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 10.0329 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.6483 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.4122 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.0016 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0694 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 19.6499 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.0755 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -9.4218 -> Shallow peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1028 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 25.7163 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 26.6020 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 26.6020 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 10.5740 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.2094 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 16.5892 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 73.0920 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.5533 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 10.0837 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 17.0026 -> Clearly above the moving-average trend level.

## TAILWINDS

### Berkshire Hathaway’s Stock Rally Puts Its Class A Shares Near the Historic $1M Mark
- Summary: Berkshire Hathaway’s Stock Rally Puts Its Class A Shares Near the Historic $1M Mark
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPVXBpWGFGejFjRVE5dVFHS0VHNmdUU2VTNFBBcEE1bDJudjczbEI0SW02YlJWbzk4R2h0Q0hZZ3pGa0FjNmdSdjlQeGEweno2NDNXVDlzOUJEYjFkdXh1eWpoejZHVFhFaGVWWUQ5SmRGamVkLVRfdDJiYld2NlZUTUVnbU50cHEwbFJNaVh4VlVlMFVYeFpNS2NERQ?oc=5>

### Berkshire Boosts Stake in Lennar, Doubling Down on Its U.S. Housing Bet
- Summary: Berkshire increases its stake in Lennar, reinforcing its U.S. housing investment strategy.
- Date: 2026-11-16 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxPaTMyWlBkeVVjYW5mWmZ0RFFmcE9KX1FJNnpxRDRnaEFpblpPS0FOQ1MyZE1hakZfRVhfTVZwX2owSUoxVGpvaUN1Q2xSUURBMWtJbzRySDRBLWZUTFMxOE5YMGVWYXd5b1hVMFpBd09vcFRvdGtfZmREUXJjbEdoUDZLTTlBcHB6NVlHQTY2Q3ZTRXRuY3lxVFd5YjRqNnBMcHZNUnJLU0trM2h1NEltd3Zobw?oc=5>

### How Investors Are Reacting To Berkshire Hathaway (BRK.A) $5.5 Billion Share Donation
- Summary: Investors react to Berkshire’s $5.5bn share donation.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxQWU4zS1Z3VU4zbmR5MWxPeWJjZzBKUlJOdXN5eENvamlJZEFsM1I0R21yWUJMTXAwN2l6THUyVlhzS0NYWmJEQjhQY210UVhWNGpNcjFtTndpWVE0eFg5MmYtd2pTYVI5eEpNa3NwT00zYXlmLVB5Y3l3Q0d3bXlKOXJOSmsza2RyR1lRcFZBMUt5OS1XY0hTbFRSQWdiZG5TR1doNnZrVkQwdw?oc=5>

## HEADWINDS

### Berkshire’s record high exposes hidden trap in S&P 500 401(k) plans
- Summary: Berkshire’s record high highlights a potential risk for 401(k) investors.
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMie0FVX3lxTFBrQ2xOVE1KellFRnE5a0JYVWhld3NMeVFxX1dEWUU2ZnZWck55WkFiQUlvSC1BWjZ1UGl6S09wV09Cb3VSLTc4N00zNlMzR2d2OFVuUzkwd3FVXzU5Q3NMS0ZocG53TGwwNXBpSXQ5T2Q3NDA0bVpBbXhoaw?oc=5>

## CATALYSTS

### Berkshire Hathaway Hits an All-Time High: Here’s What $10,000 Invested a Year Ago Is Worth Now
- Summary: Berkshire stock reaches record high, boosting $10k investment value.
- Date: 2026-11-16 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNd0hqNy1GWDNUU1BxVHhjYkpxOUVDTTFKczBzc3hMNFA3LTNWOExfRXJSOTlnSTJlLTZWQTZNeFZFR3kyazZIT3otRWxoRDB3d2hWQWNzYklLZFlLM2JlLUs1WmEtcVhKblhFS1locGdsSEZhNl9TandTUlUyR0pRSVZRNGhUMmhESUdfVEVpTmljZUJ4RldiSXpRTEFGMEU?oc=5>

### Here's What Berkshire Hathaway Bought and Sold in Q3
- Summary: Summary of Berkshire's Q3 acquisitions and divestitures.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNODdJLV9XbG85V0RTTi1lT2lZTm1KaWFVa2h6MnhXT21UWUlVenZWZFFnVW51Nk9LYWx4V2VPeW1TYlBzbUF6OGpTbWxSNGYtMVBGQklwMFUtenA0VFBRendROW9GRXNudnJGUlhubUhOZ2tPVDBTZ1dDeHFDOXg0ZXNaazlnajNGbnpwY3AzLWF0dw?oc=5>

### Warren Buffett's Berkshire Just Revealed a New Stock and Sold More Bank of America. Here's What a 68-Year-Old With 400 Shares Owns
- Summary: Berkshire disclosed a new stock and sold additional Bank of America shares.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMigAJBVV95cUxOeWtpeEZnSHpka2xZUlc5dEFJaG9Md3A5SXk5MXpVckhEb3dmWXZyODJxT1FScC1OZmF5dEgtNTB5ZFpRTjBFV0Vhbl8yU2w4VkNrOWI1MmlkZHRWZ0RTYmtUOTI0dnRjSGFjQUh0UG8xS2lyZ1NjMFdqb2hXWm80TlJTRGxtYXVfYUYwUnU1ZGhKc2xEZjFKWUlMY0Y4QllIUkpIRVZfeS00VWM1S3lPcXBWQThIbWh5SlVuamF0TTA3REVBdTR2Mkl2TzdJdVY2WjU2YndwalJlY3JjM2ZfY3FUWV92bXpWUDBXUTlmb1dzOFR4SElEVGg0YnZsT0ZQ?oc=5>

### Berkshire Hathaway (BRK.B) Reduced Its Stake in Bank of America During the Third Quarter
- Summary: Berkshire cuts Bank of America stake in Q3.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxNMUpQNVBxajZZcHBrc1gxZWwwQ3VTZmMxV3lVam5TUU1YSFNYLW9ENTIyNUtoNGRWcVdXcGg5VEFZWFFWQ0RhNzBHbUZLNFRZNFRSMjVfSUN2eHFiOXNKV3A4ZHdOYTB5ck5TUTU4VWM0V3dFV1huQTAzd0xDREx0bEFqMjBuUGNlUEs3amJvbjJhd3ViczlxOUxTWUtzdTQ4RkF1YURLYWVTckJ1MmlJVmMyYXBOblk?oc=5>

### Warren Buffett donates about $5.5 billion in Berkshire stock for Thanksgiving
- Summary: Buffett donates $5.5B of Berkshire shares for charity.
- Date: 2026-11-16 | Impact: low | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMif0FVX3lxTE9qdEJFcFBkQ3UwNUo4N3JxOFZnQkRrSkVQQi1QNVpZZHQtM3ptMERLaDVJUVAyS1hKRnNyZjBPNkh2QzNjSjBvbk1ZU1NhRjJtbnBBU25hY0FTZ2dvUWVDWGF2aWxvNWZOQ2d6aXpZZFkzTDRJREhBc3kxNHRvUFk?oc=5>

### Warren Buffett donates $5.2bn in Berkshire shares to family foundations
- Summary: Buffett donated $5.2bn of Berkshire shares to family foundations.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxNeVpmZUdqR2JKUGJPNjg1Q1E2NDlucFpobXMxU1phQXRDS0hhV1NDMHlrS1F2dmVIaVJyeGhFVjJteTZZY1BJSkpJOXpHLWdtQUZ5SWJOaUFZWVJzY2x6emRNT1JnTXVaSW93RWNxZ2NtQmJIZ1o5Qll3Zk9SMnVJR21mVW1VUjVsQ3BvQzN5ZTJsc3Y4X05DZHdfRUp3STZNQ3gwOVRUX0hiWjRLWkNuX1JkR3M2NmZrRU8tYlZ2aE1QU1RtQnN1b3pVNV9fY1BibW5PQVFn?oc=5>

### Warren Buffett’s Berkshire Just Revealed a New $689 Million Stock. The Company’s IPO Was Less Than Five Months Ago
- Summary: Berkshire Hathaway launched a new $689 million stock following an IPO less than five months ago.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQNy1zREdTaHR2aVMxWXgxR2FsSi12Si1xOVhPdFg2RC1TbnpBYllacHdsOTRyb1V0M2RHaHduc2pFWTh6UWJjVU5WclNHU2pad3hvaS1FU09tZEoxYk9wT2YzRGp2ekRQLV9wUkVHS0RKSmdyVGNDMmVvLWM4SUoxM256WEJkeGdiNUpFM0QxekRSTXN3M08xZE02TndHeVFxajg0ZF9n?oc=5>

### Warren Buffett’s Berkshire Nearly Doubled Its Stake in One Homebuilder Last Quarter. It Now Owns 26 Million Shares
- Summary: Berkshire Hathaway increased its stake in a homebuilder to 26 million shares, nearly doubling its previous holding.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxNUU5HY1NQWHB0M0Q2ZWpfczNSeEtXYm1GbWR6SXNmNWNiWHlZQ0toeENfSWZyOUlWblhhSkxONmNsZ2taZE9LeENaUm53TTFvcEZITDItV1JmR0o4QnZiYi1WQlhRdE1pSDREeVgyUlJBNGh6cmx6YkNWdUR0Q2NPU25GSnJsX0dSZzZzYUlZN2JCVE53dHlIVlJ6ZVJnS3BlRXcxSlZIQQ?oc=5>

### Berkshire Hathaway Slashes This Top 5 Stock; Nvidia Boosts SpaceX
- Summary: Berkshire sells a top 5 holding, indicating portfolio rebalancing.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxQWmtSdzA4SVl6UlZEclpaQVd2b2NSaXRLQWZDTzVIQ3dRYnU2elJoVEtmbFhWb0tMbVZiSVVnMHVSWHdRS3V2VW5uYmY3cnFWU1FHbmo1aF85QzFVY0VCVnRRcXZLSHFGNGlfWExtRlJpRU5idDgxMGlKWWlQdVhwZmkyZFVtVnNsTHc2SzVoXzR1R2xLXzVfMFJ1RnJCU2RJZDJj?oc=5>

### Berkshire Hathaway 13F: Sales Outweighed Purchases; Swapping Bank of America Stock for Lennar
- Summary: Portfolio shift: selling BofA, buying Lennar, net sales exceed purchases.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxQdmdiajF3SkI1V2Z0enpmcllyeGwxaE9iUTJMRXI3dEF1czZlekxONWppN1I1MkV6dUNmWVB6TVMtSVdYbThjTDNVZVUtZV9rYmE3bm00cEJ3VzBLa0Frbm1CZjJYSEtyUFB4dnl1NDBkTzBKZjdLNDZScVBaQjAxRHFZd05PUFJTRldnVWJJZWVOaUR3STlTaHVuZWltYUx2NVhWV2pNZ1lqQVZYdVhtWXVRZTd2dWJGMzd3?oc=5>

### Berkshire Executives Buy $2 Million in Stock With Shares Near Record
- Summary: Executives purchase $2M worth of shares, near record price.
- Date: 2026-11-17 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxObTQzbWFHcU5FR0Y5YmVZYnR3d2otWjNGRHVPYm9DbVdQM1dHTlpOcEFJOGJLT2NkX2J6cm44WUJkQzl1YnBXYTFHRHBNcVZWWUNyT2lxZHowT25tRkd2Tml2dnRReWdIZVB5WTNUVlZNVVZFQ0M1SzJnWjQ5VjFSU3BCRWktSHZZ?oc=5>

### Berkshire Hathaway Is Up 18% in Its First Year Without Buffett as CEO. Can BRK.B Stock Hit $700 by 2027?
- Summary: Berkshire’s stock surged 18% after Buffett’s departure, raising questions about future price targets.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxPM1dENGVxMWdITEZQTWNILUFtSGRGaUVmWF9tOEhzRXVncFJvLTAtSzFFdGlGVjNobUxzSTZhZUYyYVl0VFJTOTFNa1VjdnpJeHRRX2dUamk3QzN5VXZzaE5kQmM5MmY4dWdia3NPZG93TDY2WWE2MDBzOHY5bXdfc0ZvNHV0dE5uSUY3SU5Md0k2RzlzUHpMTXdXZk5HX05OSHc?oc=5>

### Warren Buffett Gives $5.4 Billion in Berkshire Shares to 4 Family Foundations— See Which One Gets the Mos
- Summary: Buffett transferred $5.4B of Berkshire shares to family foundations, a significant ownership shift.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAJBVV95cUxObHNrZldQUkx2YVRTWlA4WjFDS3VRR016Qm9VcmN3R2I4VkVfWi1pR0tCNEN4ajRxeEJLNm5OcUIzcG04cUozdU9BS3djOWM3dmwzVnhBQW9icmx6SjJjc21JZVZBQ3FpUTd2VTVjQm5iSFdTS1FVUHB5TFlMX3hoN1c1NUNySVE3N0VPTGVPSTZLQjhzTXl6aFJac003THN0bW5BemdKcnlWbVRiWEFDUFRSSGVjS2VtbHJRemtSbVVNVzI2ZmdVUDdqeW5zY3dzdkV1bXU4NWJkN1h6NWRzVE1jMU5wTU51V215cmtMUndreDBOc3NaTnRfeGxtcG0wZUhtQ2NnSk0zdjVvTHBhdmxVd0ozZlBac0VQdUpPMWI?oc=5>

### Could Nvidia Be Berkshire's Next Big Tech Purchase?
- Summary: Analysts speculate Berkshire might acquire Nvidia, indicating potential tech expansion.
- Date: 2026-11-17 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNTVVPdjRqcDRnT0o0blctbTFiQUlGZldlNHNNdXREZ0FJNmpob2JVWDJ3WW03Yndhb0VoLVZPOWczOEc3bUhrdVlvV3VJbjg0dUtWcTR2Y21FR0VaUGZUUElSQVQxZlB1N3ZwcUhDMExsVEJCM1RhOHYtYS1ibW5UX0VuT0xlSllBWWg3ZzhfamdUS2ZnT1kzSkVvV3B5QQ?oc=5>

### Warren Buffett donates over $5B of Berkshire Hathaway stock, says confidence ‘as strong as ever’
- Summary: Buffett donates more than $5 billion of Berkshire stock, signaling confidence in the company’s future.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNMXpzVU5NTmw2cVJQazB3ZDFTUW9FYUtTMUNlejVjbXFJT3VTOTQtUnRaZjVqYzhhQjA1NVRnRGhreHA5Q0RmQVpfVUdtNUU4OXNkZnl4Yk5xRXBKdk1kcFRMeFNkUFlnNnhyaFFNR1NfQnltdHZlTGtsaUVfby0yWUthbWlORDZUWjJsV0s4dnBXOGhQekh5OGJGblVIR28?oc=5>

### Warren Buffett's Successor, Greg Abel, Overhauled Berkshire's Portfolio for a 3rd Straight Quarter, Reducing 6 Stocks and Piling Into a Hot Tech IPO
- Summary: Abel trimmed six holdings and added a hot tech IPO, reshaping Berkshire’s portfolio for the third consecutive quarter.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQdU9FYXZwSllDTmRjTXM2RnItcmU0SXR2MElyRU1tNzdoX1paOFlueGN5TFAyc21aR09felFBbUkyb013Smw0ZjI3UW1wWFZ1UFdVS0s4VGtCSXRpYUpGcGZMM3cxY2VIOW5lOXAwWjVxdTE2eXA1SzhnUHRielBKYVAxUjdzZFFqTVhORnBHZWptMzNzckh0QU5XUTBQYnV4TFE?oc=5>

### Berkshire’s CFO Just Paid $888,869 a Share for Berkshire Stock
- Summary: Berkshire Hathaway’s CFO purchased its own shares for $888,869 each, signaling confidence and potentially boosting share value.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPUmp6Qk5nRGxqeDdZWHVvMnRJUFBfMmVoSWE2eWloNzJtOF9vSXlDWjVHS0xhVkYtN3BXQUlEOV8wQWl0NmhMR2VNYzRBWnBCbDVyT2pHMFZyX3lEdVI5dU8wX29DUVBNOXRYUHV5dkhtaG5PRUhVd21oLUJzYlp5MUdRaWpRUHJvN1ZEZ2ZLMFBSTjNLTHo4?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **BRK-B** | **16.59** | **0.00** | **-2.04** | **11.20** | **1,246,582,931,456.00 USD** | **16.59** |
| MKL | 13.93 | 1.30 | 8.01 | -11.20 | 23,938,981,888.00 USD | -4.18 |
| FFH.TO | 9.97 | 1.44 | 8.80 | 1.90 | 56,549,281,792.00 CAD | 16.58 |
| L | 15.24 | 1.22 | 8.65 | 1.90 | 22,285,219,840.00 USD | 5.99 |

Peers fetched as_of: 2026-11-17; BRK-B reuses existing data (market data as_of: 2026-11-17); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-07
- Next expected earnings: 2027-03-01 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-17

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

- https://news.google.com/rss/articles/CBMimwFBVV95cUxPVXBpWGFGejFjRVE5dVFHS0VHNmdUU2VTNFBBcEE1bDJudjczbEI0SW02YlJWbzk4R2h0Q0hZZ3pGa0FjNmdSdjlQeGEweno2NDNXVDlzOUJEYjFkdXh1eWpoejZHVFhFaGVWWUQ5SmRGamVkLVRfdDJiYld2NlZUTUVnbU50cHEwbFJNaVh4VlVlMFVYeFpNS2NERQ?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxPaTMyWlBkeVVjYW5mWmZ0RFFmcE9KX1FJNnpxRDRnaEFpblpPS0FOQ1MyZE1hakZfRVhfTVZwX2owSUoxVGpvaUN1Q2xSUURBMWtJbzRySDRBLWZUTFMxOE5YMGVWYXd5b1hVMFpBd09vcFRvdGtfZmREUXJjbEdoUDZLTTlBcHB6NVlHQTY2Q3ZTRXRuY3lxVFd5YjRqNnBMcHZNUnJLU0trM2h1NEltd3Zobw?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxQWU4zS1Z3VU4zbmR5MWxPeWJjZzBKUlJOdXN5eENvamlJZEFsM1I0R21yWUJMTXAwN2l6THUyVlhzS0NYWmJEQjhQY210UVhWNGpNcjFtTndpWVE0eFg5MmYtd2pTYVI5eEpNa3NwT00zYXlmLVB5Y3l3Q0d3bXlKOXJOSmsza2RyR1lRcFZBMUt5OS1XY0hTbFRSQWdiZG5TR1doNnZrVkQwdw?oc=5
- https://news.google.com/rss/articles/CBMie0FVX3lxTFBrQ2xOVE1KellFRnE5a0JYVWhld3NMeVFxX1dEWUU2ZnZWck55WkFiQUlvSC1BWjZ1UGl6S09wV09Cb3VSLTc4N00zNlMzR2d2OFVuUzkwd3FVXzU5Q3NMS0ZocG53TGwwNXBpSXQ5T2Q3NDA0bVpBbXhoaw?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNd0hqNy1GWDNUU1BxVHhjYkpxOUVDTTFKczBzc3hMNFA3LTNWOExfRXJSOTlnSTJlLTZWQTZNeFZFR3kyazZIT3otRWxoRDB3d2hWQWNzYklLZFlLM2JlLUs1WmEtcVhKblhFS1locGdsSEZhNl9TandTUlUyR0pRSVZRNGhUMmhESUdfVEVpTmljZUJ4RldiSXpRTEFGMEU?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNODdJLV9XbG85V0RTTi1lT2lZTm1KaWFVa2h6MnhXT21UWUlVenZWZFFnVW51Nk9LYWx4V2VPeW1TYlBzbUF6OGpTbWxSNGYtMVBGQklwMFUtenA0VFBRendROW9GRXNudnJGUlhubUhOZ2tPVDBTZ1dDeHFDOXg0ZXNaazlnajNGbnpwY3AzLWF0dw?oc=5
- https://news.google.com/rss/articles/CBMigAJBVV95cUxOeWtpeEZnSHpka2xZUlc5dEFJaG9Md3A5SXk5MXpVckhEb3dmWXZyODJxT1FScC1OZmF5dEgtNTB5ZFpRTjBFV0Vhbl8yU2w4VkNrOWI1MmlkZHRWZ0RTYmtUOTI0dnRjSGFjQUh0UG8xS2lyZ1NjMFdqb2hXWm80TlJTRGxtYXVfYUYwUnU1ZGhKc2xEZjFKWUlMY0Y4QllIUkpIRVZfeS00VWM1S3lPcXBWQThIbWh5SlVuamF0TTA3REVBdTR2Mkl2TzdJdVY2WjU2YndwalJlY3JjM2ZfY3FUWV92bXpWUDBXUTlmb1dzOFR4SElEVGg0YnZsT0ZQ?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxNMUpQNVBxajZZcHBrc1gxZWwwQ3VTZmMxV3lVam5TUU1YSFNYLW9ENTIyNUtoNGRWcVdXcGg5VEFZWFFWQ0RhNzBHbUZLNFRZNFRSMjVfSUN2eHFiOXNKV3A4ZHdOYTB5ck5TUTU4VWM0V3dFV1huQTAzd0xDREx0bEFqMjBuUGNlUEs3amJvbjJhd3ViczlxOUxTWUtzdTQ4RkF1YURLYWVTckJ1MmlJVmMyYXBOblk?oc=5
- https://news.google.com/rss/articles/CBMif0FVX3lxTE9qdEJFcFBkQ3UwNUo4N3JxOFZnQkRrSkVQQi1QNVpZZHQtM3ptMERLaDVJUVAyS1hKRnNyZjBPNkh2QzNjSjBvbk1ZU1NhRjJtbnBBU25hY0FTZ2dvUWVDWGF2aWxvNWZOQ2d6aXpZZFkzTDRJREhBc3kxNHRvUFk?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxNeVpmZUdqR2JKUGJPNjg1Q1E2NDlucFpobXMxU1phQXRDS0hhV1NDMHlrS1F2dmVIaVJyeGhFVjJteTZZY1BJSkpJOXpHLWdtQUZ5SWJOaUFZWVJzY2x6emRNT1JnTXVaSW93RWNxZ2NtQmJIZ1o5Qll3Zk9SMnVJR21mVW1VUjVsQ3BvQzN5ZTJsc3Y4X05DZHdfRUp3STZNQ3gwOVRUX0hiWjRLWkNuX1JkR3M2NmZrRU8tYlZ2aE1QU1RtQnN1b3pVNV9fY1BibW5PQVFn?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQNy1zREdTaHR2aVMxWXgxR2FsSi12Si1xOVhPdFg2RC1TbnpBYllacHdsOTRyb1V0M2RHaHduc2pFWTh6UWJjVU5WclNHU2pad3hvaS1FU09tZEoxYk9wT2YzRGp2ekRQLV9wUkVHS0RKSmdyVGNDMmVvLWM4SUoxM256WEJkeGdiNUpFM0QxekRSTXN3M08xZE02TndHeVFxajg0ZF9n?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxNUU5HY1NQWHB0M0Q2ZWpfczNSeEtXYm1GbWR6SXNmNWNiWHlZQ0toeENfSWZyOUlWblhhSkxONmNsZ2taZE9LeENaUm53TTFvcEZITDItV1JmR0o4QnZiYi1WQlhRdE1pSDREeVgyUlJBNGh6cmx6YkNWdUR0Q2NPU25GSnJsX0dSZzZzYUlZN2JCVE53dHlIVlJ6ZVJnS3BlRXcxSlZIQQ?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQWmtSdzA4SVl6UlZEclpaQVd2b2NSaXRLQWZDTzVIQ3dRYnU2elJoVEtmbFhWb0tMbVZiSVVnMHVSWHdRS3V2VW5uYmY3cnFWU1FHbmo1aF85QzFVY0VCVnRRcXZLSHFGNGlfWExtRlJpRU5idDgxMGlKWWlQdVhwZmkyZFVtVnNsTHc2SzVoXzR1R2xLXzVfMFJ1RnJCU2RJZDJj?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxQdmdiajF3SkI1V2Z0enpmcllyeGwxaE9iUTJMRXI3dEF1czZlekxONWppN1I1MkV6dUNmWVB6TVMtSVdYbThjTDNVZVUtZV9rYmE3bm00cEJ3VzBLa0Frbm1CZjJYSEtyUFB4dnl1NDBkTzBKZjdLNDZScVBaQjAxRHFZd05PUFJTRldnVWJJZWVOaUR3STlTaHVuZWltYUx2NVhWV2pNZ1lqQVZYdVhtWXVRZTd2dWJGMzd3?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxObTQzbWFHcU5FR0Y5YmVZYnR3d2otWjNGRHVPYm9DbVdQM1dHTlpOcEFJOGJLT2NkX2J6cm44WUJkQzl1YnBXYTFHRHBNcVZWWUNyT2lxZHowT25tRkd2Tml2dnRReWdIZVB5WTNUVlZNVVZFQ0M1SzJnWjQ5VjFSU3BCRWktSHZZ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxPM1dENGVxMWdITEZQTWNILUFtSGRGaUVmWF9tOEhzRXVncFJvLTAtSzFFdGlGVjNobUxzSTZhZUYyYVl0VFJTOTFNa1VjdnpJeHRRX2dUamk3QzN5VXZzaE5kQmM5MmY4dWdia3NPZG93TDY2WWE2MDBzOHY5bXdfc0ZvNHV0dE5uSUY3SU5Md0k2RzlzUHpMTXdXZk5HX05OSHc?oc=5
- https://news.google.com/rss/articles/CBMi3AFBVV95cUxQZXdGVjBqTEYxN3RnVkU3S0hIb2Z3Y25Vaks3NkhQQW9LZWZsVmpFdWdxTVlROHlydFU5LVFKd3BfN1I5RHZPUUNsa0hEdTd4Tms3aENCazBRQi10Y25FczVxTWFBN0NzNEwteWdYUEhybU15aTRVZERsQVozZFBpalg2Z3RTdVAxajFYU0lkRVZmelIzWU9XZHJDNzNHeGlhQ1ZOSTRra1YzYUNMT2taa2J2SHFCMG9nMU13dlFjS1dwalZ5MUowRGE5QXBmVm5jN2g2VW1DbEE3NFQw?oc=5
- https://news.google.com/rss/articles/CBMioAJBVV95cUxObHNrZldQUkx2YVRTWlA4WjFDS3VRR016Qm9VcmN3R2I4VkVfWi1pR0tCNEN4ajRxeEJLNm5OcUIzcG04cUozdU9BS3djOWM3dmwzVnhBQW9icmx6SjJjc21JZVZBQ3FpUTd2VTVjQm5iSFdTS1FVUHB5TFlMX3hoN1c1NUNySVE3N0VPTGVPSTZLQjhzTXl6aFJac003THN0bW5BemdKcnlWbVRiWEFDUFRSSGVjS2VtbHJRemtSbVVNVzI2ZmdVUDdqeW5zY3dzdkV1bXU4NWJkN1h6NWRzVE1jMU5wTU51V215cmtMUndreDBOc3NaTnRfeGxtcG0wZUhtQ2NnSk0zdjVvTHBhdmxVd0ozZlBac0VQdUpPMWI?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxNTVVPdjRqcDRnT0o0blctbTFiQUlGZldlNHNNdXREZ0FJNmpob2JVWDJ3WW03Yndhb0VoLVZPOWczOEc3bUhrdVlvV3VJbjg0dUtWcTR2Y21FR0VaUGZUUElSQVQxZlB1N3ZwcUhDMExsVEJCM1RhOHYtYS1ibW5UX0VuT0xlSllBWWg3ZzhfamdUS2ZnT1kzSkVvV3B5QQ?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNMXpzVU5NTmw2cVJQazB3ZDFTUW9FYUtTMUNlejVjbXFJT3VTOTQtUnRaZjVqYzhhQjA1NVRnRGhreHA5Q0RmQVpfVUdtNUU4OXNkZnl4Yk5xRXBKdk1kcFRMeFNkUFlnNnhyaFFNR1NfQnltdHZlTGtsaUVfby0yWUthbWlORDZUWjJsV0s4dnBXOGhQekh5OGJGblVIR28?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQdU9FYXZwSllDTmRjTXM2RnItcmU0SXR2MElyRU1tNzdoX1paOFlueGN5TFAyc21aR09felFBbUkyb013Smw0ZjI3UW1wWFZ1UFdVS0s4VGtCSXRpYUpGcGZMM3cxY2VIOW5lOXAwWjVxdTE2eXA1SzhnUHRielBKYVAxUjdzZFFqTVhORnBHZWptMzNzckh0QU5XUTBQYnV4TFE?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPUmp6Qk5nRGxqeDdZWHVvMnRJUFBfMmVoSWE2eWloNzJtOF9vSXlDWjVHS0xhVkYtN3BXQUlEOV8wQWl0NmhMR2VNYzRBWnBCbDVyT2pHMFZyX3lEdVI5dU8wX29DUVBNOXRYUHV5dkhtaG5PRUhVd21oLUJzYlp5MUdRaWpRUHJvN1ZEZ2ZLMFBSTjNLTHo4?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
