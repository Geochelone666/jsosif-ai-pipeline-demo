# NVO Intelligence Report

- ticker: **NVO**
- Report as_of: **2026-11-08**
- Market data as_of: **2026-11-06**
- Quant sources: https://finance.yahoo.com/quote/NVO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVO/key-statistics/
- AI analysis snapshot as_of: **2026-11-08**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-09T04:37:16.376651+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 7, 'ai': 13, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **12** exact headline/source/date matches; prior report **20261108T041758Z-43fb2458/NVO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 10 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 34.78%; oldest publication 2026-11-01

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 40.3100 |
| Return 1D (%) | 0.0248 |
| Return 1W (%) | 0.7750 |
| Return 1M (%) | 7.4074 |
| Return YTD (%) | -16.8193 |
| Return 1Y (%) | -9.0038 |
| Annualized volatility (%) | 45.8691 |
| Beta vs SPY | 0.9494 |
| Max drawdown (%) | -43.6699 |
| Sharpe (rf=0) | 0.0272 |
| Downside deviation (rf=0, %) | 33.9957 |
| Sortino (rf=0) | 0.0367 |
| Historical VaR 95% (1D, %) | 3.1060 |
| Historical ES 95% (1D, %) | 7.1674 |
| Correlation vs SPY | 0.2804 |
| Tracking error vs SPY (%) | 44.0337 |
| P/E (trailing) | 10.18 |
| P/B | 5.43 |
| EV/EBITDA | 1.46 |
| Revenue growth (%) | 5.60 |
| Forward P/E (estimate) | 11.91 |
| Gross margin (%) | 83.33 |
| Operating margin (%) | 40.05 |
| Return on equity (%) | 58.38 |
| Free cash flow yield (%) | N/A |
| MA50 | 40.5846 |
| Close vs MA50 (%) | -0.6766 |
| MA200 | 42.9529 |
| Close vs MA200 (%) | -6.1530 |
| RSI (14, Wilder) | 52.8182 |
| MACD (12,26) | 0.1482 |
| MACD signal (9) | -0.1942 |
| MACD histogram | 0.3423 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVO': 277, 'SPY': 277}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 40.3100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.0248 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.7750 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 7.4074 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -16.8193 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -9.0038 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 45.8691 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 33.9957 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.0367 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.1060 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 7.1674 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2804 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 44.0337 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.9494 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -43.6699 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.0272 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 11.9093 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 83.3330 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 40.0530 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 58.3840 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 10.1793 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 52.8182 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.3423 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -0.6766 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -6.1530 -> Clearly below the moving-average trend level.

## TAILWINDS

### Novo Nordisk shares jump 6% after lifting 2026 outlook on obesity-drug demand
- Summary: Novo Nordisk shares jump 6% after lifting 2026 outlook on obesity-drug demand
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPZ1hVc0t3Tl9lYVhsT3BnYnRZSjNFMHZ6bnR2N19hUXF4ZDA5cGg1RlR5a1NzcHREQlhKMDF5QldvRmd0akVFYTVvbU1lSW8wU2o0Y0RVeTVmcndkdmZLbE1oYWp0dFFRRTVZSHJqOVhjNUo2SFlpckxRRWRqS294YWVzN2F5aW1wTndYYTUxTkNnOVdpZjlCQQ?oc=5>

### Novo Nordisk AS (NVO) (Q3 2026) Earnings Call Highlights: Obesity Sales Surge 22% as Wegovy ...
- Summary: Novo Nordisk AS (NVO) (Q3 2026) Earnings Call Highlights: Obesity Sales Surge 22% as Wegovy ...
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxPaE1GMVU5S2FzZzR3OVFvOU05c1Bta1R0VUlRQXZQTXM0S242elM4ZllLd3h5MVhFQTI5QVNxMjRjYzRxM2o5d0FuanV4Z25PSG9nWWVMX2p2XzJCRkFvWC1icUNya1ZjQnB1dU1iT1NjRnBGMTlna0xtRnBfUHBkcDAxYzZSZTBUZTc2QmJn?oc=5>

### Novo Nordisk Stocks Rise 5.65% While Higher Guidance Meets Diverging Profit Measures
- Summary: Novo Nordisk Stocks Rise 5.65% While Higher Guidance Meets Diverging Profit Measures
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxNNWlBYzJsdjNrckRCVWZYQUJmbWFhX1pwSlRtRjRzZDFOMWNjZUZYWTJjRmJoNjNIMzBpb2k2TG1YWWxhYzRSZ3lIV1p0NTh3akp5anExOTdwQ0hjekhHdUU1Z0twNGFESkszMDE3c0ZSMUZleXZteHd5SlZoZ3VwMjF2ejBFU2FlRHJObzdMWGY?oc=5>

### Novo Nordisk Stock Jumps 6% as Wegovy Hits a Stunning 80% Milestone
- Summary: Novo Nordisk Stock Jumps 6% as Wegovy Hits a Stunning 80% Milestone
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxQVmVmUEUzalZRY3YzMjBaQVRYb2ZDTDV3ZHp1aW1EcVVvdUNWcGlScnhuQWJ6Ym9PUnFKbldXNFlkZUFFbjdVdUREajZhdnZ3SjB1WkFvNExZTEZTZC1lV05yS2tNNnFzazB2VXk4WFhNUVhpcGpnYmc3WnBlZk0tamxJNjZLRWd5OHJOQzVDRGVTbldKSnA4cUFqdXAxVW5CcmgzUTU2Q2JvRXlsQnc?oc=5>

### Novo Nordisk upgraded to Strong Buy on strong Q...
- Summary: Novo Nordisk upgraded to Strong Buy on strong Q...
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPT2NvczhHVlZVNVdFZkp0eWZ3a2todmh1dEE0ekpOUm9iYjhQYUtvOE5fVzNfZ0xPbjczNHVXUXA4MHVsdG1vWkhLTEpFZlBiaExQdjNwMkEwaWRkSE9takRuNUJSaWZFbGtLOVljeEMtN0JPM2YwRmNtbGZuQ0IxenpiY2c0M1cwWTZHSENqX3ZNQmRlTGpwUmhSQUdWbzA?oc=5>

### Novo Before Q3 Earnings: How Should Investors Play the Stock?
- Summary: Discusses investment strategies for Novo Nordisk ahead of Q3 earnings.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNUzA5WnJrQWxMVUZiZHhxQzU1WER1Z19qbWFwcEUwbFBsMVAzUkZxWHRoNkhfS0E5ckNKbTh1SWVaS19QWVY4ODJmNTdZV0p5amtXMWF6dDBTMzNyX1FnVVlLVGtWMGVHMlhpdG0wR3lUUkNfVXY4cnBwUHBWSzZjNXU0UFdhckdPT3JOOV9WRnE0a0hZaUUyZGthWlI?oc=5>

### Novo Surges After Crushing Forecasts On The Back Of Its GLP-1s
- Summary: Shares jump after beating forecasts, driven by GLP‑1 sales.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMigAFBVV95cUxOY1RLNmt6NDB1UVpqR0dRdGpsaFFYNkgxUnNzc2V5dzkyeW41T0hnSUVhbkhiMjFVVGhscTB1Y2ZmZXotQmNqTF9xbFExYWE2YldEZjFMQzZyckpuU1V5R3FEUVVTMlZvNDJGQm1kcXU4QVpXWU9GS3hCRDFpX2lWUg?oc=5>

### Novo Nordisk (NVO) Could Be 47% Undervalued On Obesity Pricing Debate
- Summary: Valuation upside potential highlighted amid pricing debate.
- Date: 2026-11-07 | Impact: high | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxNYmNia2dObzdWM09mVVhYX09SREI1RGs0d21vVzB5WFpEZGhOTnpoNi0tUmFqOEZ4VGVMSWtWU3V5eXFKYVVIbXE1V1BaRXJSdC1JRkdTSEJDUkE1WnBLWnU0UktkVU1PT3hRRGhtZ28zZEZZVlJCZ3lnVVhmN2hDZXZvczc1d0hCMUNFTERRb0lkZ1lVRGpFZWlmbUo5Mi1mY0FGbzZKYXJsWWlxR0ZMdVFheFdtdUk5ZDI4NUN3dHJPTUp5RGtWOEZ2S3dWV3gxTFhBRmN3N0N3Z9IB3wFBVV95cUxPd2ZJaHYtU2FVOWg0UFVvWDJJSWZkdUlPWVlnaTZPQ3R5UWw4VmlDelZBYm5YUEVDV1FHMklzbnNkUzhEUXo0V2pCUURlbWl6VE9id0xZY0dmeGU5cWVQWTV6MmNneFk2YnNRWWJraGNQNlNrYlpHd0lsQlNSdWM0R1FvZlI1TGxmN3lkeHFQbE83c09hZVpOTW9vQUJNb0JpNV9jOVI0aXFCOEdKSmUySEt2ODZBOHZYVDZ1M1pwcmNnQ2ZvWEtUcEZoeTlEdFBvcXdqZ2RCMVVvb01MZ1dZ?oc=5>

### Novo Nordisk's Wegovy Pill Has Topped 5 Million Prescriptions. Is the Stock a Buy Now?
- Summary: Wegovy prescriptions exceed 5 million, indicating strong demand and potential upside.
- Date: 2026-11-08 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNWmM2eU5IYTZOaXduRE5vaFpYcUlQNmJIb0xzeTZPcGtIMDVFWk13TUhpWkU1aE9Cc0lQQnRhOUwtMUpmS01LcW5paEw1dllJLXdOUWdkWXJXNlJfTmlOR05Ma2tJTmZOQ0xkZ056RExFVGhYODRFcnRNakZPZ0s0RFZRTG85My1kX0RsTEk5V0NnZlVvTVVCaA?oc=5>

### Novo Nordisk Owns The Oral Weight Loss Market At 7.8x Operating Income (NYSE:NVO)
- Summary: Novo Nordisk dominates oral weight‑loss market with 7.8x operating income.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQTGd2UlczdTBsWVFoUDR2WjVSemxablRhaDFtTkw4LTBTYzVHUE96b190LUJlRXZENmtHVkJXaU1GekJKdVFLY19xLVpBbFUzRExGOGtvWUtHcXc1OUZtdkstX0k2MjlxeG9WVmdRdW1SZUFXOE9sTGZKLWw3SjAwSzhMaXY2ZmRaaDRremE0M0Z1ZldVTWlEZGlkRzR1Ukx2RFFwdkt1LVlTUFJLSXVmSg?oc=5>

### Novo Nordisk: The Recovery Is Gaining Traction. Here's Why I'm Staying On Hold (NYSE:NVO)
- Summary: Analyst notes recovery traction but remains hold recommendation.
- Date: 2026-11-05 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxOZUQxZ1JZTUZIZy1WZ01MMzdLd0dCZS1LdV9aazV6V1JhcVUxWHpMMGwwdEltWlRuUUxEWk9xRnUybEdwei1ObE90RFZabElxaVVzNWw1MTNnSF9kZTNiSVU0YlNmUHRxaW9ZcnFRUk1BSHpTRUlud3RNVkVScTdyNWZnLWlHd1F0enFxdndtSHVmV0ZQYjdwNVlwUFFkNzBMeVlaNG0zZU5KcHg0dl9sQXp4RjhVUQ?oc=5>

## HEADWINDS

### Novo CEO Brushes Off Post-Midterm Drug-Pricing Fears, Says ‘Our World’ Won’t Change Dramatically – NVO Stock Gains Pre-Market
- Summary: CEO addresses pricing fears, stock gains pre‑market.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxPQ2tNRXNjVmJvRWVmcVo2V2F5UUhKZ2k5R2tUMU5aWDNaQnNQSG9NUXRKMHY4Rm5mLURoSXpsVVlsVU16OHBmaHBYZjRnU2xXMWhvTjc0blpWd1d2eXNwUXFkWXA5TDBhZHRvUy1JTk5HSGNYeWNTRzJBempLRkpMZ0pIVHBMSjBrTWlEUHFDaw?oc=5>

## CATALYSTS

### Stocks making the biggest moves premarket: Trump Media, Tesla, CoreWeave, Novo Nordisk and more
- Summary: Stocks making the biggest moves premarket: Trump Media, Tesla, CoreWeave, Novo Nordisk and more
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNbVRCTEpta2pxRWE4NkRKdlVFb3hOZmJReEp5MDRSRTRXVEZUdi1qMnlJT3o0aURDNFBaVy1Hc09JOWJ3ZW1uZWFNVzVxNGdWck80TW1VVG45MzJSQXkzcTBSaS1nYUZqRW1UOENuZnlTSkJESFJja3N3WE43NTZYcWVQcjJTTW95ckt5Z1M4WGhlQTJqOXhDcm12TG4?oc=5>

### Novo Nordisk Trades at 10 Times Earnings While Buying Back Billions in Stock. Is This the Bottom?
- Summary: Novo Nordisk Trades at 10 Times Earnings While Buying Back Billions in Stock. Is This the Bottom?
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQRkcxLUFGd0VDS2xKVmI4SlZhOHpqT1NjV2VRVGU2ekdvVnVIOWx5cWZLT19HNWdxTXN4Wk11MEVLaVkwN2lVR0tjTXRSNXd5MGxvLVJXb0dPUlhmNHhydDlGSzhvR3lYdzkyYUFiOG9Wb3VndE96R09TVVhySjkyajhBTGNNWHRJLVJxbHA4YmphRHpMT0p5cA?oc=5>

### Novo hikes outlook again as it speeds up Wegovy pill rollout
- Summary: Novo raises guidance, accelerating Wegovy rollout, boosting future revenue prospects.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQUXNSTmhfQVhISGNaNGRPM1A5R1hwalZvbm93d3lkc0thd0dZMGdLZ3h6WTI4NnVQeGxZYVdhc2IzY3M3UXUtMlBQVmtZWlMtQmhDYXhCZ1JuREQzZlhwQVVRR0tiTEZybndZdHBKbG5ZcXR1c2p6Tm5yNHRXYVNNVUs2VjViQVB6dWc3c24tTHd3UkNRN1NIdXZ1alB3TkljNGNXSUZn?oc=5>

### Novo Nordisk Q3: Just The Report I Was Waiting For (NYSE:NVO)
- Summary: Q3 results exceed expectations, highlighting robust performance of Novo Nordisk’s product portfolio.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPX1dlSENZdEQ4NkstUlB4c0xBbkpzbFdvZmdwdkRsX1hyZ1ZaUU90Z19nUUtxZFJydC03cFA4NHhBNE8xeFFUWUdSS2VfRmZJb1NSaTFnczJKNlk0RDl1eXRmajZQMGNEc1kxdHl6V1JsaVRfakFCc2xZUHpIRDNObnlISnNid3ZocU9XWkdicmF1X0hP?oc=5>

### Ozempic maker Novo Nordisk's R&D chief sold shares worth 3.42 million Danish kroner.
- Summary: Insider sale of shares by R&D chief.
- Date: 2026-11-05 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxNTlZGMkhPQWNxclIwZXhpQTBEcVJOMlNJdzlPTDZmOE93MEh2Q2Jha2RVRDlNcDYyUDV2Z2xyWkRUUENSeVp1Y1JwN3VtVmxWZW1uSWwxLW9oTndiZFdrUnJ5NXFjX0lRNjFzSmthMHh5N0JUMkVYTTN0Mnc5bHhHVk1BWlFlTm4zZnlwZWxhNW5YVk1JbUdaRWFDRFl2VUZ0LW8zSkowTzdvZExwWmlnZVRRc1NVMThDeEE?oc=5>

### Novo Nordisk set to report Q3 results as investors watch GLP-1 sales and outlook (NVO:NYSE)
- Summary: Novo Nordisk will release Q3 earnings, focusing on GLP‑1 sales performance and future outlook.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxQa2RjU1ZTM25sSHg5WWJmU0lHaVh4U0NYbk5ZazVPanBuOVMxSHpGUVQyWWNrUGFaUThjd0lYM0pkZlFqWDhYNTA5VVBYNTl6RFJNM216OUVobmZCVTJ0TW5Xb05ORi1mUF9rZUFQTVBoOW1QbXhJUmFfTVlnYzZXZVk3SWFiZVlaNE1Dc1VOSHZXNHg0anJqZjFKaXptdlBZalR1TDVBVEk2VmxDbmVXM2RDb2hHZGVFa2c?oc=5>

### Adjusted operating profit was 31.7 billion Danish kroner; reported operating profit was 23 billion at Novo Nordisk.
- Summary: Operating profit figures disclosed, higher adjusted profit.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxOX3l1X005VEQ4T3VVMHFVNDZFekM4b1lHQ3JReUVjQjFnU1B4aXpCQWRNQTVLQUJoNm83bE1GZGFEbnZrV21RX1J2VFhNaXJ6RXByai1XU1RZcUtsU0h0R2E0MVZnREMtaFpSeFo0UUxodFdIeEVLRkJTdWx3MjczaFBGTDluTURicnNyaEhPNUZNZkhOZlZVRmFTd2NVa0dFT0ZTYTdGZ3dmLVdRNzJpX3RpT0Q0NE5TVzdxZHAyVQ?oc=5>

### Wegovy linked to 18.9 pounds of average weight loss in six months versus another treatment
- Summary: Study shows Wegovy achieves 18.9 lbs average weight loss over six months compared to another treatment.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxNa3FDOTVPNUdvSEdsWHlsTVdDeHRjaDk5eU9TMW5uQjlQZ1M0dFp2NnQ5RDdCRGR2dUhjX05HX2p6RUJaZUZKWFc3UWt0ZmVoMEE5ckFYSWJ0X1FaUWZfazIzdVdOX0N2N3lUOENVYlJqOFJwYXJhZVlnU25LcGpoVGZPc3VrN1Jjdi1lcWlHczRLNWF1Zlp0MVJ5NVJoTXFNSG1UTGRWTXFWUzdyVktFN0NvYXNYZlYzR0dV?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVO** | **10.18** | **5.43** | **1.46** | **5.60** | **177,736,679,424.00 USD** | **-9.00** |
| LLY | 43.95 | 29.96 | 26.90 | 38.60 | 1,206,068,707,328.00 USD | 45.35 |
| ROG.SW | N/A | N/A | N/A | N/A | N/A unknown currency | N/A |
| SAN.PA | 24.20 | 1.38 | N/A | 15.70 | 100,326,277,120.00 EUR | 3.28 |

Peers fetched as_of: 2026-11-08; NVO reuses existing data (market data as_of: 2026-11-06); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-04
- Next expected earnings: 2027-02-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-08

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: N/A
- Filing date: N/A
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: N/A

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimAFBVV95cUxPZ1hVc0t3Tl9lYVhsT3BnYnRZSjNFMHZ6bnR2N19hUXF4ZDA5cGg1RlR5a1NzcHREQlhKMDF5QldvRmd0akVFYTVvbU1lSW8wU2o0Y0RVeTVmcndkdmZLbE1oYWp0dFFRRTVZSHJqOVhjNUo2SFlpckxRRWRqS294YWVzN2F5aW1wTndYYTUxTkNnOVdpZjlCQQ?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxPaE1GMVU5S2FzZzR3OVFvOU05c1Bta1R0VUlRQXZQTXM0S242elM4ZllLd3h5MVhFQTI5QVNxMjRjYzRxM2o5d0FuanV4Z25PSG9nWWVMX2p2XzJCRkFvWC1icUNya1ZjQnB1dU1iT1NjRnBGMTlna0xtRnBfUHBkcDAxYzZSZTBUZTc2QmJn?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxNNWlBYzJsdjNrckRCVWZYQUJmbWFhX1pwSlRtRjRzZDFOMWNjZUZYWTJjRmJoNjNIMzBpb2k2TG1YWWxhYzRSZ3lIV1p0NTh3akp5anExOTdwQ0hjekhHdUU1Z0twNGFESkszMDE3c0ZSMUZleXZteHd5SlZoZ3VwMjF2ejBFU2FlRHJObzdMWGY?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxQVmVmUEUzalZRY3YzMjBaQVRYb2ZDTDV3ZHp1aW1EcVVvdUNWcGlScnhuQWJ6Ym9PUnFKbldXNFlkZUFFbjdVdUREajZhdnZ3SjB1WkFvNExZTEZTZC1lV05yS2tNNnFzazB2VXk4WFhNUVhpcGpnYmc3WnBlZk0tamxJNjZLRWd5OHJOQzVDRGVTbldKSnA4cUFqdXAxVW5CcmgzUTU2Q2JvRXlsQnc?oc=5
- https://news.google.com/rss/articles/CBMiekFVX3lxTE52NVRvcmNObFYzXzFiWDZpeUN1SjlWV0dFTl9GbFJKUU5tc0FmVUpXLWs0X3JXNkIxd1JqSnJkUHRkNzZxWl9abVFkcG1Ubm5WLUVSZ2lQdkYwUTZnam41aGRXRGkzcXF1TXRYZ3g3dGNKSWdKczV4ZWNn?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPT2NvczhHVlZVNVdFZkp0eWZ3a2todmh1dEE0ekpOUm9iYjhQYUtvOE5fVzNfZ0xPbjczNHVXUXA4MHVsdG1vWkhLTEpFZlBiaExQdjNwMkEwaWRkSE9takRuNUJSaWZFbGtLOVljeEMtN0JPM2YwRmNtbGZuQ0IxenpiY2c0M1cwWTZHSENqX3ZNQmRlTGpwUmhSQUdWbzA?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNUzA5WnJrQWxMVUZiZHhxQzU1WER1Z19qbWFwcEUwbFBsMVAzUkZxWHRoNkhfS0E5ckNKbTh1SWVaS19QWVY4ODJmNTdZV0p5amtXMWF6dDBTMzNyX1FnVVlLVGtWMGVHMlhpdG0wR3lUUkNfVXY4cnBwUHBWSzZjNXU0UFdhckdPT3JOOV9WRnE0a0hZaUUyZGthWlI?oc=5
- https://news.google.com/rss/articles/CBMigAFBVV95cUxOY1RLNmt6NDB1UVpqR0dRdGpsaFFYNkgxUnNzc2V5dzkyeW41T0hnSUVhbkhiMjFVVGhscTB1Y2ZmZXotQmNqTF9xbFExYWE2YldEZjFMQzZyckpuU1V5R3FEUVVTMlZvNDJGQm1kcXU4QVpXWU9GS3hCRDFpX2lWUg?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxNYmNia2dObzdWM09mVVhYX09SREI1RGs0d21vVzB5WFpEZGhOTnpoNi0tUmFqOEZ4VGVMSWtWU3V5eXFKYVVIbXE1V1BaRXJSdC1JRkdTSEJDUkE1WnBLWnU0UktkVU1PT3hRRGhtZ28zZEZZVlJCZ3lnVVhmN2hDZXZvczc1d0hCMUNFTERRb0lkZ1lVRGpFZWlmbUo5Mi1mY0FGbzZKYXJsWWlxR0ZMdVFheFdtdUk5ZDI4NUN3dHJPTUp5RGtWOEZ2S3dWV3gxTFhBRmN3N0N3Z9IB3wFBVV95cUxPd2ZJaHYtU2FVOWg0UFVvWDJJSWZkdUlPWVlnaTZPQ3R5UWw4VmlDelZBYm5YUEVDV1FHMklzbnNkUzhEUXo0V2pCUURlbWl6VE9id0xZY0dmeGU5cWVQWTV6MmNneFk2YnNRWWJraGNQNlNrYlpHd0lsQlNSdWM0R1FvZlI1TGxmN3lkeHFQbE83c09hZVpOTW9vQUJNb0JpNV9jOVI0aXFCOEdKSmUySEt2ODZBOHZYVDZ1M1pwcmNnQ2ZvWEtUcEZoeTlEdFBvcXdqZ2RCMVVvb01MZ1dZ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNWmM2eU5IYTZOaXduRE5vaFpYcUlQNmJIb0xzeTZPcGtIMDVFWk13TUhpWkU1aE9Cc0lQQnRhOUwtMUpmS01LcW5paEw1dllJLXdOUWdkWXJXNlJfTmlOR05Ma2tJTmZOQ0xkZ056RExFVGhYODRFcnRNakZPZ0s0RFZRTG85My1kX0RsTEk5V0NnZlVvTVVCaA?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxQTGd2UlczdTBsWVFoUDR2WjVSemxablRhaDFtTkw4LTBTYzVHUE96b190LUJlRXZENmtHVkJXaU1GekJKdVFLY19xLVpBbFUzRExGOGtvWUtHcXc1OUZtdkstX0k2MjlxeG9WVmdRdW1SZUFXOE9sTGZKLWw3SjAwSzhMaXY2ZmRaaDRremE0M0Z1ZldVTWlEZGlkRzR1Ukx2RFFwdkt1LVlTUFJLSXVmSg?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxOZUQxZ1JZTUZIZy1WZ01MMzdLd0dCZS1LdV9aazV6V1JhcVUxWHpMMGwwdEltWlRuUUxEWk9xRnUybEdwei1ObE90RFZabElxaVVzNWw1MTNnSF9kZTNiSVU0YlNmUHRxaW9ZcnFRUk1BSHpTRUlud3RNVkVScTdyNWZnLWlHd1F0enFxdndtSHVmV0ZQYjdwNVlwUFFkNzBMeVlaNG0zZU5KcHg0dl9sQXp4RjhVUQ?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxPQ2tNRXNjVmJvRWVmcVo2V2F5UUhKZ2k5R2tUMU5aWDNaQnNQSG9NUXRKMHY4Rm5mLURoSXpsVVlsVU16OHBmaHBYZjRnU2xXMWhvTjc0blpWd1d2eXNwUXFkWXA5TDBhZHRvUy1JTk5HSGNYeWNTRzJBempLRkpMZ0pIVHBMSjBrTWlEUHFDaw?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNbVRCTEpta2pxRWE4NkRKdlVFb3hOZmJReEp5MDRSRTRXVEZUdi1qMnlJT3o0aURDNFBaVy1Hc09JOWJ3ZW1uZWFNVzVxNGdWck80TW1VVG45MzJSQXkzcTBSaS1nYUZqRW1UOENuZnlTSkJESFJja3N3WE43NTZYcWVQcjJTTW95ckt5Z1M4WGhlQTJqOXhDcm12TG4?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQRkcxLUFGd0VDS2xKVmI4SlZhOHpqT1NjV2VRVGU2ekdvVnVIOWx5cWZLT19HNWdxTXN4Wk11MEVLaVkwN2lVR0tjTXRSNXd5MGxvLVJXb0dPUlhmNHhydDlGSzhvR3lYdzkyYUFiOG9Wb3VndE96R09TVVhySjkyajhBTGNNWHRJLVJxbHA4YmphRHpMT0p5cA?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQUXNSTmhfQVhISGNaNGRPM1A5R1hwalZvbm93d3lkc0thd0dZMGdLZ3h6WTI4NnVQeGxZYVdhc2IzY3M3UXUtMlBQVmtZWlMtQmhDYXhCZ1JuREQzZlhwQVVRR0tiTEZybndZdHBKbG5ZcXR1c2p6Tm5yNHRXYVNNVUs2VjViQVB6dWc3c24tTHd3UkNRN1NIdXZ1alB3TkljNGNXSUZn?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPX1dlSENZdEQ4NkstUlB4c0xBbkpzbFdvZmdwdkRsX1hyZ1ZaUU90Z19nUUtxZFJydC03cFA4NHhBNE8xeFFUWUdSS2VfRmZJb1NSaTFnczJKNlk0RDl1eXRmajZQMGNEc1kxdHl6V1JsaVRfakFCc2xZUHpIRDNObnlISnNid3ZocU9XWkdicmF1X0hP?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxNTlZGMkhPQWNxclIwZXhpQTBEcVJOMlNJdzlPTDZmOE93MEh2Q2Jha2RVRDlNcDYyUDV2Z2xyWkRUUENSeVp1Y1JwN3VtVmxWZW1uSWwxLW9oTndiZFdrUnJ5NXFjX0lRNjFzSmthMHh5N0JUMkVYTTN0Mnc5bHhHVk1BWlFlTm4zZnlwZWxhNW5YVk1JbUdaRWFDRFl2VUZ0LW8zSkowTzdvZExwWmlnZVRRc1NVMThDeEE?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxQa2RjU1ZTM25sSHg5WWJmU0lHaVh4U0NYbk5ZazVPanBuOVMxSHpGUVQyWWNrUGFaUThjd0lYM0pkZlFqWDhYNTA5VVBYNTl6RFJNM216OUVobmZCVTJ0TW5Xb05ORi1mUF9rZUFQTVBoOW1QbXhJUmFfTVlnYzZXZVk3SWFiZVlaNE1Dc1VOSHZXNHg0anJqZjFKaXptdlBZalR1TDVBVEk2VmxDbmVXM2RDb2hHZGVFa2c?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxOX3l1X005VEQ4T3VVMHFVNDZFekM4b1lHQ3JReUVjQjFnU1B4aXpCQWRNQTVLQUJoNm83bE1GZGFEbnZrV21RX1J2VFhNaXJ6RXByai1XU1RZcUtsU0h0R2E0MVZnREMtaFpSeFo0UUxodFdIeEVLRkJTdWx3MjczaFBGTDluTURicnNyaEhPNUZNZkhOZlZVRmFTd2NVa0dFT0ZTYTdGZ3dmLVdRNzJpX3RpT0Q0NE5TVzdxZHAyVQ?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxNa3FDOTVPNUdvSEdsWHlsTVdDeHRjaDk5eU9TMW5uQjlQZ1M0dFp2NnQ5RDdCRGR2dUhjX05HX2p6RUJaZUZKWFc3UWt0ZmVoMEE5ckFYSWJ0X1FaUWZfazIzdVdOX0N2N3lUOENVYlJqOFJwYXJhZVlnU25LcGpoVGZPc3VrN1Jjdi1lcWlHczRLNWF1Zlp0MVJ5NVJoTXFNSG1UTGRWTXFWUzdyVktFN0NvYXNYZlYzR0dV?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
