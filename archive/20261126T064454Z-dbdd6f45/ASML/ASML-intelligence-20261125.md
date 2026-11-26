# ASML Intelligence Report

- ticker: **ASML**
- Report as_of: **2026-11-25**
- Market data as_of: **2026-11-25**
- Quant sources: https://finance.yahoo.com/quote/ASML/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ASML/key-statistics/
- AI analysis snapshot as_of: **2026-11-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-26T07:06:05.818261+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 5, 'ai': 9, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **11** exact headline/source/date matches; prior report **20261125T065354Z-0b3565c6/ASML** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'negative_sentiment_in_tailwinds': 1}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 12 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 21.74%; oldest publication 2026-11-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 1303.0800 |
| Return 1D (%) | -2.4685 |
| Return 1W (%) | -6.6073 |
| Return 1M (%) | -16.9870 |
| Return YTD (%) | 22.5457 |
| Return 1Y (%) | 30.6859 |
| Annualized volatility (%) | 50.1032 |
| Beta vs SPY | 2.2424 |
| Max drawdown (%) | -36.1866 |
| Sharpe (rf=0) | 0.7858 |
| Downside deviation (rf=0, %) | 33.9159 |
| Sortino (rf=0) | 1.1608 |
| Historical VaR 95% (1D, %) | 5.0034 |
| Historical ES 95% (1D, %) | 6.6569 |
| Correlation vs SPY | 0.6682 |
| Tracking error vs SPY (%) | 41.6356 |
| P/E (trailing) | 32.06 |
| P/B | 1118.89 |
| EV/EBITDA | 1713.31 |
| Revenue growth (%) | 55.20 |
| Forward P/E (estimate) | 20.55 |
| Gross margin (%) | 54.34 |
| Operating margin (%) | 38.55 |
| Return on equity (%) | 65.64 |
| Free cash flow yield (%) | N/A |
| MA50 | 1608.5563 |
| Close vs MA50 (%) | -18.9907 |
| MA200 | 1596.5158 |
| Close vs MA200 (%) | -18.3798 |
| RSI (14, Wilder) | 36.2526 |
| MACD (12,26) | -81.3646 |
| MACD signal (9) | -72.6784 |
| MACD histogram | -8.6862 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ASML': 290, 'SPY': 290}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 1303.0800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.4685 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -6.6073 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -16.9870 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 22.5457 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 30.6859 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 50.1032 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 33.9159 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.1608 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 5.0034 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.6569 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6682 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 41.6356 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.2424 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -36.1866 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.7858 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 20.5535 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.3370 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 38.5520 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 65.6360 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 32.0640 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 36.2526 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -8.6862 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -18.9907 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -18.3798 -> Clearly below the moving-average trend level.

## TAILWINDS

### ASML Stock 12‑Month Price Target Raised to $2,436.94, Implies 92% Upside
- Summary: ASML Stock 12‑Month Price Target Raised to $2,436.94, Implies 92% Upside
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxPRjFTdFR5c19TSXh2SERzMUZoSU9BVW5lTmwxaXMtSVVkdGh6SWN6V2QzSGFMa2tLbnJSZERBTkp3UDVEU0lnMWR0Zmx2NWV1Q1RpckRmWFpUMWsyaVhmZGttZF80aVZuck1Way0yamFPWGhlT1FTZ2lwQnBrTkExSm5pQ3JRYnd2bjhjZHQ3LS1WdGFmWmxIazZ6WnR0YjU2QkV0MDVjVzlrTGtidkd3N3hPd3pVSlZfNUJRSjdzWldSeWhjRFVOR0hyMA?oc=5>

### ASML Holding rises 2.17% in Thursday's session
- Summary: ASML Holding rises 2.17% in Thursday's session
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxQU1U0UTlvTkdwbzFYYTdkYWRFbEJUNG9haEdJWjFOamQ1RE9HTG1LZklTeHQwRzkyQUtnb2Vxc0hQRFd2S3dqNGJQMnZ1eWlqdzVUZlU4eUVHNHR3RUNmR1hzeU5IWWtiRnIzVVk0TmlmZTFwWVQ5Z3BzTm9nYVg3a0lJZDc?oc=5>

### ASML Holding NV Stock (ASML) Moved Down by 4.24% on Nov 20: Drivers Behind the Movement
- Summary: Shares fell 4.24% on Nov 20, reflecting short‑term market volatility.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNbWxmYk5QUXVKSXRrRURvd1RHZ19GVDFjUzZWVUYtTGFpOFdzTGJjS1J2QmdWSGM0aVpVVHF1Nkx4dkNHWEhHZnFOenNCN3M5RlVMMWtfUFllYTEwOEhNeUlHR1RqOU95dkViM2dZSWxUbWR1TVpaQzZGbUlLekNyWENaNkdKY2sxc0tr?oc=5>

### ASML Holding N.V. (NASDAQ: ASML): Powering the AI Semiconductor Supercycle Through EUV Leadership, Pricing Strength and Expanding Capacity
- Summary: ASML’s EUV leadership and capacity expansion support AI semiconductor demand, boosting future earnings.
- Date: 2026-11-23 | Impact: high | Horizon: medium | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMi-wFBVV95cUxPYUhiZWNvSlBVS2JwVjJJYzBXdlVZSWNiU1BMWm5rejlHc1cxcWhYbDBiNjJlSWxqVi1zZW5JQXdVYXRhcDZha19pb3pkTGVobGo1SURWcUxUQlNLN3MtM3cxOXR0MzZkSF9weHdvWldta2ZSaVJEYWUyeG9EaUJURy1PTmtTRy1BbXRnSWtDZXgzUUhkeDc1TElLWW9razluUHVsYlg4T0J1blBzbGIxV0M5eWhZZVNlQ2duUVZRbUVibjRFVVBqM1NXUnBDQjM4LVR3UE4zTXlRTEFzeHMyOW1HY0VBQklsd0xTVkdlajdXelNvcHRtZHEyUQ?oc=5>

## HEADWINDS

### ASML Stock Fell 25% In The AI Selloff, But Its Outlook Hasn’t Budged (NASDAQ:ASML)
- Summary: ASML Stock Fell 25% In The AI Selloff, But Its Outlook Hasn’t Budged (NASDAQ:ASML)
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxNS0xMdThabnAwMURidkl0a3A3alJKVzN2bnJTdThoMUZFQWdaZEEyNGh6OXJmQWQzSXlKM0Y4ZTN0bmNUdmVxRDY2MUlXWmVnNVNuU1VYZEhUMHdKcXlQbHZzMDBER2hlTHhfd0NWVmRkQnA5cHhBb25FTHUwTkpnU3JhQzF5dlNKZ3ZPd1RSR09lZXZkZERYc1FORkhCSlZERlBQM2xPQkg5ai1YMHF1MGFGeV8?oc=5>

### ASML Holding NV Stock (ASML) Moved Down by 7.01% on Nov 25: Drivers Behind the Movement
- Summary: ASML shares fell 7.01% on Nov 25, reflecting short‑term market pressure.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxOU0g5ZEFIeE9tY2hvbW02TjZ2akZKQXllWlUzTFVsclJfUi1nQU5XT3lrQWhOUV9iWHBZTk5IVkxqaElLYUpZTUQweE1CeTFhQlR2R01FMzVRTGFGYnc3Q183bUM2T2V1aW41MVJhYk96S1F0ZUg3VElOVUFuZ3hIamptNjA0UF9QLXdz?oc=5>

### ASML Stock And 3 Non US Chip Equipment Names Investors May Be Missing
- Summary: ASML and other chip equipment stocks may be undervalued, suggesting potential upside.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxQN2pMMFBHQnFUQ2Z4TUlZUnAzMnc5NW1xanBvRHhtWmoyeUVVSnMxa2xoc2FJUmJPcjFiTTZyU2lUajZMSkFLbld2ajJpRXFnaXRUZTh3eG9mWF80VU43SHQ1Z3ZlU1pscGptZUhEOE9iWVFJSk0xRjI2UjhHMHVHb2FnTnJtekhqV29MUVA5TENIMldWSGxuMmhVVHp0ZWdvSktrcjFPaG9rUmM0MXgzVFNkWm5kbm1aUWlYbENiOExYMWRZTjRDWlE4QnFIaUY2MDJ1V05MVUdmb1dvZGF4cC14bkJHUks3NVZEVtIB8gFBVV95cUxQX1F3elZsN1VZa3pXdk5uZ3AtdFZJVUVMNzE5SkJ4T05TQ2lvWUZLNUtIUUc2bHBoRnJsLVVXQ2FlVkFtWGpEVzE3RnhsWjdzcFRjRjNkUjdleDNzMXBuMXFPZXFkWTZQRU5qVG1TQkdzLUNnUVBwMXBDMUFSLXBrVjZFamRGSXhsYnpIcTdTd1NyN3o3blZWVzd2alJ4SXNTZ3JiRF92eUFjcmMyb2x2cUhzREFXQjdfajhtT2xoS09WcTh4Y09ydnFMQ3RmX3pCQUhEeFlGaTlsb1pTdlc5ZDY1aW5QMkdfTTJtallLVHBQQQ?oc=5>

### Congress Could Pass Tougher Chip Curbs “With Veto Proof Majorities.” ASML Has the Most to Lose
- Summary: Potential stricter chip export controls could limit ASML’s market access, impacting revenue.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7wFBVV95cUxQZVloZDBTRjJoYzd5Z3M4aURxbEV5QjRkV3VLNXp4N1hnRkFOVW5PU2dNa1N5NzBIX0FxVExCUGdVa3laZllVcXQ5Tks0Y0hpN3BadTR3TThuQWxId0FYVmk4MUdKYmkxS3VKd2JKaUxzR1JGa01yLWU3Y3hSZ2RMYTloSk9vR0U5OUtUWDNlNmZEcjhEVURUaG9Xa0w1RjU1TzBMdmxUN1ZIVzBOSXh5eU51RWJydm1wcGRicjBVejU4N016dHM0VWlldWoyakRlZmdVX2M5dlNlT2NEb0R6NFRNRlItUndTeEpLYTdnSQ?oc=5>

## CATALYSTS

### ASML reports transactions under its current share buyback program
- Summary: ASML reports transactions under its current share buyback program
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxQVWszUnZEaGRZWHZsSGNRYXhqQmtsMFlMZVltak5HdVBHVy13M2pLeWZpcTdyT2NQQVNmb2tiVy1LX20yV3lvVy1QUzNRVklFSTVJVEtZY19jUXFZcUk5cm44cGV4QlZnSzkyekRmQ3RUcUxWOF9LeTAwOHBmb3M3LV9PVmRQSlFkMGtXeERBREVtQQ?oc=5>

### ASML (ASML) Q2 2026 Earnings Preview: $7.94 EPS Expected, 8% Options Swing; Triangle at $1,800
- Summary: ASML (ASML) Q2 2026 Earnings Preview: $7.94 EPS Expected, 8% Options Swing; Triangle at $1,800
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxNUk5WVnlaMVZ4c04zTVNBV2ZTSDdGOGlsM2xvZUFVZ042UTI3U1p6N0tiaVFJNS1qZmNOTEF1NTBQaWxCWUpLVWF2eXRVSG80R0tTenZGeW5XRGVfMU1RbEEzeXhQS212QVhweVA5ZFdmbFJUamR6UTgwOXpTN1lDZDFtSVRMZWpSSndZclJ6RmxvNFo5VS11RnBtU2xRdFhDT2JkMWEtY2RvdW8zdTkyaE00dlB2WDdVb082OHVROFBoWVRwaEt1NUJn?oc=5>

### ASML surges 9% as chip stocks rally (ASML:NASDAQ)
- Summary: ASML shares jumped 9% amid broader chip market rally.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMifEFVX3lxTFBDTHVWdFhBU1B6Y0RWNmxFZG13akZXdjZGUXkxb1F5cGY3cVExejRnNmQ1bi0tUGl1akRvNDR5Y0o3UmlPaFp4c1hfbEV5eWdyOVhrN3FXTzl0SThHeU9KeFVpNkJBRG54Rnp2THdTRk0za3hsUlI4eWtoWDk?oc=5>

### ASML Stocks Jump 9.59%; Company Bought 557 Million of Its Shares in Selloff Week
- Summary: ASML executed a large share buyback, boosting stock price.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxPeFBhSzJvVUhLMDdlSHg5OWdiTWRqWDhlNWRVcTcwWjdta0tTSmxIeWxYRnUzR2lvam16LXN6RUhNOGhuUXFCdE9RQ2tiNnRVbEN2YjRoaVkxZTZwbXZRWUZRZGFiUW9tY3pUcjFIdExxNG55TkJGdzlWVEZBNXNiZnltVTFMZTNKUHFaZ1BWY0lRbzZsUmhzakhIVnRJcURuUEpyQVhwcFJ1RXplRGNNOGM0NHF3TGIwZVFwZk5GeXNGU0NBOE9vbTB2bWEyUVNrTU1Zdw?oc=5>

### ASML Holding NV Stock (ASML) Moved Up by 10.09% on Nov 23: Facts Behind the Movement
- Summary: Stock price rose 10.09% on Nov 23.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNUUw1aUVCMGN4bUpXamVoaUdhOGtvSGxZcFR4c2g5SGJwRWpsNzEzUFI5cmFoNDl2VkF3RWhIa2xBRGh3SEwwUV9wRzNkaGplU1hmZGxtdmpaWV9OTkFjcXRRdVM0Wi02MzdPbFFxcUV0OUEtcGstcUM0eTJRUlNtOUhEZnAyRGdNa2ZR?oc=5>

## RISKS

### ‘Disastrous' for ASML: Dutch Lawmakers Revolt Against US Push to Tighten China Chip Curbs
- Summary: Dutch lawmakers oppose US chip export restrictions, creating regulatory uncertainty for ASML’s China business.
- Date: 2026-11-25 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxQdi1yQ1BMQ0FZeTFWcTN3RWtjaG1fWTJScHZidExKTWxqeVFxNGthTHNXa0NxMXNuRlAzU0F4Z2NlUzA2bEdPOTE2NXlRWmtEbEpZQV9aSW9pMklxN1FrSWpOODF1czN5QU5LbVE5RWZiYjY2b1otSHlmbE1OOVZqMmp1X1VfV3B4WnVV?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ASML** | **32.06** | **1,118.89** | **1,713.31** | **55.20** | **502,230,122,496.00 USD** | **30.69** |
| AMAT | 24.66 | 9.45 | 20.47 | 53.10 | 246,951,641,088.00 USD | 28.99 |
| LRCX | 27.57 | 16.62 | 22.48 | 54.40 | 231,109,115,904.00 USD | 22.34 |
| KLAC | 33.63 | 26.81 | 26.77 | 28.90 | 174,857,551,872.00 USD | 17.73 |

Peers fetched as_of: 2026-11-25; ASML reuses existing data (market data as_of: 2026-11-25); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-14
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-25

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

- https://news.google.com/rss/articles/CBMiywFBVV95cUxPRjFTdFR5c19TSXh2SERzMUZoSU9BVW5lTmwxaXMtSVVkdGh6SWN6V2QzSGFMa2tLbnJSZERBTkp3UDVEU0lnMWR0Zmx2NWV1Q1RpckRmWFpUMWsyaVhmZGttZF80aVZuck1Way0yamFPWGhlT1FTZ2lwQnBrTkExSm5pQ3JRYnd2bjhjZHQ3LS1WdGFmWmxIazZ6WnR0YjU2QkV0MDVjVzlrTGtidkd3N3hPd3pVSlZfNUJRSjdzWldSeWhjRFVOR0hyMA?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxQU1U0UTlvTkdwbzFYYTdkYWRFbEJUNG9haEdJWjFOamQ1RE9HTG1LZklTeHQwRzkyQUtnb2Vxc0hQRFd2S3dqNGJQMnZ1eWlqdzVUZlU4eUVHNHR3RUNmR1hzeU5IWWtiRnIzVVk0TmlmZTFwWVQ5Z3BzTm9nYVg3a0lJZDc?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNbWxmYk5QUXVKSXRrRURvd1RHZ19GVDFjUzZWVUYtTGFpOFdzTGJjS1J2QmdWSGM0aVpVVHF1Nkx4dkNHWEhHZnFOenNCN3M5RlVMMWtfUFllYTEwOEhNeUlHR1RqOU95dkViM2dZSWxUbWR1TVpaQzZGbUlLekNyWENaNkdKY2sxc0tr?oc=5
- https://news.google.com/rss/articles/CBMi-wFBVV95cUxPYUhiZWNvSlBVS2JwVjJJYzBXdlVZSWNiU1BMWm5rejlHc1cxcWhYbDBiNjJlSWxqVi1zZW5JQXdVYXRhcDZha19pb3pkTGVobGo1SURWcUxUQlNLN3MtM3cxOXR0MzZkSF9weHdvWldta2ZSaVJEYWUyeG9EaUJURy1PTmtTRy1BbXRnSWtDZXgzUUhkeDc1TElLWW9razluUHVsYlg4T0J1blBzbGIxV0M5eWhZZVNlQ2duUVZRbUVibjRFVVBqM1NXUnBDQjM4LVR3UE4zTXlRTEFzeHMyOW1HY0VBQklsd0xTVkdlajdXelNvcHRtZHEyUQ?oc=5
- https://news.google.com/rss/articles/CBMi_wFBVV95cUxNa1Y3STZGTno4elRMSF9GS292V1pteXFUZjF3RmJZcXZlWDFtWERmQkc4WExsNHFfeE1IcnRUbm9sQzhRV1dwbC1wcVo3ZE1sNGZZTDBSMDVPREYwdzFWOEhrZUZxc2hPWUtndjVQcU1LbjAxZUlUMWY2c3FGZV9Vdm4wUXdZdUFseW1OWEJCZ1VOMEowcGhoWlNhdFNjdGlNNkN6bFRfb3doSjRmZTk0OGhwQ3NMV2RMaFdqb25fbzVKM0JFRjlnTjhOekF4bXFJRkpfNTQ5eVdLbEw4VkZ0b0oyNkdiTFJqRC1pbjJFbm5wY3U5NFI2N19panVkVmc?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxNS0xMdThabnAwMURidkl0a3A3alJKVzN2bnJTdThoMUZFQWdaZEEyNGh6OXJmQWQzSXlKM0Y4ZTN0bmNUdmVxRDY2MUlXWmVnNVNuU1VYZEhUMHdKcXlQbHZzMDBER2hlTHhfd0NWVmRkQnA5cHhBb25FTHUwTkpnU3JhQzF5dlNKZ3ZPd1RSR09lZXZkZERYc1FORkhCSlZERlBQM2xPQkg5ai1YMHF1MGFGeV8?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxOU0g5ZEFIeE9tY2hvbW02TjZ2akZKQXllWlUzTFVsclJfUi1nQU5XT3lrQWhOUV9iWHBZTk5IVkxqaElLYUpZTUQweE1CeTFhQlR2R01FMzVRTGFGYnc3Q183bUM2T2V1aW41MVJhYk96S1F0ZUg3VElOVUFuZ3hIamptNjA0UF9QLXdz?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxQN2pMMFBHQnFUQ2Z4TUlZUnAzMnc5NW1xanBvRHhtWmoyeUVVSnMxa2xoc2FJUmJPcjFiTTZyU2lUajZMSkFLbld2ajJpRXFnaXRUZTh3eG9mWF80VU43SHQ1Z3ZlU1pscGptZUhEOE9iWVFJSk0xRjI2UjhHMHVHb2FnTnJtekhqV29MUVA5TENIMldWSGxuMmhVVHp0ZWdvSktrcjFPaG9rUmM0MXgzVFNkWm5kbm1aUWlYbENiOExYMWRZTjRDWlE4QnFIaUY2MDJ1V05MVUdmb1dvZGF4cC14bkJHUks3NVZEVtIB8gFBVV95cUxQX1F3elZsN1VZa3pXdk5uZ3AtdFZJVUVMNzE5SkJ4T05TQ2lvWUZLNUtIUUc2bHBoRnJsLVVXQ2FlVkFtWGpEVzE3RnhsWjdzcFRjRjNkUjdleDNzMXBuMXFPZXFkWTZQRU5qVG1TQkdzLUNnUVBwMXBDMUFSLXBrVjZFamRGSXhsYnpIcTdTd1NyN3o3blZWVzd2alJ4SXNTZ3JiRF92eUFjcmMyb2x2cUhzREFXQjdfajhtT2xoS09WcTh4Y09ydnFMQ3RmX3pCQUhEeFlGaTlsb1pTdlc5ZDY1aW5QMkdfTTJtallLVHBQQQ?oc=5
- https://news.google.com/rss/articles/CBMi7wFBVV95cUxQZVloZDBTRjJoYzd5Z3M4aURxbEV5QjRkV3VLNXp4N1hnRkFOVW5PU2dNa1N5NzBIX0FxVExCUGdVa3laZllVcXQ5Tks0Y0hpN3BadTR3TThuQWxId0FYVmk4MUdKYmkxS3VKd2JKaUxzR1JGa01yLWU3Y3hSZ2RMYTloSk9vR0U5OUtUWDNlNmZEcjhEVURUaG9Xa0w1RjU1TzBMdmxUN1ZIVzBOSXh5eU51RWJydm1wcGRicjBVejU4N016dHM0VWlldWoyakRlZmdVX2M5dlNlT2NEb0R6NFRNRlItUndTeEpLYTdnSQ?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxQVWszUnZEaGRZWHZsSGNRYXhqQmtsMFlMZVltak5HdVBHVy13M2pLeWZpcTdyT2NQQVNmb2tiVy1LX20yV3lvVy1QUzNRVklFSTVJVEtZY19jUXFZcUk5cm44cGV4QlZnSzkyekRmQ3RUcUxWOF9LeTAwOHBmb3M3LV9PVmRQSlFkMGtXeERBREVtQQ?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxNUk5WVnlaMVZ4c04zTVNBV2ZTSDdGOGlsM2xvZUFVZ042UTI3U1p6N0tiaVFJNS1qZmNOTEF1NTBQaWxCWUpLVWF2eXRVSG80R0tTenZGeW5XRGVfMU1RbEEzeXhQS212QVhweVA5ZFdmbFJUamR6UTgwOXpTN1lDZDFtSVRMZWpSSndZclJ6RmxvNFo5VS11RnBtU2xRdFhDT2JkMWEtY2RvdW8zdTkyaE00dlB2WDdVb082OHVROFBoWVRwaEt1NUJn?oc=5
- https://news.google.com/rss/articles/CBMifEFVX3lxTFBDTHVWdFhBU1B6Y0RWNmxFZG13akZXdjZGUXkxb1F5cGY3cVExejRnNmQ1bi0tUGl1akRvNDR5Y0o3UmlPaFp4c1hfbEV5eWdyOVhrN3FXTzl0SThHeU9KeFVpNkJBRG54Rnp2THdTRk0za3hsUlI4eWtoWDk?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxPeFBhSzJvVUhLMDdlSHg5OWdiTWRqWDhlNWRVcTcwWjdta0tTSmxIeWxYRnUzR2lvam16LXN6RUhNOGhuUXFCdE9RQ2tiNnRVbEN2YjRoaVkxZTZwbXZRWUZRZGFiUW9tY3pUcjFIdExxNG55TkJGdzlWVEZBNXNiZnltVTFMZTNKUHFaZ1BWY0lRbzZsUmhzakhIVnRJcURuUEpyQVhwcFJ1RXplRGNNOGM0NHF3TGIwZVFwZk5GeXNGU0NBOE9vbTB2bWEyUVNrTU1Zdw?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNUUw1aUVCMGN4bUpXamVoaUdhOGtvSGxZcFR4c2g5SGJwRWpsNzEzUFI5cmFoNDl2VkF3RWhIa2xBRGh3SEwwUV9wRzNkaGplU1hmZGxtdmpaWV9OTkFjcXRRdVM0Wi02MzdPbFFxcUV0OUEtcGstcUM0eTJRUlNtOUhEZnAyRGdNa2ZR?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxQdi1yQ1BMQ0FZeTFWcTN3RWtjaG1fWTJScHZidExKTWxqeVFxNGthTHNXa0NxMXNuRlAzU0F4Z2NlUzA2bEdPOTE2NXlRWmtEbEpZQV9aSW9pMklxN1FrSWpOODF1czN5QU5LbVE5RWZiYjY2b1otSHlmbE1OOVZqMmp1X1VfV3B4WnVV?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
