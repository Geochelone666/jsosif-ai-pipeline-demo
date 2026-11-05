# AMZN Intelligence Report

- ticker: **AMZN**
- Report as_of: **2026-11-04**
- Market data as_of: **2026-11-04**
- Quant sources: https://finance.yahoo.com/quote/AMZN/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMZN/key-statistics/
- AI analysis snapshot as_of: **2026-11-04**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-05T05:26:08.037437+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 6, 'ai': 9, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261104T044411Z-6b13f9ec/AMZN** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 9 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 43.48%; oldest publication 2026-10-30

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 266.0300 |
| Return 1D (%) | 6.1191 |
| Return 1W (%) | 4.4894 |
| Return 1M (%) | 5.7689 |
| Return YTD (%) | 15.2543 |
| Return 1Y (%) | 6.7022 |
| Annualized volatility (%) | 33.9470 |
| Beta vs SPY | 1.4703 |
| Max drawdown (%) | -20.5476 |
| Sharpe (rf=0) | 0.3577 |
| Downside deviation (rf=0, %) | 21.1043 |
| Sortino (rf=0) | 0.5754 |
| Historical VaR 95% (1D, %) | 2.9597 |
| Historical ES 95% (1D, %) | 4.0742 |
| Correlation vs SPY | 0.5561 |
| Tracking error vs SPY (%) | 28.8531 |
| P/E (trailing) | 20.26 |
| P/B | 4.69 |
| EV/EBITDA | 16.70 |
| Revenue growth (%) | 12.10 |
| Forward P/E (estimate) | 24.37 |
| Gross margin (%) | 51.37 |
| Operating margin (%) | 13.90 |
| Return on equity (%) | 27.42 |
| Free cash flow yield (%) | -1.21 |
| MA50 | 253.8908 |
| Close vs MA50 (%) | 4.7813 |
| MA200 | 243.6709 |
| Close vs MA200 (%) | 9.1760 |
| RSI (14, Wilder) | 59.8733 |
| MACD (12,26) | -0.6119 |
| MACD signal (9) | -0.9877 |
| MACD histogram | 0.3757 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMZN': 275, 'SPY': 275}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 266.0300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 6.1191 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 4.4894 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 5.7689 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 15.2543 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 6.7022 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 33.9470 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.1043 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.5754 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9597 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.0742 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5561 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 28.8531 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.4703 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -20.5476 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3577 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 24.3716 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 51.3740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 13.9030 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 27.4160 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: -1.2074 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 20.2612 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 59.8733 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.3757 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 4.7813 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 9.1760 -> Clearly above the moving-average trend level.

## TAILWINDS

### Amazon rises 6% as hyperscalers advance on U.S. election results (AMZN:NASDAQ)
- Summary: Amazon rises 6% as hyperscalers advance on U.S. election results (AMZN:NASDAQ)
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQY3dmUWlDazhkTW80ZFYycWlzWkhtZk1USEoxZ0F4MmozdlpQYVdUSWpuMWRYanlhTE5LRTJsNVlWSXNhYS1rZnZTTkRIREJOSFJPRU5HYThpczRIYUR1TUl5TW5nUElhakRtM29Vd2VpTzkzSGVNN3RobXA5cGhDXzBzaTFlTXVnSUhaNWdXODVOTVAtMnhEaHNLSG5PcG9o?oc=5>

### Amazon Shares Surge 8% Post-Midterms Amid Tech Sector Optimism (AMZN)
- Summary: Amazon Shares Surge 8% Post-Midterms Amid Tech Sector Optimism (AMZN)
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxOdTkxbUJOYUNCSmJxU3kwdkdHR3dPajVlUVVmVFdxMjVsTWZtSHBfZTlPWHhVdFk5Rmo1c1VSckhMQjlNZ25tLTJHTHBxT1Q0Qk1FdHJyelUxYVE4WkRVNk1KMHRPdWZzZmdnQWNGUnhQX21FdWJJMjZrWmlWbHRXWWlDenVsSnh6aXh5VFdWQTZCc1IwV1NocEMyRTFxVXFRMlh0amdyRQ?oc=5>

### Amazon (NASDAQ:AMZN) Stock Rallies as Wall Street ‘Buy’ Upgrade Highlights 39% AWS Growth
- Summary: Amazon (NASDAQ:AMZN) Stock Rallies as Wall Street ‘Buy’ Upgrade Highlights 39% AWS Growth
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMieEFVX3lxTE5TRVJ2ODRjSDRoWUtreUFjYkJONzY4VFMyUE5GVy0zaS1lcHFVaFpOQnlkTVFXTkhTYWVIRFNJZUlIbjNUcEhjbWFfTHlRVGp3WFE1algzZzdNTVJ1amVaX2syM0piLWI1VEJPTS05OVNNbU5aZjBNZg?oc=5>

### Why Amazon Stock Rallied Monday Morning
- Summary: Amazon shares surged Monday morning due to positive market sentiment and strong earnings expectations.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxOdDBxcVFnZUY3UVczSkJGUFdIOXJweEg4NURlT09tRi12MThQQ1Y5Rl9CcUtzMWJUdDJHWnpHTWV6R015R194ZXE1cmtLZXprZGZnSWJFNndveUpBWU9sMTFwYkxPYTdib3JlOGVSSHVUalB6THFlOGFnckN4WWRLSmhYR1QzX0ROOHc?oc=5>

### Amazon (AMZN) Stock After Q3 Earnings: Buy the Dip, Sell, or Hold?
- Summary: Analyst offers buy/dip/sell/hold guidance post Q3 earnings.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxNZTRnSk1vYUtiQlJ0YVdWUEVMQm5mMFZfbjc0T1hwZDFLUjR5THFrbTFzanhGNUhIYV8wV2Vpa2FRTXFRcTRsanphR1ZSS1lHMjQ3QkoxVlhYSmo3QkFWS29fa1VHaHlMVVpCV21GcFpaQVBaLXhvd0wzbWFSRFZTNG5rdnVfM3lOTnVBaHVWSmU4MlIwYzI0WU8teXN0WTl5Q0pJ?oc=5>

### Amazon Leads Cloud Hyperscaler Stocks Higher. What 'Blue Tsunami' Means For Big Tech.
- Summary: Amazon's cloud segment drives hyperscaler stocks higher, signaling strong demand for cloud services.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOc0YzaXo0b2JIcXlEM25sejBneVBlQi1EazRyR0NoVTM5REJ4NjR0WkdKM1k1ckVsZzRTTEFVQ1pSTTJmSDFvWlFERGRDVWp2a1hsRld4dnhjbURqRnJiRENYSzJxM2JuejdFNHVVUnhRLXBnYzdOSm8zSmlTX3pkczlES1hVTnZtZG5vOWYtMTRkWTNDTEE?oc=5>

### Alphabet, Amazon, and Microsoft All Surged Today. You Can Thank the Big Blue Wave.
- Summary: Amazon shares surged alongside peers, reflecting a positive market wave.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxQS3FPNjF0Qnk2dkx5Z1hfblotbmJudmtpaWF5Zk1vR2xmMHBQLUVMbUVNTC1nQUJfRDVacldTUDllT3lpOHRVSnJCSTB0eEZlV1AycktIdFFNMmF4UVJxa0Z6VExPcFBXUFhKZzNBeUZCMHd4UGhQcjZscVl5blJodFZqSDE4WU82Q3FXTmo2YTdWM0tta01ZREFSbmxBUzdDVVpqaXNLXzM1YmlUaWlLV2RNQXRaVW1GVkJtWjlB?oc=5>

### Retail Stocks Rally Post-U.S. Election; Amazon (AMZN) Shares Ris
- Summary: Amazon shares rose as retail stocks rallied after the election.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxQODVobXhqUDVuTzhKdXRjN2p2ZGhqbDE1VWt0MG1FVGwwTEU3Sll2bVhLb3czZU5KOVFGM09wU3FlZlNzaTBlRGV0T1hyX3RkVTlVT1dFRzc5RlhKNHhsd3dSUWg5MEdnWUJnTmszd2xzRGtqOTlLdzBuWTdfQWpFV2xYN0RodHotYlRYdTdmYmVGZ3FOOENsRnpDaFYzamluZW5N?oc=5>

## HEADWINDS

### Amazon Stock Fell After Earnings. Jim Cramer Says Buy Right Here
- Summary: Amazon Stock Fell After Earnings. Jim Cramer Says Buy Right Here
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQdVZfYkpFaURIalAwZHlsWjJ0RGJlekJJNjBUWFEtbThRUkhxQVpFMk5ieENxZzNFZlpOd2s0VG5TSkpHaE5hS190bXMtb2JkeGQyRkJ5Z2JOcnE3UEdBUUFhVmRQMzFQQlVXcVBEUDdEczUyZllrUUtoV2JxTE9QS1ZLUmVtSmk0RmhMcmMwTEtaZmxaV2M1T0VOdw?oc=5>

### Amazon (AMZN) Stock Slips As Q3 Earnings Reflect Profit Reset
- Summary: Amazon (AMZN) Stock Slips As Q3 Earnings Reflect Profit Reset
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOMHVOOUNrejV0ZnJZZFhTWGhHRDFVN2hwd2djSHZDbFR0aHZhdlVZSy1rcWN5eVJzYWlJRURXN013em1KVS1lNkNVQ0wybEllb0h0dnZHajhYUjhKTFIzQjZMS2ZYb0FJQm5kcjVmOGNBOFllYWYyT2hXTVh1cmFoY1d6eENfak9XcUpCekdxSHZyaDMyQ2c?oc=5>

### Amazon CEO Andy Jassy Says Investors Are ‘Sleeping a Bit’ on Retail as AMZN Stock Falls 7% in 6 Months
- Summary: Amazon CEO Andy Jassy Says Investors Are ‘Sleeping a Bit’ on Retail as AMZN Stock Falls 7% in 6 Months
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNdENRZlJLQWhqdGtGWG9tSDVjX3Bqa2tEenVrYUJaaHBjNXo4RzFDdlM4YjNZSmtiT0h3S0YzVmVxLTBTLXBzcGhlM0ZXaXVSRlBBZmRkUGVyZ1NORS1lQUZWeGdfejh3cnNicWJyVUNjZ2NnM0wyWFk0RW1tdEx4N2diWlUyYkR1aUhLVXdzUnhFT1JWSVE?oc=5>

## CATALYSTS

### Amazon.com, Inc. (AMZN) Could Be Entering Its Next Growth Phase: Here’s What Investors Should Know
- Summary: Potential new growth phase for Amazon discussed.
- Date: 2026-11-03 | Impact: high | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOQjlDRnhEcEJFTnY0OUtqUXk4VF9CN0VMRDM0b003ZXlTT3FPa1V2cmtXNjJOa21NSnZld3k5UmRoclF5eGtHbUVlQTVtbUlSaGlOdG05cGgxcVBVbWRfbjBoVjFkYnRKY2lVdzZkWUloSm5EcVlyUkN5S0U0MXo0dVJfY20tV0VGU0xIS0gyZjB2UmxC?oc=5>

### Phillip Securities Says Amazon’s ‘Strong Demand Visibility’ Supports Aggressive Capex
- Summary: Analyst highlights strong demand, supporting higher capital expenditures.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxOTU11b201VGNET3J1SXBfbmJfekt0aWhyakdicUJkYXdoTDRvSk5ibjFUenM1N0ZjTU4yeDBoTlNIdmhSU3hOQ2ZEeWRhVUh0SUstSWtjMDh0ZHgtWFk4ZTU3WFpfcDBSS3NjVGpydXRRTnNZdzlINkN4eVh2dXJyQXF0bWlFRWpsdFRJM1dtNU0wcFR3MzQ2R0hVY1JOc1hxRWdTZA?oc=5>

### Andy Jassy Just Delivered Magnificent News for Amazon Investors
- Summary: CEO Andy Jassy announced positive developments for Amazon, boosting investor confidence.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNb0JESU9yV19hZk8xTWdnWGhRSHppYjlfaU51ajQwd3lHaHdianpsc2YwcWs5dGhnWEk5cjJfaG5ub2tRSm5zWFdDeWRZX2tnZU9UeG96REhhbUxoSjk2VzM5b2h1VVVsSDlFcGpoZFBmNURZaHRldWxEdmZjQWw0WEE0YkIxZWZVVy1xck9FakM2RkFfT205dWM0ZU01NmljVlFPTg?oc=5>

### Democratic Sweep Raises Data Center CapX Concerns; Amazon (AMZN) Shares Jump 7%
- Summary: Amazon shares rise 7% amid concerns over increased data center capital expenditures due to a Democratic electoral sweep.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxQUjZwOFFReVZtZGNjNVVUZk5qMHVzV1RZMUEtcGFheUNNWTcxSmRxU1dLV0lfbl9ESGxwSEFrejJUdVhDN3kxc1poMkVwUHBGSEVwU2tnLUZzc0JFMUlSVlY0aDRGYjZkeTdzbTljZ1JfeVZMZE5vS2F1V1dwRzdJNlhDcHBpQmRpdlNDUnZHMDJUZGxlWExISDZWNi15N1NjWTRmOU1jS21WTjBtZ29CYlQyN1o?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMZN** | **20.26** | **4.69** | **16.70** | **12.10** | **2,876,619,096,064.00 USD** | **6.70** |
| WMT | 45.16 | 10.44 | 24.84 | 5.90 | 1,027,945,070,592.00 USD | 27.37 |
| MSFT | 27.19 | 8.77 | 20.40 | 18.80 | 4,127,478,775,808.00 USD | 8.95 |
| GOOGL | 14.62 | 5.39 | 18.63 | 24.70 | 3,552,105,201,664.00 USD | 4.37 |

Peers fetched as_of: 2026-11-04; AMZN reuses existing data (market data as_of: 2026-11-04); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-29
- Next expected earnings: 2027-02-04 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-04

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-30
- Revenue (latest available single quarter): 201,944,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 20,685,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMioAFBVV95cUxQY3dmUWlDazhkTW80ZFYycWlzWkhtZk1USEoxZ0F4MmozdlpQYVdUSWpuMWRYanlhTE5LRTJsNVlWSXNhYS1rZnZTTkRIREJOSFJPRU5HYThpczRIYUR1TUl5TW5nUElhakRtM29Vd2VpTzkzSGVNN3RobXA5cGhDXzBzaTFlTXVnSUhaNWdXODVOTVAtMnhEaHNLSG5PcG9o?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxOdTkxbUJOYUNCSmJxU3kwdkdHR3dPajVlUVVmVFdxMjVsTWZtSHBfZTlPWHhVdFk5Rmo1c1VSckhMQjlNZ25tLTJHTHBxT1Q0Qk1FdHJyelUxYVE4WkRVNk1KMHRPdWZzZmdnQWNGUnhQX21FdWJJMjZrWmlWbHRXWWlDenVsSnh6aXh5VFdWQTZCc1IwV1NocEMyRTFxVXFRMlh0amdyRQ?oc=5
- https://news.google.com/rss/articles/CBMieEFVX3lxTE5TRVJ2ODRjSDRoWUtreUFjYkJONzY4VFMyUE5GVy0zaS1lcHFVaFpOQnlkTVFXTkhTYWVIRFNJZUlIbjNUcEhjbWFfTHlRVGp3WFE1algzZzdNTVJ1amVaX2syM0piLWI1VEJPTS05OVNNbU5aZjBNZg?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxOdDBxcVFnZUY3UVczSkJGUFdIOXJweEg4NURlT09tRi12MThQQ1Y5Rl9CcUtzMWJUdDJHWnpHTWV6R015R194ZXE1cmtLZXprZGZnSWJFNndveUpBWU9sMTFwYkxPYTdib3JlOGVSSHVUalB6THFlOGFnckN4WWRLSmhYR1QzX0ROOHc?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxNZTRnSk1vYUtiQlJ0YVdWUEVMQm5mMFZfbjc0T1hwZDFLUjR5THFrbTFzanhGNUhIYV8wV2Vpa2FRTXFRcTRsanphR1ZSS1lHMjQ3QkoxVlhYSmo3QkFWS29fa1VHaHlMVVpCV21GcFpaQVBaLXhvd0wzbWFSRFZTNG5rdnVfM3lOTnVBaHVWSmU4MlIwYzI0WU8teXN0WTl5Q0pJ?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOc0YzaXo0b2JIcXlEM25sejBneVBlQi1EazRyR0NoVTM5REJ4NjR0WkdKM1k1ckVsZzRTTEFVQ1pSTTJmSDFvWlFERGRDVWp2a1hsRld4dnhjbURqRnJiRENYSzJxM2JuejdFNHVVUnhRLXBnYzdOSm8zSmlTX3pkczlES1hVTnZtZG5vOWYtMTRkWTNDTEE?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxQS3FPNjF0Qnk2dkx5Z1hfblotbmJudmtpaWF5Zk1vR2xmMHBQLUVMbUVNTC1nQUJfRDVacldTUDllT3lpOHRVSnJCSTB0eEZlV1AycktIdFFNMmF4UVJxa0Z6VExPcFBXUFhKZzNBeUZCMHd4UGhQcjZscVl5blJodFZqSDE4WU82Q3FXTmo2YTdWM0tta01ZREFSbmxBUzdDVVpqaXNLXzM1YmlUaWlLV2RNQXRaVW1GVkJtWjlB?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQODVobXhqUDVuTzhKdXRjN2p2ZGhqbDE1VWt0MG1FVGwwTEU3Sll2bVhLb3czZU5KOVFGM09wU3FlZlNzaTBlRGV0T1hyX3RkVTlVT1dFRzc5RlhKNHhsd3dSUWg5MEdnWUJnTmszd2xzRGtqOTlLdzBuWTdfQWpFV2xYN0RodHotYlRYdTdmYmVGZ3FOOENsRnpDaFYzamluZW5N?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQdVZfYkpFaURIalAwZHlsWjJ0RGJlekJJNjBUWFEtbThRUkhxQVpFMk5ieENxZzNFZlpOd2s0VG5TSkpHaE5hS190bXMtb2JkeGQyRkJ5Z2JOcnE3UEdBUUFhVmRQMzFQQlVXcVBEUDdEczUyZllrUUtoV2JxTE9QS1ZLUmVtSmk0RmhMcmMwTEtaZmxaV2M1T0VOdw?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOMHVOOUNrejV0ZnJZZFhTWGhHRDFVN2hwd2djSHZDbFR0aHZhdlVZSy1rcWN5eVJzYWlJRURXN013em1KVS1lNkNVQ0wybEllb0h0dnZHajhYUjhKTFIzQjZMS2ZYb0FJQm5kcjVmOGNBOFllYWYyT2hXTVh1cmFoY1d6eENfak9XcUpCekdxSHZyaDMyQ2c?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNdENRZlJLQWhqdGtGWG9tSDVjX3Bqa2tEenVrYUJaaHBjNXo4RzFDdlM4YjNZSmtiT0h3S0YzVmVxLTBTLXBzcGhlM0ZXaXVSRlBBZmRkUGVyZ1NORS1lQUZWeGdfejh3cnNicWJyVUNjZ2NnM0wyWFk0RW1tdEx4N2diWlUyYkR1aUhLVXdzUnhFT1JWSVE?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOQjlDRnhEcEJFTnY0OUtqUXk4VF9CN0VMRDM0b003ZXlTT3FPa1V2cmtXNjJOa21NSnZld3k5UmRoclF5eGtHbUVlQTVtbUlSaGlOdG05cGgxcVBVbWRfbjBoVjFkYnRKY2lVdzZkWUloSm5EcVlyUkN5S0U0MXo0dVJfY20tV0VGU0xIS0gyZjB2UmxC?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxOTU11b201VGNET3J1SXBfbmJfekt0aWhyakdicUJkYXdoTDRvSk5ibjFUenM1N0ZjTU4yeDBoTlNIdmhSU3hOQ2ZEeWRhVUh0SUstSWtjMDh0ZHgtWFk4ZTU3WFpfcDBSS3NjVGpydXRRTnNZdzlINkN4eVh2dXJyQXF0bWlFRWpsdFRJM1dtNU0wcFR3MzQ2R0hVY1JOc1hxRWdTZA?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNb0JESU9yV19hZk8xTWdnWGhRSHppYjlfaU51ajQwd3lHaHdianpsc2YwcWs5dGhnWEk5cjJfaG5ub2tRSm5zWFdDeWRZX2tnZU9UeG96REhhbUxoSjk2VzM5b2h1VVVsSDlFcGpoZFBmNURZaHRldWxEdmZjQWw0WEE0YkIxZWZVVy1xck9FakM2RkFfT205dWM0ZU01NmljVlFPTg?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQelVMSUtLR01QSHNWZUkzd0pLY0lKcTlOUnhia2xSLXIxZnhJSzhaVXNJV0ltaTBaMERGZFBKRlhWQV9adG5LNUt1MUVPMXZnMzZiUGo1MlpYSmdOeVVfYXd6OUx5SHgxYzJZdHVkVVNpcDdxVlBGZnNBZ25WOE9JN2RyS1g3RTg4SHIxaDlYWUhTdWRj?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxQUjZwOFFReVZtZGNjNVVUZk5qMHVzV1RZMUEtcGFheUNNWTcxSmRxU1dLV0lfbl9ESGxwSEFrejJUdVhDN3kxc1poMkVwUHBGSEVwU2tnLUZzc0JFMUlSVlY0aDRGYjZkeTdzbTljZ1JfeVZMZE5vS2F1V1dwRzdJNlhDcHBpQmRpdlNDUnZHMDJUZGxlWExISDZWNi15N1NjWTRmOU1jS21WTjBtZ29CYlQyN1o?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
