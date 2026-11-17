# JWEL.TO Intelligence Report

- ticker: **JWEL.TO**
- Report as_of: **2026-11-16**
- Market data as_of: **2026-11-16**
- Quant sources: https://finance.yahoo.com/quote/JWEL.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/JWEL.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-16**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-17T06:32:02.008610+00:00**
- AI status: **N/A: RSS source unavailable (news.google.com returned an HTTP error (rate limited, service error, or request rejected)), gave up after 3 attempts. Skipping news analysis for this round; quantitative metrics unaffected.**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 0, 'rule': 0, 'ai': 0, 'unknown': 0})
- AI model(s) actually used: **N/A (no successful AI classification call)**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 0 unique headlines; 0 named publishers; 0 exact duplicates; 0 HTTPS source links; largest publisher share None%; oldest publication None

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 45.7100 |
| Return 1D (%) | 0.0438 |
| Return 1W (%) | 0.1534 |
| Return 1M (%) | 0.5499 |
| Return YTD (%) | 38.3540 |
| Return 1Y (%) | 32.2040 |
| Annualized volatility (%) | 21.5657 |
| Beta vs SPY | 0.2101 |
| Max drawdown (%) | -14.6220 |
| Sharpe (rf=0) | 1.4805 |
| Downside deviation (rf=0, %) | 10.5466 |
| Sortino (rf=0) | 3.0273 |
| Historical VaR 95% (1D, %) | 1.5453 |
| Historical ES 95% (1D, %) | 2.0798 |
| Correlation vs SPY | 0.1338 |
| Tracking error vs SPY (%) | 24.1498 |
| P/E (trailing) | 24.84 |
| P/B | 3.72 |
| EV/EBITDA | 16.40 |
| Revenue growth (%) | 17.40 |
| Forward P/E (estimate) | 18.49 |
| Gross margin (%) | 41.88 |
| Operating margin (%) | 14.83 |
| Return on equity (%) | 15.25 |
| Free cash flow yield (%) | -0.39 |
| MA50 | 45.5038 |
| Close vs MA50 (%) | 0.4531 |
| MA200 | 39.5111 |
| Close vs MA200 (%) | 15.6891 |
| RSI (14, Wilder) | 72.3160 |
| MACD (12,26) | 0.0788 |
| MACD signal (9) | 0.0782 |
| MACD histogram | 0.0006 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'JWEL.TO': 282, 'SPY': 283}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 45.7100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.0438 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.1534 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 0.5499 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 38.3540 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 32.2040 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 21.5657 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 10.5466 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 3.0273 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.5453 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.0798 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1338 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.1498 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.2101 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -14.6220 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.4805 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 18.4861 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 41.8790 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 14.8310 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 15.2460 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: -0.3944 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 24.8424 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 72.3160 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.0006 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 0.4531 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 15.6891 -> Clearly above the moving-average trend level.

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
| **JWEL.TO** | **24.84** | **3.72** | **16.40** | **17.40** | **1,896,550,784.00 CAD** | **32.20** |
| HLF | 9.50 | -4.13 | 5.34 | 6.00 | 1,694,066,816.00 USD | 74.97 |
| USNA | N/A | 0.47 | 1.61 | -3.60 | 250,337,696.00 USD | -29.44 |
| NATR | 12.88 | 1.07 | 2.96 | -9.10 | 182,991,888.00 USD | -50.12 |

Peers fetched as_of: 2026-11-16; JWEL.TO reuses existing data (market data as_of: 2026-11-16); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-16
- Next expected earnings: N/A (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-16

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
