# MG.TO Intelligence Report

- ticker: **MG.TO**
- Report as_of: **2026-11-05**
- Market data as_of: **2026-11-05**
- Quant sources: https://finance.yahoo.com/quote/MG.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MG.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-05**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-06T05:02:18.809138+00:00**
- AI status: **AI reviewed headlines; none relevant to the requested company**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 2, 'rule': 0, 'ai': 0, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 2 unique headlines; 2 named publishers; 0 exact duplicates; 2 HTTPS source links; largest publisher share 50.0%; oldest publication 2026-11-02

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 88.0100 |
| Return 1D (%) | -3.9821 |
| Return 1W (%) | -2.5468 |
| Return 1M (%) | -4.9773 |
| Return YTD (%) | 23.0395 |
| Return 1Y (%) | 28.9641 |
| Annualized volatility (%) | 37.0367 |
| Beta vs SPY | 1.1378 |
| Max drawdown (%) | -22.7904 |
| Sharpe (rf=0) | 0.8689 |
| Downside deviation (rf=0, %) | 21.6388 |
| Sortino (rf=0) | 1.4872 |
| Historical VaR 95% (1D, %) | 2.8821 |
| Historical ES 95% (1D, %) | 4.1438 |
| Correlation vs SPY | 0.4160 |
| Tracking error vs SPY (%) | 34.0198 |
| P/E (trailing) | 19.82 |
| P/B | 1.42 |
| EV/EBITDA | 6.99 |
| Revenue growth (%) | -3.90 |
| Forward P/E (estimate) | 7.98 |
| Gross margin (%) | 14.27 |
| Operating margin (%) | 5.49 |
| Return on equity (%) | N/A |
| Free cash flow yield (%) | N/A |
| MA50 | 90.8946 |
| Close vs MA50 (%) | -3.1736 |
| MA200 | 86.5660 |
| Close vs MA200 (%) | 1.6681 |
| RSI (14, Wilder) | 43.9421 |
| MACD (12,26) | -0.6001 |
| MACD signal (9) | -0.4391 |
| MACD histogram | -0.1610 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MG.TO': 275, 'SPY': 276}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 88.0100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -3.9821 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.5468 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -4.9773 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 23.0395 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 28.9641 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 37.0367 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.6388 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.4872 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8821 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.1438 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4160 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 34.0198 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.1378 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -22.7904 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.8689 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 7.9775 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 14.2730 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 5.4880 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 19.8221 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 43.9421 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.1610 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -3.1736 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 1.6681 -> Slightly above the moving-average trend level.

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
| **MG.TO** | **19.82** | **1.42** | **6.99** | **-3.90** | **22,852,390,912.00 CAD** | **28.96** |
| APTV | 12.09 | 0.95 | 4.15 | 2.30 | 8,269,268,480.00 USD | -51.14 |
| BWA | 21.31 | 1.68 | 5.59 | -2.90 | 9,544,691,712.00 USD | 7.18 |
| LEA | 10.34 | 1.10 | 4.87 | 1.60 | 5,498,711,552.00 USD | 7.19 |

Peers fetched as_of: 2026-11-05; MG.TO reuses existing data (market data as_of: 2026-11-05); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-30
- Next expected earnings: 2027-02-12 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-05

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
