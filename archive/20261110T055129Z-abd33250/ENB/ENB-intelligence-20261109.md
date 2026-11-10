# ENB Intelligence Report

- ticker: **ENB**
- Report as_of: **2026-11-09**
- Market data as_of: **2026-11-09**
- Quant sources: https://finance.yahoo.com/quote/ENB/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ENB/key-statistics/
- AI analysis snapshot as_of: **2026-11-09**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-10T06:04:08.569537+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 14, 'rule': 5, 'ai': 7, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261109T043242Z-c8e908de/ENB** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'negative_sentiment_in_tailwinds': 1}
- RSS source audit (metadata only, not article fact-checking): 14 unique headlines; 6 named publishers; 0 exact duplicates; 14 HTTPS source links; largest publisher share 28.57%; oldest publication 2026-11-04

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 47.4000 |
| Return 1D (%) | 1.0877 |
| Return 1W (%) | -3.6585 |
| Return 1M (%) | 1.7167 |
| Return YTD (%) | 3.1063 |
| Return 1Y (%) | 3.3656 |
| Annualized volatility (%) | 18.2906 |
| Beta vs SPY | -0.1105 |
| Max drawdown (%) | -19.8462 |
| Sharpe (rf=0) | 0.2494 |
| Downside deviation (rf=0, %) | 12.9327 |
| Sortino (rf=0) | 0.3527 |
| Historical VaR 95% (1D, %) | 1.7635 |
| Historical ES 95% (1D, %) | 2.5078 |
| Correlation vs SPY | -0.0827 |
| Tracking error vs SPY (%) | 23.7368 |
| P/E (trailing) | 22.90 |
| P/B | 2.44 |
| EV/EBITDA | 13.07 |
| Revenue growth (%) | 44.00 |
| Forward P/E (estimate) | 21.14 |
| Gross margin (%) | 30.20 |
| Operating margin (%) | 10.50 |
| Return on equity (%) | 9.85 |
| Free cash flow yield (%) | N/A |
| MA50 | 48.0458 |
| Close vs MA50 (%) | -1.3441 |
| MA200 | 51.4399 |
| Close vs MA200 (%) | -7.8537 |
| RSI (14, Wilder) | 43.9904 |
| MACD (12,26) | 0.0485 |
| MACD signal (9) | 0.1371 |
| MACD histogram | -0.0886 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ENB': 278, 'SPY': 278}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 47.4000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.0877 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -3.6585 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 1.7167 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 3.1063 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 3.3656 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 18.2906 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 12.9327 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.3527 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.7635 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.5078 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.0827 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.7368 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1105 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -19.8462 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2494 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 21.1393 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 30.1950 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 10.5000 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.8490 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 22.8986 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 43.9904 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.0886 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -1.3441 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -7.8537 -> Clearly below the moving-average trend level.

## TAILWINDS

### Enbridge Reports Higher Earnings as Infrastructure Expansion Accelerates
- Summary: Enbridge Reports Higher Earnings as Infrastructure Expansion Accelerates
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxNVi1fTU5DanRvTTVlNVJzYjFqeW5oczNicXQ5V2p5ZzhRY2sxZ0t6RHdCRVFRaEQwUS1WUHMwMjhKNnJzN19hX2ZjZVI3alAteEk0aGJLTnVCbjdzemJwUWFvOV93Q3hSUUVXbUZEUndVblRkMm9NTGJJOWswTDl2S3htX1VPc01VTVRJNDc0QWVqZzN4TWIxbGdpWXRySmJNRWo1enhmbFlUREpaVkN2em91cTV3ZEpfaWU3cjA5M0lyQQ?oc=5>

### Enbridge Inc (ENB) Stock Forecasts
- Summary: Enbridge releases future earnings and revenue projections.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxQQTl6NlBsaFJtZ2wxSmRBOFpsVkFaanFnRllSXzE0d29jSkNSbkpKV1hTMTBDLVdHT3VhWWk5UGh5VDlpTEZJMHRrWVg1N1Q4ajY1NUJlWFJINzZyYTdXTFlLWUx6MGlzdHNlU05GcnFlV0lYUXQ4WlJFZU82cWZ3ZlJsVjRhSUpH?oc=5>

### Enbridge (TSX:ENB) Holds Its Dividend, Is The Stock Still Cheap?
- Summary: Enbridge maintains dividend payout, questioning valuation.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOVGdGWjJGSE1MNnpKY1ZEVjd0VnFNbFhHLXl4VXM5c1czNGtwLWlOZTRSWDFyekNWVzhzZVVpM2NYOWdRMDBHeHNGTFR2RGtPa1Q2aGZuLWFrV2h0RWk2Q0syamg3N2plWG5ObFJWbFU3cXBISG1DdlBvclVkTG9ISW9QRXhvaHlHZWh2dzAyOGhWeU44ZC1kdFRwdzI?oc=5>

### Enbridge Inc $ENB Stock: Kestra Advisory Services LLC Boosts Holdings
- Summary: Kestra increases Enbridge stake, signaling confidence.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxOTjhhM3Y5bWJBTGNuUG9NX1czNUozdGNKNG5ZZVJEeTBCcWpzaEdFdDJ6Rm8xaUNUZ3gyVEQyMmE4R1FBSUc5cmRnUTUzZWlWZUhRcEVyeHcycFlpRmlCNFJ6MUxpVjE1a0duRXFrT3JEMmdLU3pRVUkxY3lWeXdBSXgzSnhVVTJWYmViRUR4SmkzQzlJSzgtUDY4dkRKbzFORnJVR0p5TnFRWVZvdklnUzJVRnFiZDNjdFdsc1phVUY5MTNWZHlv?oc=5>

### Enbridge Inc $ENB Stock Position Cut by ProShare Advisors LLC
- Summary: ProShare reduces Enbridge holdings, indicating potential concerns.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxPZ09zNWFxNENLbmJGREs2WDhZbXBIRUYySVppTFZpWmtNMHhBdmFVbGpMUjNpNExmakNlbFFpLVpGbWVLVVk4bnJjbi1vYzlFQkYyWmlwVkVGdW9iNlJjTWVoUXhFOUg3Q1hkZE90T2tYbFp5SFRQYjRSaEZpeWszSGZ2SHRTQTdoMWZvR2hkMF9kek02dzFTeHFkYlo4NV9LbWJhWlgwQUZsUnVfdDJTWkZUZFBkVXY1YTlCa3dR?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Enbridge (TSX:ENB) Q3 Results Keep Debt And Dividend In Focus
- Summary: Enbridge (TSX:ENB) Q3 Results Keep Debt And Dividend In Focus
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPQjA5aGxHUWFGbXVVNHN1SmhZdmx2VkMtbGdBVUlKNXJJWTZ4TnZ4RmFoZEl1VTlVOG9Xd1RIZWhVSGw5Q3VSeklvaW4yWUJZckdzcVd4MHo2d0o0RHUzUDl3X0FMYXJjYXhWRHZ1QzdHSGpSVkhfektLZnI4R2VyRVBjbkpRZGJORWtRcGlyeFRJZVYzbzVj?oc=5>

### Enbridge Inc. Declares Quarterly Dividends
- Summary: Enbridge Inc. Declares Quarterly Dividends
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPZ2V5RGJpRmoxNTd2amQ5MlhlX0txaXI3OXcxQ0YtSlBuNVp3dC0xZ1hTdUd5Sk9nVDh2UzZRWUZQQ1JlT2hqY1RnZFZqOXprUlFlcVhSTDhlNGFHcFZaY3h1cE5SOXRuZG03bExsaVB6U0xTNDVoV2hjYnk2VzRaSzBsT1NWUUx5X1RITE1TNW4ydnlwSkRmQXlKcWNaRHpCcXFuRDY3WmNGUQ?oc=5>

### Enbridge Inc. 2026 Q3 - Results - Earnings Call Presentation (TSX:ENB:CA) 2026-11-06
- Summary: Enbridge Inc. 2026 Q3 - Results - Earnings Call Presentation (TSX:ENB:CA) 2026-11-06
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOMjBPV3BCaUlQaFNHZFI2ZkJkeDd4TGNERHl1anozMjV1NGRKMG11ektmQ0lSbHctN0pzMmxHcTh3LXN4V0RaQVZqYk9STTJyUjFfQmJOTnFpRTQ1MVpuUnFBTUotZy01NV9LelFpeVJBb1RDQWphTGtoeUhVenEyYmFxVGRYeV9LUG4yQVZwMGltRUF2blY0R2VnSXU?oc=5>

### Enbridge (NYSE:ENB) Issues Quarterly Earnings Results
- Summary: Enbridge (NYSE:ENB) Issues Quarterly Earnings Results
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxQdmc1ZG9FZTlaYkxTb2Mzajg1amczcFZLdHlYeXdvLVdFT2o1a0o1bDBvY0VUWmlBR2NsV1pROTJIQTcyOGRKRlBJQ2kwbThoWDBTT3RiVWNrbWVXVFdsU3d5NDFOZ1BKNTZ4bms3VXpVR1F2S1lDS2xtZUxQTU5UQTNEbFVXd05iOEVaWExKNjJ3ZnpGdmpqOFJYRkk2WU5PaVNfOWpINTMxU3RLNzFrQndCU0c?oc=5>

### Stocks in play: Enbridge Inc.
- Summary: Enbridge shares are currently active in the market, indicating investor interest.
- Date: 2026-11-04 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTFBXZ01jUDVRSnF5TnZPVjdnNHhNQU5TamZqUTB1TGVhcGpRVldkSFNuV2ZjUkFGM2RTUXZRNkV2cXk0TklMVDFWOEV2eDJISWx1QTBNSXJHXzR1dnEybEh2NWJ3eEwyOVBwczEyb29Fa21XM2twYkpyNkIzSG9RUQ?oc=5>

### Enbridge may be interested in building pipeline for Canada's Pathways carbon capture project
- Summary: Enbridge shows interest in constructing a pipeline for the Pathways carbon capture initiative, potentially expanding its infrastructure portfolio.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxORXdoUkVVN1kySXJvSm5EM0t1NmFlU2lUbkpULXZUNmNUd28tYWRkR04xYm5qWUJwd0pxcnJZWXl1ZjhXU3ZRdXc0czhYb3QyY3lVUHUxU3ZWT0JmWnFwNElkdTBSakZDLWctUkVCdUxxZUJfUHpNVzdNWHFTejFFcmtDaExleHlybVNqTTk1NWgwckxZOUNaOTVhS2h1QUNMcTJmNTh2WWdLZzdwOGhyVngtYVd4eHgySWhUOVREMkItUlE4Vi1Zaw?oc=5>

### Compass Financial Management LLC Buys 25,277 Shares of Enbridge Inc $ENB
- Summary: Compass Financial Management LLC purchased 25,277 shares of Enbridge Inc, indicating a short-term market activity.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxNY0J5ZDVQUGVtRTRyVU9VVjZkRmpLTGxjdlNEemFXU3BKbXBfLURxVlVBMlBvU0huOUtSSE9oYjRsakV2N0stWVMyZkFlQjFwT0p3Rmw5ZjlsWXItbjc1czJZN3NYek1aQjNsME5KWlVmUU9ZSHBRWFZNeEl3TGVLQnotbE04N1hIaEVoNzY0V0wxYjA3ZGdlQXJZY1hlN1FXSWloeHpiZ2ZaTW1xYnN5bzk3YlRiVWo0Zy00emNpUW9DUnA4WHRJRlh0NA?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ENB** | **22.90** | **2.44** | **13.07** | **44.00** | **105,649,299,456.00 USD** | **3.37** |
| TRP.TO | 24.24 | 3.61 | 16.39 | 8.80 | 92,435,980,288.00 CAD | 26.17 |
| KMI | 18.87 | 2.16 | 13.26 | 9.30 | 68,101,255,168.00 USD | 19.48 |
| EPD | 12.15 | 2.62 | 10.67 | 49.30 | 79,147,401,216.00 USD | 24.63 |

Peers fetched as_of: 2026-11-09; ENB reuses existing data (market data as_of: 2026-11-09); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-06
- Next expected earnings: 2027-02-12 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-09

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
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxQQTl6NlBsaFJtZ2wxSmRBOFpsVkFaanFnRllSXzE0d29jSkNSbkpKV1hTMTBDLVdHT3VhWWk5UGh5VDlpTEZJMHRrWVg1N1Q4ajY1NUJlWFJINzZyYTdXTFlLWUx6MGlzdHNlU05GcnFlV0lYUXQ4WlJFZU82cWZ3ZlJsVjRhSUpH?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOVGdGWjJGSE1MNnpKY1ZEVjd0VnFNbFhHLXl4VXM5c1czNGtwLWlOZTRSWDFyekNWVzhzZVVpM2NYOWdRMDBHeHNGTFR2RGtPa1Q2aGZuLWFrV2h0RWk2Q0syamg3N2plWG5ObFJWbFU3cXBISG1DdlBvclVkTG9ISW9QRXhvaHlHZWh2dzAyOGhWeU44ZC1kdFRwdzI?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxOTjhhM3Y5bWJBTGNuUG9NX1czNUozdGNKNG5ZZVJEeTBCcWpzaEdFdDJ6Rm8xaUNUZ3gyVEQyMmE4R1FBSUc5cmRnUTUzZWlWZUhRcEVyeHcycFlpRmlCNFJ6MUxpVjE1a0duRXFrT3JEMmdLU3pRVUkxY3lWeXdBSXgzSnhVVTJWYmViRUR4SmkzQzlJSzgtUDY4dkRKbzFORnJVR0p5TnFRWVZvdklnUzJVRnFiZDNjdFdsc1phVUY5MTNWZHlv?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxPZ09zNWFxNENLbmJGREs2WDhZbXBIRUYySVppTFZpWmtNMHhBdmFVbGpMUjNpNExmakNlbFFpLVpGbWVLVVk4bnJjbi1vYzlFQkYyWmlwVkVGdW9iNlJjTWVoUXhFOUg3Q1hkZE90T2tYbFp5SFRQYjRSaEZpeWszSGZ2SHRTQTdoMWZvR2hkMF9kek02dzFTeHFkYlo4NV9LbWJhWlgwQUZsUnVfdDJTWkZUZFBkVXY1YTlCa3dR?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPQjA5aGxHUWFGbXVVNHN1SmhZdmx2VkMtbGdBVUlKNXJJWTZ4TnZ4RmFoZEl1VTlVOG9Xd1RIZWhVSGw5Q3VSeklvaW4yWUJZckdzcVd4MHo2d0o0RHUzUDl3X0FMYXJjYXhWRHZ1QzdHSGpSVkhfektLZnI4R2VyRVBjbkpRZGJORWtRcGlyeFRJZVYzbzVj?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPZ2V5RGJpRmoxNTd2amQ5MlhlX0txaXI3OXcxQ0YtSlBuNVp3dC0xZ1hTdUd5Sk9nVDh2UzZRWUZQQ1JlT2hqY1RnZFZqOXprUlFlcVhSTDhlNGFHcFZaY3h1cE5SOXRuZG03bExsaVB6U0xTNDVoV2hjYnk2VzRaSzBsT1NWUUx5X1RITE1TNW4ydnlwSkRmQXlKcWNaRHpCcXFuRDY3WmNGUQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOMjBPV3BCaUlQaFNHZFI2ZkJkeDd4TGNERHl1anozMjV1NGRKMG11ektmQ0lSbHctN0pzMmxHcTh3LXN4V0RaQVZqYk9STTJyUjFfQmJOTnFpRTQ1MVpuUnFBTUotZy01NV9LelFpeVJBb1RDQWphTGtoeUhVenEyYmFxVGRYeV9LUG4yQVZwMGltRUF2blY0R2VnSXU?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxQdmc1ZG9FZTlaYkxTb2Mzajg1amczcFZLdHlYeXdvLVdFT2o1a0o1bDBvY0VUWmlBR2NsV1pROTJIQTcyOGRKRlBJQ2kwbThoWDBTT3RiVWNrbWVXVFdsU3d5NDFOZ1BKNTZ4bms3VXpVR1F2S1lDS2xtZUxQTU5UQTNEbFVXd05iOEVaWExKNjJ3ZnpGdmpqOFJYRkk2WU5PaVNfOWpINTMxU3RLNzFrQndCU0c?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTFBXZ01jUDVRSnF5TnZPVjdnNHhNQU5TamZqUTB1TGVhcGpRVldkSFNuV2ZjUkFGM2RTUXZRNkV2cXk0TklMVDFWOEV2eDJISWx1QTBNSXJHXzR1dnEybEh2NWJ3eEwyOVBwczEyb29Fa21XM2twYkpyNkIzSG9RUQ?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxORXdoUkVVN1kySXJvSm5EM0t1NmFlU2lUbkpULXZUNmNUd28tYWRkR04xYm5qWUJwd0pxcnJZWXl1ZjhXU3ZRdXc0czhYb3QyY3lVUHUxU3ZWT0JmWnFwNElkdTBSakZDLWctUkVCdUxxZUJfUHpNVzdNWHFTejFFcmtDaExleHlybVNqTTk1NWgwckxZOUNaOTVhS2h1QUNMcTJmNTh2WWdLZzdwOGhyVngtYVd4eHgySWhUOVREMkItUlE4Vi1Zaw?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxNY0J5ZDVQUGVtRTRyVU9VVjZkRmpLTGxjdlNEemFXU3BKbXBfLURxVlVBMlBvU0huOUtSSE9oYjRsakV2N0stWVMyZkFlQjFwT0p3Rmw5ZjlsWXItbjc1czJZN3NYek1aQjNsME5KWlVmUU9ZSHBRWFZNeEl3TGVLQnotbE04N1hIaEVoNzY0V0wxYjA3ZGdlQXJZY1hlN1FXSWloeHpiZ2ZaTW1xYnN5bzk3YlRiVWo0Zy00emNpUW9DUnA4WHRJRlh0NA?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
