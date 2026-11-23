# SCHW Intelligence Report

- ticker: **SCHW**
- Report as_of: **2026-11-22**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/SCHW/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SCHW/key-statistics/
- AI analysis snapshot as_of: **2026-11-22**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-23T05:49:11.682095+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 7, 'rule': 2, 'ai': 4, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261122T045655Z-f5ef568d/SCHW** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 7 unique headlines; 4 named publishers; 0 exact duplicates; 7 HTTPS source links; largest publisher share 42.86%; oldest publication 2026-11-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 90.1600 |
| Return 1D (%) | -2.1277 |
| Return 1W (%) | -3.0329 |
| Return 1M (%) | -0.4559 |
| Return YTD (%) | -8.5451 |
| Return 1Y (%) | 0.9754 |
| Annualized volatility (%) | 25.7113 |
| Beta vs SPY | 0.4118 |
| Max drawdown (%) | -22.5253 |
| Sharpe (rf=0) | 0.1673 |
| Downside deviation (rf=0, %) | 19.4308 |
| Sortino (rf=0) | 0.2214 |
| Historical VaR 95% (1D, %) | 2.5277 |
| Historical ES 95% (1D, %) | 3.9438 |
| Correlation vs SPY | 0.2290 |
| Tracking error vs SPY (%) | 26.4027 |
| P/E (trailing) | 15.41 |
| P/B | 3.44 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 16.90 |
| Forward P/E (estimate) | 11.55 |
| Gross margin (%) | 97.51 |
| Operating margin (%) | 51.11 |
| Return on equity (%) | 21.11 |
| Free cash flow yield (%) | N/A |
| MA50 | 94.9694 |
| Close vs MA50 (%) | -5.0642 |
| MA200 | 96.0926 |
| Close vs MA200 (%) | -6.1738 |
| RSI (14, Wilder) | 41.3010 |
| MACD (12,26) | -0.6936 |
| MACD signal (9) | -1.0279 |
| MACD histogram | 0.3343 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SCHW': 287, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 90.1600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.1277 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -3.0329 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -0.4559 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -8.5451 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 0.9754 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 25.7113 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 19.4308 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.2214 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.5277 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.9438 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2290 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.4027 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.4118 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -22.5253 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1673 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 11.5549 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 97.5060 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 51.1070 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 21.1130 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 15.4120 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 41.3010 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.3343 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -5.0642 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -6.1738 -> Clearly below the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

### Charles Schwab Sells $7M As Shares Recover From Three-Month Slide
- Summary: Charles Schwab Sells $7M As Shares Recover From Three-Month Slide
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxOeEtVSXlKVTkxc01tR1RBc1ltVmNsVU56dElFUmNrQ080VlpmQk1wd1QybndwY0ZqaFFlaDJSRk13ZWFtc2hmSi01cXhBMFZkYnR1YllkcS0zbF9DYTdCSGtBTGZNUGlNbjBmNzJXMmZ6Zzl5UUhLMjJpdXliazBHTWtPVnBaN01CZnBGLU9qQm41cWVWS20xeXkteVB5bVVYbHFRYUNYaExZRjFqNGRKSDEzcUU1dTEzbXY1SmJsdXVVd3gxVmtMSVRpckZadw?oc=5>

## CATALYSTS

### Charles Schwab (SCHW) Now Has The Largest U.S. Dividend ETF
- Summary: Charles Schwab (SCHW) Now Has The Largest U.S. Dividend ETF
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOUUlPTDRtRVdHM3EtT3ZLLW5IYjh6T1lJVEJvVGVqMjlXTVJBU0hBXy02WTZuMWJpd0ZfSnA2MXE4dmt6MFR5VU5PSTd1akxUanpqMm1Fczk4MEtia294aW92RjNGX0tvTmxMdm9WZVJPZlhTUVp5SHZWUURWQ215VGRTdTVHb0E1Sm9mRzVQMGtRcEJxbG9EazQwbDI?oc=5>

### Charles Schwab (SCHW) Stock May Be 31% Undervalued Despite Its AI Push
- Summary: Despite AI initiatives, Schwab shares could still be 31% undervalued, indicating growth prospects.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3AFBVV95cUxPSHZvbHFlWHlyVmUxeW5GaGFQQ19JVVhMUE1aNEtTbmNaUGMxUXo5TTRpZTJjalFMZFU4Yllxczc3eGpCd2I4YWotaE05c2l4U1Ewd1ZtRzdiZC0yNlN4RjFlV0Nvc1dfTzE4bVJ0RjAzQ1A4T1QzS2Z6cnU3dl9ZVjJpVG1FaDV1T3BfZmNKTkw2dENTdjlEdGpBSVNVUDhVRkxWTENWd2EtX3lBaHZDTjVrRldVMFg1OFJyemlncGxFc2paRE8yeW9xTE9OTjVCSWQ1U0lqS3k4bGE00gHiAUFVX3lxTFBWNkdaTzBjTXdFeFZ0aUZsZllCWEhiOE1HSzJlUG9GS0tXaHNZaFpUVXFQbzFZblQwb0dCQWxfQWdQby0tV0duSTJrbDhTWmkwMGlXVFhwMkNXdmdCck4xRjMtR0FSa3kwQjVsUnl3b1hySEhabXU3M3JVOXEtMlZ3dE5GTHJkYWxMbXRINXZuRHlIYjI2LWp4a2VGM3ZZMVJVbDFxVTEtczVBLWJubnZqQjJqUWRkYUdZZVZqckducmdBbnpJcGNuZEg2aDlJbDNLeGJ3a0g4ek1XbzhCVlV1ZlE?oc=5>

### Charles Schwab (SCHW) Stock Could Be 31% Undervalued Today
- Summary: Analysts suggest Schwab may be undervalued, indicating potential upside for investors.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNQ2RBVldIelIyQllkU2JKVG9Hb3U3T01xUlRRM3pUVUtHVHpFV0dNTjhDMkduOENYZElfNjk3TmxoNC1MaENZYW8xME5nVEJ4Z3BQbzEzWVlNY0VyMG5FSkZ4Nm9HVE1QVmR1dWI1VllEM0p3UEYzQ0hUWXJWWmlzcW44aWwxbm9DSXVhc0lyNmRmbzVTQ3FaajUxTHE?oc=5>

### Charles Schwab (NYSE:SCHW) Stock Forecast & Analyst Predictions
- Summary: Analyst forecasts predict Schwab’s stock performance, offering guidance for investors.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxQU0RWa3FoWHptMkgzMlkxeV9LQzZmMjN0TVZjN0hZYmZhTHR1QXlQQnZKZzR1WVZpX0daSF90V3JtLUVkMkRKY3dvbHNTR3MxNl82WVc3ZUlIZkNCSlB6Q2RncnpDZHRsN0w1TXduaE41cldTeWt5bTNMckU1dnkzRGpoWFl3aTh0cTdmVXl0dw?oc=5>

### Barclays Sticks to Their Buy Rating for Charles Schwab (SCHW)
- Summary: Barclays maintains a buy rating on Schwab, supporting a positive outlook.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3AFBVV95cUxQb1RBdTBsNFdnNGQtUmRPNzlKbENWOE5Xa2VQTEdjc2Mybll5YXhFb0djS09tem5JMmdBbEhTZVpuSlRhMjVWWmVkYWJjR25pZklPb29oaEhUQmVCZl92VXVJQUdkSVEtSC0ybmRKQ19sQkRyRk1vZ3JkQTZUck5hZTk2dWRyWGVfUzNlZWtlSEYtVDRrbU16QzBuTjdCeXR3dXlDekt6VnJvejVULUFiWkNBSDYxdU93dzZsRGlGSDdFOWlNNEtsVW9uNUZ0U2M4dzFkS282ejBHRnFF?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SCHW** | **15.41** | **3.44** | **N/A** | **16.90** | **155,616,854,016.00 USD** | **0.98** |
| IBKR | 27.17 | 5.19 | N/A | 13.50 | 121,296,453,632.00 USD | 16.13 |
| HOOD | 28.65 | 5.60 | N/A | 11.80 | 55,983,542,272.00 USD | -41.47 |
| LPLA | 15.16 | 3.56 | N/A | 17.80 | 20,600,868,864.00 USD | -22.54 |

Peers fetched as_of: 2026-11-22; SCHW reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-21 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-22

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-06
- Revenue (latest available single quarter): 7,171,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 2,906,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/316709/000031670926000038/schw-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMizgFBVV95cUxOeEtVSXlKVTkxc01tR1RBc1ltVmNsVU56dElFUmNrQ080VlpmQk1wd1QybndwY0ZqaFFlaDJSRk13ZWFtc2hmSi01cXhBMFZkYnR1YllkcS0zbF9DYTdCSGtBTGZNUGlNbjBmNzJXMmZ6Zzl5UUhLMjJpdXliazBHTWtPVnBaN01CZnBGLU9qQm41cWVWS20xeXkteVB5bVVYbHFRYUNYaExZRjFqNGRKSDEzcUU1dTEzbXY1SmJsdXVVd3gxVmtMSVRpckZadw?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOUUlPTDRtRVdHM3EtT3ZLLW5IYjh6T1lJVEJvVGVqMjlXTVJBU0hBXy02WTZuMWJpd0ZfSnA2MXE4dmt6MFR5VU5PSTd1akxUanpqMm1Fczk4MEtia294aW92RjNGX0tvTmxMdm9WZVJPZlhTUVp5SHZWUURWQ215VGRTdTVHb0E1Sm9mRzVQMGtRcEJxbG9EazQwbDI?oc=5
- https://news.google.com/rss/articles/CBMi3AFBVV95cUxPSHZvbHFlWHlyVmUxeW5GaGFQQ19JVVhMUE1aNEtTbmNaUGMxUXo5TTRpZTJjalFMZFU4Yllxczc3eGpCd2I4YWotaE05c2l4U1Ewd1ZtRzdiZC0yNlN4RjFlV0Nvc1dfTzE4bVJ0RjAzQ1A4T1QzS2Z6cnU3dl9ZVjJpVG1FaDV1T3BfZmNKTkw2dENTdjlEdGpBSVNVUDhVRkxWTENWd2EtX3lBaHZDTjVrRldVMFg1OFJyemlncGxFc2paRE8yeW9xTE9OTjVCSWQ1U0lqS3k4bGE00gHiAUFVX3lxTFBWNkdaTzBjTXdFeFZ0aUZsZllCWEhiOE1HSzJlUG9GS0tXaHNZaFpUVXFQbzFZblQwb0dCQWxfQWdQby0tV0duSTJrbDhTWmkwMGlXVFhwMkNXdmdCck4xRjMtR0FSa3kwQjVsUnl3b1hySEhabXU3M3JVOXEtMlZ3dE5GTHJkYWxMbXRINXZuRHlIYjI2LWp4a2VGM3ZZMVJVbDFxVTEtczVBLWJubnZqQjJqUWRkYUdZZVZqckducmdBbnpJcGNuZEg2aDlJbDNLeGJ3a0g4ek1XbzhCVlV1ZlE?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNQ2RBVldIelIyQllkU2JKVG9Hb3U3T01xUlRRM3pUVUtHVHpFV0dNTjhDMkduOENYZElfNjk3TmxoNC1MaENZYW8xME5nVEJ4Z3BQbzEzWVlNY0VyMG5FSkZ4Nm9HVE1QVmR1dWI1VllEM0p3UEYzQ0hUWXJWWmlzcW44aWwxbm9DSXVhc0lyNmRmbzVTQ3FaajUxTHE?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxQU0RWa3FoWHptMkgzMlkxeV9LQzZmMjN0TVZjN0hZYmZhTHR1QXlQQnZKZzR1WVZpX0daSF90V3JtLUVkMkRKY3dvbHNTR3MxNl82WVc3ZUlIZkNCSlB6Q2RncnpDZHRsN0w1TXduaE41cldTeWt5bTNMckU1dnkzRGpoWFl3aTh0cTdmVXl0dw?oc=5
- https://news.google.com/rss/articles/CBMi3AFBVV95cUxQb1RBdTBsNFdnNGQtUmRPNzlKbENWOE5Xa2VQTEdjc2Mybll5YXhFb0djS09tem5JMmdBbEhTZVpuSlRhMjVWWmVkYWJjR25pZklPb29oaEhUQmVCZl92VXVJQUdkSVEtSC0ybmRKQ19sQkRyRk1vZ3JkQTZUck5hZTk2dWRyWGVfUzNlZWtlSEYtVDRrbU16QzBuTjdCeXR3dXlDekt6VnJvejVULUFiWkNBSDYxdU93dzZsRGlGSDdFOWlNNEtsVW9uNUZ0U2M4dzFkS282ejBHRnFF?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
