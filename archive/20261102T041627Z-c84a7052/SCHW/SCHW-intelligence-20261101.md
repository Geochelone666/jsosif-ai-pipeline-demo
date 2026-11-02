# SCHW Intelligence Report

- ticker: **SCHW**
- Report as_of: **2026-11-01**
- Market data as_of: **2026-10-30**
- Quant sources: https://finance.yahoo.com/quote/SCHW/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SCHW/key-statistics/
- AI analysis snapshot as_of: **2026-11-01**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-02T04:29:34.611609+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 11, 'rule': 0, 'ai': 8, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261101T014405Z-e49d1192/SCHW** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 11 unique headlines; 4 named publishers; 0 exact duplicates; 11 HTTPS source links; largest publisher share 54.55%; oldest publication 2026-10-29

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

### Charles Schwab (SCHW) Stock Could Be A Bargain Based On Returns
- Summary: Positive analyst view that Schwab stock may be undervalued based on returns.
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxObTFUOFN4cmpuSll5aHAtTm1ZRDU4TUEzRGYtTXBvb1VFQ3YwS1FqUVhZOUp5VEdTbnNLU3lFNVBScm9GZFNRYWp2R1gyVm5HRFNVOVllRjRMUTZrNkZVeUtFQVI3a05pb2dNR1MzanJhNmZIcU16aE8tNUprT3lxWVcyWEhnNktjcEZHSXVOT255WUhqNV9pd3RnRm0?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Charles Schwab (SCHW) Expands AI Tools For RIAs, Is The Stock Still 25% Undervalued?
- Summary: Schwab expands AI tools for RIAs, signaling product enhancement.
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPVmtZQzNUTUxSSDVBZVgwUURWUWREZ2ZNM0owNGdwWHlkYjVOdUZYWFhMQnlBZXVIZTBwQUlDOFc1Rmo1Q29wVWFRaXQtRGVoRV8tYUVCSjlnc3BpMU5Vb19QZERTNERMNEZTa1BtUE51X3JlZUhSOFJSUk9xU3ZLamNwSUZpWjREclIxLUFDc3Z1dGRSSUNsemI3aw?oc=5>

### 38,821 The Charles Schwab Corporation $SCHW Shares Purchased by Greenup Street Wealth Management LLC
- Summary: Greenup Street Wealth Management purchased 38,821 Schwab shares.
- Date: 2026-10-31 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi8AFBVV95cUxOUk5YUW0xTUFSQlpsZThkWkJnckdLQm5OZzZ0UzBveVB1SEtNeHBTRk1HRlVHZ0hZUU1McU0tU1ZLTW9PWjZfU0cyNUxzSjhHYUo1azBGRUVxRzVmSUQ3VnZjSFVzSFd3WHRTOE00ZGxXV0JZd2NGc3pwYks5QmgzbDFEbGVtdk5FU0ZHSVdYcm45dFp0TEhjYXItUXpMTUpUWG5pWExMVEE3SlR6Wm9jZ2YzeU9ad0c0SWtPajhFclpvQXJfNHAwTjNyZDlJZS1EVGFDMDU0MnBkWUZkRDRHaThvcjNqUU5LTUZ0M2I0MWg?oc=5>

### 22,249 The Charles Schwab Corporation $SCHW Shares Acquired by Birinyi Associates Inc.
- Summary: Birinyi Associates acquired 22,249 Schwab shares.
- Date: 2026-10-31 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3AFBVV95cUxNSllxd2FwRlJBMnlFY2ZINUFKVlItYllEdjk3R29GUzBCTm1pN3pUNDhXenZpQXV4OGpPeUtNdVVsZnVqVkpqbTEzM2V2S3Q4VXpBQlFQc0hna3VHQld1WjlmZjFIN1JLZGEwNVg0RW9hOGJZWWhWNEdxdEl6VzVqUFp2ZllyQjFvQnJkZDZ2cTFpQm92MVl1WVB4MUNtTlI4YTEzVmkyWkMzWVpKck5vZzhXYW9nTWFaM2MwWXdtMEwxbm14UEhzNkdkLXh6X2J1ZFRrMHB4cnNLdHpH?oc=5>

### Is Charles Schwab (SCHW) A Bargain Following Its AI Push?
- Summary: Questioning Schwab's valuation post AI initiatives, implying potential upside.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxNTlY3blVycWVPd1ZXejJFOEpuTEN2R2RBX0pSaTBlcWRTTjBGUndYYnQzRExoSVFLd0xlSXRST1E2S2Ztd3djaGxPUnVVUHZuNHdjeVVuNXk3WUZZMVByWUI0QUFNb0ZXTE83Mlc4dmhwRzRKOUtuZm9odW1RY1AzVHN2UkpsVnZpbjdBVUNXSlloLWM2VlgtOGRtYjRWbHFrTUpWYU1jVkN6dEJvWFBkN1lBTzVtbFpacE1yNFhjOWxoV2ZLSW5ydnEwa05PZExxYVE2d0130gHbAUFVX3lxTE9icGY0T3dNTFBOYktWNzdsUkNjdUhDeHgzZWp2ZkVFZGViRVRubHJZRkoxR1FFMG14dW4xWkZyZnU0QWlSWUhRWkkyb3hWQTgtaFNsVFFSaHItOFdpWE82MktJaGZPRkdoX1JDaVpOLTcwcndpWmNqRzhwUXd4RG5iLTNIZmhrNlk0S0VfanNONy1Ld0wwOUlfaS1XbmFxaDRfLVg4Z01LcExPcnVEQ0ZvZVhFc2FNRVNFQzJxR21sUnViZzBsVTlvWHBsbGdRZEFfU25reWhaWWlQZw?oc=5>

### The Charles Schwab Corporation $SCHW Shares Sold by Smith Group Asset Management LLC
- Summary: Smith Group Asset Management sold Schwab shares, reflecting a share sale activity.
- Date: 2026-10-29 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3AFBVV95cUxQNkNXcThVUmQwUy1zZFVzeDRESzNubWZ1R0k4bmFKTHdoa2tQRkVwYXJPYlBZSVRWR0REdHFyWXFPb2pYOEhWSlVEZ0RKcHF5YlM0VUtGdWZ1ZmZvbXJNejZpWWJIRkw1ZTRMNjNQYXlzRlljdy11bllKQ1dEd2h4QXFHY2l5RWtNS1h2OENJaDFwc0x3UkdlMmc0RjVxN1pMVUJ6aWV2NVNWLXJjRmVBenhpS0ZjRkxlWDVwbzNsbDBrYVhPZFB6TVo2RlFMTmZ4NC1tYXFKS29VaF95?oc=5>

### Did AI Rollout Just Shift Charles Schwab's (SCHW) Investment Narrative?
- Summary: AI rollout may alter Schwab's investment strategy, signaling potential product changes.
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMi3gFBVV95cUxQTzRuekx3WGpWNmFybjE2LURfcGRoUG1TVDFMX3VrSmk0cVh3M3NBVEdhSXFVNktRT2szNFYtY291alJMdzlRZjJzczdaLW1IZjFqUmxZLVA1QjhOajA5aXBKLUxmVktwM2VpSUdhMG9rbTQ1NG53SjRBNFNPV3pLMGZqTFpTZk44dWpMeVA3RzFGM0xkZ3F6dEd5dTlpSzVYdXVDbGM0YlZkQ05OUTVzZ1FJUGNGemdvb3o3dzhRRjZla1k3ckJESXZvYnA0WFMwdFpZZXE0X09URHI3OEHSAeMBQVVfeXFMT3RlVlpya0hJUWJzdE45dzFSMmdTaFBfYVFYWlpCU01CbzhwdkFxTHdER05YNHh5NXFlRlN2QkVwSl8tOEY4a0VTNkY4dHZ2YzNJQjctamZwS2Y0WUhJSnlnZXZ0ejNTWXhxQ3MxMFlCcldUdUZNckxaSmdPUHFHUUFWTV93VHdfeDVEY1F6WXZ5bFQyTUlobUhjZTlaaDVacDhOV24wTWFxaDBWa3VvbFo3bXU0RGJqX2FyX2pvdU1GSTNETTFvM1hPWm1tTzAxVTA1QWpSUzFyOFFhNlNfbEdmYTg?oc=5>

### Charles Schwab (SCHW) CEO Says Retail Investors Should Have Greater Access to IPOs
- Summary: CEO promotes broader IPO access for retail investors, indicating strategic guidance.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxPX1hrWVJjVW8zYXhqTkRjdm44WTlka0dsTElaMmdibXpUZlRkdE8xcHZPdDY4b0Mwb1BYN1pOZ1NSeVB0Rm5zYllRdTRfZThVTmZ6ZFpPeno3MlpJeVhELW1DSW5TUmowVlg0N0dBMHQ0cE45TTl5V3diMFotVzNSY2x2NWl3RUswNVdZcUNfMHNmQUFDeHJpN0tBWUMxdHFuSTVlZ1VYV2M?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SCHW** | **15.05** | **2.96** | **N/A** | **16.90** | **152,268,013,568.00 USD** | **-5.54** |
| IBKR | 29.35 | 5.60 | N/A | 13.50 | 131,023,421,440.00 USD | 12.72 |
| HOOD | 39.17 | 7.66 | N/A | 11.80 | 76,532,752,384.00 USD | -38.44 |
| LPLA | 16.26 | 3.82 | N/A | 17.80 | 22,094,383,104.00 USD | -15.87 |

Peers fetched as_of: 2026-11-01; SCHW reuses existing data (market data as_of: 2026-10-30); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-21 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-01

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

- https://news.google.com/rss/articles/CBMinAFBVV95cUxObTFUOFN4cmpuSll5aHAtTm1ZRDU4TUEzRGYtTXBvb1VFQ3YwS1FqUVhZOUp5VEdTbnNLU3lFNVBScm9GZFNRYWp2R1gyVm5HRFNVOVllRjRMUTZrNkZVeUtFQVI3a05pb2dNR1MzanJhNmZIcU16aE8tNUprT3lxWVcyWEhnNktjcEZHSXVOT255WUhqNV9pd3RnRm0?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPVmtZQzNUTUxSSDVBZVgwUURWUWREZ2ZNM0owNGdwWHlkYjVOdUZYWFhMQnlBZXVIZTBwQUlDOFc1Rmo1Q29wVWFRaXQtRGVoRV8tYUVCSjlnc3BpMU5Vb19QZERTNERMNEZTa1BtUE51X3JlZUhSOFJSUk9xU3ZLamNwSUZpWjREclIxLUFDc3Z1dGRSSUNsemI3aw?oc=5
- https://news.google.com/rss/articles/CBMi8AFBVV95cUxOUk5YUW0xTUFSQlpsZThkWkJnckdLQm5OZzZ0UzBveVB1SEtNeHBTRk1HRlVHZ0hZUU1McU0tU1ZLTW9PWjZfU0cyNUxzSjhHYUo1azBGRUVxRzVmSUQ3VnZjSFVzSFd3WHRTOE00ZGxXV0JZd2NGc3pwYks5QmgzbDFEbGVtdk5FU0ZHSVdYcm45dFp0TEhjYXItUXpMTUpUWG5pWExMVEE3SlR6Wm9jZ2YzeU9ad0c0SWtPajhFclpvQXJfNHAwTjNyZDlJZS1EVGFDMDU0MnBkWUZkRDRHaThvcjNqUU5LTUZ0M2I0MWg?oc=5
- https://news.google.com/rss/articles/CBMi3AFBVV95cUxNSllxd2FwRlJBMnlFY2ZINUFKVlItYllEdjk3R29GUzBCTm1pN3pUNDhXenZpQXV4OGpPeUtNdVVsZnVqVkpqbTEzM2V2S3Q4VXpBQlFQc0hna3VHQld1WjlmZjFIN1JLZGEwNVg0RW9hOGJZWWhWNEdxdEl6VzVqUFp2ZllyQjFvQnJkZDZ2cTFpQm92MVl1WVB4MUNtTlI4YTEzVmkyWkMzWVpKck5vZzhXYW9nTWFaM2MwWXdtMEwxbm14UEhzNkdkLXh6X2J1ZFRrMHB4cnNLdHpH?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxNTlY3blVycWVPd1ZXejJFOEpuTEN2R2RBX0pSaTBlcWRTTjBGUndYYnQzRExoSVFLd0xlSXRST1E2S2Ztd3djaGxPUnVVUHZuNHdjeVVuNXk3WUZZMVByWUI0QUFNb0ZXTE83Mlc4dmhwRzRKOUtuZm9odW1RY1AzVHN2UkpsVnZpbjdBVUNXSlloLWM2VlgtOGRtYjRWbHFrTUpWYU1jVkN6dEJvWFBkN1lBTzVtbFpacE1yNFhjOWxoV2ZLSW5ydnEwa05PZExxYVE2d0130gHbAUFVX3lxTE9icGY0T3dNTFBOYktWNzdsUkNjdUhDeHgzZWp2ZkVFZGViRVRubHJZRkoxR1FFMG14dW4xWkZyZnU0QWlSWUhRWkkyb3hWQTgtaFNsVFFSaHItOFdpWE82MktJaGZPRkdoX1JDaVpOLTcwcndpWmNqRzhwUXd4RG5iLTNIZmhrNlk0S0VfanNONy1Ld0wwOUlfaS1XbmFxaDRfLVg4Z01LcExPcnVEQ0ZvZVhFc2FNRVNFQzJxR21sUnViZzBsVTlvWHBsbGdRZEFfU25reWhaWWlQZw?oc=5
- https://news.google.com/rss/articles/CBMi3AFBVV95cUxQNkNXcThVUmQwUy1zZFVzeDRESzNubWZ1R0k4bmFKTHdoa2tQRkVwYXJPYlBZSVRWR0REdHFyWXFPb2pYOEhWSlVEZ0RKcHF5YlM0VUtGdWZ1ZmZvbXJNejZpWWJIRkw1ZTRMNjNQYXlzRlljdy11bllKQ1dEd2h4QXFHY2l5RWtNS1h2OENJaDFwc0x3UkdlMmc0RjVxN1pMVUJ6aWV2NVNWLXJjRmVBenhpS0ZjRkxlWDVwbzNsbDBrYVhPZFB6TVo2RlFMTmZ4NC1tYXFKS29VaF95?oc=5
- https://news.google.com/rss/articles/CBMi3gFBVV95cUxQTzRuekx3WGpWNmFybjE2LURfcGRoUG1TVDFMX3VrSmk0cVh3M3NBVEdhSXFVNktRT2szNFYtY291alJMdzlRZjJzczdaLW1IZjFqUmxZLVA1QjhOajA5aXBKLUxmVktwM2VpSUdhMG9rbTQ1NG53SjRBNFNPV3pLMGZqTFpTZk44dWpMeVA3RzFGM0xkZ3F6dEd5dTlpSzVYdXVDbGM0YlZkQ05OUTVzZ1FJUGNGemdvb3o3dzhRRjZla1k3ckJESXZvYnA0WFMwdFpZZXE0X09URHI3OEHSAeMBQVVfeXFMT3RlVlpya0hJUWJzdE45dzFSMmdTaFBfYVFYWlpCU01CbzhwdkFxTHdER05YNHh5NXFlRlN2QkVwSl8tOEY4a0VTNkY4dHZ2YzNJQjctamZwS2Y0WUhJSnlnZXZ0ejNTWXhxQ3MxMFlCcldUdUZNckxaSmdPUHFHUUFWTV93VHdfeDVEY1F6WXZ5bFQyTUlobUhjZTlaaDVacDhOV24wTWFxaDBWa3VvbFo3bXU0RGJqX2FyX2pvdU1GSTNETTFvM1hPWm1tTzAxVTA1QWpSUzFyOFFhNlNfbEdmYTg?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxPX1hrWVJjVW8zYXhqTkRjdm44WTlka0dsTElaMmdibXpUZlRkdE8xcHZPdDY4b0Mwb1BYN1pOZ1NSeVB0Rm5zYllRdTRfZThVTmZ6ZFpPeno3MlpJeVhELW1DSW5TUmowVlg0N0dBMHQ0cE45TTl5V3diMFotVzNSY2x2NWl3RUswNVdZcUNfMHNmQUFDeHJpN0tBWUMxdHFuSTVlZ1VYV2M?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
