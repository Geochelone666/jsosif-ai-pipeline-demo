# XYL Intelligence Report

- ticker: **XYL**
- Report as_of: **2026-11-16**
- Market data as_of: **2026-11-16**
- Quant sources: https://finance.yahoo.com/quote/XYL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/XYL/key-statistics/
- AI analysis snapshot as_of: **2026-11-16**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-17T06:46:13.771767+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 4, 'rule': 2, 'ai': 1, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261115T044154Z-6abfba73/XYL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 4 unique headlines; 4 named publishers; 0 exact duplicates; 4 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-11-10

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 95.9300 |
| Return 1D (%) | 1.8581 |
| Return 1W (%) | -3.3548 |
| Return 1M (%) | -7.8039 |
| Return YTD (%) | -28.7705 |
| Return 1Y (%) | -31.8470 |
| Annualized volatility (%) | 30.7076 |
| Beta vs SPY | 0.5735 |
| Max drawdown (%) | -38.9486 |
| Sharpe (rf=0) | -1.0603 |
| Downside deviation (rf=0, %) | 25.1507 |
| Sortino (rf=0) | -1.2945 |
| Historical VaR 95% (1D, %) | 2.9666 |
| Historical ES 95% (1D, %) | 5.0929 |
| Correlation vs SPY | 0.2571 |
| Tracking error vs SPY (%) | 30.2504 |
| P/E (trailing) | 21.27 |
| P/B | 2.15 |
| EV/EBITDA | 12.50 |
| Revenue growth (%) | -3.00 |
| Forward P/E (estimate) | 16.40 |
| Gross margin (%) | 39.32 |
| Operating margin (%) | 15.51 |
| Return on equity (%) | 9.76 |
| Free cash flow yield (%) | 5.50 |
| MA50 | 102.0836 |
| Close vs MA50 (%) | -6.0280 |
| MA200 | 114.3405 |
| Close vs MA200 (%) | -16.1014 |
| RSI (14, Wilder) | 44.1198 |
| MACD (12,26) | -2.1470 |
| MACD signal (9) | -2.0978 |
| MACD histogram | -0.0492 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'XYL': 283, 'SPY': 283}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 95.9300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.8581 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -3.3548 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -7.8039 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -28.7705 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -31.8470 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 30.7076 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 25.1507 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -1.2945 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9666 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.0929 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2571 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 30.2504 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5735 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -38.9486 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -1.0603 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.3971 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 39.3200 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 15.5090 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.7560 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 5.5017 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 21.2705 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 44.1198 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.0492 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -6.0280 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -16.1014 -> Clearly below the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Xylem Inc. $XYL Shares Sold by AEGON ASSET MANAGEMENT UK Plc
- Summary: Xylem Inc. $XYL Shares Sold by AEGON ASSET MANAGEMENT UK Plc
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxNa3d5MEhoVm0wZW5PM0tMZHBEOS05UjdTd0M1S2VaaTVCcUozQ2hkUGE2eGFVOURKcXpFMVJiVUd3eC1OSUV3ZTdscGJJTE11Y2ZXM0t2V0xxdG9zM1Ztc1lKMll0cnU3TUpvNWJRM1QtU0RlckxvS21UYWVBLVF0Ny0yTnNuM2pvWXI5RHFHYzJ4ZGlWOGpqazQ1WjVnVkR3dGxYNV95cERMR1RtWk5RMzVKTW1FdmFwSUVF?oc=5>

### Xylem (XYL) Launches $1.5 Billion Share Buyback Program
- Summary: Xylem (XYL) Launches $1.5 Billion Share Buyback Program
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQall3WF9mRnhDeUVKcTU1b29pSkhqVWtkdWl4VWtPSExrbFlFbHIyeWFxY012enFEYUVMQTU2LVYtOXdPbF9xZVpZQ3VLYXhfYVlOS25mUWJjTVI4R2ZDeVllbm5WMXNMS05uU0sya1dnSDhDaVJrRTM3S0F4LXZmS2JlUTFLMWJzVnJ0UkFUbDZfeVFG?oc=5>

### Key facts: Xylem $1.5B buyback; 2027 growth; data center orders +200%
- Summary: Xylem announces a $1.5B share buyback, signals confidence and supports stock price.
- Date: 2026-11-14 | Impact: high | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxOaUh4VnlRUVZQRWkzclIycmNJNlJJdEREdmg1UHNGTDFUODBYYW1odkV5Rmg4bVdIZjdsTzFxNDVlTjJyUkFacldMM1ZkaVhOV3pGeEFHVFdpZ3BwV2RlS0YtalRSZXNILUVSVlpfT2R2V2hldTBwTWV2SC1XZ3FKS3pUXzZFcllrM051S01NYXgxVEdCb3NoeEptTWV2T2hSQWpLWWF3Z2ZveHhoaU9kdV9TUDlsZnZMbUxXNkhEamtianM?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **XYL** | **21.27** | **2.15** | **12.50** | **-3.00** | **22,000,066,560.00 USD** | **-31.85** |
| AOS | 17.85 | 4.71 | 11.54 | -0.20 | 8,583,620,608.00 USD | 0.96 |
| PH | 32.11 | 7.38 | 22.59 | 17.90 | 117,875,277,824.00 USD | 13.29 |
| DOV | 24.05 | 3.59 | 14.79 | 7.50 | 27,415,543,808.00 USD | 13.71 |

Peers fetched as_of: 2026-11-16; XYL reuses existing data (market data as_of: 2026-11-16); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-27
- Next expected earnings: 2027-02-09 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-16

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

- https://news.google.com/rss/articles/CBMiuwFBVV95cUxNa3d5MEhoVm0wZW5PM0tMZHBEOS05UjdTd0M1S2VaaTVCcUozQ2hkUGE2eGFVOURKcXpFMVJiVUd3eC1OSUV3ZTdscGJJTE11Y2ZXM0t2V0xxdG9zM1Ztc1lKMll0cnU3TUpvNWJRM1QtU0RlckxvS21UYWVBLVF0Ny0yTnNuM2pvWXI5RHFHYzJ4ZGlWOGpqazQ1WjVnVkR3dGxYNV95cERMR1RtWk5RMzVKTW1FdmFwSUVF?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQall3WF9mRnhDeUVKcTU1b29pSkhqVWtkdWl4VWtPSExrbFlFbHIyeWFxY012enFEYUVMQTU2LVYtOXdPbF9xZVpZQ3VLYXhfYVlOS25mUWJjTVI4R2ZDeVllbm5WMXNMS05uU0sya1dnSDhDaVJrRTM3S0F4LXZmS2JlUTFLMWJzVnJ0UkFUbDZfeVFG?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxOaUh4VnlRUVZQRWkzclIycmNJNlJJdEREdmg1UHNGTDFUODBYYW1odkV5Rmg4bVdIZjdsTzFxNDVlTjJyUkFacldMM1ZkaVhOV3pGeEFHVFdpZ3BwV2RlS0YtalRSZXNILUVSVlpfT2R2V2hldTBwTWV2SC1XZ3FKS3pUXzZFcllrM051S01NYXgxVEdCb3NoeEptTWV2T2hSQWpLWWF3Z2ZveHhoaU9kdV9TUDlsZnZMbUxXNkhEamtianM?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
