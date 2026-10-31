# TSM Intelligence Report

- ticker: **TSM**
- Report as_of: **2026-10-30**
- Market data as_of: **2026-10-30**
- Quant sources: https://finance.yahoo.com/quote/TSM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TSM/key-statistics/
- AI analysis snapshot as_of: **2026-10-30**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-31T02:05:20.935869+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 1, 'ai': 10, 'unknown': 0, 'irrelevant': 11})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261030T021807Z-b9de7146/TSM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 9 named publishers; 3 exact duplicates; 22 HTTPS source links; largest publisher share 40.91%; oldest publication 2026-10-26

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 406.1300 |
| Return 1D (%) | -5.9471 |
| Return 1W (%) | -2.9581 |
| Return 1M (%) | -10.9735 |
| Return YTD (%) | 34.6945 |
| Return 1Y (%) | 35.3566 |
| Annualized volatility (%) | 39.7189 |
| Beta vs SPY | 2.1826 |
| Max drawdown (%) | -21.5466 |
| Sharpe (rf=0) | 0.9633 |
| Downside deviation (rf=0, %) | 26.7603 |
| Sortino (rf=0) | 1.4298 |
| Historical VaR 95% (1D, %) | 4.2163 |
| Historical ES 95% (1D, %) | 5.2559 |
| Correlation vs SPY | 0.7028 |
| Tracking error vs SPY (%) | 32.0495 |
| P/E (trailing) | 26.32 |
| P/B | 77.51 |
| EV/EBITDA | 3.78 |
| Revenue growth (%) | 50.90 |
| Forward P/E (estimate) | 17.37 |
| Gross margin (%) | 65.85 |
| Operating margin (%) | 58.66 |
| Return on equity (%) | 41.85 |
| Free cash flow yield (%) | N/A |
| MA50 | 434.5345 |
| Close vs MA50 (%) | -6.5368 |
| MA200 | 398.6491 |
| Close vs MA200 (%) | 1.8766 |
| RSI (14, Wilder) | 38.3932 |
| MACD (12,26) | -5.3305 |
| MACD signal (9) | -3.4843 |
| MACD histogram | -1.8462 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TSM': 272, 'SPY': 272}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 406.1300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -5.9471 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.9581 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -10.9735 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 34.6945 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 35.3566 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 39.7189 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.7603 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.4298 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.2163 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.2559 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.7028 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.0495 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.1826 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -21.5466 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9633 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.3669 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 65.8460 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 58.6550 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 41.8550 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 26.3208 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 38.3932 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.8462 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -6.5368 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 1.8766 -> Slightly above the moving-average trend level.

## TAILWINDS

### TSMC Gains 3% on Reported 20% Price Hike for AI Chip Packaging
- Summary: TSMC Gains 3% on Reported 20% Price Hike for AI Chip Packaging
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNN3UtckREdlJ1c3JCRHdVNURWNVNsOW1TaVYwa1JIdk9tbEV5YTk4YmRoZDJIMkFGcXhWeTRaZ2RHT2JzWEZaeWRkMEJvRk41WW0xNGVwa3RpWVB3Y09vRVdPbHRQRms1UHAtaUpWS3cxNHAwNnJzdzVXWjJ2WFNPQWVHMHhOa2VUTWhzYnUyRXRaUQ?oc=5>

## HEADWINDS

### Taiwan Semiconductor Manufacturing (TSM) Stock Looks Pricey Against Cash Flow
- Summary: Valuation concerns relative to cash flow.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxORldEaFpNSnljQTZVWGtRUmV3X0R2QTZQTE9pNm0yWDlremFDNV85cHVhRnlZTy02c2Zkd0dsTTE0Zkx4LWJibjZVR0RHWlhZdy1WcHRVZ2dHQlpHOWxGWEVHUnlJRU5mcFVhU1FnWXk5TzB4ZFdMYjkzRDctYjJ0d0tYeGxfbHlBU1ducHNRZEFOYkwzZy1TTXRGNjRkcDlZZTUwcDNLdlZXSGFsb3c?oc=5>

### TSMC: The Cracks Are Showing (NYSE:TSM)
- Summary: Report indicates operational or financial challenges for TSM, raising concerns.
- Date: 2026-10-29 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMid0FVX3lxTE5NM2ZPNW5mb2NfMHdER3RRX2QyeVkwSDl3anVfdVdWUTQ4UkxyRHBxeGJ0QkFRb0tybEpVNWNXRXZwR0gyWm5UNV9PQUIwOWV5M0xVc1lxZXdKeTV2eFVzTWc1MUF0cEdtYW1NRTMyamVWX0t6V0Y0?oc=5>

### Taiwan Semiconductor Manufacturing (NYSE:TSM) Stock Falls 6.2% - Should You Sell?
- Summary: TSM shares dropped 6.2% amid market volatility, prompting sell‑side analysis.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxNOTNhd1NCT0YzcF84QmlUeEstdmFvSTl4cEVlMElYOHNxTTQ2STVNZUdQTjctbXc5RlpjblF5QzMtNkpFM1FIcVF6cGdfdGVCby00V3FrMnFkcnQzY1E4OGt5NVpTQ3NiV3ptZGMyZW80ZjFzQmw4TXBwRW8zOEFVTGd0TEY5OGpPa290RlEyYy11X0RRaWxiRFVrRWlBbzZLWE0zVjFvdDZ4eE9pZGVpX2FzZzBQQTJNU3hvMzJEd1dEcDVYcFh0ZnBPRnlhUm8?oc=5>

### Taiwan Semiconductor Manufacturing Co Ltd Stock (TSM) Opened Down by 3.67% on Oct 30: A Full Analysis
- Summary: TSM opened lower 3.67% on Oct 30, reflecting short‑term market pressure.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxNb3QwTUJTTUc5ZlhVT1c4bzNFM3U5MndPZnNjcmJpQi1tMUVOR1Jya0lWUF96R2ZUWmU5M2wweUhUT2FhUE9seGRwQXpuUWhxTWR2eldJMGJGUXdBSFZ4S1E3TzZGT0xjRXNiaWdZcGZQTTE1X1hINGlUZUFpSGRWUmxTUmxUR3NnTGc?oc=5>

### TSMC to raise advanced chip packaging prices by up to 20%, report says
- Summary: TSMC plans to increase advanced chip packaging prices by up to 20%, potentially raising costs for customers.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQOXprTXl0Q2V4bzI5bEh4M0kwNDNsSzJnOWxFMFVhLUlRWmVWMm5CS2YtVWNXVkEtQWx3S1lNZlVmTWtyNVFRak5ha05XR3VEeW8wVWdJWmdGZkFYMDAxOVpwc2dzTmJqU0ZaVnJvU2pOYm1VM3Q5SGlUOFYzQ2hWdERGdldhUHZ1QnN3WHlOU2tpN0tqSVF5amljQS1WOUk?oc=5>

## CATALYSTS

### TSMC: The Toll Road Of The AI Economy Is On Sale (NYSE:TSM)
- Summary: TSMC highlights its role in AI economy, suggesting growth potential.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNMXNDRzVKSl9XSDFyUlRwRWctZzJFQVExcGZsZmhKZzVfUnRTYUtlUm5TTHZPR1dZakx3c2VEUjBtTWxGdjFoODB3RFFOVDE0Q1BKVGRpRW1hTzdxcHUxbjVkcUdLWGVfVWx1RVNCN3lWbjZOcGI2cUVlNHVwTWUwUVJ6OGlLcnp6RmV5WjBaRFhfUQ?oc=5>

### Here’s What a $10,000 Investment in TSMC Stock Will Be Worth by 2030
- Summary: Projected $10,000 TSM investment could grow significantly by 2030, indicating long‑term upside.
- Date: 2026-10-30 | Impact: high | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxOU1hNeUxiYWNYT2JHOHRZVm9JOEx2RmtSU1I3SUV6emRrUmgzUmtvR2k0clBENDlDRTF6SEtIQTRGOVZ4Tm9wTVlDam01bklqRzljU1U0akEzNW5iOGY0cmZVU21QTWJkMlZvTVBHWVpVanhlTVFRQXAteGJ5SzlLcG9ublZqQkw1SlRVZ1BjUjkxWl92dXJvT3VaWWQ2R2lhU29BOVpBUGRXMnNzWGpsakRVRQ?oc=5>

### Taiwan Semiconductor Manufacturing Company Ltd. (TSM) is Attracting Investor Attention: Here is What You Should Know
- Summary: TSM is drawing investor interest, suggesting potential positive market sentiment.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxPMlBUNlRGNktfa0JOdWxDeTFIZkdoMHhhaEkzSVRVek9acWpFNHpIYkN1dVBaVktiRXloUkcwVGtNSEdRT3AwdFdFMTJnTkNaLXFyT2p3LXF3WEVNaHo1cjdoaEszelBJbWJXbTR3NGIzTzhZSFFBUWN4SGo0aE9OcmFiWnM1R1ZsYzEtNFJFejVlMUlJR01QQU1TU0xwRE9GcklWakU1MUNWZXBBakpUTg?oc=5>

### If AI Spending Slows in 2027, These Semiconductor Stocks Could Hold Up Best
- Summary: Slower AI spending may support TSM’s performance relative to peers in 2027.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxPd0FnTTRGYlBXT1k3T0RjQmoxTWllR24wNExmQ0JqanRvLTBuT2ZwY3Z3aGpwdzJmVElmeTRneTdNNGItdG02cHhmVGc1ZXdrTkxKMEhCQ3NaOHhLMW5fT0FHSWRiYk1SVW1NcVBLQUdIUFR6SGp5eFAxckJLekVXR2ZwWGIybkh6VktsMEZxSF9abHREdzBoVkdqMHpwaldmNUFGV3pZWGJHTG5XbGdPNDVPcWtIRHRlUWc?oc=5>

### Beyond NVIDIA: Why TSMC Stock Looks Attractive After Q3 Earnings
- Summary: TSMC’s Q3 earnings boost investor interest, making the stock attractive.
- Date: 2026-10-28 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOTl9Qckw0VV9Ud2FBeDJiSnRJXzdhX2c0VGtNVklNTVZUNlZXaG14Q3VicGQ5SHhnUF9kYWRfZmNXNjJLUW9RMTdBb0d3VXlTejhyQVJsb3JLX3JjTTV0bkJlTnZ0bFEtSlZ6MkNoNDZVSHNwYktuWDF4YlBnNGlObk10WFY2enpwS0RRMk14aGFsTWVGZFdV?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TSM** | **26.32** | **77.51** | **3.78** | **50.90** | **2,106,382,745,600.00 USD** | **35.36** |
| UMC | 15.74 | 2.86 | -0.25 | 25.60 | 41,830,002,688.00 USD | 125.41 |
| GFS | 32.73 | 1.95 | 11.29 | 5.80 | 23,355,840,512.00 USD | 16.65 |
| INTC | N/A | 2.87 | 29.74 | 25.40 | 349,185,605,632.00 USD | 63.75 |

Peers fetched as_of: 2026-10-30; TSM reuses existing data (market data as_of: 2026-10-30); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-30

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMikgFBVV95cUxNN3UtckREdlJ1c3JCRHdVNURWNVNsOW1TaVYwa1JIdk9tbEV5YTk4YmRoZDJIMkFGcXhWeTRaZ2RHT2JzWEZaeWRkMEJvRk41WW0xNGVwa3RpWVB3Y09vRVdPbHRQRms1UHAtaUpWS3cxNHAwNnJzdzVXWjJ2WFNPQWVHMHhOa2VUTWhzYnUyRXRaUQ?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxORldEaFpNSnljQTZVWGtRUmV3X0R2QTZQTE9pNm0yWDlremFDNV85cHVhRnlZTy02c2Zkd0dsTTE0Zkx4LWJibjZVR0RHWlhZdy1WcHRVZ2dHQlpHOWxGWEVHUnlJRU5mcFVhU1FnWXk5TzB4ZFdMYjkzRDctYjJ0d0tYeGxfbHlBU1ducHNRZEFOYkwzZy1TTXRGNjRkcDlZZTUwcDNLdlZXSGFsb3c?oc=5
- https://news.google.com/rss/articles/CBMid0FVX3lxTE5NM2ZPNW5mb2NfMHdER3RRX2QyeVkwSDl3anVfdVdWUTQ4UkxyRHBxeGJ0QkFRb0tybEpVNWNXRXZwR0gyWm5UNV9PQUIwOWV5M0xVc1lxZXdKeTV2eFVzTWc1MUF0cEdtYW1NRTMyamVWX0t6V0Y0?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxNOTNhd1NCT0YzcF84QmlUeEstdmFvSTl4cEVlMElYOHNxTTQ2STVNZUdQTjctbXc5RlpjblF5QzMtNkpFM1FIcVF6cGdfdGVCby00V3FrMnFkcnQzY1E4OGt5NVpTQ3NiV3ptZGMyZW80ZjFzQmw4TXBwRW8zOEFVTGd0TEY5OGpPa290RlEyYy11X0RRaWxiRFVrRWlBbzZLWE0zVjFvdDZ4eE9pZGVpX2FzZzBQQTJNU3hvMzJEd1dEcDVYcFh0ZnBPRnlhUm8?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxNb3QwTUJTTUc5ZlhVT1c4bzNFM3U5MndPZnNjcmJpQi1tMUVOR1Jya0lWUF96R2ZUWmU5M2wweUhUT2FhUE9seGRwQXpuUWhxTWR2eldJMGJGUXdBSFZ4S1E3TzZGT0xjRXNiaWdZcGZQTTE1X1hINGlUZUFpSGRWUmxTUmxUR3NnTGc?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQOXprTXl0Q2V4bzI5bEh4M0kwNDNsSzJnOWxFMFVhLUlRWmVWMm5CS2YtVWNXVkEtQWx3S1lNZlVmTWtyNVFRak5ha05XR3VEeW8wVWdJWmdGZkFYMDAxOVpwc2dzTmJqU0ZaVnJvU2pOYm1VM3Q5SGlUOFYzQ2hWdERGdldhUHZ1QnN3WHlOU2tpN0tqSVF5amljQS1WOUk?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNMXNDRzVKSl9XSDFyUlRwRWctZzJFQVExcGZsZmhKZzVfUnRTYUtlUm5TTHZPR1dZakx3c2VEUjBtTWxGdjFoODB3RFFOVDE0Q1BKVGRpRW1hTzdxcHUxbjVkcUdLWGVfVWx1RVNCN3lWbjZOcGI2cUVlNHVwTWUwUVJ6OGlLcnp6RmV5WjBaRFhfUQ?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxOU1hNeUxiYWNYT2JHOHRZVm9JOEx2RmtSU1I3SUV6emRrUmgzUmtvR2k0clBENDlDRTF6SEtIQTRGOVZ4Tm9wTVlDam01bklqRzljU1U0akEzNW5iOGY0cmZVU21QTWJkMlZvTVBHWVpVanhlTVFRQXAteGJ5SzlLcG9ublZqQkw1SlRVZ1BjUjkxWl92dXJvT3VaWWQ2R2lhU29BOVpBUGRXMnNzWGpsakRVRQ?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxPMlBUNlRGNktfa0JOdWxDeTFIZkdoMHhhaEkzSVRVek9acWpFNHpIYkN1dVBaVktiRXloUkcwVGtNSEdRT3AwdFdFMTJnTkNaLXFyT2p3LXF3WEVNaHo1cjdoaEszelBJbWJXbTR3NGIzTzhZSFFBUWN4SGo0aE9OcmFiWnM1R1ZsYzEtNFJFejVlMUlJR01QQU1TU0xwRE9GcklWakU1MUNWZXBBakpUTg?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxPd0FnTTRGYlBXT1k3T0RjQmoxTWllR24wNExmQ0JqanRvLTBuT2ZwY3Z3aGpwdzJmVElmeTRneTdNNGItdG02cHhmVGc1ZXdrTkxKMEhCQ3NaOHhLMW5fT0FHSWRiYk1SVW1NcVBLQUdIUFR6SGp5eFAxckJLekVXR2ZwWGIybkh6VktsMEZxSF9abHREdzBoVkdqMHpwaldmNUFGV3pZWGJHTG5XbGdPNDVPcWtIRHRlUWc?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOTl9Qckw0VV9Ud2FBeDJiSnRJXzdhX2c0VGtNVklNTVZUNlZXaG14Q3VicGQ5SHhnUF9kYWRfZmNXNjJLUW9RMTdBb0d3VXlTejhyQVJsb3JLX3JjTTV0bkJlTnZ0bFEtSlZ6MkNoNDZVSHNwYktuWDF4YlBnNGlObk10WFY2enpwS0RRMk14aGFsTWVGZFdV?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
