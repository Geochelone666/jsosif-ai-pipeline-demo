# MC.PA Intelligence Report

- ticker: **MC.PA**
- Report as_of: **2026-11-20**
- Market data as_of: **2026-11-19**
- Quant sources: https://finance.yahoo.com/quote/MC.PA/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MC.PA/key-statistics/
- AI analysis snapshot as_of: **2026-11-20**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-21T05:55:23.727549+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 3, 'rule': 0, 'ai': 2, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261120T053808Z-e360129e/MC.PA** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'directional_claim_without_event_type': 2}
- RSS source audit (metadata only, not article fact-checking): 3 unique headlines; 3 named publishers; 0 exact duplicates; 3 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-11-15

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 391.9000 |
| Return 1D (%) | 0.9791 |
| Return 1W (%) | -3.1628 |
| Return 1M (%) | 0.4872 |
| Return YTD (%) | -38.2496 |
| Return 1Y (%) | -34.0997 |
| Annualized volatility (%) | 27.0445 |
| Beta vs SPY | 0.4154 |
| Max drawdown (%) | -41.0025 |
| Sharpe (rf=0) | -1.3875 |
| Downside deviation (rf=0, %) | 20.5124 |
| Sortino (rf=0) | -1.8293 |
| Historical VaR 95% (1D, %) | 2.7546 |
| Historical ES 95% (1D, %) | 3.9949 |
| Correlation vs SPY | 0.2148 |
| Tracking error vs SPY (%) | 27.6219 |
| P/E (trailing) | 17.41 |
| P/B | 2.77 |
| EV/EBITDA | 10.71 |
| Revenue growth (%) | -2.90 |
| Forward P/E (estimate) | 15.98 |
| Gross margin (%) | 66.36 |
| Operating margin (%) | 21.82 |
| Return on equity (%) | 16.59 |
| Free cash flow yield (%) | 6.16 |
| MA50 | 395.4080 |
| Close vs MA50 (%) | -0.8872 |
| MA200 | 456.7668 |
| Close vs MA200 (%) | -14.2013 |
| RSI (14, Wilder) | 44.8989 |
| MACD (12,26) | -0.1068 |
| MACD signal (9) | 0.8826 |
| MACD histogram | -0.9894 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MC.PA': 290, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 391.9000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.9791 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -3.1628 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 0.4872 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -38.2496 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -34.0997 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 27.0445 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 20.5124 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -1.8293 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.7546 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.9949 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2148 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 27.6219 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.4154 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -41.0025 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -1.3875 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.9780 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 66.3650 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 21.8230 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 16.5860 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 6.1565 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 17.4088 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 44.8989 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.9894 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -0.8872 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -14.2013 -> Clearly below the moving-average trend level.

## TAILWINDS

### LVMH Moët Hennessy - Louis Vuitton, Société Européenne (MC.PA) Stock Price, News, Quote & History
- Summary: Provides current stock price and historical data for LVMH.
- Date: 2026-11-20 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiU0FVX3lxTE4zcUc3akR5ZE9ZbkZKRE5HVFA0OHpSXzJfZ0NGaVFjbUNWX3hjdG03MnlqRUNNSjk0THJYdlNJM2lrN0FHNlV0SUdFNlVQV1FvRkVJ?oc=5>

## HEADWINDS

### LVMH (ENXTPA:MC) Stock Could Be 11% Undervalued On Cash Flow Strength
- Summary: Suggests LVMH stock may be undervalued based on cash flow analysis.
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOdmFuQnlPM1d5ZmNuWU52MjBXZ3VVUnJlNUY5VjU0SnU5Um5tLUplbmRoTnppM0E4R2pBTWt1eXoxVWVUdjd0anhmTXBjVHpEZjdxVEQ1elhBeFhrQ3Rrc2RwMnlpVGFPZGJ1azAwcTUwM0tLVGN3MFNfcDJ1SGhINVlGa3RpYWlJMWFfazhaNEVkS3F6c0E?oc=5>

## CATALYSTS

No items in this run

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MC.PA** | **17.41** | **2.77** | **10.71** | **-2.90** | **187,396,194,304.00 EUR** | **-34.10** |
| RMS.PA | 28.50 | 6.75 | 16.77 | 1.60 | 128,190,955,520.00 EUR | -39.11 |
| CFR.SW | 26.91 | 4.59 | 15.73 | 15.70 | 99,361,906,688.00 CHF | 5.02 |
| KER.PA | N/A | 1.46 | 12.49 | -2.90 | 21,134,759,936.00 EUR | -38.65 |

Peers fetched as_of: 2026-11-20; MC.PA reuses existing data (market data as_of: 2026-11-19); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: N/A
- Next expected earnings: 2027-01-26 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-20

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

- https://news.google.com/rss/articles/CBMiU0FVX3lxTE4zcUc3akR5ZE9ZbkZKRE5HVFA0OHpSXzJfZ0NGaVFjbUNWX3hjdG03MnlqRUNNSjk0THJYdlNJM2lrN0FHNlV0SUdFNlVQV1FvRkVJ?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOdmFuQnlPM1d5ZmNuWU52MjBXZ3VVUnJlNUY5VjU0SnU5Um5tLUplbmRoTnppM0E4R2pBTWt1eXoxVWVUdjd0anhmTXBjVHpEZjdxVEQ1elhBeFhrQ3Rrc2RwMnlpVGFPZGJ1azAwcTUwM0tLVGN3MFNfcDJ1SGhINVlGa3RpYWlJMWFfazhaNEVkS3F6c0E?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
