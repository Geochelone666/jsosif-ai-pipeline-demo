# ENB Intelligence Report

- ticker: **ENB**
- Report as_of: **2026-11-13**
- Market data as_of: **2026-11-13**
- Quant sources: https://finance.yahoo.com/quote/ENB/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ENB/key-statistics/
- AI analysis snapshot as_of: **2026-11-13**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-14T04:55:24.044237+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 16, 'rule': 1, 'ai': 6, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261113T045636Z-34122c9a/ENB** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 16 unique headlines; 11 named publishers; 0 exact duplicates; 16 HTTPS source links; largest publisher share 12.5%; oldest publication 2026-11-06

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 47.6700 |
| Return 1D (%) | 0.5060 |
| Return 1W (%) | 3.1210 |
| Return 1M (%) | 1.8825 |
| Return YTD (%) | 5.1802 |
| Return 1Y (%) | 4.2431 |
| Annualized volatility (%) | 18.2222 |
| Beta vs SPY | -0.1221 |
| Max drawdown (%) | -19.8462 |
| Sharpe (rf=0) | 0.3198 |
| Downside deviation (rf=0, %) | 12.8737 |
| Sortino (rf=0) | 0.4526 |
| Historical VaR 95% (1D, %) | 1.7623 |
| Historical ES 95% (1D, %) | 2.5078 |
| Correlation vs SPY | -0.0914 |
| Tracking error vs SPY (%) | 23.7342 |
| P/E (trailing) | 23.14 |
| P/B | 2.46 |
| EV/EBITDA | 13.11 |
| Revenue growth (%) | 44.00 |
| Forward P/E (estimate) | 21.42 |
| Gross margin (%) | 30.20 |
| Operating margin (%) | 12.82 |
| Return on equity (%) | 9.85 |
| Free cash flow yield (%) | N/A |
| MA50 | 47.1698 |
| Close vs MA50 (%) | 1.0604 |
| MA200 | 50.7422 |
| Close vs MA200 (%) | -6.0546 |
| RSI (14, Wilder) | 52.8640 |
| MACD (12,26) | 0.0316 |
| MACD signal (9) | 0.0651 |
| MACD histogram | -0.0334 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ENB': 282, 'SPY': 282}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 47.6700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.5060 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 3.1210 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 1.8825 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 5.1802 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 4.2431 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 18.2222 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 12.8737 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4526 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.7623 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.5078 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.0914 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.7342 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1221 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -19.8462 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3198 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 21.4183 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 30.1950 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 12.8210 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.8490 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 23.1408 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 52.8640 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.0334 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 1.0604 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -6.0546 -> Clearly below the moving-average trend level.

## TAILWINDS

### Energy Transfer’s EPS Missed by 20%. Enbridge’s Profit Nearly Doubled. Here’s Why I’m Not Worried About Either Dividend Even Though Both Still Fell Short.
- Summary: Enbridge’s profit nearly doubled, offsetting Energy Transfer’s EPS miss, indicating strong earnings performance.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingJBVV95cUxNRGQ5Q2RoVzN2emVUZTNsN2tEX1RQc2VLcUR0TmtENFR0ZFFGMVB1bzQxNVdzSUxPeUR2eXhSNWpCZHpTTVlRMjVpV0pjVHBERmNaTlFpeU8wUHVuYWszdTlsaXVaVm1DOWJoTTVhbVFzU0tub2xscEZTSVZMMlVaS1NvR1dFdXd3d1RNSEF5ZFZXUDJWcHloWnVZTTk0NjZHS2J6dFFSTW12YkVSam15a002bjRTM2lJeUduNEpuSmw2MmtmSW16UHIzZFRnRmsyc1A1dmJ6SUhVZWVielF0aERycDd4VFFiWFlYbHd5cEZLNWdtZWJFbVU1dVR0ZTJyQWRjd3dST2xsMFRkSFpGTjF0NWVWeWl1bG1Cd0Rn?oc=5>

### Enbridge stock: stronger Q3, steady 2026 outlook
- Summary: Enbridge reported stronger Q3 results and maintains a steady outlook for 2026, signaling robust earnings and guidance.
- Date: 2026-11-10 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxQUlk0bVFFZ3liZy1JbzlKdlEyTjhmOHpsdDNvLUktZVRRQU1FZVI4LVJxMllnZUxQLTVvS1ExbndMN0dkWi1wZUI3dkNJN29jMXFJbng5eTNma3dGY215UDMwVkt5SUUwTUk5WjdIMGtaeFk5eVJBb0c2LTIzNzFBT3o0TXJhbWV5V0VjSzVjeWNpWWdrTDgwVnRYbWNHaVRxMGlvWDhMcWtrZDFRNEE?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Enbridge (NYSE:ENB) Issues Quarterly Earnings Results
- Summary: Enbridge (NYSE:ENB) Issues Quarterly Earnings Results
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxQdmc1ZG9FZTlaYkxTb2Mzajg1amczcFZLdHlYeXdvLVdFT2o1a0o1bDBvY0VUWmlBR2NsV1pROTJIQTcyOGRKRlBJQ2kwbThoWDBTT3RiVWNrbWVXVFdsU3d5NDFOZ1BKNTZ4bms3VXpVR1F2S1lDS2xtZUxQTU5UQTNEbFVXd05iOEVaWExKNjJ3ZnpGdmpqOFJYRkk2WU5PaVNfOWpINTMxU3RLNzFrQndCU0c?oc=5>

### Enbridge vs. ExxonMobil: Which Energy Stock Is a Better Buy for 2027?
- Summary: Analyst compares Enbridge to ExxonMobil for 2027 investment.
- Date: 2026-11-10 | Impact: medium | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxPTGhhd1hWcjNNU0FXYUtVeWFoMHA2a1g2bXF2NzdWR0Z1TEpNaGNPMXpucmZtcjVyU29EemlvXy1UcldzV2ptVFBVV1I1QUN1SlI2SU9kR3RROGRqQTBKaFNXQ1NrQVpndU5MM29TZFZrUjI0dE9xTzFMU1E0RHB2dWR4RzhYSDk2LXVBWVhzOUlVeThDcElXOXZVODdoOXpsLTUxMFZvT3YweG1OSllpeEJSYUhUamQyNzVz?oc=5>

### Analysts’ Opinions Are Mixed on These Energy Stocks: Conocophillips (COP), Enbridge (ENB) and Transocean (RIG)
- Summary: Analysts hold varied views on Enbridge, suggesting uncertainty in valuation.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilgJBVV95cUxNN0hITWFXcS1BNWNtdC1DMENOdm1kcVB6VkdZQTRYb2pNU3hPZE9PVkwxamZnd3VKX0hYN0haUFRDSm5EQ1hsaUlLQ25TRjFhWmFWdmU0dDN5dFNkWXFpNENPQzZ5Mk9oR05neENfN1AzXy1ySE8tZ29JQXcxdF9RcV9qOGduWjJuWldmVmU1bEE1MDBDM0VzR2s4Q3hFSUd4a0tELWpaTDloaW95RjZuMkhYMl9qVjJRY1BRNUZ0NUlqWTBXOHFfWmtOY01HMDFFNDlxVkFtWTZQZ1hXcGdRdUdiMnZ6b19iemVrYm1YV21nOThxaVFpWVhsbWVQLThlTVEwM0RkXzJWdnEtQWw3RDBsa2xvdw?oc=5>

### Enbridge Completes $2.1 Billion Senior Notes Offering
- Summary: Enbridge issued $2.1B senior notes, expanding its debt portfolio.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxPcFhvdEt4X3M0aVhxaVZuS0NEeENwUEYxMUVHYTZxbXlpb2V5YjNETnpNb3hBNHdDSk40TzBScDdxQWdpUHM5QkRJaTJoZjFzOWpucThkR3FUTnVBQ3I3NG5tSXhVNFFkM01aaV91MVQtT0kzUWxXU0k3ZlRYWmpFV1BDakowdU5tOHFjeFYzd2ItMFMtTEFDVV9HSEZMRFprVXc0VUQ0RQ?oc=5>

### Enbridge Completes $1.1 Billion Subordinated Notes Offering
- Summary: Enbridge raised $1.1B through subordinated notes issuance.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxQRFF6NmlRZGEtWGR5LWlKMVlNeWZuLUFob0tMSk9QVGZzMFRXZktiUExOTWxOa0d3bGNVUHNxclZkSmxJYWZaY0Z1RE1vSUxYdTdRQ1BnYjJ4U01zZ1dkNXBUOGlkMEh2a2FUaWI2T05ZdVZycmZwV1BaanR4cnZHdE42N21xdFB3ejROemIyZVZGQVRLdmNRRU5semZwakhqb1VKMGdYeUt5Sy02ZThR?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ENB** | **23.14** | **2.46** | **13.11** | **44.00** | **106,251,091,968.00 USD** | **4.24** |
| TRP.TO | 24.88 | 3.76 | 16.75 | 8.80 | 96,165,502,976.00 CAD | 25.91 |
| KMI | 19.70 | 2.25 | 13.65 | 9.30 | 71,108,673,536.00 USD | 23.18 |
| EPD | 12.39 | 2.72 | 11.09 | 49.30 | 82,554,830,848.00 USD | 27.95 |

Peers fetched as_of: 2026-11-13; ENB reuses existing data (market data as_of: 2026-11-13); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-06
- Next expected earnings: 2027-02-12 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-13

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
- https://news.google.com/rss/articles/CBMirgFBVV95cUxQUlk0bVFFZ3liZy1JbzlKdlEyTjhmOHpsdDNvLUktZVRRQU1FZVI4LVJxMllnZUxQLTVvS1ExbndMN0dkWi1wZUI3dkNJN29jMXFJbng5eTNma3dGY215UDMwVkt5SUUwTUk5WjdIMGtaeFk5eVJBb0c2LTIzNzFBT3o0TXJhbWV5V0VjSzVjeWNpWWdrTDgwVnRYbWNHaVRxMGlvWDhMcWtrZDFRNEE?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxQdmc1ZG9FZTlaYkxTb2Mzajg1amczcFZLdHlYeXdvLVdFT2o1a0o1bDBvY0VUWmlBR2NsV1pROTJIQTcyOGRKRlBJQ2kwbThoWDBTT3RiVWNrbWVXVFdsU3d5NDFOZ1BKNTZ4bms3VXpVR1F2S1lDS2xtZUxQTU5UQTNEbFVXd05iOEVaWExKNjJ3ZnpGdmpqOFJYRkk2WU5PaVNfOWpINTMxU3RLNzFrQndCU0c?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxPTGhhd1hWcjNNU0FXYUtVeWFoMHA2a1g2bXF2NzdWR0Z1TEpNaGNPMXpucmZtcjVyU29EemlvXy1UcldzV2ptVFBVV1I1QUN1SlI2SU9kR3RROGRqQTBKaFNXQ1NrQVpndU5MM29TZFZrUjI0dE9xTzFMU1E0RHB2dWR4RzhYSDk2LXVBWVhzOUlVeThDcElXOXZVODdoOXpsLTUxMFZvT3YweG1OSllpeEJSYUhUamQyNzVz?oc=5
- https://news.google.com/rss/articles/CBMilgJBVV95cUxNN0hITWFXcS1BNWNtdC1DMENOdm1kcVB6VkdZQTRYb2pNU3hPZE9PVkwxamZnd3VKX0hYN0haUFRDSm5EQ1hsaUlLQ25TRjFhWmFWdmU0dDN5dFNkWXFpNENPQzZ5Mk9oR05neENfN1AzXy1ySE8tZ29JQXcxdF9RcV9qOGduWjJuWldmVmU1bEE1MDBDM0VzR2s4Q3hFSUd4a0tELWpaTDloaW95RjZuMkhYMl9qVjJRY1BRNUZ0NUlqWTBXOHFfWmtOY01HMDFFNDlxVkFtWTZQZ1hXcGdRdUdiMnZ6b19iemVrYm1YV21nOThxaVFpWVhsbWVQLThlTVEwM0RkXzJWdnEtQWw3RDBsa2xvdw?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPcFhvdEt4X3M0aVhxaVZuS0NEeENwUEYxMUVHYTZxbXlpb2V5YjNETnpNb3hBNHdDSk40TzBScDdxQWdpUHM5QkRJaTJoZjFzOWpucThkR3FUTnVBQ3I3NG5tSXhVNFFkM01aaV91MVQtT0kzUWxXU0k3ZlRYWmpFV1BDakowdU5tOHFjeFYzd2ItMFMtTEFDVV9HSEZMRFprVXc0VUQ0RQ?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxQRFF6NmlRZGEtWGR5LWlKMVlNeWZuLUFob0tMSk9QVGZzMFRXZktiUExOTWxOa0d3bGNVUHNxclZkSmxJYWZaY0Z1RE1vSUxYdTdRQ1BnYjJ4U01zZ1dkNXBUOGlkMEh2a2FUaWI2T05ZdVZycmZwV1BaanR4cnZHdE42N21xdFB3ejROemIyZVZGQVRLdmNRRU5semZwakhqb1VKMGdYeUt5Sy02ZThR?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
