# SHOP.TO Intelligence Report

- ticker: **SHOP.TO**
- Report as_of: **2026-11-04**
- Market data as_of: **2026-11-04**
- Quant sources: https://finance.yahoo.com/quote/SHOP.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SHOP.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-04**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-05T05:20:33.612526+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 6, 'rule': 5, 'ai': 1, 'unknown': 0})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 6 unique headlines; 3 named publishers; 0 exact duplicates; 6 HTTPS source links; largest publisher share 66.67%; oldest publication 2026-11-02

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 212.7100 |
| Return 1D (%) | 6.2541 |
| Return 1W (%) | -9.6658 |
| Return 1M (%) | -1.4593 |
| Return YTD (%) | -3.7511 |
| Return 1Y (%) | -6.3900 |
| Annualized volatility (%) | 58.1584 |
| Beta vs SPY | 1.7533 |
| Max drawdown (%) | -44.0932 |
| Sharpe (rf=0) | 0.1761 |
| Downside deviation (rf=0, %) | 40.6673 |
| Sortino (rf=0) | 0.2518 |
| Historical VaR 95% (1D, %) | 6.0443 |
| Historical ES 95% (1D, %) | 7.8139 |
| Correlation vs SPY | 0.3852 |
| Tracking error vs SPY (%) | 55.0179 |
| P/E (trailing) | 99.86 |
| P/B | 15.28 |
| EV/EBITDA | 103.47 |
| Revenue growth (%) | 31.60 |
| Forward P/E (estimate) | 61.89 |
| Gross margin (%) | 47.49 |
| Operating margin (%) | 18.39 |
| Return on equity (%) | 16.83 |
| Free cash flow yield (%) | N/A |
| MA50 | 213.6960 |
| Close vs MA50 (%) | -0.4614 |
| MA200 | 180.1618 |
| Close vs MA200 (%) | 18.0661 |
| RSI (14, Wilder) | 42.8461 |
| MACD (12,26) | -0.1949 |
| MACD signal (9) | 5.0739 |
| MACD histogram | -5.2687 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SHOP.TO': 274, 'SPY': 275}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 212.7100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 6.2541 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -9.6658 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -1.4593 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -3.7511 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -6.3900 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 58.1584 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 40.6673 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.2518 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 6.0443 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 7.8139 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3852 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 55.0179 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.7533 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -44.0932 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1761 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 61.8898 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 47.4910 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 18.3860 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 16.8330 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 99.8638 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 42.8461 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -5.2687 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -0.4614 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 18.0661 -> Clearly above the moving-average trend level.

## TAILWINDS

### Shopify Inc. (SHOP) Surges 30% as Revenue Climbs 34%, Bristol Gate Highlights Market Concentration
- Summary: Shopify Inc. (SHOP) Surges 30% as Revenue Climbs 34%, Bristol Gate Highlights Market Concentration
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNaTdtamJnQm1zVnhnanF0alZ4Uk9FYVg3RHpmVHJkOExobnMzb08xMDlxcG8tRGlYSmo5SW1ZQWc0YVdmZlFTbVhSOExBbjZESlBlRTQ0MlY5Q0RpTGJSSlpzNUN3Znk0Wlg2MjlCQ0g5aFppdi1zUDdkbFF3cWRQN2pyYlFPMFJzdkwxRzl6MWFBSU9UN2c?oc=5>

## HEADWINDS

### Shopify stock tanks as Q3 revenue, total order value miss Wall Street estimates
- Summary: Shopify stock tanks as Q3 revenue, total order value miss Wall Street estimates
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxQemxuQTVWUVY2NzFzOXhwRWdEV2pXdnVXUGtHYjZxYmVhOVJCMWF6cnZYelpPSVlXT1d4LTN5aHBrZGZTWTlLaHpZVkZ1elhHLThaaFN6Umc1SFRZS2dibmxBbVVnV1hJYUhwZkNtY1hjSG9KeFU1c051Q2xfQmdyN0h6UFdFYXh6aEpscEIzdlVfY2hLRXlONDNpc1V4M3hZWHM3bXpYM18tRU9rdWVHTVlyMG8waTgtb3BYS3FoNmstUklMUmFTcTF3bmo0SzNIeWtyZzNPaw?oc=5>

## CATALYSTS

### Shopify Dives As Q3 Gross Operating Profit, Revenue Miss
- Summary: Shopify Dives As Q3 Gross Operating Profit, Revenue Miss
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQZmYwV2Q5TEY5Q2FqcUxoVTJhR09CMUJtMll2N2R0OU1ic1NTcUhZbmNSZTZaQmViOWtUSmUzMzhHMEo5YWF0TDBRWGh0V2FRSGpIUVJwbjJsbnA2R2t2bFh1VGJscTJ4LTA5aHRVMmljc083TnpLWWxMQTZ1SlVUa1l6MlJyaTE0cEwwTzFNSDE3Q2hB?oc=5>

### Shopify Stock (SHOP) Plunges Premarket Despite 32% Revenue Growth – Here’s Why
- Summary: Shopify Stock (SHOP) Plunges Premarket Despite 32% Revenue Growth – Here’s Why
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxOTFF4Zy1sN3lqTldJUlZQamhZcVNMWTY1QlVEUEpBUzFNQ0VTRXR4R0NIM2ZkcXZSQmU1eEdHVjhpVkhzUk5zbmVtc2YyZ1RrcjdUNXJWYjB2RG1mTTN5QjlnUDRxMUViYndMZXREY2VZWl8tVnFpRmo3bUV5cUtzSXFrYkROemNGMlpicmFhYkQ1WVRSRXVEdzYydHphTXBkLTZhQg?oc=5>

### Shopify (SHOP) to report earnings tomorrow: here is what to expect
- Summary: Shopify (SHOP) to report earnings tomorrow: here is what to expect
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNdENoRHFmZEtZZFlGM0VYUDZyNmdOM1l0VTEtanFBTHNjNll5eG41ajZvNWxXam9xX2RqZWpINE95VlZmVktMdm5NSF9KWG8zOFU0R1JBMnd6cGZhdWVhRDc1N0g1cnRvY3A2RE9MY09jQUozQzJBUWgzUDFwcHk5TWU1RGI4WmdIa3V1VFVyYy00aGhLUk92Tl81R3dma21JbjhVTg?oc=5>

### Shopify Shows Strong FCF Results - Investors Bullish on SHOP With Unusual Call Option Activity
- Summary: Shopify reports robust free cash flow, boosting investor sentiment and option activity.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPWVhTd241QlZlSnpzNWRfQ0ZSQWhlSUFWTFZtYkotTHJUajhrOEJKWElMdW1NSkxHdnZ5aTI0VzlpYlJhNzdlOHVZRld0Yi1DWjExLWxtRFYwcm92Y3JmaDhhd3g1cDlQWnI3dEhGTG9LaTctUzc5M2tjS3MxYS12VGJuOF9LS2ZKa2FGdFoweTRtekYyamNobE5iMGp0UTA?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SHOP.TO** | **99.86** | **15.28** | **103.47** | **31.60** | **273,656,102,912.00 CAD** | **-6.39** |
| WIX | N/A | -1.99 | -30.70 | 14.90 | 3,369,722,624.00 USD | -42.10 |
| CRM | 20.33 | 4.87 | 16.89 | 10.80 | 186,911,522,816.00 USD | -9.98 |
| GDDY | 15.61 | -104.25 | 11.94 | 6.00 | 14,984,955,904.00 USD | -12.47 |

Peers fetched as_of: 2026-11-04; SHOP.TO reuses existing data (market data as_of: 2026-11-04); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-03
- Next expected earnings: 2027-02-10 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-04

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMilgFBVV95cUxNaTdtamJnQm1zVnhnanF0alZ4Uk9FYVg3RHpmVHJkOExobnMzb08xMDlxcG8tRGlYSmo5SW1ZQWc0YVdmZlFTbVhSOExBbjZESlBlRTQ0MlY5Q0RpTGJSSlpzNUN3Znk0Wlg2MjlCQ0g5aFppdi1zUDdkbFF3cWRQN2pyYlFPMFJzdkwxRzl6MWFBSU9UN2c?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxQemxuQTVWUVY2NzFzOXhwRWdEV2pXdnVXUGtHYjZxYmVhOVJCMWF6cnZYelpPSVlXT1d4LTN5aHBrZGZTWTlLaHpZVkZ1elhHLThaaFN6Umc1SFRZS2dibmxBbVVnV1hJYUhwZkNtY1hjSG9KeFU1c051Q2xfQmdyN0h6UFdFYXh6aEpscEIzdlVfY2hLRXlONDNpc1V4M3hZWHM3bXpYM18tRU9rdWVHTVlyMG8waTgtb3BYS3FoNmstUklMUmFTcTF3bmo0SzNIeWtyZzNPaw?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQZmYwV2Q5TEY5Q2FqcUxoVTJhR09CMUJtMll2N2R0OU1ic1NTcUhZbmNSZTZaQmViOWtUSmUzMzhHMEo5YWF0TDBRWGh0V2FRSGpIUVJwbjJsbnA2R2t2bFh1VGJscTJ4LTA5aHRVMmljc083TnpLWWxMQTZ1SlVUa1l6MlJyaTE0cEwwTzFNSDE3Q2hB?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxOTFF4Zy1sN3lqTldJUlZQamhZcVNMWTY1QlVEUEpBUzFNQ0VTRXR4R0NIM2ZkcXZSQmU1eEdHVjhpVkhzUk5zbmVtc2YyZ1RrcjdUNXJWYjB2RG1mTTN5QjlnUDRxMUViYndMZXREY2VZWl8tVnFpRmo3bUV5cUtzSXFrYkROemNGMlpicmFhYkQ1WVRSRXVEdzYydHphTXBkLTZhQg?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNdENoRHFmZEtZZFlGM0VYUDZyNmdOM1l0VTEtanFBTHNjNll5eG41ajZvNWxXam9xX2RqZWpINE95VlZmVktMdm5NSF9KWG8zOFU0R1JBMnd6cGZhdWVhRDc1N0g1cnRvY3A2RE9MY09jQUozQzJBUWgzUDFwcHk5TWU1RGI4WmdIa3V1VFVyYy00aGhLUk92Tl81R3dma21JbjhVTg?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPWVhTd241QlZlSnpzNWRfQ0ZSQWhlSUFWTFZtYkotTHJUajhrOEJKWElMdW1NSkxHdnZ5aTI0VzlpYlJhNzdlOHVZRld0Yi1DWjExLWxtRFYwcm92Y3JmaDhhd3g1cDlQWnI3dEhGTG9LaTctUzc5M2tjS3MxYS12VGJuOF9LS2ZKa2FGdFoweTRtekYyamNobE5iMGp0UTA?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
