# AMZN Intelligence Report

- ticker: **AMZN**
- Report as_of: **2026-11-05**
- Market data as_of: **2026-11-05**
- Quant sources: https://finance.yahoo.com/quote/AMZN/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMZN/key-statistics/
- AI analysis snapshot as_of: **2026-11-05**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-06T05:13:37.655416+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 7, 'ai': 11, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261105T045846Z-bde0a1fe/AMZN** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 12 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 39.13%; oldest publication 2026-10-30

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 260.2100 |
| Return 1D (%) | -2.1877 |
| Return 1W (%) | 6.7353 |
| Return 1M (%) | 3.5044 |
| Return YTD (%) | 12.7329 |
| Return 1Y (%) | 4.0008 |
| Annualized volatility (%) | 34.0194 |
| Beta vs SPY | 1.3654 |
| Max drawdown (%) | -20.5476 |
| Sharpe (rf=0) | 0.2820 |
| Downside deviation (rf=0, %) | 21.2178 |
| Sortino (rf=0) | 0.4521 |
| Historical VaR 95% (1D, %) | 2.9597 |
| Historical ES 95% (1D, %) | 4.0742 |
| Correlation vs SPY | 0.5456 |
| Tracking error vs SPY (%) | 28.9396 |
| P/E (trailing) | 21.50 |
| P/B | 4.58 |
| EV/EBITDA | 16.35 |
| Revenue growth (%) | 12.10 |
| Forward P/E (estimate) | 23.84 |
| Gross margin (%) | 51.37 |
| Operating margin (%) | 13.90 |
| Return on equity (%) | 27.42 |
| Free cash flow yield (%) | -1.23 |
| MA50 | 253.8894 |
| Close vs MA50 (%) | 2.4895 |
| MA200 | 243.8154 |
| Close vs MA200 (%) | 6.7242 |
| RSI (14, Wilder) | 54.9692 |
| MACD (12,26) | 0.0487 |
| MACD signal (9) | -0.7804 |
| MACD histogram | 0.8291 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMZN': 276, 'SPY': 276}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 260.2100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.1877 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 6.7353 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 3.5044 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 12.7329 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 4.0008 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 34.0194 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.2178 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4521 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9597 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.0742 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5456 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 28.9396 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.3654 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -20.5476 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2820 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 23.8384 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 51.3740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 13.9030 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 27.4160 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: -1.2344 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 21.5050 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 54.9692 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.8291 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 2.4895 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 6.7242 -> Clearly above the moving-average trend level.

## TAILWINDS

### Amazon (NASDAQ:AMZN) Stock Rallies as Wall Street ‘Buy’ Upgrade Highlights 39% AWS Growth
- Summary: Amazon (NASDAQ:AMZN) Stock Rallies as Wall Street ‘Buy’ Upgrade Highlights 39% AWS Growth
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMieEFVX3lxTE5TRVJ2ODRjSDRoWUtreUFjYkJONzY4VFMyUE5GVy0zaS1lcHFVaFpOQnlkTVFXTkhTYWVIRFNJZUlIbjNUcEhjbWFfTHlRVGp3WFE1algzZzdNTVJ1amVaX2syM0piLWI1VEJPTS05OVNNbU5aZjBNZg?oc=5>

### Amazon rises 6% as hyperscalers advance on U.S. election results (AMZN:NASDAQ)
- Summary: Amazon rises 6% as hyperscalers advance on U.S. election results (AMZN:NASDAQ)
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQY3dmUWlDazhkTW80ZFYycWlzWkhtZk1USEoxZ0F4MmozdlpQYVdUSWpuMWRYanlhTE5LRTJsNVlWSXNhYS1rZnZTTkRIREJOSFJPRU5HYThpczRIYUR1TUl5TW5nUElhakRtM29Vd2VpTzkzSGVNN3RobXA5cGhDXzBzaTFlTXVnSUhaNWdXODVOTVAtMnhEaHNLSG5PcG9o?oc=5>

### Amazon Stock Rises: What's Going On?
- Summary: Amazon Stock Rises: What's Going On?
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQQlg2eVlHWDl0QUpwa3MtZ2JBVUVMOXd6Y0xzSlNSRTMyRGl2SmRRZEhQNTRsS01vellzQ3NvSm1GYUNNbmZiRUlaOTYwaHFuejRiajNOTmxLS2lJT1J1Sld6NXp2ajRMUlRheHcxckw1OHhHdVFHSW9fYnVXdkVWNmdFeGI5UFh5OS1CM2VUQ05KODhXZlhvSTJR?oc=5>

### Amazon Leads Cloud Hyperscaler Stocks Higher. What 'Blue Tsunami' Means For Big Tech.
- Summary: Amazon's cloud segment drives hyperscaler stocks higher, signaling strong demand for cloud services.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOc0YzaXo0b2JIcXlEM25sejBneVBlQi1EazRyR0NoVTM5REJ4NjR0WkdKM1k1ckVsZzRTTEFVQ1pSTTJmSDFvWlFERGRDVWp2a1hsRld4dnhjbURqRnJiRENYSzJxM2JuejdFNHVVUnhRLXBnYzdOSm8zSmlTX3pkczlES1hVTnZtZG5vOWYtMTRkWTNDTEE?oc=5>

### Alphabet, Amazon, and Microsoft All Surged Today. You Can Thank the Big Blue Wave.
- Summary: Amazon shares surged alongside peers, reflecting a positive market wave.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxQS3FPNjF0Qnk2dkx5Z1hfblotbmJudmtpaWF5Zk1vR2xmMHBQLUVMbUVNTC1nQUJfRDVacldTUDllT3lpOHRVSnJCSTB0eEZlV1AycktIdFFNMmF4UVJxa0Z6VExPcFBXUFhKZzNBeUZCMHd4UGhQcjZscVl5blJodFZqSDE4WU82Q3FXTmo2YTdWM0tta01ZREFSbmxBUzdDVVpqaXNLXzM1YmlUaWlLV2RNQXRaVW1GVkJtWjlB?oc=5>

### Amazon (AMZN) Stock After Q3 Earnings: Buy the Dip, Sell, or Hold?
- Summary: Analyst offers buy/dip/sell/hold guidance post Q3 earnings.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxNZTRnSk1vYUtiQlJ0YVdWUEVMQm5mMFZfbjc0T1hwZDFLUjR5THFrbTFzanhGNUhIYV8wV2Vpa2FRTXFRcTRsanphR1ZSS1lHMjQ3QkoxVlhYSmo3QkFWS29fa1VHaHlMVVpCV21GcFpaQVBaLXhvd0wzbWFSRFZTNG5rdnVfM3lOTnVBaHVWSmU4MlIwYzI0WU8teXN0WTl5Q0pJ?oc=5>

## HEADWINDS

### Amazon Teams Up With Uber Eats, Sending DoorDash Stock Tumbling
- Summary: Amazon Teams Up With Uber Eats, Sending DoorDash Stock Tumbling
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxQak45N05SOHFyOEIwLTkxcUV5NXg2OHFSTmttaUVEM3pfWk0wanp1SWxhRjNqVHQwcTFsS2hEaGtMeElOQjFyTmZEazhWVTY4eTRPRU1NRDdzdnFzVUtFUWp0aTc3elhFZTdmUDhQbzBhQkZ0cnNlYm5QV3ljVnVyMFVRa01ibUhyTVE?oc=5>

### Amazon Stock Fell After Earnings. Jim Cramer Says Buy Right Here
- Summary: Amazon Stock Fell After Earnings. Jim Cramer Says Buy Right Here
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQdVZfYkpFaURIalAwZHlsWjJ0RGJlekJJNjBUWFEtbThRUkhxQVpFMk5ieENxZzNFZlpOd2s0VG5TSkpHaE5hS190bXMtb2JkeGQyRkJ5Z2JOcnE3UEdBUUFhVmRQMzFQQlVXcVBEUDdEczUyZllrUUtoV2JxTE9QS1ZLUmVtSmk0RmhMcmMwTEtaZmxaV2M1T0VOdw?oc=5>

### Amazon (AMZN) Stock Slips As Q3 Earnings Reflect Profit Reset
- Summary: Amazon (AMZN) Stock Slips As Q3 Earnings Reflect Profit Reset
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOMHVOOUNrejV0ZnJZZFhTWGhHRDFVN2hwd2djSHZDbFR0aHZhdlVZSy1rcWN5eVJzYWlJRURXN013em1KVS1lNkNVQ0wybEllb0h0dnZHajhYUjhKTFIzQjZMS2ZYb0FJQm5kcjVmOGNBOFllYWYyT2hXTVh1cmFoY1d6eENfak9XcUpCekdxSHZyaDMyQ2c?oc=5>

### Amazon CEO Andy Jassy Says Investors Are ‘Sleeping a Bit’ on Retail as AMZN Stock Falls 7% in 6 Months
- Summary: Amazon CEO Andy Jassy Says Investors Are ‘Sleeping a Bit’ on Retail as AMZN Stock Falls 7% in 6 Months
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNdENRZlJLQWhqdGtGWG9tSDVjX3Bqa2tEenVrYUJaaHBjNXo4RzFDdlM4YjNZSmtiT0h3S0YzVmVxLTBTLXBzcGhlM0ZXaXVSRlBBZmRkUGVyZ1NORS1lQUZWeGdfejh3cnNicWJyVUNjZ2NnM0wyWFk0RW1tdEx4N2diWlUyYkR1aUhLVXdzUnhFT1JWSVE?oc=5>

### Amazon Stock Pulls Back: What's Going On?
- Summary: Amazon shares decline amid market uncertainty, indicating a short‑term headwind.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQZEZIcG9ISmV5RWJCdDNzY2I2ZHBHaE1YckJnV0ZSWm0tZ3V6Q0lJZDlwclF5NGpQX0hvYlcwZmF0cmVMR29qMHhTZjgwZ293Y1ZMT2JfQ1NFd2h0ZU9xUFRlMVJBelk3d0Nqdkh1WVJyODJKVEdKNV9rTGMta19zNll6cXpaa0xhVkNRTloxQ0Y2QjhSN21RZ3FMWTMyMDl4?oc=5>

### AWS Is on Fire, But Here’s Why Amazon Stock Isn’t Ready to Fly
- Summary: Strong AWS growth contrasts with broader stock weakness, creating a short‑term headwind.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNbGh3SFg5TlU5Q1ZwTEZYbVlCbHQtVDJfVkI5SzBTbHBkZVRvUXhRTlR3V1Rzak1ydTBDYUJSZmhtOVVOT0ctbGZkUzJwWFpEejMxaURZdnVkbzZpcmIzSDlyZHhJd1dQWUFlanVkalVIVmg5eWJRZHVzM1BEWEgyMDNXNnRJZW5NaGdqaE1KUHFvS29GdzZLSVU5Z3NDVXJwS01Zam5n?oc=5>

### Stock Market Today, Nov. 5: Amazon Shares Slide as Technology Selloff Erases Early Gains
- Summary: Technology selloff pushes Amazon shares lower, a short‑term headwind.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPT1hBWi11VWIxcnd2cDlwR1RaSVhUYnZNLUxnc3hIS0w1cDRPYXJ2R0ItLW9XblVMOHh5cllxeGlBQzlHd3dvelZ5TmJNSmZacDdwTzU4RHpvamJPTkJ2blJaUnlMN0VKVW9uZUlSN01JVnZMVnNlTF9RLTlkbElYUE9aZFp5TlZLNGxDeU1NS3F3M28?oc=5>

## CATALYSTS

### Amazon.com, Inc. (AMZN) Could Be Entering Its Next Growth Phase: Here’s What Investors Should Know
- Summary: Potential new growth phase for Amazon discussed.
- Date: 2026-11-03 | Impact: high | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOQjlDRnhEcEJFTnY0OUtqUXk4VF9CN0VMRDM0b003ZXlTT3FPa1V2cmtXNjJOa21NSnZld3k5UmRoclF5eGtHbUVlQTVtbUlSaGlOdG05cGgxcVBVbWRfbjBoVjFkYnRKY2lVdzZkWUloSm5EcVlyUkN5S0U0MXo0dVJfY20tV0VGU0xIS0gyZjB2UmxC?oc=5>

### Andy Jassy Just Delivered Magnificent News for Amazon Investors
- Summary: Amazon CEO announces positive outlook and strategic initiatives, boosting investor confidence.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNb0JESU9yV19hZk8xTWdnWGhRSHppYjlfaU51ajQwd3lHaHdianpsc2YwcWs5dGhnWEk5cjJfaG5ub2tRSm5zWFdDeWRZX2tnZU9UeG96REhhbUxoSjk2VzM5b2h1VVVsSDlFcGpoZFBmNURZaHRldWxEdmZjQWw0WEE0YkIxZWZVVy1xck9FakM2RkFfT205dWM0ZU01NmljVlFPTg?oc=5>

### Amazon: An Earnings Supercycle Is Taking Shape (NASDAQ:AMZN)
- Summary: Analysis suggests Amazon may enter a prolonged earnings growth period.
- Date: 2026-11-05 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxNUzdGZWdCbUVua0h4UVk0TXVuQkE2N2JWR05Sek42bDRFbnlaamFvZ19wV2dFTm1zUzZrYWh2dGpHeDhIX0p4YWJ4VmxkUXpKSDV2bFhONG1pTnh3dmJ3VTRRR2VoNDRMdDNnM24wbUNPMXFJanpDWUJ6dm1ObWkyeURleXhHdzltZDI0TjlRaw?oc=5>

### Tech Stocks Surge Post-Election: Amazon (AMZN) and Microsoft (MS
- Summary: Broad tech rally post-election lifts Amazon shares.
- Date: 2026-11-05 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQbXJONV9YbzcxT1dxemxsSHhxQTdGUGx5NmFKWkVDT3ZmWDNubHRVdVdYdWM1QXU3dC1PbnhWdkx5SnQ1WTFJa2dEZzd6MnFRblVvV0NreGhlVHVIV0tCN0xfZjhYUnJGTVJHWE9MMEpndEIyT19kSVQ3R2drb1hxOGpqU1lUZTdqYUR2XzVPQ0JNNWZqcHJvRmRnMDRrRkVCNXVwMzd5c1F2NGpxRVVyeQ?oc=5>

## RISKS

### What Could Derail Amazon Stock?
- Summary: Potential risks to Amazon’s stock identified, indicating a high‑impact headwind.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNc2RSanZyZnEtaHBiMlkzYl83UTRKSlJ1N0VEWDEydTExcnNjSmxGc1JYYXVOV2tzMVF2U0pzaGNfZ2JIOUlJbkRCQUkwUUlrbjRGdHpqMkgwWnlaUWxQd0N6YmNKVzBuWDgyQkpUY3JVeHpMVHNSTTRLUDhZNzdWXzc2YktFOUJjR3J1bl82dmxUT3VWbnc?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMZN** | **21.50** | **4.58** | **16.35** | **12.10** | **2,813,686,448,128.00 USD** | **4.00** |
| WMT | 46.78 | 10.33 | 24.58 | 5.90 | 1,016,405,884,928.00 USD | 26.93 |
| MSFT | 29.00 | 8.46 | 19.69 | 18.80 | 3,979,920,277,504.00 USD | 6.54 |
| GOOGL | 15.09 | 5.27 | 18.20 | 24.70 | 3,473,915,510,784.00 USD | -0.35 |

Peers fetched as_of: 2026-11-05; AMZN reuses existing data (market data as_of: 2026-11-05); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-29
- Next expected earnings: 2027-02-04 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-05

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-30
- Revenue (latest available single quarter): 201,944,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 20,685,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMieEFVX3lxTE5TRVJ2ODRjSDRoWUtreUFjYkJONzY4VFMyUE5GVy0zaS1lcHFVaFpOQnlkTVFXTkhTYWVIRFNJZUlIbjNUcEhjbWFfTHlRVGp3WFE1algzZzdNTVJ1amVaX2syM0piLWI1VEJPTS05OVNNbU5aZjBNZg?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQY3dmUWlDazhkTW80ZFYycWlzWkhtZk1USEoxZ0F4MmozdlpQYVdUSWpuMWRYanlhTE5LRTJsNVlWSXNhYS1rZnZTTkRIREJOSFJPRU5HYThpczRIYUR1TUl5TW5nUElhakRtM29Vd2VpTzkzSGVNN3RobXA5cGhDXzBzaTFlTXVnSUhaNWdXODVOTVAtMnhEaHNLSG5PcG9o?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQQlg2eVlHWDl0QUpwa3MtZ2JBVUVMOXd6Y0xzSlNSRTMyRGl2SmRRZEhQNTRsS01vellzQ3NvSm1GYUNNbmZiRUlaOTYwaHFuejRiajNOTmxLS2lJT1J1Sld6NXp2ajRMUlRheHcxckw1OHhHdVFHSW9fYnVXdkVWNmdFeGI5UFh5OS1CM2VUQ05KODhXZlhvSTJR?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOc0YzaXo0b2JIcXlEM25sejBneVBlQi1EazRyR0NoVTM5REJ4NjR0WkdKM1k1ckVsZzRTTEFVQ1pSTTJmSDFvWlFERGRDVWp2a1hsRld4dnhjbURqRnJiRENYSzJxM2JuejdFNHVVUnhRLXBnYzdOSm8zSmlTX3pkczlES1hVTnZtZG5vOWYtMTRkWTNDTEE?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxQS3FPNjF0Qnk2dkx5Z1hfblotbmJudmtpaWF5Zk1vR2xmMHBQLUVMbUVNTC1nQUJfRDVacldTUDllT3lpOHRVSnJCSTB0eEZlV1AycktIdFFNMmF4UVJxa0Z6VExPcFBXUFhKZzNBeUZCMHd4UGhQcjZscVl5blJodFZqSDE4WU82Q3FXTmo2YTdWM0tta01ZREFSbmxBUzdDVVpqaXNLXzM1YmlUaWlLV2RNQXRaVW1GVkJtWjlB?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxNZTRnSk1vYUtiQlJ0YVdWUEVMQm5mMFZfbjc0T1hwZDFLUjR5THFrbTFzanhGNUhIYV8wV2Vpa2FRTXFRcTRsanphR1ZSS1lHMjQ3QkoxVlhYSmo3QkFWS29fa1VHaHlMVVpCV21GcFpaQVBaLXhvd0wzbWFSRFZTNG5rdnVfM3lOTnVBaHVWSmU4MlIwYzI0WU8teXN0WTl5Q0pJ?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxQak45N05SOHFyOEIwLTkxcUV5NXg2OHFSTmttaUVEM3pfWk0wanp1SWxhRjNqVHQwcTFsS2hEaGtMeElOQjFyTmZEazhWVTY4eTRPRU1NRDdzdnFzVUtFUWp0aTc3elhFZTdmUDhQbzBhQkZ0cnNlYm5QV3ljVnVyMFVRa01ibUhyTVE?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQdVZfYkpFaURIalAwZHlsWjJ0RGJlekJJNjBUWFEtbThRUkhxQVpFMk5ieENxZzNFZlpOd2s0VG5TSkpHaE5hS190bXMtb2JkeGQyRkJ5Z2JOcnE3UEdBUUFhVmRQMzFQQlVXcVBEUDdEczUyZllrUUtoV2JxTE9QS1ZLUmVtSmk0RmhMcmMwTEtaZmxaV2M1T0VOdw?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOMHVOOUNrejV0ZnJZZFhTWGhHRDFVN2hwd2djSHZDbFR0aHZhdlVZSy1rcWN5eVJzYWlJRURXN013em1KVS1lNkNVQ0wybEllb0h0dnZHajhYUjhKTFIzQjZMS2ZYb0FJQm5kcjVmOGNBOFllYWYyT2hXTVh1cmFoY1d6eENfak9XcUpCekdxSHZyaDMyQ2c?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNdENRZlJLQWhqdGtGWG9tSDVjX3Bqa2tEenVrYUJaaHBjNXo4RzFDdlM4YjNZSmtiT0h3S0YzVmVxLTBTLXBzcGhlM0ZXaXVSRlBBZmRkUGVyZ1NORS1lQUZWeGdfejh3cnNicWJyVUNjZ2NnM0wyWFk0RW1tdEx4N2diWlUyYkR1aUhLVXdzUnhFT1JWSVE?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQZEZIcG9ISmV5RWJCdDNzY2I2ZHBHaE1YckJnV0ZSWm0tZ3V6Q0lJZDlwclF5NGpQX0hvYlcwZmF0cmVMR29qMHhTZjgwZ293Y1ZMT2JfQ1NFd2h0ZU9xUFRlMVJBelk3d0Nqdkh1WVJyODJKVEdKNV9rTGMta19zNll6cXpaa0xhVkNRTloxQ0Y2QjhSN21RZ3FMWTMyMDl4?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNbGh3SFg5TlU5Q1ZwTEZYbVlCbHQtVDJfVkI5SzBTbHBkZVRvUXhRTlR3V1Rzak1ydTBDYUJSZmhtOVVOT0ctbGZkUzJwWFpEejMxaURZdnVkbzZpcmIzSDlyZHhJd1dQWUFlanVkalVIVmg5eWJRZHVzM1BEWEgyMDNXNnRJZW5NaGdqaE1KUHFvS29GdzZLSVU5Z3NDVXJwS01Zam5n?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPT1hBWi11VWIxcnd2cDlwR1RaSVhUYnZNLUxnc3hIS0w1cDRPYXJ2R0ItLW9XblVMOHh5cllxeGlBQzlHd3dvelZ5TmJNSmZacDdwTzU4RHpvamJPTkJ2blJaUnlMN0VKVW9uZUlSN01JVnZMVnNlTF9RLTlkbElYUE9aZFp5TlZLNGxDeU1NS3F3M28?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOQjlDRnhEcEJFTnY0OUtqUXk4VF9CN0VMRDM0b003ZXlTT3FPa1V2cmtXNjJOa21NSnZld3k5UmRoclF5eGtHbUVlQTVtbUlSaGlOdG05cGgxcVBVbWRfbjBoVjFkYnRKY2lVdzZkWUloSm5EcVlyUkN5S0U0MXo0dVJfY20tV0VGU0xIS0gyZjB2UmxC?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNb0JESU9yV19hZk8xTWdnWGhRSHppYjlfaU51ajQwd3lHaHdianpsc2YwcWs5dGhnWEk5cjJfaG5ub2tRSm5zWFdDeWRZX2tnZU9UeG96REhhbUxoSjk2VzM5b2h1VVVsSDlFcGpoZFBmNURZaHRldWxEdmZjQWw0WEE0YkIxZWZVVy1xck9FakM2RkFfT205dWM0ZU01NmljVlFPTg?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQelVMSUtLR01QSHNWZUkzd0pLY0lKcTlOUnhia2xSLXIxZnhJSzhaVXNJV0ltaTBaMERGZFBKRlhWQV9adG5LNUt1MUVPMXZnMzZiUGo1MlpYSmdOeVVfYXd6OUx5SHgxYzJZdHVkVVNpcDdxVlBGZnNBZ25WOE9JN2RyS1g3RTg4SHIxaDlYWUhTdWRj?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxNUzdGZWdCbUVua0h4UVk0TXVuQkE2N2JWR05Sek42bDRFbnlaamFvZ19wV2dFTm1zUzZrYWh2dGpHeDhIX0p4YWJ4VmxkUXpKSDV2bFhONG1pTnh3dmJ3VTRRR2VoNDRMdDNnM24wbUNPMXFJanpDWUJ6dm1ObWkyeURleXhHdzltZDI0TjlRaw?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxQbXJONV9YbzcxT1dxemxsSHhxQTdGUGx5NmFKWkVDT3ZmWDNubHRVdVdYdWM1QXU3dC1PbnhWdkx5SnQ1WTFJa2dEZzd6MnFRblVvV0NreGhlVHVIV0tCN0xfZjhYUnJGTVJHWE9MMEpndEIyT19kSVQ3R2drb1hxOGpqU1lUZTdqYUR2XzVPQ0JNNWZqcHJvRmRnMDRrRkVCNXVwMzd5c1F2NGpxRVVyeQ?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNc2RSanZyZnEtaHBiMlkzYl83UTRKSlJ1N0VEWDEydTExcnNjSmxGc1JYYXVOV2tzMVF2U0pzaGNfZ2JIOUlJbkRCQUkwUUlrbjRGdHpqMkgwWnlaUWxQd0N6YmNKVzBuWDgyQkpUY3JVeHpMVHNSTTRLUDhZNzdWXzc2YktFOUJjR3J1bl82dmxUT3VWbnc?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
