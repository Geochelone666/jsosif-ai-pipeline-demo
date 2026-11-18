# TSM Intelligence Report

- ticker: **TSM**
- Report as_of: **2026-11-17**
- Market data as_of: **2026-11-17**
- Quant sources: https://finance.yahoo.com/quote/TSM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TSM/key-statistics/
- AI analysis snapshot as_of: **2026-11-17**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-18T06:04:13.852586+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 1, 'ai': 18, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261117T062519Z-6171f6c2/TSM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'directional_claim_without_event_type': 1, 'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 13 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 29.17%; oldest publication 2026-11-10

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 359.6900 |
| Return 1D (%) | -3.6846 |
| Return 1W (%) | -9.2792 |
| Return 1M (%) | -12.8257 |
| Return YTD (%) | 19.2926 |
| Return 1Y (%) | 28.8950 |
| Annualized volatility (%) | 42.4476 |
| Beta vs SPY | 2.2086 |
| Max drawdown (%) | -27.3158 |
| Sharpe (rf=0) | 0.8129 |
| Downside deviation (rf=0, %) | 29.5558 |
| Sortino (rf=0) | 1.1675 |
| Historical VaR 95% (1D, %) | 4.2918 |
| Historical ES 95% (1D, %) | 5.9199 |
| Correlation vs SPY | 0.7170 |
| Tracking error vs SPY (%) | 33.9531 |
| P/E (trailing) | 23.31 |
| P/B | 69.09 |
| EV/EBITDA | 3.34 |
| Revenue growth (%) | 50.90 |
| Forward P/E (estimate) | 15.38 |
| Gross margin (%) | 65.85 |
| Operating margin (%) | 57.96 |
| Return on equity (%) | 41.86 |
| Free cash flow yield (%) | N/A |
| MA50 | 427.3001 |
| Close vs MA50 (%) | -15.8226 |
| MA200 | 402.0018 |
| Close vs MA200 (%) | -10.5253 |
| RSI (14, Wilder) | 35.6688 |
| MACD (12,26) | -14.1280 |
| MACD signal (9) | -11.9098 |
| MACD histogram | -2.2182 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TSM': 284, 'SPY': 284}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 359.6900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -3.6846 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -9.2792 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -12.8257 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 19.2926 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 28.8950 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 42.4476 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 29.5558 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.1675 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.2918 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.9199 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.7170 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 33.9531 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.2086 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.3158 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.8129 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.3810 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 65.8460 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 57.9610 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 41.8600 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 23.3111 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 35.6688 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -2.2182 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -15.8226 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -10.5253 -> Clearly below the moving-average trend level.

## TAILWINDS

### Taiwan Semi's deal with power supplier provides long-term visibility for Arizona fab: BofA (TSM:NYSE)
- Summary: TSM secures long-term power supply for Arizona fab, ensuring operational stability.
- Date: 2026-11-16 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxQLWJWOTdOYUdwOVc1MnhqeDRTeTBRZUVtVldqS0ZveFAxOFp1M1BOLTRFOWxBdGVmblZuVUxEUFVTRFJPU1cwSEtCeDBvN1JWcmJhWGRXZmxCQmtJRDVYdFQzVlZCSm5kQnUySVR5T3BwSWpDZmNPME9SeFdDNmtnZFQ5NFZ6cG5LUGs3dEc3cmlqNE1yS1BOaUZuR1dfRFNwa3I4Yy1jRjB3OHRrVklqSm9DTjczR1g2TEF5cmZZUFNwM0da?oc=5>

### Taiwan Semiconductor Manufacturing (TSM) Takes A $1 Billion Step Further Into AI
- Summary: TSM invests $1B to expand AI chip capabilities, boosting its product portfolio.
- Date: 2026-11-13 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxORVdVMmRDVnBVTWo0N1lvQzh1U05OUnZveUs1Q08wLWFOVHQ2d3dPb3hRNVcyVFJ0TFQ2dWFKX1NZcDR4UTA3QXk3SXo4WkVyQXYycjVGVGNVVGlEZWtJSnBsY2N4X3dCM1pTaHZzcE5xOW8zMl8xak1tUjhzZUtRZWg3a1VaeDRXWFlYaUc1MmV1OXNpQ2ZjYkZXU1VxWmZpZW9IQzVLZy11RGFB?oc=5>

### Joseph Carlson Eyes TSMC Over NVDA After 7.7% Drop in 2 Days - Taiwan Semiconductor (NYSE:TSM)
- Summary: Analyst Joseph Carlson shows interest in TSMC, favoring it over NVDA after a sharp drop.
- Date: 2026-11-17 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxOc1NIa2Q0a0VLLU1HWVViaUpIWkdhREpSTlB4UVc1SWZLVV9sdC14WGhRMTc0NlZmOVJ5OHJLOV9Wd0ZHX1JQWG1LQWRKVUpPaUNIcm5NbUZ2OE5iR0tIbF85UUlkbVRGNTF2RkpZYVRobVdDWS01dDBidThIM2liYV9XRlpMMHJsdXBXZC03WQ?oc=5>

### Surging AI Demand and Advanced Chipmaking Strengthens Taiwan Semiconductor Manufacturing Company Limited (TSM) Growth Outlook
- Summary: AI demand and advanced chipmaking boost TSMC’s growth outlook.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPc2hWWjNRTC1WNlBrNGRnN19wdlRTMVZaMHJmTmdxRm5xTlBUdEpZX0ZMc29adFJKcGdrSEo3Q192X0FtWGxjaXZYOG9hR0VaX2RGZ25GVGhlREZxR1ozV1pCZ3ZPbTlVeG9WWXJCc0x2T1gtdUJHR0xQUzZPa1dMOXhjZEJETzhNQldveFFPUmQtNmU2T3JXWXRUdDAwWXhUa0lj?oc=5>

### Taiwan Semiconductor Manufacturing (NYSE:TSM) Hit A Revenue High, Is The Stock Fully Valued?
- Summary: TSM reported a revenue high, indicating strong financial performance.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNdFZMVDR0eERfMHJrVHExSVR2VjhvaXMyNnN1YTBPY1FrLUxWVWtrRmMzTDMtN0RPUlB4RGI4dW9uODFLRVNRWmh4Vk4zZ3dLSmFSTVZHaEJsbjVOQk1jUHFyeEFUeXRjMm5VY2J4UWlRZXVWWnNWcGZwajNrVDlqWmNEMHVJQW5Tb2ZMQjNIUDREZ0M1NE13?oc=5>

### Taiwan Semiconductor Booked a Record NT$587 Billion Month. The Stock Has Lost Nearly 10% in Three Days Anyway
- Summary: TSM booked record monthly revenue, showing robust sales.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxOaHExV3laWFhjQ1o4WFdDUWttdkxGckxUVkVtemV5dFcyYm5BMWNQbUJuR2Ezb2QxcVY4YmNLajBVbzhEX3lwMWRYUU5uQjdSdVJFM0stMjdWV3ZlWlFGZmNwZTZ4M3hBaWFXNXNPVE1sbE8yT0t6QTJCUTFMNU1ralNybjkzaU5KcUlCYUFFbHVLRG5MYjdQVU5PeVY5RFRheWlKVg?oc=5>

## HEADWINDS

### Taiwan Semiconductor Falls 4% as U.S. Tightens AI Chip Curbs on China; Intel Drops 3%, AMD Slides 2%
- Summary: Taiwan Semiconductor Falls 4% as U.S. Tightens AI Chip Curbs on China; Intel Drops 3%, AMD Slides 2%
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxQbTYxU1FmUU5YaC1IY0pVU2FNWHVqZkpud3MybzRhZW9MR3RYNDdwUGFzSkJWTEJELWVWcFNIWU1GcU94QnRJRDl0OUYtTXVyeFlacWxLQnVWRTh0ZmVKaEwyNHd1MUtNdWZ6X1diRW5IZVJOeHVWQS1pRndMQTdUbGw0ODNZTmdYUjRCRUx0VHFtZDdvT3k0clRGdTRDYS1tek1hcEFGLVVjaUZ2bzdRdDJfOXh3RGdVMTg5S0ZFS0txdm8xWmJJaWQ3RFItZ2hNRkw2ZA?oc=5>

### NVIDIA Falls 4% Ahead of Earnings as Elon Musk Joins Calls to Reinstate Jensen Huang; AMD Drops 6%, Taiwan Semiconductor Slides 5%
- Summary: TSM shares slid 5% as NVIDIA and AMD fell, reflecting market uncertainty ahead of earnings.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi_gFBVV95cUxNTlF0QzdtLURGTVV5cHVhYzlGdXdHMG80eFVuWVk1QVlQOU5kWHo3d0l1cjBxYmlYT0E2Y0pzNnA3cEQxNUpmX0ZOSDk3d2ZIbkl2WkkxMTdDZTV0d0dPcWFQc1haX19jbmdzLS0xSWY4WGJUcGFBY0FKYVF6YVJxb3JPc3RwVVRZRF9VMXB4MXFuM09Sazk0ZlJaSS11UnRhMWpSZzVvOTNYY3Q4TWhvaV9tSGlEMU5vaHY3ZFRnamU2bV9zc3VUWnVOMnJqSFM3WHNGaUV0c2hKY0F4MF9MWnJDTGNqc2VnWUt5V3JVeHAwVWVQWjV1ZVBqb1RFUQ?oc=5>

### Is TSM Still a Buy as AI Growth Faces Heavy Spending and Valuation?
- Summary: Analyst questions TSM's valuation amid high AI spending, indicating potential downside.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxPSWM2MHNEREw5SUdxcWtzVGRYY09kUTQ1YzMwZE5WdGRaQ3VCVVd6eDBkNHZyUlIycTBUZWlyeHI2eE9oM2NBQTkzMTg0cU9XR0FtSkw0Q3FYT205cDVkeUw3eDA5NFdVbUN4ZGRQM1JPaHRTSDAwVW9CNVZ6dXJNbTAzZm9YZUVFYlV4WXZfLUFIZw?oc=5>

### Taiwan Semiconductor Manufacturing (TSM) Stock Could Be 7% Undervalued Despite Fab Expansion Plans
- Summary: Analysts suggest TSMC may be undervalued, indicating potential downside risk.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxNclhidVc5Z2VTNE9uZzRCcldGRDUzLXcyc1otalhRaExZNHR2cVRPNk03Z052ekExdUt1QzgxWGkya1NHcElYeWowOXRESHM1UFlsZUx3Yi14bUFHcHp3bVJuTlJPUDlzZFZjYV9URFR6b19NQVRtYUhMdFNobGIwWWFJb1JwODdWM1h6ZjQ4RS1obDRfNUkxdHdGUDdFR0JqbkhnX2ZzVUtRTml2Nmc?oc=5>

### Samsung Elec, TSMC shares fall after US announces curbs on China's chip access
- Summary: TSMC shares decline following US curbs on China chip access.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxQcGNxSE1UcHdSX01hUmo4QTVjQmZPcG1oR19fVUdINUVzaEFhaHlIemRCMnBTQkVBZjQ3LXVoNFl5bWxRTWxxU255N3NZZi0xT0JHODJwYXNaVFJVNVA1Smo5ZHdsX3dySklKUUxUd2p3djR4YklCa2xsTW9BMU9ja19aNzlXaHhaaU5rcFBvU2o3WEJnMXU1N0oxR2c0bU9hWHMybWtGdnN5NkN4NVZwbW01d1FhWE5TdVFLZFpn?oc=5>

### Samsung, TSMC Stocks Slide as U.S. Tightens AI Chip Curbs on China
- Summary: US AI chip curbs on China cause TSMC stock slide.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQMEdUZjJMZHRBdU0yNnBjTi1LUGhpc1N6dV90VWxxTi1lckFyZ2twMTBmcjlVQTNKSEdVU3BnY3B6SDhEdk92Tm5uWmVkbUIxeW02andVQjFXX3BKcm9xLTIwQ2JiR3VJc3ZpeHA2eThsbUNVaEJoNURBbjVmZDJRRVRBejc1LVFhRks5VjZCYlBOcFRwVEZveE5R?oc=5>

### TSMC Is Sliding Before Nvidia Reports. Your Chip ETF Is Taking the Hit
- Summary: TSMC shares slide pre-Nvidia report, hurting chip ETFs.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxQNEpVRGhUb1FiUFMtMmJkMHg5b1VhWENfdFNGMmVuVGxmYjYyOE9qcEVzZFVpbFFTX0U2eWlPdEJnRnUweDByNWh4OC10UEZkTmlMb3NwWWVJMG9yc1hxNVhEQ1I5SDVyeWlXY25obnl3SURqSWQ3YlVNRXpBcmVNS0NrM0tSVjg4bXdfeVJ0WVZkai1uenFwallCbmZQQ2RlakNpUGluUVkzNExqdW5GVkZRUEowUVZK?oc=5>

### Taiwan Semiconductor Manufacturing Co Ltd Stock (TSM) Moved Down by 3.37% on Nov 17: What Signal Does It Send?
- Summary: TSM shares fell 3.37%, indicating a negative market reaction.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxNX2Q3SnlKSTY2enlQX0o2OGc0QndpYUZyNnFPUEdHenNJRnJwSlNPeWV0N2Nid1IyazZIUFJZbl8zTnNkMTNFdGMwN2hBVEhSMDhfbTl1STEzZEJXM1U2UkE4aGZMZTI1bDlEc3luWUdrczZaMWZKQWtDRDlDMzlmRTk2ZmxiNDdmRFE?oc=5>

### Taiwan Semiconductor Manufacturing Company Limited (TSM) Pulled Back Amid Broader AI Buildout Correction
- Summary: TSM shares pulled back amid broader AI market correction.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOdjNPOHgzT3pYVEo3cHNwU21pVGxUT1lYcTZiRkFid1lqTUxibFRtbXBNTVAzSGc0eWVDN2xaeFFxaFVFLWlYMmlfbkM1bzZja18yZUR2MFJjZ3BEYU42T1pUcHhGYlFrVDJhTExiWndnRjIxemJhMUR6ZkRMRDJGYU5UZnVSdnZLTjNRSWxyaU12V2FITGplY2VSOEtvTGRH?oc=5>

## CATALYSTS

### Nvidia Stock Shock Has Investors Looking At TSMC And AI Chip Tooling
- Summary: Nvidia's stock shock drives investor focus to TSMC's AI tooling, potentially boosting demand.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxPYlRMMDd2bUVuYUdUMWIzRGlaUkRWQXZlYlVWejJ6Skdnclc3RkVsYkhxblQtNGx1bXdRLVAxNENXLWlyNEdWR2JEMGljcENZb2RkNnI1M01xUEFsMUF2d05jNENQYmhuOWdLYjAzMjJ6Z1Ffb1Y0X3FqUGhzalhQOHM1MVRwNnk0dUtyRlNzcDVRY2ZMLWJjZmtNejFOZGxTLUE?oc=5>

### TSM Plans $500M Investment in Anthropic IPO: Will the Pivot Pay Off?
- Summary: TSM plans a $500M investment in Anthropic's IPO, potentially expanding its AI portfolio.
- Date: 2026-11-17 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPTVNlTHQzd2V0NnVoVFZWcmdfVGg2aGNROTdOaXpWVXZCaEZwdlpSMHplbmFWNFpMbmprLXNTVDhhZ0tYc0QzMnpiMFNZcEVlVHNNcGxrVjJtUlZvY2NKUW9LZTFlMWVTUHk0d3luNGhPbnZaYm1IMGZYTXJtdlg3TllBdEJQejFxS2cwWVU5Rm5pT3Azd0dxOTVHSVpXdjY5?oc=5>

### 3G Capital starts position Nu, adds to Taiwan Semiconductor, cuts stake in Intel among Q3 moves
- Summary: 3G Capital increases its stake in TSM, signaling confidence in the company’s growth prospects.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxNYkNNTGNqZzBPcjlCRUpyTVZSM1NYdEl3UGR5OGlaM1ZRUTBCQXZ0RGdvOXNOc3M2XzVZdjJ1UEIzTnYwWDJNdFl4OHpoenkwVVcyQXlRRk1WZnctM3RXZUZucFgwN05vbVotMXFkR0JpS2MyUzN5Ty1GWTlhdmlkajVSV2dHNUxkR2VhNVRjVnYxbmJlZDZUMnJHOUVoZWRkbDJkNHJqaTJmRXlCbDQ0U2VWd1V6VlFlR05nRmR6c1pOQU9iVEdGTzlhdjBfWnU5SFg1ZGcwSm1MOHVMUDVqVk80dDZ3UUlsMzF4cg?oc=5>

## RISKS

### Why is Taiwan Semiconductor Manufacturing stock tumbling today?
- Summary: TSM stock is experiencing a sharp decline today.
- Date: 2026-11-16 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxQQjdLMF9mOWJpSXhRa3BhSlAzcEs3V1FSTFhMWGZzQ2hsNnBwZ0VWMDZfRVBHNVZ1M3Njak1QUlh2TkxKLVpCVmcwLVNKbk9WOHczbVVqZS12bmJHeENMb2E0c0MxS0VLOV9WVS1QcE5ZZHZ0Zk1MeWh5NFVQbGFRQkdET0thY3JMRTM0b0hPb1FhWVpUZGxid2V2Njg1YnF6dEtZc0ljbzdYM0FlMUJWeGtfRnFrcTNESHZ0aWR5NWZ5UQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TSM** | **23.31** | **69.09** | **3.34** | **50.90** | **1,865,522,479,104.00 USD** | **28.89** |
| UMC | 13.34 | 2.44 | -0.31 | 25.60 | 35,460,206,592.00 USD | 104.97 |
| GFS | 113.14 | 1.85 | 10.62 | 12.50 | 22,074,970,112.00 USD | 20.62 |
| INTC | N/A | 2.55 | 15.99 | 20.90 | 293,228,544,000.00 USD | 58.95 |

Peers fetched as_of: 2026-11-17; TSM reuses existing data (market data as_of: 2026-11-17); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-17

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

- https://news.google.com/rss/articles/CBMixAFBVV95cUxQLWJWOTdOYUdwOVc1MnhqeDRTeTBRZUVtVldqS0ZveFAxOFp1M1BOLTRFOWxBdGVmblZuVUxEUFVTRFJPU1cwSEtCeDBvN1JWcmJhWGRXZmxCQmtJRDVYdFQzVlZCSm5kQnUySVR5T3BwSWpDZmNPME9SeFdDNmtnZFQ5NFZ6cG5LUGs3dEc3cmlqNE1yS1BOaUZuR1dfRFNwa3I4Yy1jRjB3OHRrVklqSm9DTjczR1g2TEF5cmZZUFNwM0da?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxORVdVMmRDVnBVTWo0N1lvQzh1U05OUnZveUs1Q08wLWFOVHQ2d3dPb3hRNVcyVFJ0TFQ2dWFKX1NZcDR4UTA3QXk3SXo4WkVyQXYycjVGVGNVVGlEZWtJSnBsY2N4X3dCM1pTaHZzcE5xOW8zMl8xak1tUjhzZUtRZWg3a1VaeDRXWFlYaUc1MmV1OXNpQ2ZjYkZXU1VxWmZpZW9IQzVLZy11RGFB?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxOc1NIa2Q0a0VLLU1HWVViaUpIWkdhREpSTlB4UVc1SWZLVV9sdC14WGhRMTc0NlZmOVJ5OHJLOV9Wd0ZHX1JQWG1LQWRKVUpPaUNIcm5NbUZ2OE5iR0tIbF85UUlkbVRGNTF2RkpZYVRobVdDWS01dDBidThIM2liYV9XRlpMMHJsdXBXZC03WQ?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPc2hWWjNRTC1WNlBrNGRnN19wdlRTMVZaMHJmTmdxRm5xTlBUdEpZX0ZMc29adFJKcGdrSEo3Q192X0FtWGxjaXZYOG9hR0VaX2RGZ25GVGhlREZxR1ozV1pCZ3ZPbTlVeG9WWXJCc0x2T1gtdUJHR0xQUzZPa1dMOXhjZEJETzhNQldveFFPUmQtNmU2T3JXWXRUdDAwWXhUa0lj?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNdFZMVDR0eERfMHJrVHExSVR2VjhvaXMyNnN1YTBPY1FrLUxWVWtrRmMzTDMtN0RPUlB4RGI4dW9uODFLRVNRWmh4Vk4zZ3dLSmFSTVZHaEJsbjVOQk1jUHFyeEFUeXRjMm5VY2J4UWlRZXVWWnNWcGZwajNrVDlqWmNEMHVJQW5Tb2ZMQjNIUDREZ0M1NE13?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxOaHExV3laWFhjQ1o4WFdDUWttdkxGckxUVkVtemV5dFcyYm5BMWNQbUJuR2Ezb2QxcVY4YmNLajBVbzhEX3lwMWRYUU5uQjdSdVJFM0stMjdWV3ZlWlFGZmNwZTZ4M3hBaWFXNXNPVE1sbE8yT0t6QTJCUTFMNU1ralNybjkzaU5KcUlCYUFFbHVLRG5MYjdQVU5PeVY5RFRheWlKVg?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxQbTYxU1FmUU5YaC1IY0pVU2FNWHVqZkpud3MybzRhZW9MR3RYNDdwUGFzSkJWTEJELWVWcFNIWU1GcU94QnRJRDl0OUYtTXVyeFlacWxLQnVWRTh0ZmVKaEwyNHd1MUtNdWZ6X1diRW5IZVJOeHVWQS1pRndMQTdUbGw0ODNZTmdYUjRCRUx0VHFtZDdvT3k0clRGdTRDYS1tek1hcEFGLVVjaUZ2bzdRdDJfOXh3RGdVMTg5S0ZFS0txdm8xWmJJaWQ3RFItZ2hNRkw2ZA?oc=5
- https://news.google.com/rss/articles/CBMi_gFBVV95cUxNTlF0QzdtLURGTVV5cHVhYzlGdXdHMG80eFVuWVk1QVlQOU5kWHo3d0l1cjBxYmlYT0E2Y0pzNnA3cEQxNUpmX0ZOSDk3d2ZIbkl2WkkxMTdDZTV0d0dPcWFQc1haX19jbmdzLS0xSWY4WGJUcGFBY0FKYVF6YVJxb3JPc3RwVVRZRF9VMXB4MXFuM09Sazk0ZlJaSS11UnRhMWpSZzVvOTNYY3Q4TWhvaV9tSGlEMU5vaHY3ZFRnamU2bV9zc3VUWnVOMnJqSFM3WHNGaUV0c2hKY0F4MF9MWnJDTGNqc2VnWUt5V3JVeHAwVWVQWjV1ZVBqb1RFUQ?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxPSWM2MHNEREw5SUdxcWtzVGRYY09kUTQ1YzMwZE5WdGRaQ3VCVVd6eDBkNHZyUlIycTBUZWlyeHI2eE9oM2NBQTkzMTg0cU9XR0FtSkw0Q3FYT205cDVkeUw3eDA5NFdVbUN4ZGRQM1JPaHRTSDAwVW9CNVZ6dXJNbTAzZm9YZUVFYlV4WXZfLUFIZw?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxNclhidVc5Z2VTNE9uZzRCcldGRDUzLXcyc1otalhRaExZNHR2cVRPNk03Z052ekExdUt1QzgxWGkya1NHcElYeWowOXRESHM1UFlsZUx3Yi14bUFHcHp3bVJuTlJPUDlzZFZjYV9URFR6b19NQVRtYUhMdFNobGIwWWFJb1JwODdWM1h6ZjQ4RS1obDRfNUkxdHdGUDdFR0JqbkhnX2ZzVUtRTml2Nmc?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxQcGNxSE1UcHdSX01hUmo4QTVjQmZPcG1oR19fVUdINUVzaEFhaHlIemRCMnBTQkVBZjQ3LXVoNFl5bWxRTWxxU255N3NZZi0xT0JHODJwYXNaVFJVNVA1Smo5ZHdsX3dySklKUUxUd2p3djR4YklCa2xsTW9BMU9ja19aNzlXaHhaaU5rcFBvU2o3WEJnMXU1N0oxR2c0bU9hWHMybWtGdnN5NkN4NVZwbW01d1FhWE5TdVFLZFpn?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQMEdUZjJMZHRBdU0yNnBjTi1LUGhpc1N6dV90VWxxTi1lckFyZ2twMTBmcjlVQTNKSEdVU3BnY3B6SDhEdk92Tm5uWmVkbUIxeW02andVQjFXX3BKcm9xLTIwQ2JiR3VJc3ZpeHA2eThsbUNVaEJoNURBbjVmZDJRRVRBejc1LVFhRks5VjZCYlBOcFRwVEZveE5R?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxQNEpVRGhUb1FiUFMtMmJkMHg5b1VhWENfdFNGMmVuVGxmYjYyOE9qcEVzZFVpbFFTX0U2eWlPdEJnRnUweDByNWh4OC10UEZkTmlMb3NwWWVJMG9yc1hxNVhEQ1I5SDVyeWlXY25obnl3SURqSWQ3YlVNRXpBcmVNS0NrM0tSVjg4bXdfeVJ0WVZkai1uenFwallCbmZQQ2RlakNpUGluUVkzNExqdW5GVkZRUEowUVZK?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxNX2Q3SnlKSTY2enlQX0o2OGc0QndpYUZyNnFPUEdHenNJRnJwSlNPeWV0N2Nid1IyazZIUFJZbl8zTnNkMTNFdGMwN2hBVEhSMDhfbTl1STEzZEJXM1U2UkE4aGZMZTI1bDlEc3luWUdrczZaMWZKQWtDRDlDMzlmRTk2ZmxiNDdmRFE?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOdjNPOHgzT3pYVEo3cHNwU21pVGxUT1lYcTZiRkFid1lqTUxibFRtbXBNTVAzSGc0eWVDN2xaeFFxaFVFLWlYMmlfbkM1bzZja18yZUR2MFJjZ3BEYU42T1pUcHhGYlFrVDJhTExiWndnRjIxemJhMUR6ZkRMRDJGYU5UZnVSdnZLTjNRSWxyaU12V2FITGplY2VSOEtvTGRH?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxPYlRMMDd2bUVuYUdUMWIzRGlaUkRWQXZlYlVWejJ6Skdnclc3RkVsYkhxblQtNGx1bXdRLVAxNENXLWlyNEdWR2JEMGljcENZb2RkNnI1M01xUEFsMUF2d05jNENQYmhuOWdLYjAzMjJ6Z1Ffb1Y0X3FqUGhzalhQOHM1MVRwNnk0dUtyRlNzcDVRY2ZMLWJjZmtNejFOZGxTLUE?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPTVNlTHQzd2V0NnVoVFZWcmdfVGg2aGNROTdOaXpWVXZCaEZwdlpSMHplbmFWNFpMbmprLXNTVDhhZ0tYc0QzMnpiMFNZcEVlVHNNcGxrVjJtUlZvY2NKUW9LZTFlMWVTUHk0d3luNGhPbnZaYm1IMGZYTXJtdlg3TllBdEJQejFxS2cwWVU5Rm5pT3Azd0dxOTVHSVpXdjY5?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxNYkNNTGNqZzBPcjlCRUpyTVZSM1NYdEl3UGR5OGlaM1ZRUTBCQXZ0RGdvOXNOc3M2XzVZdjJ1UEIzTnYwWDJNdFl4OHpoenkwVVcyQXlRRk1WZnctM3RXZUZucFgwN05vbVotMXFkR0JpS2MyUzN5Ty1GWTlhdmlkajVSV2dHNUxkR2VhNVRjVnYxbmJlZDZUMnJHOUVoZWRkbDJkNHJqaTJmRXlCbDQ0U2VWd1V6VlFlR05nRmR6c1pOQU9iVEdGTzlhdjBfWnU5SFg1ZGcwSm1MOHVMUDVqVk80dDZ3UUlsMzF4cg?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxQQjdLMF9mOWJpSXhRa3BhSlAzcEs3V1FSTFhMWGZzQ2hsNnBwZ0VWMDZfRVBHNVZ1M3Njak1QUlh2TkxKLVpCVmcwLVNKbk9WOHczbVVqZS12bmJHeENMb2E0c0MxS0VLOV9WVS1QcE5ZZHZ0Zk1MeWh5NFVQbGFRQkdET0thY3JMRTM0b0hPb1FhWVpUZGxid2V2Njg1YnF6dEtZc0ljbzdYM0FlMUJWeGtfRnFrcTNESHZ0aWR5NWZ5UQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
