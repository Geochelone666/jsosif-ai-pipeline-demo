# TSM Intelligence Report

- ticker: **TSM**
- Report as_of: **2026-11-23**
- Market data as_of: **2026-11-23**
- Quant sources: https://finance.yahoo.com/quote/TSM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TSM/key-statistics/
- AI analysis snapshot as_of: **2026-11-23**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-24T08:24:56.757407+00:00**
- AI status: **Partial: 1 headline remains unclassified and excluded from research conclusions**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 3, 'ai': 12, 'unknown': 1, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261123T053847Z-45053549/TSM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 14 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 20.83%; oldest publication 2026-11-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 363.6000 |
| Return 1D (%) | 14.0849 |
| Return 1W (%) | -2.6376 |
| Return 1M (%) | -13.1204 |
| Return YTD (%) | 20.5893 |
| Return 1Y (%) | 33.5884 |
| Annualized volatility (%) | 45.7025 |
| Beta vs SPY | 2.3190 |
| Max drawdown (%) | -34.3948 |
| Sharpe (rf=0) | 0.7908 |
| Downside deviation (rf=0, %) | 31.1486 |
| Sortino (rf=0) | 1.1603 |
| Historical VaR 95% (1D, %) | 4.3962 |
| Historical ES 95% (1D, %) | 6.3161 |
| Correlation vs SPY | 0.7599 |
| Tracking error vs SPY (%) | 35.6776 |
| P/E (trailing) | 23.56 |
| P/B | 69.84 |
| EV/EBITDA | 3.38 |
| Revenue growth (%) | 50.90 |
| Forward P/E (estimate) | 15.55 |
| Gross margin (%) | 65.85 |
| Operating margin (%) | 57.96 |
| Return on equity (%) | 41.86 |
| Free cash flow yield (%) | N/A |
| MA50 | 421.0395 |
| Close vs MA50 (%) | -13.6423 |
| MA200 | 402.3339 |
| Close vs MA200 (%) | -9.6273 |
| RSI (14, Wilder) | 43.0604 |
| MACD (12,26) | -19.9325 |
| MACD signal (9) | -15.9500 |
| MACD histogram | -3.9826 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TSM': 288, 'SPY': 288}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 363.6000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 14.0849 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.6376 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -13.1204 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 20.5893 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 33.5884 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 45.7025 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 31.1486 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.1603 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.3962 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.3161 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.7599 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 35.6776 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.3190 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -34.3948 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.7908 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.5482 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 65.8460 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 57.9610 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 41.8600 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 23.5645 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 43.0604 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.9826 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -13.6423 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -9.6273 -> Clearly below the moving-average trend level.

## TAILWINDS

### TSMC shares surge almost 15% after halting advanced chip deliveries to some clients due to U.S. regulations
- Summary: TSMC shares surge almost 15% after halting advanced chip deliveries to some clients due to U.S. regulations
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPQTdIdlg4WUU0cTJmTXphUVF0RkRTOXg3SXRabHRIYnpTNWg3aHIwRUV2eS02Z2JwX3ZKV2JYdVNCdDBoMzhicjJSR2dTOF8wLTE5OERyN05UMG53TUJFVkpCempwdXBtbmw3aWFQZXlHNm5qOHlGOEp4aXVGUmQtTUhYbG1aWDdma3dVaHd6dXAtSFUtY0praXFRSlB3Zw?oc=5>

### Why TSMC Stock Soared Today
- Summary: TSMC shares experienced a significant price increase today.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOMEdpVWJwSTh1cU9tb25IQWwwR3VjdlNfYWZUYXI5b3lrZzRTb3c3SHBqVy00endjamt2M3RvMFZLcGZRTmRLcTZTOE92ejJqM09vejF6Y29zRy02XzRQeGJ2a2ZKaTVDNE5DeU1YbjJUc3NOM3plT3NJOWZWZ1ZoTm9YZ0JZZkZGMXZwUkNxQ3NnSVhDWDVn?oc=5>

### If You Invested $100 In Taiwan Semiconductor Stock 10 Years Ago, You Would Have This Much Today
- Summary: Historical performance shows substantial growth over a decade.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxQQzVDWHFBM0JfNG1lQ0NXZnZDRGpraS0wNWttbmFCbjlwTEVycEg4THhxZ3hjMFpIVW1tbXRhM3JjaWFLMGFPLWc2UlE4dkFfVGFIekdOMzUtaXpJTGg4QnhVWTVSRmZVM3hlWlA1V2VwUXlyUV9ScWxuUnNoV29vVl8wZWFwZFV5SHhpVl85RkhiZkxzSW1hTnotRlZPN3p1eHdyVk9CczMwc2J1ZW9FSTZWM1dkeVYzZzBaUUQxMmdzQ3dJcUF1YzVn?oc=5>

### Why is Taiwan Semiconductor Manufacturing stock surging today?
- Summary: TSM stock surges today, reflecting positive market sentiment and potential earnings optimism.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxOVzYtSW9VcXlfZzBTc1gyWmpWSmRRTVdFcUlFQTNVcWp6ZFh2ZWFwUUJhM0Y1cXdrZ0RKRUFIbjE2ODNPclh3NDMyZGFDZ3prQ1NGbHVDY2RjYk1mSExWLWhZamc2Y3p0ZjZ0eDl2Q1lQelBnUGZkb0JEU2pMM0hTRkl2NDVUbDhlYlhkZDVvWUREWUpPWk9Cb2JteDI1cmVVVWtwa29kTkxNRTBXdVVwSDVXRDMtbHVlUmVkNThRWGo?oc=5>

### Tollbooths Like Taiwan Semiconductor Rarely Get This Cheap and With October Revenue Up 60%, I am Taking Advantage
- Summary: Revenue up 60% in October, indicating strong performance.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi6wFBVV95cUxNQkVybnpqUF9GVHpaWk1KbHliV0FLWm5VNEcxNFB3RVUtbFZKdDlvSDhSMTBxOGN1TFFRVXZGWXpoV3Fxc0p5ZmVIVW9yOENXUXNPSV9PRDdOUXM3T3d4YjloUmtVWXlVV3hMOXpmVWJ0aXRoQXBBSXlCcEMxYnZmUjBkMm1mWWluY2s4NmhsYWozSXRIVkFpLVpsZndUT3dyWVEyS1hQUGE2T0VVMmpuaTRqQ2RGX0dPMmV2QzFvX1VNb2tra0pTM2U0SENEd0FseUFwRlU1QzFNVmhlY1pMRzRZY3ZPTmFKQkZv?oc=5>

### Taiwan Semiconductor Manufacturing Co Ltd Stock (TSM) Moved Up by 15.94% on Nov 23: A Full Analysis
- Summary: TSM shares surged 15.94% on Nov 23, indicating strong market momentum.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxOT1Z3NGFEZVR5VndRZlV3TjhwYkd3YjN5dWJqbkpzR2N5VWd3aDlaNHRRVm9WN0lzcEw4NVpLRXhpYlUweFlpYnNiTVktcHE5NTZfU29BTzhMNFh0N294bTEwelowSEtaTndHOWFraHJDVkxfMk5BQVcwbnRhZG95SUpXMkFfNl9hOUE?oc=5>

## HEADWINDS

### TSMC Stock Slides As Taiwan Market Suffers Worst Week Since 1990: What's Going On?
- Summary: TSMC Stock Slides As Taiwan Market Suffers Worst Week Since 1990: What's Going On?
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxPQVhxWWp0SU9TOVVGLWQ1azhrbXlnVng0QjBUNzhXS3J1Q1FSU3F4dG1ZYzlzaW0xa3I4M3FoNzVsazV4TTNCRHNOb3BNUHQxVjRRZ011a3licEdIZmdsLUdVVGVJdjZWdlp5X251Q1VhdnZETmFYa3BURGtjenZiX0dqZVZFUkREd29XNkNiM1RuR3l2Y1Q5VE9JRzZ3NEdDY1cxLWRQQlJtTFlzdjk2NzZicThkeFIydzduVjlWUXhKdXNRZkFXbHdUc2pyVnpaaTVMOWR1SQ?oc=5>

### Taiwan Semiconductor Manufacturing (NYSE:TSM) Shares Tumble As Customer Shock Clouds AI Outlook
- Summary: Taiwan Semiconductor Manufacturing (NYSE:TSM) Shares Tumble As Customer Shock Clouds AI Outlook
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxPRGhfT1h2VHNtYVlES2FYa3lSdm40WmcxQ3d3TGl2bG9xZG5KbHFYeHlqZ044TEFjUHNZZDBvVjZxc3ZxdGxKQ18wc1lXNjVXZzItMUt2Ym50X1lfWk84eXJneUpZYUtIVEdwZFN0SlBXbnpPUWdnNmxPUGVBRDI2amdTUDdOU1Naal9ocl9iSlQ2TkJkVl81ZGlnaTFpcWRFX05XZDl2VzVhcXE1?oc=5>

### TSMC Stock Faces China Fallout, but Wall Street Sees a Bigger Story
- Summary: China fallout poses potential risk to TSMC stock.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxNcWNxU2w0LWRJc2M5YURjMDJpdlZmVHZkWW1ENlJlZmVjLTNsSEJuSHpBWlZqdjd0Z0dCYUlpRHRDVm1DX29IMFdSWGFWRkFFOF9jTjNXeEx0UjhVNWJEN3hEcExLNmZ0RVpBT3FZNi1Ia0ppRUNLYmZsLUFfbEkyNFFmTWxhcTJRVm1HT01Vb011Z0VIQ0NXSVRxeWtwaU1DUk1keDZPa1QtaTNnbVdVYXVwR2tURTNxU21GYWVBQ0F4a0N3?oc=5>

### Taiwan Semiconductor Short Interest Climbs After Q3 Results
- Summary: Short interest in TSM increased post-Q3, signaling bearish sentiment.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxQcmdsWGEzU2FSSUFWRzlnQ0Q1a0hCX0M5OFVYenJJVHI2TzBLTHBXY2ZfVzduVzg2LTlYQlVKcWhOeE5Gc3F3Ql9RWmttbVlHUThzZGl3aUIyVTdOV2NoSElQbDFCT2tfbk43ZGJhWTU4WmtlZmlfMGdCcHRwYUNWejVUQ2RwalNpOTBCaTZublJDMFhCcnJ2MjY3UnIyMDdLS0tHNmRDUlZkYlJXRzNRS1JqNFpHLTAzN2FJX2xzcUtKSjg?oc=5>

## CATALYSTS

### History Says TSMC Stock Falls Before Its Sales
- Summary: TSMC shares decline ahead of sales, indicating potential short-term downside.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPUFFsQTg2cVZWZjh5R3RsUk1QbkdWTC1VazlPT25ONmVqZ3EyY3o2LU9Sa1BFN1VJZjRiOGF1bXJIZlNKYjYxX3lZdm5RTjE3aHRJUWMzcHg0UWJSYkxLaWJSTHo5VkllWGN1ZjRwX1NpWlhiOVBqNk9BdDFNWXNhRmU4UDZBQUtJckFHYlBPM3ZWOC1vNjVScVl0QUE2bG5RckpvT1E4Wm0xQQ?oc=5>

### A $1.9 Billion Fund Is Betting Big on Taiwan Semiconductor
- Summary: A fund invested $1.9B in TSM, boosting ownership stakes.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxQVHZTakZkaUN0b2ItZFVIaENoZXVBZGtoeU10TGpXeEU5SUV4eE13ckFTQ3hOOUVyeFFHOTkwNlRpQVNwMkpZNDhmQllMZ3Q2OUlKNnJVcFVJZDBfdnV2WGdYdzdHSDZYeW1WYlVseTdhXzM2TUUyMGtEMUp1UXI5UWZPNERJUnRJRXVaNFRmbVlqX3M?oc=5>

## RISKS

### Taiwan Semiconductor Manufacturing (NYSE:TSM) Pauses Advanced Chip Shipments To China
- Summary: TSMC halts advanced chip shipments to China, potentially impacting revenue and supply chain stability.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxNOGhIWnVaYlI5aFc1emtra29CdDBWS3J0dXVRTFZhQmdXNThUU2hUVXZBYWVLR2RpaHJEX1ZqNnJXTzQyWFJ4Q1BQN1dmeDlXVGxQTDZwTkNKbHlxWUFzT2VaZFFENXBwYjVyV2NCN1d2dVBmODA2MGVUdTk0UEJHcW9Mc2dJRHRTTUpJanI1dGR3dDMyNkVVM1QycU9iVzJ5VGVIUEpJWQ?oc=5>

### Tech rally sparks 14% rise in Taiwan Semiconductor Manufacturing (TSM:NYSE)
- Summary: TSM shares jump 14% amid broader tech rally, signaling bullish momentum.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxNRTRBZ2lSU1RSRkx2U2U5eDRld2g4V0dfZlY5QjFhX1JPeVlrM2g3WFIxMnhodldqNFlJZHN5VGNFWWRXX0ZyZVBLdDJVWkVseTNyc3hFYjFLR3dBOS1rVVlQaVdzSkxoMEh4NGJwQVNjdGJaV3lvbjd3aUFhVzFKNFBkd2VDdFl6bGhwSWxGb292WWEzQnkxU3dtOHhjQlJNS2xz?oc=5>

### TSMC’s Future Could Look Very Different by the End of 2028
- Summary: Uncertain future outlook through 2028.
- Date: 2026-11-23 | Impact: medium | Horizon: long | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPalZtS18yM1R4aE56S19JdUpUSVY3OUM4MHktcVdRTTVwNUpKSDh1NTEtNHJ0bXd6TXcxYU8td0t1OUpWMlhEV1NHV3FNNDZmc3MtaElDcm96anlOSF9PY3daMTlUSE02VFZ2T1k1Q3pqSExhVGczVlJkSTd1WmUxdjJiVlQtbHNVWkp1Q0dBOGN5Zy1EZU9kU3licmtTRXNmOHY4?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TSM** | **23.56** | **69.84** | **3.38** | **50.90** | **1,885,801,545,728.00 USD** | **33.59** |
| UMC | 13.58 | 2.48 | -0.30 | 25.60 | 36,087,156,736.00 USD | 102.25 |
| GFS | 111.29 | 1.82 | 10.44 | 12.50 | 21,712,629,760.00 USD | 15.05 |
| INTC | N/A | 2.76 | 17.24 | 20.90 | 317,092,888,576.00 USD | 72.93 |

Peers fetched as_of: 2026-11-23; TSM reuses existing data (market data as_of: 2026-11-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-23

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

- https://news.google.com/rss/articles/CBMingFBVV95cUxPQTdIdlg4WUU0cTJmTXphUVF0RkRTOXg3SXRabHRIYnpTNWg3aHIwRUV2eS02Z2JwX3ZKV2JYdVNCdDBoMzhicjJSR2dTOF8wLTE5OERyN05UMG53TUJFVkpCempwdXBtbmw3aWFQZXlHNm5qOHlGOEp4aXVGUmQtTUhYbG1aWDdma3dVaHd6dXAtSFUtY0praXFRSlB3Zw?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOMEdpVWJwSTh1cU9tb25IQWwwR3VjdlNfYWZUYXI5b3lrZzRTb3c3SHBqVy00endjamt2M3RvMFZLcGZRTmRLcTZTOE92ejJqM09vejF6Y29zRy02XzRQeGJ2a2ZKaTVDNE5DeU1YbjJUc3NOM3plT3NJOWZWZ1ZoTm9YZ0JZZkZGMXZwUkNxQ3NnSVhDWDVn?oc=5
- https://news.google.com/rss/articles/CBMiekFVX3lxTE92TkVUSlNHYU1SY3BsX3E1MWN3elI4c2hqQ0NONE5DOU5FVWl2cTZEVk1tb282dTE0TEJGU1RhRndzTTZhOU5rbXEyVVlRQzd2ckxua1dORnktSjljNG1KNnlrSVQtZEE2YUFxbDFoY0JRdXFRdnZ1UERn?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxQQzVDWHFBM0JfNG1lQ0NXZnZDRGpraS0wNWttbmFCbjlwTEVycEg4THhxZ3hjMFpIVW1tbXRhM3JjaWFLMGFPLWc2UlE4dkFfVGFIekdOMzUtaXpJTGg4QnhVWTVSRmZVM3hlWlA1V2VwUXlyUV9ScWxuUnNoV29vVl8wZWFwZFV5SHhpVl85RkhiZkxzSW1hTnotRlZPN3p1eHdyVk9CczMwc2J1ZW9FSTZWM1dkeVYzZzBaUUQxMmdzQ3dJcUF1YzVn?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxOVzYtSW9VcXlfZzBTc1gyWmpWSmRRTVdFcUlFQTNVcWp6ZFh2ZWFwUUJhM0Y1cXdrZ0RKRUFIbjE2ODNPclh3NDMyZGFDZ3prQ1NGbHVDY2RjYk1mSExWLWhZamc2Y3p0ZjZ0eDl2Q1lQelBnUGZkb0JEU2pMM0hTRkl2NDVUbDhlYlhkZDVvWUREWUpPWk9Cb2JteDI1cmVVVWtwa29kTkxNRTBXdVVwSDVXRDMtbHVlUmVkNThRWGo?oc=5
- https://news.google.com/rss/articles/CBMi6wFBVV95cUxNQkVybnpqUF9GVHpaWk1KbHliV0FLWm5VNEcxNFB3RVUtbFZKdDlvSDhSMTBxOGN1TFFRVXZGWXpoV3Fxc0p5ZmVIVW9yOENXUXNPSV9PRDdOUXM3T3d4YjloUmtVWXlVV3hMOXpmVWJ0aXRoQXBBSXlCcEMxYnZmUjBkMm1mWWluY2s4NmhsYWozSXRIVkFpLVpsZndUT3dyWVEyS1hQUGE2T0VVMmpuaTRqQ2RGX0dPMmV2QzFvX1VNb2tra0pTM2U0SENEd0FseUFwRlU1QzFNVmhlY1pMRzRZY3ZPTmFKQkZv?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxOT1Z3NGFEZVR5VndRZlV3TjhwYkd3YjN5dWJqbkpzR2N5VWd3aDlaNHRRVm9WN0lzcEw4NVpLRXhpYlUweFlpYnNiTVktcHE5NTZfU29BTzhMNFh0N294bTEwelowSEtaTndHOWFraHJDVkxfMk5BQVcwbnRhZG95SUpXMkFfNl9hOUE?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxPQVhxWWp0SU9TOVVGLWQ1azhrbXlnVng0QjBUNzhXS3J1Q1FSU3F4dG1ZYzlzaW0xa3I4M3FoNzVsazV4TTNCRHNOb3BNUHQxVjRRZ011a3licEdIZmdsLUdVVGVJdjZWdlp5X251Q1VhdnZETmFYa3BURGtjenZiX0dqZVZFUkREd29XNkNiM1RuR3l2Y1Q5VE9JRzZ3NEdDY1cxLWRQQlJtTFlzdjk2NzZicThkeFIydzduVjlWUXhKdXNRZkFXbHdUc2pyVnpaaTVMOWR1SQ?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxPRGhfT1h2VHNtYVlES2FYa3lSdm40WmcxQ3d3TGl2bG9xZG5KbHFYeHlqZ044TEFjUHNZZDBvVjZxc3ZxdGxKQ18wc1lXNjVXZzItMUt2Ym50X1lfWk84eXJneUpZYUtIVEdwZFN0SlBXbnpPUWdnNmxPUGVBRDI2amdTUDdOU1Naal9ocl9iSlQ2TkJkVl81ZGlnaTFpcWRFX05XZDl2VzVhcXE1?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxNcWNxU2w0LWRJc2M5YURjMDJpdlZmVHZkWW1ENlJlZmVjLTNsSEJuSHpBWlZqdjd0Z0dCYUlpRHRDVm1DX29IMFdSWGFWRkFFOF9jTjNXeEx0UjhVNWJEN3hEcExLNmZ0RVpBT3FZNi1Ia0ppRUNLYmZsLUFfbEkyNFFmTWxhcTJRVm1HT01Vb011Z0VIQ0NXSVRxeWtwaU1DUk1keDZPa1QtaTNnbVdVYXVwR2tURTNxU21GYWVBQ0F4a0N3?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxQcmdsWGEzU2FSSUFWRzlnQ0Q1a0hCX0M5OFVYenJJVHI2TzBLTHBXY2ZfVzduVzg2LTlYQlVKcWhOeE5Gc3F3Ql9RWmttbVlHUThzZGl3aUIyVTdOV2NoSElQbDFCT2tfbk43ZGJhWTU4WmtlZmlfMGdCcHRwYUNWejVUQ2RwalNpOTBCaTZublJDMFhCcnJ2MjY3UnIyMDdLS0tHNmRDUlZkYlJXRzNRS1JqNFpHLTAzN2FJX2xzcUtKSjg?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPUFFsQTg2cVZWZjh5R3RsUk1QbkdWTC1VazlPT25ONmVqZ3EyY3o2LU9Sa1BFN1VJZjRiOGF1bXJIZlNKYjYxX3lZdm5RTjE3aHRJUWMzcHg0UWJSYkxLaWJSTHo5VkllWGN1ZjRwX1NpWlhiOVBqNk9BdDFNWXNhRmU4UDZBQUtJckFHYlBPM3ZWOC1vNjVScVl0QUE2bG5RckpvT1E4Wm0xQQ?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxQVHZTakZkaUN0b2ItZFVIaENoZXVBZGtoeU10TGpXeEU5SUV4eE13ckFTQ3hOOUVyeFFHOTkwNlRpQVNwMkpZNDhmQllMZ3Q2OUlKNnJVcFVJZDBfdnV2WGdYdzdHSDZYeW1WYlVseTdhXzM2TUUyMGtEMUp1UXI5UWZPNERJUnRJRXVaNFRmbVlqX3M?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxNOGhIWnVaYlI5aFc1emtra29CdDBWS3J0dXVRTFZhQmdXNThUU2hUVXZBYWVLR2RpaHJEX1ZqNnJXTzQyWFJ4Q1BQN1dmeDlXVGxQTDZwTkNKbHlxWUFzT2VaZFFENXBwYjVyV2NCN1d2dVBmODA2MGVUdTk0UEJHcW9Mc2dJRHRTTUpJanI1dGR3dDMyNkVVM1QycU9iVzJ5VGVIUEpJWQ?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxNRTRBZ2lSU1RSRkx2U2U5eDRld2g4V0dfZlY5QjFhX1JPeVlrM2g3WFIxMnhodldqNFlJZHN5VGNFWWRXX0ZyZVBLdDJVWkVseTNyc3hFYjFLR3dBOS1rVVlQaVdzSkxoMEh4NGJwQVNjdGJaV3lvbjd3aUFhVzFKNFBkd2VDdFl6bGhwSWxGb292WWEzQnkxU3dtOHhjQlJNS2xz?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPalZtS18yM1R4aE56S19JdUpUSVY3OUM4MHktcVdRTTVwNUpKSDh1NTEtNHJ0bXd6TXcxYU8td0t1OUpWMlhEV1NHV3FNNDZmc3MtaElDcm96anlOSF9PY3daMTlUSE02VFZ2T1k1Q3pqSExhVGczVlJkSTd1WmUxdjJiVlQtbHNVWkp1Q0dBOGN5Zy1EZU9kU3licmtTRXNmOHY4?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
