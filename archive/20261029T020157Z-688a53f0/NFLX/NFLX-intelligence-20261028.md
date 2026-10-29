# NFLX Intelligence Report

- ticker: **NFLX**
- Report as_of: **2026-10-28**
- Market data as_of: **2026-10-28**
- Quant sources: https://finance.yahoo.com/quote/NFLX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NFLX/key-statistics/
- AI analysis snapshot as_of: **2026-10-28**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-29T02:23:23.108209+00:00**
- AI status: **Partial: 4 headlines remain unclassified and excluded from research conclusions**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 5, 'ai': 9, 'unknown': 4, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261028T015717Z-533e470c/NFLX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 9 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 29.17%; oldest publication 2026-10-21

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 61.9900 |
| Return 1D (%) | -0.8477 |
| Return 1W (%) | -4.6894 |
| Return 1M (%) | -10.4579 |
| Return YTD (%) | -33.8844 |
| Return 1Y (%) | -43.7732 |
| Annualized volatility (%) | 35.9160 |
| Beta vs SPY | 0.2078 |
| Max drawdown (%) | -46.4449 |
| Sharpe (rf=0) | -1.4295 |
| Downside deviation (rf=0, %) | 26.4628 |
| Sortino (rf=0) | -1.9401 |
| Historical VaR 95% (1D, %) | 3.5133 |
| Historical ES 95% (1D, %) | 5.1308 |
| Correlation vs SPY | 0.0735 |
| Tracking error vs SPY (%) | 37.2057 |
| P/E (trailing) | 18.07 |
| P/B | 8.69 |
| EV/EBITDA | 16.54 |
| Revenue growth (%) | 11.80 |
| Forward P/E (estimate) | 16.44 |
| Gross margin (%) | 50.69 |
| Operating margin (%) | 34.63 |
| Return on equity (%) | 53.46 |
| Free cash flow yield (%) | 9.87 |
| MA50 | 73.3972 |
| Close vs MA50 (%) | -15.5417 |
| MA200 | 81.8700 |
| Close vs MA200 (%) | -24.2824 |
| RSI (14, Wilder) | 30.2526 |
| MACD (12,26) | -2.5000 |
| MACD signal (9) | -1.9010 |
| MACD histogram | -0.5991 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NFLX': 270, 'SPY': 270}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 61.9900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.8477 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -4.6894 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -10.4579 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -33.8844 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -43.7732 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 35.9160 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.4628 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -1.9401 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.5133 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1308 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0735 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.2057 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.2078 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -46.4449 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -1.4295 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.4371 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 50.6850 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 34.6320 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 53.4630 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 9.8697 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 18.0729 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 30.2526 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.5991 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -15.5417 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -24.2824 -> Clearly below the moving-average trend level.

## TAILWINDS

### Netflix (NFLX) Stock Stays Cheap After Its 58% Three Year Gain
- Summary: Netflix (NFLX) Stock Stays Cheap After Its 58% Three Year Gain
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOVmpXNWh4OWZNOUI5d0lnd1NGYzBBU2tLSFhPeDY3UFpFM1ZXODVVdzNuMy1CM1pMelUxdFZEQ25XVW5NMHlPYnZ1WFZ3RXZXbXB6aDg2eFpWNUF5RC1KWUFJc2dmMHlkbkJQY1k2Z2JLb25RY0J6cURXR2hxV1AzZDZMM0dvWW84WHFIalR2Q05pbDZzMlBpekhKdw?oc=5>

### Netflix Q3: An Opportunity Hiding In Plain Sight (NASDAQ:NFLX)
- Summary: Positive Q3 earnings signal potential upside.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxQUTBjcy1lMWVqMHEwVzJ6dmNJYmJuM011ZG5pUXFlQTRWbGs3MkpEYlhzSmp5ajJhcWUzYnQyQkQwV2ZuZllmOFZlYm5lYWRITHZHcS1rS201OWg4ZElvSU1jVFdMeHhsck9qZkZtN0IyWWFkZndsSHVoUDRYclczaVNCTWVsanVLTUUxS285U3NQdw?oc=5>

## HEADWINDS

### Netflix Shares Are Down 9% Since Earnings. Is the Stock a Buy?
- Summary: Netflix Shares Are Down 9% Since Earnings. Is the Stock a Buy?
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxPZ1pZb216M0NKaGhqWmdoXzkwOC1TQjFzRExLVEpXYVpSU19HTWN5QUVKbTg3cGNYem9nQmw5Mmsxd0V1M2IyMmJQWDJrdUszTllwRmFsRG5UNTZpTjRrVWRCYzBsdGlGazhkeGFwNW5ENUhXRzFEOUJ1U0J4aHJtaDhYdW5hNWdPM1FCajlZZk1pUQ?oc=5>

### Netflix (NFLX) Stock Price Falls As Q3 Earnings Stir Valuation Doubts
- Summary: Netflix (NFLX) Stock Price Falls As Q3 Earnings Stir Valuation Doubts
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOVmRBaFZXZGZad2d5SGVQS2J4c2xPOTdpNjNqRmlQWXliMWpIVFdpV2RsSlZ1NHRiUFBtZ0hQbGxDS2U3bjBSNE5pR2hlUFNPY3Y4YVp2LUhsRHlvZ1dhemdCc2twWXJYX2JBZm1ELU5fRGJVWnpFOTlQcU5sOGlGZl9qazJhajZTaFRqWnQ4X3kxVTBqWXFyMDdKRQ?oc=5>

### Netflix Is Now Down 29% This Year: Is NFLX Stock Hopeless or Ready for a Rebound?
- Summary: Netflix shares fell 29% YTD, raising concerns about future growth and valuation.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxQLUd5d2xvbWNXbkpvYmY3VmhEYUtsbU83V2VIMnptYW5WbUNMZ1dibkJmZEwxYUg0RXhmOWRQZ0t6aW5RaTNoUkQ4Y3ZEZ3FaU2FGSjl2VC1uQlE3bkNnVUtaNi1DY1RzS05zeE55ZGNuS2UtYmlSbTR2ZDlqRXNvaTF1V3QyalNmNkdYN3JsTU50bDZwNXFvR0FVajlpODFvWlZrSGlpYmhDRTg0a0RkWTRLWXFFdzg1YmxZc3RFSQ?oc=5>

### Netflix Is Down 51% From Its High. History Suggests This Is What Happens Next.
- Summary: Shares dropped 51% from peak, hinting at potential further decline.
- Date: 2026-10-25 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxPZTg4c2VtT2d1SV9meTFhZFpzN2ItRk85YXlQWnAwQUxDRm5VMmhBU0RrVXAyRWROcWk4RUpFdk4yWlhkc3dlUjFyU3hkVDVkaklFNC0zTmRPRmJZNHQxN2xvYmQtMVlDVm9Bd2VJdkZIOEI1Mnh0blZMNEJ4d0FGOXBvY25ic1UwV2NYa2ZPcw?oc=5>

### Down Roughly 50% From Its Highs, Is Netflix Stock Finally a Buy?
- Summary: Stock price has dropped 50%, questioning buy potential.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPaUxsUFM0YmRJeEtMU3VUTG1kT0FEMVpHckhVenVyMXZ5Y25YZFlhWGc5SklnZWJJNHljMzA0NmlGTGdTU3VYTUtlenBKcFhLcXhYN0MxdGVyQkk4eDZfQU9WZ3hOelJoU01ocnQ3UEQ0R0ZNWWRiSEZIOERkaTBoMnMtY3Jnam9CaTlKMk41OGpPMVdl?oc=5>

### Should You Buy Netflix Stock After Its 51% Plunge?
- Summary: Stock plunged 51%, raising concerns.
- Date: 2026-10-24 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOS0JnUml0VTFqcjdudFhjaW55d3M3cnpzMjFDby1iODYyUFJiZzN5TkExMFhHVEFjb0JjRDFuSVJEaE03MWUtdkJrcXN6LWRtS01WYmtFWHI5U0Y5dFhqbUdXYS1KVkJhdE5CY2tQN0thdC01UVRUeWJLVlNUY2VKa0NMSXlka0p5MFBzZ1lxa3hydU5tVVdF?oc=5>

### Netflix Stock Has Always Overcome the Odds. Has It Finally Hit a Wall?
- Summary: Stock may have reached a resistance level.
- Date: 2026-10-24 | Impact: high | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPMlEtcTktT2NrV1BGT2V2UVhMVFE5OE9sQVFPMmhfdUh5dlF3SzI5QXdmTF9JODNXZFFIY2IyQy1uemZYZ2NIdENSOWktblBtY3RvMHlRaFR5aDRsQzl3b0JFM1ByRHpDOGhxODBwc3E5ekVpamtvTTlNVVhfNnVyOEVROGpGcno2NjZINmVwLWU3SENkN2hR?oc=5>

### SA Asks: Netflix hit a 52-week low this week. Is now the time to buy?
- Summary: 52‑week low triggers market‑move concerns.
- Date: 2026-10-23 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxNTDNhdnR1QmZqalRiR3dRQ1hoM3hGZXZSMjVWcnpUS0FTZDFKWERXcWd3dlhOcG9jdV9mT0tnUWhNWFg2WWlWRW9pZV81UU5yb0RNTE1oWnBwSV92cnpveDhNdkJuNkdKOVJjbWk1R3Z4NllSbXhFRzN3VThVVUZtUkZJZll4eTJncWhnT2hWa00tNF9oc2xvWHprRUJLcFBWdG5ieEI0QmQtaEVYY0FnaDVGU3ZBcUZ6dlQ3NzhZMlMzeXlnUmRv?oc=5>

## CATALYSTS

### Netflix (NFLX) Stock Fair Value Falls After Cautious Q3 Analyst Revisions
- Summary: Netflix (NFLX) Stock Fair Value Falls After Cautious Q3 Analyst Revisions
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQSE1oLXBDN2dSRUZabVZhbzJvTDZpSVV3NmNVQ2VlYjJJQVVRSTBfQmJHT2FhWGt6LUl4NjFBMElxaVFGajh2eWlIRm1abUp2cFVoekg1VGdZN0pmbGV2ckZjWXB2ZzcwRWV2RkZ6S1pqVTBFNjRuamREVk5RMkoxZUw5ZjZyQXg1SDNHdzRIWDhweXJYTGpacC1R?oc=5>

### Netflix Stock Tanks 5% as Revenue Growth Slows in Q3. How to Play NFLX Here.
- Summary: Netflix Stock Tanks 5% as Revenue Growth Slows in Q3. How to Play NFLX Here.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxPUU4zX0ktN0t1V3gyYkZ1NEY0SmkzdUozTl90UTRxU0ZBZmZDUDhzWEZJbjViZmxGMnpJbTdOWlpTam4zczktWnlJaW5lSFllOTRYS05iVFkwMUNfNmNWOHE5LUVHbVM5SUNhSzFpdkJaYmpsY2NwZlhCSTNIMFBHNnFwRXo4WERtbjRGaXRSOFYwdHNjVmVLSWRIcG9zU25GdG1RQ2t5WUhjc1Q0X29QdEpJQWxaVC1o?oc=5>

### Why Netflix (NFLX) shares are falling today
- Summary: Explains factors behind today's decline in Netflix stock price.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQMi1rUzE5c3J6OEZESUJ3RmhEZkNsYldiRXMxRDRBX1g1eFRLd2pZQ3dHUl9ZZDFlVF9KYlk0OThYS3Q2bG9mVGtYWUIxTUhYdFNRVF83bUtFemNmQ29xSk1vd1ZQUURvbWJVMjEtdnEzUWl1cW0yRmE1LVNWYUZzamNCbEVDamFZeFczblY0ZHdzU0JZLXRBNEM0RjQ?oc=5>

### Netflix Just Posted a Record Margin. So Why Is Wall Street Panicking?
- Summary: Record margin reported, yet market reacts negatively.
- Date: 2026-10-26 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQVnpmQm5iU3RTNWg3S19pMUNyeXIxdnFXMXItXzJRNUxnQmpfUDlCZTlJc0dGN3hBRXNVYmpTaG8wVlluQmZwOWVBQ0NEdWc5dG1ZUkhka0gya0hQem5rMUI3NlZMS3V3bVZMdVFCSGRycFRfWmJxMU9ja0JtNHlEb3dNRUJ0cDF5NDVXQWN3S3FmRC1GanRVM2toSnY2YXc?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NFLX** | **18.07** | **8.69** | **16.54** | **11.80** | **258,122,629,120.00 USD** | **-43.77** |
| DIS | 22.72 | 1.71 | 11.26 | 6.80 | 188,277,932,032.00 USD | -0.92 |
| WBD | N/A | 2.36 | 13.79 | -11.20 | 77,595,885,568.00 USD | N/A |
| CMCSA | 6.91 | 0.83 | 4.67 | -6.10 | 76,595,200,000.00 USD | -17.19 |

Peers fetched as_of: 2026-10-28; NFLX reuses existing data (market data as_of: 2026-10-28); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-20
- Next expected earnings: 2027-01-19 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-28

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 12,874,176,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 3,663,927,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimwFBVV95cUxOVmpXNWh4OWZNOUI5d0lnd1NGYzBBU2tLSFhPeDY3UFpFM1ZXODVVdzNuMy1CM1pMelUxdFZEQ25XVW5NMHlPYnZ1WFZ3RXZXbXB6aDg2eFpWNUF5RC1KWUFJc2dmMHlkbkJQY1k2Z2JLb25RY0J6cURXR2hxV1AzZDZMM0dvWW84WHFIalR2Q05pbDZzMlBpekhKdw?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxQUTBjcy1lMWVqMHEwVzJ6dmNJYmJuM011ZG5pUXFlQTRWbGs3MkpEYlhzSmp5ajJhcWUzYnQyQkQwV2ZuZllmOFZlYm5lYWRITHZHcS1rS201OWg4ZElvSU1jVFdMeHhsck9qZkZtN0IyWWFkZndsSHVoUDRYclczaVNCTWVsanVLTUUxS285U3NQdw?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxPZ1pZb216M0NKaGhqWmdoXzkwOC1TQjFzRExLVEpXYVpSU19HTWN5QUVKbTg3cGNYem9nQmw5Mmsxd0V1M2IyMmJQWDJrdUszTllwRmFsRG5UNTZpTjRrVWRCYzBsdGlGazhkeGFwNW5ENUhXRzFEOUJ1U0J4aHJtaDhYdW5hNWdPM1FCajlZZk1pUQ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOVmRBaFZXZGZad2d5SGVQS2J4c2xPOTdpNjNqRmlQWXliMWpIVFdpV2RsSlZ1NHRiUFBtZ0hQbGxDS2U3bjBSNE5pR2hlUFNPY3Y4YVp2LUhsRHlvZ1dhemdCc2twWXJYX2JBZm1ELU5fRGJVWnpFOTlQcU5sOGlGZl9qazJhajZTaFRqWnQ4X3kxVTBqWXFyMDdKRQ?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxQLUd5d2xvbWNXbkpvYmY3VmhEYUtsbU83V2VIMnptYW5WbUNMZ1dibkJmZEwxYUg0RXhmOWRQZ0t6aW5RaTNoUkQ4Y3ZEZ3FaU2FGSjl2VC1uQlE3bkNnVUtaNi1DY1RzS05zeE55ZGNuS2UtYmlSbTR2ZDlqRXNvaTF1V3QyalNmNkdYN3JsTU50bDZwNXFvR0FVajlpODFvWlZrSGlpYmhDRTg0a0RkWTRLWXFFdzg1YmxZc3RFSQ?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxPZTg4c2VtT2d1SV9meTFhZFpzN2ItRk85YXlQWnAwQUxDRm5VMmhBU0RrVXAyRWROcWk4RUpFdk4yWlhkc3dlUjFyU3hkVDVkaklFNC0zTmRPRmJZNHQxN2xvYmQtMVlDVm9Bd2VJdkZIOEI1Mnh0blZMNEJ4d0FGOXBvY25ic1UwV2NYa2ZPcw?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPaUxsUFM0YmRJeEtMU3VUTG1kT0FEMVpHckhVenVyMXZ5Y25YZFlhWGc5SklnZWJJNHljMzA0NmlGTGdTU3VYTUtlenBKcFhLcXhYN0MxdGVyQkk4eDZfQU9WZ3hOelJoU01ocnQ3UEQ0R0ZNWWRiSEZIOERkaTBoMnMtY3Jnam9CaTlKMk41OGpPMVdl?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOS0JnUml0VTFqcjdudFhjaW55d3M3cnpzMjFDby1iODYyUFJiZzN5TkExMFhHVEFjb0JjRDFuSVJEaE03MWUtdkJrcXN6LWRtS01WYmtFWHI5U0Y5dFhqbUdXYS1KVkJhdE5CY2tQN0thdC01UVRUeWJLVlNUY2VKa0NMSXlka0p5MFBzZ1lxa3hydU5tVVdF?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPMlEtcTktT2NrV1BGT2V2UVhMVFE5OE9sQVFPMmhfdUh5dlF3SzI5QXdmTF9JODNXZFFIY2IyQy1uemZYZ2NIdENSOWktblBtY3RvMHlRaFR5aDRsQzl3b0JFM1ByRHpDOGhxODBwc3E5ekVpamtvTTlNVVhfNnVyOEVROGpGcno2NjZINmVwLWU3SENkN2hR?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxNTDNhdnR1QmZqalRiR3dRQ1hoM3hGZXZSMjVWcnpUS0FTZDFKWERXcWd3dlhOcG9jdV9mT0tnUWhNWFg2WWlWRW9pZV81UU5yb0RNTE1oWnBwSV92cnpveDhNdkJuNkdKOVJjbWk1R3Z4NllSbXhFRzN3VThVVUZtUkZJZll4eTJncWhnT2hWa00tNF9oc2xvWHprRUJLcFBWdG5ieEI0QmQtaEVYY0FnaDVGU3ZBcUZ6dlQ3NzhZMlMzeXlnUmRv?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQSE1oLXBDN2dSRUZabVZhbzJvTDZpSVV3NmNVQ2VlYjJJQVVRSTBfQmJHT2FhWGt6LUl4NjFBMElxaVFGajh2eWlIRm1abUp2cFVoekg1VGdZN0pmbGV2ckZjWXB2ZzcwRWV2RkZ6S1pqVTBFNjRuamREVk5RMkoxZUw5ZjZyQXg1SDNHdzRIWDhweXJYTGpacC1R?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxPUU4zX0ktN0t1V3gyYkZ1NEY0SmkzdUozTl90UTRxU0ZBZmZDUDhzWEZJbjViZmxGMnpJbTdOWlpTam4zczktWnlJaW5lSFllOTRYS05iVFkwMUNfNmNWOHE5LUVHbVM5SUNhSzFpdkJaYmpsY2NwZlhCSTNIMFBHNnFwRXo4WERtbjRGaXRSOFYwdHNjVmVLSWRIcG9zU25GdG1RQ2t5WUhjc1Q0X29QdEpJQWxaVC1o?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQMi1rUzE5c3J6OEZESUJ3RmhEZkNsYldiRXMxRDRBX1g1eFRLd2pZQ3dHUl9ZZDFlVF9KYlk0OThYS3Q2bG9mVGtYWUIxTUhYdFNRVF83bUtFemNmQ29xSk1vd1ZQUURvbWJVMjEtdnEzUWl1cW0yRmE1LVNWYUZzamNCbEVDamFZeFczblY0ZHdzU0JZLXRBNEM0RjQ?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQVnpmQm5iU3RTNWg3S19pMUNyeXIxdnFXMXItXzJRNUxnQmpfUDlCZTlJc0dGN3hBRXNVYmpTaG8wVlluQmZwOWVBQ0NEdWc5dG1ZUkhka0gya0hQem5rMUI3NlZMS3V3bVZMdVFCSGRycFRfWmJxMU9ja0JtNHlEb3dNRUJ0cDF5NDVXQWN3S3FmRC1GanRVM2toSnY2YXc?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
