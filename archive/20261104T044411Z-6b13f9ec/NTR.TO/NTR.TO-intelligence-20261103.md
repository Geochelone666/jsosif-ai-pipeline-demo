# NTR.TO Intelligence Report

- ticker: **NTR.TO**
- Report as_of: **2026-11-03**
- Market data as_of: **2026-11-03**
- Quant sources: https://finance.yahoo.com/quote/NTR.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NTR.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-03**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-04T05:05:09.134887+00:00**
- AI status: **AI reviewed headlines; none relevant to the requested company**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 6, 'rule': 0, 'ai': 0, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 6 unique headlines; 5 named publishers; 1 exact duplicates; 6 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-10-27

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 97.0700 |
| Return 1D (%) | -1.1507 |
| Return 1W (%) | -0.4002 |
| Return 1M (%) | -2.9009 |
| Return YTD (%) | 17.3484 |
| Return 1Y (%) | 30.7924 |
| Annualized volatility (%) | 32.0425 |
| Beta vs SPY | -0.3340 |
| Max drawdown (%) | -24.3405 |
| Sharpe (rf=0) | 1.0011 |
| Downside deviation (rf=0, %) | 21.6169 |
| Sortino (rf=0) | 1.4839 |
| Historical VaR 95% (1D, %) | 3.0027 |
| Historical ES 95% (1D, %) | 4.2740 |
| Correlation vs SPY | -0.1326 |
| Tracking error vs SPY (%) | 36.3691 |
| P/E (trailing) | 14.05 |
| P/B | 1.28 |
| EV/EBITDA | 10.29 |
| Revenue growth (%) | 4.00 |
| Forward P/E (estimate) | 13.53 |
| Gross margin (%) | 32.06 |
| Operating margin (%) | 17.46 |
| Return on equity (%) | 9.44 |
| Free cash flow yield (%) | N/A |
| MA50 | 102.0451 |
| Close vs MA50 (%) | -4.8754 |
| MA200 | 97.3486 |
| Close vs MA200 (%) | -0.2861 |
| RSI (14, Wilder) | 45.2116 |
| MACD (12,26) | -1.2374 |
| MACD signal (9) | -1.3832 |
| MACD histogram | 0.1458 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NTR.TO': 273, 'SPY': 274}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 97.0700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.1507 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.4002 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -2.9009 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 17.3484 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 30.7924 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 32.0425 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.6169 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.4839 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.0027 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.2740 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1326 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 36.3691 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.3340 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -24.3405 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.0011 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 13.5345 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 32.0620 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 17.4570 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.4400 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 14.0478 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 45.2116 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.1458 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -4.8754 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -0.2861 -> Slightly below the moving-average trend level.

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
| **NTR.TO** | **14.05** | **1.28** | **10.29** | **4.00** | **46,322,782,208.00 CAD** | **30.79** |
| MOS | N/A | 0.51 | 6.87 | -6.00 | 5,855,638,016.00 USD | -29.95 |
| CF | 8.67 | 3.08 | 5.68 | 17.60 | 17,677,805,568.00 USD | 41.25 |
| IPI | 32.71 | 0.79 | 3.53 | -1.50 | 413,792,736.00 USD | 17.01 |

Peers fetched as_of: 2026-11-03; NTR.TO reuses existing data (market data as_of: 2026-11-03); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-05
- Next expected earnings: 2026-11-04 (yfinance; expected dates may change)

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



## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
