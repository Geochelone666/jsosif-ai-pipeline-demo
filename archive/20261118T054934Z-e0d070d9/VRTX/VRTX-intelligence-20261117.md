# VRTX Intelligence Report

- ticker: **VRTX**
- Report as_of: **2026-11-17**
- Market data as_of: **2026-11-17**
- Quant sources: https://finance.yahoo.com/quote/VRTX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/VRTX/key-statistics/
- AI analysis snapshot as_of: **2026-11-17**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-18T06:06:26.804924+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 5, 'rule': 0, 'ai': 1, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261117T062519Z-6171f6c2/VRTX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 5 unique headlines; 4 named publishers; 0 exact duplicates; 5 HTTPS source links; largest publisher share 40.0%; oldest publication 2026-11-11

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 534.2000 |
| Return 1D (%) | -0.6675 |
| Return 1W (%) | -2.4987 |
| Return 1M (%) | 6.8956 |
| Return YTD (%) | 17.8313 |
| Return 1Y (%) | 23.0819 |
| Annualized volatility (%) | 29.6250 |
| Beta vs SPY | 0.4264 |
| Max drawdown (%) | -15.2113 |
| Sharpe (rf=0) | 0.8502 |
| Downside deviation (rf=0, %) | 18.2714 |
| Sortino (rf=0) | 1.3786 |
| Historical VaR 95% (1D, %) | 2.8866 |
| Historical ES 95% (1D, %) | 3.4957 |
| Correlation vs SPY | 0.1984 |
| Tracking error vs SPY (%) | 30.0928 |
| P/E (trailing) | 34.38 |
| P/B | 6.48 |
| EV/EBITDA | 26.59 |
| Revenue growth (%) | 11.80 |
| Forward P/E (estimate) | 26.82 |
| Gross margin (%) | 54.81 |
| Operating margin (%) | 37.79 |
| Return on equity (%) | 20.80 |
| Free cash flow yield (%) | 1.73 |
| MA50 | 522.3068 |
| Close vs MA50 (%) | 2.2771 |
| MA200 | 483.9928 |
| Close vs MA200 (%) | 10.3735 |
| RSI (14, Wilder) | 50.3844 |
| MACD (12,26) | 5.7818 |
| MACD signal (9) | 7.2253 |
| MACD histogram | -1.4434 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'VRTX': 284, 'SPY': 284}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 534.2000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.6675 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.4987 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 6.8956 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 17.8313 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 23.0819 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 29.6250 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 18.2714 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.3786 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8866 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.4957 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1984 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 30.0928 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.4264 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.2113 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.8502 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 26.8211 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.8090 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 37.7920 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 20.8020 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.7261 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 34.3758 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 50.3844 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.4434 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 2.2771 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 10.3735 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

### What Will Decide Vertex Stock Over The Next Six Months?
- Summary: Analysis of factors likely to influence Vertex stock performance in the next six months.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxOcnVWQ0NDLUY4cTBaRHRQekZxSEJUTGM3bktQYWNKLUJvanRYVl9yWGtWakpsSDZiXzVWZTdTZExNLU9NckNmMmsxS2pydW5tU0NNNmlKbS1CbFNZWjFnWkVyWWdWU01TUjJzQ1E0OGFVTXhpYnB4ajVReHQ3THVnTElxTWJiZ3QwY1BhSDFBWDdLSFA1Z2drMldFS3ZEM1dOdlp4Z3ptSnJiWVNFTS01elNJdFM1dw?oc=5>

## CATALYSTS

No items in this run

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **VRTX** | **34.38** | **6.48** | **26.59** | **11.80** | **135,439,835,136.00 USD** | **23.08** |
| REGN | 21.05 | 2.87 | 15.85 | 36.30 | 99,078,217,728.00 USD | 36.68 |
| BIIB | 108.57 | 1.96 | 13.19 | 10.60 | 37,071,831,040.00 USD | 52.29 |
| AMGN | 26.80 | 17.26 | 16.36 | 8.50 | 247,699,587,072.00 USD | 37.73 |

Peers fetched as_of: 2026-11-17; VRTX reuses existing data (market data as_of: 2026-11-17); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-02
- Next expected earnings: 2027-02-11 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-17

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-03
- Revenue (latest available single quarter): 640,799,000.00 USD; period 2018-01-01/2018-03-31; fiscal year/reporting period 2018/Q1
- Net income (latest available single quarter): 653,600,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/875320/000087532026000291/vrtx-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMitgFBVV95cUxOcnVWQ0NDLUY4cTBaRHRQekZxSEJUTGM3bktQYWNKLUJvanRYVl9yWGtWakpsSDZiXzVWZTdTZExNLU9NckNmMmsxS2pydW5tU0NNNmlKbS1CbFNZWjFnWkVyWWdWU01TUjJzQ1E0OGFVTXhpYnB4ajVReHQ3THVnTElxTWJiZ3QwY1BhSDFBWDdLSFA1Z2drMldFS3ZEM1dOdlp4Z3ptSnJiWVNFTS01elNJdFM1dw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
