# NVO Intelligence Report

- ticker: **NVO**
- Report as_of: **2026-11-05**
- Market data as_of: **2026-11-05**
- Quant sources: https://finance.yahoo.com/quote/NVO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVO/key-statistics/
- AI analysis snapshot as_of: **2026-11-05**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-06T05:05:30.878545+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 8, 'ai': 13, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261105T045846Z-bde0a1fe/NVO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 13 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-10-30

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 40.3000 |
| Return 1D (%) | -4.4571 |
| Return 1W (%) | 2.9637 |
| Return 1M (%) | 7.3522 |
| Return YTD (%) | -16.8399 |
| Return 1Y (%) | -12.6871 |
| Annualized volatility (%) | 46.0464 |
| Beta vs SPY | 0.9677 |
| Max drawdown (%) | -43.6699 |
| Sharpe (rf=0) | -0.0612 |
| Downside deviation (rf=0, %) | 34.2340 |
| Sortino (rf=0) | -0.0823 |
| Historical VaR 95% (1D, %) | 3.2173 |
| Historical ES 95% (1D, %) | 7.2368 |
| Correlation vs SPY | 0.2857 |
| Tracking error vs SPY (%) | 44.1296 |
| P/E (trailing) | 10.63 |
| P/B | 5.42 |
| EV/EBITDA | 1.52 |
| Revenue growth (%) | 5.60 |
| Forward P/E (estimate) | 11.72 |
| Gross margin (%) | 81.09 |
| Operating margin (%) | 29.06 |
| Return on equity (%) | 58.38 |
| Free cash flow yield (%) | N/A |
| MA50 | 40.7036 |
| Close vs MA50 (%) | -0.9916 |
| MA200 | 43.0477 |
| Close vs MA200 (%) | -6.3829 |
| RSI (14, Wilder) | 52.7663 |
| MACD (12,26) | 0.1241 |
| MACD signal (9) | -0.2798 |
| MACD histogram | 0.4039 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVO': 276, 'SPY': 276}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 40.3000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -4.4571 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.9637 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 7.3522 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -16.8399 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -12.6871 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 46.0464 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 34.2340 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.0823 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.2173 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 7.2368 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2857 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 44.1296 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.9677 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -43.6699 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.0612 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 11.7166 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 81.0860 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 29.0560 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 58.3840 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 10.6332 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 52.7663 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.4039 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -0.9916 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -6.3829 -> Clearly below the moving-average trend level.

## TAILWINDS

### Novo Nordisk Stock Jumps 6% as Wegovy Hits a Stunning 80% Milestone
- Summary: Novo Nordisk Stock Jumps 6% as Wegovy Hits a Stunning 80% Milestone
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxQVmVmUEUzalZRY3YzMjBaQVRYb2ZDTDV3ZHp1aW1EcVVvdUNWcGlScnhuQWJ6Ym9PUnFKbldXNFlkZUFFbjdVdUREajZhdnZ3SjB1WkFvNExZTEZTZC1lV05yS2tNNnFzazB2VXk4WFhNUVhpcGpnYmc3WnBlZk0tamxJNjZLRWd5OHJOQzVDRGVTbldKSnA4cUFqdXAxVW5CcmgzUTU2Q2JvRXlsQnc?oc=5>

### Novo Nordisk shares jump 6% after lifting 2026 outlook on obesity-drug demand
- Summary: Novo Nordisk shares jump 6% after lifting 2026 outlook on obesity-drug demand
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPZ1hVc0t3Tl9lYVhsT3BnYnRZSjNFMHZ6bnR2N19hUXF4ZDA5cGg1RlR5a1NzcHREQlhKMDF5QldvRmd0akVFYTVvbU1lSW8wU2o0Y0RVeTVmcndkdmZLbE1oYWp0dFFRRTVZSHJqOVhjNUo2SFlpckxRRWRqS294YWVzN2F5aW1wTndYYTUxTkNnOVdpZjlCQQ?oc=5>

### Novo Nordisk AS (NVO) (Q3 2026) Earnings Call Highlights: Obesity Sales Surge 22% as Wegovy ...
- Summary: Novo Nordisk AS (NVO) (Q3 2026) Earnings Call Highlights: Obesity Sales Surge 22% as Wegovy ...
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxPaE1GMVU5S2FzZzR3OVFvOU05c1Bta1R0VUlRQXZQTXM0S242elM4ZllLd3h5MVhFQTI5QVNxMjRjYzRxM2o5d0FuanV4Z25PSG9nWWVMX2p2XzJCRkFvWC1icUNya1ZjQnB1dU1iT1NjRnBGMTlna0xtRnBfUHBkcDAxYzZSZTBUZTc2QmJn?oc=5>

### Novo Nordisk stock jumps as Wegovy pill sales beat estimates
- Summary: Novo Nordisk stock jumps as Wegovy pill sales beat estimates
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNb203TE5TNzN4NnNxRDRFQnRiTWFWdmlTRXI2WmxlOC1yZVczMFB6ekJHbU9EX3FxTGhtWXpHdDUzM0M0c2oycjc1QnlUVnNFTW5QUE51NzBjSzE1dWJEUUZ6b2Q3QmU5dVVUSzR6QzhDYnBEUnVFYWVERWNVbmZuTkZ5OUlFWHFlRFVSdUp5b0FLN0M4b3NSRnJHMnA?oc=5>

### Can Novo Nordisk (NYSE:NVO) Trade Below Fair Value On Earnings?
- Summary: Questioning if NVO trades below fair value based on earnings.
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOc3ZtQjBQOENCS3Uxb1doRDc5a1l1bTVyRUxuSUN0Y3IxanZHMjJmWVlTTW5oVGR5V3p6YXlKdEc5a1BocUREd25DOHBJTC1jNnRDZGdpbGtzN2xTVmZYdDk4UVNEZXlFSElyTm9PYUJ3UXowV3JCcUlIWV9fWE5PLWx5UHlfZlRDbDBBT1NXcUFIUDVFdWpr?oc=5>

### Novo CEO Brushes Off Post-Midterm Drug-Pricing Fears, Says ‘Our World’ Won’t Change Dramatically – NVO Stock Gains Pre-Market
- Summary: CEO dismisses pricing concerns, signals stable outlook, boosting investor confidence.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijgJBVV95cUxNN1pPYW04WUgzRGhFMUF2czhZc3hrTzRVcExVOWUzRWVCMUk4MDc5Rl8zYVZtZWtIaDRkTWdFamloSDhDRTktVkdMWlUxLXk1UEduZ1hXdEQtaFlSOXloUWNuekFNSnBTRGhqblRoaVdaVU80NHNCZXZ0SXNNc3JRNVYtemRwNjk1cy1JV0RMbTB0XzhGZ3ZPTldpb0tWTWNGVUJCcXNxUEhBdThzZjRTdXlOWDBmYmtueEpoOHJfT2NwSDFqUkxYbVhVQXZFM0JOQnR6MTBZNldzcTB1WU1RMDVTY0YtNjN2TW1qTGxpY3F6dktGYlkycW9ma2g1Ylo3ZEl5NUZHTG5jME9YTEE?oc=5>

### NVO rises as upward price move continues
- Summary: Stock price climbs, reflecting positive market sentiment.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxQbHZTV2RCaU1sOG1Ib0pCR0FpbWtSbU1WcmhXeVJaYk54WUtxWGRKY1IwZXZsQU1LcWx5ME9CWmlOZVJNYzhjZm1QQXFHWkxqRVRIZkxoRVZNenNPMlJsdTBwTTVtOGN0RnI5V0xYZkNkZUlBQVRuSE15bjFCS1psNVVNdjdiQzNwdW55TlVlMGs?oc=5>

## HEADWINDS

### Novo Nordisk stock closes 0.64% lower, below its $40.77 EMA resistance
- Summary: Novo Nordisk stock closes 0.64% lower, below its $40.77 EMA resistance
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNaGtHdXRKcFp0ZEtqMVBuSXNSbHNkU1ZoRU1xTmREeHl5ZU44d3ljWWs4ajR6S0tFWF9YQ0xrNkdHWWZuY3QzS3NpMjNFMjkxNDZfd2lvM2g3V0h2cnp2UzFjNzhVTWNVeGxDMmo0dG9EdUxjQWYxUlA2RG5sR2l3eWFwVXdydUJIUHMw?oc=5>

## CATALYSTS

### Stocks making the biggest moves premarket: Trump Media, Tesla, CoreWeave, Novo Nordisk and more
- Summary: Stocks making the biggest moves premarket: Trump Media, Tesla, CoreWeave, Novo Nordisk and more
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNbVRCTEpta2pxRWE4NkRKdlVFb3hOZmJReEp5MDRSRTRXVEZUdi1qMnlJT3o0aURDNFBaVy1Hc09JOWJ3ZW1uZWFNVzVxNGdWck80TW1VVG45MzJSQXkzcTBSaS1nYUZqRW1UOENuZnlTSkJESFJja3N3WE43NTZYcWVQcjJTTW95ckt5Z1M4WGhlQTJqOXhDcm12TG4?oc=5>

### Novo Nordisk Trades at 10 Times Earnings While Buying Back Billions in Stock. Is This the Bottom?
- Summary: Novo Nordisk Trades at 10 Times Earnings While Buying Back Billions in Stock. Is This the Bottom?
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQRkcxLUFGd0VDS2xKVmI4SlZhOHpqT1NjV2VRVGU2ekdvVnVIOWx5cWZLT19HNWdxTXN4Wk11MEVLaVkwN2lVR0tjTXRSNXd5MGxvLVJXb0dPUlhmNHhydDlGSzhvR3lYdzkyYUFiOG9Wb3VndE96R09TVVhySjkyajhBTGNNWHRJLVJxbHA4YmphRHpMT0p5cA?oc=5>

### Novo Nordisk stock consolidates near $39.72 support amid mixed earnings and buyer support
- Summary: Novo Nordisk stock consolidates near $39.72 support amid mixed earnings and buyer support
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNd2YwZUZvUVVfczU4dFJXX1RCMWZtVXphQzB5UXF4bkVNTXFtV1RGbjV6ZjIyS0pKa0IzejVFZV8zNy1hRFpTcGRDTVlQUjVUM2h6MmU2dXhUS0x3Y1FOSUFKTVcyVUtzSllpQVltTVFIMUp4cU81QXFFMzhSVVRvUHoyeE1TUFhfR25v?oc=5>

### Novo Nordisk: Q3 Earnings Snapshot
- Summary: Q3 earnings data released, showing operating profit figures.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQMzEwTE1jUndjaE01WXFia3JXWXFxeDZzODFIVEc2b0hSY1U2VHVqXzU3RFBFS3ZBZTFWMlliWGNBQlRObjFmSHBWLXV0dER6UjNtSUMxN1NQaXBYTUR6SDBpU1BCZF9UMnR3OWsyNFV3RzZMZ0Q5Y2daN3pJWGVLdmVIQ2ZsZUNMLVVhazJFTkNpd1FZc0JVVFhn?oc=5>

### Novo Nordisk Q3: Just The Report I Was Waiting For (NYSE:NVO)
- Summary: Q3 results exceed expectations, highlighting robust performance of Novo Nordisk’s product portfolio.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPX1dlSENZdEQ4NkstUlB4c0xBbkpzbFdvZmdwdkRsX1hyZ1ZaUU90Z19nUUtxZFJydC03cFA4NHhBNE8xeFFUWUdSS2VfRmZJb1NSaTFnczJKNlk0RDl1eXRmajZQMGNEc1kxdHl6V1JsaVRfakFCc2xZUHpIRDNObnlISnNid3ZocU9XWkdicmF1X0hP?oc=5>

### Novo Nordisk set to report Q3 results as investors watch GLP-1 sales and outlook (NVO:NYSE)
- Summary: Novo Nordisk will release Q3 earnings, focusing on GLP‑1 sales performance and future outlook.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxQa2RjU1ZTM25sSHg5WWJmU0lHaVh4U0NYbk5ZazVPanBuOVMxSHpGUVQyWWNrUGFaUThjd0lYM0pkZlFqWDhYNTA5VVBYNTl6RFJNM216OUVobmZCVTJ0TW5Xb05ORi1mUF9rZUFQTVBoOW1QbXhJUmFfTVlnYzZXZVk3SWFiZVlaNE1Dc1VOSHZXNHg0anJqZjFKaXptdlBZalR1TDVBVEk2VmxDbmVXM2RDb2hHZGVFa2c?oc=5>

### Why Is Novo Nordisk Stock Surging Wednesday? - Novo Nordisk (NYSE:NVO)
- Summary: Stock surge attributed to positive earnings and guidance, reinforcing market optimism.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQcXBjdHlHcXdNWnRIOVZ5clo4enViVzNndEgtcmdITVFPb0E3YW42VmRCNHRuNU5yaWJjZnRVMWVrUGp1dHh1MXI0cXFnQ2dWTzFlZkVVZ2N5M1ctY0FJUzVLQU5rRHZxTnBsbzVmS2dsdHhjbEM0VS1OMVJmV25OVkRzMEVGRzl2N3VqRmFtRklhTTIyUkdkTnQ5cXJ6RXhwenFFWnFMMGRpRmRZSUtyRw?oc=5>

### Adjusted operating profit was 31.7 billion Danish kroner; reported operating profit was 23 billion at Novo Nordisk.
- Summary: Operating profit figures disclosed, higher adjusted profit.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxOX3l1X005VEQ4T3VVMHFVNDZFekM4b1lHQ3JReUVjQjFnU1B4aXpCQWRNQTVLQUJoNm83bE1GZGFEbnZrV21RX1J2VFhNaXJ6RXByai1XU1RZcUtsU0h0R2E0MVZnREMtaFpSeFo0UUxodFdIeEVLRkJTdWx3MjczaFBGTDluTURicnNyaEhPNUZNZkhOZlZVRmFTd2NVa0dFT0ZTYTdGZ3dmLVdRNzJpX3RpT0Q0NE5TVzdxZHAyVQ?oc=5>

### Ozempic maker Novo Nordisk's R&D chief sold shares worth 3.42 million Danish kroner.
- Summary: Insider sale of shares by R&D chief.
- Date: 2026-11-05 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxNTlZGMkhPQWNxclIwZXhpQTBEcVJOMlNJdzlPTDZmOE93MEh2Q2Jha2RVRDlNcDYyUDV2Z2xyWkRUUENSeVp1Y1JwN3VtVmxWZW1uSWwxLW9oTndiZFdrUnJ5NXFjX0lRNjFzSmthMHh5N0JUMkVYTTN0Mnc5bHhHVk1BWlFlTm4zZnlwZWxhNW5YVk1JbUdaRWFDRFl2VUZ0LW8zSkowTzdvZExwWmlnZVRRc1NVMThDeEE?oc=5>

### Novo Nordisk: The Recovery Is Gaining Traction. Here's Why I'm Staying On Hold (NYSE:NVO)
- Summary: Analyst maintains hold recommendation.
- Date: 2026-11-05 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxOZUQxZ1JZTUZIZy1WZ01MMzdLd0dCZS1LdV9aazV6V1JhcVUxWHpMMGwwdEltWlRuUUxEWk9xRnUybEdwei1ObE90RFZabElxaVVzNWw1MTNnSF9kZTNiSVU0YlNmUHRxaW9ZcnFRUk1BSHpTRUlud3RNVkVScTdyNWZnLWlHd1F0enFxdndtSHVmV0ZQYjdwNVlwUFFkNzBMeVlaNG0zZU5KcHg0dl9sQXp4RjhVUQ?oc=5>

### Novo Surges 5% After Walloping Expectations On The Back Of Its GLP-1 Drugs
- Summary: Stock rally following strong GLP‑1 drug performance.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMigAFBVV95cUxOY1RLNmt6NDB1UVpqR0dRdGpsaFFYNkgxUnNzc2V5dzkyeW41T0hnSUVhbkhiMjFVVGhscTB1Y2ZmZXotQmNqTF9xbFExYWE2YldEZjFMQzZyckpuU1V5R3FEUVVTMlZvNDJGQm1kcXU4QVpXWU9GS3hCRDFpX2lWUg?oc=5>

### Novo Nordisk A/S (NVO) Stock Forecasts
- Summary: Analyst forecast for NVO stock.
- Date: 2026-11-05 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxQS21welRnVHZpSVFaY0wzQWdJNjJaVnRURVBhVklTcVg5R21yUk5tYmtMVC1wV2d4RGRxZ3c4SEhTUjBoNUFaa0hIVmRTRmY1eXByemVsamtWYjhHRTZpYl8zdVJtNl83V1dla0JWRmtFdjJBMm5QVUpNMzdZb09yNUhXcksxdnlj?oc=5>

### Novo Nordisk CEO: Wegovy pill 'exceeded our expectations'
- Summary: CEO praises Wegovy drug performance.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQOGtFTGxCNnFaekxMTjdUUHl3b196NF9tN0VWbHpudzNnOUdPVmN4SHBaNGVzT0VWTGFNQ3pxVlptNU9TdGdJcUtVM3JRTWpWMk4yRWFra2pNLVNqSTZhMWZCT2drZUo3Q1ZvVkp1VE5CVGhaRHJwZnBDQ3M3Wk1qSTNlTUFkZmJGa3VERjBWUC1nR3pvaG5GNVIzSjR4dGNxMDRrcGhVZlI3MmVKY3A2OA?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVO** | **10.63** | **5.42** | **1.52** | **5.60** | **177,692,573,696.00 USD** | **-12.69** |
| LLY | 44.30 | 30.20 | 27.11 | 38.60 | 1,215,626,477,568.00 USD | 48.34 |
| ROG.SW | N/A | N/A | N/A | N/A | N/A unknown currency | N/A |
| SAN.PA | 24.43 | 1.39 | 8.00 | 15.70 | 101,272,748,032.00 EUR | 2.89 |

Peers fetched as_of: 2026-11-05; NVO reuses existing data (market data as_of: 2026-11-05); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-04
- Next expected earnings: 2027-02-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-05

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMirgFBVV95cUxQVmVmUEUzalZRY3YzMjBaQVRYb2ZDTDV3ZHp1aW1EcVVvdUNWcGlScnhuQWJ6Ym9PUnFKbldXNFlkZUFFbjdVdUREajZhdnZ3SjB1WkFvNExZTEZTZC1lV05yS2tNNnFzazB2VXk4WFhNUVhpcGpnYmc3WnBlZk0tamxJNjZLRWd5OHJOQzVDRGVTbldKSnA4cUFqdXAxVW5CcmgzUTU2Q2JvRXlsQnc?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPZ1hVc0t3Tl9lYVhsT3BnYnRZSjNFMHZ6bnR2N19hUXF4ZDA5cGg1RlR5a1NzcHREQlhKMDF5QldvRmd0akVFYTVvbU1lSW8wU2o0Y0RVeTVmcndkdmZLbE1oYWp0dFFRRTVZSHJqOVhjNUo2SFlpckxRRWRqS294YWVzN2F5aW1wTndYYTUxTkNnOVdpZjlCQQ?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxPaE1GMVU5S2FzZzR3OVFvOU05c1Bta1R0VUlRQXZQTXM0S242elM4ZllLd3h5MVhFQTI5QVNxMjRjYzRxM2o5d0FuanV4Z25PSG9nWWVMX2p2XzJCRkFvWC1icUNya1ZjQnB1dU1iT1NjRnBGMTlna0xtRnBfUHBkcDAxYzZSZTBUZTc2QmJn?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNb203TE5TNzN4NnNxRDRFQnRiTWFWdmlTRXI2WmxlOC1yZVczMFB6ekJHbU9EX3FxTGhtWXpHdDUzM0M0c2oycjc1QnlUVnNFTW5QUE51NzBjSzE1dWJEUUZ6b2Q3QmU5dVVUSzR6QzhDYnBEUnVFYWVERWNVbmZuTkZ5OUlFWHFlRFVSdUp5b0FLN0M4b3NSRnJHMnA?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOc3ZtQjBQOENCS3Uxb1doRDc5a1l1bTVyRUxuSUN0Y3IxanZHMjJmWVlTTW5oVGR5V3p6YXlKdEc5a1BocUREd25DOHBJTC1jNnRDZGdpbGtzN2xTVmZYdDk4UVNEZXlFSElyTm9PYUJ3UXowV3JCcUlIWV9fWE5PLWx5UHlfZlRDbDBBT1NXcUFIUDVFdWpr?oc=5
- https://news.google.com/rss/articles/CBMijgJBVV95cUxNN1pPYW04WUgzRGhFMUF2czhZc3hrTzRVcExVOWUzRWVCMUk4MDc5Rl8zYVZtZWtIaDRkTWdFamloSDhDRTktVkdMWlUxLXk1UEduZ1hXdEQtaFlSOXloUWNuekFNSnBTRGhqblRoaVdaVU80NHNCZXZ0SXNNc3JRNVYtemRwNjk1cy1JV0RMbTB0XzhGZ3ZPTldpb0tWTWNGVUJCcXNxUEhBdThzZjRTdXlOWDBmYmtueEpoOHJfT2NwSDFqUkxYbVhVQXZFM0JOQnR6MTBZNldzcTB1WU1RMDVTY0YtNjN2TW1qTGxpY3F6dktGYlkycW9ma2g1Ylo3ZEl5NUZHTG5jME9YTEE?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxQbHZTV2RCaU1sOG1Ib0pCR0FpbWtSbU1WcmhXeVJaYk54WUtxWGRKY1IwZXZsQU1LcWx5ME9CWmlOZVJNYzhjZm1QQXFHWkxqRVRIZkxoRVZNenNPMlJsdTBwTTVtOGN0RnI5V0xYZkNkZUlBQVRuSE15bjFCS1psNVVNdjdiQzNwdW55TlVlMGs?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNaGtHdXRKcFp0ZEtqMVBuSXNSbHNkU1ZoRU1xTmREeHl5ZU44d3ljWWs4ajR6S0tFWF9YQ0xrNkdHWWZuY3QzS3NpMjNFMjkxNDZfd2lvM2g3V0h2cnp2UzFjNzhVTWNVeGxDMmo0dG9EdUxjQWYxUlA2RG5sR2l3eWFwVXdydUJIUHMw?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNbVRCTEpta2pxRWE4NkRKdlVFb3hOZmJReEp5MDRSRTRXVEZUdi1qMnlJT3o0aURDNFBaVy1Hc09JOWJ3ZW1uZWFNVzVxNGdWck80TW1VVG45MzJSQXkzcTBSaS1nYUZqRW1UOENuZnlTSkJESFJja3N3WE43NTZYcWVQcjJTTW95ckt5Z1M4WGhlQTJqOXhDcm12TG4?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQRkcxLUFGd0VDS2xKVmI4SlZhOHpqT1NjV2VRVGU2ekdvVnVIOWx5cWZLT19HNWdxTXN4Wk11MEVLaVkwN2lVR0tjTXRSNXd5MGxvLVJXb0dPUlhmNHhydDlGSzhvR3lYdzkyYUFiOG9Wb3VndE96R09TVVhySjkyajhBTGNNWHRJLVJxbHA4YmphRHpMT0p5cA?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNd2YwZUZvUVVfczU4dFJXX1RCMWZtVXphQzB5UXF4bkVNTXFtV1RGbjV6ZjIyS0pKa0IzejVFZV8zNy1hRFpTcGRDTVlQUjVUM2h6MmU2dXhUS0x3Y1FOSUFKTVcyVUtzSllpQVltTVFIMUp4cU81QXFFMzhSVVRvUHoyeE1TUFhfR25v?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQMzEwTE1jUndjaE01WXFia3JXWXFxeDZzODFIVEc2b0hSY1U2VHVqXzU3RFBFS3ZBZTFWMlliWGNBQlRObjFmSHBWLXV0dER6UjNtSUMxN1NQaXBYTUR6SDBpU1BCZF9UMnR3OWsyNFV3RzZMZ0Q5Y2daN3pJWGVLdmVIQ2ZsZUNMLVVhazJFTkNpd1FZc0JVVFhn?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPX1dlSENZdEQ4NkstUlB4c0xBbkpzbFdvZmdwdkRsX1hyZ1ZaUU90Z19nUUtxZFJydC03cFA4NHhBNE8xeFFUWUdSS2VfRmZJb1NSaTFnczJKNlk0RDl1eXRmajZQMGNEc1kxdHl6V1JsaVRfakFCc2xZUHpIRDNObnlISnNid3ZocU9XWkdicmF1X0hP?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxQa2RjU1ZTM25sSHg5WWJmU0lHaVh4U0NYbk5ZazVPanBuOVMxSHpGUVQyWWNrUGFaUThjd0lYM0pkZlFqWDhYNTA5VVBYNTl6RFJNM216OUVobmZCVTJ0TW5Xb05ORi1mUF9rZUFQTVBoOW1QbXhJUmFfTVlnYzZXZVk3SWFiZVlaNE1Dc1VOSHZXNHg0anJqZjFKaXptdlBZalR1TDVBVEk2VmxDbmVXM2RDb2hHZGVFa2c?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxQcXBjdHlHcXdNWnRIOVZ5clo4enViVzNndEgtcmdITVFPb0E3YW42VmRCNHRuNU5yaWJjZnRVMWVrUGp1dHh1MXI0cXFnQ2dWTzFlZkVVZ2N5M1ctY0FJUzVLQU5rRHZxTnBsbzVmS2dsdHhjbEM0VS1OMVJmV25OVkRzMEVGRzl2N3VqRmFtRklhTTIyUkdkTnQ5cXJ6RXhwenFFWnFMMGRpRmRZSUtyRw?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxOX3l1X005VEQ4T3VVMHFVNDZFekM4b1lHQ3JReUVjQjFnU1B4aXpCQWRNQTVLQUJoNm83bE1GZGFEbnZrV21RX1J2VFhNaXJ6RXByai1XU1RZcUtsU0h0R2E0MVZnREMtaFpSeFo0UUxodFdIeEVLRkJTdWx3MjczaFBGTDluTURicnNyaEhPNUZNZkhOZlZVRmFTd2NVa0dFT0ZTYTdGZ3dmLVdRNzJpX3RpT0Q0NE5TVzdxZHAyVQ?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxNTlZGMkhPQWNxclIwZXhpQTBEcVJOMlNJdzlPTDZmOE93MEh2Q2Jha2RVRDlNcDYyUDV2Z2xyWkRUUENSeVp1Y1JwN3VtVmxWZW1uSWwxLW9oTndiZFdrUnJ5NXFjX0lRNjFzSmthMHh5N0JUMkVYTTN0Mnc5bHhHVk1BWlFlTm4zZnlwZWxhNW5YVk1JbUdaRWFDRFl2VUZ0LW8zSkowTzdvZExwWmlnZVRRc1NVMThDeEE?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxOZUQxZ1JZTUZIZy1WZ01MMzdLd0dCZS1LdV9aazV6V1JhcVUxWHpMMGwwdEltWlRuUUxEWk9xRnUybEdwei1ObE90RFZabElxaVVzNWw1MTNnSF9kZTNiSVU0YlNmUHRxaW9ZcnFRUk1BSHpTRUlud3RNVkVScTdyNWZnLWlHd1F0enFxdndtSHVmV0ZQYjdwNVlwUFFkNzBMeVlaNG0zZU5KcHg0dl9sQXp4RjhVUQ?oc=5
- https://news.google.com/rss/articles/CBMigAFBVV95cUxOY1RLNmt6NDB1UVpqR0dRdGpsaFFYNkgxUnNzc2V5dzkyeW41T0hnSUVhbkhiMjFVVGhscTB1Y2ZmZXotQmNqTF9xbFExYWE2YldEZjFMQzZyckpuU1V5R3FEUVVTMlZvNDJGQm1kcXU4QVpXWU9GS3hCRDFpX2lWUg?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxQS21welRnVHZpSVFaY0wzQWdJNjJaVnRURVBhVklTcVg5R21yUk5tYmtMVC1wV2d4RGRxZ3c4SEhTUjBoNUFaa0hIVmRTRmY1eXByemVsamtWYjhHRTZpYl8zdVJtNl83V1dla0JWRmtFdjJBMm5QVUpNMzdZb09yNUhXcksxdnlj?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxPWi1ucVZOcG5zU3pYbUlmNUxGQWZVV2VULWFTSU4xblNPVUNsQldUME9NZkpLcGluc0ktekZyZ0tHTTVnX3VJTWtFNU80dW40N24yaVVJRE9ncm9oNm5iZDF2akVnN3ZMN2htbFFsU1h5S1dLd3FEcUVhQlhxRTRyM2J3Q2Q2UHVZY0tSWQ?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxQOGtFTGxCNnFaekxMTjdUUHl3b196NF9tN0VWbHpudzNnOUdPVmN4SHBaNGVzT0VWTGFNQ3pxVlptNU9TdGdJcUtVM3JRTWpWMk4yRWFra2pNLVNqSTZhMWZCT2drZUo3Q1ZvVkp1VE5CVGhaRHJwZnBDQ3M3Wk1qSTNlTUFkZmJGa3VERjBWUC1nR3pvaG5GNVIzSjR4dGNxMDRrcGhVZlI3MmVKY3A2OA?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
