# ASML Intelligence Report

- ticker: **ASML**
- Report as_of: **2026-11-23**
- Market data as_of: **2026-11-23**
- Quant sources: https://finance.yahoo.com/quote/ASML/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ASML/key-statistics/
- AI analysis snapshot as_of: **2026-11-23**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-24T08:29:57.859030+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 7, 'ai': 8, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261123T053847Z-45053549/ASML** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'negative_sentiment_in_tailwinds': 2}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 19 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 8.33%; oldest publication 2026-11-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 1383.7800 |
| Return 1D (%) | 9.2843 |
| Return 1W (%) | -1.6356 |
| Return 1M (%) | -11.8459 |
| Return YTD (%) | 30.1350 |
| Return 1Y (%) | 44.0415 |
| Annualized volatility (%) | 50.0205 |
| Beta vs SPY | 2.2312 |
| Max drawdown (%) | -36.1866 |
| Sharpe (rf=0) | 0.9409 |
| Downside deviation (rf=0, %) | 33.7158 |
| Sortino (rf=0) | 1.3959 |
| Historical VaR 95% (1D, %) | 5.0250 |
| Historical ES 95% (1D, %) | 6.6569 |
| Correlation vs SPY | 0.6680 |
| Tracking error vs SPY (%) | 41.5402 |
| P/E (trailing) | 34.05 |
| P/B | 1188.18 |
| EV/EBITDA | 1819.46 |
| Revenue growth (%) | 55.20 |
| Forward P/E (estimate) | 21.83 |
| Gross margin (%) | 54.34 |
| Operating margin (%) | 38.55 |
| Return on equity (%) | 65.64 |
| Free cash flow yield (%) | N/A |
| MA50 | 1619.5633 |
| Close vs MA50 (%) | -14.5584 |
| MA200 | 1597.4584 |
| Close vs MA200 (%) | -13.3761 |
| RSI (14, Wilder) | 40.9307 |
| MACD (12,26) | -78.3096 |
| MACD signal (9) | -68.3705 |
| MACD histogram | -9.9391 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ASML': 288, 'SPY': 288}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 1383.7800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 9.2843 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.6356 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -11.8459 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 30.1350 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 44.0415 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 50.0205 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 33.7158 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.3959 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 5.0250 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.6569 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6680 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 41.5402 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.2312 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -36.1866 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9409 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 21.8264 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.3370 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 38.5520 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 65.6360 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 34.0497 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 40.9307 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -9.9391 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -14.5584 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -13.3761 -> Clearly below the moving-average trend level.

## TAILWINDS

### ASML Stock 12‑Month Price Target Raised to $2,436.94, Implies 92% Upside
- Summary: ASML Stock 12‑Month Price Target Raised to $2,436.94, Implies 92% Upside
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxPRjFTdFR5c19TSXh2SERzMUZoSU9BVW5lTmwxaXMtSVVkdGh6SWN6V2QzSGFMa2tLbnJSZERBTkp3UDVEU0lnMWR0Zmx2NWV1Q1RpckRmWFpUMWsyaVhmZGttZF80aVZuck1Way0yamFPWGhlT1FTZ2lwQnBrTkExSm5pQ3JRYnd2bjhjZHQ3LS1WdGFmWmxIazZ6WnR0YjU2QkV0MDVjVzlrTGtidkd3N3hPd3pVSlZfNUJRSjdzWldSeWhjRFVOR0hyMA?oc=5>

### ASML Holding NV (ASML) Stock Up 9.3% and Still Undervalued -- GF Score: 98/100
- Summary: ASML Holding NV (ASML) Stock Up 9.3% and Still Undervalued -- GF Score: 98/100
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxPVV9fQTk3el92MnFLa1g1S0pRUmhDcTlDYURiaEN0UWFlcHZrZXhTdjIyd3BiVXJ1Q2R1ckl4TG5EVEU4X0F6Z0dfd2E2cm8wdDJIOVNjSzhYaTFlTS1aRDFQb3lCQjdJcm1QOS1ZNFJQOHd2akNjb3UtdENjR3M2OW9SX003aExqOEozQi1nMkEyc1ZCNmp1UWFHYVJyWm00MG04TkNoV2pXU3Vj?oc=5>

### ASML Holding NV Stock (ASML) Moved Down by 4.24% on Nov 20: Drivers Behind the Movement
- Summary: Shares fell 4.24% on Nov 20, reflecting short‑term market volatility.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNbWxmYk5QUXVKSXRrRURvd1RHZ19GVDFjUzZWVUYtTGFpOFdzTGJjS1J2QmdWSGM0aVpVVHF1Nkx4dkNHWEhHZnFOenNCN3M5RlVMMWtfUFllYTEwOEhNeUlHR1RqOU95dkViM2dZSWxUbWR1TVpaQzZGbUlLekNyWENaNkdKY2sxc0tr?oc=5>

### ASML Holding shares rebound 4.5% but are down 14.5% over the quarter
- Summary: Shares rebounded 4.5% intraday but remain 14.5% lower YTD, indicating ongoing downside pressure.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxQTVdLYWNYOWdhQkJmdEhYNFViWVNlLWJ4RkVPSV9SRXQtUEQxaFE1OFFQX2tHeXk4ZU0wMTV3ZlZ0VWxzbC1pemdkM3pGOXRvakE1U3h0TjJUQUtiMkZ6UnI1RkNoeks5bkJZZVc0ZmU0R3hnRHFtRnA0NG5sRy1NSE1hWHY4VlVIMDYzRGFWYkV2bFhxc3BraGpBTnJiaHJ3U25zaDlTZUJQSWRxOEdTeGQzc2ZzdW41U0FaM0tRM0xiUFk?oc=5>

### ASML Holding N.V. (NASDAQ: ASML): Powering the AI Semiconductor Supercycle Through EUV Leadership, Pricing Strength and Expanding Capacity
- Summary: ASML expands EUV capacity, strengthens pricing, supporting AI semiconductor demand.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi_wFBVV95cUxNa1Y3STZGTno4elRMSF9GS292V1pteXFUZjF3RmJZcXZlWDFtWERmQkc4WExsNHFfeE1IcnRUbm9sQzhRV1dwbC1wcVo3ZE1sNGZZTDBSMDVPREYwdzFWOEhrZUZxc2hPWUtndjVQcU1LbjAxZUlUMWY2c3FGZV9Vdm4wUXdZdUFseW1OWEJCZ1VOMEowcGhoWlNhdFNjdGlNNkN6bFRfb3doSjRmZTk0OGhwQ3NMV2RMaFdqb25fbzVKM0JFRjlnTjhOekF4bXFJRkpfNTQ5eVdLbEw4VkZ0b0oyNkdiTFJqRC1pbjJFbm5wY3U5NFI2N19panVkVmc?oc=5>

## HEADWINDS

### ASML Stock Fell 25% In The AI Selloff, But Its Outlook Hasn’t Budged (NASDAQ:ASML)
- Summary: ASML Stock Fell 25% In The AI Selloff, But Its Outlook Hasn’t Budged (NASDAQ:ASML)
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxNS0xMdThabnAwMURidkl0a3A3alJKVzN2bnJTdThoMUZFQWdaZEEyNGh6OXJmQWQzSXlKM0Y4ZTN0bmNUdmVxRDY2MUlXWmVnNVNuU1VYZEhUMHdKcXlQbHZzMDBER2hlTHhfd0NWVmRkQnA5cHhBb25FTHUwTkpnU3JhQzF5dlNKZ3ZPd1RSR09lZXZkZERYc1FORkhCSlZERlBQM2xPQkg5ai1YMHF1MGFGeV8?oc=5>

### ASML Holding falls 9.04% in Friday's session
- Summary: ASML Holding falls 9.04% in Friday's session
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxNd09KVEw0ZUFQcm5OWFdaY0VxMTV1YW9xVFZnOU9ZbERDS2MtaWN6bFFJN3FsbXJRS2NPY2ZwMGZqVm9oSS1aUjdzZDdEc3VXZWRUT1VDZERVeVg5T0xPblFtZnUxZjBIbElKZ2tiWFpGUnRpbVlUdjF0cUx6YWNiMVQxRDU?oc=5>

### Can ASML (NASDAQ:ASML) Deliver When It Matters Most?
- Summary: Questions about ASML’s ability to meet critical demand.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOODRNR0lpQ3p2OTE1VjVaeUpLVHlXUl9POVRKbWo5U19mbjhtUGc0N1NneVo4c1dnVG0wVnA1d0VWd3Vxb3RCS21IMXVaMnBOSU9tOFFaSlhiYWlPYTJCbFVhTmV1bUdOMWZ3b0YxM0xfWnlLdGI0cTdpLWJXVTRGYnZlYWFwMnVjcWFJQzNOa1BZMUQ3RXpraEN3?oc=5>

## CATALYSTS

### ASML reports transactions under its current share buyback program
- Summary: ASML reports transactions under its current share buyback program
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxPa3dUS3AzOEtFMjNONHhWTnJSbHNFMjlRdkg1Tl81cFBKcVpESjc1ZTlRdkttY2dXamM3S0c3bF81UXQ4LThjVEJEQ3BncG5EVFh3VW9yM3l6QnFaOUQ4c3VLd2pRUU83bWJYQVhyeUtJdXU1SndpTkt3WXFrOUpzWE9IbWh1OHluOXBfdnZBend5d0tmSWd3dl9JZ1ZVVzM2ZnFXOHdPTjF3WnFC?oc=5>

### ASML reports €557m share buyback transactions last week
- Summary: ASML reports €557m share buyback transactions last week
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQVmNwbTdRb0s1bGpweFl5cDV6ODgxeFNlSjhhVTRvdjNWNEZpY0tsYUswdk1oblpybTh1cFdaSVE1eWFjVGdpbXdNdnU2anlNbmdFejBmeDdOLUdBTzJ1QjJzYkFWSGNWNGJwTWVJSjA3Q3YtT2xEQWRQTW1TVERpUk1IbGZCTmN5Q2tlRWVJNjEtVFd2dkZVV1NSOHQ5Q2pfYUNTVVJ3ZVh4WGpjZkJHMw?oc=5>

### ASML reports €557m share buyback transactions last week By Investing.com
- Summary: ASML reports €557m share buyback transactions last week By Investing.com
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxQb3BkNlEtNE1jbEkyQUV6VjVHZTFtaTBmemE4TGl0OUgzVVdRX3Z6REFmWGJzbVVKVHk4d0JmQTJTRVE3VVJ1b1Q0Y1JxcmJTTUlJVHAzaEJjMnhoZFJ6a3BveFdseUFQQUJjUG1HMXlnZTBBdVhEWFdFQUNUM2hmTHEtZWdjQjRTQUVaVy1VWDdaVWJBWnRONWpQWF9nbkFIbkhsZG9tVWpVRDFpemVwX19iY05RQQ?oc=5>

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

### European stocks open higher as ASML rebounds 3% after the AI rout
- Summary: ASML shares jump 3% as European markets rally post AI downturn, signaling investor confidence.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxNTVV5MGxXbzVqZzNHdnVvcFVBalpIQUtISGwtb0NYVW9KOW1LWDlWYlpKNkwyTTJtaExjbnZDRkFRbHM1WmgzU2xkdWI1SGpQYmszT2lKNTQxSGVJY2dqaFEtTzJhNVRxa05TdGdZYVNnTFJwellRaWZfZVdJMUkxRzNVVUN4dXRQYWRHMmF3?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ASML** | **34.05** | **1,188.18** | **1,819.46** | **55.20** | **533,333,344,256.00 USD** | **44.04** |
| AMAT | 27.49 | 10.54 | 22.84 | 53.10 | 275,275,153,408.00 USD | 55.63 |
| LRCX | 31.26 | 18.84 | 25.54 | 54.40 | 262,026,084,352.00 USD | 47.72 |
| KLAC | 31.78 | 29.14 | 29.07 | 28.90 | 190,037,082,112.00 USD | 33.63 |

Peers fetched as_of: 2026-11-23; ASML reuses existing data (market data as_of: 2026-11-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-14
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-23

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
- https://news.google.com/rss/articles/CBMirAFBVV95cUxPVV9fQTk3el92MnFLa1g1S0pRUmhDcTlDYURiaEN0UWFlcHZrZXhTdjIyd3BiVXJ1Q2R1ckl4TG5EVEU4X0F6Z0dfd2E2cm8wdDJIOVNjSzhYaTFlTS1aRDFQb3lCQjdJcm1QOS1ZNFJQOHd2akNjb3UtdENjR3M2OW9SX003aExqOEozQi1nMkEyc1ZCNmp1UWFHYVJyWm00MG04TkNoV2pXU3Vj?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNbWxmYk5QUXVKSXRrRURvd1RHZ19GVDFjUzZWVUYtTGFpOFdzTGJjS1J2QmdWSGM0aVpVVHF1Nkx4dkNHWEhHZnFOenNCN3M5RlVMMWtfUFllYTEwOEhNeUlHR1RqOU95dkViM2dZSWxUbWR1TVpaQzZGbUlLekNyWENaNkdKY2sxc0tr?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxQTVdLYWNYOWdhQkJmdEhYNFViWVNlLWJ4RkVPSV9SRXQtUEQxaFE1OFFQX2tHeXk4ZU0wMTV3ZlZ0VWxzbC1pemdkM3pGOXRvakE1U3h0TjJUQUtiMkZ6UnI1RkNoeks5bkJZZVc0ZmU0R3hnRHFtRnA0NG5sRy1NSE1hWHY4VlVIMDYzRGFWYkV2bFhxc3BraGpBTnJiaHJ3U25zaDlTZUJQSWRxOEdTeGQzc2ZzdW41U0FaM0tRM0xiUFk?oc=5
- https://news.google.com/rss/articles/CBMi_wFBVV95cUxNa1Y3STZGTno4elRMSF9GS292V1pteXFUZjF3RmJZcXZlWDFtWERmQkc4WExsNHFfeE1IcnRUbm9sQzhRV1dwbC1wcVo3ZE1sNGZZTDBSMDVPREYwdzFWOEhrZUZxc2hPWUtndjVQcU1LbjAxZUlUMWY2c3FGZV9Vdm4wUXdZdUFseW1OWEJCZ1VOMEowcGhoWlNhdFNjdGlNNkN6bFRfb3doSjRmZTk0OGhwQ3NMV2RMaFdqb25fbzVKM0JFRjlnTjhOekF4bXFJRkpfNTQ5eVdLbEw4VkZ0b0oyNkdiTFJqRC1pbjJFbm5wY3U5NFI2N19panVkVmc?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxNS0xMdThabnAwMURidkl0a3A3alJKVzN2bnJTdThoMUZFQWdaZEEyNGh6OXJmQWQzSXlKM0Y4ZTN0bmNUdmVxRDY2MUlXWmVnNVNuU1VYZEhUMHdKcXlQbHZzMDBER2hlTHhfd0NWVmRkQnA5cHhBb25FTHUwTkpnU3JhQzF5dlNKZ3ZPd1RSR09lZXZkZERYc1FORkhCSlZERlBQM2xPQkg5ai1YMHF1MGFGeV8?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxNd09KVEw0ZUFQcm5OWFdaY0VxMTV1YW9xVFZnOU9ZbERDS2MtaWN6bFFJN3FsbXJRS2NPY2ZwMGZqVm9oSS1aUjdzZDdEc3VXZWRUT1VDZERVeVg5T0xPblFtZnUxZjBIbElKZ2tiWFpGUnRpbVlUdjF0cUx6YWNiMVQxRDU?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOODRNR0lpQ3p2OTE1VjVaeUpLVHlXUl9POVRKbWo5U19mbjhtUGc0N1NneVo4c1dnVG0wVnA1d0VWd3Vxb3RCS21IMXVaMnBOSU9tOFFaSlhiYWlPYTJCbFVhTmV1bUdOMWZ3b0YxM0xfWnlLdGI0cTdpLWJXVTRGYnZlYWFwMnVjcWFJQzNOa1BZMUQ3RXpraEN3?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxPa3dUS3AzOEtFMjNONHhWTnJSbHNFMjlRdkg1Tl81cFBKcVpESjc1ZTlRdkttY2dXamM3S0c3bF81UXQ4LThjVEJEQ3BncG5EVFh3VW9yM3l6QnFaOUQ4c3VLd2pRUU83bWJYQVhyeUtJdXU1SndpTkt3WXFrOUpzWE9IbWh1OHluOXBfdnZBend5d0tmSWd3dl9JZ1ZVVzM2ZnFXOHdPTjF3WnFC?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxQVmNwbTdRb0s1bGpweFl5cDV6ODgxeFNlSjhhVTRvdjNWNEZpY0tsYUswdk1oblpybTh1cFdaSVE1eWFjVGdpbXdNdnU2anlNbmdFejBmeDdOLUdBTzJ1QjJzYkFWSGNWNGJwTWVJSjA3Q3YtT2xEQWRQTW1TVERpUk1IbGZCTmN5Q2tlRWVJNjEtVFd2dkZVV1NSOHQ5Q2pfYUNTVVJ3ZVh4WGpjZkJHMw?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxQb3BkNlEtNE1jbEkyQUV6VjVHZTFtaTBmemE4TGl0OUgzVVdRX3Z6REFmWGJzbVVKVHk4d0JmQTJTRVE3VVJ1b1Q0Y1JxcmJTTUlJVHAzaEJjMnhoZFJ6a3BveFdseUFQQUJjUG1HMXlnZTBBdVhEWFdFQUNUM2hmTHEtZWdjQjRTQUVaVy1VWDdaVWJBWnRONWpQWF9nbkFIbkhsZG9tVWpVRDFpemVwX19iY05RQQ?oc=5
- https://news.google.com/rss/articles/CBMifEFVX3lxTFBDTHVWdFhBU1B6Y0RWNmxFZG13akZXdjZGUXkxb1F5cGY3cVExejRnNmQ1bi0tUGl1akRvNDR5Y0o3UmlPaFp4c1hfbEV5eWdyOVhrN3FXTzl0SThHeU9KeFVpNkJBRG54Rnp2THdTRk0za3hsUlI4eWtoWDk?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxPeFBhSzJvVUhLMDdlSHg5OWdiTWRqWDhlNWRVcTcwWjdta0tTSmxIeWxYRnUzR2lvam16LXN6RUhNOGhuUXFCdE9RQ2tiNnRVbEN2YjRoaVkxZTZwbXZRWUZRZGFiUW9tY3pUcjFIdExxNG55TkJGdzlWVEZBNXNiZnltVTFMZTNKUHFaZ1BWY0lRbzZsUmhzakhIVnRJcURuUEpyQVhwcFJ1RXplRGNNOGM0NHF3TGIwZVFwZk5GeXNGU0NBOE9vbTB2bWEyUVNrTU1Zdw?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNUUw1aUVCMGN4bUpXamVoaUdhOGtvSGxZcFR4c2g5SGJwRWpsNzEzUFI5cmFoNDl2VkF3RWhIa2xBRGh3SEwwUV9wRzNkaGplU1hmZGxtdmpaWV9OTkFjcXRRdVM0Wi02MzdPbFFxcUV0OUEtcGstcUM0eTJRUlNtOUhEZnAyRGdNa2ZR?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxNTVV5MGxXbzVqZzNHdnVvcFVBalpIQUtISGwtb0NYVW9KOW1LWDlWYlpKNkwyTTJtaExjbnZDRkFRbHM1WmgzU2xkdWI1SGpQYmszT2lKNTQxSGVJY2dqaFEtTzJhNVRxa05TdGdZYVNnTFJwellRaWZfZVdJMUkxRzNVVUN4dXRQYWRHMmF3?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
