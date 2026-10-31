# AAPL Intelligence Report

- ticker: **AAPL**
- Report as_of: **2026-10-30**
- Market data as_of: **2026-10-30**
- Quant sources: https://finance.yahoo.com/quote/AAPL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AAPL/key-statistics/
- AI analysis snapshot as_of: **2026-10-30**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-31T02:07:20.117815+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 6, 'ai': 14, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **10** exact headline/source/date matches; prior report **20261030T021807Z-b9de7146/AAPL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **4**; {'low_uncalibrated_model_confidence': 4}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 7 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 54.17%; oldest publication 2026-10-26

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 344.6300 |
| Return 1D (%) | -1.2267 |
| Return 1W (%) | -0.8915 |
| Return 1M (%) | 3.4863 |
| Return YTD (%) | 27.1125 |
| Return 1Y (%) | 27.4514 |
| Annualized volatility (%) | 24.0776 |
| Beta vs SPY | 0.5648 |
| Max drawdown (%) | -13.7985 |
| Sharpe (rf=0) | 1.1324 |
| Downside deviation (rf=0, %) | 16.6766 |
| Sortino (rf=0) | 1.6350 |
| Historical VaR 95% (1D, %) | 2.0034 |
| Historical ES 95% (1D, %) | 3.4742 |
| Correlation vs SPY | 0.3000 |
| Tracking error vs SPY (%) | 23.6335 |
| P/E (trailing) | 39.52 |
| P/B | 46.82 |
| EV/EBITDA | 30.08 |
| Revenue growth (%) | 16.40 |
| Forward P/E (estimate) | 36.07 |
| Gross margin (%) | 48.65 |
| Operating margin (%) | 32.62 |
| Return on equity (%) | 148.75 |
| Free cash flow yield (%) | 2.14 |
| MA50 | 333.0408 |
| Close vs MA50 (%) | 3.4798 |
| MA200 | 296.2692 |
| Close vs MA200 (%) | 16.3233 |
| RSI (14, Wilder) | 55.3532 |
| MACD (12,26) | 3.7861 |
| MACD signal (9) | 4.0101 |
| MACD histogram | -0.2239 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AAPL': 272, 'SPY': 272}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 344.6300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.2267 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.8915 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 3.4863 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 27.1125 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 27.4514 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 24.0776 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.6766 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.6350 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0034 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.4742 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3000 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.6335 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5648 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -13.7985 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1324 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 36.0687 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 48.6530 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 32.6230 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 148.7510 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.1418 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 39.5218 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 55.3532 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.2239 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 3.4798 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 16.3233 -> Clearly above the moving-average trend level.

## TAILWINDS

### Apple Stock Heads Toward All-Time High: What's Going On?
- Summary: Apple Stock Heads Toward All-Time High: What's Going On?
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxPdVp4UjB2M3RvOWRfR2xTdjkydDFvTTJOdlgxZ3d1NzNfamJ6VjM4SDZpcXhVRm9fV0FDdVlGUEl4SXRsSDNqdi1OeC1lb204c3AxSXQwNlFTMFNWN0FtZVJQZWtrT1YtdlJEWlVaMmVacDRJdGh1NFhpYTladGdseHVmMUJkRHIxaG53MUxPSWVyVVYzOFdVZEZ1eHg5R1NCd0ZTeU5SdEFfMk1XWEdqV0JaZGg?oc=5>

### Apple Inc. (AAPL) is Attracting Investor Attention: Here is What You Should Know
- Summary: Investors are focusing on Apple, indicating potential interest in future growth.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPMThESjliM3d5eVFiN2Y5X2FjWWNUZGRpWklILWJDVkQ2S056OWVjcGRHOS1nQ3ptSDNqMGlxRGNaVncxMU9QMkVRTk9kNUdoMnMyMEZPOFhUWkw0RlRDU3c3dlY2YllrOWJFTVdpSThkVmozWWlsR1NkSGlDNWNhSkFhb2JDYXJUUnFZUWNGQU41Wkt1OURVV0U2bUpGMl9z?oc=5>

### Apple (AAPL) Earnings Expected to Grow: Should You Buy?
- Summary: Analysts forecast rising earnings, suggesting a positive outlook for Apple.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPNkZWUzFDVnV6dnJSNWxJZzQwWm94bFpsa1lGaXpXR3RGQktsN0JzaVMxZUVkTk56Z0M0cG9KTHFFa2w4QVg0dVF3RjRVYjFNams2NTJreTJsTlNQd1hEMkQxMVBMZ2lxVUxzMV9FZHRnd2oyVlc1eFlUMWdtWFdyamk3Zy14ZzBneFRvSE01YmpiSXFjSXNGTTQybEFFeUE?oc=5>

### What Does Apple (AAPL) New OLED iPad Mini Mean For Its AI Push?
- Summary: Apple launches OLED iPad Mini, boosting AI capabilities and product lineup.
- Date: 2026-10-27 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxOWXh1UmFwUVNWd3FhWUNKSG13R1BJbHdheXBRNFdGcVFqYnJqc3hWdXE2N2RwUGdlUU1yTXl4X2VSNWNMQUZBQkphR0dsNnV0b2F0SGI3UWRJSk1CMlNBNERCRXhUbkRaaHR2VkViaHQxajBGS09GZXRCdjBxd3c4YVowd1FpWmctTjA4cmJVQ2Q2QVk?oc=5>

## HEADWINDS

### Apple's Stock Faces A Post-Earnings Selloff (NASDAQ:AAPL)
- Summary: Apple's Stock Faces A Post-Earnings Selloff (NASDAQ:AAPL)
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxPcEkwcDh0NVZlMWg3WlRHQUlGM0ZnV0dpbktGdHBpT3FYamkyZ0NYVm5qSkVxajFwVXdiMFZpT3UzQUwydjVfWXdsN0Y0X3ZxRm1UZmJ4V3dFSGRJOHpCb2E4YzdEMi1BWUxrRm5RTGtqdUpRZkJ1c19COWxhTzQzX0RSbS1CNkRaaTlJ?oc=5>

### Apple (AAPL) Stock Falls Amid Market Uptick: What Investors Need to Know
- Summary: Apple (AAPL) Stock Falls Amid Market Uptick: What Investors Need to Know
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPRm40OVVmVmxpU3Z1alRpUDV2U2wtYmk2enZKQmlkdTNWd0NWbXVvenNremt5RmRodVgtak5JdHdlVUZXQUkxdDRna1dNSDJROEhqWlJvQ0phMTUxcVVJUGxnNFNrSXFvMzBmTGhQWjdfVnAzOGNnYlJGTFFNSk5FTFhpcVQyRy1VdHlPMVB6SDI3QnBUYUFN?oc=5>

## CATALYSTS

### Apple acquires agentic platform Ascension Labs (AAPL:NASDAQ)
- Summary: Apple acquires agentic platform Ascension Labs (AAPL:NASDAQ)
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxPa3EtSHdSTV81YXVmX05MVzRPbDBmTk9UM292ZzdsRnAxNE8wYkpSWEd6Qmg5QzlGRTVHdnM3aHdacjVobHdaNEc4Q29XQnN5UENvdHd1U2Z2THgtQjlMTGVEdEdqZndhSW9meTRXTGhrXzFPb09VT3BPMEFTZjg2VG1qWTBNQXYwYWpvQg?oc=5>

### Apple in focus as BofA questions Wall Street estimates amid staggered iPhone launch (AAPL:NASDAQ)
- Summary: Apple in focus as BofA questions Wall Street estimates amid staggered iPhone launch (AAPL:NASDAQ)
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxOX0RWNUJyNWZkX0VTTVZXYXZ5U3pwMkVieTlZcnpDT0YyRU5BbmJHUzRHVnEzWVdzal9CcE8yN1ZYSFFXZUppMzg3VjA5cHlJbHJCVl80dEZxaUh4X0xVM09KWDVXOWR0ZWt1MTBfVy0wTXhNWm42RVpVZ0l4TUk4bWFlczZadE56NENJWENHLTFpRlROXy1mMU45ZE5tbHlXRW5kT05LZkh2YWhKOWo2eGxFUU8zeGxOYWN0a19R?oc=5>

### Apple Just Became the Most Valuable Company in the World. It Faces a Key iPhone Test.
- Summary: Apple Just Became the Most Valuable Company in the World. It Faces a Key iPhone Test.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOb1drZnhod1VWM3VxQVJVbUpSUkV3T19fVXU1RkZvNFYycXdabW0yMXlVRXExa1BhZk0ySVR4d0J6N1FVS0hTdV81ODk1ZHRsSGpsNV9sWEhyOFJudEhNdktBejB6UjRWaTEyMEpQdUdpRGZidUFyWHRkZjRLeXdwRzYwdEVOUVZ4ckdOakk4U01kSV9sQ1c1alp6U04?oc=5>

### Apple (AAPL) vs. MSFT and GOOGL: Is the Post-Earnings Selloff Creating a Long-Term Buying Opportunity?
- Summary: Analyst questions if recent selloff offers a buying chance for Apple shares.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxOWmtIUVJ6QllHYkFmS3pqMDh6WkR1ZUM0X0QyWll5d0RpMllEeFJrVG1pcl9WdUlyWmtDWkhZbU1HZU1oSF9lVVB2b3R2SHZFNzVPOUFseEhQS1Fqc04xaWlYdE14SUxoYTFyRFYzVjUyUGZ0NE5VMGhBWkZPQzVURV9mcWE1TEU1aFBUakFZU3I1dXc?oc=5>

### Will Apple (AAPL) Beat Estimates Again in Its Next Earnings Report?
- Summary: Upcoming earnings could exceed expectations, supporting investor confidence.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQdU1HbzlwTm93MndfY1VROENtajdjV2c5UHZ6RWFiaWJlZWRFekFhbTBmRTQzR080aUZFMlBBa3NnRE5jYkN0TTJ3RW5POU5OaVFzWDJmRm5BVU00MnBnNTZKX0ZiLW5CNkZ6a2hkZXV3cXkzZFpqZmJ4S0VxMkRqWXNCWEpZWWhfbFJ3ckhsdllUMVdHX1I5NnNTQUg?oc=5>

### Apple (AAPL) Could Be 36% Overvalued As AI Launches Meet iPhone Duo Scrutiny
- Summary: Report suggests Apple may be overvalued amid AI product launch concerns.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOVlREYjhBblZnel80UUYwWHdMeU9UU0ZXeTRaMWhYNk14VUdYZUs0RV9ucHZYc1MwbTM2MG1QQ2NuaENfcFlFWEM2N0RpSTlfYW9aUlBRS2FxUTM4RGtfUVMtSnJULXR6QUk2bGtTN3I2aEVlTlF5ampXT3IwY1lTbEd6LTU2V0FGQ3JaLXJTWjl6OThUd2pIRnIxVQ?oc=5>

### Loop Capital Lowers Apple Stock Price Target on iPhone Shipment Concerns
- Summary: Loop Capital cuts price target due to worries about iPhone shipments.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxOZGptMG9GN3dsVmc1MzZzZHdKQldZMm0wdmVSay01a3FWMURQUEktQ2tGRE9mNGMyb3l2OEVqczhKdTJJRmVFcGYzd1lLQXNaQjJkLWhqZC15SmY0Z1NyT0tNVEFDTE9FeFdqNUZwRFNRTmRKRXRNZTVjSGNaYk9aY19kdXdUamVDZ21RdEl1Q052YVFaNVJDeTVjdDlSeEllTVFLRjhPQUZQVDhIbE85RlBFSVFSUU0?oc=5>

### Retail Investors Cut Holdings in Apple Stock (AAPL) Ahead of Q4 Earnings Next Week
- Summary: Retail investors reduce AAPL holdings before Q4 earnings.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxQb3h4anVfaEFKZDg1QkpHWTZ4NVI4UFpBdkZyQ0JEejhYckIxelJEQ0lfVTBmSEw0MTk4cDg2djFoRHVRbDd3MXVJWV83NnFPQmpBOW5xZHFvVURiSVg3TE02Zm4tVzVUUTNkR0NWaXpCYWEza0lvcG5LblVBc0Rlb1BZRFFhcG5rQ19RNHNkb3REUWZVX0FtRXJoLW5iZXpPbTJGSFo4eEFXVlA1SktJ?oc=5>

### Apple's Q4 Earnings Loom: Buy or Sell AAPL Stock Ahead of Results?
- Summary: Q4 earnings approaching; investors weigh buying or selling AAPL.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOMHN2dUpzWHQ5Zzh6ZGVBSWZsSUk5Wnozek5sbmNZQjhWYTVIQlRJZUdBT2xhU2xDZ2Jsb1dIbkkzNWtacTNRTXl6NVpwVENHdHgycTA2YmJsbXFHZmVpSnQxcTl3eVNXY045NUgwSlE4UnpLYzR4QTJOV0JrUGNGelR0TGpPTTlaQmNrVGY3eU03TXExdEtF?oc=5>

### Nov. 2 Could Be a Big Day for Apple Stock
- Summary: Nov 2 may influence AAPL stock movements.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNVDRxN2F0dVA1OXdhZFZCY21IYkYyRS1SQnYyT2taYXRlMDZ2SXl0NEZxY0h5aHNPenl5ZmlDbTZUZVNzU2ZhRHIwemt2TmpNMXhwcUY2RzBTWktXaU9Ga0NXNDl3cnlRNm55UWdDbjJGWjk0b2VWNnFGNW1GVHdFTlhJLWFtUVpsQmlV?oc=5>

### Apple (AAPL) Sees $728.2 Million in Net ETF Buying on Oct. 28
- Summary: Apple experienced significant net ETF buying of $728.2 million on Oct. 28, indicating institutional confidence and potential upward price pressure.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxQLU8zMTNNbElVNzlnV2NKWFlhRmhsaHpLRktHeGRhRDAwTnVna0tRemgtZWlvaWJ4d244aXp1ZjFpREhHUm8zak9zTEh0a1dKcnY3YXZ2RVZPdVVSWXg1N1VTbG1xeWRZV3BYaklEZkFHOVZUUjRFMWtfZUVROE5qTHNGZXdOSTZNYk45dHZLZw?oc=5>

### What to Expect From Apple’s Q4
- Summary: Apple outlines Q4 expectations, including revenue and earnings forecasts.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxPSFdoSjlEX3l4d3Fha3ExR3hObW1OOXdEWWplN2VIMEVPV0tLd2gxUER4NVpHSE1TdUJyZ0NNNkhieTFYaU8xWl8wYmpCVzllZHloZ0trQ2FUYVItRklBSV81c09lNmF5anR2bzRPNks0RGdRanVuN2tqUnlpMkp2WXpCWXdUczQ?oc=5>

### Key facts: Apple (AAPL) Q4 Estimates; M5 MacBooks; M6 AI Chip
- Summary: Apple releases Q4 estimates and announces upcoming M5 MacBooks and M6 AI Chip.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxPWFlWUUZsU1ZKajFWSnZ5SXpYSmgweDVqdGNDYk5TWnpfNTNEcDA3Y0ZPUGppQkhJN1RGb2xDR1pxUjh6LXZ6blZkY1FtdV8yS1lJc3NrSnhMN1M2UmNjRFk4YlZheW9yT0hpUzJyZWxEWmpLeEpjZ1pUZUVKZEFibEhOU0NKUFF0clI1ZV9Wakl4MEtVS0taQm5jaDdZdVBScnR6cE5pTlFnNnhicDVRcXJieTNPVDVqOVE?oc=5>

## RISKS

### Why Buying Apple Stock Before Q4 Earnings Could Be Risky
- Summary: Investors warned that buying Apple stock before Q4 earnings may expose them to volatility and potential downside, suggesting caution.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOSmRTRXU1S3VTbjVrSVhnMktzbEJDWF9CejhyMktuWXRESEY4b2I4TzlSc0s1V1ZxUWJPVndlNnd5TXR6RlR1Q2xtOFc3aGltSmF4S05LRUVBdWNJWEhzTXIxZkNzUHRSLXFPUWpPMUJrQWc2Szk3YUota2IzWERpYjU0dVVvNk85S3h4RGQwM2RRMDVB?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AAPL** | **39.52** | **46.82** | **30.08** | **16.40** | **5,029,592,301,568.00 USD** | **27.45** |
| MSFT | 27.24 | 8.24 | 18.80 | 18.80 | 3,875,804,807,168.00 USD | 0.08 |
| GOOGL | 14.61 | 5.22 | 18.03 | 24.70 | 3,440,352,690,176.00 USD | -0.32 |
| SONY | 20.91 | 2.81 | 0.12 | 8.20 | 147,748,093,952.00 USD | -8.83 |

Peers fetched as_of: 2026-10-30; AAPL reuses existing data (market data as_of: 2026-10-30); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-07-30
- Next expected earnings: 2026-11-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-30

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-07-31
- Revenue (latest available single quarter): 62,900,000,000.00 USD; period 2018-07-01/2018-09-29; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 29,789,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/320193/000032019326000020/aapl-20260627.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMitAFBVV95cUxPdVp4UjB2M3RvOWRfR2xTdjkydDFvTTJOdlgxZ3d1NzNfamJ6VjM4SDZpcXhVRm9fV0FDdVlGUEl4SXRsSDNqdi1OeC1lb204c3AxSXQwNlFTMFNWN0FtZVJQZWtrT1YtdlJEWlVaMmVacDRJdGh1NFhpYTladGdseHVmMUJkRHIxaG53MUxPSWVyVVYzOFdVZEZ1eHg5R1NCd0ZTeU5SdEFfMk1XWEdqV0JaZGg?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPMThESjliM3d5eVFiN2Y5X2FjWWNUZGRpWklILWJDVkQ2S056OWVjcGRHOS1nQ3ptSDNqMGlxRGNaVncxMU9QMkVRTk9kNUdoMnMyMEZPOFhUWkw0RlRDU3c3dlY2YllrOWJFTVdpSThkVmozWWlsR1NkSGlDNWNhSkFhb2JDYXJUUnFZUWNGQU41Wkt1OURVV0U2bUpGMl9z?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPNkZWUzFDVnV6dnJSNWxJZzQwWm94bFpsa1lGaXpXR3RGQktsN0JzaVMxZUVkTk56Z0M0cG9KTHFFa2w4QVg0dVF3RjRVYjFNams2NTJreTJsTlNQd1hEMkQxMVBMZ2lxVUxzMV9FZHRnd2oyVlc1eFlUMWdtWFdyamk3Zy14ZzBneFRvSE01YmpiSXFjSXNGTTQybEFFeUE?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxOWXh1UmFwUVNWd3FhWUNKSG13R1BJbHdheXBRNFdGcVFqYnJqc3hWdXE2N2RwUGdlUU1yTXl4X2VSNWNMQUZBQkphR0dsNnV0b2F0SGI3UWRJSk1CMlNBNERCRXhUbkRaaHR2VkViaHQxajBGS09GZXRCdjBxd3c4YVowd1FpWmctTjA4cmJVQ2Q2QVk?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxPcEkwcDh0NVZlMWg3WlRHQUlGM0ZnV0dpbktGdHBpT3FYamkyZ0NYVm5qSkVxajFwVXdiMFZpT3UzQUwydjVfWXdsN0Y0X3ZxRm1UZmJ4V3dFSGRJOHpCb2E4YzdEMi1BWUxrRm5RTGtqdUpRZkJ1c19COWxhTzQzX0RSbS1CNkRaaTlJ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPRm40OVVmVmxpU3Z1alRpUDV2U2wtYmk2enZKQmlkdTNWd0NWbXVvenNremt5RmRodVgtak5JdHdlVUZXQUkxdDRna1dNSDJROEhqWlJvQ0phMTUxcVVJUGxnNFNrSXFvMzBmTGhQWjdfVnAzOGNnYlJGTFFNSk5FTFhpcVQyRy1VdHlPMVB6SDI3QnBUYUFN?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxPa3EtSHdSTV81YXVmX05MVzRPbDBmTk9UM292ZzdsRnAxNE8wYkpSWEd6Qmg5QzlGRTVHdnM3aHdacjVobHdaNEc4Q29XQnN5UENvdHd1U2Z2THgtQjlMTGVEdEdqZndhSW9meTRXTGhrXzFPb09VT3BPMEFTZjg2VG1qWTBNQXYwYWpvQg?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxOX0RWNUJyNWZkX0VTTVZXYXZ5U3pwMkVieTlZcnpDT0YyRU5BbmJHUzRHVnEzWVdzal9CcE8yN1ZYSFFXZUppMzg3VjA5cHlJbHJCVl80dEZxaUh4X0xVM09KWDVXOWR0ZWt1MTBfVy0wTXhNWm42RVpVZ0l4TUk4bWFlczZadE56NENJWENHLTFpRlROXy1mMU45ZE5tbHlXRW5kT05LZkh2YWhKOWo2eGxFUU8zeGxOYWN0a19R?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOb1drZnhod1VWM3VxQVJVbUpSUkV3T19fVXU1RkZvNFYycXdabW0yMXlVRXExa1BhZk0ySVR4d0J6N1FVS0hTdV81ODk1ZHRsSGpsNV9sWEhyOFJudEhNdktBejB6UjRWaTEyMEpQdUdpRGZidUFyWHRkZjRLeXdwRzYwdEVOUVZ4ckdOakk4U01kSV9sQ1c1alp6U04?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxOWmtIUVJ6QllHYkFmS3pqMDh6WkR1ZUM0X0QyWll5d0RpMllEeFJrVG1pcl9WdUlyWmtDWkhZbU1HZU1oSF9lVVB2b3R2SHZFNzVPOUFseEhQS1Fqc04xaWlYdE14SUxoYTFyRFYzVjUyUGZ0NE5VMGhBWkZPQzVURV9mcWE1TEU1aFBUakFZU3I1dXc?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQdU1HbzlwTm93MndfY1VROENtajdjV2c5UHZ6RWFiaWJlZWRFekFhbTBmRTQzR080aUZFMlBBa3NnRE5jYkN0TTJ3RW5POU5OaVFzWDJmRm5BVU00MnBnNTZKX0ZiLW5CNkZ6a2hkZXV3cXkzZFpqZmJ4S0VxMkRqWXNCWEpZWWhfbFJ3ckhsdllUMVdHX1I5NnNTQUg?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOVlREYjhBblZnel80UUYwWHdMeU9UU0ZXeTRaMWhYNk14VUdYZUs0RV9ucHZYc1MwbTM2MG1QQ2NuaENfcFlFWEM2N0RpSTlfYW9aUlBRS2FxUTM4RGtfUVMtSnJULXR6QUk2bGtTN3I2aEVlTlF5ampXT3IwY1lTbEd6LTU2V0FGQ3JaLXJTWjl6OThUd2pIRnIxVQ?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxOZGptMG9GN3dsVmc1MzZzZHdKQldZMm0wdmVSay01a3FWMURQUEktQ2tGRE9mNGMyb3l2OEVqczhKdTJJRmVFcGYzd1lLQXNaQjJkLWhqZC15SmY0Z1NyT0tNVEFDTE9FeFdqNUZwRFNRTmRKRXRNZTVjSGNaYk9aY19kdXdUamVDZ21RdEl1Q052YVFaNVJDeTVjdDlSeEllTVFLRjhPQUZQVDhIbE85RlBFSVFSUU0?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxQb3h4anVfaEFKZDg1QkpHWTZ4NVI4UFpBdkZyQ0JEejhYckIxelJEQ0lfVTBmSEw0MTk4cDg2djFoRHVRbDd3MXVJWV83NnFPQmpBOW5xZHFvVURiSVg3TE02Zm4tVzVUUTNkR0NWaXpCYWEza0lvcG5LblVBc0Rlb1BZRFFhcG5rQ19RNHNkb3REUWZVX0FtRXJoLW5iZXpPbTJGSFo4eEFXVlA1SktJ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOMHN2dUpzWHQ5Zzh6ZGVBSWZsSUk5Wnozek5sbmNZQjhWYTVIQlRJZUdBT2xhU2xDZ2Jsb1dIbkkzNWtacTNRTXl6NVpwVENHdHgycTA2YmJsbXFHZmVpSnQxcTl3eVNXY045NUgwSlE4UnpLYzR4QTJOV0JrUGNGelR0TGpPTTlaQmNrVGY3eU03TXExdEtF?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxOdnJXRXBJMnkxY1EyaDEydE40SUJFd3I4b0xXaVY2T1kySXFFSFdkV2owb1JRak90UGtISjFWemstZ1VCVHZGSzg5ZFNIc1hwMi1BSXltSTdzejVjMHZ6bDlic3VmTzhxRkJUMjg0T21Ba1dSRUFycUc5RElER3JqdlB3ZmhfSlVRckhMbWR1MEdBOUxMWktiaUFCY041eldNN3NiU0tLaw?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNVDRxN2F0dVA1OXdhZFZCY21IYkYyRS1SQnYyT2taYXRlMDZ2SXl0NEZxY0h5aHNPenl5ZmlDbTZUZVNzU2ZhRHIwemt2TmpNMXhwcUY2RzBTWktXaU9Ga0NXNDl3cnlRNm55UWdDbjJGWjk0b2VWNnFGNW1GVHdFTlhJLWFtUVpsQmlV?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxQLU8zMTNNbElVNzlnV2NKWFlhRmhsaHpLRktHeGRhRDAwTnVna0tRemgtZWlvaWJ4d244aXp1ZjFpREhHUm8zak9zTEh0a1dKcnY3YXZ2RVZPdVVSWXg1N1VTbG1xeWRZV3BYaklEZkFHOVZUUjRFMWtfZUVROE5qTHNGZXdOSTZNYk45dHZLZw?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxPSFdoSjlEX3l4d3Fha3ExR3hObW1OOXdEWWplN2VIMEVPV0tLd2gxUER4NVpHSE1TdUJyZ0NNNkhieTFYaU8xWl8wYmpCVzllZHloZ0trQ2FUYVItRklBSV81c09lNmF5anR2bzRPNks0RGdRanVuN2tqUnlpMkp2WXpCWXdUczQ?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxPWFlWUUZsU1ZKajFWSnZ5SXpYSmgweDVqdGNDYk5TWnpfNTNEcDA3Y0ZPUGppQkhJN1RGb2xDR1pxUjh6LXZ6blZkY1FtdV8yS1lJc3NrSnhMN1M2UmNjRFk4YlZheW9yT0hpUzJyZWxEWmpLeEpjZ1pUZUVKZEFibEhOU0NKUFF0clI1ZV9Wakl4MEtVS0taQm5jaDdZdVBScnR6cE5pTlFnNnhicDVRcXJieTNPVDVqOVE?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOSmRTRXU1S3VTbjVrSVhnMktzbEJDWF9CejhyMktuWXRESEY4b2I4TzlSc0s1V1ZxUWJPVndlNnd5TXR6RlR1Q2xtOFc3aGltSmF4S05LRUVBdWNJWEhzTXIxZkNzUHRSLXFPUWpPMUJrQWc2Szk3YUota2IzWERpYjU0dVVvNk85S3h4RGQwM2RRMDVB?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
