# MC.PA Intelligence Report

- ticker: **MC.PA**
- Report as_of: **2026-11-08**
- Market data as_of: **2026-11-06**
- Quant sources: https://finance.yahoo.com/quote/MC.PA/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MC.PA/key-statistics/
- AI analysis snapshot as_of: **2026-11-08**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-09T04:51:42.429179+00:00**
- AI status: **AI reviewed headlines; none relevant to the requested company**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 3, 'rule': 0, 'ai': 0, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261108T041758Z-43fb2458/MC.PA** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 3 unique headlines; 2 named publishers; 0 exact duplicates; 3 HTTPS source links; largest publisher share 66.67%; oldest publication 2026-11-04

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 408.7500 |
| Return 1D (%) | -2.3647 |
| Return 1W (%) | 5.6202 |
| Return 1M (%) | 6.0036 |
| Return YTD (%) | -35.5946 |
| Return 1Y (%) | -30.1665 |
| Annualized volatility (%) | 27.3514 |
| Beta vs SPY | 0.5061 |
| Max drawdown (%) | -41.0025 |
| Sharpe (rf=0) | -1.1598 |
| Downside deviation (rf=0, %) | 20.4979 |
| Sortino (rf=0) | -1.5475 |
| Historical VaR 95% (1D, %) | 2.7422 |
| Historical ES 95% (1D, %) | 3.9949 |
| Correlation vs SPY | 0.2523 |
| Tracking error vs SPY (%) | 27.2895 |
| P/E (trailing) | 18.63 |
| P/B | 2.96 |
| EV/EBITDA | 11.37 |
| Revenue growth (%) | -2.90 |
| Forward P/E (estimate) | 17.07 |
| Gross margin (%) | 66.36 |
| Operating margin (%) | 22.52 |
| Return on equity (%) | 16.59 |
| Free cash flow yield (%) | 5.75 |
| MA50 | 401.0330 |
| Close vs MA50 (%) | 1.9243 |
| MA200 | 462.6461 |
| Close vs MA200 (%) | -11.6495 |
| RSI (14, Wilder) | 58.5360 |
| MACD (12,26) | 2.2723 |
| MACD signal (9) | -2.1113 |
| MACD histogram | 4.3836 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MC.PA': 281, 'SPY': 277}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 408.7500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.3647 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 5.6202 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 6.0036 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -35.5946 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -30.1665 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 27.3514 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 20.4979 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -1.5475 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.7422 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.9949 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2523 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 27.2895 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5061 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -41.0025 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -1.1598 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.0729 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 66.3650 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 22.5210 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 16.5860 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 5.7529 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 18.6304 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 58.5360 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 4.3836 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 1.9243 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -11.6495 -> Clearly below the moving-average trend level.

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
| **MC.PA** | **18.63** | **2.96** | **11.37** | **-2.90** | **200,545,091,584.00 EUR** | **-30.17** |
| RMS.PA | 31.69 | 7.50 | 18.80 | 1.60 | 142,702,182,400.00 EUR | -32.64 |
| CFR.SW | 31.01 | 4.48 | 17.94 | 4.20 | 99,744,063,488.00 CHF | 11.25 |
| KER.PA | N/A | 1.59 | 13.21 | -2.90 | 22,960,328,704.00 EUR | -34.78 |

Peers fetched as_of: 2026-11-08; MC.PA reuses existing data (market data as_of: 2026-11-06); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: N/A
- Next expected earnings: 2027-01-26 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-08

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
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
