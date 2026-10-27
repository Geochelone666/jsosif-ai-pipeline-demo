# AMD Intelligence Report

- ticker: **AMD**
- Report as_of: **2026-10-26**
- Market data as_of: **2026-10-26**
- Quant sources: https://finance.yahoo.com/quote/AMD/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMD/key-statistics/
- AI analysis snapshot as_of: **2026-10-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-27T02:13:55.436630+00:00**
- AI status: **Partial: 1 headline remains unclassified and excluded from research conclusions**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 3, 'ai': 9, 'unknown': 1, 'irrelevant': 11})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261026T005504Z-6368ad31/AMD** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 11 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-10-21

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 531.2800 |
| Return 1D (%) | 2.8039 |
| Return 1W (%) | -1.2582 |
| Return 1M (%) | -15.7541 |
| Return YTD (%) | 148.0762 |
| Return 1Y (%) | 110.0585 |
| Annualized volatility (%) | 68.0980 |
| Beta vs SPY | 3.2291 |
| Max drawdown (%) | -27.7608 |
| Sharpe (rf=0) | 1.3975 |
| Downside deviation (rf=0, %) | 42.8893 |
| Sortino (rf=0) | 2.2189 |
| Historical VaR 95% (1D, %) | 5.8677 |
| Historical ES 95% (1D, %) | 8.2198 |
| Correlation vs SPY | 0.6030 |
| Tracking error vs SPY (%) | 61.2760 |
| P/E (trailing) | 135.53 |
| P/B | 12.90 |
| EV/EBITDA | 89.78 |
| Revenue growth (%) | 50.10 |
| Forward P/E (estimate) | 33.72 |
| Gross margin (%) | 55.72 |
| Operating margin (%) | 17.25 |
| Return on equity (%) | 10.20 |
| Free cash flow yield (%) | 1.02 |
| MA50 | 542.6172 |
| Close vs MA50 (%) | -2.0893 |
| MA200 | 403.7163 |
| Close vs MA200 (%) | 31.5974 |
| RSI (14, Wilder) | 42.8880 |
| MACD (12,26) | -10.9911 |
| MACD signal (9) | 1.0135 |
| MACD histogram | -12.0046 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMD': 268, 'SPY': 268}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 531.2800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.8039 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.2582 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -15.7541 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 148.0762 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 110.0585 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 68.0980 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 42.8893 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.2189 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 5.8677 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 8.2198 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6030 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 61.2760 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.2291 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.7608 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.3975 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 33.7196 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 55.7240 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 17.2500 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 10.1960 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.0194 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 135.5306 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 42.8880 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -12.0046 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -2.0893 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 31.5974 -> Clearly above the moving-average trend level.

## TAILWINDS

### Advanced Micro Devices (NASDAQ:AMD) Stock Jumps 2.8% - Here's What Happened
- Summary: Advanced Micro Devices (NASDAQ:AMD) Stock Jumps 2.8% - Here's What Happened
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxNLTc4TU5CWlhhblhmMUp5WnBZSGRfdnBLWGdabHFXQnNfUjBKOHdGeDRmVjBfY3cza0ZPZ08tRFFkQjNPbHlsV2gwTGlTOXVOSDZzcjVVN1JSdmZhdHVOZHNDOEs4NWpLaXdBTzVlUGNHR0JGektpT2t2Rm5IXzRKcExZR2I2Q3FTenJJQTFSdzBMX256b2xTbDVIU1ZqdHhLbGVNc3VYNWlrWHFLSllpaWFwZFZ1UmQ5eXNUdGJNbVR6c0FSMjBv?oc=5>

### Dell, Lenovo, Cisco, HPE, Supermicro: Why AMD’s New AI Blueprint Has Everyone Signing On
- Summary: Major PC and server vendors adopt AMD’s AI blueprint, boosting demand for AMD processors.
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNWXB6a3d0Yml4a2t1bHNKNTZkZ3B4SEpqYjgyN0JHcTJBTVQ1NUJKMjg0V3pnWERNSjJHVS1QUHdZZ2xOVUl1MVNraGJrd1ZULTlyaW5ObnB4Vko3R013Tkx3bUZzRzFBVThNLVcweGx4dTA2SC1MSzFtd0xXUUc1QnVtX0RyZjl1MTd5bDJTcFBXcGZidFl6d3dQdDI?oc=5>

## HEADWINDS

### AMD Stock Rebounds to $516.79 Ahead of Q3 Earnings After Lam Research Warning
- Summary: AMD Stock Rebounds to $516.79 Ahead of Q3 Earnings After Lam Research Warning
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxPQnpLNXB2bnRKUGNYb3VyYWlFRHVySjM3R2RnQktRcnVHM1FQRi1wVW5kei1JY3R2eDduRlk5ck1sYTRyZGk2U0x3ekY4MWhvTGxUeUMxano3M0E5VlVWNjdyTzVLN205RTdmTE5mcElybTdzbldjQ3c1QWFzdWZaUWdFMlktRGNrVE9DT2tmbFlLd1J6Y3NlbEZpbDNlTWNNWm9SdHdNSk9GWWpXWGhseThqbWR6aDJRUzJR?oc=5>

### AMD pulled lower by tech slide, falls 8% (AMD:NASDAQ)
- Summary: AMD pulled lower by tech slide, falls 8% (AMD:NASDAQ)
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxPY2lkd3hiVjE5em5HUHJFQXlMT1h6TU5mUWpNbVVmc0J5a2Jvc2pkVHkxellvSFZtb3FSdEpDWVBBV2lmLUtEODFkUWVuWmxrX291STAzWjlBc3NKNThCR1lZVGdCUzdXMS1adFhOVXgyTGlUVG5NV2xjNVRoV05wRVNn?oc=5>

### Advanced Micro Devices (AMD) Stock Plummeted 13% Last Week. Should You Buy the Dip Before Nov. 3?
- Summary: AMD shares fell 13% last week, prompting a dip-buy question.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPUlVoTFR4akRJeFNUaVJlU2VDcEktX3ZCc2ZGaWladVNjaVZtdmFXOVNqdlVOU2ZvQnV1dVVYNXNYeUh6dFJGdFV5bjc2NTFDOFJjblpQM1NkMHZzTGExcTdNV212RUQ1VWdLQUI2MnpTRWx6TmRDbXB3VTRoald6c0JDZ0lLZUpSRWZEOUtVcUhza3FGOUhz?oc=5>

## CATALYSTS

### Advanced Micro Devices (AMD) Rises Higher Than Market: Key Facts
- Summary: AMD stock rose above market average, indicating positive investor sentiment.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNZzYtRE1JWERFWUdyTHdsRzdScUtHN3ZQRHlyZ3B2WW5qU3plWk9JWXc5Um9FZlJvOU03MkhKSFBnV2pCUTNqZjBvaVQ4eXJkamNnd01VNFp3MFZRY1M3R1VSNmlLNVNBa1pNclozc0FtU190NnV1U1ZpNlNGbWlVc3VXSkJNbGEzMTAtaEdtX1R5NWZOUjFFUmgtaDU2dw?oc=5>

### Advanced Micro Devices Inc Stock (AMD) Moved Up by 3.03% on Oct 26: Drivers Behind the Movement
- Summary: AMD shares increased 3.03% on Oct 26, driven by market factors.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxQSGpYQ29SQVJscUNkYWRMdjRnN2ZGUnBfYTFaRENTbUJuMDZOaTlFbHJMVl9MRkd6MzBtcTQ1R1dXbFU5ZXpnMVVmbGZhQ000aE56Uk9OT1FZb1VFZ3lqOElaU0pOVUhVeDU3S3NHVC1qMHhqMENyemxsT0RpNDcxZHdiTnVvbE5hNmc?oc=5>

### Why AMD Stock Fell on Thursday
- Summary: AMD shares declined on Thursday, reflecting negative market reaction.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTE1DZ3llMlpDb3RCZVFiWlkyNkp6cDZXenZLYmdvOE1RMWFuemJnUUN4RXZEcS1PUDBtVmJadjZmNmtDa1NfMWtmSW1VQXZ0WHVjZXdBQlZ4U3NvYWpzWFZMUGx0VFB6VV9ZQzJ0aDBIVDUxOXl4S3BNcWRTSmFPUQ?oc=5>

### AMD Q3 Preview: The Market Is Watching OpenAI, I'm Watching EPYC (NASDAQ:AMD)
- Summary: Preview of AMD Q3 earnings, focusing on EPYC and market expectations.
- Date: 2026-10-26 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNY3IzX3Q4eEEzdVBuN0p2WEpQYmtOQ0hYV2VXV0hFejZnRUlLT1c5bnMwbmtiYXRxT1dGZUUwajFIMVNxR2o4UDlaeFJVVFZ0aEJiOXVQMGthWjhMR2pZQWJ4M3RhZTBKV0JjYmViX3RCWVJaMnh3YjhYcy0xaXd5S2w2QmttNzBNczhQYlR4ZU1UVmZDQ01WR3F3SHlnOWdYZGxQYg?oc=5>

### Advanced Micro Devices (AMD) Sees $332.1 Million in Net ETF Buying on Oct. 19
- Summary: Net ETF buying of $332.1M indicates institutional support for AMD shares.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNNk5ReEZ3dVdtWGtjdFRpd3BWbkhpUmhtalZKUDEyWmVuc2k1QXRZSTR2MjlkTnE0ejJ0ZEpPSjN0WUZhX3V6aWVMb1JYanBzU3FqU0ZQZXdJWGM3d0o5dW5KWVhVWVNGNTR2WmZwQmRFajZSejdfRWNsVHI3Z0Q3N1ZaR0NTRUZOaGRmNkZyU3BHX3BFZ1d2QWtBQXA?oc=5>

### Advanced Micro Devices (AMD) Lands New AI Infrastructure Builds In Europe And India
- Summary: AMD announces new AI infrastructure projects in Europe and India, expanding its data center presence.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNRGdLYzBDX1dqOHo0RTJNRU1BLXhpMUNsaVpjVUlMbWdKOEdSV2dSRTFBU2x6QUdmNlRES3ZqWEtTV3c0OTFoR2ZyalZLUW12b0tHTm1LblZZbWRPdjJqcmJ1VWxJeU1BQjRjZ1FpYWlyQ2dvMVltQl9Wb3lPb01vRGdaRWxYM19JckkxcXZXTE9jQ3hXRUFSMFloN1k?oc=5>

## RISKS

### 1 Red Flag That Keeps Me From Buying AMD Stock
- Summary: Highlights a concern deterring purchase of AMD shares.
- Date: 2026-10-25 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPNENhNjZRRVpLRDJfRzg4Xy03WmtTNE4xWmVxNXZQejEwbno1Zkh6SldtTzg3bHd3ZEQ0NFJ6MlFyWUV4MUV2T2c5c1BiQ2lrS3JGSnI1ektxSGRHcGNmU1I1SWFLVnFPbFY0dmpUYjZJdVpQT3BHMUhTS1ZfVnZBTGVzSEhiaHJpdURQWTB6d2ktU3M?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMD** | **135.53** | **12.90** | **89.78** | **50.10** | **867,301,392,384.00 USD** | **110.06** |
| NVDA | 27.31 | 22.78 | 25.75 | 105.90 | 5,215,751,766,016.00 USD | 16.24 |
| INTC | N/A | 5.21 | 29.26 | 25.40 | 478,233,919,488.00 USD | 136.34 |
| AVGO | 42.04 | 15.76 | 30.75 | 85.50 | 1,571,335,831,552.00 USD | -6.36 |

Peers fetched as_of: 2026-10-26; AMD reuses existing data (market data as_of: 2026-10-26); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-04
- Next expected earnings: 2026-11-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-26

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-05
- Revenue (latest available single quarter): 1,584,000,000.00 USD; period 2017-07-02/2017-09-30; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 2,297,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/2488/000000248826000123/amd-20260627.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMixwFBVV95cUxNLTc4TU5CWlhhblhmMUp5WnBZSGRfdnBLWGdabHFXQnNfUjBKOHdGeDRmVjBfY3cza0ZPZ08tRFFkQjNPbHlsV2gwTGlTOXVOSDZzcjVVN1JSdmZhdHVOZHNDOEs4NWpLaXdBTzVlUGNHR0JGektpT2t2Rm5IXzRKcExZR2I2Q3FTenJJQTFSdzBMX256b2xTbDVIU1ZqdHhLbGVNc3VYNWlrWHFLSllpaWFwZFZ1UmQ5eXNUdGJNbVR6c0FSMjBv?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNWXB6a3d0Yml4a2t1bHNKNTZkZ3B4SEpqYjgyN0JHcTJBTVQ1NUJKMjg0V3pnWERNSjJHVS1QUHdZZ2xOVUl1MVNraGJrd1ZULTlyaW5ObnB4Vko3R013Tkx3bUZzRzFBVThNLVcweGx4dTA2SC1MSzFtd0xXUUc1QnVtX0RyZjl1MTd5bDJTcFBXcGZidFl6d3dQdDI?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxPQnpLNXB2bnRKUGNYb3VyYWlFRHVySjM3R2RnQktRcnVHM1FQRi1wVW5kei1JY3R2eDduRlk5ck1sYTRyZGk2U0x3ekY4MWhvTGxUeUMxano3M0E5VlVWNjdyTzVLN205RTdmTE5mcElybTdzbldjQ3c1QWFzdWZaUWdFMlktRGNrVE9DT2tmbFlLd1J6Y3NlbEZpbDNlTWNNWm9SdHdNSk9GWWpXWGhseThqbWR6aDJRUzJR?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxPY2lkd3hiVjE5em5HUHJFQXlMT1h6TU5mUWpNbVVmc0J5a2Jvc2pkVHkxellvSFZtb3FSdEpDWVBBV2lmLUtEODFkUWVuWmxrX291STAzWjlBc3NKNThCR1lZVGdCUzdXMS1adFhOVXgyTGlUVG5NV2xjNVRoV05wRVNn?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPUlVoTFR4akRJeFNUaVJlU2VDcEktX3ZCc2ZGaWladVNjaVZtdmFXOVNqdlVOU2ZvQnV1dVVYNXNYeUh6dFJGdFV5bjc2NTFDOFJjblpQM1NkMHZzTGExcTdNV212RUQ1VWdLQUI2MnpTRWx6TmRDbXB3VTRoald6c0JDZ0lLZUpSRWZEOUtVcUhza3FGOUhz?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxNZzYtRE1JWERFWUdyTHdsRzdScUtHN3ZQRHlyZ3B2WW5qU3plWk9JWXc5Um9FZlJvOU03MkhKSFBnV2pCUTNqZjBvaVQ4eXJkamNnd01VNFp3MFZRY1M3R1VSNmlLNVNBa1pNclozc0FtU190NnV1U1ZpNlNGbWlVc3VXSkJNbGEzMTAtaEdtX1R5NWZOUjFFUmgtaDU2dw?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxQSGpYQ29SQVJscUNkYWRMdjRnN2ZGUnBfYTFaRENTbUJuMDZOaTlFbHJMVl9MRkd6MzBtcTQ1R1dXbFU5ZXpnMVVmbGZhQ000aE56Uk9OT1FZb1VFZ3lqOElaU0pOVUhVeDU3S3NHVC1qMHhqMENyemxsT0RpNDcxZHdiTnVvbE5hNmc?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTE1DZ3llMlpDb3RCZVFiWlkyNkp6cDZXenZLYmdvOE1RMWFuemJnUUN4RXZEcS1PUDBtVmJadjZmNmtDa1NfMWtmSW1VQXZ0WHVjZXdBQlZ4U3NvYWpzWFZMUGx0VFB6VV9ZQzJ0aDBIVDUxOXl4S3BNcWRTSmFPUQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQQUVweGpxUTdqakVrOUFnVUhlZWZqa1k1OWlpOU9hWUNpOElia3B4cGZ5RXJabnEwX3VaTEd3eHFHM1hqX2xYTlU5T2ZyaGJsbU96OUdJaWVLd1hfanJHektSNF95TlpHVzk5MnAtdzd4TWNneUd4RlMwTV9RcDdYVHV5MlZOckJDWHFRWlQyeW00dk44RzYw?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNY3IzX3Q4eEEzdVBuN0p2WEpQYmtOQ0hYV2VXV0hFejZnRUlLT1c5bnMwbmtiYXRxT1dGZUUwajFIMVNxR2o4UDlaeFJVVFZ0aEJiOXVQMGthWjhMR2pZQWJ4M3RhZTBKV0JjYmViX3RCWVJaMnh3YjhYcy0xaXd5S2w2QmttNzBNczhQYlR4ZU1UVmZDQ01WR3F3SHlnOWdYZGxQYg?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNNk5ReEZ3dVdtWGtjdFRpd3BWbkhpUmhtalZKUDEyWmVuc2k1QXRZSTR2MjlkTnE0ejJ0ZEpPSjN0WUZhX3V6aWVMb1JYanBzU3FqU0ZQZXdJWGM3d0o5dW5KWVhVWVNGNTR2WmZwQmRFajZSejdfRWNsVHI3Z0Q3N1ZaR0NTRUZOaGRmNkZyU3BHX3BFZ1d2QWtBQXA?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNRGdLYzBDX1dqOHo0RTJNRU1BLXhpMUNsaVpjVUlMbWdKOEdSV2dSRTFBU2x6QUdmNlRES3ZqWEtTV3c0OTFoR2ZyalZLUW12b0tHTm1LblZZbWRPdjJqcmJ1VWxJeU1BQjRjZ1FpYWlyQ2dvMVltQl9Wb3lPb01vRGdaRWxYM19JckkxcXZXTE9jQ3hXRUFSMFloN1k?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPNENhNjZRRVpLRDJfRzg4Xy03WmtTNE4xWmVxNXZQejEwbno1Zkh6SldtTzg3bHd3ZEQ0NFJ6MlFyWUV4MUV2T2c5c1BiQ2lrS3JGSnI1ektxSGRHcGNmU1I1SWFLVnFPbFY0dmpUYjZJdVpQT3BHMUhTS1ZfVnZBTGVzSEhiaHJpdURQWTB6d2ktU3M?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
