# MU Intelligence Report

- ticker: **MU**
- Report as_of: **2026-11-13**
- Market data as_of: **2026-11-13**
- Quant sources: https://finance.yahoo.com/quote/MU/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MU/key-statistics/
- AI analysis snapshot as_of: **2026-11-13**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-14T05:02:07.873781+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 1, 'ai': 20, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **11** exact headline/source/date matches; prior report **20261113T045636Z-34122c9a/MU** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **11**; {'directional_claim_without_event_type': 5, 'low_uncalibrated_model_confidence': 5, 'negative_sentiment_in_tailwinds': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 11 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 50.0%; oldest publication 2026-11-09

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 778.3100 |
| Return 1D (%) | -2.5212 |
| Return 1W (%) | 12.7986 |
| Return 1M (%) | -18.3340 |
| Return YTD (%) | 172.8984 |
| Return 1Y (%) | 228.8432 |
| Annualized volatility (%) | 84.2775 |
| Beta vs SPY | 3.4202 |
| Max drawdown (%) | -45.8952 |
| Sharpe (rf=0) | 1.8374 |
| Downside deviation (rf=0, %) | 52.5115 |
| Sortino (rf=0) | 2.9489 |
| Historical VaR 95% (1D, %) | 7.0090 |
| Historical ES 95% (1D, %) | 10.3312 |
| Correlation vs SPY | 0.5533 |
| Tracking error vs SPY (%) | 77.5703 |
| P/E (trailing) | 10.74 |
| P/B | 6.36 |
| EV/EBITDA | 7.74 |
| Revenue growth (%) | 379.30 |
| Forward P/E (estimate) | 3.75 |
| Gross margin (%) | 80.72 |
| Operating margin (%) | 74.59 |
| Return on equity (%) | 88.26 |
| Free cash flow yield (%) | 3.31 |
| MA50 | 943.6894 |
| Close vs MA50 (%) | -17.5248 |
| MA200 | 765.4167 |
| Close vs MA200 (%) | 1.6845 |
| RSI (14, Wilder) | 42.4539 |
| MACD (12,26) | -55.0053 |
| MACD signal (9) | -53.5923 |
| MACD histogram | -1.4130 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MU': 282, 'SPY': 282}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 778.3100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.5212 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 12.7986 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -18.3340 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 172.8984 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 228.8432 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 84.2775 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 52.5115 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.9489 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 7.0090 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 10.3312 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5533 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 77.5703 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.4202 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -45.8952 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.8374 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 3.7462 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 80.7160 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 74.5860 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 88.2600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 3.3091 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 10.7412 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 42.4539 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.4130 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -17.5248 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 1.6845 -> Slightly above the moving-average trend level.

## TAILWINDS

### Micron Is Rebounding. Goldman Prefers These Memory Stocks.
- Summary: Micron’s stock rebounds, attracting Goldman’s preference for memory stocks, indicating positive market sentiment.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTFB2bWhjUktMQU1qZzVGbWF5ZE9XNmdGVmtUVU5EMUozbl9pNlJRZnJjOWl6N2ZLLUEwQVMyWEZpa19RT1NLMXZzbVZxTTlGd2lKMDNLa3FKSUUwQi1EQllKbndwY20zMUF3Q0tkeHFXSnUwQllJdGhiRjJKY3I2dw?oc=5>

### Micron Technology climbs 13% as one-month slide reverses (MU:NASDAQ)
- Summary: Micron’s stock climbs 13%, reversing a one-month decline, signaling strong investor confidence.
- Date: 2026-11-11 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPSExVYU1oeW91UFFKa2VQNUx1ekRnOGFlVThvR3lGTmtxZnhQSXRsaHl4eG1YV2VGTkdxN0pZOWJmQnl5WTVXWDBaYy1IYjc4cTJ1MDZHVXAtbnZtRF96eXZfSnFVNWVwNl9iYlo1bXBjeV9XcHZmNGotRlJNNEt4al9wSWw0bTFGQXZUMGFfQXprVHhyeFNWM0lEdWJvUUFTRTM0?oc=5>

### Micron Stock Is Down 40% From Its Peak After the Sell-Off. History Says This Is What Happens Next.
- Summary: Micron’s shares fell 40% post sell-off, suggesting a potential rebound per historical patterns.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOc3hPSUpZNHRWLXNkRFpvYzl2YWZ4RDVWeThpUkVLX0Z3aUdmc01GTktyNWw4MHpNWHZaU04tVTkxeG5VLTd2Um1qZGJ5QzFWNzN1MHdZaERSdGRieTdwOGI3djlfVXEyY2hYMTZRT1JFTkZXdFBXZ3dONE9oOTVuRGdYbmZfS2xGbEl2VGlHTlRsQlpm?oc=5>

### I Still Think Micron Stock Is a Buy. Here's the Price at Which I'd Sell It.
- Summary: Analyst expresses bullish view and target sell price for Micron shares.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxNY2stTE5ZNjFmLXlvbkxTMFNzZXduV1BwdDdRRmV6YnBPa2xlWTZqUjhaNmoxb0J0MG10THZQSXBDWEVUWkgwdVpUVE9Zd3dDYlh5aWVrUkZiS3E4LURZbV9xMS1pSlpVU1ZjVnpUbXNIelR6aldwWlVYdFBpWnNkbHplTUFLeEtpNkFmQTkzN1hMN3hwd0lnX0dYang5a3FzQ256SzNELWpwTDhzNl81Vk5oX2ZDbDA?oc=5>

### What Is Going on With Micron Stock on Friday?
- Summary: Discussion of Micron stock movement on Friday.
- Date: 2026-11-13 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPV21XaVk3OHBCQXdGdElzYmNzTUI1ek5pQzF2T1Z5SHRZTzd0MENiMEJBQV9ya0N1Wk91LURJTlRDa1lPZ1lvRklEOHY3QVFCU2tCM19aSENsMjRYalFsRnFxcnlZR3E5M0ZHZHVXdll2OWVRYzBtWkg5WnlDUkVHWXpkdDU1T2N2SXdFOWRDeFNndld3NS1vVEZYN2hrQQ?oc=5>

### Why Micron Stock Was Sliding Today
- Summary: Analysis of Micron stock decline today.
- Date: 2026-11-13 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMigwFBVV95cUxQWm51RHk0MnZpTDZrTWFTR0l5RDJyTVBFWFBEQTNoVHZmQUNxLS1lMTlyNzJKajJkd1RHOW1LRVBPaFR5djF1aUJEV0ZxamlhTTZOUUhBSXVEenMzRVN1S05qZ282V3ZYa0xIa0FJVE52c1NNN08xbEUxaFQ2VXZldkN5cw?oc=5>

### Micron Is Down 20% in a Month. What Will It Take to Get MU Stock Back to $1,000?
- Summary: Micron's 20% drop and recovery prospects.
- Date: 2026-11-13 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxNelVwdm5oMDVMRW1lazFacTZYZXpVTHNKQXNQbjBoREsyUkpBVHVDbnJWM2dHTXdYQTZmVG9hUDR5NjV0c2FoWVFsaExLRXRBUWlGTUhBV0taQkRMbTQtZmpNbzR1TGxaUFNfWHgyM3NyMnU2VWxPTTRpRW0zczEwUm9vMm1Kc2ViMTZBM2MxeVZDQmxTQWR0T0ZRa3pFSmVVS29NczJHQTAzaVZSMUhITTZibjhNamFlQ2pr?oc=5>

### What Micron Stock Needs to Mount a Serious Rally
- Summary: Factors needed for Micron stock rally.
- Date: 2026-11-13 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMihgFBVV95cUxQTnJJSHFKRWJ0S3l2eGZvX1FCU00tM21KUzVnOEtNb0hwSkR5ck1hRkp6UkZ6eUxFblFRdGpQX0ZwUHZ0VXJHOUxMVXVtdThXYTdvR3hoOEZHcXZBQzFicW9pTE5JT29xdFZLdl9qUm1qZnZQc0V5Zl8yYUVEbFR0clhnRVkxUQ?oc=5>

### MU Stock Quote Price and Forecast
- Summary: Current Micron stock price and forecast.
- Date: 2026-11-11 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMiTkFVX3lxTE12OGhUSWtGTk9iWTJqbXhwZ2hpa25tNUxnRWlMam1RYkNBckpUdlVCMXgzY2ZDbG1HUkdxeFlUMWRkZ3ljR2xXUkdJb285UQ?oc=5>

### What Bernstein Sees in Micron (MU) After the Memory Selloff
- Summary: Bernstein analysis following Micron’s recent selloff, discussing potential recovery and valuation.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPdUdkNlU1SG9TdmdNNU9IQW1tZl9lLVBFR1QzNUdUQVl4TzVxY3NfY3VLQW1BWmhpWDNlTjlTUC1rUTlXbEFXYUdmS0dMWHJkOUR0NTR1RXc0X3pGb1VPY0FJSjc5ZU5XbFRTMEJQQXFHaFpPMHZ3a2t0Vmo5c2w1a0FDc2JXZ3RqZlVid1pELVJ3T09OVERoOUhJUnQ?oc=5>

### Is the Micron Sell-Off a Buying Opportunity or a Falling Knife?
- Summary: Analysis debating whether Micron’s sell-off signals a buying chance or a risky decline.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOaFRQSWU0UGg1Z1VnMW5TbnJTdmpYbERtUTRhMUZhX0ZrUXBPLUQzN3RNd3hjbTZtOU1TM2NNaDBjRmlUZi12elJ3SFZwT2N4eEhJem5HX29lNlRCZHhQckF5ZXk4WU9saHozczV2bUVMTHlOcEt0eko4N0hzaXF1eVp6RlBYbk95eTRNbG1lYUlDbUNaWTJXRUhvTkpRMjA5?oc=5>

### Why Micron Stock Dropped on Thursday
- Summary: Explains factors behind Micron’s stock decline on Thursday.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOV0U3WERRLXdqM09NRmo1QVZkMGpRN2xncG5iZkJJTzBrcFhLa0ExNW94UjY0MmlKWUFHMEFmV0xReFNhNThEcTRFbC1VYU5XWVYzWE5RVGljWklmX1VGOEcwWndhd3FZalBCamZGR3lnQjM0cW5oRUVNRnRSazFTcTA3Qmc3UDdBVEpUUU9CZUJfVy13SExFUFAySUptYUE?oc=5>

### Why Micron Stock Popped Today
- Summary: Details reasons for Micron’s stock increase today.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOTTkwM0ZCMklJZklWUmRiT012SUt1QnRDVWQtT2VPT3N0Z2JaZTdxejV0MTRpWVFRTE9QMHQ5VGlOY3VadjI0eGhwN0dUX211VTJxQ2RvZVBPNVQ5NHdaZEwxdEJWTkIweHhta0MybkVMQTFCM3VZT0RhZDVIaDlvOFQ5Nlg2Q1hBUEFwLVBYNmxhdzRZSEcycnhB?oc=5>

### Why Micron Technology Stock Gained On Monday
- Summary: Outlines causes of Micron’s stock gain on Monday.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxNb1hrRzc0OGpMSFBjQ0lmcVpCY3YwMGZ2dFhHSXRaWHU4b0xubTNHaE8yUzBxT3BBQk5xcnZrSHY0QWpKVUdzb1lUMFRldWpSLVpEbFg2QXZRM0ZtN0tKczJnaFJDanlKZmROQWN5SzdnNUU4VEVpamI3WWFLdkpTQmVrQUk4QUpGWXQzUXM4eWtSVG5zU2prOER0TVNXeThH?oc=5>

## HEADWINDS

### Micron Technology stock falls amid sector profit-taking and inventory concerns
- Summary: Micron Technology stock falls amid sector profit-taking and inventory concerns
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPRVZaanVQNm1oR2ZNbERvcC14RlhRSzc3LXM5N1k5cjdHTnVrNnBZa1NPRW1MMDBENXV6UzMxUk1HYUs2VlF6ZXJqbXBRazcxZ2V1YTZPc2NuUlBmenpaU0xCNFJmVkN5YWp4Zy01Um5lVmFLcG9lTFhja1BxMjNOdlRUSUNjcEhhSnpBam5ma0Q0YmsyUE5Ccw?oc=5>

### Micron Stock Pulls Back After 184% Rally. Who Still Owns MU Stock?
- Summary: MU stock retraces after huge rally.
- Date: 2026-11-12 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOakxpTG5idlpTaGhxMEdLM050TTVhZ2VzXy1NMkgtWm9uOVI2SDhLSVJZckhDdUhTUnVMZVZxOEVabDBYcGhKdTZsTTd4LUp3WjVQNGt0enU0dFZpVEh2NG1FYTQwOVNvc1BKRXhIRXV0ZGF0NVV4SEYyR0pqZVcxcGhPc21YeFQxeVJhQ0N0QnA0NzNLbFk1eg?oc=5>

### Micron Technology Stocks Slip 1.27% as Hot CPI Overshadows $1 Billion Anthropic Bet
- Summary: Micron shares fall 1.27% due to inflation concerns outweighing AI investment.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPb3ltSGpYNHg5X1N1VW5PMEJtTk5Ba0hkakhXWjdXOFRvVnp3aGxROFgyWHRheFZxMG1MY1YtT3RXN25hcTgwT2xaUEphbjJrVWI1UHgzZ1VxN1FLNXdjYm1yZTJtT2hjdjJRVDVtR01BT0c3R0RqanFYd1BQdnlRdm1KdktwZ0tOMmNxRndoRWVLSFhlci1MQWNCYU8?oc=5>

### Micron Technology Inc Stock (MU) Opened Down by 3.17% on Nov 12: What Investors Need To Know
- Summary: MU opened down 3.17% Nov 12.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxPVW1nV3ZQWl9BZ1drYWMzZEMyc0hsNXE4N2k3RjdHcE13YXJ2cFdlMnhseFhreTNidjgwcjRGU3htOU5nLVdDVE1BWVlhckFzbXZveDJjUlB0aVRPZHhYWWxLZXdPbWdIaVFGMDZfTTdrWm9pU0hTRV84MVlKS3NOWHdvMFFzczhE?oc=5>

## CATALYSTS

### Prediction: This Will Be Micron's Stock Price by the End of 2027
- Summary: Predicted MU stock price by end 2027.
- Date: 2026-11-12 | Impact: medium | Horizon: long | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQdExhLTYyT2s0OGJycElyRmxOTE1sWjRVRUhRajhPMld4VGNzZlpvSHJzWi1GYTdSZDROdEJZUmJHNU9CaXl6aFY0dTdtZHgtd243Z0M3WnNEemdwWHZUX3d2YjVHZXpaSG95aExpaEV0Ri1henl5akpqRzVRUi1QWG9sVVJ0UFl1OTZndlhPWEczTUhYbEp1Q3MwWjNtWmVp?oc=5>

### Why You Should Think About Micron Differently Now
- Summary: Opinion urges new perspective on MU.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxPcFNnQTlwa05zX0NIRktFcVBSaF9RMTFkVXJUbERZNFlVTzdqM2FGdDkwQVFtdGpnQUhtU2hqSklFb1VLOWkwT1RsWEE2Mzg4cmsycFE1VndieDBjZzJDU0dVeWpwU3VXdlhMNXBtWlRoYVd1YnNIQmEtY2JBVFBpdldSVlFiT2RLeVVYT3dHTGp6bTM5LXFfRVhVYnJPMVNUaC1GaVh2VlZVQTBx?oc=5>

### Micron Technology (MU) Commits $1 Billion To Landmark AI Infrastructure IPO
- Summary: Micron pledges $1B to support AI infrastructure IPO, boosting its AI ecosystem.
- Date: 2026-11-11 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxORC1PS1FreEtDdjc3c0lRUTVvazRVVzBFVkNXYzNMMDBXRGV0R2Nfc1V5cjFlcnh6cHRhanE0a0dUbjByaGNBWExfcmpibDlYc1NoU3VYcjd2SzYzQ0hlcnh6WER0eXZUbHJQRUZ5WG5LS0NTRWxtTG1jcnJnMlVuOFJqaU1TbHg1dTFLLXdJQ21acXZ0MG5IMFZR?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MU** | **10.74** | **6.36** | **7.74** | **379.30** | **880,597,991,424.00 USD** | **228.84** |
| WDC | 10.95 | 11.83 | 17.47 | 55.50 | 110,668,668,928.00 USD | 88.47 |
| STX | 28.59 | 35.14 | 20.91 | 61.00 | 121,274,826,752.00 USD | 102.39 |
| NXPI | 21.02 | 5.53 | 13.78 | 19.30 | 66,816,724,992.00 USD | 34.07 |

Peers fetched as_of: 2026-11-13; MU reuses existing data (market data as_of: 2026-11-13); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-30
- Next expected earnings: 2026-12-23 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-13

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-10-09
- Revenue (latest available single quarter): 8,440,000,000.00 USD; period 2018-06-01/2018-08-30; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 28,243,000,000.00 USD; period 2026-02-27/2026-05-28; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/723125/000072312526000023/mu-20260903.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMifkFVX3lxTFB2bWhjUktMQU1qZzVGbWF5ZE9XNmdGVmtUVU5EMUozbl9pNlJRZnJjOWl6N2ZLLUEwQVMyWEZpa19RT1NLMXZzbVZxTTlGd2lKMDNLa3FKSUUwQi1EQllKbndwY20zMUF3Q0tkeHFXSnUwQllJdGhiRjJKY3I2dw?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPSExVYU1oeW91UFFKa2VQNUx1ekRnOGFlVThvR3lGTmtxZnhQSXRsaHl4eG1YV2VGTkdxN0pZOWJmQnl5WTVXWDBaYy1IYjc4cTJ1MDZHVXAtbnZtRF96eXZfSnFVNWVwNl9iYlo1bXBjeV9XcHZmNGotRlJNNEt4al9wSWw0bTFGQXZUMGFfQXprVHhyeFNWM0lEdWJvUUFTRTM0?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOc3hPSUpZNHRWLXNkRFpvYzl2YWZ4RDVWeThpUkVLX0Z3aUdmc01GTktyNWw4MHpNWHZaU04tVTkxeG5VLTd2Um1qZGJ5QzFWNzN1MHdZaERSdGRieTdwOGI3djlfVXEyY2hYMTZRT1JFTkZXdFBXZ3dONE9oOTVuRGdYbmZfS2xGbEl2VGlHTlRsQlpm?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxNY2stTE5ZNjFmLXlvbkxTMFNzZXduV1BwdDdRRmV6YnBPa2xlWTZqUjhaNmoxb0J0MG10THZQSXBDWEVUWkgwdVpUVE9Zd3dDYlh5aWVrUkZiS3E4LURZbV9xMS1pSlpVU1ZjVnpUbXNIelR6aldwWlVYdFBpWnNkbHplTUFLeEtpNkFmQTkzN1hMN3hwd0lnX0dYang5a3FzQ256SzNELWpwTDhzNl81Vk5oX2ZDbDA?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPV21XaVk3OHBCQXdGdElzYmNzTUI1ek5pQzF2T1Z5SHRZTzd0MENiMEJBQV9ya0N1Wk91LURJTlRDa1lPZ1lvRklEOHY3QVFCU2tCM19aSENsMjRYalFsRnFxcnlZR3E5M0ZHZHVXdll2OWVRYzBtWkg5WnlDUkVHWXpkdDU1T2N2SXdFOWRDeFNndld3NS1vVEZYN2hrQQ?oc=5
- https://news.google.com/rss/articles/CBMigwFBVV95cUxQWm51RHk0MnZpTDZrTWFTR0l5RDJyTVBFWFBEQTNoVHZmQUNxLS1lMTlyNzJKajJkd1RHOW1LRVBPaFR5djF1aUJEV0ZxamlhTTZOUUhBSXVEenMzRVN1S05qZ282V3ZYa0xIa0FJVE52c1NNN08xbEUxaFQ2VXZldkN5cw?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxNelVwdm5oMDVMRW1lazFacTZYZXpVTHNKQXNQbjBoREsyUkpBVHVDbnJWM2dHTXdYQTZmVG9hUDR5NjV0c2FoWVFsaExLRXRBUWlGTUhBV0taQkRMbTQtZmpNbzR1TGxaUFNfWHgyM3NyMnU2VWxPTTRpRW0zczEwUm9vMm1Kc2ViMTZBM2MxeVZDQmxTQWR0T0ZRa3pFSmVVS29NczJHQTAzaVZSMUhITTZibjhNamFlQ2pr?oc=5
- https://news.google.com/rss/articles/CBMihgFBVV95cUxQTnJJSHFKRWJ0S3l2eGZvX1FCU00tM21KUzVnOEtNb0hwSkR5ck1hRkp6UkZ6eUxFblFRdGpQX0ZwUHZ0VXJHOUxMVXVtdThXYTdvR3hoOEZHcXZBQzFicW9pTE5JT29xdFZLdl9qUm1qZnZQc0V5Zl8yYUVEbFR0clhnRVkxUQ?oc=5
- https://news.google.com/rss/articles/CBMiTkFVX3lxTE12OGhUSWtGTk9iWTJqbXhwZ2hpa25tNUxnRWlMam1RYkNBckpUdlVCMXgzY2ZDbG1HUkdxeFlUMWRkZ3ljR2xXUkdJb285UQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPdUdkNlU1SG9TdmdNNU9IQW1tZl9lLVBFR1QzNUdUQVl4TzVxY3NfY3VLQW1BWmhpWDNlTjlTUC1rUTlXbEFXYUdmS0dMWHJkOUR0NTR1RXc0X3pGb1VPY0FJSjc5ZU5XbFRTMEJQQXFHaFpPMHZ3a2t0Vmo5c2w1a0FDc2JXZ3RqZlVid1pELVJ3T09OVERoOUhJUnQ?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOaFRQSWU0UGg1Z1VnMW5TbnJTdmpYbERtUTRhMUZhX0ZrUXBPLUQzN3RNd3hjbTZtOU1TM2NNaDBjRmlUZi12elJ3SFZwT2N4eEhJem5HX29lNlRCZHhQckF5ZXk4WU9saHozczV2bUVMTHlOcEt0eko4N0hzaXF1eVp6RlBYbk95eTRNbG1lYUlDbUNaWTJXRUhvTkpRMjA5?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOV0U3WERRLXdqM09NRmo1QVZkMGpRN2xncG5iZkJJTzBrcFhLa0ExNW94UjY0MmlKWUFHMEFmV0xReFNhNThEcTRFbC1VYU5XWVYzWE5RVGljWklmX1VGOEcwWndhd3FZalBCamZGR3lnQjM0cW5oRUVNRnRSazFTcTA3Qmc3UDdBVEpUUU9CZUJfVy13SExFUFAySUptYUE?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOTTkwM0ZCMklJZklWUmRiT012SUt1QnRDVWQtT2VPT3N0Z2JaZTdxejV0MTRpWVFRTE9QMHQ5VGlOY3VadjI0eGhwN0dUX211VTJxQ2RvZVBPNVQ5NHdaZEwxdEJWTkIweHhta0MybkVMQTFCM3VZT0RhZDVIaDlvOFQ5Nlg2Q1hBUEFwLVBYNmxhdzRZSEcycnhB?oc=5
- https://news.google.com/rss/articles/CBMifEFVX3lxTFAyOUM1OGJlREtsc0h4T2phU0UyamlOdnRSUXRMdzFJWVhzRm9ZMDJTeUo3VXBlZVo1YXdBazFzeWgyRUNpRFRIaHhvOXBGeVdqMWZqby15LXZMZVNZTlhYaW1MSUtWZlhYdGwwRzRELU96RXR4Vk8zZmRRb2s?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxNb1hrRzc0OGpMSFBjQ0lmcVpCY3YwMGZ2dFhHSXRaWHU4b0xubTNHaE8yUzBxT3BBQk5xcnZrSHY0QWpKVUdzb1lUMFRldWpSLVpEbFg2QXZRM0ZtN0tKczJnaFJDanlKZmROQWN5SzdnNUU4VEVpamI3WWFLdkpTQmVrQUk4QUpGWXQzUXM4eWtSVG5zU2prOER0TVNXeThH?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPRVZaanVQNm1oR2ZNbERvcC14RlhRSzc3LXM5N1k5cjdHTnVrNnBZa1NPRW1MMDBENXV6UzMxUk1HYUs2VlF6ZXJqbXBRazcxZ2V1YTZPc2NuUlBmenpaU0xCNFJmVkN5YWp4Zy01Um5lVmFLcG9lTFhja1BxMjNOdlRUSUNjcEhhSnpBam5ma0Q0YmsyUE5Ccw?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOakxpTG5idlpTaGhxMEdLM050TTVhZ2VzXy1NMkgtWm9uOVI2SDhLSVJZckhDdUhTUnVMZVZxOEVabDBYcGhKdTZsTTd4LUp3WjVQNGt0enU0dFZpVEh2NG1FYTQwOVNvc1BKRXhIRXV0ZGF0NVV4SEYyR0pqZVcxcGhPc21YeFQxeVJhQ0N0QnA0NzNLbFk1eg?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPb3ltSGpYNHg5X1N1VW5PMEJtTk5Ba0hkakhXWjdXOFRvVnp3aGxROFgyWHRheFZxMG1MY1YtT3RXN25hcTgwT2xaUEphbjJrVWI1UHgzZ1VxN1FLNXdjYm1yZTJtT2hjdjJRVDVtR01BT0c3R0RqanFYd1BQdnlRdm1KdktwZ0tOMmNxRndoRWVLSFhlci1MQWNCYU8?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxPVW1nV3ZQWl9BZ1drYWMzZEMyc0hsNXE4N2k3RjdHcE13YXJ2cFdlMnhseFhreTNidjgwcjRGU3htOU5nLVdDVE1BWVlhckFzbXZveDJjUlB0aVRPZHhYWWxLZXdPbWdIaVFGMDZfTTdrWm9pU0hTRV84MVlKS3NOWHdvMFFzczhE?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQdExhLTYyT2s0OGJycElyRmxOTE1sWjRVRUhRajhPMld4VGNzZlpvSHJzWi1GYTdSZDROdEJZUmJHNU9CaXl6aFY0dTdtZHgtd243Z0M3WnNEemdwWHZUX3d2YjVHZXpaSG95aExpaEV0Ri1henl5akpqRzVRUi1QWG9sVVJ0UFl1OTZndlhPWEczTUhYbEp1Q3MwWjNtWmVp?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxPcFNnQTlwa05zX0NIRktFcVBSaF9RMTFkVXJUbERZNFlVTzdqM2FGdDkwQVFtdGpnQUhtU2hqSklFb1VLOWkwT1RsWEE2Mzg4cmsycFE1VndieDBjZzJDU0dVeWpwU3VXdlhMNXBtWlRoYVd1YnNIQmEtY2JBVFBpdldSVlFiT2RLeVVYT3dHTGp6bTM5LXFfRVhVYnJPMVNUaC1GaVh2VlZVQTBx?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxORC1PS1FreEtDdjc3c0lRUTVvazRVVzBFVkNXYzNMMDBXRGV0R2Nfc1V5cjFlcnh6cHRhanE0a0dUbjByaGNBWExfcmpibDlYc1NoU3VYcjd2SzYzQ0hlcnh6WER0eXZUbHJQRUZ5WG5LS0NTRWxtTG1jcnJnMlVuOFJqaU1TbHg1dTFLLXdJQ21acXZ0MG5IMFZR?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
