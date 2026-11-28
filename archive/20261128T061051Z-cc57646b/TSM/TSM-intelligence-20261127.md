# TSM Intelligence Report

- ticker: **TSM**
- Report as_of: **2026-11-27**
- Market data as_of: **2026-11-27**
- Quant sources: https://finance.yahoo.com/quote/TSM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TSM/key-statistics/
- AI analysis snapshot as_of: **2026-11-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-28T06:33:07.774958+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 2, 'ai': 12, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **11** exact headline/source/date matches; prior report **20261127T063646Z-c0c26981/TSM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'directional_claim_without_event_type': 1}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 9 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 34.78%; oldest publication 2026-11-23

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 353.3400 |
| Return 1D (%) | 3.2132 |
| Return 1W (%) | 10.8657 |
| Return 1M (%) | -19.1201 |
| Return YTD (%) | 17.1866 |
| Return 1Y (%) | 23.1479 |
| Annualized volatility (%) | 46.0060 |
| Beta vs SPY | 2.3336 |
| Max drawdown (%) | -34.3948 |
| Sharpe (rf=0) | 0.6735 |
| Downside deviation (rf=0, %) | 31.4632 |
| Sortino (rf=0) | 0.9848 |
| Historical VaR 95% (1D, %) | 4.3962 |
| Historical ES 95% (1D, %) | 6.3161 |
| Correlation vs SPY | 0.7620 |
| Tracking error vs SPY (%) | 35.9027 |
| P/E (trailing) | 22.90 |
| P/B | 67.87 |
| EV/EBITDA | 3.27 |
| Revenue growth (%) | 50.90 |
| Forward P/E (estimate) | 15.09 |
| Gross margin (%) | 65.85 |
| Operating margin (%) | 57.96 |
| Return on equity (%) | 41.86 |
| Free cash flow yield (%) | N/A |
| MA50 | 416.7246 |
| Close vs MA50 (%) | -15.2102 |
| MA200 | 402.1438 |
| Close vs MA200 (%) | -12.1359 |
| RSI (14, Wilder) | 42.1657 |
| MACD (12,26) | -19.9606 |
| MACD signal (9) | -18.0490 |
| MACD histogram | -1.9116 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TSM': 291, 'SPY': 291}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 353.3400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 3.2132 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 10.8657 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -19.1201 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 17.1866 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 23.1479 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 46.0060 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 31.4632 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.9848 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.3962 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.3161 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.7620 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 35.9027 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.3336 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -34.3948 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.6735 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.0901 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 65.8460 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 57.9610 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 41.8600 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 22.8995 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 42.1657 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.9116 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -15.2102 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -12.1359 -> Clearly below the moving-average trend level.

## TAILWINDS

### TSMC (TSM) Upgraded to Strong Buy: Here's Why
- Summary: TSMC (TSM) Upgraded to Strong Buy: Here's Why
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxORGc1OVBNTENnRDdzbGZBaDVxemF1S1k5UC01OE1aUjdwWUtYeVFJbU03M3RXenJtRy1HQW9FdklHSkdhNnhqdUVwYzBtcWZzeXRtY1JPaEhRR2RCd2NhT3RORnNVeUR5U3NXNEtQOEpJZ0E2eVdLSl9MMk1PVXJGQ085M0p1RWxhSWNvSERFZGpfRFp0dEo4Nw?oc=5>

### Taiwan Semiconductor Manufacturing Co Ltd Stock (TSM) Moved Up by 3.22% on Nov 27: A Full Analysis
- Summary: Taiwan Semiconductor Manufacturing Co Ltd Stock (TSM) Moved Up by 3.22% on Nov 27: A Full Analysis
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxOLVZvY2dOVDN4RmdOX3JMeUJNVjlDZGFOaVRwcTZoOHktMC11OVRvWlhxaTVzR0phZkFZNjB4UGJvU2E2c0VvRUptUHZNMHFsX2dJTVYybW1ETlRwNEFhM1FIbmpsY3hONUVTeEdOdTUtWGNjRVBkWmhyUkFhQ3liWkltV0ZId1hWRVE?oc=5>

### Trump Is Heading to Arizona to Break Ground on TSMC’s Newest Chip Plant
- Summary: President Trump will break ground on TSMC’s new Arizona chip plant, signaling expansion and increased production capacity.
- Date: 2026-11-27 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQRFRoOTNQMkpXZFlTSG0zVUxwSk5oSVpCN0EtZ1pGWEZoQ0NMNlB1dWdHYVpHb1ZCYnd1TnNKNlVuc252YWRzY19Od2ZfTGlWS2NiZ3luUEQ2eWd5eXlfbFROeXNoTGg0R3gxMTJwTGhzZHljWVFwMzlXdVVYdVQ4bFBidHExRm4tOVg2RXhDTHh3M3g2X3luOGV0TQ?oc=5>

### TSMC (TSM) Is Building a Semiconductor Moat That Rivals May Struggle to Cross
- Summary: TSMC is strengthening its competitive moat, enhancing market dominance and resilience against rivals.
- Date: 2026-11-27 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNMjlVWllkMzBpVm9IUEkxT2RieWszOXlNVERiVzVYTGdiWmtBZ0ZkVjFhSmJiRTRleW5lc3gxRWpjU3hfUVlseTFTc1R0UkYzOUtLYkc5TVNGS0R0dmhkVWZIOHVBVXdMblBfZW5uQ2l0ZUJRUm5hVTBtM2RZb3luV0xINXBBMGhZNmg2ZmRSV2hBSXVENFdhSmRUMFoxZw?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Trump Warns of “Paying 200 Percent on Chips” in Two Years. That Pushes TSMC Toward a $22.6 Billion Texas Plant
- Summary: Potential U.S. plant expansion could boost TSMC’s production capacity.
- Date: 2026-11-24 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi3gFBVV95cUxNeVNuU2V1WFJMVG1qWmkwNUZqQjh5WWk3eFEtcC10ZWhGQU1GNC14bWw3NllTSjZpOVpEVFlybFVsTmd6ZDVaSzlFU3lTdEhfWG5nMklCVXhrOHhKN1ZyRF82NmJkYUVWbHo3Z1N2X0RldDJ4WTZXN3pTd1Iwb2dUZTNzN1hqV0NVVkREZmNhOEpPd1VYemtKOG9xSFhzbzN5YVluZVFKeUtQeUVYQWlQUUEzRmh2bWQzMk5CbTVFMWF4Z0ZURXItWm0taU9nSjYweHE2S2phU0JLbFd6V1E?oc=5>

### Taiwan Semiconductor Manufacturing (NYSE:TSM) Stock May Be Reasonable After New Export Curbs
- Summary: TSM stock may be reasonable following new export curbs, suggesting potential upside.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxPa1JvdC0wSGFvVjBwYUYzVlhoX2FHMkdLMUdUUUtibHZhUmJzWkxoT24wQlBjeGZfWGxydF92YnAxN3BDRl9VdkFtTVRiY0tyc1ZjS1RYWE16NUN1X2ZDLW1SRW9vYmdxSmhFMzU5UmdJSV81RE9XOGNIWEYwZFJCMm1OWTFzWS1hckRybm9MVXZLUV9HVTRNZmZRNVdMNDlhVkprUC1DYTBKOHdv?oc=5>

### Down On TSMC Stock? Your Buy Price Decides It
- Summary: TSM stock performance depends on buy price, indicating market sensitivity.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxOLWc4NXFYcWoxVVljOGZaR2kzVHF2QnY5X2l0eEY4Ri1BWGNhTzlMWWhiM1BLdWtXWnN2QWhabzliQzBSYjI1UFBMV3gxYUlqMnBfTjhqWTBDb0Z0SUFCeTBxdVRvTjBNVEF2ZFVmeWFXSXQyZ0RNbTZpb0dlYmhLT2Yzc2hzam5ENVVzZzJOSC1kWWN3cjI5WTh0Nm1xVWlGSlVsR2NIWQ?oc=5>

### Nvidia vs. TSMC: With Jensen Huang Back, Which AI Stock Is the Better Buy for 2027?
- Summary: Analyst comparison of TSMC vs Nvidia for 2027, offering investment guidance.
- Date: 2026-11-23 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxNdWhCeTlBalBJa1lLUlZlX0xlOWFaWUZQS2VTRVFUUEJwbWVrcU85OTVwQXRKRG9ZUldYZjNaZHk0QWN2dWtPblkwdXluTjB5cDFnZjMzMVEyaVZSZG9QVTdvVUFGSFV1Yk1vd09tQ3Y3NTN1RzNpMHBNQUtsZzBOZFpBdDhjeXRQaWw3MTNFX2Y1ZUdkbjZhZFBmYzNuZ1pUSFlhb3laRG50X0IzQm8wM1p2bUtwOHdSSUMxejNSR1FLZlVnbTZQMzVkR0o?oc=5>

### History Says TSMC Stock Falls Before Its Sales
- Summary: Stock fell before sales announcement, no event specified.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPUFFsQTg2cVZWZjh5R3RsUk1QbkdWTC1VazlPT25ONmVqZ3EyY3o2LU9Sa1BFN1VJZjRiOGF1bXJIZlNKYjYxX3lZdm5RTjE3aHRJUWMzcHg0UWJSYkxLaWJSTHo5VkllWGN1ZjRwX1NpWlhiOVBqNk9BdDFNWXNhRmU4UDZBQUtJckFHYlBPM3ZWOC1vNjVScVl0QUE2bG5RckpvT1E4Wm0xQQ?oc=5>

### Why TSMC Stock Soared Today
- Summary: TSMC shares surged today, reflecting positive market sentiment.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOMEdpVWJwSTh1cU9tb25IQWwwR3VjdlNfYWZUYXI5b3lrZzRTb3c3SHBqVy00endjamt2M3RvMFZLcGZRTmRLcTZTOE92ejJqM09vejF6Y29zRy02XzRQeGJ2a2ZKaTVDNE5DeU1YbjJUc3NOM3plT3NJOWZWZ1ZoTm9YZ0JZZkZGMXZwUkNxQ3NnSVhDWDVn?oc=5>

### Taiwan Semiconductor Manufacturing (TSM) May Make Its $22.6 Billion Texas Plant Conditional
- Summary: TSM may condition its $22.6B Texas plant on regulatory approvals, potentially delaying construction.
- Date: 2026-11-26 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQY0Vwa0dtbVZjbmlKcW1zeXlsNlZRNFc2YkJTNURRbnJnTWI4aVZTbHZQMWY3UWpJb0FKRjJQOFJSMDFWU0NlVGUtM3NYd2FQTVNycno0U1hDNmp4Tml1OXllS0hVenotUzlDVkxsUThzd3VXUFpyek9uMC1EbjFlOURDZERyZkVEUm40ZGV2RGUzeExVcDN1d1hqMXpfTDUzZ3RyZHNR?oc=5>

### TSMC: Starting To Look Like A Buy Again (Rating Upgrade) (NYSE:TSM)
- Summary: Analyst upgrade signals renewed confidence in TSMC’s prospects, potentially boosting investor sentiment.
- Date: 2026-11-27 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxQQnd3NWV0Z0NKOFNuTXktdTI0S05UZDluc2V1UVJld3YtZU1oRXpSZFRNSWVZNnhFZlhkOGlUX05zcTY2VTVGcHhJbkVvM1JrYWEyRDVwaHFPWTZvVGpFbUd6NU11cVE4TFVJLVBWdGZvV1ZmSHJWelAwSU1UbjM3MF9KVWFUS0c4MVJRdzljeTg?oc=5>

### TSMC Stock Just Had Its Best Day Since 2008
- Summary: TSMC shares surged, marking the strongest performance since 2008.
- Date: 2026-11-24 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxQeVFFYS1CVFNpYzJZQ2VUM3hMOGFJb2ZnRV9vMzZpYnlXUEZEOTlTZVFwdkg3SGZHekhoRnNKRXlrNU5UeXROQzZHdE5qd2dDcG5pVTFfYnVVa0tPVUkwRUNWQ242R292azd3ckM1dTQwVUF4MlJPNUNNaTRfSG9OQmE2MjUtTmJ5ZWUxVEhYWGw?oc=5>

## RISKS

### No Threat to TSMC Before 2028: Intel’s Foundry Gap Is Still Huge
- Summary: Intel’s foundry gap remains large, indicating no imminent threat to TSMC before 2028.
- Date: 2026-11-27 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxQX21kN1Ria3AzTjNrN2syTmIydk1XVlJQRF81ZGxXOUFOdE5OSkkxNTdHZ1lPNHdOaEl0aHBMdU5hdklNUWFSN0FpVFpNaGRCeXVXQ05xdjl4QjBmZXVvVVU1VnI0MUl1TE9ZUE1nMUJOMEVwam5WdVd3NWZMd3dyTHI1Y2xVVzBfc2pPUnlVZw?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TSM** | **22.90** | **67.87** | **3.27** | **50.90** | **1,832,588,279,808.00 USD** | **23.15** |
| UMC | 12.68 | 2.32 | -0.32 | 25.60 | 33,704,749,056.00 USD | 86.58 |
| GFS | 107.74 | 1.76 | 10.10 | 12.50 | 21,021,392,896.00 USD | 7.34 |
| INTC | N/A | 2.65 | 16.61 | 20.90 | 305,080,991,744.00 USD | 55.94 |

Peers fetched as_of: 2026-11-27; TSM reuses existing data (market data as_of: 2026-11-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-27

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

- https://news.google.com/rss/articles/CBMimAFBVV95cUxORGc1OVBNTENnRDdzbGZBaDVxemF1S1k5UC01OE1aUjdwWUtYeVFJbU03M3RXenJtRy1HQW9FdklHSkdhNnhqdUVwYzBtcWZzeXRtY1JPaEhRR2RCd2NhT3RORnNVeUR5U3NXNEtQOEpJZ0E2eVdLSl9MMk1PVXJGQ085M0p1RWxhSWNvSERFZGpfRFp0dEo4Nw?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxOLVZvY2dOVDN4RmdOX3JMeUJNVjlDZGFOaVRwcTZoOHktMC11OVRvWlhxaTVzR0phZkFZNjB4UGJvU2E2c0VvRUptUHZNMHFsX2dJTVYybW1ETlRwNEFhM1FIbmpsY3hONUVTeEdOdTUtWGNjRVBkWmhyUkFhQ3liWkltV0ZId1hWRVE?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQRFRoOTNQMkpXZFlTSG0zVUxwSk5oSVpCN0EtZ1pGWEZoQ0NMNlB1dWdHYVpHb1ZCYnd1TnNKNlVuc252YWRzY19Od2ZfTGlWS2NiZ3luUEQ2eWd5eXlfbFROeXNoTGg0R3gxMTJwTGhzZHljWVFwMzlXdVVYdVQ4bFBidHExRm4tOVg2RXhDTHh3M3g2X3luOGV0TQ?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxQbXBCM01wNWZqejdvRVNVNWZwQW1fNWVTb2J2dGo5aFpJZ2lVWmtrNUVvNnZaRThlX3NlYkstSjF3T2JBSy1KRDFILWt2TFJ2cW1mMEpaV3hXVzNieURJODcwNHdtTV8weTlKZWp1c3VIalRIOVZfbHdqOEtNVW04Tl9vR3RFVWJKNEhHUXNwaUdZYXhjNUtQVjZ3WnZkdEFzSnpXQVlNc2RNNk9SRl9WVC1SN0Q?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxNMjlVWllkMzBpVm9IUEkxT2RieWszOXlNVERiVzVYTGdiWmtBZ0ZkVjFhSmJiRTRleW5lc3gxRWpjU3hfUVlseTFTc1R0UkYzOUtLYkc5TVNGS0R0dmhkVWZIOHVBVXdMblBfZW5uQ2l0ZUJRUm5hVTBtM2RZb3luV0xINXBBMGhZNmg2ZmRSV2hBSXVENFdhSmRUMFoxZw?oc=5
- https://news.google.com/rss/articles/CBMi3gFBVV95cUxNeVNuU2V1WFJMVG1qWmkwNUZqQjh5WWk3eFEtcC10ZWhGQU1GNC14bWw3NllTSjZpOVpEVFlybFVsTmd6ZDVaSzlFU3lTdEhfWG5nMklCVXhrOHhKN1ZyRF82NmJkYUVWbHo3Z1N2X0RldDJ4WTZXN3pTd1Iwb2dUZTNzN1hqV0NVVkREZmNhOEpPd1VYemtKOG9xSFhzbzN5YVluZVFKeUtQeUVYQWlQUUEzRmh2bWQzMk5CbTVFMWF4Z0ZURXItWm0taU9nSjYweHE2S2phU0JLbFd6V1E?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxPa1JvdC0wSGFvVjBwYUYzVlhoX2FHMkdLMUdUUUtibHZhUmJzWkxoT24wQlBjeGZfWGxydF92YnAxN3BDRl9VdkFtTVRiY0tyc1ZjS1RYWE16NUN1X2ZDLW1SRW9vYmdxSmhFMzU5UmdJSV81RE9XOGNIWEYwZFJCMm1OWTFzWS1hckRybm9MVXZLUV9HVTRNZmZRNVdMNDlhVkprUC1DYTBKOHdv?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxOLWc4NXFYcWoxVVljOGZaR2kzVHF2QnY5X2l0eEY4Ri1BWGNhTzlMWWhiM1BLdWtXWnN2QWhabzliQzBSYjI1UFBMV3gxYUlqMnBfTjhqWTBDb0Z0SUFCeTBxdVRvTjBNVEF2ZFVmeWFXSXQyZ0RNbTZpb0dlYmhLT2Yzc2hzam5ENVVzZzJOSC1kWWN3cjI5WTh0Nm1xVWlGSlVsR2NIWQ?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxNdWhCeTlBalBJa1lLUlZlX0xlOWFaWUZQS2VTRVFUUEJwbWVrcU85OTVwQXRKRG9ZUldYZjNaZHk0QWN2dWtPblkwdXluTjB5cDFnZjMzMVEyaVZSZG9QVTdvVUFGSFV1Yk1vd09tQ3Y3NTN1RzNpMHBNQUtsZzBOZFpBdDhjeXRQaWw3MTNFX2Y1ZUdkbjZhZFBmYzNuZ1pUSFlhb3laRG50X0IzQm8wM1p2bUtwOHdSSUMxejNSR1FLZlVnbTZQMzVkR0o?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPUFFsQTg2cVZWZjh5R3RsUk1QbkdWTC1VazlPT25ONmVqZ3EyY3o2LU9Sa1BFN1VJZjRiOGF1bXJIZlNKYjYxX3lZdm5RTjE3aHRJUWMzcHg0UWJSYkxLaWJSTHo5VkllWGN1ZjRwX1NpWlhiOVBqNk9BdDFNWXNhRmU4UDZBQUtJckFHYlBPM3ZWOC1vNjVScVl0QUE2bG5RckpvT1E4Wm0xQQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOMEdpVWJwSTh1cU9tb25IQWwwR3VjdlNfYWZUYXI5b3lrZzRTb3c3SHBqVy00endjamt2M3RvMFZLcGZRTmRLcTZTOE92ejJqM09vejF6Y29zRy02XzRQeGJ2a2ZKaTVDNE5DeU1YbjJUc3NOM3plT3NJOWZWZ1ZoTm9YZ0JZZkZGMXZwUkNxQ3NnSVhDWDVn?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQY0Vwa0dtbVZjbmlKcW1zeXlsNlZRNFc2YkJTNURRbnJnTWI4aVZTbHZQMWY3UWpJb0FKRjJQOFJSMDFWU0NlVGUtM3NYd2FQTVNycno0U1hDNmp4Tml1OXllS0hVenotUzlDVkxsUThzd3VXUFpyek9uMC1EbjFlOURDZERyZkVEUm40ZGV2RGUzeExVcDN1d1hqMXpfTDUzZ3RyZHNR?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxQQnd3NWV0Z0NKOFNuTXktdTI0S05UZDluc2V1UVJld3YtZU1oRXpSZFRNSWVZNnhFZlhkOGlUX05zcTY2VTVGcHhJbkVvM1JrYWEyRDVwaHFPWTZvVGpFbUd6NU11cVE4TFVJLVBWdGZvV1ZmSHJWelAwSU1UbjM3MF9KVWFUS0c4MVJRdzljeTg?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxQeVFFYS1CVFNpYzJZQ2VUM3hMOGFJb2ZnRV9vMzZpYnlXUEZEOTlTZVFwdkg3SGZHekhoRnNKRXlrNU5UeXROQzZHdE5qd2dDcG5pVTFfYnVVa0tPVUkwRUNWQ242R292azd3ckM1dTQwVUF4MlJPNUNNaTRfSG9OQmE2MjUtTmJ5ZWUxVEhYWGw?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxQX21kN1Ria3AzTjNrN2syTmIydk1XVlJQRF81ZGxXOUFOdE5OSkkxNTdHZ1lPNHdOaEl0aHBMdU5hdklNUWFSN0FpVFpNaGRCeXVXQ05xdjl4QjBmZXVvVVU1VnI0MUl1TE9ZUE1nMUJOMEVwam5WdVd3NWZMd3dyTHI1Y2xVVzBfc2pPUnlVZw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
