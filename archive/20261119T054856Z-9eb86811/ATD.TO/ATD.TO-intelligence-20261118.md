# ATD.TO Intelligence Report

- ticker: **ATD.TO**
- Report as_of: **2026-11-18**
- Market data as_of: **2026-11-18**
- Quant sources: https://finance.yahoo.com/quote/ATD.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ATD.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-18**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-19T05:55:41.584955+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 2, 'rule': 0, 'ai': 2, 'unknown': 0})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 2 unique headlines; 2 named publishers; 0 exact duplicates; 2 HTTPS source links; largest publisher share 50.0%; oldest publication 2026-11-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 83.0000 |
| Return 1D (%) | -0.7770 |
| Return 1W (%) | 0.7893 |
| Return 1M (%) | -0.5988 |
| Return YTD (%) | 11.5861 |
| Return 1Y (%) | 20.6837 |
| Annualized volatility (%) | 26.1264 |
| Beta vs SPY | 0.1016 |
| Max drawdown (%) | -17.5708 |
| Sharpe (rf=0) | 0.8505 |
| Downside deviation (rf=0, %) | 15.0871 |
| Sortino (rf=0) | 1.4729 |
| Historical VaR 95% (1D, %) | 2.1810 |
| Historical ES 95% (1D, %) | 2.8393 |
| Correlation vs SPY | 0.0533 |
| Tracking error vs SPY (%) | 29.0943 |
| P/E (trailing) | 17.36 |
| P/B | 3.25 |
| EV/EBITDA | 13.78 |
| Revenue growth (%) | 25.10 |
| Forward P/E (estimate) | 16.47 |
| Gross margin (%) | 18.24 |
| Operating margin (%) | 5.88 |
| Return on equity (%) | 19.61 |
| Free cash flow yield (%) | N/A |
| MA50 | 80.8114 |
| Close vs MA50 (%) | 2.7083 |
| MA200 | 82.4320 |
| Close vs MA200 (%) | 0.6891 |
| RSI (14, Wilder) | 53.1080 |
| MACD (12,26) | 0.5380 |
| MACD signal (9) | 0.5239 |
| MACD histogram | 0.0141 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ATD.TO': 284, 'SPY': 285}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 83.0000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.7770 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.7893 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -0.5988 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 11.5861 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 20.6837 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 26.1264 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 15.0871 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.4729 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.1810 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.8393 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0533 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 29.0943 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.1016 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -17.5708 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.8505 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.4722 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 18.2380 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 5.8820 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 19.6150 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 17.3640 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 53.1080 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.0141 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 2.7083 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 0.6891 -> Slightly above the moving-average trend level.

## TAILWINDS

### Couche Tard (TSX:ATD) Stock Still Looks Undervalued After Its 73% Run
- Summary: ATD stock appears undervalued after a 73% run, suggesting potential upside.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMif0FVX3lxTE5LaWtOVXRWNUVmOU03VWQ5c2YxbWpPYTZmcC1lNHBqUUtFc25QWEk0akh5TUZWRElXcHZMczB2eGpJYmlNUVRLc2dObXpnZTVNZ2MzSThDN2tiUGNuSnFlSzctelM2dExKTWliM1o3aFA1T0hGWnFpYXlMeGZ1amM?oc=5>

### Alimentation Couche Tard (TSX:ATD) Could Be 40% Undervalued On Zabka Deal Closing In December
- Summary: ATD may be 40% undervalued ahead of Zabka deal closing in December, indicating upside potential.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPR29jZklSR3ZOZ3VsNnhiQTY3SVlsb0c0OGFkeFlTUklmanNzUXJMYUg3ZDlFY3B5bUxCa3JseE5hVXZXR3RoWlcwQUNsNFREOFpFM2RDR0Z2cTRETlR5N1NmN0VlWEhCeXN2T3N0RTNGSTNJT1ZDVnQ1TmtmNnpyS2dieHNPSXJhRTU1NHpPaVRXWGFZMW9fSTVLMzd3UQ?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

No items in this run

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ATD.TO** | **17.36** | **3.25** | **13.78** | **25.10** | **76,190,900,224.00 CAD** | **20.68** |
| CASY | 32.94 | 6.31 | 18.02 | 24.30 | 25,822,959,616.00 USD | 27.85 |
| MUSA | 14.48 | 11.74 | 9.28 | 39.30 | 9,320,006,656.00 USD | 40.43 |
| SUN | 10.47 | 1.24 | 6.88 | 198.90 | 12,017,040,384.00 USD | 24.70 |

Peers fetched as_of: 2026-11-18; ATD.TO reuses existing data (market data as_of: 2026-11-18); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-01
- Next expected earnings: 2026-11-24 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-18

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

- https://news.google.com/rss/articles/CBMif0FVX3lxTE5LaWtOVXRWNUVmOU03VWQ5c2YxbWpPYTZmcC1lNHBqUUtFc25QWEk0akh5TUZWRElXcHZMczB2eGpJYmlNUVRLc2dObXpnZTVNZ2MzSThDN2tiUGNuSnFlSzctelM2dExKTWliM1o3aFA1T0hGWnFpYXlMeGZ1amM?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPR29jZklSR3ZOZ3VsNnhiQTY3SVlsb0c0OGFkeFlTUklmanNzUXJMYUg3ZDlFY3B5bUxCa3JseE5hVXZXR3RoWlcwQUNsNFREOFpFM2RDR0Z2cTRETlR5N1NmN0VlWEhCeXN2T3N0RTNGSTNJT1ZDVnQ1TmtmNnpyS2dieHNPSXJhRTU1NHpPaVRXWGFZMW9fSTVLMzd3UQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
