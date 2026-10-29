# AAPL Intelligence Report

- ticker: **AAPL**
- Report as_of: **2026-10-28**
- Market data as_of: **2026-10-28**
- Quant sources: https://finance.yahoo.com/quote/AAPL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AAPL/key-statistics/
- AI analysis snapshot as_of: **2026-10-28**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-29T02:08:24.326334+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 5, 'ai': 15, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **14** exact headline/source/date matches; prior report **20261028T015717Z-533e470c/AAPL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **6**; {'low_uncalibrated_model_confidence': 6}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 9 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 44.0%; oldest publication 2026-10-21

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 343.8300 |
| Return 1D (%) | -0.9421 |
| Return 1W (%) | -0.0465 |
| Return 1M (%) | 1.6046 |
| Return YTD (%) | 26.8174 |
| Return 1Y (%) | 28.2900 |
| Annualized volatility (%) | 24.0071 |
| Beta vs SPY | 0.5572 |
| Max drawdown (%) | -13.7985 |
| Sharpe (rf=0) | 1.1625 |
| Downside deviation (rf=0, %) | 16.6312 |
| Sortino (rf=0) | 1.6781 |
| Historical VaR 95% (1D, %) | 2.0034 |
| Historical ES 95% (1D, %) | 3.4742 |
| Correlation vs SPY | 0.2948 |
| Tracking error vs SPY (%) | 23.6194 |
| P/E (trailing) | 39.80 |
| P/B | 46.72 |
| EV/EBITDA | 30.01 |
| Revenue growth (%) | 16.40 |
| Forward P/E (estimate) | 35.96 |
| Gross margin (%) | 48.65 |
| Operating margin (%) | 32.62 |
| Return on equity (%) | 148.75 |
| Free cash flow yield (%) | 2.15 |
| MA50 | 331.7326 |
| Close vs MA50 (%) | 3.6467 |
| MA200 | 295.3995 |
| Close vs MA200 (%) | 16.3949 |
| RSI (14, Wilder) | 56.1152 |
| MACD (12,26) | 3.9198 |
| MACD signal (9) | 4.0670 |
| MACD histogram | -0.1472 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AAPL': 270, 'SPY': 270}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 343.8300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.9421 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.0465 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 1.6046 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 26.8174 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 28.2900 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 24.0071 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.6312 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.6781 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0034 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.4742 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2948 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.6194 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5572 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -13.7985 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1625 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 35.9563 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 48.6530 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 32.6230 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 148.7510 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.1467 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 39.7951 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 56.1152 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.1472 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 3.6467 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 16.3949 -> Clearly above the moving-average trend level.

## TAILWINDS

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

### Apple takes wraps off MacBook Pro with touch screen to end product blitz (AAPL:NASDAQ)
- Summary: Apple introduces touch‑screen MacBook Pro, signaling product innovation.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxPNVZqNVJZNmM5VGtOSXNuRnN6Z3VEQTl0OTZUV09DSTF6TEJnNjg5LWJGOXdZR1h2aEgxcXRPVmp1RGpyV2VOX0ZNRWlzbHJ1MWdLVHk3eHlwRFNpWnpKLUdWMXVLOE9rNG5ZNnBzU0NRVVVMV0t1NHhIWU1DeUY1bG9oWVFhQ3VMNzJQdVlveHhLX01pdS1RaXhFTmtWMm5rb09HMTVXS2lrZGs3VGVr?oc=5>

## HEADWINDS

### Apple (AAPL) Stock Falls Amid Market Uptick: What Investors Need to Know
- Summary: Apple (AAPL) Stock Falls Amid Market Uptick: What Investors Need to Know
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPRm40OVVmVmxpU3Z1alRpUDV2U2wtYmk2enZKQmlkdTNWd0NWbXVvenNremt5RmRodVgtak5JdHdlVUZXQUkxdDRna1dNSDJROEhqWlJvQ0phMTUxcVVJUGxnNFNrSXFvMzBmTGhQWjdfVnAzOGNnYlJGTFFNSk5FTFhpcVQyRy1VdHlPMVB6SDI3QnBUYUFN?oc=5>

### Apple Stock Dips: What's Going On?
- Summary: Apple shares decline, indicating market uncertainty.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPVnVwYUpiYU1BWTF4a0Z1VnBTWmEyVng0MWItc0RESUZIQmN3OWw4YnJ6VGZmdFVOcTBWX0dLcHVLejdJREN2b0U4bXItU09iTk5ZZDlFMmYwQTVJY01sT1ZmdnRVdlVLSHF3cUd5SkFqc055MTFMSnFzRUVwcnIxRkhCeUppRF95OGVqMDdHVWdUOXY5cWI0?oc=5>

### Apple zigs while Nasdaq zags, correlation turns negative (AAPL:NASDAQ)
- Summary: Apple’s performance diverges from Nasdaq, reflecting negative correlation.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOZzhpTnRSQmhnTFJVcDJqNE50WWJtZGVjYXluWE5JdENoLUM4OUFoWkZLVEVDM2d1TTZzeHpBc2V6VXNEaEEzMjRoM0VmSTN3cXk2U190akpUcW43R2pBbW1MejdtbE96aG9oUTlCT1ZUeWtILXlOUzhwU3RRYnhzc1IxUGdnYXVMTWxUTEt1Y2lZeVBqcXlMMA?oc=5>

## CATALYSTS

### Apple Stock (AAPL) Looks Risky Ahead of Q4 Earnings
- Summary: Apple Stock (AAPL) Looks Risky Ahead of Q4 Earnings
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihgFBVV95cUxNRnJkRHVuTW9OZ3pCT01pWV9zSjJxU0E0ZUhjVmN4QnRwUzgtdDNaVjJVbjI1M2VLV0VfbTRwX3k2eHpTMXo3bTZDS01mY2U1UldoaXZGMFg0RkQ2SUtRRE1ubkYwR0sxYk16RVBEMFp2NTBYTS1hTEtKcGtpZG1IY3h0Vjl0QQ?oc=5>

### Apple in spotlight as Monness, Crespi, Hardt ups price target on new products (AAPL:NASDAQ)
- Summary: Apple in spotlight as Monness, Crespi, Hardt ups price target on new products (AAPL:NASDAQ)
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxNXzNLSTBNbGdOX2N3WExQSGkyRDFHYkFyVEwyOF9SRTl1b251TW02eEtMdUhGRUZPUWEySzcxY0FXYnMwWWo3QW9KdEduQTIzbEM1eTJ1SC03ODQzR2U5Uy1aclkyb01seU5ycEp6d1RxekppYTU2TXhzQmVZeVJ0Nlk3LWwzV1dLaXJOOXY0N3VSVW9DT01qYmVwdDd4alhNUnp5b1YyMks4ZzRzblg4cWhrWQ?oc=5>

### Apple Stock Hits Record High On iPhone Duo Launch
- Summary: Apple Stock Hits Record High On iPhone Duo Launch
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNdUltNURaQjNjcmctdzRVNGdxX3ZWbmE0ejVOc0c3aXFjQVUzVC14VURDMGRKQzViUzFQdlV1Z3hOQy1sZTJNdkVrWDFxOC0zSXlTalJyQW1TbVdhYVRQRFU3UmxCREFPdWlHbzRxOEg3T1BRMTh5cGxPRk00d3VualFvbnhhOEFaYkIwVTRsRUtNRlZobjdz?oc=5>

### Apple's iPhone Duo: Management Listened To The Innovation Critics (NASDAQ:AAPL)
- Summary: Apple's iPhone Duo: Management Listened To The Innovation Critics (NASDAQ:AAPL)
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxPUG5NM01uN3RIWHlIZkwyTTUzbF9rYjhvOXpMeF9LLU5vSENwYWdta2dfZ2pVdTJCQ0ZSc2RYaEtrLTJuOTFNbFozbjF4NEJ1THpGUEJ0YXVMcE1mZW54bHVfNi1SUDB1VnpEakNZODNRcWl0WkM2bmZpei1GRTg2Z2hDamJtMDhPTEFFdUxTS0Fwa09FMTVRcVFIQy1FZGpqNmZqXzVyOA?oc=5>

### Apple (AAPL) vs. MSFT and GOOGL: Is the Post-Earnings Selloff Creating a Long-Term Buying Opportunity?
- Summary: Analyst questions if recent selloff offers a buying chance for Apple shares.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxOWmtIUVJ6QllHYkFmS3pqMDh6WkR1ZUM0X0QyWll5d0RpMllEeFJrVG1pcl9WdUlyWmtDWkhZbU1HZU1oSF9lVVB2b3R2SHZFNzVPOUFseEhQS1Fqc04xaWlYdE14SUxoYTFyRFYzVjUyUGZ0NE5VMGhBWkZPQzVURV9mcWE1TEU1aFBUakFZU3I1dXc?oc=5>

### Loop Capital Lowers Apple Stock Price Target on iPhone Shipment Concerns
- Summary: Loop Capital cuts price target due to worries about iPhone shipments.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxOZGptMG9GN3dsVmc1MzZzZHdKQldZMm0wdmVSay01a3FWMURQUEktQ2tGRE9mNGMyb3l2OEVqczhKdTJJRmVFcGYzd1lLQXNaQjJkLWhqZC15SmY0Z1NyT0tNVEFDTE9FeFdqNUZwRFNRTmRKRXRNZTVjSGNaYk9aY19kdXdUamVDZ21RdEl1Q052YVFaNVJDeTVjdDlSeEllTVFLRjhPQUZQVDhIbE85RlBFSVFSUU0?oc=5>

### Apple (AAPL) Could Be 36% Overvalued As AI Launches Meet iPhone Duo Scrutiny
- Summary: Report suggests Apple may be overvalued amid AI product launch concerns.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOVlREYjhBblZnel80UUYwWHdMeU9UU0ZXeTRaMWhYNk14VUdYZUs0RV9ucHZYc1MwbTM2MG1QQ2NuaENfcFlFWEM2N0RpSTlfYW9aUlBRS2FxUTM4RGtfUVMtSnJULXR6QUk2bGtTN3I2aEVlTlF5ampXT3IwY1lTbEd6LTU2V0FGQ3JaLXJTWjl6OThUd2pIRnIxVQ?oc=5>

### Will Apple (AAPL) Beat Estimates Again in Its Next Earnings Report?
- Summary: Upcoming earnings could exceed expectations, supporting investor confidence.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQdU1HbzlwTm93MndfY1VROENtajdjV2c5UHZ6RWFiaWJlZWRFekFhbTBmRTQzR080aUZFMlBBa3NnRE5jYkN0TTJ3RW5POU5OaVFzWDJmRm5BVU00MnBnNTZKX0ZiLW5CNkZ6a2hkZXV3cXkzZFpqZmJ4S0VxMkRqWXNCWEpZWWhfbFJ3ckhsdllUMVdHX1I5NnNTQUg?oc=5>

### Apple’s Next Growth Engine Could Change the Stock’s Trajectory
- Summary: Speculation that new growth engine could alter Apple’s stock performance.
- Date: 2026-10-27 | Impact: medium | Horizon: medium | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxPdjN2SHZNOGRURjJUTXRPdkEyNkx2RHVxdXpadWZvVUU1a3FFcXNFYnpjdi1iN1RUVVNCX0FKRkxlbzBpalRiaWhXbXE5bDJMM1FyUkxtUmxBdG5KZkhKRi15Z1c1R0hLSkZMZzZtdWtFWnFJRDlkRC1DLTlBUlNKRnVDcWxRdXVZRlBCd01NSDlVLTZQNF91aWRjTGF1TGVHMDN6MW1UUQ?oc=5>

### What Is Going On With Apple Stock on Tuesday?
- Summary: Investors seek explanation for Apple stock movement on Tuesday.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOVDVmamRlV0sxY1JPSmJJbXRZbGllbGlIUkxzZ09YMzFuSF9WNDRRWlRWYzd4R2l2eERBUlB3R09DaUQ1YmVZOHRYQ3lhXzFRcU9RR2hHTzlRR3ZzX0htTTRoMkgzaGx1TlBSWVBNOUUzTmo2VjVOMlBhU3BQc01XZ0duREstSmZGcFRqRC13cjZCZmtFSmRJWmVBQzZ2dw?oc=5>

### Billionaire Ken Fisher and Jim Cramer Still Like Apple (AAPL). Should You?
- Summary: Analysts Ken Fisher and Jim Cramer express continued confidence in Apple, suggesting potential upside for investors.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNY3JUbWpTS29yaXBSMVRxZjM0bmttUDZLZzVTWFhjU1hLWHJhWGtEWVl1T1JJUjdEeXZrb05rUFpzWTVMR1JHWjd3TFphWTFlQ25OWWtQSm5Udk42R2NlNnFFcEM3azNRNllGNnQxNWJKb2U1S3I0ZzFfZTkyYkp5UWw2c3ZWa0IydzRKaGpLVEJCbzU5XzJzbzVIUGxyY3M?oc=5>

## RISKS

### Why Buying Apple Stock Before Q4 Earnings Could Be Risky
- Summary: Investors warned that buying Apple stock before Q4 earnings may expose them to volatility and potential downside, suggesting caution.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOSmRTRXU1S3VTbjVrSVhnMktzbEJDWF9CejhyMktuWXRESEY4b2I4TzlSc0s1V1ZxUWJPVndlNnd5TXR6RlR1Q2xtOFc3aGltSmF4S05LRUVBdWNJWEhzTXIxZkNzUHRSLXFPUWpPMUJrQWc2Szk3YUota2IzWERpYjU0dVVvNk85S3h4RGQwM2RRMDVB?oc=5>

### Google, Apple hit with $47.6M fine in South Korea over unfair app market practices (AAPL:NASDAQ)
- Summary: Apple fined $47.6M for alleged unfair app market practices in South Korea.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxNcFU5TnpJYzAzeWRnazF3dWtEUExpMzh4azg4LW8wQm1vWENMbmVwalZxWWJNMDV0aWw1UmJ0Z1ladldLQzFSUk1pRmZSSGpDZHZwQTNQSmJEX3lEV2lTWmFOQ3ljcGZJeDBDdE1KUEotRjA4ME1NUUV0TnJaZkY5QzBXRV9Dd19PRjdUdzZKS3RUTHNrSm80cUhSY1VCRUU1S2N6Q0o3WFM5VzNPMEhLcEd0c095VkNN?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AAPL** | **39.80** | **46.72** | **30.01** | **16.40** | **5,017,916,932,096.00 USD** | **28.29** |
| MSFT | 29.58 | 8.91 | 20.57 | 17.70 | 3,943,039,238,144.00 USD | -1.23 |
| GOOGL | 16.08 | 6.38 | 22.35 | 24.20 | 3,973,383,716,864.00 USD | 21.78 |
| SONY | 21.19 | 2.80 | 0.12 | 8.20 | 147,280,904,192.00 USD | -13.00 |

Peers fetched as_of: 2026-10-28; AAPL reuses existing data (market data as_of: 2026-10-28); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-07-30
- Next expected earnings: 2026-11-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-28

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

- https://news.google.com/rss/articles/CBMioAFBVV95cUxPMThESjliM3d5eVFiN2Y5X2FjWWNUZGRpWklILWJDVkQ2S056OWVjcGRHOS1nQ3ptSDNqMGlxRGNaVncxMU9QMkVRTk9kNUdoMnMyMEZPOFhUWkw0RlRDU3c3dlY2YllrOWJFTVdpSThkVmozWWlsR1NkSGlDNWNhSkFhb2JDYXJUUnFZUWNGQU41Wkt1OURVV0U2bUpGMl9z?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPNkZWUzFDVnV6dnJSNWxJZzQwWm94bFpsa1lGaXpXR3RGQktsN0JzaVMxZUVkTk56Z0M0cG9KTHFFa2w4QVg0dVF3RjRVYjFNams2NTJreTJsTlNQd1hEMkQxMVBMZ2lxVUxzMV9FZHRnd2oyVlc1eFlUMWdtWFdyamk3Zy14ZzBneFRvSE01YmpiSXFjSXNGTTQybEFFeUE?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxOWXh1UmFwUVNWd3FhWUNKSG13R1BJbHdheXBRNFdGcVFqYnJqc3hWdXE2N2RwUGdlUU1yTXl4X2VSNWNMQUZBQkphR0dsNnV0b2F0SGI3UWRJSk1CMlNBNERCRXhUbkRaaHR2VkViaHQxajBGS09GZXRCdjBxd3c4YVowd1FpWmctTjA4cmJVQ2Q2QVk?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxPNVZqNVJZNmM5VGtOSXNuRnN6Z3VEQTl0OTZUV09DSTF6TEJnNjg5LWJGOXdZR1h2aEgxcXRPVmp1RGpyV2VOX0ZNRWlzbHJ1MWdLVHk3eHlwRFNpWnpKLUdWMXVLOE9rNG5ZNnBzU0NRVVVMV0t1NHhIWU1DeUY1bG9oWVFhQ3VMNzJQdVlveHhLX01pdS1RaXhFTmtWMm5rb09HMTVXS2lrZGs3VGVr?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPRm40OVVmVmxpU3Z1alRpUDV2U2wtYmk2enZKQmlkdTNWd0NWbXVvenNremt5RmRodVgtak5JdHdlVUZXQUkxdDRna1dNSDJROEhqWlJvQ0phMTUxcVVJUGxnNFNrSXFvMzBmTGhQWjdfVnAzOGNnYlJGTFFNSk5FTFhpcVQyRy1VdHlPMVB6SDI3QnBUYUFN?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPVnVwYUpiYU1BWTF4a0Z1VnBTWmEyVng0MWItc0RESUZIQmN3OWw4YnJ6VGZmdFVOcTBWX0dLcHVLejdJREN2b0U4bXItU09iTk5ZZDlFMmYwQTVJY01sT1ZmdnRVdlVLSHF3cUd5SkFqc055MTFMSnFzRUVwcnIxRkhCeUppRF95OGVqMDdHVWdUOXY5cWI0?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOZzhpTnRSQmhnTFJVcDJqNE50WWJtZGVjYXluWE5JdENoLUM4OUFoWkZLVEVDM2d1TTZzeHpBc2V6VXNEaEEzMjRoM0VmSTN3cXk2U190akpUcW43R2pBbW1MejdtbE96aG9oUTlCT1ZUeWtILXlOUzhwU3RRYnhzc1IxUGdnYXVMTWxUTEt1Y2lZeVBqcXlMMA?oc=5
- https://news.google.com/rss/articles/CBMihgFBVV95cUxNRnJkRHVuTW9OZ3pCT01pWV9zSjJxU0E0ZUhjVmN4QnRwUzgtdDNaVjJVbjI1M2VLV0VfbTRwX3k2eHpTMXo3bTZDS01mY2U1UldoaXZGMFg0RkQ2SUtRRE1ubkYwR0sxYk16RVBEMFp2NTBYTS1hTEtKcGtpZG1IY3h0Vjl0QQ?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxNXzNLSTBNbGdOX2N3WExQSGkyRDFHYkFyVEwyOF9SRTl1b251TW02eEtMdUhGRUZPUWEySzcxY0FXYnMwWWo3QW9KdEduQTIzbEM1eTJ1SC03ODQzR2U5Uy1aclkyb01seU5ycEp6d1RxekppYTU2TXhzQmVZeVJ0Nlk3LWwzV1dLaXJOOXY0N3VSVW9DT01qYmVwdDd4alhNUnp5b1YyMks4ZzRzblg4cWhrWQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNdUltNURaQjNjcmctdzRVNGdxX3ZWbmE0ejVOc0c3aXFjQVUzVC14VURDMGRKQzViUzFQdlV1Z3hOQy1sZTJNdkVrWDFxOC0zSXlTalJyQW1TbVdhYVRQRFU3UmxCREFPdWlHbzRxOEg3T1BRMTh5cGxPRk00d3VualFvbnhhOEFaYkIwVTRsRUtNRlZobjdz?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPUG5NM01uN3RIWHlIZkwyTTUzbF9rYjhvOXpMeF9LLU5vSENwYWdta2dfZ2pVdTJCQ0ZSc2RYaEtrLTJuOTFNbFozbjF4NEJ1THpGUEJ0YXVMcE1mZW54bHVfNi1SUDB1VnpEakNZODNRcWl0WkM2bmZpei1GRTg2Z2hDamJtMDhPTEFFdUxTS0Fwa09FMTVRcVFIQy1FZGpqNmZqXzVyOA?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxOWmtIUVJ6QllHYkFmS3pqMDh6WkR1ZUM0X0QyWll5d0RpMllEeFJrVG1pcl9WdUlyWmtDWkhZbU1HZU1oSF9lVVB2b3R2SHZFNzVPOUFseEhQS1Fqc04xaWlYdE14SUxoYTFyRFYzVjUyUGZ0NE5VMGhBWkZPQzVURV9mcWE1TEU1aFBUakFZU3I1dXc?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxOZGptMG9GN3dsVmc1MzZzZHdKQldZMm0wdmVSay01a3FWMURQUEktQ2tGRE9mNGMyb3l2OEVqczhKdTJJRmVFcGYzd1lLQXNaQjJkLWhqZC15SmY0Z1NyT0tNVEFDTE9FeFdqNUZwRFNRTmRKRXRNZTVjSGNaYk9aY19kdXdUamVDZ21RdEl1Q052YVFaNVJDeTVjdDlSeEllTVFLRjhPQUZQVDhIbE85RlBFSVFSUU0?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOVlREYjhBblZnel80UUYwWHdMeU9UU0ZXeTRaMWhYNk14VUdYZUs0RV9ucHZYc1MwbTM2MG1QQ2NuaENfcFlFWEM2N0RpSTlfYW9aUlBRS2FxUTM4RGtfUVMtSnJULXR6QUk2bGtTN3I2aEVlTlF5ampXT3IwY1lTbEd6LTU2V0FGQ3JaLXJTWjl6OThUd2pIRnIxVQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQdU1HbzlwTm93MndfY1VROENtajdjV2c5UHZ6RWFiaWJlZWRFekFhbTBmRTQzR080aUZFMlBBa3NnRE5jYkN0TTJ3RW5POU5OaVFzWDJmRm5BVU00MnBnNTZKX0ZiLW5CNkZ6a2hkZXV3cXkzZFpqZmJ4S0VxMkRqWXNCWEpZWWhfbFJ3ckhsdllUMVdHX1I5NnNTQUg?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPdjN2SHZNOGRURjJUTXRPdkEyNkx2RHVxdXpadWZvVUU1a3FFcXNFYnpjdi1iN1RUVVNCX0FKRkxlbzBpalRiaWhXbXE5bDJMM1FyUkxtUmxBdG5KZkhKRi15Z1c1R0hLSkZMZzZtdWtFWnFJRDlkRC1DLTlBUlNKRnVDcWxRdXVZRlBCd01NSDlVLTZQNF91aWRjTGF1TGVHMDN6MW1UUQ?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOVDVmamRlV0sxY1JPSmJJbXRZbGllbGlIUkxzZ09YMzFuSF9WNDRRWlRWYzd4R2l2eERBUlB3R09DaUQ1YmVZOHRYQ3lhXzFRcU9RR2hHTzlRR3ZzX0htTTRoMkgzaGx1TlBSWVBNOUUzTmo2VjVOMlBhU3BQc01XZ0duREstSmZGcFRqRC13cjZCZmtFSmRJWmVBQzZ2dw?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNY3JUbWpTS29yaXBSMVRxZjM0bmttUDZLZzVTWFhjU1hLWHJhWGtEWVl1T1JJUjdEeXZrb05rUFpzWTVMR1JHWjd3TFphWTFlQ25OWWtQSm5Udk42R2NlNnFFcEM3azNRNllGNnQxNWJKb2U1S3I0ZzFfZTkyYkp5UWw2c3ZWa0IydzRKaGpLVEJCbzU5XzJzbzVIUGxyY3M?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOSmRTRXU1S3VTbjVrSVhnMktzbEJDWF9CejhyMktuWXRESEY4b2I4TzlSc0s1V1ZxUWJPVndlNnd5TXR6RlR1Q2xtOFc3aGltSmF4S05LRUVBdWNJWEhzTXIxZkNzUHRSLXFPUWpPMUJrQWc2Szk3YUota2IzWERpYjU0dVVvNk85S3h4RGQwM2RRMDVB?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxNcFU5TnpJYzAzeWRnazF3dWtEUExpMzh4azg4LW8wQm1vWENMbmVwalZxWWJNMDV0aWw1UmJ0Z1ladldLQzFSUk1pRmZSSGpDZHZwQTNQSmJEX3lEV2lTWmFOQ3ljcGZJeDBDdE1KUEotRjA4ME1NUUV0TnJaZkY5QzBXRV9Dd19PRjdUdzZKS3RUTHNrSm80cUhSY1VCRUU1S2N6Q0o3WFM5VzNPMEhLcEd0c095VkNN?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
