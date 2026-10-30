# ENB Intelligence Report

- ticker: **ENB**
- Report as_of: **2026-10-29**
- Market data as_of: **2026-10-29**
- Quant sources: https://finance.yahoo.com/quote/ENB/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ENB/key-statistics/
- AI analysis snapshot as_of: **2026-10-29**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-30T02:23:58.932517+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 8, 'rule': 1, 'ai': 6, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261029T020157Z-688a53f0/ENB** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 8 unique headlines; 6 named publishers; 0 exact duplicates; 8 HTTPS source links; largest publisher share 37.5%; oldest publication 2026-10-22

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 49.2700 |
| Return 1D (%) | 1.4830 |
| Return 1W (%) | 2.6245 |
| Return 1M (%) | 5.6163 |
| Return YTD (%) | 7.1740 |
| Return 1Y (%) | 9.8378 |
| Annualized volatility (%) | 18.1014 |
| Beta vs SPY | -0.1727 |
| Max drawdown (%) | -19.8462 |
| Sharpe (rf=0) | 0.6107 |
| Downside deviation (rf=0, %) | 12.5860 |
| Sortino (rf=0) | 0.8783 |
| Historical VaR 95% (1D, %) | 1.7452 |
| Historical ES 95% (1D, %) | 2.4474 |
| Correlation vs SPY | -0.1213 |
| Tracking error vs SPY (%) | 23.3453 |
| P/E (trailing) | 26.35 |
| P/B | 2.58 |
| EV/EBITDA | 13.12 |
| Revenue growth (%) | 97.10 |
| Forward P/E (estimate) | 21.76 |
| Gross margin (%) | 32.59 |
| Operating margin (%) | 10.16 |
| Return on equity (%) | 9.22 |
| Free cash flow yield (%) | N/A |
| MA50 | 48.3058 |
| Close vs MA50 (%) | 1.9960 |
| MA200 | 51.3371 |
| Close vs MA200 (%) | -4.0265 |
| RSI (14, Wilder) | 63.2943 |
| MACD (12,26) | 0.1790 |
| MACD signal (9) | -0.1210 |
| MACD histogram | 0.3001 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ENB': 271, 'SPY': 271}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 49.2700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.4830 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.6245 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 5.6163 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 7.1740 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 9.8378 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 18.1014 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 12.5860 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.8783 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.7452 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.4474 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1213 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.3453 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1727 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -19.8462 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.6107 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 21.7615 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 32.5940 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 10.1610 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.2210 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 26.3476 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 63.2943 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.3001 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 1.9960 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -4.0265 -> Slightly below the moving-average trend level.

## TAILWINDS

### Enbridge (ENB) Gains As Market Dips: What You Should Know
- Summary: Enbridge shares rise amid broader market decline, reflecting investor confidence in the company.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOcGlxcW90c0V2WGtiQlRjUll0RVdfQ1JNbkY0V3oxZjFWS1BTRWtJb0tCUnZkOWVndG91ZC1ISi10VkotVkw1dUxkNXJ4N2xoSS1LcE9YOExNakNJSkFLVkpiczRScUJOeUwxYnlSRmVNZUtMYzJTQjQ1SVVBTzVlcHdyNktIR0lVMTM1Y1FIY0ZrVHNfd0F0T2hndw?oc=5>

## HEADWINDS

### Enbridge Stock is Down 16%, but the Business Looks Smart: Here’s How I’d Buy the Stock
- Summary: Enbridge Stock is Down 16%, but the Business Looks Smart: Here’s How I’d Buy the Stock
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi-wFBVV95cUxOR3dDYnVSQmpybU5nYXlpNjBLQThBMW5RNXBlTzk1V2ttbnhPMFNHdXJxUUlTS3YzTVlPTFdfT1d5MU1rMkp0czJyTXgteU9GaFNra3VzTXhBdk1QaUhIWVJJZzFzdGFTSTlBdW9jMUF5SDBSY3pQamJmQXlaOWVic2ZIQTJSWkZqSW5STFF6RnVNOXhVZ25fWmFlb1dkT29vTjRlRThGOUZ2cEpMOVQwNDdjT0w3MlNaQlNMN0IyS2RNWE9tcE5GOERKMFl0Y0tpNnpDX0Jkcmoyd0lDR3ZSYlJ0elRhWFdQLXNHS2c2STVyZWV2U0IweUxEaw?oc=5>

## CATALYSTS

### Investors Heavily Search Enbridge Inc (ENB): Here is What You Need to Know
- Summary: Investors are actively researching Enbridge, indicating growing interest and potential positive sentiment.
- Date: 2026-10-28 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxPQzBzUFVBMHNRb2Y1YS1OYktvekxLUWxKc0VJbzRKdDFrdG5EdklBVnVaRFdXeGctLUZsNzJud2pMMjh2T01IZE5xX1Q5QlJFcWR1Q1lHTjZrM0NCVWQwZy1MSTRua1dpNnVDTHctYnVqWjRyaHVVRzRRbFVjbnZTNGM5bTdSM0Z6Skd0STVlNA?oc=5>

### Enbridge Stock: 3 Things to Look for in Its Q3 Results
- Summary: Highlights key metrics for upcoming earnings.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigwFBVV95cUxNZ3VuR2ZHZlZjWFBiVlRId2hyTmJIeHRfd2NwUHI5RWtRaXk3MUZqUEJVc3EwN2lqaUhsQUhVS3NORkxnWFdMSHFzTlVxbGV0Vk85RUxqNXF6akQyZkFsMVZfR1VKdmU3NnBuc193Qlk4bklqN2RJcEVILVpnX2w0d21YTQ?oc=5>

### 41,197 Enbridge Inc $ENB Shares Bought by Oppenheimer & Co. Inc.
- Summary: Oppenheimer purchased 41,197 Enbridge shares, reflecting institutional interest.
- Date: 2026-10-27 | Impact: low | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxPd21wZG5lRWlFUmZ4TXpHYnMxNkplYTlrVkhwX1RLVmlKVmt0MEE4VG5uSFM4UnV6eXJJTERwWHoxTk5NcC1uYzd4b19vWURjSk44eGk1ZDl1MFFHRmtrT3RhMV9rWFpOeVZWcEJNVFJESUdhemxLLS1wcnppY0E3d0I4OTdWM0pLdGNFaEU2ejN3R0tRV0ZpQ2xGM25aejRSZVZhNEgyb0diMjhsallKbUdiVTZhZk5ERXBV?oc=5>

### 24,314 Enbridge Inc $ENB Shares Bought by Tectonic Advisors LLC
- Summary: Shares of ENB were purchased by Tectonic Advisors LLC, indicating investor activity but no direct company action.
- Date: 2026-10-24 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxNdjh2azJVREhUcThocHVEejMxaENic2xYb1ZPc2w5c0liZmFiWko4bXVtQUpHQks5U3dCRVNBT0ZYb3F1TVdIaC14SURPLW5wY25uaC1UM29VWm9PNENtaHZQRHNxcWFKanBZZTM5dTUtS19Damxyb043OWdwMGlSdUFRTU9NcDUwR0NFRGxFZER0bmFhak1mM21OMmk5dTZVUXJDRWtIdF9vWEJHcXhYR3hEcWpUeTQ5WjBBZXo4TQ?oc=5>

## RISKS

### Enbridge: Risks Lurking Beneath Its 5.8% Dividend Yield (NYSE:ENB)
- Summary: Potential risks associated with maintaining a 5.8% dividend yield may affect future payouts.
- Date: 2026-10-22 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPZTdFcllrMDZkTy1WN29DMGdhbjZKcWJaSXUxS0VGdFc2aUUydDBxZzNuaVFrQzZQRkdLeTFIZEZMbVdHakRzWWhidHNieGcwaHdxOV9JYTlOUkVRZTNOSks4eVhmRXBkVE9FVGw5QkxqMlBHOC1FejhKTXBxdlhlVnFIQS1lUHJ5TmpVdUp4el9jTU9DNV9xTmdYTlU0enRCT0ZMUw?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ENB** | **26.35** | **2.58** | **13.12** | **97.10** | **109,815,119,872.00 USD** | **9.84** |
| TRP.TO | 25.66 | 3.68 | 16.43 | 5.70 | 93,821,526,016.00 CAD | 33.53 |
| KMI | 20.97 | 2.40 | 14.24 | 9.30 | 75,675,492,352.00 USD | 36.43 |
| EPD | 13.56 | 2.84 | 11.56 | 60.80 | 84,327,587,840.00 USD | 33.61 |

Peers fetched as_of: 2026-10-29; ENB reuses existing data (market data as_of: 2026-10-29); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-07-31
- Next expected earnings: 2026-11-06 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-29

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-07-31
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: https://www.sec.gov/Archives/edgar/data/895728/000119312526326752/enb-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimwFBVV95cUxOcGlxcW90c0V2WGtiQlRjUll0RVdfQ1JNbkY0V3oxZjFWS1BTRWtJb0tCUnZkOWVndG91ZC1ISi10VkotVkw1dUxkNXJ4N2xoSS1LcE9YOExNakNJSkFLVkpiczRScUJOeUwxYnlSRmVNZUtMYzJTQjQ1SVVBTzVlcHdyNktIR0lVMTM1Y1FIY0ZrVHNfd0F0T2hndw?oc=5
- https://news.google.com/rss/articles/CBMi-wFBVV95cUxOR3dDYnVSQmpybU5nYXlpNjBLQThBMW5RNXBlTzk1V2ttbnhPMFNHdXJxUUlTS3YzTVlPTFdfT1d5MU1rMkp0czJyTXgteU9GaFNra3VzTXhBdk1QaUhIWVJJZzFzdGFTSTlBdW9jMUF5SDBSY3pQamJmQXlaOWVic2ZIQTJSWkZqSW5STFF6RnVNOXhVZ25fWmFlb1dkT29vTjRlRThGOUZ2cEpMOVQwNDdjT0w3MlNaQlNMN0IyS2RNWE9tcE5GOERKMFl0Y0tpNnpDX0Jkcmoyd0lDR3ZSYlJ0elRhWFdQLXNHS2c2STVyZWV2U0IweUxEaw?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxPQzBzUFVBMHNRb2Y1YS1OYktvekxLUWxKc0VJbzRKdDFrdG5EdklBVnVaRFdXeGctLUZsNzJud2pMMjh2T01IZE5xX1Q5QlJFcWR1Q1lHTjZrM0NCVWQwZy1MSTRua1dpNnVDTHctYnVqWjRyaHVVRzRRbFVjbnZTNGM5bTdSM0Z6Skd0STVlNA?oc=5
- https://news.google.com/rss/articles/CBMigwFBVV95cUxNZ3VuR2ZHZlZjWFBiVlRId2hyTmJIeHRfd2NwUHI5RWtRaXk3MUZqUEJVc3EwN2lqaUhsQUhVS3NORkxnWFdMSHFzTlVxbGV0Vk85RUxqNXF6akQyZkFsMVZfR1VKdmU3NnBuc193Qlk4bklqN2RJcEVILVpnX2w0d21YTQ?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxPd21wZG5lRWlFUmZ4TXpHYnMxNkplYTlrVkhwX1RLVmlKVmt0MEE4VG5uSFM4UnV6eXJJTERwWHoxTk5NcC1uYzd4b19vWURjSk44eGk1ZDl1MFFHRmtrT3RhMV9rWFpOeVZWcEJNVFJESUdhemxLLS1wcnppY0E3d0I4OTdWM0pLdGNFaEU2ejN3R0tRV0ZpQ2xGM25aejRSZVZhNEgyb0diMjhsallKbUdiVTZhZk5ERXBV?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxNdjh2azJVREhUcThocHVEejMxaENic2xYb1ZPc2w5c0liZmFiWko4bXVtQUpHQks5U3dCRVNBT0ZYb3F1TVdIaC14SURPLW5wY25uaC1UM29VWm9PNENtaHZQRHNxcWFKanBZZTM5dTUtS19Damxyb043OWdwMGlSdUFRTU9NcDUwR0NFRGxFZER0bmFhak1mM21OMmk5dTZVUXJDRWtIdF9vWEJHcXhYR3hEcWpUeTQ5WjBBZXo4TQ?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPZTdFcllrMDZkTy1WN29DMGdhbjZKcWJaSXUxS0VGdFc2aUUydDBxZzNuaVFrQzZQRkdLeTFIZEZMbVdHakRzWWhidHNieGcwaHdxOV9JYTlOUkVRZTNOSks4eVhmRXBkVE9FVGw5QkxqMlBHOC1FejhKTXBxdlhlVnFIQS1lUHJ5TmpVdUp4el9jTU9DNV9xTmdYTlU0enRCT0ZMUw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
