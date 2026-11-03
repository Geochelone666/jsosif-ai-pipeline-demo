# AMZN Intelligence Report

- ticker: **AMZN**
- Report as_of: **2026-11-02**
- Market data as_of: **2026-11-02**
- Quant sources: https://finance.yahoo.com/quote/AMZN/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMZN/key-statistics/
- AI analysis snapshot as_of: **2026-11-02**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-03T05:32:09.375080+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 7, 'ai': 10, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261102T041627Z-c84a7052/AMZN** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **5**; {'directional_claim_without_event_type': 2, 'low_uncalibrated_model_confidence': 1, 'negative_sentiment_in_tailwinds': 1, 'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 14 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 29.17%; oldest publication 2026-10-29

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 245.6300 |
| Return 1D (%) | 2.1968 |
| Return 1W (%) | -1.3891 |
| Return 1M (%) | -2.3418 |
| Return YTD (%) | 6.4163 |
| Return 1Y (%) | 0.5773 |
| Annualized volatility (%) | 33.4491 |
| Beta vs SPY | 1.4313 |
| Max drawdown (%) | -21.7362 |
| Sharpe (rf=0) | 0.0625 |
| Downside deviation (rf=0, %) | 21.2272 |
| Sortino (rf=0) | 0.0985 |
| Historical VaR 95% (1D, %) | 2.9695 |
| Historical ES 95% (1D, %) | 4.0742 |
| Correlation vs SPY | 0.5487 |
| Tracking error vs SPY (%) | 28.5064 |
| P/E (trailing) | 19.86 |
| P/B | 4.33 |
| EV/EBITDA | 15.49 |
| Revenue growth (%) | 12.10 |
| Forward P/E (estimate) | 22.50 |
| Gross margin (%) | 51.37 |
| Operating margin (%) | 13.90 |
| Return on equity (%) | 27.42 |
| Free cash flow yield (%) | -1.31 |
| MA50 | 254.0190 |
| Close vs MA50 (%) | -3.3025 |
| MA200 | 243.4379 |
| Close vs MA200 (%) | 0.9005 |
| RSI (14, Wilder) | 43.8602 |
| MACD (12,26) | -2.2685 |
| MACD signal (9) | -0.8423 |
| MACD histogram | -1.4262 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMZN': 273, 'SPY': 273}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 245.6300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.1968 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.3891 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -2.3418 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 6.4163 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 0.5773 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 33.4491 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.2272 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.0985 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9695 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.0742 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5487 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 28.5064 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.4313 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -21.7362 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.0625 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 22.5029 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 51.3740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 13.9030 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 27.4160 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: -1.3077 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 19.8569 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 43.8602 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.4262 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -3.3025 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 0.9005 -> Slightly above the moving-average trend level.

## TAILWINDS

### Amazon (NASDAQ:AMZN) Stock Rallies as Wall Street ‘Buy’ Upgrade Highlights 39% AWS Growth
- Summary: Amazon (NASDAQ:AMZN) Stock Rallies as Wall Street ‘Buy’ Upgrade Highlights 39% AWS Growth
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMieEFVX3lxTE5TRVJ2ODRjSDRoWUtreUFjYkJONzY4VFMyUE5GVy0zaS1lcHFVaFpOQnlkTVFXTkhTYWVIRFNJZUlIbjNUcEhjbWFfTHlRVGp3WFE1algzZzdNTVJ1amVaX2syM0piLWI1VEJPTS05OVNNbU5aZjBNZg?oc=5>

### AMZN Analysts Split After Earnings: TD Cowen Says Amazon Selloff Is ‘Overdone,’ Mizuho Raises Target
- Summary: AMZN Analysts Split After Earnings: TD Cowen Says Amazon Selloff Is ‘Overdone,’ Mizuho Raises Target
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7gFBVV95cUxQb29PVHlYM0pGdGtkbXZTMms5UjJjNmFhWGQtVHdJRVBzMWdFem9aOF9fYU1YQWxNaTktZWpqMHJ4X0tZNV9EQ2taYnJvU05TUElfTVREMmpkSHhpdTVyRTdBRDg4TjVIR2l0S2VGeHc0YzhrWUxXQzgzSlVVcUZIc0R4djhVQkQzbWVpcDQ1X1RQZk9zcy1qbWxZYkk1M1dPemJSd3VLQWg5dG1mYUdPTFQ2X2xEckVFd2V2cGJOa3k2cnR5TkJBTWF4NVY2VGtjUjZUV3ZEOGJWSHlmbFpCU29hUUhmYzE5VWRVMHJn?oc=5>

### Amazon Stock Rises: What's Going On?
- Summary: Amazon Stock Rises: What's Going On?
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQQlg2eVlHWDl0QUpwa3MtZ2JBVUVMOXd6Y0xzSlNSRTMyRGl2SmRRZEhQNTRsS01vellzQ3NvSm1GYUNNbmZiRUlaOTYwaHFuejRiajNOTmxLS2lJT1J1Sld6NXp2ajRMUlRheHcxckw1OHhHdVFHSW9fYnVXdkVWNmdFeGI5UFh5OS1CM2VUQ05KODhXZlhvSTJR?oc=5>

### Amazon Stock Slides As Bullish Cloud Forecast Not Enough To Overcome AI Fears
- Summary: Amazon shares fall as bullish cloud forecast fails to offset AI concerns.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigwFBVV95cUxOUUcycHJPVi1rV3dqc1N5LWEtbmJhMW1ZWjI4MWxXdy13NXBEWnBKRG5vUGl6U00tOEVlNVk5T2p2a2ZkdGcwUEpBR1hETE9zVVREZnNOZ1Q5amF6SHdDLVR4Yzh3STdDeGhJMFBRRkhKVmZlVmJudFF1R2wtNGFLcGh3UQ?oc=5>

### Is Amazon (AMZN) a 'Buy' Ahead of Earnings?
- Summary: Analyst recommends buying Amazon before earnings.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNS0Z5Z1RsdUJFdHdXdzNnbC1hVXZlYVB4SlQteXNpeFZxNUJMS2VNZVBuLXZFdzd3aHJWQzZOZk1tZWMxWWZNVUNWc1QzdGJPQ0c4bndHczk2M0xPeFQwOWNRMGlic0NXTjFnZndlZEozVElKemJmQ18yRVUxcmVDR2hzalUydTY4RkxHQm1wS0ZxUE1mdmhYSUNEdw?oc=5>

### Amazon (AMZN) Stock After Q3 Earnings: Buy the Dip, Sell, or Hold?
- Summary: Analyst offers buy/dip/sell/hold guidance post Q3 earnings.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxNZTRnSk1vYUtiQlJ0YVdWUEVMQm5mMFZfbjc0T1hwZDFLUjR5THFrbTFzanhGNUhIYV8wV2Vpa2FRTXFRcTRsanphR1ZSS1lHMjQ3QkoxVlhYSmo3QkFWS29fa1VHaHlMVVpCV21GcFpaQVBaLXhvd0wzbWFSRFZTNG5rdnVfM3lOTnVBaHVWSmU4MlIwYzI0WU8teXN0WTl5Q0pJ?oc=5>

### Why Amazon Stock Rallied Monday Morning
- Summary: Amazon shares surged Monday morning due to positive market sentiment and strong earnings expectations.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxOdDBxcVFnZUY3UVczSkJGUFdIOXJweEg4NURlT09tRi12MThQQ1Y5Rl9CcUtzMWJUdDJHWnpHTWV6R015R194ZXE1cmtLZXprZGZnSWJFNndveUpBWU9sMTFwYkxPYTdib3JlOGVSSHVUalB6THFlOGFnckN4WWRLSmhYR1QzX0ROOHc?oc=5>

### Amazon: Tune Out The Noise. Focus On The $1 Trillion AWS Number (NASDAQ:AMZN)
- Summary: Amazon emphasizes AWS's $1 trillion revenue, highlighting its growth.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPNHU1TE9TbnphOU43d1JrYXAzajZKZVVuQkF6TThNQVhJUmQ4RmU1U2RTUnpPYmQ5UE9tS2ZnenNTcWhyTVpGTkFCem5jeU1mZkl2QUJhTENCMDBKOGJVTnJGSTE0UmUyblhZQnM0UGxyVk1NZUVMbVp5cEhzTmdhanA3eUtLaEozTTAzRmhmSmZ1M1FRbEhPaEl6cVBIRGIzSVJ3?oc=5>

### Amazon: Don't Look At The Cash Flow (NASDAQ:AMZN)
- Summary: Amazon advises investors to focus beyond cash flow metrics.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMif0FVX3lxTFBUejFDcXJiQ0NLMHd5alJ5Znp6N1h5X0ZqaFRDNHpTQ0cxenJOZHVBLS1ReDA0Rm5GMHg1NXRrOWVGYl8wUU9HZm13TUR0SmNqQU1PR3hMQTNYaC1oelJKUU55QnExUVVoV0hta204RG91VDZWUUhOVWZpT1FmNWs?oc=5>

## HEADWINDS

### Amazon (AMZN) Stock Slips As Q3 Earnings Reflect Profit Reset
- Summary: Amazon (AMZN) Stock Slips As Q3 Earnings Reflect Profit Reset
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOMHVOOUNrejV0ZnJZZFhTWGhHRDFVN2hwd2djSHZDbFR0aHZhdlVZSy1rcWN5eVJzYWlJRURXN013em1KVS1lNkNVQ0wybEllb0h0dnZHajhYUjhKTFIzQjZMS2ZYb0FJQm5kcjVmOGNBOFllYWYyT2hXTVh1cmFoY1d6eENfak9XcUpCekdxSHZyaDMyQ2c?oc=5>

### Amazon Stock Fell After Earnings. Jim Cramer Says Buy Right Here
- Summary: Amazon Stock Fell After Earnings. Jim Cramer Says Buy Right Here
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQdVZfYkpFaURIalAwZHlsWjJ0RGJlekJJNjBUWFEtbThRUkhxQVpFMk5ieENxZzNFZlpOd2s0VG5TSkpHaE5hS190bXMtb2JkeGQyRkJ5Z2JOcnE3UEdBUUFhVmRQMzFQQlVXcVBEUDdEczUyZllrUUtoV2JxTE9QS1ZLUmVtSmk0RmhMcmMwTEtaZmxaV2M1T0VOdw?oc=5>

### Amazon slides after sales and capex guidance overshadow accelerating AWS growth (AMZN:NASDAQ)
- Summary: Amazon slides after sales and capex guidance overshadow accelerating AWS growth (AMZN:NASDAQ)
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxQQVNlTDBZVzFmVkpRZTdJYWlGRGR1VkZsXzBTM1ljc1JLNmx3MG5GdGREblh0NWpaQ0k1R2VXc29UUEdpSlZoa1RXaW1MTjdGSFpRRTYxRXkxVWFLb3NKVUV0N21iMVQ4dG9DMkJvLV9TT2JLQ2otaVNwck9meVlWdEUwT09YZENCTTZkU0xXV2dMUHBWcHF0XzRVNWFMY2xZUVdITFlPN0xVWHhibU15NE9GWF9QMVdH?oc=5>

### AMZN Stock Set To Drop For Third Straight Week: Amazon Taps $80B Credit Line To Fund AI Capex
- Summary: AMZN Stock Set To Drop For Third Straight Week: Amazon Taps $80B Credit Line To Fund AI Capex
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxPYnZtTWxaSGhHVEIxZ2xxcHYxdFBVSUJVRXNPaGJBMlBoVnZ3UmdDWGZyV1dUV2ZsaTZCcHc0MGpRR091NElxcWdoVDF4MHloaUdTbG9fOF82ZTU2TmNKQWxFeHIzS0hNaW1ia3lMTVhMWVhOelJjMWlPRXFwN3BGclVaZzBHWDdyYWYwWVNqelZUMHhRX091c1ZGRDFKcVRHZzh0TERvUG82cVJyMWJKYkhRZHpJLXpkbUhOYWNHZUFWMm1rdFdLWklLYzcxZTU5TkdMeE8xZVBTWFRQbG8tWTY5Vi0wZzZsZ0I1Vw?oc=5>

## CATALYSTS

### Stock Market Today, Oct. 30: Amazon Misses Revenue and Earnings Expectations
- Summary: Amazon reported revenue and earnings below expectations, impacting short-term outlook.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQTVVnNnFNVEt1SnlTWEVYSWVTam9lZEgwcUwtMG8waUZCVDNxVkVRZDBuOFlfQjFvZkRVTHlobzlaakJreUNlSjIxcXIzVjd5X3Q3YzBGUWlkeFdRYmxxWlNxc3J2YVZNQ2V6WUhvR0JwSTVlOEZqMm54R2dUb3FGb0RmaE5qSC1WZXZyS3R5LTR1V1kt?oc=5>

### Phillip Securities Says Amazon’s ‘Strong Demand Visibility’ Supports Aggressive Capex
- Summary: Analyst highlights strong demand, supporting higher capital expenditures.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxOTU11b201VGNET3J1SXBfbmJfekt0aWhyakdicUJkYXdoTDRvSk5ibjFUenM1N0ZjTU4yeDBoTlNIdmhSU3hOQ2ZEeWRhVUh0SUstSWtjMDh0ZHgtWFk4ZTU3WFpfcDBSS3NjVGpydXRRTnNZdzlINkN4eVh2dXJyQXF0bWlFRWpsdFRJM1dtNU0wcFR3MzQ2R0hVY1JOc1hxRWdTZA?oc=5>

### Amazon Vs. Alphabet: The $420B AI Capex Squeeze Leaves Both At Hold (NASDAQ:AMZN)
- Summary: Both Amazon and Alphabet face a $420B AI capital expenditure squeeze, prompting a hold rating. The move may limit short‑term growth but preserves long‑term investment.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQMTBOdW1vN1RWbkxOVXY0bl96c1U5R2hPbE12Y2VJdkJySDRfeDg5ZjRUOWpSb3c0WjdTWVdEME4tdkhjenlJOTlsa1ZFWE0tQVo5REtZRWZWOXBfeUtYaDVQSjFYZmFoTjgyZDdYejNXTFlQV21QWmtnRGhJVVVkNHhCSDR3VkxOX2xpdFJzbzZ3MkN6NE1OSlBMZGh1eFc3NlF1TTFIN1U?oc=5>

## RISKS

### Amazon.com Stock: Is Wall Street Bullish or Bearish?
- Summary: Investors debate Amazon’s stock direction, reflecting uncertainty in earnings outlook and market sentiment. The debate may influence short‑term price volatility.
- Date: 2026-10-30 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOOTlFYkZ6X0hrRy11VDRkcGQxVzVpMXJETFpLSkZ4aUxfLWVTVEp1eDdsQkFXUGg3TWlLcUQ2dVBOLUkzdkVBM1ZVNkE1ZjdGWnk0b25VNFNLcEE0TDJKbFVweGJfYy0wYVJMVmxULXdhN2laYjRlekJZdXNTY2JXZ2l2bWwwVHdyOUNLTmt3VWY4MWlISDF5Qw?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMZN** | **19.86** | **4.33** | **15.49** | **12.10** | **2,656,031,211,520.00 USD** | **0.58** |
| WMT | 44.80 | 10.32 | 24.58 | 5.90 | 1,016,167,137,280.00 USD | 27.26 |
| MSFT | 27.24 | 8.00 | 18.65 | 18.80 | 3,765,971,714,048.00 USD | -1.26 |
| GOOGL | 14.57 | 5.20 | 17.97 | 24.70 | 3,429,902,843,904.00 USD | -0.52 |

Peers fetched as_of: 2026-11-02; AMZN reuses existing data (market data as_of: 2026-11-02); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-29
- Next expected earnings: 2027-02-04 (yfinance; expected dates may change)

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
- Filing date: 2026-10-30
- Revenue (latest available single quarter): 201,944,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 20,685,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMieEFVX3lxTE5TRVJ2ODRjSDRoWUtreUFjYkJONzY4VFMyUE5GVy0zaS1lcHFVaFpOQnlkTVFXTkhTYWVIRFNJZUlIbjNUcEhjbWFfTHlRVGp3WFE1algzZzdNTVJ1amVaX2syM0piLWI1VEJPTS05OVNNbU5aZjBNZg?oc=5
- https://news.google.com/rss/articles/CBMi7gFBVV95cUxQb29PVHlYM0pGdGtkbXZTMms5UjJjNmFhWGQtVHdJRVBzMWdFem9aOF9fYU1YQWxNaTktZWpqMHJ4X0tZNV9EQ2taYnJvU05TUElfTVREMmpkSHhpdTVyRTdBRDg4TjVIR2l0S2VGeHc0YzhrWUxXQzgzSlVVcUZIc0R4djhVQkQzbWVpcDQ1X1RQZk9zcy1qbWxZYkk1M1dPemJSd3VLQWg5dG1mYUdPTFQ2X2xEckVFd2V2cGJOa3k2cnR5TkJBTWF4NVY2VGtjUjZUV3ZEOGJWSHlmbFpCU29hUUhmYzE5VWRVMHJn?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQQlg2eVlHWDl0QUpwa3MtZ2JBVUVMOXd6Y0xzSlNSRTMyRGl2SmRRZEhQNTRsS01vellzQ3NvSm1GYUNNbmZiRUlaOTYwaHFuejRiajNOTmxLS2lJT1J1Sld6NXp2ajRMUlRheHcxckw1OHhHdVFHSW9fYnVXdkVWNmdFeGI5UFh5OS1CM2VUQ05KODhXZlhvSTJR?oc=5
- https://news.google.com/rss/articles/CBMigwFBVV95cUxOUUcycHJPVi1rV3dqc1N5LWEtbmJhMW1ZWjI4MWxXdy13NXBEWnBKRG5vUGl6U00tOEVlNVk5T2p2a2ZkdGcwUEpBR1hETE9zVVREZnNOZ1Q5amF6SHdDLVR4Yzh3STdDeGhJMFBRRkhKVmZlVmJudFF1R2wtNGFLcGh3UQ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNS0Z5Z1RsdUJFdHdXdzNnbC1hVXZlYVB4SlQteXNpeFZxNUJMS2VNZVBuLXZFdzd3aHJWQzZOZk1tZWMxWWZNVUNWc1QzdGJPQ0c4bndHczk2M0xPeFQwOWNRMGlic0NXTjFnZndlZEozVElKemJmQ18yRVUxcmVDR2hzalUydTY4RkxHQm1wS0ZxUE1mdmhYSUNEdw?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxNZTRnSk1vYUtiQlJ0YVdWUEVMQm5mMFZfbjc0T1hwZDFLUjR5THFrbTFzanhGNUhIYV8wV2Vpa2FRTXFRcTRsanphR1ZSS1lHMjQ3QkoxVlhYSmo3QkFWS29fa1VHaHlMVVpCV21GcFpaQVBaLXhvd0wzbWFSRFZTNG5rdnVfM3lOTnVBaHVWSmU4MlIwYzI0WU8teXN0WTl5Q0pJ?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxOdDBxcVFnZUY3UVczSkJGUFdIOXJweEg4NURlT09tRi12MThQQ1Y5Rl9CcUtzMWJUdDJHWnpHTWV6R015R194ZXE1cmtLZXprZGZnSWJFNndveUpBWU9sMTFwYkxPYTdib3JlOGVSSHVUalB6THFlOGFnckN4WWRLSmhYR1QzX0ROOHc?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPNHU1TE9TbnphOU43d1JrYXAzajZKZVVuQkF6TThNQVhJUmQ4RmU1U2RTUnpPYmQ5UE9tS2ZnenNTcWhyTVpGTkFCem5jeU1mZkl2QUJhTENCMDBKOGJVTnJGSTE0UmUyblhZQnM0UGxyVk1NZUVMbVp5cEhzTmdhanA3eUtLaEozTTAzRmhmSmZ1M1FRbEhPaEl6cVBIRGIzSVJ3?oc=5
- https://news.google.com/rss/articles/CBMif0FVX3lxTFBUejFDcXJiQ0NLMHd5alJ5Znp6N1h5X0ZqaFRDNHpTQ0cxenJOZHVBLS1ReDA0Rm5GMHg1NXRrOWVGYl8wUU9HZm13TUR0SmNqQU1PR3hMQTNYaC1oelJKUU55QnExUVVoV0hta204RG91VDZWUUhOVWZpT1FmNWs?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOMHVOOUNrejV0ZnJZZFhTWGhHRDFVN2hwd2djSHZDbFR0aHZhdlVZSy1rcWN5eVJzYWlJRURXN013em1KVS1lNkNVQ0wybEllb0h0dnZHajhYUjhKTFIzQjZMS2ZYb0FJQm5kcjVmOGNBOFllYWYyT2hXTVh1cmFoY1d6eENfak9XcUpCekdxSHZyaDMyQ2c?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQdVZfYkpFaURIalAwZHlsWjJ0RGJlekJJNjBUWFEtbThRUkhxQVpFMk5ieENxZzNFZlpOd2s0VG5TSkpHaE5hS190bXMtb2JkeGQyRkJ5Z2JOcnE3UEdBUUFhVmRQMzFQQlVXcVBEUDdEczUyZllrUUtoV2JxTE9QS1ZLUmVtSmk0RmhMcmMwTEtaZmxaV2M1T0VOdw?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxQQVNlTDBZVzFmVkpRZTdJYWlGRGR1VkZsXzBTM1ljc1JLNmx3MG5GdGREblh0NWpaQ0k1R2VXc29UUEdpSlZoa1RXaW1MTjdGSFpRRTYxRXkxVWFLb3NKVUV0N21iMVQ4dG9DMkJvLV9TT2JLQ2otaVNwck9meVlWdEUwT09YZENCTTZkU0xXV2dMUHBWcHF0XzRVNWFMY2xZUVdITFlPN0xVWHhibU15NE9GWF9QMVdH?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxPYnZtTWxaSGhHVEIxZ2xxcHYxdFBVSUJVRXNPaGJBMlBoVnZ3UmdDWGZyV1dUV2ZsaTZCcHc0MGpRR091NElxcWdoVDF4MHloaUdTbG9fOF82ZTU2TmNKQWxFeHIzS0hNaW1ia3lMTVhMWVhOelJjMWlPRXFwN3BGclVaZzBHWDdyYWYwWVNqelZUMHhRX091c1ZGRDFKcVRHZzh0TERvUG82cVJyMWJKYkhRZHpJLXpkbUhOYWNHZUFWMm1rdFdLWklLYzcxZTU5TkdMeE8xZVBTWFRQbG8tWTY5Vi0wZzZsZ0I1Vw?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQTVVnNnFNVEt1SnlTWEVYSWVTam9lZEgwcUwtMG8waUZCVDNxVkVRZDBuOFlfQjFvZkRVTHlobzlaakJreUNlSjIxcXIzVjd5X3Q3YzBGUWlkeFdRYmxxWlNxc3J2YVZNQ2V6WUhvR0JwSTVlOEZqMm54R2dUb3FGb0RmaE5qSC1WZXZyS3R5LTR1V1kt?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxOTU11b201VGNET3J1SXBfbmJfekt0aWhyakdicUJkYXdoTDRvSk5ibjFUenM1N0ZjTU4yeDBoTlNIdmhSU3hOQ2ZEeWRhVUh0SUstSWtjMDh0ZHgtWFk4ZTU3WFpfcDBSS3NjVGpydXRRTnNZdzlINkN4eVh2dXJyQXF0bWlFRWpsdFRJM1dtNU0wcFR3MzQ2R0hVY1JOc1hxRWdTZA?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQMTBOdW1vN1RWbkxOVXY0bl96c1U5R2hPbE12Y2VJdkJySDRfeDg5ZjRUOWpSb3c0WjdTWVdEME4tdkhjenlJOTlsa1ZFWE0tQVo5REtZRWZWOXBfeUtYaDVQSjFYZmFoTjgyZDdYejNXTFlQV21QWmtnRGhJVVVkNHhCSDR3VkxOX2xpdFJzbzZ3MkN6NE1OSlBMZGh1eFc3NlF1TTFIN1U?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOOTlFYkZ6X0hrRy11VDRkcGQxVzVpMXJETFpLSkZ4aUxfLWVTVEp1eDdsQkFXUGg3TWlLcUQ2dVBOLUkzdkVBM1ZVNkE1ZjdGWnk0b25VNFNLcEE0TDJKbFVweGJfYy0wYVJMVmxULXdhN2laYjRlekJZdXNTY2JXZ2l2bWwwVHdyOUNLTmt3VWY4MWlISDF5Qw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
