# ENB Intelligence Report

- ticker: **ENB**
- Report as_of: **2026-11-24**
- Market data as_of: **2026-11-24**
- Quant sources: https://finance.yahoo.com/quote/ENB/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ENB/key-statistics/
- AI analysis snapshot as_of: **2026-11-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-25T07:09:07.931358+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 17, 'rule': 5, 'ai': 3, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261124T081701Z-6c335e3d/ENB** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'directional_claim_without_event_type': 1}
- RSS source audit (metadata only, not article fact-checking): 17 unique headlines; 8 named publishers; 0 exact duplicates; 17 HTTPS source links; largest publisher share 29.41%; oldest publication 2026-11-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 46.2400 |
| Return 1D (%) | 1.9176 |
| Return 1W (%) | -1.9300 |
| Return 1M (%) | -2.5900 |
| Return YTD (%) | 2.0250 |
| Return 1Y (%) | 3.1246 |
| Annualized volatility (%) | 18.3356 |
| Beta vs SPY | -0.0771 |
| Max drawdown (%) | -19.8462 |
| Sharpe (rf=0) | 0.2598 |
| Downside deviation (rf=0, %) | 12.9555 |
| Sortino (rf=0) | 0.3678 |
| Historical VaR 95% (1D, %) | 1.8065 |
| Historical ES 95% (1D, %) | 2.5127 |
| Correlation vs SPY | -0.0629 |
| Tracking error vs SPY (%) | 24.3785 |
| P/E (trailing) | 22.34 |
| P/B | 2.38 |
| EV/EBITDA | 12.93 |
| Revenue growth (%) | 44.00 |
| Forward P/E (estimate) | 20.82 |
| Gross margin (%) | 30.20 |
| Operating margin (%) | 12.82 |
| Return on equity (%) | 9.85 |
| Free cash flow yield (%) | N/A |
| MA50 | 46.8912 |
| Close vs MA50 (%) | -1.3888 |
| MA200 | 50.7154 |
| Close vs MA200 (%) | -8.8246 |
| RSI (14, Wilder) | 43.5435 |
| MACD (12,26) | -0.3546 |
| MACD signal (9) | -0.1640 |
| MACD histogram | -0.1907 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ENB': 289, 'SPY': 289}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 46.2400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.9176 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.9300 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -2.5900 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 2.0250 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 3.1246 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 18.3356 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 12.9555 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.3678 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.8065 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.5127 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.0629 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.3785 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.0771 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -19.8462 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2598 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 20.8223 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 30.1950 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 12.8210 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.8490 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 22.3382 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 43.5435 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.1907 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -1.3888 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -8.8246 -> Clearly below the moving-average trend level.

## TAILWINDS

### Utilities Focus: Enbridge Inc. (TSX:ENB) — S&P/TSX Composite Large Cap Value Stock in Focus After Fresh Corporate News
- Summary: Enbridge highlighted as a value stock in the TSX Composite after recent corporate updates.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi2wFBVV95cUxNR2ZjM1kza0RlcU9zaEZKSWVzUUFhNnJXNUZFNnlGSFF4OFNqd2tLWENNdVZXU1FXT1NDc2NWN29idGozTDRId1hXS1p5MzNKeWhnQ2FhSWNSaHVhLVotLTVrY2Q1V1J5TEE2bzJXTzU5YklSM0ljdmpfeU1sWDUtcTlmMnJLMlduNVFtNmxWaVowUmZrWGJUbjV6aDhVbGVrMTJmcDEyd1RKRUZwN3NFZHdOdnZRRzV3RnAtd3B6QXlxR3ozeHVUR1ZuR0JpS1lkUjF6eGJnamZjdE0?oc=5>

## HEADWINDS

### Enbridge shares technical analysis: Trading flat under seller pressure near key support
- Summary: Enbridge shares technical analysis: Trading flat under seller pressure near key support
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPeGxzNTdkZDYwTWc0WUFSQ0pwYzJLS1RMV1lEWGM3eEMtVmFhOTBfTXp4SFpvSl93dUwwZnAyaWpIWXdSYVRUcXhJandYaGtXb1FyWWpDMXktNUJ0dzkzdk83c1dRekctdEFJbk9TRU1VM1lObjZmY2U3bEhPTWp4VTNWeXZ2ZGdjLUJ6Y0RYbnR4aFU?oc=5>

### Enbridge Inc. (TSX:ENB) Stock Under Pressure: 1.42% Decline Raises Valuation Concerns Despite Resilient Energy Infrastructure Business
- Summary: Enbridge Inc. (TSX:ENB) Stock Under Pressure: 1.42% Decline Raises Valuation Concerns Despite Resilient Energy Infrastructure Business
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7wFBVV95cUxQZlJ1WkpaNnoxRF9XaVNPZ1VPSEktb0Q1WW5zVll3bVA3UVIzR3dVTmZ3elJnZ2F5UlpjZ0ZhSkhJUFJ3RTBfU3h2cmc1b3MzNUFBcm13Tm42MHZZdEZTZlBwREFTbC1RVlRqNTN5RFdaRGtCbVdsNUVndkRSWGdIdlN2R01BX0FZQUtZblRUZldDSnNFQmpRLTZGaVFxazUyRjRDYjFta3J5cTAtTU1lR1Z3a2lkdHA3N0NfWk8wcjlKb2FWV18tNDFSRjU4RzRGQ0dEU1Bib2VmS1ZYU2wyTnhTYWh0ZVhuVzljaVhhVQ?oc=5>

## CATALYSTS

### Enbridge sees large fund acquisition: ENB remains range-bound
- Summary: Enbridge sees large fund acquisition: ENB remains range-bound
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPS0FoRnJaaGtLakkxeTNhYTRQNjU1VC1VanpYYlRmWnlpNzZWNEtER05GR1BOR1VHMXJUNTRmczFPaTNBTEJZM1ZYM04zb0oyWE5mNEFjUmZPZ01xWlIzcjdlN0dJY2NXMVIyUEdkLUhPX1NBREtRU3pRbm80bVU4eVFlSWYtOWVtTjZWd0tycVMtWDg?oc=5>

### Enbridge Stock: Is It Still a Top Passive Income Pick for Retirees?
- Summary: Enbridge Stock: Is It Still a Top Passive Income Pick for Retirees?
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxNaHJLNGp5dW44UnlHVEhKMmZvazQ0bmJpV2x4bGtlMjM3MURBUHBYSEtpbFJid3hYdkRKZzhiNUJwWnluSWFJLUczNEo2clNxYkx6eEhvSVJzWks4VjU4Q0IydGVVbEZNMlVzWmoyeEdCUFNsbkVKT1JGUlhDQUNVZDdFYUlsUncw?oc=5>

### Enbridge stock: Wexpro secures approval for US dollar 485 million deal
- Summary: Enbridge stock: Wexpro secures approval for US dollar 485 million deal
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxOQzBHOE81Q0Z1WG52NE9oTUpvU1c2OUM5SklPMFYxU2VhTDJhRGFtUDVkeEpRbUZ4OWNBX0U0ZmhUdkZGbTBNQmF5YlRYbWdrem9heWdkNXFvVXZLV082bktDaWNrVXBQN0lKMkhiMnZyY3BZMktzdTFlTDFSc0pGUW1LcnprYmlPNUNENkxLXzRiTTNJLVNHQUM4ZDV3Y0JmdG81azh5eTZzVWxNaEFVNVZabVJRRVI1ZFpIczJiZGRJVmkyT21KOENfUW8?oc=5>

### Enbridge sees major pension fund stake increase: Can ENB recover from persistent seller pressure?
- Summary: A major pension fund increased its stake in Enbridge, potentially supporting the stock amid seller pressure.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxQaXhhWEZvc0RCYUF0M0pibEVYRzBLc0xGenBmdkZUdG1IY2F2a2d1M0ZuMVF1ODlEc09IQ0FZVEhYTUZ5U2NXY0VRZ1NiLXFaT3RVRXNBV2ZiNDB4VDZXdGJRLUFSSmpNeFJvQVJDZXdScGREMXotSldaTndGaDZzbW5IYlJld1NST29PQlJTZzJNdw?oc=5>

### Is Enbridge (TSX:ENB) Undervalued As Investors Reassess Its Acquisition Driven Growth?
- Summary: Analysts question Enbridge’s valuation, suggesting potential upside from acquisition-driven growth.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxPTGRfRnpycWZUUlNzUnpaZVFTZGswakdQRmZWRDVXbldPTk1tVUhheWNCbUdEVDBoUFRPdlRPZGwwUGs0UHNucWNtMHZ3U0ZOaVpzbkh3VXI5V1hra2JJUG1PVjVpYzJpdi14Q2Q0Mm54RG55cEc3andwODdYNXAyNVJxQ2Fkd19OSnppbVItN2Q1NFhLaWpLX2YtYVhSUDRMbjBWVXF0VU1udmt1U1FONVl0VFc2VUlsWWVhWE9ENlhQeThKV3Bj0gHMAUFVX3lxTE9hUW10el9ZaXJFbGdLN2wxajhyVHFiNXlxZDRRZjRCeVJwUERfbFdJblFOUTJsSW9PaERCaXhyZ2xpSlRNZWNuTkJBQUI4RXJBZGw3aF9kc3p5NVRDTzJoelpLdUNIQk15dDVWcldyZUdIN1pJWXpKcldtY05aNHNBRmJKV00taXhHY3dPSUNHZm1lR3dJM2hoVWdBZmN2VkVsa0FUMzlOWEVGSDJITDk2bzNwNjREdDJYVTdCV3QzekhHenJpLXhiSzJTQw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ENB** | **22.34** | **2.38** | **12.93** | **44.00** | **103,063,789,568.00 USD** | **3.12** |
| TRP.TO | 23.77 | 3.60 | 16.36 | 8.80 | 92,133,867,520.00 CAD | 21.40 |
| KMI | 19.19 | 2.19 | 13.40 | 9.30 | 69,237,391,360.00 USD | 20.25 |
| EPD | 11.92 | 2.56 | 10.63 | 49.30 | 77,637,779,456.00 USD | 17.41 |

Peers fetched as_of: 2026-11-24; ENB reuses existing data (market data as_of: 2026-11-24); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-06
- Next expected earnings: 2027-02-12 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-24

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

- https://news.google.com/rss/articles/CBMi2wFBVV95cUxNR2ZjM1kza0RlcU9zaEZKSWVzUUFhNnJXNUZFNnlGSFF4OFNqd2tLWENNdVZXU1FXT1NDc2NWN29idGozTDRId1hXS1p5MzNKeWhnQ2FhSWNSaHVhLVotLTVrY2Q1V1J5TEE2bzJXTzU5YklSM0ljdmpfeU1sWDUtcTlmMnJLMlduNVFtNmxWaVowUmZrWGJUbjV6aDhVbGVrMTJmcDEyd1RKRUZwN3NFZHdOdnZRRzV3RnAtd3B6QXlxR3ozeHVUR1ZuR0JpS1lkUjF6eGJnamZjdE0?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPeGxzNTdkZDYwTWc0WUFSQ0pwYzJLS1RMV1lEWGM3eEMtVmFhOTBfTXp4SFpvSl93dUwwZnAyaWpIWXdSYVRUcXhJandYaGtXb1FyWWpDMXktNUJ0dzkzdk83c1dRekctdEFJbk9TRU1VM1lObjZmY2U3bEhPTWp4VTNWeXZ2ZGdjLUJ6Y0RYbnR4aFU?oc=5
- https://news.google.com/rss/articles/CBMi7wFBVV95cUxQZlJ1WkpaNnoxRF9XaVNPZ1VPSEktb0Q1WW5zVll3bVA3UVIzR3dVTmZ3elJnZ2F5UlpjZ0ZhSkhJUFJ3RTBfU3h2cmc1b3MzNUFBcm13Tm42MHZZdEZTZlBwREFTbC1RVlRqNTN5RFdaRGtCbVdsNUVndkRSWGdIdlN2R01BX0FZQUtZblRUZldDSnNFQmpRLTZGaVFxazUyRjRDYjFta3J5cTAtTU1lR1Z3a2lkdHA3N0NfWk8wcjlKb2FWV18tNDFSRjU4RzRGQ0dEU1Bib2VmS1ZYU2wyTnhTYWh0ZVhuVzljaVhhVQ?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPS0FoRnJaaGtLakkxeTNhYTRQNjU1VC1VanpYYlRmWnlpNzZWNEtER05GR1BOR1VHMXJUNTRmczFPaTNBTEJZM1ZYM04zb0oyWE5mNEFjUmZPZ01xWlIzcjdlN0dJY2NXMVIyUEdkLUhPX1NBREtRU3pRbm80bVU4eVFlSWYtOWVtTjZWd0tycVMtWDg?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxNaHJLNGp5dW44UnlHVEhKMmZvazQ0bmJpV2x4bGtlMjM3MURBUHBYSEtpbFJid3hYdkRKZzhiNUJwWnluSWFJLUczNEo2clNxYkx6eEhvSVJzWks4VjU4Q0IydGVVbEZNMlVzWmoyeEdCUFNsbkVKT1JGUlhDQUNVZDdFYUlsUncw?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxOQzBHOE81Q0Z1WG52NE9oTUpvU1c2OUM5SklPMFYxU2VhTDJhRGFtUDVkeEpRbUZ4OWNBX0U0ZmhUdkZGbTBNQmF5YlRYbWdrem9heWdkNXFvVXZLV082bktDaWNrVXBQN0lKMkhiMnZyY3BZMktzdTFlTDFSc0pGUW1LcnprYmlPNUNENkxLXzRiTTNJLVNHQUM4ZDV3Y0JmdG81azh5eTZzVWxNaEFVNVZabVJRRVI1ZFpIczJiZGRJVmkyT21KOENfUW8?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxQaXhhWEZvc0RCYUF0M0pibEVYRzBLc0xGenBmdkZUdG1IY2F2a2d1M0ZuMVF1ODlEc09IQ0FZVEhYTUZ5U2NXY0VRZ1NiLXFaT3RVRXNBV2ZiNDB4VDZXdGJRLUFSSmpNeFJvQVJDZXdScGREMXotSldaTndGaDZzbW5IYlJld1NST29PQlJTZzJNdw?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxPTGRfRnpycWZUUlNzUnpaZVFTZGswakdQRmZWRDVXbldPTk1tVUhheWNCbUdEVDBoUFRPdlRPZGwwUGs0UHNucWNtMHZ3U0ZOaVpzbkh3VXI5V1hra2JJUG1PVjVpYzJpdi14Q2Q0Mm54RG55cEc3andwODdYNXAyNVJxQ2Fkd19OSnppbVItN2Q1NFhLaWpLX2YtYVhSUDRMbjBWVXF0VU1udmt1U1FONVl0VFc2VUlsWWVhWE9ENlhQeThKV3Bj0gHMAUFVX3lxTE9hUW10el9ZaXJFbGdLN2wxajhyVHFiNXlxZDRRZjRCeVJwUERfbFdJblFOUTJsSW9PaERCaXhyZ2xpSlRNZWNuTkJBQUI4RXJBZGw3aF9kc3p5NVRDTzJoelpLdUNIQk15dDVWcldyZUdIN1pJWXpKcldtY05aNHNBRmJKV00taXhHY3dPSUNHZm1lR3dJM2hoVWdBZmN2VkVsa0FUMzlOWEVGSDJITDk2bzNwNjREdDJYVTdCV3QzekhHenJpLXhiSzJTQw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
