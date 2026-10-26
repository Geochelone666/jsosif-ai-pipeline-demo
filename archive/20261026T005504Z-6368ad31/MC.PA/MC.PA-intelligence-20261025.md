# MC.PA Intelligence Report

- ticker: **MC.PA**
- Report as_of: **2026-10-25**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/MC.PA/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MC.PA/key-statistics/
- AI analysis snapshot as_of: **2026-10-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-26T01:32:40.227334+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 4, 'rule': 0, 'ai': 1, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 4 unique headlines; 3 named publishers; 0 exact duplicates; 4 HTTPS source links; largest publisher share 50.0%; oldest publication 2026-10-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 383.0000 |
| Return 1D (%) | -1.2377 |
| Return 1W (%) | -3.5264 |
| Return 1M (%) | -3.5021 |
| Return YTD (%) | -39.6519 |
| Return 1Y (%) | -36.7582 |
| Annualized volatility (%) | 26.9642 |
| Beta vs SPY | 0.5917 |
| Max drawdown (%) | -41.0025 |
| Sharpe (rf=0) | -1.5431 |
| Downside deviation (rf=0, %) | 20.5604 |
| Sortino (rf=0) | -2.0237 |
| Historical VaR 95% (1D, %) | 2.7422 |
| Historical ES 95% (1D, %) | 3.9949 |
| Correlation vs SPY | 0.2815 |
| Tracking error vs SPY (%) | 26.3705 |
| P/E (trailing) | 17.46 |
| P/B | 2.77 |
| EV/EBITDA | 10.74 |
| Revenue growth (%) | -2.90 |
| Forward P/E (estimate) | 15.87 |
| Gross margin (%) | 66.36 |
| Operating margin (%) | 22.52 |
| Return on equity (%) | 16.59 |
| Free cash flow yield (%) | 6.11 |
| MA50 | 411.9620 |
| Close vs MA50 (%) | -7.0303 |
| MA200 | 472.2012 |
| Close vs MA200 (%) | -18.8905 |
| RSI (14, Wilder) | 38.2879 |
| MACD (12,26) | -6.5434 |
| MACD signal (9) | -8.4194 |
| MACD histogram | 1.8760 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MC.PA': 271, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 383.0000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.2377 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -3.5264 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -3.5021 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -39.6519 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -36.7582 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 26.9642 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 20.5604 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -2.0237 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.7422 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.9949 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2815 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.3705 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5917 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -41.0025 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -1.5431 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.8659 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 66.3650 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 22.5210 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 16.5860 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 6.1106 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 17.4567 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 38.2879 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.8760 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -7.0303 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -18.8905 -> Clearly below the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

No items in this run

## RISKS

### LVMH (ENXTPA:MC) Faces Fresh France Riot Risk To Tourism And Luxury Demand
- Summary: LVMH warns of potential impact on tourism and luxury demand due to recent France riots.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPRUlEaDV3N3NNeWdFUDJQdEJ1NU50OGNEVmtzbEJuLWlFYU9JXzNOVUhvSkQtdmRlejFNR2Z5ajlkc2pZdnk5dEZqcDZxa0xzZkR3cTh0UHpTZl9XaXBrdEp5WnkwRXczeDJiak9TaUkxR0Rkd0RFbDhWUHNxdDBGeGZ5QTc4bW1XQnVEZjZKVEdpLXcxSnc?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MC.PA** | **17.46** | **2.77** | **10.74** | **-2.90** | **188,805,677,056.00 EUR** | **-36.76** |
| RMS.PA | 28.80 | 6.82 | 16.96 | 1.60 | 129,714,978,816.00 EUR | -42.98 |
| CFR.SW | 29.52 | 4.26 | 17.04 | 4.20 | 94,922,956,800.00 CHF | 2.31 |
| KER.PA | N/A | 1.51 | 12.77 | -2.90 | 21,840,736,256.00 EUR | -47.58 |

Peers fetched as_of: 2026-10-25; MC.PA reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: N/A
- Next expected earnings: 2027-01-26 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-25

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

- https://news.google.com/rss/articles/CBMilgFBVV95cUxPRUlEaDV3N3NNeWdFUDJQdEJ1NU50OGNEVmtzbEJuLWlFYU9JXzNOVUhvSkQtdmRlejFNR2Z5ajlkc2pZdnk5dEZqcDZxa0xzZkR3cTh0UHpTZl9XaXBrdEp5WnkwRXczeDJiak9TaUkxR0Rkd0RFbDhWUHNxdDBGeGZ5QTc4bW1XQnVEZjZKVEdpLXcxSnc?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
