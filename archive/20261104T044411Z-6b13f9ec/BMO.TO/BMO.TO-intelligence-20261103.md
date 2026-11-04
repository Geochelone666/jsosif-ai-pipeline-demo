# BMO.TO Intelligence Report

- ticker: **BMO.TO**
- Report as_of: **2026-11-03**
- Market data as_of: **2026-11-03**
- Quant sources: https://finance.yahoo.com/quote/BMO.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/BMO.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-03**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-04T04:53:19.989664+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 3, 'rule': 0, 'ai': 2, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **N/A (no successful AI classification call)**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261103T051441Z-8b1c85d8/BMO.TO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 3 unique headlines; 3 named publishers; 0 exact duplicates; 3 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-10-29

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 240.5600 |
| Return 1D (%) | -0.6074 |
| Return 1W (%) | 0.1083 |
| Return 1M (%) | 2.5363 |
| Return YTD (%) | 39.1777 |
| Return 1Y (%) | 41.3666 |
| Annualized volatility (%) | 19.2801 |
| Beta vs SPY | 0.8741 |
| Max drawdown (%) | -11.4239 |
| Sharpe (rf=0) | 1.9002 |
| Downside deviation (rf=0, %) | 13.2409 |
| Sortino (rf=0) | 2.7669 |
| Historical VaR 95% (1D, %) | 1.9150 |
| Historical ES 95% (1D, %) | 2.6099 |
| Correlation vs SPY | 0.5778 |
| Tracking error vs SPY (%) | 15.9504 |
| P/E (trailing) | 19.49 |
| P/B | 1.97 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 12.00 |
| Forward P/E (estimate) | 14.61 |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 30.50 |
| Return on equity (%) | 10.57 |
| Free cash flow yield (%) | N/A |
| MA50 | 237.6974 |
| Close vs MA50 (%) | 1.2043 |
| MA200 | 219.6364 |
| Close vs MA200 (%) | 9.5265 |
| RSI (14, Wilder) | 54.1925 |
| MACD (12,26) | 1.0816 |
| MACD signal (9) | 0.1157 |
| MACD histogram | 0.9659 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'BMO.TO': 273, 'SPY': 274}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 240.5600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.6074 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.1083 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 2.5363 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 39.1777 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 41.3666 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 19.2801 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 13.2409 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.7669 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.9150 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.6099 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5778 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 15.9504 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.8741 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -11.4239 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.9002 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 14.6115 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 30.4990 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 10.5740 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 19.4943 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 54.1925 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.9659 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 1.2043 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 9.5265 -> Clearly above the moving-average trend level.

## TAILWINDS

### More than 70 companies, including BlackRock, are expected at BMO's Florida conference.
- Summary: BMO hosts a Florida conference with 70+ companies, including BlackRock, indicating industry engagement and potential networking opportunities.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxOMHI5aTFhTWdVQ0RQNHI0QUpHTDBCb0ZUSTM2QUdTZ0hkbnFWY2hHSTUydExPMGtJZmhXN2tjQjlDbWYzWU5jZ1BXaFpwSUF3cjVEV0NmSnRXNjV4OXp1ck1TOTNvbHJOd2RIS0dxNjYzZ3BrVmJXVW5VZGZWcUpSWGZfUnpUcl9TLS0zYURXcjlZc0hiNGgwOE1ZNjQtRFd3cHkxYVBtYmhPbzNBLWwtXzI5dzRISWkwVDZEbQ?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Bank Of Montreal (TSX:BMO) Debuts Canada’s First Single Stock Autocallable Income ETFs
- Summary: BMO introduces its first single‑stock autocallable income ETF in Canada.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOY05EeGdVOVhLcWtWZFYySWgxclRJT3dXMUJ4NkdKSjZURFZ2b3dTNnNiZ0hrM1Mtd0tnbXBtRmpEa05hVm5LY0oxWnRUUFVRWGFUc3N5VGJ4TVNwRnRvb09DbldhZFhqWTNOR1dFUFcweW1YLWZ0Nk5iZ0M2N21HSFJpZGJjTE5PYzQyLUFCNlJMYkgteEo5Zw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **BMO.TO** | **19.49** | **1.97** | **N/A** | **12.00** | **167,211,384,832.00 CAD** | **41.37** |
| RY.TO | 18.00 | 2.95 | N/A | 8.90 | 395,143,970,816.00 CAD | 41.39 |
| TD.TO | 18.69 | 2.31 | N/A | 11.50 | 285,369,663,488.00 CAD | 56.30 |
| BNS.TO | 17.08 | 1.79 | N/A | 11.70 | 159,608,504,320.00 CAD | 47.85 |

Peers fetched as_of: 2026-11-03; BMO.TO reuses existing data (market data as_of: 2026-11-03); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-25
- Next expected earnings: 2026-12-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-03

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMivAFBVV95cUxOMHI5aTFhTWdVQ0RQNHI0QUpHTDBCb0ZUSTM2QUdTZ0hkbnFWY2hHSTUydExPMGtJZmhXN2tjQjlDbWYzWU5jZ1BXaFpwSUF3cjVEV0NmSnRXNjV4OXp1ck1TOTNvbHJOd2RIS0dxNjYzZ3BrVmJXVW5VZGZWcUpSWGZfUnpUcl9TLS0zYURXcjlZc0hiNGgwOE1ZNjQtRFd3cHkxYVBtYmhPbzNBLWwtXzI5dzRISWkwVDZEbQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOY05EeGdVOVhLcWtWZFYySWgxclRJT3dXMUJ4NkdKSjZURFZ2b3dTNnNiZ0hrM1Mtd0tnbXBtRmpEa05hVm5LY0oxWnRUUFVRWGFUc3N5VGJ4TVNwRnRvb09DbldhZFhqWTNOR1dFUFcweW1YLWZ0Nk5iZ0M2N21HSFJpZGJjTE5PYzQyLUFCNlJMYkgteEo5Zw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
