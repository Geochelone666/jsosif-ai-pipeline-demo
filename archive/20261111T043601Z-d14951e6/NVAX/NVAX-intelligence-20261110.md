# NVAX Intelligence Report

- ticker: **NVAX**
- Report as_of: **2026-11-10**
- Market data as_of: **2026-11-10**
- Quant sources: https://finance.yahoo.com/quote/NVAX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVAX/key-statistics/
- AI analysis snapshot as_of: **2026-11-10**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-11T04:44:48.783179+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 15, 'rule': 7, 'ai': 6, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261110T055129Z-abd33250/NVAX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 15 unique headlines; 9 named publishers; 0 exact duplicates; 15 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-11-04

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 10.2000 |
| Return 1D (%) | -6.3361 |
| Return 1W (%) | 5.3719 |
| Return 1M (%) | -20.0000 |
| Return YTD (%) | 51.7857 |
| Return 1Y (%) | 43.4599 |
| Annualized volatility (%) | 72.7187 |
| Beta vs SPY | 2.1074 |
| Max drawdown (%) | -34.5844 |
| Sharpe (rf=0) | 0.8489 |
| Downside deviation (rf=0, %) | 42.3928 |
| Sortino (rf=0) | 1.4562 |
| Historical VaR 95% (1D, %) | 6.0209 |
| Historical ES 95% (1D, %) | 7.9017 |
| Correlation vs SPY | 0.3962 |
| Tracking error vs SPY (%) | 68.4631 |
| P/E (trailing) | N/A |
| P/B | -7.76 |
| EV/EBITDA | -24.39 |
| Revenue growth (%) | -3.00 |
| Forward P/E (estimate) | N/A |
| Gross margin (%) | 5.30 |
| Operating margin (%) | -41.26 |
| Return on equity (%) | N/A |
| Free cash flow yield (%) | 0.70 |
| MA50 | 10.6072 |
| Close vs MA50 (%) | -3.8389 |
| MA200 | 9.3400 |
| Close vs MA200 (%) | 9.2077 |
| RSI (14, Wilder) | 47.7045 |
| MACD (12,26) | -0.1314 |
| MACD signal (9) | -0.1299 |
| MACD histogram | -0.0015 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVAX': 279, 'SPY': 279}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 10.2000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -6.3361 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 5.3719 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -20.0000 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 51.7857 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 43.4599 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 72.7187 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 42.3928 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.4562 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 6.0209 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 7.9017 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3962 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 68.4631 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.1074 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -34.5844 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.8489 -> Modest risk-adjusted return.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 5.2970 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: -41.2620 -> No interpretation rule is available for this metric.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.6985 -> No interpretation rule is available for this metric.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 47.7045 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.0015 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -3.8389 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 9.2077 -> Clearly above the moving-average trend level.

## TAILWINDS

### Novavax boosts 2026 revenue forecast as licensing deals pay off
- Summary: Novavax boosts 2026 revenue forecast as licensing deals pay off
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQZy1jR0JEXzRyTkE0dTY2X09qMVNGWVVMd2h3V0p2WHJ6TEtoaUR5dC1PbzREbzVuNkFhX3h0ZWM3Y0s4bDlPRFFBZzdhR2JtWnJXaGN5NlY1bUdPcWtUWV9hYU5KcG9uM082N0JudTdqblRIVXRNZjZHak5VaklwTG1FVkdYSTNHR09OcHpVYW4xTkItMTROTWt3THN3UQ?oc=5>

### Novavax (NVAX) Reports Q3 Loss, Tops Revenue Estimates
- Summary: Novavax (NVAX) Reports Q3 Loss, Tops Revenue Estimates
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPWVE3dFZEaUI1TGVMMGJzaTRfQmtRaTViUHFsb0cxdVpUX2kzbUdfeU5qN2Zac2FnTGMyYWpwekVRdlg0TVloRHhwajN0WkFyR056WWdnUXVFQ1M0Q3RDRjQ5dTVvamlReWVWTGVHaDJxM0Y3c21MTWF1TGlfTEkzZ0RSUmZONzl6aFlXUFl2Sy0xdmM?oc=5>

### Novavax (NVAX) Shares Rise Premarket After Strong Q3 Revenue Bea
- Summary: Novavax (NVAX) Shares Rise Premarket After Strong Q3 Revenue Bea
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxOTFIyTXA0VWthUzdJYW9JZC1yd3RIUElraG40dkx4VThHNlN1bFJpMmJIOVIzUkl4UTNUWE5wS1ZHMTlVWHJLS3JOMzVfMG9Cc3BQNHVWSzRNQldiMl9MdGJrZERhNUI3WUpxb1ZGcUNJclJoX0RIcGpuYUZLUVF4M1Bhbl9hNWhWTk00SmtqTFhtZGsyMlc4aWV0U3hMSjFsang0OA?oc=5>

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

### Novavax’s (NASDAQ:NVAX) Q3 2026: strong sales, guides for strong full-year sales
- Summary: Company reports robust Q3 sales and upbeat full-year guidance, boosting investor confidence.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxQWlFhTU9Ec05EcVdlRVo1NzdlRnh0S2R4N2YtQzdxMXNfSHc5aEJNN0dKM3lSNHNNWWFZRlpfajRPTm5hbFViamtYQlM3SXJyTndaYmxicDdrUWhabUVVWW9ncVpzOGF4NmRNMkQ0WFllZmRZUTlVUFhCVW5WOFBiWFo4WFhNaWRGX1Q4VG43VzVISnowM2poWURqbERETC1QOXdMa2RFYXdQRktwLWJXS1NmTWhuRDhQc0dNV3ItSkQ0d0ZoZ2xfcFBja0s4QWplZjNF?oc=5>

### Novavax Stock Gets A Lift From Narrower Q3 Loss
- Summary: Stock gains after reporting a reduced Q3 loss, indicating improving profitability.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxQQVcyRW5Ya0s2M2ZsQmlrRGFPN1dhcVVfYy1ENzBra1lLWHZEUFhYVXpfcG0tNXNlLVlKNDZpQldXQjg1WnowOFp1TUF2MlQ4djYyTWpNMGFjb3d4SEpEeTVqNVRtVWhBX0hNSGJLNU5TaXlOS01RLWkxWXFvb2RPc2l3SFpsTEYyR19Yam5IcXFkU2JLMXd0OXVLRjFJcS1yN2FzeHRKN3FmU05PLS1URE83OGpOWlByUGdsN2ZCRGgzTnJ2SWNR0gHMAUFVX3lxTFBiR2toMWlVZU9ZSDV5eTdDa1BEY1ZLeEc3bHQxblpCaXd0bjVjVWt5OGxwaGlVcDgycjVtVXZSaklUYUhiVkVlZDJuOVUxLUt5WjQ0Y2hrQVVuam9kMXktR1NYcnJ6R1VNeXZxdTRLdWlqblI5LXpXQnkxTkFxQWozLWpyaFhtVm1ISVRCN2ViczhOb3B6MkhtSE4tQ1pUaW5iVjd0YWt5TzVWemF5WG1nX1M1N0RJeUdaZnJVZGc0QWJrQTZOTHZsdjYyUA?oc=5>

### A partner's flu-and-COVID vaccine trial triggered a $125 million payment to Novavax.
- Summary: Partner's trial generated a $125M payment, enhancing cash flow.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxNNmRFNlVLUURhQklvQjRtb0FNaHU5RUhHbm1pMGw4Z3dubHlIT2YzVU10NGprT1J5eXl3U1lLM2dtVnA2cWJsY1RqYUhvNTQ5MzVKYzNGODlmY2JSbER5cWVidzAwczI3anBybkdSUlFMbmtnckY1bG00am1CbXdsZHdIYnI2bG5qZXd4MnNfc3NaQjNpSGdBV1ZaUVZkS0JJVV9VQk4yNTdTMUJ0cExjc2FrSUNHQnBHT21zTnM5dDQ?oc=5>

### Novavax (NVAX) stock trades up, here is why
- Summary: Shares of Novavax rose, driven by positive market sentiment and recent corporate developments.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQY1BYNFRsZjVRcEZNd3JxSFZ6MVpYSk5jRGRzNmJNR1EwdDVoMWtSN0lvUU1WaHhXZFpybTBLLXJOOFRFMDNNaTNNaHg4SzRDVGx6bC02Sm1fZUwwRmJqeHhFcm1FdWlrZDV1R18tSkFEVDdEaHQ2UFhnVkVxSUNmS1JOMVRBdnZNR2tyNklxaGMtd29UYVNVeHVR?oc=5>

## RISKS

### Novavax, Inc. (NVAX) Is a Trending Stock: Facts to Know Before Betting on It
- Summary: General information about Novavax’s market status; no specific event disclosed.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxPS0U2d1FwYS04TUJPbDdheVpiWmJFUGVCSVp0Uk45Z3U5bkJYTzVSZUtrVUhRWEtaUENGOGlwYmRvYksyTG9CWHBnSFY2dEtBY0tVRXZYMUhxY2pmd295amFQdk4tOXdKRkc4QU5HX2JENDVsRFB0OXFDZkNUZFVnbFdUd0s5Y1U?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVAX** | **N/A** | **-7.76** | **-24.39** | **-3.00** | **1,683,091,840.00 USD** | **43.46** |
| MRNA | N/A | 14.82 | -56.39 | 29.20 | 101,491,073,024.00 USD | 913.05 |
| BNTX | N/A | 1.09 | -8.15 | -15.10 | 21,621,815,296.00 USD | -17.00 |
| GSK | 17.98 | 4.09 | 10.71 | 4.00 | 102,688,980,992.00 USD | 12.00 |

Peers fetched as_of: 2026-11-10; NVAX reuses existing data (market data as_of: 2026-11-10); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-05
- Next expected earnings: 2027-02-25 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-10

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

- https://news.google.com/rss/articles/CBMingFBVV95cUxQZy1jR0JEXzRyTkE0dTY2X09qMVNGWVVMd2h3V0p2WHJ6TEtoaUR5dC1PbzREbzVuNkFhX3h0ZWM3Y0s4bDlPRFFBZzdhR2JtWnJXaGN5NlY1bUdPcWtUWV9hYU5KcG9uM082N0JudTdqblRIVXRNZjZHak5VaklwTG1FVkdYSTNHR09OcHpVYW4xTkItMTROTWt3THN3UQ?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPWVE3dFZEaUI1TGVMMGJzaTRfQmtRaTViUHFsb0cxdVpUX2kzbUdfeU5qN2Zac2FnTGMyYWpwekVRdlg0TVloRHhwajN0WkFyR056WWdnUXVFQ1M0Q3RDRjQ5dTVvamlReWVWTGVHaDJxM0Y3c21MTWF1TGlfTEkzZ0RSUmZONzl6aFlXUFl2Sy0xdmM?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxOTFIyTXA0VWthUzdJYW9JZC1yd3RIUElraG40dkx4VThHNlN1bFJpMmJIOVIzUkl4UTNUWE5wS1ZHMTlVWHJLS3JOMzVfMG9Cc3BQNHVWSzRNQldiMl9MdGJrZERhNUI3WUpxb1ZGcUNJclJoX0RIcGpuYUZLUVF4M1Bhbl9hNWhWTk00SmtqTFhtZGsyMlc4aWV0U3hMSjFsang0OA?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNYW5lcDFjeHhuUGdORFlpZDRDWVdZeERNX3ZkMTdjVWg2bUlXT3J3bkZXWXZTdFR1OFZiYl9kZU1aNWJFdDNYU2dCSDV6U2RIOXdBc3Fnc0lpSDhwY3VVNGxLTXlKUWxGQmdibmp0ZEpVbHdNeHpEcEZ4YXFpSmFPaU9zSGhlYUNZWE1ISEQ1MHFlOWpHdEl3TlQ5TlI?oc=5
- https://news.google.com/rss/articles/CBMihgFBVV95cUxPNEc2aHVnY3QzRXZRMXZ6QVZCcXRhQklyNDJZV09uWUxweTlobnhQczlaYjJwLXZ2eml0azgxVy1lVTRhVkpGTTlLdVo5aW1wUnJDR29RbFotaEU3SzNEc1UzeXVqTkN1NkNuRVF3Z2hpd0FNMlI3VDlPM1VPMGJDOFBEX3Judw?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxPanIwazVBaGxjVmFBYnZudUl6VUJXNEpCREZacHpFdHRpeWVnN3JYM3N6T1F2OTF3Tk1nLURWaW9yc05sby1XRWxKcEZ0WS1XR0lmNTV0bHFPTmV0TFFmeEFId2RSWEV0eC15LWxXVktpbWtZVjRMVHdwT2VNVXdFaFFmWHBUTFFKRUNqV3lfQW4?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxPVmNjaUVfTHlyUWR2aWVwcHYyM2lNeUFnU1RLWDUwdDE0Q2d6NV9hRk96Zl8yT3pUMWlMbTV0dUhMOHJaSzYydEZZb3FvTzUzdkFpQVYyQmRTZkxsVUw3eDVtTkZEUXZfc0ROMkdrT2d0VnB3U1VxNWZpSDgzZFA2dWctSUtPbE0?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxQUko2SUNaM0JJRWN5dHNKVi1lcXZMZVdaeE5EVjdZOHVSQmhpTVZUNXZzSWdocFI2dkZZb2R5S3BNYVVXOUsxMkMwLVBpa1JhVW9sdktqdTVYaGJyUTBzd1ZpWlVLZXR3WFdMbzRHSUtyVm1PcEJCZTBLTkFCbWRHd3RhYnBlOG1jeUtrUkhfUVhrR00xeGZrM24wUEZXQXpIWGYzelk4c0RzYVotX0k2eXdB?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxQWlFhTU9Ec05EcVdlRVo1NzdlRnh0S2R4N2YtQzdxMXNfSHc5aEJNN0dKM3lSNHNNWWFZRlpfajRPTm5hbFViamtYQlM3SXJyTndaYmxicDdrUWhabUVVWW9ncVpzOGF4NmRNMkQ0WFllZmRZUTlVUFhCVW5WOFBiWFo4WFhNaWRGX1Q4VG43VzVISnowM2poWURqbERETC1QOXdMa2RFYXdQRktwLWJXS1NmTWhuRDhQc0dNV3ItSkQ0d0ZoZ2xfcFBja0s4QWplZjNF?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxQQVcyRW5Ya0s2M2ZsQmlrRGFPN1dhcVVfYy1ENzBra1lLWHZEUFhYVXpfcG0tNXNlLVlKNDZpQldXQjg1WnowOFp1TUF2MlQ4djYyTWpNMGFjb3d4SEpEeTVqNVRtVWhBX0hNSGJLNU5TaXlOS01RLWkxWXFvb2RPc2l3SFpsTEYyR19Yam5IcXFkU2JLMXd0OXVLRjFJcS1yN2FzeHRKN3FmU05PLS1URE83OGpOWlByUGdsN2ZCRGgzTnJ2SWNR0gHMAUFVX3lxTFBiR2toMWlVZU9ZSDV5eTdDa1BEY1ZLeEc3bHQxblpCaXd0bjVjVWt5OGxwaGlVcDgycjVtVXZSaklUYUhiVkVlZDJuOVUxLUt5WjQ0Y2hrQVVuam9kMXktR1NYcnJ6R1VNeXZxdTRLdWlqblI5LXpXQnkxTkFxQWozLWpyaFhtVm1ISVRCN2ViczhOb3B6MkhtSE4tQ1pUaW5iVjd0YWt5TzVWemF5WG1nX1M1N0RJeUdaZnJVZGc0QWJrQTZOTHZsdjYyUA?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxNNmRFNlVLUURhQklvQjRtb0FNaHU5RUhHbm1pMGw4Z3dubHlIT2YzVU10NGprT1J5eXl3U1lLM2dtVnA2cWJsY1RqYUhvNTQ5MzVKYzNGODlmY2JSbER5cWVidzAwczI3anBybkdSUlFMbmtnckY1bG00am1CbXdsZHdIYnI2bG5qZXd4MnNfc3NaQjNpSGdBV1ZaUVZkS0JJVV9VQk4yNTdTMUJ0cExjc2FrSUNHQnBHT21zTnM5dDQ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQY1BYNFRsZjVRcEZNd3JxSFZ6MVpYSk5jRGRzNmJNR1EwdDVoMWtSN0lvUU1WaHhXZFpybTBLLXJOOFRFMDNNaTNNaHg4SzRDVGx6bC02Sm1fZUwwRmJqeHhFcm1FdWlrZDV1R18tSkFEVDdEaHQ2UFhnVkVxSUNmS1JOMVRBdnZNR2tyNklxaGMtd29UYVNVeHVR?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxPS0U2d1FwYS04TUJPbDdheVpiWmJFUGVCSVp0Uk45Z3U5bkJYTzVSZUtrVUhRWEtaUENGOGlwYmRvYksyTG9CWHBnSFY2dEtBY0tVRXZYMUhxY2pmd295amFQdk4tOXdKRkc4QU5HX2JENDVsRFB0OXFDZkNUZFVnbFdUd0s5Y1U?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
