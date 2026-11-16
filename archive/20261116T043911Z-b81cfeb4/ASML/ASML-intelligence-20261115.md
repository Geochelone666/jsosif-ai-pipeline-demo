# ASML Intelligence Report

- ticker: **ASML**
- Report as_of: **2026-11-15**
- Market data as_of: **2026-11-13**
- Quant sources: https://finance.yahoo.com/quote/ASML/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ASML/key-statistics/
- AI analysis snapshot as_of: **2026-11-15**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-16T04:46:05.049798+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 2, 'rule': 0, 'ai': 2, 'unknown': 0})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261115T044154Z-6abfba73/ASML** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 2 unique headlines; 2 named publishers; 0 exact duplicates; 2 HTTPS source links; largest publisher share 50.0%; oldest publication 2026-11-09

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 1495.1600 |
| Return 1D (%) | -0.1309 |
| Return 1W (%) | 4.9419 |
| Return 1M (%) | -12.8439 |
| Return YTD (%) | 40.6095 |
| Return 1Y (%) | 47.5030 |
| Annualized volatility (%) | 48.6773 |
| Beta vs SPY | 2.2734 |
| Max drawdown (%) | -31.6292 |
| Sharpe (rf=0) | 1.0447 |
| Downside deviation (rf=0, %) | 32.8643 |
| Sortino (rf=0) | 1.5473 |
| Historical VaR 95% (1D, %) | 4.7389 |
| Historical ES 95% (1D, %) | 6.4916 |
| Correlation vs SPY | 0.6367 |
| Tracking error vs SPY (%) | 41.3548 |
| P/E (trailing) | 36.79 |
| P/B | 1283.82 |
| EV/EBITDA | 1965.96 |
| Revenue growth (%) | 55.20 |
| Forward P/E (estimate) | 23.58 |
| Gross margin (%) | 54.34 |
| Operating margin (%) | 38.55 |
| Return on equity (%) | 65.64 |
| Free cash flow yield (%) | N/A |
| MA50 | 1658.8705 |
| Close vs MA50 (%) | -9.8688 |
| MA200 | 1598.0596 |
| Close vs MA200 (%) | -6.4390 |
| RSI (14, Wilder) | 42.2687 |
| MACD (12,26) | -54.9359 |
| MACD signal (9) | -55.0822 |
| MACD histogram | 0.1463 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ASML': 282, 'SPY': 282}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 1495.1600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.1309 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 4.9419 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -12.8439 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 40.6095 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 47.5030 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 48.6773 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 32.8643 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.5473 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.7389 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.4916 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6367 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 41.3548 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.2734 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -31.6292 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.0447 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 23.5832 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.3370 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 38.5520 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 65.6360 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 36.7904 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 42.2687 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.1463 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -9.8688 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -6.4390 -> Clearly below the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Applied Materials Jumps 11% Ahead of Earnings; Lam Research Surges 9%, ASML Rises 6%
- Summary: ASML shares rise 6% in market reaction to sector moves.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxPcjFldU84UWg4b21Nd1pyd2VsaXlDaWhDRUk3THdxQ0xtTGZpWkUyYnpwRnYyNDFZbk1FSDQwcTZhaXlmQmNJY0x6cDF3QkhWdnNLUkc3dnc1eGZYUXotUFpGN2QxSC1sVVlQWXZ5YVJDZzUtcVlzZWdYWWR2NDlIOFFiRWwzMTNqclJLSDJQOFNjajJ5NVJVQjZLX3preUgwNHN2R2FOMlNITGwybGJZckFhQmxVQUJmSVJxc0Y5dmk?oc=5>

### ASML's Real Test Isn't Friday's Tape — It's Whether Customers Keep Knocking
- Summary: ASML faces pressure to maintain customer demand amid upcoming tape release, highlighting potential market volatility.
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi3gFBVV95cUxQaGl2WDVVVlZlRFZ3bFROTWZXVzRESzJwTlBjOTd4SnZweGpuX2ViWFdqRGE5LXRKTXExcEVVTXJmX25UU1ZiSjdBTnlMSm5fVVBvdGhzY1NSaWZaSEFjc1FRcV85aXNWbERZZndnVmRCNmFteVU1VG9IVHRtcEVwdks1Y2xKV0dSNnVzNzdHZE9mUURNQ0xwUW5lWU54V2FhRXY1N1gzdVFyeUpVMzZub1V2Vm9uSDNJdnZsNGd3LTN6SWM1OEljWFRTVnI1X193TU5vQjVUTXZ1bTFzMWc?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ASML** | **36.79** | **1,283.82** | **1,965.96** | **55.20** | **576,261,193,728.00 USD** | **47.50** |
| AMAT | 29.36 | 11.25 | 24.41 | 53.10 | 294,027,853,824.00 USD | 66.89 |
| LRCX | 33.67 | 20.29 | 27.53 | 54.40 | 282,212,696,064.00 USD | 48.03 |
| KLAC | 38.18 | 30.43 | 30.35 | 28.90 | 198,467,239,936.00 USD | 31.82 |

Peers fetched as_of: 2026-11-15; ASML reuses existing data (market data as_of: 2026-11-13); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-14
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-15

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

- https://news.google.com/rss/articles/CBMiwAFBVV95cUxPcjFldU84UWg4b21Nd1pyd2VsaXlDaWhDRUk3THdxQ0xtTGZpWkUyYnpwRnYyNDFZbk1FSDQwcTZhaXlmQmNJY0x6cDF3QkhWdnNLUkc3dnc1eGZYUXotUFpGN2QxSC1sVVlQWXZ5YVJDZzUtcVlzZWdYWWR2NDlIOFFiRWwzMTNqclJLSDJQOFNjajJ5NVJVQjZLX3preUgwNHN2R2FOMlNITGwybGJZckFhQmxVQUJmSVJxc0Y5dmk?oc=5
- https://news.google.com/rss/articles/CBMi3gFBVV95cUxQaGl2WDVVVlZlRFZ3bFROTWZXVzRESzJwTlBjOTd4SnZweGpuX2ViWFdqRGE5LXRKTXExcEVVTXJmX25UU1ZiSjdBTnlMSm5fVVBvdGhzY1NSaWZaSEFjc1FRcV85aXNWbERZZndnVmRCNmFteVU1VG9IVHRtcEVwdks1Y2xKV0dSNnVzNzdHZE9mUURNQ0xwUW5lWU54V2FhRXY1N1gzdVFyeUpVMzZub1V2Vm9uSDNJdnZsNGd3LTN6SWM1OEljWFRTVnI1X193TU5vQjVUTXZ1bTFzMWc?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
