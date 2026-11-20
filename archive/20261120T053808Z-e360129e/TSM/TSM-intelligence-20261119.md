# TSM Intelligence Report

- ticker: **TSM**
- Report as_of: **2026-11-19**
- Market data as_of: **2026-11-19**
- Quant sources: https://finance.yahoo.com/quote/TSM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TSM/key-statistics/
- AI analysis snapshot as_of: **2026-11-19**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-20T05:57:01.439169+00:00**
- AI status: **Partial: 2 headlines remain unclassified and excluded from research conclusions**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 3, 'ai': 10, 'unknown': 2, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **10** exact headline/source/date matches; prior report **20261119T054856Z-9eb86811/TSM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'negative_sentiment_in_tailwinds': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 14 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-11-13

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 352.0900 |
| Return 1D (%) | -2.9039 |
| Return 1W (%) | -13.1693 |
| Return 1M (%) | -16.2129 |
| Return YTD (%) | 16.7720 |
| Return 1Y (%) | 26.0107 |
| Annualized volatility (%) | 42.5069 |
| Beta vs SPY | 2.1918 |
| Max drawdown (%) | -27.5237 |
| Sharpe (rf=0) | 0.7589 |
| Downside deviation (rf=0, %) | 29.6630 |
| Sortino (rf=0) | 1.0875 |
| Historical VaR 95% (1D, %) | 4.2918 |
| Historical ES 95% (1D, %) | 5.9199 |
| Correlation vs SPY | 0.7167 |
| Tracking error vs SPY (%) | 33.9583 |
| P/E (trailing) | 22.82 |
| P/B | 67.63 |
| EV/EBITDA | 3.25 |
| Revenue growth (%) | 50.90 |
| Forward P/E (estimate) | 15.06 |
| Gross margin (%) | 65.85 |
| Operating margin (%) | 57.96 |
| Return on equity (%) | 41.86 |
| Free cash flow yield (%) | N/A |
| MA50 | 424.3727 |
| Close vs MA50 (%) | -17.0328 |
| MA200 | 402.2937 |
| Close vs MA200 (%) | -12.4794 |
| RSI (14, Wilder) | 34.4495 |
| MACD (12,26) | -17.0398 |
| MACD signal (9) | -13.4923 |
| MACD histogram | -3.5475 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TSM': 286, 'SPY': 286}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 352.0900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.9039 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -13.1693 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -16.2129 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 16.7720 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 26.0107 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 42.5069 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 29.6630 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.0875 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.2918 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.9199 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.7167 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 33.9583 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.1918 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.5237 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.7589 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.0560 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 65.8460 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 57.9610 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 41.8600 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 22.8185 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 34.4495 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.5475 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -17.0328 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -12.4794 -> Clearly below the moving-average trend level.

## TAILWINDS

### Taiwan Semiconductor Shares Jump 4.66% After Hours - Taiwan Semiconductor (NYSE:TSM), NVIDIA (NASDAQ:NVDA
- Summary: Taiwan Semiconductor Shares Jump 4.66% After Hours - Taiwan Semiconductor (NYSE:TSM), NVIDIA (NASDAQ:NVDA
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxPNFJtektvbGxSYVJkOWgtWWtxalpCR1p5VkVySWJHRFZ4UWNsRllyWVNVVWszOWtoXzJmZTFib2lPZHlfLTlsRW12Q3lfczNsYWRXU2pHMzJheUVKTXVsV09vbm8tV1pHdFNwYS0yMW5yX0J2N0xIVXprNTdIVlJldkM2UHlnS3VtWTRtb3F0Z0RKQWNKV2tMN2NrSnhTZ2hwa1hwc1U4VFBjSmZCSHF2bUo1cy1xRmt4Z3ZUWE9n?oc=5>

### The AI Chip Bubble Meets Reality: AMD, TSMC, Intel, Micron, Broadcom Tumble
- Summary: TSMC shares fell amid a broader downturn in the AI chip sector, reflecting market corrections and investor concerns.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxNQ2pDb3BaNWFQWjhYQnQwOFJTT3VUUndCUzhYVjNCUDZIYndlWHdKaTVGMzN0QjVFWUlVckpKUFhiZlhfM3dzY0RqYnJFaExDT3Foc2RGbkR0TjMwZXplbHVncmJ0ekZmaEFIYy1Ea3A5bmJpZEp2NjVHOUZwX1h6a1lHVWNYUVR0XzRhdmJWdHNDMWgtU2tCZFlqT3h6aGltbmNfcUpSb1c4blhqcmh5WW05bw?oc=5>

### Taiwan Semiconductor Manufacturing (NYSE:TSM) Hit A Revenue High, Is The Stock Fully Valued?
- Summary: TSM reported a revenue high, indicating strong financial performance.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNdFZMVDR0eERfMHJrVHExSVR2VjhvaXMyNnN1YTBPY1FrLUxWVWtrRmMzTDMtN0RPUlB4RGI4dW9uODFLRVNRWmh4Vk4zZ3dLSmFSTVZHaEJsbjVOQk1jUHFyeEFUeXRjMm5VY2J4UWlRZXVWWnNWcGZwajNrVDlqWmNEMHVJQW5Tb2ZMQjNIUDREZ0M1NE13?oc=5>

### Surging AI Demand and Advanced Chipmaking Strengthens Taiwan Semiconductor Manufacturing Company Limited (TSM) Growth Outlook
- Summary: AI demand and advanced chipmaking boost TSMC’s growth outlook.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPc2hWWjNRTC1WNlBrNGRnN19wdlRTMVZaMHJmTmdxRm5xTlBUdEpZX0ZMc29adFJKcGdrSEo3Q192X0FtWGxjaXZYOG9hR0VaX2RGZ25GVGhlREZxR1ozV1pCZ3ZPbTlVeG9WWXJCc0x2T1gtdUJHR0xQUzZPa1dMOXhjZEJETzhNQldveFFPUmQtNmU2T3JXWXRUdDAwWXhUa0lj?oc=5>

### Taiwan Semiconductor Stock (TSM) Looks Too Cheap for Its Growth Outlook
- Summary: Analyst view that TSMC is undervalued, suggesting potential upside.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxNdkVJOTVfM1d3SVNMRWI3V0FXU1lEam1PNXZ5Vzhwdk1rUWI0TDhmazdFdEV2Nkdaa3RnQjdXQjBQaXlZSngtTy05NHdlWnFEel95M3BLWmk3QjFyYUMtNnRoZ2pyVnJUbExFalBWdm1MaGJHTXBRc3Z0cnRoQVhMdGd0SWFuR1AtTzhXTll1MF9HX2dzY054N0E3N3pSckVISUhQT1dhT2lkVTg?oc=5>

### Ken Fisher’s Quiet Bet on TSMC (TSM): Owning the AI Boom Without Picking a Winner
- Summary: Analyst bullish stance on TSMC benefiting from AI demand.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMif0FVX3lxTFBxRnNta0JjZS1NN2hzWXNPRnFFbUh0Qm0wYmx6SGItX0hISHVRMWpXTV90TVpPME5WZVRKNVF5aDUzcmpCbEdldm12N1lIUzBoYV92bS1WUWlydmVMSVhJV3JtTWw4eFVNcDAtM0I4ZlBuTE9ubHh1YzQ0NDhBbzg?oc=5>

## HEADWINDS

### Taiwan Semiconductor Manufacturing (NYSE:TSM) Shares Tumble As Customer Shock Clouds AI Outlook
- Summary: Taiwan Semiconductor Manufacturing (NYSE:TSM) Shares Tumble As Customer Shock Clouds AI Outlook
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxPRGhfT1h2VHNtYVlES2FYa3lSdm40WmcxQ3d3TGl2bG9xZG5KbHFYeHlqZ044TEFjUHNZZDBvVjZxc3ZxdGxKQ18wc1lXNjVXZzItMUt2Ym50X1lfWk84eXJneUpZYUtIVEdwZFN0SlBXbnpPUWdnNmxPUGVBRDI2amdTUDdOU1Naal9ocl9iSlQ2TkJkVl81ZGlnaTFpcWRFX05XZDl2VzVhcXE1?oc=5>

### Is TSM Still a Buy as AI Growth Faces Heavy Spending and Valuation?
- Summary: Analyst questions TSM's valuation amid high AI spending, indicating potential downside.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxPSWM2MHNEREw5SUdxcWtzVGRYY09kUTQ1YzMwZE5WdGRaQ3VCVVd6eDBkNHZyUlIycTBUZWlyeHI2eE9oM2NBQTkzMTg0cU9XR0FtSkw0Q3FYT205cDVkeUw3eDA5NFdVbUN4ZGRQM1JPaHRTSDAwVW9CNVZ6dXJNbTAzZm9YZUVFYlV4WXZfLUFIZw?oc=5>

### Taiwan Semiconductor Manufacturing Company Limited (TSM) Pulled Back Amid Broader AI Buildout Correction
- Summary: TSM shares pulled back amid broader AI market correction.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOdjNPOHgzT3pYVEo3cHNwU21pVGxUT1lYcTZiRkFid1lqTUxibFRtbXBNTVAzSGc0eWVDN2xaeFFxaFVFLWlYMmlfbkM1bzZja18yZUR2MFJjZ3BEYU42T1pUcHhGYlFrVDJhTExiWndnRjIxemJhMUR6ZkRMRDJGYU5UZnVSdnZLTjNRSWxyaU12V2FITGplY2VSOEtvTGRH?oc=5>

### Here’s What Weighed on Taiwan Semiconductor Manufacturing Company Limited (TSM) in Q3
- Summary: Review of factors impacting TSM in Q3, highlighting challenges and opportunities.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxQckttYWtjRDVYQW9sRlNvUk9iTjVrejk4Z1dsaTJwVWV5dWNvb0RUWFhzSFlSVnpRenZkM2g4aVdLZGc5bUhKb2lVTWYzQTBiWE5lQ0FROXNIXzM4Z1dLMURzejFIaEJ2a0VUeGR4aDBmRWtVb3prQTdXcDFxa2NIUUlBMWpRZERzQ2hmR2ZGQVlYNjcwVS1pNG43cTY3dndjY3lVZVVuTUV5TmFrY01sSzg5dmU2QQ?oc=5>

## CATALYSTS

### TSMC, Samsung Reportedly Suspend Some Chip Deliveries To Chinese Customers Amid New US Export Rules
- Summary: TSMC, Samsung Reportedly Suspend Some Chip Deliveries To Chinese Customers Amid New US Export Rules
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi8AFBVV95cUxPNW5IYW5ubWZhdEw3S09KeC1xWUZKZzlmMW9ORFR6R01hY2p1MlpmZHpleVRKN3hwcmRQTWJicFhDYkJ5OC1IX1pBSDZfVDNETHB2Z1BaUUV5QVZhaFF1RXF3NGdLZ3JZcHVLeTIyMnFQb3hud2tlT2RoMU9uMlEyOEVpbW5jOE9xQnBYYnVnYVRpLVlESk03TTczN3JMYjU0SjJUU1pxQ2tYVTIzUHJBWU9VTEVEVzVwY3RGTkZUcmRGWVhGUUlPTEpNTlYyUEZnRjhWdXVDU2xJenE1dFNtVlZxc2RfWGctYnc2VUZndV8?oc=5>

### Taiwan Semiconductor Manufacturing (TSM) Takes A $1 Billion Step Further Into AI
- Summary: TSM invests $1B to expand AI chip production, enhancing its product portfolio and market position.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxORVdVMmRDVnBVTWo0N1lvQzh1U05OUnZveUs1Q08wLWFOVHQ2d3dPb3hRNVcyVFJ0TFQ2dWFKX1NZcDR4UTA3QXk3SXo4WkVyQXYycjVGVGNVVGlEZWtJSnBsY2N4X3dCM1pTaHZzcE5xOW8zMl8xak1tUjhzZUtRZWg3a1VaeDRXWFlYaUc1MmV1OXNpQ2ZjYkZXU1VxWmZpZW9IQzVLZy11RGFB?oc=5>

## RISKS

### TSMC reportedly demands cash up front from AI chip clients amid circular financing fears
- Summary: TSMC is requiring upfront cash from AI chip customers, raising concerns about circular financing and potential liquidity issues for clients.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxORXlCNFRCMWNyakhjQXplMl9uNk1CT0FBTUNQcVE1aFRxMy1iM3FfZGZidDFMOVZUVzZOMVJZU3lpX0I4SVllcFo3RnJDczlOV2VpcndfdTladFlzWFM2REh3Z2hKV0Z1am9udWp1eUl3Zl9UWmN3STBQRkt4aEpuaGtsTEZKdGtLT3dzdnUwbFZNT2liRDJ6QXJSVURoQmxsMkV2TC1nTUt0d0tveVFTaGtmajgtTHBMWHFsTg?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TSM** | **22.82** | **67.63** | **3.25** | **50.90** | **1,826,105,196,544.00 USD** | **26.01** |
| UMC | 12.64 | 2.31 | -0.32 | 25.60 | 33,604,438,016.00 USD | 88.60 |
| GFS | 111.26 | 1.82 | 10.44 | 12.50 | 21,707,055,104.00 USD | 21.73 |
| INTC | N/A | 2.57 | 16.14 | 20.90 | 296,151,810,048.00 USD | 58.70 |

Peers fetched as_of: 2026-11-19; TSM reuses existing data (market data as_of: 2026-11-19); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-19

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

- https://news.google.com/rss/articles/CBMivgFBVV95cUxPNFJtektvbGxSYVJkOWgtWWtxalpCR1p5VkVySWJHRFZ4UWNsRllyWVNVVWszOWtoXzJmZTFib2lPZHlfLTlsRW12Q3lfczNsYWRXU2pHMzJheUVKTXVsV09vbm8tV1pHdFNwYS0yMW5yX0J2N0xIVXprNTdIVlJldkM2UHlnS3VtWTRtb3F0Z0RKQWNKV2tMN2NrSnhTZ2hwa1hwc1U4VFBjSmZCSHF2bUo1cy1xRmt4Z3ZUWE9n?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxNQ2pDb3BaNWFQWjhYQnQwOFJTT3VUUndCUzhYVjNCUDZIYndlWHdKaTVGMzN0QjVFWUlVckpKUFhiZlhfM3dzY0RqYnJFaExDT3Foc2RGbkR0TjMwZXplbHVncmJ0ekZmaEFIYy1Ea3A5bmJpZEp2NjVHOUZwX1h6a1lHVWNYUVR0XzRhdmJWdHNDMWgtU2tCZFlqT3h6aGltbmNfcUpSb1c4blhqcmh5WW05bw?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNdFZMVDR0eERfMHJrVHExSVR2VjhvaXMyNnN1YTBPY1FrLUxWVWtrRmMzTDMtN0RPUlB4RGI4dW9uODFLRVNRWmh4Vk4zZ3dLSmFSTVZHaEJsbjVOQk1jUHFyeEFUeXRjMm5VY2J4UWlRZXVWWnNWcGZwajNrVDlqWmNEMHVJQW5Tb2ZMQjNIUDREZ0M1NE13?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPc2hWWjNRTC1WNlBrNGRnN19wdlRTMVZaMHJmTmdxRm5xTlBUdEpZX0ZMc29adFJKcGdrSEo3Q192X0FtWGxjaXZYOG9hR0VaX2RGZ25GVGhlREZxR1ozV1pCZ3ZPbTlVeG9WWXJCc0x2T1gtdUJHR0xQUzZPa1dMOXhjZEJETzhNQldveFFPUmQtNmU2T3JXWXRUdDAwWXhUa0lj?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxNdkVJOTVfM1d3SVNMRWI3V0FXU1lEam1PNXZ5Vzhwdk1rUWI0TDhmazdFdEV2Nkdaa3RnQjdXQjBQaXlZSngtTy05NHdlWnFEel95M3BLWmk3QjFyYUMtNnRoZ2pyVnJUbExFalBWdm1MaGJHTXBRc3Z0cnRoQVhMdGd0SWFuR1AtTzhXTll1MF9HX2dzY054N0E3N3pSckVISUhQT1dhT2lkVTg?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPSHZ4N0lvQl9kcTU2ZlRNbUdrQkl5bUR6Y3Q2YkxMZXFDWWUyeE9rMWhkWEdRUkd3clA5MjE0aGFkZFAzRnNLVFE5SThEeWJYUWZudEd3SGh5SFFwdDF4Qk9HZWw0dTRzYWoyQmxvc3psN3dWRW4wQ2c2Ml9kbkQ1cEhJaDBidUh1VDN5T3hIRXIyTmZ6TThDVW1LR0pEZ1FoTEVZ?oc=5
- https://news.google.com/rss/articles/CBMif0FVX3lxTFBxRnNta0JjZS1NN2hzWXNPRnFFbUh0Qm0wYmx6SGItX0hISHVRMWpXTV90TVpPME5WZVRKNVF5aDUzcmpCbEdldm12N1lIUzBoYV92bS1WUWlydmVMSVhJV3JtTWw4eFVNcDAtM0I4ZlBuTE9ubHh1YzQ0NDhBbzg?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxPRGhfT1h2VHNtYVlES2FYa3lSdm40WmcxQ3d3TGl2bG9xZG5KbHFYeHlqZ044TEFjUHNZZDBvVjZxc3ZxdGxKQ18wc1lXNjVXZzItMUt2Ym50X1lfWk84eXJneUpZYUtIVEdwZFN0SlBXbnpPUWdnNmxPUGVBRDI2amdTUDdOU1Naal9ocl9iSlQ2TkJkVl81ZGlnaTFpcWRFX05XZDl2VzVhcXE1?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxPSWM2MHNEREw5SUdxcWtzVGRYY09kUTQ1YzMwZE5WdGRaQ3VCVVd6eDBkNHZyUlIycTBUZWlyeHI2eE9oM2NBQTkzMTg0cU9XR0FtSkw0Q3FYT205cDVkeUw3eDA5NFdVbUN4ZGRQM1JPaHRTSDAwVW9CNVZ6dXJNbTAzZm9YZUVFYlV4WXZfLUFIZw?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOdjNPOHgzT3pYVEo3cHNwU21pVGxUT1lYcTZiRkFid1lqTUxibFRtbXBNTVAzSGc0eWVDN2xaeFFxaFVFLWlYMmlfbkM1bzZja18yZUR2MFJjZ3BEYU42T1pUcHhGYlFrVDJhTExiWndnRjIxemJhMUR6ZkRMRDJGYU5UZnVSdnZLTjNRSWxyaU12V2FITGplY2VSOEtvTGRH?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxQckttYWtjRDVYQW9sRlNvUk9iTjVrejk4Z1dsaTJwVWV5dWNvb0RUWFhzSFlSVnpRenZkM2g4aVdLZGc5bUhKb2lVTWYzQTBiWE5lQ0FROXNIXzM4Z1dLMURzejFIaEJ2a0VUeGR4aDBmRWtVb3prQTdXcDFxa2NIUUlBMWpRZERzQ2hmR2ZGQVlYNjcwVS1pNG43cTY3dndjY3lVZVVuTUV5TmFrY01sSzg5dmU2QQ?oc=5
- https://news.google.com/rss/articles/CBMi8AFBVV95cUxPNW5IYW5ubWZhdEw3S09KeC1xWUZKZzlmMW9ORFR6R01hY2p1MlpmZHpleVRKN3hwcmRQTWJicFhDYkJ5OC1IX1pBSDZfVDNETHB2Z1BaUUV5QVZhaFF1RXF3NGdLZ3JZcHVLeTIyMnFQb3hud2tlT2RoMU9uMlEyOEVpbW5jOE9xQnBYYnVnYVRpLVlESk03TTczN3JMYjU0SjJUU1pxQ2tYVTIzUHJBWU9VTEVEVzVwY3RGTkZUcmRGWVhGUUlPTEpNTlYyUEZnRjhWdXVDU2xJenE1dFNtVlZxc2RfWGctYnc2VUZndV8?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxORVdVMmRDVnBVTWo0N1lvQzh1U05OUnZveUs1Q08wLWFOVHQ2d3dPb3hRNVcyVFJ0TFQ2dWFKX1NZcDR4UTA3QXk3SXo4WkVyQXYycjVGVGNVVGlEZWtJSnBsY2N4X3dCM1pTaHZzcE5xOW8zMl8xak1tUjhzZUtRZWg3a1VaeDRXWFlYaUc1MmV1OXNpQ2ZjYkZXU1VxWmZpZW9IQzVLZy11RGFB?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxORXlCNFRCMWNyakhjQXplMl9uNk1CT0FBTUNQcVE1aFRxMy1iM3FfZGZidDFMOVZUVzZOMVJZU3lpX0I4SVllcFo3RnJDczlOV2VpcndfdTladFlzWFM2REh3Z2hKV0Z1am9udWp1eUl3Zl9UWmN3STBQRkt4aEpuaGtsTEZKdGtLT3dzdnUwbFZNT2liRDJ6QXJSVURoQmxsMkV2TC1nTUt0d0tveVFTaGtmajgtTHBMWHFsTg?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
