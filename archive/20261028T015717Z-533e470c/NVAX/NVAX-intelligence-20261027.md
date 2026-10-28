# NVAX Intelligence Report

- ticker: **NVAX**
- Report as_of: **2026-10-27**
- Market data as_of: **2026-10-27**
- Quant sources: https://finance.yahoo.com/quote/NVAX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVAX/key-statistics/
- AI analysis snapshot as_of: **2026-10-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-28T02:07:00.714477+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 2, 'rule': 1, 'ai': 0, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **N/A (no successful AI classification call)**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261027T014607Z-b66f6bd5/NVAX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 2 unique headlines; 1 named publishers; 0 exact duplicates; 2 HTTPS source links; largest publisher share 100.0%; oldest publication 2026-10-21

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 10.0200 |
| Return 1D (%) | 6.5958 |
| Return 1W (%) | -12.3360 |
| Return 1M (%) | -5.7385 |
| Return YTD (%) | 49.1072 |
| Return 1Y (%) | 15.1724 |
| Annualized volatility (%) | 70.8742 |
| Beta vs SPY | 1.9961 |
| Max drawdown (%) | -34.5844 |
| Sharpe (rf=0) | 0.5413 |
| Downside deviation (rf=0, %) | 41.6938 |
| Sortino (rf=0) | 0.9201 |
| Historical VaR 95% (1D, %) | 5.9349 |
| Historical ES 95% (1D, %) | 7.7057 |
| Correlation vs SPY | 0.3577 |
| Tracking error vs SPY (%) | 67.3830 |
| P/E (trailing) | N/A |
| P/B | -8.66 |
| EV/EBITDA | -12.12 |
| Revenue growth (%) | -76.30 |
| Forward P/E (estimate) | N/A |
| Gross margin (%) | -2.56 |
| Operating margin (%) | -89.61 |
| Return on equity (%) | N/A |
| Free cash flow yield (%) | 9.28 |
| MA50 | 10.3450 |
| Close vs MA50 (%) | -3.1416 |
| MA200 | 9.2633 |
| Close vs MA200 (%) | 8.1682 |
| RSI (14, Wilder) | 44.0745 |
| MACD (12,26) | -0.1029 |
| MACD signal (9) | 0.2420 |
| MACD histogram | -0.3449 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVAX': 269, 'SPY': 269}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 10.0200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 6.5958 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -12.3360 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -5.7385 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 49.1072 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 15.1724 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 70.8742 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 41.6938 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.9201 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 5.9349 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 7.7057 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3577 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 67.3830 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.9961 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -34.5844 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.5413 -> Modest risk-adjusted return.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: -2.5580 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: -89.6080 -> No interpretation rule is available for this metric.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 9.2811 -> No interpretation rule is available for this metric.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 44.0745 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.3449 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -3.1416 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 8.1682 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

### Novavax (NVAX) Stock Falls Amid Market Uptick: What Investors Need to Know
- Summary: Novavax (NVAX) Stock Falls Amid Market Uptick: What Investors Need to Know
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOX01Na1ozU085VFhKMlVzUndqOEVXdURuYTh0b2djRU9vc2VybXJfa1F6SGZjcUh1YnJMdkVHMmVXbDFtc09nN1FleTUtYWxpSHU0SERIOFpTUV91ZFlqNnBoaXNHWWg3ZUlrTHhNZjY1LVpBVVJfVExocVBLbDduY2I4aWozeDdMd2U5emxmMzRHcDZpcW1MZUpB?oc=5>

## CATALYSTS

No items in this run

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVAX** | **N/A** | **-8.66** | **-12.12** | **-76.30** | **1,652,756,224.00 USD** | **15.17** |
| MRNA | N/A | 12.27 | -36.07 | 2.10 | 83,029,090,304.00 USD | 680.08 |
| BNTX | N/A | 1.10 | -6.32 | -59.50 | 21,869,852,672.00 USD | -17.91 |
| GSK | 16.07 | 4.32 | 10.79 | 5.30 | 102,059,065,344.00 USD | 20.42 |

Peers fetched as_of: 2026-10-27; NVAX reuses existing data (market data as_of: 2026-10-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-06
- Next expected earnings: 2026-11-05 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-27

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-06
- Revenue (latest available single quarter): 56,698,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): -53,387,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1000694/000100069426000018/nvax-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimgFBVV95cUxOX01Na1ozU085VFhKMlVzUndqOEVXdURuYTh0b2djRU9vc2VybXJfa1F6SGZjcUh1YnJMdkVHMmVXbDFtc09nN1FleTUtYWxpSHU0SERIOFpTUV91ZFlqNnBoaXNHWWg3ZUlrTHhNZjY1LVpBVVJfVExocVBLbDduY2I4aWozeDdMd2U5emxmMzRHcDZpcW1MZUpB?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
