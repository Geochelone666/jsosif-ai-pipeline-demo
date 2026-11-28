# ACN Intelligence Report

- ticker: **ACN**
- Report as_of: **2026-11-27**
- Market data as_of: **2026-11-27**
- Quant sources: https://finance.yahoo.com/quote/ACN/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ACN/key-statistics/
- AI analysis snapshot as_of: **2026-11-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-28T06:12:19.224668+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 7, 'rule': 2, 'ai': 0, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261127T063646Z-c0c26981/ACN** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 7 unique headlines; 6 named publishers; 0 exact duplicates; 7 HTTPS source links; largest publisher share 28.57%; oldest publication 2026-11-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 241.8400 |
| Return 1D (%) | 0.5614 |
| Return 1W (%) | 9.3458 |
| Return 1M (%) | 2.8406 |
| Return YTD (%) | -7.2667 |
| Return 1Y (%) | 0.3847 |
| Annualized volatility (%) | 50.5804 |
| Beta vs SPY | -0.0096 |
| Max drawdown (%) | -56.5068 |
| Sharpe (rf=0) | 0.2443 |
| Downside deviation (rf=0, %) | 35.3517 |
| Sortino (rf=0) | 0.3495 |
| Historical VaR 95% (1D, %) | 4.7187 |
| Historical ES 95% (1D, %) | 6.8166 |
| Correlation vs SPY | -0.0028 |
| Tracking error vs SPY (%) | 52.8050 |
| P/E (trailing) | 17.83 |
| P/B | 4.56 |
| EV/EBITDA | 10.81 |
| Revenue growth (%) | 6.20 |
| Forward P/E (estimate) | 15.20 |
| Gross margin (%) | 32.05 |
| Operating margin (%) | 16.42 |
| Return on equity (%) | 26.02 |
| Free cash flow yield (%) | 7.48 |
| MA50 | 224.5636 |
| Close vs MA50 (%) | 7.6933 |
| MA200 | 187.2292 |
| Close vs MA200 (%) | 29.1679 |
| RSI (14, Wilder) | 53.5533 |
| MACD (12,26) | 0.3253 |
| MACD signal (9) | 3.0748 |
| MACD histogram | -2.7495 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ACN': 291, 'SPY': 291}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 241.8400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.5614 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 9.3458 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 2.8406 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -7.2667 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 0.3847 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 50.5804 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 35.3517 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.3495 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.7187 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.8166 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.0028 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 52.8050 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.0096 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -56.5068 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2443 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.1963 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 32.0500 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 16.4190 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 26.0250 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 7.4788 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 17.8348 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 53.5533 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -2.7495 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 7.6933 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 29.1679 -> Clearly above the moving-average trend level.

## TAILWINDS

### Accenture PLC Stock (ACN) Moved Up by 4.83% on Nov 24: Facts Behind the Movement
- Summary: Accenture PLC Stock (ACN) Moved Up by 4.83% on Nov 24: Facts Behind the Movement
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxNVzN2ZGtRQ2JpanZ4MXd3c0xCUWpuZHA1UW9BLTlzN0RiWW5pb3VBSDBLWlRlWC1WVk5lLWFIMVhMZmNmRExLWUoxWWczaUQ1Q25md2NSNlBHTFRGckM0ZzEtQmFJUVF6YlZWNWdwblZKZDZaMjNEVGl6RWxpcGQ4RkZsYTZWeE1tZWc?oc=5>

### Accenture PLC Stock (ACN) Moved Up by 4.94% on Nov 25: What Investors Need To Know
- Summary: Accenture PLC Stock (ACN) Moved Up by 4.94% on Nov 25: What Investors Need To Know
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxQZkQ0MU9HT1VGd1k0aGh2ZGJNOHNHeElHUXlBRWNaNDNnZnVtcUIzNzU0VGkzbzhqSnZKdmJObWZrd0ZMQ2VyXzlERDV4MS1OdFRJZ05HOFdVNHN3MTBlaFlQdU5UNFY0cE44YVBNUmlqNHNqMjZ1aFh0MEhKdXNTRkx0dklWbDloMnc?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

No items in this run

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ACN** | **17.83** | **4.56** | **10.81** | **6.20** | **142,863,941,632.00 USD** | **0.38** |
| IBM | 21.17 | 6.60 | 17.51 | 4.70 | 234,465,574,912.00 USD | -15.94 |
| CTSH | 11.57 | 1.93 | 7.04 | 4.60 | 28,350,668,800.00 USD | -15.76 |
| INFY | 16.14 | 10.25 | 21.00 | 1.40 | 52,938,420,224.00 USD | -23.35 |

Peers fetched as_of: 2026-11-27; ACN reuses existing data (market data as_of: 2026-11-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-01
- Next expected earnings: 2026-12-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-27

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-10-16
- Revenue (latest available single quarter): 18,679,110,000.00 USD; period 2026-06-01/2026-08-31; fiscal year/reporting period 2026/FY
- Net income (latest available single quarter): 1,991,267,000.00 USD; period 2026-06-01/2026-08-31; fiscal year/reporting period 2026/FY
- SEC link: https://www.sec.gov/Archives/edgar/data/1467373/000146737326000049/acn-20260831.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiigFBVV95cUxNVzN2ZGtRQ2JpanZ4MXd3c0xCUWpuZHA1UW9BLTlzN0RiWW5pb3VBSDBLWlRlWC1WVk5lLWFIMVhMZmNmRExLWUoxWWczaUQ1Q25md2NSNlBHTFRGckM0ZzEtQmFJUVF6YlZWNWdwblZKZDZaMjNEVGl6RWxpcGQ4RkZsYTZWeE1tZWc?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxQZkQ0MU9HT1VGd1k0aGh2ZGJNOHNHeElHUXlBRWNaNDNnZnVtcUIzNzU0VGkzbzhqSnZKdmJObWZrd0ZMQ2VyXzlERDV4MS1OdFRJZ05HOFdVNHN3MTBlaFlQdU5UNFY0cE44YVBNUmlqNHNqMjZ1aFh0MEhKdXNTRkx0dklWbDloMnc?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
