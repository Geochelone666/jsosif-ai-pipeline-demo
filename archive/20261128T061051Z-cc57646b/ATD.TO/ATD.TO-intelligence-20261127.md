# ATD.TO Intelligence Report

- ticker: **ATD.TO**
- Report as_of: **2026-11-27**
- Market data as_of: **2026-11-27**
- Quant sources: https://finance.yahoo.com/quote/ATD.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ATD.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-28T06:16:53.219508+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 3, 'rule': 0, 'ai': 2, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261127T063646Z-c0c26981/ATD.TO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 3 unique headlines; 3 named publishers; 0 exact duplicates; 3 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-11-24

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 85.4800 |
| Return 1D (%) | -1.6793 |
| Return 1W (%) | 4.6011 |
| Return 1M (%) | 5.0252 |
| Return YTD (%) | 14.9202 |
| Return 1Y (%) | 13.0808 |
| Annualized volatility (%) | 25.9406 |
| Beta vs SPY | 0.0978 |
| Max drawdown (%) | -17.5708 |
| Sharpe (rf=0) | 0.6029 |
| Downside deviation (rf=0, %) | 15.4874 |
| Sortino (rf=0) | 1.0099 |
| Historical VaR 95% (1D, %) | 2.2683 |
| Historical ES 95% (1D, %) | 2.9356 |
| Correlation vs SPY | 0.0565 |
| Tracking error vs SPY (%) | 29.4001 |
| P/E (trailing) | 17.77 |
| P/B | 3.35 |
| EV/EBITDA | 13.98 |
| Revenue growth (%) | 26.20 |
| Forward P/E (estimate) | 16.96 |
| Gross margin (%) | 17.38 |
| Operating margin (%) | 5.60 |
| Return on equity (%) | 19.24 |
| Free cash flow yield (%) | N/A |
| MA50 | 81.3356 |
| Close vs MA50 (%) | 5.0954 |
| MA200 | 82.6223 |
| Close vs MA200 (%) | 3.4588 |
| RSI (14, Wilder) | 58.2489 |
| MACD (12,26) | 0.9035 |
| MACD signal (9) | 0.5899 |
| MACD histogram | 0.3135 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ATD.TO': 291, 'SPY': 291}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 85.4800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.6793 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 4.6011 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 5.0252 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 14.9202 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 13.0808 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 25.9406 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 15.4874 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.0099 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.2683 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.9356 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0565 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 29.4001 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.0978 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -17.5708 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.6029 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.9644 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 17.3810 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 5.6040 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 19.2410 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 17.7713 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 58.2489 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.3135 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 5.0954 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 3.4588 -> Slightly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### What Alimentation Couche-Tard (ATD) Said on Its Q2 Earnings Call
- Summary: ATD reported Q2 earnings, detailing revenue, operating income, and guidance for the upcoming quarter.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPX1ZUTGphN0hYQmttRDd5UWVzLTIwaTFPS1Vlb0l2bU9NazloTGpQSkNPVFNlRkZrT2pmR25keGNQVVVWUUlZdjExTmN0WFRORGV6a0NXbjNZVVFLZkM1QURJNko2WGlZM3l3SG1jTnJXT0YzbXlhREMwX3RKT1N6ei04VG9RbG5vWnRMZjVoWnZvNWxLVWg3aFp6MFIzODg?oc=5>

### Alimentation Couche-Tard (TSX: ATD) to report second-quarter results
- Summary: Company will release Q2 earnings, providing insight into performance and guidance.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxQOUkzbXdySEVsNVlzdHk0N0hNQkt0a2hLUml0akV4SndqaXNRbFE3dXo3NFk5RWFxb010emlNTTZoWHF2Q1pRQURPZXNWWnEwUWRXWGJCRGNMZHBWLVlxSnFPT2hvSkF6akJXUGRlcFNlM0xqbGhOdTkwVVo1MEl2WThXdnNLUEhYWUlKZ0tQN3BmZw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ATD.TO** | **17.77** | **3.35** | **13.98** | **26.20** | **78,467,858,432.00 CAD** | **13.08** |
| CASY | 34.44 | 6.46 | 18.41 | 24.30 | 26,427,260,928.00 USD | 25.60 |
| MUSA | 14.35 | 11.63 | 9.21 | 39.30 | 9,231,316,992.00 USD | 33.20 |
| SUN | 10.56 | 1.22 | 6.84 | 198.90 | 11,834,279,936.00 USD | 19.33 |

Peers fetched as_of: 2026-11-27; ATD.TO reuses existing data (market data as_of: 2026-11-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-24
- Next expected earnings: 2027-03-16 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-27

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

- https://news.google.com/rss/articles/CBMinwFBVV95cUxPX1ZUTGphN0hYQmttRDd5UWVzLTIwaTFPS1Vlb0l2bU9NazloTGpQSkNPVFNlRkZrT2pmR25keGNQVVVWUUlZdjExTmN0WFRORGV6a0NXbjNZVVFLZkM1QURJNko2WGlZM3l3SG1jTnJXT0YzbXlhREMwX3RKT1N6ei04VG9RbG5vWnRMZjVoWnZvNWxLVWg3aFp6MFIzODg?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxQOUkzbXdySEVsNVlzdHk0N0hNQkt0a2hLUml0akV4SndqaXNRbFE3dXo3NFk5RWFxb010emlNTTZoWHF2Q1pRQURPZXNWWnEwUWRXWGJCRGNMZHBWLVlxSnFPT2hvSkF6akJXUGRlcFNlM0xqbGhOdTkwVVo1MEl2WThXdnNLUEhYWUlKZ0tQN3BmZw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
