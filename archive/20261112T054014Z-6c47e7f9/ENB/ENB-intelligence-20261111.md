# ENB Intelligence Report

- ticker: **ENB**
- Report as_of: **2026-11-11**
- Market data as_of: **2026-11-11**
- Quant sources: https://finance.yahoo.com/quote/ENB/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ENB/key-statistics/
- AI analysis snapshot as_of: **2026-11-11**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-12T05:59:48.013015+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 14, 'rule': 2, 'ai': 9, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261111T043601Z-d14951e6/ENB** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 14 unique headlines; 9 named publishers; 0 exact duplicates; 14 HTTPS source links; largest publisher share 28.57%; oldest publication 2026-11-06

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 47.9100 |
| Return 1D (%) | 0.3141 |
| Return 1W (%) | -1.7835 |
| Return 1M (%) | 2.8112 |
| Return YTD (%) | 4.2156 |
| Return 1Y (%) | 3.2229 |
| Annualized volatility (%) | 18.2559 |
| Beta vs SPY | -0.1098 |
| Max drawdown (%) | -19.8462 |
| Sharpe (rf=0) | 0.2654 |
| Downside deviation (rf=0, %) | 12.9069 |
| Sortino (rf=0) | 0.3754 |
| Historical VaR 95% (1D, %) | 1.7623 |
| Historical ES 95% (1D, %) | 2.5078 |
| Correlation vs SPY | -0.0826 |
| Tracking error vs SPY (%) | 23.7310 |
| P/E (trailing) | 23.14 |
| P/B | 2.47 |
| EV/EBITDA | 13.14 |
| Revenue growth (%) | 44.00 |
| Forward P/E (estimate) | 21.53 |
| Gross margin (%) | 30.20 |
| Operating margin (%) | 12.82 |
| Return on equity (%) | 9.85 |
| Free cash flow yield (%) | N/A |
| MA50 | 47.9334 |
| Close vs MA50 (%) | -0.0488 |
| MA200 | 51.4574 |
| Close vs MA200 (%) | -6.8938 |
| RSI (14, Wilder) | 48.7486 |
| MACD (12,26) | 0.0030 |
| MACD signal (9) | 0.0910 |
| MACD histogram | -0.0879 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ENB': 280, 'SPY': 280}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 47.9100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.3141 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.7835 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 2.8112 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 4.2156 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 3.2229 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 18.2559 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 12.9069 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.3754 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.7623 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.5078 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.0826 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.7310 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1098 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -19.8462 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2654 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 21.5262 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 30.1950 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 12.8210 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.8490 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 23.1449 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 48.7486 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.0879 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -0.0488 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -6.8938 -> Clearly below the moving-average trend level.

## TAILWINDS

### Energy Transfer’s EPS Missed by 20%. Enbridge’s Profit Nearly Doubled. Here’s Why I’m Not Worried About Either Dividend Even Though Both Still Fell Short.
- Summary: Enbridge’s profit nearly doubled, offsetting Energy Transfer’s EPS miss, indicating strong earnings performance.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingJBVV95cUxNRGQ5Q2RoVzN2emVUZTNsN2tEX1RQc2VLcUR0TmtENFR0ZFFGMVB1bzQxNVdzSUxPeUR2eXhSNWpCZHpTTVlRMjVpV0pjVHBERmNaTlFpeU8wUHVuYWszdTlsaXVaVm1DOWJoTTVhbVFzU0tub2xscEZTSVZMMlVaS1NvR1dFdXd3d1RNSEF5ZFZXUDJWcHloWnVZTTk0NjZHS2J6dFFSTW12YkVSam15a002bjRTM2lJeUduNEpuSmw2MmtmSW16UHIzZFRnRmsyc1A1dmJ6SUhVZWVielF0aERycDd4VFFiWFlYbHd5cEZLNWdtZWJFbVU1dVR0ZTJyQWRjd3dST2xsMFRkSFpGTjF0NWVWeWl1bG1Cd0Rn?oc=5>

### Enbridge Inc (ENB) Stock Forecasts
- Summary: Enbridge releases future earnings and revenue projections.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxQQTl6NlBsaFJtZ2wxSmRBOFpsVkFaanFnRllSXzE0d29jSkNSbkpKV1hTMTBDLVdHT3VhWWk5UGh5VDlpTEZJMHRrWVg1N1Q4ajY1NUJlWFJINzZyYTdXTFlLWUx6MGlzdHNlU05GcnFlV0lYUXQ4WlJFZU82cWZ3ZlJsVjRhSUpH?oc=5>

### Enbridge Inc $ENB Stock: Kestra Advisory Services LLC Boosts Holdings
- Summary: Kestra increases Enbridge stake, signaling confidence.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxOTjhhM3Y5bWJBTGNuUG9NX1czNUozdGNKNG5ZZVJEeTBCcWpzaEdFdDJ6Rm8xaUNUZ3gyVEQyMmE4R1FBSUc5cmRnUTUzZWlWZUhRcEVyeHcycFlpRmlCNFJ6MUxpVjE1a0duRXFrT3JEMmdLU3pRVUkxY3lWeXdBSXgzSnhVVTJWYmViRUR4SmkzQzlJSzgtUDY4dkRKbzFORnJVR0p5TnFRWVZvdklnUzJVRnFiZDNjdFdsc1phVUY5MTNWZHlv?oc=5>

### Enbridge stock: stronger Q3, steady 2026 outlook
- Summary: Enbridge reported stronger Q3 results and maintains a steady outlook for 2026, signaling robust earnings and guidance.
- Date: 2026-11-10 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxQUlk0bVFFZ3liZy1JbzlKdlEyTjhmOHpsdDNvLUktZVRRQU1FZVI4LVJxMllnZUxQLTVvS1ExbndMN0dkWi1wZUI3dkNJN29jMXFJbng5eTNma3dGY215UDMwVkt5SUUwTUk5WjdIMGtaeFk5eVJBb0c2LTIzNzFBT3o0TXJhbWV5V0VjSzVjeWNpWWdrTDgwVnRYbWNHaVRxMGlvWDhMcWtrZDFRNEE?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Enbridge Inc. 2026 Q3 - Results - Earnings Call Presentation (TSX:ENB:CA) 2026-11-06
- Summary: Enbridge Inc. 2026 Q3 - Results - Earnings Call Presentation (TSX:ENB:CA) 2026-11-06
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOMjBPV3BCaUlQaFNHZFI2ZkJkeDd4TGNERHl1anozMjV1NGRKMG11ektmQ0lSbHctN0pzMmxHcTh3LXN4V0RaQVZqYk9STTJyUjFfQmJOTnFpRTQ1MVpuUnFBTUotZy01NV9LelFpeVJBb1RDQWphTGtoeUhVenEyYmFxVGRYeV9LUG4yQVZwMGltRUF2blY0R2VnSXU?oc=5>

### Enbridge (NYSE:ENB) Issues Quarterly Earnings Results
- Summary: Enbridge (NYSE:ENB) Issues Quarterly Earnings Results
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxQdmc1ZG9FZTlaYkxTb2Mzajg1amczcFZLdHlYeXdvLVdFT2o1a0o1bDBvY0VUWmlBR2NsV1pROTJIQTcyOGRKRlBJQ2kwbThoWDBTT3RiVWNrbWVXVFdsU3d5NDFOZ1BKNTZ4bms3VXpVR1F2S1lDS2xtZUxQTU5UQTNEbFVXd05iOEVaWExKNjJ3ZnpGdmpqOFJYRkk2WU5PaVNfOWpINTMxU3RLNzFrQndCU0c?oc=5>

### Enbridge may be interested in building pipeline for Canada's Pathways carbon capture project
- Summary: Enbridge shows interest in constructing a pipeline for the Pathways carbon capture initiative, potentially expanding its infrastructure portfolio.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxORXdoUkVVN1kySXJvSm5EM0t1NmFlU2lUbkpULXZUNmNUd28tYWRkR04xYm5qWUJwd0pxcnJZWXl1ZjhXU3ZRdXc0czhYb3QyY3lVUHUxU3ZWT0JmWnFwNElkdTBSakZDLWctUkVCdUxxZUJfUHpNVzdNWHFTejFFcmtDaExleHlybVNqTTk1NWgwckxZOUNaOTVhS2h1QUNMcTJmNTh2WWdLZzdwOGhyVngtYVd4eHgySWhUOVREMkItUlE4Vi1Zaw?oc=5>

### Strong Q3 earnings coincide with Enbridge stock buyer support
- Summary: Enbridge reports strong Q3 earnings, boosting investor confidence.
- Date: 2026-11-11 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQTjROQjJhVUJaVUVzdkZlS1ZiVERQUHZzVU5ZT01IWmd0dnJPUkdjVFdkaTdSc3ZQYmRZOXNIdFNRbkVVZDktZmlHWGZBbHFxTlEyekVWUktYOFp2ejhOOHZ1UGlRUkhQRjkybGx3ZzEwMUFtb1A4Y1MyZGxfc1NjeDhWeEE0ZHBIYUJxaEdYY3VNbGI2?oc=5>

### Enbridge vs. ExxonMobil: Which Energy Stock Is a Better Buy for 2027?
- Summary: Analyst compares Enbridge to ExxonMobil for 2027 investment.
- Date: 2026-11-10 | Impact: medium | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxPTGhhd1hWcjNNU0FXYUtVeWFoMHA2a1g2bXF2NzdWR0Z1TEpNaGNPMXpucmZtcjVyU29EemlvXy1UcldzV2ptVFBVV1I1QUN1SlI2SU9kR3RROGRqQTBKaFNXQ1NrQVpndU5MM29TZFZrUjI0dE9xTzFMU1E0RHB2dWR4RzhYSDk2LXVBWVhzOUlVeThDcElXOXZVODdoOXpsLTUxMFZvT3YweG1OSllpeEJSYUhUamQyNzVz?oc=5>

### Commonwealth Equity Services LLC Sells 29,234 Shares of Enbridge Inc $ENB
- Summary: Institutional seller offloads Enbridge shares.
- Date: 2026-11-09 | Impact: low | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxOZDdueVVpYndEZ240US1ZeURHeW1nX25Nb1VCdDJoUHpYd2I5WXZiLWdTUHpDVnI3RHhTamhqLUc3NXZiX0FsUTRDN1owd1pCU19Rem9JMThxa0tHMlZycEtBamV4TVdtVVpadDZPU3NKcFJ5MVF1LVdfdEY0RkJuVXozREhuSUNDNGR2aDdmcHluSWZBRG9MbFk1ZjhhUmFDSHlrMWhNY2VGMGxscDZHdGFINzYxYjFicHBORjNvU3FYTHFnNUFGeUNXejE?oc=5>

### Enbridge (NYSE:ENB) Shares Cross Below Fifty Day Moving Average - What's Next?
- Summary: Enbridge shares dip below 50‑day MA, signaling potential trend shift.
- Date: 2026-11-07 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxQcmE0d3pyc1dqb1c3ZzU5RnhDSy15aHVVcVFDU1NUMUN4X085ZmtjVnJhbEgxejltZEs1MWREN1ZrZlMyTkZJSEV6ZmFTb0tzai1UclEyZzdtMnhUTzMyc08yb2ZDQ3Ric1VhUFpVUmVPN3c0bU1DSEpVSVJkU2IzM3pPcnlFRzNjYkJZbUppZ0pWbzJia2dfajRheVpnbzAtVmFQeUtDeHAxR1ZRY3plSzNyM09uNUtiREFIZkZISlNQUnFsSnpsS3ZNbFU?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ENB** | **23.14** | **2.47** | **13.14** | **44.00** | **106,786,029,568.00 USD** | **3.22** |
| TRP.TO | 25.09 | 3.73 | 16.68 | 8.80 | 95,405,015,040.00 CAD | 27.25 |
| KMI | 19.50 | 2.23 | 13.55 | 9.30 | 70,373,523,456.00 USD | 21.68 |
| EPD | 12.30 | 2.65 | 10.77 | 49.30 | 80,139,436,032.00 USD | 25.39 |

Peers fetched as_of: 2026-11-11; ENB reuses existing data (market data as_of: 2026-11-11); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-06
- Next expected earnings: 2027-02-12 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-11

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

- https://news.google.com/rss/articles/CBMingJBVV95cUxNRGQ5Q2RoVzN2emVUZTNsN2tEX1RQc2VLcUR0TmtENFR0ZFFGMVB1bzQxNVdzSUxPeUR2eXhSNWpCZHpTTVlRMjVpV0pjVHBERmNaTlFpeU8wUHVuYWszdTlsaXVaVm1DOWJoTTVhbVFzU0tub2xscEZTSVZMMlVaS1NvR1dFdXd3d1RNSEF5ZFZXUDJWcHloWnVZTTk0NjZHS2J6dFFSTW12YkVSam15a002bjRTM2lJeUduNEpuSmw2MmtmSW16UHIzZFRnRmsyc1A1dmJ6SUhVZWVielF0aERycDd4VFFiWFlYbHd5cEZLNWdtZWJFbVU1dVR0ZTJyQWRjd3dST2xsMFRkSFpGTjF0NWVWeWl1bG1Cd0Rn?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxQQTl6NlBsaFJtZ2wxSmRBOFpsVkFaanFnRllSXzE0d29jSkNSbkpKV1hTMTBDLVdHT3VhWWk5UGh5VDlpTEZJMHRrWVg1N1Q4ajY1NUJlWFJINzZyYTdXTFlLWUx6MGlzdHNlU05GcnFlV0lYUXQ4WlJFZU82cWZ3ZlJsVjRhSUpH?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxOTjhhM3Y5bWJBTGNuUG9NX1czNUozdGNKNG5ZZVJEeTBCcWpzaEdFdDJ6Rm8xaUNUZ3gyVEQyMmE4R1FBSUc5cmRnUTUzZWlWZUhRcEVyeHcycFlpRmlCNFJ6MUxpVjE1a0duRXFrT3JEMmdLU3pRVUkxY3lWeXdBSXgzSnhVVTJWYmViRUR4SmkzQzlJSzgtUDY4dkRKbzFORnJVR0p5TnFRWVZvdklnUzJVRnFiZDNjdFdsc1phVUY5MTNWZHlv?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxQUlk0bVFFZ3liZy1JbzlKdlEyTjhmOHpsdDNvLUktZVRRQU1FZVI4LVJxMllnZUxQLTVvS1ExbndMN0dkWi1wZUI3dkNJN29jMXFJbng5eTNma3dGY215UDMwVkt5SUUwTUk5WjdIMGtaeFk5eVJBb0c2LTIzNzFBT3o0TXJhbWV5V0VjSzVjeWNpWWdrTDgwVnRYbWNHaVRxMGlvWDhMcWtrZDFRNEE?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOMjBPV3BCaUlQaFNHZFI2ZkJkeDd4TGNERHl1anozMjV1NGRKMG11ektmQ0lSbHctN0pzMmxHcTh3LXN4V0RaQVZqYk9STTJyUjFfQmJOTnFpRTQ1MVpuUnFBTUotZy01NV9LelFpeVJBb1RDQWphTGtoeUhVenEyYmFxVGRYeV9LUG4yQVZwMGltRUF2blY0R2VnSXU?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxQdmc1ZG9FZTlaYkxTb2Mzajg1amczcFZLdHlYeXdvLVdFT2o1a0o1bDBvY0VUWmlBR2NsV1pROTJIQTcyOGRKRlBJQ2kwbThoWDBTT3RiVWNrbWVXVFdsU3d5NDFOZ1BKNTZ4bms3VXpVR1F2S1lDS2xtZUxQTU5UQTNEbFVXd05iOEVaWExKNjJ3ZnpGdmpqOFJYRkk2WU5PaVNfOWpINTMxU3RLNzFrQndCU0c?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxORXdoUkVVN1kySXJvSm5EM0t1NmFlU2lUbkpULXZUNmNUd28tYWRkR04xYm5qWUJwd0pxcnJZWXl1ZjhXU3ZRdXc0czhYb3QyY3lVUHUxU3ZWT0JmWnFwNElkdTBSakZDLWctUkVCdUxxZUJfUHpNVzdNWHFTejFFcmtDaExleHlybVNqTTk1NWgwckxZOUNaOTVhS2h1QUNMcTJmNTh2WWdLZzdwOGhyVngtYVd4eHgySWhUOVREMkItUlE4Vi1Zaw?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQTjROQjJhVUJaVUVzdkZlS1ZiVERQUHZzVU5ZT01IWmd0dnJPUkdjVFdkaTdSc3ZQYmRZOXNIdFNRbkVVZDktZmlHWGZBbHFxTlEyekVWUktYOFp2ejhOOHZ1UGlRUkhQRjkybGx3ZzEwMUFtb1A4Y1MyZGxfc1NjeDhWeEE0ZHBIYUJxaEdYY3VNbGI2?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxPTGhhd1hWcjNNU0FXYUtVeWFoMHA2a1g2bXF2NzdWR0Z1TEpNaGNPMXpucmZtcjVyU29EemlvXy1UcldzV2ptVFBVV1I1QUN1SlI2SU9kR3RROGRqQTBKaFNXQ1NrQVpndU5MM29TZFZrUjI0dE9xTzFMU1E0RHB2dWR4RzhYSDk2LXVBWVhzOUlVeThDcElXOXZVODdoOXpsLTUxMFZvT3YweG1OSllpeEJSYUhUamQyNzVz?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxOZDdueVVpYndEZ240US1ZeURHeW1nX25Nb1VCdDJoUHpYd2I5WXZiLWdTUHpDVnI3RHhTamhqLUc3NXZiX0FsUTRDN1owd1pCU19Rem9JMThxa0tHMlZycEtBamV4TVdtVVpadDZPU3NKcFJ5MVF1LVdfdEY0RkJuVXozREhuSUNDNGR2aDdmcHluSWZBRG9MbFk1ZjhhUmFDSHlrMWhNY2VGMGxscDZHdGFINzYxYjFicHBORjNvU3FYTHFnNUFGeUNXejE?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxQcmE0d3pyc1dqb1c3ZzU5RnhDSy15aHVVcVFDU1NUMUN4X085ZmtjVnJhbEgxejltZEs1MWREN1ZrZlMyTkZJSEV6ZmFTb0tzai1UclEyZzdtMnhUTzMyc08yb2ZDQ3Ric1VhUFpVUmVPN3c0bU1DSEpVSVJkU2IzM3pPcnlFRzNjYkJZbUppZ0pWbzJia2dfajRheVpnbzAtVmFQeUtDeHAxR1ZRY3plSzNyM09uNUtiREFIZkZISlNQUnFsSnpsS3ZNbFU?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
