# ENB Intelligence Report

- ticker: **ENB**
- Report as_of: **2026-11-08**
- Market data as_of: **2026-11-06**
- Quant sources: https://finance.yahoo.com/quote/ENB/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ENB/key-statistics/
- AI analysis snapshot as_of: **2026-11-08**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-09T04:48:08.029707+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 12, 'rule': 7, 'ai': 3, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261108T041758Z-43fb2458/ENB** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 12 unique headlines; 8 named publishers; 0 exact duplicates; 12 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-11-02

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 46.8900 |
| Return 1D (%) | -2.5359 |
| Return 1W (%) | -5.1961 |
| Return 1M (%) | 0.7520 |
| Return YTD (%) | 1.9969 |
| Return 1Y (%) | 4.0638 |
| Annualized volatility (%) | 18.3119 |
| Beta vs SPY | -0.1220 |
| Max drawdown (%) | -19.8462 |
| Sharpe (rf=0) | 0.3097 |
| Downside deviation (rf=0, %) | 12.9069 |
| Sortino (rf=0) | 0.4393 |
| Historical VaR 95% (1D, %) | 1.7623 |
| Historical ES 95% (1D, %) | 2.5078 |
| Correlation vs SPY | -0.0902 |
| Tracking error vs SPY (%) | 23.7427 |
| P/E (trailing) | 22.65 |
| P/B | 2.42 |
| EV/EBITDA | 13.01 |
| Revenue growth (%) | 44.00 |
| Forward P/E (estimate) | 20.71 |
| Gross margin (%) | 30.20 |
| Operating margin (%) | 10.50 |
| Return on equity (%) | 9.85 |
| Free cash flow yield (%) | N/A |
| MA50 | 48.1018 |
| Close vs MA50 (%) | -2.5192 |
| MA200 | 51.4346 |
| Close vs MA200 (%) | -8.8356 |
| RSI (14, Wilder) | 38.8339 |
| MACD (12,26) | 0.1254 |
| MACD signal (9) | 0.1592 |
| MACD histogram | -0.0339 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ENB': 277, 'SPY': 277}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 46.8900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.5359 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -5.1961 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 0.7520 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 1.9969 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 4.0638 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 18.3119 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 12.9069 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4393 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.7623 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.5078 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.0902 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.7427 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1220 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -19.8462 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3097 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 20.7099 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 30.1950 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 10.5000 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.8490 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 22.6522 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 38.8339 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.0339 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -2.5192 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -8.8356 -> Clearly below the moving-average trend level.

## TAILWINDS

### Enbridge Reports Higher Earnings as Infrastructure Expansion Accelerates
- Summary: Enbridge Reports Higher Earnings as Infrastructure Expansion Accelerates
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxNVi1fTU5DanRvTTVlNVJzYjFqeW5oczNicXQ5V2p5ZzhRY2sxZ0t6RHdCRVFRaEQwUS1WUHMwMjhKNnJzN19hX2ZjZVI3alAteEk0aGJLTnVCbjdzemJwUWFvOV93Q3hSUUVXbUZEUndVblRkMm9NTGJJOWswTDl2S3htX1VPc01VTVRJNDc0QWVqZzN4TWIxbGdpWXRySmJNRWo1enhmbFlUREpaVkN2em91cTV3ZEpfaWU3cjA5M0lyQQ?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Enbridge (TSX:ENB) Q3 Results Keep Debt And Dividend In Focus
- Summary: Enbridge (TSX:ENB) Q3 Results Keep Debt And Dividend In Focus
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPQjA5aGxHUWFGbXVVNHN1SmhZdmx2VkMtbGdBVUlKNXJJWTZ4TnZ4RmFoZEl1VTlVOG9Xd1RIZWhVSGw5Q3VSeklvaW4yWUJZckdzcVd4MHo2d0o0RHUzUDl3X0FMYXJjYXhWRHZ1QzdHSGpSVkhfektLZnI4R2VyRVBjbkpRZGJORWtRcGlyeFRJZVYzbzVj?oc=5>

### Enbridge Prepares to Report Q3 Earnings: What's in the Cards?
- Summary: Enbridge Prepares to Report Q3 Earnings: What's in the Cards?
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxOUC11RTN2Y0RWTGVrOUhHLVFjallHY3Z3eXo2TnhCcnFNa0Mwdy1STjJvX3R3cm5vaFpmaGtnODFwaGlOc3BvYnFaN0tGbHhTNEhWNEtJSlI3VGhGSnFmVExESURZd1dCQUhJcG1WVDRSTTF3TUlHaTZxR0NsZHB2M0hpZktteEZMNjI4SG9IYm04eF9FYVEtZUgtRWdRZ0NrMFZJ?oc=5>

### Enbridge Inc. Declares Quarterly Dividends
- Summary: Enbridge Inc. Declares Quarterly Dividends
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPZ2V5RGJpRmoxNTd2amQ5MlhlX0txaXI3OXcxQ0YtSlBuNVp3dC0xZ1hTdUd5Sk9nVDh2UzZRWUZQQ1JlT2hqY1RnZFZqOXprUlFlcVhSTDhlNGFHcFZaY3h1cE5SOXRuZG03bExsaVB6U0xTNDVoV2hjYnk2VzRaSzBsT1NWUUx5X1RITE1TNW4ydnlwSkRmQXlKcWNaRHpCcXFuRDY3WmNGUQ?oc=5>

### Enbridge Inc. 2026 Q3 - Results - Earnings Call Presentation (TSX:ENB:CA) 2026-11-06
- Summary: Enbridge Inc. 2026 Q3 - Results - Earnings Call Presentation (TSX:ENB:CA) 2026-11-06
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOMjBPV3BCaUlQaFNHZFI2ZkJkeDd4TGNERHl1anozMjV1NGRKMG11ektmQ0lSbHctN0pzMmxHcTh3LXN4V0RaQVZqYk9STTJyUjFfQmJOTnFpRTQ1MVpuUnFBTUotZy01NV9LelFpeVJBb1RDQWphTGtoeUhVenEyYmFxVGRYeV9LUG4yQVZwMGltRUF2blY0R2VnSXU?oc=5>

### Enbridge Inc. (TSE:ENB) Stock Has Consensus Price Target of C$77.62 According to Brokerages
- Summary: Enbridge Inc. (TSE:ENB) Stock Has Consensus Price Target of C$77.62 According to Brokerages
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi5AFBVV95cUxNTVJBU09DTWdSZnFLbVZuLWxWYndlYUJ3bEdfakZKbllZYW5lVHA5bXo4aDlsT3RCS1ltNmxoM2Z1WVQ5dTJBc243cWFNaC1ucWRZczF5TU45eFotNkhIZnFoX3ZLNXc0SFdVd0NwQmhxcnpYOFdBQkpHRW5wVlV2cFBiY1FUdXFOd3RuWXZ6QV92RlJWaC1aQmtpVjRickZ2T3BzcEtEdEk2TGpGLS1EUmphNmFkT24zWnZZQ05hZjJYcndhU0RRLXE5aUVGX3VQSGw4Q1oycDk0b1ZFTTd6Z3I3TkE?oc=5>

### Enbridge Maintains Quarterly Common-Share Dividend at $0.9700
- Summary: Enbridge Maintains Quarterly Common-Share Dividend at $0.9700
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxQSFNwejJOS3lkai1rSXBIanV1UnVscWRRUjAydUJ2eEZLR1ZDbXg4ZV9MNGFJVmw0V1RJZEE0Yk1feXRFUks5eEVEcnlEclo4Q192Z0VNVFFJRjVGZ2o1aW5yOWxFVEIxLUhyc0pqa2VJSFlYd242bEg2QnBzOE5uX1ExWXZoOWwwTzJWSEYzU2R1S2hFVXJIeFFrcXlBODI0YVY4TkZCRmZZa2VodWFhTm93?oc=5>

### Stocks in play: Enbridge Inc.
- Summary: Enbridge shares are currently active in the market, indicating investor interest.
- Date: 2026-11-04 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTFBXZ01jUDVRSnF5TnZPVjdnNHhNQU5TamZqUTB1TGVhcGpRVldkSFNuV2ZjUkFGM2RTUXZRNkV2cXk0TklMVDFWOEV2eDJISWx1QTBNSXJHXzR1dnEybEh2NWJ3eEwyOVBwczEyb29Fa21XM2twYkpyNkIzSG9RUQ?oc=5>

### Enbridge may be interested in building pipeline for Canada's Pathways carbon capture project
- Summary: Enbridge shows interest in constructing a pipeline for the Pathways carbon capture initiative, potentially expanding its infrastructure portfolio.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxORXdoUkVVN1kySXJvSm5EM0t1NmFlU2lUbkpULXZUNmNUd28tYWRkR04xYm5qWUJwd0pxcnJZWXl1ZjhXU3ZRdXc0czhYb3QyY3lVUHUxU3ZWT0JmWnFwNElkdTBSakZDLWctUkVCdUxxZUJfUHpNVzdNWHFTejFFcmtDaExleHlybVNqTTk1NWgwckxZOUNaOTVhS2h1QUNMcTJmNTh2WWdLZzdwOGhyVngtYVd4eHgySWhUOVREMkItUlE4Vi1Zaw?oc=5>

## RISKS

### Why is Enbridge stock down 1.5% today?
- Summary: Enbridge shares fell 1.5% amid market volatility and investor concerns about future earnings.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxNTzI5djFBRWdwTkpDU0h5RDFZWUFGSUtpU1BTWjZfVHZxTkE5ckl0Si02R3pkT3dUdW5vZEo1ZU5wbDhpMUdJeHJjSmYwWGsxc04ydmFIQ3ZaeEloeVRfLWpaMGlSUDJTV3haTnYzVzZRSE10Q3R6SUd6QXI4Z01nVHJKYUwweFpnNlVpaFJXSVU?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ENB** | **22.65** | **2.42** | **13.01** | **44.00** | **104,512,561,152.00 USD** | **4.06** |
| TRP.TO | 23.59 | 3.56 | 16.26 | 8.80 | 91,175,436,288.00 CAD | 27.92 |
| KMI | 18.49 | 2.11 | 13.08 | 9.30 | 66,742,349,824.00 USD | 19.02 |
| EPD | 12.26 | 2.64 | N/A | 49.30 | 79,859,081,216.00 USD | 26.93 |

Peers fetched as_of: 2026-11-08; ENB reuses existing data (market data as_of: 2026-11-06); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-06
- Next expected earnings: 2027-02-12 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-08

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMiwgFBVV95cUxNVi1fTU5DanRvTTVlNVJzYjFqeW5oczNicXQ5V2p5ZzhRY2sxZ0t6RHdCRVFRaEQwUS1WUHMwMjhKNnJzN19hX2ZjZVI3alAteEk0aGJLTnVCbjdzemJwUWFvOV93Q3hSUUVXbUZEUndVblRkMm9NTGJJOWswTDl2S3htX1VPc01VTVRJNDc0QWVqZzN4TWIxbGdpWXRySmJNRWo1enhmbFlUREpaVkN2em91cTV3ZEpfaWU3cjA5M0lyQQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPQjA5aGxHUWFGbXVVNHN1SmhZdmx2VkMtbGdBVUlKNXJJWTZ4TnZ4RmFoZEl1VTlVOG9Xd1RIZWhVSGw5Q3VSeklvaW4yWUJZckdzcVd4MHo2d0o0RHUzUDl3X0FMYXJjYXhWRHZ1QzdHSGpSVkhfektLZnI4R2VyRVBjbkpRZGJORWtRcGlyeFRJZVYzbzVj?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxOUC11RTN2Y0RWTGVrOUhHLVFjallHY3Z3eXo2TnhCcnFNa0Mwdy1STjJvX3R3cm5vaFpmaGtnODFwaGlOc3BvYnFaN0tGbHhTNEhWNEtJSlI3VGhGSnFmVExESURZd1dCQUhJcG1WVDRSTTF3TUlHaTZxR0NsZHB2M0hpZktteEZMNjI4SG9IYm04eF9FYVEtZUgtRWdRZ0NrMFZJ?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPZ2V5RGJpRmoxNTd2amQ5MlhlX0txaXI3OXcxQ0YtSlBuNVp3dC0xZ1hTdUd5Sk9nVDh2UzZRWUZQQ1JlT2hqY1RnZFZqOXprUlFlcVhSTDhlNGFHcFZaY3h1cE5SOXRuZG03bExsaVB6U0xTNDVoV2hjYnk2VzRaSzBsT1NWUUx5X1RITE1TNW4ydnlwSkRmQXlKcWNaRHpCcXFuRDY3WmNGUQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOMjBPV3BCaUlQaFNHZFI2ZkJkeDd4TGNERHl1anozMjV1NGRKMG11ektmQ0lSbHctN0pzMmxHcTh3LXN4V0RaQVZqYk9STTJyUjFfQmJOTnFpRTQ1MVpuUnFBTUotZy01NV9LelFpeVJBb1RDQWphTGtoeUhVenEyYmFxVGRYeV9LUG4yQVZwMGltRUF2blY0R2VnSXU?oc=5
- https://news.google.com/rss/articles/CBMi5AFBVV95cUxNTVJBU09DTWdSZnFLbVZuLWxWYndlYUJ3bEdfakZKbllZYW5lVHA5bXo4aDlsT3RCS1ltNmxoM2Z1WVQ5dTJBc243cWFNaC1ucWRZczF5TU45eFotNkhIZnFoX3ZLNXc0SFdVd0NwQmhxcnpYOFdBQkpHRW5wVlV2cFBiY1FUdXFOd3RuWXZ6QV92RlJWaC1aQmtpVjRickZ2T3BzcEtEdEk2TGpGLS1EUmphNmFkT24zWnZZQ05hZjJYcndhU0RRLXE5aUVGX3VQSGw4Q1oycDk0b1ZFTTd6Z3I3TkE?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxQSFNwejJOS3lkai1rSXBIanV1UnVscWRRUjAydUJ2eEZLR1ZDbXg4ZV9MNGFJVmw0V1RJZEE0Yk1feXRFUks5eEVEcnlEclo4Q192Z0VNVFFJRjVGZ2o1aW5yOWxFVEIxLUhyc0pqa2VJSFlYd242bEg2QnBzOE5uX1ExWXZoOWwwTzJWSEYzU2R1S2hFVXJIeFFrcXlBODI0YVY4TkZCRmZZa2VodWFhTm93?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTFBXZ01jUDVRSnF5TnZPVjdnNHhNQU5TamZqUTB1TGVhcGpRVldkSFNuV2ZjUkFGM2RTUXZRNkV2cXk0TklMVDFWOEV2eDJISWx1QTBNSXJHXzR1dnEybEh2NWJ3eEwyOVBwczEyb29Fa21XM2twYkpyNkIzSG9RUQ?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxORXdoUkVVN1kySXJvSm5EM0t1NmFlU2lUbkpULXZUNmNUd28tYWRkR04xYm5qWUJwd0pxcnJZWXl1ZjhXU3ZRdXc0czhYb3QyY3lVUHUxU3ZWT0JmWnFwNElkdTBSakZDLWctUkVCdUxxZUJfUHpNVzdNWHFTejFFcmtDaExleHlybVNqTTk1NWgwckxZOUNaOTVhS2h1QUNMcTJmNTh2WWdLZzdwOGhyVngtYVd4eHgySWhUOVREMkItUlE4Vi1Zaw?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxNTzI5djFBRWdwTkpDU0h5RDFZWUFGSUtpU1BTWjZfVHZxTkE5ckl0Si02R3pkT3dUdW5vZEo1ZU5wbDhpMUdJeHJjSmYwWGsxc04ydmFIQ3ZaeEloeVRfLWpaMGlSUDJTV3haTnYzVzZRSE10Q3R6SUd6QXI4Z01nVHJKYUwweFpnNlVpaFJXSVU?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
