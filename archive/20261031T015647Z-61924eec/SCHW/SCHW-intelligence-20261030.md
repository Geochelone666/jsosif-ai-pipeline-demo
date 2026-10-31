# SCHW Intelligence Report

- ticker: **SCHW**
- Report as_of: **2026-10-30**
- Market data as_of: **2026-10-30**
- Quant sources: https://finance.yahoo.com/quote/SCHW/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SCHW/key-statistics/
- AI analysis snapshot as_of: **2026-10-30**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-31T02:03:19.357970+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 11, 'rule': 0, 'ai': 8, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261030T021807Z-b9de7146/SCHW** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 11 unique headlines; 8 named publishers; 0 exact duplicates; 11 HTTPS source links; largest publisher share 36.36%; oldest publication 2026-10-23

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 88.0500 |
| Return 1D (%) | -1.5871 |
| Return 1W (%) | -2.7931 |
| Return 1M (%) | -9.9141 |
| Return YTD (%) | -10.9970 |
| Return 1Y (%) | -5.5445 |
| Annualized volatility (%) | 25.4995 |
| Beta vs SPY | 0.4294 |
| Max drawdown (%) | -22.5253 |
| Sharpe (rf=0) | -0.0961 |
| Downside deviation (rf=0, %) | 19.7157 |
| Sortino (rf=0) | -0.1243 |
| Historical VaR 95% (1D, %) | 2.5523 |
| Historical ES 95% (1D, %) | 3.9505 |
| Correlation vs SPY | 0.2153 |
| Tracking error vs SPY (%) | 25.9486 |
| P/E (trailing) | 15.05 |
| P/B | 2.96 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 16.90 |
| Forward P/E (estimate) | 11.28 |
| Gross margin (%) | 97.51 |
| Operating margin (%) | 52.67 |
| Return on equity (%) | 21.12 |
| Free cash flow yield (%) | N/A |
| MA50 | 100.4938 |
| Close vs MA50 (%) | -12.3827 |
| MA200 | 97.1914 |
| Close vs MA200 (%) | -9.4056 |
| RSI (14, Wilder) | 27.7255 |
| MACD (12,26) | -3.2521 |
| MACD signal (9) | -3.1683 |
| MACD histogram | -0.0838 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SCHW': 272, 'SPY': 272}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 88.0500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.5871 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.7931 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -9.9141 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -10.9970 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -5.5445 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 25.4995 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 19.7157 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.1243 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.5523 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.9505 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2153 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 25.9486 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.4294 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -22.5253 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.0961 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 11.2839 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 97.5060 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 52.6700 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 21.1220 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 15.0513 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 27.7255 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.0838 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -12.3827 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -9.4056 -> Clearly below the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Schwab: It's Time To Evaluate The Preferreds And Common (NYSE:SCHW)
- Summary: Schwab signals review of preferred and common shares, indicating potential restructuring or strategic shift.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQd2Nob3RYc01EOWxkUEpRTGlUdjZQb2NUZ2QzbXhuTWk0ZmExNTU1Z0JDZmo5SGVXUXdCNGF0b1BvLUhwZ1VwclV5R1d4NUo5WjVjbndRQ3M3YXA0NWxvVUpLb2d0dHkzSUN5ZjlaVGFyV1hmaUlQMTJ2OWlsRUlPdmRoNDNGRzRmZnp0YjBEc3AyNGtjRVFjbEZR?oc=5>

### Evercore ISI Adjusts Price Target on Charles Schwab to $98 From $104
- Summary: Evercore ISI lowered Schwab's price target, suggesting a more cautious outlook.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOSGVRRTNqWXJtU3ZQeDJPTjQ4dVg3S3JybTdzaEJBYnNqMS1jWk8zWUp1dURkMUFtYXNaUV8wX2RXZ3M3WVlzU1ZSem81MG5KUHlqRHllNXZaOWl3TlVZaHpUYjhNNjM3eUZPQUV5WVlUc05GS0lVNUQtcm90QWRmMlFSbmNQNDBwRXpUR196c0p5Y3hvSE9PTkVKVWs1N00?oc=5>

### A trust sold Charles Schwab (SCHW) shares in two trades tied to its co-chairman's indirect holdings.
- Summary: Trust sold Schwab shares linked to co-chairman's holdings, indicating a share sale event.
- Date: 2026-10-29 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxQeExCUHpDT1VxU3F6OEthSzF5RXd3dk9aa1Nidmk4SUwzVThhcFVUNkNONzJWUWRuNFY2cXpDS1pHeVZ1bWhTOWtUMUV4c1pIWmVTbVZOSTBrdU14OTd1cUh3Tk82UU9RR3BsNTU1LUNYbFlXcHpQemVPLUNFbTlhX0lJaWJBMzFrQ0hxRmJ5V3VDYkJvVkhjYW1ERDdfeGhDcWlwTERocGYtdGlZZ3BydzcwRQ?oc=5>

### Is Charles Schwab (SCHW) A Bargain Following Its AI Push?
- Summary: Questioning Schwab's valuation post AI initiatives, implying potential upside.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxNTlY3blVycWVPd1ZXejJFOEpuTEN2R2RBX0pSaTBlcWRTTjBGUndYYnQzRExoSVFLd0xlSXRST1E2S2Ztd3djaGxPUnVVUHZuNHdjeVVuNXk3WUZZMVByWUI0QUFNb0ZXTE83Mlc4dmhwRzRKOUtuZm9odW1RY1AzVHN2UkpsVnZpbjdBVUNXSlloLWM2VlgtOGRtYjRWbHFrTUpWYU1jVkN6dEJvWFBkN1lBTzVtbFpacE1yNFhjOWxoV2ZLSW5ydnEwa05PZExxYVE2d0130gHbAUFVX3lxTE9icGY0T3dNTFBOYktWNzdsUkNjdUhDeHgzZWp2ZkVFZGViRVRubHJZRkoxR1FFMG14dW4xWkZyZnU0QWlSWUhRWkkyb3hWQTgtaFNsVFFSaHItOFdpWE82MktJaGZPRkdoX1JDaVpOLTcwcndpWmNqRzhwUXd4RG5iLTNIZmhrNlk0S0VfanNONy1Ld0wwOUlfaS1XbmFxaDRfLVg4Z01LcExPcnVEQ0ZvZVhFc2FNRVNFQzJxR21sUnViZzBsVTlvWHBsbGdRZEFfU25reWhaWWlQZw?oc=5>

### The Charles Schwab Corporation $SCHW Shares Sold by Smith Group Asset Management LLC
- Summary: Smith Group Asset Management sold Schwab shares, reflecting a share sale activity.
- Date: 2026-10-29 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3AFBVV95cUxQNkNXcThVUmQwUy1zZFVzeDRESzNubWZ1R0k4bmFKTHdoa2tQRkVwYXJPYlBZSVRWR0REdHFyWXFPb2pYOEhWSlVEZ0RKcHF5YlM0VUtGdWZ1ZmZvbXJNejZpWWJIRkw1ZTRMNjNQYXlzRlljdy11bllKQ1dEd2h4QXFHY2l5RWtNS1h2OENJaDFwc0x3UkdlMmc0RjVxN1pMVUJ6aWV2NVNWLXJjRmVBenhpS0ZjRkxlWDVwbzNsbDBrYVhPZFB6TVo2RlFMTmZ4NC1tYXFKS29VaF95?oc=5>

### The Charles Schwab Corporation $SCHW Shares Bought by Sowell Financial Services LLC
- Summary: Shares of SCHW purchased by Sowell Financial Services LLC.
- Date: 2026-10-23 | Impact: low | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMi2wFBVV95cUxOdkJmdEt3RGRsZFJWSUF3TG53Y0lTRHBuQ2FRWHpvdU9lc0s4TXVDLTZ2azRjazFGRHdOQUZQaTZCN2ZpZ0lJczRoZHpCcEdWbmVhOWVPUnpJRTRzZTVCVldPRlMtY2toSHhGanJLMjlKVUtiaFdSNnFLLWZWQy1kOG1YM0ZHTmZOcUc2VzNqaklWWWRJb3RoN1ZaT3NBN0JZamYyNDhJbkFXSGpzalpaRk9uaVRzY1BsbEdNYVR6eE5zN2lUWHZ4SlFXQ09UZXFwYUJWekQxWTJJVk0?oc=5>

### 20,480 Shares of The Charles Schwab Corporation $SCHW Bought by NBT Bank N.A.
- Summary: NBT Bank N.A. bought 20,480 SCHW shares.
- Date: 2026-10-23 | Impact: low | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxNelpseS13a2VnYWN4NDZLYnJ0eEUwYVlETXN2NFhPbndDUlVmSm9IVTNnS21zSUVCektQUl9jR2RrQkhUck9qZl84VmVtQ1ZGcjNxdWVaM3JuMXNSWjVMNEFfbnRuMzhuNE5PMlVNNkh5VVFJa3ZOVElRZTJpRG5BZDFDdGw3cS04SjZsVWk3QzlneExFZmJURmZTdy1NYTVkWi1XWVlFbjhMVjJwOTFwZk5UdUtGMEdpSkgtWHd5ZnBlQ21IMFFiX2xFbmdybmc?oc=5>

### Charles Schwab (SCHW) CEO Says Retail Investors Should Have Greater Access to IPOs
- Summary: CEO announces plans to broaden IPO access for retail investors, potentially boosting Schwab’s product offerings and client engagement.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxPX1hrWVJjVW8zYXhqTkRjdm44WTlka0dsTElaMmdibXpUZlRkdE8xcHZPdDY4b0Mwb1BYN1pOZ1NSeVB0Rm5zYllRdTRfZThVTmZ6ZFpPeno3MlpJeVhELW1DSW5TUmowVlg0N0dBMHQ0cE45TTl5V3diMFotVzNSY2x2NWl3RUswNVdZcUNfMHNmQUFDeHJpN0tBWUMxdHFuSTVlZ1VYV2M?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SCHW** | **15.05** | **2.96** | **N/A** | **16.90** | **152,268,013,568.00 USD** | **-5.54** |
| IBKR | 29.35 | 5.60 | N/A | 13.50 | 131,023,421,440.00 USD | 12.72 |
| HOOD | 39.17 | 7.66 | N/A | 11.80 | 76,532,752,384.00 USD | -38.44 |
| LPLA | 16.26 | 3.82 | N/A | 17.80 | 22,219,880,448.00 USD | -15.87 |

Peers fetched as_of: 2026-10-30; SCHW reuses existing data (market data as_of: 2026-10-30); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-21 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-30

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-07
- Revenue (latest available single quarter): 7,072,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): 2,800,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/316709/000031670926000031/schw-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimgFBVV95cUxQd2Nob3RYc01EOWxkUEpRTGlUdjZQb2NUZ2QzbXhuTWk0ZmExNTU1Z0JDZmo5SGVXUXdCNGF0b1BvLUhwZ1VwclV5R1d4NUo5WjVjbndRQ3M3YXA0NWxvVUpLb2d0dHkzSUN5ZjlaVGFyV1hmaUlQMTJ2OWlsRUlPdmRoNDNGRzRmZnp0YjBEc3AyNGtjRVFjbEZR?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOSGVRRTNqWXJtU3ZQeDJPTjQ4dVg3S3JybTdzaEJBYnNqMS1jWk8zWUp1dURkMUFtYXNaUV8wX2RXZ3M3WVlzU1ZSem81MG5KUHlqRHllNXZaOWl3TlVZaHpUYjhNNjM3eUZPQUV5WVlUc05GS0lVNUQtcm90QWRmMlFSbmNQNDBwRXpUR196c0p5Y3hvSE9PTkVKVWs1N00?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxQeExCUHpDT1VxU3F6OEthSzF5RXd3dk9aa1Nidmk4SUwzVThhcFVUNkNONzJWUWRuNFY2cXpDS1pHeVZ1bWhTOWtUMUV4c1pIWmVTbVZOSTBrdU14OTd1cUh3Tk82UU9RR3BsNTU1LUNYbFlXcHpQemVPLUNFbTlhX0lJaWJBMzFrQ0hxRmJ5V3VDYkJvVkhjYW1ERDdfeGhDcWlwTERocGYtdGlZZ3BydzcwRQ?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxNTlY3blVycWVPd1ZXejJFOEpuTEN2R2RBX0pSaTBlcWRTTjBGUndYYnQzRExoSVFLd0xlSXRST1E2S2Ztd3djaGxPUnVVUHZuNHdjeVVuNXk3WUZZMVByWUI0QUFNb0ZXTE83Mlc4dmhwRzRKOUtuZm9odW1RY1AzVHN2UkpsVnZpbjdBVUNXSlloLWM2VlgtOGRtYjRWbHFrTUpWYU1jVkN6dEJvWFBkN1lBTzVtbFpacE1yNFhjOWxoV2ZLSW5ydnEwa05PZExxYVE2d0130gHbAUFVX3lxTE9icGY0T3dNTFBOYktWNzdsUkNjdUhDeHgzZWp2ZkVFZGViRVRubHJZRkoxR1FFMG14dW4xWkZyZnU0QWlSWUhRWkkyb3hWQTgtaFNsVFFSaHItOFdpWE82MktJaGZPRkdoX1JDaVpOLTcwcndpWmNqRzhwUXd4RG5iLTNIZmhrNlk0S0VfanNONy1Ld0wwOUlfaS1XbmFxaDRfLVg4Z01LcExPcnVEQ0ZvZVhFc2FNRVNFQzJxR21sUnViZzBsVTlvWHBsbGdRZEFfU25reWhaWWlQZw?oc=5
- https://news.google.com/rss/articles/CBMi3AFBVV95cUxQNkNXcThVUmQwUy1zZFVzeDRESzNubWZ1R0k4bmFKTHdoa2tQRkVwYXJPYlBZSVRWR0REdHFyWXFPb2pYOEhWSlVEZ0RKcHF5YlM0VUtGdWZ1ZmZvbXJNejZpWWJIRkw1ZTRMNjNQYXlzRlljdy11bllKQ1dEd2h4QXFHY2l5RWtNS1h2OENJaDFwc0x3UkdlMmc0RjVxN1pMVUJ6aWV2NVNWLXJjRmVBenhpS0ZjRkxlWDVwbzNsbDBrYVhPZFB6TVo2RlFMTmZ4NC1tYXFKS29VaF95?oc=5
- https://news.google.com/rss/articles/CBMi2wFBVV95cUxOdkJmdEt3RGRsZFJWSUF3TG53Y0lTRHBuQ2FRWHpvdU9lc0s4TXVDLTZ2azRjazFGRHdOQUZQaTZCN2ZpZ0lJczRoZHpCcEdWbmVhOWVPUnpJRTRzZTVCVldPRlMtY2toSHhGanJLMjlKVUtiaFdSNnFLLWZWQy1kOG1YM0ZHTmZOcUc2VzNqaklWWWRJb3RoN1ZaT3NBN0JZamYyNDhJbkFXSGpzalpaRk9uaVRzY1BsbEdNYVR6eE5zN2lUWHZ4SlFXQ09UZXFwYUJWekQxWTJJVk0?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxNelpseS13a2VnYWN4NDZLYnJ0eEUwYVlETXN2NFhPbndDUlVmSm9IVTNnS21zSUVCektQUl9jR2RrQkhUck9qZl84VmVtQ1ZGcjNxdWVaM3JuMXNSWjVMNEFfbnRuMzhuNE5PMlVNNkh5VVFJa3ZOVElRZTJpRG5BZDFDdGw3cS04SjZsVWk3QzlneExFZmJURmZTdy1NYTVkWi1XWVlFbjhMVjJwOTFwZk5UdUtGMEdpSkgtWHd5ZnBlQ21IMFFiX2xFbmdybmc?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxPX1hrWVJjVW8zYXhqTkRjdm44WTlka0dsTElaMmdibXpUZlRkdE8xcHZPdDY4b0Mwb1BYN1pOZ1NSeVB0Rm5zYllRdTRfZThVTmZ6ZFpPeno3MlpJeVhELW1DSW5TUmowVlg0N0dBMHQ0cE45TTl5V3diMFotVzNSY2x2NWl3RUswNVdZcUNfMHNmQUFDeHJpN0tBWUMxdHFuSTVlZ1VYV2M?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
