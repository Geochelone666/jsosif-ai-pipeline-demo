# ENB Intelligence Report

- ticker: **ENB**
- Report as_of: **2026-11-17**
- Market data as_of: **2026-11-17**
- Quant sources: https://finance.yahoo.com/quote/ENB/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ENB/key-statistics/
- AI analysis snapshot as_of: **2026-11-17**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-18T06:15:36.914130+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 2, 'ai': 13, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **17** exact headline/source/date matches; prior report **20261117T062519Z-6171f6c2/ENB** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'directional_claim_without_event_type': 1, 'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 10 named publishers; 0 exact duplicates; 23 HTTPS source links; largest publisher share 26.09%; oldest publication 2026-11-11

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 47.1500 |
| Return 1D (%) | -0.2960 |
| Return 1W (%) | 0.1382 |
| Return 1M (%) | -0.5697 |
| Return YTD (%) | 4.0329 |
| Return 1Y (%) | 4.2072 |
| Annualized volatility (%) | 18.2230 |
| Beta vs SPY | -0.1110 |
| Max drawdown (%) | -19.8462 |
| Sharpe (rf=0) | 0.3179 |
| Downside deviation (rf=0, %) | 12.8749 |
| Sortino (rf=0) | 0.4499 |
| Historical VaR 95% (1D, %) | 1.7623 |
| Historical ES 95% (1D, %) | 2.5078 |
| Correlation vs SPY | -0.0839 |
| Tracking error vs SPY (%) | 23.7519 |
| P/E (trailing) | 22.78 |
| P/B | 2.43 |
| EV/EBITDA | 13.04 |
| Revenue growth (%) | 44.00 |
| Forward P/E (estimate) | 21.23 |
| Gross margin (%) | 30.20 |
| Operating margin (%) | 12.82 |
| Return on equity (%) | 9.85 |
| Free cash flow yield (%) | N/A |
| MA50 | 47.0756 |
| Close vs MA50 (%) | 0.1580 |
| MA200 | 50.7543 |
| Close vs MA200 (%) | -7.1014 |
| RSI (14, Wilder) | 47.6904 |
| MACD (12,26) | -0.0020 |
| MACD signal (9) | 0.0443 |
| MACD histogram | -0.0463 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ENB': 284, 'SPY': 284}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 47.1500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.2960 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.1382 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -0.5697 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 4.0329 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 4.2072 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 18.2230 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 12.8749 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4499 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.7623 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.5078 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.0839 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.7519 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1110 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -19.8462 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3179 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 21.2295 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 30.1950 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 12.8210 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.8490 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 22.7778 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 47.6904 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.0463 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 0.1580 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -7.1014 -> Clearly below the moving-average trend level.

## TAILWINDS

### Enbridge (TSX:ENB) Gets Government Backing For Woodfibre LNG Growth Plans
- Summary: Government backing supports Enbridge’s LNG growth plans, boosting future prospects.
- Date: 2026-11-16 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPZE9OQncyVDhZem5xYUZoOHM2T0t2UGZ5VDhWLUVKUmR1WUxxNV9na25WYWNzVTBsbTUwOGZzUXJDb1NZNXE0MmgxX1RCV0kwYkNLMnFYTVVfc3BCanFZT1NpY3lMb1B6U3lhYWhVSmJMV25YSmx3dGpBSTVQbThrUllHbUUtbThGUkR6dTlMN2VpX2M?oc=5>

### Enbridge: A 5.7% Yield With A Growing Cash Flow Engine
- Summary: Enbridge offers a 5.7% yield, backed by growing cash flow, appealing to income-focused investors.
- Date: 2026-11-15 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPMS1jMXRwUmtyTHB6ajVMN25ESzBBNkpPb3lTOXhxT2lBXy1Nang5VlFKNXlqamxVZkJLN3FWVkhza25yMnpfRGRKSjNVbEtOVlZWQ0VSRUFYbkVRTzdVcF8tYkZFbzFDRmRjSHNtcGI1c01qcG1OeVlscWdpa0NjOXpYQUFWMkdIMTlhcUgtbGVGeUN3RVFFYXpqdWhPbUlTbWFN?oc=5>

### Enbridge Q3: The Market Isn't Paying Attention To The Near 6% Yield And $38 Billion Backlog
- Summary: Q3 results highlight a near 6% yield and $38B backlog, indicating strong performance.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxQZUQ1UW5sOUlMU0lhbkx0VHRpNUEwa2liM3JMWktuWlZMdXpRN3lmUFU2ZnFSTG00VS1PVWtxR1VWV0NTS1FoZUt3UGp3dTQzWE9qOW1IWFVsZFNiMWN2Q0FPbmhrTTBrRXQwdE5KM1dzME9YbTN6Mndfd0gyOHdTQ0ZOWnFRbWhscTF1dFVhMnlDVS1ibkdyc1lSUzljY25aMWR2aTQ4TkVXVWdWV3NpS0FFdFY1SnhnZFR5eTFIUHRIOWFhX1QxREZmaE1RX2xKTHc?oc=5>

### Enbridge: The 6% Yielder I'd Put In My IRA
- Summary: Investor endorses Enbridge’s 6% yield as a solid IRA investment.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxOM2ZITU1hSUU4Q2lCOEhidHNfZXZVTk1xS2hrYV8ydlpaWEVQSEpUVllxZjN1a0ZXRHpaSUxET2szeUNuaGp5LWlkU21pc2ZvTWFMdUxOYlFYb3dEREhCcHhaNzlabFFGWnVDLUVaRnlzYzgyTWNmSU1tVTBuZno4aUFULTVOWEJiT1dILS05NUlyUQ?oc=5>

### Better High-Yield Dividend Stock: Altria vs. Enbridge
- Summary: Comparison of high-yield dividend stocks, positioning Enbridge favorably.
- Date: 2026-11-13 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxQZEJVeHBGS19WUi1QdEdyM3I3dGhDSThleDd5SEVXc2VkdUNGMGUyU1JidXZFN080UFBpbHdqV3o2UnJwZHoyU3RYT0tWY0pxVXdhWVVDcU05TEZKZFNZN2tLaWxDM3BYLUJkaUtMVTBlNzAzOXVSa25yMV9HcVU0RzBSQUo?oc=5>

### Enbridge (NYSE:ENB) Keeps Energy Flowing. What’s Next?
- Summary: Article discusses Enbridge’s continued energy operations and future prospects.
- Date: 2026-11-14 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPdEFlNi1lU3ZnelRIcXVwU0taNUFJUUFuWWozWV80WmNjTHg4RnJ4S1pmbFg0OFVsTUtsQUIzV05jdnp0LU9uRmRqTldleWhwNWt2amRGMmlQWFlSamNvNmhiZFQxVGstQXZUOHlVSUdHdzZ0QTByczVPVnFvMG1vS3NYblotLUVPMzFDV0RMWVlNd01i?oc=5>

## HEADWINDS

### Enbridge: A 32nd Raise Looks Likely, But I Will Wait For A Better Yield (Hold)
- Summary: Potential dividend raise may be delayed, signaling cautious outlook.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxPeE0tNzBWUXFDNTloQmhuZkpLbTNLS0hwNFRFV25ZM1pvZk5ocENGTVR0ODZ4bUhmODVWV1o5bUVfUzB5Z0F3c0FXeVlLdjFNTnFYOC1IenN4TXc0bE5RNGxzVWNVZ3UwVHQ4MlRIZzB2ejQwaGdPUko3a01FQkJXRlZTTDFqaHliQnRRYzNBdklIRHJpdkVvU1Y3bWhqVmZlTlBoSHE5MWlrRk5jNHhz?oc=5>

## CATALYSTS

### Enbridge (TSX:ENB) Stock Looks About Right As Acquisition Activity Builds
- Summary: Enbridge (TSX:ENB) Stock Looks About Right As Acquisition Activity Builds
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQSXh0dmJGNGdveTZKcjE3SnljM2ltLUYtaS0wRXZrMEhkSndzVW9jeTNHdjh6OUFOM3RkRzQ2Qk8yajNrQzgzTXV4QUxlQUFCX1dRU0xNM0QyMWphNDFTOXczWVNxdHNKM3VUX3RXUnBBeHBuLXY2anNjem1ic3I0VDFrLVhCVXpUbWFVQUlZNWVRUGc2WFpqYw?oc=5>

### Enbridge or Enterprise Products: I Can Only Pick One Dividend Stock for the Next 10 Years. Here’s Mine
- Summary: Enbridge or Enterprise Products: I Can Only Pick One Dividend Stock for the Next 10 Years. Here’s Mine
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxPMFJsXzYyb05DZG10el9QY1NISVhPNVVPOEp4c2lFbTVCSDVqYjVjZ0VVazQxZmV0XzdRaXdQeEtRWDh4cGszay1vNVVLczROUkM2WXJJbGgtcjNVVFZZdzNRc1FOeHdmbnlZRzhUR3ZxTzJpeWphOGpTQUsxTjRGS09VQTVqT0g3XzBJTWt4VENrZGdJSk9Jdy02allKV1lEdHFFR1dSS0ZmelMwdC1SOVV3ZU93RVdPWldDQzlTRUM2SXpH?oc=5>

### How Strong Quarterly Results Will Impact Enbridge (TSX:ENB) Investors
- Summary: Strong quarterly results could positively influence investor sentiment.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxOUlg0aDAyOXV5WXdja0ctQkRrTmxHOFpGMEc2Ty1tUm1zS3RSU3VRdTVXR1ktOThQQnQtcWh4RE5VZGdvUGVlazdHb1o4dFpfMlNRdURBbHdadFBTdGRFQ09GemF3bXNFRFVzNTNNQXM4cjJQWjNtcXZ0NG5DUEJNQUJaY2FjaTB6UlIzbi1jTkswdG55MXE5Y0sxdEwwNHJPZXlSRm5RbE0?oc=5>

### Enbridge stock completes subordinated note offering
- Summary: Enbridge has finished issuing subordinated notes, raising capital to support its operations and future projects.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxOMnZra0xCWVlNUm1UeGdXN1JQRVZNTTRJdFZMTWlLcFNaWWVkZ1ZqVXJoZVFsWnkwaHZFSWR2VFpEZWJlQnpBUFRIeFNYTWFzaGpWTy1qaXJKTTl2VlNIX0lBOTBPTGUxZ3IzUlVOQ3o3UHFudlhjdWNkV0ZtcnZWci1YZGh5WFJFV2dSQ3A4SThodUNJemFIMUlCNjZYVTdrYnpseV9ZV1BYUllIZ19rdWtTNmU?oc=5>

### Enbridge: The Moat Is Holding, But Growth Is Stalling (Rating Downgrade) (NYSE:ENB)
- Summary: Rating downgrade signals potential earnings pressure.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOU0dUd0NGX3lZQzNDRm5mM01aWWEyYjVob0t2NG1mdml2aUlVQ3ZWUERpZUFnN3NlR29uUk03TFMtWWdNM2dEVzEweWt1S1lWb1Vqdlk0cnZYYkFpY3UtdW85ZFVGOTVZdUJ6aDFpZE8wNUIxc1YtZjEyVW5wdG5tczRDazBnWmlnR3Z6N1JzZ2NPVEY2cDlv?oc=5>

### Enbridge management transition and asset deals: Can ENB regain momentum?
- Summary: Management shift and asset deals may boost growth.
- Date: 2026-11-17 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxNNy1zNDVUM2VubEdEMHM2d1lSNXBlLVBKOWpqSHRRSkNnbmJVMnRpU2FjR3lLaFEtTW5GTWQ0a2UtaHpQYkR3WWF1Y09XRVdaRDk2dVZHeVdnRHVSM3RXbElYMWx6aTE5dFlGZGFfWWxYdlY2LVFybGtYRG5KT0N6R0hjTzdnRk5EUTVlUEVROUFlWXM?oc=5>

### Enbridge's North Dakota pipeline system shut over contamination concerns - Argus (ENB:NYSE)
- Summary: Pipeline shutdown raises operational risk.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxORTBsOUFTNmxkZWFfSkExdXE3NVNRWFg2TlAtZk9rNld0Q0prSWxIb2FWU3ZDQUhjclgzOENUcWpLSlhZaVFzWlU3RDM0VU9qYldWa3lMSGVMM0hKNjNqMG1kNnZiRmp5VmFHdHZjM01QT0Y2cE12N3U5RnBtNkpXakhORTdRdXI4X3V6SFVGUFZsTTQ5Tzg5a3c2QnpQVHJkVzU1ME1hZ3JNSW9IRi1mMUFRSTVFQQ?oc=5>

### Enbridge stock: company completes US dollar 1.1 billion notes
- Summary: Debt issuance increases financial leverage.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxNLTdhNk5sYVE2dWRvZmRsbUx0OFh4emNIUXJhYTdZOFdfVC1PVVhWNWpuQXNhb1RuN1ZmbWdGemVDcVN2Z3c4QlVhRkxpWHk0NWNUTl84WUxVZlNhSFNldnpjeWozZ1Joc1YyblF5eGdrWEJ2UE0xWlQwdzg5Mlh3ZF8wZ1doWmdjOWx4Q05BRjhCUVRaR1lfYmlUc1RHSjA3MW40R25mNG0zU1MxUlYxU1g0a29PMVVHclYxZGZBZGo?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ENB** | **22.78** | **2.43** | **13.04** | **44.00** | **105,092,079,616.00 USD** | **4.21** |
| TRP.TO | 24.98 | 3.75 | 16.74 | 8.80 | 96,009,240,576.00 CAD | 25.31 |
| KMI | 19.57 | 2.24 | 13.58 | 9.30 | 70,618,578,944.00 USD | 21.20 |
| EPD | 12.40 | 2.61 | 10.80 | 49.30 | 79,406,194,688.00 USD | 23.11 |

Peers fetched as_of: 2026-11-17; ENB reuses existing data (market data as_of: 2026-11-17); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-06
- Next expected earnings: 2027-02-12 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-17

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-06
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: https://www.sec.gov/Archives/edgar/data/895728/000119312526450714/enb-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMikwFBVV95cUxPZE9OQncyVDhZem5xYUZoOHM2T0t2UGZ5VDhWLUVKUmR1WUxxNV9na25WYWNzVTBsbTUwOGZzUXJDb1NZNXE0MmgxX1RCV0kwYkNLMnFYTVVfc3BCanFZT1NpY3lMb1B6U3lhYWhVSmJMV25YSmx3dGpBSTVQbThrUllHbUUtbThGUkR6dTlMN2VpX2M?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPMS1jMXRwUmtyTHB6ajVMN25ESzBBNkpPb3lTOXhxT2lBXy1Nang5VlFKNXlqamxVZkJLN3FWVkhza25yMnpfRGRKSjNVbEtOVlZWQ0VSRUFYbkVRTzdVcF8tYkZFbzFDRmRjSHNtcGI1c01qcG1OeVlscWdpa0NjOXpYQUFWMkdIMTlhcUgtbGVGeUN3RVFFYXpqdWhPbUlTbWFN?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxQZUQ1UW5sOUlMU0lhbkx0VHRpNUEwa2liM3JMWktuWlZMdXpRN3lmUFU2ZnFSTG00VS1PVWtxR1VWV0NTS1FoZUt3UGp3dTQzWE9qOW1IWFVsZFNiMWN2Q0FPbmhrTTBrRXQwdE5KM1dzME9YbTN6Mndfd0gyOHdTQ0ZOWnFRbWhscTF1dFVhMnlDVS1ibkdyc1lSUzljY25aMWR2aTQ4TkVXVWdWV3NpS0FFdFY1SnhnZFR5eTFIUHRIOWFhX1QxREZmaE1RX2xKTHc?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxOM2ZITU1hSUU4Q2lCOEhidHNfZXZVTk1xS2hrYV8ydlpaWEVQSEpUVllxZjN1a0ZXRHpaSUxET2szeUNuaGp5LWlkU21pc2ZvTWFMdUxOYlFYb3dEREhCcHhaNzlabFFGWnVDLUVaRnlzYzgyTWNmSU1tVTBuZno4aUFULTVOWEJiT1dILS05NUlyUQ?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxQZEJVeHBGS19WUi1QdEdyM3I3dGhDSThleDd5SEVXc2VkdUNGMGUyU1JidXZFN080UFBpbHdqV3o2UnJwZHoyU3RYT0tWY0pxVXdhWVVDcU05TEZKZFNZN2tLaWxDM3BYLUJkaUtMVTBlNzAzOXVSa25yMV9HcVU0RzBSQUo?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPdEFlNi1lU3ZnelRIcXVwU0taNUFJUUFuWWozWV80WmNjTHg4RnJ4S1pmbFg0OFVsTUtsQUIzV05jdnp0LU9uRmRqTldleWhwNWt2amRGMmlQWFlSamNvNmhiZFQxVGstQXZUOHlVSUdHdzZ0QTByczVPVnFvMG1vS3NYblotLUVPMzFDV0RMWVlNd01i?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxPeE0tNzBWUXFDNTloQmhuZkpLbTNLS0hwNFRFV25ZM1pvZk5ocENGTVR0ODZ4bUhmODVWV1o5bUVfUzB5Z0F3c0FXeVlLdjFNTnFYOC1IenN4TXc0bE5RNGxzVWNVZ3UwVHQ4MlRIZzB2ejQwaGdPUko3a01FQkJXRlZTTDFqaHliQnRRYzNBdklIRHJpdkVvU1Y3bWhqVmZlTlBoSHE5MWlrRk5jNHhz?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQSXh0dmJGNGdveTZKcjE3SnljM2ltLUYtaS0wRXZrMEhkSndzVW9jeTNHdjh6OUFOM3RkRzQ2Qk8yajNrQzgzTXV4QUxlQUFCX1dRU0xNM0QyMWphNDFTOXczWVNxdHNKM3VUX3RXUnBBeHBuLXY2anNjem1ic3I0VDFrLVhCVXpUbWFVQUlZNWVRUGc2WFpqYw?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxPMFJsXzYyb05DZG10el9QY1NISVhPNVVPOEp4c2lFbTVCSDVqYjVjZ0VVazQxZmV0XzdRaXdQeEtRWDh4cGszay1vNVVLczROUkM2WXJJbGgtcjNVVFZZdzNRc1FOeHdmbnlZRzhUR3ZxTzJpeWphOGpTQUsxTjRGS09VQTVqT0g3XzBJTWt4VENrZGdJSk9Jdy02allKV1lEdHFFR1dSS0ZmelMwdC1SOVV3ZU93RVdPWldDQzlTRUM2SXpH?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxOUlg0aDAyOXV5WXdja0ctQkRrTmxHOFpGMEc2Ty1tUm1zS3RSU3VRdTVXR1ktOThQQnQtcWh4RE5VZGdvUGVlazdHb1o4dFpfMlNRdURBbHdadFBTdGRFQ09GemF3bXNFRFVzNTNNQXM4cjJQWjNtcXZ0NG5DUEJNQUJaY2FjaTB6UlIzbi1jTkswdG55MXE5Y0sxdEwwNHJPZXlSRm5RbE0?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxOMnZra0xCWVlNUm1UeGdXN1JQRVZNTTRJdFZMTWlLcFNaWWVkZ1ZqVXJoZVFsWnkwaHZFSWR2VFpEZWJlQnpBUFRIeFNYTWFzaGpWTy1qaXJKTTl2VlNIX0lBOTBPTGUxZ3IzUlVOQ3o3UHFudlhjdWNkV0ZtcnZWci1YZGh5WFJFV2dSQ3A4SThodUNJemFIMUlCNjZYVTdrYnpseV9ZV1BYUllIZ19rdWtTNmU?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOU0dUd0NGX3lZQzNDRm5mM01aWWEyYjVob0t2NG1mdml2aUlVQ3ZWUERpZUFnN3NlR29uUk03TFMtWWdNM2dEVzEweWt1S1lWb1Vqdlk0cnZYYkFpY3UtdW85ZFVGOTVZdUJ6aDFpZE8wNUIxc1YtZjEyVW5wdG5tczRDazBnWmlnR3Z6N1JzZ2NPVEY2cDlv?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxNNy1zNDVUM2VubEdEMHM2d1lSNXBlLVBKOWpqSHRRSkNnbmJVMnRpU2FjR3lLaFEtTW5GTWQ0a2UtaHpQYkR3WWF1Y09XRVdaRDk2dVZHeVdnRHVSM3RXbElYMWx6aTE5dFlGZGFfWWxYdlY2LVFybGtYRG5KT0N6R0hjTzdnRk5EUTVlUEVROUFlWXM?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxORTBsOUFTNmxkZWFfSkExdXE3NVNRWFg2TlAtZk9rNld0Q0prSWxIb2FWU3ZDQUhjclgzOENUcWpLSlhZaVFzWlU3RDM0VU9qYldWa3lMSGVMM0hKNjNqMG1kNnZiRmp5VmFHdHZjM01QT0Y2cE12N3U5RnBtNkpXakhORTdRdXI4X3V6SFVGUFZsTTQ5Tzg5a3c2QnpQVHJkVzU1ME1hZ3JNSW9IRi1mMUFRSTVFQQ?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxNLTdhNk5sYVE2dWRvZmRsbUx0OFh4emNIUXJhYTdZOFdfVC1PVVhWNWpuQXNhb1RuN1ZmbWdGemVDcVN2Z3c4QlVhRkxpWHk0NWNUTl84WUxVZlNhSFNldnpjeWozZ1Joc1YyblF5eGdrWEJ2UE0xWlQwdzg5Mlh3ZF8wZ1doWmdjOWx4Q05BRjhCUVRaR1lfYmlUc1RHSjA3MW40R25mNG0zU1MxUlYxU1g0a29PMVVHclYxZGZBZGo?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
