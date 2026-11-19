# BRK-B Intelligence Report

- ticker: **BRK-B**
- Report as_of: **2026-11-18**
- Market data as_of: **2026-11-18**
- Quant sources: https://finance.yahoo.com/quote/BRK-B/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/BRK-B/key-statistics/
- AI analysis snapshot as_of: **2026-11-18**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-19T05:56:05.000007+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 1, 'ai': 16, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261118T054934Z-e0d070d9/BRK-B** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'directional_claim_without_event_type': 1, 'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 16 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 30.43%; oldest publication 2026-11-14

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 574.6200 |
| Return 1D (%) | -2.0690 |
| Return 1W (%) | -2.3154 |
| Return 1M (%) | 8.0072 |
| Return YTD (%) | 14.3181 |
| Return 1Y (%) | 13.9283 |
| Annualized volatility (%) | 15.1470 |
| Beta vs SPY | 0.0805 |
| Max drawdown (%) | -9.4218 |
| Sharpe (rf=0) | 0.9400 |
| Downside deviation (rf=0, %) | 10.2448 |
| Sortino (rf=0) | 1.3898 |
| Historical VaR 95% (1D, %) | 1.4206 |
| Historical ES 95% (1D, %) | 2.0519 |
| Correlation vs SPY | 0.0731 |
| Tracking error vs SPY (%) | 19.7027 |
| P/E (trailing) | 16.08 |
| P/B | 0.00 |
| EV/EBITDA | -2.04 |
| Revenue growth (%) | 11.20 |
| Forward P/E (estimate) | 25.18 |
| Gross margin (%) | 26.60 |
| Operating margin (%) | 26.60 |
| Return on equity (%) | 10.57 |
| Free cash flow yield (%) | 4.30 |
| MA50 | 534.3708 |
| Close vs MA50 (%) | 7.5321 |
| MA200 | 501.8974 |
| Close vs MA200 (%) | 14.4895 |
| RSI (14, Wilder) | 60.6785 |
| MACD (12,26) | 16.0062 |
| MACD signal (9) | 16.0157 |
| MACD histogram | -0.0096 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'BRK-B': 285, 'SPY': 285}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 574.6200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.0690 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.3154 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 8.0072 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 14.3181 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 13.9283 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 15.1470 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 10.2448 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.3898 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.4206 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.0519 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0731 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 19.7027 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.0805 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -9.4218 -> Shallow peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9400 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 25.1843 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 26.6020 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 26.6020 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 10.5740 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.2984 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 16.0823 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 60.6785 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.0096 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 7.5321 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 14.4895 -> Clearly above the moving-average trend level.

## TAILWINDS

### Berkshire Hathaway’s Stock Rally Puts Its Class A Shares Near the Historic $1M Mark
- Summary: Berkshire Hathaway’s Stock Rally Puts Its Class A Shares Near the Historic $1M Mark
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPVXBpWGFGejFjRVE5dVFHS0VHNmdUU2VTNFBBcEE1bDJudjczbEI0SW02YlJWbzk4R2h0Q0hZZ3pGa0FjNmdSdjlQeGEweno2NDNXVDlzOUJEYjFkdXh1eWpoejZHVFhFaGVWWUQ5SmRGamVkLVRfdDJiYld2NlZUTUVnbU50cHEwbFJNaVh4VlVlMFVYeFpNS2NERQ?oc=5>

### Warren Buffett to Donate $5.4 Billion of Berkshire Hathaway Stock to Family Foundations
- Summary: Buffett will give $5.4B of Berkshire stock to family foundations, a philanthropic move.
- Date: 2026-11-16 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxNNGlvLVVuUXAzSXJWd0xyNnVacDZJOHBSQ29XSERtaE1nUDhsbXlmVnkzQjlYMmdLWGFQc1EyN1pyY0p0M1h1eXhmOXNJNEJLOFBaUGFBVWVoWmdNeE1QeFlhdGJhY0hVUHVJWFZfSUVsdTFfejMzVTFVVlF4QTYyMEs1QlVodnQtYk5UWFlOSkFmT0YyVjBUZVFhQkkzTURBOWg0QTZuc00zaUlOdGZJOERVOHktemxDdHhSUEYzekM?oc=5>

### Berkshire Hathaway Is Up 18% in Its First Year Without Buffett as CEO. Can BRK.B Stock Hit $700 by 2027?
- Summary: Berkshire's 18% year‑over‑year gain signals strong momentum, raising 2027 price target prospects.
- Date: 2026-11-17 | Impact: high | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxPM1dENGVxMWdITEZQTWNILUFtSGRGaUVmWF9tOEhzRXVncFJvLTAtSzFFdGlGVjNobUxzSTZhZUYyYVl0VFJTOTFNa1VjdnpJeHRRX2dUamk3QzN5VXZzaE5kQmM5MmY4dWdia3NPZG93TDY2WWE2MDBzOHY5bXdfc0ZvNHV0dE5uSUY3SU5Md0k2RzlzUHpMTXdXZk5HX05OSHc?oc=5>

## HEADWINDS

### Warren Buffett's Successor, Greg Abel, Just Dropped a $426 Million Bombshell on Wall Street
- Summary: Abel released a $426M announcement, potentially unsettling markets.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxQM0gycUNHMXhuQW1kaGdyT0xreEg3My1HdG5xUFFQSVVSVlJ5TDlXbzFQS1ROcjM5ekIxZnVUQy1CR2pKcEU2RVFKX2pkdWlSSHlHZTRJX0lzOUd1Zkx6ZUc1NXVxMmdmVlhselBROXZKSlZoZzRrZ0JUTG96YWR3dGp4WFAtX20yUDQ1VEJHUWo1RDJTcjU4cUVlSFZyM2NaSFg1Rk50WTJrTks1djlhWUNGUjFIR2dGNzhhYXRPM1dXN2IzeERyZA?oc=5>

## CATALYSTS

### Berkshire Hathaway Slashes This Top 5 Stock; Nvidia Boosts SpaceX
- Summary: Berkshire sells a top 5 holding, indicating portfolio rebalancing.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxQWmtSdzA4SVl6UlZEclpaQVd2b2NSaXRLQWZDTzVIQ3dRYnU2elJoVEtmbFhWb0tMbVZiSVVnMHVSWHdRS3V2VW5uYmY3cnFWU1FHbmo1aF85QzFVY0VCVnRRcXZLSHFGNGlfWExtRlJpRU5idDgxMGlKWWlQdVhwZmkyZFVtVnNsTHc2SzVoXzR1R2xLXzVfMFJ1RnJCU2RJZDJj?oc=5>

### Berkshire Hathaway 13F: Sales Outweighed Purchases; Swapping Bank of America Stock for Lennar
- Summary: Portfolio shift: selling BofA, buying Lennar, net sales exceed purchases.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxQdmdiajF3SkI1V2Z0enpmcllyeGwxaE9iUTJMRXI3dEF1czZlekxONWppN1I1MkV6dUNmWVB6TVMtSVdYbThjTDNVZVUtZV9rYmE3bm00cEJ3VzBLa0Frbm1CZjJYSEtyUFB4dnl1NDBkTzBKZjdLNDZScVBaQjAxRHFZd05PUFJTRldnVWJJZWVOaUR3STlTaHVuZWltYUx2NVhWV2pNZ1lqQVZYdVhtWXVRZTd2dWJGMzd3?oc=5>

### Here's What Berkshire Hathaway Bought and Sold in Q3
- Summary: Summary of Berkshire's Q3 acquisitions and divestitures.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNODdJLV9XbG85V0RTTi1lT2lZTm1KaWFVa2h6MnhXT21UWUlVenZWZFFnVW51Nk9LYWx4V2VPeW1TYlBzbUF6OGpTbWxSNGYtMVBGQklwMFUtenA0VFBRendROW9GRXNudnJGUlhubUhOZ2tPVDBTZ1dDeHFDOXg0ZXNaazlnajNGbnpwY3AzLWF0dw?oc=5>

### Berkshire Hathaway (BRK.B) Reduced Its Stake in Bank of America During the Third Quarter
- Summary: Berkshire cuts Bank of America stake in Q3.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxNMUpQNVBxajZZcHBrc1gxZWwwQ3VTZmMxV3lVam5TUU1YSFNYLW9ENTIyNUtoNGRWcVdXcGg5VEFZWFFWQ0RhNzBHbUZLNFRZNFRSMjVfSUN2eHFiOXNKV3A4ZHdOYTB5ck5TUTU4VWM0V3dFV1huQTAzd0xDREx0bEFqMjBuUGNlUEs3amJvbjJhd3ViczlxOUxTWUtzdTQ4RkF1YURLYWVTckJ1MmlJVmMyYXBOblk?oc=5>

### Warren Buffett donates about $5.5 billion in Berkshire stock for Thanksgiving
- Summary: Buffett donates $5.5B of Berkshire shares for charity.
- Date: 2026-11-16 | Impact: low | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMif0FVX3lxTE9qdEJFcFBkQ3UwNUo4N3JxOFZnQkRrSkVQQi1QNVpZZHQtM3ptMERLaDVJUVAyS1hKRnNyZjBPNkh2QzNjSjBvbk1ZU1NhRjJtbnBBU25hY0FTZ2dvUWVDWGF2aWxvNWZOQ2d6aXpZZFkzTDRJREhBc3kxNHRvUFk?oc=5>

### Warren Buffett Gives $5.4 Billion in Berkshire Shares to 4 Family Foundations— See Which One Gets the Mos
- Summary: Buffett transferred $5.4B of Berkshire shares to family foundations, a significant ownership shift.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAJBVV95cUxObHNrZldQUkx2YVRTWlA4WjFDS3VRR016Qm9VcmN3R2I4VkVfWi1pR0tCNEN4ajRxeEJLNm5OcUIzcG04cUozdU9BS3djOWM3dmwzVnhBQW9icmx6SjJjc21JZVZBQ3FpUTd2VTVjQm5iSFdTS1FVUHB5TFlMX3hoN1c1NUNySVE3N0VPTGVPSTZLQjhzTXl6aFJac003THN0bW5BemdKcnlWbVRiWEFDUFRSSGVjS2VtbHJRemtSbVVNVzI2ZmdVUDdqeW5zY3dzdkV1bXU4NWJkN1h6NWRzVE1jMU5wTU51V215cmtMUndreDBOc3NaTnRfeGxtcG0wZUhtQ2NnSk0zdjVvTHBhdmxVd0ozZlBac0VQdUpPMWI?oc=5>

### Warren Buffett donates $5.2bn in Berkshire shares to family foundations
- Summary: Buffett donated $5.2bn of Berkshire shares to family foundations.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxNeVpmZUdqR2JKUGJPNjg1Q1E2NDlucFpobXMxU1phQXRDS0hhV1NDMHlrS1F2dmVIaVJyeGhFVjJteTZZY1BJSkpJOXpHLWdtQUZ5SWJOaUFZWVJzY2x6emRNT1JnTXVaSW93RWNxZ2NtQmJIZ1o5Qll3Zk9SMnVJR21mVW1VUjVsQ3BvQzN5ZTJsc3Y4X05DZHdfRUp3STZNQ3gwOVRUX0hiWjRLWkNuX1JkR3M2NmZrRU8tYlZ2aE1QU1RtQnN1b3pVNV9fY1BibW5PQVFn?oc=5>

### Berkshire Hathaway Hits an All-Time High: Here’s What $10,000 Invested a Year Ago Is Worth Now
- Summary: Berkshire stock reaches record high, boosting $10k investment value.
- Date: 2026-11-16 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNd0hqNy1GWDNUU1BxVHhjYkpxOUVDTTFKczBzc3hMNFA3LTNWOExfRXJSOTlnSTJlLTZWQTZNeFZFR3kyazZIT3otRWxoRDB3d2hWQWNzYklLZFlLM2JlLUs1WmEtcVhKblhFS1locGdsSEZhNl9TandTUlUyR0pRSVZRNGhUMmhESUdfVEVpTmljZUJ4RldiSXpRTEFGMEU?oc=5>

### Berkshire reveals new $689 million stake in major tech stock
- Summary: Berkshire invests $689M in a major tech company, expanding its portfolio.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxNbDJTbl8wdkZhbjNvWTRxQWg0NUhONDF2UnhBN01Jd1NiTzhOVmljTG1sbllNLXMweC0yTXEwNXpjZC1BSXFwT29nalBDSHQ1VGZWUTBkOU9JUTZXWTVCNnRUaXFENk1mTTVOdURJZXRCNmVZVXZlaHdNQ2Y4XzNzUlNJSHZrdUgxYVBNYlhCcHZsNWpVckwwMDZzMDU1UkstUHRfNFRrLS1fTVZieTI0RkJzeE1Vd3Rr?oc=5>

### Berkshire Hathaway (BRK.B) Reveals New Stake And Nearly Doubles One Holding
- Summary: Berkshire doubles a holding, adding a significant stake to its holdings.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPdVhDY2h0djVhZ3dwUXNPSHg3TFFhT1NFUnVvNWpHanZ5M1kzS3JrSENsdlQzNmhHZUJJUjdNc2NXam1LSTdjV0VEZXNneS1Vc2RrZTR2Q1dvREUwUHUxUmJheDJjY1lQTV9zOFlfQ0Z1ZXJiTDJueGdXRnRobzNWQ3pVRmpWcW9tYnY4d0dwZjhuU1dGYUpFQ0VBbDVWQQ?oc=5>

### Warren Buffett Just Gave Away $5.5 Billion of Berkshire Stock. He Says His Confidence in Berkshire Is "As Strong as Ever."
- Summary: Buffett distributes $5.5B of Berkshire shares, signaling strong confidence.
- Date: 2026-11-18 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPZWE3aFRHaTlWWkdRRUxteUdMX1pOSVRBc1NlNmZTMFZlMEdMeHVQRDdSY1JfNlZHMVRZaHJNdkthM3ByYm1udHVFMVROVHhuVk82eGJtcFVXS3pDOTdrQmRfa0dEQ0lTUlNGcW1GenlDQ2QyWGt5dGVuaFNMRmNIQzBaMkt4c1JoenBsQlhEeTBXMmxNR3l0cFlR?oc=5>

### Berkshire breaks out to record high with fourth-quarter rally reaching 19%
- Summary: Berkshire’s stock surges 19% in Q4 rally, hitting record highs.
- Date: 2026-11-14 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxQbUV4NF9lbkt0WEpneTdsTUFfMDE2dklud1lnVnFPR0YtWGNTck9NbUNJZHk2WWtIeERxXzQ5VWdUTzNDNGRnb2Npd3h0SEp2aVc2VmszQ2lXUjVjZ1lrMEtoSTRYdXJFM0d1TnNNV0ROV1R5VFN5RjJoZjgtWlZBM0lsVnpydV82a1BVQmZibTdaNDA0WFpQMklSaHMwZEtmZ0FhSHM3a0VLQXpwTHFBRHVFMWFaRGZ10gG-AUFVX3lxTE0ycGVWQ2xHWWV0U2xFdWpmbkZiWVhMR2tlQy0wNFlvMXZ0ejlHU0IyNE85Yk0wSjdXODRpSTF4MkZJYXpqMTBSRlZFakhHTjdGSXNpcFZKRHVNcWk0YW5EanM4cW1iYU1oR29PVVYyODUwajRjSjZiR0VFdDdlbWZkUXFXanNTby1fYl9hdkFzVHFKUy1lQXZlUkNzRWNENElhUXBfU0Z1NVdpcXZwM0RVRXpTT3BtQy11QnFGc0E?oc=5>

### Berkshire Executives Buy $2 Million in Stock With Shares Near a Record
- Summary: Berkshire Hathaway executives purchased $2 million of the company's stock as share prices approached a record high.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxObTQzbWFHcU5FR0Y5YmVZYnR3d2otWjNGRHVPYm9DbVdQM1dHTlpOcEFJOGJLT2NkX2J6cm44WUJkQzl1YnBXYTFHRHBNcVZWWUNyT2lxZHowT25tRkd2Tml2dnRReWdIZVB5WTNUVlZNVVZFQ0M1SzJnWjQ5VjFSU3BCRWktSHZZ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **BRK-B** | **16.08** | **0.00** | **-2.04** | **11.20** | **1,220,791,238,656.00 USD** | **13.93** |
| MKL | 13.81 | 1.28 | 7.93 | -11.20 | 23,727,046,656.00 USD | -5.48 |
| FFH.TO | 9.86 | 1.42 | 8.72 | 1.90 | 55,879,794,688.00 CAD | 15.22 |
| L | 15.21 | 1.22 | 8.63 | 1.90 | 22,240,731,136.00 USD | 4.86 |

Peers fetched as_of: 2026-11-18; BRK-B reuses existing data (market data as_of: 2026-11-18); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-07
- Next expected earnings: 2027-03-01 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-18

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
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxNNGlvLVVuUXAzSXJWd0xyNnVacDZJOHBSQ29XSERtaE1nUDhsbXlmVnkzQjlYMmdLWGFQc1EyN1pyY0p0M1h1eXhmOXNJNEJLOFBaUGFBVWVoWmdNeE1QeFlhdGJhY0hVUHVJWFZfSUVsdTFfejMzVTFVVlF4QTYyMEs1QlVodnQtYk5UWFlOSkFmT0YyVjBUZVFhQkkzTURBOWg0QTZuc00zaUlOdGZJOERVOHktemxDdHhSUEYzekM?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxPM1dENGVxMWdITEZQTWNILUFtSGRGaUVmWF9tOEhzRXVncFJvLTAtSzFFdGlGVjNobUxzSTZhZUYyYVl0VFJTOTFNa1VjdnpJeHRRX2dUamk3QzN5VXZzaE5kQmM5MmY4dWdia3NPZG93TDY2WWE2MDBzOHY5bXdfc0ZvNHV0dE5uSUY3SU5Md0k2RzlzUHpMTXdXZk5HX05OSHc?oc=5
- https://news.google.com/rss/articles/CBMi3AFBVV95cUxQZXdGVjBqTEYxN3RnVkU3S0hIb2Z3Y25Vaks3NkhQQW9LZWZsVmpFdWdxTVlROHlydFU5LVFKd3BfN1I5RHZPUUNsa0hEdTd4Tms3aENCazBRQi10Y25FczVxTWFBN0NzNEwteWdYUEhybU15aTRVZERsQVozZFBpalg2Z3RTdVAxajFYU0lkRVZmelIzWU9XZHJDNzNHeGlhQ1ZOSTRra1YzYUNMT2taa2J2SHFCMG9nMU13dlFjS1dwalZ5MUowRGE5QXBmVm5jN2g2VW1DbEE3NFQw?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxQM0gycUNHMXhuQW1kaGdyT0xreEg3My1HdG5xUFFQSVVSVlJ5TDlXbzFQS1ROcjM5ekIxZnVUQy1CR2pKcEU2RVFKX2pkdWlSSHlHZTRJX0lzOUd1Zkx6ZUc1NXVxMmdmVlhselBROXZKSlZoZzRrZ0JUTG96YWR3dGp4WFAtX20yUDQ1VEJHUWo1RDJTcjU4cUVlSFZyM2NaSFg1Rk50WTJrTks1djlhWUNGUjFIR2dGNzhhYXRPM1dXN2IzeERyZA?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQWmtSdzA4SVl6UlZEclpaQVd2b2NSaXRLQWZDTzVIQ3dRYnU2elJoVEtmbFhWb0tMbVZiSVVnMHVSWHdRS3V2VW5uYmY3cnFWU1FHbmo1aF85QzFVY0VCVnRRcXZLSHFGNGlfWExtRlJpRU5idDgxMGlKWWlQdVhwZmkyZFVtVnNsTHc2SzVoXzR1R2xLXzVfMFJ1RnJCU2RJZDJj?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxQdmdiajF3SkI1V2Z0enpmcllyeGwxaE9iUTJMRXI3dEF1czZlekxONWppN1I1MkV6dUNmWVB6TVMtSVdYbThjTDNVZVUtZV9rYmE3bm00cEJ3VzBLa0Frbm1CZjJYSEtyUFB4dnl1NDBkTzBKZjdLNDZScVBaQjAxRHFZd05PUFJTRldnVWJJZWVOaUR3STlTaHVuZWltYUx2NVhWV2pNZ1lqQVZYdVhtWXVRZTd2dWJGMzd3?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNODdJLV9XbG85V0RTTi1lT2lZTm1KaWFVa2h6MnhXT21UWUlVenZWZFFnVW51Nk9LYWx4V2VPeW1TYlBzbUF6OGpTbWxSNGYtMVBGQklwMFUtenA0VFBRendROW9GRXNudnJGUlhubUhOZ2tPVDBTZ1dDeHFDOXg0ZXNaazlnajNGbnpwY3AzLWF0dw?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxNMUpQNVBxajZZcHBrc1gxZWwwQ3VTZmMxV3lVam5TUU1YSFNYLW9ENTIyNUtoNGRWcVdXcGg5VEFZWFFWQ0RhNzBHbUZLNFRZNFRSMjVfSUN2eHFiOXNKV3A4ZHdOYTB5ck5TUTU4VWM0V3dFV1huQTAzd0xDREx0bEFqMjBuUGNlUEs3amJvbjJhd3ViczlxOUxTWUtzdTQ4RkF1YURLYWVTckJ1MmlJVmMyYXBOblk?oc=5
- https://news.google.com/rss/articles/CBMif0FVX3lxTE9qdEJFcFBkQ3UwNUo4N3JxOFZnQkRrSkVQQi1QNVpZZHQtM3ptMERLaDVJUVAyS1hKRnNyZjBPNkh2QzNjSjBvbk1ZU1NhRjJtbnBBU25hY0FTZ2dvUWVDWGF2aWxvNWZOQ2d6aXpZZFkzTDRJREhBc3kxNHRvUFk?oc=5
- https://news.google.com/rss/articles/CBMioAJBVV95cUxObHNrZldQUkx2YVRTWlA4WjFDS3VRR016Qm9VcmN3R2I4VkVfWi1pR0tCNEN4ajRxeEJLNm5OcUIzcG04cUozdU9BS3djOWM3dmwzVnhBQW9icmx6SjJjc21JZVZBQ3FpUTd2VTVjQm5iSFdTS1FVUHB5TFlMX3hoN1c1NUNySVE3N0VPTGVPSTZLQjhzTXl6aFJac003THN0bW5BemdKcnlWbVRiWEFDUFRSSGVjS2VtbHJRemtSbVVNVzI2ZmdVUDdqeW5zY3dzdkV1bXU4NWJkN1h6NWRzVE1jMU5wTU51V215cmtMUndreDBOc3NaTnRfeGxtcG0wZUhtQ2NnSk0zdjVvTHBhdmxVd0ozZlBac0VQdUpPMWI?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxNeVpmZUdqR2JKUGJPNjg1Q1E2NDlucFpobXMxU1phQXRDS0hhV1NDMHlrS1F2dmVIaVJyeGhFVjJteTZZY1BJSkpJOXpHLWdtQUZ5SWJOaUFZWVJzY2x6emRNT1JnTXVaSW93RWNxZ2NtQmJIZ1o5Qll3Zk9SMnVJR21mVW1VUjVsQ3BvQzN5ZTJsc3Y4X05DZHdfRUp3STZNQ3gwOVRUX0hiWjRLWkNuX1JkR3M2NmZrRU8tYlZ2aE1QU1RtQnN1b3pVNV9fY1BibW5PQVFn?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNd0hqNy1GWDNUU1BxVHhjYkpxOUVDTTFKczBzc3hMNFA3LTNWOExfRXJSOTlnSTJlLTZWQTZNeFZFR3kyazZIT3otRWxoRDB3d2hWQWNzYklLZFlLM2JlLUs1WmEtcVhKblhFS1locGdsSEZhNl9TandTUlUyR0pRSVZRNGhUMmhESUdfVEVpTmljZUJ4RldiSXpRTEFGMEU?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxNbDJTbl8wdkZhbjNvWTRxQWg0NUhONDF2UnhBN01Jd1NiTzhOVmljTG1sbllNLXMweC0yTXEwNXpjZC1BSXFwT29nalBDSHQ1VGZWUTBkOU9JUTZXWTVCNnRUaXFENk1mTTVOdURJZXRCNmVZVXZlaHdNQ2Y4XzNzUlNJSHZrdUgxYVBNYlhCcHZsNWpVckwwMDZzMDU1UkstUHRfNFRrLS1fTVZieTI0RkJzeE1Vd3Rr?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPdVhDY2h0djVhZ3dwUXNPSHg3TFFhT1NFUnVvNWpHanZ5M1kzS3JrSENsdlQzNmhHZUJJUjdNc2NXam1LSTdjV0VEZXNneS1Vc2RrZTR2Q1dvREUwUHUxUmJheDJjY1lQTV9zOFlfQ0Z1ZXJiTDJueGdXRnRobzNWQ3pVRmpWcW9tYnY4d0dwZjhuU1dGYUpFQ0VBbDVWQQ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPZWE3aFRHaTlWWkdRRUxteUdMX1pOSVRBc1NlNmZTMFZlMEdMeHVQRDdSY1JfNlZHMVRZaHJNdkthM3ByYm1udHVFMVROVHhuVk82eGJtcFVXS3pDOTdrQmRfa0dEQ0lTUlNGcW1GenlDQ2QyWGt5dGVuaFNMRmNIQzBaMkt4c1JoenBsQlhEeTBXMmxNR3l0cFlR?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxQbUV4NF9lbkt0WEpneTdsTUFfMDE2dklud1lnVnFPR0YtWGNTck9NbUNJZHk2WWtIeERxXzQ5VWdUTzNDNGRnb2Npd3h0SEp2aVc2VmszQ2lXUjVjZ1lrMEtoSTRYdXJFM0d1TnNNV0ROV1R5VFN5RjJoZjgtWlZBM0lsVnpydV82a1BVQmZibTdaNDA0WFpQMklSaHMwZEtmZ0FhSHM3a0VLQXpwTHFBRHVFMWFaRGZ10gG-AUFVX3lxTE0ycGVWQ2xHWWV0U2xFdWpmbkZiWVhMR2tlQy0wNFlvMXZ0ejlHU0IyNE85Yk0wSjdXODRpSTF4MkZJYXpqMTBSRlZFakhHTjdGSXNpcFZKRHVNcWk0YW5EanM4cW1iYU1oR29PVVYyODUwajRjSjZiR0VFdDdlbWZkUXFXanNTby1fYl9hdkFzVHFKUy1lQXZlUkNzRWNENElhUXBfU0Z1NVdpcXZwM0RVRXpTT3BtQy11QnFGc0E?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxObTQzbWFHcU5FR0Y5YmVZYnR3d2otWjNGRHVPYm9DbVdQM1dHTlpOcEFJOGJLT2NkX2J6cm44WUJkQzl1YnBXYTFHRHBNcVZWWUNyT2lxZHowT25tRkd2Tml2dnRReWdIZVB5WTNUVlZNVVZFQ0M1SzJnWjQ5VjFSU3BCRWktSHZZ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
