# NVO Intelligence Report

- ticker: **NVO**
- Report as_of: **2026-11-16**
- Market data as_of: **2026-11-16**
- Quant sources: https://finance.yahoo.com/quote/NVO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVO/key-statistics/
- AI analysis snapshot as_of: **2026-11-16**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-17T06:38:44.365303+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 19, 'rule': 2, 'ai': 10, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261116T043911Z-b81cfeb4/NVO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 19 unique headlines; 12 named publishers; 0 exact duplicates; 19 HTTPS source links; largest publisher share 15.79%; oldest publication 2026-11-09

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 41.6000 |
| Return 1D (%) | -0.0721 |
| Return 1W (%) | 0.5317 |
| Return 1M (%) | 7.1337 |
| Return YTD (%) | -14.1573 |
| Return 1Y (%) | -9.4970 |
| Annualized volatility (%) | 45.4284 |
| Beta vs SPY | 0.9347 |
| Max drawdown (%) | -43.6699 |
| Sharpe (rf=0) | 0.0012 |
| Downside deviation (rf=0, %) | 33.9529 |
| Sortino (rf=0) | 0.0016 |
| Historical VaR 95% (1D, %) | 3.1076 |
| Historical ES 95% (1D, %) | 7.1674 |
| Correlation vs SPY | 0.2833 |
| Tracking error vs SPY (%) | 43.5769 |
| P/E (trailing) | 10.51 |
| P/B | 5.60 |
| EV/EBITDA | 1.50 |
| Revenue growth (%) | 5.60 |
| Forward P/E (estimate) | 11.84 |
| Gross margin (%) | 83.33 |
| Operating margin (%) | 50.78 |
| Return on equity (%) | 58.38 |
| Free cash flow yield (%) | N/A |
| MA50 | 39.9868 |
| Close vs MA50 (%) | 4.0343 |
| MA200 | 42.4346 |
| Close vs MA200 (%) | -1.9667 |
| RSI (14, Wilder) | 57.8884 |
| MACD (12,26) | 0.4401 |
| MACD signal (9) | 0.2118 |
| MACD histogram | 0.2283 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVO': 283, 'SPY': 283}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 41.6000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.0721 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.5317 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 7.1337 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -14.1573 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -9.4970 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 45.4284 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 33.9529 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.0016 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.1076 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 7.1674 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2833 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 43.5769 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.9347 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -43.6699 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.0012 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 11.8436 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 83.3330 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 50.7790 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 58.3840 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 10.5051 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 57.8884 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.2283 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 4.0343 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -1.9667 -> Slightly below the moving-average trend level.

## TAILWINDS

### Novo Nordisk Shares Gain 2.4% Following Additional CagriSema Weight-Loss Trial Analyses
- Summary: Novo Nordisk Shares Gain 2.4% Following Additional CagriSema Weight-Loss Trial Analyses
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxNNnNyS1J4UmNBSHdJS0VZXzdKZ0ljTnZPRHZ6NkF6Z2tDbm52LVRUM3MxNVVJVUFYdDdjTHlzbUVhQmRvTHV0WmJYT3ZKV3g1cjk4WHhWeUtrN1FPUzcwMHFremhhWTFVdlRNdV9ISk16dW55OE9EeTl1SXgzazRFLTJ6VWNjTnlOMVVxQ2RTaHk?oc=5>

### Novo Nordisk Seeks FDA, EMA Approval For Sickle Cell Disease Treatment – Here Are The Key Takeaways
- Summary: Novo Nordisk is pursuing regulatory approval for a sickle cell disease therapy, potentially opening a new market segment.
- Date: 2026-11-13 | Impact: high | Horizon: short | Confidence: 0.92
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxQei1KRWgxYnNxM1AtVlFXeFZxSElRUmJnS1gtX0M5SW5Ua0Q2YmQ0TndDVEVfWkx6SWFxNzFSWEt2QmgzSGNoNmJ0LXpaX1hmaGFZS0pLN2hUdElWY1pITGxUdEdSWnlhQnJWeUVRLUY4Q2NSSlV5MUpIbHNiRHpJMXE0NHRNRWotMlI2dlRFdEc?oc=5>

### Novo Nordisk reports additional CagriSema weight-loss findings (NVO:NYSE)
- Summary: Novo Nordisk announces new weight‑loss study results for CagriSema, supporting its efficacy and expanding its product portfolio.
- Date: 2026-11-15 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNaFdxUTJqNDdlLVA1b3FTR0ZJM1BzR3diSVlGSE9pQy1ZNmxpQS1HcHRsR0c5TEFaNzFGN3VlVDF0bU96REVEblFpOGtSQ0x4a3dMdU0ybVhjNVd3SlVZRDVyR0VkV2VKV3hSMHUyOUFONFRLMUhaYVlKRjhBYmN6bHptY0ZaeTJWNGJDZGstUnNpOVJtZDZzNlRRbVlIQUU5bEE?oc=5>

### Hims & Hers Climbs 6% Despite Five States Joining FTC Suit; Eli Lilly Dips, Novo Nordisk Holds Steady
- Summary: Novo Nordisk holds steady amid market fluctuations.
- Date: 2026-11-11 | Impact: low | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxNcVBlai1aLXh1d0pyRFBLQ1RkUHdxYUE2NEtST01QS2FQNjFvQzlKNk4tN1p3YllqOGhtLWtadzJFOEU3QnRJaUkzdkc4WDh5a1FNX0w0d0xteHotN1ZNUWpaVjJpWXVyZXlCWUZuTXJQTmFmaEtwNHdhblJaUnAxZnFmQTBlcGg4a3Fkd2tmQUEwZVhTaVVzMjkxaEJyQ1ZfVU5WRS1QWlJKdGtvOC1KdzVqQmdBVDJIZ0dWSzRpVGNOWXhUeDEzTVl2aFNQcW84M2RSVERCTQ?oc=5>

### What Could Novo Nordisk (NYSE:NVO) Reveal in Its Next Quarterly Results?
- Summary: Speculation on upcoming quarterly earnings highlights potential financial performance and guidance from Novo Nordisk.
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxOcHBNWHh3dEtZWUotYV92ZXg4VEpHbVlOeVhhRjdDeXNETE1pUE9yUFRYLWlrV0lPZGNqXzJDTjc2aHBOQ0tsTmRuUGdEQm9fSkRPLVNXM2RHeTdhTzQ2Zk5tQ1VPekdveWM2Mi1KVmo1T2xSVC1RMkxrMTAwMXhrQktiWkxHVjRlYUFHWHo4MmRFMXVRUTBoYjdlZmJIQkZGb0pLNU1PNkJhaGNualNhUFRDWFI?oc=5>

### Novo Nordisk (NVO) Stock Price Prediction 2026, 2030, 2040-2060
- Summary: Long‑term price forecasts up to 2060.
- Date: 2026-11-09 | Impact: medium | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiWkFVX3lxTE5mbUJYcVVhZnVIYmpiS3NFZGhfX1ppYUtIRXdsNC1hXy1sMFg0YjFFLW5DZmx3RGQ4d2JlVEZEYnluSDZjbHJBeEJBODQ2RHZpX25XLWc2ck5YUQ?oc=5>

## HEADWINDS

### Novo Nordisk hit by FDA warning on Ozempic: Can NVO avoid further decline?
- Summary: FDA warning risks further decline.
- Date: 2026-11-11 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxQOC1MYXFoRzRtTjFmSVRpTVdFVkF0T1d1Q3VRYnRWRE1mcUg1V3gxMjJYSnNYNGVVNFFLdVE3eEJ6RUxDTE4tZEg5WlI0c0ZSZW5FZnRabFZqLVdCTkY2LXlsbmczeXNQN3Y4UE9VS1VGckFmY1NvS2dHSUNYNkhHLTVTWXpCOGMtdlAyOTNpMno2dw?oc=5>

## CATALYSTS

### Novo Nordisk Details Share Repurchases Through November 13
- Summary: Novo Nordisk Details Share Repurchases Through November 13
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxQWnRVYXd1cHFIVFZhTkt6YVB0RGdmMXIwMUtWTzdrLVhLZTRsLUw3RkpWak0wUmpVb3oxSjg2dV9zdThzekFTRUVVazYwWTJqTl9WejFfck5aeUpLd05oN2Rjc25SWEVuREFEVVdjdExycC00Zm5va040dm9iUS1kenVzNHR2NER6X1kwSFlJVHFzWGxtUWk5Q19OV3pDQkFXR21CMnZkbDBPRS1wYXU4?oc=5>

### Buybacks at Novo Nordisk (NVO) total 43.7 million B shares; treasury holdings equal 1.3%.
- Summary: Company repurchases 43.7M shares, reducing shares outstanding.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQSm1sdVlfVVg2ZEZHTU9PNTl3UmdFb21SRHZGaV9YdTFXWXczdDlONkZkVEE1QXJYcjBPU0FXWF9QSHBWbjc5ek04X3F3WE5hQzBuUFFvXzAzbF8xQWpiTFpIOFF6WjhTN2Qzb0RHa2tHZkZGS1RnM25LWENCTFlLNjNVQlRYOWF1Y0FjZUZfbjl0UGpLX1BKbFJkMXM3TGZmaGs3Umw1UHZCX3RYdEdueQ?oc=5>

### Novo Nordisk's (NYSE: NVO) 70% Stock Decline Creates Value Case As Wegovy Pill Crosses 8 Million Prescriptions
- Summary: Stock fell 70%, but Wegovy prescriptions hit 8M, suggesting value potential.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi6gFBVV95cUxNMFV3M2lPNjBpdHBrZC1UZVVIak9rUF9OZzhydVlSSG1vd2twblVLSXc2aU05M3E5dzJ1WHp2VVBXM2RLeGVZWm1jelMtOFVEemlfbC1hdzBwTWNOb3ZRNm5JQWVDR1RQMWxEaDhDZFZaOWlsTVBtNzllV2hyb0hOazRTOWVrTkhZMlkxRlVDZ1dfUlV1OWMxdm1SamxTVFlnc09jZDRYNEZhallINjJQTm5tNU0wOGgzdkR2MmU4ZUlCdjQya0s3dTV3YlB0OE5HOGNOM0xRMGdDY0VpSUtvdjhQUTExTXRfM1E?oc=5>

### Novo Nordisk (NVO) Could Be 46% Undervalued After Wegovy Pill Prescription Focus
- Summary: Analysis indicates 46% undervaluation based on Wegovy prescription data.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi2wFBVV95cUxOTjZCQzdadDc2R3JJMWJDUUw5TWpLNndudjNBcXN3RlRENXhZeTRGaUwwMkoteUxOeGhXNTZvS29vY0dGRnJzYlFOdV83MnVoSUVTM3FlWlJRY0t3OGwyS29LMjFWa2h2aFktQkcxM3NaXzRKRVpUWWdlbTVpcG9UcGY5STE1ZXZSNmxNRmdBam9Ea3p0b2lqT3NCeGs2U0xWZ2JETC1Mc0p1YUpBZ2RHU3lyRVU2bEpJWElwRHNpVkxiWnY3OW8tOXVWTkF6dFRXdnhWT0pGcHVta3fSAeABQVVfeXFMT1BQZ2gxMExPVDlVY3VBeDA1LWx5eHhtVkdja0hkbFl6YmotYWZVdWNXM2IzWEhEaV9XTWFnVXVmZGxDdEVVTXJkbjNELVRSdk1XTWxNZXZWQW40cmM3T3kzOGtnSkEzZTlCVU00SUl2RVAtZ2x6RVdpSjMwTHdYN0FqMVRTV1ZGNmpDcnpCWWdWSmpMbG5vMkhPakFQZW1KSzMwOXRTSWpRZ2pvSGw3QldGUVotdHpVVnYwM1FNamFtS3l1bTVwSHcySWplRTBaa1NrSERTaVVpTW40cERZMFQ?oc=5>

### Novo Nordisk (NVO) Stock Price Prediction: BMO’s higher target meets a mixed technical tape
- Summary: BMO raises target; technical signals mixed, neutral outlook.
- Date: 2026-11-12 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxORXlQbEs4U2NOdEtMc1UzZUlxdHUyTEtHNVVpNG5tN08tdlk1UnF6OFpybXoySTh1dEdEMWx6TVJXUDV1RWVzeEYyWXoxUC1UY0c4anIxR2RqRFVoZzlRb2tScDllaWZSVzYtb3RrbmxZWURWYTVBMmFDS1BxZ1JvM3dVUzRHRjhYbzJtVGNwa0htNTVNWXg2bk94bWZYMlZlTFhn?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVO** | **10.51** | **5.60** | **1.50** | **5.60** | **183,387,570,176.00 USD** | **-9.50** |
| LLY | 46.47 | 31.68 | 28.39 | 38.60 | 1,275,252,965,376.00 USD | 40.48 |
| ROG.SW | N/A | N/A | N/A | N/A | N/A unknown currency | N/A |
| SAN.PA | 25.53 | 1.45 | 8.14 | 15.70 | 106,037,551,104.00 EUR | 2.28 |

Peers fetched as_of: 2026-11-16; NVO reuses existing data (market data as_of: 2026-11-16); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-04
- Next expected earnings: 2027-02-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-16

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: N/A
- Filing date: N/A
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: N/A

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMikAFBVV95cUxNNnNyS1J4UmNBSHdJS0VZXzdKZ0ljTnZPRHZ6NkF6Z2tDbm52LVRUM3MxNVVJVUFYdDdjTHlzbUVhQmRvTHV0WmJYT3ZKV3g1cjk4WHhWeUtrN1FPUzcwMHFremhhWTFVdlRNdV9ISk16dW55OE9EeTl1SXgzazRFLTJ6VWNjTnlOMVVxQ2RTaHk?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxQei1KRWgxYnNxM1AtVlFXeFZxSElRUmJnS1gtX0M5SW5Ua0Q2YmQ0TndDVEVfWkx6SWFxNzFSWEt2QmgzSGNoNmJ0LXpaX1hmaGFZS0pLN2hUdElWY1pITGxUdEdSWnlhQnJWeUVRLUY4Q2NSSlV5MUpIbHNiRHpJMXE0NHRNRWotMlI2dlRFdEc?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNaFdxUTJqNDdlLVA1b3FTR0ZJM1BzR3diSVlGSE9pQy1ZNmxpQS1HcHRsR0c5TEFaNzFGN3VlVDF0bU96REVEblFpOGtSQ0x4a3dMdU0ybVhjNVd3SlVZRDVyR0VkV2VKV3hSMHUyOUFONFRLMUhaYVlKRjhBYmN6bHptY0ZaeTJWNGJDZGstUnNpOVJtZDZzNlRRbVlIQUU5bEE?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxNcVBlai1aLXh1d0pyRFBLQ1RkUHdxYUE2NEtST01QS2FQNjFvQzlKNk4tN1p3YllqOGhtLWtadzJFOEU3QnRJaUkzdkc4WDh5a1FNX0w0d0xteHotN1ZNUWpaVjJpWXVyZXlCWUZuTXJQTmFmaEtwNHdhblJaUnAxZnFmQTBlcGg4a3Fkd2tmQUEwZVhTaVVzMjkxaEJyQ1ZfVU5WRS1QWlJKdGtvOC1KdzVqQmdBVDJIZ0dWSzRpVGNOWXhUeDEzTVl2aFNQcW84M2RSVERCTQ?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxOcHBNWHh3dEtZWUotYV92ZXg4VEpHbVlOeVhhRjdDeXNETE1pUE9yUFRYLWlrV0lPZGNqXzJDTjc2aHBOQ0tsTmRuUGdEQm9fSkRPLVNXM2RHeTdhTzQ2Zk5tQ1VPekdveWM2Mi1KVmo1T2xSVC1RMkxrMTAwMXhrQktiWkxHVjRlYUFHWHo4MmRFMXVRUTBoYjdlZmJIQkZGb0pLNU1PNkJhaGNualNhUFRDWFI?oc=5
- https://news.google.com/rss/articles/CBMiWkFVX3lxTE5mbUJYcVVhZnVIYmpiS3NFZGhfX1ppYUtIRXdsNC1hXy1sMFg0YjFFLW5DZmx3RGQ4d2JlVEZEYnluSDZjbHJBeEJBODQ2RHZpX25XLWc2ck5YUQ?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxQOC1MYXFoRzRtTjFmSVRpTVdFVkF0T1d1Q3VRYnRWRE1mcUg1V3gxMjJYSnNYNGVVNFFLdVE3eEJ6RUxDTE4tZEg5WlI0c0ZSZW5FZnRabFZqLVdCTkY2LXlsbmczeXNQN3Y4UE9VS1VGckFmY1NvS2dHSUNYNkhHLTVTWXpCOGMtdlAyOTNpMno2dw?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxQWnRVYXd1cHFIVFZhTkt6YVB0RGdmMXIwMUtWTzdrLVhLZTRsLUw3RkpWak0wUmpVb3oxSjg2dV9zdThzekFTRUVVazYwWTJqTl9WejFfck5aeUpLd05oN2Rjc25SWEVuREFEVVdjdExycC00Zm5va040dm9iUS1kenVzNHR2NER6X1kwSFlJVHFzWGxtUWk5Q19OV3pDQkFXR21CMnZkbDBPRS1wYXU4?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxQSm1sdVlfVVg2ZEZHTU9PNTl3UmdFb21SRHZGaV9YdTFXWXczdDlONkZkVEE1QXJYcjBPU0FXWF9QSHBWbjc5ek04X3F3WE5hQzBuUFFvXzAzbF8xQWpiTFpIOFF6WjhTN2Qzb0RHa2tHZkZGS1RnM25LWENCTFlLNjNVQlRYOWF1Y0FjZUZfbjl0UGpLX1BKbFJkMXM3TGZmaGs3Umw1UHZCX3RYdEdueQ?oc=5
- https://news.google.com/rss/articles/CBMi6gFBVV95cUxNMFV3M2lPNjBpdHBrZC1UZVVIak9rUF9OZzhydVlSSG1vd2twblVLSXc2aU05M3E5dzJ1WHp2VVBXM2RLeGVZWm1jelMtOFVEemlfbC1hdzBwTWNOb3ZRNm5JQWVDR1RQMWxEaDhDZFZaOWlsTVBtNzllV2hyb0hOazRTOWVrTkhZMlkxRlVDZ1dfUlV1OWMxdm1SamxTVFlnc09jZDRYNEZhallINjJQTm5tNU0wOGgzdkR2MmU4ZUlCdjQya0s3dTV3YlB0OE5HOGNOM0xRMGdDY0VpSUtvdjhQUTExTXRfM1E?oc=5
- https://news.google.com/rss/articles/CBMi2wFBVV95cUxOTjZCQzdadDc2R3JJMWJDUUw5TWpLNndudjNBcXN3RlRENXhZeTRGaUwwMkoteUxOeGhXNTZvS29vY0dGRnJzYlFOdV83MnVoSUVTM3FlWlJRY0t3OGwyS29LMjFWa2h2aFktQkcxM3NaXzRKRVpUWWdlbTVpcG9UcGY5STE1ZXZSNmxNRmdBam9Ea3p0b2lqT3NCeGs2U0xWZ2JETC1Mc0p1YUpBZ2RHU3lyRVU2bEpJWElwRHNpVkxiWnY3OW8tOXVWTkF6dFRXdnhWT0pGcHVta3fSAeABQVVfeXFMT1BQZ2gxMExPVDlVY3VBeDA1LWx5eHhtVkdja0hkbFl6YmotYWZVdWNXM2IzWEhEaV9XTWFnVXVmZGxDdEVVTXJkbjNELVRSdk1XTWxNZXZWQW40cmM3T3kzOGtnSkEzZTlCVU00SUl2RVAtZ2x6RVdpSjMwTHdYN0FqMVRTV1ZGNmpDcnpCWWdWSmpMbG5vMkhPakFQZW1KSzMwOXRTSWpRZ2pvSGw3QldGUVotdHpVVnYwM1FNamFtS3l1bTVwSHcySWplRTBaa1NrSERTaVVpTW40cERZMFQ?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxORXlQbEs4U2NOdEtMc1UzZUlxdHUyTEtHNVVpNG5tN08tdlk1UnF6OFpybXoySTh1dEdEMWx6TVJXUDV1RWVzeEYyWXoxUC1UY0c4anIxR2RqRFVoZzlRb2tScDllaWZSVzYtb3RrbmxZWURWYTVBMmFDS1BxZ1JvM3dVUzRHRjhYbzJtVGNwa0htNTVNWXg2bk94bWZYMlZlTFhn?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
