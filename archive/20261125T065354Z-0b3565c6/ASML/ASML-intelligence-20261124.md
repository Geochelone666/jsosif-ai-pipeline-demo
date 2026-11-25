# ASML Intelligence Report

- ticker: **ASML**
- Report as_of: **2026-11-24**
- Market data as_of: **2026-11-24**
- Quant sources: https://finance.yahoo.com/quote/ASML/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ASML/key-statistics/
- AI analysis snapshot as_of: **2026-11-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-25T07:01:59.648167+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 20, 'rule': 5, 'ai': 6, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261124T081701Z-6c335e3d/ASML** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'negative_sentiment_in_tailwinds': 1}
- RSS source audit (metadata only, not article fact-checking): 20 unique headlines; 12 named publishers; 2 exact duplicates; 20 HTTPS source links; largest publisher share 15.0%; oldest publication 2026-11-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 1336.0601 |
| Return 1D (%) | -3.4485 |
| Return 1W (%) | -3.4017 |
| Return 1M (%) | -14.8860 |
| Return YTD (%) | 25.6472 |
| Return 1Y (%) | 36.0824 |
| Annualized volatility (%) | 50.0531 |
| Beta vs SPY | 2.2370 |
| Max drawdown (%) | -36.1866 |
| Sharpe (rf=0) | 0.8674 |
| Downside deviation (rf=0, %) | 33.8256 |
| Sortino (rf=0) | 1.2835 |
| Historical VaR 95% (1D, %) | 5.0034 |
| Historical ES 95% (1D, %) | 6.6569 |
| Correlation vs SPY | 0.6684 |
| Tracking error vs SPY (%) | 41.5739 |
| P/E (trailing) | 32.88 |
| P/B | 1147.21 |
| EV/EBITDA | 1756.69 |
| Revenue growth (%) | 55.20 |
| Forward P/E (estimate) | 21.07 |
| Gross margin (%) | 54.34 |
| Operating margin (%) | 38.55 |
| Return on equity (%) | 65.64 |
| Free cash flow yield (%) | N/A |
| MA50 | 1614.4969 |
| Close vs MA50 (%) | -17.2460 |
| MA200 | 1597.0347 |
| Close vs MA200 (%) | -16.3412 |
| RSI (14, Wilder) | 38.1112 |
| MACD (12,26) | -79.0525 |
| MACD signal (9) | -70.5069 |
| MACD histogram | -8.5456 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ASML': 289, 'SPY': 289}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 1336.0601 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -3.4485 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -3.4017 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -14.8860 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 25.6472 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 36.0824 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 50.0531 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 33.8256 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.2835 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 5.0034 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.6569 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6684 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 41.5739 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.2370 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -36.1866 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.8674 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 21.0737 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.3370 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 38.5520 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 65.6360 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 32.8755 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 38.1112 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -8.5456 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -17.2460 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -16.3412 -> Clearly below the moving-average trend level.

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
- Summary: ASML expands EUV capacity, strengthens pricing, supporting AI semiconductor demand.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi_wFBVV95cUxNa1Y3STZGTno4elRMSF9GS292V1pteXFUZjF3RmJZcXZlWDFtWERmQkc4WExsNHFfeE1IcnRUbm9sQzhRV1dwbC1wcVo3ZE1sNGZZTDBSMDVPREYwdzFWOEhrZUZxc2hPWUtndjVQcU1LbjAxZUlUMWY2c3FGZV9Vdm4wUXdZdUFseW1OWEJCZ1VOMEowcGhoWlNhdFNjdGlNNkN6bFRfb3doSjRmZTk0OGhwQ3NMV2RMaFdqb25fbzVKM0JFRjlnTjhOekF4bXFJRkpfNTQ5eVdLbEw4VkZ0b0oyNkdiTFJqRC1pbjJFbm5wY3U5NFI2N19panVkVmc?oc=5>

## HEADWINDS

### ASML Stock Fell 25% In The AI Selloff, But Its Outlook Hasn’t Budged (NASDAQ:ASML)
- Summary: ASML Stock Fell 25% In The AI Selloff, But Its Outlook Hasn’t Budged (NASDAQ:ASML)
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxNS0xMdThabnAwMURidkl0a3A3alJKVzN2bnJTdThoMUZFQWdaZEEyNGh6OXJmQWQzSXlKM0Y4ZTN0bmNUdmVxRDY2MUlXWmVnNVNuU1VYZEhUMHdKcXlQbHZzMDBER2hlTHhfd0NWVmRkQnA5cHhBb25FTHUwTkpnU3JhQzF5dlNKZ3ZPd1RSR09lZXZkZERYc1FORkhCSlZERlBQM2xPQkg5ai1YMHF1MGFGeV8?oc=5>

### Why is ASML stock sliding today?
- Summary: ASML shares decline due to market volatility and investor concerns about earnings outlook.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPUjUxQVlLLUhQRlhhbDhiazlZempiRGR3ZnNRT2JmWmdsTG9sUWpHN1UyS29rRHVEVGNQUjR4eEpGZ3BpcnFBVmV6Vnp3RDNuS0Y4ZXZCWGVRVEV4Y24wRUtyYmhWemVsRXFRa1JRdVBaRTNYNktHWi1zaVVSTTdSTTFkMUpPUDRnSExpM3hnRDh0bnluZDR2UQ?oc=5>

## CATALYSTS

### ASML reports transactions under its current share buyback program
- Summary: ASML reports transactions under its current share buyback program
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxPa3dUS3AzOEtFMjNONHhWTnJSbHNFMjlRdkg1Tl81cFBKcVpESjc1ZTlRdkttY2dXamM3S0c3bF81UXQ4LThjVEJEQ3BncG5EVFh3VW9yM3l6QnFaOUQ4c3VLd2pRUU83bWJYQVhyeUtJdXU1SndpTkt3WXFrOUpzWE9IbWh1OHluOXBfdnZBend5d0tmSWd3dl9JZ1ZVVzM2ZnFXOHdPTjF3WnFC?oc=5>

### ASML reports €557m share buyback transactions last week
- Summary: ASML reports €557m share buyback transactions last week
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQVmNwbTdRb0s1bGpweFl5cDV6ODgxeFNlSjhhVTRvdjNWNEZpY0tsYUswdk1oblpybTh1cFdaSVE1eWFjVGdpbXdNdnU2anlNbmdFejBmeDdOLUdBTzJ1QjJzYkFWSGNWNGJwTWVJSjA3Q3YtT2xEQWRQTW1TVERpUk1IbGZCTmN5Q2tlRWVJNjEtVFd2dkZVV1NSOHQ5Q2pfYUNTVVJ3ZVh4WGpjZkJHMw?oc=5>

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

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ASML** | **32.88** | **1,147.21** | **1,756.69** | **55.20** | **514,941,222,912.00 USD** | **36.08** |
| AMAT | 25.65 | 9.83 | 21.30 | 53.10 | 256,935,116,800.00 USD | 40.92 |
| LRCX | 29.23 | 17.62 | 23.86 | 54.40 | 245,037,383,680.00 USD | 31.05 |
| KLAC | 29.12 | 26.70 | 26.66 | 28.90 | 174,140,915,712.00 USD | 18.19 |

Peers fetched as_of: 2026-11-24; ASML reuses existing data (market data as_of: 2026-11-24); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-14
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-24

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
- https://news.google.com/rss/articles/CBMi_wFBVV95cUxNa1Y3STZGTno4elRMSF9GS292V1pteXFUZjF3RmJZcXZlWDFtWERmQkc4WExsNHFfeE1IcnRUbm9sQzhRV1dwbC1wcVo3ZE1sNGZZTDBSMDVPREYwdzFWOEhrZUZxc2hPWUtndjVQcU1LbjAxZUlUMWY2c3FGZV9Vdm4wUXdZdUFseW1OWEJCZ1VOMEowcGhoWlNhdFNjdGlNNkN6bFRfb3doSjRmZTk0OGhwQ3NMV2RMaFdqb25fbzVKM0JFRjlnTjhOekF4bXFJRkpfNTQ5eVdLbEw4VkZ0b0oyNkdiTFJqRC1pbjJFbm5wY3U5NFI2N19panVkVmc?oc=5
- https://news.google.com/rss/articles/CBMi-gFBVV95cUxONjVkUVRJRnV3U0s1bW84ajFlSWVrVkJ0Q3E0TWowSnI2Y2NHOHpoMUhtT0luMmR0MDhlUXRjTE8zcjQ3UmNqMXJvaE1FS3ZibVBwVUI1eG1PdWw1cDB4R3Y4ekJuem0wSVNncExQVFcteXN2UkdtYmg0Qk5HS0ZkeGNXZmJfZ2VyYmxrcklaM2JnOTk0RE9ZLUZKc2FGeHc2QS1JNEJSOXVITURLYlpQZGpFd3B1YnI4VWdnUXdLaS12dmFpQlVnUmJxNTBGa05haTFqQ2YzbV9mN2w4NlFwb01TdjFicWFxQ2pLdVpmMmR6T3FDOWY2LW5B?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxNS0xMdThabnAwMURidkl0a3A3alJKVzN2bnJTdThoMUZFQWdaZEEyNGh6OXJmQWQzSXlKM0Y4ZTN0bmNUdmVxRDY2MUlXWmVnNVNuU1VYZEhUMHdKcXlQbHZzMDBER2hlTHhfd0NWVmRkQnA5cHhBb25FTHUwTkpnU3JhQzF5dlNKZ3ZPd1RSR09lZXZkZERYc1FORkhCSlZERlBQM2xPQkg5ai1YMHF1MGFGeV8?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPUjUxQVlLLUhQRlhhbDhiazlZempiRGR3ZnNRT2JmWmdsTG9sUWpHN1UyS29rRHVEVGNQUjR4eEpGZ3BpcnFBVmV6Vnp3RDNuS0Y4ZXZCWGVRVEV4Y24wRUtyYmhWemVsRXFRa1JRdVBaRTNYNktHWi1zaVVSTTdSTTFkMUpPUDRnSExpM3hnRDh0bnluZDR2UQ?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxPa3dUS3AzOEtFMjNONHhWTnJSbHNFMjlRdkg1Tl81cFBKcVpESjc1ZTlRdkttY2dXamM3S0c3bF81UXQ4LThjVEJEQ3BncG5EVFh3VW9yM3l6QnFaOUQ4c3VLd2pRUU83bWJYQVhyeUtJdXU1SndpTkt3WXFrOUpzWE9IbWh1OHluOXBfdnZBend5d0tmSWd3dl9JZ1ZVVzM2ZnFXOHdPTjF3WnFC?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxQVmNwbTdRb0s1bGpweFl5cDV6ODgxeFNlSjhhVTRvdjNWNEZpY0tsYUswdk1oblpybTh1cFdaSVE1eWFjVGdpbXdNdnU2anlNbmdFejBmeDdOLUdBTzJ1QjJzYkFWSGNWNGJwTWVJSjA3Q3YtT2xEQWRQTW1TVERpUk1IbGZCTmN5Q2tlRWVJNjEtVFd2dkZVV1NSOHQ5Q2pfYUNTVVJ3ZVh4WGpjZkJHMw?oc=5
- https://news.google.com/rss/articles/CBMifEFVX3lxTFBDTHVWdFhBU1B6Y0RWNmxFZG13akZXdjZGUXkxb1F5cGY3cVExejRnNmQ1bi0tUGl1akRvNDR5Y0o3UmlPaFp4c1hfbEV5eWdyOVhrN3FXTzl0SThHeU9KeFVpNkJBRG54Rnp2THdTRk0za3hsUlI4eWtoWDk?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxPeFBhSzJvVUhLMDdlSHg5OWdiTWRqWDhlNWRVcTcwWjdta0tTSmxIeWxYRnUzR2lvam16LXN6RUhNOGhuUXFCdE9RQ2tiNnRVbEN2YjRoaVkxZTZwbXZRWUZRZGFiUW9tY3pUcjFIdExxNG55TkJGdzlWVEZBNXNiZnltVTFMZTNKUHFaZ1BWY0lRbzZsUmhzakhIVnRJcURuUEpyQVhwcFJ1RXplRGNNOGM0NHF3TGIwZVFwZk5GeXNGU0NBOE9vbTB2bWEyUVNrTU1Zdw?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNUUw1aUVCMGN4bUpXamVoaUdhOGtvSGxZcFR4c2g5SGJwRWpsNzEzUFI5cmFoNDl2VkF3RWhIa2xBRGh3SEwwUV9wRzNkaGplU1hmZGxtdmpaWV9OTkFjcXRRdVM0Wi02MzdPbFFxcUV0OUEtcGstcUM0eTJRUlNtOUhEZnAyRGdNa2ZR?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
