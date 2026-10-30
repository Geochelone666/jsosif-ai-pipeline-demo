# AAPL Intelligence Report

- ticker: **AAPL**
- Report as_of: **2026-10-29**
- Market data as_of: **2026-10-29**
- Quant sources: https://finance.yahoo.com/quote/AAPL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AAPL/key-statistics/
- AI analysis snapshot as_of: **2026-10-29**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-30T02:38:45.388927+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 7, 'ai': 10, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **12** exact headline/source/date matches; prior report **20261029T020157Z-688a53f0/AAPL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **5**; {'low_uncalibrated_model_confidence': 5}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 8 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 50.0%; oldest publication 2026-10-22

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 348.9100 |
| Return 1D (%) | 1.4775 |
| Return 1W (%) | 0.1982 |
| Return 1M (%) | 5.9229 |
| Return YTD (%) | 28.6911 |
| Return 1Y (%) | 29.8476 |
| Annualized volatility (%) | 24.0457 |
| Beta vs SPY | 0.5529 |
| Max drawdown (%) | -13.7985 |
| Sharpe (rf=0) | 1.2115 |
| Downside deviation (rf=0, %) | 16.6312 |
| Sortino (rf=0) | 1.7516 |
| Historical VaR 95% (1D, %) | 2.0034 |
| Historical ES 95% (1D, %) | 3.4742 |
| Correlation vs SPY | 0.2922 |
| Tracking error vs SPY (%) | 23.6879 |
| P/E (trailing) | 40.01 |
| P/B | 47.41 |
| EV/EBITDA | 30.45 |
| Revenue growth (%) | 16.40 |
| Forward P/E (estimate) | 36.51 |
| Gross margin (%) | 48.65 |
| Operating margin (%) | 32.62 |
| Return on equity (%) | 148.75 |
| Free cash flow yield (%) | 2.12 |
| MA50 | 332.3742 |
| Close vs MA50 (%) | 4.9751 |
| MA200 | 295.8423 |
| Close vs MA200 (%) | 17.9378 |
| RSI (14, Wilder) | 61.3915 |
| MACD (12,26) | 4.0623 |
| MACD signal (9) | 4.0661 |
| MACD histogram | -0.0038 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AAPL': 271, 'SPY': 271}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 348.9100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.4775 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.1982 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 5.9229 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 28.6911 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 29.8476 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 24.0457 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.6312 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.7516 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0034 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.4742 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2922 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.6879 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5529 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -13.7985 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.2115 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 36.5114 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 48.6530 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 32.6230 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 148.7510 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.1155 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 40.0126 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 61.3915 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.0038 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 4.9751 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 17.9378 -> Clearly above the moving-average trend level.

## TAILWINDS

### Apple stock price forecast: $354.45 resistance as AAPL gains 1.56%
- Summary: Apple stock price forecast: $354.45 resistance as AAPL gains 1.56%
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxQY09mb0JlX0dFZi1ZeWx5SGN2RVFnMG50Wmx5VEdVbDU4bVItOF9uV1VuVlZiRVQ0dEdJZWRUQ2VaTFFjMWtxbE1wS0VCMUM0OEZFWWFVNkdIOWp4V0pWVU5BOHhKeVZETlA0a0Npdkg1eVNBZVMzbUY4bkNwVlF2RkRSdlRDRmxzYmg4T0hWWmk?oc=5>

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

### Apple Stock (AAPL) Looks Risky Ahead of Q4 Earnings
- Summary: Apple Stock (AAPL) Looks Risky Ahead of Q4 Earnings
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihgFBVV95cUxNRnJkRHVuTW9OZ3pCT01pWV9zSjJxU0E0ZUhjVmN4QnRwUzgtdDNaVjJVbjI1M2VLV0VfbTRwX3k2eHpTMXo3bTZDS01mY2U1UldoaXZGMFg0RkQ2SUtRRE1ubkYwR0sxYk16RVBEMFp2NTBYTS1hTEtKcGtpZG1IY3h0Vjl0QQ?oc=5>

### Apple Just Became the Most Valuable Company in the World. It Faces a Key iPhone Test.
- Summary: Apple Just Became the Most Valuable Company in the World. It Faces a Key iPhone Test.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOb1drZnhod1VWM3VxQVJVbUpSUkV3T19fVXU1RkZvNFYycXdabW0yMXlVRXExa1BhZk0ySVR4d0J6N1FVS0hTdV81ODk1ZHRsSGpsNV9sWEhyOFJudEhNdktBejB6UjRWaTEyMEpQdUdpRGZidUFyWHRkZjRLeXdwRzYwdEVOUVZ4ckdOakk4U01kSV9sQ1c1alp6U04?oc=5>

### Apple in spotlight as Monness, Crespi, Hardt ups price target on new products (AAPL:NASDAQ)
- Summary: Apple in spotlight as Monness, Crespi, Hardt ups price target on new products (AAPL:NASDAQ)
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxNXzNLSTBNbGdOX2N3WExQSGkyRDFHYkFyVEwyOF9SRTl1b251TW02eEtMdUhGRUZPUWEySzcxY0FXYnMwWWo3QW9KdEduQTIzbEM1eTJ1SC03ODQzR2U5Uy1aclkyb01seU5ycEp6d1RxekppYTU2TXhzQmVZeVJ0Nlk3LWwzV1dLaXJOOXY0N3VSVW9DT01qYmVwdDd4alhNUnp5b1YyMks4ZzRzblg4cWhrWQ?oc=5>

### Apple (AAPL) vs. MSFT and GOOGL: Is the Post-Earnings Selloff Creating a Long-Term Buying Opportunity?
- Summary: Analyst questions if recent selloff offers a buying chance for Apple shares.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxOWmtIUVJ6QllHYkFmS3pqMDh6WkR1ZUM0X0QyWll5d0RpMllEeFJrVG1pcl9WdUlyWmtDWkhZbU1HZU1oSF9lVVB2b3R2SHZFNzVPOUFseEhQS1Fqc04xaWlYdE14SUxoYTFyRFYzVjUyUGZ0NE5VMGhBWkZPQzVURV9mcWE1TEU1aFBUakFZU3I1dXc?oc=5>

### Apple (AAPL) Could Be 36% Overvalued As AI Launches Meet iPhone Duo Scrutiny
- Summary: Report suggests Apple may be overvalued amid AI product launch concerns.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOVlREYjhBblZnel80UUYwWHdMeU9UU0ZXeTRaMWhYNk14VUdYZUs0RV9ucHZYc1MwbTM2MG1QQ2NuaENfcFlFWEM2N0RpSTlfYW9aUlBRS2FxUTM4RGtfUVMtSnJULXR6QUk2bGtTN3I2aEVlTlF5ampXT3IwY1lTbEd6LTU2V0FGQ3JaLXJTWjl6OThUd2pIRnIxVQ?oc=5>

### Will Apple (AAPL) Beat Estimates Again in Its Next Earnings Report?
- Summary: Upcoming earnings could exceed expectations, supporting investor confidence.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQdU1HbzlwTm93MndfY1VROENtajdjV2c5UHZ6RWFiaWJlZWRFekFhbTBmRTQzR080aUZFMlBBa3NnRE5jYkN0TTJ3RW5POU5OaVFzWDJmRm5BVU00MnBnNTZKX0ZiLW5CNkZ6a2hkZXV3cXkzZFpqZmJ4S0VxMkRqWXNCWEpZWWhfbFJ3ckhsdllUMVdHX1I5NnNTQUg?oc=5>

### Loop Capital Lowers Apple Stock Price Target on iPhone Shipment Concerns
- Summary: Loop Capital cuts price target due to worries about iPhone shipments.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxOZGptMG9GN3dsVmc1MzZzZHdKQldZMm0wdmVSay01a3FWMURQUEktQ2tGRE9mNGMyb3l2OEVqczhKdTJJRmVFcGYzd1lLQXNaQjJkLWhqZC15SmY0Z1NyT0tNVEFDTE9FeFdqNUZwRFNRTmRKRXRNZTVjSGNaYk9aY19kdXdUamVDZ21RdEl1Q052YVFaNVJDeTVjdDlSeEllTVFLRjhPQUZQVDhIbE85RlBFSVFSUU0?oc=5>

### Apple’s Next Growth Engine Could Change the Stock’s Trajectory
- Summary: Speculation that new growth engine could alter Apple’s stock performance.
- Date: 2026-10-27 | Impact: medium | Horizon: medium | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxPdjN2SHZNOGRURjJUTXRPdkEyNkx2RHVxdXpadWZvVUU1a3FFcXNFYnpjdi1iN1RUVVNCX0FKRkxlbzBpalRiaWhXbXE5bDJMM1FyUkxtUmxBdG5KZkhKRi15Z1c1R0hLSkZMZzZtdWtFWnFJRDlkRC1DLTlBUlNKRnVDcWxRdXVZRlBCd01NSDlVLTZQNF91aWRjTGF1TGVHMDN6MW1UUQ?oc=5>

### Apple Q4 Preview: One Phone Could Beat Wall Street's Flat Holiday Forecast (NASDAQ:AAPL)
- Summary: Apple anticipates Q4 revenue surpassing Wall Street forecasts, driven by a strong flagship phone launch.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxQTmlKWXVlUWcyblAzRTZqd09OYnRlQXZqeXN3VFBvZzBRTGFaXzItdkpGdm9aOHhtQzJPNlVPV3AxcVVRUXB1dnFQaHdoYkxQLTRFZFVfRUtPUzAtR2tCTUVWU0lrMXNqNkZKVElvMzJOYy1janN4Yll6OVBOMDd5ekNNYTlKamF3SGIxZzFac0ZCTkdDalJ5VGQ0MGE3M3ZCT0NWaVVOQ29HWFlmM3YxWTJ6WQ?oc=5>

## RISKS

### Why Buying Apple Stock Before Q4 Earnings Could Be Risky
- Summary: Investors warned that buying Apple stock before Q4 earnings may expose them to volatility and potential downside, suggesting caution.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOSmRTRXU1S3VTbjVrSVhnMktzbEJDWF9CejhyMktuWXRESEY4b2I4TzlSc0s1V1ZxUWJPVndlNnd5TXR6RlR1Q2xtOFc3aGltSmF4S05LRUVBdWNJWEhzTXIxZkNzUHRSLXFPUWpPMUJrQWc2Szk3YUota2IzWERpYjU0dVVvNk85S3h4RGQwM2RRMDVB?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AAPL** | **40.01** | **47.41** | **30.45** | **16.40** | **5,092,055,449,600.00 USD** | **29.85** |
| MSFT | 29.53 | 8.90 | 20.57 | 17.70 | 3,936,578,961,408.00 USD | -1.30 |
| GOOGL | 14.82 | 8.26 | 22.35 | 24.20 | 3,471,100,346,368.00 USD | 3.64 |
| SONY | 21.05 | 2.83 | 0.12 | 8.20 | 148,740,866,048.00 USD | -9.62 |

Peers fetched as_of: 2026-10-29; AAPL reuses existing data (market data as_of: 2026-10-29); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-07-30
- Next expected earnings: 2026-11-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-29

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

- https://news.google.com/rss/articles/CBMikAFBVV95cUxQY09mb0JlX0dFZi1ZeWx5SGN2RVFnMG50Wmx5VEdVbDU4bVItOF9uV1VuVlZiRVQ0dEdJZWRUQ2VaTFFjMWtxbE1wS0VCMUM0OEZFWWFVNkdIOWp4V0pWVU5BOHhKeVZETlA0a0Npdkg1eVNBZVMzbUY4bkNwVlF2RkRSdlRDRmxzYmg4T0hWWmk?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxPdVp4UjB2M3RvOWRfR2xTdjkydDFvTTJOdlgxZ3d1NzNfamJ6VjM4SDZpcXhVRm9fV0FDdVlGUEl4SXRsSDNqdi1OeC1lb204c3AxSXQwNlFTMFNWN0FtZVJQZWtrT1YtdlJEWlVaMmVacDRJdGh1NFhpYTladGdseHVmMUJkRHIxaG53MUxPSWVyVVYzOFdVZEZ1eHg5R1NCd0ZTeU5SdEFfMk1XWEdqV0JaZGg?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPMThESjliM3d5eVFiN2Y5X2FjWWNUZGRpWklILWJDVkQ2S056OWVjcGRHOS1nQ3ptSDNqMGlxRGNaVncxMU9QMkVRTk9kNUdoMnMyMEZPOFhUWkw0RlRDU3c3dlY2YllrOWJFTVdpSThkVmozWWlsR1NkSGlDNWNhSkFhb2JDYXJUUnFZUWNGQU41Wkt1OURVV0U2bUpGMl9z?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPNkZWUzFDVnV6dnJSNWxJZzQwWm94bFpsa1lGaXpXR3RGQktsN0JzaVMxZUVkTk56Z0M0cG9KTHFFa2w4QVg0dVF3RjRVYjFNams2NTJreTJsTlNQd1hEMkQxMVBMZ2lxVUxzMV9FZHRnd2oyVlc1eFlUMWdtWFdyamk3Zy14ZzBneFRvSE01YmpiSXFjSXNGTTQybEFFeUE?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxOWXh1UmFwUVNWd3FhWUNKSG13R1BJbHdheXBRNFdGcVFqYnJqc3hWdXE2N2RwUGdlUU1yTXl4X2VSNWNMQUZBQkphR0dsNnV0b2F0SGI3UWRJSk1CMlNBNERCRXhUbkRaaHR2VkViaHQxajBGS09GZXRCdjBxd3c4YVowd1FpWmctTjA4cmJVQ2Q2QVk?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxPcEkwcDh0NVZlMWg3WlRHQUlGM0ZnV0dpbktGdHBpT3FYamkyZ0NYVm5qSkVxajFwVXdiMFZpT3UzQUwydjVfWXdsN0Y0X3ZxRm1UZmJ4V3dFSGRJOHpCb2E4YzdEMi1BWUxrRm5RTGtqdUpRZkJ1c19COWxhTzQzX0RSbS1CNkRaaTlJ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPRm40OVVmVmxpU3Z1alRpUDV2U2wtYmk2enZKQmlkdTNWd0NWbXVvenNremt5RmRodVgtak5JdHdlVUZXQUkxdDRna1dNSDJROEhqWlJvQ0phMTUxcVVJUGxnNFNrSXFvMzBmTGhQWjdfVnAzOGNnYlJGTFFNSk5FTFhpcVQyRy1VdHlPMVB6SDI3QnBUYUFN?oc=5
- https://news.google.com/rss/articles/CBMihgFBVV95cUxNRnJkRHVuTW9OZ3pCT01pWV9zSjJxU0E0ZUhjVmN4QnRwUzgtdDNaVjJVbjI1M2VLV0VfbTRwX3k2eHpTMXo3bTZDS01mY2U1UldoaXZGMFg0RkQ2SUtRRE1ubkYwR0sxYk16RVBEMFp2NTBYTS1hTEtKcGtpZG1IY3h0Vjl0QQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOb1drZnhod1VWM3VxQVJVbUpSUkV3T19fVXU1RkZvNFYycXdabW0yMXlVRXExa1BhZk0ySVR4d0J6N1FVS0hTdV81ODk1ZHRsSGpsNV9sWEhyOFJudEhNdktBejB6UjRWaTEyMEpQdUdpRGZidUFyWHRkZjRLeXdwRzYwdEVOUVZ4ckdOakk4U01kSV9sQ1c1alp6U04?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxNXzNLSTBNbGdOX2N3WExQSGkyRDFHYkFyVEwyOF9SRTl1b251TW02eEtMdUhGRUZPUWEySzcxY0FXYnMwWWo3QW9KdEduQTIzbEM1eTJ1SC03ODQzR2U5Uy1aclkyb01seU5ycEp6d1RxekppYTU2TXhzQmVZeVJ0Nlk3LWwzV1dLaXJOOXY0N3VSVW9DT01qYmVwdDd4alhNUnp5b1YyMks4ZzRzblg4cWhrWQ?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxOWmtIUVJ6QllHYkFmS3pqMDh6WkR1ZUM0X0QyWll5d0RpMllEeFJrVG1pcl9WdUlyWmtDWkhZbU1HZU1oSF9lVVB2b3R2SHZFNzVPOUFseEhQS1Fqc04xaWlYdE14SUxoYTFyRFYzVjUyUGZ0NE5VMGhBWkZPQzVURV9mcWE1TEU1aFBUakFZU3I1dXc?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOVlREYjhBblZnel80UUYwWHdMeU9UU0ZXeTRaMWhYNk14VUdYZUs0RV9ucHZYc1MwbTM2MG1QQ2NuaENfcFlFWEM2N0RpSTlfYW9aUlBRS2FxUTM4RGtfUVMtSnJULXR6QUk2bGtTN3I2aEVlTlF5ampXT3IwY1lTbEd6LTU2V0FGQ3JaLXJTWjl6OThUd2pIRnIxVQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQdU1HbzlwTm93MndfY1VROENtajdjV2c5UHZ6RWFiaWJlZWRFekFhbTBmRTQzR080aUZFMlBBa3NnRE5jYkN0TTJ3RW5POU5OaVFzWDJmRm5BVU00MnBnNTZKX0ZiLW5CNkZ6a2hkZXV3cXkzZFpqZmJ4S0VxMkRqWXNCWEpZWWhfbFJ3ckhsdllUMVdHX1I5NnNTQUg?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxOZGptMG9GN3dsVmc1MzZzZHdKQldZMm0wdmVSay01a3FWMURQUEktQ2tGRE9mNGMyb3l2OEVqczhKdTJJRmVFcGYzd1lLQXNaQjJkLWhqZC15SmY0Z1NyT0tNVEFDTE9FeFdqNUZwRFNRTmRKRXRNZTVjSGNaYk9aY19kdXdUamVDZ21RdEl1Q052YVFaNVJDeTVjdDlSeEllTVFLRjhPQUZQVDhIbE85RlBFSVFSUU0?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPdjN2SHZNOGRURjJUTXRPdkEyNkx2RHVxdXpadWZvVUU1a3FFcXNFYnpjdi1iN1RUVVNCX0FKRkxlbzBpalRiaWhXbXE5bDJMM1FyUkxtUmxBdG5KZkhKRi15Z1c1R0hLSkZMZzZtdWtFWnFJRDlkRC1DLTlBUlNKRnVDcWxRdXVZRlBCd01NSDlVLTZQNF91aWRjTGF1TGVHMDN6MW1UUQ?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxQTmlKWXVlUWcyblAzRTZqd09OYnRlQXZqeXN3VFBvZzBRTGFaXzItdkpGdm9aOHhtQzJPNlVPV3AxcVVRUXB1dnFQaHdoYkxQLTRFZFVfRUtPUzAtR2tCTUVWU0lrMXNqNkZKVElvMzJOYy1janN4Yll6OVBOMDd5ekNNYTlKamF3SGIxZzFac0ZCTkdDalJ5VGQ0MGE3M3ZCT0NWaVVOQ29HWFlmM3YxWTJ6WQ?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOSmRTRXU1S3VTbjVrSVhnMktzbEJDWF9CejhyMktuWXRESEY4b2I4TzlSc0s1V1ZxUWJPVndlNnd5TXR6RlR1Q2xtOFc3aGltSmF4S05LRUVBdWNJWEhzTXIxZkNzUHRSLXFPUWpPMUJrQWc2Szk3YUota2IzWERpYjU0dVVvNk85S3h4RGQwM2RRMDVB?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
