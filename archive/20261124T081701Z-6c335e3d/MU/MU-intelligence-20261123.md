# MU Intelligence Report

- ticker: **MU**
- Report as_of: **2026-11-23**
- Market data as_of: **2026-11-23**
- Quant sources: https://finance.yahoo.com/quote/MU/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MU/key-statistics/
- AI analysis snapshot as_of: **2026-11-23**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-24T08:42:19.398561+00:00**
- AI status: **Partial: 5 headlines remain unclassified and excluded from research conclusions**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 0, 'ai': 3, 'unknown': 5, 'irrelevant': 14})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261123T053847Z-45053549/MU** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 11 named publishers; 3 exact duplicates; 22 HTTPS source links; largest publisher share 22.73%; oldest publication 2026-11-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 707.7000 |
| Return 1D (%) | 19.0392 |
| Return 1W (%) | -1.5744 |
| Return 1M (%) | -19.3550 |
| Return YTD (%) | 148.1405 |
| Return 1Y (%) | 241.6617 |
| Annualized volatility (%) | 86.6811 |
| Beta vs SPY | 3.4111 |
| Max drawdown (%) | -50.9958 |
| Sharpe (rf=0) | 1.7692 |
| Downside deviation (rf=0, %) | 53.5956 |
| Sortino (rf=0) | 2.8613 |
| Historical VaR 95% (1D, %) | 7.3472 |
| Historical ES 95% (1D, %) | 10.6103 |
| Correlation vs SPY | 0.5893 |
| Tracking error vs SPY (%) | 78.7907 |
| P/E (trailing) | 9.52 |
| P/B | 5.78 |
| EV/EBITDA | 7.00 |
| Revenue growth (%) | 379.30 |
| Forward P/E (estimate) | 3.42 |
| Gross margin (%) | 80.72 |
| Operating margin (%) | 74.59 |
| Return on equity (%) | 88.26 |
| Free cash flow yield (%) | 3.64 |
| MA50 | 907.8688 |
| Close vs MA50 (%) | -22.0482 |
| MA200 | 773.9269 |
| Close vs MA200 (%) | -8.5573 |
| RSI (14, Wilder) | 42.4539 |
| MACD (12,26) | -65.6852 |
| MACD signal (9) | -60.7667 |
| MACD histogram | -4.9185 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MU': 288, 'SPY': 288}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 707.7000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 19.0392 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.5744 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -19.3550 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 148.1405 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 241.6617 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 86.6811 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 53.5956 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.8613 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 7.3472 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 10.6103 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5893 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 78.7907 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.4111 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -50.9958 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.7692 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 3.4247 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 80.7160 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 74.5860 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 88.2600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 3.6393 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 9.5211 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 42.4539 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -4.9185 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -22.0482 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -8.5573 -> Clearly below the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

### What Happens To Micron Stock If Prices Stop Rising?
- Summary: Explores potential decline if Micron’s share price stalls, indicating possible downside risk.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxOaEc0VF9fdFRCeTVJU0lHMkxCYzVHLTd2NXZMc0toOWhlbUd5bEl3eTY4aVJoV0huWU1jR1FuVHExOWJLM1k4bmt5bXkzMl80cnliZEhURHhzMHhWZWdXWUg1d09LS1VaLU1ubXpCVWFqcEQ1VXpFX2h4a1hMMGgxdFoyUWZFdHRRWFZzaWY1RS1ndHppaV9xcUdUWHRNWktEeTh6NmRxMzkyc2dJQkE?oc=5>

### 7 Red Days In A Row: Micron Technology Stock Is Down 27%
- Summary: Stock has fallen 27% over seven consecutive days, indicating a sharp decline.
- Date: 2026-11-21 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxPWi1laGRDdmxIMDBFMk8zaTEzNXRUUWV3VlNQRTYwM0VpMVlBcTFBcUVZUlhZd1FIUXJRM0xrcC1OM1VrYUljd0RmQ2R6WVBwbzh5U2hoR09KUG9maGc3ZERoQkpzNlVWb0dsdmg0MHBTMVFjUk1qcFNkV3pZcEN2TVJ6OUVBOFE0dF8xNjVBOWhTRS16eUR1ampBNURWN25ibm1vY25ydWVOZ2k4X0RxMVVCVQ?oc=5>

## CATALYSTS

### Prediction: This Will Be Micron’s Stock Price by the End of 2028
- Summary: Forecasts project Micron's stock price trajectory through 2028, indicating potential long-term trends.
- Date: 2026-11-21 | Impact: medium | Horizon: long | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxOODQ0aGxEM1BzSF9NdGdnY3FsbXZvR09xN2JKLUw4NjAxQ3ZQdVlIMFlTOUxQSlJsQ3hjQVE5UGI2d1lRVUgyWVNUZVJCUTBMZldINElOMExQY3c5YWdiZVMzOGNnNmx2TzhmQjEyVmVIZWJjaTRhenpNUkxGUmlYSzdmZ29iUVYtc1J3Szl0Rm0yNGtUSGZzM2piUnRZUVZaMUVLcmJQc0g?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MU** | **9.52** | **5.78** | **7.00** | **379.30** | **800,708,231,168.00 USD** | **241.66** |
| WDC | 10.46 | 11.89 | 17.57 | 55.50 | 111,267,594,240.00 USD | 113.96 |
| STX | 27.27 | 34.60 | 20.59 | 61.00 | 119,394,721,792.00 USD | 120.29 |
| NXPI | 20.14 | 5.34 | 13.36 | 19.30 | 64,533,127,168.00 USD | 36.17 |

Peers fetched as_of: 2026-11-23; MU reuses existing data (market data as_of: 2026-11-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-30
- Next expected earnings: 2026-12-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-23

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-10-09
- Revenue (latest available single quarter): 8,440,000,000.00 USD; period 2018-06-01/2018-08-30; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 28,243,000,000.00 USD; period 2026-02-27/2026-05-28; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/723125/000072312526000023/mu-20260903.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMirgFBVV95cUxOaEc0VF9fdFRCeTVJU0lHMkxCYzVHLTd2NXZMc0toOWhlbUd5bEl3eTY4aVJoV0huWU1jR1FuVHExOWJLM1k4bmt5bXkzMl80cnliZEhURHhzMHhWZWdXWUg1d09LS1VaLU1ubXpCVWFqcEQ1VXpFX2h4a1hMMGgxdFoyUWZFdHRRWFZzaWY1RS1ndHppaV9xcUdUWHRNWktEeTh6NmRxMzkyc2dJQkE?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxPWi1laGRDdmxIMDBFMk8zaTEzNXRUUWV3VlNQRTYwM0VpMVlBcTFBcUVZUlhZd1FIUXJRM0xrcC1OM1VrYUljd0RmQ2R6WVBwbzh5U2hoR09KUG9maGc3ZERoQkpzNlVWb0dsdmg0MHBTMVFjUk1qcFNkV3pZcEN2TVJ6OUVBOFE0dF8xNjVBOWhTRS16eUR1ampBNURWN25ibm1vY25ydWVOZ2k4X0RxMVVCVQ?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxOODQ0aGxEM1BzSF9NdGdnY3FsbXZvR09xN2JKLUw4NjAxQ3ZQdVlIMFlTOUxQSlJsQ3hjQVE5UGI2d1lRVUgyWVNUZVJCUTBMZldINElOMExQY3c5YWdiZVMzOGNnNmx2TzhmQjEyVmVIZWJjaTRhenpNUkxGUmlYSzdmZ29iUVYtc1J3Szl0Rm0yNGtUSGZzM2piUnRZUVZaMUVLcmJQc0g?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
