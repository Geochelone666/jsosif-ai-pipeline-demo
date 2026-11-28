# AMD Intelligence Report

- ticker: **AMD**
- Report as_of: **2026-11-27**
- Market data as_of: **2026-11-27**
- Quant sources: https://finance.yahoo.com/quote/AMD/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMD/key-statistics/
- AI analysis snapshot as_of: **2026-11-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-28T06:12:35.096785+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 3, 'ai': 8, 'unknown': 0, 'irrelevant': 14})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261127T063646Z-c0c26981/AMD** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **3**; {'short_term_price_move_in_structural_risks': 3}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 15 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 28.0%; oldest publication 2026-11-24

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 424.5400 |
| Return 1D (%) | 4.5588 |
| Return 1W (%) | 0.0353 |
| Return 1M (%) | -24.2245 |
| Return YTD (%) | 98.2350 |
| Return 1Y (%) | 98.1609 |
| Annualized volatility (%) | 75.5262 |
| Beta vs SPY | 3.2824 |
| Max drawdown (%) | -37.7290 |
| Sharpe (rf=0) | 1.2708 |
| Downside deviation (rf=0, %) | 50.2570 |
| Sortino (rf=0) | 1.9097 |
| Historical VaR 95% (1D, %) | 7.1869 |
| Historical ES 95% (1D, %) | 10.2670 |
| Correlation vs SPY | 0.6529 |
| Tracking error vs SPY (%) | 66.6969 |
| P/E (trailing) | 90.71 |
| P/B | 10.18 |
| EV/EBITDA | 61.90 |
| Revenue growth (%) | 44.70 |
| Forward P/E (estimate) | 24.07 |
| Gross margin (%) | 56.00 |
| Operating margin (%) | 17.82 |
| Return on equity (%) | 11.96 |
| Free cash flow yield (%) | 1.05 |
| MA50 | 545.9396 |
| Close vs MA50 (%) | -22.2368 |
| MA200 | 434.0147 |
| Close vs MA200 (%) | -2.1830 |
| RSI (14, Wilder) | 40.8394 |
| MACD (12,26) | -29.5778 |
| MACD signal (9) | -20.6415 |
| MACD histogram | -8.9363 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMD': 291, 'SPY': 291}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 424.5400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 4.5588 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.0353 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -24.2245 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 98.2350 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 98.1609 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 75.5262 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 50.2570 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.9097 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 7.1869 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 10.2670 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6529 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 66.6969 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.2824 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -37.7290 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.2708 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 24.0693 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 56.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 17.8210 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 11.9600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.0471 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 90.7137 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 40.8394 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -8.9363 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -22.2368 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -2.1830 -> Slightly below the moving-average trend level.

## TAILWINDS

### Advanced Micro Devices (NASDAQ:AMD) Shares Up 4.1% - Here's What Happened
- Summary: Advanced Micro Devices (NASDAQ:AMD) Shares Up 4.1% - Here's What Happened
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxQd0ZVUlB3a3ZuamtEX1NCNi1LdUFQSXM4X3RKOUhfRWFuRks1d0ZsRm1wdklrWXd4aDFrMzBwamJrbUxXcHRoWWpaSjVBVDljQVhYMEp1TGc3U1lnalRBdmM1NEFRbHJpaDZ0MGM2dzZibVQyZnZvSEpOeXJRZUM0M1VEeWR3dXc5TXVobmRqblJYaVFHNDV2WW1zNmJOY2lva2ViWVNfOUlYdlI3OWFTa295dWpadkZmR291R0EyMVl6aVdl?oc=5>

### AMD Stock Rises Over 2% as Chipmakers Rebound Despite AI Export, Security Scrutiny
- Summary: AMD Stock Rises Over 2% as Chipmakers Rebound Despite AI Export, Security Scrutiny
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxQSk1JZ2gxcGdlTm1heUtZU0R2VUl4S2tYZGFaSVpmOGNzZUM5ZFdVMXJnUFZIV242SmdjdURPUmpjdFZSSmc1dXIxTWRJVElkeVZBd1RWclQ5TTdiQk5oQ1VkenA5enZWaVg1bXhuWVNxM1VvZjNaWldiaWhUelZnV3VzNENOd0FmblBtZEFuM2ZfbnltbmhIZmg5ajdKbE9DUjkyT0ZRRTZ1WVlEaDJBaWNTeVRpWFN6RlhuRHVBd3JUZUF4TXpSUzhrLV8yUQ?oc=5>

### Advanced Micro Devices (AMD) After AI Data Center Wins Looks Cheap Or Already Priced In
- Summary: AI data center wins may boost AMD’s valuation, suggesting potential upside.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPdV8tZUUxREQ0MzVPWUdabFZOTzdheFJUMjhmVVd5cGk4UUVRNlRBckdHVjc5ZlJEeUFxQzMzWnRVS0E4TmxHZFQ2WGZpS3F3YWFYMmNiU21NZXVMLTdIc0RyYXBndkVKU2NlUzg2dm9tbXVNRjdNcWJwZGxzNkdVTXQ0N3hmdjZmbmt6Vjhnc21lWTZxeUlodkF3?oc=5>

### Advanced Micro Devices Inc Stock (AMD) Moved Up by 3.04% on Nov 27: What Signal Does It Send?
- Summary: A 3% price increase signals positive market sentiment for AMD.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxPMlM1ZnlCTG1lczFPemd3N0J0UUpwUHJCZFhRNXBfNVNCcDBMLVA1TVBIX1R4Sm5FeGNNaGxOOHE4a0tVM1ZlTFdvYW12bUgzWndWalpHbjAzQ1dMU0xUVnJTdUNRWFJyc1FYUTltVDh6RlBDeHZVV1NmS1htOVgxekJ3YW9ZYUx2ZEE?oc=5>

## HEADWINDS

### Advanced Micro Devices downgraded by Erste Group
- Summary: Advanced Micro Devices downgraded by Erste Group
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNZGNRWlQwbHZuYTYzbWxBRlkzR0FPSk9URGdqSHp6ZXdXZV9Pb0hkME5IcUpjN2d4YmFJZDgtcWlkOU1CYTNLZk1zTERKWXRyenFWTjhlaTJRckxMdkFmS2FFUXNwVXpHREVWOHNEUjVpNW9UNnF6V3lmSm9xUmJ0T09ub19VLWVHVlVRbm0zSjdRV193VEE?oc=5>

### AMD Stock Shows the Market Has Stopped Making Sense After Huang’s Dramatic Return
- Summary: Stock volatility following CEO Huang’s return, negative market reaction.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxQZFZiUXAwenUzWFNOTXVsanB4ZEdoeU1nMFozQTF5T0NNRnZGZG1UVnhuWXFwb3Rhc2ZlU1h5dVc1aXUydlcxdEl3ZUZGY2p5MzBQUEZGSzNWb1ZkZ2tDQnh4NTJLX2FJUUtfSmVvQllMY3FESV9uc0g5Z25fTlpBV2FHMjhJY3M?oc=5>

### AMD Shares Just Got Crushed on a Short Report. Why the Drop Is a Golden Buying Opportunity.
- Summary: Short report triggered a sharp drop, indicating negative sentiment.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxQeWFoX3BiZW91cUFEUlBMLXZVeFcxUjVMR2JWOTJveFlIcnRyNk4xUHFRUTJVWlJYajZ5QkNyOXozU2VNOTNPR3BnV3A2TzhlOEhZdldmU3Zwb0dJeDAyRDJ2c3ctM1E2MnVrclpnZmtkdkpKX3BrWUZKaThoa2lrVWdsMnNjWV8temxXeENrUFdxdU5aMURkV2d3REtzdDdDTXBYOGpfMjR2TS1YTi1NWXRscVVKUWNxOTlhS3k4ZkhybUluNUVsaVpEbFU?oc=5>

## CATALYSTS

### Why Is Advanced Micro Devices Stock Rallying Today?
- Summary: AMD shares surge today, driven by positive market sentiment and recent performance highlights.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPTHluRzJsN0J5dHFzZXVXRzVEM01uVmdteTg1WFNucWhwS0JDa2tkUTRjOGFFd1J0WTFLUkVMQjdHbUdXNmpiV0lEcGh6MHY4VGVCY0VvZ25nenptZVhrWEhRWjFLN2J3eDFjOFF0TGV2QkIwUFlybjB4b2lQU3gxaFBuZGdVcDhfV2lsdkdIdnFhS3JVaDJmMWJQRVdYZw?oc=5>

## RISKS

### AMD: The Sell-Off Is Getting Interesting (NASDAQ:AMD)
- Summary: Reports indicate a significant sell-off in AMD shares, reflecting investor concerns about valuation and market conditions.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxPZ2x2emVWVnhaNTJJZkd5SEMtakRlRENHZk43NWp4akNDOXhVdUVhelFhVENCUm1COWc5RDFCa2pHSmJvR0diM0dyaEtiUWxaY3I0TUxSUWVtd1FEa2x3Rkx3SnMxRlpKMnYxMExzSHlkRjIxaUphb1VrS0ZkczJ2Wk45WkVmWlE?oc=5>

### Why Are Nvidia, AMD, Oracle and CoreWeave Stocks Crashing Today? AI Spending and Debt Fears Grow
- Summary: Multiple tech stocks, including AMD, are experiencing sharp declines due to fears over AI spending and rising debt levels.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigAFBVV95cUxPV3ctVzB5ZWkxMnFYX2VCNXZHZXY0SFc1QWh4U1dkNHhmU0JoaGFQY05DTEVPbDhYeE5OWjJJNVY3S1dhMXJjTFV2YXVZS1U1cDJWYjBYckdOQkNrRm9qTG4xazBUWVNmVk1aVnFISWZ3emxVREtvVjg3SWJyRjVCTg?oc=5>

### Advanced Micro Devices falls amid Hunterbrook post on X (update)
- Summary: AMD shares dropped following a negative post by Hunterbrook on X, impacting investor sentiment.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxNT2JfcEdtbnVqcWRNWVkwc0R1bHpzWndsTnUxbFFTakdNY3FveVBfV2t2VE1WQklxc2ljdnFWX2tTVnk3MFU4UXVrUlR4SVJkT2JLMEJ4Z01hM3U4UVdUUG84MC1SRXlWOTExaUYtQ25STmNtMjlYUnVPTXBnakcwd2IwR3NDdzMwRDJGVzdKQnZ3M0pZMFdTLWpWWldoVlhIU1h0NUV5RVMtWnA0alE3dElrR3ZZNjBMM1E?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMD** | **90.71** | **10.18** | **61.90** | **44.70** | **702,641,537,024.00 USD** | **98.16** |
| NVDA | 16.16 | 13.60 | 14.67 | 103.20 | 3,633,882,071,040.00 USD | -16.32 |
| INTC | N/A | 2.65 | 16.61 | 20.90 | 305,080,991,744.00 USD | 55.94 |
| AVGO | 39.89 | 14.96 | 29.21 | 85.50 | 1,490,995,511,296.00 USD | -20.85 |

Peers fetched as_of: 2026-11-27; AMD reuses existing data (market data as_of: 2026-11-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-03
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-27

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 1,584,000,000.00 USD; period 2017-07-02/2017-09-30; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 2,428,000,000.00 USD; period 2026-06-28/2026-09-26; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMixAFBVV95cUxQd0ZVUlB3a3ZuamtEX1NCNi1LdUFQSXM4X3RKOUhfRWFuRks1d0ZsRm1wdklrWXd4aDFrMzBwamJrbUxXcHRoWWpaSjVBVDljQVhYMEp1TGc3U1lnalRBdmM1NEFRbHJpaDZ0MGM2dzZibVQyZnZvSEpOeXJRZUM0M1VEeWR3dXc5TXVobmRqblJYaVFHNDV2WW1zNmJOY2lva2ViWVNfOUlYdlI3OWFTa295dWpadkZmR291R0EyMVl6aVdl?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxQSk1JZ2gxcGdlTm1heUtZU0R2VUl4S2tYZGFaSVpmOGNzZUM5ZFdVMXJnUFZIV242SmdjdURPUmpjdFZSSmc1dXIxTWRJVElkeVZBd1RWclQ5TTdiQk5oQ1VkenA5enZWaVg1bXhuWVNxM1VvZjNaWldiaWhUelZnV3VzNENOd0FmblBtZEFuM2ZfbnltbmhIZmg5ajdKbE9DUjkyT0ZRRTZ1WVlEaDJBaWNTeVRpWFN6RlhuRHVBd3JUZUF4TXpSUzhrLV8yUQ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPdV8tZUUxREQ0MzVPWUdabFZOTzdheFJUMjhmVVd5cGk4UUVRNlRBckdHVjc5ZlJEeUFxQzMzWnRVS0E4TmxHZFQ2WGZpS3F3YWFYMmNiU21NZXVMLTdIc0RyYXBndkVKU2NlUzg2dm9tbXVNRjdNcWJwZGxzNkdVTXQ0N3hmdjZmbmt6Vjhnc21lWTZxeUlodkF3?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxPMlM1ZnlCTG1lczFPemd3N0J0UUpwUHJCZFhRNXBfNVNCcDBMLVA1TVBIX1R4Sm5FeGNNaGxOOHE4a0tVM1ZlTFdvYW12bUgzWndWalpHbjAzQ1dMU0xUVnJTdUNRWFJyc1FYUTltVDh6RlBDeHZVV1NmS1htOVgxekJ3YW9ZYUx2ZEE?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNZGNRWlQwbHZuYTYzbWxBRlkzR0FPSk9URGdqSHp6ZXdXZV9Pb0hkME5IcUpjN2d4YmFJZDgtcWlkOU1CYTNLZk1zTERKWXRyenFWTjhlaTJRckxMdkFmS2FFUXNwVXpHREVWOHNEUjVpNW9UNnF6V3lmSm9xUmJ0T09ub19VLWVHVlVRbm0zSjdRV193VEE?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxQZFZiUXAwenUzWFNOTXVsanB4ZEdoeU1nMFozQTF5T0NNRnZGZG1UVnhuWXFwb3Rhc2ZlU1h5dVc1aXUydlcxdEl3ZUZGY2p5MzBQUEZGSzNWb1ZkZ2tDQnh4NTJLX2FJUUtfSmVvQllMY3FESV9uc0g5Z25fTlpBV2FHMjhJY3M?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxQeWFoX3BiZW91cUFEUlBMLXZVeFcxUjVMR2JWOTJveFlIcnRyNk4xUHFRUTJVWlJYajZ5QkNyOXozU2VNOTNPR3BnV3A2TzhlOEhZdldmU3Zwb0dJeDAyRDJ2c3ctM1E2MnVrclpnZmtkdkpKX3BrWUZKaThoa2lrVWdsMnNjWV8temxXeENrUFdxdU5aMURkV2d3REtzdDdDTXBYOGpfMjR2TS1YTi1NWXRscVVKUWNxOTlhS3k4ZkhybUluNUVsaVpEbFU?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPTHluRzJsN0J5dHFzZXVXRzVEM01uVmdteTg1WFNucWhwS0JDa2tkUTRjOGFFd1J0WTFLUkVMQjdHbUdXNmpiV0lEcGh6MHY4VGVCY0VvZ25nenptZVhrWEhRWjFLN2J3eDFjOFF0TGV2QkIwUFlybjB4b2lQU3gxaFBuZGdVcDhfV2lsdkdIdnFhS3JVaDJmMWJQRVdYZw?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxPZ2x2emVWVnhaNTJJZkd5SEMtakRlRENHZk43NWp4akNDOXhVdUVhelFhVENCUm1COWc5RDFCa2pHSmJvR0diM0dyaEtiUWxaY3I0TUxSUWVtd1FEa2x3Rkx3SnMxRlpKMnYxMExzSHlkRjIxaUphb1VrS0ZkczJ2Wk45WkVmWlE?oc=5
- https://news.google.com/rss/articles/CBMigAFBVV95cUxPV3ctVzB5ZWkxMnFYX2VCNXZHZXY0SFc1QWh4U1dkNHhmU0JoaGFQY05DTEVPbDhYeE5OWjJJNVY3S1dhMXJjTFV2YXVZS1U1cDJWYjBYckdOQkNrRm9qTG4xazBUWVNmVk1aVnFISWZ3emxVREtvVjg3SWJyRjVCTg?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxNT2JfcEdtbnVqcWRNWVkwc0R1bHpzWndsTnUxbFFTakdNY3FveVBfV2t2VE1WQklxc2ljdnFWX2tTVnk3MFU4UXVrUlR4SVJkT2JLMEJ4Z01hM3U4UVdUUG84MC1SRXlWOTExaUYtQ25STmNtMjlYUnVPTXBnakcwd2IwR3NDdzMwRDJGVzdKQnZ3M0pZMFdTLWpWWldoVlhIU1h0NUV5RVMtWnA0alE3dElrR3ZZNjBMM1E?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
