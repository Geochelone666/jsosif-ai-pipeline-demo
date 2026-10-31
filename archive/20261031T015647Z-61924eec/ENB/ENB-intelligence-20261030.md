# ENB Intelligence Report

- ticker: **ENB**
- Report as_of: **2026-10-30**
- Market data as_of: **2026-10-30**
- Quant sources: https://finance.yahoo.com/quote/ENB/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ENB/key-statistics/
- AI analysis snapshot as_of: **2026-10-30**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-31T02:18:20.245313+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 7, 'rule': 2, 'ai': 2, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261030T021807Z-b9de7146/ENB** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 7 unique headlines; 4 named publishers; 0 exact duplicates; 7 HTTPS source links; largest publisher share 28.57%; oldest publication 2026-10-27

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 49.4600 |
| Return 1D (%) | 0.3856 |
| Return 1W (%) | 2.7207 |
| Return 1M (%) | 6.3885 |
| Return YTD (%) | 7.5872 |
| Return 1Y (%) | 9.5338 |
| Annualized volatility (%) | 18.0939 |
| Beta vs SPY | -0.1700 |
| Max drawdown (%) | -19.8462 |
| Sharpe (rf=0) | 0.5955 |
| Downside deviation (rf=0, %) | 12.5860 |
| Sortino (rf=0) | 0.8561 |
| Historical VaR 95% (1D, %) | 1.7452 |
| Historical ES 95% (1D, %) | 2.4474 |
| Correlation vs SPY | -0.1202 |
| Tracking error vs SPY (%) | 23.3788 |
| P/E (trailing) | 26.45 |
| P/B | 2.59 |
| EV/EBITDA | 13.14 |
| Revenue growth (%) | 97.10 |
| Forward P/E (estimate) | 21.85 |
| Gross margin (%) | 32.59 |
| Operating margin (%) | 10.16 |
| Return on equity (%) | 9.22 |
| Free cash flow yield (%) | N/A |
| MA50 | 48.2752 |
| Close vs MA50 (%) | 2.4543 |
| MA200 | 51.3606 |
| Close vs MA200 (%) | -3.7004 |
| RSI (14, Wilder) | 64.6376 |
| MACD (12,26) | 0.2739 |
| MACD signal (9) | -0.0421 |
| MACD histogram | 0.3159 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ENB': 272, 'SPY': 272}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 49.4600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.3856 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.7207 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 6.3885 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 7.5872 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 9.5338 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 18.0939 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 12.5860 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.8561 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.7452 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.4474 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1202 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.3788 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1700 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -19.8462 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.5955 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 21.8454 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 32.5940 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 10.1610 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.2210 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 26.4492 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 64.6376 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.3159 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 2.4543 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -3.7004 -> Slightly below the moving-average trend level.

## TAILWINDS

### Enbridge (ENB) Gains As Market Dips: What You Should Know
- Summary: Enbridge shares rise amid broader market decline, reflecting investor confidence in the company.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOcGlxcW90c0V2WGtiQlRjUll0RVdfQ1JNbkY0V3oxZjFWS1BTRWtJb0tCUnZkOWVndG91ZC1ISi10VkotVkw1dUxkNXJ4N2xoSS1LcE9YOExNakNJSkFLVkpiczRScUJOeUwxYnlSRmVNZUtMYzJTQjQ1SVVBTzVlcHdyNktIR0lVMTM1Y1FIY0ZrVHNfd0F0T2hndw?oc=5>

## HEADWINDS

### Enbridge Stock is Down 16%, but the Business Looks Smart: Here’s How I’d Buy the Stock
- Summary: Enbridge Stock is Down 16%, but the Business Looks Smart: Here’s How I’d Buy the Stock
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxOaTZzN083OGdvX3dMa1owN1c3cmwyWkVORU5UbUw5ZUZRV1dYWFVkVGNidDFPaDVlNEFjWUk2WER5eVd1Nm1Gb0h5YzZLd21xQzlfNU9jRmVqNFBqSGRrMHVRX1RieThqWVU1S0RneGgwOS0yQmlFT096d3NnbEw0LVBuQlRxRFU?oc=5>

## CATALYSTS

### Enbridge (ENB) Reports Next Week: Wall Street Expects Earnings Growth
- Summary: Enbridge (ENB) Reports Next Week: Wall Street Expects Earnings Growth
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNZWplM2psMXRxeTc3UU95XzJjSWpoYkVzSkowM2E0d0RLRkx2T1gtemNjZlhtYlZrOTFGTnQ5aERwUTdaNDByU19jaGM0bXVGVEItcWxMV1hTbDF1eVRQN3lza2dGTk81QWpyOHN2a0dVXy1jOV9lSTRSa1M2b0NuQXdMbjRjNGJpcGVtT1FCZnJmRVA2ektWdnBQcw?oc=5>

### Enbridge (ENB) Expected to Post Earnings on Friday
- Summary: Enbridge is expected to release earnings on Friday.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxOYlBMQ3FnU2xRSVlaaDY2UWctSlVGOWtVNHM2OVZWWktTbjluaWNSLU92UDRZQUlzcUpINk9BN1lGdFdvb0JjSkc0R1daSnZGXzNvMzltRlVpQnNLYTByUm5zSy14ZHNsOG4wcTdVN3hGUk1CZDY0S01XTzZ3dVlWS3R0eTZETkVaQXlBYlJTR1AtNVotMXNnemI5cXRPdzlFLTBiTDlPTFMweFdUb29STg?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ENB** | **26.45** | **2.59** | **13.14** | **97.10** | **110,238,597,120.00 USD** | **9.53** |
| TRP.TO | 25.69 | 3.68 | 16.45 | 5.70 | 93,925,711,872.00 CAD | 32.99 |
| KMI | 20.91 | 2.39 | 14.21 | 9.30 | 75,452,719,104.00 USD | 35.09 |
| EPD | 13.25 | 2.77 | N/A | 49.30 | 82,384,060,416.00 USD | 30.50 |

Peers fetched as_of: 2026-10-30; ENB reuses existing data (market data as_of: 2026-10-30); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-07-31
- Next expected earnings: 2026-11-06 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-30

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
- https://news.google.com/rss/articles/CBMihwFBVV95cUxOaTZzN083OGdvX3dMa1owN1c3cmwyWkVORU5UbUw5ZUZRV1dYWFVkVGNidDFPaDVlNEFjWUk2WER5eVd1Nm1Gb0h5YzZLd21xQzlfNU9jRmVqNFBqSGRrMHVRX1RieThqWVU1S0RneGgwOS0yQmlFT096d3NnbEw0LVBuQlRxRFU?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNZWplM2psMXRxeTc3UU95XzJjSWpoYkVzSkowM2E0d0RLRkx2T1gtemNjZlhtYlZrOTFGTnQ5aERwUTdaNDByU19jaGM0bXVGVEItcWxMV1hTbDF1eVRQN3lza2dGTk81QWpyOHN2a0dVXy1jOV9lSTRSa1M2b0NuQXdMbjRjNGJpcGVtT1FCZnJmRVA2ektWdnBQcw?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxOYlBMQ3FnU2xRSVlaaDY2UWctSlVGOWtVNHM2OVZWWktTbjluaWNSLU92UDRZQUlzcUpINk9BN1lGdFdvb0JjSkc0R1daSnZGXzNvMzltRlVpQnNLYTByUm5zSy14ZHNsOG4wcTdVN3hGUk1CZDY0S01XTzZ3dVlWS3R0eTZETkVaQXlBYlJTR1AtNVotMXNnemI5cXRPdzlFLTBiTDlPTFMweFdUb29STg?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
