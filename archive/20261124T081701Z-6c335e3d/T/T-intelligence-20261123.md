# T Intelligence Report

- ticker: **T**
- Report as_of: **2026-11-23**
- Market data as_of: **2026-11-23**
- Quant sources: https://finance.yahoo.com/quote/T/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/T/key-statistics/
- AI analysis snapshot as_of: **2026-11-23**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-24T08:24:12.246885+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 8, 'rule': 1, 'ai': 3, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261123T053847Z-45053549/T** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 8 unique headlines; 7 named publishers; 1 exact duplicates; 8 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-11-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 22.3000 |
| Return 1D (%) | -0.0448 |
| Return 1W (%) | -0.2683 |
| Return 1M (%) | 6.5456 |
| Return YTD (%) | -5.9420 |
| Return 1Y (%) | -9.8959 |
| Annualized volatility (%) | 28.7095 |
| Beta vs SPY | -0.3141 |
| Max drawdown (%) | -28.8854 |
| Sharpe (rf=0) | -0.1787 |
| Downside deviation (rf=0, %) | 22.0025 |
| Sortino (rf=0) | -0.2331 |
| Historical VaR 95% (1D, %) | 2.8611 |
| Historical ES 95% (1D, %) | 4.6484 |
| Correlation vs SPY | -0.1638 |
| Tracking error vs SPY (%) | 34.4871 |
| P/E (trailing) | 11.93 |
| P/B | 1.41 |
| EV/EBITDA | 7.36 |
| Revenue growth (%) | 5.30 |
| Forward P/E (estimate) | 8.59 |
| Gross margin (%) | 59.74 |
| Operating margin (%) | 22.59 |
| Return on equity (%) | 11.61 |
| Free cash flow yield (%) | 7.96 |
| MA50 | 23.0293 |
| Close vs MA50 (%) | -3.1668 |
| MA200 | 24.2813 |
| Close vs MA200 (%) | -8.1599 |
| RSI (14, Wilder) | 50.6634 |
| MACD (12,26) | -0.1477 |
| MACD signal (9) | -0.2871 |
| MACD histogram | 0.1394 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'T': 288, 'SPY': 288}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 22.3000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.0448 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.2683 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 6.5456 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -5.9420 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -9.8959 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 28.7095 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 22.0025 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.2331 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8611 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.6484 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1638 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 34.4871 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.3141 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.8854 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.1787 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 8.5908 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 59.7420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 22.5930 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 11.6130 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 7.9626 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 11.9251 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 50.6634 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.1394 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -3.1668 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -8.1599 -> Clearly below the moving-average trend level.

## TAILWINDS

### Can T's Extended U.S. Soccer Deal Boost Sports Technology Innovation?
- Summary: AT&T's extended U.S. Soccer deal could enhance sports tech innovation.
- Date: 2026-11-23 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxQTjVzSkJvanJ1TG1iTEp6TGZUdHJ5U2ZNVmgtZjlRVGlKVkdpNWdzYzlhOFY0UGsxamhCa1VOOElzbXVWMkZLNnhOYkxRV1RWU3NxR0F3TVUtOGNieFdfN1hGX0dXRGZxUHlzem1HQUJiWkhiVVN5N1dYMzFsR040VmJaa2lWcWx1YTBCQlMyZmVrUTRSd19HZHk3c212TXhEbHBvZ01IcnBkNUd2LWFiRWlSM1pMblh0RXVxUzJwRkM?oc=5>

### AT&T will connect U.S. Soccer’s new center, where men’s and women’s teams will train at one site for the first time.
- Summary: AT&T will connect U.S. Soccer’s new training center, uniting men's and women's teams.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxOdEgyMkxYUU05LVdLNUY3UnUtQlFyMTM4LVhqMTBaTEROaHBRcl90dlJ2RDB4ZGNOSllxY3FLWFBDb3VaeDB5dHBrWmFRWDJJVlRRalo3RnZEZlRKVmpFdnlqTDQyREtiSVBrLUFsemljU1U0bDlxTE5KaHduSDJxblBlejl4dDJfQTdlREpGd3ByaDVhWWNYeTRiN2Z6NG9haEpIbVQydnpCZ0FrUlNIWTQ4T20tb3c?oc=5>

### AT&T stock gets FCC clearance to phase out California copper lines
- Summary: FCC clears AT&T to phase out California copper lines.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxOTmZNalVFYzYtajlrblpBNHhuLUdsNWJLLUVib0hZZ0VQTTE5eVFoNHpRQUV1UTF4Zk0yOHNUWVRpeVhvTHQyQjNNWkhrOEhUT2lveEkxdXFKdk5pUTUzZ1l1R3JqSFRNeUZOeWdzMjhUeDQyaldsTWxuUkxTV0Z5NldzRmstYjctREtsMWcwV3BhMWRYa0xwSFhwSG1wcnFFVWQ4Qk40cHB1eC1pN0tzY3lJcHRfRGpkUHo2b2dyZDE5a3ZFQTNUTg?oc=5>

## HEADWINDS

### AT&T Inc. (T) Stock: Slips Despite Renewed Partnership Supporting 27 U.S. National Teams
- Summary: AT&T Inc. (T) Stock: Slips Despite Renewed Partnership Supporting 27 U.S. National Teams
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxOQkhIX01xQnUyVWVMZnpmN19WZmVsY0hQRUxmNHJQbTh2Y0ZHN01jSXNwdXpqcFpsMkxNbUtEeTRFcnUxd3ZucE45bmNKN056Vld4b3drNkpMV2VScU5ZbkJMWGhYOFhrV0tEb0pFR2RUNDM3bjZVTmVlM1lwWGVfTDByLWh2blluZld4OW10NmFWYXRzT1g1cm5tVzJybzRscFRxaEh2NE9tQQ?oc=5>

## CATALYSTS

No items in this run

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **T** | **11.93** | **1.41** | **7.36** | **5.30** | **150,223,355,904.00 USD** | **-9.90** |
| VZ | 11.85 | 1.82 | 7.38 | 1.50 | 192,516,587,520.00 USD | 20.16 |
| TMUS | 16.04 | 3.14 | 8.19 | 7.40 | 176,220,585,984.00 USD | -18.91 |
| BCE | 11.78 | 1.36 | 7.40 | 2.20 | 20,329,062,400.00 USD | -0.69 |

Peers fetched as_of: 2026-11-23; T reuses existing data (market data as_of: 2026-11-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-23

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

- https://news.google.com/rss/articles/CBMiwAFBVV95cUxQTjVzSkJvanJ1TG1iTEp6TGZUdHJ5U2ZNVmgtZjlRVGlKVkdpNWdzYzlhOFY0UGsxamhCa1VOOElzbXVWMkZLNnhOYkxRV1RWU3NxR0F3TVUtOGNieFdfN1hGX0dXRGZxUHlzem1HQUJiWkhiVVN5N1dYMzFsR040VmJaa2lWcWx1YTBCQlMyZmVrUTRSd19HZHk3c212TXhEbHBvZ01IcnBkNUd2LWFiRWlSM1pMblh0RXVxUzJwRkM?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxOdEgyMkxYUU05LVdLNUY3UnUtQlFyMTM4LVhqMTBaTEROaHBRcl90dlJ2RDB4ZGNOSllxY3FLWFBDb3VaeDB5dHBrWmFRWDJJVlRRalo3RnZEZlRKVmpFdnlqTDQyREtiSVBrLUFsemljU1U0bDlxTE5KaHduSDJxblBlejl4dDJfQTdlREpGd3ByaDVhWWNYeTRiN2Z6NG9haEpIbVQydnpCZ0FrUlNIWTQ4T20tb3c?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxOTmZNalVFYzYtajlrblpBNHhuLUdsNWJLLUVib0hZZ0VQTTE5eVFoNHpRQUV1UTF4Zk0yOHNUWVRpeVhvTHQyQjNNWkhrOEhUT2lveEkxdXFKdk5pUTUzZ1l1R3JqSFRNeUZOeWdzMjhUeDQyaldsTWxuUkxTV0Z5NldzRmstYjctREtsMWcwV3BhMWRYa0xwSFhwSG1wcnFFVWQ4Qk40cHB1eC1pN0tzY3lJcHRfRGpkUHo2b2dyZDE5a3ZFQTNUTg?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxOQkhIX01xQnUyVWVMZnpmN19WZmVsY0hQRUxmNHJQbTh2Y0ZHN01jSXNwdXpqcFpsMkxNbUtEeTRFcnUxd3ZucE45bmNKN056Vld4b3drNkpMV2VScU5ZbkJMWGhYOFhrV0tEb0pFR2RUNDM3bjZVTmVlM1lwWGVfTDByLWh2blluZld4OW10NmFWYXRzT1g1cm5tVzJybzRscFRxaEh2NE9tQQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
