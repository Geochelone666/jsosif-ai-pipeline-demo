# CSU.TO Intelligence Report

- ticker: **CSU.TO**
- Report as_of: **2026-11-23**
- Market data as_of: **2026-11-23**
- Quant sources: https://finance.yahoo.com/quote/CSU.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CSU.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-23**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-24T08:33:41.564144+00:00**
- AI status: **No recent headlines returned by RSS; no AI classification performed**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 0, 'rule': 0, 'ai': 0, 'unknown': 0})
- AI model(s) actually used: **N/A (no successful AI classification call)**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 0 unique headlines; 0 named publishers; 0 exact duplicates; 0 HTTPS source links; largest publisher share None%; oldest publication None

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 3109.1001 |
| Return 1D (%) | 0.4231 |
| Return 1W (%) | -9.5279 |
| Return 1M (%) | -8.4212 |
| Return YTD (%) | -5.6750 |
| Return 1Y (%) | -5.3495 |
| Annualized volatility (%) | 43.8836 |
| Beta vs SPY | 0.0834 |
| Max drawdown (%) | -33.9828 |
| Sharpe (rf=0) | 0.0286 |
| Downside deviation (rf=0, %) | 29.9118 |
| Sortino (rf=0) | 0.0419 |
| Historical VaR 95% (1D, %) | 4.3858 |
| Historical ES 95% (1D, %) | 5.4742 |
| Correlation vs SPY | 0.0284 |
| Tracking error vs SPY (%) | 46.3140 |
| P/E (trailing) | 49.29 |
| P/B | 10.89 |
| EV/EBITDA | 31.11 |
| Revenue growth (%) | 19.10 |
| Forward P/E (estimate) | 16.16 |
| Gross margin (%) | 37.29 |
| Operating margin (%) | 15.65 |
| Return on equity (%) | 24.22 |
| Free cash flow yield (%) | N/A |
| MA50 | 3155.4421 |
| Close vs MA50 (%) | -1.4686 |
| MA200 | 2827.9548 |
| Close vs MA200 (%) | 9.9416 |
| RSI (14, Wilder) | 36.9421 |
| MACD (12,26) | -0.2227 |
| MACD signal (9) | 56.8196 |
| MACD histogram | -57.0423 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CSU.TO': 287, 'SPY': 288}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 3109.1001 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.4231 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -9.5279 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -8.4212 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -5.6750 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -5.3495 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 43.8836 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 29.9118 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.0419 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.3858 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.4742 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0284 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 46.3140 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.0834 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -33.9828 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.0286 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.1634 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 37.2920 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 15.6470 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 24.2210 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 49.2882 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 36.9421 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -57.0423 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -1.4686 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 9.9416 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

No items in this run

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CSU.TO** | **49.29** | **10.89** | **31.11** | **19.10** | **65,886,588,928.00 CAD** | **-5.35** |
| DSG.TO | 44.10 | 4.80 | 32.34 | 11.80 | 11,090,513,920.00 CAD | 12.92 |
| OTEX.TO | 9.18 | 1.36 | 7.97 | -4.00 | 7,985,309,696.00 CAD | -26.07 |
| TOI.V | 34.54 | 8.75 | 26.26 | 14.70 | 20,240,021,504.00 CAD | -25.82 |

Peers fetched as_of: 2026-11-23; CSU.TO reuses existing data (market data as_of: 2026-11-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-05
- Next expected earnings: 2027-03-08 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-23

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



## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
