# TSM Intelligence Report

- ticker: **TSM**
- Report as_of: **2026-11-22**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/TSM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TSM/key-statistics/
- AI analysis snapshot as_of: **2026-11-22**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-23T05:50:36.169294+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 3, 'ai': 11, 'unknown': 0, 'irrelevant': 11})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **13** exact headline/source/date matches; prior report **20261122T045655Z-f5ef568d/TSM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 11 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 40.0%; oldest publication 2026-11-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 318.7100 |
| Return 1D (%) | -9.4805 |
| Return 1W (%) | -20.0687 |
| Return 1M (%) | -25.0235 |
| Return YTD (%) | 5.7014 |
| Return 1Y (%) | 16.0660 |
| Annualized volatility (%) | 43.5453 |
| Beta vs SPY | 2.2318 |
| Max drawdown (%) | -34.3948 |
| Sharpe (rf=0) | 0.5620 |
| Downside deviation (rf=0, %) | 31.0989 |
| Sortino (rf=0) | 0.7869 |
| Historical VaR 95% (1D, %) | 4.3901 |
| Historical ES 95% (1D, %) | 6.3161 |
| Correlation vs SPY | 0.7327 |
| Tracking error vs SPY (%) | 34.4731 |
| P/E (trailing) | 20.66 |
| P/B | 61.22 |
| EV/EBITDA | 2.87 |
| Revenue growth (%) | 50.90 |
| Forward P/E (estimate) | 13.63 |
| Gross margin (%) | 65.85 |
| Operating margin (%) | 57.96 |
| Return on equity (%) | 41.86 |
| Free cash flow yield (%) | N/A |
| MA50 | 422.1053 |
| Close vs MA50 (%) | -24.4951 |
| MA200 | 402.2465 |
| Close vs MA200 (%) | -20.7675 |
| RSI (14, Wilder) | 28.2713 |
| MACD (12,26) | -20.8025 |
| MACD signal (9) | -14.9543 |
| MACD histogram | -5.8482 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TSM': 287, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 318.7100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -9.4805 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -20.0687 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -25.0235 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 5.7014 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 16.0660 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 43.5453 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 31.0989 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.7869 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.3901 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.3161 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.7327 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 34.4731 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.2318 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -34.3948 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.5620 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 13.6287 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 65.8460 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 57.9610 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 41.8600 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 20.6552 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 28.2713 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -5.8482 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -24.4951 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -20.7675 -> Clearly below the moving-average trend level.

## TAILWINDS

### Taiwan Semiconductor Shares Jump 4.66% After Hours - Taiwan Semiconductor (NYSE:TSM), NVIDIA (NASDAQ:NVDA
- Summary: Taiwan Semiconductor Shares Jump 4.66% After Hours - Taiwan Semiconductor (NYSE:TSM), NVIDIA (NASDAQ:NVDA
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxPNFJtektvbGxSYVJkOWgtWWtxalpCR1p5VkVySWJHRFZ4UWNsRllyWVNVVWszOWtoXzJmZTFib2lPZHlfLTlsRW12Q3lfczNsYWRXU2pHMzJheUVKTXVsV09vbm8tV1pHdFNwYS0yMW5yX0J2N0xIVXprNTdIVlJldkM2UHlnS3VtWTRtb3F0Z0RKQWNKV2tMN2NrSnhTZ2hwa1hwc1U4VFBjSmZCSHF2bUo1cy1xRmt4Z3ZUWE9n?oc=5>

## HEADWINDS

### TSMC Stock Slides As Taiwan Market Suffers Worst Week Since 1990: What's Going On?
- Summary: TSMC Stock Slides As Taiwan Market Suffers Worst Week Since 1990: What's Going On?
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxPQVhxWWp0SU9TOVVGLWQ1azhrbXlnVng0QjBUNzhXS3J1Q1FSU3F4dG1ZYzlzaW0xa3I4M3FoNzVsazV4TTNCRHNOb3BNUHQxVjRRZ011a3licEdIZmdsLUdVVGVJdjZWdlp5X251Q1VhdnZETmFYa3BURGtjenZiX0dqZVZFUkREd29XNkNiM1RuR3l2Y1Q5VE9JRzZ3NEdDY1cxLWRQQlJtTFlzdjk2NzZicThkeFIydzduVjlWUXhKdXNRZkFXbHdUc2pyVnpaaTVMOWR1SQ?oc=5>

### Taiwan Semiconductor Manufacturing (NYSE:TSM) Shares Tumble As Customer Shock Clouds AI Outlook
- Summary: Taiwan Semiconductor Manufacturing (NYSE:TSM) Shares Tumble As Customer Shock Clouds AI Outlook
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxPRGhfT1h2VHNtYVlES2FYa3lSdm40WmcxQ3d3TGl2bG9xZG5KbHFYeHlqZ044TEFjUHNZZDBvVjZxc3ZxdGxKQ18wc1lXNjVXZzItMUt2Ym50X1lfWk84eXJneUpZYUtIVEdwZFN0SlBXbnpPUWdnNmxPUGVBRDI2amdTUDdOU1Naal9ocl9iSlQ2TkJkVl81ZGlnaTFpcWRFX05XZDl2VzVhcXE1?oc=5>

### TSMC, Samsung suspend some chip shipments to Chinese customers, FT reports
- Summary: TSMC and Samsung halted certain chip shipments to Chinese customers, potentially limiting revenue and affecting supply chain dynamics.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxPbjF1dzFmQTBpQ2FXQ2NSV05xcFVReXBnUS1YZ1hDS3RvbXZOY2RHTlJaNGJORGozUDh0bHBtWndqVlJjQnk3VzJlaDhBQWpqZlJ2WXF5UkxRYTRsTlNBLURMcS1pQXBBVl94ZmxEQzFqSGV0MWlubTJEMFZ0OWdYWEVSRHJaWGx5dWdtLWdOOE9HSVVzeVlUY3AwaGE0cmVSd3hXMFVzRG0tSFBUblRZakdYY2lOZWZ3MUFkb3dxUQ?oc=5>

### Taiwan Semiconductor Manufacturing Company Limited (TSM) Pulled Back Amid Broader AI Buildout Correction
- Summary: AI buildout correction leads to TSMC pullback, reducing growth momentum.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxPT0s2ZFZUb0pqQVhOWmJhem81bkdWenZqZUpTbGpncHdiNW9aNHpFd004dVFIUDVRb3ZPVmMwZnhnUnlqYUxVUEkzNXlHQXRqdGJzY2k5T2Eyd1VkQ01EQUMwU1RjSjJfYVhqV0YtX0FvS3JnTUROY3lvQ2ZqS3BsZ0dzX001VmdsaFVHd0dzUmJ4MnppZTVNWWV4WmY4SnV0M0x2TnlsMTE5Ty1lMkViZkNQV1JpUQ?oc=5>

### Taiwan Semiconductor Manufacturing down 8.66% on Friday
- Summary: TSM shares fell 8.66% on Friday, reflecting market pressure.
- Date: 2026-11-20 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQaGlPZGhsSnpuOEdtUGprWUxqS3FDQlhLV2w1R1JTc2VGczdyeUZQa0tjTVpEb0NaV3Y0OTRZS2E4U0lXU25qZk5ndWNocFhKZmQzNGJiUkRORFFuZXAycTFrYUw5SjVSdmNiVmdTZkl2czhEM243LU1YZ01JQ0kyX0xrZkFwOU9TeHFkNkxmLXM3bXp0VWZYc0lNYUM?oc=5>

### TSMC halts advanced chip orders from Chinese designers in Taiwan
- Summary: TSMC stops advanced chip orders from Chinese designers, limiting production capacity.
- Date: 2026-11-20 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxObEZkM3lQWGU4dnZKNlRZUEZJRzNPU19DS1BpckgxdGxOR204amJWRW5rcjdOWDNJczdnUE1zLWhyQ3RlWnZzcVdTaXAxSU8tSS04Y0szZmIzVXVYbFpfeUVpcFBJSEtZVWViQnc4VDZDZXkwQ0tYN1JERWpZT2M0VkdydVVtSGVBRW4xVEdndU1YTHBkVkM1MXZmaw?oc=5>

## CATALYSTS

### Susquehanna’s $600 Target Says TSMC’s Selloff Went Too Far
- Summary: Susquehanna argues TSMC’s recent price decline was excessive, suggesting a rebound is likely.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOQ2sxNG5QZzRDR2p4dXFBd3pUVXZOZHpWRFlNc3hEVGhoekpZMnItWnc5TnFBMUQ5VnRPQlV4RzJTNkZBeDVXNnVtekQ3UHM3X1NOOVpTVmRUSzUtSFdsd0w0dTJYOEhENlhjN2o2X2xhRi1KYVFYOFdLTWp1S1BsTmJ1V3JRWnVsX0g4cjd4d2dWQ2phMlQyZFZ5c09vUQ?oc=5>

### Stanley Druckenmiller, Leopold Aschenbrenner and 25 Other Big Funds Sold Taiwan Semiconductor Last Quarter, While 38 Bought. Who’s Right?
- Summary: Large funds sold and bought TSM shares, indicating market activity.
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7wFBVV95cUxNTDBiR1JxVXF5T3QzNVE2WkF1aW9SRVM2ekc0clVaSTM1TGM3MkZIeGFWQi1YUU9yVTJTdDNDS3ROQ0plS2ZCQTVDT3dTOHduWkpzMTVLUlFad3M0R1Y2NlBfVS0yejBacGZrRFY4TndBSFBCXzN4QVBwaHJjU2xHcnlEYmRDOGpNX091UWVYSU1vY1U1bVY1enVxVkt3OVY3OGlPaWVUTTNFLU1CcmVYeXd1Ql9GdFRTSWhwQTlVeWwybnJnQkpZdm5Zc2VROE5MbWx3cjdLVUVVS085ZlZYZVNxXzJ0OXBpWXFFSDcwYw?oc=5>

### Taiwan Semiconductor Manufacturing (TSM) executive Lu bought 5,000 shares for $303K at $60.57
- Summary: TSM executive Lu purchased 5,000 shares, indicating insider confidence in the company.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxNd2ZOWkpyQUJiaDc5LUphRmpUcXE2cXRKX2VqMjRYaEkxQ3ZNTERkRGhzYVFYMHAtMW90TmY1em0xU2ZKUEJqVk85ZGRwQmNybHlFbmtSQ0UyTkhHbGRuYmNlaTdrbWIxRm00T3V2MVVtU3lqaXVaa2wwdV8yRWY4bEdRbjItSjhIMndzNHVrZ05UMWwxNUlUaVZ4aFh3TENG?oc=5>

## RISKS

### TSMC: Look At The Warning Signs From Chinese Tech Giants (NYSE:TSM)
- Summary: TSMC highlights potential risks from Chinese tech giants, signaling possible supply chain or regulatory challenges.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNVndRbzM2WUFsNk5OT1J2WkRhSWpaUThEaUxRcEl3UlJDRWlEVmpuN3FIQ2ZWNmQ5U3lMTWlKWTY4clVoZkg4RHVnSER2X28tVmU2UWhvbmo4UDBiU1RXRnFCWEFKNzdpNUNsbnU3NDV5RVVhSUpveGNSc09FdkhxdmVqZDh1YzhMdjNEc3FWTUVLSU1ZbTV2ZXF1dXM?oc=5>

### Taiwan Semiconductor Manufacturing (NYSE:TSM) Pauses Advanced Chip Shipments To China
- Summary: TSMC halts advanced chip shipments to China, potentially impacting revenue and supply chain stability.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxNOGhIWnVaYlI5aFc1emtra29CdDBWS3J0dXVRTFZhQmdXNThUU2hUVXZBYWVLR2RpaHJEX1ZqNnJXTzQyWFJ4Q1BQN1dmeDlXVGxQTDZwTkNKbHlxWUFzT2VaZFFENXBwYjVyV2NCN1d2dVBmODA2MGVUdTk0UEJHcW9Mc2dJRHRTTUpJanI1dGR3dDMyNkVVM1QycU9iVzJ5VGVIUEpJWQ?oc=5>

### Taiwan Semiconductor Manufacturing (NYSE:TSM) Hit A Revenue High, Is The Stock Fully Valued?
- Summary: TSMC reports record revenue, raising questions about valuation and future growth prospects.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxQbkVadHZpUmp3RjA2VXZmTUdNOFZ2X0ZQQTdaZ1FpYV81dWxWNTJfUjJDUFNDb1JYQUhfNXdQdlV2a2FEWGNJaUJfUXJUSk5WTW11NkJqWEVIWkFxT0JXbXY0SHpsQy1RMnJ1Yml4clVlVmpnWjBhWWxlSU1OeHV3SmRQRFBnZ1lQVWh3QUJEMG5NRXFFeFkzOTRpQUk5WW1RN1JvdHYxa2Nvc1c5?oc=5>

### Ken Fisher’s Quiet Bet on TSMC (TSM): Owning the AI Boom Without Picking a Winner
- Summary: Analyst Ken Fisher highlights TSMC’s role in AI, suggesting a positive outlook for the company.
- Date: 2026-11-19 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMif0FVX3lxTE43WURqSjBnSXhKb1ZvNFhvREM5UmEycXNlc043ZEFncG8weXl5NklhSG5IWDZSRFdTOVlVWF8zWTg5aUNCeGlSLXJtNVk0T2VfMWRoa3VJdUZwR1lxeTFhbWhCSXh5SWRMSGFEVU9MY3Zkbm5iT1NBOFZFeDlxazQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TSM** | **20.66** | **61.22** | **2.87** | **50.90** | **1,652,980,711,424.00 USD** | **16.07** |
| UMC | 11.36 | 2.08 | -0.35 | 25.60 | 30,193,838,080.00 USD | 72.08 |
| GFS | 101.60 | 1.66 | 9.51 | 12.50 | 19,822,878,720.00 USD | 10.73 |
| INTC | N/A | 2.37 | 14.91 | 20.90 | 272,553,181,184.00 USD | 52.53 |

Peers fetched as_of: 2026-11-22; TSM reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-22

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
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxPQVhxWWp0SU9TOVVGLWQ1azhrbXlnVng0QjBUNzhXS3J1Q1FSU3F4dG1ZYzlzaW0xa3I4M3FoNzVsazV4TTNCRHNOb3BNUHQxVjRRZ011a3licEdIZmdsLUdVVGVJdjZWdlp5X251Q1VhdnZETmFYa3BURGtjenZiX0dqZVZFUkREd29XNkNiM1RuR3l2Y1Q5VE9JRzZ3NEdDY1cxLWRQQlJtTFlzdjk2NzZicThkeFIydzduVjlWUXhKdXNRZkFXbHdUc2pyVnpaaTVMOWR1SQ?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxPRGhfT1h2VHNtYVlES2FYa3lSdm40WmcxQ3d3TGl2bG9xZG5KbHFYeHlqZ044TEFjUHNZZDBvVjZxc3ZxdGxKQ18wc1lXNjVXZzItMUt2Ym50X1lfWk84eXJneUpZYUtIVEdwZFN0SlBXbnpPUWdnNmxPUGVBRDI2amdTUDdOU1Naal9ocl9iSlQ2TkJkVl81ZGlnaTFpcWRFX05XZDl2VzVhcXE1?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxPbjF1dzFmQTBpQ2FXQ2NSV05xcFVReXBnUS1YZ1hDS3RvbXZOY2RHTlJaNGJORGozUDh0bHBtWndqVlJjQnk3VzJlaDhBQWpqZlJ2WXF5UkxRYTRsTlNBLURMcS1pQXBBVl94ZmxEQzFqSGV0MWlubTJEMFZ0OWdYWEVSRHJaWGx5dWdtLWdOOE9HSVVzeVlUY3AwaGE0cmVSd3hXMFVzRG0tSFBUblRZakdYY2lOZWZ3MUFkb3dxUQ?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxPT0s2ZFZUb0pqQVhOWmJhem81bkdWenZqZUpTbGpncHdiNW9aNHpFd004dVFIUDVRb3ZPVmMwZnhnUnlqYUxVUEkzNXlHQXRqdGJzY2k5T2Eyd1VkQ01EQUMwU1RjSjJfYVhqV0YtX0FvS3JnTUROY3lvQ2ZqS3BsZ0dzX001VmdsaFVHd0dzUmJ4MnppZTVNWWV4WmY4SnV0M0x2TnlsMTE5Ty1lMkViZkNQV1JpUQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQaGlPZGhsSnpuOEdtUGprWUxqS3FDQlhLV2w1R1JTc2VGczdyeUZQa0tjTVpEb0NaV3Y0OTRZS2E4U0lXU25qZk5ndWNocFhKZmQzNGJiUkRORFFuZXAycTFrYUw5SjVSdmNiVmdTZkl2czhEM243LU1YZ01JQ0kyX0xrZkFwOU9TeHFkNkxmLXM3bXp0VWZYc0lNYUM?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxObEZkM3lQWGU4dnZKNlRZUEZJRzNPU19DS1BpckgxdGxOR204amJWRW5rcjdOWDNJczdnUE1zLWhyQ3RlWnZzcVdTaXAxSU8tSS04Y0szZmIzVXVYbFpfeUVpcFBJSEtZVWViQnc4VDZDZXkwQ0tYN1JERWpZT2M0VkdydVVtSGVBRW4xVEdndU1YTHBkVkM1MXZmaw?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOQ2sxNG5QZzRDR2p4dXFBd3pUVXZOZHpWRFlNc3hEVGhoekpZMnItWnc5TnFBMUQ5VnRPQlV4RzJTNkZBeDVXNnVtekQ3UHM3X1NOOVpTVmRUSzUtSFdsd0w0dTJYOEhENlhjN2o2X2xhRi1KYVFYOFdLTWp1S1BsTmJ1V3JRWnVsX0g4cjd4d2dWQ2phMlQyZFZ5c09vUQ?oc=5
- https://news.google.com/rss/articles/CBMi7wFBVV95cUxNTDBiR1JxVXF5T3QzNVE2WkF1aW9SRVM2ekc0clVaSTM1TGM3MkZIeGFWQi1YUU9yVTJTdDNDS3ROQ0plS2ZCQTVDT3dTOHduWkpzMTVLUlFad3M0R1Y2NlBfVS0yejBacGZrRFY4TndBSFBCXzN4QVBwaHJjU2xHcnlEYmRDOGpNX091UWVYSU1vY1U1bVY1enVxVkt3OVY3OGlPaWVUTTNFLU1CcmVYeXd1Ql9GdFRTSWhwQTlVeWwybnJnQkpZdm5Zc2VROE5MbWx3cjdLVUVVS085ZlZYZVNxXzJ0OXBpWXFFSDcwYw?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxNd2ZOWkpyQUJiaDc5LUphRmpUcXE2cXRKX2VqMjRYaEkxQ3ZNTERkRGhzYVFYMHAtMW90TmY1em0xU2ZKUEJqVk85ZGRwQmNybHlFbmtSQ0UyTkhHbGRuYmNlaTdrbWIxRm00T3V2MVVtU3lqaXVaa2wwdV8yRWY4bEdRbjItSjhIMndzNHVrZ05UMWwxNUlUaVZ4aFh3TENG?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNVndRbzM2WUFsNk5OT1J2WkRhSWpaUThEaUxRcEl3UlJDRWlEVmpuN3FIQ2ZWNmQ5U3lMTWlKWTY4clVoZkg4RHVnSER2X28tVmU2UWhvbmo4UDBiU1RXRnFCWEFKNzdpNUNsbnU3NDV5RVVhSUpveGNSc09FdkhxdmVqZDh1YzhMdjNEc3FWTUVLSU1ZbTV2ZXF1dXM?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxNOGhIWnVaYlI5aFc1emtra29CdDBWS3J0dXVRTFZhQmdXNThUU2hUVXZBYWVLR2RpaHJEX1ZqNnJXTzQyWFJ4Q1BQN1dmeDlXVGxQTDZwTkNKbHlxWUFzT2VaZFFENXBwYjVyV2NCN1d2dVBmODA2MGVUdTk0UEJHcW9Mc2dJRHRTTUpJanI1dGR3dDMyNkVVM1QycU9iVzJ5VGVIUEpJWQ?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxQbkVadHZpUmp3RjA2VXZmTUdNOFZ2X0ZQQTdaZ1FpYV81dWxWNTJfUjJDUFNDb1JYQUhfNXdQdlV2a2FEWGNJaUJfUXJUSk5WTW11NkJqWEVIWkFxT0JXbXY0SHpsQy1RMnJ1Yml4clVlVmpnWjBhWWxlSU1OeHV3SmRQRFBnZ1lQVWh3QUJEMG5NRXFFeFkzOTRpQUk5WW1RN1JvdHYxa2Nvc1c5?oc=5
- https://news.google.com/rss/articles/CBMif0FVX3lxTE43WURqSjBnSXhKb1ZvNFhvREM5UmEycXNlc043ZEFncG8weXl5NklhSG5IWDZSRFdTOVlVWF8zWTg5aUNCeGlSLXJtNVk0T2VfMWRoa3VJdUZwR1lxeTFhbWhCSXh5SWRMSGFEVU9MY3Zkbm5iT1NBOFZFeDlxazQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
