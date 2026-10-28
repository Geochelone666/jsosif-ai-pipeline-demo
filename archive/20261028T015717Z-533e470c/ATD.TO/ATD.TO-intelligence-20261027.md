# ATD.TO Intelligence Report

- ticker: **ATD.TO**
- Report as_of: **2026-10-27**
- Market data as_of: **2026-10-27**
- Quant sources: https://finance.yahoo.com/quote/ATD.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ATD.TO/key-statistics/
- AI analysis snapshot as_of: **2026-10-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-28T02:17:41.150268+00:00**
- AI status: **AI reviewed headlines; none relevant to the requested company**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 2, 'rule': 0, 'ai': 0, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 2 unique headlines; 2 named publishers; 0 exact duplicates; 2 HTTPS source links; largest publisher share 50.0%; oldest publication 2026-10-25

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 81.3900 |
| Return 1D (%) | -1.5959 |
| Return 1W (%) | -4.6509 |
| Return 1M (%) | 3.6815 |
| Return YTD (%) | 9.4216 |
| Return 1Y (%) | 11.0571 |
| Annualized volatility (%) | 26.5762 |
| Beta vs SPY | 0.1073 |
| Max drawdown (%) | -17.5708 |
| Sharpe (rf=0) | 0.5265 |
| Downside deviation (rf=0, %) | 16.0014 |
| Sortino (rf=0) | 0.8745 |
| Historical VaR 95% (1D, %) | 2.3429 |
| Historical ES 95% (1D, %) | 3.0441 |
| Correlation vs SPY | 0.0511 |
| Tracking error vs SPY (%) | 29.0849 |
| P/E (trailing) | 17.06 |
| P/B | 3.19 |
| EV/EBITDA | 13.55 |
| Revenue growth (%) | 25.10 |
| Forward P/E (estimate) | 16.12 |
| Gross margin (%) | 18.24 |
| Operating margin (%) | 5.61 |
| Return on equity (%) | 19.61 |
| Free cash flow yield (%) | N/A |
| MA50 | 81.4465 |
| Close vs MA50 (%) | -0.0694 |
| MA200 | 81.7049 |
| Close vs MA200 (%) | -0.3854 |
| RSI (14, Wilder) | 50.0491 |
| MACD (12,26) | 0.7102 |
| MACD signal (9) | 0.2931 |
| MACD histogram | 0.4171 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ATD.TO': 268, 'SPY': 269}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 81.3900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.5959 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -4.6509 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 3.6815 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 9.4216 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 11.0571 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 26.5762 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.0014 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.8745 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.3429 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.0441 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0511 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 29.0849 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.1073 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -17.5708 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.5265 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.1195 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 18.2380 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 5.6110 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 19.6150 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 17.0629 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 50.0491 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.4171 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -0.0694 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -0.3854 -> Slightly below the moving-average trend level.

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
| **ATD.TO** | **17.06** | **3.19** | **13.55** | **25.10** | **74,712,973,312.00 CAD** | **11.06** |
| CASY | 33.60 | 6.30 | 17.99 | 24.30 | 25,781,194,752.00 USD | 30.60 |
| MUSA | 16.21 | 12.47 | 10.03 | 40.80 | 9,761,986,560.00 USD | 35.55 |
| SUN | 16.10 | 1.46 | 8.83 | 164.50 | 13,742,907,392.00 USD | 43.57 |

Peers fetched as_of: 2026-10-27; ATD.TO reuses existing data (market data as_of: 2026-10-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-01
- Next expected earnings: 2026-11-23 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-27

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
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
