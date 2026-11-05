# ENB Intelligence Report

- ticker: **ENB**
- Report as_of: **2026-11-04**
- Market data as_of: **2026-11-04**
- Quant sources: https://finance.yahoo.com/quote/ENB/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ENB/key-statistics/
- AI analysis snapshot as_of: **2026-11-04**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-05T05:08:12.630958+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 15, 'rule': 8, 'ai': 7, 'unknown': 0})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261104T044411Z-6b13f9ec/ENB** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 15 unique headlines; 6 named publishers; 0 exact duplicates; 15 HTTPS source links; largest publisher share 26.67%; oldest publication 2026-10-29

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 48.7800 |
| Return 1D (%) | -0.3269 |
| Return 1W (%) | 0.4737 |
| Return 1M (%) | 6.1127 |
| Return YTD (%) | 6.1081 |
| Return 1Y (%) | 9.4018 |
| Annualized volatility (%) | 18.0895 |
| Beta vs SPY | -0.1740 |
| Max drawdown (%) | -19.8462 |
| Sharpe (rf=0) | 0.5889 |
| Downside deviation (rf=0, %) | 12.5793 |
| Sortino (rf=0) | 0.8469 |
| Historical VaR 95% (1D, %) | 1.7452 |
| Historical ES 95% (1D, %) | 2.4474 |
| Correlation vs SPY | -0.1235 |
| Tracking error vs SPY (%) | 23.4400 |
| P/E (trailing) | 26.09 |
| P/B | 2.56 |
| EV/EBITDA | 13.06 |
| Revenue growth (%) | 97.10 |
| Forward P/E (estimate) | 21.55 |
| Gross margin (%) | 32.59 |
| Operating margin (%) | 10.16 |
| Return on equity (%) | 9.22 |
| Free cash flow yield (%) | N/A |
| MA50 | 48.2080 |
| Close vs MA50 (%) | 1.1865 |
| MA200 | 51.4150 |
| Close vs MA200 (%) | -5.1250 |
| RSI (14, Wilder) | 56.1821 |
| MACD (12,26) | 0.3346 |
| MACD signal (9) | 0.1412 |
| MACD histogram | 0.1934 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ENB': 275, 'SPY': 275}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 48.7800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.3269 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.4737 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 6.1127 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 6.1081 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 9.4018 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 18.0895 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 12.5793 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.8469 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.7452 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.4474 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1235 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.4400 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1740 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -19.8462 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.5889 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 21.5451 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 32.5940 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 10.1610 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.2210 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 26.0856 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 56.1821 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.1934 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 1.1865 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -5.1250 -> Clearly below the moving-average trend level.

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

### Enbridge Inc. Declares Quarterly Dividends
- Summary: Enbridge Inc. Declares Quarterly Dividends
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPZ2V5RGJpRmoxNTd2amQ5MlhlX0txaXI3OXcxQ0YtSlBuNVp3dC0xZ1hTdUd5Sk9nVDh2UzZRWUZQQ1JlT2hqY1RnZFZqOXprUlFlcVhSTDhlNGFHcFZaY3h1cE5SOXRuZG03bExsaVB6U0xTNDVoV2hjYnk2VzRaSzBsT1NWUUx5X1RITE1TNW4ydnlwSkRmQXlKcWNaRHpCcXFuRDY3WmNGUQ?oc=5>

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

### Enbridge stock keeps CAD 0.9700 dividend ahead of Q3 update
- Summary: Enbridge stock keeps CAD 0.9700 dividend ahead of Q3 update
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxQakd1SzZudTBpOHI1SVF4cE15ZkZsODBQQnFzV0kzWTlUVlFGeWktYWhCRl9vMUxXREhDMjhVdU14UllFTXV1LXR2VUtON1NDY1RRSEp2QzB5emgtWXhLaDVNak5NVzJtQ0Q1S3VZSFhNamxwM09ZZVlLVzFhVXNIR1I0ZGNNR1lxRHF4M29sbm9TZUdmV0N4dHk0WUJ3NGhKZFo4OXlNWmFYSnpxQ3R3YVZYSGpxS0s5Q091ZDdFNA?oc=5>

### Enbridge Maintains Quarterly Common-Share Dividend at $0.9700
- Summary: Enbridge Maintains Quarterly Common-Share Dividend at $0.9700
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxQSFNwejJOS3lkai1rSXBIanV1UnVscWRRUjAydUJ2eEZLR1ZDbXg4ZV9MNGFJVmw0V1RJZEE0Yk1feXRFUks5eEVEcnlEclo4Q192Z0VNVFFJRjVGZ2o1aW5yOWxFVEIxLUhyc0pqa2VJSFlYd242bEg2QnBzOE5uX1ExWXZoOWwwTzJWSEYzU2R1S2hFVXJIeFFrcXlBODI0YVY4TkZCRmZZa2VodWFhTm93?oc=5>

### Is Enbridge Stock Still a Buy for Retirees Seeking Passive Income?
- Summary: Assessment of Enbridge as a retirement income investment.
- Date: 2026-10-30 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxPVWdBbVFXcWF1b2Z5QUpWMllWMzdJbWF0QU1TQ3FucmxWVUpaaS1GRmJxMWxQa0duZlQ3eVdSOHVTWnNEV2RwUmZLTmtsZXgzSHZDNGpod0oxZldyeGx5Tkt4ei1DYjJnRDVIbnZ4eW9nN2Q0VVZTNGNvdmNIZmg5Ym9sTEJNbG1BNUE?oc=5>

### Enbridge (ENB) Expected to Post Earnings on Friday
- Summary: Enbridge is expected to release earnings on Friday.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxOYlBMQ3FnU2xRSVlaaDY2UWctSlVGOWtVNHM2OVZWWktTbjluaWNSLU92UDRZQUlzcUpINk9BN1lGdFdvb0JjSkc0R1daSnZGXzNvMzltRlVpQnNLYTByUm5zSy14ZHNsOG4wcTdVN3hGUk1CZDY0S01XTzZ3dVlWS3R0eTZETkVaQXlBYlJTR1AtNVotMXNnemI5cXRPdzlFLTBiTDlPTFMweFdUb29STg?oc=5>

### Stocks in play: Enbridge Inc.
- Summary: Enbridge shares are currently active in the market, indicating investor interest.
- Date: 2026-11-04 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTFBXZ01jUDVRSnF5TnZPVjdnNHhNQU5TamZqUTB1TGVhcGpRVldkSFNuV2ZjUkFGM2RTUXZRNkV2cXk0TklMVDFWOEV2eDJISWx1QTBNSXJHXzR1dnEybEh2NWJ3eEwyOVBwczEyb29Fa21XM2twYkpyNkIzSG9RUQ?oc=5>

### Enbridge Inc $ENB Stock Position Cut by ProShare Advisors LLC
- Summary: ProShare Advisors reduced its holdings in Enbridge, signaling a potential shift in institutional confidence.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxPZ09zNWFxNENLbmJGREs2WDhZbXBIRUYySVppTFZpWmtNMHhBdmFVbGpMUjNpNExmakNlbFFpLVpGbWVLVVk4bnJjbi1vYzlFQkYyWmlwVkVGdW9iNlJjTWVoUXhFOUg3Q1hkZE90T2tYbFp5SFRQYjRSaEZpeWszSGZ2SHRTQTdoMWZvR2hkMF9kek02dzFTeHFkYlo4NV9LbWJhWlgwQUZsUnVfdDJTWkZUZFBkVXY1YTlCa3dR?oc=5>

### Enbridge stock draws new institutional buyers: Can ENB maintain momentum?
- Summary: New institutional investors are buying Enbridge shares, raising questions about sustaining growth.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPNkxQQnF0VDAxenBRaTZubGdhTEdyNHlWZWlHM2VJRmJoTUUta3VzaVRBb21OMG9rT3lza0d3bU91akZjUjZwaWJYUHdESlphaVFmY1NCQ2xyX1Z4X09vbldfeEhMMnlGSUtaa01GUzVNcDEydDhnTGNWcjkxWkoxVnNfSTVLZ1ZBT3UzWWdWckw2VHM?oc=5>

### Will Enbridge stock break C$69.46 resistance amid steady buyer support?
- Summary: Investors are monitoring Enbridge's price action near a key resistance level.
- Date: 2026-10-29 | Impact: low | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxQbHJYNWpVUVB3aHFoQ0l4T2lfNWlHRFA3QW1tcU5LSDJCdzVSaERkcXpCSXJsa3dLZU9ZUkJ2aEVNcDFVX1huYkxrTzFfZk9ZaC1BVi1xQ2M3elhacS1xcE5KZThQdUJFQkNSMlJvazRCVzg2OFZDNk1Ld0RMdW9MaXZnQ3JkajlPVURKMHNUbUsySFk?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ENB** | **26.09** | **2.56** | **13.06** | **97.10** | **108,722,987,008.00 USD** | **9.40** |
| TRP.TO | 24.93 | 3.58 | 16.18 | 5.70 | 91,175,436,288.00 CAD | 29.94 |
| KMI | 20.34 | 2.22 | 13.53 | 9.30 | 70,217,588,736.00 USD | 26.58 |
| EPD | 12.36 | 2.62 | 10.68 | 49.30 | 79,274,409,984.00 USD | 28.96 |

Peers fetched as_of: 2026-11-04; ENB reuses existing data (market data as_of: 2026-11-04); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-07-31
- Next expected earnings: 2026-11-06 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-04

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
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPZ2V5RGJpRmoxNTd2amQ5MlhlX0txaXI3OXcxQ0YtSlBuNVp3dC0xZ1hTdUd5Sk9nVDh2UzZRWUZQQ1JlT2hqY1RnZFZqOXprUlFlcVhSTDhlNGFHcFZaY3h1cE5SOXRuZG03bExsaVB6U0xTNDVoV2hjYnk2VzRaSzBsT1NWUUx5X1RITE1TNW4ydnlwSkRmQXlKcWNaRHpCcXFuRDY3WmNGUQ?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxOUC11RTN2Y0RWTGVrOUhHLVFjallHY3Z3eXo2TnhCcnFNa0Mwdy1STjJvX3R3cm5vaFpmaGtnODFwaGlOc3BvYnFaN0tGbHhTNEhWNEtJSlI3VGhGSnFmVExESURZd1dCQUhJcG1WVDRSTTF3TUlHaTZxR0NsZHB2M0hpZktteEZMNjI4SG9IYm04eF9FYVEtZUgtRWdRZ0NrMFZJ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNZWplM2psMXRxeTc3UU95XzJjSWpoYkVzSkowM2E0d0RLRkx2T1gtemNjZlhtYlZrOTFGTnQ5aERwUTdaNDByU19jaGM0bXVGVEItcWxMV1hTbDF1eVRQN3lza2dGTk81QWpyOHN2a0dVXy1jOV9lSTRSa1M2b0NuQXdMbjRjNGJpcGVtT1FCZnJmRVA2ektWdnBQcw?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxNYklhQ3AwbEtRUW4yaXpJZUdBdi1zN2NyQ2RLNTJxRDF4Y2RsWHhEeEVvaEVPM0hZcGM4RzJiLWp4dmNjd1k1WEV3SDI4aHc3aEhwMGZZQ0huS3hXYXhLX1RJb3FMSHQ4UmxFcTlNSUdMd3dUeU9XWVpDbEZlN2FxdjBlNHR2RFotT0MweFFDZDFaaUlqYjlGN2VSNGhGVFVyLS1JTWw1UG03bW1BME8tRUhscjZyekZxWGc?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxQWVlhLU03aTRhb0RyLW8xeTZIZDl4Y1Iwdk5vOW55R1lZRmJXeGxITkZiaXJOeHBlanpwcEg5YUZMdEpSbnJPSGNubGZFNlFRYnJULTdXU0QzSGlTOEZKdEhWQUxvVGlaVnk2ckhnSEVQQkhlVnZQak84SDFYN3FoV3pjYW10cHJ5eHZBa09wRzdCR0t0UFlRNWdZNlF0Q1lqNTBrSm9nZFNZRTM1WU81ejhfb01YV2JrQ2dVVTU0dTVNbDJlaVJHQTlZT2FFZ1libHAzMmo1a04?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxQakd1SzZudTBpOHI1SVF4cE15ZkZsODBQQnFzV0kzWTlUVlFGeWktYWhCRl9vMUxXREhDMjhVdU14UllFTXV1LXR2VUtON1NDY1RRSEp2QzB5emgtWXhLaDVNak5NVzJtQ0Q1S3VZSFhNamxwM09ZZVlLVzFhVXNIR1I0ZGNNR1lxRHF4M29sbm9TZUdmV0N4dHk0WUJ3NGhKZFo4OXlNWmFYSnpxQ3R3YVZYSGpxS0s5Q091ZDdFNA?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxQSFNwejJOS3lkai1rSXBIanV1UnVscWRRUjAydUJ2eEZLR1ZDbXg4ZV9MNGFJVmw0V1RJZEE0Yk1feXRFUks5eEVEcnlEclo4Q192Z0VNVFFJRjVGZ2o1aW5yOWxFVEIxLUhyc0pqa2VJSFlYd242bEg2QnBzOE5uX1ExWXZoOWwwTzJWSEYzU2R1S2hFVXJIeFFrcXlBODI0YVY4TkZCRmZZa2VodWFhTm93?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxPVWdBbVFXcWF1b2Z5QUpWMllWMzdJbWF0QU1TQ3FucmxWVUpaaS1GRmJxMWxQa0duZlQ3eVdSOHVTWnNEV2RwUmZLTmtsZXgzSHZDNGpod0oxZldyeGx5Tkt4ei1DYjJnRDVIbnZ4eW9nN2Q0VVZTNGNvdmNIZmg5Ym9sTEJNbG1BNUE?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxOYlBMQ3FnU2xRSVlaaDY2UWctSlVGOWtVNHM2OVZWWktTbjluaWNSLU92UDRZQUlzcUpINk9BN1lGdFdvb0JjSkc0R1daSnZGXzNvMzltRlVpQnNLYTByUm5zSy14ZHNsOG4wcTdVN3hGUk1CZDY0S01XTzZ3dVlWS3R0eTZETkVaQXlBYlJTR1AtNVotMXNnemI5cXRPdzlFLTBiTDlPTFMweFdUb29STg?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTFBXZ01jUDVRSnF5TnZPVjdnNHhNQU5TamZqUTB1TGVhcGpRVldkSFNuV2ZjUkFGM2RTUXZRNkV2cXk0TklMVDFWOEV2eDJISWx1QTBNSXJHXzR1dnEybEh2NWJ3eEwyOVBwczEyb29Fa21XM2twYkpyNkIzSG9RUQ?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxPZ09zNWFxNENLbmJGREs2WDhZbXBIRUYySVppTFZpWmtNMHhBdmFVbGpMUjNpNExmakNlbFFpLVpGbWVLVVk4bnJjbi1vYzlFQkYyWmlwVkVGdW9iNlJjTWVoUXhFOUg3Q1hkZE90T2tYbFp5SFRQYjRSaEZpeWszSGZ2SHRTQTdoMWZvR2hkMF9kek02dzFTeHFkYlo4NV9LbWJhWlgwQUZsUnVfdDJTWkZUZFBkVXY1YTlCa3dR?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPNkxQQnF0VDAxenBRaTZubGdhTEdyNHlWZWlHM2VJRmJoTUUta3VzaVRBb21OMG9rT3lza0d3bU91akZjUjZwaWJYUHdESlphaVFmY1NCQ2xyX1Z4X09vbldfeEhMMnlGSUtaa01GUzVNcDEydDhnTGNWcjkxWkoxVnNfSTVLZ1ZBT3UzWWdWckw2VHM?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxQbHJYNWpVUVB3aHFoQ0l4T2lfNWlHRFA3QW1tcU5LSDJCdzVSaERkcXpCSXJsa3dLZU9ZUkJ2aEVNcDFVX1huYkxrTzFfZk9ZaC1BVi1xQ2M3elhacS1xcE5KZThQdUJFQkNSMlJvazRCVzg2OFZDNk1Ld0RMdW9MaXZnQ3JkajlPVURKMHNUbUsySFk?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
