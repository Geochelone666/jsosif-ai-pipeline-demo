# MCO Intelligence Report

- ticker: **MCO**
- Report as_of: **2026-11-13**
- Market data as_of: **2026-11-13**
- Quant sources: https://finance.yahoo.com/quote/MCO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MCO/key-statistics/
- AI analysis snapshot as_of: **2026-11-13**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-14T05:00:06.704832+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 2, 'rule': 0, 'ai': 2, 'unknown': 0})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261113T045636Z-34122c9a/MCO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 2 unique headlines; 2 named publishers; 0 exact duplicates; 2 HTTPS source links; largest publisher share 50.0%; oldest publication 2026-11-09

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 508.2000 |
| Return 1D (%) | 0.3238 |
| Return 1W (%) | 0.5003 |
| Return 1M (%) | 9.4952 |
| Return YTD (%) | 0.1454 |
| Return 1Y (%) | 4.4497 |
| Annualized volatility (%) | 28.5761 |
| Beta vs SPY | 0.5313 |
| Max drawdown (%) | -23.6059 |
| Sharpe (rf=0) | 0.2959 |
| Downside deviation (rf=0, %) | 20.2804 |
| Sortino (rf=0) | 0.4169 |
| Historical VaR 95% (1D, %) | 2.4637 |
| Historical ES 95% (1D, %) | 3.8509 |
| Correlation vs SPY | 0.2535 |
| Tracking error vs SPY (%) | 28.3720 |
| P/E (trailing) | 30.91 |
| P/B | 26.81 |
| EV/EBITDA | 23.16 |
| Revenue growth (%) | 0.80 |
| Forward P/E (estimate) | 27.31 |
| Gross margin (%) | 74.63 |
| Operating margin (%) | 46.04 |
| Return on equity (%) | 76.74 |
| Free cash flow yield (%) | 2.89 |
| MA50 | 478.3400 |
| Close vs MA50 (%) | 6.2424 |
| MA200 | 464.9573 |
| Close vs MA200 (%) | 9.3004 |
| RSI (14, Wilder) | 57.7076 |
| MACD (12,26) | 10.1818 |
| MACD signal (9) | 9.6911 |
| MACD histogram | 0.4907 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MCO': 282, 'SPY': 282}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 508.2000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.3238 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.5003 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 9.4952 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 0.1454 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 4.4497 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 28.5761 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 20.2804 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4169 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.4637 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.8509 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2535 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 28.3720 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5313 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -23.6059 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2959 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 27.3133 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.6330 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 46.0370 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 76.7410 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.8926 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 30.9124 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 57.7076 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.4907 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 6.2424 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 9.3004 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Moody's (MCO) Tests On Chain Ratings, Is The Stock Already Expensive?
- Summary: Moody's tests on-chain ratings, questioning stock valuation.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNY0NZT0RkQ2xPNm1POUhHbXI5dmY1ZlNYN2tocnFrbzlsY2diX3F3eDEwX3NzUGxWTzAyYU9zaGdKazVSSlpzMnFZbENBRFcwZkNDQ0ltZ25ZTTR6T3Jzd1ZYQTlUTWNtM0gyUExFU3ljMG9RWEVTdmgxc2FOT0JxcWl3dldUc1l2WWdpX29MRXRFR1dNMTA5MUJMRQ?oc=5>

### MCO: Moody's prices €500M 4.125% notes due 2033
- Summary: Moody’s issues €500M 4.125% notes due 2033, raising capital.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxQOXdHZ095WGwwRHRURzI4Ry1mMU9fa0FPUldkVk5LM3BjWkszb3Zoall4b3dOUjAySEQ0OVZwVUFYZVk0bnJjOHJMcjY4YU5BREV0bl9Ga05Cd2pla1BnME02MHItcUE4ajBpSFU3QVI5TnBVZXdib19tSThUQTlqbmVQaElQY3V6cWxv?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MCO** | **30.91** | **26.81** | **23.16** | **0.80** | **87,625,916,416.00 USD** | **4.45** |
| SPGI | 27.99 | 6.97 | 18.32 | 6.80 | 137,293,742,080.00 USD | 0.41 |
| MSCI | 34.46 | -15.64 | 26.60 | 12.40 | 47,059,152,896.00 USD | 16.81 |
| FDS | 22.77 | 5.86 | 14.45 | 6.30 | 11,733,934,080.00 USD | 21.84 |

Peers fetched as_of: 2026-11-13; MCO reuses existing data (market data as_of: 2026-11-13); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-02-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-13

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

- https://news.google.com/rss/articles/CBMimwFBVV95cUxNY0NZT0RkQ2xPNm1POUhHbXI5dmY1ZlNYN2tocnFrbzlsY2diX3F3eDEwX3NzUGxWTzAyYU9zaGdKazVSSlpzMnFZbENBRFcwZkNDQ0ltZ25ZTTR6T3Jzd1ZYQTlUTWNtM0gyUExFU3ljMG9RWEVTdmgxc2FOT0JxcWl3dldUc1l2WWdpX29MRXRFR1dNMTA5MUJMRQ?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxQOXdHZ095WGwwRHRURzI4Ry1mMU9fa0FPUldkVk5LM3BjWkszb3Zoall4b3dOUjAySEQ0OVZwVUFYZVk0bnJjOHJMcjY4YU5BREV0bl9Ga05Cd2pla1BnME02MHItcUE4ajBpSFU3QVI5TnBVZXdib19tSThUQTlqbmVQaElQY3V6cWxv?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
