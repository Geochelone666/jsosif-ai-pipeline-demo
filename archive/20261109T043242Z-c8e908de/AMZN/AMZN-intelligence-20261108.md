# AMZN Intelligence Report

- ticker: **AMZN**
- Report as_of: **2026-11-08**
- Market data as_of: **2026-11-06**
- Quant sources: https://finance.yahoo.com/quote/AMZN/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMZN/key-statistics/
- AI analysis snapshot as_of: **2026-11-08**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-09T04:43:48.302840+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 4, 'ai': 15, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **15** exact headline/source/date matches; prior report **20261108T041758Z-43fb2458/AMZN** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **6**; {'directional_claim_without_event_type': 3, 'low_uncalibrated_model_confidence': 3}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 8 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 37.5%; oldest publication 2026-11-02

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 259.3000 |
| Return 1D (%) | -0.3497 |
| Return 1W (%) | 7.8843 |
| Return 1M (%) | 1.1744 |
| Return YTD (%) | 12.3386 |
| Return 1Y (%) | 6.6903 |
| Annualized volatility (%) | 33.8964 |
| Beta vs SPY | 1.3558 |
| Max drawdown (%) | -20.1967 |
| Sharpe (rf=0) | 0.3574 |
| Downside deviation (rf=0, %) | 21.0261 |
| Sortino (rf=0) | 0.5762 |
| Historical VaR 95% (1D, %) | 2.8843 |
| Historical ES 95% (1D, %) | 4.0742 |
| Correlation vs SPY | 0.5420 |
| Tracking error vs SPY (%) | 28.8915 |
| P/E (trailing) | 20.96 |
| P/B | 4.57 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 12.10 |
| Forward P/E (estimate) | 23.78 |
| Gross margin (%) | 51.37 |
| Operating margin (%) | 13.90 |
| Return on equity (%) | 27.42 |
| Free cash flow yield (%) | -1.24 |
| MA50 | 253.9502 |
| Close vs MA50 (%) | 2.1066 |
| MA200 | 243.9401 |
| Close vs MA200 (%) | 6.2966 |
| RSI (14, Wilder) | 54.2213 |
| MACD (12,26) | 0.4931 |
| MACD signal (9) | -0.5257 |
| MACD histogram | 1.0188 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMZN': 277, 'SPY': 277}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 259.3000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.3497 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 7.8843 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 1.1744 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 12.3386 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 6.6903 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 33.8964 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.0261 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.5762 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8843 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.0742 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5420 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 28.8915 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.3558 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -20.1967 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3574 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 23.7810 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 51.3740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 13.9030 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 27.4160 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: -1.2387 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 20.9620 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 54.2213 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.0188 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 2.1066 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 6.2966 -> Clearly above the moving-average trend level.

## TAILWINDS

### Amazon rises 6% as hyperscalers advance on U.S. election results (AMZN:NASDAQ)
- Summary: Amazon rises 6% as hyperscalers advance on U.S. election results (AMZN:NASDAQ)
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQY3dmUWlDazhkTW80ZFYycWlzWkhtZk1USEoxZ0F4MmozdlpQYVdUSWpuMWRYanlhTE5LRTJsNVlWSXNhYS1rZnZTTkRIREJOSFJPRU5HYThpczRIYUR1TUl5TW5nUElhakRtM29Vd2VpTzkzSGVNN3RobXA5cGhDXzBzaTFlTXVnSUhaNWdXODVOTVAtMnhEaHNLSG5PcG9o?oc=5>

### Amazon Leads Cloud Hyperscaler Stocks Higher. What 'Blue Tsunami' Means For Big Tech.
- Summary: Amazon's cloud segment drives hyperscaler stocks higher, signaling strong demand for cloud services.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOc0YzaXo0b2JIcXlEM25sejBneVBlQi1EazRyR0NoVTM5REJ4NjR0WkdKM1k1ckVsZzRTTEFVQ1pSTTJmSDFvWlFERGRDVWp2a1hsRld4dnhjbURqRnJiRENYSzJxM2JuejdFNHVVUnhRLXBnYzdOSm8zSmlTX3pkczlES1hVTnZtZG5vOWYtMTRkWTNDTEE?oc=5>

### What's Going on With Amazon Stock?
- Summary: Analysis of Amazon's current stock performance and future outlook.
- Date: 2026-11-06 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxNaWJ0cmR2Z0JzbnU3MkY4VHFVUm1YSFAxS0ZlT29kbFU3c3hlb01zekw4T3JIUV9veDZXUXdRbVN0OFBhM013dHNBclZwaGszWE11Z2ctb3FMZnh1YlRLNHd3UDZaZ2tmMEdoSU53UUhIb1dyTE8xNnZ3RVVDb21yeG13?oc=5>

### Alphabet, Amazon, and Microsoft All Surged Today. You Can Thank the Big Blue Wave.
- Summary: Amazon shares surged alongside peers, reflecting a positive market wave.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxQS3FPNjF0Qnk2dkx5Z1hfblotbmJudmtpaWF5Zk1vR2xmMHBQLUVMbUVNTC1nQUJfRDVacldTUDllT3lpOHRVSnJCSTB0eEZlV1AycktIdFFNMmF4UVJxa0Z6VExPcFBXUFhKZzNBeUZCMHd4UGhQcjZscVl5blJodFZqSDE4WU82Q3FXTmo2YTdWM0tta01ZREFSbmxBUzdDVVpqaXNLXzM1YmlUaWlLV2RNQXRaVW1GVkJtWjlB?oc=5>

### Why Amazon Stock Can Keep Rising Through 2035
- Summary: Analysts predict Amazon stock growth through 2035 based on long-term trends.
- Date: 2026-11-03 | Impact: high | Horizon: long | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNazhWUG9wbUNZb3hwbGZFSHo2UE5xaG1pSDRqdmdLV1ZEZWZ0aEp4Qk82ZVNWVlpRb0RVZmZpSklWcGFvOFVORmJadUR3bjB5UHNaRllyNi1EZ0NDQ2lZcTg0MjY1Q1YyR0t1R1Z3S0ZVMEN2T3BRR21WdjdDcmJYczhvRVdvSmZhN21DNmxSUTI3MldTQWp5RA?oc=5>

### Amazon.com, Inc. (AMZN) Could Be Entering Its Next Growth Phase: Here’s What Investors Should Know
- Summary: Speculation that Amazon may enter a new growth phase, highlighting potential opportunities for investors.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOQjlDRnhEcEJFTnY0OUtqUXk4VF9CN0VMRDM0b003ZXlTT3FPa1V2cmtXNjJOa21NSnZld3k5UmRoclF5eGtHbUVlQTVtbUlSaGlOdG05cGgxcVBVbWRfbjBoVjFkYnRKY2lVdzZkWUloSm5EcVlyUkN5S0U0MXo0dVJfY20tV0VGU0xIS0gyZjB2UmxC?oc=5>

### Amazon.com, Inc. (AMZN) Stock Forecasts
- Summary: Analysts provide stock price projections for Amazon, offering insight into future valuation expectations.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxQaXpCYmdNMVpuZmhuVk5mbkJqOXdpN2FRZ1NPek03NmlvdUEzY292cXluWk1UZFNwWmM4Vk90Ym1sVDQtRF9DcGNGZ3dpa2lXeVBsc3d2a0V6bWFGR01LMFZ4SHlsd1ZwRXFKODhkMFZjdlNQTXVJZFdUaG92cVhFUTczNFlDSjRfRHl2dQ?oc=5>

## HEADWINDS

### Amazon Teams Up With Uber Eats, Sending DoorDash Stock Tumbling
- Summary: Amazon Teams Up With Uber Eats, Sending DoorDash Stock Tumbling
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxQak45N05SOHFyOEIwLTkxcUV5NXg2OHFSTmttaUVEM3pfWk0wanp1SWxhRjNqVHQwcTFsS2hEaGtMeElOQjFyTmZEazhWVTY4eTRPRU1NRDdzdnFzVUtFUWp0aTc3elhFZTdmUDhQbzBhQkZ0cnNlYm5QV3ljVnVyMFVRa01ibUhyTVE?oc=5>

### Amazon CEO Andy Jassy Says Investors Are ‘Sleeping a Bit’ on Retail as AMZN Stock Falls 7% in 6 Months
- Summary: Amazon CEO Andy Jassy Says Investors Are ‘Sleeping a Bit’ on Retail as AMZN Stock Falls 7% in 6 Months
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNdENRZlJLQWhqdGtGWG9tSDVjX3Bqa2tEenVrYUJaaHBjNXo4RzFDdlM4YjNZSmtiT0h3S0YzVmVxLTBTLXBzcGhlM0ZXaXVSRlBBZmRkUGVyZ1NORS1lQUZWeGdfejh3cnNicWJyVUNjZ2NnM0wyWFk0RW1tdEx4N2diWlUyYkR1aUhLVXdzUnhFT1JWSVE?oc=5>

### Amazon Stock Pulls Back: What's Going On?
- Summary: Amazon shares decline amid market uncertainty, indicating a short‑term headwind.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQZEZIcG9ISmV5RWJCdDNzY2I2ZHBHaE1YckJnV0ZSWm0tZ3V6Q0lJZDlwclF5NGpQX0hvYlcwZmF0cmVMR29qMHhTZjgwZ293Y1ZMT2JfQ1NFd2h0ZU9xUFRlMVJBelk3d0Nqdkh1WVJyODJKVEdKNV9rTGMta19zNll6cXpaa0xhVkNRTloxQ0Y2QjhSN21RZ3FMWTMyMDl4?oc=5>

### AWS Is on Fire, But Here’s Why Amazon Stock Isn’t Ready to Fly
- Summary: Despite AWS growth, concerns about overall stock performance remain.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPcUFMek9tMUZ1ZkMzZzZUZ0lNOVpNZkdfYUpVUERqaDZMNENrWlFFNVowOE9TeWlHeDRxWmtBQlpaYWFXbG9BU2NNVGdmSlZXc2VaS0ZuYWdZZVBLazF0SU84WkgxclRXTjZlc01nS0RfTEdFMkR5UXgxaVh2V05ydWNrZTloWFFNV2M5ZE5aRGpUaUox?oc=5>

### Stock Market Today, Nov. 5: Amazon Shares Slide as Technology Selloff Erases Early Gains
- Summary: Technology selloff pushes Amazon shares lower, a short‑term headwind.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPT1hBWi11VWIxcnd2cDlwR1RaSVhUYnZNLUxnc3hIS0w1cDRPYXJ2R0ItLW9XblVMOHh5cllxeGlBQzlHd3dvelZ5TmJNSmZacDdwTzU4RHpvamJPTkJ2blJaUnlMN0VKVW9uZUlSN01JVnZMVnNlTF9RLTlkbElYUE9aZFp5TlZLNGxDeU1NS3F3M28?oc=5>

## CATALYSTS

### Amazon Stock: Strong Buy Before AWS Growth Rewrites The Earnings Story (NASDAQ:AMZN)
- Summary: Amazon Stock: Strong Buy Before AWS Growth Rewrites The Earnings Story (NASDAQ:AMZN)
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxQQl93OVpSVnlBdHh4UXdoM21WcHVRSFdWc0NDSU1oMXZVcl9QcmEtOHRxa2pOTmxkWFNhN2RjcXMyZTVSX1pYWFhqa0s3Z0xxakQ0eTF2dTBVWDZtZ3lNR2M2emY4eVNlTzJRWkF1OHJsQ1lhcjc4UExBVkdoN3lzd0xkX0ROSzQzcklfLU5JU2NKNE5ELU04U3M0VHNEangzblBmX3Nibw?oc=5>

### Is Amazon Stock Paying You Enough For The Swings?
- Summary: Analysis of Amazon's dividend and volatility for investors.
- Date: 2026-11-07 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxOSnBTWi1kaWtQUW5GY1RLaEVXd2pDVDRCRXFGVFBUS3phanRnSzRKUkNlRWZFaFZWTWZUOWNtZC1XUEZoSHhhSWoyXzl5YXNzNXVyb0Q5WkxncndtaHVSM2dOejJRRlNZX185dUQxOEVqTDdEZGthNGxTZldBQ25obXlLdkpDdTNKa1R5OVh3Rmt2NnNoUHliaHhqTDR3Z1VEczVoRUJtNUtfUHcycEE?oc=5>

### Amazon's CEO Andy Jassy Just Announced Huge News for Amazon Investors
- Summary: CEO Jassy announced significant news for investors.
- Date: 2026-11-06 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPbWRaT1l6VHFoLWlFNThuekNIcllxd2lQbWxZYkM4Qk5EVjNlQ0E4di13cjk4UXQ4YjdnQWRVZjg4ZWpPTGlEeHpJUW40YllHbUxQY09Gb2UzSENJam9KbEJyb3pURzdGZ3ZvbGhwcU1weUFqZk5uTlVaS1FmRHkzWTR1NlVCZEthQWxpWWFZbVdFZ1c2?oc=5>

### Amazon: An Earnings Supercycle Is Taking Shape (NASDAQ:AMZN)
- Summary: Discussion of Amazon's earnings trajectory and potential supercycle.
- Date: 2026-11-05 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxNUzdGZWdCbUVua0h4UVk0TXVuQkE2N2JWR05Sek42bDRFbnlaamFvZ19wV2dFTm1zUzZrYWh2dGpHeDhIX0p4YWJ4VmxkUXpKSDV2bFhONG1pTnh3dmJ3VTRRR2VoNDRMdDNnM24wbUNPMXFJanpDWUJ6dm1ObWkyeURleXhHdzltZDI0TjlRaw?oc=5>

### Forget The Short-Term Noise: This is Where Amazon Will Be in 2028
- Summary: Forecast of Amazon's position in 2028, ignoring short-term fluctuations.
- Date: 2026-11-04 | Impact: low | Horizon: long | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxQRVVYemxVQ25ZWmJLVDBlSjVqYXgyTkVtS1FuOGJlNmRMWDM5NWtTRU41cVN6UFhocV9UMTJCQno3ZVFzc1FxZDJjUWtVQ2V5TXlEQUJtd3F3amV2eFhwcG1Val84d0psTXNnZS00RG9RWUdMNlpubVZpVm11TDFMcVAzRUxPSlVmTWFvUWFHdDFUOFRScXpMSWtNVVlmWjNzNWRtNDU5UG42U1Qt?oc=5>

### Andy Jassy Just Delivered Magnificent News for Amazon Investors
- Summary: Positive guidance or earnings announcement from CEO Andy Jassy, likely boosting investor sentiment.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNb0JESU9yV19hZk8xTWdnWGhRSHppYjlfaU51ajQwd3lHaHdianpsc2YwcWs5dGhnWEk5cjJfaG5ub2tRSm5zWFdDeWRZX2tnZU9UeG96REhhbUxoSjk2VzM5b2h1VVVsSDlFcGpoZFBmNURZaHRldWxEdmZjQWw0WEE0YkIxZWZVVy1xck9FakM2RkFfT205dWM0ZU01NmljVlFPTg?oc=5>

## RISKS

### What Could Derail Amazon Stock?
- Summary: Potential risks to Amazon’s stock identified, indicating a high‑impact headwind.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNc2RSanZyZnEtaHBiMlkzYl83UTRKSlJ1N0VEWDEydTExcnNjSmxGc1JYYXVOV2tzMVF2U0pzaGNfZ2JIOUlJbkRCQUkwUUlrbjRGdHpqMkgwWnlaUWxQd0N6YmNKVzBuWDgyQkpUY3JVeHpMVHNSTTRLUDhZNzdWXzc2YktFOUJjR3J1bl82dmxUT3VWbnc?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMZN** | **20.96** | **4.57** | **N/A** | **12.10** | **2,803,846,610,944.00 USD** | **6.69** |
| WMT | 45.48 | 10.15 | 24.19 | 5.90 | 998,898,073,600.00 USD | 24.49 |
| MSFT | 27.69 | 8.38 | 19.49 | 18.80 | 3,940,412,817,408.00 USD | 7.62 |
| GOOGL | 14.87 | 5.31 | N/A | 24.70 | 3,501,085,163,520.00 USD | 0.27 |

Peers fetched as_of: 2026-11-08; AMZN reuses existing data (market data as_of: 2026-11-06); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-29
- Next expected earnings: 2027-02-04 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-08

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMioAFBVV95cUxQY3dmUWlDazhkTW80ZFYycWlzWkhtZk1USEoxZ0F4MmozdlpQYVdUSWpuMWRYanlhTE5LRTJsNVlWSXNhYS1rZnZTTkRIREJOSFJPRU5HYThpczRIYUR1TUl5TW5nUElhakRtM29Vd2VpTzkzSGVNN3RobXA5cGhDXzBzaTFlTXVnSUhaNWdXODVOTVAtMnhEaHNLSG5PcG9o?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOc0YzaXo0b2JIcXlEM25sejBneVBlQi1EazRyR0NoVTM5REJ4NjR0WkdKM1k1ckVsZzRTTEFVQ1pSTTJmSDFvWlFERGRDVWp2a1hsRld4dnhjbURqRnJiRENYSzJxM2JuejdFNHVVUnhRLXBnYzdOSm8zSmlTX3pkczlES1hVTnZtZG5vOWYtMTRkWTNDTEE?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxNaWJ0cmR2Z0JzbnU3MkY4VHFVUm1YSFAxS0ZlT29kbFU3c3hlb01zekw4T3JIUV9veDZXUXdRbVN0OFBhM013dHNBclZwaGszWE11Z2ctb3FMZnh1YlRLNHd3UDZaZ2tmMEdoSU53UUhIb1dyTE8xNnZ3RVVDb21yeG13?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxQS3FPNjF0Qnk2dkx5Z1hfblotbmJudmtpaWF5Zk1vR2xmMHBQLUVMbUVNTC1nQUJfRDVacldTUDllT3lpOHRVSnJCSTB0eEZlV1AycktIdFFNMmF4UVJxa0Z6VExPcFBXUFhKZzNBeUZCMHd4UGhQcjZscVl5blJodFZqSDE4WU82Q3FXTmo2YTdWM0tta01ZREFSbmxBUzdDVVpqaXNLXzM1YmlUaWlLV2RNQXRaVW1GVkJtWjlB?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNazhWUG9wbUNZb3hwbGZFSHo2UE5xaG1pSDRqdmdLV1ZEZWZ0aEp4Qk82ZVNWVlpRb0RVZmZpSklWcGFvOFVORmJadUR3bjB5UHNaRllyNi1EZ0NDQ2lZcTg0MjY1Q1YyR0t1R1Z3S0ZVMEN2T3BRR21WdjdDcmJYczhvRVdvSmZhN21DNmxSUTI3MldTQWp5RA?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOQjlDRnhEcEJFTnY0OUtqUXk4VF9CN0VMRDM0b003ZXlTT3FPa1V2cmtXNjJOa21NSnZld3k5UmRoclF5eGtHbUVlQTVtbUlSaGlOdG05cGgxcVBVbWRfbjBoVjFkYnRKY2lVdzZkWUloSm5EcVlyUkN5S0U0MXo0dVJfY20tV0VGU0xIS0gyZjB2UmxC?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxQaXpCYmdNMVpuZmhuVk5mbkJqOXdpN2FRZ1NPek03NmlvdUEzY292cXluWk1UZFNwWmM4Vk90Ym1sVDQtRF9DcGNGZ3dpa2lXeVBsc3d2a0V6bWFGR01LMFZ4SHlsd1ZwRXFKODhkMFZjdlNQTXVJZFdUaG92cVhFUTczNFlDSjRfRHl2dQ?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxQak45N05SOHFyOEIwLTkxcUV5NXg2OHFSTmttaUVEM3pfWk0wanp1SWxhRjNqVHQwcTFsS2hEaGtMeElOQjFyTmZEazhWVTY4eTRPRU1NRDdzdnFzVUtFUWp0aTc3elhFZTdmUDhQbzBhQkZ0cnNlYm5QV3ljVnVyMFVRa01ibUhyTVE?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNdENRZlJLQWhqdGtGWG9tSDVjX3Bqa2tEenVrYUJaaHBjNXo4RzFDdlM4YjNZSmtiT0h3S0YzVmVxLTBTLXBzcGhlM0ZXaXVSRlBBZmRkUGVyZ1NORS1lQUZWeGdfejh3cnNicWJyVUNjZ2NnM0wyWFk0RW1tdEx4N2diWlUyYkR1aUhLVXdzUnhFT1JWSVE?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQZEZIcG9ISmV5RWJCdDNzY2I2ZHBHaE1YckJnV0ZSWm0tZ3V6Q0lJZDlwclF5NGpQX0hvYlcwZmF0cmVMR29qMHhTZjgwZ293Y1ZMT2JfQ1NFd2h0ZU9xUFRlMVJBelk3d0Nqdkh1WVJyODJKVEdKNV9rTGMta19zNll6cXpaa0xhVkNRTloxQ0Y2QjhSN21RZ3FMWTMyMDl4?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPcUFMek9tMUZ1ZkMzZzZUZ0lNOVpNZkdfYUpVUERqaDZMNENrWlFFNVowOE9TeWlHeDRxWmtBQlpaYWFXbG9BU2NNVGdmSlZXc2VaS0ZuYWdZZVBLazF0SU84WkgxclRXTjZlc01nS0RfTEdFMkR5UXgxaVh2V05ydWNrZTloWFFNV2M5ZE5aRGpUaUox?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPT1hBWi11VWIxcnd2cDlwR1RaSVhUYnZNLUxnc3hIS0w1cDRPYXJ2R0ItLW9XblVMOHh5cllxeGlBQzlHd3dvelZ5TmJNSmZacDdwTzU4RHpvamJPTkJ2blJaUnlMN0VKVW9uZUlSN01JVnZMVnNlTF9RLTlkbElYUE9aZFp5TlZLNGxDeU1NS3F3M28?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxQQl93OVpSVnlBdHh4UXdoM21WcHVRSFdWc0NDSU1oMXZVcl9QcmEtOHRxa2pOTmxkWFNhN2RjcXMyZTVSX1pYWFhqa0s3Z0xxakQ0eTF2dTBVWDZtZ3lNR2M2emY4eVNlTzJRWkF1OHJsQ1lhcjc4UExBVkdoN3lzd0xkX0ROSzQzcklfLU5JU2NKNE5ELU04U3M0VHNEangzblBmX3Nibw?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxOSnBTWi1kaWtQUW5GY1RLaEVXd2pDVDRCRXFGVFBUS3phanRnSzRKUkNlRWZFaFZWTWZUOWNtZC1XUEZoSHhhSWoyXzl5YXNzNXVyb0Q5WkxncndtaHVSM2dOejJRRlNZX185dUQxOEVqTDdEZGthNGxTZldBQ25obXlLdkpDdTNKa1R5OVh3Rmt2NnNoUHliaHhqTDR3Z1VEczVoRUJtNUtfUHcycEE?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPbWRaT1l6VHFoLWlFNThuekNIcllxd2lQbWxZYkM4Qk5EVjNlQ0E4di13cjk4UXQ4YjdnQWRVZjg4ZWpPTGlEeHpJUW40YllHbUxQY09Gb2UzSENJam9KbEJyb3pURzdGZ3ZvbGhwcU1weUFqZk5uTlVaS1FmRHkzWTR1NlVCZEthQWxpWWFZbVdFZ1c2?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxNUzdGZWdCbUVua0h4UVk0TXVuQkE2N2JWR05Sek42bDRFbnlaamFvZ19wV2dFTm1zUzZrYWh2dGpHeDhIX0p4YWJ4VmxkUXpKSDV2bFhONG1pTnh3dmJ3VTRRR2VoNDRMdDNnM24wbUNPMXFJanpDWUJ6dm1ObWkyeURleXhHdzltZDI0TjlRaw?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxQRVVYemxVQ25ZWmJLVDBlSjVqYXgyTkVtS1FuOGJlNmRMWDM5NWtTRU41cVN6UFhocV9UMTJCQno3ZVFzc1FxZDJjUWtVQ2V5TXlEQUJtd3F3amV2eFhwcG1Val84d0psTXNnZS00RG9RWUdMNlpubVZpVm11TDFMcVAzRUxPSlVmTWFvUWFHdDFUOFRScXpMSWtNVVlmWjNzNWRtNDU5UG42U1Qt?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNb0JESU9yV19hZk8xTWdnWGhRSHppYjlfaU51ajQwd3lHaHdianpsc2YwcWs5dGhnWEk5cjJfaG5ub2tRSm5zWFdDeWRZX2tnZU9UeG96REhhbUxoSjk2VzM5b2h1VVVsSDlFcGpoZFBmNURZaHRldWxEdmZjQWw0WEE0YkIxZWZVVy1xck9FakM2RkFfT205dWM0ZU01NmljVlFPTg?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNc2RSanZyZnEtaHBiMlkzYl83UTRKSlJ1N0VEWDEydTExcnNjSmxGc1JYYXVOV2tzMVF2U0pzaGNfZ2JIOUlJbkRCQUkwUUlrbjRGdHpqMkgwWnlaUWxQd0N6YmNKVzBuWDgyQkpUY3JVeHpMVHNSTTRLUDhZNzdWXzc2YktFOUJjR3J1bl82dmxUT3VWbnc?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
