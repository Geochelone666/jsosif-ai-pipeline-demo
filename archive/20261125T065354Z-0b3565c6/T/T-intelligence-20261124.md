# T Intelligence Report

- ticker: **T**
- Report as_of: **2026-11-24**
- Market data as_of: **2026-11-24**
- Quant sources: https://finance.yahoo.com/quote/T/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/T/key-statistics/
- AI analysis snapshot as_of: **2026-11-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-25T07:21:53.502048+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 16, 'rule': 2, 'ai': 5, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261124T081701Z-6c335e3d/T** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 16 unique headlines; 10 named publishers; 1 exact duplicates; 16 HTTPS source links; largest publisher share 18.75%; oldest publication 2026-11-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 22.8800 |
| Return 1D (%) | 2.6009 |
| Return 1W (%) | 2.6469 |
| Return 1M (%) | 9.3168 |
| Return YTD (%) | -3.4957 |
| Return 1Y (%) | -6.4338 |
| Annualized volatility (%) | 28.7722 |
| Beta vs SPY | -0.3199 |
| Max drawdown (%) | -28.8854 |
| Sharpe (rf=0) | -0.0868 |
| Downside deviation (rf=0, %) | 21.9586 |
| Sortino (rf=0) | -0.1138 |
| Historical VaR 95% (1D, %) | 2.8546 |
| Historical ES 95% (1D, %) | 4.6484 |
| Correlation vs SPY | -0.1663 |
| Tracking error vs SPY (%) | 34.5622 |
| P/E (trailing) | 12.24 |
| P/B | 1.45 |
| EV/EBITDA | 7.44 |
| Revenue growth (%) | 5.30 |
| Forward P/E (estimate) | 8.81 |
| Gross margin (%) | 59.74 |
| Operating margin (%) | 22.59 |
| Return on equity (%) | 11.61 |
| Free cash flow yield (%) | 7.76 |
| MA50 | 22.9585 |
| Close vs MA50 (%) | -0.3418 |
| MA200 | 24.2648 |
| Close vs MA200 (%) | -5.7071 |
| RSI (14, Wilder) | 58.0320 |
| MACD (12,26) | -0.0736 |
| MACD signal (9) | -0.2444 |
| MACD histogram | 0.1708 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'T': 289, 'SPY': 289}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 22.8800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.6009 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.6469 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 9.3168 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -3.4957 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -6.4338 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 28.7722 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.9586 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.1138 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8546 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.6484 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1663 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 34.5622 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.3199 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.8854 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.0868 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 8.8142 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 59.7420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 22.5930 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 11.6130 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 7.7608 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 12.2353 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 58.0320 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.1708 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -0.3418 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -5.7071 -> Clearly below the moving-average trend level.

## TAILWINDS

### AT&T (NYSE:T) Stock Jumps 2.6% - Here's Why
- Summary: AT&T (NYSE:T) Stock Jumps 2.6% - Here's Why
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQX2dsLUV0TnpEdGFaTTUtb1d1RGVSdWV3ZzEyVzFURG1SWGlINmtCOWRYMVZnOV9od1JybXBjbkp1M3hkd0ZybVJxSWx1Q0ZPX0ZXR1pTQjZ2UGEwNkJwczhuNzFja2REM0RGVnhvUkl3UUlqaHNEay1EZlJVdHpBa1ZkWFRMM0piWUpNa3FvZFlwX1hSNldZOEFOOA?oc=5>

### Can T's Extended U.S. Soccer Deal Boost Sports Technology Innovation?
- Summary: AT&T's extended U.S. Soccer deal could enhance sports tech innovation.
- Date: 2026-11-23 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxQTjVzSkJvanJ1TG1iTEp6TGZUdHJ5U2ZNVmgtZjlRVGlKVkdpNWdzYzlhOFY0UGsxamhCa1VOOElzbXVWMkZLNnhOYkxRV1RWU3NxR0F3TVUtOGNieFdfN1hGX0dXRGZxUHlzem1HQUJiWkhiVVN5N1dYMzFsR040VmJaa2lWcWx1YTBCQlMyZmVrUTRSd19HZHk3c212TXhEbHBvZ01IcnBkNUd2LWFiRWlSM1pMblh0RXVxUzJwRkM?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### AT&T Inc. $T Stock: State Street Corp Reduces Stake
- Summary: AT&T Inc. $T Stock: State Street Corp Reduces Stake
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxNa2x0TTJSTEl4VHh0c00xLWpQaGhWdkUzdmZucDkyR3ZtTldxYVp4VUY2b0V3X1pkUXE3UXQyNWZieW0wcHR0WTNUR3NRY2FwVFhBclhLaExnTVBQUThIWllEWUF3ZGlIR19taGd0R1NGMUZ5OEpJTnl6dXBlOXlqQUtCUVZ2aDVwUi1YRnE5SzNhZmJ6cm54S0twLTNpREJRSDlGZk5KdE5sbVRy?oc=5>

### Will Subscriber Growth Change AT&T Stock Narrative
- Summary: Subscriber growth trends may shift investor perception of AT&T’s future performance.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQU0JZZF9uZlhLcUVkRlN6WWh2RW8yemdjV1hFWk1Dem1zVjZ3TVRYU3g3RGhENkhjU2dyb2h6SFN2TV9vSHhaa1FuMVd5RlJsN095Q3JjdE1oekFna21Ka0JPTUZJWURQTGFXbDd2eklmMHJtV2NSVEtacWRwSzVmYmlhVGx2TFNHYlNpS3oxQkN0RHYxMEQtbGxVT3I5QQ?oc=5>

### What Could Surprise AT&T Stock Investors On The Upside?
- Summary: Potential upside factors could positively influence AT&T stock, though specifics remain unclear.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQME9kTmY2N0haSHE2RXhlWFN0bjk0OVp6RWhvbjAtSVFBd21lVVBGTGNIaVJwLTFkQ2FhemVQWU9mbWl2dm1TTmN4UmlfOGFZN1VXWU9yb2ZURUNVbmRjc1FtejNrRXVNb191ck9VYWotRW5tNXNNUV96SENQeHpIRVYtZlVra29yTzRYQ3VjZEkzcWl4a1JqclRLVjlFNjg2OFp0anhOVG1ZeEc1dHpUXw?oc=5>

### Clean Execution Lifted AT&T (T) in Q3
- Summary: AT&T’s Q3 performance improved due to efficient execution.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNOG8zdFF2YjExaGFJamFKLUJ0MmQ3SzJLeW8tUnFwOThVREh4NzllWWhuQmtUU05MakRIWkVtRDl0VmVpSnotbkczaC1FcE5CdGFlSGIxNndkN0JDcFlaSUhHeno3U1M4RExJTkZUVFE1VVZ1NDh1YVg0RVdqZjU3X3lXakN0cTByQlhFNl84bWRqN1ZlZ1E?oc=5>

### AT&T and U.S. Soccer Extend Longstanding Relationship to Continue Shaping the Future of Soccer in America
- Summary: AT&T renewed partnership with U.S. Soccer.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxPSnJNQU9mcXdGbjRpNE5oUEQ2b2JRMjRPTmVHdHBnSVRPWEZHcDJUMkp2Mk13OXExeHFPWWIwTGRkT1ZHQ1FZWUZLTFdPTDR4OGtUd1RrSlJRaTl0bmFSQkF0VHFib29JMkdIeGpOQk54cjhJSXgxWU83OENhamI1Mk1VdTZXNG9JMXhoZzlla0ZCbzEzMWlCVVpzSlJaLVk2MDM1U1hLQTVTN0N1NGpYT1l0VQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **T** | **12.24** | **1.45** | **7.44** | **5.30** | **154,130,513,920.00 USD** | **-6.43** |
| VZ | 12.03 | 1.84 | 7.44 | 1.50 | 195,459,252,224.00 USD | 25.09 |
| TMUS | 16.13 | 3.16 | 8.22 | 7.40 | 177,216,307,200.00 USD | -17.61 |
| BCE | 11.97 | 1.39 | 7.44 | 2.20 | 20,646,121,472.00 USD | 1.12 |

Peers fetched as_of: 2026-11-24; T reuses existing data (market data as_of: 2026-11-24); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

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
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 32,322,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 891,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/732717/000073271726000372/t-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimwFBVV95cUxQX2dsLUV0TnpEdGFaTTUtb1d1RGVSdWV3ZzEyVzFURG1SWGlINmtCOWRYMVZnOV9od1JybXBjbkp1M3hkd0ZybVJxSWx1Q0ZPX0ZXR1pTQjZ2UGEwNkJwczhuNzFja2REM0RGVnhvUkl3UUlqaHNEay1EZlJVdHpBa1ZkWFRMM0piWUpNa3FvZFlwX1hSNldZOEFOOA?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxQTjVzSkJvanJ1TG1iTEp6TGZUdHJ5U2ZNVmgtZjlRVGlKVkdpNWdzYzlhOFY0UGsxamhCa1VOOElzbXVWMkZLNnhOYkxRV1RWU3NxR0F3TVUtOGNieFdfN1hGX0dXRGZxUHlzem1HQUJiWkhiVVN5N1dYMzFsR040VmJaa2lWcWx1YTBCQlMyZmVrUTRSd19HZHk3c212TXhEbHBvZ01IcnBkNUd2LWFiRWlSM1pMblh0RXVxUzJwRkM?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxNa2x0TTJSTEl4VHh0c00xLWpQaGhWdkUzdmZucDkyR3ZtTldxYVp4VUY2b0V3X1pkUXE3UXQyNWZieW0wcHR0WTNUR3NRY2FwVFhBclhLaExnTVBQUThIWllEWUF3ZGlIR19taGd0R1NGMUZ5OEpJTnl6dXBlOXlqQUtCUVZ2aDVwUi1YRnE5SzNhZmJ6cm54S0twLTNpREJRSDlGZk5KdE5sbVRy?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQU0JZZF9uZlhLcUVkRlN6WWh2RW8yemdjV1hFWk1Dem1zVjZ3TVRYU3g3RGhENkhjU2dyb2h6SFN2TV9vSHhaa1FuMVd5RlJsN095Q3JjdE1oekFna21Ka0JPTUZJWURQTGFXbDd2eklmMHJtV2NSVEtacWRwSzVmYmlhVGx2TFNHYlNpS3oxQkN0RHYxMEQtbGxVT3I5QQ?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxQME9kTmY2N0haSHE2RXhlWFN0bjk0OVp6RWhvbjAtSVFBd21lVVBGTGNIaVJwLTFkQ2FhemVQWU9mbWl2dm1TTmN4UmlfOGFZN1VXWU9yb2ZURUNVbmRjc1FtejNrRXVNb191ck9VYWotRW5tNXNNUV96SENQeHpIRVYtZlVra29yTzRYQ3VjZEkzcWl4a1JqclRLVjlFNjg2OFp0anhOVG1ZeEc1dHpUXw?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNOG8zdFF2YjExaGFJamFKLUJ0MmQ3SzJLeW8tUnFwOThVREh4NzllWWhuQmtUU05MakRIWkVtRDl0VmVpSnotbkczaC1FcE5CdGFlSGIxNndkN0JDcFlaSUhHeno3U1M4RExJTkZUVFE1VVZ1NDh1YVg0RVdqZjU3X3lXakN0cTByQlhFNl84bWRqN1ZlZ1E?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxPSnJNQU9mcXdGbjRpNE5oUEQ2b2JRMjRPTmVHdHBnSVRPWEZHcDJUMkp2Mk13OXExeHFPWWIwTGRkT1ZHQ1FZWUZLTFdPTDR4OGtUd1RrSlJRaTl0bmFSQkF0VHFib29JMkdIeGpOQk54cjhJSXgxWU83OENhamI1Mk1VdTZXNG9JMXhoZzlla0ZCbzEzMWlCVVpzSlJaLVk2MDM1U1hLQTVTN0N1NGpYT1l0VQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
