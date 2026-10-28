# T Intelligence Report

- ticker: **T**
- Report as_of: **2026-10-27**
- Market data as_of: **2026-10-27**
- Quant sources: https://finance.yahoo.com/quote/T/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/T/key-statistics/
- AI analysis snapshot as_of: **2026-10-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-28T02:11:05.212570+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 5, 'ai': 14, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261027T014607Z-b66f6bd5/T** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 9 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 45.83%; oldest publication 2026-10-21

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 20.9400 |
| Return 1D (%) | 0.4317 |
| Return 1W (%) | -10.5892 |
| Return 1M (%) | -16.5614 |
| Return YTD (%) | -11.6783 |
| Return 1Y (%) | -14.0654 |
| Annualized volatility (%) | 28.6381 |
| Beta vs SPY | -0.3991 |
| Max drawdown (%) | -28.8854 |
| Sharpe (rf=0) | -0.3867 |
| Downside deviation (rf=0, %) | 22.1368 |
| Sortino (rf=0) | -0.5003 |
| Historical VaR 95% (1D, %) | 2.8546 |
| Historical ES 95% (1D, %) | 4.6484 |
| Correlation vs SPY | -0.1770 |
| Tracking error vs SPY (%) | 33.3200 |
| P/E (trailing) | 11.20 |
| P/B | 1.33 |
| EV/EBITDA | 7.16 |
| Revenue growth (%) | 5.30 |
| Forward P/E (estimate) | 8.08 |
| Gross margin (%) | 59.74 |
| Operating margin (%) | 24.65 |
| Return on equity (%) | 11.61 |
| Free cash flow yield (%) | 8.48 |
| MA50 | 24.3852 |
| Close vs MA50 (%) | -14.1284 |
| MA200 | 24.4712 |
| Close vs MA200 (%) | -14.4301 |
| RSI (14, Wilder) | 32.2155 |
| MACD (12,26) | -0.8494 |
| MACD signal (9) | -0.6137 |
| MACD histogram | -0.2357 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'T': 269, 'SPY': 269}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 20.9400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.4317 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -10.5892 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -16.5614 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -11.6783 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -14.0654 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 28.6381 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 22.1368 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.5003 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8546 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.6484 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1770 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 33.3200 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.3991 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.8854 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.3867 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 8.0763 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 59.7420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 24.6520 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 11.6130 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 8.4798 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 11.1979 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 32.2155 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.2357 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -14.1284 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -14.4301 -> Clearly below the moving-average trend level.

## TAILWINDS

### AT&T Sinks 5% Despite Q3 Beat and Raised Outlook; Verizon and T-Mobile Drop 3%
- Summary: AT&T Sinks 5% Despite Q3 Beat and Raised Outlook; Verizon and T-Mobile Drop 3%
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxOaUJKUGstUVhON1ptalVFRWExNk9fR3NkZVNuYmxuMkF4NGxlbkJBYkxUeW1idVQzS3ZOeXJRdlpMbk50RFc5Y2dXVk52eXhaemp4dWJTVlFvVUV5d1FfVUNvb0JINGlxcDZrS2QwOWpJbzRCZzh6QXo5MGotN0tBTGRScW9xNUs4MTk3RW9B?oc=5>

### AT&T And TMobile Boost Infrastructure Investments To Counter AI Threats
- Summary: AT&T and T-Mobile jointly invest in infrastructure to mitigate AI competition.
- Date: 2026-10-26 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxNcmwyZkNEX2NHMjNGN2RrYjlZM1hkbXpiOTR6c2xrdTNtNUM0ZUM4dU5IWEhuVXRCdnlfRmdZTjZ4SGF4bjBfdUJRdzFaWGlWYmQ2NnBwbDYxNG5fa1c5OGxWT2JmeHhpeXJLVU9jV0xEa1U4UXVFZ2FvQ0pmWW1KNUZTVFF4YWhiNXRScHV1a1lJdE44VkVha3VWeWtYTUJZakFOVG9NZTg2QQ?oc=5>

### AT&T (T) Stock Looks Cheap Relative To Its Earnings Outlook
- Summary: AT&T’s stock appears undervalued compared to earnings outlook.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxQc1BkUDFaVkRUUEg5LTI4eVZuN3FOUEs2TFl4SmJEOERMRWV1RU9VNU5yVDZ0T25MTmliZVRxV0d2S05jMllRd0lRbFNjdHo3N1FLb1l5U2hLOHVQcVM0WXhOeUhjSkRWTVZmcWlSRDI5RjVNSlFnSXdLWHBlQ3NiZkpxMXZMMkk3VEZnaWZBaw?oc=5>

### Should You Buy AT&T Stock For Its Cash?
- Summary: AT&T’s cash holdings make it an attractive buy.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPTEZORThKcjZjV213ckw5R2dPNTFIMFA1d0kyV1FJX1pXR2R5NkZDQzdwbW0yQ0tXejlxd3J3Z2c0WEtMMzJIUmdIeDJDbnN1TjRtWVhZalpxNUJGTDZuMzdnT0RyLWk4dFJOeFRpaGxob3dVd0JyU01ibTdGVzZUamt5bzFZUl9Jd0NXV09JZUJjTG0tV0hvNUJKWQ?oc=5>

### AT&T: The SpaceX Panic Is A Gift (NYSE:T)
- Summary: SpaceX issues benefit AT&T amid panic.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxNXzU1S2c5UEFSSzJMbDIzSWZnb0F6V09vRjdqQVU3QVZ1YXkyV2J3SXhRZjZRY3BRajU1UGRSSERZbXFDNzBIZWhON21WUzRGQmoxV0FJWE1qYzZSRXJJSlByN1FEM1NRSlMtd0wwU2NhQ3hWWW0xek9HbWVJcXA4UEJB?oc=5>

## HEADWINDS

### AT&T Stock Sinks on Subscriber and SpaceX Worries. Is the Stock a Buy on the Dip?
- Summary: AT&T Stock Sinks on Subscriber and SpaceX Worries. Is the Stock a Buy on the Dip?
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOWUIwNUc2YTBxbDJBeXA5ZHhXV1lfUGlhd3RPYTdhWDRmQmtoMzQ3dEtzZ3Rzd2dRMktWMDRJVGdHVDVkdC1qbE0wWVhNTFVMRV9OVk14aWZ0UFcyUXhzUXlqbGpYS3JjTHo4dWFnZUtuZXpudlJDOW5TSHUtSHVWOVZmbEMyYzAtYkhGMU5feEVQQnk4dUR3aGdGeGI?oc=5>

### AT&T (T) Stock Price Sinks As Q3 Results Spotlight Debt Tension
- Summary: AT&T (T) Stock Price Sinks As Q3 Results Spotlight Debt Tension
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxQWXhZbTZGcV9ZcWRjbWtnYzhUaTVHS3I2ZWUzU1BHNnFucjVIQjlLTHJfZEV2dzNWbERqVWhiMVNwZk1iMVVtR3BuY0JuQ3lTd0oxN0xfWGJ4NDcxdTZNSjFNRTdvZWpmcUNORWl3RkhRcloyb0p4STEzNmF5SHBHZXRmUTYzb19oblBzcXR4WQ?oc=5>

### AT&T, Verizon, T-Mobile Shares Slip As SpaceX Reportedly Holds Cell Tower Talks For Starlink Mobile
- Summary: AT&T, Verizon, T-Mobile Shares Slip As SpaceX Reportedly Holds Cell Tower Talks For Starlink Mobile
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi5AFBVV95cUxORzZ2YUxFVlR5V2dHMHVudTZwZ2w1QS1aS1YxR3ZXZUtjZnZXYzd1VTJCYWFfU05JNlNkemVjZ2hGRjBGQ1NtT2ZWYmhsNzRVbVVicU81LUlOYS04cFBzWHVXUXpmUzJSbmEwUDRrUjA3QUdVQVE3dThIdnBrZEd6dzg3N2YxTFZCWko1WGtzLTJoU292LVZBVnczblkxaGFQa1RYWVdKbEo3WkRkRkszMTJIYWFaWjRTc2xiVEE0bEw1WncyNXFDU2tfTHJBR3FjdV9Dd2VoVjJwSy1sc195dHkwTk0?oc=5>

### AT&T Stock Falls 13.4% in a Month. Is the Drop a Buying Opportunity?
- Summary: AT&T Stock Falls 13.4% in a Month. Is the Drop a Buying Opportunity?
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxQNDRYZi1iRTN4RE5Yc291aG4zbnNWS3gwNkJYdkxrOGhvU3ZfV1loeFJLcy1YeG1JVHplSW1EVG1fZkxESmEteXhMQVphVTVYc3NrUEEzMU13SE1vQXAzak5HVHAtRExjWnJYRXhHaXR2ZkdqelJQUVljMlZCWXpMb2F0ZUxkRGVMV3Rr?oc=5>

### AT&T (T) stock trades down, here is why
- Summary: AT&T shares declined, with analysts citing recent factors.
- Date: 2026-10-21 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxNYUJRRlhFV2lBa3k1R2N2ZVhJbGRkOHptTFd0bkZ6X3puT1RjS2JUUl9abkVVY25xdXNjWmcxTUw3UUxsNnNxMFIwUG5EeUVNbXFEdWtpc3VibzBtU25vaWFvalpkVVYyUjFzSGxiYTY0cENjVFVJSWpRSng0emotd3lUOGlaOEN5RFlidERPNA?oc=5>

### What Just Happened To AT&T Stock?
- Summary: AT&T stock experienced recent volatility, prompting analysis of underlying factors.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxNNDJMd2R3QkRqZ1U2dXMzT0VEMXEyVV9Ia1BCUDFvRk1OYy1GNV9HTWdqVlRXV3ZFd2tZSmRUT05PV1RoQ0JQTlBnZmJENC1TMUFxdGE2eW5nR2hSR2NqNkZHdzJ6aTNWZHJFS1RUM0dIa2hLZ3FWX2I4aFQ3UVBSNkhmSWJOZVVqcDJ3SjBnOA?oc=5>

### AT&T extends recent slump with another 8% retreat (T:NYSE)
- Summary: Stock price fell 8%, extending slump.
- Date: 2026-10-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxOYVlUZjJnTXBSZ3R0LVBzejFUcDQ5MklPeURDajNjR3BNLV96dXlDYU92U0QxTnlIVG92WE1oTlNOQW5ub0NNN2tRSzRzcGo2NUREdk51cFo2UW1oajN0akNBWWFuNFBZREhTdUg4d1BrTjgwb3Bua3U4Z2JVektQeG04NEVzNS1NS1VaR0Jn?oc=5>

### Stock Market Today, Oct. 23: AT&T Slides on SpaceX Cell-Site Talks
- Summary: Stock slid due to SpaceX cell-site talks.
- Date: 2026-10-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxOd05hZV9CR1JuTWw5ZUE3Q0pyU2gyaHp0cEFGQXYtS3MwSUdaV2JpN2E3a3E0VjlmUldBNWpjLVFyeDNiY3JnX1haTjhsY28xa2VpbFdXLU9TMk1RazhkOVRqX296dFZKNFVkWE84dnFWcVNicEhKcFFualpFS0pYSnpwWXI3QlVpdkhVQ2trckJQcUhIemp0aWV0MGxNQk91a0dpd0llVFJrdy1BVmJWcWtORU4zNUVmQ2VBY29nWGYtdkZXNzZV?oc=5>

### T Stock Update: AT&T 2024 Data Breach Settlements Could Arrive Soon
- Summary: Potential data breach settlements pose a risk to AT&T.
- Date: 2026-10-27 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOaHNQa3M3bTI2SGJnemZwMTlSTEdQMHNJRGZOY0lRcGl3VXhmQ01DS3pvNlFBbHR5ME9wdzJDTTRqei1OU2FnbkNmWTgzTFR2cHFHS2ZubTBCMUVab3NKSG45UGlUTktkQmpZSTBqUTdQR2xIU2xFWVE0OFFkSTJmVVFIa0h3b3B5c2tZaDQwSkltR2RxRGNTVnlvUQ?oc=5>

### AT&T: 80,000 Reasons To Worry (NYSE:T)
- Summary: AT&T faces widespread concerns, indicating potential operational or financial challenges.
- Date: 2026-10-27 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMifEFVX3lxTFA3NV9JQnhaTjM4SlJTN2VsaUd4MXZLUVpLUGc2NXcxM0RBUmxycGdSVjZ5c19RT2xCUktWTDdWYUZ2a3RTSmNrdUZZalBMRDlHUlhvb2gwT2lxdE8wTzktNDZ0ZHRrTUxfeU9vdTJSdUJ1emdUUlFxME51N00?oc=5>

### Why AT&T Stock Plunged on Friday
- Summary: AT&T stock experienced a significant decline, reflecting market negative sentiment.
- Date: 2026-10-24 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMif0FVX3lxTFBqeWRleVNIT3JOR2duMEJ4T0xfZjZ4Y1ppMEpHSTlnajNvZzI5aUxYbWh6eDBwWFhmdlgydk0yT1NrSHdQY3NLemJrdE5uc1d6MkZuQ2VXa3htN183TjVHS1lSSUpKOTFxRkxuMGZPVmo0a3V4VHVQNVdPYnZlNEk?oc=5>

## CATALYSTS

### Telecom Stocks Fall as SpaceX Eyes 80,000 Cell Sites: T-Mobile Sinks 5%, AT&T Drops 4%, Verizon Slides 3%
- Summary: AT&T shares fell 4% amid broader telecom sell‑off linked to SpaceX’s cell‑site plans.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQeW9YX2JfMVZfN2FVVGZXWmdNS181YzFZaWU5elRHeFlpMmNWZGJ3eWUtcmtPWnl1cFEzZE1aa3lZYkMxM1lYWW93WWw4dzgyQUVuRUd3ZTZiSjdhRVh0Wk0xVndjU2hLdmJHR1FrMExCdFVubWM3QXJubnpXX2NJcUpJQnB0VDFYVlo2STBjYlJ3YUtDdU1vM1Ezb1Y?oc=5>

### What Should AT&T Stock Holders Take From Its Third Quarter?
- Summary: Review of AT&T's Q3 performance and implications for shareholders.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxOM1ExY0ZwQllsOVIwaUUtMnc0WXpLNi1rQklwaGV5b3hBdV9NM0hfM1A3ekpYNVREajg5eTloWWR2Szc2VnA5c1NialNVWjRzdmdSQ3hPbHNTRTlCSy1Hc01rb1BSc2JUS3VQMC1hOF9RY0p6c3JScUtkenpsOGY3d0xPSUdseVY2SGw4M2RZSUd6Qjhjd1JyMkc5cUkxNzhRS2lBdTlvdVFNMzZaT2F1aldzODNlZw?oc=5>

## RISKS

### ‘Real consequences’: AT&T, Verizon and T-Mobile warn FCC as Elon Musk plots a SpaceX phone network for the US by 2028
- Summary: Regulatory warning over potential competition from SpaceX phone network, posing future risk to AT&T.
- Date: 2026-10-25 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQWXc0TzBOUndZQ1Q2Y0xrRlZMZmU5VlhhWm1tOEt5WXhHaERMeFE4TjhWUnFlTzl5bDBrZFFxWDhxNXdreEpOdU9zQkUtQi12QUZ5SkZMdnFPNjlsUlBUNmxZcGpKaHl6Yzg5aTd1eU9aYm5RdkVUMEZiWC1uenY3ZHlpX0N1UFVjM1dVZWdhNVgtT1U2?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **T** | **11.20** | **1.33** | **7.16** | **5.30** | **141,061,767,168.00 USD** | **-14.07** |
| VZ | 11.44 | 1.72 | 7.23 | 1.50 | 182,089,842,688.00 USD | 19.43 |
| TMUS | 15.34 | 2.80 | 8.00 | 7.90 | 157,500,375,040.00 USD | -32.06 |
| BCE | 4.12 | 1.27 | 7.31 | 1.50 | 18,734,444,544.00 USD | -9.85 |

Peers fetched as_of: 2026-10-27; T reuses existing data (market data as_of: 2026-10-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-27

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
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxNcmwyZkNEX2NHMjNGN2RrYjlZM1hkbXpiOTR6c2xrdTNtNUM0ZUM4dU5IWEhuVXRCdnlfRmdZTjZ4SGF4bjBfdUJRdzFaWGlWYmQ2NnBwbDYxNG5fa1c5OGxWT2JmeHhpeXJLVU9jV0xEa1U4UXVFZ2FvQ0pmWW1KNUZTVFF4YWhiNXRScHV1a1lJdE44VkVha3VWeWtYTUJZakFOVG9NZTg2QQ?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxQc1BkUDFaVkRUUEg5LTI4eVZuN3FOUEs2TFl4SmJEOERMRWV1RU9VNU5yVDZ0T25MTmliZVRxV0d2S05jMllRd0lRbFNjdHo3N1FLb1l5U2hLOHVQcVM0WXhOeUhjSkRWTVZmcWlSRDI5RjVNSlFnSXdLWHBlQ3NiZkpxMXZMMkk3VEZnaWZBaw?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPTEZORThKcjZjV213ckw5R2dPNTFIMFA1d0kyV1FJX1pXR2R5NkZDQzdwbW0yQ0tXejlxd3J3Z2c0WEtMMzJIUmdIeDJDbnN1TjRtWVhZalpxNUJGTDZuMzdnT0RyLWk4dFJOeFRpaGxob3dVd0JyU01ibTdGVzZUamt5bzFZUl9Jd0NXV09JZUJjTG0tV0hvNUJKWQ?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxNXzU1S2c5UEFSSzJMbDIzSWZnb0F6V09vRjdqQVU3QVZ1YXkyV2J3SXhRZjZRY3BRajU1UGRSSERZbXFDNzBIZWhON21WUzRGQmoxV0FJWE1qYzZSRXJJSlByN1FEM1NRSlMtd0wwU2NhQ3hWWW0xek9HbWVJcXA4UEJB?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOWUIwNUc2YTBxbDJBeXA5ZHhXV1lfUGlhd3RPYTdhWDRmQmtoMzQ3dEtzZ3Rzd2dRMktWMDRJVGdHVDVkdC1qbE0wWVhNTFVMRV9OVk14aWZ0UFcyUXhzUXlqbGpYS3JjTHo4dWFnZUtuZXpudlJDOW5TSHUtSHVWOVZmbEMyYzAtYkhGMU5feEVQQnk4dUR3aGdGeGI?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxQWXhZbTZGcV9ZcWRjbWtnYzhUaTVHS3I2ZWUzU1BHNnFucjVIQjlLTHJfZEV2dzNWbERqVWhiMVNwZk1iMVVtR3BuY0JuQ3lTd0oxN0xfWGJ4NDcxdTZNSjFNRTdvZWpmcUNORWl3RkhRcloyb0p4STEzNmF5SHBHZXRmUTYzb19oblBzcXR4WQ?oc=5
- https://news.google.com/rss/articles/CBMi5AFBVV95cUxORzZ2YUxFVlR5V2dHMHVudTZwZ2w1QS1aS1YxR3ZXZUtjZnZXYzd1VTJCYWFfU05JNlNkemVjZ2hGRjBGQ1NtT2ZWYmhsNzRVbVVicU81LUlOYS04cFBzWHVXUXpmUzJSbmEwUDRrUjA3QUdVQVE3dThIdnBrZEd6dzg3N2YxTFZCWko1WGtzLTJoU292LVZBVnczblkxaGFQa1RYWVdKbEo3WkRkRkszMTJIYWFaWjRTc2xiVEE0bEw1WncyNXFDU2tfTHJBR3FjdV9Dd2VoVjJwSy1sc195dHkwTk0?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxQNDRYZi1iRTN4RE5Yc291aG4zbnNWS3gwNkJYdkxrOGhvU3ZfV1loeFJLcy1YeG1JVHplSW1EVG1fZkxESmEteXhMQVphVTVYc3NrUEEzMU13SE1vQXAzak5HVHAtRExjWnJYRXhHaXR2ZkdqelJQUVljMlZCWXpMb2F0ZUxkRGVMV3Rr?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxNYUJRRlhFV2lBa3k1R2N2ZVhJbGRkOHptTFd0bkZ6X3puT1RjS2JUUl9abkVVY25xdXNjWmcxTUw3UUxsNnNxMFIwUG5EeUVNbXFEdWtpc3VibzBtU25vaWFvalpkVVYyUjFzSGxiYTY0cENjVFVJSWpRSng0emotd3lUOGlaOEN5RFlidERPNA?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxNNDJMd2R3QkRqZ1U2dXMzT0VEMXEyVV9Ia1BCUDFvRk1OYy1GNV9HTWdqVlRXV3ZFd2tZSmRUT05PV1RoQ0JQTlBnZmJENC1TMUFxdGE2eW5nR2hSR2NqNkZHdzJ6aTNWZHJFS1RUM0dIa2hLZ3FWX2I4aFQ3UVBSNkhmSWJOZVVqcDJ3SjBnOA?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxOYVlUZjJnTXBSZ3R0LVBzejFUcDQ5MklPeURDajNjR3BNLV96dXlDYU92U0QxTnlIVG92WE1oTlNOQW5ub0NNN2tRSzRzcGo2NUREdk51cFo2UW1oajN0akNBWWFuNFBZREhTdUg4d1BrTjgwb3Bua3U4Z2JVektQeG04NEVzNS1NS1VaR0Jn?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxOd05hZV9CR1JuTWw5ZUE3Q0pyU2gyaHp0cEFGQXYtS3MwSUdaV2JpN2E3a3E0VjlmUldBNWpjLVFyeDNiY3JnX1haTjhsY28xa2VpbFdXLU9TMk1RazhkOVRqX296dFZKNFVkWE84dnFWcVNicEhKcFFualpFS0pYSnpwWXI3QlVpdkhVQ2trckJQcUhIemp0aWV0MGxNQk91a0dpd0llVFJrdy1BVmJWcWtORU4zNUVmQ2VBY29nWGYtdkZXNzZV?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOaHNQa3M3bTI2SGJnemZwMTlSTEdQMHNJRGZOY0lRcGl3VXhmQ01DS3pvNlFBbHR5ME9wdzJDTTRqei1OU2FnbkNmWTgzTFR2cHFHS2ZubTBCMUVab3NKSG45UGlUTktkQmpZSTBqUTdQR2xIU2xFWVE0OFFkSTJmVVFIa0h3b3B5c2tZaDQwSkltR2RxRGNTVnlvUQ?oc=5
- https://news.google.com/rss/articles/CBMifEFVX3lxTFA3NV9JQnhaTjM4SlJTN2VsaUd4MXZLUVpLUGc2NXcxM0RBUmxycGdSVjZ5c19RT2xCUktWTDdWYUZ2a3RTSmNrdUZZalBMRDlHUlhvb2gwT2lxdE8wTzktNDZ0ZHRrTUxfeU9vdTJSdUJ1emdUUlFxME51N00?oc=5
- https://news.google.com/rss/articles/CBMif0FVX3lxTFBqeWRleVNIT3JOR2duMEJ4T0xfZjZ4Y1ppMEpHSTlnajNvZzI5aUxYbWh6eDBwWFhmdlgydk0yT1NrSHdQY3NLemJrdE5uc1d6MkZuQ2VXa3htN183TjVHS1lSSUpKOTFxRkxuMGZPVmo0a3V4VHVQNVdPYnZlNEk?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOeDZaZ0RBRUZ2aDQ0TV9lUWtzWkNuUk81RFhOSUVZSVYtcExFazBhRlR5LXdVR1BESjdyTXlsekh3azNJRERnU0hINGpBdEFFRFhWZHoxOXVFY0JBbDlfUXRfakFPaG5rMy1Ub2JaVlVxTlJJQzhGcG53SkliNUl2a01UTUR0UGE1RWxzVFhpLV9aSGVZY2c?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQeW9YX2JfMVZfN2FVVGZXWmdNS181YzFZaWU5elRHeFlpMmNWZGJ3eWUtcmtPWnl1cFEzZE1aa3lZYkMxM1lYWW93WWw4dzgyQUVuRUd3ZTZiSjdhRVh0Wk0xVndjU2hLdmJHR1FrMExCdFVubWM3QXJubnpXX2NJcUpJQnB0VDFYVlo2STBjYlJ3YUtDdU1vM1Ezb1Y?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxOM1ExY0ZwQllsOVIwaUUtMnc0WXpLNi1rQklwaGV5b3hBdV9NM0hfM1A3ekpYNVREajg5eTloWWR2Szc2VnA5c1NialNVWjRzdmdSQ3hPbHNTRTlCSy1Hc01rb1BSc2JUS3VQMC1hOF9RY0p6c3JScUtkenpsOGY3d0xPSUdseVY2SGw4M2RZSUd6Qjhjd1JyMkc5cUkxNzhRS2lBdTlvdVFNMzZaT2F1aldzODNlZw?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQWXc0TzBOUndZQ1Q2Y0xrRlZMZmU5VlhhWm1tOEt5WXhHaERMeFE4TjhWUnFlTzl5bDBrZFFxWDhxNXdreEpOdU9zQkUtQi12QUZ5SkZMdnFPNjlsUlBUNmxZcGpKaHl6Yzg5aTd1eU9aYm5RdkVUMEZiWC1uenY3ZHlpX0N1UFVjM1dVZWdhNVgtT1U2?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
