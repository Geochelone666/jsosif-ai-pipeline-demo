# AAPL Intelligence Report

- ticker: **AAPL**
- Report as_of: **2026-11-27**
- Market data as_of: **2026-11-27**
- Quant sources: https://finance.yahoo.com/quote/AAPL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AAPL/key-statistics/
- AI analysis snapshot as_of: **2026-11-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-28T06:11:36.656826+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 6, 'ai': 14, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261127T063646Z-c0c26981/AAPL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 13 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 24.0%; oldest publication 2026-11-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 358.5400 |
| Return 1D (%) | 0.8324 |
| Return 1W (%) | 4.6649 |
| Return 1M (%) | 3.3744 |
| Return YTD (%) | 32.3435 |
| Return 1Y (%) | 29.6304 |
| Annualized volatility (%) | 25.0070 |
| Beta vs SPY | 0.5709 |
| Max drawdown (%) | -13.7985 |
| Sharpe (rf=0) | 1.1527 |
| Downside deviation (rf=0, %) | 17.0174 |
| Sortino (rf=0) | 1.6939 |
| Historical VaR 95% (1D, %) | 2.0102 |
| Historical ES 95% (1D, %) | 3.4742 |
| Correlation vs SPY | 0.3430 |
| Tracking error vs SPY (%) | 24.3584 |
| P/E (trailing) | 39.93 |
| P/B | 46.49 |
| EV/EBITDA | 30.60 |
| Revenue growth (%) | 11.70 |
| Forward P/E (estimate) | 33.91 |
| Gross margin (%) | 48.79 |
| Operating margin (%) | 33.01 |
| Return on equity (%) | 142.26 |
| Free cash flow yield (%) | 2.03 |
| MA50 | 343.2741 |
| Close vs MA50 (%) | 4.4471 |
| MA200 | 304.3778 |
| Close vs MA200 (%) | 17.7944 |
| RSI (14, Wilder) | 60.3470 |
| MACD (12,26) | 3.4352 |
| MACD signal (9) | 3.2125 |
| MACD histogram | 0.2226 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AAPL': 291, 'SPY': 291}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 358.5400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.8324 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 4.6649 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 3.3744 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 32.3435 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 29.6304 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 25.0070 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 17.0174 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.6939 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0102 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.4742 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3430 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.3584 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5709 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -13.7985 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1527 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 33.9118 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 48.7860 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 33.0100 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 142.2570 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.0278 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 39.9265 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 60.3470 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.2226 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 4.4471 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 17.7944 -> Clearly above the moving-average trend level.

## TAILWINDS

### Apple Enters the AI Agent Race as It Takes on OpenAI, Anthropic, and Meta. What That Means for AAPL Stock.
- Summary: Apple launches AI agent initiative, competing with OpenAI, Anthropic, Meta.
- Date: 2026-11-26 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3wFBVV95cUxQYXdfa3Bna1FYMHFuMy1haFR5VzUwdDBta2xLbzU3UnhnTlZVQ1JETWFKT0ZORGNDeVQyNEF5dHQ0X3loYXNlVktodi1xMHR6eTdUdGVxSnhMS1NJN0lXZnBuQTdWRGVoN3ctYkk0Y0hXSkpfLUhEQXY4N0dxcUpyQkRsYkU4NWhMVDNmMjQ0a0xXdmdCWktWaVhBYlZUd2hSNzBoOWtCTWloa1RscW9KcEdBZms1YUxlRktHM0VveVhYS0VnMDVKaGx2TzA5QkJYeTlUSENUOTV3bjZNTG5F?oc=5>

### Apple Takes Bigger Bite Of US Smartphone Market - Apple (NASDAQ:AAPL)
- Summary: Apple expands smartphone market share in the U.S., boosting sales prospects.
- Date: 2026-11-27 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxPRlNHMDNhLXJpX0xrbkFTMmNJd1B3bGVJS3BVTXR5UXRrRVlmNHZoWG11eXR5Q01OWEJrN3Z5ckowek5QY0JHcnZPTnNKd0lFQUhNeXgyUC1RSTMyY0R1eFNtb3RDaHNqUVc1d1ltSDl4cHMtRGRhZ3BaOVd2dlJLcVluNDRKZTZRQVlmS001dFJiN1R0LUNMaHYzT1BQNVBEVkZqa2lkaDhFWVRydEIyeU5JNjBtNUhSZ29HM3BNVTZNVXlvVnd3SHFTMTdZZVo0S1JnR2tNRnNOZw?oc=5>

### Apple (AAPL) Stock Hits New 52-Week High
- Summary: Apple shares reach a new 52-week peak, reflecting strong investor confidence.
- Date: 2026-11-27 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxQYkRFSGxoVklobldqLWxRaWVxR01EcmRDcF8ydldmTlVxZ0M0b2dSOVRGREYwUEV3ZldFdlNOWFA3eUZSWXJfTUNFR29qNVZGZThzX0dLZTJJNUhCY05XOV8wVnpwZVJUbnEyQzRlSVd1RkRnN05HTFpKa1JrdXNhQm8zUVZoc3B0TnVVbDFn?oc=5>

### Tech Stock Sell-Off: Here's Why Apple Has Been Immune
- Summary: Apple remains resilient amid broader tech sell-off, supporting its valuation.
- Date: 2026-11-25 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNZmx0QkdUUWF5dUxZbnBYa1RYYjBXTXdDR0FQOHJwWUszbm50Mk5NTWg1VHJlUVo0YlZ4WEpsRmlQOTZqOGZnelA4NXhBbDRTWUFYN1hLT0FnSmUyWUJFRG1TbXc0dTlBU0U2RnVxV2tDNjdiSUZyUXI2U1NVdVl3Q0tmWFJMWldvNlE1cEdiWVpIcDhldnBHZWFpTQ?oc=5>

### Apple Now Ships 57% of U.S. Smartphones as Memory Costs Crush Cheap Android Phones
- Summary: Apple captures majority of U.S. smartphone market, boosting sales and brand dominance.
- Date: 2026-11-27 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxPb3BWVS1fck1oUmtVSWNwWF9xZjlXRkpPV2VnRDJjMm1UUjB5M2E2SWlBN0ZpS3lUQlNtQmNLdnl3ZU1iQ1RySkJRdG9EUXM5dllYd1RQcS1nRDJCbEt1UTUzUUZZd2hZSEoyZ3lyQUdSMVl1ek9jelRMWWRlNHZrUFJKRkVLRk9aS214SUdnam16a2JDYWdrUkROTTRHeW1Qc0ZkNW5uSnpHTzYxMlZqUlJ1cVdERVc3QWd1WFM5Sy04Zw?oc=5>

### How Apple Avoided the Stock Market Crash With 31% Gains
- Summary: Apple's strong performance shields it from market downturns, enhancing investor confidence.
- Date: 2026-11-27 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMib0FVX3lxTE56MDRwbDVnRVZwbGEybFlQZjZLOEdCNGdRMTBhMlhkY0pNLWJaUnFIWEZlQl8yTmw1aU1GS1BZamY2WTM3YUZyX0RDSVNXVXZpcGtDOFVHNS1BVjlIOGIxb2ZMVUxSQk1ETDFzQU01cw?oc=5>

## HEADWINDS

### Apple Stock Defies AI Selloff: Is It the Market's Safe Haven?
- Summary: Apple Stock Defies AI Selloff: Is It the Market's Safe Haven?
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiaEFVX3lxTE82a01DUHNCbGVoR3dxYWlCa2c3ZXNUdVFkVmV2MkFYWV9kVExUeDhFRWthMUJhOG1qOElLZjAzV3I2SFlwbk5LbFF1ZHpxV2gzSjZyVFo5N3hVc21YSzV1d0F0enFpd0c2?oc=5>

### Apple Stock Has Run Too Far
- Summary: Apple shares appear overvalued, raising concerns about a potential correction.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxPLWg2c0dlU29XLWRXa0tDNUd4MzFGNE55ZXp3cUptSk5mbTBlel9LZDFhcnNwSkpXX1NwWXVJRnFaSWN2Q011cDVjSnkySDlrUG5xc2hKaFlrOXhJSFdLTVZzOGdNZ2dVTXJYT2V1dDFQR2R0TFltSW5tRnhyX2pEVDZHdGkxek5vLUZCOGtHX2hzdw?oc=5>

### Apple: The Mispricing Of The Market's AI Hedge (NASDAQ:AAPL)
- Summary: Market mispricing of Apple’s AI initiatives may dampen future growth expectations.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxPaFA3a0FPQUUybWRiS2ZBdE9iU3ptTUxoZzB5YnpiajVyaDktbVVMLTM1MXNzRDlGbnhkWld1T2RKQ0FzczcwaVQ5NzY0eW9FVm5hS3VucUNhR2E4Um1pX1J4dmNXXzNOTk5MTVNMZ3pQNjVzOU04Y25MVmFGSW4tcFlqLVRjUVVSZTdaa2Jn?oc=5>

## CATALYSTS

### Apple Stock Has 3 Things Going for It in 2027. Here’s My Price Target
- Summary: Apple Stock Has 3 Things Going for It in 2027. Here’s My Price Target
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPSUhjckIzQThzNXJUVXhqNzRLVUp1eEhsY1p2VDVNTGhOblRmOFJxXzRKV09wZkFhbmF1U3JIaEsxclB4Y0Fwc0RiajhCMGJDanpSbEVZdGg1SlhaNy1VNGxaTWJKU1RnUmdPSFMxdkxSYkFXb2F3azV3TGdlVVhDT1pmQldxVklzTXJiR3E2bVppNkQzeVE?oc=5>

### Apple (AAPL) Has Found a New AI Opportunity That Has Little to Do With the iPhone
- Summary: Apple (AAPL) Has Found a New AI Opportunity That Has Little to Do With the iPhone
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOSWhUc0xMVndoX0IxZEo1QWk3MzRxQzhpYkx4Q3ZaVDF6SEpWNkFZNEVnZ2ZUN1ItR3hXa3pUVjFWeDhjSVVMSWxuOHBYdkJ2Y2hjaC0tbktheDh5WTdzQmlTcmh0YndKN19JdW1xcWhLNnVTY1dmNVpReTMyV3dobXo0cTVqSDZTNUpIUExTanQwNFVQV1B4YXJxVQ?oc=5>

### Apple Inc. (AAPL) Delivered Strong Results: Why Investors Are Watching Its Next Move Closely
- Summary: Apple Inc. (AAPL) Delivered Strong Results: Why Investors Are Watching Its Next Move Closely
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPLTlCTmhMLXRPNjhlZnU1Q2Z0V3VwR3FTR0haUlBObWNOWjdWM3luWnhwWWNfNnhxVXlrT1kwMlVpdEYySEFMMkxTbi1sR0Nza19XS2tQUjFkWHQ4V3dzT1VIQTFyVzRPU2RZd2Q1N2hENkxuN09TU3llRWRjMVZCZGNlbzFOXzBJbDZ0QXlQbHZfLUoybUl3N2VDQlU?oc=5>

### Apple Inc. $AAPL Stock Sold by Legacy CG LLC
- Summary: Apple Inc. $AAPL Stock Sold by Legacy CG LLC
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPTGltVXo3Qk5HMkNkTmlxWlNKbXQ4Z3V6dXBRajdvYnRZSXJTQmdVZ1pPZVhvdVQ2emVkNUJvRS1CWG52UVBuNG14WVJXZ2NIcjg3SzJ4TWIwOW9reUhpNHRValZYMU9DZ1g2cWtrTFVaMkpLa29LejlucGhVN1V4VERtQ1pJSjRwcktuaW5hZDJCNjNtSkZfbXBBcHBrc3R2cE9LNnhR?oc=5>

### Apple Inc. $AAPL Stock Sold by Integrity Alliance LLC.
- Summary: Apple Inc. $AAPL Stock Sold by Integrity Alliance LLC.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxPUmxOdlhJdVlUNEt5aFFOMUdtakRhUmlRbGJteWdnMUpXZ1hGQ1RRejdYTVUtZ1JKSk0yOV9YTGNEcllKcG5hU3NxeGsyNl9fMl8xTHZtQnowcEVucVJPWk13bmtjSTd1cUxlOGNrLUlXWjd0R2MxRGVyTEhXeXgzdkFCVnhNdU5EaFdhUmhTVmItYTdqZUdSb0Rpa1pydk1fSndiWVRfOUc4czgyUV9KQTh3?oc=5>

### Is Apple (AAPL) Above Fair Value As ETF Buying Returns?
- Summary: Questioning whether Apple’s valuation exceeds fair value amid ETF buying activity.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOVkFWM051XzB5b0RCeFhPQm5iUTNIWlZvNFZ2VzUwSnlVQXVzTDBSZkVPUU1ZeDRheTdIa3lBWmwzV0JqWFBpcjFJQjhpSHkwY1V1SEZXQmVaYmJHdmIxcUNnMmxzRDZYWlExQ05JN0ZpSU0xeEItMjFwY0xnMUgzejg2VnRpRkZab0dFUWp5T2hFZk5IMmVj?oc=5>

### AAPL Stock Alert: What to Know as Apple Develops AI Agent to Compete With Muse
- Summary: Apple’s new AI agent launch could boost product portfolio and market share.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQekFPM3ZncUc5OWU5R3NERDJHalhFbE9WNURJNUNmc3RnelpCTW9OcHNHcXZuTDMxVGtMbWkwUnM3WDBCSHVYalU4dnhzWFY4NW10dGJROGVEOE5KNXNIUjJUY1ltN1A3SHJTZE9XS0ZUQTNUT0c5S1BVUzJGRDlzVlVuZkV4YUNNTHFxZVhmai05QUcwdmc?oc=5>

### Apple Is Now Worth Over $5 Trillion Without Betting Big on AI Data Centers. AAPL Stock Now Trades Near Wall Street’s Targets.
- Summary: Apple’s market cap surpasses $5 trillion; stock trades near analyst targets, indicating bullish sentiment.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi-AFBVV95cUxNRXVwb1laS1Btbm1iTjFsMEg3OGRxd2I4MDBheXBhTmpLTnBpLVpFaGZCdmVabEZnS3FWREh5WDAxcW1KVGpOVFB5NzltWnAyakRibjhhckdQM3BpcVRtSTdHckRoY2RtRFdmZG82T3NlY0xkLS1MczU4b29KQXFXVGdXSjNHMUxBT0NoZmRSb0tuYTdCOEZYWWhGRW8xbUVOTlhkZjJFVGhOUEVaQVptUW05eW1UalZBeG9wRUhLVXljWlVFU0JLc0dkVm1aZjM5OHJEWlVuUmFUd1FJNW1Rdi1UdDN5YlRER0JMZnVpaGNvSVUyRUx5ZA?oc=5>

### Apple: $136 Billion Of Free Cash Flow Without The AI CapEx Bill (NASDAQ:AAPL)
- Summary: Apple reports $136B free cash flow, excluding AI capital expenditures, indicating strong liquidity and potential for future investments.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPTGhlNjVzYXh4MXk0NlRMNnpKMGhmMDJKYXJ3a1FRbzhFZ08zZzJvN3ZhZGVTN05wWnpILV9lX0M2ZFAyWTFEb3ZpTFJVTVJ4OHRjZklzcS1Xd29nUHlxQVFXUVcwUHRQR2wwRW5oTk1OM2JOTUhLenJ1NjJ6VDkybEhEZi1FSlBkd3pJaDAyZUp0bkFFTDVmbVJ2ejNnaEN1Skw3bQ?oc=5>

### An Apple (AAPL) officer’s trust plans another share sale after grossing $19.2M on Nov. 25.
- Summary: Officer trust to sell shares may dilute holdings and affect share price.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxOMzN5QV9wOGttd1BWV1N1WUVHbzVDZWwtdWFsMjZkc2RCUTVSQmxmVDRHZmRmNjM2TzFPRGtlMDlfeDdVYWtpODRXY3B5U0kwVk5zLXNwMmJJaVBocG9lNEFTMWhudWh4TTJyUkJWcUdqakdManItWl82c3JGeHZYRmFvMlg3RFZ1MTMybTRCNA?oc=5>

### Analysts Offer Insights on Technology Companies: Xiaomi (OtherXIACF) and Apple (AAPL)
- Summary: Analyst coverage may influence market perception and trading activity.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMi-wFBVV95cUxOWkVLQy1DS1FJZlR6clJpTHNjTXVkM1hMRnZmWnBDam5Haks0QzFERDhlUExjODRBYmk0M1R1TGI5QTQyYjBVTjRvVjZqZmJ1eW1DS2JzazVual9RSDNLQnBTWVozZWZEZUcxM3V0WlRockxYam5DeWpWOGFLazVUb0lVNktJY0pVNmtmemQ2Y2xMa3o0ZkM4N2NYdU96UWRzb3hGSmZ4SUhNTE90dG9aeXc2NWlFVkRzMWQ0WUdoUmhreHZ3a3JXVUhvd3kzaXdxbGxlZkJ2U1UyS0JNb2swTjRMUWdqaS0tREt4dVM1NXhIOWYwSnFySmRIMA?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AAPL** | **39.93** | **46.49** | **30.60** | **11.70** | **5,210,368,901,120.00 USD** | **29.63** |
| MSFT | 25.72 | 7.78 | 18.13 | 18.80 | 3,660,000,002,048.00 USD | 2.36 |
| GOOGL | 14.36 | 5.13 | 17.70 | 24.70 | 3,380,358,152,192.00 USD | -13.84 |
| SONY | 20.87 | 3.02 | 0.30 | 10.30 | 163,016,245,248.00 USD | -3.82 |

Peers fetched as_of: 2026-11-27; AAPL reuses existing data (market data as_of: 2026-11-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-02
- Next expected earnings: 2027-01-28 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-27

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-11-03
- Revenue (latest available single quarter): 62,900,000,000.00 USD; period 2018-07-01/2018-09-29; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 29,789,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/320193/000032019326000026/aapl-20260926.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi3wFBVV95cUxQYXdfa3Bna1FYMHFuMy1haFR5VzUwdDBta2xLbzU3UnhnTlZVQ1JETWFKT0ZORGNDeVQyNEF5dHQ0X3loYXNlVktodi1xMHR6eTdUdGVxSnhMS1NJN0lXZnBuQTdWRGVoN3ctYkk0Y0hXSkpfLUhEQXY4N0dxcUpyQkRsYkU4NWhMVDNmMjQ0a0xXdmdCWktWaVhBYlZUd2hSNzBoOWtCTWloa1RscW9KcEdBZms1YUxlRktHM0VveVhYS0VnMDVKaGx2TzA5QkJYeTlUSENUOTV3bjZNTG5F?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxPRlNHMDNhLXJpX0xrbkFTMmNJd1B3bGVJS3BVTXR5UXRrRVlmNHZoWG11eXR5Q01OWEJrN3Z5ckowek5QY0JHcnZPTnNKd0lFQUhNeXgyUC1RSTMyY0R1eFNtb3RDaHNqUVc1d1ltSDl4cHMtRGRhZ3BaOVd2dlJLcVluNDRKZTZRQVlmS001dFJiN1R0LUNMaHYzT1BQNVBEVkZqa2lkaDhFWVRydEIyeU5JNjBtNUhSZ29HM3BNVTZNVXlvVnd3SHFTMTdZZVo0S1JnR2tNRnNOZw?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxQYkRFSGxoVklobldqLWxRaWVxR01EcmRDcF8ydldmTlVxZ0M0b2dSOVRGREYwUEV3ZldFdlNOWFA3eUZSWXJfTUNFR29qNVZGZThzX0dLZTJJNUhCY05XOV8wVnpwZVJUbnEyQzRlSVd1RkRnN05HTFpKa1JrdXNhQm8zUVZoc3B0TnVVbDFn?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNZmx0QkdUUWF5dUxZbnBYa1RYYjBXTXdDR0FQOHJwWUszbm50Mk5NTWg1VHJlUVo0YlZ4WEpsRmlQOTZqOGZnelA4NXhBbDRTWUFYN1hLT0FnSmUyWUJFRG1TbXc0dTlBU0U2RnVxV2tDNjdiSUZyUXI2U1NVdVl3Q0tmWFJMWldvNlE1cEdiWVpIcDhldnBHZWFpTQ?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxPb3BWVS1fck1oUmtVSWNwWF9xZjlXRkpPV2VnRDJjMm1UUjB5M2E2SWlBN0ZpS3lUQlNtQmNLdnl3ZU1iQ1RySkJRdG9EUXM5dllYd1RQcS1nRDJCbEt1UTUzUUZZd2hZSEoyZ3lyQUdSMVl1ek9jelRMWWRlNHZrUFJKRkVLRk9aS214SUdnam16a2JDYWdrUkROTTRHeW1Qc0ZkNW5uSnpHTzYxMlZqUlJ1cVdERVc3QWd1WFM5Sy04Zw?oc=5
- https://news.google.com/rss/articles/CBMib0FVX3lxTE56MDRwbDVnRVZwbGEybFlQZjZLOEdCNGdRMTBhMlhkY0pNLWJaUnFIWEZlQl8yTmw1aU1GS1BZamY2WTM3YUZyX0RDSVNXVXZpcGtDOFVHNS1BVjlIOGIxb2ZMVUxSQk1ETDFzQU01cw?oc=5
- https://news.google.com/rss/articles/CBMiaEFVX3lxTE82a01DUHNCbGVoR3dxYWlCa2c3ZXNUdVFkVmV2MkFYWV9kVExUeDhFRWthMUJhOG1qOElLZjAzV3I2SFlwbk5LbFF1ZHpxV2gzSjZyVFo5N3hVc21YSzV1d0F0enFpd0c2?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxPLWg2c0dlU29XLWRXa0tDNUd4MzFGNE55ZXp3cUptSk5mbTBlel9LZDFhcnNwSkpXX1NwWXVJRnFaSWN2Q011cDVjSnkySDlrUG5xc2hKaFlrOXhJSFdLTVZzOGdNZ2dVTXJYT2V1dDFQR2R0TFltSW5tRnhyX2pEVDZHdGkxek5vLUZCOGtHX2hzdw?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxPaFA3a0FPQUUybWRiS2ZBdE9iU3ptTUxoZzB5YnpiajVyaDktbVVMLTM1MXNzRDlGbnhkWld1T2RKQ0FzczcwaVQ5NzY0eW9FVm5hS3VucUNhR2E4Um1pX1J4dmNXXzNOTk5MTVNMZ3pQNjVzOU04Y25MVmFGSW4tcFlqLVRjUVVSZTdaa2Jn?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPSUhjckIzQThzNXJUVXhqNzRLVUp1eEhsY1p2VDVNTGhOblRmOFJxXzRKV09wZkFhbmF1U3JIaEsxclB4Y0Fwc0RiajhCMGJDanpSbEVZdGg1SlhaNy1VNGxaTWJKU1RnUmdPSFMxdkxSYkFXb2F3azV3TGdlVVhDT1pmQldxVklzTXJiR3E2bVppNkQzeVE?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOSWhUc0xMVndoX0IxZEo1QWk3MzRxQzhpYkx4Q3ZaVDF6SEpWNkFZNEVnZ2ZUN1ItR3hXa3pUVjFWeDhjSVVMSWxuOHBYdkJ2Y2hjaC0tbktheDh5WTdzQmlTcmh0YndKN19JdW1xcWhLNnVTY1dmNVpReTMyV3dobXo0cTVqSDZTNUpIUExTanQwNFVQV1B4YXJxVQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPLTlCTmhMLXRPNjhlZnU1Q2Z0V3VwR3FTR0haUlBObWNOWjdWM3luWnhwWWNfNnhxVXlrT1kwMlVpdEYySEFMMkxTbi1sR0Nza19XS2tQUjFkWHQ4V3dzT1VIQTFyVzRPU2RZd2Q1N2hENkxuN09TU3llRWRjMVZCZGNlbzFOXzBJbDZ0QXlQbHZfLUoybUl3N2VDQlU?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPTGltVXo3Qk5HMkNkTmlxWlNKbXQ4Z3V6dXBRajdvYnRZSXJTQmdVZ1pPZVhvdVQ2emVkNUJvRS1CWG52UVBuNG14WVJXZ2NIcjg3SzJ4TWIwOW9reUhpNHRValZYMU9DZ1g2cWtrTFVaMkpLa29LejlucGhVN1V4VERtQ1pJSjRwcktuaW5hZDJCNjNtSkZfbXBBcHBrc3R2cE9LNnhR?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxPUmxOdlhJdVlUNEt5aFFOMUdtakRhUmlRbGJteWdnMUpXZ1hGQ1RRejdYTVUtZ1JKSk0yOV9YTGNEcllKcG5hU3NxeGsyNl9fMl8xTHZtQnowcEVucVJPWk13bmtjSTd1cUxlOGNrLUlXWjd0R2MxRGVyTEhXeXgzdkFCVnhNdU5EaFdhUmhTVmItYTdqZUdSb0Rpa1pydk1fSndiWVRfOUc4czgyUV9KQTh3?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOVkFWM051XzB5b0RCeFhPQm5iUTNIWlZvNFZ2VzUwSnlVQXVzTDBSZkVPUU1ZeDRheTdIa3lBWmwzV0JqWFBpcjFJQjhpSHkwY1V1SEZXQmVaYmJHdmIxcUNnMmxzRDZYWlExQ05JN0ZpSU0xeEItMjFwY0xnMUgzejg2VnRpRkZab0dFUWp5T2hFZk5IMmVj?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQekFPM3ZncUc5OWU5R3NERDJHalhFbE9WNURJNUNmc3RnelpCTW9OcHNHcXZuTDMxVGtMbWkwUnM3WDBCSHVYalU4dnhzWFY4NW10dGJROGVEOE5KNXNIUjJUY1ltN1A3SHJTZE9XS0ZUQTNUT0c5S1BVUzJGRDlzVlVuZkV4YUNNTHFxZVhmai05QUcwdmc?oc=5
- https://news.google.com/rss/articles/CBMi-AFBVV95cUxNRXVwb1laS1Btbm1iTjFsMEg3OGRxd2I4MDBheXBhTmpLTnBpLVpFaGZCdmVabEZnS3FWREh5WDAxcW1KVGpOVFB5NzltWnAyakRibjhhckdQM3BpcVRtSTdHckRoY2RtRFdmZG82T3NlY0xkLS1MczU4b29KQXFXVGdXSjNHMUxBT0NoZmRSb0tuYTdCOEZYWWhGRW8xbUVOTlhkZjJFVGhOUEVaQVptUW05eW1UalZBeG9wRUhLVXljWlVFU0JLc0dkVm1aZjM5OHJEWlVuUmFUd1FJNW1Rdi1UdDN5YlRER0JMZnVpaGNvSVUyRUx5ZA?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPTGhlNjVzYXh4MXk0NlRMNnpKMGhmMDJKYXJ3a1FRbzhFZ08zZzJvN3ZhZGVTN05wWnpILV9lX0M2ZFAyWTFEb3ZpTFJVTVJ4OHRjZklzcS1Xd29nUHlxQVFXUVcwUHRQR2wwRW5oTk1OM2JOTUhLenJ1NjJ6VDkybEhEZi1FSlBkd3pJaDAyZUp0bkFFTDVmbVJ2ejNnaEN1Skw3bQ?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxOMzN5QV9wOGttd1BWV1N1WUVHbzVDZWwtdWFsMjZkc2RCUTVSQmxmVDRHZmRmNjM2TzFPRGtlMDlfeDdVYWtpODRXY3B5U0kwVk5zLXNwMmJJaVBocG9lNEFTMWhudWh4TTJyUkJWcUdqakdManItWl82c3JGeHZYRmFvMlg3RFZ1MTMybTRCNA?oc=5
- https://news.google.com/rss/articles/CBMi-wFBVV95cUxOWkVLQy1DS1FJZlR6clJpTHNjTXVkM1hMRnZmWnBDam5Haks0QzFERDhlUExjODRBYmk0M1R1TGI5QTQyYjBVTjRvVjZqZmJ1eW1DS2JzazVual9RSDNLQnBTWVozZWZEZUcxM3V0WlRockxYam5DeWpWOGFLazVUb0lVNktJY0pVNmtmemQ2Y2xMa3o0ZkM4N2NYdU96UWRzb3hGSmZ4SUhNTE90dG9aeXc2NWlFVkRzMWQ0WUdoUmhreHZ3a3JXVUhvd3kzaXdxbGxlZkJ2U1UyS0JNb2swTjRMUWdqaS0tREt4dVM1NXhIOWYwSnFySmRIMA?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
