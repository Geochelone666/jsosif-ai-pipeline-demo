# CP.TO Intelligence Report

- ticker: **CP.TO**
- Report as_of: **2026-11-03**
- Market data as_of: **2026-11-03**
- Quant sources: https://finance.yahoo.com/quote/CP.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CP.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-03**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-04T04:54:57.858043+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 5, 'rule': 1, 'ai': 3, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261103T051441Z-8b1c85d8/CP.TO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 5 unique headlines; 5 named publishers; 0 exact duplicates; 5 HTTPS source links; largest publisher share 20.0%; oldest publication 2026-10-28

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 127.7200 |
| Return 1D (%) | -0.1407 |
| Return 1W (%) | -0.2110 |
| Return 1M (%) | 4.2527 |
| Return YTD (%) | 27.2078 |
| Return 1Y (%) | 29.6619 |
| Annualized volatility (%) | 21.9497 |
| Beta vs SPY | 0.3707 |
| Max drawdown (%) | -11.9692 |
| Sharpe (rf=0) | 1.2980 |
| Downside deviation (rf=0, %) | 14.5292 |
| Sortino (rf=0) | 1.9609 |
| Historical VaR 95% (1D, %) | 1.8654 |
| Historical ES 95% (1D, %) | 2.9512 |
| Correlation vs SPY | 0.2153 |
| Tracking error vs SPY (%) | 23.0713 |
| P/E (trailing) | 29.43 |
| P/B | 2.43 |
| EV/EBITDA | 16.28 |
| Revenue growth (%) | 15.20 |
| Forward P/E (estimate) | 21.64 |
| Gross margin (%) | 52.76 |
| Operating margin (%) | 38.56 |
| Return on equity (%) | 8.27 |
| Free cash flow yield (%) | 2.47 |
| MA50 | 124.3605 |
| Close vs MA50 (%) | 2.7014 |
| MA200 | 119.2391 |
| Close vs MA200 (%) | 7.1125 |
| RSI (14, Wilder) | 59.0643 |
| MACD (12,26) | 0.9415 |
| MACD signal (9) | 0.4639 |
| MACD histogram | 0.4776 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CP.TO': 273, 'SPY': 274}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 127.7200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.1407 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.2110 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 4.2527 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 27.2078 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 29.6619 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 21.9497 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.5292 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.9609 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.8654 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.9512 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2153 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.0713 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3707 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -11.9692 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.2980 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 21.6387 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 52.7640 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 38.5640 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 8.2680 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.4668 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 29.4286 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 59.0643 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.4776 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 2.7014 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 7.1125 -> Clearly above the moving-average trend level.

## TAILWINDS

### Canadian Pacific Kansas City stock extends upward price move as buyer support outweighs weak momentum
- Summary: CP.TO shares rally as buyer support drives upward momentum, despite weak underlying performance.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxPbDMxSDdzUEN6aGxCUS1BUm1DOFVZQ09lVGVobUJYOVlOUWI2ODNEaFppUVVmWnZkS2ptX2x4b3lKQmN2QjVLZXI3S0EwcW55UUlpNk9ZRWluLWtSY3RSUHh2eVZlQ09hWTlUYTFIX1NyeE5SNkxHMjJvZHNyeDFjZ2UtdkhVTTdVOFE?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Canadian Pacific Kansas City (CP) Reports Q3 Earnings: What Key Metrics Have to Say
- Summary: Canadian Pacific Kansas City (CP) Reports Q3 Earnings: What Key Metrics Have to Say
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxOYWRReWJ0RmM4ZW9oZjFFZUtJbnV4Zlp4TW82UDJLWW1YV3B3Y2NGajRLaExycFZTUTdhXzZvUGFqNnNOU252WERTeFA1cnBPODducmhiMlhDQjRyam1jQjlodHRRQ2xLZDkydWFSMlpuNjYydUYwVjVVZVY1bnYyT1VOOU5SWU0?oc=5>

### Earnings Flash (CP.TO) Canadian Pacific Kansas City Limited Reports Q3 Revenue CA$4.22B, vs. FactSet Est of CA$4.21B
- Summary: CP reports Q3 revenue of CA$4.22B, slightly above estimates.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi4wFBVV95cUxQWXRoemkwWVRMdzgxbkpId1VqZDY4ekRTNmZ4VHdGVEhTX04wYUplSlREZm1uaFB1aVVtMWhrS3VlWnB2U1lxTUgtdXJ3dElVbFk1TWh0UWU5dGZzUGZHS2ZQSVZTTnMxNU5ZckpSa1QwX2JjZjdZeE1SWENZQlE4bjZTazMxdEFSN19yRXBKTHRITXozU1FHa05rYVVwZTVKRk96cl9HZ0lKZ3BoU1pxdkhoeWVCZ2didVFaT2piOUNnNVVXRE9HdWxzV09pbzUxUzJmSnFCLXU0cjE2MXVLZmZJaw?oc=5>

### Evercore ISI cuts Canadian Pacific Kansas City stock price target on cost pressures
- Summary: Evercore ISI lowered CP.TO price target citing cost pressures, signaling negative outlook for the company.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2wFBVV95cUxNMFdFaGpTZ184SzJJNFQwNDZnQ3kzMXI3d1hmZHh4QTd3RkpDUjhkQmd2VW1oMFpZcFJtdDRuaHk1blFmYWhRSHg4cG5sekoxb1UyMGttTHNWZkU4ZGV5el8wVzB2cmR5aF9SVGFuU0I5cHhTdjBMV1VUSk96R0ZaX0FNQ054Ul9wRHF0ZWp4X3BQNWw0ZGhHcllMZUZPczhMdUNsLW14Q1RMdUQycEIzYWVvaW9KdzBVR0QyaUlBUU15dWZxLTZqbVg2QlJsMUstajJMQm9fX1NmNFU?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CP.TO** | **29.43** | **2.43** | **16.28** | **15.20** | **111,059,533,824.00 CAD** | **29.66** |
| CNR.TO | 22.23 | 4.85 | 13.76 | 14.60 | 106,116,907,008.00 CAD | 34.81 |
| UNP | 23.95 | 8.19 | 15.69 | 15.30 | 180,260,323,328.00 USD | 41.59 |
| NSC | 28.97 | 4.58 | 15.91 | 13.60 | 76,583,059,456.00 USD | 22.96 |

Peers fetched as_of: 2026-11-03; CP.TO reuses existing data (market data as_of: 2026-11-03); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-28
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-03

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-29
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: https://www.sec.gov/Archives/edgar/data/16875/000001687526000033/cp-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiigFBVV95cUxPbDMxSDdzUEN6aGxCUS1BUm1DOFVZQ09lVGVobUJYOVlOUWI2ODNEaFppUVVmWnZkS2ptX2x4b3lKQmN2QjVLZXI3S0EwcW55UUlpNk9ZRWluLWtSY3RSUHh2eVZlQ09hWTlUYTFIX1NyeE5SNkxHMjJvZHNyeDFjZ2UtdkhVTTdVOFE?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxOYWRReWJ0RmM4ZW9oZjFFZUtJbnV4Zlp4TW82UDJLWW1YV3B3Y2NGajRLaExycFZTUTdhXzZvUGFqNnNOU252WERTeFA1cnBPODducmhiMlhDQjRyam1jQjlodHRRQ2xLZDkydWFSMlpuNjYydUYwVjVVZVY1bnYyT1VOOU5SWU0?oc=5
- https://news.google.com/rss/articles/CBMi4wFBVV95cUxQWXRoemkwWVRMdzgxbkpId1VqZDY4ekRTNmZ4VHdGVEhTX04wYUplSlREZm1uaFB1aVVtMWhrS3VlWnB2U1lxTUgtdXJ3dElVbFk1TWh0UWU5dGZzUGZHS2ZQSVZTTnMxNU5ZckpSa1QwX2JjZjdZeE1SWENZQlE4bjZTazMxdEFSN19yRXBKTHRITXozU1FHa05rYVVwZTVKRk96cl9HZ0lKZ3BoU1pxdkhoeWVCZ2didVFaT2piOUNnNVVXRE9HdWxzV09pbzUxUzJmSnFCLXU0cjE2MXVLZmZJaw?oc=5
- https://news.google.com/rss/articles/CBMi2wFBVV95cUxNMFdFaGpTZ184SzJJNFQwNDZnQ3kzMXI3d1hmZHh4QTd3RkpDUjhkQmd2VW1oMFpZcFJtdDRuaHk1blFmYWhRSHg4cG5sekoxb1UyMGttTHNWZkU4ZGV5el8wVzB2cmR5aF9SVGFuU0I5cHhTdjBMV1VUSk96R0ZaX0FNQ054Ul9wRHF0ZWp4X3BQNWw0ZGhHcllMZUZPczhMdUNsLW14Q1RMdUQycEIzYWVvaW9KdzBVR0QyaUlBUU15dWZxLTZqbVg2QlJsMUstajJMQm9fX1NmNFU?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
