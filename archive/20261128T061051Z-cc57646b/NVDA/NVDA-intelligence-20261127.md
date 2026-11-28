# NVDA Intelligence Report

- ticker: **NVDA**
- Report as_of: **2026-11-27**
- Market data as_of: **2026-11-27**
- Quant sources: https://finance.yahoo.com/quote/NVDA/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVDA/key-statistics/
- AI analysis snapshot as_of: **2026-11-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-28T06:29:06.401784+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 7, 'ai': 17, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261127T063646Z-c0c26981/NVDA** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **6**; {'directional_claim_without_event_type': 5, 'negative_sentiment_in_tailwinds': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 9 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 44.0%; oldest publication 2026-11-23

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 150.4900 |
| Return 1D (%) | 0.7971 |
| Return 1W (%) | 19.8837 |
| Return 1M (%) | -30.9489 |
| Return YTD (%) | -19.1195 |
| Return 1Y (%) | -16.3150 |
| Annualized volatility (%) | 52.3469 |
| Beta vs SPY | 2.4129 |
| Max drawdown (%) | -47.5297 |
| Sharpe (rf=0) | -0.0609 |
| Downside deviation (rf=0, %) | 32.0091 |
| Sortino (rf=0) | -0.0996 |
| Historical VaR 95% (1D, %) | 4.3086 |
| Historical ES 95% (1D, %) | 5.9994 |
| Correlation vs SPY | 0.6924 |
| Tracking error vs SPY (%) | 43.3229 |
| P/E (trailing) | 16.16 |
| P/B | 13.60 |
| EV/EBITDA | 14.67 |
| Revenue growth (%) | 103.20 |
| Forward P/E (estimate) | 9.06 |
| Gross margin (%) | 74.92 |
| Operating margin (%) | 66.08 |
| Return on equity (%) | 117.36 |
| Free cash flow yield (%) | 2.73 |
| MA50 | 202.2774 |
| Close vs MA50 (%) | -25.6022 |
| MA200 | 202.4250 |
| Close vs MA200 (%) | -25.6564 |
| RSI (14, Wilder) | 38.1186 |
| MACD (12,26) | -16.3561 |
| MACD signal (9) | -16.2629 |
| MACD histogram | -0.0932 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVDA': 291, 'SPY': 291}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 150.4900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.7971 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 19.8837 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -30.9489 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -19.1195 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -16.3150 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 52.3469 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 32.0091 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.0996 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.3086 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.9994 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6924 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 43.3229 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.4129 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -47.5297 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.0609 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 9.0628 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.9210 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 66.0820 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 117.3640 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.7310 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 16.1643 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 38.1186 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.0932 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -25.6022 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -25.6564 -> Clearly below the moving-average trend level.

## TAILWINDS

### Nvidia Stock Gains. It’s Still Finding Its Floor With Huang 2.0.
- Summary: Nvidia Stock Gains. It’s Still Finding Its Floor With Huang 2.0.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMidEFVX3lxTE1qVUI0cGtEYUtyUERNQk1nMElsa0dsZzBGOUJoM0Z3SGFpZE1saHJ3QTVBM0N5M29ISzJhc3RhaUw4cmkwa2Q4UHBoV3V1TzA3LTlHU3dpMEF3d0dJd0YxVDIzWXM5eWhUY24xSVkxeEFkR25R?oc=5>

### Nvidia stock has best day since May 2003, gaining nearly $1T in market cap after Jensen Huang is reinstated as CEO
- Summary: Nvidia stock has best day since May 2003, gaining nearly $1T in market cap after Jensen Huang is reinstated as CEO
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiggJBVV95cUxPWE52dEljX0cyZVo2a1A1dWJaNXFBemdNUE9jcU94RjNXc1JwMEJyZkpjd3h5cHF0VFUxZWpCOTRpTlRRSzJBTlJGa0tubHEwa3VROU9xRFd4a1czS1Z3d05tMklnTFdESzMyTVRpdVFUQXBoMmkwdE0zd0V4TkcxRnhocTdBSm9fS3pvcksteFlqRGtIMUpjdldDbElVQlgzX3hMNWotbEJXelczemJac2h0TWhKeW9PTmJrZlIwNVBpY2VQVFVaRHFadlNOV0d2bWN2aDl4WlVQeU9IVkFRRUNDSU9tSV9xcjNJcFdJVGhkQWw0cmpJbld3WWE5OHhKcnc?oc=5>

### Nvidia, AMD, and Micron stocks trim steep losses amid jittery AI trade
- Summary: Nvidia stock trims losses amid jittery AI trade.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxOVk9mVUxsUll4NmpxRklUb1dFaHduU3ZURXZRV2ktV0pDM2ZMNElPb3RrV0NiS0JlLTVXQXJKNnpTV1JmV1k2NGMtdzNLa0F0c2tsY2xRMmJKZHhwY1dueWZXb0l4VXhWNkl4NmJ6QUlTNjBpZUItN0xkX21JUXJ5WGlUbWdON0E0V2FOT2lGYkozcm9VSjlXVjR3SDc5WWQ3VzJhWm5mb29YbjBQSU1hQURkYw?oc=5>

### Nvidia Stock: 5 Reasons The AI Trade Has Only Begun (NASDAQ:NVDA)
- Summary: Highlights AI trade momentum as a positive factor for Nvidia.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNN2o0b2xkdHNBUUlES1pQNVBVQ281SjNoQzlqcmRrVHRZY0xnX3poUnVaZWpiVWRpc2UtOUFuR0FfNEhoOU9wdDRRVVhBUGF1bG5jX1pfbUFMSXpaTDNLZ1hKakxlM2JvRGhXV1UyOGpjemdJQlRZZnUxb01ORVQ2eFpEandobGxJV1BLQl8zUGxzVi0wTGc?oc=5>

### Should You Buy Nvidia Stock Before CEO Jensen Huang Testifies in Front of Congress on Dec. 1 and Dec. 3?
- Summary: Opinion piece urging investors to consider buying Nvidia stock ahead of CEO testimony.
- Date: 2026-11-27 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3AFBVV95cUxOLXRieWlpNzJqdWQ3RVRNQk5WUXBUSUY5WE5oNHdRNXNCekJFc1pWcEViZE95RFRzbDFKWTdDc29VbXNRTTBobDVGQnFnOXg0NFVLRzQ4NUVTeHFmT2NNRkM2WjFVYmxvQTg1UnpRU0R4OGNjbGZIUVpTT2R2VU5DdzFyb1RUYkY4VTBXM0NaTmpGM2h4OUMwVkZiRVFWaS12eEhLUGRrQVVkVDcyODl4ZlQ5dElBRDd6U3ROa2hzS3ZJNm9semJQZkk5ajBsUGVGbnhKajR6ZE1xdUtZ?oc=5>

### Fire Sale: Here's Why Now May Be the Perfect Time to Buy Nvidia Stock
- Summary: Article argues current market conditions make Nvidia a good buy.
- Date: 2026-11-27 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxPelI5QmYxOVVWWEh4SklrdkNoMFpYZlVJOE4yZzE1WHVySWRucmJ1TUd1ZjUxV0Yzdm5aY091ZUlrenlsRUh6YkhzVVBxcWREeGl3V29ZUF9qY1BrcnRSMlp1MEpFSUtlUzFrdEFzY0dEdVNJNjdmWEdFOFhwVGZsYTVNbXNBTlRpUGgxTmpRZ2ZlM21MT01TbFhrMWVDYTJndDVWX0M2Y0NjNm5nVldPMg?oc=5>

### Here’s Why I’d Still Buy Nvidia Over AMD With or Without Jensen Huang at CEO.
- Summary: Author prefers Nvidia over AMD regardless of CEO presence.
- Date: 2026-11-27 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxPajRlTlBVSXV1NFo0ek9McHAyZjJOWm5relByU1FyREotVkNPaEZ2LS1mUEp4cUxBN3RkSzVSZUQtRUYwOHJlaTFoOWFadGhROFk1SzBkMEF1Q0NBWXRsMmI5VXE4NnpwaEJKREdLZGg1Q2tqTnF6ZzNpQ2lUZDE0bDdHa3lXUHZoUi1FcmxWVGZPVGluMV9FTlVWUFNwNjFkWGE1QlZEdGZjWFZ1bXpVWFljZS1HTmJKTWJr?oc=5>

### Is Nvidia a Screaming Buy or a Value Trap?
- Summary: Questioning whether Nvidia is overvalued or a good buy.
- Date: 2026-11-27 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxQN0JHZHBUZXJlWmx3RkU1bGtCdktFSURpdjlOWGNEc3VhSTJ5ZkR4OUFMRUdmUEpyamhjOWRMSFJuZ2pmQUJENHFUWmNzc0tuMGVwYXZHQUR2RENGTDV5QUtzM2t1QzJESDFrVUp3WkVqWm9GNkxLQTRVOEF5R0lRRU5hc3lPMmdNLTJ2bA?oc=5>

### Not AMD. This Is the 1 Company Nvidia Should Worry About Most.
- Summary: Suggests a competitor that Nvidia should monitor closely.
- Date: 2026-11-27 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOcGppNUlRdlVSeF85amlHWjUwWU5XTXFiLVRmSy12SlQyVEpzU05MLXB4NlVuaWgxcmFkUmpLOEJ6UXpKeXFWNkY0LUo1OGw5aEZ3RmhpTGxnUlk4RXhPRkVzalFvc2YyU3o1U0NEM05MNy1BeWsyZmYtLVRuWEZhLUFKYUxRNk5nVnlQVzU1ajdkQ0poaWx4XzRyY05VM2hjZkNHYm1n?oc=5>

## HEADWINDS

### NVIDIA Just Dropped 31% in a Month. Will NVDA Stock Hit $125 or $200 First?
- Summary: NVIDIA Just Dropped 31% in a Month. Will NVDA Stock Hit $125 or $200 First?
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQVXFSdnRPQk1JV3F3SzQ5VHVza3dwb1RNVlk5WGt2QnA1OHlZaWRhdTRlRUdqSUlfS196STEwWXVNWWxOUE1BeW1PeWh3WmI1M1MzSUZvenZOVlplWnROYnl3NGswVTBmd3R3bU5peGpOWkF6MEIyQUZOOWlTMW1CMGZDOVd4XzJ6cS1yNEJuRFZlTzZjTDdTVg?oc=5>

### Nvidia Stock (NVDA) Drops Nearly 6% as CEO Jensen Huang Admits Code-of-Conduct Violations
- Summary: Nvidia Stock (NVDA) Drops Nearly 6% as CEO Jensen Huang Admits Code-of-Conduct Violations
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxNSzBxY0ZkcF9QbTNMVXliOXpibnRxcWRBNkRnNnFTQWphQVRFR2p5ck9sWFV0OUJSWURiUnRhTDRuV2d4TUoyTzRjdjBNWnhBemJyUmpYVmxvWDNSb3k2bTVjRDBfTXFuQWpROC1BTGVoX2l3Rk01dkJRTS1KZUZSYmdUdGVnUm1tOFVhbUFNRGFzYkljeVNjY2lLbDYyX1J2RlhNTXRYS3cxZ0xCeUJpY0NvMUota1E?oc=5>

### Jensen Huang’s Return Doesn’t Make Nvidia Stock (NVDA) a Buy
- Summary: Analyst opinion deems stock unattractive despite CEO return.
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPSndtT1dTZXdiYWpqTXRoMktMU3pTZ3U0d1lMTURLenJTa1BpdkE5c0IwNnVPTFJYX2NidVRlb2FuT3BNZFptMDBvQ3ZPdTVEbGowUlRvbVlpNXpZRFlTQUkyd0VMTmtmUUZfWjlnWWJYbVJYY0VGa3BDVEU2clpGR18zbmlaV0xOTWRDb2xWYnBhWE5iZUdJ?oc=5>

### NVDA Stock Alert: Nvidia CEO Jensen Huang Rejects Calls for Succession Plan
- Summary: CEO Huang rejects succession plan calls, raising governance concerns.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQanBEQ2g0YVdlS0owSUNzQXQxV0pnMjVfZ3M0di1YaFIxejgxT2lVeGIyQThMT3dOMUlkQ3IxLVNlYlhFVFMySHE4UWhQQWFtNDZycDhUSXNyZTJCZXo3ZjFoM0JMZXNqcjF0NXVORXF0Uml3cjdaWmhjMEZSRUZ4UDFLbmFCSUJqQTBZZkdMTVoxVjVJR1Zn?oc=5>

### Nvidia stock is still paying the price for the Jensen Huang CEO drama
- Summary: CEO drama continues to negatively affect Nvidia stock.
- Date: 2026-11-27 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxPTEw1bXM4LW9fQ280Q256NWtHYXowN2YzeGFmb29VZzVZcXZacTNwODZubi1TR2lzSXYtZFUzWVpMS2RPdkdYeVZmd29HMkZNaFZOdXlQRl9vN3czUDNoUFZENUtvQ0ltWUdGUHR4OXNTdFNzMkRLNHJMTUUwYkJobmNTd1R4aExmRjhFTExpaFJhdTJ5MlJOWnZEelltN0QwMzZGbTlmRHYwTnl4amQ0M1VwYkVCcl9zdVVHaVY0UGI4Y3J4WThVOTZlSWxOUQ?oc=5>

### Chip stocks lead a Black Friday rally, but Nvidia misses out: AlphaCheck
- Summary: Nvidia did not benefit from the broader chip rally.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxQbkxyTV9zSklTSFBpa3A3S0o3YnNudHVjamUtNlBVQWUyZ0xIb3FrS1ptbVNiR1dESHlSVGFLUERKUFZXeHlVLVlNSDVvQ3gyNDJ6UnlZUTFvOW9iTjMycG9TLWhuSUFCdjQ0X3BWelR1UXZSbjlKNHkwRDVzNW1qWlFiVkItanAwV1BsVWJYd19jVkdsYkFpYTRSUGRxdkhHLVBHZDVxV2Izbmg0NHo0R3JSakJEczB4cHd0LUxwQkxNWTBZckE?oc=5>

### Learn Why The Bull Case For Nvidia Stock Could Change Following CEO Reinstatement
- Summary: CEO reinstatement may alter Nvidia's bullish outlook.
- Date: 2026-11-27 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQbEtfekZpU3YzbUh2eENiaGtONGRtOXVzcC0zWkJlOEJENW1mOGdkUC04VTd1Q0gybTFaNWpiZm5kRHMzel9RVGdXWmlia1prbXBkWnVXbnRoTkV4amJzRXBjMW1tcXNSZTlya2hka0hwQlpqZWpBaU9WdlZhU2VHX1JXcDRJeGZ0MF8ydjJZS0VEWUtwQ1E?oc=5>

## CATALYSTS

### Nvidia (NVDA) Stock Fair Value Falls After Analysts Reassess Leadership And Regulatory Risks
- Summary: Nvidia (NVDA) Stock Fair Value Falls After Analysts Reassess Leadership And Regulatory Risks
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQMm9pLVhQZmpyYU9BaFMzX1hIRk1jdDNIblcxQXFHVjh3SXZhZUFlRVhNRmhNaDlZYkJFVUotS3Bvbm53VGYzbjIwcUYwdVhHbzJEWWhWdG5jdjlmN1IwWTg3UlZ2TmNFR3YxWTZ2dFdQU21kMkFydFBTTERwXzNuLVZOV2VpTkU1d3oxaUdOYTk0eS0yejVDMw?oc=5>

### Nvidia Forecast $130 Billion in Revenue and Added $150 Billion to Its Buyback. Should You Buy the Stock?
- Summary: Nvidia Forecast $130 Billion in Revenue and Added $150 Billion to Its Buyback. Should You Buy the Stock?
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4wFBVV95cUxNc0pTZDVoR01raXhlSWRKYjI0MVFzQWFBREt0UzUxQkVBaS16bVZrZWNtcE5xVnhpZnFSSGNWbmRjMkdFTGZIdGlvRFVUTWp1NFctYTdCT00yc19DNm9VX3RxN2JuVVNEc1o2YlFRRGgxb0xESlZkSkpCQ0ZBQWI3YW43SnUyTWRNd2Rnd0MwcHhGd1F0UVpUN1NpV1lqNUNEZmpURnM2S3V6dU4wM1FjYzZrY3R1Q245Mk1UcW1HQ3ZrU0FnUzdqdm1QekVJQ1FRMVZMUjhmSHlrM2pfQkQ2a3lqZw?oc=5>

### Nvidia (NVDA) Stock Looks Below Fair Value After Recent Turmoil
- Summary: Nvidia (NVDA) Stock Looks Below Fair Value After Recent Turmoil
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQbUpxbnpVNGpTNThJa3dsbWR4R3cyQ3hWbVFydFJ6bW10dldabWVTU3hPMGRoZlFhczNXZWgzbHppOVBIZzNKb1VTNWZ0dFd3S3lHdTJFRkdJOUo2N0FIQ1I3VnVPLVdwSWdmS1NsbWVmVW9WVXdrOFI5TnV2a1JFb0dfVWRjUWxMMUhwT0FQdUdRMEFvVFBjTjZR?oc=5>

### Nvidia Sell-Off: You Won’t Believe How Cheap the Stock Is
- Summary: Nvidia stock falls sharply, seen as cheap.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOcU1sN2NqMk9iRHNZTTNZTldZRVc4UWhvZXhTZ0NOd3M3TEphU2JXbmxyaTZoTnJXOHg3SjlTamhxb0FvZlFTQVo2OERzeldyQXNQanJzZmhYUFNYWXI0MmE5UThjVXN4OUEzUHVWQ3FQSkFBTFV1VlROQjN6ZmZYVVQtV2VzWnRod1R4TXVIMFJPVFBGTGVteFgwTlU4RUx4?oc=5>

### Unstoppable NVDA Stock? Jensen Huang is Back, and Nvidia Is Eyeing 75% Revenue Growth in FY 2028.
- Summary: CEO reinstatement and 75% revenue growth target signal strong future prospects.
- Date: 2026-11-27 | Impact: high | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxNQS1oUmpYRnQzOTJyUjlBZWgzN3QtdTZWd1RzVV9qVEd0YjFiSE4zQkszVUdmOEJaZlE1c1NUOXg1dU9nZExlYjRJajBCZ0JuM0FjTnRPZFMxTzFMNkhNQnp6c2xwSUVyZHNBNEt0U0psb0FtMks4SnUyVlVkSTNqUlpPb3RYMmtkcWtrZk9WbUFKRUZ1YUg4MC1ZRGVoSkxPRUxMWXNXbkg1ejFUYUpyTFcybmxYR1JWUENneWR2WVhjdFJ4T0dENmlYOG14OS1BdFdr?oc=5>

### Jensen Huang Is Back. Nvidia’s (NVDA) Bull Case Remains
- Summary: Bull case for NVDA remains strong, indicating potential upside.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPNlZGTzVZUW5pNEFCczVoQjZCY1YxNzJqMU5VZE1HT1R3TnZkY0ZpUnl6d1RZd0xUTWdJakpYMDBPZUx1eGNFN3RpakgwY2tiVDdoWS1Ud1pVVS1KY3NLZFRLV1ZoVTZmZV9UWG9YaHJBLW9MY09kMFp4Qk1LLWFGdERCMkp1cndRMGRPVWlBZzVMT2NFdUNxSVhn?oc=5>

## RISKS

### Top Analyst Flags 5 Major Risks for NVDA Stock, Says Nvidia Could Stay in ‘Penalty Box’ for 1-2 Quarters
- Summary: Five key risks identified, potential short-term performance impact.
- Date: 2026-11-26 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxNM0h2OGVIVXpRNWtNWDd6bk5iWnJmZTAtNG5sOW80UnpZbUJKOXVlUHB5WUk0TGVoYkJ6aHhuZUV0YkFrdWVSaEJjV1ZGaTczRnYzUXBydG92VUc1WGR5SjN3SndmczZIYUpNdkFpM3RQMHlCdUtLcmotZHEybXhKVUlpaUFqUkZzNjBLRVM3b252WmZXRjlPUnZuRVJXM3lRTWViMmc4bzJKT3UwZTJoc1V6OWJ1YTVxdDVXVV9ndUduTkMzb0E?oc=5>

### Nvidia Stock Wavers On Headline Risks From Huang Testimony, Asia Sales
- Summary: NVDA stock volatility due to risks from testimony and Asia sales concerns.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxOdWlzeGdReHVRcXN3WnBtQ1BxRXhRNENVMjFVMHNVVFdBVXhmYTlIcWVJUHZkRUNveGluQk51ci12RG83cUNKZXlMcnhZcFl2VnZQWkhYWVUtYndjREVEUTZSUkFzU3YzbVJlVWEzSXRZUnpaQkxMaXhaMkpMR3U2ZGlaVkE?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVDA** | **16.16** | **13.60** | **14.67** | **103.20** | **3,633,882,071,040.00 USD** | **-16.32** |
| AMD | 90.71 | 10.18 | 61.90 | 44.70 | 702,641,537,024.00 USD | 98.16 |
| AVGO | 39.89 | 14.96 | 29.21 | 85.50 | 1,490,995,511,296.00 USD | -20.85 |
| INTC | N/A | 2.65 | 16.61 | 20.90 | 305,080,991,744.00 USD | 55.94 |

Peers fetched as_of: 2026-11-27; NVDA reuses existing data (market data as_of: 2026-11-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-17
- Next expected earnings: 2027-02-24 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-27

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

- https://news.google.com/rss/articles/CBMidEFVX3lxTE1qVUI0cGtEYUtyUERNQk1nMElsa0dsZzBGOUJoM0Z3SGFpZE1saHJ3QTVBM0N5M29ISzJhc3RhaUw4cmkwa2Q4UHBoV3V1TzA3LTlHU3dpMEF3d0dJd0YxVDIzWXM5eWhUY24xSVkxeEFkR25R?oc=5
- https://news.google.com/rss/articles/CBMiggJBVV95cUxPWE52dEljX0cyZVo2a1A1dWJaNXFBemdNUE9jcU94RjNXc1JwMEJyZkpjd3h5cHF0VFUxZWpCOTRpTlRRSzJBTlJGa0tubHEwa3VROU9xRFd4a1czS1Z3d05tMklnTFdESzMyTVRpdVFUQXBoMmkwdE0zd0V4TkcxRnhocTdBSm9fS3pvcksteFlqRGtIMUpjdldDbElVQlgzX3hMNWotbEJXelczemJac2h0TWhKeW9PTmJrZlIwNVBpY2VQVFVaRHFadlNOV0d2bWN2aDl4WlVQeU9IVkFRRUNDSU9tSV9xcjNJcFdJVGhkQWw0cmpJbld3WWE5OHhKcnc?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxOVk9mVUxsUll4NmpxRklUb1dFaHduU3ZURXZRV2ktV0pDM2ZMNElPb3RrV0NiS0JlLTVXQXJKNnpTV1JmV1k2NGMtdzNLa0F0c2tsY2xRMmJKZHhwY1dueWZXb0l4VXhWNkl4NmJ6QUlTNjBpZUItN0xkX21JUXJ5WGlUbWdON0E0V2FOT2lGYkozcm9VSjlXVjR3SDc5WWQ3VzJhWm5mb29YbjBQSU1hQURkYw?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNN2o0b2xkdHNBUUlES1pQNVBVQ281SjNoQzlqcmRrVHRZY0xnX3poUnVaZWpiVWRpc2UtOUFuR0FfNEhoOU9wdDRRVVhBUGF1bG5jX1pfbUFMSXpaTDNLZ1hKakxlM2JvRGhXV1UyOGpjemdJQlRZZnUxb01ORVQ2eFpEandobGxJV1BLQl8zUGxzVi0wTGc?oc=5
- https://news.google.com/rss/articles/CBMi3AFBVV95cUxOLXRieWlpNzJqdWQ3RVRNQk5WUXBUSUY5WE5oNHdRNXNCekJFc1pWcEViZE95RFRzbDFKWTdDc29VbXNRTTBobDVGQnFnOXg0NFVLRzQ4NUVTeHFmT2NNRkM2WjFVYmxvQTg1UnpRU0R4OGNjbGZIUVpTT2R2VU5DdzFyb1RUYkY4VTBXM0NaTmpGM2h4OUMwVkZiRVFWaS12eEhLUGRrQVVkVDcyODl4ZlQ5dElBRDd6U3ROa2hzS3ZJNm9semJQZkk5ajBsUGVGbnhKajR6ZE1xdUtZ?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxPelI5QmYxOVVWWEh4SklrdkNoMFpYZlVJOE4yZzE1WHVySWRucmJ1TUd1ZjUxV0Yzdm5aY091ZUlrenlsRUh6YkhzVVBxcWREeGl3V29ZUF9qY1BrcnRSMlp1MEpFSUtlUzFrdEFzY0dEdVNJNjdmWEdFOFhwVGZsYTVNbXNBTlRpUGgxTmpRZ2ZlM21MT01TbFhrMWVDYTJndDVWX0M2Y0NjNm5nVldPMg?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxPajRlTlBVSXV1NFo0ek9McHAyZjJOWm5relByU1FyREotVkNPaEZ2LS1mUEp4cUxBN3RkSzVSZUQtRUYwOHJlaTFoOWFadGhROFk1SzBkMEF1Q0NBWXRsMmI5VXE4NnpwaEJKREdLZGg1Q2tqTnF6ZzNpQ2lUZDE0bDdHa3lXUHZoUi1FcmxWVGZPVGluMV9FTlVWUFNwNjFkWGE1QlZEdGZjWFZ1bXpVWFljZS1HTmJKTWJr?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxQN0JHZHBUZXJlWmx3RkU1bGtCdktFSURpdjlOWGNEc3VhSTJ5ZkR4OUFMRUdmUEpyamhjOWRMSFJuZ2pmQUJENHFUWmNzc0tuMGVwYXZHQUR2RENGTDV5QUtzM2t1QzJESDFrVUp3WkVqWm9GNkxLQTRVOEF5R0lRRU5hc3lPMmdNLTJ2bA?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOcGppNUlRdlVSeF85amlHWjUwWU5XTXFiLVRmSy12SlQyVEpzU05MLXB4NlVuaWgxcmFkUmpLOEJ6UXpKeXFWNkY0LUo1OGw5aEZ3RmhpTGxnUlk4RXhPRkVzalFvc2YyU3o1U0NEM05MNy1BeWsyZmYtLVRuWEZhLUFKYUxRNk5nVnlQVzU1ajdkQ0poaWx4XzRyY05VM2hjZkNHYm1n?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQVXFSdnRPQk1JV3F3SzQ5VHVza3dwb1RNVlk5WGt2QnA1OHlZaWRhdTRlRUdqSUlfS196STEwWXVNWWxOUE1BeW1PeWh3WmI1M1MzSUZvenZOVlplWnROYnl3NGswVTBmd3R3bU5peGpOWkF6MEIyQUZOOWlTMW1CMGZDOVd4XzJ6cS1yNEJuRFZlTzZjTDdTVg?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxNSzBxY0ZkcF9QbTNMVXliOXpibnRxcWRBNkRnNnFTQWphQVRFR2p5ck9sWFV0OUJSWURiUnRhTDRuV2d4TUoyTzRjdjBNWnhBemJyUmpYVmxvWDNSb3k2bTVjRDBfTXFuQWpROC1BTGVoX2l3Rk01dkJRTS1KZUZSYmdUdGVnUm1tOFVhbUFNRGFzYkljeVNjY2lLbDYyX1J2RlhNTXRYS3cxZ0xCeUJpY0NvMUota1E?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPSndtT1dTZXdiYWpqTXRoMktMU3pTZ3U0d1lMTURLenJTa1BpdkE5c0IwNnVPTFJYX2NidVRlb2FuT3BNZFptMDBvQ3ZPdTVEbGowUlRvbVlpNXpZRFlTQUkyd0VMTmtmUUZfWjlnWWJYbVJYY0VGa3BDVEU2clpGR18zbmlaV0xOTWRDb2xWYnBhWE5iZUdJ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQanBEQ2g0YVdlS0owSUNzQXQxV0pnMjVfZ3M0di1YaFIxejgxT2lVeGIyQThMT3dOMUlkQ3IxLVNlYlhFVFMySHE4UWhQQWFtNDZycDhUSXNyZTJCZXo3ZjFoM0JMZXNqcjF0NXVORXF0Uml3cjdaWmhjMEZSRUZ4UDFLbmFCSUJqQTBZZkdMTVoxVjVJR1Zn?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxPTEw1bXM4LW9fQ280Q256NWtHYXowN2YzeGFmb29VZzVZcXZacTNwODZubi1TR2lzSXYtZFUzWVpMS2RPdkdYeVZmd29HMkZNaFZOdXlQRl9vN3czUDNoUFZENUtvQ0ltWUdGUHR4OXNTdFNzMkRLNHJMTUUwYkJobmNTd1R4aExmRjhFTExpaFJhdTJ5MlJOWnZEelltN0QwMzZGbTlmRHYwTnl4amQ0M1VwYkVCcl9zdVVHaVY0UGI4Y3J4WThVOTZlSWxOUQ?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxQbkxyTV9zSklTSFBpa3A3S0o3YnNudHVjamUtNlBVQWUyZ0xIb3FrS1ptbVNiR1dESHlSVGFLUERKUFZXeHlVLVlNSDVvQ3gyNDJ6UnlZUTFvOW9iTjMycG9TLWhuSUFCdjQ0X3BWelR1UXZSbjlKNHkwRDVzNW1qWlFiVkItanAwV1BsVWJYd19jVkdsYkFpYTRSUGRxdkhHLVBHZDVxV2Izbmg0NHo0R3JSakJEczB4cHd0LUxwQkxNWTBZckE?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQbEtfekZpU3YzbUh2eENiaGtONGRtOXVzcC0zWkJlOEJENW1mOGdkUC04VTd1Q0gybTFaNWpiZm5kRHMzel9RVGdXWmlia1prbXBkWnVXbnRoTkV4amJzRXBjMW1tcXNSZTlya2hka0hwQlpqZWpBaU9WdlZhU2VHX1JXcDRJeGZ0MF8ydjJZS0VEWUtwQ1E?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQMm9pLVhQZmpyYU9BaFMzX1hIRk1jdDNIblcxQXFHVjh3SXZhZUFlRVhNRmhNaDlZYkJFVUotS3Bvbm53VGYzbjIwcUYwdVhHbzJEWWhWdG5jdjlmN1IwWTg3UlZ2TmNFR3YxWTZ2dFdQU21kMkFydFBTTERwXzNuLVZOV2VpTkU1d3oxaUdOYTk0eS0yejVDMw?oc=5
- https://news.google.com/rss/articles/CBMi4wFBVV95cUxNc0pTZDVoR01raXhlSWRKYjI0MVFzQWFBREt0UzUxQkVBaS16bVZrZWNtcE5xVnhpZnFSSGNWbmRjMkdFTGZIdGlvRFVUTWp1NFctYTdCT00yc19DNm9VX3RxN2JuVVNEc1o2YlFRRGgxb0xESlZkSkpCQ0ZBQWI3YW43SnUyTWRNd2Rnd0MwcHhGd1F0UVpUN1NpV1lqNUNEZmpURnM2S3V6dU4wM1FjYzZrY3R1Q245Mk1UcW1HQ3ZrU0FnUzdqdm1QekVJQ1FRMVZMUjhmSHlrM2pfQkQ2a3lqZw?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQbUpxbnpVNGpTNThJa3dsbWR4R3cyQ3hWbVFydFJ6bW10dldabWVTU3hPMGRoZlFhczNXZWgzbHppOVBIZzNKb1VTNWZ0dFd3S3lHdTJFRkdJOUo2N0FIQ1I3VnVPLVdwSWdmS1NsbWVmVW9WVXdrOFI5TnV2a1JFb0dfVWRjUWxMMUhwT0FQdUdRMEFvVFBjTjZR?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOcU1sN2NqMk9iRHNZTTNZTldZRVc4UWhvZXhTZ0NOd3M3TEphU2JXbmxyaTZoTnJXOHg3SjlTamhxb0FvZlFTQVo2OERzeldyQXNQanJzZmhYUFNYWXI0MmE5UThjVXN4OUEzUHVWQ3FQSkFBTFV1VlROQjN6ZmZYVVQtV2VzWnRod1R4TXVIMFJPVFBGTGVteFgwTlU4RUx4?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxNQS1oUmpYRnQzOTJyUjlBZWgzN3QtdTZWd1RzVV9qVEd0YjFiSE4zQkszVUdmOEJaZlE1c1NUOXg1dU9nZExlYjRJajBCZ0JuM0FjTnRPZFMxTzFMNkhNQnp6c2xwSUVyZHNBNEt0U0psb0FtMks4SnUyVlVkSTNqUlpPb3RYMmtkcWtrZk9WbUFKRUZ1YUg4MC1ZRGVoSkxPRUxMWXNXbkg1ejFUYUpyTFcybmxYR1JWUENneWR2WVhjdFJ4T0dENmlYOG14OS1BdFdr?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPNlZGTzVZUW5pNEFCczVoQjZCY1YxNzJqMU5VZE1HT1R3TnZkY0ZpUnl6d1RZd0xUTWdJakpYMDBPZUx1eGNFN3RpakgwY2tiVDdoWS1Ud1pVVS1KY3NLZFRLV1ZoVTZmZV9UWG9YaHJBLW9MY09kMFp4Qk1LLWFGdERCMkp1cndRMGRPVWlBZzVMT2NFdUNxSVhn?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxNM0h2OGVIVXpRNWtNWDd6bk5iWnJmZTAtNG5sOW80UnpZbUJKOXVlUHB5WUk0TGVoYkJ6aHhuZUV0YkFrdWVSaEJjV1ZGaTczRnYzUXBydG92VUc1WGR5SjN3SndmczZIYUpNdkFpM3RQMHlCdUtLcmotZHEybXhKVUlpaUFqUkZzNjBLRVM3b252WmZXRjlPUnZuRVJXM3lRTWViMmc4bzJKT3UwZTJoc1V6OWJ1YTVxdDVXVV9ndUduTkMzb0E?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxOdWlzeGdReHVRcXN3WnBtQ1BxRXhRNENVMjFVMHNVVFdBVXhmYTlIcWVJUHZkRUNveGluQk51ci12RG83cUNKZXlMcnhZcFl2VnZQWkhYWVUtYndjREVEUTZSUkFzU3YzbVJlVWEzSXRZUnpaQkxMaXhaMkpMR3U2ZGlaVkE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
