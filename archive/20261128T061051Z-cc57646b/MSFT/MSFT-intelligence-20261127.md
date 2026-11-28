# MSFT Intelligence Report

- ticker: **MSFT**
- Report as_of: **2026-11-27**
- Market data as_of: **2026-11-27**
- Quant sources: https://finance.yahoo.com/quote/MSFT/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MSFT/key-statistics/
- AI analysis snapshot as_of: **2026-11-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-28T06:25:34.396099+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 4, 'ai': 8, 'unknown': 0, 'irrelevant': 12})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261127T063646Z-c0c26981/MSFT** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 14 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 16.67%; oldest publication 2026-11-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 492.8500 |
| Return 1D (%) | 0.5960 |
| Return 1W (%) | 1.7192 |
| Return 1M (%) | -7.0630 |
| Return YTD (%) | 2.7532 |
| Return 1Y (%) | 2.3553 |
| Annualized volatility (%) | 34.0707 |
| Beta vs SPY | 0.9265 |
| Max drawdown (%) | -27.9702 |
| Sharpe (rf=0) | 0.1965 |
| Downside deviation (rf=0, %) | 21.8565 |
| Sortino (rf=0) | 0.3063 |
| Historical VaR 95% (1D, %) | 2.8549 |
| Historical ES 95% (1D, %) | 4.1000 |
| Correlation vs SPY | 0.4085 |
| Tracking error vs SPY (%) | 31.1182 |
| P/E (trailing) | 25.72 |
| P/B | 7.78 |
| EV/EBITDA | 18.13 |
| Revenue growth (%) | 18.80 |
| Forward P/E (estimate) | 20.34 |
| Gross margin (%) | 67.66 |
| Operating margin (%) | 47.10 |
| Return on equity (%) | 34.22 |
| Free cash flow yield (%) | 0.08 |
| MA50 | 518.5656 |
| Close vs MA50 (%) | -4.9590 |
| MA200 | 443.6882 |
| Close vs MA200 (%) | 11.0803 |
| RSI (14, Wilder) | 40.6478 |
| MACD (12,26) | -8.6531 |
| MACD signal (9) | -5.0469 |
| MACD histogram | -3.6063 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MSFT': 291, 'SPY': 291}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 492.8500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.5960 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.7192 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -7.0630 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 2.7532 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 2.3553 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 34.0707 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.8565 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.3063 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8549 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.1000 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4085 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.1182 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.9265 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.9702 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1965 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 20.3423 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 67.6570 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 47.1040 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 34.2210 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.0818 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 25.7229 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 40.6478 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.6063 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -4.9590 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 11.0803 -> Clearly above the moving-average trend level.

## TAILWINDS

### Microsoft Stock (MSFT) Rises 0.7% to $496.13 (Nov 24)
- Summary: Microsoft Stock (MSFT) Rises 0.7% to $496.13 (Nov 24)
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxQM0luQzAyX0lFeUV4bmJjZk9IRk94QlJyQms0OTl1SXpmeVBaSDdkcmJqVXF3YzhSZHJVY0xmeC05SlBld1RmbUg3N2ExaDhQa0thLUF6VXVjeDg2dEpQckJaSzhnV0ZDTWdTTzdrY2JyRVRJQndfQVdMdUdRRTlLa1FuLTM?oc=5>

### Microsoft (NASDAQ: MSFT) Stock Price Sits 11% Below Record Highs Despite Monday's Nvidia-Driven Tech Rally
- Summary: Microsoft (NASDAQ: MSFT) Stock Price Sits 11% Below Record Highs Despite Monday's Nvidia-Driven Tech Rally
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi5AFBVV95cUxQWk9fMnlSS3RJREZlVExGelNuS0JSNm50Y2EzWHNMNDlMWDNRdV80OXdqRnFNMmJUcEJ5X2VRMDk5Ml82VGs1UUVHalpuYXFDU2lTOVBsU0Y3bUNXV0RuTk5nOVRoajlManhuLVV0eUR4eW5Qai1HY3lGRFBKZnhkRGpRSkdYY2Z5UWRXZUlidWhEajU4MnVuU0ExcjlaQjdIekJkcE9vNm16R0ZkUEpPSTJERi1rXzhMaGJtM1J2d3MzVzZFSmxUY0xMVnpPZ2xOcDdpaDFFQWRwVGdRZzZZbEFoYXo?oc=5>

### Microsoft (MSFT) Is One of the Safest Ways to Own AI
- Summary: Positive view on MSFT as a safe AI investment.
- Date: 2026-11-25 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxPWmxUMFRHUzFVUVB2dnBUWEZPMGF5NGZXZG5FNnhXRF9lMDRaOGpuRmU4MHhaTUM4X09Ba1Zmb3AwNGhWMS0ydXJGQk9xcUdfbnZoODZha1AxQnF3QmxhU281QUE0cDVfaGx0T1FxckpyX25sbkVkcmpXUHZrWHNmZXVUR0hVX3pxdFlnX3Z6Z2Rmcy1tWGdFTXpxY0ZSTkxfdk5ldXBHZzdZdGJTWms2bW1PSjMyZElLb09WUDgtZjRYWk5mTFRyZDhfTy1CaVNMNGNj?oc=5>

## HEADWINDS

### Microsoft Stocks Fall 2.53% as Hyperscalers Join AI Selloff
- Summary: Microsoft Stocks Fall 2.53% as Hyperscalers Join AI Selloff
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxPUlNuenNyci02QTQtcEFiaTFad2ZGUTFiWXdqaE90d183SVRCVF9iWFBHRFRsd2lvejgtb3JiYTRTdFpuZ0M5NzFUeEJ6ZEpkNUlmcTE1ZlhkU3hVYURhSFR0SkxfSFJpSHFuQmxudjQwdUdvR0RiTVJOYmNVVkcyZmxnZ1U0dWNYUGM1cjBmcnhITkxVRWVldEthT2JxS3Jxd1FRNkI3eEh4NkZrQ19iV0J3U1NRMHdXVmc?oc=5>

### Microsoft Stock Drops Over 2.8% Amid AI Spending Concerns, Trump Tariffs, and Cloud Outage
- Summary: Microsoft Stock Drops Over 2.8% Amid AI Spending Concerns, Trump Tariffs, and Cloud Outage
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxPeFRPVG9rYUVPNmlLOUtjRjB1a3RCbWVJWWNNS0ZwZEpOUDdrOWtUdWlFWjJrRGw1UEhkenMxRFZlVU5ZQlRrZFQxbXpESmcwTVRQeEJGNkd6SG1GbEVWakk0Z256OG91YVlGTGQ1LWlNTzc5SmdtSGJGQ3JKczNYX2RYenowM1RJa3Bhc2JEd0Vud2VnQW1DZzZHeXNKTVBpemFQOHE3Snpnc21VUk9pSjlRdHE4RTlDcUpjdlRB?oc=5>

### Microsoft Corporation (MSFT) Is Facing AI Spending Fears: Could Its Cloud Growth Change the Narrative?
- Summary: Highlights concerns over AI spending impacting cloud growth.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPSHhZLXZ3QWQ5eFRidGdBVDBfeXYteFljWGQ4Uk9PRUxaOHlNWWVXSzdmOVRyX0pmSm91dWV2SmRZa3pGMHpvQjcxTldsd3hSS1pwVWxtclYxUTNOc1hHZkZYa3ZteFlaakJKNGRwUkJaYVQxdUs0c2V1RjEzOU1yUnA5aWN3a0pFUzhBbHZQVWNvd1FUWXNKV1BNZ3dPMm8zWlZn?oc=5>

### Cloud Outage Might Change Microsoft (MSFT) Stock Narrative
- Summary: Potential negative impact from cloud outage on MSFT stock.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxQYXNEWnh3XzhqWl9sLVhaekhvbjNsWnM1WHZUSzk1aHBubjR1ZEN4b21oaGNTejgzY3RHTzNmZ3ZrTGUyQWR4TmxXOXp4Zzl2RVNBWTB6VTIwWmc5V1YyZkd0cU0yUEFtam5FTWtlLS03blY0QXRLajJnQ1ZmcE12dU1SNEt6ckFVSi02S2pTZ2hfWUlnb3FYbmh1eEpCQkUtbGNPYUZvRzRRYXoxU0NzZjZ2VmNlejIzUFVzQ1R6YjJ3a1RfbVcw0gHHAUFVX3lxTFBhc0RaeHdfOGpaX2wtWFp6SG9uM2xaczVYdlRLOTVocG5uNHVkQ3hvbWhoY1N6ODNjdEdPM2ZndmtMZTJBZHhObFc5enhnOXZFU0FZMHpVMjBaZzlXVjJmR3RxTTJQQW1qbkVNa2UtLTduVjRBdEtqMmdDVmZwTXZ1TVI0S3pyQVVKLTZLalNnaF9ZSWdvcVhuaHV4SkJCRS1sY09hRm9HNFFhejFTQ3NmNnZWY2V6MjNQVXNDVHpiMndrVF9tVzA?oc=5>

## CATALYSTS

### Microsoft beats earnings estimates and lifts dividend: Can MSFT sustain gains?
- Summary: Microsoft reported earnings above estimates and increased its dividend, potentially supporting future growth.
- Date: 2026-11-24 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxONWdLNmU3ckxKNHE2MUk5ZFdyZ0p1cmlRcjhsUHI4YktvcWN3S2wtb09nT0pZdElRMnVUa3Ewc3FoMU1FTGkzd2FuSlNIVEN0UVVyREFpejFmdTBBSEg1eDdLY2ZjZDljdGNzeVRqVkc3VmtCUkNLRnd0azlXc1hOaGlKNU1ON0lLOUNJTTdGU01tQjNrOWc?oc=5>

### Automation software stocks Q3 teardown: Microsoft vs the rest
- Summary: Analyst teardown compares Microsoft’s automation software performance to peers in Q3, highlighting strengths and weaknesses.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxOSy1sbjVvN19tRktuWFVXeGkwNzNPdThrUnFDOXNJVlNvNE5PeEstN2FITmlRN3VDTXRDZFZOSzU4VFF1aWU1S1pLRHBKWDhvMG9fZ3d3RmR6VkQtWk5tbnpFbldxb1VWNXhTWVQwQkxGU21FNHZOMHdrMWt4cnEwc1BvT3FsQXpqQmR6UG14dnlNdXFHTGh5R05tMWpsUjdjODh5bHZzcmotbEZEbmhmekp5ZnU2d2VFaXdZ?oc=5>

## RISKS

### Is Microsoft Stock Worth Owning as AI Capex Weighs on Free Cash Flow?
- Summary: Examines AI spending impact on MSFT's free cash flow and valuation.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxPYTFrRzFPS2FrbHk2TjJGR1NvdDd5eGFyd1o3bjY1blFYU045bElKUGQwUHpNWHh5SEszU0p2SkwtS1VDUE8zdWY5aFhvaWQ3ZHV4T0tWOXR0U3FjTndpM1RMQTRNZjk1My04OGFMTW9HejRVcWdkR2RoOC0wZGFkQzNOZ3FrSml5OVNzZ2JnajBGRlZzOWRPWmF5dlRONm9MTDQyb2ZHUGdSenB4T3psNlZUb0cxeTVvSFFjaEVZOERadw?oc=5>

### Can Microsoft security overhaul pressure MSFT further?
- Summary: Considers potential security challenges affecting MSFT's operations.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPSE9HM1NZQmg0V2lmLTRCcnFVS1RMcDdiV3AwVmVlbi1KSVo4dmYxbUtvMGdsamxvVkd3OXdkV1VlN3RrUUw0eWczRlZ2SnhkbGpkWFFKU3ZzVkIyaXp1bmVscUR3THBXOENZS3M2QXlGeXktb0JKZWQyTDlzZlVsLU53OFNwV2kzQzF2Tjk0NmpCMG9UeUE?oc=5>

### Why Is Microsoft (MSFT) Down 7.6% Since Last Earnings Report?
- Summary: Shares fell 7.6% after earnings, reflecting investor concerns about performance.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNNHFVMmZSRUw3SnZ0YmZrQmlXcjFOWFQ5bi10U1pKSlR3ZlZYNWN3dkZZSnh5bHJlX2xSaFJvdWR1WW9xcjAxTXZ4U0NKcDFGaXAxZHo3aHJrQ3VkUmJwdmY5YnZpTkJLYlV4d2g3aG5kS1NHTzFKTVJSb0JtMWFBT1ZwMjBVVWtzX2lqbHZmMDlWTnV0?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MSFT** | **25.72** | **7.78** | **18.13** | **18.80** | **3,660,000,002,048.00 USD** | **2.36** |
| ORCL | 16.79 | 5.24 | 13.40 | 29.60 | 334,000,062,464.00 USD | -47.03 |
| GOOGL | 14.36 | 5.13 | 17.70 | 24.70 | 3,380,358,152,192.00 USD | -13.84 |
| AMZN | 20.54 | 4.48 | 15.99 | 12.10 | 2,747,834,564,608.00 USD | 10.89 |

Peers fetched as_of: 2026-11-27; MSFT reuses existing data (market data as_of: 2026-11-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-28
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-27

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-28
- Revenue (latest available single quarter): 19,953,000,000.00 USD; period 2010-10-01/2010-12-31; fiscal year/reporting period 2011/Q2
- Net income (latest available single quarter): 36,629,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2027/Q1
- SEC link: https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMihAFBVV95cUxQM0luQzAyX0lFeUV4bmJjZk9IRk94QlJyQms0OTl1SXpmeVBaSDdkcmJqVXF3YzhSZHJVY0xmeC05SlBld1RmbUg3N2ExaDhQa0thLUF6VXVjeDg2dEpQckJaSzhnV0ZDTWdTTzdrY2JyRVRJQndfQVdMdUdRRTlLa1FuLTM?oc=5
- https://news.google.com/rss/articles/CBMi5AFBVV95cUxQWk9fMnlSS3RJREZlVExGelNuS0JSNm50Y2EzWHNMNDlMWDNRdV80OXdqRnFNMmJUcEJ5X2VRMDk5Ml82VGs1UUVHalpuYXFDU2lTOVBsU0Y3bUNXV0RuTk5nOVRoajlManhuLVV0eUR4eW5Qai1HY3lGRFBKZnhkRGpRSkdYY2Z5UWRXZUlidWhEajU4MnVuU0ExcjlaQjdIekJkcE9vNm16R0ZkUEpPSTJERi1rXzhMaGJtM1J2d3MzVzZFSmxUY0xMVnpPZ2xOcDdpaDFFQWRwVGdRZzZZbEFoYXo?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxPWmxUMFRHUzFVUVB2dnBUWEZPMGF5NGZXZG5FNnhXRF9lMDRaOGpuRmU4MHhaTUM4X09Ba1Zmb3AwNGhWMS0ydXJGQk9xcUdfbnZoODZha1AxQnF3QmxhU281QUE0cDVfaGx0T1FxckpyX25sbkVkcmpXUHZrWHNmZXVUR0hVX3pxdFlnX3Z6Z2Rmcy1tWGdFTXpxY0ZSTkxfdk5ldXBHZzdZdGJTWms2bW1PSjMyZElLb09WUDgtZjRYWk5mTFRyZDhfTy1CaVNMNGNj?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxPUlNuenNyci02QTQtcEFiaTFad2ZGUTFiWXdqaE90d183SVRCVF9iWFBHRFRsd2lvejgtb3JiYTRTdFpuZ0M5NzFUeEJ6ZEpkNUlmcTE1ZlhkU3hVYURhSFR0SkxfSFJpSHFuQmxudjQwdUdvR0RiTVJOYmNVVkcyZmxnZ1U0dWNYUGM1cjBmcnhITkxVRWVldEthT2JxS3Jxd1FRNkI3eEh4NkZrQ19iV0J3U1NRMHdXVmc?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxPeFRPVG9rYUVPNmlLOUtjRjB1a3RCbWVJWWNNS0ZwZEpOUDdrOWtUdWlFWjJrRGw1UEhkenMxRFZlVU5ZQlRrZFQxbXpESmcwTVRQeEJGNkd6SG1GbEVWakk0Z256OG91YVlGTGQ1LWlNTzc5SmdtSGJGQ3JKczNYX2RYenowM1RJa3Bhc2JEd0Vud2VnQW1DZzZHeXNKTVBpemFQOHE3Snpnc21VUk9pSjlRdHE4RTlDcUpjdlRB?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPSHhZLXZ3QWQ5eFRidGdBVDBfeXYteFljWGQ4Uk9PRUxaOHlNWWVXSzdmOVRyX0pmSm91dWV2SmRZa3pGMHpvQjcxTldsd3hSS1pwVWxtclYxUTNOc1hHZkZYa3ZteFlaakJKNGRwUkJaYVQxdUs0c2V1RjEzOU1yUnA5aWN3a0pFUzhBbHZQVWNvd1FUWXNKV1BNZ3dPMm8zWlZn?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxQYXNEWnh3XzhqWl9sLVhaekhvbjNsWnM1WHZUSzk1aHBubjR1ZEN4b21oaGNTejgzY3RHTzNmZ3ZrTGUyQWR4TmxXOXp4Zzl2RVNBWTB6VTIwWmc5V1YyZkd0cU0yUEFtam5FTWtlLS03blY0QXRLajJnQ1ZmcE12dU1SNEt6ckFVSi02S2pTZ2hfWUlnb3FYbmh1eEpCQkUtbGNPYUZvRzRRYXoxU0NzZjZ2VmNlejIzUFVzQ1R6YjJ3a1RfbVcw0gHHAUFVX3lxTFBhc0RaeHdfOGpaX2wtWFp6SG9uM2xaczVYdlRLOTVocG5uNHVkQ3hvbWhoY1N6ODNjdEdPM2ZndmtMZTJBZHhObFc5enhnOXZFU0FZMHpVMjBaZzlXVjJmR3RxTTJQQW1qbkVNa2UtLTduVjRBdEtqMmdDVmZwTXZ1TVI0S3pyQVVKLTZLalNnaF9ZSWdvcVhuaHV4SkJCRS1sY09hRm9HNFFhejFTQ3NmNnZWY2V6MjNQVXNDVHpiMndrVF9tVzA?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxONWdLNmU3ckxKNHE2MUk5ZFdyZ0p1cmlRcjhsUHI4YktvcWN3S2wtb09nT0pZdElRMnVUa3Ewc3FoMU1FTGkzd2FuSlNIVEN0UVVyREFpejFmdTBBSEg1eDdLY2ZjZDljdGNzeVRqVkc3VmtCUkNLRnd0azlXc1hOaGlKNU1ON0lLOUNJTTdGU01tQjNrOWc?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxOSy1sbjVvN19tRktuWFVXeGkwNzNPdThrUnFDOXNJVlNvNE5PeEstN2FITmlRN3VDTXRDZFZOSzU4VFF1aWU1S1pLRHBKWDhvMG9fZ3d3RmR6VkQtWk5tbnpFbldxb1VWNXhTWVQwQkxGU21FNHZOMHdrMWt4cnEwc1BvT3FsQXpqQmR6UG14dnlNdXFHTGh5R05tMWpsUjdjODh5bHZzcmotbEZEbmhmekp5ZnU2d2VFaXdZ?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxPYTFrRzFPS2FrbHk2TjJGR1NvdDd5eGFyd1o3bjY1blFYU045bElKUGQwUHpNWHh5SEszU0p2SkwtS1VDUE8zdWY5aFhvaWQ3ZHV4T0tWOXR0U3FjTndpM1RMQTRNZjk1My04OGFMTW9HejRVcWdkR2RoOC0wZGFkQzNOZ3FrSml5OVNzZ2JnajBGRlZzOWRPWmF5dlRONm9MTDQyb2ZHUGdSenB4T3psNlZUb0cxeTVvSFFjaEVZOERadw?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPSE9HM1NZQmg0V2lmLTRCcnFVS1RMcDdiV3AwVmVlbi1KSVo4dmYxbUtvMGdsamxvVkd3OXdkV1VlN3RrUUw0eWczRlZ2SnhkbGpkWFFKU3ZzVkIyaXp1bmVscUR3THBXOENZS3M2QXlGeXktb0JKZWQyTDlzZlVsLU53OFNwV2kzQzF2Tjk0NmpCMG9UeUE?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNNHFVMmZSRUw3SnZ0YmZrQmlXcjFOWFQ5bi10U1pKSlR3ZlZYNWN3dkZZSnh5bHJlX2xSaFJvdWR1WW9xcjAxTXZ4U0NKcDFGaXAxZHo3aHJrQ3VkUmJwdmY5YnZpTkJLYlV4d2g3aG5kS1NHTzFKTVJSb0JtMWFBT1ZwMjBVVWtzX2lqbHZmMDlWTnV0?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
