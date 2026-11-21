# TSM Intelligence Report

- ticker: **TSM**
- Report as_of: **2026-11-20**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/TSM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TSM/key-statistics/
- AI analysis snapshot as_of: **2026-11-20**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-21T05:31:12.359005+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 4, 'ai': 11, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261119T054856Z-9eb86811/TSM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 13 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-11-17

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
| P/E (trailing) | 22.81 |
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
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 22.8139 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 28.2713 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -5.8482 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -24.4951 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -20.7675 -> Clearly below the moving-average trend level.

## TAILWINDS

### Taiwan Semiconductor Shares Jump 4.66% After Hours - Taiwan Semiconductor (NYSE:TSM), NVIDIA (NASDAQ:NVDA
- Summary: Taiwan Semiconductor Shares Jump 4.66% After Hours - Taiwan Semiconductor (NYSE:TSM), NVIDIA (NASDAQ:NVDA
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxPNFJtektvbGxSYVJkOWgtWWtxalpCR1p5VkVySWJHRFZ4UWNsRllyWVNVVWszOWtoXzJmZTFib2lPZHlfLTlsRW12Q3lfczNsYWRXU2pHMzJheUVKTXVsV09vbm8tV1pHdFNwYS0yMW5yX0J2N0xIVXprNTdIVlJldkM2UHlnS3VtWTRtb3F0Z0RKQWNKV2tMN2NrSnhTZ2hwa1hwc1U4VFBjSmZCSHF2bUo1cy1xRmt4Z3ZUWE9n?oc=5>

### Taiwan Semiconductor Manufacturing (NYSE:TSM) Hit A Revenue High, Is The Stock Fully Valued?
- Summary: TSM reported a revenue high, indicating strong financial performance.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNdFZMVDR0eERfMHJrVHExSVR2VjhvaXMyNnN1YTBPY1FrLUxWVWtrRmMzTDMtN0RPUlB4RGI4dW9uODFLRVNRWmh4Vk4zZ3dLSmFSTVZHaEJsbjVOQk1jUHFyeEFUeXRjMm5VY2J4UWlRZXVWWnNWcGZwajNrVDlqWmNEMHVJQW5Tb2ZMQjNIUDREZ0M1NE13?oc=5>

### Taiwan Semiconductor Booked a Record NT$587 Billion Month. The Stock Has Lost Nearly 10% in Three Days Anyway
- Summary: Record bookings boost revenue outlook, though stock fell 10% recently.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxOaHExV3laWFhjQ1o4WFdDUWttdkxGckxUVkVtemV5dFcyYm5BMWNQbUJuR2Ezb2QxcVY4YmNLajBVbzhEX3lwMWRYUU5uQjdSdVJFM0stMjdWV3ZlWlFGZmNwZTZ4M3hBaWFXNXNPVE1sbE8yT0t6QTJCUTFMNU1ralNybjkzaU5KcUlCYUFFbHVLRG5MYjdQVU5PeVY5RFRheWlKVg?oc=5>

## HEADWINDS

### TSMC Stock Slides As Taiwan Market Suffers Worst Week Since 1990: What's Going On?
- Summary: TSMC Stock Slides As Taiwan Market Suffers Worst Week Since 1990: What's Going On?
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxPQVhxWWp0SU9TOVVGLWQ1azhrbXlnVng0QjBUNzhXS3J1Q1FSU3F4dG1ZYzlzaW0xa3I4M3FoNzVsazV4TTNCRHNOb3BNUHQxVjRRZ011a3licEdIZmdsLUdVVGVJdjZWdlp5X251Q1VhdnZETmFYa3BURGtjenZiX0dqZVZFUkREd29XNkNiM1RuR3l2Y1Q5VE9JRzZ3NEdDY1cxLWRQQlJtTFlzdjk2NzZicThkeFIydzduVjlWUXhKdXNRZkFXbHdUc2pyVnpaaTVMOWR1SQ?oc=5>

### Taiwan Semiconductor Manufacturing (NYSE:TSM) Shares Tumble As Customer Shock Clouds AI Outlook
- Summary: Taiwan Semiconductor Manufacturing (NYSE:TSM) Shares Tumble As Customer Shock Clouds AI Outlook
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxPRGhfT1h2VHNtYVlES2FYa3lSdm40WmcxQ3d3TGl2bG9xZG5KbHFYeHlqZ044TEFjUHNZZDBvVjZxc3ZxdGxKQ18wc1lXNjVXZzItMUt2Ym50X1lfWk84eXJneUpZYUtIVEdwZFN0SlBXbnpPUWdnNmxPUGVBRDI2amdTUDdOU1Naal9ocl9iSlQ2TkJkVl81ZGlnaTFpcWRFX05XZDl2VzVhcXE1?oc=5>

### Billionaire Stanley Druckenmiller Cut TSMC 94% in One Quarter, Leaving Just $14.9 Million
- Summary: Major shareholder sold 94% of TSMC shares, reducing stake to $14.9M.
- Date: 2026-11-19 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxPeUN5R2Q3c0phcFFzd1RVbnRCNzlFdDZkSXhFdERNTmg3Sjl1S0pXOWRQVmFSbkdYbHJHSFJxZDFYOUNSclFlUElEVzlobGRRbWpZNWdCMjdaTGFIS1BGWEctejBfOHR1clUtR2RzYWpDek5ldjZVdzRRSDJoZ28yNW1MQ3RsWFN1cEs0c1Vpb3V2WlBCa3VZSTBTbHo1aWlTamhxQ2k3eWZ3ZTg?oc=5>

### AMD Stock Drops Another 7% Before the Bell and Taiwan Semiconductor Slides 4.2% as Nasdaq Futures Fall 1.6% After Asia's Chip Selloff
- Summary: TSMC shares fell 4.2% amid broader market selloff and Nasdaq decline.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihgJBVV95cUxPWHNvMF9Dd0hVZ19jbHZ3T1NBcjFXYVBNMlYtWlNWRDZGQ0ZEcVd0UmduSU01UHY2V0s4V2tfMWZRVlNPUFJrbl9hM0FyMHFJaXpiQm9yb3NiLU9GbnAtdG84M3FZblYyMWFUNVBtSk45Vnc4UzR4YmRiRHRxVG1JNnhONFhKa2xDQVRIeDBBaTFJeURhRzRSZFZKdXF4N1lnbGZHTHhWek94UXgzVjVqMDdKNXlpbkdNZ1pBajQ1UTJpUWNTVVFrdHVRczRmdFJ1cWNkVm9iZ0owNnk4SjBqajRxa0FSY3djOTlYVVZ5NGxGNUpYYjhtNEtzZy03RUpzZF9PdTB3?oc=5>

### Taiwan market plunges 6.23% as AI suppliers report steady orders after Huang's exit
- Summary: Taiwan market drops 6.23% amid AI supplier concerns post-Huang exit.
- Date: 2026-11-20 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxQVEFzN2F2VkNPUDg1a1NLQTVQRDNfTmI2dkE0ZEIycVpndEk1bk5xRVdWT0Uyenc5bTVsNE9LZlJ5Uk1iRFBLZVBmcTFwUzd4TTB5WVhPZTBkdS1CcjVubTFPMl9JY3RsYkREaHlKeXZRcUc5VVRCRFBOOXlCeTJvZ0dVbF9wMUU2WGZGUTVmNA?oc=5>

### Taiwan Semiconductor Manufacturing down 8.66% on Friday
- Summary: TSM shares fell 8.66% on Friday, reflecting market pressure.
- Date: 2026-11-20 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQaGlPZGhsSnpuOEdtUGprWUxqS3FDQlhLV2w1R1JTc2VGczdyeUZQa0tjTVpEb0NaV3Y0OTRZS2E4U0lXU25qZk5ndWNocFhKZmQzNGJiUkRORFFuZXAycTFrYUw5SjVSdmNiVmdTZkl2czhEM243LU1YZ01JQ0kyX0xrZkFwOU9TeHFkNkxmLXM3bXp0VWZYc0lNYUM?oc=5>

### Seven funds trim positions in Taiwan Semiconductor in Q3 (TSM:NYSE)
- Summary: Seven funds reduced TSM holdings in Q3, indicating investor pullback.
- Date: 2026-11-20 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOUkdEaEF0ak9TekxtY0NRZ09KWURJNmRjSVdVaFd2blgzX2FDQzB0REtiNGZVbVA5bzloeWFEV1JXS1EyN3NuMTRmbkhsN1dpb2xvaG5aLUhCTUhmMmxxdUw0TElMcUVUaGV4QTlYMkdsaVJzYVh4ZkhzQ3BkZm5fWGlTUm4yQ09td2tVS2JmUGtfcjRpeG9Vb3Rn?oc=5>

### TSMC Is Halting Some China Chip Orders as a New U.S. Rule Kicks In
- Summary: New U.S. rule forces TSMC to stop China orders, hurting demand.
- Date: 2026-11-20 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxQLU5wYVlGTzVOQ214NVN2WWNFaFRSQmFneEFQTGxHYkZzNy1fUFU4MHMtR09YWXVKV3ZqalpBNHFjRVFqaHR5ejU3cGMydVcxN3lidGJrelF3bnNpWHljbkE2anl6UFI0dmNTRXcweXN5b0dRX3o4T093a2YtMmNRRkxoMC1KZFVsVWF4bUcxTkFXSFRVYTNybzFwd25QZ0lDcGJYcG1fTFo5NHRDSXc?oc=5>

### Taiwan Stocks Post Worst Week Since 1990 on 16nm Chip Curbs - Taiwan Semiconductor (NYSE:TSM)
- Summary: 16nm chip curbs trigger worst week, pressuring TSMC shares.
- Date: 2026-11-20 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQUlVPelRWV2tMYjlhR1Z5bl9BMTc4dDdkWUFleElyeDlFbEQxekItTEh3NHhyVmxQbEx2Y01LXzVMWG9MR094U2hMS2lyUU9tM2Q3YmdLUGZybnZKX0R6M1RRaThSWms0OExFQVpoSHN1TVZMMXFrQ3pMUXdLdU5TWUdaTlFqZ09XQnhfcmoxUW91UkxfaDBYS08yVE9RQXdDbGxrMkFHT1ZWU1hXbjRwcQ?oc=5>

### Taiwan Semiconductor Manufacturing Company Limited (TSM) Pulled Back Amid Broader AI Buildout Correction
- Summary: AI buildout correction leads to TSMC pullback, reducing growth momentum.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxPT0s2ZFZUb0pqQVhOWmJhem81bkdWenZqZUpTbGpncHdiNW9aNHpFd004dVFIUDVRb3ZPVmMwZnhnUnlqYUxVUEkzNXlHQXRqdGJzY2k5T2Eyd1VkQ01EQUMwU1RjSjJfYVhqV0YtX0FvS3JnTUROY3lvQ2ZqS3BsZ0dzX001VmdsaFVHd0dzUmJ4MnppZTVNWWV4WmY4SnV0M0x2TnlsMTE5Ty1lMkViZkNQV1JpUQ?oc=5>

## CATALYSTS

### TSMC, Samsung Reportedly Suspend Some Chip Deliveries To Chinese Customers Amid New US Export Rules
- Summary: TSMC, Samsung Reportedly Suspend Some Chip Deliveries To Chinese Customers Amid New US Export Rules
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi8AFBVV95cUxPNW5IYW5ubWZhdEw3S09KeC1xWUZKZzlmMW9ORFR6R01hY2p1MlpmZHpleVRKN3hwcmRQTWJicFhDYkJ5OC1IX1pBSDZfVDNETHB2Z1BaUUV5QVZhaFF1RXF3NGdLZ3JZcHVLeTIyMnFQb3hud2tlT2RoMU9uMlEyOEVpbW5jOE9xQnBYYnVnYVRpLVlESk03TTczN3JMYjU0SjJUU1pxQ2tYVTIzUHJBWU9VTEVEVzVwY3RGTkZUcmRGWVhGUUlPTEpNTlYyUEZnRjhWdXVDU2xJenE1dFNtVlZxc2RfWGctYnc2VUZndV8?oc=5>

### Susquehanna’s $600 Target Says TSMC’s Selloff Went Too Far
- Summary: Susquehanna argues TSMC’s recent price decline was excessive, suggesting a rebound is likely.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOQ2sxNG5QZzRDR2p4dXFBd3pUVXZOZHpWRFlNc3hEVGhoekpZMnItWnc5TnFBMUQ5VnRPQlV4RzJTNkZBeDVXNnVtekQ3UHM3X1NOOVpTVmRUSzUtSFdsd0w0dTJYOEhENlhjN2o2X2xhRi1KYVFYOFdLTWp1S1BsTmJ1V3JRWnVsX0g4cjd4d2dWQ2phMlQyZFZ5c09vUQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TSM** | **22.81** | **61.22** | **2.87** | **50.90** | **1,652,980,711,424.00 USD** | **16.07** |
| UMC | 11.36 | 2.08 | -0.35 | 25.60 | 30,193,838,080.00 USD | 72.08 |
| GFS | 111.13 | 1.66 | 9.51 | 12.50 | 19,822,878,720.00 USD | 10.73 |
| INTC | N/A | 2.37 | 14.91 | 20.90 | 272,553,181,184.00 USD | 52.53 |

Peers fetched as_of: 2026-11-20; TSM reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-20

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
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNdFZMVDR0eERfMHJrVHExSVR2VjhvaXMyNnN1YTBPY1FrLUxWVWtrRmMzTDMtN0RPUlB4RGI4dW9uODFLRVNRWmh4Vk4zZ3dLSmFSTVZHaEJsbjVOQk1jUHFyeEFUeXRjMm5VY2J4UWlRZXVWWnNWcGZwajNrVDlqWmNEMHVJQW5Tb2ZMQjNIUDREZ0M1NE13?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxOaHExV3laWFhjQ1o4WFdDUWttdkxGckxUVkVtemV5dFcyYm5BMWNQbUJuR2Ezb2QxcVY4YmNLajBVbzhEX3lwMWRYUU5uQjdSdVJFM0stMjdWV3ZlWlFGZmNwZTZ4M3hBaWFXNXNPVE1sbE8yT0t6QTJCUTFMNU1ralNybjkzaU5KcUlCYUFFbHVLRG5MYjdQVU5PeVY5RFRheWlKVg?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxPQVhxWWp0SU9TOVVGLWQ1azhrbXlnVng0QjBUNzhXS3J1Q1FSU3F4dG1ZYzlzaW0xa3I4M3FoNzVsazV4TTNCRHNOb3BNUHQxVjRRZ011a3licEdIZmdsLUdVVGVJdjZWdlp5X251Q1VhdnZETmFYa3BURGtjenZiX0dqZVZFUkREd29XNkNiM1RuR3l2Y1Q5VE9JRzZ3NEdDY1cxLWRQQlJtTFlzdjk2NzZicThkeFIydzduVjlWUXhKdXNRZkFXbHdUc2pyVnpaaTVMOWR1SQ?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxPRGhfT1h2VHNtYVlES2FYa3lSdm40WmcxQ3d3TGl2bG9xZG5KbHFYeHlqZ044TEFjUHNZZDBvVjZxc3ZxdGxKQ18wc1lXNjVXZzItMUt2Ym50X1lfWk84eXJneUpZYUtIVEdwZFN0SlBXbnpPUWdnNmxPUGVBRDI2amdTUDdOU1Naal9ocl9iSlQ2TkJkVl81ZGlnaTFpcWRFX05XZDl2VzVhcXE1?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxPeUN5R2Q3c0phcFFzd1RVbnRCNzlFdDZkSXhFdERNTmg3Sjl1S0pXOWRQVmFSbkdYbHJHSFJxZDFYOUNSclFlUElEVzlobGRRbWpZNWdCMjdaTGFIS1BGWEctejBfOHR1clUtR2RzYWpDek5ldjZVdzRRSDJoZ28yNW1MQ3RsWFN1cEs0c1Vpb3V2WlBCa3VZSTBTbHo1aWlTamhxQ2k3eWZ3ZTg?oc=5
- https://news.google.com/rss/articles/CBMihgJBVV95cUxPWHNvMF9Dd0hVZ19jbHZ3T1NBcjFXYVBNMlYtWlNWRDZGQ0ZEcVd0UmduSU01UHY2V0s4V2tfMWZRVlNPUFJrbl9hM0FyMHFJaXpiQm9yb3NiLU9GbnAtdG84M3FZblYyMWFUNVBtSk45Vnc4UzR4YmRiRHRxVG1JNnhONFhKa2xDQVRIeDBBaTFJeURhRzRSZFZKdXF4N1lnbGZHTHhWek94UXgzVjVqMDdKNXlpbkdNZ1pBajQ1UTJpUWNTVVFrdHVRczRmdFJ1cWNkVm9iZ0owNnk4SjBqajRxa0FSY3djOTlYVVZ5NGxGNUpYYjhtNEtzZy03RUpzZF9PdTB3?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxQVEFzN2F2VkNPUDg1a1NLQTVQRDNfTmI2dkE0ZEIycVpndEk1bk5xRVdWT0Uyenc5bTVsNE9LZlJ5Uk1iRFBLZVBmcTFwUzd4TTB5WVhPZTBkdS1CcjVubTFPMl9JY3RsYkREaHlKeXZRcUc5VVRCRFBOOXlCeTJvZ0dVbF9wMUU2WGZGUTVmNA?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQaGlPZGhsSnpuOEdtUGprWUxqS3FDQlhLV2w1R1JTc2VGczdyeUZQa0tjTVpEb0NaV3Y0OTRZS2E4U0lXU25qZk5ndWNocFhKZmQzNGJiUkRORFFuZXAycTFrYUw5SjVSdmNiVmdTZkl2czhEM243LU1YZ01JQ0kyX0xrZkFwOU9TeHFkNkxmLXM3bXp0VWZYc0lNYUM?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOUkdEaEF0ak9TekxtY0NRZ09KWURJNmRjSVdVaFd2blgzX2FDQzB0REtiNGZVbVA5bzloeWFEV1JXS1EyN3NuMTRmbkhsN1dpb2xvaG5aLUhCTUhmMmxxdUw0TElMcUVUaGV4QTlYMkdsaVJzYVh4ZkhzQ3BkZm5fWGlTUm4yQ09td2tVS2JmUGtfcjRpeG9Vb3Rn?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxQLU5wYVlGTzVOQ214NVN2WWNFaFRSQmFneEFQTGxHYkZzNy1fUFU4MHMtR09YWXVKV3ZqalpBNHFjRVFqaHR5ejU3cGMydVcxN3lidGJrelF3bnNpWHljbkE2anl6UFI0dmNTRXcweXN5b0dRX3o4T093a2YtMmNRRkxoMC1KZFVsVWF4bUcxTkFXSFRVYTNybzFwd25QZ0lDcGJYcG1fTFo5NHRDSXc?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxQUlVPelRWV2tMYjlhR1Z5bl9BMTc4dDdkWUFleElyeDlFbEQxekItTEh3NHhyVmxQbEx2Y01LXzVMWG9MR094U2hMS2lyUU9tM2Q3YmdLUGZybnZKX0R6M1RRaThSWms0OExFQVpoSHN1TVZMMXFrQ3pMUXdLdU5TWUdaTlFqZ09XQnhfcmoxUW91UkxfaDBYS08yVE9RQXdDbGxrMkFHT1ZWU1hXbjRwcQ?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxPT0s2ZFZUb0pqQVhOWmJhem81bkdWenZqZUpTbGpncHdiNW9aNHpFd004dVFIUDVRb3ZPVmMwZnhnUnlqYUxVUEkzNXlHQXRqdGJzY2k5T2Eyd1VkQ01EQUMwU1RjSjJfYVhqV0YtX0FvS3JnTUROY3lvQ2ZqS3BsZ0dzX001VmdsaFVHd0dzUmJ4MnppZTVNWWV4WmY4SnV0M0x2TnlsMTE5Ty1lMkViZkNQV1JpUQ?oc=5
- https://news.google.com/rss/articles/CBMi8AFBVV95cUxPNW5IYW5ubWZhdEw3S09KeC1xWUZKZzlmMW9ORFR6R01hY2p1MlpmZHpleVRKN3hwcmRQTWJicFhDYkJ5OC1IX1pBSDZfVDNETHB2Z1BaUUV5QVZhaFF1RXF3NGdLZ3JZcHVLeTIyMnFQb3hud2tlT2RoMU9uMlEyOEVpbW5jOE9xQnBYYnVnYVRpLVlESk03TTczN3JMYjU0SjJUU1pxQ2tYVTIzUHJBWU9VTEVEVzVwY3RGTkZUcmRGWVhGUUlPTEpNTlYyUEZnRjhWdXVDU2xJenE1dFNtVlZxc2RfWGctYnc2VUZndV8?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOQ2sxNG5QZzRDR2p4dXFBd3pUVXZOZHpWRFlNc3hEVGhoekpZMnItWnc5TnFBMUQ5VnRPQlV4RzJTNkZBeDVXNnVtekQ3UHM3X1NOOVpTVmRUSzUtSFdsd0w0dTJYOEhENlhjN2o2X2xhRi1KYVFYOFdLTWp1S1BsTmJ1V3JRWnVsX0g4cjd4d2dWQ2phMlQyZFZ5c09vUQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
