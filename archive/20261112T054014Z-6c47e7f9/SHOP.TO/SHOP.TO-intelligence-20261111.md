# SHOP.TO Intelligence Report

- ticker: **SHOP.TO**
- Report as_of: **2026-11-11**
- Market data as_of: **2026-11-11**
- Quant sources: https://finance.yahoo.com/quote/SHOP.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SHOP.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-11**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-12T05:49:11.921790+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 3, 'rule': 0, 'ai': 1, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261111T043601Z-d14951e6/SHOP.TO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 3 unique headlines; 3 named publishers; 0 exact duplicates; 3 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-11-04

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 212.5700 |
| Return 1D (%) | 2.1382 |
| Return 1W (%) | -0.0658 |
| Return 1M (%) | -12.8204 |
| Return YTD (%) | -3.8145 |
| Return 1Y (%) | -4.5530 |
| Annualized volatility (%) | 58.3598 |
| Beta vs SPY | 1.6550 |
| Max drawdown (%) | -44.0932 |
| Sharpe (rf=0) | 0.2109 |
| Downside deviation (rf=0, %) | 40.8070 |
| Sortino (rf=0) | 0.3016 |
| Historical VaR 95% (1D, %) | 6.0443 |
| Historical ES 95% (1D, %) | 7.8139 |
| Correlation vs SPY | 0.3877 |
| Tracking error vs SPY (%) | 55.0262 |
| P/E (trailing) | 95.75 |
| P/B | 15.27 |
| EV/EBITDA | 103.92 |
| Revenue growth (%) | 31.60 |
| Forward P/E (estimate) | 61.58 |
| Gross margin (%) | 47.49 |
| Operating margin (%) | 18.07 |
| Return on equity (%) | 16.83 |
| Free cash flow yield (%) | N/A |
| MA50 | 213.6070 |
| Close vs MA50 (%) | -0.4855 |
| MA200 | 180.6111 |
| Close vs MA200 (%) | 17.6949 |
| RSI (14, Wilder) | 45.7285 |
| MACD (12,26) | -3.5370 |
| MACD signal (9) | -0.3992 |
| MACD histogram | -3.1379 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SHOP.TO': 279, 'SPY': 280}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 212.5700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.1382 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.0658 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -12.8204 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -3.8145 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -4.5530 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 58.3598 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 40.8070 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.3016 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 6.0443 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 7.8139 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3877 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 55.0262 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.6550 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -44.0932 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2109 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 61.5843 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 47.4910 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 18.0700 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 16.8330 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 95.7523 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 45.7285 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.1379 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -0.4855 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 17.6949 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Shopify Shows Strong FCF Results - Investors Bullish on SHOP With Unusual Call Option Activity
- Summary: Shopify reports strong free cash flow, boosting investor sentiment and option activity.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxOVVRZV18yQUFMN25aQkdyd1FYSGpzUzZYd2ljaUhJdmU5RzlSZ0hwV0hFZXA1QjV1TDZtV1I1cDJOY3R3SGx5b1AtY2tVU3NJVEFYSWdYU0k3d3h1SGZfQUVFVElaTG1xSUlrRWxFaTBZRlBZR2pnVUhMUkhtbkQ3UEN0RVVZWGFRbkVvTFpxNWx5MUF5clVTc1BLSzZBdnh6OFlnNjVVQVBpb2dOUF9ramJkYnkwWXlhTktTb0hUTFlQZF9MeXc5T2ZXenpOdWtwbUE?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SHOP.TO** | **95.75** | **15.27** | **103.92** | **31.60** | **273,475,993,600.00 CAD** | **-4.55** |
| WIX | N/A | -10.27 | -27.57 | 14.90 | 2,859,995,392.00 USD | -48.60 |
| CRM | 19.95 | 4.68 | 16.31 | 10.80 | 179,422,232,576.00 USD | -10.08 |
| GDDY | 15.55 | -100.04 | 11.53 | 6.00 | 13,769,530,368.00 USD | -13.77 |

Peers fetched as_of: 2026-11-11; SHOP.TO reuses existing data (market data as_of: 2026-11-11); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-03
- Next expected earnings: 2027-02-10 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-11

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

- https://news.google.com/rss/articles/CBMi0gFBVV95cUxOVVRZV18yQUFMN25aQkdyd1FYSGpzUzZYd2ljaUhJdmU5RzlSZ0hwV0hFZXA1QjV1TDZtV1I1cDJOY3R3SGx5b1AtY2tVU3NJVEFYSWdYU0k3d3h1SGZfQUVFVElaTG1xSUlrRWxFaTBZRlBZR2pnVUhMUkhtbkQ3UEN0RVVZWGFRbkVvTFpxNWx5MUF5clVTc1BLSzZBdnh6OFlnNjVVQVBpb2dOUF9ramJkYnkwWXlhTktTb0hUTFlQZF9MeXc5T2ZXenpOdWtwbUE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
