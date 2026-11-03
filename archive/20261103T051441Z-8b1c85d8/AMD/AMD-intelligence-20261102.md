# AMD Intelligence Report

- ticker: **AMD**
- Report as_of: **2026-11-02**
- Market data as_of: **2026-11-02**
- Quant sources: https://finance.yahoo.com/quote/AMD/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMD/key-statistics/
- AI analysis snapshot as_of: **2026-11-02**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-03T05:30:58.880000+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 5, 'ai': 16, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261102T041627Z-c84a7052/AMD** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 15 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-10-30

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 466.8400 |
| Return 1D (%) | -7.5198 |
| Return 1W (%) | -12.1292 |
| Return 1M (%) | -26.3555 |
| Return YTD (%) | 117.9865 |
| Return 1Y (%) | 82.2739 |
| Annualized volatility (%) | 69.6153 |
| Beta vs SPY | 3.3277 |
| Max drawdown (%) | -28.1143 |
| Sharpe (rf=0) | 1.1951 |
| Downside deviation (rf=0, %) | 44.7967 |
| Sortino (rf=0) | 1.8572 |
| Historical VaR 95% (1D, %) | 6.3376 |
| Historical ES 95% (1D, %) | 8.7057 |
| Correlation vs SPY | 0.6129 |
| Tracking error vs SPY (%) | 62.5822 |
| P/E (trailing) | 119.09 |
| P/B | 11.33 |
| EV/EBITDA | 78.78 |
| Revenue growth (%) | 50.10 |
| Forward P/E (estimate) | 29.16 |
| Gross margin (%) | 55.72 |
| Operating margin (%) | 17.25 |
| Return on equity (%) | 10.20 |
| Free cash flow yield (%) | 1.16 |
| MA50 | 548.1620 |
| Close vs MA50 (%) | -14.8354 |
| MA200 | 411.6833 |
| Close vs MA200 (%) | 13.3978 |
| RSI (14, Wilder) | 34.6087 |
| MACD (12,26) | -14.9755 |
| MACD signal (9) | -6.2238 |
| MACD histogram | -8.7517 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMD': 273, 'SPY': 273}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 466.8400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -7.5198 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -12.1292 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -26.3555 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 117.9865 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 82.2739 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 69.6153 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 44.7967 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.8572 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 6.3376 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 8.7057 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6129 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 62.5822 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.3277 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.1143 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1951 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 29.1588 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 55.7240 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 17.2500 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 10.1960 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.1601 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 119.0918 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 34.6087 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -8.7517 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -14.8354 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 13.3978 -> Clearly above the moving-average trend level.

## TAILWINDS

### AMD Q3 Preview: Expert Says ‘Growth Story Remains Impressive,’ Can Earnings Send Stock Back to Highs?
- Summary: Positive analyst outlook on Q3 earnings, suggesting potential upside for AMD stock.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi4wFBVV95cUxPYmpQbzdwSUE4a2NJZmpKQ0lGaE1PUHRvbk9MZmlGT2w2WHg3M1NtSGcyMlpJdjZ0OFE5NDJyQUpsSGdnLWlVaC1TRDlDdThtZmZZaTVVcnQ1MlNiS09BM1NuTWViM1NqN0ZFX2c0bGRsNkdjaV9Tb18tbzBYX3JjN3lkQm9IR3EwWXRZblNlcl8wZ2hqd3dTejJ3ZXZGN2R5emZ3ZFRaSGdlR3RCcWpYMEFtTDVmcUh0NUV2bWdCamhEb01fSjRIQUh5aG5NdkhLTW15ZkgxbnBpdFNaeFQ1R1BLaw?oc=5>

### AMD Stock $511 Before Results: Options Price a 9% Move
- Summary: Options pricing indicates market anticipation of earnings, reflecting moderate bullish sentiment.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxQbUtyekwxWHBFN3NCTFRGcXlJa0UzdzNSZzR5M1BiUmNIN3JXMFRvQVhLNkZ2Z3gyaEV0bXdKS05mSFdxN3N1X1ZsbkJxLXhQYzFfT0NSbXJWZGR5aXFRSnYxVkx3c0N4TmFIWGd3S2h0ZXNqYmp0dDZBZ3kySF9kVGRyQ3cybnRMbHRYZFo2LTlOSmF4N01WSTlGXzNyeEl6azhCaDM3cThLUkY0NjZycThYVU1VZUI2VHlOVzNjYXVfRDZleUE?oc=5>

### 23 Big Funds Bought Advanced Micro Devices Last Quarter. Is It a Buy Before Earnings?
- Summary: Large institutional purchases suggest confidence ahead of earnings.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.92
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPNWpNdV9aMks3Sk92V3U0akxMZXdBOGxuemtvR3JZNldrU0FIcjVPODhyNlY5ZzRDNnJxS1U1VUQ2QnFlNnlNeGdPdjNObVFCbkktZnp2bzgzMk52TnBrRW5oT2RFNy1HYmRkZVBlYVV4b0g4ZG51WTZscGRtbHlXUFFwdno4dnpfWWY5Ui1iSHAyakxqTkM0VQ?oc=5>

## HEADWINDS

### Advanced Micro Devices (NASDAQ:AMD) Shares Down 7.5% - Here's Why
- Summary: Advanced Micro Devices (NASDAQ:AMD) Shares Down 7.5% - Here's Why
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxPa2JFaWNkdFBCSzNCMEMtRU51R09XWTRBMm1IMVdMM1NnX0N0LW13QURpUm5JaEZQazJfR19PWXV1UHJOQnlkUGlLbldVb3hSTG1GWXZlYkNxZ1Z6QmRHVGl3LTFnYUMxZnFtYUFuVlBXU0pRbnlCSGRMSFp4RW1nSXI1ekE1RzFKa2psSjBXYWszQXByMV9GbzhUVmVvMmUtamJtVndxOUlEOW9ubE5wVzlOanAtYWx1a3c?oc=5>

### AMD Stock Got Caught in Intel’s Selloff. What to Watch This Week.
- Summary: AMD Stock Got Caught in Intel’s Selloff. What to Watch This Week.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxOQ0dnXzRmUWRQeVFlSVdGUFVQTEhqQ0I3aWw0WXMwLUdLWVUwdGtfZF9aYk1mNXF4YkZqRXRpZnZoMV9INDI3eHdMZGFlTFF0cWg1MHV2cjc1Tko0S3hkbUg4NzctQ2VnR2VaLWRLY0RJWXQ1N3RtNWtuVHdrU1hyZ3F6THIxaFNEU1g2ZXd5VnVQOFhzM0JYSmd1eVBJdjgwZDQ3T3ljZmlsZw?oc=5>

### AMD’s stock slides after Intel earnings reveal two big issues
- Summary: AMD’s stock slides after Intel earnings reveal two big issues
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQSG1ER3NBSmVWMHJlelZ0akVNa1FTVDFlM1J3b2ZMOWZXanV1cVdDblB6dDlHRmJYZDRVZ2JKWTRfRDIyTkZaNENTZVQ2MGFJUjk2X0ZfU2ZTVjZEcm02VlJZXzQyYmlVdHY2Mm5BaEVvUmN0Tm1rQUF2NWlIQTdLMFpWNVl3QUNvX05MRlg0cmw5d1JQWjAxeUtDeHpVandzY2tDZGxn?oc=5>

### Advanced Micro Devices slides 13% as part of tech selloff (AMD:NASDAQ)
- Summary: AMD stock fell 13% amid broader tech selloff, indicating short-term downside pressure.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPWGV3V2xDR1l0WWdPb1JuRk9WYm81cDQxdFB3NHFXUGZUamIxQzk2MTZ3MFFYSkx1c0VPQTNrT09mdmh5UERtTjZvVTBKRXVPc2NwMHJYMVlfZldGNW9CY2xobXpsTmZjUFRtcDE3dTJwemxHNVRRcU1vcG1uZUZZN1lidjJyWnRXRkVlX2w3ZnVmbEkxcG0yX3FB?oc=5>

### Chip and AI stocks give up some gains ahead of AMD earnings (AMD:NASDAQ)
- Summary: Market gains in chip and AI stocks decline before AMD earnings release.
- Date: 2026-11-02 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOd2tWdkUzZldKRGVYT0FjMlRDZnJ6b2F6cWlQbTVxRWRjQjlMTDZFVERkYldQMnhqNmRwazN4X0pQQi1EYnlqbWNVTTRSOUNFUWtmUlVRa1FfcXdxdzh2TjlIdVlqUFl6WXlKNFFCVzFLRjBMWWRyaWVjOXQySTJsXy05RUZFcWU0NTZJTTRLeHlIdDh6QU5VRmdxclJQUQ?oc=5>

### AMD Just Dropped 16% in a Month. Is It Time to Sell, or Load Up?
- Summary: AMD shares fell 16% over a month, raising sell or buy considerations.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxQSEFWcjcyVUh0UW5Oa1JRQzY4TE5md2wtejdtS0FOQmJyUlJXWE9FajVHNVhnOVZOLUotaW1DTWR6V2p0ZXJ6TnpQNlU0LWVHSjdTbE1JbGdGQTdMd3RsOHNScjExVzk3cl9WbWJtVzBhVXBFd3ZvdUtkNkF2UElfaXpEMnptV3p6Yno2MHZtbUo?oc=5>

### AMD Slides 3% Ahead of Earnings as PC Worries Linger; Intel Drops 5%, NVIDIA Edges Higher
- Summary: PC market concerns weigh on AMD shares before earnings release.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxNVU9zM3VwTGlsdkpyZE1zenRfZmRxNEk1VG45R1QzdEpqOWhoOTFxdi1RYTZMZFhxNDRFTHVlRFlHeTNJRWpPd0UtM1ViUjJCT0FWS0lIdTEyLXUzYkVXYktpek1fYkdPcXJVczUzUEpodWQySDFWVTlmS19DYjFMZklkLV9oSkRza1ZnVTFvdVltaHZUakpOb1lpeHRLV2FldGNkckRQR0drSVB6TDB3bHFxUkZLeWM1bVJjYTc3Z25qN0s1LUk0OQ?oc=5>

### One-Chart Preview | AMD's Q3 earnings report will be released after the market closes on November 3! Following Intel's sharp decline, a critical test lies ahead—can AI growth offset concerns about PCs?
- Summary: PC worries highlighted; AI growth questioned as potential offset.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.78
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOMnFUdV9jZGNlNGt3T2ZqalpVd2Jqb3B5Y0xheUpjaDhVWHlMRjk1MW80R291ajVBMVNzNVlLN1dQZlE4TjV6ZTZRUUd3U0lxbnlEWERVWkpfcWsyNGpvNGtsYXpuTkxScVRxenlUTHVfZlo1ZXMtUi1zUFptcWtHYlJXYlNoYU9aM3hKS1lFNi00MWNodGVvcg?oc=5>

### AMD (NASDAQ:AMD) Stock Crashes 11% Ahead of Earnings: Can AI Chip Growth Reverse the Selloff?
- Summary: Stock fell 11% before earnings, raising concerns.
- Date: 2026-11-01 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMieEFVX3lxTFBGbVMyR0I3YVN1bWdBUGRSTmFHWXFxUzllMnAtcUctdnZpSXdtMWxBVHVSTU5xVkU3SEdLMlA5RGtwVTNFNExDWHNLTTNkUzlibGNmY0dadmZyc2kybmlpZ25FTWFudTlLZ1R4VXBxRzZBYjRGZzNvZw?oc=5>

### Buy, Sell or Hold AMD Stock? Key Tips Ahead of Q3 Earnings
- Summary: Analyst tips reflect uncertainty before earnings.
- Date: 2026-11-02 | Impact: low | Horizon: short | Confidence: 0.88
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxQWGp3WmpKTnV2YnBiRUJrZW9FMThyVG41aUgxTk1HMHRvSUgtbGIzSkozUlpvWlRqTm54OUdxbHFuX2R6cVRNQlpqdGZkTjFUMFNueXhRMGgzel9pMy1JRkhENEdqQVgwRFc0S2Npa0pkMzRiTlMwc01TaG9EZUJDZVhGNEhJYmxoU0UwM0pFMUdYUQ?oc=5>

### What to Expect From AMD’s Q3 Earnings
- Summary: Forecasts outline potential earnings outcomes.
- Date: 2026-10-31 | Impact: low | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxQV0p3MGMzdy12MXRpU0E5NnlXZGNnN2VhbHVwYzl0blZWX1BfR3c4Yk1VcEJBcWhQQ0gtR2xLUG54M3FwYm85ZGV5bjl5ZThreUZYTTNTVFdzV093RHpRejhGb3JnYnRfMGs5TjVKODB4QVpNZE5OMC1iblZ6Y3ZkSjJrdXFsM1NjOE5ZYzdXTjg?oc=5>

## CATALYSTS

### Advanced Micro Devices (AMD) Set to Report Q3 Earnings Amid Stro
- Summary: Advanced Micro Devices (AMD) Set to Report Q3 Earnings Amid Stro
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxPSXVhUGVKeXBqaTY4U01xd3l1S2hUWmg2cldJRlZRencwQUhORlI4Zm9hLXpVYmV2VVFCX2lIOU1XWHgyMVFPTzZzenZFSFdIdVZhWWV3aE85Z0Zza3RBRFp1a3dwSHA5d25ERmtNLXlBTFMzaU00eHpOVW9sSHJYU2JfdC1NaFFzMXFnNUpIbFVpUTNHZVc0VlpveTFkOWtPYmcwYW1GTlVBWFo2elRBZGc4QWpReVNYNmxr?oc=5>

### AMD (AMD) Q3 earnings: what to expect
- Summary: AMD (AMD) Q3 earnings: what to expect
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOWkxjc3FEazRqZlNFVEdITkpZeDhQRUxjNjMzN25oZ280ZUpKTkxlcXAySEVVUERPU3ZqOGtpSDZBYW5TR2gtczdiajZYUW5mam1JTWprVG1raW52X0tITmN4dUpJZUNPNmR6SUlBQnloa3h4RUEtdUxrWWxycE16OFFLb2pWdFNCQ01oNWFnbmR5Tzd4Q1E?oc=5>

### AMD to report Q3 results following disappointing showing from Intel
- Summary: AMD will announce Q3 earnings after Intel's weak performance.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxQU2VNY3ZGSGxNTTQ4ZDYzaXhaOUdwNjNiUGFQQkZ6MFY0WXZ1ZzJ6YW8ySFljMVpIOUVTME80dUdCOEJma1FCS3Z5OE10Y0ZwSnhTTVlZT204QTJ5NXVTZElqTWREeDB4V2NLNWV1R3ZFbGlzZ0JNeTRJVko2M2xFS3B3TWVMX0lKUWozdTltVGpKa0VPY2tmWVlnSnVWUzNnNVJrcUl4dzRyWUZIaTgyck1panRDc0pNT09YSnlqQkZUcVNkOGc?oc=5>

### Ahead of Advanced Micro Devices Earnings, Here’s What Barchart Data Says Comes Next for AMD Stock
- Summary: Barchart data predicts next moves for AMD ahead of earnings.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxQbXJodzQtaWtBSi1tRFpVZ1VyQ0tObE5BOU5uY2htQU4ya0Fncm1ITE5xYXhoNlp5NUlwTGIxQ0ZfejExYzZvMXJYSUg0bUo4bE1fU3lOSTgyeS11U0YzRTZEODZncjVvTmtjeTdwWHJSMVVNY2E1QTlSbTdJMnpfZV92NUhSSEM4eGNjN0JyenFCWEo2OURpNmt6Z1AwaXhqMFVEVWgxa2NTbUJkSU92V3ZRVEVUeGgxaXhma2N6aXFXWjRyaGNTbkVWT1hkT3VuZzBYWlV3?oc=5>

### AMD Reports Tuesday. Here's the Number That Will Show Whether It's Gaining on Nvidia
- Summary: AMD's upcoming earnings will indicate performance relative to Nvidia.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxOcWNUVlUtVkh0MF8wN0tDaVlMR0ZDTDJheDR2d0tIczFpY0REY2dBbnZqN0tXZVUzLUxDelV2eGZRRVhkV2k2TlZNeFl3WXNHVHo1RTVoMUI2ZUx1VjBSNmlualF3X2g0clpEdmFjM1U1T01SQnpDU2VETWNMVFV2QnVWZGplZ0JZTDNwZ1dRbTZIbWtoYjd0aUp6aVRCUE11ckJEcmJ5WXAwdEE2QjRnZ3M3N1duTnl2Y3AzMWx3UV9OWVpw?oc=5>

### AMD, Arista, Supermicro Earnings Previews: Can AI Infrastructure Shake Off Friday’s Rout?
- Summary: Earnings previews may boost sentiment if results exceed expectations.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxOWk8wanoxTlU4RHRyNUMxUV8xLXhKeDdVQzRSMGJyRlQ3ZjNnUWw1azNIS3l4bHRWN3BXc2o3NE5FUFJJR0E2Rzh4Vmd4Q25kWnozWW1Udy1LSUpnbzBrSHlrSUtWbW5DTHdlZ0c0dHNTUThTTXpaZk5iNGw1OGlGak1tOG9ya0E2YTFwWW9NT0FzSHM3WVB3M2d4clVZWnZHajlXSGd6OA?oc=5>

### AMD Could Swing $90.7 Billion After Earnings
- Summary: AMD may see a $90.7B swing post-earnings, indicating strong performance potential.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQM0FwVTVfOEJRRjN5bmhJd0ZGYjJNbnBSVFBZZU1Qam44RlJhSGJ3enVuRGxESDJITzU1enBIanhWZEtHLXRjdEpWbTlUY1RlZ3lTVFBkck5zVHZGX0p2bllGTjBsS3JhTlRzQ1JhRDlBanp6eHRRbTI4UXhCRy1UWmhFZjVZa2FMQkdzZWEyR2xrU01xZXlLS2lLSm81aUtJ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMD** | **119.09** | **11.33** | **78.78** | **50.10** | **762,104,643,584.00 USD** | **82.27** |
| NVDA | 25.54 | 21.31 | 24.08 | 105.90 | 4,879,142,617,088.00 USD | 0.03 |
| INTC | N/A | 2.77 | 17.32 | 20.90 | 318,740,529,152.00 USD | 49.96 |
| AVGO | 41.15 | 15.43 | 30.11 | 85.50 | 1,538,206,859,264.00 USD | -12.18 |

Peers fetched as_of: 2026-11-02; AMD reuses existing data (market data as_of: 2026-11-02); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-04
- Next expected earnings: 2026-11-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-02

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-05
- Revenue (latest available single quarter): 1,584,000,000.00 USD; period 2017-07-02/2017-09-30; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 2,297,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/2488/000000248826000123/amd-20260627.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi4wFBVV95cUxPYmpQbzdwSUE4a2NJZmpKQ0lGaE1PUHRvbk9MZmlGT2w2WHg3M1NtSGcyMlpJdjZ0OFE5NDJyQUpsSGdnLWlVaC1TRDlDdThtZmZZaTVVcnQ1MlNiS09BM1NuTWViM1NqN0ZFX2c0bGRsNkdjaV9Tb18tbzBYX3JjN3lkQm9IR3EwWXRZblNlcl8wZ2hqd3dTejJ3ZXZGN2R5emZ3ZFRaSGdlR3RCcWpYMEFtTDVmcUh0NUV2bWdCamhEb01fSjRIQUh5aG5NdkhLTW15ZkgxbnBpdFNaeFQ1R1BLaw?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxQbUtyekwxWHBFN3NCTFRGcXlJa0UzdzNSZzR5M1BiUmNIN3JXMFRvQVhLNkZ2Z3gyaEV0bXdKS05mSFdxN3N1X1ZsbkJxLXhQYzFfT0NSbXJWZGR5aXFRSnYxVkx3c0N4TmFIWGd3S2h0ZXNqYmp0dDZBZ3kySF9kVGRyQ3cybnRMbHRYZFo2LTlOSmF4N01WSTlGXzNyeEl6azhCaDM3cThLUkY0NjZycThYVU1VZUI2VHlOVzNjYXVfRDZleUE?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPNWpNdV9aMks3Sk92V3U0akxMZXdBOGxuemtvR3JZNldrU0FIcjVPODhyNlY5ZzRDNnJxS1U1VUQ2QnFlNnlNeGdPdjNObVFCbkktZnp2bzgzMk52TnBrRW5oT2RFNy1HYmRkZVBlYVV4b0g4ZG51WTZscGRtbHlXUFFwdno4dnpfWWY5Ui1iSHAyakxqTkM0VQ?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxPa2JFaWNkdFBCSzNCMEMtRU51R09XWTRBMm1IMVdMM1NnX0N0LW13QURpUm5JaEZQazJfR19PWXV1UHJOQnlkUGlLbldVb3hSTG1GWXZlYkNxZ1Z6QmRHVGl3LTFnYUMxZnFtYUFuVlBXU0pRbnlCSGRMSFp4RW1nSXI1ekE1RzFKa2psSjBXYWszQXByMV9GbzhUVmVvMmUtamJtVndxOUlEOW9ubE5wVzlOanAtYWx1a3c?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxOQ0dnXzRmUWRQeVFlSVdGUFVQTEhqQ0I3aWw0WXMwLUdLWVUwdGtfZF9aYk1mNXF4YkZqRXRpZnZoMV9INDI3eHdMZGFlTFF0cWg1MHV2cjc1Tko0S3hkbUg4NzctQ2VnR2VaLWRLY0RJWXQ1N3RtNWtuVHdrU1hyZ3F6THIxaFNEU1g2ZXd5VnVQOFhzM0JYSmd1eVBJdjgwZDQ3T3ljZmlsZw?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQSG1ER3NBSmVWMHJlelZ0akVNa1FTVDFlM1J3b2ZMOWZXanV1cVdDblB6dDlHRmJYZDRVZ2JKWTRfRDIyTkZaNENTZVQ2MGFJUjk2X0ZfU2ZTVjZEcm02VlJZXzQyYmlVdHY2Mm5BaEVvUmN0Tm1rQUF2NWlIQTdLMFpWNVl3QUNvX05MRlg0cmw5d1JQWjAxeUtDeHpVandzY2tDZGxn?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPWGV3V2xDR1l0WWdPb1JuRk9WYm81cDQxdFB3NHFXUGZUamIxQzk2MTZ3MFFYSkx1c0VPQTNrT09mdmh5UERtTjZvVTBKRXVPc2NwMHJYMVlfZldGNW9CY2xobXpsTmZjUFRtcDE3dTJwemxHNVRRcU1vcG1uZUZZN1lidjJyWnRXRkVlX2w3ZnVmbEkxcG0yX3FB?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOd2tWdkUzZldKRGVYT0FjMlRDZnJ6b2F6cWlQbTVxRWRjQjlMTDZFVERkYldQMnhqNmRwazN4X0pQQi1EYnlqbWNVTTRSOUNFUWtmUlVRa1FfcXdxdzh2TjlIdVlqUFl6WXlKNFFCVzFLRjBMWWRyaWVjOXQySTJsXy05RUZFcWU0NTZJTTRLeHlIdDh6QU5VRmdxclJQUQ?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxQSEFWcjcyVUh0UW5Oa1JRQzY4TE5md2wtejdtS0FOQmJyUlJXWE9FajVHNVhnOVZOLUotaW1DTWR6V2p0ZXJ6TnpQNlU0LWVHSjdTbE1JbGdGQTdMd3RsOHNScjExVzk3cl9WbWJtVzBhVXBFd3ZvdUtkNkF2UElfaXpEMnptV3p6Yno2MHZtbUo?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxNVU9zM3VwTGlsdkpyZE1zenRfZmRxNEk1VG45R1QzdEpqOWhoOTFxdi1RYTZMZFhxNDRFTHVlRFlHeTNJRWpPd0UtM1ViUjJCT0FWS0lIdTEyLXUzYkVXYktpek1fYkdPcXJVczUzUEpodWQySDFWVTlmS19DYjFMZklkLV9oSkRza1ZnVTFvdVltaHZUakpOb1lpeHRLV2FldGNkckRQR0drSVB6TDB3bHFxUkZLeWM1bVJjYTc3Z25qN0s1LUk0OQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOMnFUdV9jZGNlNGt3T2ZqalpVd2Jqb3B5Y0xheUpjaDhVWHlMRjk1MW80R291ajVBMVNzNVlLN1dQZlE4TjV6ZTZRUUd3U0lxbnlEWERVWkpfcWsyNGpvNGtsYXpuTkxScVRxenlUTHVfZlo1ZXMtUi1zUFptcWtHYlJXYlNoYU9aM3hKS1lFNi00MWNodGVvcg?oc=5
- https://news.google.com/rss/articles/CBMieEFVX3lxTFBGbVMyR0I3YVN1bWdBUGRSTmFHWXFxUzllMnAtcUctdnZpSXdtMWxBVHVSTU5xVkU3SEdLMlA5RGtwVTNFNExDWHNLTTNkUzlibGNmY0dadmZyc2kybmlpZ25FTWFudTlLZ1R4VXBxRzZBYjRGZzNvZw?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxQWGp3WmpKTnV2YnBiRUJrZW9FMThyVG41aUgxTk1HMHRvSUgtbGIzSkozUlpvWlRqTm54OUdxbHFuX2R6cVRNQlpqdGZkTjFUMFNueXhRMGgzel9pMy1JRkhENEdqQVgwRFc0S2Npa0pkMzRiTlMwc01TaG9EZUJDZVhGNEhJYmxoU0UwM0pFMUdYUQ?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxQV0p3MGMzdy12MXRpU0E5NnlXZGNnN2VhbHVwYzl0blZWX1BfR3c4Yk1VcEJBcWhQQ0gtR2xLUG54M3FwYm85ZGV5bjl5ZThreUZYTTNTVFdzV093RHpRejhGb3JnYnRfMGs5TjVKODB4QVpNZE5OMC1iblZ6Y3ZkSjJrdXFsM1NjOE5ZYzdXTjg?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxPSXVhUGVKeXBqaTY4U01xd3l1S2hUWmg2cldJRlZRencwQUhORlI4Zm9hLXpVYmV2VVFCX2lIOU1XWHgyMVFPTzZzenZFSFdIdVZhWWV3aE85Z0Zza3RBRFp1a3dwSHA5d25ERmtNLXlBTFMzaU00eHpOVW9sSHJYU2JfdC1NaFFzMXFnNUpIbFVpUTNHZVc0VlpveTFkOWtPYmcwYW1GTlVBWFo2elRBZGc4QWpReVNYNmxr?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOWkxjc3FEazRqZlNFVEdITkpZeDhQRUxjNjMzN25oZ280ZUpKTkxlcXAySEVVUERPU3ZqOGtpSDZBYW5TR2gtczdiajZYUW5mam1JTWprVG1raW52X0tITmN4dUpJZUNPNmR6SUlBQnloa3h4RUEtdUxrWWxycE16OFFLb2pWdFNCQ01oNWFnbmR5Tzd4Q1E?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxQU2VNY3ZGSGxNTTQ4ZDYzaXhaOUdwNjNiUGFQQkZ6MFY0WXZ1ZzJ6YW8ySFljMVpIOUVTME80dUdCOEJma1FCS3Z5OE10Y0ZwSnhTTVlZT204QTJ5NXVTZElqTWREeDB4V2NLNWV1R3ZFbGlzZ0JNeTRJVko2M2xFS3B3TWVMX0lKUWozdTltVGpKa0VPY2tmWVlnSnVWUzNnNVJrcUl4dzRyWUZIaTgyck1panRDc0pNT09YSnlqQkZUcVNkOGc?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxQbXJodzQtaWtBSi1tRFpVZ1VyQ0tObE5BOU5uY2htQU4ya0Fncm1ITE5xYXhoNlp5NUlwTGIxQ0ZfejExYzZvMXJYSUg0bUo4bE1fU3lOSTgyeS11U0YzRTZEODZncjVvTmtjeTdwWHJSMVVNY2E1QTlSbTdJMnpfZV92NUhSSEM4eGNjN0JyenFCWEo2OURpNmt6Z1AwaXhqMFVEVWgxa2NTbUJkSU92V3ZRVEVUeGgxaXhma2N6aXFXWjRyaGNTbkVWT1hkT3VuZzBYWlV3?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxOcWNUVlUtVkh0MF8wN0tDaVlMR0ZDTDJheDR2d0tIczFpY0REY2dBbnZqN0tXZVUzLUxDelV2eGZRRVhkV2k2TlZNeFl3WXNHVHo1RTVoMUI2ZUx1VjBSNmlualF3X2g0clpEdmFjM1U1T01SQnpDU2VETWNMVFV2QnVWZGplZ0JZTDNwZ1dRbTZIbWtoYjd0aUp6aVRCUE11ckJEcmJ5WXAwdEE2QjRnZ3M3N1duTnl2Y3AzMWx3UV9OWVpw?oc=5
- https://news.google.com/rss/articles/CBMi-AFBVV95cUxNMUJ5dXZNM0N6VEdnTEJObkdFaEpKQ0ZJZUd4Vi0yYU1VVTdLWTQ1TWdsTDlucjR2NGF6VUNhSFNoN3lVdU9GdHNfdkhmbGlURVhDQ3hNUFJSYUVJQ3o4bHkwLUxaVjVXMW9nN0RTQmM0MkFsekhCdnUxRHdVVHVzSDhWN3d6TnNfaWxaMGxKSDJKYnFLYy1XQURpelBuX2dMRUs0WUp3LXNtN2dMZXFoRkwwYlducjhQM3VrRzEyX3VqQWRUckpnWFBNUzV3SkdCNXZPZEl3czJPSnpXX2hSVnpDYWxkTUFCa3ItVUh1aHk5RVZMWEttRg?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxOWk8wanoxTlU4RHRyNUMxUV8xLXhKeDdVQzRSMGJyRlQ3ZjNnUWw1azNIS3l4bHRWN3BXc2o3NE5FUFJJR0E2Rzh4Vmd4Q25kWnozWW1Udy1LSUpnbzBrSHlrSUtWbW5DTHdlZ0c0dHNTUThTTXpaZk5iNGw1OGlGak1tOG9ya0E2YTFwWW9NT0FzSHM3WVB3M2d4clVZWnZHajlXSGd6OA?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQM0FwVTVfOEJRRjN5bmhJd0ZGYjJNbnBSVFBZZU1Qam44RlJhSGJ3enVuRGxESDJITzU1enBIanhWZEtHLXRjdEpWbTlUY1RlZ3lTVFBkck5zVHZGX0p2bllGTjBsS3JhTlRzQ1JhRDlBanp6eHRRbTI4UXhCRy1UWmhFZjVZa2FMQkdzZWEyR2xrU01xZXlLS2lLSm81aUtJ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
