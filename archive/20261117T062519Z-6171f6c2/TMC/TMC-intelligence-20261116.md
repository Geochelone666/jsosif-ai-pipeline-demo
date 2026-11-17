# TMC Intelligence Report

- ticker: **TMC**
- Report as_of: **2026-11-16**
- Market data as_of: **2026-11-16**
- Quant sources: https://finance.yahoo.com/quote/TMC/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TMC/key-statistics/
- AI analysis snapshot as_of: **2026-11-16**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-17T06:41:44.900085+00:00**
- AI status: **N/A: RSS source unavailable (news.google.com returned an HTTP error (rate limited, service error, or request rejected)), gave up after 3 attempts. Skipping news analysis for this round; quantitative metrics unaffected.**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 0, 'rule': 0, 'ai': 0, 'unknown': 0})
- AI model(s) actually used: **N/A (no successful AI classification call)**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 0 unique headlines; 0 named publishers; 0 exact duplicates; 0 HTTPS source links; largest publisher share None%; oldest publication None

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 2.1100 |
| Return 1D (%) | -8.6580 |
| Return 1W (%) | -19.4656 |
| Return 1M (%) | -18.2171 |
| Return YTD (%) | -65.8023 |
| Return 1Y (%) | -58.4646 |
| Annualized volatility (%) | 94.4225 |
| Beta vs SPY | 3.4781 |
| Max drawdown (%) | -78.0720 |
| Sharpe (rf=0) | -0.4311 |
| Downside deviation (rf=0, %) | 63.0476 |
| Sortino (rf=0) | -0.6457 |
| Historical VaR 95% (1D, %) | 8.9088 |
| Historical ES 95% (1D, %) | 11.8344 |
| Correlation vs SPY | 0.5071 |
| Tracking error vs SPY (%) | 88.2423 |
| P/E (trailing) | N/A |
| P/B | -26.71 |
| EV/EBITDA | -4.46 |
| Revenue growth (%) | N/A |
| Forward P/E (estimate) | N/A |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 0.00 |
| Return on equity (%) | -1123.19 |
| Free cash flow yield (%) | 1.74 |
| MA50 | 3.1589 |
| Close vs MA50 (%) | -33.2046 |
| MA200 | 4.5933 |
| Close vs MA200 (%) | -54.0640 |
| RSI (14, Wilder) | 35.1270 |
| MACD (12,26) | -0.2475 |
| MACD signal (9) | -0.2726 |
| MACD histogram | 0.0251 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TMC': 283, 'SPY': 283}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 2.1100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -8.6580 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -19.4656 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -18.2171 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -65.8023 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -58.4646 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 94.4225 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 63.0476 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.6457 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 8.9088 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 11.8344 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5071 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 88.2423 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.4781 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -78.0720 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.4311 -> Negative risk-adjusted return.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: -1123.1911 -> Adjusted price fell over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.7403 -> No interpretation rule is available for this metric.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 35.1270 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.0251 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -33.2046 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -54.0640 -> Clearly below the moving-average trend level.

## TAILWINDS

N/A: RSS source unavailable (news.google.com returned an HTTP error (rate limited, service error, or request rejected)), gave up after 3 attempts. Skipping news analysis for this round; quantitative metrics unaffected.

## HEADWINDS

N/A: RSS source unavailable (news.google.com returned an HTTP error (rate limited, service error, or request rejected)), gave up after 3 attempts. Skipping news analysis for this round; quantitative metrics unaffected.

## CATALYSTS

N/A: RSS source unavailable (news.google.com returned an HTTP error (rate limited, service error, or request rejected)), gave up after 3 attempts. Skipping news analysis for this round; quantitative metrics unaffected.

## RISKS

N/A: RSS source unavailable (news.google.com returned an HTTP error (rate limited, service error, or request rejected)), gave up after 3 attempts. Skipping news analysis for this round; quantitative metrics unaffected.

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TMC** | **N/A** | **-26.71** | **-4.46** | **N/A** | **1,194,245,120.00 USD** | **-58.46** |
| MP | N/A | 3.30 | 104.18 | 190.90 | 6,433,691,136.00 USD | -38.45 |
| LAC | 4.27 | 0.34 | -22.71 | N/A | 532,041,984.00 USD | -68.39 |
| VALE | 65.38 | 1.15 | 1.90 | -3.90 | 44,515,287,040.00 USD | -7.90 |

Peers fetched as_of: 2026-11-16; TMC reuses existing data (market data as_of: 2026-11-16); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-12
- Next expected earnings: 2027-03-25 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-16

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-12
- Revenue (latest available single quarter): 410,000.00 USD; period 2024-04-01/2024-06-30; fiscal year/reporting period 2024/Q2
- Net income (latest available single quarter): -28,361,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1798562/000162828026073463/tmc-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES



## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
