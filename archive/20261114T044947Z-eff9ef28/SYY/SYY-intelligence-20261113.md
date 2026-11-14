# SYY Intelligence Report

- ticker: **SYY**
- Report as_of: **2026-11-13**
- Market data as_of: **2026-11-13**
- Quant sources: https://finance.yahoo.com/quote/SYY/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SYY/key-statistics/
- AI analysis snapshot as_of: **2026-11-13**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-14T05:05:42.007592+00:00**
- AI status: **AI reviewed headlines; none relevant to the requested company**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 5, 'rule': 0, 'ai': 0, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 5 unique headlines; 5 named publishers; 0 exact duplicates; 5 HTTPS source links; largest publisher share 20.0%; oldest publication 2026-11-12

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 77.1000 |
| Return 1D (%) | 1.1280 |
| Return 1W (%) | 0.3123 |
| Return 1M (%) | -2.4421 |
| Return YTD (%) | 7.6597 |
| Return 1Y (%) | 5.6806 |
| Annualized volatility (%) | 29.2170 |
| Beta vs SPY | 0.2338 |
| Max drawdown (%) | -23.9798 |
| Sharpe (rf=0) | 0.3396 |
| Downside deviation (rf=0, %) | 22.3940 |
| Sortino (rf=0) | 0.4431 |
| Historical VaR 95% (1D, %) | 2.1606 |
| Historical ES 95% (1D, %) | 4.3236 |
| Correlation vs SPY | 0.1091 |
| Tracking error vs SPY (%) | 30.8642 |
| P/E (trailing) | 20.29 |
| P/B | 9.38 |
| EV/EBITDA | 11.11 |
| Revenue growth (%) | 2.80 |
| Forward P/E (estimate) | 14.29 |
| Gross margin (%) | 18.54 |
| Operating margin (%) | 4.13 |
| Return on equity (%) | 58.74 |
| Free cash flow yield (%) | 6.34 |
| MA50 | 79.2519 |
| Close vs MA50 (%) | -2.7153 |
| MA200 | 79.4921 |
| Close vs MA200 (%) | -3.0093 |
| RSI (14, Wilder) | 44.5249 |
| MACD (12,26) | -0.9376 |
| MACD signal (9) | -0.5417 |
| MACD histogram | -0.3958 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SYY': 282, 'SPY': 282}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 77.1000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.1280 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.3123 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -2.4421 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 7.6597 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 5.6806 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 29.2170 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 22.3940 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4431 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.1606 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.3236 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1091 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 30.8642 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.2338 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -23.9798 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3396 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 14.2872 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 18.5430 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 4.1330 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 58.7360 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 6.3435 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 20.2895 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 44.5249 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.3958 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -2.7153 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -3.0093 -> Slightly below the moving-average trend level.

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
| **SYY** | **20.29** | **9.38** | **11.11** | **2.80** | **37,954,072,576.00 USD** | **5.68** |
| USFD | 30.21 | 5.37 | 15.02 | 2.10 | 23,283,320,832.00 USD | 50.35 |
| PFGC | 43.77 | 3.43 | 14.41 | 5.50 | 17,540,904,960.00 USD | 16.60 |
| CHEF | 45.58 | 6.34 | 19.74 | 11.20 | 4,635,752,448.00 USD | 79.26 |

Peers fetched as_of: 2026-11-13; SYY reuses existing data (market data as_of: 2026-11-13); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-03
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-13

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 21,744,000,000.00 USD; period 2026-06-28/2026-09-26; fiscal year/reporting period 2027/Q1
- Net income (latest available single quarter): 526,000,000.00 USD; period 2026-06-28/2026-09-26; fiscal year/reporting period 2027/Q1
- SEC link: https://www.sec.gov/Archives/edgar/data/96021/000009602126000050/syy-20260926.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES



## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
