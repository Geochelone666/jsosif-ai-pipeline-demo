# NVAX Intelligence Report

- ticker: **NVAX**
- Report as_of: **2026-11-05**
- Market data as_of: **2026-11-05**
- Quant sources: https://finance.yahoo.com/quote/NVAX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVAX/key-statistics/
- AI analysis snapshot as_of: **2026-11-05**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-06T05:05:18.304317+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 9, 'rule': 5, 'ai': 3, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261105T045846Z-bde0a1fe/NVAX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 9 unique headlines; 5 named publishers; 0 exact duplicates; 9 HTTPS source links; largest publisher share 44.44%; oldest publication 2026-10-29

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 9.7800 |
| Return 1D (%) | -8.1690 |
| Return 1W (%) | -6.5903 |
| Return 1M (%) | -22.1338 |
| Return YTD (%) | 45.5357 |
| Return 1Y (%) | 27.1781 |
| Annualized volatility (%) | 71.9178 |
| Beta vs SPY | 2.0619 |
| Max drawdown (%) | -34.5844 |
| Sharpe (rf=0) | 0.6822 |
| Downside deviation (rf=0, %) | 42.2163 |
| Sortino (rf=0) | 1.1621 |
| Historical VaR 95% (1D, %) | 5.9784 |
| Historical ES 95% (1D, %) | 7.8765 |
| Correlation vs SPY | 0.3897 |
| Tracking error vs SPY (%) | 67.7860 |
| P/E (trailing) | N/A |
| P/B | -8.45 |
| EV/EBITDA | -11.73 |
| Revenue growth (%) | -76.30 |
| Forward P/E (estimate) | N/A |
| Gross margin (%) | -2.56 |
| Operating margin (%) | -89.61 |
| Return on equity (%) | N/A |
| Free cash flow yield (%) | 9.51 |
| MA50 | 10.5234 |
| Close vs MA50 (%) | -7.0643 |
| MA200 | 9.3234 |
| Close vs MA200 (%) | 4.8974 |
| RSI (14, Wilder) | 44.5898 |
| MACD (12,26) | -0.2435 |
| MACD signal (9) | -0.1181 |
| MACD histogram | -0.1254 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVAX': 276, 'SPY': 276}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 9.7800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -8.1690 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -6.5903 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -22.1338 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 45.5357 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 27.1781 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 71.9178 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 42.2163 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.1621 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 5.9784 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 7.8765 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3897 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 67.7860 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.0619 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -34.5844 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.6822 -> Modest risk-adjusted return.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: -2.5580 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: -89.6080 -> No interpretation rule is available for this metric.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 9.5089 -> No interpretation rule is available for this metric.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 44.5898 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.1254 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -7.0643 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 4.8974 -> Slightly above the moving-average trend level.

## TAILWINDS

### Novavax (NVAX) Shares Rise Premarket After Strong Q3 Revenue Bea
- Summary: Novavax (NVAX) Shares Rise Premarket After Strong Q3 Revenue Bea
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxOTFIyTXA0VWthUzdJYW9JZC1yd3RIUElraG40dkx4VThHNlN1bFJpMmJIOVIzUkl4UTNUWE5wS1ZHMTlVWHJLS3JOMzVfMG9Cc3BQNHVWSzRNQldiMl9MdGJrZERhNUI3WUpxb1ZGcUNJclJoX0RIcGpuYUZLUVF4M1Bhbl9hNWhWTk00SmtqTFhtZGsyMlc4aWV0U3hMSjFsang0OA?oc=5>

### Novavax (NVAX) Reports Q3 Loss, Tops Revenue Estimates
- Summary: Novavax (NVAX) Reports Q3 Loss, Tops Revenue Estimates
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPWVE3dFZEaUI1TGVMMGJzaTRfQmtRaTViUHFsb0cxdVpUX2kzbUdfeU5qN2Zac2FnTGMyYWpwekVRdlg0TVloRHhwajN0WkFyR056WWdnUXVFQ1M0Q3RDRjQ5dTVvamlReWVWTGVHaDJxM0Y3c21MTWF1TGlfTEkzZ0RSUmZONzl6aFlXUFl2Sy0xdmM?oc=5>

### Novavax stock gains after Q3 beat, guidance hike (NVAX:NASDAQ)
- Summary: Novavax stock gains after Q3 beat, guidance hike (NVAX:NASDAQ)
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNZFl1LVN6VnE3eVY2bTQ4M0kxSm5pUkczVERka0FhTkh4RmRMVmh0U05fYTh1OWNuX2VIZ3A5S0x2aXFxdXlNVFVNRXZNZWdYb3FaTlM0R3lFaTJ0QWw0MEFxcHcta2ZKN1RhRUZOX2V5cGJFeFIzaVluNGJUMzQxRzJsdW04R0RuLUZwOHh3S0NnWU5OTjA4U2tuSXhqcXM?oc=5>

## HEADWINDS

### Novavax stock falls despite Q3 beat (update) (NVAX:NASDAQ)
- Summary: Novavax stock falls despite Q3 beat (update) (NVAX:NASDAQ)
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihgFBVV95cUxPNEc2aHVnY3QzRXZRMXZ6QVZCcXRhQklyNDJZV09uWUxweTlobnhQczlaYjJwLXZ2eml0azgxVy1lVTRhVkpGTTlLdVo5aW1wUnJDR29RbFotaEU3SzNEc1UzeXVqTkN1NkNuRVF3Z2hpd0FNMlI3VDlPM1VPMGJDOFBEX3Judw?oc=5>

## CATALYSTS

### NOVAVAX ($NVAX) Releases Q3 2026 Earnings
- Summary: NOVAVAX ($NVAX) Releases Q3 2026 Earnings
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxPVmNjaUVfTHlyUWR2aWVwcHYyM2lNeUFnU1RLWDUwdDE0Q2d6NV9hRk96Zl8yT3pUMWlMbTV0dUhMOHJaSzYydEZZb3FvTzUzdkFpQVYyQmRTZkxsVUw3eDVtTkZEUXZfc0ROMkdrT2d0VnB3U1VxNWZpSDgzZFA2dWctSUtPbE0?oc=5>

### Novavax’s (NASDAQ:NVAX) Q3 2026: strong sales, guides for strong full-year sales
- Summary: Q3 2026 results show strong sales; company provides optimistic full-year guidance.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxOZDBVNU5kSzFLQVQzaE1keXhLNjVkeWRxRlNiV29RN0dlVXhDcTRZdGxVNXp6cFE0eGU1dWlFZmJtXzhUbENYTXRWdm9rOTI3cTNMQ1YwZGc2cjBidklnX3gxMk1GVVZxcURvc1poRENPWFVtTUlsazFaeGswaTRqX2tocW42eHpDMm5iWG9OdHQtdw?oc=5>

### Novavax Raises FY26 Revenue Outlook By 50% – Retail Says Licensing Deals Could Create ‘Tremendous Financial Leverage’
- Summary: FY26 revenue outlook increased 50% due to licensing deals, boosting financial leverage.
- Date: 2026-11-05 | Impact: high | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNYW5lcDFjeHhuUGdORFlpZDRDWVdZeERNX3ZkMTdjVWg2bUlXT3J3bkZXWXZTdFR1OFZiYl9kZU1aNWJFdDNYU2dCSDV6U2RIOXdBc3Fnc0lpSDhwY3VVNGxLTXlKUWxGQmdibmp0ZEpVbHdNeHpEcEZ4YXFpSmFPaU9zSGhlYUNZWE1ISEQ1MHFlOWpHdEl3TlQ5TlI?oc=5>

### A partner's flu-and-COVID vaccine trial triggered a $125 million payment to Novavax.
- Summary: Partner's trial generated a $125M payment, enhancing cash flow.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxNNmRFNlVLUURhQklvQjRtb0FNaHU5RUhHbm1pMGw4Z3dubHlIT2YzVU10NGprT1J5eXl3U1lLM2dtVnA2cWJsY1RqYUhvNTQ5MzVKYzNGODlmY2JSbER5cWVidzAwczI3anBybkdSUlFMbmtnckY1bG00am1CbXdsZHdIYnI2bG5qZXd4MnNfc3NaQjNpSGdBV1ZaUVZkS0JJVV9VQk4yNTdTMUJ0cExjc2FrSUNHQnBHT21zTnM5dDQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVAX** | **N/A** | **-8.45** | **-11.73** | **-76.30** | **1,613,169,152.00 USD** | **27.18** |
| MRNA | N/A | 14.25 | -42.16 | 2.10 | 96,399,507,456.00 USD | 924.87 |
| BNTX | N/A | 1.07 | -11.39 | -15.10 | 21,287,112,704.00 USD | -16.99 |
| GSK | 17.56 | 4.02 | 10.97 | 4.00 | 101,045,313,536.00 USD | 11.79 |

Peers fetched as_of: 2026-11-05; NVAX reuses existing data (market data as_of: 2026-11-05); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-05
- Next expected earnings: N/A (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-05

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMipAFBVV95cUxOTFIyTXA0VWthUzdJYW9JZC1yd3RIUElraG40dkx4VThHNlN1bFJpMmJIOVIzUkl4UTNUWE5wS1ZHMTlVWHJLS3JOMzVfMG9Cc3BQNHVWSzRNQldiMl9MdGJrZERhNUI3WUpxb1ZGcUNJclJoX0RIcGpuYUZLUVF4M1Bhbl9hNWhWTk00SmtqTFhtZGsyMlc4aWV0U3hMSjFsang0OA?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPWVE3dFZEaUI1TGVMMGJzaTRfQmtRaTViUHFsb0cxdVpUX2kzbUdfeU5qN2Zac2FnTGMyYWpwekVRdlg0TVloRHhwajN0WkFyR056WWdnUXVFQ1M0Q3RDRjQ5dTVvamlReWVWTGVHaDJxM0Y3c21MTWF1TGlfTEkzZ0RSUmZONzl6aFlXUFl2Sy0xdmM?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNZFl1LVN6VnE3eVY2bTQ4M0kxSm5pUkczVERka0FhTkh4RmRMVmh0U05fYTh1OWNuX2VIZ3A5S0x2aXFxdXlNVFVNRXZNZWdYb3FaTlM0R3lFaTJ0QWw0MEFxcHcta2ZKN1RhRUZOX2V5cGJFeFIzaVluNGJUMzQxRzJsdW04R0RuLUZwOHh3S0NnWU5OTjA4U2tuSXhqcXM?oc=5
- https://news.google.com/rss/articles/CBMihgFBVV95cUxPNEc2aHVnY3QzRXZRMXZ6QVZCcXRhQklyNDJZV09uWUxweTlobnhQczlaYjJwLXZ2eml0azgxVy1lVTRhVkpGTTlLdVo5aW1wUnJDR29RbFotaEU3SzNEc1UzeXVqTkN1NkNuRVF3Z2hpd0FNMlI3VDlPM1VPMGJDOFBEX3Judw?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxPVmNjaUVfTHlyUWR2aWVwcHYyM2lNeUFnU1RLWDUwdDE0Q2d6NV9hRk96Zl8yT3pUMWlMbTV0dUhMOHJaSzYydEZZb3FvTzUzdkFpQVYyQmRTZkxsVUw3eDVtTkZEUXZfc0ROMkdrT2d0VnB3U1VxNWZpSDgzZFA2dWctSUtPbE0?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxOZDBVNU5kSzFLQVQzaE1keXhLNjVkeWRxRlNiV29RN0dlVXhDcTRZdGxVNXp6cFE0eGU1dWlFZmJtXzhUbENYTXRWdm9rOTI3cTNMQ1YwZGc2cjBidklnX3gxMk1GVVZxcURvc1poRENPWFVtTUlsazFaeGswaTRqX2tocW42eHpDMm5iWG9OdHQtdw?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNYW5lcDFjeHhuUGdORFlpZDRDWVdZeERNX3ZkMTdjVWg2bUlXT3J3bkZXWXZTdFR1OFZiYl9kZU1aNWJFdDNYU2dCSDV6U2RIOXdBc3Fnc0lpSDhwY3VVNGxLTXlKUWxGQmdibmp0ZEpVbHdNeHpEcEZ4YXFpSmFPaU9zSGhlYUNZWE1ISEQ1MHFlOWpHdEl3TlQ5TlI?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxNNmRFNlVLUURhQklvQjRtb0FNaHU5RUhHbm1pMGw4Z3dubHlIT2YzVU10NGprT1J5eXl3U1lLM2dtVnA2cWJsY1RqYUhvNTQ5MzVKYzNGODlmY2JSbER5cWVidzAwczI3anBybkdSUlFMbmtnckY1bG00am1CbXdsZHdIYnI2bG5qZXd4MnNfc3NaQjNpSGdBV1ZaUVZkS0JJVV9VQk4yNTdTMUJ0cExjc2FrSUNHQnBHT21zTnM5dDQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
