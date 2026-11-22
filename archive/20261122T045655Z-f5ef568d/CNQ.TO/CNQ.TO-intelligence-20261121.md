# CNQ.TO Intelligence Report

- ticker: **CNQ.TO**
- Report as_of: **2026-11-21**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/CNQ.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CNQ.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-21**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-22T05:05:53.731430+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 5, 'rule': 2, 'ai': 0, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261121T053104Z-422ce34b/CNQ.TO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 5 unique headlines; 4 named publishers; 0 exact duplicates; 5 HTTPS source links; largest publisher share 40.0%; oldest publication 2026-11-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 63.7400 |
| Return 1D (%) | -0.5616 |
| Return 1W (%) | -10.1114 |
| Return 1M (%) | -16.3846 |
| Return YTD (%) | 41.0818 |
| Return 1Y (%) | 38.7168 |
| Annualized volatility (%) | 32.1823 |
| Beta vs SPY | -0.4558 |
| Max drawdown (%) | -18.7197 |
| Sharpe (rf=0) | 1.1831 |
| Downside deviation (rf=0, %) | 22.9668 |
| Sortino (rf=0) | 1.6578 |
| Historical VaR 95% (1D, %) | 3.4582 |
| Historical ES 95% (1D, %) | 4.8736 |
| Correlation vs SPY | -0.2031 |
| Tracking error vs SPY (%) | 37.8804 |
| P/E (trailing) | 9.40 |
| P/B | 2.78 |
| EV/EBITDA | 6.49 |
| Revenue growth (%) | 34.40 |
| Forward P/E (estimate) | 10.68 |
| Gross margin (%) | 52.92 |
| Operating margin (%) | 30.67 |
| Return on equity (%) | 32.38 |
| Free cash flow yield (%) | 9.39 |
| MA50 | 70.8202 |
| Close vs MA50 (%) | -9.9974 |
| MA200 | 64.3541 |
| Close vs MA200 (%) | -0.9543 |
| RSI (14, Wilder) | 29.3607 |
| MACD (12,26) | -1.9039 |
| MACD signal (9) | -0.9721 |
| MACD histogram | -0.9318 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CNQ.TO': 286, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 63.7400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.5616 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -10.1114 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -16.3846 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 41.0818 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 38.7168 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 32.1823 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 22.9668 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.6578 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.4582 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.8736 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.2031 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.8804 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.4558 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -18.7197 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1831 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 10.6793 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 52.9160 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 30.6740 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 32.3850 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 9.3878 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 9.4012 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 29.3607 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.9318 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -9.9974 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -0.9543 -> Slightly below the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Canadian Natural Resources Has Raised Its Dividend for 26 Straight Years: Here’s Why It Stands Out
- Summary: Canadian Natural Resources Has Raised Its Dividend for 26 Straight Years: Here’s Why It Stands Out
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQOVdQN01mT0JXNFJJVDdlYXFFMjdUemhDRmhIRG5qb2xzU2wyOU43VTRFLUhyZVBqN2NhUTdsUTl6OTU2M0dSRnZIZ1YzNXFSaTRYRkEwdnh0QllRc3RySlpyc0ZOMGprU2NFRVJPc3hhNEFFOTB5UndHR05reDNoREstS1cxNlJOYnVkZmZXenUydV9LUFE?oc=5>

### Canadian Natural Resources (TSX:CNQ) Plans To Acquire Advantage Energy
- Summary: Canadian Natural Resources (TSX:CNQ) Plans To Acquire Advantage Energy
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNTUx0b0dyamljMVYwb3VDZ2pKT2VLd0NKbi1yNFJBSnZrYXMteXFfTWN5b2d3eWFoS1VaM2RfSk1JRWxLNVhmamY0TlVFR1JmZHFWR3NZeGpSZXJjTEFRYURueEVXbDFqTGxEa2ZRNDRRQm12YlZaTWg2U18tQl91d01LVUtkcXZpWnFfd0JLVEM1SGxvWkE?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CNQ.TO** | **9.40** | **2.78** | **6.49** | **34.40** | **129,719,189,504.00 CAD** | **38.72** |
| SU.TO | 9.73 | 2.14 | 4.82 | 50.40 | 105,429,114,880.00 CAD | 49.89 |
| IMO.TO | 13.26 | 3.22 | 7.80 | 34.90 | 78,693,810,176.00 CAD | 23.14 |
| CVE.TO | 8.27 | 1.99 | 4.43 | 21.10 | 70,250,610,688.00 CAD | 56.36 |

Peers fetched as_of: 2026-11-21; CNQ.TO reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-05
- Next expected earnings: 2027-03-04 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-21

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

- https://news.google.com/rss/articles/CBMilgFBVV95cUxQOVdQN01mT0JXNFJJVDdlYXFFMjdUemhDRmhIRG5qb2xzU2wyOU43VTRFLUhyZVBqN2NhUTdsUTl6OTU2M0dSRnZIZ1YzNXFSaTRYRkEwdnh0QllRc3RySlpyc0ZOMGprU2NFRVJPc3hhNEFFOTB5UndHR05reDNoREstS1cxNlJOYnVkZmZXenUydV9LUFE?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNTUx0b0dyamljMVYwb3VDZ2pKT2VLd0NKbi1yNFJBSnZrYXMteXFfTWN5b2d3eWFoS1VaM2RfSk1JRWxLNVhmamY0TlVFR1JmZHFWR3NZeGpSZXJjTEFRYURueEVXbDFqTGxEa2ZRNDRRQm12YlZaTWg2U18tQl91d01LVUtkcXZpWnFfd0JLVEM1SGxvWkE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
