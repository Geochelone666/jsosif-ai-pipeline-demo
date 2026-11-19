# TSM Intelligence Report

- ticker: **TSM**
- Report as_of: **2026-11-18**
- Market data as_of: **2026-11-18**
- Quant sources: https://finance.yahoo.com/quote/TSM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TSM/key-statistics/
- AI analysis snapshot as_of: **2026-11-18**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-19T05:50:19.243925+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 2, 'ai': 12, 'unknown': 0, 'irrelevant': 10})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261118T054934Z-e0d070d9/TSM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'negative_sentiment_in_tailwinds': 1, 'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 13 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 29.17%; oldest publication 2026-11-16

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 362.6200 |
| Return 1D (%) | 0.8146 |
| Return 1W (%) | -12.2729 |
| Return 1M (%) | -12.1156 |
| Return YTD (%) | 20.2643 |
| Return 1Y (%) | 31.8621 |
| Annualized volatility (%) | 42.4227 |
| Beta vs SPY | 2.2076 |
| Max drawdown (%) | -27.3158 |
| Sharpe (rf=0) | 0.8671 |
| Downside deviation (rf=0, %) | 29.5199 |
| Sortino (rf=0) | 1.2461 |
| Historical VaR 95% (1D, %) | 4.2918 |
| Historical ES 95% (1D, %) | 5.9199 |
| Correlation vs SPY | 0.7159 |
| Tracking error vs SPY (%) | 33.9612 |
| P/E (trailing) | 23.50 |
| P/B | 69.65 |
| EV/EBITDA | 3.37 |
| Revenue growth (%) | 50.90 |
| Forward P/E (estimate) | 15.51 |
| Gross margin (%) | 65.85 |
| Operating margin (%) | 57.96 |
| Return on equity (%) | 41.86 |
| Free cash flow yield (%) | N/A |
| MA50 | 425.8686 |
| Close vs MA50 (%) | -14.8517 |
| MA200 | 402.1493 |
| Close vs MA200 (%) | -9.8295 |
| RSI (14, Wilder) | 36.8055 |
| MACD (12,26) | -15.3880 |
| MACD signal (9) | -12.6054 |
| MACD histogram | -2.7825 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TSM': 285, 'SPY': 285}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 362.6200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.8146 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -12.2729 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -12.1156 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 20.2643 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 31.8621 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 42.4227 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 29.5199 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.2461 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.2918 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.9199 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.7159 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 33.9612 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.2076 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.3158 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.8671 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.5063 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 65.8460 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 57.9610 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 41.8600 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 23.5010 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 36.8055 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -2.7825 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -14.8517 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -9.8295 -> Clearly below the moving-average trend level.

## TAILWINDS

### Taiwan Semiconductor Shares Jump 4.66% After Hours - Taiwan Semiconductor (NYSE:TSM), NVIDIA (NASDAQ:NVDA
- Summary: Taiwan Semiconductor Shares Jump 4.66% After Hours - Taiwan Semiconductor (NYSE:TSM), NVIDIA (NASDAQ:NVDA
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxPNFJtektvbGxSYVJkOWgtWWtxalpCR1p5VkVySWJHRFZ4UWNsRllyWVNVVWszOWtoXzJmZTFib2lPZHlfLTlsRW12Q3lfczNsYWRXU2pHMzJheUVKTXVsV09vbm8tV1pHdFNwYS0yMW5yX0J2N0xIVXprNTdIVlJldkM2UHlnS3VtWTRtb3F0Z0RKQWNKV2tMN2NrSnhTZ2hwa1hwc1U4VFBjSmZCSHF2bUo1cy1xRmt4Z3ZUWE9n?oc=5>

### Surging AI Demand and Advanced Chipmaking Strengthens Taiwan Semiconductor Manufacturing Company Limited (TSM) Growth Outlook
- Summary: AI demand and advanced chipmaking boost TSMC’s growth outlook.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPc2hWWjNRTC1WNlBrNGRnN19wdlRTMVZaMHJmTmdxRm5xTlBUdEpZX0ZMc29adFJKcGdrSEo3Q192X0FtWGxjaXZYOG9hR0VaX2RGZ25GVGhlREZxR1ozV1pCZ3ZPbTlVeG9WWXJCc0x2T1gtdUJHR0xQUzZPa1dMOXhjZEJETzhNQldveFFPUmQtNmU2T3JXWXRUdDAwWXhUa0lj?oc=5>

### Taiwan Semiconductor Manufacturing (NYSE:TSM) Hit A Revenue High, Is The Stock Fully Valued?
- Summary: TSM reported a revenue high, indicating strong financial performance.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNdFZMVDR0eERfMHJrVHExSVR2VjhvaXMyNnN1YTBPY1FrLUxWVWtrRmMzTDMtN0RPUlB4RGI4dW9uODFLRVNRWmh4Vk4zZ3dLSmFSTVZHaEJsbjVOQk1jUHFyeEFUeXRjMm5VY2J4UWlRZXVWWnNWcGZwajNrVDlqWmNEMHVJQW5Tb2ZMQjNIUDREZ0M1NE13?oc=5>

### The AI Chip Bubble Meets Reality: AMD, TSMC, Intel, Micron, Broadcom Tumble
- Summary: TSMC shares fell amid a broader downturn in the AI chip sector, reflecting market corrections and investor concerns.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxNQ2pDb3BaNWFQWjhYQnQwOFJTT3VUUndCUzhYVjNCUDZIYndlWHdKaTVGMzN0QjVFWUlVckpKUFhiZlhfM3dzY0RqYnJFaExDT3Foc2RGbkR0TjMwZXplbHVncmJ0ekZmaEFIYy1Ea3A5bmJpZEp2NjVHOUZwX1h6a1lHVWNYUVR0XzRhdmJWdHNDMWgtU2tCZFlqT3h6aGltbmNfcUpSb1c4blhqcmh5WW05bw?oc=5>

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

## CATALYSTS

### 3G Capital starts position Nu, adds to Taiwan Semiconductor, cuts stake in Intel among Q3 moves
- Summary: 3G Capital increases its stake in TSM, signaling confidence in the company’s growth prospects.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxNYkNNTGNqZzBPcjlCRUpyTVZSM1NYdEl3UGR5OGlaM1ZRUTBCQXZ0RGdvOXNOc3M2XzVZdjJ1UEIzTnYwWDJNdFl4OHpoenkwVVcyQXlRRk1WZnctM3RXZUZucFgwN05vbVotMXFkR0JpS2MyUzN5Ty1GWTlhdmlkajVSV2dHNUxkR2VhNVRjVnYxbmJlZDZUMnJHOUVoZWRkbDJkNHJqaTJmRXlCbDQ0U2VWd1V6VlFlR05nRmR6c1pOQU9iVEdGTzlhdjBfWnU5SFg1ZGcwSm1MOHVMUDVqVk80dDZ3UUlsMzF4cg?oc=5>

### Nvidia Stock Shock Has Investors Looking At TSMC And AI Chip Tooling
- Summary: Nvidia's stock shock drives investor focus to TSMC's AI tooling, potentially boosting demand.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxPYlRMMDd2bUVuYUdUMWIzRGlaUkRWQXZlYlVWejJ6Skdnclc3RkVsYkhxblQtNGx1bXdRLVAxNENXLWlyNEdWR2JEMGljcENZb2RkNnI1M01xUEFsMUF2d05jNENQYmhuOWdLYjAzMjJ6Z1Ffb1Y0X3FqUGhzalhQOHM1MVRwNnk0dUtyRlNzcDVRY2ZMLWJjZmtNejFOZGxTLUE?oc=5>

### NVIDIA's Leadership Woes: Buy TSMC & ASML Despite Supply-Chain Risks?
- Summary: Analyst recommends buying TSMC shares despite supply-chain risks, citing potential upside from NVIDIA's leadership challenges.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4gFBVV95cUxNS0lLM0JsX0hJUzFjNzFQcVNEeUJqYzNnTl9DT2hjU256dm14Qk9RWGdlWk9LdTBJcE1pUmp1OUQxZEtKZmhFd1Fqd2djaUxvcnd6ZmcycmFtMjZsU2N1Z2xzdVRYb1RDVTFvcXpKRzJTdzBCMVJpOWNYejVLblFaWGxucHprZ3owRkc4RmM0TzBRUW00VDludG82LW1uQTBjWDlmd0pNVlFVX0V2ZG9QNk1UeG96SUVIMGdzN1Rkd1ljMlFCMkJkN2ZCcEgtX3RGWW5RMEptUHNtV3EtOE5PQjFR?oc=5>

### TSMC Is Reportedly Setting Credit Limits for AI Customers
- Summary: TSMC may limit credit for AI clients, potentially tightening sales terms and affecting revenue streams.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPYjlVak5WVjlfMV9PdG5rb1ZWZGxFcTBUY0NNTXFyYThnb013Ui1NSk9OWGlNSkNKNVc4T2RpbXl5Q2toZjBfeVVzWC11Y043SGdBeWhKZnQ5TnBoYjVoMUVNSDJLZHN3NVRwaUtWV1pVcGdpRzZrOEpaY3RNM1hkaU1ZQ2lkazBETzc3SkJkUnFTakt0T2Y3RGNpZEFIbHdLQW1B?oc=5>

## RISKS

### Why is Taiwan Semiconductor Manufacturing stock tumbling today?
- Summary: TSM stock is experiencing a sharp decline today.
- Date: 2026-11-16 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxQQjdLMF9mOWJpSXhRa3BhSlAzcEs3V1FSTFhMWGZzQ2hsNnBwZ0VWMDZfRVBHNVZ1M3Njak1QUlh2TkxKLVpCVmcwLVNKbk9WOHczbVVqZS12bmJHeENMb2E0c0MxS0VLOV9WVS1QcE5ZZHZ0Zk1MeWh5NFVQbGFRQkdET0thY3JMRTM0b0hPb1FhWVpUZGxid2V2Njg1YnF6dEtZc0ljbzdYM0FlMUJWeGtfRnFrcTNESHZ0aWR5NWZ5UQ?oc=5>

### TSMC reportedly demands cash up front from AI chip clients amid circular financing fears
- Summary: TSMC is requiring upfront cash from AI chip customers, raising concerns about circular financing and potential liquidity issues for clients.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxORXlCNFRCMWNyakhjQXplMl9uNk1CT0FBTUNQcVE1aFRxMy1iM3FfZGZidDFMOVZUVzZOMVJZU3lpX0I4SVllcFo3RnJDczlOV2VpcndfdTladFlzWFM2REh3Z2hKV0Z1am9udWp1eUl3Zl9UWmN3STBQRkt4aEpuaGtsTEZKdGtLT3dzdnUwbFZNT2liRDJ6QXJSVURoQmxsMkV2TC1nTUt0d0tveVFTaGtmajgtTHBMWHFsTg?oc=5>

### Taiwan Semiconductor Booked a Record NT$587 Billion Month. The Stock Has Lost Nearly 10% in Three Days Anyway
- Summary: Despite record monthly revenue, TSM's stock fell 10% in three days, indicating market skepticism or external pressures.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxOaHExV3laWFhjQ1o4WFdDUWttdkxGckxUVkVtemV5dFcyYm5BMWNQbUJuR2Ezb2QxcVY4YmNLajBVbzhEX3lwMWRYUU5uQjdSdVJFM0stMjdWV3ZlWlFGZmNwZTZ4M3hBaWFXNXNPVE1sbE8yT0t6QTJCUTFMNU1ralNybjkzaU5KcUlCYUFFbHVLRG5MYjdQVU5PeVY5RFRheWlKVg?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TSM** | **23.50** | **69.65** | **3.37** | **50.90** | **1,880,718,835,712.00 USD** | **31.86** |
| UMC | 13.17 | 2.41 | -0.31 | 25.60 | 35,008,802,816.00 USD | 101.21 |
| GFS | 113.80 | 1.86 | 10.68 | 12.50 | 22,203,185,152.00 USD | 21.73 |
| INTC | N/A | 2.53 | 15.85 | 20.90 | 290,571,026,432.00 USD | 59.25 |

Peers fetched as_of: 2026-11-18; TSM reuses existing data (market data as_of: 2026-11-18); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-18

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
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPc2hWWjNRTC1WNlBrNGRnN19wdlRTMVZaMHJmTmdxRm5xTlBUdEpZX0ZMc29adFJKcGdrSEo3Q192X0FtWGxjaXZYOG9hR0VaX2RGZ25GVGhlREZxR1ozV1pCZ3ZPbTlVeG9WWXJCc0x2T1gtdUJHR0xQUzZPa1dMOXhjZEJETzhNQldveFFPUmQtNmU2T3JXWXRUdDAwWXhUa0lj?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNdFZMVDR0eERfMHJrVHExSVR2VjhvaXMyNnN1YTBPY1FrLUxWVWtrRmMzTDMtN0RPUlB4RGI4dW9uODFLRVNRWmh4Vk4zZ3dLSmFSTVZHaEJsbjVOQk1jUHFyeEFUeXRjMm5VY2J4UWlRZXVWWnNWcGZwajNrVDlqWmNEMHVJQW5Tb2ZMQjNIUDREZ0M1NE13?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxNQ2pDb3BaNWFQWjhYQnQwOFJTT3VUUndCUzhYVjNCUDZIYndlWHdKaTVGMzN0QjVFWUlVckpKUFhiZlhfM3dzY0RqYnJFaExDT3Foc2RGbkR0TjMwZXplbHVncmJ0ekZmaEFIYy1Ea3A5bmJpZEp2NjVHOUZwX1h6a1lHVWNYUVR0XzRhdmJWdHNDMWgtU2tCZFlqT3h6aGltbmNfcUpSb1c4blhqcmh5WW05bw?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxPRGhfT1h2VHNtYVlES2FYa3lSdm40WmcxQ3d3TGl2bG9xZG5KbHFYeHlqZ044TEFjUHNZZDBvVjZxc3ZxdGxKQ18wc1lXNjVXZzItMUt2Ym50X1lfWk84eXJneUpZYUtIVEdwZFN0SlBXbnpPUWdnNmxPUGVBRDI2amdTUDdOU1Naal9ocl9iSlQ2TkJkVl81ZGlnaTFpcWRFX05XZDl2VzVhcXE1?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxPSWM2MHNEREw5SUdxcWtzVGRYY09kUTQ1YzMwZE5WdGRaQ3VCVVd6eDBkNHZyUlIycTBUZWlyeHI2eE9oM2NBQTkzMTg0cU9XR0FtSkw0Q3FYT205cDVkeUw3eDA5NFdVbUN4ZGRQM1JPaHRTSDAwVW9CNVZ6dXJNbTAzZm9YZUVFYlV4WXZfLUFIZw?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOdjNPOHgzT3pYVEo3cHNwU21pVGxUT1lYcTZiRkFid1lqTUxibFRtbXBNTVAzSGc0eWVDN2xaeFFxaFVFLWlYMmlfbkM1bzZja18yZUR2MFJjZ3BEYU42T1pUcHhGYlFrVDJhTExiWndnRjIxemJhMUR6ZkRMRDJGYU5UZnVSdnZLTjNRSWxyaU12V2FITGplY2VSOEtvTGRH?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxNYkNNTGNqZzBPcjlCRUpyTVZSM1NYdEl3UGR5OGlaM1ZRUTBCQXZ0RGdvOXNOc3M2XzVZdjJ1UEIzTnYwWDJNdFl4OHpoenkwVVcyQXlRRk1WZnctM3RXZUZucFgwN05vbVotMXFkR0JpS2MyUzN5Ty1GWTlhdmlkajVSV2dHNUxkR2VhNVRjVnYxbmJlZDZUMnJHOUVoZWRkbDJkNHJqaTJmRXlCbDQ0U2VWd1V6VlFlR05nRmR6c1pOQU9iVEdGTzlhdjBfWnU5SFg1ZGcwSm1MOHVMUDVqVk80dDZ3UUlsMzF4cg?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxPYlRMMDd2bUVuYUdUMWIzRGlaUkRWQXZlYlVWejJ6Skdnclc3RkVsYkhxblQtNGx1bXdRLVAxNENXLWlyNEdWR2JEMGljcENZb2RkNnI1M01xUEFsMUF2d05jNENQYmhuOWdLYjAzMjJ6Z1Ffb1Y0X3FqUGhzalhQOHM1MVRwNnk0dUtyRlNzcDVRY2ZMLWJjZmtNejFOZGxTLUE?oc=5
- https://news.google.com/rss/articles/CBMi4gFBVV95cUxNS0lLM0JsX0hJUzFjNzFQcVNEeUJqYzNnTl9DT2hjU256dm14Qk9RWGdlWk9LdTBJcE1pUmp1OUQxZEtKZmhFd1Fqd2djaUxvcnd6ZmcycmFtMjZsU2N1Z2xzdVRYb1RDVTFvcXpKRzJTdzBCMVJpOWNYejVLblFaWGxucHprZ3owRkc4RmM0TzBRUW00VDludG82LW1uQTBjWDlmd0pNVlFVX0V2ZG9QNk1UeG96SUVIMGdzN1Rkd1ljMlFCMkJkN2ZCcEgtX3RGWW5RMEptUHNtV3EtOE5PQjFR?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPYjlVak5WVjlfMV9PdG5rb1ZWZGxFcTBUY0NNTXFyYThnb013Ui1NSk9OWGlNSkNKNVc4T2RpbXl5Q2toZjBfeVVzWC11Y043SGdBeWhKZnQ5TnBoYjVoMUVNSDJLZHN3NVRwaUtWV1pVcGdpRzZrOEpaY3RNM1hkaU1ZQ2lkazBETzc3SkJkUnFTakt0T2Y3RGNpZEFIbHdLQW1B?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxQQjdLMF9mOWJpSXhRa3BhSlAzcEs3V1FSTFhMWGZzQ2hsNnBwZ0VWMDZfRVBHNVZ1M3Njak1QUlh2TkxKLVpCVmcwLVNKbk9WOHczbVVqZS12bmJHeENMb2E0c0MxS0VLOV9WVS1QcE5ZZHZ0Zk1MeWh5NFVQbGFRQkdET0thY3JMRTM0b0hPb1FhWVpUZGxid2V2Njg1YnF6dEtZc0ljbzdYM0FlMUJWeGtfRnFrcTNESHZ0aWR5NWZ5UQ?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxORXlCNFRCMWNyakhjQXplMl9uNk1CT0FBTUNQcVE1aFRxMy1iM3FfZGZidDFMOVZUVzZOMVJZU3lpX0I4SVllcFo3RnJDczlOV2VpcndfdTladFlzWFM2REh3Z2hKV0Z1am9udWp1eUl3Zl9UWmN3STBQRkt4aEpuaGtsTEZKdGtLT3dzdnUwbFZNT2liRDJ6QXJSVURoQmxsMkV2TC1nTUt0d0tveVFTaGtmajgtTHBMWHFsTg?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxOaHExV3laWFhjQ1o4WFdDUWttdkxGckxUVkVtemV5dFcyYm5BMWNQbUJuR2Ezb2QxcVY4YmNLajBVbzhEX3lwMWRYUU5uQjdSdVJFM0stMjdWV3ZlWlFGZmNwZTZ4M3hBaWFXNXNPVE1sbE8yT0t6QTJCUTFMNU1ralNybjkzaU5KcUlCYUFFbHVLRG5MYjdQVU5PeVY5RFRheWlKVg?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
