# MU Intelligence Report

- ticker: **MU**
- Report as_of: **2026-11-04**
- Market data as_of: **2026-11-04**
- Quant sources: https://finance.yahoo.com/quote/MU/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MU/key-statistics/
- AI analysis snapshot as_of: **2026-11-04**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-05T05:15:03.358289+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 0, 'ai': 14, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261104T044411Z-6b13f9ec/MU** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 10 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 47.83%; oldest publication 2026-11-02

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 795.2300 |
| Return 1D (%) | -7.0015 |
| Return 1W (%) | -19.1207 |
| Return 1M (%) | -26.0059 |
| Return YTD (%) | 178.8310 |
| Return 1Y (%) | 265.1484 |
| Annualized volatility (%) | 82.0082 |
| Beta vs SPY | 3.2761 |
| Max drawdown (%) | -39.0954 |
| Sharpe (rf=0) | 1.9921 |
| Downside deviation (rf=0, %) | 49.7512 |
| Sortino (rf=0) | 3.2838 |
| Historical VaR 95% (1D, %) | 6.9980 |
| Historical ES 95% (1D, %) | 9.5267 |
| Correlation vs SPY | 0.5129 |
| Tracking error vs SPY (%) | 76.2241 |
| P/E (trailing) | 11.50 |
| P/B | 6.50 |
| EV/EBITDA | 7.92 |
| Revenue growth (%) | 379.30 |
| Forward P/E (estimate) | 3.83 |
| Gross margin (%) | 80.72 |
| Operating margin (%) | 80.68 |
| Return on equity (%) | 88.26 |
| Free cash flow yield (%) | 3.24 |
| MA50 | 972.0758 |
| Close vs MA50 (%) | -18.1926 |
| MA200 | 753.7265 |
| Close vs MA200 (%) | 5.5064 |
| RSI (14, Wilder) | 35.3811 |
| MACD (12,26) | -38.8910 |
| MACD signal (9) | -29.1164 |
| MACD histogram | -9.7746 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MU': 275, 'SPY': 275}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 795.2300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -7.0015 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -19.1207 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -26.0059 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 178.8310 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 265.1484 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 82.0082 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 49.7512 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 3.2838 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 6.9980 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 9.5267 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5129 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 76.2241 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.2761 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -39.0954 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.9921 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 3.8276 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 80.7160 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 80.6780 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 88.2600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 3.2387 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 11.5034 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 35.3811 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -9.7746 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -18.1926 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 5.5064 -> Clearly above the moving-average trend level.

## TAILWINDS

### Micron, Nvidia, and AMD lead chip stocks' rebound
- Summary: Micron’s inclusion in a rebound of chip stocks signals positive market sentiment.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOR241WmdKTExjbmZJcndhY3BOVG91eVFPT29xVzBLcVQ4NGQtUExYVDlray1hM1c5dENLekg3bkxyaHFramhTTVEwclZnci1uLWdvbi0zc21pbUMzazNZOFlRUEduSDF5al9jRjMxUG5FOGlTaTdTQVVKZVNRTWplRzh4UjdiYnNhZzBpTHlzS0Q4NzZLZmpfcjJLM1p3TlI3?oc=5>

### ETFs Are Buying Micron Technology (MU) on Oct. 30
- Summary: ETF purchases signal confidence in MU’s short‑term prospects.
- Date: 2026-11-03 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPMTgtN2JOTHgxZWZ1SzNQVlJ1RXVkbUhjX0JRQTA3azdUdUtEbkNhdGhWV2Z1TFJNSmlIMDdmdmJQU1AtRkpDakhGRTdfalB4SmI2Wk14VHg3Tm9VZXFjbzFwemRIRjM3Q2loU1FsZjNTOG9hNTNzNHZHNDRPRGdJbDFndmJHWmZMaS00NjV5LWpWeHVSbWNLOEU3dzBjdw?oc=5>

### Micron Stock: Massive Buybacks Expected in December
- Summary: Micron plans significant share buybacks in December.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMif0FVX3lxTE1PaEJIZWFJMXNaTnNieTMyTzFvT1NtOVVPT1FURXRpTEtQdWtIVDl6VTZsWjZrLWQyTDhHc19qUUN4OVNkLUpqUjN2Q3FLemM1SzNnb1VwcldfSmIwVzJ5VUpLWmQ4NFhPdWoxZ3BOczRuYmdzUEFxdEdIVTFCSnM?oc=5>

## HEADWINDS

### Micron Falls 4% as Kioxia's Cautious Outlook Hits Memory Stocks; Western Digital Drops 5%, SanDisk Slides 3%
- Summary: Micron shares dropped 4% following Kioxia’s cautious outlook, impacting memory sector sentiment.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi3wFBVV95cUxQd24xZ3lROHBoV1M2WWN3VmlMUjNjZ1ZfZnNNNGFmWnhZZ2d5Qnl4TjZMd3FPSm44N0VIRFhVM2s2RkNpVmdvMWJYeUZnRWR5YWhIdmtKdUpiQndZV19vaFlFRU1hZ1FfTk9GRzJ4M3lXLVJHclZ0cmpzYW9CbkJvb1BYNGNDYmpJTkJhWkRmMklmN3EtM2ZYc2V2bzEzdGZCVTJtZmVvVVk1SjhTQUQtNzZ2MDlQaXQ3T3NSaVBjQ0FCRm53Mkc3UEtzOGNWaUc2XzhVb0NNS3Ryc1JsZkVN?oc=5>

### Micron (MU) Stock Sinks As Market Gains: Here's Why
- Summary: Micron shares decline amid market gains.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQc3NNb1RNWmpjTFRUWWdBOC1mampaLWQ1YWFoYW9aRlNCcndUWXBWSkJEb2RnWWFPMVhkTS1mSG5sNmFNS0RmaEJ1aXFPVnBhTzdHc1hyUDA5enpSeFgzUjBqRnBhSURweGtoNHRNNTA5MWpabi1MMHpxTE91MFdJSzRDUGdmVkNCbERuV21fYVZMdUFyS2FHcg?oc=5>

### Why is Micron Technology stock sliding today?
- Summary: Micron shares are falling today.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPZjJoVEs0aDhFUndVU1duMmtTVEc4aVFEV1lWTTNtSlNDYlVOQ0RYOVY1Y1l1Y0FkRG9oZWFlcmNkOXZrNDh3X25kZ1hvOWtqaWZ1Nk5VQk9kMnYtRjNfZFZ3bHpyeXpTUnpJRWRQUEN1T0RCbkJkUXJyUDhrdUV6aDRVTmFSQ002TmRwWDRaSlFBeHg2eTF2X1NxMzlUaEl6bzJuUndnNXRPZw?oc=5>

### Micron Stock Drops. Memory Price Warnings Pile Up After Democrat Success.
- Summary: Stock fell amid memory price warnings following political event.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxNMG04amV1VGQyVVBhNFhUZ0lmNXRxUTdJX1FNbmlXSGpkVC1rNnBTQ3VHb2xGbDhpZWpQYzZIek5ySURSWnVxZjdGLTZNY2ZGOVVVcnJDS0JIdmE4c0ttZ0tCUENZTFhOczlQeXZOTTJYNVpaanhzREdCTURHR2g2Y0hETkFZNmJNTS0wVkln?oc=5>

### Why Micron Stock Is Falling Today
- Summary: Stock decline attributed to recent factors.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPU0RwVjVWeDQ2RENzVzNYZXRJT0E4ZWtkWE5VcXdnbm5Fb0VpTksyVG92UXFNNWpybVBoMFJ3WWtZZGQ4ZGoxM2YyRzkxLWI0SnNnQ3UtbnRCQmpsQ0V6WkpQdE1PNDRnWFhEVUZTbndmNktZeVlwdW03bzJLand6Ri1STm9VTHkzU083bHZSM2VJYnFWUWJJeW9EYw?oc=5>

### Micron Technology (MU) Pulls Back Amid Broader AI Memory Sell-Off; Underweight Position Aids Relative Returns
- Summary: Pullback due to AI memory sell-off, underweight stance helps returns.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNcmV6OW9ld041cUU0MWl4QU9wN3pGcnhKZER4NmlYYnI3R3NvWDcxbGFGTTNEdFBYX2ItY0JpY2RveHcxUzktNDBCRllGQmw4U29jMkJyY0pFcy1YUmhpbzhuLVhBMHlHdXhsdjh4VFhfRHdETU9pUTFDR1ByUHNrM0ZWb21nM1NPZGJtbHZ0VW00dGw0M192dGtqZ3o?oc=5>

## CATALYSTS

### Micron Investors: Mark December 9 On Your Calendar (NASDAQ:MU)
- Summary: Scheduled investor event may influence MU’s short‑term outlook.
- Date: 2026-11-03 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNM2hSczhyTDFGck50RmRLOWFyT0VEbGxYYkhQQVpRUEFIVlpYdVBOVzJteXhUX054SVhlazIzS3NXR1VxWkJaclpYcDZkRW1zWVEwamd2Y2R6ZnJhaVNNRENEVDUycE1iU1JmN25HUzJGVEFuU1lMZEU3eXJwUXZNdVdURmNOMUtHZTQxS19lWG83SkhT?oc=5>

### Micron Tech Gains as Tech Giants Scramble to Lock in Multiyear Supply
- Summary: Supply agreements with major tech firms boost MU’s product pipeline.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNOWtudFV6QUw5eHN3bGR5bThpblZ4azhIUW5NZ0xTWlg4UTFEV0FDTHVrcEdUZE5taXV2T3htR183YndhOXNERVRxY05ibHF4a1pZSWJ4S3dpVU41V2xidnN6YWtOYVJuNUYwZFgzT1VxN2QwdHJNbEZLZlJPZWR0cldJTElFOE9DLWUzclJpT0VFWV83bDFFaFBR?oc=5>

### Are Wall Street Analysts Predicting Micron Technology Stock Will Climb or Sink?
- Summary: Analysts debate future price direction.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxOQzFLbG1SdzdfdFR3RDJLT29yZWxra25qekVZWlNCYVNhNmpFQVhpdmY0VUFnVDdsUXpSbzFsSlhxX2NIcGhvS3E4ZUxESzdCWVlOaUdMcUdJSXNnSml1VHAyal9iN3NEYTVQNGNHZVNEaWNUZ3hBQmk1NFFHWHZ2aUR5Ui0yVEJnbmc2ZktuZUhvT29CRE5wRTRjSUV2RlpvVUxmU256bFFkdGNoYVAyYWxBa1J6MUdQS0tmeXBIUQ?oc=5>

### What Wall Street is Missing About Micron’s (MU) Ultra-Low Earnings Multiple
- Summary: Earnings multiple lower than expected, analysts may overlook.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOZm5OcG9fOWsxbGR6RGlCZXVQRFdDNFZYb1dWUVZqNUw3UUdKcWd6Rk1XVkFZVFZTc0RKMUZuRTVIZmxZSUhFTVZZYm81al9uT3B4QXQzUzRKR3FjdXVhOW55WF94enVWdWpha3RJUHJPZ0JGUEtvTjNxbmtmNTQzOEdNbldicGtjNXU1TGd4dzJqeld2bjZEalV3?oc=5>

### Micron Technology (MU) is Holding Firm on High-Bandwidth Memory (HBM)
- Summary: Micron maintains commitment to HBM technology development.
- Date: 2026-11-04 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPbmE2VkVuZlFSb045UDJrTXdTNE1QMVlzblhoM2hqUVdqU3pzRGQwZzFWeS1wRHVaNktxN01QYXFwUHYxOGtWY0s2M2k4MWdXem11YThKc1BJTVgxWTBwcVFmVk1LTzJ4UzJrTUZic01VekRoNk5hUEs0MUU2b2U2b1EtRlBwZ1pWdFlzempvWHkzdVNTMzNZOW9ueE9TWkk?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MU** | **11.50** | **6.50** | **7.92** | **379.30** | **899,741,646,848.00 USD** | **265.15** |
| WDC | 12.22 | 12.96 | 19.14 | 55.50 | 121,217,097,728.00 USD | 113.19 |
| STX | 31.80 | 37.06 | 22.04 | 61.00 | 127,879,307,264.00 USD | 123.80 |
| NXPI | 20.67 | 5.53 | 13.78 | 19.30 | 66,796,564,480.00 USD | 31.93 |

Peers fetched as_of: 2026-11-04; MU reuses existing data (market data as_of: 2026-11-04); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-30
- Next expected earnings: 2026-12-23 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-04

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-10-09
- Revenue (latest available single quarter): 8,440,000,000.00 USD; period 2018-06-01/2018-08-30; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 28,243,000,000.00 USD; period 2026-02-27/2026-05-28; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/723125/000072312526000023/mu-20260903.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMioAFBVV95cUxOR241WmdKTExjbmZJcndhY3BOVG91eVFPT29xVzBLcVQ4NGQtUExYVDlray1hM1c5dENLekg3bkxyaHFramhTTVEwclZnci1uLWdvbi0zc21pbUMzazNZOFlRUEduSDF5al9jRjMxUG5FOGlTaTdTQVVKZVNRTWplRzh4UjdiYnNhZzBpTHlzS0Q4NzZLZmpfcjJLM1p3TlI3?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPMTgtN2JOTHgxZWZ1SzNQVlJ1RXVkbUhjX0JRQTA3azdUdUtEbkNhdGhWV2Z1TFJNSmlIMDdmdmJQU1AtRkpDakhGRTdfalB4SmI2Wk14VHg3Tm9VZXFjbzFwemRIRjM3Q2loU1FsZjNTOG9hNTNzNHZHNDRPRGdJbDFndmJHWmZMaS00NjV5LWpWeHVSbWNLOEU3dzBjdw?oc=5
- https://news.google.com/rss/articles/CBMif0FVX3lxTE1PaEJIZWFJMXNaTnNieTMyTzFvT1NtOVVPT1FURXRpTEtQdWtIVDl6VTZsWjZrLWQyTDhHc19qUUN4OVNkLUpqUjN2Q3FLemM1SzNnb1VwcldfSmIwVzJ5VUpLWmQ4NFhPdWoxZ3BOczRuYmdzUEFxdEdIVTFCSnM?oc=5
- https://news.google.com/rss/articles/CBMi3wFBVV95cUxQd24xZ3lROHBoV1M2WWN3VmlMUjNjZ1ZfZnNNNGFmWnhZZ2d5Qnl4TjZMd3FPSm44N0VIRFhVM2s2RkNpVmdvMWJYeUZnRWR5YWhIdmtKdUpiQndZV19vaFlFRU1hZ1FfTk9GRzJ4M3lXLVJHclZ0cmpzYW9CbkJvb1BYNGNDYmpJTkJhWkRmMklmN3EtM2ZYc2V2bzEzdGZCVTJtZmVvVVk1SjhTQUQtNzZ2MDlQaXQ3T3NSaVBjQ0FCRm53Mkc3UEtzOGNWaUc2XzhVb0NNS3Ryc1JsZkVN?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQc3NNb1RNWmpjTFRUWWdBOC1mampaLWQ1YWFoYW9aRlNCcndUWXBWSkJEb2RnWWFPMVhkTS1mSG5sNmFNS0RmaEJ1aXFPVnBhTzdHc1hyUDA5enpSeFgzUjBqRnBhSURweGtoNHRNNTA5MWpabi1MMHpxTE91MFdJSzRDUGdmVkNCbERuV21fYVZMdUFyS2FHcg?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPZjJoVEs0aDhFUndVU1duMmtTVEc4aVFEV1lWTTNtSlNDYlVOQ0RYOVY1Y1l1Y0FkRG9oZWFlcmNkOXZrNDh3X25kZ1hvOWtqaWZ1Nk5VQk9kMnYtRjNfZFZ3bHpyeXpTUnpJRWRQUEN1T0RCbkJkUXJyUDhrdUV6aDRVTmFSQ002TmRwWDRaSlFBeHg2eTF2X1NxMzlUaEl6bzJuUndnNXRPZw?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxNMG04amV1VGQyVVBhNFhUZ0lmNXRxUTdJX1FNbmlXSGpkVC1rNnBTQ3VHb2xGbDhpZWpQYzZIek5ySURSWnVxZjdGLTZNY2ZGOVVVcnJDS0JIdmE4c0ttZ0tCUENZTFhOczlQeXZOTTJYNVpaanhzREdCTURHR2g2Y0hETkFZNmJNTS0wVkln?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPU0RwVjVWeDQ2RENzVzNYZXRJT0E4ZWtkWE5VcXdnbm5Fb0VpTksyVG92UXFNNWpybVBoMFJ3WWtZZGQ4ZGoxM2YyRzkxLWI0SnNnQ3UtbnRCQmpsQ0V6WkpQdE1PNDRnWFhEVUZTbndmNktZeVlwdW03bzJLand6Ri1STm9VTHkzU083bHZSM2VJYnFWUWJJeW9EYw?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNcmV6OW9ld041cUU0MWl4QU9wN3pGcnhKZER4NmlYYnI3R3NvWDcxbGFGTTNEdFBYX2ItY0JpY2RveHcxUzktNDBCRllGQmw4U29jMkJyY0pFcy1YUmhpbzhuLVhBMHlHdXhsdjh4VFhfRHdETU9pUTFDR1ByUHNrM0ZWb21nM1NPZGJtbHZ0VW00dGw0M192dGtqZ3o?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNM2hSczhyTDFGck50RmRLOWFyT0VEbGxYYkhQQVpRUEFIVlpYdVBOVzJteXhUX054SVhlazIzS3NXR1VxWkJaclpYcDZkRW1zWVEwamd2Y2R6ZnJhaVNNRENEVDUycE1iU1JmN25HUzJGVEFuU1lMZEU3eXJwUXZNdVdURmNOMUtHZTQxS19lWG83SkhT?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNOWtudFV6QUw5eHN3bGR5bThpblZ4azhIUW5NZ0xTWlg4UTFEV0FDTHVrcEdUZE5taXV2T3htR183YndhOXNERVRxY05ibHF4a1pZSWJ4S3dpVU41V2xidnN6YWtOYVJuNUYwZFgzT1VxN2QwdHJNbEZLZlJPZWR0cldJTElFOE9DLWUzclJpT0VFWV83bDFFaFBR?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxOQzFLbG1SdzdfdFR3RDJLT29yZWxra25qekVZWlNCYVNhNmpFQVhpdmY0VUFnVDdsUXpSbzFsSlhxX2NIcGhvS3E4ZUxESzdCWVlOaUdMcUdJSXNnSml1VHAyal9iN3NEYTVQNGNHZVNEaWNUZ3hBQmk1NFFHWHZ2aUR5Ui0yVEJnbmc2ZktuZUhvT29CRE5wRTRjSUV2RlpvVUxmU256bFFkdGNoYVAyYWxBa1J6MUdQS0tmeXBIUQ?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNMlRjajRncUFXWGJweWVDNUpCMVZRaVhCTEFGZkloOXdwY0RKLTNKN3I1U0ZzcHZNWXFXWGY3ZXYxLW9WejZFV3VOLTVCOFFYU1dPSG9ISGpRX1Y2RjQ4THlzX3dReTNGc29WZ0N0T1g5NFZMeG02MmpKSHB3N3E4Z2psRGJIZWhuWWgweXU5b1h2NkJhNjVFbHBDVXZDVk1SVVRBQW5n?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOZm5OcG9fOWsxbGR6RGlCZXVQRFdDNFZYb1dWUVZqNUw3UUdKcWd6Rk1XVkFZVFZTc0RKMUZuRTVIZmxZSUhFTVZZYm81al9uT3B4QXQzUzRKR3FjdXVhOW55WF94enVWdWpha3RJUHJPZ0JGUEtvTjNxbmtmNTQzOEdNbldicGtjNXU1TGd4dzJqeld2bjZEalV3?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPbmE2VkVuZlFSb045UDJrTXdTNE1QMVlzblhoM2hqUVdqU3pzRGQwZzFWeS1wRHVaNktxN01QYXFwUHYxOGtWY0s2M2k4MWdXem11YThKc1BJTVgxWTBwcVFmVk1LTzJ4UzJrTUZic01VekRoNk5hUEs0MUU2b2U2b1EtRlBwZ1pWdFlzempvWHkzdVNTMzNZOW9ueE9TWkk?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
