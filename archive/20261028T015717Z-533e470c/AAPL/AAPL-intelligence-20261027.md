# AAPL Intelligence Report

- ticker: **AAPL**
- Report as_of: **2026-10-27**
- Market data as_of: **2026-10-27**
- Quant sources: https://finance.yahoo.com/quote/AAPL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AAPL/key-statistics/
- AI analysis snapshot as_of: **2026-10-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-28T02:14:29.489580+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 5, 'ai': 12, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261027T014607Z-b66f6bd5/AAPL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **6**; {'low_uncalibrated_model_confidence': 6}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 11 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 44.0%; oldest publication 2026-10-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 347.1000 |
| Return 1D (%) | 0.9276 |
| Return 1W (%) | 2.2386 |
| Return 1M (%) | 1.7680 |
| Return YTD (%) | 28.0235 |
| Return 1Y (%) | 29.6016 |
| Annualized volatility (%) | 23.9838 |
| Beta vs SPY | 0.5592 |
| Max drawdown (%) | -13.7985 |
| Sharpe (rf=0) | 1.2060 |
| Downside deviation (rf=0, %) | 16.6044 |
| Sortino (rf=0) | 1.7420 |
| Historical VaR 95% (1D, %) | 2.0034 |
| Historical ES 95% (1D, %) | 3.4742 |
| Correlation vs SPY | 0.2961 |
| Tracking error vs SPY (%) | 23.5821 |
| P/E (trailing) | 39.81 |
| P/B | 47.16 |
| EV/EBITDA | 30.29 |
| Revenue growth (%) | 16.40 |
| Forward P/E (estimate) | 36.30 |
| Gross margin (%) | 48.65 |
| Operating margin (%) | 32.62 |
| Return on equity (%) | 148.75 |
| Free cash flow yield (%) | 2.13 |
| MA50 | 331.0566 |
| Close vs MA50 (%) | 4.8461 |
| MA200 | 294.9780 |
| Close vs MA200 (%) | 17.6698 |
| RSI (14, Wilder) | 61.1067 |
| MACD (12,26) | 4.1983 |
| MACD signal (9) | 4.1038 |
| MACD histogram | 0.0945 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AAPL': 269, 'SPY': 269}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 347.1000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.9276 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.2386 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 1.7680 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 28.0235 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 29.6016 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 23.9838 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.6044 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.7420 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0034 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.4742 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2961 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.5821 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5592 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -13.7985 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.2060 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 36.2982 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 48.6530 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 32.6230 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 148.7510 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.1265 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 39.8050 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 61.1067 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.0945 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 4.8461 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 17.6698 -> Clearly above the moving-average trend level.

## TAILWINDS

### Apple Inc. (AAPL) is Attracting Investor Attention: Here is What You Should Know
- Summary: Investors are focusing on Apple, indicating potential interest in future growth.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPMThESjliM3d5eVFiN2Y5X2FjWWNUZGRpWklILWJDVkQ2S056OWVjcGRHOS1nQ3ptSDNqMGlxRGNaVncxMU9QMkVRTk9kNUdoMnMyMEZPOFhUWkw0RlRDU3c3dlY2YllrOWJFTVdpSThkVmozWWlsR1NkSGlDNWNhSkFhb2JDYXJUUnFZUWNGQU41Wkt1OURVV0U2bUpGMl9z?oc=5>

### Apple (AAPL) Earnings Expected to Grow: Should You Buy?
- Summary: Analysts forecast rising earnings, suggesting a positive outlook for Apple.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPNkZWUzFDVnV6dnJSNWxJZzQwWm94bFpsa1lGaXpXR3RGQktsN0JzaVMxZUVkTk56Z0M0cG9KTHFFa2w4QVg0dVF3RjRVYjFNams2NTJreTJsTlNQd1hEMkQxMVBMZ2lxVUxzMV9FZHRnd2oyVlc1eFlUMWdtWFdyamk3Zy14ZzBneFRvSE01YmpiSXFjSXNGTTQybEFFeUE?oc=5>

### Apple expands Siri AI languages from Portuguese to Japanese (AAPL:NASDAQ)
- Summary: Apple adds Japanese to Siri’s language support, expanding its AI capabilities.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQSzJxNGstbU5Fck55X2FMSmViZF9DdTRDSnJINVVVNXhxcnNkc2I5VEcwSEJnWWVqZ2JoZ0pFNVpyci01NkJYOFVjZkZZLVNrTlRZVk1kQzhQRUxXcWFnOFVqN1NVNnhLMC0xcl81dGZWeDRTLW40RHNteVBYbVpkU0tydWhuV0UzS0ZwNWd6S0d0QVFfV1Q2cVRodG5HZw?oc=5>

### What Does Apple (AAPL) New OLED iPad Mini Mean For Its AI Push?
- Summary: Apple launches OLED iPad Mini, boosting AI capabilities and product lineup.
- Date: 2026-10-27 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxOWXh1UmFwUVNWd3FhWUNKSG13R1BJbHdheXBRNFdGcVFqYnJqc3hWdXE2N2RwUGdlUU1yTXl4X2VSNWNMQUZBQkphR0dsNnV0b2F0SGI3UWRJSk1CMlNBNERCRXhUbkRaaHR2VkViaHQxajBGS09GZXRCdjBxd3c4YVowd1FpWmctTjA4cmJVQ2Q2QVk?oc=5>

## HEADWINDS

### Apple (AAPL) Stock Falls Amid Market Uptick: What Investors Need to Know
- Summary: Apple (AAPL) Stock Falls Amid Market Uptick: What Investors Need to Know
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPRm40OVVmVmxpU3Z1alRpUDV2U2wtYmk2enZKQmlkdTNWd0NWbXVvenNremt5RmRodVgtak5JdHdlVUZXQUkxdDRna1dNSDJROEhqWlJvQ0phMTUxcVVJUGxnNFNrSXFvMzBmTGhQWjdfVnAzOGNnYlJGTFFNSk5FTFhpcVQyRy1VdHlPMVB6SDI3QnBUYUFN?oc=5>

### Apple Inc. (AAPL) stock price, news, quote and history
- Summary: Current stock price reflects market sentiment and recent performance.
- Date: 2026-10-24 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiUkFVX3lxTE5pbUxLdFVNSjJfVjFOUm9UYmFBYUVBRmV5Q3FJU3lfblNtbVNvZjI4N1hEdlVtTnBMYWRCMi0wUTVTUGdxMUhDb0plLWlmcWdqMEE?oc=5>

## CATALYSTS

### Apple responds to early screen flaws on $1,999 foldable iPhone Duo (AAPL:NASDAQ)
- Summary: Apple responds to early screen flaws on $1,999 foldable iPhone Duo (AAPL:NASDAQ)
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxOMXRnVWdleFY1eTlSWjc2VlM5dlgyc1NqT1hHdklKVng0aXVvT004dVRSTmVfM3dBY3R5RlF4WUNVTjV2bHB3aHpXaFZ0UFZBNjdTR05DV3dSTnNGTDA1dEpYVXZvaGZOLUcydldWNUVpZEo0UkczZWcyM3V1cHBvRGdWQk05aEpMSVJPa1h0YTc2cWlWX1ExR0xENEtjaWRjYzVPZw?oc=5>

### Apple (NASDAQ:AAPL) Stock Hits Record US$351.73 as iPhone Duo Production Target Reportedly Jumps 44%
- Summary: Apple (NASDAQ:AAPL) Stock Hits Record US$351.73 as iPhone Duo Production Target Reportedly Jumps 44%
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiekFVX3lxTE42YWZvT3p4TXJERy1HVHRZTTROeWlHWURrY3VnV25CTFpFcTJ4dndMSXR3b3owTW9rTy14eXFTLXNFOGtaV2h3MzFKaFYwMkpJWWV4WnpLaG1iTjI0U0ZMYmtnNTRvUEZIZnhfbnZ3Y01aeHBaUmNlSGJn?oc=5>

### Apple's iPhone Duo: Management Listened To The Innovation Critics (NASDAQ:AAPL)
- Summary: Apple's iPhone Duo: Management Listened To The Innovation Critics (NASDAQ:AAPL)
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxPUG5NM01uN3RIWHlIZkwyTTUzbF9rYjhvOXpMeF9LLU5vSENwYWdta2dfZ2pVdTJCQ0ZSc2RYaEtrLTJuOTFNbFozbjF4NEJ1THpGUEJ0YXVMcE1mZW54bHVfNi1SUDB1VnpEakNZODNRcWl0WkM2bmZpei1GRTg2Z2hDamJtMDhPTEFFdUxTS0Fwa09FMTVRcVFIQy1FZGpqNmZqXzVyOA?oc=5>

### Apple Inc. $AAPL Stock Sold by First Pacific Financial
- Summary: Apple Inc. $AAPL Stock Sold by First Pacific Financial
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxOSVpjTlV0OVJLNWVPWGxwNnZKNFlPdjNTQXpHbUdXbHBwY1N6Vl8xamJlQTM5TDhrY3BETG1YemNEZUVpNnVsYmVsWVB3ejkzN2NyVUJIeXFyZlUxQjFCTk1zUmZWQXBwZHhTX2l0bzNMTWhNdl8xakZBNmktRVNkWHZzVl9XZ0FsX1N3dzlTWFpmYUJnUnZuazFaRlMyYTIwVFZfUGxZRk9LVUpKMmdFT0hmOA?oc=5>

### Will Apple (AAPL) Beat Estimates Again in Its Next Earnings Report?
- Summary: Upcoming earnings could exceed expectations, supporting investor confidence.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQdU1HbzlwTm93MndfY1VROENtajdjV2c5UHZ6RWFiaWJlZWRFekFhbTBmRTQzR080aUZFMlBBa3NnRE5jYkN0TTJ3RW5POU5OaVFzWDJmRm5BVU00MnBnNTZKX0ZiLW5CNkZ6a2hkZXV3cXkzZFpqZmJ4S0VxMkRqWXNCWEpZWWhfbFJ3ckhsdllUMVdHX1I5NnNTQUg?oc=5>

### Apple (AAPL) vs. MSFT and GOOGL: Is the Post-Earnings Selloff Creating a Long-Term Buying Opportunity?
- Summary: Analyst questions if recent selloff offers a buying chance for Apple shares.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxOWmtIUVJ6QllHYkFmS3pqMDh6WkR1ZUM0X0QyWll5d0RpMllEeFJrVG1pcl9WdUlyWmtDWkhZbU1HZU1oSF9lVVB2b3R2SHZFNzVPOUFseEhQS1Fqc04xaWlYdE14SUxoYTFyRFYzVjUyUGZ0NE5VMGhBWkZPQzVURV9mcWE1TEU1aFBUakFZU3I1dXc?oc=5>

### Apple (AAPL) Could Be 36% Overvalued As AI Launches Meet iPhone Duo Scrutiny
- Summary: Report suggests Apple may be overvalued amid AI product launch concerns.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOVlREYjhBblZnel80UUYwWHdMeU9UU0ZXeTRaMWhYNk14VUdYZUs0RV9ucHZYc1MwbTM2MG1QQ2NuaENfcFlFWEM2N0RpSTlfYW9aUlBRS2FxUTM4RGtfUVMtSnJULXR6QUk2bGtTN3I2aEVlTlF5ampXT3IwY1lTbEd6LTU2V0FGQ3JaLXJTWjl6OThUd2pIRnIxVQ?oc=5>

### Loop Capital Lowers Apple Stock Price Target on iPhone Shipment Concerns
- Summary: Loop Capital cuts price target due to worries about iPhone shipments.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxOZGptMG9GN3dsVmc1MzZzZHdKQldZMm0wdmVSay01a3FWMURQUEktQ2tGRE9mNGMyb3l2OEVqczhKdTJJRmVFcGYzd1lLQXNaQjJkLWhqZC15SmY0Z1NyT0tNVEFDTE9FeFdqNUZwRFNRTmRKRXRNZTVjSGNaYk9aY19kdXdUamVDZ21RdEl1Q052YVFaNVJDeTVjdDlSeEllTVFLRjhPQUZQVDhIbE85RlBFSVFSUU0?oc=5>

### Apple’s Next Growth Engine Could Change the Stock’s Trajectory
- Summary: Speculation that new growth engine could alter Apple’s stock performance.
- Date: 2026-10-27 | Impact: medium | Horizon: medium | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxPdjN2SHZNOGRURjJUTXRPdkEyNkx2RHVxdXpadWZvVUU1a3FFcXNFYnpjdi1iN1RUVVNCX0FKRkxlbzBpalRiaWhXbXE5bDJMM1FyUkxtUmxBdG5KZkhKRi15Z1c1R0hLSkZMZzZtdWtFWnFJRDlkRC1DLTlBUlNKRnVDcWxRdXVZRlBCd01NSDlVLTZQNF91aWRjTGF1TGVHMDN6MW1UUQ?oc=5>

### What Is Going On With Apple Stock on Tuesday?
- Summary: Investors seek explanation for Apple stock movement on Tuesday.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOVDVmamRlV0sxY1JPSmJJbXRZbGllbGlIUkxzZ09YMzFuSF9WNDRRWlRWYzd4R2l2eERBUlB3R09DaUQ1YmVZOHRYQ3lhXzFRcU9RR2hHTzlRR3ZzX0htTTRoMkgzaGx1TlBSWVBNOUUzTmo2VjVOMlBhU3BQc01XZ0duREstSmZGcFRqRC13cjZCZmtFSmRJWmVBQzZ2dw?oc=5>

## RISKS

### Why Buying Apple Stock Before Q4 Earnings Could Be Risky
- Summary: Investors warned that buying Apple stock before Q4 earnings may expose them to volatility and potential downside, suggesting caution.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOSmRTRXU1S3VTbjVrSVhnMktzbEJDWF9CejhyMktuWXRESEY4b2I4TzlSc0s1V1ZxUWJPVndlNnd5TXR6RlR1Q2xtOFc3aGltSmF4S05LRUVBdWNJWEhzTXIxZkNzUHRSLXFPUWpPMUJrQWc2Szk3YUota2IzWERpYjU0dVVvNk85S3h4RGQwM2RRMDVB?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AAPL** | **39.81** | **47.16** | **30.29** | **16.40** | **5,065,640,247,296.00 USD** | **29.60** |
| MSFT | 29.60 | 8.92 | 20.58 | 17.70 | 3,945,415,311,360.00 USD | 0.79 |
| GOOGL | 16.09 | 6.30 | 22.04 | 24.20 | 3,920,672,325,632.00 USD | 19.36 |
| SONY | 21.19 | 2.85 | 0.12 | 8.20 | 149,733,638,144.00 USD | -10.66 |

Peers fetched as_of: 2026-10-27; AAPL reuses existing data (market data as_of: 2026-10-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-07-30
- Next expected earnings: 2026-11-02 (yfinance; expected dates may change)

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
- Filing date: 2026-07-31
- Revenue (latest available single quarter): 62,900,000,000.00 USD; period 2018-07-01/2018-09-29; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 29,789,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/320193/000032019326000020/aapl-20260627.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMioAFBVV95cUxPMThESjliM3d5eVFiN2Y5X2FjWWNUZGRpWklILWJDVkQ2S056OWVjcGRHOS1nQ3ptSDNqMGlxRGNaVncxMU9QMkVRTk9kNUdoMnMyMEZPOFhUWkw0RlRDU3c3dlY2YllrOWJFTVdpSThkVmozWWlsR1NkSGlDNWNhSkFhb2JDYXJUUnFZUWNGQU41Wkt1OURVV0U2bUpGMl9z?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPNkZWUzFDVnV6dnJSNWxJZzQwWm94bFpsa1lGaXpXR3RGQktsN0JzaVMxZUVkTk56Z0M0cG9KTHFFa2w4QVg0dVF3RjRVYjFNams2NTJreTJsTlNQd1hEMkQxMVBMZ2lxVUxzMV9FZHRnd2oyVlc1eFlUMWdtWFdyamk3Zy14ZzBneFRvSE01YmpiSXFjSXNGTTQybEFFeUE?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQSzJxNGstbU5Fck55X2FMSmViZF9DdTRDSnJINVVVNXhxcnNkc2I5VEcwSEJnWWVqZ2JoZ0pFNVpyci01NkJYOFVjZkZZLVNrTlRZVk1kQzhQRUxXcWFnOFVqN1NVNnhLMC0xcl81dGZWeDRTLW40RHNteVBYbVpkU0tydWhuV0UzS0ZwNWd6S0d0QVFfV1Q2cVRodG5HZw?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxOWXh1UmFwUVNWd3FhWUNKSG13R1BJbHdheXBRNFdGcVFqYnJqc3hWdXE2N2RwUGdlUU1yTXl4X2VSNWNMQUZBQkphR0dsNnV0b2F0SGI3UWRJSk1CMlNBNERCRXhUbkRaaHR2VkViaHQxajBGS09GZXRCdjBxd3c4YVowd1FpWmctTjA4cmJVQ2Q2QVk?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPRm40OVVmVmxpU3Z1alRpUDV2U2wtYmk2enZKQmlkdTNWd0NWbXVvenNremt5RmRodVgtak5JdHdlVUZXQUkxdDRna1dNSDJROEhqWlJvQ0phMTUxcVVJUGxnNFNrSXFvMzBmTGhQWjdfVnAzOGNnYlJGTFFNSk5FTFhpcVQyRy1VdHlPMVB6SDI3QnBUYUFN?oc=5
- https://news.google.com/rss/articles/CBMiUkFVX3lxTE5pbUxLdFVNSjJfVjFOUm9UYmFBYUVBRmV5Q3FJU3lfblNtbVNvZjI4N1hEdlVtTnBMYWRCMi0wUTVTUGdxMUhDb0plLWlmcWdqMEE?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxOMXRnVWdleFY1eTlSWjc2VlM5dlgyc1NqT1hHdklKVng0aXVvT004dVRSTmVfM3dBY3R5RlF4WUNVTjV2bHB3aHpXaFZ0UFZBNjdTR05DV3dSTnNGTDA1dEpYVXZvaGZOLUcydldWNUVpZEo0UkczZWcyM3V1cHBvRGdWQk05aEpMSVJPa1h0YTc2cWlWX1ExR0xENEtjaWRjYzVPZw?oc=5
- https://news.google.com/rss/articles/CBMiekFVX3lxTE42YWZvT3p4TXJERy1HVHRZTTROeWlHWURrY3VnV25CTFpFcTJ4dndMSXR3b3owTW9rTy14eXFTLXNFOGtaV2h3MzFKaFYwMkpJWWV4WnpLaG1iTjI0U0ZMYmtnNTRvUEZIZnhfbnZ3Y01aeHBaUmNlSGJn?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPUG5NM01uN3RIWHlIZkwyTTUzbF9rYjhvOXpMeF9LLU5vSENwYWdta2dfZ2pVdTJCQ0ZSc2RYaEtrLTJuOTFNbFozbjF4NEJ1THpGUEJ0YXVMcE1mZW54bHVfNi1SUDB1VnpEakNZODNRcWl0WkM2bmZpei1GRTg2Z2hDamJtMDhPTEFFdUxTS0Fwa09FMTVRcVFIQy1FZGpqNmZqXzVyOA?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxOSVpjTlV0OVJLNWVPWGxwNnZKNFlPdjNTQXpHbUdXbHBwY1N6Vl8xamJlQTM5TDhrY3BETG1YemNEZUVpNnVsYmVsWVB3ejkzN2NyVUJIeXFyZlUxQjFCTk1zUmZWQXBwZHhTX2l0bzNMTWhNdl8xakZBNmktRVNkWHZzVl9XZ0FsX1N3dzlTWFpmYUJnUnZuazFaRlMyYTIwVFZfUGxZRk9LVUpKMmdFT0hmOA?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQdU1HbzlwTm93MndfY1VROENtajdjV2c5UHZ6RWFiaWJlZWRFekFhbTBmRTQzR080aUZFMlBBa3NnRE5jYkN0TTJ3RW5POU5OaVFzWDJmRm5BVU00MnBnNTZKX0ZiLW5CNkZ6a2hkZXV3cXkzZFpqZmJ4S0VxMkRqWXNCWEpZWWhfbFJ3ckhsdllUMVdHX1I5NnNTQUg?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxOWmtIUVJ6QllHYkFmS3pqMDh6WkR1ZUM0X0QyWll5d0RpMllEeFJrVG1pcl9WdUlyWmtDWkhZbU1HZU1oSF9lVVB2b3R2SHZFNzVPOUFseEhQS1Fqc04xaWlYdE14SUxoYTFyRFYzVjUyUGZ0NE5VMGhBWkZPQzVURV9mcWE1TEU1aFBUakFZU3I1dXc?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOVlREYjhBblZnel80UUYwWHdMeU9UU0ZXeTRaMWhYNk14VUdYZUs0RV9ucHZYc1MwbTM2MG1QQ2NuaENfcFlFWEM2N0RpSTlfYW9aUlBRS2FxUTM4RGtfUVMtSnJULXR6QUk2bGtTN3I2aEVlTlF5ampXT3IwY1lTbEd6LTU2V0FGQ3JaLXJTWjl6OThUd2pIRnIxVQ?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxOZGptMG9GN3dsVmc1MzZzZHdKQldZMm0wdmVSay01a3FWMURQUEktQ2tGRE9mNGMyb3l2OEVqczhKdTJJRmVFcGYzd1lLQXNaQjJkLWhqZC15SmY0Z1NyT0tNVEFDTE9FeFdqNUZwRFNRTmRKRXRNZTVjSGNaYk9aY19kdXdUamVDZ21RdEl1Q052YVFaNVJDeTVjdDlSeEllTVFLRjhPQUZQVDhIbE85RlBFSVFSUU0?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPdjN2SHZNOGRURjJUTXRPdkEyNkx2RHVxdXpadWZvVUU1a3FFcXNFYnpjdi1iN1RUVVNCX0FKRkxlbzBpalRiaWhXbXE5bDJMM1FyUkxtUmxBdG5KZkhKRi15Z1c1R0hLSkZMZzZtdWtFWnFJRDlkRC1DLTlBUlNKRnVDcWxRdXVZRlBCd01NSDlVLTZQNF91aWRjTGF1TGVHMDN6MW1UUQ?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOVDVmamRlV0sxY1JPSmJJbXRZbGllbGlIUkxzZ09YMzFuSF9WNDRRWlRWYzd4R2l2eERBUlB3R09DaUQ1YmVZOHRYQ3lhXzFRcU9RR2hHTzlRR3ZzX0htTTRoMkgzaGx1TlBSWVBNOUUzTmo2VjVOMlBhU3BQc01XZ0duREstSmZGcFRqRC13cjZCZmtFSmRJWmVBQzZ2dw?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOSmRTRXU1S3VTbjVrSVhnMktzbEJDWF9CejhyMktuWXRESEY4b2I4TzlSc0s1V1ZxUWJPVndlNnd5TXR6RlR1Q2xtOFc3aGltSmF4S05LRUVBdWNJWEhzTXIxZkNzUHRSLXFPUWpPMUJrQWc2Szk3YUota2IzWERpYjU0dVVvNk85S3h4RGQwM2RRMDVB?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
