# TD.TO Intelligence Report

- ticker: **TD.TO**
- Report as_of: **2026-10-30**
- Market data as_of: **2026-10-30**
- Quant sources: https://finance.yahoo.com/quote/TD.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TD.TO/key-statistics/
- AI analysis snapshot as_of: **2026-10-30**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-31T02:04:42.596843+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 3, 'rule': 2, 'ai': 0, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 3 unique headlines; 2 named publishers; 0 exact duplicates; 3 HTTPS source links; largest publisher share 66.67%; oldest publication 2026-10-29

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 174.0400 |
| Return 1D (%) | -2.2961 |
| Return 1W (%) | -0.2465 |
| Return 1M (%) | 4.7331 |
| Return YTD (%) | 38.5976 |
| Return 1Y (%) | 56.3938 |
| Annualized volatility (%) | 17.1161 |
| Beta vs SPY | 0.6948 |
| Max drawdown (%) | -8.0048 |
| Sharpe (rf=0) | 2.7110 |
| Downside deviation (rf=0, %) | 11.5840 |
| Sortino (rf=0) | 4.0057 |
| Historical VaR 95% (1D, %) | 1.6767 |
| Historical ES 95% (1D, %) | 2.5212 |
| Correlation vs SPY | 0.5174 |
| Tracking error vs SPY (%) | 15.2658 |
| P/E (trailing) | 18.63 |
| P/B | 2.30 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 11.50 |
| Forward P/E (estimate) | 15.55 |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 38.02 |
| Return on equity (%) | 12.83 |
| Free cash flow yield (%) | N/A |
| MA50 | 168.1373 |
| Close vs MA50 (%) | 3.5107 |
| MA200 | 151.7181 |
| Close vs MA200 (%) | 14.7127 |
| RSI (14, Wilder) | 56.9513 |
| MACD (12,26) | 2.5084 |
| MACD signal (9) | 1.9003 |
| MACD histogram | 0.6080 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TD.TO': 271, 'SPY': 272}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 174.0400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.2961 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.2465 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 4.7331 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 38.5976 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 56.3938 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 17.1161 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 11.5840 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 4.0057 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.6767 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.5212 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5174 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 15.2658 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.6948 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -8.0048 -> Shallow peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 2.7110 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.5451 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 38.0200 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 12.8280 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 18.6338 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 56.9513 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.6080 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 3.5107 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 14.7127 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### TD Bank stock: CAD 10 billion buyback gains regulatory approval
- Summary: TD Bank stock: CAD 10 billion buyback gains regulatory approval
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxNRXhyY3hpN0F5WWRWc1M2bnN2V0Q3RllMd0czUzRONHhPekI2Ynhpc05zWmMwZWIzU1liWnBkeFN6Tkt1SWxTTWl4OTlycTB4QjBDeHZGeHdncEF4S1lHY05oLW5PallOZldaQVowaWhWczZJMGRuWGlKbHNGMzV4UWRLQk5SVVhkdGNfaFBnaEV6VDRMdG5uVzUyTGRjcnFqcVFoY2ZIMUlKMG9YMFV4NHpYMFVFNmVRSmx5bk1Hd2d6NzQ?oc=5>

### TD Bank stock: CAD 10 billion buyback wins Canadian approval
- Summary: TD Bank stock: CAD 10 billion buyback wins Canadian approval
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxQS1BFWHY3d1VveXhCWl9SU2k3RDRvRkNzRUVMRmlGNVJmZjRJd2oxMFVYZE56NGhUSDRtY0d0U0hLMnN0bElFb3FXUENjSEk2OWgyTi11WWpjLTNfYTBzanVTTXZhbWNucGRPazhDVDFzWWEteUJHdlBqVEpyeEo2RmtNcjVMOVhnTS1RMWxyVkdfaGIybkwzSktyeGsyRzhQYWZiak1FS3B4bzVRbHlFWkx0ZGNHNGdkbVlyZ2lpMA?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TD.TO** | **18.63** | **2.30** | **N/A** | **11.50** | **284,210,200,576.00 CAD** | **56.39** |
| RY.TO | 17.90 | 2.94 | N/A | 8.90 | 393,081,159,680.00 CAD | 42.78 |
| BMO.TO | 19.50 | 1.96 | N/A | 12.00 | 166,279,970,816.00 CAD | 42.56 |
| BNS.TO | 17.13 | 1.79 | N/A | 11.70 | 159,727,665,152.00 CAD | 48.52 |

Peers fetched as_of: 2026-10-30; TD.TO reuses existing data (market data as_of: 2026-10-30); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-27
- Next expected earnings: 2026-12-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-30

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

- https://news.google.com/rss/articles/CBMiwwFBVV95cUxNRXhyY3hpN0F5WWRWc1M2bnN2V0Q3RllMd0czUzRONHhPekI2Ynhpc05zWmMwZWIzU1liWnBkeFN6Tkt1SWxTTWl4OTlycTB4QjBDeHZGeHdncEF4S1lHY05oLW5PallOZldaQVowaWhWczZJMGRuWGlKbHNGMzV4UWRLQk5SVVhkdGNfaFBnaEV6VDRMdG5uVzUyTGRjcnFqcVFoY2ZIMUlKMG9YMFV4NHpYMFVFNmVRSmx5bk1Hd2d6NzQ?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxQS1BFWHY3d1VveXhCWl9SU2k3RDRvRkNzRUVMRmlGNVJmZjRJd2oxMFVYZE56NGhUSDRtY0d0U0hLMnN0bElFb3FXUENjSEk2OWgyTi11WWpjLTNfYTBzanVTTXZhbWNucGRPazhDVDFzWWEteUJHdlBqVEpyeEo2RmtNcjVMOVhnTS1RMWxyVkdfaGIybkwzSktyeGsyRzhQYWZiak1FS3B4bzVRbHlFWkx0ZGNHNGdkbVlyZ2lpMA?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
