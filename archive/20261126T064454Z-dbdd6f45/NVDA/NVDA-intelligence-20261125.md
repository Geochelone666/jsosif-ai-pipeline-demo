# NVDA Intelligence Report

- ticker: **NVDA**
- Report as_of: **2026-11-25**
- Market data as_of: **2026-11-25**
- Quant sources: https://finance.yahoo.com/quote/NVDA/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVDA/key-statistics/
- AI analysis snapshot as_of: **2026-11-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-26T06:53:16.400902+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 4, 'ai': 17, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261125T065354Z-0b3565c6/NVDA** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'negative_sentiment_in_tailwinds': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 10 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 41.67%; oldest publication 2026-11-23

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 149.3000 |
| Return 1D (%) | -3.9130 |
| Return 1W (%) | -1.0996 |
| Return 1M (%) | -29.2283 |
| Return YTD (%) | -19.7591 |
| Return 1Y (%) | -15.8375 |
| Annualized volatility (%) | 52.2853 |
| Beta vs SPY | 2.4270 |
| Max drawdown (%) | -47.5297 |
| Sharpe (rf=0) | -0.0844 |
| Downside deviation (rf=0, %) | 31.9966 |
| Sortino (rf=0) | -0.1379 |
| Historical VaR 95% (1D, %) | 4.3052 |
| Historical ES 95% (1D, %) | 5.9994 |
| Correlation vs SPY | 0.6930 |
| Tracking error vs SPY (%) | 43.2973 |
| P/E (trailing) | 16.04 |
| P/B | 13.50 |
| EV/EBITDA | 14.55 |
| Revenue growth (%) | 103.20 |
| Forward P/E (estimate) | 8.99 |
| Gross margin (%) | 74.92 |
| Operating margin (%) | 66.08 |
| Return on equity (%) | 117.36 |
| Free cash flow yield (%) | 2.75 |
| MA50 | 203.6544 |
| Close vs MA50 (%) | -26.6895 |
| MA200 | 202.6206 |
| Close vs MA200 (%) | -26.3155 |
| RSI (14, Wilder) | 37.4527 |
| MACD (12,26) | -16.9154 |
| MACD signal (9) | -16.2396 |
| MACD histogram | -0.6757 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVDA': 290, 'SPY': 290}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 149.3000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -3.9130 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.0996 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -29.2283 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -19.7591 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -15.8375 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 52.2853 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 31.9966 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.1379 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.3052 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.9994 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6930 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 43.2973 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.4270 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -47.5297 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.0844 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 8.9911 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.9210 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 66.0820 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 117.3640 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.7528 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 16.0365 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 37.4527 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.6757 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -26.6895 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -26.3155 -> Clearly below the moving-average trend level.

## TAILWINDS

### Nvidia stock stumbles again after Jensen Huang's spectacular comeback rally
- Summary: Nvidia stock stumbles again after Jensen Huang's spectacular comeback rally
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxPRjhpLUVxeElZVDJYWkRuMEZkMmFOUW85NDlnZjVKTnRxTHRvZlZHQlZwRjZGNmZPaUdVdlkycC10RzQzSm1nZ0taalgzajJLRzNIb0lGd3RCb183WGhJMlN1Ul9QTEQ5a2VhcVdYM0ZNWnFHOG9JT29tc1FtMzlzTm5DZmVHTUpSQWdIc2pMaFBnN29TUEpzSlZPeHVBZ3Q1VDBKRUJYczl2ZGNmMjgyUVZIT1R1NkYtM0EwRzF0X0ZDNWRqT2VZM0g2Um8xVU5SaTZzNQ?oc=5>

### Anthropic’s Chip Choices Could Change the Nvidia Story. Here’s How.
- Summary: Anthropic’s chip strategy may benefit Nvidia’s market position.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxNSW1VTjZHMTM4LWRZT292cVltYmZJSUd5clVvOTZjQ3c5MlNxZEhnaFVyVzVTWlNMRHBmQ1JoYXJCRlRDQmgxRXQ0ZWlqRmVkTk9Yb01taVJYVnAyZ1NUSzBuQlFsVXd1WmV5bGZNLUl0OWd4ckNrY0lHanA2TjRIdTNwenhCWHh0M3NEWkEybEtxZ1FIN3FhRUdxV2VUNnNCTVNteC0wblBwNV9H?oc=5>

### Nvidia, AMD, and Micron stocks trim steep losses amid jittery AI trade
- Summary: Nvidia stock trims losses amid jittery AI trade.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxOVk9mVUxsUll4NmpxRklUb1dFaHduU3ZURXZRV2ktV0pDM2ZMNElPb3RrV0NiS0JlLTVXQXJKNnpTV1JmV1k2NGMtdzNLa0F0c2tsY2xRMmJKZHhwY1dueWZXb0l4VXhWNkl4NmJ6QUlTNjBpZUItN0xkX21JUXJ5WGlUbWdON0E0V2FOT2lGYkozcm9VSjlXVjR3SDc5WWQ3VzJhWm5mb29YbjBQSU1hQURkYw?oc=5>

## HEADWINDS

### NVIDIA (NASDAQ:NVDA) Stock Falls 3.9% - Here's Why
- Summary: NVIDIA (NASDAQ:NVDA) Stock Falls 3.9% - Here's Why
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQbVFEVmJNSXJDTkhQdGZ2bWJUZGdJUUpfRlF3eEtEWlJrem5fQWNpVWgwUERuOGpLZnNnVXpVdkRSYmxQZU1IU2d3Sko1Z0EwdHRCTi1oWVNvbS1aZWQ1cjI3SzJOSGVRdnA1OWp5MVM3ckhoeVcwWVZFMDY4QzMyOFhGYnk2Sjd4VXowTFVOYXY5T2pSSmdQcUl1OXB2U1djeEJlMmln?oc=5>

### Nvidia Stock (NVDA) on Verge of Forming a ‘Death Cross’
- Summary: Nvidia stock may form a death cross, signaling potential downward trend.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxPSlUwSXVvMzJQUTVwaGhHODNzZjF5UTRoLUZjSDB0TGJTNEstejZOWXZhR21PTmFxMmRic2RzeTRrVVdqT0M1amV0dUIxc3VOeWk3dWMzcFNJXzAzN2ZRdjdtQnM1UFpvYW03UTk0Wm9PRmNVbXc4S1V3YVBCS3BFdTZOX0JqNUJX?oc=5>

### NVDA Stock Alert: Nvidia CEO Jensen Huang Rejects Calls for Succession Plan
- Summary: CEO Huang rejects succession plan calls, raising governance concerns.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQanBEQ2g0YVdlS0owSUNzQXQxV0pnMjVfZ3M0di1YaFIxejgxT2lVeGIyQThMT3dOMUlkQ3IxLVNlYlhFVFMySHE4UWhQQWFtNDZycDhUSXNyZTJCZXo3ZjFoM0JMZXNqcjF0NXVORXF0Uml3cjdaWmhjMEZSRUZ4UDFLbmFCSUJqQTBZZkdMTVoxVjVJR1Zn?oc=5>

### Why Nvidia Stock Continues to Fall After the Jensen Huang Pop
- Summary: Nvidia shares decline post-Jensen Huang announcement.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxNeEdUYmZIR2RoMjZ5ZGR0dWlNU002TXhHeGoySnJSTjVObWlzVDhZYk85WW1FaWNndzFkR05tYk9LTkdCcUo4QjNPVzdoMWNnZkg0U1hCV05WSlhyQUpYNmVURDJCRFdyQWhsNTZsNDVQeWppbUdHeFQyNnFsV01LaThmZ3lXUEVIOWlRMnFRUU12bVdMY2haY2xhM2NZUzE2ZllMZkhINA?oc=5>

### Michael Burry Loads Up on 3 Chinese Stocks; Sticks to Nvidia Bearish Bet
- Summary: Burry’s bearish stance on Nvidia fuels negative sentiment.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQWUNHTm9Qakozcnczd2hxR21qUFRnYjBORTFjY09lblpNQnVSQ29kTFBDSFMzM1RiVUFFWTVrd2d4V05UMW1TTTJxSVlVYmxOOWczSHlQNDU0X09JVGxzVGdSeU05NDBKSERpc21IejNneXdieXZwTDZSdVhYdkxDb2NSSVFYMGtWZ0hNWksybjdkVVl1TkdLaFN3?oc=5>

### Nvidia stock continues to fall after massive rally, Jensen Huang apologizes to employees
- Summary: Nvidia stock falls after rally; CEO apologizes to staff.
- Date: 2026-11-25 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi6AFBVV95cUxNYnBZTkhUUGlCUVBvdW9Mam9JbGJueElLNmRUenk3eTZ2YmhXSEJhb3VCTTlrQ0xDZzF1N3pURFZFNDROVkZhOW1Mc0JxQUhGQ25rSjdWZXdxMnZNLWFaNzJfdXdFeEpUMzFQMUl3alZfWVotcFRHRGxSRzNiWHJuSlpyaXVHTld1MDFLSy1rdDJCU1F6ME9vZDB1bzB2bS1PeHpZbTg5czJrQ1lzdFRHbUlmS3JzYlFvQnRjZ2xRT3hoR1FVMUQ2a0hNMXZwNEtYckw1Q0ZYOThJMTlobXZTY3JzdDFESjBN?oc=5>

## CATALYSTS

### Nvidia (NVDA) Stock Looks Below Fair Value After Recent Turmoil
- Summary: Nvidia (NVDA) Stock Looks Below Fair Value After Recent Turmoil
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQbUpxbnpVNGpTNThJa3dsbWR4R3cyQ3hWbVFydFJ6bW10dldabWVTU3hPMGRoZlFhczNXZWgzbHppOVBIZzNKb1VTNWZ0dFd3S3lHdTJFRkdJOUo2N0FIQ1I3VnVPLVdwSWdmS1NsbWVmVW9WVXdrOFI5TnV2a1JFb0dfVWRjUWxMMUhwT0FQdUdRMEFvVFBjTjZR?oc=5>

### Nvidia Just Delivered Its Latest Earnings Report. Is the Stock a Buy Below $160?
- Summary: Nvidia Just Delivered Its Latest Earnings Report. Is the Stock a Buy Below $160?
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxQaGIzVGRHN0JkaFdjMG5nQnNTcGZQNW1nX1NjbDdjOGR6LXU3TU5UTjdkVG9NbHlIQ3dXVHNyZ2pUWDdQQ0czc1dwdWVzeUt4ZTBtWnpvcThSUUJjTGpzMXdzR0xNNmhWZnV1SGxkRjVGS1NKV01xcHZYSGtCWTBhUHFZUW9FcEJHTVpmZXhLWEpveDRUc09MUG5hUlpwVDVwaUl6Zg?oc=5>

### Is the AI Rally Safe With Jensen Huang Back at Nvidia—Here’s What Wall Street Thinks
- Summary: Wall Street assesses AI rally risk with Huang back.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxQeGVqQi1qQ0dvVlVDWXlNVUNSMklhbzdZWFBRWnZMbVlXVkpDZjZxd3dpNm4tM1RSLVF3QjFETHljS05TbHRDWXBXdlFCTlVyZXpGU3lWV21UU0YwU01VT0N5RGl5ZUxieVBUM0xQZkV5cTgzR3JZOXFLNjJPdzdZWHQxdVZDc0dHS2RudXFnU1pLNFpTU19SNWMtWkwtcmF4T1NIbXNaOUUwbkR5RVB6UDFuRTdua2xPejJHR3l1NnJkZXZ2?oc=5>

### Stock Market Today: Dow, Nasdaq Surge As Jensen Huang Makes This Nvidia Promise; Anthropic Falls
- Summary: Jensen Huang’s promise spurred market rally, signaling positive outlook.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.88
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxQbFRJSUJYanAyQ3Z1TzEwdDRnM084bjRZUTJNYlpHMDFZVk9zZzJ1d2NjSVUtcHpGWFpaVEppMzR6N203ZFVyRVRJQlpKSDY3TGMzMkUzMVVZRlFsUl9EdXdvY3FIbVEyVF9lcmdiNWdicl9McXU2NUNFMjIta0RmbEVkQ01nUXZ2NzRZYXJfTExSVVlNRE93SEN6ZFJ5N2Z1NXotbVZWQjNKMVlyYzRpdnNVRQ?oc=5>

### Why Nvidia (NVDA) Stock Is Falling Today: Tech and Chip Selloff
- Summary: Nvidia shares drop amid broader tech selloff.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPbUtXWTRwbjJyUHJSeW96c01xRU5wT0hINTlCU0hhRXpIc2dQa2hhSkpSRkwyeW9YSFhHOGpPVVRTb0Z4Tzd1Z3cyaWV0NWM2emR1Qk5lTktDdnhwYVBsTWdnOXFsbDVnV2hMVDNQbVNvNFJGeUVrTno2eDZSZExtWjZfZVRKMGNjT3czM2xHSm1OUEtnSG1SN0F3?oc=5>

### Nvidia Sell-Off: You Won’t Believe How Cheap the Stock Is
- Summary: Nvidia stock falls sharply, seen as cheap.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOcU1sN2NqMk9iRHNZTTNZTldZRVc4UWhvZXhTZ0NOd3M3TEphU2JXbmxyaTZoTnJXOHg3SjlTamhxb0FvZlFTQVo2OERzeldyQXNQanJzZmhYUFNYWXI0MmE5UThjVXN4OUEzUHVWQ3FQSkFBTFV1VlROQjN6ZmZYVVQtV2VzWnRod1R4TXVIMFJPVFBGTGVteFgwTlU4RUx4?oc=5>

### ‘Big Short’ investor Michael Burry pinpoints the next time he’ll be betting against Nvidia stock
- Summary: Burry signals future bet against Nvidia.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxOSXJabHpKbGl3S2tfeW9PM3M3V3JCaGpQOWEyZjZET1VzSERvZDRIYWhFeDdIallVUmF1V2g1UkFEM0ZpZHA4RkQ3QzREVGJfMUFLZzZlYWN3RE04Qllqa1Mzb0JIX2hSMDNXWmtFTGVQdkR2Z0c5aUZMQ2tmSHBua2d2bWwwSUFYY0VKcVliY1pRZw?oc=5>

### Why Nvidia Stock Is Falling Again
- Summary: Nvidia shares continue to decline.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxNYVQ1RTVqbTdmZFZzR1hlWDRsQ2FTNHUyUW9GQjA4c3VxRm1OMTlVWlBVNjk5VjFIcDJTY1NZc3dxOWxyVWJ3NHZoV1hmUzBsUXZ0ek1GZGwxcWRwUGV1cUxhajlHblRMZ3FXNFZ2d2k5QVowNE4zMTByakR6ai04ZFZR?oc=5>

### Is Jensen Huang Really Worth $954 Billion to Nvidia?
- Summary: Questioning Huang's value to Nvidia.
- Date: 2026-11-25 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPWUVyd2llVG4zZ09TUlU0cElYSXY3NjFHQ0Z0dVFDNUd4R2tUa3R0Y2FiZi02ZHZQMG1LN1doOHA3N2FLZmlIX0VDVlpJWFYtMHI4WEpYbmhxY1JGRWFTTHg4amRiTzB4QmRfR0NKSThvMXJIeEdnUWlNOUxVZlRfR2c0NWZoMEFsTHNVSjRjYVBiU0ttVksyRmIzR0s?oc=5>

### 5-Star Analyst Revamps Nvidia Stock Price Target for 2027
- Summary: Analyst updates Nvidia 2027 price target.
- Date: 2026-11-25 | Impact: medium | Horizon: long | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNS2hzS1B6LVBLQ0RHeU1Za29PUWxpRWdMeVc2cXhPZm1lWF8zYkFIenR6VFR0d0Naa2F2cEN1M0tvbDV1Y3dzdTYzTXZ0cVVRakVLMzRfTU91eDJWb1VZWHFieG1QSF9adzlfeGpBUEpRTkxTQzVyTzJUU1JkU1lORHlFa2xyWDJjYnhmOWFhY2F1RE82anh1SGhR?oc=5>

## RISKS

### Nvidia’s Top Lawyer Sold $4.5 Million of Nvidia Stock the Day Before Its 14% Plunge
- Summary: Insider sold large stake before sharp decline, raising concerns about confidence.
- Date: 2026-11-25 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxQRkE4VnFkcDdSOVlQc1cySDl4S2FrYTQ5ZFdlOVNVblRQbm9na2J4VDc4Y201U2VZMEU2ekxDV3pOSWZBSmo5a003Y29XdmE4VjJoZGVtazEyenVXZVZSWjhjeUt4QVdmV0c1NFJTZWVXdE9xc1padmh6YVg0VmNzNkNMTEpFTmxoMUdLWUxfeUdveGlQS0t3ZGVLUzZQN1dZMVpUOFppYTkteFRYLXhuVUVGY240VWpIaGJRd0w4eVNUUQ?oc=5>

### The Nvidia Scandal Set Off a Chip Crackdown in Congress. Which Stocks Are Most at Risk?
- Summary: Congressional crackdown poses regulatory risk to Nvidia.
- Date: 2026-11-25 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOQ080MUVCYUxiMVpjODdXWmJuX1hNbDFGMHVfUkk4d3ZjZlYzc1lrM0dUSTAxNWNlZ3prdTNnUWwtcGYxVFFGU3FYZXhrUDRuaEdwWlUyaUFkbEd1Y3loODBkQ1gzYXN4Y0lsb2dHckFLVGZTRmlGT3EtTm01N0pHWmMtdnBwT0R3OEpvenR6WWkwaks3elRz?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVDA** | **16.04** | **13.50** | **14.55** | **103.20** | **3,605,147,156,480.00 USD** | **-15.84** |
| AMD | 86.76 | 9.74 | 59.17 | 44.70 | 672,006,275,072.00 USD | 96.98 |
| AVGO | 38.42 | 14.41 | 28.16 | 85.50 | 1,436,194,177,024.00 USD | -21.28 |
| INTC | N/A | 2.52 | 15.80 | 20.90 | 289,508,032,512.00 USD | 52.02 |

Peers fetched as_of: 2026-11-25; NVDA reuses existing data (market data as_of: 2026-11-25); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-17
- Next expected earnings: 2027-02-24 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-25

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

- https://news.google.com/rss/articles/CBMi1AFBVV95cUxPRjhpLUVxeElZVDJYWkRuMEZkMmFOUW85NDlnZjVKTnRxTHRvZlZHQlZwRjZGNmZPaUdVdlkycC10RzQzSm1nZ0taalgzajJLRzNIb0lGd3RCb183WGhJMlN1Ul9QTEQ5a2VhcVdYM0ZNWnFHOG9JT29tc1FtMzlzTm5DZmVHTUpSQWdIc2pMaFBnN29TUEpzSlZPeHVBZ3Q1VDBKRUJYczl2ZGNmMjgyUVZIT1R1NkYtM0EwRzF0X0ZDNWRqT2VZM0g2Um8xVU5SaTZzNQ?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxNSW1VTjZHMTM4LWRZT292cVltYmZJSUd5clVvOTZjQ3c5MlNxZEhnaFVyVzVTWlNMRHBmQ1JoYXJCRlRDQmgxRXQ0ZWlqRmVkTk9Yb01taVJYVnAyZ1NUSzBuQlFsVXd1WmV5bGZNLUl0OWd4ckNrY0lHanA2TjRIdTNwenhCWHh0M3NEWkEybEtxZ1FIN3FhRUdxV2VUNnNCTVNteC0wblBwNV9H?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxOVk9mVUxsUll4NmpxRklUb1dFaHduU3ZURXZRV2ktV0pDM2ZMNElPb3RrV0NiS0JlLTVXQXJKNnpTV1JmV1k2NGMtdzNLa0F0c2tsY2xRMmJKZHhwY1dueWZXb0l4VXhWNkl4NmJ6QUlTNjBpZUItN0xkX21JUXJ5WGlUbWdON0E0V2FOT2lGYkozcm9VSjlXVjR3SDc5WWQ3VzJhWm5mb29YbjBQSU1hQURkYw?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQbVFEVmJNSXJDTkhQdGZ2bWJUZGdJUUpfRlF3eEtEWlJrem5fQWNpVWgwUERuOGpLZnNnVXpVdkRSYmxQZU1IU2d3Sko1Z0EwdHRCTi1oWVNvbS1aZWQ1cjI3SzJOSGVRdnA1OWp5MVM3ckhoeVcwWVZFMDY4QzMyOFhGYnk2Sjd4VXowTFVOYXY5T2pSSmdQcUl1OXB2U1djeEJlMmln?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxPSlUwSXVvMzJQUTVwaGhHODNzZjF5UTRoLUZjSDB0TGJTNEstejZOWXZhR21PTmFxMmRic2RzeTRrVVdqT0M1amV0dUIxc3VOeWk3dWMzcFNJXzAzN2ZRdjdtQnM1UFpvYW03UTk0Wm9PRmNVbXc4S1V3YVBCS3BFdTZOX0JqNUJX?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQanBEQ2g0YVdlS0owSUNzQXQxV0pnMjVfZ3M0di1YaFIxejgxT2lVeGIyQThMT3dOMUlkQ3IxLVNlYlhFVFMySHE4UWhQQWFtNDZycDhUSXNyZTJCZXo3ZjFoM0JMZXNqcjF0NXVORXF0Uml3cjdaWmhjMEZSRUZ4UDFLbmFCSUJqQTBZZkdMTVoxVjVJR1Zn?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxNeEdUYmZIR2RoMjZ5ZGR0dWlNU002TXhHeGoySnJSTjVObWlzVDhZYk85WW1FaWNndzFkR05tYk9LTkdCcUo4QjNPVzdoMWNnZkg0U1hCV05WSlhyQUpYNmVURDJCRFdyQWhsNTZsNDVQeWppbUdHeFQyNnFsV01LaThmZ3lXUEVIOWlRMnFRUU12bVdMY2haY2xhM2NZUzE2ZllMZkhINA?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQWUNHTm9Qakozcnczd2hxR21qUFRnYjBORTFjY09lblpNQnVSQ29kTFBDSFMzM1RiVUFFWTVrd2d4V05UMW1TTTJxSVlVYmxOOWczSHlQNDU0X09JVGxzVGdSeU05NDBKSERpc21IejNneXdieXZwTDZSdVhYdkxDb2NSSVFYMGtWZ0hNWksybjdkVVl1TkdLaFN3?oc=5
- https://news.google.com/rss/articles/CBMi6AFBVV95cUxNYnBZTkhUUGlCUVBvdW9Mam9JbGJueElLNmRUenk3eTZ2YmhXSEJhb3VCTTlrQ0xDZzF1N3pURFZFNDROVkZhOW1Mc0JxQUhGQ25rSjdWZXdxMnZNLWFaNzJfdXdFeEpUMzFQMUl3alZfWVotcFRHRGxSRzNiWHJuSlpyaXVHTld1MDFLSy1rdDJCU1F6ME9vZDB1bzB2bS1PeHpZbTg5czJrQ1lzdFRHbUlmS3JzYlFvQnRjZ2xRT3hoR1FVMUQ2a0hNMXZwNEtYckw1Q0ZYOThJMTlobXZTY3JzdDFESjBN?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQbUpxbnpVNGpTNThJa3dsbWR4R3cyQ3hWbVFydFJ6bW10dldabWVTU3hPMGRoZlFhczNXZWgzbHppOVBIZzNKb1VTNWZ0dFd3S3lHdTJFRkdJOUo2N0FIQ1I3VnVPLVdwSWdmS1NsbWVmVW9WVXdrOFI5TnV2a1JFb0dfVWRjUWxMMUhwT0FQdUdRMEFvVFBjTjZR?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxQaGIzVGRHN0JkaFdjMG5nQnNTcGZQNW1nX1NjbDdjOGR6LXU3TU5UTjdkVG9NbHlIQ3dXVHNyZ2pUWDdQQ0czc1dwdWVzeUt4ZTBtWnpvcThSUUJjTGpzMXdzR0xNNmhWZnV1SGxkRjVGS1NKV01xcHZYSGtCWTBhUHFZUW9FcEJHTVpmZXhLWEpveDRUc09MUG5hUlpwVDVwaUl6Zg?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxQeGVqQi1qQ0dvVlVDWXlNVUNSMklhbzdZWFBRWnZMbVlXVkpDZjZxd3dpNm4tM1RSLVF3QjFETHljS05TbHRDWXBXdlFCTlVyZXpGU3lWV21UU0YwU01VT0N5RGl5ZUxieVBUM0xQZkV5cTgzR3JZOXFLNjJPdzdZWHQxdVZDc0dHS2RudXFnU1pLNFpTU19SNWMtWkwtcmF4T1NIbXNaOUUwbkR5RVB6UDFuRTdua2xPejJHR3l1NnJkZXZ2?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxQbFRJSUJYanAyQ3Z1TzEwdDRnM084bjRZUTJNYlpHMDFZVk9zZzJ1d2NjSVUtcHpGWFpaVEppMzR6N203ZFVyRVRJQlpKSDY3TGMzMkUzMVVZRlFsUl9EdXdvY3FIbVEyVF9lcmdiNWdicl9McXU2NUNFMjIta0RmbEVkQ01nUXZ2NzRZYXJfTExSVVlNRE93SEN6ZFJ5N2Z1NXotbVZWQjNKMVlyYzRpdnNVRQ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPbUtXWTRwbjJyUHJSeW96c01xRU5wT0hINTlCU0hhRXpIc2dQa2hhSkpSRkwyeW9YSFhHOGpPVVRTb0Z4Tzd1Z3cyaWV0NWM2emR1Qk5lTktDdnhwYVBsTWdnOXFsbDVnV2hMVDNQbVNvNFJGeUVrTno2eDZSZExtWjZfZVRKMGNjT3czM2xHSm1OUEtnSG1SN0F3?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOcU1sN2NqMk9iRHNZTTNZTldZRVc4UWhvZXhTZ0NOd3M3TEphU2JXbmxyaTZoTnJXOHg3SjlTamhxb0FvZlFTQVo2OERzeldyQXNQanJzZmhYUFNYWXI0MmE5UThjVXN4OUEzUHVWQ3FQSkFBTFV1VlROQjN6ZmZYVVQtV2VzWnRod1R4TXVIMFJPVFBGTGVteFgwTlU4RUx4?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxOSXJabHpKbGl3S2tfeW9PM3M3V3JCaGpQOWEyZjZET1VzSERvZDRIYWhFeDdIallVUmF1V2g1UkFEM0ZpZHA4RkQ3QzREVGJfMUFLZzZlYWN3RE04Qllqa1Mzb0JIX2hSMDNXWmtFTGVQdkR2Z0c5aUZMQ2tmSHBua2d2bWwwSUFYY0VKcVliY1pRZw?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxNYVQ1RTVqbTdmZFZzR1hlWDRsQ2FTNHUyUW9GQjA4c3VxRm1OMTlVWlBVNjk5VjFIcDJTY1NZc3dxOWxyVWJ3NHZoV1hmUzBsUXZ0ek1GZGwxcWRwUGV1cUxhajlHblRMZ3FXNFZ2d2k5QVowNE4zMTByakR6ai04ZFZR?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOVnZYQmNDcUVPbkdnb3J6b2xpMU9DVFFqbTNBdDFnTUk2cDBHbTNXQnBuVk9vRWVVdmYwN3dCWjF5RTZRSXV3dENOVGRnLU9BYjkxelMxNi1jRVpneUVmOEdoVjVSUGszREFxNE0xVjM2b2FlOXF5UDJQV0VEVEJra2lCeC1iZUpIQmF1SnZpWklreDQ2MVpjZG90NA?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPWUVyd2llVG4zZ09TUlU0cElYSXY3NjFHQ0Z0dVFDNUd4R2tUa3R0Y2FiZi02ZHZQMG1LN1doOHA3N2FLZmlIX0VDVlpJWFYtMHI4WEpYbmhxY1JGRWFTTHg4amRiTzB4QmRfR0NKSThvMXJIeEdnUWlNOUxVZlRfR2c0NWZoMEFsTHNVSjRjYVBiU0ttVksyRmIzR0s?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNS2hzS1B6LVBLQ0RHeU1Za29PUWxpRWdMeVc2cXhPZm1lWF8zYkFIenR6VFR0d0Naa2F2cEN1M0tvbDV1Y3dzdTYzTXZ0cVVRakVLMzRfTU91eDJWb1VZWHFieG1QSF9adzlfeGpBUEpRTkxTQzVyTzJUU1JkU1lORHlFa2xyWDJjYnhmOWFhY2F1RE82anh1SGhR?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxQRkE4VnFkcDdSOVlQc1cySDl4S2FrYTQ5ZFdlOVNVblRQbm9na2J4VDc4Y201U2VZMEU2ekxDV3pOSWZBSmo5a003Y29XdmE4VjJoZGVtazEyenVXZVZSWjhjeUt4QVdmV0c1NFJTZWVXdE9xc1padmh6YVg0VmNzNkNMTEpFTmxoMUdLWUxfeUdveGlQS0t3ZGVLUzZQN1dZMVpUOFppYTkteFRYLXhuVUVGY240VWpIaGJRd0w4eVNUUQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOQ080MUVCYUxiMVpjODdXWmJuX1hNbDFGMHVfUkk4d3ZjZlYzc1lrM0dUSTAxNWNlZ3prdTNnUWwtcGYxVFFGU3FYZXhrUDRuaEdwWlUyaUFkbEd1Y3loODBkQ1gzYXN4Y0lsb2dHckFLVGZTRmlGT3EtTm01N0pHWmMtdnBwT0R3OEpvenR6WWkwaks3elRz?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
