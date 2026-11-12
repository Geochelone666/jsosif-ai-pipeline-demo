# MCO Intelligence Report

- ticker: **MCO**
- Report as_of: **2026-11-11**
- Market data as_of: **2026-11-11**
- Quant sources: https://finance.yahoo.com/quote/MCO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MCO/key-statistics/
- AI analysis snapshot as_of: **2026-11-11**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-12T06:03:25.705503+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 6, 'rule': 0, 'ai': 4, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261111T043601Z-d14951e6/MCO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 6 unique headlines; 5 named publishers; 0 exact duplicates; 6 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-11-05

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 514.9300 |
| Return 1D (%) | 0.8263 |
| Return 1W (%) | -2.5381 |
| Return 1M (%) | 10.9213 |
| Return YTD (%) | 1.4716 |
| Return 1Y (%) | 5.3542 |
| Annualized volatility (%) | 28.5299 |
| Beta vs SPY | 0.5214 |
| Max drawdown (%) | -23.6059 |
| Sharpe (rf=0) | 0.3262 |
| Downside deviation (rf=0, %) | 20.2196 |
| Sortino (rf=0) | 0.4603 |
| Historical VaR 95% (1D, %) | 2.4637 |
| Historical ES 95% (1D, %) | 3.8509 |
| Correlation vs SPY | 0.2509 |
| Tracking error vs SPY (%) | 28.3884 |
| P/E (trailing) | 31.42 |
| P/B | 27.17 |
| EV/EBITDA | 23.45 |
| Revenue growth (%) | 0.80 |
| Forward P/E (estimate) | 27.68 |
| Gross margin (%) | 74.63 |
| Operating margin (%) | 46.04 |
| Return on equity (%) | 76.74 |
| Free cash flow yield (%) | 2.85 |
| MA50 | 477.9308 |
| Close vs MA50 (%) | 7.7415 |
| MA200 | 465.0096 |
| Close vs MA200 (%) | 10.7353 |
| RSI (14, Wilder) | 62.0452 |
| MACD (12,26) | 11.3159 |
| MACD signal (9) | 9.2919 |
| MACD histogram | 2.0240 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MCO': 280, 'SPY': 280}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 514.9300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.8263 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.5381 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 10.9213 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 1.4716 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 5.3542 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 28.5299 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 20.2196 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4603 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.4637 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.8509 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2509 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 28.3884 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5214 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -23.6059 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3262 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 27.6750 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.6330 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 46.0370 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 76.7410 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.8547 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 31.4173 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 62.0452 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 2.0240 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 7.7415 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 10.7353 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Moody's Corporation $MCO Stock: Kestra Advisory Services LLC Grows Stake
- Summary: Kestra Advisory Services LLC increased its stake in Moody’s Corporation.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxPd1Fhd2c3VmhwaFVlTEZQQ191c3J5M04waktmWjhibGpuYmhqTkRuQU94R2wzVzVKX1ItYUxlekVPMjFJX3I2THdsRmRhQW1OcFhRSXc3d3NNa3hsMVN2YVo1SVN5NWlaS1dsLVJ5Q1hHWUZnaldzV1VDZE53azVnQ1JwT0RMcDB0M3V4ZzJIaDBfcDZiQ3FCZ0stUkxmLXA5Tld0RXR1bGQ5UTNjalNwNUFtbXJaV0RvT0dmbmJINm5Pa3FKbGJfSjRR?oc=5>

### An officer and director proposes selling 1,743 Moody's (MCO) shares worth $890K.
- Summary: An officer and director plans to sell 1,743 shares, potentially indicating a shift in ownership structure.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQSldjcFBrWm0zQUtlUW1SUE1CUE1TZFNBRTFOWno3SVBQclJxSDRyOWZ5MXo1TUx4U2tINWNZNGNUcy1Wb2kwRGZUeTZOcEtGbXJTSWpHSi1Oam56TkhFU3hLcko3TkZqTk5LRVZRY0w0ekFZUDBlUjczcjAyRTR1SDRSakpCdDVVQVd3UXg5SlJiZmk5?oc=5>

### Moody's (MCO) Tests On Chain Ratings, Is The Stock Already Expensive?
- Summary: Moody's tests on-chain ratings, questioning stock valuation.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNY0NZT0RkQ2xPNm1POUhHbXI5dmY1ZlNYN2tocnFrbzlsY2diX3F3eDEwX3NzUGxWTzAyYU9zaGdKazVSSlpzMnFZbENBRFcwZkNDQ0ltZ25ZTTR6T3Jzd1ZYQTlUTWNtM0gyUExFU3ljMG9RWEVTdmgxc2FOT0JxcWl3dldUc1l2WWdpX29MRXRFR1dNMTA5MUJMRQ?oc=5>

## RISKS

### Insider Selling: Moody's (NYSE:MCO) CEO Sells $890,237.25 in Stock
- Summary: CEO sells nearly $890k in MCO shares.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxPcy1oUEo5UTlhTVkwTHplb3h2MWp0MElQdURGMnB4NzV3QlpMdmJnUkVodXpwRlA3d1pOLUwxM3ZNUzhEemVOaDVSazNBbzdycm85YnMyZkxudi1NVGJfSUFNNjV2RmdvTFZfRENoOHQyS0JVS1djc2xCbm1acHVpNmZmYnNGU1lEVEFicEhNSXU2LVF5SGN2U19vVFhNSno5U2NSbVZaeEdTeTBZTGI3RVBsWFVtaVh2Wm5rdG9R?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MCO** | **31.42** | **27.17** | **23.45** | **0.80** | **88,786,329,600.00 USD** | **5.35** |
| SPGI | 28.28 | 6.99 | 18.37 | 6.80 | 137,734,389,760.00 USD | 1.79 |
| MSCI | 34.98 | -15.72 | 26.72 | 12.40 | 47,299,395,584.00 USD | 14.83 |
| FDS | 22.98 | 5.90 | 14.53 | 6.30 | 11,811,174,400.00 USD | 25.53 |

Peers fetched as_of: 2026-11-11; MCO reuses existing data (market data as_of: 2026-11-11); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-02-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-11

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

- https://news.google.com/rss/articles/CBMiygFBVV95cUxPd1Fhd2c3VmhwaFVlTEZQQ191c3J5M04waktmWjhibGpuYmhqTkRuQU94R2wzVzVKX1ItYUxlekVPMjFJX3I2THdsRmRhQW1OcFhRSXc3d3NNa3hsMVN2YVo1SVN5NWlaS1dsLVJ5Q1hHWUZnaldzV1VDZE53azVnQ1JwT0RMcDB0M3V4ZzJIaDBfcDZiQ3FCZ0stUkxmLXA5Tld0RXR1bGQ5UTNjalNwNUFtbXJaV0RvT0dmbmJINm5Pa3FKbGJfSjRR?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQSldjcFBrWm0zQUtlUW1SUE1CUE1TZFNBRTFOWno3SVBQclJxSDRyOWZ5MXo1TUx4U2tINWNZNGNUcy1Wb2kwRGZUeTZOcEtGbXJTSWpHSi1Oam56TkhFU3hLcko3TkZqTk5LRVZRY0w0ekFZUDBlUjczcjAyRTR1SDRSakpCdDVVQVd3UXg5SlJiZmk5?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNY0NZT0RkQ2xPNm1POUhHbXI5dmY1ZlNYN2tocnFrbzlsY2diX3F3eDEwX3NzUGxWTzAyYU9zaGdKazVSSlpzMnFZbENBRFcwZkNDQ0ltZ25ZTTR6T3Jzd1ZYQTlUTWNtM0gyUExFU3ljMG9RWEVTdmgxc2FOT0JxcWl3dldUc1l2WWdpX29MRXRFR1dNMTA5MUJMRQ?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxPcy1oUEo5UTlhTVkwTHplb3h2MWp0MElQdURGMnB4NzV3QlpMdmJnUkVodXpwRlA3d1pOLUwxM3ZNUzhEemVOaDVSazNBbzdycm85YnMyZkxudi1NVGJfSUFNNjV2RmdvTFZfRENoOHQyS0JVS1djc2xCbm1acHVpNmZmYnNGU1lEVEFicEhNSXU2LVF5SGN2U19vVFhNSno5U2NSbVZaeEdTeTBZTGI3RVBsWFVtaVh2Wm5rdG9R?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
