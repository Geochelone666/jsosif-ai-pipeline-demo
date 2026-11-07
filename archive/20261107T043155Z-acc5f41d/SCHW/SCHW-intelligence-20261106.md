# SCHW Intelligence Report

- ticker: **SCHW**
- Report as_of: **2026-11-06**
- Market data as_of: **2026-11-06**
- Quant sources: https://finance.yahoo.com/quote/SCHW/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SCHW/key-statistics/
- AI analysis snapshot as_of: **2026-11-06**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-07T04:57:12.143415+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 8, 'rule': 2, 'ai': 4, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261106T045829Z-1db1e5a7/SCHW** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 8 unique headlines; 5 named publishers; 1 exact duplicates; 8 HTTPS source links; largest publisher share 37.5%; oldest publication 2026-10-31

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 91.4900 |
| Return 1D (%) | -1.1774 |
| Return 1W (%) | 3.9069 |
| Return 1M (%) | -5.4855 |
| Return YTD (%) | -7.5198 |
| Return 1Y (%) | -1.6355 |
| Annualized volatility (%) | 25.9127 |
| Beta vs SPY | 0.4502 |
| Max drawdown (%) | -22.5253 |
| Sharpe (rf=0) | 0.0665 |
| Downside deviation (rf=0, %) | 19.7150 |
| Sortino (rf=0) | 0.0874 |
| Historical VaR 95% (1D, %) | 2.5523 |
| Historical ES 95% (1D, %) | 3.9505 |
| Correlation vs SPY | 0.2354 |
| Tracking error vs SPY (%) | 26.2632 |
| P/E (trailing) | 15.83 |
| P/B | 3.08 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 16.90 |
| Forward P/E (estimate) | 11.72 |
| Gross margin (%) | 97.51 |
| Operating margin (%) | 52.67 |
| Return on equity (%) | 21.12 |
| Free cash flow yield (%) | N/A |
| MA50 | 98.4892 |
| Close vs MA50 (%) | -7.1066 |
| MA200 | 96.9267 |
| Close vs MA200 (%) | -5.6091 |
| RSI (14, Wilder) | 44.0967 |
| MACD (12,26) | -2.0344 |
| MACD signal (9) | -2.7032 |
| MACD histogram | 0.6688 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SCHW': 277, 'SPY': 277}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 91.4900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.1774 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 3.9069 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -5.4855 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -7.5198 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -1.6355 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 25.9127 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 19.7150 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.0874 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.5523 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.9505 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2354 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.2632 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.4502 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -22.5253 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.0665 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 11.7248 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 97.5060 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 52.6700 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 21.1220 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 15.8287 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 44.0967 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.6688 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -7.1066 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -5.6091 -> Clearly below the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Charles Schwab Stock: Analyst Estimates & Ratings
- Summary: Charles Schwab Stock: Analyst Estimates & Ratings
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPRm4td3hlLWZLcmNzT3ctaXJMbjhiX3BQX003dm1mQ0F6dXdySGJmZUhZUjVNR3U5VE9MZDFoQUFyYlUzN2cwZmR0NUdIaGh6RDBMeWlTdVFPQllDY19pZERlR0tHQUQ0UzZUTUp2MENqUWZnWGNNLV91TUlodDQzSURaamZtVFZoSGkxZUlGTUJvSWdwNm1aYjJoQTg3bUVIN3JubjZB?oc=5>

### Charles Schwab Corporation (NYSE:SCHW) Stock Analysis — Earnings Recovery and Technical Divergence
- Summary: Charles Schwab Corporation (NYSE:SCHW) Stock Analysis — Earnings Recovery and Technical Divergence
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxNQ2FDcEdQZy1tQS1ubHA2U1JIcHFleEh1X0dJcC1FWkZLaGRia2l2U2FZcE0xNHVlc19NdmJETmliaGZBemRUTzRuc3dNWHM4UVVhTWdFUlZhRDYxTV80S21Fc2N0UDRFRF9wOEYzT0lYUVBsWEQwbThpSzNuNVJGU1pzdk9zZFJRZVh4RjlyWjBCbHVNeXVKZHBLY1ZPeGZSTUFueDdhOVBZM2l6eU1wVDd5aWRSclZCbzBzX2cybUpTXzBXUmlXQXU4VkllaDVTX3c?oc=5>

### Charles Schwab (SCHW) Expands AI Tools For RIAs, Is The Stock Still 25% Undervalued?
- Summary: Schwab expands AI tools for RIAs, signaling product enhancement.
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPVmtZQzNUTUxSSDVBZVgwUURWUWREZ2ZNM0owNGdwWHlkYjVOdUZYWFhMQnlBZXVIZTBwQUlDOFc1Rmo1Q29wVWFRaXQtRGVoRV8tYUVCSjlnc3BpMU5Vb19QZERTNERMNEZTa1BtUE51X3JlZUhSOFJSUk9xU3ZLamNwSUZpWjREclIxLUFDc3Z1dGRSSUNsemI3aw?oc=5>

### Charles Schwab (SCHW) Stock May Trade At A Discount On Record Revenue News
- Summary: Schwab’s stock may trade at a discount despite record revenue, indicating potential market overreaction or valuation concerns.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi3AFBVV95cUxQVE56WWI5UjE3dTF4YTZTNjRzTkstc254R2tkRzJMR0xVYmVGV05MNkVJYzVkUVF2UjN0SDBPUUtUZnNqUE94Ni1mR1BLN0ZBREMxbmpKbThzT0RYeXdsd09ELTFOdjBEQkdFYUw1ZzdWd08zMHdsSG1YLTNyZE1UNmNVUXgxc2FSQk41dHV5TXVtSlctMzA0SFc4d2RsbVJ4REpzc2FUTzNkNWVQMTUxcEtUeUxyZ0hBeVZmNXlfRGpTR1lVYzVTd3lRbzhJa3JaSDM0VXlKVEdZZko50gHiAUFVX3lxTE81SGZYMEJOcnhqYWhUM0x1TnB3SDFaclY5TU1zdGNBREFWSmg1M1pvRno4TUI0OG15SDdzNUFGbUNyanlnSm5saWROazl6WVN6eUVwWWRPTWFxQWMwZGZsbUd5dWJDMEFMTVlnLURaQ0MwUTdqSV9jQURsenI1Sks0ZC1vcnpsd2ZoNFNqb0ZwX3dkNEZKOVBJLVlVZ25IVFp2QUJUNE1qUUZOWFNOSmpZaEkwM0tHWVdZTzhSR3h5dnM4dFBrejFucTJnS0NUOTd3N0dUamdGSmtYS1JIRnB0V2c?oc=5>

## RISKS

### Charles Schwab (SCHW) co-chairman sells 11,675 shares; his trust retains 53.3M.
- Summary: Insider sale by co-chairman may signal confidence concerns, affecting investor perception.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxNWnZLUG1QS3A2UTJDVG9DeGJBS0RicHBlbUtlOFIxVTdzVHh5Z21vQzNoeWZPb3lnOHQtZ2VsRnRRdV9zdXlCZWFRbHpRTFV1REFfNEZQT1dPdmVvWjU0S3p2VGpVRWN1RXpPUU5TTklBNkNhRWFfZ1Nqd01LWThwMmc0ODk2NzBrcEo3VG9SRXhXNmhIbFhnWHRVRWd4N05kb2hjS0tmNTZkaHhUQ1FpdWxvQQ?oc=5>

### 493,951 Shares in The Charles Schwab Corporation $SCHW Acquired by Associated Banc Corp
- Summary: Associated Banc Corp acquired nearly half a million Schwab shares, potentially signaling a strategic buyback or consolidation move.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3wFBVV95cUxOS0Y0alJOdUJUcFNvUXhjTlNhT1VmQ21OR1FQQUg4VzFNUjVyajNyLS1mU0VzUkI3SjQybE9kQkZKLVVaOGlkLWh6MlJ0WDBGSkxHWkhwbkUtTW1wOE0zbFg0WUlwekR6bTJSdVIzZnQwengyRUpJNVNsaVE4Vlh0NU90Nl9BTXUwZG1RcV9tT19QZnpieUxuRlRDV3oyY3JkTzJDbjRJQ24wNXNnSWpsQVFiZ0FjbTl0YVphQ0VRUjN0emFVWm1UNVlqM0Z3cDFzZVZ0dDBOd0lfR19oOC1V?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SCHW** | **15.83** | **3.08** | **N/A** | **16.90** | **158,216,912,896.00 USD** | **-1.64** |
| IBKR | 27.77 | 5.52 | N/A | 13.50 | 129,183,293,440.00 USD | 8.99 |
| HOOD | 37.29 | 7.29 | N/A | 11.80 | 72,858,755,072.00 USD | -36.33 |
| LPLA | 16.93 | 3.98 | N/A | 17.80 | 23,010,895,872.00 USD | -20.42 |

Peers fetched as_of: 2026-11-06; SCHW reuses existing data (market data as_of: 2026-11-06); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-21 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-06

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-06
- Revenue (latest available single quarter): 7,171,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 2,906,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/316709/000031670926000038/schw-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMipgFBVV95cUxPRm4td3hlLWZLcmNzT3ctaXJMbjhiX3BQX003dm1mQ0F6dXdySGJmZUhZUjVNR3U5VE9MZDFoQUFyYlUzN2cwZmR0NUdIaGh6RDBMeWlTdVFPQllDY19pZERlR0tHQUQ0UzZUTUp2MENqUWZnWGNNLV91TUlodDQzSURaamZtVFZoSGkxZUlGTUJvSWdwNm1aYjJoQTg3bUVIN3JubjZB?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxNQ2FDcEdQZy1tQS1ubHA2U1JIcHFleEh1X0dJcC1FWkZLaGRia2l2U2FZcE0xNHVlc19NdmJETmliaGZBemRUTzRuc3dNWHM4UVVhTWdFUlZhRDYxTV80S21Fc2N0UDRFRF9wOEYzT0lYUVBsWEQwbThpSzNuNVJGU1pzdk9zZFJRZVh4RjlyWjBCbHVNeXVKZHBLY1ZPeGZSTUFueDdhOVBZM2l6eU1wVDd5aWRSclZCbzBzX2cybUpTXzBXUmlXQXU4VkllaDVTX3c?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPVmtZQzNUTUxSSDVBZVgwUURWUWREZ2ZNM0owNGdwWHlkYjVOdUZYWFhMQnlBZXVIZTBwQUlDOFc1Rmo1Q29wVWFRaXQtRGVoRV8tYUVCSjlnc3BpMU5Vb19QZERTNERMNEZTa1BtUE51X3JlZUhSOFJSUk9xU3ZLamNwSUZpWjREclIxLUFDc3Z1dGRSSUNsemI3aw?oc=5
- https://news.google.com/rss/articles/CBMi3AFBVV95cUxQVE56WWI5UjE3dTF4YTZTNjRzTkstc254R2tkRzJMR0xVYmVGV05MNkVJYzVkUVF2UjN0SDBPUUtUZnNqUE94Ni1mR1BLN0ZBREMxbmpKbThzT0RYeXdsd09ELTFOdjBEQkdFYUw1ZzdWd08zMHdsSG1YLTNyZE1UNmNVUXgxc2FSQk41dHV5TXVtSlctMzA0SFc4d2RsbVJ4REpzc2FUTzNkNWVQMTUxcEtUeUxyZ0hBeVZmNXlfRGpTR1lVYzVTd3lRbzhJa3JaSDM0VXlKVEdZZko50gHiAUFVX3lxTE81SGZYMEJOcnhqYWhUM0x1TnB3SDFaclY5TU1zdGNBREFWSmg1M1pvRno4TUI0OG15SDdzNUFGbUNyanlnSm5saWROazl6WVN6eUVwWWRPTWFxQWMwZGZsbUd5dWJDMEFMTVlnLURaQ0MwUTdqSV9jQURsenI1Sks0ZC1vcnpsd2ZoNFNqb0ZwX3dkNEZKOVBJLVlVZ25IVFp2QUJUNE1qUUZOWFNOSmpZaEkwM0tHWVdZTzhSR3h5dnM4dFBrejFucTJnS0NUOTd3N0dUamdGSmtYS1JIRnB0V2c?oc=5
- https://news.google.com/rss/articles/CBMi4gFBVV95cUxPNUhmWDBCTnJ4amFoVDNMdU5wd0gxWnJWOU1Nc3RjQURBVkpoNTNab0Z6OE1CNDhteUg3czVBRm1Dcmp5Z0pubGlkTms5ellTenlFcFlkT01hcUFjMGRmbG1HeXViQzBBTE1ZZy1EWkNDMFE3aklfY0FEbHpyNUpLNGQtb3J6bHdmaDRTam9GcF93ZDRGSjlQSS1ZVWduSFRadkFCVDRNalFGTlhTTkpqWWhJMDNLR1lXWU84Ukd4eXZzOHRQa3oxbnEyZ0tDVDk3dzdHVGpnRkprWEtSSEZwdFdn0gHiAUFVX3lxTE81SGZYMEJOcnhqYWhUM0x1TnB3SDFaclY5TU1zdGNBREFWSmg1M1pvRno4TUI0OG15SDdzNUFGbUNyanlnSm5saWROazl6WVN6eUVwWWRPTWFxQWMwZGZsbUd5dWJDMEFMTVlnLURaQ0MwUTdqSV9jQURsenI1Sks0ZC1vcnpsd2ZoNFNqb0ZwX3dkNEZKOVBJLVlVZ25IVFp2QUJUNE1qUUZOWFNOSmpZaEkwM0tHWVdZTzhSR3h5dnM4dFBrejFucTJnS0NUOTd3N0dUamdGSmtYS1JIRnB0V2c?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxNWnZLUG1QS3A2UTJDVG9DeGJBS0RicHBlbUtlOFIxVTdzVHh5Z21vQzNoeWZPb3lnOHQtZ2VsRnRRdV9zdXlCZWFRbHpRTFV1REFfNEZQT1dPdmVvWjU0S3p2VGpVRWN1RXpPUU5TTklBNkNhRWFfZ1Nqd01LWThwMmc0ODk2NzBrcEo3VG9SRXhXNmhIbFhnWHRVRWd4N05kb2hjS0tmNTZkaHhUQ1FpdWxvQQ?oc=5
- https://news.google.com/rss/articles/CBMi3wFBVV95cUxOS0Y0alJOdUJUcFNvUXhjTlNhT1VmQ21OR1FQQUg4VzFNUjVyajNyLS1mU0VzUkI3SjQybE9kQkZKLVVaOGlkLWh6MlJ0WDBGSkxHWkhwbkUtTW1wOE0zbFg0WUlwekR6bTJSdVIzZnQwengyRUpJNVNsaVE4Vlh0NU90Nl9BTXUwZG1RcV9tT19QZnpieUxuRlRDV3oyY3JkTzJDbjRJQ24wNXNnSWpsQVFiZ0FjbTl0YVphQ0VRUjN0emFVWm1UNVlqM0Z3cDFzZVZ0dDBOd0lfR19oOC1V?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
