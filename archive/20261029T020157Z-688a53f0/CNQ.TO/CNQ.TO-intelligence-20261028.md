# CNQ.TO Intelligence Report

- ticker: **CNQ.TO**
- Report as_of: **2026-10-28**
- Market data as_of: **2026-10-28**
- Quant sources: https://finance.yahoo.com/quote/CNQ.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CNQ.TO/key-statistics/
- AI analysis snapshot as_of: **2026-10-28**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-29T02:14:07.622972+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 8, 'rule': 1, 'ai': 1, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261028T015717Z-533e470c/CNQ.TO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 8 unique headlines; 3 named publishers; 0 exact duplicates; 8 HTTPS source links; largest publisher share 62.5%; oldest publication 2026-10-22

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 76.7800 |
| Return 1D (%) | 1.0928 |
| Return 1W (%) | 0.7612 |
| Return 1M (%) | 13.9507 |
| Return YTD (%) | 69.9444 |
| Return 1Y (%) | 83.2390 |
| Annualized volatility (%) | 30.5540 |
| Beta vs SPY | -0.5850 |
| Max drawdown (%) | -18.6770 |
| Sharpe (rf=0) | 2.1452 |
| Downside deviation (rf=0, %) | 20.5170 |
| Sortino (rf=0) | 3.1947 |
| Historical VaR 95% (1D, %) | 2.9758 |
| Historical ES 95% (1D, %) | 4.3580 |
| Correlation vs SPY | -0.2439 |
| Tracking error vs SPY (%) | 35.8946 |
| P/E (trailing) | 13.64 |
| P/B | 3.39 |
| EV/EBITDA | 9.19 |
| Revenue growth (%) | 69.50 |
| Forward P/E (estimate) | 12.30 |
| Gross margin (%) | 51.58 |
| Operating margin (%) | 43.09 |
| Return on equity (%) | 26.68 |
| Free cash flow yield (%) | 4.69 |
| MA50 | 70.6015 |
| Close vs MA50 (%) | 8.7512 |
| MA200 | 62.4801 |
| Close vs MA200 (%) | 22.8871 |
| RSI (14, Wilder) | 67.2844 |
| MACD (12,26) | 2.1938 |
| MACD signal (9) | 1.9307 |
| MACD histogram | 0.2631 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CNQ.TO': 269, 'SPY': 270}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 76.7800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.0928 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.7612 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 13.9507 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 69.9444 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 83.2390 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 30.5540 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 20.5170 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 3.1947 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9758 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.3580 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.2439 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 35.8946 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.5850 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -18.6770 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 2.1452 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 12.3044 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 51.5760 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 43.0910 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 26.6850 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.6879 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 13.6377 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 67.2844 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.2631 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 8.7512 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 22.8871 -> Clearly above the moving-average trend level.

## TAILWINDS

### Canadian Natural Resources (TSE:CNQ) Price Target Raised to C$85.00
- Summary: Canadian Natural Resources (TSE:CNQ) Price Target Raised to C$85.00
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxQWGJDVDVHeEFJM3RaWm4zb0tmd1NGTXZDTjAxT3ZBQjNMb2pVWVpLWUxWemRSbWV1X1dLdThvZ3JQUGlpQzVjQXNjLXhFZnlpcUdyR2ZDSXBXbXBnY1VTMXBDWmE0TmZVWEJmLVVxNEkyYUhUSUlob1hlUG9qSGVlOEV4ZWpTdzJETUZXdlkyNkdMYWtKektZNFpCb2lrdldnUkVXbjd0c1lxTUJDTGdqX1JHLVJULVZTNWFGeWNNbi1yczQ?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Canadian Natural Resources Limited (TSE:CNQ) Stock Rated "Moderate Buy" by Sell-Side Brokerages
- Summary: Sell-side brokerages rate CNQ as a moderate buy, indicating a positive outlook for the company.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi6wFBVV95cUxQYTNYSHJnUTkwb1B3dFl6UG9XQUpKaWkyX2hrdEVWNG1MNFcxRzhSQjVicXc4aHhfR2wxaFhSdGR1eDBTQVNGQU1UN0NGak5Vem1Fck42dEhRUm1tRUlVT1UyTFk0d2ZmdG0tX2FqUnN2aE9NNUlyTUVzbWhnbUhhMFFGaHNENEhraWY5b2gxeVJYcXJablp4SnFpbzAzQVI4eTJybUJuZzFQd0x4SEkxUWFrdTlEbzEzNVNxT2hKTmI1dFB6Q1FuMThaUC1MLWdkdkV1T0Vpb2FoY1RPcnA5TmFSR1pZeUo0YldV?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CNQ.TO** | **13.64** | **3.39** | **9.19** | **69.50** | **158,281,973,760.00 CAD** | **83.24** |
| SU.TO | 14.49 | 2.64 | 6.99 | 45.90 | 128,134,463,488.00 CAD | 102.50 |
| IMO.TO | 21.41 | 3.61 | 10.97 | 42.60 | 88,526,479,360.00 CAD | 46.60 |
| CVE.TO | 12.59 | 2.44 | 6.41 | 41.50 | 83,359,875,072.00 CAD | 96.98 |

Peers fetched as_of: 2026-10-28; CNQ.TO reuses existing data (market data as_of: 2026-10-28); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-06
- Next expected earnings: 2026-11-05 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-28

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

- https://news.google.com/rss/articles/CBMiwwFBVV95cUxQWGJDVDVHeEFJM3RaWm4zb0tmd1NGTXZDTjAxT3ZBQjNMb2pVWVpLWUxWemRSbWV1X1dLdThvZ3JQUGlpQzVjQXNjLXhFZnlpcUdyR2ZDSXBXbXBnY1VTMXBDWmE0TmZVWEJmLVVxNEkyYUhUSUlob1hlUG9qSGVlOEV4ZWpTdzJETUZXdlkyNkdMYWtKektZNFpCb2lrdldnUkVXbjd0c1lxTUJDTGdqX1JHLVJULVZTNWFGeWNNbi1yczQ?oc=5
- https://news.google.com/rss/articles/CBMi6wFBVV95cUxQYTNYSHJnUTkwb1B3dFl6UG9XQUpKaWkyX2hrdEVWNG1MNFcxRzhSQjVicXc4aHhfR2wxaFhSdGR1eDBTQVNGQU1UN0NGak5Vem1Fck42dEhRUm1tRUlVT1UyTFk0d2ZmdG0tX2FqUnN2aE9NNUlyTUVzbWhnbUhhMFFGaHNENEhraWY5b2gxeVJYcXJablp4SnFpbzAzQVI4eTJybUJuZzFQd0x4SEkxUWFrdTlEbzEzNVNxT2hKTmI1dFB6Q1FuMThaUC1MLWdkdkV1T0Vpb2FoY1RPcnA5TmFSR1pZeUo0YldV?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
