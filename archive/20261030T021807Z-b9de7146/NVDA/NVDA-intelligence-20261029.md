# NVDA Intelligence Report

- ticker: **NVDA**
- Report as_of: **2026-10-29**
- Market data as_of: **2026-10-29**
- Quant sources: https://finance.yahoo.com/quote/NVDA/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVDA/key-statistics/
- AI analysis snapshot as_of: **2026-10-29**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-30T02:32:04.928579+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 7, 'ai': 5, 'unknown': 0, 'irrelevant': 12})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261029T020157Z-688a53f0/NVDA** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'directional_claim_without_event_type': 1, 'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 11 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 45.83%; oldest publication 2026-10-26

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 213.6600 |
| Return 1D (%) | -0.7986 |
| Return 1W (%) | 0.6833 |
| Return 1M (%) | -5.9636 |
| Return YTD (%) | 14.8311 |
| Return 1Y (%) | 3.4447 |
| Annualized volatility (%) | 37.1795 |
| Beta vs SPY | 1.9246 |
| Max drawdown (%) | -20.2144 |
| Sharpe (rf=0) | 0.2760 |
| Downside deviation (rf=0, %) | 25.3059 |
| Sortino (rf=0) | 0.4054 |
| Historical VaR 95% (1D, %) | 3.7736 |
| Historical ES 95% (1D, %) | 4.5600 |
| Correlation vs SPY | 0.6579 |
| Tracking error vs SPY (%) | 30.3654 |
| P/E (trailing) | 27.01 |
| P/B | 22.53 |
| EV/EBITDA | 25.47 |
| Revenue growth (%) | 105.90 |
| Forward P/E (estimate) | 13.43 |
| Gross margin (%) | 74.67 |
| Operating margin (%) | 66.24 |
| Return on equity (%) | 117.21 |
| Free cash flow yield (%) | 0.81 |
| MA50 | 221.9240 |
| Close vs MA50 (%) | -3.7238 |
| MA200 | 203.9825 |
| Close vs MA200 (%) | 4.7443 |
| RSI (14, Wilder) | 42.2847 |
| MACD (12,26) | -2.8256 |
| MACD signal (9) | -1.7909 |
| MACD histogram | -1.0348 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVDA': 271, 'SPY': 271}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 213.6600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.7986 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.6833 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -5.9636 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 14.8311 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 3.4447 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 37.1795 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 25.3059 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4054 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.7736 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.5600 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6579 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 30.3654 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.9246 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -20.2144 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2760 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 13.4254 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.6740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 66.2370 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 117.2110 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.8104 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 27.0114 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 42.2847 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.0348 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -3.7238 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 4.7443 -> Slightly above the moving-average trend level.

## TAILWINDS

### Nvidia Reports a Big Win, But Its Stock Stagnates. Wall Street Is Worried About a Potential Plunge to $180.
- Summary: Nvidia Reports a Big Win, But Its Stock Stagnates. Wall Street Is Worried About a Potential Plunge to $180.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOTXZESlFUMlNnVnpVQmw5TUdUZEt0NTRadFFCZW9IYThsRWV4SDJoX3pKQ19HUkNRc0VLdm5LM0JoS0Y4eXVwZlNuc2FPdHNlcnF4SVJpU1pGU0UzNDJ1SnNrMHd2QUt6bDV4OWd6aGV3OUVZbG1YOXJ6Ymh4eEd2ZHFCVXdXVG41MEg2c0ZfU25qcnhNbGh5eg?oc=5>

### NVDA Stock Ticks Higher Overnight: a16z Data Shows GPU Rental Prices Rising Sharply, Even For Older Chips
- Summary: NVDA Stock Ticks Higher Overnight: a16z Data Shows GPU Rental Prices Rising Sharply, Even For Older Chips
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNVzhIbU14cHlhdjlKTUNmTkpxbXBMTXRHb2U5Wk1rMVg0dEhwX216VVJmUEhfT3l5SUtKZVB0ZU91QklIdERHMDRzSXhmcExnMmJxSUxNMUhJNmpYdEN4bUFMTXlwbjY4WjRENmZyR0JfQWMwTWxramtEVi0teDZWOUVMTUVFRjJSTGg2NjJ6eTVXYmFxWllIT1BQeHFGemM?oc=5>

### Nvidia (NVDA) Surpasses Market Returns: Some Facts Worth Knowing
- Summary: NVDA outperformed market returns, indicating strong performance.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxQdnNyZ1g4R2pVdTJTQW1HNE53cGJLSDVBbGFTUWZlOFd0akxCQUJ6SzBwWVVlaDFYZjlLdXA3TktObUZrdnJRX1lCcEFnbDBvZTliYUVCeC1OUDMtVGxhT2pvVWxnYm05UUhEUnRER1NGbFVLZmhWVG8wYVcxQ3hKRHdjdnNkMkRGWFFuRjBFRjdUeE5oU1drR3oxV2tyUUFCcExN?oc=5>

### Can NVIDIA Stock Jump 50%?
- Summary: Speculative question about future price surge.
- Date: 2026-10-29 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxOQXQyVjdJVW4xalMtNHZlclFJN1BOQkxUMElvOFZzZENuX2VCZUplTG1JdVoyZndURXhRaTN2UHZGNEVsM0FwSG41ZWR4TkFUb3VPM2R5cWp2eUw0UktEbzhqbmdiZ0tpSUVGdXA4a3lQMlhUMnlOclRTNXVXQnhZTlcwcDVlb0dDTGRtelV3?oc=5>

### 51 ETFs Add to NVIDIA (NVDA) Holdings on Oct. 27
- Summary: Fifty-one ETFs increased their NVIDIA holdings, indicating growing institutional confidence.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNSFRQOEN5a0xSdVR1QXZyRTI2cEsySXhEcHZLSzJGUldjczR2dEZIYzFtU2pBQ1dGRWFYQUd4MjJBMkdEdE9MSkg5VnBhSDQ5ZjFvMW5LNXowTUVKbWNLM1hXR2s5Q2U3ZGR2NmNMVU9XOVlpNFRqbUpGN29tMVRwcGFDNXhJa3dreDVuSUNqXzZuQQ?oc=5>

## HEADWINDS

### Nvidia Stock Has Dropped Nearly 6% in a Month; Now Jim Cramer Is Asking Why ‘Anything Negative in Tech’ Immediately Crushes NVDA
- Summary: Nvidia Stock Has Dropped Nearly 6% in a Month; Now Jim Cramer Is Asking Why ‘Anything Negative in Tech’ Immediately Crushes NVDA
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNcWZmNGZfcHpPQ3V5YWpBOV8yTTZ5OFhVbWV2M0VtLUprRzJwRllPbXVMWDVodmFoUG9wYndHZFlVdFc5Q3RIMkwzMzRGWUVhVmh0M3RURjd1VVJCRVpYbGJiTlc4V1pqTGpuWThGVFpCdXdHVWthTEUycVNybkh1STJYeUtXbFQ2YkhvYVUzdV82RFlGRXcxcGVn?oc=5>

### Nvidia stock price forecast: $204.13 support in focus as NVDA falls 1.5%
- Summary: Nvidia stock price forecast: $204.13 support in focus as NVDA falls 1.5%
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxPSlFjUVRWcUJmUUw3eXlSQ29tWTJPa2R0TlY5TW1GWGYzc2RWWTBiaTNGZzNCUnoxS20xOE9VWHh6NzhJTUZoU1F6Tm9VYndxYTVSbDVYRzcxczZsaDdpMGExVzlLT1FTVUh1aFRnTFNTUlRtZnlKNWMtaWZCUlpGVGswWlBwT1NkaHJHaw?oc=5>

### Nvidia Stock Is Down 12% From Its High. Here's What History Says Happens Next.
- Summary: Nvidia Stock Is Down 12% From Its High. Here's What History Says Happens Next.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxPcEZla1VqXzQxakdfSk52MkVWQ191TzRxSDJpSi1JMU5jUkZiNTYxQi1xeG92dnhHUDFsWjhBejM1dXNUTUs4WmVvZHFtTUw0bUh0bHVuN0hwUFJvcGdNb2FRZmRoaEtRbHd1aS1BYS11NmU3cXltVm9iZEd0N29IWVZxal9XZjg?oc=5>

### Nvidia Stock Has Dropped Nearly 6% in a Month; Now Jim Cramer Is Asking Why ‘Anything Negative in Tech’ I
- Summary: Nvidia Stock Has Dropped Nearly 6% in a Month; Now Jim Cramer Is Asking Why ‘Anything Negative in Tech’ I
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxPRmMtRmV3UmRJOVFzQ0NyS01vaVlnTTBXV01GbW52UDhNeGo4ZHNfMWNTUmE2MW1LT01Fb19xZDB6VndBOVlQTldtNFZLeXJTRDZuRndHWEVZSnIzV3FzUEZRUEFXQ0RFdnJGbnFNY0FaOUtLdDRkak40Q0hUZjkzaThiY1ZwNFYwWnNvRHNwYlpEOEk0T291Q3paTzhFTnlzODRxRXRib0t3LWVpanV2cQ?oc=5>

## CATALYSTS

### Nvidia Stock $216: SpaceX $40B GPU Deal, Bull $243
- Summary: Nvidia Stock $216: SpaceX $40B GPU Deal, Bull $243
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxOT2ZzTjNmanRRMnAxOW5GZTR0Y2hPU1NtZ29TOElBa3BfTHVlR2pCUzQ5UTBkRGtyeHhNWkhpZUlKZDN2UnRVdG1wNzdHeUhoakNhbmFaSkhBeF9vY1ZLajNLWk9mQmVSYXJjbldsYUIwYS1ycnplSnQtZ1lvVlZYV0RMcjdueXgtOUd5aEQzVER3bHh0c21MUWl6RGJzRkxfNjlmOWZsRjJpMWY0Mnp4b2NPWGJ1UjlNbm1vbQ?oc=5>

### NVDA Stock Alert: What to Know as Nvidia Invests $3 Billion in Meta
- Summary: NVIDIA invests $3B in Meta, strengthening partnership and expanding AI collaboration.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxON0JPdEc2MXNVR1UzZF8tZk00UERCQTF2RnkwU3Q0QTNXcDJ5MmtNeF94dmpoZXVTWFRydkUwb1UySkU5dEtSQ1NweGRVTUN0V2FDQU14QUIzU3Zfa2JZRTlLSks4Zm1LVWxiN1FnTzd4ZXdrZEF1VnhEeWF0LTMtWDZrNTBlSmJ1YUJ4a1dfZXAtOTBJZnJ0Yw?oc=5>

## RISKS

### Nvidia CEO Jensen Huang May Have Been Targeted by Chinese Spy Plot. What It Means for NVDA Stock.
- Summary: Chinese espionage threat targeting Nvidia CEO could impact company security and investor confidence.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxPSlhIOHBrX2pVcnVZNF9Lck5OZTgyX1VxZ1MtLXVuMGxJMVgyQUpOampMUmNWNDhCYUpGT01meXRDNUh1d2RZOXdmeU1VaHJ3XzVqcExuWEEyZEFHQ3V2QjhoWl9kNGUxNGNMSHFmVGw5S0YzVTFVaV90ekZTdVVNVE0zTHdMMjd1dFJRem5KZTlDRmdyOF9RTEUxaGpiVXE3TTNQalh4OXVrWFFWdDNGal9udHJCRnNoQU43ODJxTnR1TkRGZVRjT0RnTWZMb3RUZUJ1Rnln?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVDA** | **27.01** | **22.53** | **25.47** | **105.90** | **5,159,248,199,680.00 USD** | **3.44** |
| AMD | 144.49 | 13.75 | 95.78 | 50.10 | 924,666,494,976.00 USD | 114.29 |
| AVGO | 44.06 | 16.52 | 32.19 | 85.50 | 1,646,902,378,496.00 USD | -9.95 |
| INTC | N/A | 5.30 | 29.74 | 25.40 | 486,691,700,736.00 USD | 122.71 |

Peers fetched as_of: 2026-10-29; NVDA reuses existing data (market data as_of: 2026-10-29); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-26
- Next expected earnings: 2026-11-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-29

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-26
- Revenue (latest available single quarter): 96,221,000,000.00 USD; period 2026-04-27/2026-07-26; fiscal year/reporting period 2027/Q2
- Net income (latest available single quarter): 59,688,000,000.00 USD; period 2026-04-27/2026-07-26; fiscal year/reporting period 2027/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimAFBVV95cUxOTXZESlFUMlNnVnpVQmw5TUdUZEt0NTRadFFCZW9IYThsRWV4SDJoX3pKQ19HUkNRc0VLdm5LM0JoS0Y4eXVwZlNuc2FPdHNlcnF4SVJpU1pGU0UzNDJ1SnNrMHd2QUt6bDV4OWd6aGV3OUVZbG1YOXJ6Ymh4eEd2ZHFCVXdXVG41MEg2c0ZfU25qcnhNbGh5eg?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNVzhIbU14cHlhdjlKTUNmTkpxbXBMTXRHb2U5Wk1rMVg0dEhwX216VVJmUEhfT3l5SUtKZVB0ZU91QklIdERHMDRzSXhmcExnMmJxSUxNMUhJNmpYdEN4bUFMTXlwbjY4WjRENmZyR0JfQWMwTWxramtEVi0teDZWOUVMTUVFRjJSTGg2NjJ6eTVXYmFxWllIT1BQeHFGemM?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQdnNyZ1g4R2pVdTJTQW1HNE53cGJLSDVBbGFTUWZlOFd0akxCQUJ6SzBwWVVlaDFYZjlLdXA3TktObUZrdnJRX1lCcEFnbDBvZTliYUVCeC1OUDMtVGxhT2pvVWxnYm05UUhEUnRER1NGbFVLZmhWVG8wYVcxQ3hKRHdjdnNkMkRGWFFuRjBFRjdUeE5oU1drR3oxV2tyUUFCcExN?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxOQXQyVjdJVW4xalMtNHZlclFJN1BOQkxUMElvOFZzZENuX2VCZUplTG1JdVoyZndURXhRaTN2UHZGNEVsM0FwSG41ZWR4TkFUb3VPM2R5cWp2eUw0UktEbzhqbmdiZ0tpSUVGdXA4a3lQMlhUMnlOclRTNXVXQnhZTlcwcDVlb0dDTGRtelV3?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNSFRQOEN5a0xSdVR1QXZyRTI2cEsySXhEcHZLSzJGUldjczR2dEZIYzFtU2pBQ1dGRWFYQUd4MjJBMkdEdE9MSkg5VnBhSDQ5ZjFvMW5LNXowTUVKbWNLM1hXR2s5Q2U3ZGR2NmNMVU9XOVlpNFRqbUpGN29tMVRwcGFDNXhJa3dreDVuSUNqXzZuQQ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNcWZmNGZfcHpPQ3V5YWpBOV8yTTZ5OFhVbWV2M0VtLUprRzJwRllPbXVMWDVodmFoUG9wYndHZFlVdFc5Q3RIMkwzMzRGWUVhVmh0M3RURjd1VVJCRVpYbGJiTlc4V1pqTGpuWThGVFpCdXdHVWthTEUycVNybkh1STJYeUtXbFQ2YkhvYVUzdV82RFlGRXcxcGVn?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxPSlFjUVRWcUJmUUw3eXlSQ29tWTJPa2R0TlY5TW1GWGYzc2RWWTBiaTNGZzNCUnoxS20xOE9VWHh6NzhJTUZoU1F6Tm9VYndxYTVSbDVYRzcxczZsaDdpMGExVzlLT1FTVUh1aFRnTFNTUlRtZnlKNWMtaWZCUlpGVGswWlBwT1NkaHJHaw?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxPcEZla1VqXzQxakdfSk52MkVWQ191TzRxSDJpSi1JMU5jUkZiNTYxQi1xeG92dnhHUDFsWjhBejM1dXNUTUs4WmVvZHFtTUw0bUh0bHVuN0hwUFJvcGdNb2FRZmRoaEtRbHd1aS1BYS11NmU3cXltVm9iZEd0N29IWVZxal9XZjg?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxPRmMtRmV3UmRJOVFzQ0NyS01vaVlnTTBXV01GbW52UDhNeGo4ZHNfMWNTUmE2MW1LT01Fb19xZDB6VndBOVlQTldtNFZLeXJTRDZuRndHWEVZSnIzV3FzUEZRUEFXQ0RFdnJGbnFNY0FaOUtLdDRkak40Q0hUZjkzaThiY1ZwNFYwWnNvRHNwYlpEOEk0T291Q3paTzhFTnlzODRxRXRib0t3LWVpanV2cQ?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxOT2ZzTjNmanRRMnAxOW5GZTR0Y2hPU1NtZ29TOElBa3BfTHVlR2pCUzQ5UTBkRGtyeHhNWkhpZUlKZDN2UnRVdG1wNzdHeUhoakNhbmFaSkhBeF9vY1ZLajNLWk9mQmVSYXJjbldsYUIwYS1ycnplSnQtZ1lvVlZYV0RMcjdueXgtOUd5aEQzVER3bHh0c21MUWl6RGJzRkxfNjlmOWZsRjJpMWY0Mnp4b2NPWGJ1UjlNbm1vbQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxON0JPdEc2MXNVR1UzZF8tZk00UERCQTF2RnkwU3Q0QTNXcDJ5MmtNeF94dmpoZXVTWFRydkUwb1UySkU5dEtSQ1NweGRVTUN0V2FDQU14QUIzU3Zfa2JZRTlLSks4Zm1LVWxiN1FnTzd4ZXdrZEF1VnhEeWF0LTMtWDZrNTBlSmJ1YUJ4a1dfZXAtOTBJZnJ0Yw?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxPSlhIOHBrX2pVcnVZNF9Lck5OZTgyX1VxZ1MtLXVuMGxJMVgyQUpOampMUmNWNDhCYUpGT01meXRDNUh1d2RZOXdmeU1VaHJ3XzVqcExuWEEyZEFHQ3V2QjhoWl9kNGUxNGNMSHFmVGw5S0YzVTFVaV90ekZTdVVNVE0zTHdMMjd1dFJRem5KZTlDRmdyOF9RTEUxaGpiVXE3TTNQalh4OXVrWFFWdDNGal9udHJCRnNoQU43ODJxTnR1TkRGZVRjT0RnTWZMb3RUZUJ1Rnln?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
