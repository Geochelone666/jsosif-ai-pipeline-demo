# AMTM Intelligence Report

- ticker: **AMTM**
- Report as_of: **2026-11-02**
- Market data as_of: **2026-11-02**
- Quant sources: https://finance.yahoo.com/quote/AMTM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMTM/key-statistics/
- AI analysis snapshot as_of: **2026-11-02**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-03T05:31:59.234776+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 3, 'rule': 1, 'ai': 1, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **N/A (no successful AI classification call)**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261102T041627Z-c84a7052/AMTM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 3 unique headlines; 2 named publishers; 0 exact duplicates; 3 HTTPS source links; largest publisher share 66.67%; oldest publication 2026-10-30

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 22.4700 |
| Return 1D (%) | 2.7435 |
| Return 1W (%) | 1.8124 |
| Return 1M (%) | 23.8699 |
| Return YTD (%) | -22.5172 |
| Return 1Y (%) | 0.2677 |
| Annualized volatility (%) | 46.9020 |
| Beta vs SPY | 1.1106 |
| Max drawdown (%) | -51.7186 |
| Sharpe (rf=0) | 0.2549 |
| Downside deviation (rf=0, %) | 30.0344 |
| Sortino (rf=0) | 0.3980 |
| Historical VaR 95% (1D, %) | 3.9749 |
| Historical ES 95% (1D, %) | 5.9781 |
| Correlation vs SPY | 0.3036 |
| Tracking error vs SPY (%) | 44.7104 |
| P/E (trailing) | 27.07 |
| P/B | 1.17 |
| EV/EBITDA | 8.90 |
| Revenue growth (%) | -2.00 |
| Forward P/E (estimate) | 8.51 |
| Gross margin (%) | 10.49 |
| Operating margin (%) | 4.38 |
| Return on equity (%) | 4.29 |
| Free cash flow yield (%) | 8.81 |
| MA50 | 19.8290 |
| Close vs MA50 (%) | 13.3189 |
| MA200 | 24.4211 |
| Close vs MA200 (%) | -7.9896 |
| RSI (14, Wilder) | 69.8766 |
| MACD (12,26) | 0.7534 |
| MACD signal (9) | 0.4565 |
| MACD histogram | 0.2970 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMTM': 273, 'SPY': 273}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 22.4700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.7435 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.8124 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 23.8699 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -22.5172 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 0.2677 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 46.9020 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 30.0344 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.3980 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.9749 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.9781 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3036 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 44.7104 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.1106 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -51.7186 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2549 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 8.5129 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 10.4880 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 4.3840 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 4.2870 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 8.8141 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 27.0723 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 69.8766 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.2970 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 13.3189 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -7.9896 -> Clearly below the moving-average trend level.

## TAILWINDS

### AMTM Q3 2026 Earnings: EPS Beats Estimates by 7.5% Despite Modest Stock Pullback - Estimate Revision Count
- Summary: AMTM Q3 2026 Earnings: EPS Beats Estimates by 7.5% Despite Modest Stock Pullback - Estimate Revision Count
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxNZUtILV9fWl9lbFpOUFFQblRVbC1VcFF5Y2I3WjR3N2ZkTFRZTTg4R09MbU45Z1ExdC1QVXRrSGhMZnNPVGROY1ROXzllVGJjQjZMVmlYR0paNHZEV2J5QU90bVRlQ25ILU5lUHZET0p6TWN1XzJTS0liUkZUdi1YYW92cXBYUFluOC00Q3FzZ1BUd20wdVIxTlN5eWpzMnVTRnFOUWdudk83RGp4TTh4QjVibWp1ckw2Tll0Qg?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### How Investors May Respond To Amentum Holdings (AMTM) Colorado Springs Expansion
- Summary: Investors react to Amentum’s expansion in Colorado Springs, potentially influencing stock performance.
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2wFBVV95cUxPOUJVTVFOeXJtT08yLUVPR2pjUl9oaDVLOGJQVFY5RXFObVRKZUJHMS00WVZsREsyYTRVNVE2TFp5aW81UnZPbGVFMFRyakxXZFl0b05HUmt4Tl9wTUVkS3hSQWRWNzBZUVl6VHNqaF80NUdiZ3F1TkJUOExGbGhySDBjNDdxbDZQaTNES0NlbGtQQ3lvT25kYlVwazVCX3g3Y3VIVmt3Q3NLNVZjSHFmTUk5eTVYS1RGYlRpQXltY2ktZHpVZXlNS0hkcFdBM0F5M1M1T05nc1JXRUXSAeABQVVfeXFMTzlsVW1aMEM1a0c4a1UxOTB5Z3ZuTHJtdVRhTVRaVUtYN0NiRUFQZDZDbXR4YXZBek9KaGQzeEtWT0hwb3p3OFM2dDZrSzVmSjZzWXI1cmVnc09PRGh1ZC1kajFwSENBajZmSG5TcmlfdzNzT2tPM1k1bnVKcFBoRW9fNW13WE13VXYzSmdlaTJIM1p3T1NGNURhdjdDMWw0WHoxYkxsOGV6M3RjdWJraVVYaTNjU0ljRVdSSklrLTZCWmFmU0FpMjhCTTJQamJsUzVCY0hTTklfQW5YQnNGYkw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMTM** | **27.07** | **1.17** | **8.90** | **-2.00** | **5,494,059,008.00 USD** | **0.27** |
| LDOS | 13.46 | 3.42 | 10.06 | 7.20 | 18,090,956,800.00 USD | -23.44 |
| CACI | 27.94 | 3.25 | 16.10 | 8.20 | 15,038,775,296.00 USD | 21.03 |
| SAIC | 17.84 | 4.47 | 11.93 | 6.30 | 6,406,567,424.00 USD | 65.36 |

Peers fetched as_of: 2026-11-02; AMTM reuses existing data (market data as_of: 2026-11-02); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-10
- Next expected earnings: 2026-11-23 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-02

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-11
- Revenue (latest available single quarter): 3,490,000,000.00 USD; period 2026-04-04/2026-07-03; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 66,000,000.00 USD; period 2026-04-04/2026-07-03; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/2011286/000162828026055727/amtm-20260703.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMivAFBVV95cUxNZUtILV9fWl9lbFpOUFFQblRVbC1VcFF5Y2I3WjR3N2ZkTFRZTTg4R09MbU45Z1ExdC1QVXRrSGhMZnNPVGROY1ROXzllVGJjQjZMVmlYR0paNHZEV2J5QU90bVRlQ25ILU5lUHZET0p6TWN1XzJTS0liUkZUdi1YYW92cXBYUFluOC00Q3FzZ1BUd20wdVIxTlN5eWpzMnVTRnFOUWdudk83RGp4TTh4QjVibWp1ckw2Tll0Qg?oc=5
- https://news.google.com/rss/articles/CBMi2wFBVV95cUxPOUJVTVFOeXJtT08yLUVPR2pjUl9oaDVLOGJQVFY5RXFObVRKZUJHMS00WVZsREsyYTRVNVE2TFp5aW81UnZPbGVFMFRyakxXZFl0b05HUmt4Tl9wTUVkS3hSQWRWNzBZUVl6VHNqaF80NUdiZ3F1TkJUOExGbGhySDBjNDdxbDZQaTNES0NlbGtQQ3lvT25kYlVwazVCX3g3Y3VIVmt3Q3NLNVZjSHFmTUk5eTVYS1RGYlRpQXltY2ktZHpVZXlNS0hkcFdBM0F5M1M1T05nc1JXRUXSAeABQVVfeXFMTzlsVW1aMEM1a0c4a1UxOTB5Z3ZuTHJtdVRhTVRaVUtYN0NiRUFQZDZDbXR4YXZBek9KaGQzeEtWT0hwb3p3OFM2dDZrSzVmSjZzWXI1cmVnc09PRGh1ZC1kajFwSENBajZmSG5TcmlfdzNzT2tPM1k1bnVKcFBoRW9fNW13WE13VXYzSmdlaTJIM1p3T1NGNURhdjdDMWw0WHoxYkxsOGV6M3RjdWJraVVYaTNjU0ljRVdSSklrLTZCWmFmU0FpMjhCTTJQamJsUzVCY0hTTklfQW5YQnNGYkw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
