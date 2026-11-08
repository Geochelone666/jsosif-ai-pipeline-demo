# CSU.TO Intelligence Report

- ticker: **CSU.TO**
- Report as_of: **2026-11-07**
- Market data as_of: **2026-11-06**
- Quant sources: https://finance.yahoo.com/quote/CSU.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CSU.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-07**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-08T04:21:56.559576+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 2, 'rule': 0, 'ai': 1, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261107T043155Z-acc5f41d/CSU.TO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 2 unique headlines; 2 named publishers; 0 exact duplicates; 2 HTTPS source links; largest publisher share 50.0%; oldest publication 2026-11-05

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 3526.5200 |
| Return 1D (%) | 0.4223 |
| Return 1W (%) | 3.9232 |
| Return 1M (%) | 19.5171 |
| Return YTD (%) | 6.9888 |
| Return 1Y (%) | 4.1473 |
| Annualized volatility (%) | 43.6837 |
| Beta vs SPY | 0.0411 |
| Max drawdown (%) | -33.9828 |
| Sharpe (rf=0) | 0.3102 |
| Downside deviation (rf=0, %) | 29.3158 |
| Sortino (rf=0) | 0.4622 |
| Historical VaR 95% (1D, %) | 4.3857 |
| Historical ES 95% (1D, %) | 5.4742 |
| Correlation vs SPY | 0.0127 |
| Tracking error vs SPY (%) | 45.9164 |
| P/E (trailing) | 55.91 |
| P/B | 12.35 |
| EV/EBITDA | 27.66 |
| Revenue growth (%) | 19.10 |
| Forward P/E (estimate) | 19.03 |
| Gross margin (%) | 37.29 |
| Operating margin (%) | 16.03 |
| Return on equity (%) | 24.22 |
| Free cash flow yield (%) | N/A |
| MA50 | 3077.4067 |
| Close vs MA50 (%) | 14.5939 |
| MA200 | 2785.9587 |
| Close vs MA200 (%) | 26.5819 |
| RSI (14, Wilder) | 72.6985 |
| MACD (12,26) | 127.8162 |
| MACD signal (9) | 115.2930 |
| MACD histogram | 12.5232 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CSU.TO': 276, 'SPY': 277}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 3526.5200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.4223 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 3.9232 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 19.5171 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 6.9888 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 4.1473 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 43.6837 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 29.3158 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4622 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.3857 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.4742 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0127 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 45.9164 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.0411 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -33.9828 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3102 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 19.0288 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 37.2920 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 16.0310 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 24.2210 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 55.9055 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 72.6985 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 12.5232 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 14.5939 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 26.5819 -> Clearly above the moving-average trend level.

## TAILWINDS

### Earnings Flash (CSU.TO) Constellation Software Inc. Reports Q3 Revenue $3.51B
- Summary: Constellation Software reports Q3 revenue of $3.51 billion, indicating strong financial performance for the quarter.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxNRm1Zd0U5R29mMTdkODhxT0lLN2lPUVVPSEZlanBnODR1eXo4WnJtaDlwYXljMG5OVjBocGxQY0pyZ3hNWmRMZVo3ak5DejRhc3FNTkl2MVoxMmNkMDJKNmY5elZjemZ1NUJpNklnNkZibnUyRFZEZ09sTEl2NzRvQWJZMkxGaFlHTDRDcDlHM29CNHZNUUtuUGROQTVrR1hsTjVJNGpuYTRQemhUa1F5TGFXSnMwNGpyTVBZMFAyNndOTkFk?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

No items in this run

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CSU.TO** | **55.91** | **12.35** | **27.66** | **19.10** | **74,732,355,584.00 CAD** | **4.15** |
| DSG.TO | 44.52 | 4.91 | 33.12 | 11.80 | 11,349,726,208.00 CAD | 12.00 |
| OTEX.TO | 9.61 | 1.44 | 8.28 | -4.00 | 8,492,542,976.00 CAD | -27.82 |
| TOI.V | 38.24 | 11.68 | 26.27 | 17.50 | 22,406,227,968.00 CAD | -18.14 |

Peers fetched as_of: 2026-11-07; CSU.TO reuses existing data (market data as_of: 2026-11-06); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-05
- Next expected earnings: 2027-03-08 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-07

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

- https://news.google.com/rss/articles/CBMixAFBVV95cUxNRm1Zd0U5R29mMTdkODhxT0lLN2lPUVVPSEZlanBnODR1eXo4WnJtaDlwYXljMG5OVjBocGxQY0pyZ3hNWmRMZVo3ak5DejRhc3FNTkl2MVoxMmNkMDJKNmY5elZjemZ1NUJpNklnNkZibnUyRFZEZ09sTEl2NzRvQWJZMkxGaFlHTDRDcDlHM29CNHZNUUtuUGROQTVrR1hsTjVJNGpuYTRQemhUa1F5TGFXSnMwNGpyTVBZMFAyNndOTkFk?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
