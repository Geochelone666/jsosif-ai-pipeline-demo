# MCO Intelligence Report

- ticker: **MCO**
- Report as_of: **2026-11-27**
- Market data as_of: **2026-11-27**
- Quant sources: https://finance.yahoo.com/quote/MCO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MCO/key-statistics/
- AI analysis snapshot as_of: **2026-11-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-28T06:24:46.841448+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 4, 'rule': 1, 'ai': 1, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261127T063646Z-c0c26981/MCO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 4 unique headlines; 4 named publishers; 0 exact duplicates; 4 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-11-21

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 487.9400 |
| Return 1D (%) | 0.4633 |
| Return 1W (%) | 4.5220 |
| Return 1M (%) | 3.1661 |
| Return YTD (%) | -3.6367 |
| Return 1Y (%) | 1.0555 |
| Annualized volatility (%) | 29.0057 |
| Beta vs SPY | 0.5388 |
| Max drawdown (%) | -23.6059 |
| Sharpe (rf=0) | 0.1556 |
| Downside deviation (rf=0, %) | 20.7123 |
| Sortino (rf=0) | 0.2179 |
| Historical VaR 95% (1D, %) | 2.4807 |
| Historical ES 95% (1D, %) | 3.9934 |
| Correlation vs SPY | 0.2791 |
| Tracking error vs SPY (%) | 28.7020 |
| P/E (trailing) | 29.77 |
| P/B | 25.74 |
| EV/EBITDA | 22.30 |
| Revenue growth (%) | 0.80 |
| Forward P/E (estimate) | 26.24 |
| Gross margin (%) | 74.63 |
| Operating margin (%) | 46.04 |
| Return on equity (%) | 76.74 |
| Free cash flow yield (%) | 3.01 |
| MA50 | 479.1235 |
| Close vs MA50 (%) | 1.8401 |
| MA200 | 465.0767 |
| Close vs MA200 (%) | 4.9160 |
| RSI (14, Wilder) | 49.8999 |
| MACD (12,26) | -0.7581 |
| MACD signal (9) | 1.8996 |
| MACD histogram | -2.6578 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MCO': 291, 'SPY': 291}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 487.9400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.4633 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 4.5220 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 3.1661 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -3.6367 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 1.0555 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 29.0057 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 20.7123 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.2179 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.4807 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.9934 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2791 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 28.7020 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5388 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -23.6059 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1556 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 26.2362 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.6330 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 46.0370 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 76.7410 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 3.0127 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 29.7706 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 49.8999 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -2.6578 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 1.8401 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 4.9160 -> Slightly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Moody's Corporation (MCO) Launches Zero-Copy Data Sharing to Enh
- Summary: Moody's Corporation (MCO) Launches Zero-Copy Data Sharing to Enh
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxOU3BHN0FHdDVMY2tBcWJxNjFfbGVGSmlmOW4xMkVhenlGdy1EbWFRdkZOdnlyaWdKQnZ1WHR0QUQtS0Q4V3pES2dOWVNBM2NtWmNKeXl1TmktQ080bE14eFdnbnZKSnFPQmoxNEhCYXo2RmwwWk5tZTNNVWdSb2hNdHhBelRSNlJFUmtGOUowMUk5bGd0SV9Nb2M4czFFVmFTVUtuNXdaZjNndWRFdlQ0VHFlS29XR3M0Vmc?oc=5>

### MCO Embeds Connected Intelligence in AI Platforms to Support Growth
- Summary: Moody’s introduces connected intelligence in its AI platforms, aiming to boost growth and enhance analytical capabilities.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxQaU9jMFRFVDVOa1lUTDFfVG02bzZkYmE3NGxMeGhQODktb2JxVmhxcXJQTW13QUJNSVBZOVJMb3dMMFFlTnVBSFpJOTUwakZVX1NsbVc5TFNhWjc3dmxjaFJuZzlCMDZndUtWYUdXWWluZWNQVXJ3RE0xYldBNTlScFd2bjVnT3ZBa1pfRmJhUWJqNXd2M2hSVkRqTXZINExpc1YyTl9lMXdQemxHSVMyYUItdWpweDNuMW1fV0t1Zko?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MCO** | **29.77** | **25.74** | **22.30** | **0.80** | **84,132,610,048.00 USD** | **1.06** |
| SPGI | 27.55 | 6.78 | 17.89 | 6.80 | 133,713,469,440.00 USD | -0.74 |
| MSCI | 33.71 | -15.15 | 25.86 | 12.40 | 45,574,811,648.00 USD | 14.90 |
| FDS | 22.18 | 5.69 | 14.07 | 6.30 | 11,391,808,512.00 USD | 18.56 |

Peers fetched as_of: 2026-11-27; MCO reuses existing data (market data as_of: 2026-11-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-02-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-27

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 1,142,100,000.00 USD; period 2019-01-01/2019-03-31; fiscal year/reporting period 2019/Q1
- Net income (latest available single quarter): 734,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1059556/000162828026066731/mco-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiugFBVV95cUxOU3BHN0FHdDVMY2tBcWJxNjFfbGVGSmlmOW4xMkVhenlGdy1EbWFRdkZOdnlyaWdKQnZ1WHR0QUQtS0Q4V3pES2dOWVNBM2NtWmNKeXl1TmktQ080bE14eFdnbnZKSnFPQmoxNEhCYXo2RmwwWk5tZTNNVWdSb2hNdHhBelRSNlJFUmtGOUowMUk5bGd0SV9Nb2M4czFFVmFTVUtuNXdaZjNndWRFdlQ0VHFlS29XR3M0Vmc?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxQaU9jMFRFVDVOa1lUTDFfVG02bzZkYmE3NGxMeGhQODktb2JxVmhxcXJQTW13QUJNSVBZOVJMb3dMMFFlTnVBSFpJOTUwakZVX1NsbVc5TFNhWjc3dmxjaFJuZzlCMDZndUtWYUdXWWluZWNQVXJ3RE0xYldBNTlScFd2bjVnT3ZBa1pfRmJhUWJqNXd2M2hSVkRqTXZINExpc1YyTl9lMXdQemxHSVMyYUItdWpweDNuMW1fV0t1Zko?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
