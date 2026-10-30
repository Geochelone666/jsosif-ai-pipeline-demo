# CNQ.TO Intelligence Report

- ticker: **CNQ.TO**
- Report as_of: **2026-10-29**
- Market data as_of: **2026-10-29**
- Quant sources: https://finance.yahoo.com/quote/CNQ.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CNQ.TO/key-statistics/
- AI analysis snapshot as_of: **2026-10-29**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-30T02:21:47.158677+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 11, 'rule': 2, 'ai': 1, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261029T020157Z-688a53f0/CNQ.TO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 11 unique headlines; 7 named publishers; 1 exact duplicates; 11 HTTPS source links; largest publisher share 27.27%; oldest publication 2026-10-26

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 77.0500 |
| Return 1D (%) | 0.3517 |
| Return 1W (%) | 2.0530 |
| Return 1M (%) | 15.1547 |
| Return YTD (%) | 70.5421 |
| Return 1Y (%) | 79.1663 |
| Annualized volatility (%) | 30.4608 |
| Beta vs SPY | -0.5845 |
| Max drawdown (%) | -18.6770 |
| Sharpe (rf=0) | 2.0766 |
| Downside deviation (rf=0, %) | 20.5170 |
| Sortino (rf=0) | 3.0830 |
| Historical VaR 95% (1D, %) | 2.9758 |
| Historical ES 95% (1D, %) | 4.3580 |
| Correlation vs SPY | -0.2446 |
| Tracking error vs SPY (%) | 35.8180 |
| P/E (trailing) | 13.69 |
| P/B | 3.41 |
| EV/EBITDA | 9.22 |
| Revenue growth (%) | 69.50 |
| Forward P/E (estimate) | 12.35 |
| Gross margin (%) | 51.58 |
| Operating margin (%) | 43.09 |
| Return on equity (%) | 26.68 |
| Free cash flow yield (%) | 4.67 |
| MA50 | 70.7750 |
| Close vs MA50 (%) | 8.8662 |
| MA200 | 62.6419 |
| Close vs MA200 (%) | 23.0008 |
| RSI (14, Wilder) | 68.0523 |
| MACD (12,26) | 2.1779 |
| MACD signal (9) | 1.9802 |
| MACD histogram | 0.1977 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CNQ.TO': 270, 'SPY': 271}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 77.0500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.3517 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.0530 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 15.1547 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 70.5421 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 79.1663 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 30.4608 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 20.5170 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 3.0830 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9758 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.3580 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.2446 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 35.8180 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.5845 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -18.6770 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 2.0766 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 12.3477 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 51.5760 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 43.0910 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 26.6850 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.6715 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 13.6856 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 68.0523 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.1977 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 8.8662 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 23.0008 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Canadian Natural Resources Limited $CNQ Stock Sold by Miller Howard Investments Inc. NY
- Summary: Canadian Natural Resources Limited $CNQ Stock Sold by Miller Howard Investments Inc. NY
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3wFBVV95cUxPendDY1NSOGdCQmRWM09pMFNCaUJiUkkzaGFTWi14ZEtNeEhFUW5TZ0RjSV9hZVhHTEQzTWJKQ19pWW5xaTBUb3NQb2NVZXBIRm4teG1TUkFrc2ZyV2hQaWVQeDJPNl8zY0lCTG1BMUhHeWo4UUY1NjdVZW51aVoxcTFjdG9jYklBd09MQldFaDlZQjA0UlZmdlBqd2wxYTV1RkEyVmlIZkppZEVGN0xqeUswVWFBbEhPeWRxUnFhUm5MUlZwWG5sNUtnNkxTNElPdlY2Nk81SmZobzExVzBj?oc=5>

### Canadian Natural Resources (CNQ) Set to Release Earnings on Thursday
- Summary: Canadian Natural Resources (CNQ) Set to Release Earnings on Thursday
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxNcmEtZU9MZmRSaC1vdmVRYjlXLW1aV1gtWm5OeG1LdVdkTTJpeFJsd2M5WHU3Q2RPN2tPM29pUldwRTJHNE56ZFBnMVh0MFpmdTBSNDRERUxhdzFXTkNPQTJjc1c1Um1DSFA5bTZDdnRmb3diVFBXTHBweFBKdG03cFF3Z0hqX1Vwb1BWQmxuRExoekptb19wcVFVVTk4REo2eEtDZjZLOWhzS1lCcC1YVC1aOExpQktFeHBKWXk5Mm16NXhUUW5vbQ?oc=5>

### ATB Cormark raises target for Canadian Natural Resources stock to CAD 85.00
- Summary: ATB Cormark lifts its target price for CNQ.TO to CAD 85.00, signaling bullish outlook.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxQUlBEQUhZajB6MVllMGVCNFJrVldPVFZNZHZNQ0lHY2NFVjdBVHFobVowYjdDMlNEMzRnOHVtdFFuRTU5LVp2V2VSRzQtdVJMeDJTNmx6TGUta1pBb2ZEdFYyTHBHZjdFS1c1VEloaEhCU29idGg2YWJJbDZrWnQzamhaMEV5WThUUG1nQU1pVl9BcGxDYVdtd1pZQ2lsQ1BaWDNVRGpsRGZKdWhvaktiVHB2TzV3ZzNhSjRzQ05JZ0h2dzllOFYxT211c1pJQUV5WHV5Vw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CNQ.TO** | **13.69** | **3.41** | **9.22** | **69.50** | **158,838,587,392.00 CAD** | **79.17** |
| SU.TO | 14.51 | 2.65 | 6.99 | 45.90 | 128,287,973,376.00 CAD | 100.78 |
| IMO.TO | 21.48 | 3.62 | 11.00 | 42.60 | 88,797,290,496.00 CAD | 45.49 |
| CVE.TO | 12.54 | 2.43 | 6.38 | 41.50 | 83,027,910,656.00 CAD | 93.88 |

Peers fetched as_of: 2026-10-29; CNQ.TO reuses existing data (market data as_of: 2026-10-29); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-06
- Next expected earnings: 2026-11-05 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-29

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMi3wFBVV95cUxPendDY1NSOGdCQmRWM09pMFNCaUJiUkkzaGFTWi14ZEtNeEhFUW5TZ0RjSV9hZVhHTEQzTWJKQ19pWW5xaTBUb3NQb2NVZXBIRm4teG1TUkFrc2ZyV2hQaWVQeDJPNl8zY0lCTG1BMUhHeWo4UUY1NjdVZW51aVoxcTFjdG9jYklBd09MQldFaDlZQjA0UlZmdlBqd2wxYTV1RkEyVmlIZkppZEVGN0xqeUswVWFBbEhPeWRxUnFhUm5MUlZwWG5sNUtnNkxTNElPdlY2Nk81SmZobzExVzBj?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxNcmEtZU9MZmRSaC1vdmVRYjlXLW1aV1gtWm5OeG1LdVdkTTJpeFJsd2M5WHU3Q2RPN2tPM29pUldwRTJHNE56ZFBnMVh0MFpmdTBSNDRERUxhdzFXTkNPQTJjc1c1Um1DSFA5bTZDdnRmb3diVFBXTHBweFBKdG03cFF3Z0hqX1Vwb1BWQmxuRExoekptb19wcVFVVTk4REo2eEtDZjZLOWhzS1lCcC1YVC1aOExpQktFeHBKWXk5Mm16NXhUUW5vbQ?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxQUlBEQUhZajB6MVllMGVCNFJrVldPVFZNZHZNQ0lHY2NFVjdBVHFobVowYjdDMlNEMzRnOHVtdFFuRTU5LVp2V2VSRzQtdVJMeDJTNmx6TGUta1pBb2ZEdFYyTHBHZjdFS1c1VEloaEhCU29idGg2YWJJbDZrWnQzamhaMEV5WThUUG1nQU1pVl9BcGxDYVdtd1pZQ2lsQ1BaWDNVRGpsRGZKdWhvaktiVHB2TzV3ZzNhSjRzQ05JZ0h2dzllOFYxT211c1pJQUV5WHV5Vw?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxQSDR0SmwxRW55WEw3Y0hRTDdFWVFZcjgxTzk1bXlsNUFNSjIxdXpzeTFDWFVNVndKME5GcW4tV005SUhwN1B2dGJNdnFueU51bGN2TktaYzZzb0UzVUJTQzVLcTNVVjA3cUE1Z0k2dGJhS0ZvUFgza0ZlbUN4M05JNURSeUxWRWdDLWtDa2JfT0JGcGw0d1RHOVFQaERianJKSDIxWkFNTlpFYW9tRGItUENRMVBUTzdJNkVWa1V5X3Aycm11aVAxRWxuckpGN3o4eEwwQw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
