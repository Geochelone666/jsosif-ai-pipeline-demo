# NVAX Intelligence Report

- ticker: **NVAX**
- Report as_of: **2026-11-11**
- Market data as_of: **2026-11-11**
- Quant sources: https://finance.yahoo.com/quote/NVAX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVAX/key-statistics/
- AI analysis snapshot as_of: **2026-11-11**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-12T05:44:11.035391+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 11, 'rule': 4, 'ai': 5, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261111T043601Z-d14951e6/NVAX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 11 unique headlines; 6 named publishers; 0 exact duplicates; 11 HTTPS source links; largest publisher share 45.45%; oldest publication 2026-11-04

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 9.9800 |
| Return 1D (%) | -2.1569 |
| Return 1W (%) | -6.2911 |
| Return 1M (%) | -21.7255 |
| Return YTD (%) | 48.5119 |
| Return 1Y (%) | 34.1398 |
| Annualized volatility (%) | 72.6234 |
| Beta vs SPY | 2.0691 |
| Max drawdown (%) | -34.5844 |
| Sharpe (rf=0) | 0.7560 |
| Downside deviation (rf=0, %) | 42.4479 |
| Sortino (rf=0) | 1.2935 |
| Historical VaR 95% (1D, %) | 6.0209 |
| Historical ES 95% (1D, %) | 7.9017 |
| Correlation vs SPY | 0.3911 |
| Tracking error vs SPY (%) | 68.4299 |
| P/E (trailing) | N/A |
| P/B | -7.60 |
| EV/EBITDA | -23.74 |
| Revenue growth (%) | -3.00 |
| Forward P/E (estimate) | N/A |
| Gross margin (%) | 5.30 |
| Operating margin (%) | -16.98 |
| Return on equity (%) | N/A |
| Free cash flow yield (%) | 0.71 |
| MA50 | 10.6044 |
| Close vs MA50 (%) | -5.8881 |
| MA200 | 9.3408 |
| Close vs MA200 (%) | 6.8431 |
| RSI (14, Wilder) | 46.2006 |
| MACD (12,26) | -0.1535 |
| MACD signal (9) | -0.1346 |
| MACD histogram | -0.0189 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVAX': 280, 'SPY': 280}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 9.9800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.1569 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -6.2911 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -21.7255 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 48.5119 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 34.1398 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 72.6234 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 42.4479 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.2935 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 6.0209 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 7.9017 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3911 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 68.4299 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.0691 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -34.5844 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.7560 -> Modest risk-adjusted return.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 5.2970 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: -16.9770 -> No interpretation rule is available for this metric.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.7139 -> No interpretation rule is available for this metric.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 46.2006 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.0189 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -5.8881 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 6.8431 -> Clearly above the moving-average trend level.

## TAILWINDS

### Novavax Raises FY26 Revenue Outlook By 50% – Retail Says Licensing Deals Could Create ‘Tremendous Financial Leverage’
- Summary: Novavax lifts FY26 revenue outlook by 50%, citing licensing deals for financial leverage.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNYW5lcDFjeHhuUGdORFlpZDRDWVdZeERNX3ZkMTdjVWg2bUlXT3J3bkZXWXZTdFR1OFZiYl9kZU1aNWJFdDNYU2dCSDV6U2RIOXdBc3Fnc0lpSDhwY3VVNGxLTXlKUWxGQmdibmp0ZEpVbHdNeHpEcEZ4YXFpSmFPaU9zSGhlYUNZWE1ISEQ1MHFlOWpHdEl3TlQ5TlI?oc=5>

## HEADWINDS

### Novavax stock falls despite Q3 beat (update) (NVAX:NASDAQ)
- Summary: Novavax stock falls despite Q3 beat (update) (NVAX:NASDAQ)
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihgFBVV95cUxPNEc2aHVnY3QzRXZRMXZ6QVZCcXRhQklyNDJZV09uWUxweTlobnhQczlaYjJwLXZ2eml0azgxVy1lVTRhVkpGTTlLdVo5aW1wUnJDR29RbFotaEU3SzNEc1UzeXVqTkN1NkNuRVF3Z2hpd0FNMlI3VDlPM1VPMGJDOFBEX3Judw?oc=5>

### NVAX Stock Falls 8% Despite Q3 Earnings & Sales Beat, Costs Decline
- Summary: NVAX Stock Falls 8% Despite Q3 Earnings & Sales Beat, Costs Decline
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxPanIwazVBaGxjVmFBYnZudUl6VUJXNEpCREZacHpFdHRpeWVnN3JYM3N6T1F2OTF3Tk1nLURWaW9yc05sby1XRWxKcEZ0WS1XR0lmNTV0bHFPTmV0TFFmeEFId2RSWEV0eC15LWxXVktpbWtZVjRMVHdwT2VNVXdFaFFmWHBUTFFKRUNqV3lfQW4?oc=5>

## CATALYSTS

### NOVAVAX ($NVAX) Releases Q3 2026 Earnings
- Summary: NOVAVAX ($NVAX) Releases Q3 2026 Earnings
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxPVmNjaUVfTHlyUWR2aWVwcHYyM2lNeUFnU1RLWDUwdDE0Q2d6NV9hRk96Zl8yT3pUMWlMbTV0dUhMOHJaSzYydEZZb3FvTzUzdkFpQVYyQmRTZkxsVUw3eDVtTkZEUXZfc0ROMkdrT2d0VnB3U1VxNWZpSDgzZFA2dWctSUtPbE0?oc=5>

### Novavax (NVAX) reports earnings tomorrow: what to expect
- Summary: Novavax (NVAX) reports earnings tomorrow: what to expect
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxQUko2SUNaM0JJRWN5dHNKVi1lcXZMZVdaeE5EVjdZOHVSQmhpTVZUNXZzSWdocFI2dkZZb2R5S3BNYVVXOUsxMkMwLVBpa1JhVW9sdktqdTVYaGJyUTBzd1ZpWlVLZXR3WFdMbzRHSUtyVm1PcEJCZTBLTkFCbWRHd3RhYnBlOG1jeUtrUkhfUVhrR00xeGZrM24wUEZXQXpIWGYzelk4c0RzYVotX0k2eXdB?oc=5>

### Novavax (NVAX) stock trades up, here is why
- Summary: Shares of Novavax rose, driven by positive market sentiment and recent corporate developments.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQY1BYNFRsZjVRcEZNd3JxSFZ6MVpYSk5jRGRzNmJNR1EwdDVoMWtSN0lvUU1WaHhXZFpybTBLLXJOOFRFMDNNaTNNaHg4SzRDVGx6bC02Sm1fZUwwRmJqeHhFcm1FdWlrZDV1R18tSkFEVDdEaHQ2UFhnVkVxSUNmS1JOMVRBdnZNR2tyNklxaGMtd29UYVNVeHVR?oc=5>

### Novavax Stock Gets A Lift From Narrower Q3 Loss
- Summary: Stock gains after reporting a reduced Q3 loss, indicating improving profitability.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxQQVcyRW5Ya0s2M2ZsQmlrRGFPN1dhcVVfYy1ENzBra1lLWHZEUFhYVXpfcG0tNXNlLVlKNDZpQldXQjg1WnowOFp1TUF2MlQ4djYyTWpNMGFjb3d4SEpEeTVqNVRtVWhBX0hNSGJLNU5TaXlOS01RLWkxWXFvb2RPc2l3SFpsTEYyR19Yam5IcXFkU2JLMXd0OXVLRjFJcS1yN2FzeHRKN3FmU05PLS1URE83OGpOWlByUGdsN2ZCRGgzTnJ2SWNR0gHMAUFVX3lxTFBiR2toMWlVZU9ZSDV5eTdDa1BEY1ZLeEc3bHQxblpCaXd0bjVjVWt5OGxwaGlVcDgycjVtVXZSaklUYUhiVkVlZDJuOVUxLUt5WjQ0Y2hrQVVuam9kMXktR1NYcnJ6R1VNeXZxdTRLdWlqblI5LXpXQnkxTkFxQWozLWpyaFhtVm1ISVRCN2ViczhOb3B6MkhtSE4tQ1pUaW5iVjd0YWt5TzVWemF5WG1nX1M1N0RJeUdaZnJVZGc0QWJrQTZOTHZsdjYyUA?oc=5>

### A partner's flu-and-COVID vaccine trial triggered a $125 million payment to Novavax.
- Summary: Partner's trial generated a $125M payment, enhancing cash flow.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxNNmRFNlVLUURhQklvQjRtb0FNaHU5RUhHbm1pMGw4Z3dubHlIT2YzVU10NGprT1J5eXl3U1lLM2dtVnA2cWJsY1RqYUhvNTQ5MzVKYzNGODlmY2JSbER5cWVidzAwczI3anBybkdSUlFMbmtnckY1bG00am1CbXdsZHdIYnI2bG5qZXd4MnNfc3NaQjNpSGdBV1ZaUVZkS0JJVV9VQk4yNTdTMUJ0cExjc2FrSUNHQnBHT21zTnM5dDQ?oc=5>

### Novavax Inc (NVAX) (Q3 2026) Earnings Call Highlights: Sanofi Milestone Lifts Revenue Outlook ...
- Summary: Q3 2026 earnings call highlighted a Sanofi milestone that boosted revenue outlook.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxONnZJTDMzSkdIeW9sUnNnN1E0Tk9UaHJpV1VJMHZSbktpUFJuR2JSczhpVXlWTmd5aUktWGg5TEZwdXRiMjFkdGtydHZFbmpSSEh3U3pBbnR6dXlqVmZCYzJGMnZPUjNBTVVqSk83c2dBU1ZKbTJNd3lZR1EtZ0k2OUNZOHAxdVJJX2NXMWh3?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVAX** | **N/A** | **-7.60** | **-23.74** | **-3.00** | **1,646,789,888.00 USD** | **34.14** |
| MRNA | N/A | 14.70 | -55.91 | 29.20 | 100,625,186,816.00 USD | 841.65 |
| BNTX | N/A | 1.09 | -8.26 | -15.10 | 21,730,904,064.00 USD | -19.33 |
| GSK | 17.63 | 4.04 | 10.61 | 4.00 | 101,426,159,616.00 USD | 8.23 |

Peers fetched as_of: 2026-11-11; NVAX reuses existing data (market data as_of: 2026-11-11); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-05
- Next expected earnings: 2027-02-25 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-11

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-05
- Revenue (latest available single quarter): 68,298,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): -31,376,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1000694/000100069426000022/nvax-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMinAFBVV95cUxNYW5lcDFjeHhuUGdORFlpZDRDWVdZeERNX3ZkMTdjVWg2bUlXT3J3bkZXWXZTdFR1OFZiYl9kZU1aNWJFdDNYU2dCSDV6U2RIOXdBc3Fnc0lpSDhwY3VVNGxLTXlKUWxGQmdibmp0ZEpVbHdNeHpEcEZ4YXFpSmFPaU9zSGhlYUNZWE1ISEQ1MHFlOWpHdEl3TlQ5TlI?oc=5
- https://news.google.com/rss/articles/CBMihgFBVV95cUxPNEc2aHVnY3QzRXZRMXZ6QVZCcXRhQklyNDJZV09uWUxweTlobnhQczlaYjJwLXZ2eml0azgxVy1lVTRhVkpGTTlLdVo5aW1wUnJDR29RbFotaEU3SzNEc1UzeXVqTkN1NkNuRVF3Z2hpd0FNMlI3VDlPM1VPMGJDOFBEX3Judw?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxPanIwazVBaGxjVmFBYnZudUl6VUJXNEpCREZacHpFdHRpeWVnN3JYM3N6T1F2OTF3Tk1nLURWaW9yc05sby1XRWxKcEZ0WS1XR0lmNTV0bHFPTmV0TFFmeEFId2RSWEV0eC15LWxXVktpbWtZVjRMVHdwT2VNVXdFaFFmWHBUTFFKRUNqV3lfQW4?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxPVmNjaUVfTHlyUWR2aWVwcHYyM2lNeUFnU1RLWDUwdDE0Q2d6NV9hRk96Zl8yT3pUMWlMbTV0dUhMOHJaSzYydEZZb3FvTzUzdkFpQVYyQmRTZkxsVUw3eDVtTkZEUXZfc0ROMkdrT2d0VnB3U1VxNWZpSDgzZFA2dWctSUtPbE0?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxQUko2SUNaM0JJRWN5dHNKVi1lcXZMZVdaeE5EVjdZOHVSQmhpTVZUNXZzSWdocFI2dkZZb2R5S3BNYVVXOUsxMkMwLVBpa1JhVW9sdktqdTVYaGJyUTBzd1ZpWlVLZXR3WFdMbzRHSUtyVm1PcEJCZTBLTkFCbWRHd3RhYnBlOG1jeUtrUkhfUVhrR00xeGZrM24wUEZXQXpIWGYzelk4c0RzYVotX0k2eXdB?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQY1BYNFRsZjVRcEZNd3JxSFZ6MVpYSk5jRGRzNmJNR1EwdDVoMWtSN0lvUU1WaHhXZFpybTBLLXJOOFRFMDNNaTNNaHg4SzRDVGx6bC02Sm1fZUwwRmJqeHhFcm1FdWlrZDV1R18tSkFEVDdEaHQ2UFhnVkVxSUNmS1JOMVRBdnZNR2tyNklxaGMtd29UYVNVeHVR?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxQQVcyRW5Ya0s2M2ZsQmlrRGFPN1dhcVVfYy1ENzBra1lLWHZEUFhYVXpfcG0tNXNlLVlKNDZpQldXQjg1WnowOFp1TUF2MlQ4djYyTWpNMGFjb3d4SEpEeTVqNVRtVWhBX0hNSGJLNU5TaXlOS01RLWkxWXFvb2RPc2l3SFpsTEYyR19Yam5IcXFkU2JLMXd0OXVLRjFJcS1yN2FzeHRKN3FmU05PLS1URE83OGpOWlByUGdsN2ZCRGgzTnJ2SWNR0gHMAUFVX3lxTFBiR2toMWlVZU9ZSDV5eTdDa1BEY1ZLeEc3bHQxblpCaXd0bjVjVWt5OGxwaGlVcDgycjVtVXZSaklUYUhiVkVlZDJuOVUxLUt5WjQ0Y2hrQVVuam9kMXktR1NYcnJ6R1VNeXZxdTRLdWlqblI5LXpXQnkxTkFxQWozLWpyaFhtVm1ISVRCN2ViczhOb3B6MkhtSE4tQ1pUaW5iVjd0YWt5TzVWemF5WG1nX1M1N0RJeUdaZnJVZGc0QWJrQTZOTHZsdjYyUA?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxNNmRFNlVLUURhQklvQjRtb0FNaHU5RUhHbm1pMGw4Z3dubHlIT2YzVU10NGprT1J5eXl3U1lLM2dtVnA2cWJsY1RqYUhvNTQ5MzVKYzNGODlmY2JSbER5cWVidzAwczI3anBybkdSUlFMbmtnckY1bG00am1CbXdsZHdIYnI2bG5qZXd4MnNfc3NaQjNpSGdBV1ZaUVZkS0JJVV9VQk4yNTdTMUJ0cExjc2FrSUNHQnBHT21zTnM5dDQ?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxONnZJTDMzSkdIeW9sUnNnN1E0Tk9UaHJpV1VJMHZSbktpUFJuR2JSczhpVXlWTmd5aUktWGg5TEZwdXRiMjFkdGtydHZFbmpSSEh3U3pBbnR6dXlqVmZCYzJGMnZPUjNBTVVqSk83c2dBU1ZKbTJNd3lZR1EtZ0k2OUNZOHAxdVJJX2NXMWh3?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
