# TSM Intelligence Report

- ticker: **TSM**
- Report as_of: **2026-11-24**
- Market data as_of: **2026-11-24**
- Quant sources: https://finance.yahoo.com/quote/TSM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TSM/key-statistics/
- AI analysis snapshot as_of: **2026-11-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-25T06:56:43.648952+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 2, 'ai': 15, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261123T053847Z-45053549/TSM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 12 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 21.74%; oldest publication 2026-11-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 349.2000 |
| Return 1D (%) | -3.9604 |
| Return 1W (%) | -2.9164 |
| Return 1M (%) | -16.5611 |
| Return YTD (%) | 15.8135 |
| Return 1Y (%) | 23.9797 |
| Annualized volatility (%) | 45.7960 |
| Beta vs SPY | 2.3258 |
| Max drawdown (%) | -34.3948 |
| Sharpe (rf=0) | 0.6992 |
| Downside deviation (rf=0, %) | 31.3387 |
| Sortino (rf=0) | 1.0218 |
| Historical VaR 95% (1D, %) | 4.3901 |
| Historical ES 95% (1D, %) | 6.3161 |
| Correlation vs SPY | 0.7595 |
| Tracking error vs SPY (%) | 35.7862 |
| P/E (trailing) | 22.63 |
| P/B | 67.07 |
| EV/EBITDA | 3.22 |
| Revenue growth (%) | 50.90 |
| Forward P/E (estimate) | 14.93 |
| Gross margin (%) | 65.85 |
| Operating margin (%) | 57.96 |
| Return on equity (%) | 41.86 |
| Free cash flow yield (%) | N/A |
| MA50 | 419.7706 |
| Close vs MA50 (%) | -16.8117 |
| MA200 | 402.3167 |
| Close vs MA200 (%) | -13.2027 |
| RSI (14, Wilder) | 40.1972 |
| MACD (12,26) | -20.1725 |
| MACD signal (9) | -16.7945 |
| MACD histogram | -3.3780 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TSM': 289, 'SPY': 289}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 349.2000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -3.9604 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.9164 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -16.5611 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 15.8135 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 23.9797 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 45.7960 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 31.3387 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.0218 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.3901 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.3161 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.7595 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 35.7862 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.3258 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -34.3948 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.6992 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 14.9325 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 65.8460 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 57.9610 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 41.8600 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 22.6312 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 40.1972 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.3780 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -16.8117 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -13.2027 -> Clearly below the moving-average trend level.

## TAILWINDS

### Taiwan Semiconductor Rallies 17% as Jensen Huang's Return to NVIDIA Lifts Chip Stocks; Intel Surges 15%, AMD Jumps 8%
- Summary: TSM shares surged 17% following Jensen Huang’s return to NVIDIA, boosting chip sector sentiment.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi6wFBVV95cUxPY3NBa1ZIRXJyUHFCWERaWWxiTGFoRW53aGY2Q1pqUzZQNmpiVGpQdG00T2hzVWpQNEN4Q0JBYlRja3FvdWhKaHpxVjVxQjRfQnlwRmc1Tm0tMFVVQjVNTzUzM29rbTlwWE5DZDNRYWM3aHQ0NkNzbGhIUExDa1F3MnhibXEwWEc3RzhUUzNIUkYtV1haWGtfYWdzNnlpaHFLU3dQS1R1dDZKVUx1SC1GczJ5UnMyTVF6alEyblVtdmIwdldnQjhIc01OaDgycmpQQ0pNQlBGaVRmWHJMS1ExemxsdFFVNkpLVEZn?oc=5>

### TSMC: Amazing Chance To Double Down On The AI Market Panic (NYSE:TSM)
- Summary: TSMC sees opportunity to capitalize on AI market downturn.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNbVI3ZDlyMFBRakI3cl8td1J6aTZBWWZnTkdyLTF0cm1ib0JnZjFjMDJ0NTBPMEpKRmZndWtBNG1MTTdsQmFZWTNldm9uOXdMU2EzSFJxWWZnZHozVmo2WFljZml1ekRnRUxNVm9oQ09yeEZRdHlEWjRrcktZWXhocl9RODhHb1dWU21veldIeVkyNWV5NURwZlRQQXoyZEk?oc=5>

## HEADWINDS

### TSMC Stock Slides As Taiwan Market Suffers Worst Week Since 1990: What's Going On?
- Summary: TSMC Stock Slides As Taiwan Market Suffers Worst Week Since 1990: What's Going On?
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxPQVhxWWp0SU9TOVVGLWQ1azhrbXlnVng0QjBUNzhXS3J1Q1FSU3F4dG1ZYzlzaW0xa3I4M3FoNzVsazV4TTNCRHNOb3BNUHQxVjRRZ011a3licEdIZmdsLUdVVGVJdjZWdlp5X251Q1VhdnZETmFYa3BURGtjenZiX0dqZVZFUkREd29XNkNiM1RuR3l2Y1Q5VE9JRzZ3NEdDY1cxLWRQQlJtTFlzdjk2NzZicThkeFIydzduVjlWUXhKdXNRZkFXbHdUc2pyVnpaaTVMOWR1SQ?oc=5>

### Taiwan Semiconductor Stocks Fall 2.78% After Taipei Shares Hit the 10% Limit
- Summary: Taiwan Semiconductor Stocks Fall 2.78% After Taipei Shares Hit the 10% Limit
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxNbWhPakhJTVpWYXJfa3ozbVM5ZGdaNFB4Nm5PQmREU0tMckNpUjFRcFEzTUlLRDNrWXI2aHY4Y0lhWEp0Nk9WVmg1N0R1RDFneFFjRXhUdnlmRF93TDVLTHNoVVkwd1g2QmQ2OWtRcGVRTk43TXZyZGpaeUFYaEIwS28tMk9OaUI5c2d3Z2NkWlVoNks3YlZ4VlhfdERmeUZVbk04Qml4WkJHVmppUWxDQzUxeVc5c3dpRTd5X2ZtVi1iLVlVb2xzNWRZWS0xcnM?oc=5>

### Taiwan loosens margin call rules in bid to steady market amid AI rout
- Summary: Policy change may affect market stability, impacting TSM.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxQMW5zeVBBNVlWOHV5OTUtc3RHWWh0S0doTGVDeUlNeVJTT2NtUzBQSVpnV2dUMFNuYlBjNVVtMDF6dWxUemItMDJZTVdIUlZteXFLZzNCcjg3cFhGTFIxNlp5MEdnZ3dGSnpiYmI5RDAxMW5wVl93NlVUVDlrclc1Z1hfREwyRWo2Q1hWQ0U5LWRnUE1XU1duRjJ3c3JtNnVqNDhDSU81UFN6UTJKUmpuUHdsdTZVYjdiU0E2TA?oc=5>

## CATALYSTS

### Why TSMC Stock Soared Today
- Summary: TSM stock experienced a sharp rise today, reflecting positive market sentiment.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOMEdpVWJwSTh1cU9tb25IQWwwR3VjdlNfYWZUYXI5b3lrZzRTb3c3SHBqVy00endjamt2M3RvMFZLcGZRTmRLcTZTOE92ejJqM09vejF6Y29zRy02XzRQeGJ2a2ZKaTVDNE5DeU1YbjJUc3NOM3plT3NJOWZWZ1ZoTm9YZ0JZZkZGMXZwUkNxQ3NnSVhDWDVn?oc=5>

### TSMC's $22.6 Billion Texas Chip Plant Hinges on Two Tax Breaks
- Summary: Plant investment depends on tax incentives, creating risk if not granted.
- Date: 2026-11-24 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOY1VYSGNLbGJ2UjctSWx4WFhXV2VLZXozUEVxRWtfUFBiSWkyR0VmUEU2ZWQwMjhJOGNwX0lkTjB3cUhhOUV5aUxEUVNfVVVhVzRFaGVlR1RkbjZ0d05fWXBHT1VXaFVLUVUwMUE5ZjR4eDJOS2ttMUVQbExqSnkzOGpaVHFKQ2d2QnktSVJZYVRseThOSzNiVA?oc=5>

### Taiwan Semiconductor Manufacturing (NYSE:TSM) Stock May Be Reasonable After New Export Curbs
- Summary: TSM stock may be reasonable following new export curbs, suggesting potential upside.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxPa1JvdC0wSGFvVjBwYUYzVlhoX2FHMkdLMUdUUUtibHZhUmJzWkxoT24wQlBjeGZfWGxydF92YnAxN3BDRl9VdkFtTVRiY0tyc1ZjS1RYWE16NUN1X2ZDLW1SRW9vYmdxSmhFMzU5UmdJSV81RE9XOGNIWEYwZFJCMm1OWTFzWS1hckRybm9MVXZLUV9HVTRNZmZRNVdMNDlhVkprUC1DYTBKOHdv?oc=5>

### Down On TSMC Stock? Your Buy Price Decides It
- Summary: TSM stock performance depends on buy price, indicating market sensitivity.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxOLWc4NXFYcWoxVVljOGZaR2kzVHF2QnY5X2l0eEY4Ri1BWGNhTzlMWWhiM1BLdWtXWnN2QWhabzliQzBSYjI1UFBMV3gxYUlqMnBfTjhqWTBDb0Z0SUFCeTBxdVRvTjBNVEF2ZFVmeWFXSXQyZ0RNbTZpb0dlYmhLT2Yzc2hzam5ENVVzZzJOSC1kWWN3cjI5WTh0Nm1xVWlGSlVsR2NIWQ?oc=5>

### TSMC Stock Just Had Its Best Day Since 2008
- Summary: TSM stock reached a high not seen since 2008, indicating strong market momentum.
- Date: 2026-11-24 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxQeVFFYS1CVFNpYzJZQ2VUM3hMOGFJb2ZnRV9vMzZpYnlXUEZEOTlTZVFwdkg3SGZHekhoRnNKRXlrNU5UeXROQzZHdE5qd2dDcG5pVTFfYnVVa0tPVUkwRUNWQ242R292azd3ckM1dTQwVUF4MlJPNUNNaTRfSG9OQmE2MjUtTmJ5ZWUxVEhYWGw?oc=5>

### Nvidia vs. TSMC: With Jensen Huang Back, Which AI Stock Is the Better Buy for 2027?
- Summary: Analyst comparison of TSMC vs Nvidia for 2027, offering investment guidance.
- Date: 2026-11-23 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxNdWhCeTlBalBJa1lLUlZlX0xlOWFaWUZQS2VTRVFUUEJwbWVrcU85OTVwQXRKRG9ZUldYZjNaZHk0QWN2dWtPblkwdXluTjB5cDFnZjMzMVEyaVZSZG9QVTdvVUFGSFV1Yk1vd09tQ3Y3NTN1RzNpMHBNQUtsZzBOZFpBdDhjeXRQaWw3MTNFX2Y1ZUdkbjZhZFBmYzNuZ1pUSFlhb3laRG50X0IzQm8wM1p2bUtwOHdSSUMxejNSR1FLZlVnbTZQMzVkR0o?oc=5>

### Why is Taiwan Semiconductor Manufacturing stock surging today?
- Summary: Question about recent stock surge, no specific event disclosed.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxOVzYtSW9VcXlfZzBTc1gyWmpWSmRRTVdFcUlFQTNVcWp6ZFh2ZWFwUUJhM0Y1cXdrZ0RKRUFIbjE2ODNPclh3NDMyZGFDZ3prQ1NGbHVDY2RjYk1mSExWLWhZamc2Y3p0ZjZ0eDl2Q1lQelBnUGZkb0JEU2pMM0hTRkl2NDVUbDhlYlhkZDVvWUREWUpPWk9Cb2JteDI1cmVVVWtwa29kTkxNRTBXdVVwSDVXRDMtbHVlUmVkNThRWGo?oc=5>

### Taiwan Semiconductor Manufacturing Co Ltd Stock (TSM) Opened Down by 3.19% on Nov 24: A Full Analysis
- Summary: Stock opened down 3.19% on Nov 24, no underlying event identified.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxOQ1gteVM1R2l0N3l1MndBamRiZGZaQmtqa2RJRWhhU3oxQ3VTSXQza1RhZGlzVFlPRERndzRlWno0VXRERi1GanBtMzFOOHduTkJCTWhMb0gxWjhQal9Wb25QOEtMSlc3d2lhQ2FiTkhQVjBOaDh3UHNwZmJxRzdUTFFJb3RBVU0wdEE?oc=5>

### History Says TSMC Stock Falls Before Its Sales
- Summary: Stock fell before sales announcement, no event specified.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPUFFsQTg2cVZWZjh5R3RsUk1QbkdWTC1VazlPT25ONmVqZ3EyY3o2LU9Sa1BFN1VJZjRiOGF1bXJIZlNKYjYxX3lZdm5RTjE3aHRJUWMzcHg0UWJSYkxLaWJSTHo5VkllWGN1ZjRwX1NpWlhiOVBqNk9BdDFNWXNhRmU4UDZBQUtJckFHYlBPM3ZWOC1vNjVScVl0QUE2bG5RckpvT1E4Wm0xQQ?oc=5>

### Tech rally sparks 14% rise in Taiwan Semiconductor Manufacturing (TSM:NYSE)
- Summary: 14% rise due to tech rally, no specific company event.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxNRTRBZ2lSU1RSRkx2U2U5eDRld2g4V0dfZlY5QjFhX1JPeVlrM2g3WFIxMnhodldqNFlJZHN5VGNFWWRXX0ZyZVBLdDJVWkVseTNyc3hFYjFLR3dBOS1rVVlQaVdzSkxoMEh4NGJwQVNjdGJaV3lvbjd3aUFhVzFKNFBkd2VDdFl6bGhwSWxGb292WWEzQnkxU3dtOHhjQlJNS2xz?oc=5>

### A $1.9 Billion Fund Is Betting Big on Taiwan Semiconductor
- Summary: Fund invests $1.9B, no company action disclosed.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxQVHZTakZkaUN0b2ItZFVIaENoZXVBZGtoeU10TGpXeEU5SUV4eE13ckFTQ3hOOUVyeFFHOTkwNlRpQVNwMkpZNDhmQllMZ3Q2OUlKNnJVcFVJZDBfdnV2WGdYdzdHSDZYeW1WYlVseTdhXzM2TUUyMGtEMUp1UXI5UWZPNERJUnRJRXVaNFRmbVlqX3M?oc=5>

## RISKS

### Taiwan Semiconductor Manufacturing (NYSE:TSM) Pauses Advanced Chip Shipments To China
- Summary: TSMC halts advanced chip shipments to China, potentially impacting revenue and supply chain stability.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxNOGhIWnVaYlI5aFc1emtra29CdDBWS3J0dXVRTFZhQmdXNThUU2hUVXZBYWVLR2RpaHJEX1ZqNnJXTzQyWFJ4Q1BQN1dmeDlXVGxQTDZwTkNKbHlxWUFzT2VaZFFENXBwYjVyV2NCN1d2dVBmODA2MGVUdTk0UEJHcW9Mc2dJRHRTTUpJanI1dGR3dDMyNkVVM1QycU9iVzJ5VGVIUEpJWQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TSM** | **22.63** | **67.07** | **3.22** | **50.90** | **1,811,116,457,984.00 USD** | **23.98** |
| UMC | 12.64 | 2.31 | -0.32 | 25.60 | 33,604,438,016.00 USD | 83.28 |
| GFS | 104.06 | 1.70 | 9.75 | 12.50 | 20,302,282,752.00 USD | 5.55 |
| INTC | N/A | 2.53 | 15.89 | 20.90 | 291,261,972,480.00 USD | 53.12 |

Peers fetched as_of: 2026-11-24; TSM reuses existing data (market data as_of: 2026-11-24); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-24

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMi6wFBVV95cUxPY3NBa1ZIRXJyUHFCWERaWWxiTGFoRW53aGY2Q1pqUzZQNmpiVGpQdG00T2hzVWpQNEN4Q0JBYlRja3FvdWhKaHpxVjVxQjRfQnlwRmc1Tm0tMFVVQjVNTzUzM29rbTlwWE5DZDNRYWM3aHQ0NkNzbGhIUExDa1F3MnhibXEwWEc3RzhUUzNIUkYtV1haWGtfYWdzNnlpaHFLU3dQS1R1dDZKVUx1SC1GczJ5UnMyTVF6alEyblVtdmIwdldnQjhIc01OaDgycmpQQ0pNQlBGaVRmWHJMS1ExemxsdFFVNkpLVEZn?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNbVI3ZDlyMFBRakI3cl8td1J6aTZBWWZnTkdyLTF0cm1ib0JnZjFjMDJ0NTBPMEpKRmZndWtBNG1MTTdsQmFZWTNldm9uOXdMU2EzSFJxWWZnZHozVmo2WFljZml1ekRnRUxNVm9oQ09yeEZRdHlEWjRrcktZWXhocl9RODhHb1dWU21veldIeVkyNWV5NURwZlRQQXoyZEk?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxPQVhxWWp0SU9TOVVGLWQ1azhrbXlnVng0QjBUNzhXS3J1Q1FSU3F4dG1ZYzlzaW0xa3I4M3FoNzVsazV4TTNCRHNOb3BNUHQxVjRRZ011a3licEdIZmdsLUdVVGVJdjZWdlp5X251Q1VhdnZETmFYa3BURGtjenZiX0dqZVZFUkREd29XNkNiM1RuR3l2Y1Q5VE9JRzZ3NEdDY1cxLWRQQlJtTFlzdjk2NzZicThkeFIydzduVjlWUXhKdXNRZkFXbHdUc2pyVnpaaTVMOWR1SQ?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxNbWhPakhJTVpWYXJfa3ozbVM5ZGdaNFB4Nm5PQmREU0tMckNpUjFRcFEzTUlLRDNrWXI2aHY4Y0lhWEp0Nk9WVmg1N0R1RDFneFFjRXhUdnlmRF93TDVLTHNoVVkwd1g2QmQ2OWtRcGVRTk43TXZyZGpaeUFYaEIwS28tMk9OaUI5c2d3Z2NkWlVoNks3YlZ4VlhfdERmeUZVbk04Qml4WkJHVmppUWxDQzUxeVc5c3dpRTd5X2ZtVi1iLVlVb2xzNWRZWS0xcnM?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxQMW5zeVBBNVlWOHV5OTUtc3RHWWh0S0doTGVDeUlNeVJTT2NtUzBQSVpnV2dUMFNuYlBjNVVtMDF6dWxUemItMDJZTVdIUlZteXFLZzNCcjg3cFhGTFIxNlp5MEdnZ3dGSnpiYmI5RDAxMW5wVl93NlVUVDlrclc1Z1hfREwyRWo2Q1hWQ0U5LWRnUE1XU1duRjJ3c3JtNnVqNDhDSU81UFN6UTJKUmpuUHdsdTZVYjdiU0E2TA?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOMEdpVWJwSTh1cU9tb25IQWwwR3VjdlNfYWZUYXI5b3lrZzRTb3c3SHBqVy00endjamt2M3RvMFZLcGZRTmRLcTZTOE92ejJqM09vejF6Y29zRy02XzRQeGJ2a2ZKaTVDNE5DeU1YbjJUc3NOM3plT3NJOWZWZ1ZoTm9YZ0JZZkZGMXZwUkNxQ3NnSVhDWDVn?oc=5
- https://news.google.com/rss/articles/CBMiekFVX3lxTE92TkVUSlNHYU1SY3BsX3E1MWN3elI4c2hqQ0NONE5DOU5FVWl2cTZEVk1tb282dTE0TEJGU1RhRndzTTZhOU5rbXEyVVlRQzd2ckxua1dORnktSjljNG1KNnlrSVQtZEE2YUFxbDFoY0JRdXFRdnZ1UERn?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOY1VYSGNLbGJ2UjctSWx4WFhXV2VLZXozUEVxRWtfUFBiSWkyR0VmUEU2ZWQwMjhJOGNwX0lkTjB3cUhhOUV5aUxEUVNfVVVhVzRFaGVlR1RkbjZ0d05fWXBHT1VXaFVLUVUwMUE5ZjR4eDJOS2ttMUVQbExqSnkzOGpaVHFKQ2d2QnktSVJZYVRseThOSzNiVA?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxPa1JvdC0wSGFvVjBwYUYzVlhoX2FHMkdLMUdUUUtibHZhUmJzWkxoT24wQlBjeGZfWGxydF92YnAxN3BDRl9VdkFtTVRiY0tyc1ZjS1RYWE16NUN1X2ZDLW1SRW9vYmdxSmhFMzU5UmdJSV81RE9XOGNIWEYwZFJCMm1OWTFzWS1hckRybm9MVXZLUV9HVTRNZmZRNVdMNDlhVkprUC1DYTBKOHdv?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxOLWc4NXFYcWoxVVljOGZaR2kzVHF2QnY5X2l0eEY4Ri1BWGNhTzlMWWhiM1BLdWtXWnN2QWhabzliQzBSYjI1UFBMV3gxYUlqMnBfTjhqWTBDb0Z0SUFCeTBxdVRvTjBNVEF2ZFVmeWFXSXQyZ0RNbTZpb0dlYmhLT2Yzc2hzam5ENVVzZzJOSC1kWWN3cjI5WTh0Nm1xVWlGSlVsR2NIWQ?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxQeVFFYS1CVFNpYzJZQ2VUM3hMOGFJb2ZnRV9vMzZpYnlXUEZEOTlTZVFwdkg3SGZHekhoRnNKRXlrNU5UeXROQzZHdE5qd2dDcG5pVTFfYnVVa0tPVUkwRUNWQ242R292azd3ckM1dTQwVUF4MlJPNUNNaTRfSG9OQmE2MjUtTmJ5ZWUxVEhYWGw?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPN002UnhrTzlCU1BJUk1kd2xHVmhXcXk4Y0hwcHE2ZEk2TkVYT3ZmX2k3OWNFQlJMV2RIR2t1QXc0ek9zMzRwVWU2ZEljQ1ZTZ1VWSnRYM0xxVE40eDVTeUpTRklBSFpzSjhUUDZlWFY1Q0NQcXlvcmZENTBSeWotRGJGM2pOWEZXX2pTaXlhZ3cwT0U?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxNdWhCeTlBalBJa1lLUlZlX0xlOWFaWUZQS2VTRVFUUEJwbWVrcU85OTVwQXRKRG9ZUldYZjNaZHk0QWN2dWtPblkwdXluTjB5cDFnZjMzMVEyaVZSZG9QVTdvVUFGSFV1Yk1vd09tQ3Y3NTN1RzNpMHBNQUtsZzBOZFpBdDhjeXRQaWw3MTNFX2Y1ZUdkbjZhZFBmYzNuZ1pUSFlhb3laRG50X0IzQm8wM1p2bUtwOHdSSUMxejNSR1FLZlVnbTZQMzVkR0o?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxOVzYtSW9VcXlfZzBTc1gyWmpWSmRRTVdFcUlFQTNVcWp6ZFh2ZWFwUUJhM0Y1cXdrZ0RKRUFIbjE2ODNPclh3NDMyZGFDZ3prQ1NGbHVDY2RjYk1mSExWLWhZamc2Y3p0ZjZ0eDl2Q1lQelBnUGZkb0JEU2pMM0hTRkl2NDVUbDhlYlhkZDVvWUREWUpPWk9Cb2JteDI1cmVVVWtwa29kTkxNRTBXdVVwSDVXRDMtbHVlUmVkNThRWGo?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxOQ1gteVM1R2l0N3l1MndBamRiZGZaQmtqa2RJRWhhU3oxQ3VTSXQza1RhZGlzVFlPRERndzRlWno0VXRERi1GanBtMzFOOHduTkJCTWhMb0gxWjhQal9Wb25QOEtMSlc3d2lhQ2FiTkhQVjBOaDh3UHNwZmJxRzdUTFFJb3RBVU0wdEE?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPUFFsQTg2cVZWZjh5R3RsUk1QbkdWTC1VazlPT25ONmVqZ3EyY3o2LU9Sa1BFN1VJZjRiOGF1bXJIZlNKYjYxX3lZdm5RTjE3aHRJUWMzcHg0UWJSYkxLaWJSTHo5VkllWGN1ZjRwX1NpWlhiOVBqNk9BdDFNWXNhRmU4UDZBQUtJckFHYlBPM3ZWOC1vNjVScVl0QUE2bG5RckpvT1E4Wm0xQQ?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxNRTRBZ2lSU1RSRkx2U2U5eDRld2g4V0dfZlY5QjFhX1JPeVlrM2g3WFIxMnhodldqNFlJZHN5VGNFWWRXX0ZyZVBLdDJVWkVseTNyc3hFYjFLR3dBOS1rVVlQaVdzSkxoMEh4NGJwQVNjdGJaV3lvbjd3aUFhVzFKNFBkd2VDdFl6bGhwSWxGb292WWEzQnkxU3dtOHhjQlJNS2xz?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxQVHZTakZkaUN0b2ItZFVIaENoZXVBZGtoeU10TGpXeEU5SUV4eE13ckFTQ3hOOUVyeFFHOTkwNlRpQVNwMkpZNDhmQllMZ3Q2OUlKNnJVcFVJZDBfdnV2WGdYdzdHSDZYeW1WYlVseTdhXzM2TUUyMGtEMUp1UXI5UWZPNERJUnRJRXVaNFRmbVlqX3M?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxNOGhIWnVaYlI5aFc1emtra29CdDBWS3J0dXVRTFZhQmdXNThUU2hUVXZBYWVLR2RpaHJEX1ZqNnJXTzQyWFJ4Q1BQN1dmeDlXVGxQTDZwTkNKbHlxWUFzT2VaZFFENXBwYjVyV2NCN1d2dVBmODA2MGVUdTk0UEJHcW9Mc2dJRHRTTUpJanI1dGR3dDMyNkVVM1QycU9iVzJ5VGVIUEpJWQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
