# TSM Intelligence Report

- ticker: **TSM**
- Report as_of: **2026-11-16**
- Market data as_of: **2026-11-16**
- Quant sources: https://finance.yahoo.com/quote/TSM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TSM/key-statistics/
- AI analysis snapshot as_of: **2026-11-16**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-17T06:41:59.285903+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 2, 'ai': 14, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261116T043911Z-b81cfeb4/TSM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **3**; {'directional_claim_without_event_type': 1, 'short_term_price_move_in_structural_risks': 2}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 13 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-11-10

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 373.4500 |
| Return 1D (%) | -6.3401 |
| Return 1W (%) | -3.9036 |
| Return 1M (%) | -9.4908 |
| Return YTD (%) | 23.8561 |
| Return 1Y (%) | 32.5056 |
| Annualized volatility (%) | 42.3579 |
| Beta vs SPY | 2.2002 |
| Max drawdown (%) | -27.3158 |
| Sharpe (rf=0) | 0.9056 |
| Downside deviation (rf=0, %) | 29.3829 |
| Sortino (rf=0) | 1.3055 |
| Historical VaR 95% (1D, %) | 4.2955 |
| Historical ES 95% (1D, %) | 5.9199 |
| Correlation vs SPY | 0.7151 |
| Tracking error vs SPY (%) | 33.9072 |
| P/E (trailing) | 24.20 |
| P/B | 71.27 |
| EV/EBITDA | 3.40 |
| Revenue growth (%) | 50.90 |
| Forward P/E (estimate) | 15.97 |
| Gross margin (%) | 65.85 |
| Operating margin (%) | 57.96 |
| Return on equity (%) | 41.85 |
| Free cash flow yield (%) | N/A |
| MA50 | 428.8628 |
| Close vs MA50 (%) | -12.9209 |
| MA200 | 401.8968 |
| Close vs MA200 (%) | -7.0781 |
| RSI (14, Wilder) | 38.7050 |
| MACD (12,26) | -12.0159 |
| MACD signal (9) | -11.3552 |
| MACD histogram | -0.6607 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TSM': 283, 'SPY': 283}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 373.4500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -6.3401 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -3.9036 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -9.4908 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 23.8561 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 32.5056 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 42.3579 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 29.3829 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.3055 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.2955 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.9199 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.7151 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 33.9072 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.2002 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.3158 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9056 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.9694 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 65.8460 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 57.9600 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 41.8550 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 24.2029 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 38.7050 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.6607 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -12.9209 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -7.0781 -> Clearly below the moving-average trend level.

## TAILWINDS

### TSMC approves a $500m investment company to back the next Nvidia and, for the first time, its own suppliers
- Summary: TSMC backs a $500m investment firm to support Nvidia and its suppliers, strengthening its AI ecosystem.
- Date: 2026-11-16 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxNclpNUE5XRWFCUWhRcUF3WDFZVXQwVnlCV1hkTWJLRjBTQm85ek1aNjY1RWtvVWZTYXdhMkVuai14SVJCSVRibkpWME1xVXdURVkzdjZSdnBFempYa2RydElQeEV4TXM3aGFmeklRbDBtM2dtWF83eldpZkoyYUpscWhhNVFHVXRfSXROckNuc1BlWmMyRm1XT3pBbm9pcXNac1JkLVRDMGVzdFpRbC0wUG9HTFhyZmVFcnpKVU5xbVV3MUtMdlg5R0JzY0UybjY3ZG5KaQ?oc=5>

### Taiwan Semiconductor Manufacturing (TSM) Takes A $1 Billion Step Further Into AI
- Summary: TSM invests $1B to expand AI chip capabilities, boosting its product portfolio.
- Date: 2026-11-13 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxORVdVMmRDVnBVTWo0N1lvQzh1U05OUnZveUs1Q08wLWFOVHQ2d3dPb3hRNVcyVFJ0TFQ2dWFKX1NZcDR4UTA3QXk3SXo4WkVyQXYycjVGVGNVVGlEZWtJSnBsY2N4X3dCM1pTaHZzcE5xOW8zMl8xak1tUjhzZUtRZWg3a1VaeDRXWFlYaUc1MmV1OXNpQ2ZjYkZXU1VxWmZpZW9IQzVLZy11RGFB?oc=5>

### Taiwan Semi's deal with power supplier provides long-term visibility for Arizona fab: BofA (TSM:NYSE)
- Summary: TSM secures long-term power supply for Arizona fab, ensuring operational stability.
- Date: 2026-11-16 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxQLWJWOTdOYUdwOVc1MnhqeDRTeTBRZUVtVldqS0ZveFAxOFp1M1BOLTRFOWxBdGVmblZuVUxEUFVTRFJPU1cwSEtCeDBvN1JWcmJhWGRXZmxCQmtJRDVYdFQzVlZCSm5kQnUySVR5T3BwSWpDZmNPME9SeFdDNmtnZFQ5NFZ6cG5LUGs3dEc3cmlqNE1yS1BOaUZuR1dfRFNwa3I4Yy1jRjB3OHRrVklqSm9DTjczR1g2TEF5cmZZUFNwM0da?oc=5>

## HEADWINDS

### Taiwan Semiconductor Manufacturing (NYSE:TSM) Stock Price Down 6.4% - Here's What Happened
- Summary: Taiwan Semiconductor Manufacturing (NYSE:TSM) Stock Price Down 6.4% - Here's What Happened
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2wFBVV95cUxPTDdOVWZodndEeDYyb2RxZkdmRC1XYW9FZ1RZR2xXRW5WMTJzX0JoaER4UjdHaGs2V25XTEh2NlZCSnpadk4zVThjdGpUU09KUEV3U2hWeV9oUWxvMVJSUmRTNzEtZjNobXdpZk93LUVpZWFUWUw4UmpEbmVXMlE3aWxsNVJJM3lZWFNfeUhUMUk5M3kxN0FoYVBMMkpxZ3JkdEJxWklsdW1GVFBMWWM5R21nRGRyU3l3VFl3MkREbkFDR1k2OXBtUl9xVDFSX1BNM1Y4QXhxeDhmM0E?oc=5>

### Taiwan Semiconductor Manufacturing (TSM) Stock Could Be 7% Undervalued Despite Fab Expansion Plans
- Summary: Analysts suggest TSMC may be undervalued, indicating potential downside risk.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxNclhidVc5Z2VTNE9uZzRCcldGRDUzLXcyc1otalhRaExZNHR2cVRPNk03Z052ekExdUt1QzgxWGkya1NHcElYeWowOXRESHM1UFlsZUx3Yi14bUFHcHp3bVJuTlJPUDlzZFZjYV9URFR6b19NQVRtYUhMdFNobGIwWWFJb1JwODdWM1h6ZjQ4RS1obDRfNUkxdHdGUDdFR0JqbkhnX2ZzVUtRTml2Nmc?oc=5>

### Is TSM Still a Buy as AI Growth Faces Heavy Spending and Valuation?
- Summary: Analyst questions TSM's valuation amid high AI spending, indicating potential downside.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxPSWM2MHNEREw5SUdxcWtzVGRYY09kUTQ1YzMwZE5WdGRaQ3VCVVd6eDBkNHZyUlIycTBUZWlyeHI2eE9oM2NBQTkzMTg0cU9XR0FtSkw0Q3FYT205cDVkeUw3eDA5NFdVbUN4ZGRQM1JPaHRTSDAwVW9CNVZ6dXJNbTAzZm9YZUVFYlV4WXZfLUFIZw?oc=5>

### TSMC Stocks Slide 5.7% Despite October Sales Jumping 59.7% to a 2026 High
- Summary: TSMC shares fell 5.7% even though October sales surged 59.7% to a 2026 high.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxOdDFoUmJjTGZBTE1YaVVtdDI3X2N3U0NDTWdnTno2aXZGSVZvSVFvOGc5enZHTFh2dFc2aHdpNHlFcGVMWUwySWtMSWR0Q3NKR1NFZnFhYWtRVDZ2R1h5VlN1M1lXME9fOG1yRlpjWi1ZZlpnenRKaWJwQVlBaWVOTVBqSXQ2N1ZfV2paWFNyUjVjSV9BUExYSkR1YlBDbVYwTUFZSmlYRklJc2xDLVoxQkVSdnlQRTJKQm1BMTIzU084MmtPbkZMbVVNaw?oc=5>

### INTW 2X Intel ETF Tumbles 13% as Intel Drops Amid Shareholder Lawsuit and AI Chip Selloff; Taiwan Semiconductor Falls 5%
- Summary: Taiwan Semiconductor shares fell 5% amid broader market selloff linked to Intel's lawsuit and AI chip concerns.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi8wFBVV95cUxPT0lEcGNlTVBvYV9uUEdhNHBMQnhEaS1DMXUybEYwTDdFWDNGc2hJendVWUM1M1ptTFVQMEs3cWlzWHFqZ3ZOOU5NNFhyMGpUTUVzWklhTjdnMF91WEd2YWNqU3JCQi0xaWJReEVOUmZrNjlETFo4NVgwQTI1VGVXaHhYaXZBeTRPeGpLSzZYbFVzWGVmTTRxNjlxZUZhS2hzaGRnQVRMRFFYSFpPdllWc2lMbFh3UVVyNWFld2ZqWWxUWUtXM3g2SDlUWmZ0Qjdka0Zxamc1ZlVBcEM2RjR2N0ZfWVl4em1fZW82WFM0cnBYcmM?oc=5>

### NVIDIA Falls 4% Ahead of Earnings as Elon Musk Joins Calls to Reinstate Jensen Huang; AMD Drops 6%, Taiwan Semiconductor Slides 5%
- Summary: TSM shares slid 5% as NVIDIA and AMD fell, reflecting market uncertainty ahead of earnings.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi_gFBVV95cUxNTlF0QzdtLURGTVV5cHVhYzlGdXdHMG80eFVuWVk1QVlQOU5kWHo3d0l1cjBxYmlYT0E2Y0pzNnA3cEQxNUpmX0ZOSDk3d2ZIbkl2WkkxMTdDZTV0d0dPcWFQc1haX19jbmdzLS0xSWY4WGJUcGFBY0FKYVF6YVJxb3JPc3RwVVRZRF9VMXB4MXFuM09Sazk0ZlJaSS11UnRhMWpSZzVvOTNYY3Q4TWhvaV9tSGlEMU5vaHY3ZFRnamU2bV9zc3VUWnVOMnJqSFM3WHNGaUV0c2hKY0F4MF9MWnJDTGNqc2VnWUt5V3JVeHAwVWVQWjV1ZVBqb1RFUQ?oc=5>

## CATALYSTS

### TSMC (NYSE:TSM) Stock in Focus as Taiwan Market Plunges 6% Ahead of Nvidia Earnings
- Summary: TSMC (NYSE:TSM) Stock in Focus as Taiwan Market Plunges 6% Ahead of Nvidia Earnings
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTE5YY3ZmZHdGc3d6cG9Qa3RZcmE4akZFUm5GY0xOcElqbnV2em1iQXlJbjJxaUt2VWxRbTRRN1h5bnNrS3FxWEwyMVlUeEpjZHdIdC1qRTVmNkUxOFI2RGtOVURuNjRiYVlrNkJEMFZiNUwzb0JsLWM3TU5aR3J2UQ?oc=5>

### Top Analyst Reports for Taiwan Semiconductor, Johnson & Johnson and Palantir
- Summary: Analyst reports released for TSM, J&J, and Palantir.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxOek1YUnU3MkZUQWl6NWUxelEzOUdUdHRPbkdYbTFaVS03ZndibW5ZTUUyNkMwNllNS0RWS21HZGowRjZQZTVDZW5KMTgtajM0M2d2UE1qc1BrZ1BVM2RmdnpPT0FTQjZIYkhPSWluRS1WN0E1Q2U0ckF4TnlGNGpiVEduaVhBN0ZXRndtVjNaVW9mbnotSHJyUi1oeVloNHpOcWdqV3BMWmU?oc=5>

### Nvidia Stock Shock Has Investors Looking At TSMC And AI Chip Tooling
- Summary: Nvidia's stock shock drives investor focus to TSMC's AI tooling, potentially boosting demand.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxPYlRMMDd2bUVuYUdUMWIzRGlaUkRWQXZlYlVWejJ6Skdnclc3RkVsYkhxblQtNGx1bXdRLVAxNENXLWlyNEdWR2JEMGljcENZb2RkNnI1M01xUEFsMUF2d05jNENQYmhuOWdLYjAzMjJ6Z1Ffb1Y0X3FqUGhzalhQOHM1MVRwNnk0dUtyRlNzcDVRY2ZMLWJjZmtNejFOZGxTLUE?oc=5>

### TSM's $2 Billion Packaging Deal Could Ease a Critical AI Bottleneck
- Summary: TSM announced a $2B packaging partnership to address AI chip bottlenecks.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxNSjF2Nm5YWGFmWk9UTVloaHRsUDUtMmdkWGtQWnZ4d2RyUjVjVVRHVWlSMkU5dDE1UFZsMmlFNXBlb3IzeFh5MlNidDFyT2FIUWZrT180cC1GZzB1S3BVMEVLT19UY09rWFJPUkpPLUxHSlRPdmVFSlNQWi01dGlyQVhiN0R0SWd2bFdUYzRFdE1WbVdQNk44a0piYldMVi03cTAtenRjN0Z1MTZBaEpteElEZGcxM1U4TEdZTng3VQ?oc=5>

## RISKS

### TSMC Slumps 6% on Nvidia Financing Fears - Taiwan Semiconductor (NYSE:TSM)
- Summary: TSM shares fell 6% amid Nvidia financing concerns.
- Date: 2026-11-16 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNYzh1VFNkVHJxRm5iWlhSV3NvX0JlaUlCRG5sM0h5MVFPazFKai14OGhacVRQb2I0c2ZwcFI3Mzh4U0MwaHZDdG5XLW00NzU5Ui1XNElBZmdBYXdmR1lwc2pJbktPNHlPNWdKaDBzWVVlUHgxZklZNGYzMUx5UGJENC1qakNfY0REWWZSOGdPb3lvZw?oc=5>

### Why is Taiwan Semiconductor Manufacturing stock tumbling today?
- Summary: TSM stock is experiencing a sharp decline today.
- Date: 2026-11-16 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxQQjdLMF9mOWJpSXhRa3BhSlAzcEs3V1FSTFhMWGZzQ2hsNnBwZ0VWMDZfRVBHNVZ1M3Njak1QUlh2TkxKLVpCVmcwLVNKbk9WOHczbVVqZS12bmJHeENMb2E0c0MxS0VLOV9WVS1QcE5ZZHZ0Zk1MeWh5NFVQbGFRQkdET0thY3JMRTM0b0hPb1FhWVpUZGxid2V2Njg1YnF6dEtZc0ljbzdYM0FlMUJWeGtfRnFrcTNESHZ0aWR5NWZ5UQ?oc=5>

### 3G Capital starts position Nu, adds to Taiwan Semiconductor, cuts stake in Intel among Q3 moves
- Summary: 3G Capital increased stake in TSM, reducing Intel holdings.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxPVWNydFZUeWs2VjEtQnFKQ2FMNE83VVdQaEJqM1FOd1JQQ3h5UlFxMUVLVEVvbmhRUVRTcklONFBELUFDUk9YRWFiQnRlaDdwWHJBTDF1ak1TQ0g2OWF3dC1SdF9vN0FmbHpIVHJmaFJ4ZjNZWWNWV0E0dW50TUgweE9NdUFfckNEOGFjMUYwTnlyYUd6MjFhQldmb1pWYVA0WnZXeFhSbGZJWXVZa3M4czR0MzhrQ04xWGZueE9uMklrYU04RFZYMFdwQQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TSM** | **24.20** | **71.27** | **3.40** | **50.90** | **1,936,888,430,592.00 USD** | **32.51** |
| UMC | 13.53 | 2.47 | -0.30 | 25.60 | 35,961,765,888.00 USD | 104.37 |
| GFS | 112.63 | 1.84 | 10.57 | 12.50 | 21,974,630,400.00 USD | 19.75 |
| INTC | N/A | 2.56 | 16.07 | 20.90 | 294,823,034,880.00 USD | 56.17 |

Peers fetched as_of: 2026-11-16; TSM reuses existing data (market data as_of: 2026-11-16); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-16

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

- https://news.google.com/rss/articles/CBMi1AFBVV95cUxNclpNUE5XRWFCUWhRcUF3WDFZVXQwVnlCV1hkTWJLRjBTQm85ek1aNjY1RWtvVWZTYXdhMkVuai14SVJCSVRibkpWME1xVXdURVkzdjZSdnBFempYa2RydElQeEV4TXM3aGFmeklRbDBtM2dtWF83eldpZkoyYUpscWhhNVFHVXRfSXROckNuc1BlWmMyRm1XT3pBbm9pcXNac1JkLVRDMGVzdFpRbC0wUG9HTFhyZmVFcnpKVU5xbVV3MUtMdlg5R0JzY0UybjY3ZG5KaQ?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxORVdVMmRDVnBVTWo0N1lvQzh1U05OUnZveUs1Q08wLWFOVHQ2d3dPb3hRNVcyVFJ0TFQ2dWFKX1NZcDR4UTA3QXk3SXo4WkVyQXYycjVGVGNVVGlEZWtJSnBsY2N4X3dCM1pTaHZzcE5xOW8zMl8xak1tUjhzZUtRZWg3a1VaeDRXWFlYaUc1MmV1OXNpQ2ZjYkZXU1VxWmZpZW9IQzVLZy11RGFB?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxQLWJWOTdOYUdwOVc1MnhqeDRTeTBRZUVtVldqS0ZveFAxOFp1M1BOLTRFOWxBdGVmblZuVUxEUFVTRFJPU1cwSEtCeDBvN1JWcmJhWGRXZmxCQmtJRDVYdFQzVlZCSm5kQnUySVR5T3BwSWpDZmNPME9SeFdDNmtnZFQ5NFZ6cG5LUGs3dEc3cmlqNE1yS1BOaUZuR1dfRFNwa3I4Yy1jRjB3OHRrVklqSm9DTjczR1g2TEF5cmZZUFNwM0da?oc=5
- https://news.google.com/rss/articles/CBMi2wFBVV95cUxPTDdOVWZodndEeDYyb2RxZkdmRC1XYW9FZ1RZR2xXRW5WMTJzX0JoaER4UjdHaGs2V25XTEh2NlZCSnpadk4zVThjdGpUU09KUEV3U2hWeV9oUWxvMVJSUmRTNzEtZjNobXdpZk93LUVpZWFUWUw4UmpEbmVXMlE3aWxsNVJJM3lZWFNfeUhUMUk5M3kxN0FoYVBMMkpxZ3JkdEJxWklsdW1GVFBMWWM5R21nRGRyU3l3VFl3MkREbkFDR1k2OXBtUl9xVDFSX1BNM1Y4QXhxeDhmM0E?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxNclhidVc5Z2VTNE9uZzRCcldGRDUzLXcyc1otalhRaExZNHR2cVRPNk03Z052ekExdUt1QzgxWGkya1NHcElYeWowOXRESHM1UFlsZUx3Yi14bUFHcHp3bVJuTlJPUDlzZFZjYV9URFR6b19NQVRtYUhMdFNobGIwWWFJb1JwODdWM1h6ZjQ4RS1obDRfNUkxdHdGUDdFR0JqbkhnX2ZzVUtRTml2Nmc?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxPSWM2MHNEREw5SUdxcWtzVGRYY09kUTQ1YzMwZE5WdGRaQ3VCVVd6eDBkNHZyUlIycTBUZWlyeHI2eE9oM2NBQTkzMTg0cU9XR0FtSkw0Q3FYT205cDVkeUw3eDA5NFdVbUN4ZGRQM1JPaHRTSDAwVW9CNVZ6dXJNbTAzZm9YZUVFYlV4WXZfLUFIZw?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxOdDFoUmJjTGZBTE1YaVVtdDI3X2N3U0NDTWdnTno2aXZGSVZvSVFvOGc5enZHTFh2dFc2aHdpNHlFcGVMWUwySWtMSWR0Q3NKR1NFZnFhYWtRVDZ2R1h5VlN1M1lXME9fOG1yRlpjWi1ZZlpnenRKaWJwQVlBaWVOTVBqSXQ2N1ZfV2paWFNyUjVjSV9BUExYSkR1YlBDbVYwTUFZSmlYRklJc2xDLVoxQkVSdnlQRTJKQm1BMTIzU084MmtPbkZMbVVNaw?oc=5
- https://news.google.com/rss/articles/CBMi8wFBVV95cUxPT0lEcGNlTVBvYV9uUEdhNHBMQnhEaS1DMXUybEYwTDdFWDNGc2hJendVWUM1M1ptTFVQMEs3cWlzWHFqZ3ZOOU5NNFhyMGpUTUVzWklhTjdnMF91WEd2YWNqU3JCQi0xaWJReEVOUmZrNjlETFo4NVgwQTI1VGVXaHhYaXZBeTRPeGpLSzZYbFVzWGVmTTRxNjlxZUZhS2hzaGRnQVRMRFFYSFpPdllWc2lMbFh3UVVyNWFld2ZqWWxUWUtXM3g2SDlUWmZ0Qjdka0Zxamc1ZlVBcEM2RjR2N0ZfWVl4em1fZW82WFM0cnBYcmM?oc=5
- https://news.google.com/rss/articles/CBMi_gFBVV95cUxNTlF0QzdtLURGTVV5cHVhYzlGdXdHMG80eFVuWVk1QVlQOU5kWHo3d0l1cjBxYmlYT0E2Y0pzNnA3cEQxNUpmX0ZOSDk3d2ZIbkl2WkkxMTdDZTV0d0dPcWFQc1haX19jbmdzLS0xSWY4WGJUcGFBY0FKYVF6YVJxb3JPc3RwVVRZRF9VMXB4MXFuM09Sazk0ZlJaSS11UnRhMWpSZzVvOTNYY3Q4TWhvaV9tSGlEMU5vaHY3ZFRnamU2bV9zc3VUWnVOMnJqSFM3WHNGaUV0c2hKY0F4MF9MWnJDTGNqc2VnWUt5V3JVeHAwVWVQWjV1ZVBqb1RFUQ?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTE5YY3ZmZHdGc3d6cG9Qa3RZcmE4akZFUm5GY0xOcElqbnV2em1iQXlJbjJxaUt2VWxRbTRRN1h5bnNrS3FxWEwyMVlUeEpjZHdIdC1qRTVmNkUxOFI2RGtOVURuNjRiYVlrNkJEMFZiNUwzb0JsLWM3TU5aR3J2UQ?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxOek1YUnU3MkZUQWl6NWUxelEzOUdUdHRPbkdYbTFaVS03ZndibW5ZTUUyNkMwNllNS0RWS21HZGowRjZQZTVDZW5KMTgtajM0M2d2UE1qc1BrZ1BVM2RmdnpPT0FTQjZIYkhPSWluRS1WN0E1Q2U0ckF4TnlGNGpiVEduaVhBN0ZXRndtVjNaVW9mbnotSHJyUi1oeVloNHpOcWdqV3BMWmU?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxPYlRMMDd2bUVuYUdUMWIzRGlaUkRWQXZlYlVWejJ6Skdnclc3RkVsYkhxblQtNGx1bXdRLVAxNENXLWlyNEdWR2JEMGljcENZb2RkNnI1M01xUEFsMUF2d05jNENQYmhuOWdLYjAzMjJ6Z1Ffb1Y0X3FqUGhzalhQOHM1MVRwNnk0dUtyRlNzcDVRY2ZMLWJjZmtNejFOZGxTLUE?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxNSjF2Nm5YWGFmWk9UTVloaHRsUDUtMmdkWGtQWnZ4d2RyUjVjVVRHVWlSMkU5dDE1UFZsMmlFNXBlb3IzeFh5MlNidDFyT2FIUWZrT180cC1GZzB1S3BVMEVLT19UY09rWFJPUkpPLUxHSlRPdmVFSlNQWi01dGlyQVhiN0R0SWd2bFdUYzRFdE1WbVdQNk44a0piYldMVi03cTAtenRjN0Z1MTZBaEpteElEZGcxM1U4TEdZTng3VQ?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNYzh1VFNkVHJxRm5iWlhSV3NvX0JlaUlCRG5sM0h5MVFPazFKai14OGhacVRQb2I0c2ZwcFI3Mzh4U0MwaHZDdG5XLW00NzU5Ui1XNElBZmdBYXdmR1lwc2pJbktPNHlPNWdKaDBzWVVlUHgxZklZNGYzMUx5UGJENC1qakNfY0REWWZSOGdPb3lvZw?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxQQjdLMF9mOWJpSXhRa3BhSlAzcEs3V1FSTFhMWGZzQ2hsNnBwZ0VWMDZfRVBHNVZ1M3Njak1QUlh2TkxKLVpCVmcwLVNKbk9WOHczbVVqZS12bmJHeENMb2E0c0MxS0VLOV9WVS1QcE5ZZHZ0Zk1MeWh5NFVQbGFRQkdET0thY3JMRTM0b0hPb1FhWVpUZGxid2V2Njg1YnF6dEtZc0ljbzdYM0FlMUJWeGtfRnFrcTNESHZ0aWR5NWZ5UQ?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxPVWNydFZUeWs2VjEtQnFKQ2FMNE83VVdQaEJqM1FOd1JQQ3h5UlFxMUVLVEVvbmhRUVRTcklONFBELUFDUk9YRWFiQnRlaDdwWHJBTDF1ak1TQ0g2OWF3dC1SdF9vN0FmbHpIVHJmaFJ4ZjNZWWNWV0E0dW50TUgweE9NdUFfckNEOGFjMUYwTnlyYUd6MjFhQldmb1pWYVA0WnZXeFhSbGZJWXVZa3M4czR0MzhrQ04xWGZueE9uMklrYU04RFZYMFdwQQ?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxNYkNNTGNqZzBPcjlCRUpyTVZSM1NYdEl3UGR5OGlaM1ZRUTBCQXZ0RGdvOXNOc3M2XzVZdjJ1UEIzTnYwWDJNdFl4OHpoenkwVVcyQXlRRk1WZnctM3RXZUZucFgwN05vbVotMXFkR0JpS2MyUzN5Ty1GWTlhdmlkajVSV2dHNUxkR2VhNVRjVnYxbmJlZDZUMnJHOUVoZWRkbDJkNHJqaTJmRXlCbDQ0U2VWd1V6VlFlR05nRmR6c1pOQU9iVEdGTzlhdjBfWnU5SFg1ZGcwSm1MOHVMUDVqVk80dDZ3UUlsMzF4cg?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
