# XYL Intelligence Report

- ticker: **XYL**
- Report as_of: **2026-11-12**
- Market data as_of: **2026-11-12**
- Quant sources: https://finance.yahoo.com/quote/XYL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/XYL/key-statistics/
- AI analysis snapshot as_of: **2026-11-12**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-13T05:01:26.599018+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 6, 'rule': 2, 'ai': 2, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261112T054014Z-6c47e7f9/XYL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 6 unique headlines; 5 named publishers; 0 exact duplicates; 6 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-11-06

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 94.0300 |
| Return 1D (%) | -1.1355 |
| Return 1W (%) | -6.0170 |
| Return 1M (%) | -8.3439 |
| Return YTD (%) | -30.1812 |
| Return 1Y (%) | -36.3795 |
| Annualized volatility (%) | 30.7808 |
| Beta vs SPY | 0.6168 |
| Max drawdown (%) | -40.3037 |
| Sharpe (rf=0) | -1.3162 |
| Downside deviation (rf=0, %) | 25.3790 |
| Sortino (rf=0) | -1.5964 |
| Historical VaR 95% (1D, %) | 3.0031 |
| Historical ES 95% (1D, %) | 5.0991 |
| Correlation vs SPY | 0.2752 |
| Tracking error vs SPY (%) | 30.0566 |
| P/E (trailing) | 20.85 |
| P/B | 2.11 |
| EV/EBITDA | 12.28 |
| Revenue growth (%) | -3.00 |
| Forward P/E (estimate) | 16.07 |
| Gross margin (%) | 39.32 |
| Operating margin (%) | 15.51 |
| Return on equity (%) | 9.76 |
| Free cash flow yield (%) | 5.61 |
| MA50 | 102.5530 |
| Close vs MA50 (%) | -8.3108 |
| MA200 | 114.7537 |
| Close vs MA200 (%) | -18.0593 |
| RSI (14, Wilder) | 40.0865 |
| MACD (12,26) | -2.1482 |
| MACD signal (9) | -2.0468 |
| MACD histogram | -0.1014 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'XYL': 281, 'SPY': 281}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 94.0300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.1355 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -6.0170 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -8.3439 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -30.1812 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -36.3795 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 30.7808 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 25.3790 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -1.5964 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.0031 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.0991 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2752 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 30.0566 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.6168 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -40.3037 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -1.3162 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.0724 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 39.3200 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 15.5090 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.7560 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 5.6129 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 20.8492 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 40.0865 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.1014 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -8.3108 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -18.0593 -> Clearly below the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Xylem Acquires Cornell Pump and Roper Pump to Expand Portfolio
- Summary: Xylem Acquires Cornell Pump and Roper Pump to Expand Portfolio
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxOYTk1OVZoRmp6bjF4Q25BSU15Smo3aFJURzk2cUtsOVVWbjhHQWtwTWFXUkpXd25GTGc5UTVTczdqay1TczFjS2JTM3A5OHZiNEI5TkZFSjdKbmlrYUVyYXhtVmdrUW9IcVNhcUF6VExnZkE5a1VKak5vWUxlb0JESXpYM0FNZVpoWEFWSU9UVTNPTktGdFQxdktvdkJlc2g0SkdZYVMzR19yMXkwSDVRd0o1cVkxOUo0d0E?oc=5>

### Xylem Completes Acquisition of Cornell Pump and Roper Pump
- Summary: Xylem Completes Acquisition of Cornell Pump and Roper Pump
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxPbHBjNnVRUHV4RG9lWWVVTDV3cDd5R2R3dHp2NmhFSzlxWi1ZeHBkWmZTcWZtR2hESTBQUTBtVE9BOVRQLThqYVhmSnFEUnpHdERKYVh1ZUxNS0xxSDI0WFp5VDN6emk2Z2ZRaWxNUkZOZHJMM20xU2pXWHdfNWlRc29qZjZFUVNNeHNFQXBvaDNKT2x2dkhPRi1RV3JCdDVWbTQxSFlYUHJYV00?oc=5>

### 12,001 Xylem Inc. $XYL Shares Bought by Ethic Inc.
- Summary: Ethic Inc. purchased 12,001 Xylem shares, indicating investor interest.
- Date: 2026-11-09 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxNMkFPelpvbkY0RWVDOEE1ZHZqS2lXZkEtSVpBR0xBRmtZSXhyV2tPZjA5NFYta1FwMHROazFiV3lIZWF5cklnY0VuTC0waHR3d1p4M1RuOVZGS1I2V1M3UmNrUlcyZnJRRG9IbHZfYjZmWlB6dkdubjV0bXoyblJmWWNsX2xOMHV2Rjc2YlgyOTc0Q0I0dDlBaHpPZUxaRWZObm5PUUFzY0NHdEk?oc=5>

## RISKS

### 106,420 Xylem Inc. $XYL Shares Sold by Candriam S.C.A.
- Summary: Candriam S.C.A. sold 106,420 Xylem shares, reflecting a large divestiture.
- Date: 2026-11-08 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxPMkhlSkExRU0yN0NoM1k4cUM5RnNiaDdYLUFJazRUbUlqWE9BYWZhelFiVHhORGgxUjlRZWwxaTR2R1oyVDlDT3RRNjVNVWZxX3BtcXYySHBFVV93MDltMnc5WUJ5bkVfUVd6QXdjcE1VejlneEVVUWs5Q2pNcnZaWVkxQlVNbGhPTXY2QTdtYmdocUkwZjg5UWdjam9UT2FWY1VQamNwWW5sZUplYnc?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **XYL** | **20.85** | **2.11** | **12.28** | **-3.00** | **21,564,332,032.00 USD** | **-36.38** |
| AOS | 18.02 | 4.71 | 11.55 | -0.20 | 8,594,366,464.00 USD | -1.39 |
| PH | 32.91 | 7.57 | 23.08 | 17.90 | 120,798,199,808.00 USD | 12.82 |
| DOV | 24.79 | 3.65 | 15.02 | 7.50 | 27,861,121,024.00 USD | 15.25 |

Peers fetched as_of: 2026-11-12; XYL reuses existing data (market data as_of: 2026-11-12); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-27
- Next expected earnings: 2027-02-09 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-12

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-27
- Revenue (latest available single quarter): 2,201,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 291,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1524472/000152447226000148/xyl-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiugFBVV95cUxOYTk1OVZoRmp6bjF4Q25BSU15Smo3aFJURzk2cUtsOVVWbjhHQWtwTWFXUkpXd25GTGc5UTVTczdqay1TczFjS2JTM3A5OHZiNEI5TkZFSjdKbmlrYUVyYXhtVmdrUW9IcVNhcUF6VExnZkE5a1VKak5vWUxlb0JESXpYM0FNZVpoWEFWSU9UVTNPTktGdFQxdktvdkJlc2g0SkdZYVMzR19yMXkwSDVRd0o1cVkxOUo0d0E?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxPbHBjNnVRUHV4RG9lWWVVTDV3cDd5R2R3dHp2NmhFSzlxWi1ZeHBkWmZTcWZtR2hESTBQUTBtVE9BOVRQLThqYVhmSnFEUnpHdERKYVh1ZUxNS0xxSDI0WFp5VDN6emk2Z2ZRaWxNUkZOZHJMM20xU2pXWHdfNWlRc29qZjZFUVNNeHNFQXBvaDNKT2x2dkhPRi1RV3JCdDVWbTQxSFlYUHJYV00?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxNMkFPelpvbkY0RWVDOEE1ZHZqS2lXZkEtSVpBR0xBRmtZSXhyV2tPZjA5NFYta1FwMHROazFiV3lIZWF5cklnY0VuTC0waHR3d1p4M1RuOVZGS1I2V1M3UmNrUlcyZnJRRG9IbHZfYjZmWlB6dkdubjV0bXoyblJmWWNsX2xOMHV2Rjc2YlgyOTc0Q0I0dDlBaHpPZUxaRWZObm5PUUFzY0NHdEk?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxPMkhlSkExRU0yN0NoM1k4cUM5RnNiaDdYLUFJazRUbUlqWE9BYWZhelFiVHhORGgxUjlRZWwxaTR2R1oyVDlDT3RRNjVNVWZxX3BtcXYySHBFVV93MDltMnc5WUJ5bkVfUVd6QXdjcE1VejlneEVVUWs5Q2pNcnZaWVkxQlVNbGhPTXY2QTdtYmdocUkwZjg5UWdjam9UT2FWY1VQamNwWW5sZUplYnc?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
