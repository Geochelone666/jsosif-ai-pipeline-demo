# NVO Intelligence Report

- ticker: **NVO**
- Report as_of: **2026-11-04**
- Market data as_of: **2026-11-04**
- Quant sources: https://finance.yahoo.com/quote/NVO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVO/key-statistics/
- AI analysis snapshot as_of: **2026-11-04**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-05T05:18:08.792198+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 8, 'ai': 10, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261104T044411Z-6b13f9ec/NVO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 13 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 41.67%; oldest publication 2026-10-30

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 42.1800 |
| Return 1D (%) | 4.9515 |
| Return 1W (%) | 10.1593 |
| Return 1M (%) | 13.0225 |
| Return YTD (%) | -12.9605 |
| Return 1Y (%) | -8.2162 |
| Annualized volatility (%) | 45.8307 |
| Beta vs SPY | 0.9641 |
| Max drawdown (%) | -43.6699 |
| Sharpe (rf=0) | 0.0457 |
| Downside deviation (rf=0, %) | 33.9415 |
| Sortino (rf=0) | 0.0617 |
| Historical VaR 95% (1D, %) | 3.1060 |
| Historical ES 95% (1D, %) | 7.1341 |
| Correlation vs SPY | 0.2701 |
| Tracking error vs SPY (%) | 44.1298 |
| P/E (trailing) | 9.83 |
| P/B | 6.43 |
| EV/EBITDA | 1.57 |
| Revenue growth (%) | 2.10 |
| Forward P/E (estimate) | 12.26 |
| Gross margin (%) | 81.99 |
| Operating margin (%) | 42.54 |
| Return on equity (%) | 59.81 |
| Free cash flow yield (%) | N/A |
| MA50 | 40.8414 |
| Close vs MA50 (%) | 3.2776 |
| MA200 | 43.1287 |
| Close vs MA200 (%) | -2.1997 |
| RSI (14, Wilder) | 65.2897 |
| MACD (12,26) | 0.0926 |
| MACD signal (9) | -0.3807 |
| MACD histogram | 0.4733 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVO': 275, 'SPY': 275}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 42.1800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 4.9515 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 10.1593 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 13.0225 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -12.9605 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -8.2162 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 45.8307 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 33.9415 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.0617 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.1060 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 7.1341 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2701 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 44.1298 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.9641 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -43.6699 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.0457 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 12.2632 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 81.9870 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 42.5400 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 59.8150 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 9.8322 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 65.2897 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.4733 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 3.2776 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -2.1997 -> Slightly below the moving-average trend level.

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

## HEADWINDS

### Novo Nordisk stock closes 0.64% lower, below its $40.77 EMA resistance
- Summary: Novo Nordisk stock closes 0.64% lower, below its $40.77 EMA resistance
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNaGtHdXRKcFp0ZEtqMVBuSXNSbHNkU1ZoRU1xTmREeHl5ZU44d3ljWWs4ajR6S0tFWF9YQ0xrNkdHWWZuY3QzS3NpMjNFMjkxNDZfd2lvM2g3V0h2cnp2UzFjNzhVTWNVeGxDMmo0dG9EdUxjQWYxUlA2RG5sR2l3eWFwVXdydUJIUHMw?oc=5>

## CATALYSTS

### Novo Nordisk Buys DKK 377 Million of Shares in Latest Repurchase Round
- Summary: Novo Nordisk Buys DKK 377 Million of Shares in Latest Repurchase Round
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi6gFBVV95cUxNd1V4MWFJTGg0SDQyNXNaS05uSmN1bWpTek1SVW1leWxSS2JUSTY4U2J6M0ZjMGxRQTJlSVZBMkdCNktvOWlXUlZPbjJFYVZnQTM5RzV6Tlc1YXp1V0dkVkQ0dzB1Z0JQWDg0eXNid1Y3MUFfOVBmY0JSX2htSlpVWE1PWUZlT0hid0xGQl9pZEVyWmdxdU9FcERWQk85ckI1UmduLVh1bTE4c3VHUGNWczVIZ3ZkZzdrOWVoMkJzUmkwYUhBZVU5VjQ4OEVrY3VQalNTdC1LQUs3U1B6Zi10T2RHay1rRUN3YXc?oc=5>

### Stocks making the biggest moves premarket: Trump Media, Tesla, CoreWeave, Novo Nordisk and more
- Summary: Stocks making the biggest moves premarket: Trump Media, Tesla, CoreWeave, Novo Nordisk and more
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNbVRCTEpta2pxRWE4NkRKdlVFb3hOZmJReEp5MDRSRTRXVEZUdi1qMnlJT3o0aURDNFBaVy1Hc09JOWJ3ZW1uZWFNVzVxNGdWck80TW1VVG45MzJSQXkzcTBSaS1nYUZqRW1UOENuZnlTSkJESFJja3N3WE43NTZYcWVQcjJTTW95ckt5Z1M4WGhlQTJqOXhDcm12TG4?oc=5>

### Novo Nordisk Trades at 10 Times Earnings While Buying Back Billions in Stock. Is This the Bottom?
- Summary: Novo Nordisk Trades at 10 Times Earnings While Buying Back Billions in Stock. Is This the Bottom?
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQRkcxLUFGd0VDS2xKVmI4SlZhOHpqT1NjV2VRVGU2ekdvVnVIOWx5cWZLT19HNWdxTXN4Wk11MEVLaVkwN2lVR0tjTXRSNXd5MGxvLVJXb0dPUlhmNHhydDlGSzhvR3lYdzkyYUFiOG9Wb3VndE96R09TVVhySjkyajhBTGNNWHRJLVJxbHA4YmphRHpMT0p5cA?oc=5>

### Novo Nordisk set to report Q3 results as investors watch GLP-1 sales and outlook (NVO:NYSE)
- Summary: Novo Nordisk will release Q3 earnings, focusing on GLP‑1 sales performance and future outlook.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxQa2RjU1ZTM25sSHg5WWJmU0lHaVh4U0NYbk5ZazVPanBuOVMxSHpGUVQyWWNrUGFaUThjd0lYM0pkZlFqWDhYNTA5VVBYNTl6RFJNM216OUVobmZCVTJ0TW5Xb05ORi1mUF9rZUFQTVBoOW1QbXhJUmFfTVlnYzZXZVk3SWFiZVlaNE1Dc1VOSHZXNHg0anJqZjFKaXptdlBZalR1TDVBVEk2VmxDbmVXM2RDb2hHZGVFa2c?oc=5>

### Treasury shares total 1.2% of capital as Novo Nordisk (NVO) buybacks reach DKK 11.6B.
- Summary: Novo Nordisk completed a buyback of DKK 11.6B, increasing treasury shares to 1.2% of capital.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQam9RNmZVZ0VwRDBLVi13VFpXcGhtTlphQVRGY095d0pmeFN6LXhscGt0bG1DZ25ZdU55dV9mZjJ3Q2ZHVmNhTTVTeFFIc1ZHRzFXRFJzQlhKcGN0V1pObXZEMFloX3VNTFpiNG4ta1h6dF9aa1d4MEZ0ZVktVGlVdjZ4bXdseFQ4Q1gwVDhfQ1BPQkF4UG9oX0MxR1R5SW1wZndIWlF2c1Y0ZXM1RnNqOA?oc=5>

### Novo hikes outlook again as it speeds up Wegovy pill rollout
- Summary: Novo Nordisk raises its financial outlook, accelerating the rollout of its Wegovy obesity drug, boosting investor confidence.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQUXNSTmhfQVhISGNaNGRPM1A5R1hwalZvbm93d3lkc0thd0dZMGdLZ3h6WTI4NnVQeGxZYVdhc2IzY3M3UXUtMlBQVmtZWlMtQmhDYXhCZ1JuREQzZlhwQVVRR0tiTEZybndZdHBKbG5ZcXR1c2p6Tm5yNHRXYVNNVUs2VjViQVB6dWc3c24tTHd3UkNRN1NIdXZ1alB3TkljNGNXSUZn?oc=5>

### Novo Surges After Crushing Forecasts On The Back Of Its GLP-1s
- Summary: Shares jump as Novo Nordisk surpasses earnings forecasts, driven by strong GLP-1 drug sales.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMigAFBVV95cUxOY1RLNmt6NDB1UVpqR0dRdGpsaFFYNkgxUnNzc2V5dzkyeW41T0hnSUVhbkhiMjFVVGhscTB1Y2ZmZXotQmNqTF9xbFExYWE2YldEZjFMQzZyckpuU1V5R3FEUVVTMlZvNDJGQm1kcXU4QVpXWU9GS3hCRDFpX2lWUg?oc=5>

### Novo Nordisk Q3: Just The Report I Was Waiting For (NYSE:NVO)
- Summary: Q3 results exceed expectations, highlighting robust performance of Novo Nordisk’s product portfolio.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPX1dlSENZdEQ4NkstUlB4c0xBbkpzbFdvZmdwdkRsX1hyZ1ZaUU90Z19nUUtxZFJydC03cFA4NHhBNE8xeFFUWUdSS2VfRmZJb1NSaTFnczJKNlk0RDl1eXRmajZQMGNEc1kxdHl6V1JsaVRfakFCc2xZUHpIRDNObnlISnNid3ZocU9XWkdicmF1X0hP?oc=5>

### Why Is Novo Nordisk Stock Surging Wednesday? - Novo Nordisk (NYSE:NVO)
- Summary: Stock surge attributed to positive earnings and guidance, reinforcing market optimism.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQcXBjdHlHcXdNWnRIOVZ5clo4enViVzNndEgtcmdITVFPb0E3YW42VmRCNHRuNU5yaWJjZnRVMWVrUGp1dHh1MXI0cXFnQ2dWTzFlZkVVZ2N5M1ctY0FJUzVLQU5rRHZxTnBsbzVmS2dsdHhjbEM0VS1OMVJmV25OVkRzMEVGRzl2N3VqRmFtRklhTTIyUkdkTnQ5cXJ6RXhwenFFWnFMMGRpRmRZSUtyRw?oc=5>

### Novo Nordisk: Q3 Earnings Snapshot
- Summary: Q3 earnings data released, showing operating profit figures.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQMzEwTE1jUndjaE01WXFia3JXWXFxeDZzODFIVEc2b0hSY1U2VHVqXzU3RFBFS3ZBZTFWMlliWGNBQlRObjFmSHBWLXV0dER6UjNtSUMxN1NQaXBYTUR6SDBpU1BCZF9UMnR3OWsyNFV3RzZMZ0Q5Y2daN3pJWGVLdmVIQ2ZsZUNMLVVhazJFTkNpd1FZc0JVVFhn?oc=5>

### Novo CEO Brushes Off Post-Midterm Drug-Pricing Fears, Says ‘Our World’ Won’t Change Dramatically – NVO Stock Gains Pre-Market
- Summary: CEO reassures investors, stock gains pre-market.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxPQ2tNRXNjVmJvRWVmcVo2V2F5UUhKZ2k5R2tUMU5aWDNaQnNQSG9NUXRKMHY4Rm5mLURoSXpsVVlsVU16OHBmaHBYZjRnU2xXMWhvTjc0blpWd1d2eXNwUXFkWXA5TDBhZHRvUy1JTk5HSGNYeWNTRzJBempLRkpMZ0pIVHBMSjBrTWlEUHFDaw?oc=5>

### Adjusted operating profit was 31.7 billion Danish kroner; reported operating profit was 23 billion at Novo Nordisk.
- Summary: Operating profit figures disclosed, higher adjusted profit.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxOX3l1X005VEQ4T3VVMHFVNDZFekM4b1lHQ3JReUVjQjFnU1B4aXpCQWRNQTVLQUJoNm83bE1GZGFEbnZrV21RX1J2VFhNaXJ6RXByai1XU1RZcUtsU0h0R2E0MVZnREMtaFpSeFo0UUxodFdIeEVLRkJTdWx3MjczaFBGTDluTURicnNyaEhPNUZNZkhOZlZVRmFTd2NVa0dFT0ZTYTdGZ3dmLVdRNzJpX3RpT0Q0NE5TVzdxZHAyVQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVO** | **9.83** | **6.43** | **1.57** | **2.10** | **185,981,960,192.00 USD** | **-8.22** |
| LLY | 46.02 | 31.38 | 28.13 | 38.60 | 1,263,067,463,680.00 USD | 57.35 |
| ROG.SW | N/A | N/A | N/A | N/A | N/A unknown currency | N/A |
| SAN.PA | 24.31 | 1.38 | 7.96 | 15.70 | 100,757,577,728.00 EUR | -1.65 |

Peers fetched as_of: 2026-11-04; NVO reuses existing data (market data as_of: 2026-11-04); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-04
- Next expected earnings: N/A (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-04

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
- https://news.google.com/rss/articles/CBMiekFVX3lxTE52NVRvcmNObFYzXzFiWDZpeUN1SjlWV0dFTl9GbFJKUU5tc0FmVUpXLWs0X3JXNkIxd1JqSnJkUHRkNzZxWl9abVFkcG1Ubm5WLUVSZ2lQdkYwUTZnam41aGRXRGkzcXF1TXRYZ3g3dGNKSWdKczV4ZWNn?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPZ1hVc0t3Tl9lYVhsT3BnYnRZSjNFMHZ6bnR2N19hUXF4ZDA5cGg1RlR5a1NzcHREQlhKMDF5QldvRmd0akVFYTVvbU1lSW8wU2o0Y0RVeTVmcndkdmZLbE1oYWp0dFFRRTVZSHJqOVhjNUo2SFlpckxRRWRqS294YWVzN2F5aW1wTndYYTUxTkNnOVdpZjlCQQ?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxPaE1GMVU5S2FzZzR3OVFvOU05c1Bta1R0VUlRQXZQTXM0S242elM4ZllLd3h5MVhFQTI5QVNxMjRjYzRxM2o5d0FuanV4Z25PSG9nWWVMX2p2XzJCRkFvWC1icUNya1ZjQnB1dU1iT1NjRnBGMTlna0xtRnBfUHBkcDAxYzZSZTBUZTc2QmJn?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNb203TE5TNzN4NnNxRDRFQnRiTWFWdmlTRXI2WmxlOC1yZVczMFB6ekJHbU9EX3FxTGhtWXpHdDUzM0M0c2oycjc1QnlUVnNFTW5QUE51NzBjSzE1dWJEUUZ6b2Q3QmU5dVVUSzR6QzhDYnBEUnVFYWVERWNVbmZuTkZ5OUlFWHFlRFVSdUp5b0FLN0M4b3NSRnJHMnA?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOc3ZtQjBQOENCS3Uxb1doRDc5a1l1bTVyRUxuSUN0Y3IxanZHMjJmWVlTTW5oVGR5V3p6YXlKdEc5a1BocUREd25DOHBJTC1jNnRDZGdpbGtzN2xTVmZYdDk4UVNEZXlFSElyTm9PYUJ3UXowV3JCcUlIWV9fWE5PLWx5UHlfZlRDbDBBT1NXcUFIUDVFdWpr?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNaGtHdXRKcFp0ZEtqMVBuSXNSbHNkU1ZoRU1xTmREeHl5ZU44d3ljWWs4ajR6S0tFWF9YQ0xrNkdHWWZuY3QzS3NpMjNFMjkxNDZfd2lvM2g3V0h2cnp2UzFjNzhVTWNVeGxDMmo0dG9EdUxjQWYxUlA2RG5sR2l3eWFwVXdydUJIUHMw?oc=5
- https://news.google.com/rss/articles/CBMi6gFBVV95cUxNd1V4MWFJTGg0SDQyNXNaS05uSmN1bWpTek1SVW1leWxSS2JUSTY4U2J6M0ZjMGxRQTJlSVZBMkdCNktvOWlXUlZPbjJFYVZnQTM5RzV6Tlc1YXp1V0dkVkQ0dzB1Z0JQWDg0eXNid1Y3MUFfOVBmY0JSX2htSlpVWE1PWUZlT0hid0xGQl9pZEVyWmdxdU9FcERWQk85ckI1UmduLVh1bTE4c3VHUGNWczVIZ3ZkZzdrOWVoMkJzUmkwYUhBZVU5VjQ4OEVrY3VQalNTdC1LQUs3U1B6Zi10T2RHay1rRUN3YXc?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNbVRCTEpta2pxRWE4NkRKdlVFb3hOZmJReEp5MDRSRTRXVEZUdi1qMnlJT3o0aURDNFBaVy1Hc09JOWJ3ZW1uZWFNVzVxNGdWck80TW1VVG45MzJSQXkzcTBSaS1nYUZqRW1UOENuZnlTSkJESFJja3N3WE43NTZYcWVQcjJTTW95ckt5Z1M4WGhlQTJqOXhDcm12TG4?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQRkcxLUFGd0VDS2xKVmI4SlZhOHpqT1NjV2VRVGU2ekdvVnVIOWx5cWZLT19HNWdxTXN4Wk11MEVLaVkwN2lVR0tjTXRSNXd5MGxvLVJXb0dPUlhmNHhydDlGSzhvR3lYdzkyYUFiOG9Wb3VndE96R09TVVhySjkyajhBTGNNWHRJLVJxbHA4YmphRHpMT0p5cA?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxQa2RjU1ZTM25sSHg5WWJmU0lHaVh4U0NYbk5ZazVPanBuOVMxSHpGUVQyWWNrUGFaUThjd0lYM0pkZlFqWDhYNTA5VVBYNTl6RFJNM216OUVobmZCVTJ0TW5Xb05ORi1mUF9rZUFQTVBoOW1QbXhJUmFfTVlnYzZXZVk3SWFiZVlaNE1Dc1VOSHZXNHg0anJqZjFKaXptdlBZalR1TDVBVEk2VmxDbmVXM2RDb2hHZGVFa2c?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxQam9RNmZVZ0VwRDBLVi13VFpXcGhtTlphQVRGY095d0pmeFN6LXhscGt0bG1DZ25ZdU55dV9mZjJ3Q2ZHVmNhTTVTeFFIc1ZHRzFXRFJzQlhKcGN0V1pObXZEMFloX3VNTFpiNG4ta1h6dF9aa1d4MEZ0ZVktVGlVdjZ4bXdseFQ4Q1gwVDhfQ1BPQkF4UG9oX0MxR1R5SW1wZndIWlF2c1Y0ZXM1RnNqOA?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQUXNSTmhfQVhISGNaNGRPM1A5R1hwalZvbm93d3lkc0thd0dZMGdLZ3h6WTI4NnVQeGxZYVdhc2IzY3M3UXUtMlBQVmtZWlMtQmhDYXhCZ1JuREQzZlhwQVVRR0tiTEZybndZdHBKbG5ZcXR1c2p6Tm5yNHRXYVNNVUs2VjViQVB6dWc3c24tTHd3UkNRN1NIdXZ1alB3TkljNGNXSUZn?oc=5
- https://news.google.com/rss/articles/CBMigAFBVV95cUxOY1RLNmt6NDB1UVpqR0dRdGpsaFFYNkgxUnNzc2V5dzkyeW41T0hnSUVhbkhiMjFVVGhscTB1Y2ZmZXotQmNqTF9xbFExYWE2YldEZjFMQzZyckpuU1V5R3FEUVVTMlZvNDJGQm1kcXU4QVpXWU9GS3hCRDFpX2lWUg?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPX1dlSENZdEQ4NkstUlB4c0xBbkpzbFdvZmdwdkRsX1hyZ1ZaUU90Z19nUUtxZFJydC03cFA4NHhBNE8xeFFUWUdSS2VfRmZJb1NSaTFnczJKNlk0RDl1eXRmajZQMGNEc1kxdHl6V1JsaVRfakFCc2xZUHpIRDNObnlISnNid3ZocU9XWkdicmF1X0hP?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxQcXBjdHlHcXdNWnRIOVZ5clo4enViVzNndEgtcmdITVFPb0E3YW42VmRCNHRuNU5yaWJjZnRVMWVrUGp1dHh1MXI0cXFnQ2dWTzFlZkVVZ2N5M1ctY0FJUzVLQU5rRHZxTnBsbzVmS2dsdHhjbEM0VS1OMVJmV25OVkRzMEVGRzl2N3VqRmFtRklhTTIyUkdkTnQ5cXJ6RXhwenFFWnFMMGRpRmRZSUtyRw?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQMzEwTE1jUndjaE01WXFia3JXWXFxeDZzODFIVEc2b0hSY1U2VHVqXzU3RFBFS3ZBZTFWMlliWGNBQlRObjFmSHBWLXV0dER6UjNtSUMxN1NQaXBYTUR6SDBpU1BCZF9UMnR3OWsyNFV3RzZMZ0Q5Y2daN3pJWGVLdmVIQ2ZsZUNMLVVhazJFTkNpd1FZc0JVVFhn?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxPQ2tNRXNjVmJvRWVmcVo2V2F5UUhKZ2k5R2tUMU5aWDNaQnNQSG9NUXRKMHY4Rm5mLURoSXpsVVlsVU16OHBmaHBYZjRnU2xXMWhvTjc0blpWd1d2eXNwUXFkWXA5TDBhZHRvUy1JTk5HSGNYeWNTRzJBempLRkpMZ0pIVHBMSjBrTWlEUHFDaw?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxOX3l1X005VEQ4T3VVMHFVNDZFekM4b1lHQ3JReUVjQjFnU1B4aXpCQWRNQTVLQUJoNm83bE1GZGFEbnZrV21RX1J2VFhNaXJ6RXByai1XU1RZcUtsU0h0R2E0MVZnREMtaFpSeFo0UUxodFdIeEVLRkJTdWx3MjczaFBGTDluTURicnNyaEhPNUZNZkhOZlZVRmFTd2NVa0dFT0ZTYTdGZ3dmLVdRNzJpX3RpT0Q0NE5TVzdxZHAyVQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
