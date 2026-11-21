# ENB Intelligence Report

- ticker: **ENB**
- Report as_of: **2026-11-20**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/ENB/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ENB/key-statistics/
- AI analysis snapshot as_of: **2026-11-20**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-21T05:50:16.419415+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 15, 'rule': 4, 'ai': 8, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261120T053808Z-e360129e/ENB** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 15 unique headlines; 6 named publishers; 0 exact duplicates; 15 HTTPS source links; largest publisher share 26.67%; oldest publication 2026-11-15

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 45.6900 |
| Return 1D (%) | -0.5009 |
| Return 1W (%) | -4.1536 |
| Return 1M (%) | -3.2260 |
| Return YTD (%) | 0.8115 |
| Return 1Y (%) | -0.1695 |
| Annualized volatility (%) | 18.2845 |
| Beta vs SPY | -0.0759 |
| Max drawdown (%) | -19.8462 |
| Sharpe (rf=0) | 0.0818 |
| Downside deviation (rf=0, %) | 13.0227 |
| Sortino (rf=0) | 0.1148 |
| Historical VaR 95% (1D, %) | 1.8065 |
| Historical ES 95% (1D, %) | 2.5127 |
| Correlation vs SPY | -0.0593 |
| Tracking error vs SPY (%) | 23.8683 |
| P/E (trailing) | 22.18 |
| P/B | 2.35 |
| EV/EBITDA | 12.85 |
| Revenue growth (%) | 44.00 |
| Forward P/E (estimate) | 20.57 |
| Gross margin (%) | 30.20 |
| Operating margin (%) | 12.82 |
| Return on equity (%) | 9.85 |
| Free cash flow yield (%) | N/A |
| MA50 | 46.9621 |
| Close vs MA50 (%) | -2.7089 |
| MA200 | 50.7356 |
| Close vs MA200 (%) | -9.9450 |
| RSI (14, Wilder) | 35.7439 |
| MACD (12,26) | -0.2504 |
| MACD signal (9) | -0.0579 |
| MACD histogram | -0.1925 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ENB': 287, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 45.6900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.5009 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -4.1536 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -3.2260 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 0.8115 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -0.1695 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 18.2845 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 13.0227 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.1148 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.8065 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.5127 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.0593 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.8683 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.0759 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -19.8462 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.0818 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 20.5722 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 30.1950 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 12.8210 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.8490 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 22.1796 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 35.7439 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.1925 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -2.7089 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -9.9450 -> Clearly below the moving-average trend level.

## TAILWINDS

### Enbridge: A 5.7% Yield With A Growing Cash Flow Engine
- Summary: Enbridge offers a 5.7% yield, backed by growing cash flow, appealing to income-focused investors.
- Date: 2026-11-15 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPMS1jMXRwUmtyTHB6ajVMN25ESzBBNkpPb3lTOXhxT2lBXy1Nang5VlFKNXlqamxVZkJLN3FWVkhza25yMnpfRGRKSjNVbEtOVlZWQ0VSRUFYbkVRTzdVcF8tYkZFbzFDRmRjSHNtcGI1c01qcG1OeVlscWdpa0NjOXpYQUFWMkdIMTlhcUgtbGVGeUN3RVFFYXpqdWhPbUlTbWFN?oc=5>

### Enbridge (TSX:ENB) Gets Government Backing For Woodfibre LNG Growth Plans
- Summary: Government backing supports Enbridge’s LNG growth plans, boosting future prospects.
- Date: 2026-11-16 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPZE9OQncyVDhZem5xYUZoOHM2T0t2UGZ5VDhWLUVKUmR1WUxxNV9na25WYWNzVTBsbTUwOGZzUXJDb1NZNXE0MmgxX1RCV0kwYkNLMnFYTVVfc3BCanFZT1NpY3lMb1B6U3lhYWhVSmJMV25YSmx3dGpBSTVQbThrUllHbUUtbThGUkR6dTlMN2VpX2M?oc=5>

## HEADWINDS

### Enbridge Inc. (TSX:ENB) Stock Under Pressure: 1.42% Decline Raises Valuation Concerns Despite Resilient Energy Infrastructure Business
- Summary: Enbridge Inc. (TSX:ENB) Stock Under Pressure: 1.42% Decline Raises Valuation Concerns Despite Resilient Energy Infrastructure Business
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7wFBVV95cUxQZlJ1WkpaNnoxRF9XaVNPZ1VPSEktb0Q1WW5zVll3bVA3UVIzR3dVTmZ3elJnZ2F5UlpjZ0ZhSkhJUFJ3RTBfU3h2cmc1b3MzNUFBcm13Tm42MHZZdEZTZlBwREFTbC1RVlRqNTN5RFdaRGtCbVdsNUVndkRSWGdIdlN2R01BX0FZQUtZblRUZldDSnNFQmpRLTZGaVFxazUyRjRDYjFta3J5cTAtTU1lR1Z3a2lkdHA3N0NfWk8wcjlKb2FWV18tNDFSRjU4RzRGQ0dEU1Bib2VmS1ZYU2wyTnhTYWh0ZVhuVzljaVhhVQ?oc=5>

### Enbridge shares technical analysis: Trading flat under seller pressure near key support
- Summary: Enbridge shares technical analysis: Trading flat under seller pressure near key support
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPeGxzNTdkZDYwTWc0WUFSQ0pwYzJLS1RMV1lEWGM3eEMtVmFhOTBfTXp4SFpvSl93dUwwZnAyaWpIWXdSYVRUcXhJandYaGtXb1FyWWpDMXktNUJ0dzkzdk83c1dRekctdEFJbk9TRU1VM1lObjZmY2U3bEhPTWp4VTNWeXZ2ZGdjLUJ6Y0RYbnR4aFU?oc=5>

### Enbridge: A 32nd Raise Looks Likely, But I Will Wait For A Better Yield (Hold)
- Summary: Potential dividend raise may be delayed, signaling cautious outlook.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxPeE0tNzBWUXFDNTloQmhuZkpLbTNLS0hwNFRFV25ZM1pvZk5ocENGTVR0ODZ4bUhmODVWV1o5bUVfUzB5Z0F3c0FXeVlLdjFNTnFYOC1IenN4TXc0bE5RNGxzVWNVZ3UwVHQ4MlRIZzB2ejQwaGdPUko3a01FQkJXRlZTTDFqaHliQnRRYzNBdklIRHJpdkVvU1Y3bWhqVmZlTlBoSHE5MWlrRk5jNHhz?oc=5>

## CATALYSTS

### Enbridge (TSX:ENB) Stock Looks About Right As Acquisition Activity Builds
- Summary: Enbridge (TSX:ENB) Stock Looks About Right As Acquisition Activity Builds
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQSXh0dmJGNGdveTZKcjE3SnljM2ltLUYtaS0wRXZrMEhkSndzVW9jeTNHdjh6OUFOM3RkRzQ2Qk8yajNrQzgzTXV4QUxlQUFCX1dRU0xNM0QyMWphNDFTOXczWVNxdHNKM3VUX3RXUnBBeHBuLXY2anNjem1ic3I0VDFrLVhCVXpUbWFVQUlZNWVRUGc2WFpqYw?oc=5>

### Enbridge Stock: Is It Still a Top Passive Income Pick for Retirees?
- Summary: Enbridge Stock: Is It Still a Top Passive Income Pick for Retirees?
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxNaHJLNGp5dW44UnlHVEhKMmZvazQ0bmJpV2x4bGtlMjM3MURBUHBYSEtpbFJid3hYdkRKZzhiNUJwWnluSWFJLUczNEo2clNxYkx6eEhvSVJzWks4VjU4Q0IydGVVbEZNMlVzWmoyeEdCUFNsbkVKT1JGUlhDQUNVZDdFYUlsUncw?oc=5>

### Enbridge: The Moat Is Holding, But Growth Is Stalling (Rating Downgrade) (NYSE:ENB)
- Summary: Rating downgrade signals potential earnings pressure.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOU0dUd0NGX3lZQzNDRm5mM01aWWEyYjVob0t2NG1mdml2aUlVQ3ZWUERpZUFnN3NlR29uUk03TFMtWWdNM2dEVzEweWt1S1lWb1Vqdlk0cnZYYkFpY3UtdW85ZFVGOTVZdUJ6aDFpZE8wNUIxc1YtZjEyVW5wdG5tczRDazBnWmlnR3Z6N1JzZ2NPVEY2cDlv?oc=5>

### Enbridge: My Verdict Is Buy – Here’s the Dividend $6,000 Would Collect
- Summary: Analyst recommends buying Enbridge, citing attractive dividend potential.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi5AFBVV95cUxNVXlpWFk4TDVSdDM5cUJrT0Y1Tm1yZkdlbUhFTDJaSHR6eG91bjNZb0NUeDRpUmJld3V5WDc0bngyN05qQlRacDYyM3Q2UHhPaDdzWEhIOFNwdEJPeUxhQlZnbUtfOU5OYXRHam1ZcF9XQ01ET2F0NHFvbmlnWnJoVFNIQVJwaUxvZGhNRkt6bXpsTzR4VVNHY3lfQ2Y3YlVLQWpfbG9uV3VZX0Y2RkEwUVVvVFpOcUx1QUFGdHE2Vk9ULVZkVXktVnRyQ3NWdGtEeDNtLUpxYlI2bW5XTDI5OURGTGc?oc=5>

### Enbridge management transition and asset deals: Can ENB regain momentum?
- Summary: Management shift and asset deals may boost growth.
- Date: 2026-11-17 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxNNy1zNDVUM2VubEdEMHM2d1lSNXBlLVBKOWpqSHRRSkNnbmJVMnRpU2FjR3lLaFEtTW5GTWQ0a2UtaHpQYkR3WWF1Y09XRVdaRDk2dVZHeVdnRHVSM3RXbElYMWx6aTE5dFlGZGFfWWxYdlY2LVFybGtYRG5KT0N6R0hjTzdnRk5EUTVlUEVROUFlWXM?oc=5>

### Enbridge's North Dakota pipeline system shut over contamination concerns - Argus (ENB:NYSE)
- Summary: Pipeline shutdown raises operational risk.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxORTBsOUFTNmxkZWFfSkExdXE3NVNRWFg2TlAtZk9rNld0Q0prSWxIb2FWU3ZDQUhjclgzOENUcWpLSlhZaVFzWlU3RDM0VU9qYldWa3lMSGVMM0hKNjNqMG1kNnZiRmp5VmFHdHZjM01QT0Y2cE12N3U5RnBtNkpXakhORTdRdXI4X3V6SFVGUFZsTTQ5Tzg5a3c2QnpQVHJkVzU1ME1hZ3JNSW9IRi1mMUFRSTVFQQ?oc=5>

### Enbridge sees major pension fund stake increase: Can ENB recover from persistent seller pressure?
- Summary: A major pension fund increased its stake in Enbridge, potentially supporting the stock amid seller pressure.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxQaXhhWEZvc0RCYUF0M0pibEVYRzBLc0xGenBmdkZUdG1IY2F2a2d1M0ZuMVF1ODlEc09IQ0FZVEhYTUZ5U2NXY0VRZ1NiLXFaT3RVRXNBV2ZiNDB4VDZXdGJRLUFSSmpNeFJvQVJDZXdScGREMXotSldaTndGaDZzbW5IYlJld1NST29PQlJTZzJNdw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ENB** | **22.18** | **2.35** | **12.85** | **44.00** | **101,837,889,536.00 USD** | **-0.17** |
| TRP.TO | 23.75 | 3.63 | 16.42 | 8.80 | 92,800,598,016.00 CAD | 21.30 |
| KMI | 19.22 | 2.14 | 13.20 | 9.30 | 67,633,438,720.00 USD | 17.91 |
| EPD | 11.86 | 2.54 | 10.60 | 49.30 | 77,271,154,688.00 USD | 19.28 |

Peers fetched as_of: 2026-11-20; ENB reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-06
- Next expected earnings: 2027-02-12 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-20

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

- https://news.google.com/rss/articles/CBMiowFBVV95cUxPMS1jMXRwUmtyTHB6ajVMN25ESzBBNkpPb3lTOXhxT2lBXy1Nang5VlFKNXlqamxVZkJLN3FWVkhza25yMnpfRGRKSjNVbEtOVlZWQ0VSRUFYbkVRTzdVcF8tYkZFbzFDRmRjSHNtcGI1c01qcG1OeVlscWdpa0NjOXpYQUFWMkdIMTlhcUgtbGVGeUN3RVFFYXpqdWhPbUlTbWFN?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPZE9OQncyVDhZem5xYUZoOHM2T0t2UGZ5VDhWLUVKUmR1WUxxNV9na25WYWNzVTBsbTUwOGZzUXJDb1NZNXE0MmgxX1RCV0kwYkNLMnFYTVVfc3BCanFZT1NpY3lMb1B6U3lhYWhVSmJMV25YSmx3dGpBSTVQbThrUllHbUUtbThGUkR6dTlMN2VpX2M?oc=5
- https://news.google.com/rss/articles/CBMi7wFBVV95cUxQZlJ1WkpaNnoxRF9XaVNPZ1VPSEktb0Q1WW5zVll3bVA3UVIzR3dVTmZ3elJnZ2F5UlpjZ0ZhSkhJUFJ3RTBfU3h2cmc1b3MzNUFBcm13Tm42MHZZdEZTZlBwREFTbC1RVlRqNTN5RFdaRGtCbVdsNUVndkRSWGdIdlN2R01BX0FZQUtZblRUZldDSnNFQmpRLTZGaVFxazUyRjRDYjFta3J5cTAtTU1lR1Z3a2lkdHA3N0NfWk8wcjlKb2FWV18tNDFSRjU4RzRGQ0dEU1Bib2VmS1ZYU2wyTnhTYWh0ZVhuVzljaVhhVQ?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPeGxzNTdkZDYwTWc0WUFSQ0pwYzJLS1RMV1lEWGM3eEMtVmFhOTBfTXp4SFpvSl93dUwwZnAyaWpIWXdSYVRUcXhJandYaGtXb1FyWWpDMXktNUJ0dzkzdk83c1dRekctdEFJbk9TRU1VM1lObjZmY2U3bEhPTWp4VTNWeXZ2ZGdjLUJ6Y0RYbnR4aFU?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxPeE0tNzBWUXFDNTloQmhuZkpLbTNLS0hwNFRFV25ZM1pvZk5ocENGTVR0ODZ4bUhmODVWV1o5bUVfUzB5Z0F3c0FXeVlLdjFNTnFYOC1IenN4TXc0bE5RNGxzVWNVZ3UwVHQ4MlRIZzB2ejQwaGdPUko3a01FQkJXRlZTTDFqaHliQnRRYzNBdklIRHJpdkVvU1Y3bWhqVmZlTlBoSHE5MWlrRk5jNHhz?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQSXh0dmJGNGdveTZKcjE3SnljM2ltLUYtaS0wRXZrMEhkSndzVW9jeTNHdjh6OUFOM3RkRzQ2Qk8yajNrQzgzTXV4QUxlQUFCX1dRU0xNM0QyMWphNDFTOXczWVNxdHNKM3VUX3RXUnBBeHBuLXY2anNjem1ic3I0VDFrLVhCVXpUbWFVQUlZNWVRUGc2WFpqYw?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxNaHJLNGp5dW44UnlHVEhKMmZvazQ0bmJpV2x4bGtlMjM3MURBUHBYSEtpbFJid3hYdkRKZzhiNUJwWnluSWFJLUczNEo2clNxYkx6eEhvSVJzWks4VjU4Q0IydGVVbEZNMlVzWmoyeEdCUFNsbkVKT1JGUlhDQUNVZDdFYUlsUncw?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOU0dUd0NGX3lZQzNDRm5mM01aWWEyYjVob0t2NG1mdml2aUlVQ3ZWUERpZUFnN3NlR29uUk03TFMtWWdNM2dEVzEweWt1S1lWb1Vqdlk0cnZYYkFpY3UtdW85ZFVGOTVZdUJ6aDFpZE8wNUIxc1YtZjEyVW5wdG5tczRDazBnWmlnR3Z6N1JzZ2NPVEY2cDlv?oc=5
- https://news.google.com/rss/articles/CBMi5AFBVV95cUxNVXlpWFk4TDVSdDM5cUJrT0Y1Tm1yZkdlbUhFTDJaSHR6eG91bjNZb0NUeDRpUmJld3V5WDc0bngyN05qQlRacDYyM3Q2UHhPaDdzWEhIOFNwdEJPeUxhQlZnbUtfOU5OYXRHam1ZcF9XQ01ET2F0NHFvbmlnWnJoVFNIQVJwaUxvZGhNRkt6bXpsTzR4VVNHY3lfQ2Y3YlVLQWpfbG9uV3VZX0Y2RkEwUVVvVFpOcUx1QUFGdHE2Vk9ULVZkVXktVnRyQ3NWdGtEeDNtLUpxYlI2bW5XTDI5OURGTGc?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxNNy1zNDVUM2VubEdEMHM2d1lSNXBlLVBKOWpqSHRRSkNnbmJVMnRpU2FjR3lLaFEtTW5GTWQ0a2UtaHpQYkR3WWF1Y09XRVdaRDk2dVZHeVdnRHVSM3RXbElYMWx6aTE5dFlGZGFfWWxYdlY2LVFybGtYRG5KT0N6R0hjTzdnRk5EUTVlUEVROUFlWXM?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxORTBsOUFTNmxkZWFfSkExdXE3NVNRWFg2TlAtZk9rNld0Q0prSWxIb2FWU3ZDQUhjclgzOENUcWpLSlhZaVFzWlU3RDM0VU9qYldWa3lMSGVMM0hKNjNqMG1kNnZiRmp5VmFHdHZjM01QT0Y2cE12N3U5RnBtNkpXakhORTdRdXI4X3V6SFVGUFZsTTQ5Tzg5a3c2QnpQVHJkVzU1ME1hZ3JNSW9IRi1mMUFRSTVFQQ?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxQaXhhWEZvc0RCYUF0M0pibEVYRzBLc0xGenBmdkZUdG1IY2F2a2d1M0ZuMVF1ODlEc09IQ0FZVEhYTUZ5U2NXY0VRZ1NiLXFaT3RVRXNBV2ZiNDB4VDZXdGJRLUFSSmpNeFJvQVJDZXdScGREMXotSldaTndGaDZzbW5IYlJld1NST29PQlJTZzJNdw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
