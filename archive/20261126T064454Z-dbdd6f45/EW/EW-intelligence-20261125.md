# EW Intelligence Report

- ticker: **EW**
- Report as_of: **2026-11-25**
- Market data as_of: **2026-11-25**
- Quant sources: https://finance.yahoo.com/quote/EW/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/EW/key-statistics/
- AI analysis snapshot as_of: **2026-11-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-26T06:45:39.921557+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 12, 'rule': 1, 'ai': 1, 'unknown': 0, 'irrelevant': 10})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261125T065354Z-0b3565c6/EW** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 12 unique headlines; 10 named publishers; 1 exact duplicates; 12 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-11-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 106.3600 |
| Return 1D (%) | 0.2262 |
| Return 1W (%) | 1.0738 |
| Return 1M (%) | 19.4117 |
| Return YTD (%) | 24.7625 |
| Return 1Y (%) | 22.5063 |
| Annualized volatility (%) | 25.5508 |
| Beta vs SPY | 0.5351 |
| Max drawdown (%) | -13.1855 |
| Sharpe (rf=0) | 0.9249 |
| Downside deviation (rf=0, %) | 16.8444 |
| Sortino (rf=0) | 1.4030 |
| Historical VaR 95% (1D, %) | 2.5317 |
| Historical ES 95% (1D, %) | 3.1155 |
| Correlation vs SPY | 0.3127 |
| Tracking error vs SPY (%) | 25.2427 |
| P/E (trailing) | 61.84 |
| P/B | 5.64 |
| EV/EBITDA | 27.36 |
| Revenue growth (%) | 10.50 |
| Forward P/E (estimate) | 31.25 |
| Gross margin (%) | 78.02 |
| Operating margin (%) | 28.82 |
| Return on equity (%) | 9.33 |
| Free cash flow yield (%) | 1.87 |
| MA50 | 93.3554 |
| Close vs MA50 (%) | 13.9302 |
| MA200 | 87.3574 |
| Close vs MA200 (%) | 21.7527 |
| RSI (14, Wilder) | 67.9022 |
| MACD (12,26) | 3.7383 |
| MACD signal (9) | 3.9936 |
| MACD histogram | -0.2553 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'EW': 290, 'SPY': 290}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 106.3600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.2262 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.0738 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 19.4117 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 24.7625 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 22.5063 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 25.5508 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.8444 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.4030 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.5317 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.1155 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3127 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 25.2427 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5351 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -13.1855 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9249 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 31.2505 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 78.0180 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 28.8180 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.3330 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.8728 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 61.8372 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 67.9022 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.2553 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 13.9302 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 21.7527 -> Clearly above the moving-average trend level.

## TAILWINDS

### Edwards Lifesciences (NYSE:EW) Stock Forecast & Analyst Predictions
- Summary: Analysts project favorable stock performance for Edwards Lifesciences based on current market trends.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxNVURZUTZibGZKdmdBdVlyWVkxWVh5TkdvcnNFQkZTSTl1T2wxX0N5bENtQU5XZTN0YzZmSFBXcWJCekdncGJja0dKT2hXZHlJQk1yOXp3a2hQdDVMd3hrU29CaFBiT2NjMmtmRnRKRFdrQTlPR2k0TEdlb1ZiM1hBbnZBbE8?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Edwards Lifesciences Corporation $EW Shares Sold by State Street Corp
- Summary: Edwards Lifesciences Corporation $EW Shares Sold by State Street Corp
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxOWkozLUpnUTBJd19KRFlES1lINXk4dVBfNGRyVXY5WXVHeFUyYjFQYUotSmZuYWRBY0MxdHBHUXdOX3I0cV94cGExempZNFdEczhCMG9pRHQtYktQV04yeUp2R3pzOW9XbkNfN1NFanR1UEZ6OUlQMDB2RWRmOHU1dFozUGJrWWgzQjBzYnJtVk1pRzhiSUk4Rk10bjdVOUk1OWwyam9leHdEcTluTFlrMUtCSjZTb3BqMlVQT1E5NlloLXl0YUpxMw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **EW** | **61.84** | **5.64** | **27.36** | **10.50** | **61,156,999,168.00 USD** | **22.51** |
| MDT | 23.60 | 2.45 | 13.43 | 4.50 | 122,873,987,072.00 USD | -5.80 |
| BSX | 19.04 | 2.55 | 13.82 | 1.40 | 65,400,233,984.00 USD | -55.49 |
| ABT | 40.30 | 3.67 | 18.75 | 14.50 | 187,049,689,088.00 USD | -13.56 |

Peers fetched as_of: 2026-11-25; EW reuses existing data (market data as_of: 2026-11-25); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-04
- Next expected earnings: 2027-02-09 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-25

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 1,715,500,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 307,500,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1099800/000109980026000054/ew-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMihAFBVV95cUxNVURZUTZibGZKdmdBdVlyWVkxWVh5TkdvcnNFQkZTSTl1T2wxX0N5bENtQU5XZTN0YzZmSFBXcWJCekdncGJja0dKT2hXZHlJQk1yOXp3a2hQdDVMd3hrU29CaFBiT2NjMmtmRnRKRFdrQTlPR2k0TEdlb1ZiM1hBbnZBbE8?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxOWkozLUpnUTBJd19KRFlES1lINXk4dVBfNGRyVXY5WXVHeFUyYjFQYUotSmZuYWRBY0MxdHBHUXdOX3I0cV94cGExempZNFdEczhCMG9pRHQtYktQV04yeUp2R3pzOW9XbkNfN1NFanR1UEZ6OUlQMDB2RWRmOHU1dFozUGJrWWgzQjBzYnJtVk1pRzhiSUk4Rk10bjdVOUk1OWwyam9leHdEcTluTFlrMUtCSjZTb3BqMlVQT1E5NlloLXl0YUpxMw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
