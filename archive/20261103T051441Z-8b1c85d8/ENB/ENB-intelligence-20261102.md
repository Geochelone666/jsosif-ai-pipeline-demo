# ENB Intelligence Report

- ticker: **ENB**
- Report as_of: **2026-11-02**
- Market data as_of: **2026-11-02**
- Quant sources: https://finance.yahoo.com/quote/ENB/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ENB/key-statistics/
- AI analysis snapshot as_of: **2026-11-02**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-03T05:38:20.056407+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 13, 'rule': 6, 'ai': 6, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261102T041627Z-c84a7052/ENB** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 13 unique headlines; 4 named publishers; 0 exact duplicates; 13 HTTPS source links; largest publisher share 38.46%; oldest publication 2026-10-27

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 49.2000 |
| Return 1D (%) | -0.5257 |
| Return 1W (%) | 1.9478 |
| Return 1M (%) | 7.0263 |
| Return YTD (%) | 7.0217 |
| Return 1Y (%) | 9.7994 |
| Annualized volatility (%) | 18.1209 |
| Beta vs SPY | -0.1666 |
| Max drawdown (%) | -19.8462 |
| Sharpe (rf=0) | 0.6104 |
| Downside deviation (rf=0, %) | 12.5987 |
| Sortino (rf=0) | 0.8779 |
| Historical VaR 95% (1D, %) | 1.7456 |
| Historical ES 95% (1D, %) | 2.4474 |
| Correlation vs SPY | -0.1179 |
| Tracking error vs SPY (%) | 23.3994 |
| P/E (trailing) | 26.31 |
| P/B | 2.58 |
| EV/EBITDA | 13.11 |
| Revenue growth (%) | 97.10 |
| Forward P/E (estimate) | 21.73 |
| Gross margin (%) | 32.59 |
| Operating margin (%) | 10.16 |
| Return on equity (%) | 9.22 |
| Free cash flow yield (%) | N/A |
| MA50 | 48.2500 |
| Close vs MA50 (%) | 1.9689 |
| MA200 | 51.3816 |
| Close vs MA200 (%) | -4.2459 |
| RSI (14, Wilder) | 61.3300 |
| MACD (12,26) | 0.3244 |
| MACD signal (9) | 0.0312 |
| MACD histogram | 0.2931 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ENB': 273, 'SPY': 273}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 49.2000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.5257 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.9478 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 7.0263 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 7.0217 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 9.7994 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 18.1209 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 12.5987 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.8779 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.7456 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.4474 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1179 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.3994 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1666 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -19.8462 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.6104 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 21.7306 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 32.5940 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 10.1610 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.2210 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 26.3102 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 61.3300 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.2931 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 1.9689 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -4.2459 -> Slightly below the moving-average trend level.

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

### Enbridge Prepares to Report Q3 Earnings: What's in the Cards?
- Summary: Enbridge Prepares to Report Q3 Earnings: What's in the Cards?
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxOUC11RTN2Y0RWTGVrOUhHLVFjallHY3Z3eXo2TnhCcnFNa0Mwdy1STjJvX3R3cm5vaFpmaGtnODFwaGlOc3BvYnFaN0tGbHhTNEhWNEtJSlI3VGhGSnFmVExESURZd1dCQUhJcG1WVDRSTTF3TUlHaTZxR0NsZHB2M0hpZktteEZMNjI4SG9IYm04eF9FYVEtZUgtRWdRZ0NrMFZJ?oc=5>

### Enbridge (ENB) Reports Next Week: Wall Street Expects Earnings Growth
- Summary: Enbridge (ENB) Reports Next Week: Wall Street Expects Earnings Growth
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNZWplM2psMXRxeTc3UU95XzJjSWpoYkVzSkowM2E0d0RLRkx2T1gtemNjZlhtYlZrOTFGTnQ5aERwUTdaNDByU19jaGM0bXVGVEItcWxMV1hTbDF1eVRQN3lza2dGTk81QWpyOHN2a0dVXy1jOV9lSTRSa1M2b0NuQXdMbjRjNGJpcGVtT1FCZnJmRVA2ektWdnBQcw?oc=5>

### Enbridge Inc $ENB Shares Acquired by Hennessy Advisors Inc.
- Summary: Enbridge Inc $ENB Shares Acquired by Hennessy Advisors Inc.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxNYklhQ3AwbEtRUW4yaXpJZUdBdi1zN2NyQ2RLNTJxRDF4Y2RsWHhEeEVvaEVPM0hZcGM4RzJiLWp4dmNjd1k1WEV3SDI4aHc3aEhwMGZZQ0huS3hXYXhLX1RJb3FMSHQ4UmxFcTlNSUdMd3dUeU9XWVpDbEZlN2FxdjBlNHR2RFotT0MweFFDZDFaaUlqYjlGN2VSNGhGVFVyLS1JTWw1UG03bW1BME8tRUhscjZyekZxWGc?oc=5>

### Enbridge Inc $ENB Shares Bought by International Assets Investment Management LLC
- Summary: Enbridge Inc $ENB Shares Bought by International Assets Investment Management LLC
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxQWVlhLU03aTRhb0RyLW8xeTZIZDl4Y1Iwdk5vOW55R1lZRmJXeGxITkZiaXJOeHBlanpwcEg5YUZMdEpSbnJPSGNubGZFNlFRYnJULTdXU0QzSGlTOEZKdEhWQUxvVGlaVnk2ckhnSEVQQkhlVnZQak84SDFYN3FoV3pjYW10cHJ5eHZBa09wRzdCR0t0UFlRNWdZNlF0Q1lqNTBrSm9nZFNZRTM1WU81ejhfb01YV2JrQ2dVVTU0dTVNbDJlaVJHQTlZT2FFZ1libHAzMmo1a04?oc=5>

### Enbridge Inc (NYSE:ENB) Stock Now Rated "Moderate Buy" by Sell-Side Analysts
- Summary: Enbridge Inc (NYSE:ENB) Stock Now Rated "Moderate Buy" by Sell-Side Analysts
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxOSzlZRC1TNWxkZFlDUFJyS01OV3ZwWTV4aE9ZWXhYbVpOSTJLNFJ6VHNCNHhMd1N0X3FLYTVuOW1mNnoxVkZzQk9NTVU3T3Z0dkk1ZDFtd09xUndPOWZHQXRUWTV1Y1ljQ0w0emZMQjBKaF9Zb253VE04V2lUUjF1SFk4dlZ3anFneHlWRXkwbU8xZExSaGR4UEpXMEVPODFTNURmNVNxeWpjZzl2N29abnZsR3JEbWMyZzlhZHFHUWNOZG1FSWxabnlHbXY0czJ6TGc?oc=5>

### Enbridge (ENB) Expected to Post Earnings on Friday
- Summary: Enbridge is expected to release earnings on Friday.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxOYlBMQ3FnU2xRSVlaaDY2UWctSlVGOWtVNHM2OVZWWktTbjluaWNSLU92UDRZQUlzcUpINk9BN1lGdFdvb0JjSkc0R1daSnZGXzNvMzltRlVpQnNLYTByUm5zSy14ZHNsOG4wcTdVN3hGUk1CZDY0S01XTzZ3dVlWS3R0eTZETkVaQXlBYlJTR1AtNVotMXNnemI5cXRPdzlFLTBiTDlPTFMweFdUb29STg?oc=5>

### Enbridge (TSX:ENB) Stock May Trade At A Premium Despite Gas Demand Growth News
- Summary: Enbridge shares could trade above current levels amid rising gas demand.
- Date: 2026-10-30 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQUzQ5UTdWTDhnMFMtejhlNWh1czBNb3l0ZmpxcDBodnBWUGhlcUR3TkJDdHkwUHVSckJtZlZHcEYwcHctbjMwUDQwTEVqWHNpWllua2ZKX2F0c3pjcEpHOTNnWmhwdHp0SGdzNnNld2E4YjZUXzFLdjM3UnhNYkxvNGtaQkJ3U1B0SXFEMXl4Mmw3YjVDX2c?oc=5>

### Enbridge vs. Enterprise Products: Which High-Yield Dividend Is Actually Safer?
- Summary: Comparison of dividend safety between Enbridge and Enterprise Products.
- Date: 2026-10-31 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQSEltU05oZUFIOEl4dVIwQ0hnQUNoN1c2TEVmZmJoaHFKSFpfblppVUwyMWx5SXZlZnZzOEl3eXYtMkowaVVxZU5ldGZaNklfeUdZcGd4UmdSZFVvNW9IekMwaE1xemVMSGV3OTg0M2o3eWQtZWVXR3A2cGktREhsWE1HM1NGNHNhTkJRTXZtU0tGZzZFN1dpRg?oc=5>

### Investors Heavily Search Enbridge Inc (ENB): Here is What You Need to Know
- Summary: High search volume indicates growing investor interest in Enbridge.
- Date: 2026-10-28 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPSExrOHBjUUZYeUZuel9VenpGZWhEdWlheE00X1BqUF9qLWFVdEtBZGVFT0FKcUVtQkNySFNWbTYxRHFiZXVEODY4cUg2bnpoa0EyWENQMFlSVFYwNEQ0cmJLZ0h6UDUyUUI3T2s5N2pjbVJCU29HS3BfSTk4WUo1cUE0T3NHWE1zZDA4MGdhRkd2UFRRc2psZlQ4blNBYWdadW8zSQ?oc=5>

### Is Enbridge Stock Still a Buy for Retirees Seeking Passive Income?
- Summary: Assessment of Enbridge as a retirement income investment.
- Date: 2026-10-30 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxPVWdBbVFXcWF1b2Z5QUpWMllWMzdJbWF0QU1TQ3FucmxWVUpaaS1GRmJxMWxQa0duZlQ3eVdSOHVTWnNEV2RwUmZLTmtsZXgzSHZDNGpod0oxZldyeGx5Tkt4ei1DYjJnRDVIbnZ4eW9nN2Q0VVZTNGNvdmNIZmg5Ym9sTEJNbG1BNUE?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ENB** | **26.31** | **2.58** | **13.11** | **97.10** | **109,659,103,232.00 USD** | **9.80** |
| TRP.TO | 25.37 | 3.64 | 16.33 | 5.70 | 92,769,345,536.00 CAD | 31.80 |
| KMI | 20.97 | 2.31 | 13.88 | 9.30 | 72,868,569,088.00 USD | 31.07 |
| EPD | 12.33 | 2.67 | 10.81 | 49.30 | 80,699,662,336.00 USD | 28.85 |

Peers fetched as_of: 2026-11-02; ENB reuses existing data (market data as_of: 2026-11-02); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-07-31
- Next expected earnings: 2026-11-06 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-02

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
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
- https://news.google.com/rss/articles/CBMiowFBVV95cUxOUC11RTN2Y0RWTGVrOUhHLVFjallHY3Z3eXo2TnhCcnFNa0Mwdy1STjJvX3R3cm5vaFpmaGtnODFwaGlOc3BvYnFaN0tGbHhTNEhWNEtJSlI3VGhGSnFmVExESURZd1dCQUhJcG1WVDRSTTF3TUlHaTZxR0NsZHB2M0hpZktteEZMNjI4SG9IYm04eF9FYVEtZUgtRWdRZ0NrMFZJ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNZWplM2psMXRxeTc3UU95XzJjSWpoYkVzSkowM2E0d0RLRkx2T1gtemNjZlhtYlZrOTFGTnQ5aERwUTdaNDByU19jaGM0bXVGVEItcWxMV1hTbDF1eVRQN3lza2dGTk81QWpyOHN2a0dVXy1jOV9lSTRSa1M2b0NuQXdMbjRjNGJpcGVtT1FCZnJmRVA2ektWdnBQcw?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxNYklhQ3AwbEtRUW4yaXpJZUdBdi1zN2NyQ2RLNTJxRDF4Y2RsWHhEeEVvaEVPM0hZcGM4RzJiLWp4dmNjd1k1WEV3SDI4aHc3aEhwMGZZQ0huS3hXYXhLX1RJb3FMSHQ4UmxFcTlNSUdMd3dUeU9XWVpDbEZlN2FxdjBlNHR2RFotT0MweFFDZDFaaUlqYjlGN2VSNGhGVFVyLS1JTWw1UG03bW1BME8tRUhscjZyekZxWGc?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxQWVlhLU03aTRhb0RyLW8xeTZIZDl4Y1Iwdk5vOW55R1lZRmJXeGxITkZiaXJOeHBlanpwcEg5YUZMdEpSbnJPSGNubGZFNlFRYnJULTdXU0QzSGlTOEZKdEhWQUxvVGlaVnk2ckhnSEVQQkhlVnZQak84SDFYN3FoV3pjYW10cHJ5eHZBa09wRzdCR0t0UFlRNWdZNlF0Q1lqNTBrSm9nZFNZRTM1WU81ejhfb01YV2JrQ2dVVTU0dTVNbDJlaVJHQTlZT2FFZ1libHAzMmo1a04?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxOSzlZRC1TNWxkZFlDUFJyS01OV3ZwWTV4aE9ZWXhYbVpOSTJLNFJ6VHNCNHhMd1N0X3FLYTVuOW1mNnoxVkZzQk9NTVU3T3Z0dkk1ZDFtd09xUndPOWZHQXRUWTV1Y1ljQ0w0emZMQjBKaF9Zb253VE04V2lUUjF1SFk4dlZ3anFneHlWRXkwbU8xZExSaGR4UEpXMEVPODFTNURmNVNxeWpjZzl2N29abnZsR3JEbWMyZzlhZHFHUWNOZG1FSWxabnlHbXY0czJ6TGc?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxOYlBMQ3FnU2xRSVlaaDY2UWctSlVGOWtVNHM2OVZWWktTbjluaWNSLU92UDRZQUlzcUpINk9BN1lGdFdvb0JjSkc0R1daSnZGXzNvMzltRlVpQnNLYTByUm5zSy14ZHNsOG4wcTdVN3hGUk1CZDY0S01XTzZ3dVlWS3R0eTZETkVaQXlBYlJTR1AtNVotMXNnemI5cXRPdzlFLTBiTDlPTFMweFdUb29STg?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQUzQ5UTdWTDhnMFMtejhlNWh1czBNb3l0ZmpxcDBodnBWUGhlcUR3TkJDdHkwUHVSckJtZlZHcEYwcHctbjMwUDQwTEVqWHNpWllua2ZKX2F0c3pjcEpHOTNnWmhwdHp0SGdzNnNld2E4YjZUXzFLdjM3UnhNYkxvNGtaQkJ3U1B0SXFEMXl4Mmw3YjVDX2c?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQSEltU05oZUFIOEl4dVIwQ0hnQUNoN1c2TEVmZmJoaHFKSFpfblppVUwyMWx5SXZlZnZzOEl3eXYtMkowaVVxZU5ldGZaNklfeUdZcGd4UmdSZFVvNW9IekMwaE1xemVMSGV3OTg0M2o3eWQtZWVXR3A2cGktREhsWE1HM1NGNHNhTkJRTXZtU0tGZzZFN1dpRg?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPSExrOHBjUUZYeUZuel9VenpGZWhEdWlheE00X1BqUF9qLWFVdEtBZGVFT0FKcUVtQkNySFNWbTYxRHFiZXVEODY4cUg2bnpoa0EyWENQMFlSVFYwNEQ0cmJLZ0h6UDUyUUI3T2s5N2pjbVJCU29HS3BfSTk4WUo1cUE0T3NHWE1zZDA4MGdhRkd2UFRRc2psZlQ4blNBYWdadW8zSQ?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxPVWdBbVFXcWF1b2Z5QUpWMllWMzdJbWF0QU1TQ3FucmxWVUpaaS1GRmJxMWxQa0duZlQ3eVdSOHVTWnNEV2RwUmZLTmtsZXgzSHZDNGpod0oxZldyeGx5Tkt4ei1DYjJnRDVIbnZ4eW9nN2Q0VVZTNGNvdmNIZmg5Ym9sTEJNbG1BNUE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
