# CSCO Intelligence Report

- ticker: **CSCO**
- Report as_of: **2026-11-04**
- Market data as_of: **2026-11-04**
- Quant sources: https://finance.yahoo.com/quote/CSCO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CSCO/key-statistics/
- AI analysis snapshot as_of: **2026-11-04**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-05T05:07:39.426223+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 9, 'ai': 9, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **12** exact headline/source/date matches; prior report **20261104T044411Z-6b13f9ec/CSCO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 6 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 60.0%; oldest publication 2026-10-29

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 103.6100 |
| Return 1D (%) | 0.6215 |
| Return 1W (%) | -6.0568 |
| Return 1M (%) | -7.6560 |
| Return YTD (%) | 36.4671 |
| Return 1Y (%) | 45.3549 |
| Annualized volatility (%) | 35.5897 |
| Beta vs SPY | 1.1437 |
| Max drawdown (%) | -21.5461 |
| Sharpe (rf=0) | 1.2336 |
| Downside deviation (rf=0, %) | 24.2241 |
| Sortino (rf=0) | 1.8123 |
| Historical VaR 95% (1D, %) | 2.9985 |
| Historical ES 95% (1D, %) | 4.9898 |
| Correlation vs SPY | 0.4126 |
| Tracking error vs SPY (%) | 32.4719 |
| P/E (trailing) | 30.93 |
| P/B | 8.13 |
| EV/EBITDA | 22.73 |
| Revenue growth (%) | 17.60 |
| Forward P/E (estimate) | 18.43 |
| Gross margin (%) | 64.52 |
| Operating margin (%) | 27.72 |
| Return on equity (%) | 27.32 |
| Free cash flow yield (%) | 2.74 |
| MA50 | 109.5156 |
| Close vs MA50 (%) | -5.3925 |
| MA200 | 101.3015 |
| Close vs MA200 (%) | 2.2788 |
| RSI (14, Wilder) | 40.1403 |
| MACD (12,26) | -1.8503 |
| MACD signal (9) | -1.1411 |
| MACD histogram | -0.7092 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CSCO': 275, 'SPY': 275}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 103.6100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.6215 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -6.0568 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -7.6560 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 36.4671 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 45.3549 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 35.5897 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 24.2241 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.8123 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9985 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.9898 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4126 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.4719 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.1437 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -21.5461 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.2336 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 18.4293 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 64.5240 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 27.7190 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 27.3190 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.7375 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 30.9284 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 40.1403 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.7092 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -5.3925 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 2.2788 -> Slightly above the moving-average trend level.

## TAILWINDS

### Cisco Gains From AI Networking Boom: Can It Outpace HPE & ANET?
- Summary: Cisco benefits from AI networking surge, potentially surpassing rivals.
- Date: 2026-10-29 | Impact: high | Horizon: short | Confidence: 0.88
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPR1QxblFweHdxYlBzMmFDWFQxRGNvWWQzZnpVVm9sSHlvVXFLcktyQllaT3h4UG1Tdlk5TjBEUzhQaXdiWG1JaUN4WVhIaGJIb1BkM2dlZ05DdEplaFdEUlhqdVNNTzE3Wl9BeHduZHY3bHBacXNvaFZhNDhxcWM4di10RXhjQ3hEeF9sN1ZfZERKQUZ4VkhwTjNn?oc=5>

### How Low Can Cisco Stock Go?
- Summary: Shares of Cisco are being discussed for potential price decline.
- Date: 2026-11-04 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxPNHJjVFhEbG1IQmplZ3pOVFNXbzVtY01oT0ZCdm53QVAwV19kV2dVbi1HVVQyYWxReTNmQ2xIUEZwdFoxcVBvSWJBbjRPaERhbjVTNnFmY0ZUM3Q4U0RYZTVEQlhZbW44ZVhKVFNZQTNWT0t6SjVENlY4alYtUDZCWnYyQ0dqQzQ?oc=5>

### Cisco Systems, Inc. $CSCO Stock Position Boosted by Provenance Wealth Advisors LLC
- Summary: Provenance Wealth Advisors increased its Cisco holdings.
- Date: 2026-11-04 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxNNmdKUExrYVZYSTNzX2dFY3kxQjd3UzlFSEg3aHIzeEtpeWRmTVlzSm1wckhlcVdlX0h5OGdkM2J4dkR4cHh2RENCZ0daUnEwaFdnRGstdUtDTlVyT0ZYUGI1VmNpREtnSnF6dWxaSGlKOU9aNS1OUWZaRG1BMnhVRlhSYnc3QzlodnRIZ1dhUF9lTW5iUXloaFRvMWFuRnZzSnVpN1QzZXQ5ZjU0akIwQXZYblZLNEtHMjJTdnN5YTVkV3B3OUN2QU9jeGVPcGEwcks2SWZQTQ?oc=5>

### 301,219 Shares in Cisco Systems, Inc. $CSCO Bought by Associated Banc Corp
- Summary: Associated Banc Corp purchased 301,219 Cisco shares.
- Date: 2026-11-04 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxQbmNCb2tyQ2ZPT0pVTjRLanZOYkVYTmNNQ3dTcll0UmkxeW5DMXRhQTdiQmIwOUNNVEpLM0ZmUXFkaC1PX2hMdGNLQXRXdXc1ZEJ1SEtpWFRyQzlNMVRyQ1BWX2E1RFF1NDdVeC1OR3dVOGpZMnVwbzJQZjR0WlFkYm9wRWh5VnU0NGh5OVhQYU1RZVVEY3g4T1ZHSmFmOGZ2U2Q0VkwwcDZsQWtIOVVHS05qZE9Kc29tTGZQNldzOGhCMG1nUU1xRDktcw?oc=5>

### Cisco Systems, Inc. $CSCO Position Increased by Vise Technologies Inc.
- Summary: Vise Technologies increased its Cisco stake.
- Date: 2026-11-01 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxNTW1OY2VvcDdEWUNjQjVQemphV3Y4YXRmNV9uRjd5dHdiX0VVVHNXZHFvdEdlMTRaRlZkd3FCTXVWUGVjaE43THdZS2RwQjNjM2FINFpfWWZhZVFkRkpFYlBXZ0tTOEx0QlNIcVZVV05FbFpVcjlfOE1iUEZSaXVZWnc4ZFoyZzdGVktQVUZtQWxfaFZBUjVUVWJBdThZZTJwTlNzVmtheUctY1QzRkdSbTA1V2FZVGZmdTU0bU5XYWd3RjRnZ0E?oc=5>

## HEADWINDS

### Cisco Systems Inc (CSCO) Shares Fall 3.8% -- What GF Score of 88 Tells Investors
- Summary: Cisco Systems Inc (CSCO) Shares Fall 3.8% -- What GF Score of 88 Tells Investors
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxOeGk2UUJEUDdQZURYT1BlaVBaQ01ibkU2Ujk5d0NTNzNPZnU0TjlLWWxFWWpGcEwyWDFNX3UtY1NLT05UQ21CdGEzTTE1Z0F6QU44S3paS1BWSWdMemExMkVyQmlDbGQ4Mnc4a0pRME41QUFTYWQxMjExZUwxS1Ztb2RPM01hQ2lmYks5akF5d29RanNPMTZvOW9wbXlhY0x5RzRieXpkR0xfNFJhWVNyYUVR?oc=5>

### Cisco Systems (NASDAQ:CSCO) Stock Price Down 2.8% - Here's What Happened
- Summary: Cisco Systems (NASDAQ:CSCO) Stock Price Down 2.8% - Here's What Happened
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxPNm1MTERFbkduR2VwaFBIdENsVFNDMkgteGVmV2xHSEd6c1djRTZyYzBTRFNQY2dJZmwxN0xIOE1GbEwxRThjMXpyV2NUeFY3Z2dRZEVYZE1aUU9jcGtha0hZYWtzbTloNE5jYTRrQXE1NUUySUxNbmswTk5aUl9VZk1rRWhubDFRNHZnb0MyT0JFeElLVjc4Vi1zRDVwb0MzT1NJQ1BmaGJSQlJGU1pBZDhzTlZGb0E5OTBvT2t5dnBfQTQ?oc=5>

### Cisco Systems (NASDAQ:CSCO) Shares Down 1.5% - Here's What Happened
- Summary: Cisco Systems (NASDAQ:CSCO) Shares Down 1.5% - Here's What Happened
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxQVG5fQXRDMUJGenBZSVVPOWk0SUp0Q281M0p6OGhYZWJPUFlCSnZHNWprYkRzT3ppQTIwVWpON3NWZUhmSDg4Vk1nYWZsTk5SZFU3VzdEZ3VnWnNkdXA5eHM0dGR0Z1pPTjY0dG1wY3dvTVRjNHdiMGxGbHlyRzBnWXA0Z1lqUVNkWHhocGNLRXRqSUdvLVZEeXV5LW1zcGpZR1lTUGpXYXB6aWZIeDFPVER6d3g0MEdGZHUzcg?oc=5>

### Cisco Systems Inc Stock (CSCO) Moved Down by 4.09% on Oct 30: Drivers Behind the Movement
- Summary: Stock fell 4.09%, reflecting short-term pressure.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNV05jeWZSZzZFU0JtbzRaZW5acXl3eHVqVUtRX0ZUamE4V1JyQ18yY0lmV2EzUEdkMWVoN2k0dkVMSk5JZ1pIeVlSRVVGalc3NDE1azMxSkR6LUZkMl9CM091NE54ZHZWbVY0VkJodm1mNGRORWNGa1NhbWhrZVpldzFqQzVOQW8zZlVv?oc=5>

### Why Cisco Systems (CSCO) Dipped More Than Broader Market Today
- Summary: Cisco stock fell more than the broader market today.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPTGtSaFE3OVRZdGp1MzdnWm1OWEZDYlpzZUMxUGlPaHVsRVVWZ2gyWENCTFk4dHJKMk9WdEgxdHRjeHFCVXNPbjNTOGExTlZJMDlDSXhZZmctUFpxSW1pZW9ISnFkUkUwcElKT1JfRDg2Z3UxVzR6WGw4bjJraVJ2SlhnYjZDcnJvdGpvNGY0RnhzZ1RYNFZxVDNR?oc=5>

## CATALYSTS

### Cisco Systems, Inc. $CSCO Shares Acquired by Rakuten Investment Management Inc.
- Summary: Cisco Systems, Inc. $CSCO Shares Acquired by Rakuten Investment Management Inc.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxQSXpIQjhxZmZobUVKdHU2N1VDQWlaYmxyOWFTczRPdXpheERpTjlrQXRERlkyWHlzME1kVHFIQUJodWE4NXFwdHdBTklkTzJubDNPUUFwWE4tLVNmYXBIVUxCWFdSZHdqZ2RPNkRiLVZvYWpZWFFNODVJNzMtLVp5eU1ZR3hENVdkM2hob3JHYzlVeU1NRU4tSWlqSzdydTRMaGxSWDhUdlpKSWIycHhOdGtJeE9QaV90NF82RnlGYXJYYVFmNktXaXYyQ1lrcmVRUHc?oc=5>

### Cisco Systems, Inc. $CSCO Shares Sold by GRIMES & Co WEALTH MANAGEMENT LLC
- Summary: Cisco Systems, Inc. $CSCO Shares Sold by GRIMES & Co WEALTH MANAGEMENT LLC
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxNQV84T3ktclhDV180c1dZZXFWUGhRbmgxZXBudUVZeFpuNWR0TDZybXlub2lXODY3SDBwbWZiZ0Y2X2drRkVFRU02cWxIVWRNeXJ2all0dlV5MVgtcm5HQXg0MkRqczVSNnczUXBmd1VIVnpRMmt0N1RLai1kNUMxR2dYTS0wMk1lWF9lN09xNGw0N0RxczdPSmZEcVFXR093RTRZQlZyOVVxMDRFeVNVRi1ZNHBCRFNVMnRpaEVlRElMOVZyUk93QTBR?oc=5>

### Cisco Systems, Inc. $CSCO Shares Bought by Aware Super Pty Ltd as trustee of Aware Super
- Summary: Cisco Systems, Inc. $CSCO Shares Bought by Aware Super Pty Ltd as trustee of Aware Super
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3wFBVV95cUxQZElNczBUU3NSRV9MZEJqMkJ3a3ZNcVBpazhVVHItVkhuWkVOZ2NxZnJ2LUZvR0hocEJrR2txektOQ1BPdzlFMWpndnNSRkFCQmdMWDZkN29oeXZNWE5GVThiYTU0ZFN1U2xGMXRmT2J1VlhXZ2R2LTAwLUZEdjhQNUV5bkVGYVZsM1cyc1N6WE1kX2tKVTJLQW1STTBZSlJOc3drbFVWT1dqSTZrUmxHZ0pPMUxfZGEyZTFYSEFnMTJWQWF1ZlMtUWNpSEk0RTNpSE1qRnZWanBuN04zcW9V?oc=5>

### Cisco Systems, Inc. $CSCO Shares Sold by Welch Group LLC
- Summary: Cisco Systems, Inc. $CSCO Shares Sold by Welch Group LLC
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxOR1o3WjZHSmU2MmNuRDFOUDhFX0hIaTNDRHdXSTRVVDJaZHZwUzRONXd6eXh2VW9scjFmNm5QRDB1b2RLSUhBc2JDUmE0MkFnbDY5T1RHaFVyMTlKajRRR2FPU0tzUkhLaG1NT0FJNjEzR3VxZmoxeDZxV0ctVmhlQ0hVTm9oVlc5NFdfbVNua2VBQjFuVGgtNUhQY0h6bjg5OGRWYmRHTW0yQWptbV9XQmFRUHY?oc=5>

### Cisco Systems, Inc. $CSCO Stock Bought by Choreo LLC
- Summary: Cisco Systems, Inc. $CSCO Stock Bought by Choreo LLC
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxNdGtSUFBTMm5RYjh4RFN2T2pmREU0ZWRXcGFsZDh2VWRYc3kybFkzcTlBX1ZZYXpUMGNvNktXNy1yZzNBOElyMkt5dUpqUFFMN2ZDMkQ3ZTBFV0RVanUzbWI2S0NRMUZheEV5WWtYbFhMSkUtelM4SFJNYl9rTS1vUGYxWkdfak1TZWlUNFFRTzZlY1dLWVFEQS1vOXFHdmV2bGZkSFFNNjhLVEtRQi1R?oc=5>

### Cisco Systems, Inc. $CSCO Stock: China Universal Asset Management Co. Ltd. Raises Stake
- Summary: Cisco Systems, Inc. $CSCO Stock: China Universal Asset Management Co. Ltd. Raises Stake
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxNSDVXTzlEcV9hWHNHR2tiU0lmclNlcWlMei1OOFZvenlRV3c5NzJOUTZFRG53SjBLVHlhT0JjREo4NmJtbmFTWEU5X2tVMnRLNjZuYm9ycExmREdpZDM0Z3E5dlJEMkZJdC1CMGQyN0hMZGNrS1dkVnVRdW5mVnlyX3FycTlnc0FlWS1QeDR0TTVJMGpWMWxfTVRESFNQVW9LZmdvcXBBY2NZQkxlVHI3MVJVcjJDWDdmV2RCQmtlelVqbHN3dzdBUHg5SHpRWGJjLWhMZGxZWlRPUQ?oc=5>

### Cisco (CSCO) Stock Looks Undervalued On Future Cash Flow Estimates
- Summary: Analyst suggests Cisco stock undervalued based on future cash flow estimates.
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxNRkVmNHFuMzZObmVHRkpVOEZZNFJmT3ZKQ0NGYjBtdTBQVFIwbko0Mk53UnFfNU05dTRPdE9MWXRKZWhjbVJ2dXJOdzJFaXBHWkNuZWxvNGRha0lKQ0o5OG82WXVpN0o2azdRV2dCQ3R1WE80QjB0dDUteTZjTG5NRU9YQWE1MFI5clJQaWIyUTNsXzBvVVpaM29FdjJZSlZ5QTlqSDdJc05zMmU2LVJzazVtMWlXcENGU0dGTzBCSEtxQXljNTdj0gHMAUFVX3lxTE1oM0RXNVdySG1lbmpDZ2gyYWpSNmFGRGdjR21kd3NHOURpZXFSTUdjMDVMaDJFc0c2emtWXzRfTnE2ckdoYjFjMjVMMWdQTTFmRUFQQy0zOFZwallqX1lhelQ0MHNmaGR0Mk5BTXRDM1lfSFNvX216UXlwVk1YaTktampMQXRseDdYdXhFcTEybzdFZmNNQzJEdmVOTVNQM0tMZllMZ05nVDBEUkhNUEpGS3JtSkp1bllURDE1SnZfOXZ5THRRbGRIdlNQZg?oc=5>

### Cisco Systems, Inc. $CSCO Stock: Parcion Private Wealth LLC Boosts Position
- Summary: Parcion Private Wealth LLC increased its Cisco holdings.
- Date: 2026-10-31 | Impact: low | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxORl9NbF9KQVNuaGlrRFR1UG1KUFZTYlg2SnFPbWl5aHhMZDZFQnBueURSY3ZobFJxZlVVS0ZEb1lLNkFpY2xvWjk4bVoyNzZzcnFhd0tZMHplTDRWYXRUNXgxSURxdTJuWVFoemU5S2w0QzFQeEhndW9VT1ZiLV9pT3lQMDcyc25xYnZSaE85QzN5V0VBRUlNYVllSFJ6WXBTajFwZFlsZEY0Rmc0UkVsbVJvRm0zYmFzMV9jdEVBS2JkU2tRRGJGdTZIajM?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CSCO** | **30.93** | **8.13** | **22.73** | **17.60** | **408,491,425,792.00 USD** | **45.35** |
| ANET | 45.53 | 18.13 | 43.31 | 37.70 | 225,103,380,480.00 USD | 16.24 |
| FFIV | 26.44 | 4.68 | 18.75 | 13.30 | 18,731,722,752.00 USD | 36.60 |
| HPE | 27.37 | 2.51 | 11.71 | 33.70 | 66,492,715,008.00 USD | 116.44 |

Peers fetched as_of: 2026-11-04; CSCO reuses existing data (market data as_of: 2026-11-04); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-12
- Next expected earnings: 2026-11-12 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-04

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-09-02
- Revenue (latest available single quarter): 12,844,000,000.00 USD; period 2018-04-29/2018-07-28; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 3,373,000,000.00 USD; period 2026-01-25/2026-04-25; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/858877/000085887726000132/csco-20260725.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimgFBVV95cUxPR1QxblFweHdxYlBzMmFDWFQxRGNvWWQzZnpVVm9sSHlvVXFLcktyQllaT3h4UG1Tdlk5TjBEUzhQaXdiWG1JaUN4WVhIaGJIb1BkM2dlZ05DdEplaFdEUlhqdVNNTzE3Wl9BeHduZHY3bHBacXNvaFZhNDhxcWM4di10RXhjQ3hEeF9sN1ZfZERKQUZ4VkhwTjNn?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxPNHJjVFhEbG1IQmplZ3pOVFNXbzVtY01oT0ZCdm53QVAwV19kV2dVbi1HVVQyYWxReTNmQ2xIUEZwdFoxcVBvSWJBbjRPaERhbjVTNnFmY0ZUM3Q4U0RYZTVEQlhZbW44ZVhKVFNZQTNWT0t6SjVENlY4alYtUDZCWnYyQ0dqQzQ?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxNNmdKUExrYVZYSTNzX2dFY3kxQjd3UzlFSEg3aHIzeEtpeWRmTVlzSm1wckhlcVdlX0h5OGdkM2J4dkR4cHh2RENCZ0daUnEwaFdnRGstdUtDTlVyT0ZYUGI1VmNpREtnSnF6dWxaSGlKOU9aNS1OUWZaRG1BMnhVRlhSYnc3QzlodnRIZ1dhUF9lTW5iUXloaFRvMWFuRnZzSnVpN1QzZXQ5ZjU0akIwQXZYblZLNEtHMjJTdnN5YTVkV3B3OUN2QU9jeGVPcGEwcks2SWZQTQ?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxQbmNCb2tyQ2ZPT0pVTjRLanZOYkVYTmNNQ3dTcll0UmkxeW5DMXRhQTdiQmIwOUNNVEpLM0ZmUXFkaC1PX2hMdGNLQXRXdXc1ZEJ1SEtpWFRyQzlNMVRyQ1BWX2E1RFF1NDdVeC1OR3dVOGpZMnVwbzJQZjR0WlFkYm9wRWh5VnU0NGh5OVhQYU1RZVVEY3g4T1ZHSmFmOGZ2U2Q0VkwwcDZsQWtIOVVHS05qZE9Kc29tTGZQNldzOGhCMG1nUU1xRDktcw?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxNTW1OY2VvcDdEWUNjQjVQemphV3Y4YXRmNV9uRjd5dHdiX0VVVHNXZHFvdEdlMTRaRlZkd3FCTXVWUGVjaE43THdZS2RwQjNjM2FINFpfWWZhZVFkRkpFYlBXZ0tTOEx0QlNIcVZVV05FbFpVcjlfOE1iUEZSaXVZWnc4ZFoyZzdGVktQVUZtQWxfaFZBUjVUVWJBdThZZTJwTlNzVmtheUctY1QzRkdSbTA1V2FZVGZmdTU0bU5XYWd3RjRnZ0E?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxOeGk2UUJEUDdQZURYT1BlaVBaQ01ibkU2Ujk5d0NTNzNPZnU0TjlLWWxFWWpGcEwyWDFNX3UtY1NLT05UQ21CdGEzTTE1Z0F6QU44S3paS1BWSWdMemExMkVyQmlDbGQ4Mnc4a0pRME41QUFTYWQxMjExZUwxS1Ztb2RPM01hQ2lmYks5akF5d29RanNPMTZvOW9wbXlhY0x5RzRieXpkR0xfNFJhWVNyYUVR?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxPNm1MTERFbkduR2VwaFBIdENsVFNDMkgteGVmV2xHSEd6c1djRTZyYzBTRFNQY2dJZmwxN0xIOE1GbEwxRThjMXpyV2NUeFY3Z2dRZEVYZE1aUU9jcGtha0hZYWtzbTloNE5jYTRrQXE1NUUySUxNbmswTk5aUl9VZk1rRWhubDFRNHZnb0MyT0JFeElLVjc4Vi1zRDVwb0MzT1NJQ1BmaGJSQlJGU1pBZDhzTlZGb0E5OTBvT2t5dnBfQTQ?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxQVG5fQXRDMUJGenBZSVVPOWk0SUp0Q281M0p6OGhYZWJPUFlCSnZHNWprYkRzT3ppQTIwVWpON3NWZUhmSDg4Vk1nYWZsTk5SZFU3VzdEZ3VnWnNkdXA5eHM0dGR0Z1pPTjY0dG1wY3dvTVRjNHdiMGxGbHlyRzBnWXA0Z1lqUVNkWHhocGNLRXRqSUdvLVZEeXV5LW1zcGpZR1lTUGpXYXB6aWZIeDFPVER6d3g0MEdGZHUzcg?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNV05jeWZSZzZFU0JtbzRaZW5acXl3eHVqVUtRX0ZUamE4V1JyQ18yY0lmV2EzUEdkMWVoN2k0dkVMSk5JZ1pIeVlSRVVGalc3NDE1azMxSkR6LUZkMl9CM091NE54ZHZWbVY0VkJodm1mNGRORWNGa1NhbWhrZVpldzFqQzVOQW8zZlVv?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPTGtSaFE3OVRZdGp1MzdnWm1OWEZDYlpzZUMxUGlPaHVsRVVWZ2gyWENCTFk4dHJKMk9WdEgxdHRjeHFCVXNPbjNTOGExTlZJMDlDSXhZZmctUFpxSW1pZW9ISnFkUkUwcElKT1JfRDg2Z3UxVzR6WGw4bjJraVJ2SlhnYjZDcnJvdGpvNGY0RnhzZ1RYNFZxVDNR?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxQSXpIQjhxZmZobUVKdHU2N1VDQWlaYmxyOWFTczRPdXpheERpTjlrQXRERlkyWHlzME1kVHFIQUJodWE4NXFwdHdBTklkTzJubDNPUUFwWE4tLVNmYXBIVUxCWFdSZHdqZ2RPNkRiLVZvYWpZWFFNODVJNzMtLVp5eU1ZR3hENVdkM2hob3JHYzlVeU1NRU4tSWlqSzdydTRMaGxSWDhUdlpKSWIycHhOdGtJeE9QaV90NF82RnlGYXJYYVFmNktXaXYyQ1lrcmVRUHc?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxNQV84T3ktclhDV180c1dZZXFWUGhRbmgxZXBudUVZeFpuNWR0TDZybXlub2lXODY3SDBwbWZiZ0Y2X2drRkVFRU02cWxIVWRNeXJ2all0dlV5MVgtcm5HQXg0MkRqczVSNnczUXBmd1VIVnpRMmt0N1RLai1kNUMxR2dYTS0wMk1lWF9lN09xNGw0N0RxczdPSmZEcVFXR093RTRZQlZyOVVxMDRFeVNVRi1ZNHBCRFNVMnRpaEVlRElMOVZyUk93QTBR?oc=5
- https://news.google.com/rss/articles/CBMi3wFBVV95cUxQZElNczBUU3NSRV9MZEJqMkJ3a3ZNcVBpazhVVHItVkhuWkVOZ2NxZnJ2LUZvR0hocEJrR2txektOQ1BPdzlFMWpndnNSRkFCQmdMWDZkN29oeXZNWE5GVThiYTU0ZFN1U2xGMXRmT2J1VlhXZ2R2LTAwLUZEdjhQNUV5bkVGYVZsM1cyc1N6WE1kX2tKVTJLQW1STTBZSlJOc3drbFVWT1dqSTZrUmxHZ0pPMUxfZGEyZTFYSEFnMTJWQWF1ZlMtUWNpSEk0RTNpSE1qRnZWanBuN04zcW9V?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxOR1o3WjZHSmU2MmNuRDFOUDhFX0hIaTNDRHdXSTRVVDJaZHZwUzRONXd6eXh2VW9scjFmNm5QRDB1b2RLSUhBc2JDUmE0MkFnbDY5T1RHaFVyMTlKajRRR2FPU0tzUkhLaG1NT0FJNjEzR3VxZmoxeDZxV0ctVmhlQ0hVTm9oVlc5NFdfbVNua2VBQjFuVGgtNUhQY0h6bjg5OGRWYmRHTW0yQWptbV9XQmFRUHY?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxNdGtSUFBTMm5RYjh4RFN2T2pmREU0ZWRXcGFsZDh2VWRYc3kybFkzcTlBX1ZZYXpUMGNvNktXNy1yZzNBOElyMkt5dUpqUFFMN2ZDMkQ3ZTBFV0RVanUzbWI2S0NRMUZheEV5WWtYbFhMSkUtelM4SFJNYl9rTS1vUGYxWkdfak1TZWlUNFFRTzZlY1dLWVFEQS1vOXFHdmV2bGZkSFFNNjhLVEtRQi1R?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxNSDVXTzlEcV9hWHNHR2tiU0lmclNlcWlMei1OOFZvenlRV3c5NzJOUTZFRG53SjBLVHlhT0JjREo4NmJtbmFTWEU5X2tVMnRLNjZuYm9ycExmREdpZDM0Z3E5dlJEMkZJdC1CMGQyN0hMZGNrS1dkVnVRdW5mVnlyX3FycTlnc0FlWS1QeDR0TTVJMGpWMWxfTVRESFNQVW9LZmdvcXBBY2NZQkxlVHI3MVJVcjJDWDdmV2RCQmtlelVqbHN3dzdBUHg5SHpRWGJjLWhMZGxZWlRPUQ?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxNRkVmNHFuMzZObmVHRkpVOEZZNFJmT3ZKQ0NGYjBtdTBQVFIwbko0Mk53UnFfNU05dTRPdE9MWXRKZWhjbVJ2dXJOdzJFaXBHWkNuZWxvNGRha0lKQ0o5OG82WXVpN0o2azdRV2dCQ3R1WE80QjB0dDUteTZjTG5NRU9YQWE1MFI5clJQaWIyUTNsXzBvVVpaM29FdjJZSlZ5QTlqSDdJc05zMmU2LVJzazVtMWlXcENGU0dGTzBCSEtxQXljNTdj0gHMAUFVX3lxTE1oM0RXNVdySG1lbmpDZ2gyYWpSNmFGRGdjR21kd3NHOURpZXFSTUdjMDVMaDJFc0c2emtWXzRfTnE2ckdoYjFjMjVMMWdQTTFmRUFQQy0zOFZwallqX1lhelQ0MHNmaGR0Mk5BTXRDM1lfSFNvX216UXlwVk1YaTktampMQXRseDdYdXhFcTEybzdFZmNNQzJEdmVOTVNQM0tMZllMZ05nVDBEUkhNUEpGS3JtSkp1bllURDE1SnZfOXZ5THRRbGRIdlNQZg?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxORl9NbF9KQVNuaGlrRFR1UG1KUFZTYlg2SnFPbWl5aHhMZDZFQnBueURSY3ZobFJxZlVVS0ZEb1lLNkFpY2xvWjk4bVoyNzZzcnFhd0tZMHplTDRWYXRUNXgxSURxdTJuWVFoemU5S2w0QzFQeEhndW9VT1ZiLV9pT3lQMDcyc25xYnZSaE85QzN5V0VBRUlNYVllSFJ6WXBTajFwZFlsZEY0Rmc0UkVsbVJvRm0zYmFzMV9jdEVBS2JkU2tRRGJGdTZIajM?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
