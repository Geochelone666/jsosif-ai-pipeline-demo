# ASML Intelligence Report

- ticker: **ASML**
- Report as_of: **2026-11-20**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/ASML/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ASML/key-statistics/
- AI analysis snapshot as_of: **2026-11-20**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-21T05:32:27.376098+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 5, 'ai': 10, 'unknown': 0, 'irrelevant': 10})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261119T054856Z-9eb86811/ASML** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **3**; {'negative_sentiment_in_tailwinds': 3}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 14 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 16.0%; oldest publication 2026-11-16

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 1266.2200 |
| Return 1D (%) | -6.6347 |
| Return 1W (%) | -15.3121 |
| Return 1M (%) | -22.2554 |
| Return YTD (%) | 19.0792 |
| Return 1Y (%) | 29.8603 |
| Annualized volatility (%) | 49.1444 |
| Beta vs SPY | 2.2352 |
| Max drawdown (%) | -36.1866 |
| Sharpe (rf=0) | 0.7790 |
| Downside deviation (rf=0, %) | 33.6811 |
| Sortino (rf=0) | 1.1366 |
| Historical VaR 95% (1D, %) | 5.0034 |
| Historical ES 95% (1D, %) | 6.6569 |
| Correlation vs SPY | 0.6502 |
| Tracking error vs SPY (%) | 41.3037 |
| P/E (trailing) | 31.16 |
| P/B | 1087.24 |
| EV/EBITDA | 1664.83 |
| Revenue growth (%) | 55.20 |
| Forward P/E (estimate) | 19.97 |
| Gross margin (%) | 54.34 |
| Operating margin (%) | 38.55 |
| Return on equity (%) | 65.64 |
| Free cash flow yield (%) | N/A |
| MA50 | 1623.3492 |
| Close vs MA50 (%) | -21.9995 |
| MA200 | 1597.5615 |
| Close vs MA200 (%) | -20.7405 |
| RSI (14, Wilder) | 28.8979 |
| MACD (12,26) | -81.0811 |
| MACD signal (9) | -65.8857 |
| MACD histogram | -15.1953 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ASML': 287, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 1266.2200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -6.6347 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -15.3121 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -22.2554 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 19.0792 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 29.8603 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 49.1444 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 33.6811 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.1366 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 5.0034 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.6569 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6502 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 41.3037 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.2352 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -36.1866 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.7790 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 19.9721 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.3370 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 38.5520 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 65.6360 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 31.1570 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 28.8979 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -15.1953 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -21.9995 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -20.7405 -> Clearly below the moving-average trend level.

## TAILWINDS

### ASML emerges as a top AI stock pick as volatility hits ahead of the Anthropic IPO
- Summary: ASML emerges as a top AI stock pick as volatility hits ahead of the Anthropic IPO
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMia0FVX3lxTFA5SzAtRE1SMDIyUEh3QjI3VEJWMmEza0xyRFYzQWdqRXRzcnFoQWpqRXltVnZKYW80aDN4WTdRNlZLZDhpTjhxaFhEQW1FMXd5RnZMeWJHTGVKZHRuSmM1NEJPWk1XVUhSaTJ3?oc=5>

### ASML Holding NV Stock (ASML) Moved Down by 4.24% on Nov 20: Drivers Behind the Movement
- Summary: Shares fell 4.24% on Nov 20, reflecting short‑term market volatility.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNbWxmYk5QUXVKSXRrRURvd1RHZ19GVDFjUzZWVUYtTGFpOFdzTGJjS1J2QmdWSGM0aVpVVHF1Nkx4dkNHWEhHZnFOenNCN3M5RlVMMWtfUFllYTEwOEhNeUlHR1RqOU95dkViM2dZSWxUbWR1TVpaQzZGbUlLekNyWENaNkdKY2sxc0tr?oc=5>

### ASML Holding shares rebound 4.5% but are down 14.5% over the quarter
- Summary: Shares rebounded 4.5% intraday but remain 14.5% lower YTD, indicating ongoing downside pressure.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxQTVdLYWNYOWdhQkJmdEhYNFViWVNlLWJ4RkVPSV9SRXQtUEQxaFE1OFFQX2tHeXk4ZU0wMTV3ZlZ0VWxzbC1pemdkM3pGOXRvakE1U3h0TjJUQUtiMkZ6UnI1RkNoeks5bkJZZVc0ZmU0R3hnRHFtRnA0NG5sRy1NSE1hWHY4VlVIMDYzRGFWYkV2bFhxc3BraGpBTnJiaHJ3U25zaDlTZUJQSWRxOEdTeGQzc2ZzdW41U0FaM0tRM0xiUFk?oc=5>

### ASML Holding NV (ASML) Stock Down 6.4% -- Now Undervalued? GF Sc
- Summary: Shares dropped 6.4%, raising questions about valuation but no fundamental change reported.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxORUdqSzZ6R0h2MERHYXRacTFrbVd2dG5GZWtRRy1VLUl0bGRPUS1vWnNLQzF1Wkl0QTB6emcyaWdVYllDYWlOel95c25OMUU4dThrYXBDblFoMVcycVhQeExhc09vS3o0RmZXOWkwRUpkOFVRVWZaaFZ3YWk3NTdoTzhrUnY5NHg4R2d4MDFoemstY3pmeXBfeHlFNFhOa3pucF85T2FmOA?oc=5>

## HEADWINDS

### ASML Holding falls 9.04% in Friday's session
- Summary: ASML Holding falls 9.04% in Friday's session
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxNd09KVEw0ZUFQcm5OWFdaY0VxMTV1YW9xVFZnOU9ZbERDS2MtaWN6bFFJN3FsbXJRS2NPY2ZwMGZqVm9oSS1aUjdzZDdEc3VXZWRUT1VDZERVeVg5T0xPblFtZnUxZjBIbElKZ2tiWFpGUnRpbVlUdjF0cUx6YWNiMVQxRDU?oc=5>

### ASML Stocks Fall 2.72% as New US Rule Tightens the Chip Supply Chain It Serves
- Summary: ASML Stocks Fall 2.72% as New US Rule Tightens the Chip Supply Chain It Serves
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxOUl9OTjV3ak52UDhNeENtTG9GOElJUF9fWWNtZ0dIN1Bzb0R5QUt4WG5tZHEwbHJmM0ZvQnVaWktvaGw5OW9YUFhvSGxodC1yM1B5RVRWNXFNSGJmT2lINGFHazkwSy1zWl9ya2FtVkJmbGJwSThnTmZCeWFraDAwdXE0TG45Q0lucGc?oc=5>

### ASML slides as broader chip selloff appears to pressure shares
- Summary: ASML slides as broader chip selloff appears to pressure shares
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxON3V1T0l4QmtndUVSMHM1RzJWalliN3BIaDlFTExiQnpELUI4Y2Yyc2UzVk9XbnczcGx3RzFjN3BPN3dhTWotOG42MWQybE5iQW5NTEE3Y19ZTzFBbV9weW9tcnRocmdEdWlfY0RlT0M5Q1R3SlRwbmRxWWhFZUZQcmVLS1VUbFNnUVpaV0EzamJUZjhPU3pvd0o3WQ?oc=5>

### ASML Holding NV (ASML) Shares Fall 5.9% -- What GF Score of 97 T
- Summary: ASML Holding NV (ASML) Shares Fall 5.9% -- What GF Score of 97 T
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxNS1JVYW1TU2RuaUI5S1Z6YmE0WktQa3NKWTJtc0cycVBuMnNhTi0ydTNLeEc1eEhzUENMa3U0TG9tUmMwZW9QM3M0Q2tlRG1PSmRGZTd0UU15SjZhUlhSVEh6blJCeGpaU01PRnVBOXRNbkZaMldTQU02azBwb016RHd1RXFybk54QW94MnFCQkREZUJlUFlfOXRKLUZLc19GQkxxbF9hbzFZMTRPMW9v?oc=5>

### Why is ASML stock sliding today?
- Summary: Investors question the factors behind ASML's recent share price decline.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPUjUxQVlLLUhQRlhhbDhiazlZempiRGR3ZnNRT2JmWmdsTG9sUWpHN1UyS29rRHVEVGNQUjR4eEpGZ3BpcnFBVmV6Vnp3RDNuS0Y4ZXZCWGVRVEV4Y24wRUtyYmhWemVsRXFRa1JRdVBaRTNYNktHWi1zaVVSTTdSTTFkMUpPUDRnSExpM3hnRDh0bnluZDR2UQ?oc=5>

### ASML Holding NV Stock (ASML) Moved Down by 3.02% on Nov 17: What Investors Need To Know
- Summary: ASML shares fell 3.02% on Nov 17, prompting investors to assess reasons for the decline.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxOaHFra2Y3LUFrdVY3ejF4TnptNmhHOVFXV0Z0c1RYQ0s2eXlWYmJ1YzZfTG9aeFNyN3ZoVHhZZGZmdjhwaVZ3dTNGY3dpWUNWbEJGd1RQNklnVVE3LUJ3TGVubzIwZWxfNTdhUE1CbXAxd21lZ3JIR1I2ZE1XanRxemx1anlfU0xFN2VR?oc=5>

### Can ASML Holding (ENXTAM:ASML) Stay Cheap Enough on Cash Flow?
- Summary: Questioning ASML's ability to maintain low cash flow costs amid rising expenses.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxNN3J5SkhiTk5hdmRyUTVuREItYmxSMEszWWFCS29RTHVWZ001WTlaa2tUZ1V2c0hoVDBQNTROYTBMU2dRQWpSRzVnTXVzVnlLclZ6VnNEbDJuUUtjYlNtWWM2SkhfYVo3ZXpBSk0tS1VjTjRfUU5iZldJUl9rQ3lMMTBGbzVUZUJEUG9CV2xlSExYQ3FFRkhkOGNwLWZLdjBWN1VFSHN0NkdkYzV3cFo0NkNEbVdtWTYxQ2F2Ry1EOUpqcVVwekJBeWJJZGdpQ0tmcmdGZm9n0gHbAUFVX3lxTE1yM2NwbDYySThYQzJzTHNvYVJWbkY4dnFoZUNaVmZ1bTRlY2JCRzkyeEU0TS12RngzejdzR0I1S1FvY3JMYnBIU3E0UjlGUUhwY0ZmWVJxbXd6QWI0bTdvOVI4cjJGVFdqX043MzdhTThBX1E1NDlnVmtBQmIzdGU2bGxSRWRSRnBZME1nVlNCZFZ4cjB2M085d1VhYWljYmhoU3RXb2xsdWhmb2JLSjJVN0JOX0NzbXBSMlo4QXlNMzIzRWpmTTdBZkNqRlczTjdFNzNJRVFzMWdnVQ?oc=5>

## CATALYSTS

### ASML Stock Price Prediction: ASML lifts guidance again as the stock tests lower support
- Summary: ASML raises guidance, indicating positive outlook.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQOWY1cDlwVWExLTUwUHFTUXpTa0ZUVDMtRkxVaExqdHNWY0FZMDByWXdVaXpUTV9pTmdqN3d1S2VMTUtmR0VvRWxnWENxRnE2TUhfQktYNm5LNlFaUUZzSGlvZHVYb1FYSDRveE5YTE04S3ZmSy1KMjZHR1ZhZzF2cTdLd05aN1ZQd1dKamh5Y2FnaXk4QUpR?oc=5>

### ASML Stock Price Prediction: Strong buy analyst backdrop meets a still-fragile trend
- Summary: Analyst predicts strong buy for ASML amid fragile trend.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPWkVYLVdQT2FraHBaeEROTEJULVRkY0w0U29jR3V6dEFpZVhhVWpTZlkwNWIza2xVR01sRC04dFNtbFd1Z2NUUHZxb3piOXg5MEdza2JFS3d0OWEtYy01UFpIdF9mM2lkN1ktUEp4ekFhem42Qm5ZVEVfaDhZTG1VRTZwdnNNeVowU2x1WFJVY1hIMXVoVlZtaG1WTQ?oc=5>

### 14 ETFs Add to ASML Holding (ASML) on Nov. 18
- Summary: Fourteen ETFs increased holdings in ASML on Nov. 18.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxQdVZwbVE1aVRaU3ZtWGJ3eU9RclpRcHJhRW9BT2JxTXN0MkE0VjV1WktZeEVJaERIekhCaHh6dHBGMEZ1T0xOUXBkVGhhSk1tanlPLXk0V3c1SHkxcC02ZEtnNWJERFFzMlAzR2hLdExFbHFhTTBxRFFuaTlPQ3NEVTk4TXBGNDJF?oc=5>

### ASML Holding stock keeps Bernstein Buy rating and 2,500-euro target
- Summary: Bernstein maintains buy rating with €2,500 target for ASML.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxPQ2k2akpvZmZOUmZWU0NISUNxLWNHMDFIbUtsckd3dGI0S1Nhczd3M2pGOGgtRWVIeGN4Wjk4ZXh4LWY1aGFrTFlVQXBZSWh3ZGxmMGs2YjJxd0J2NnpObTc3SUdXV0R1UUF0YV9UUDBOdjVGSEN1T1dQTFg0NzdaOG9VQUFKR3puZU5LdjN1ZlVkbU1GSmNub045bUt3emxGbmhwWHFhMFBLV0hlaWRpREdZTk9yNXZkNDUtLWRNOE1MOHZsMWk0bi1n?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ASML** | **31.16** | **1,087.24** | **1,664.83** | **55.20** | **488,023,621,632.00 USD** | **29.86** |
| AMAT | 26.85 | 9.19 | 19.90 | 53.10 | 240,166,404,096.00 USD | 38.11 |
| LRCX | 27.31 | 16.46 | 22.26 | 54.40 | 228,935,565,312.00 USD | 31.90 |
| KLAC | 31.80 | 25.35 | 25.31 | 28.90 | 165,306,843,136.00 USD | 15.68 |

Peers fetched as_of: 2026-11-20; ASML reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-14
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-20

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

- https://news.google.com/rss/articles/CBMia0FVX3lxTFA5SzAtRE1SMDIyUEh3QjI3VEJWMmEza0xyRFYzQWdqRXRzcnFoQWpqRXltVnZKYW80aDN4WTdRNlZLZDhpTjhxaFhEQW1FMXd5RnZMeWJHTGVKZHRuSmM1NEJPWk1XVUhSaTJ3?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNbWxmYk5QUXVKSXRrRURvd1RHZ19GVDFjUzZWVUYtTGFpOFdzTGJjS1J2QmdWSGM0aVpVVHF1Nkx4dkNHWEhHZnFOenNCN3M5RlVMMWtfUFllYTEwOEhNeUlHR1RqOU95dkViM2dZSWxUbWR1TVpaQzZGbUlLekNyWENaNkdKY2sxc0tr?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxQTVdLYWNYOWdhQkJmdEhYNFViWVNlLWJ4RkVPSV9SRXQtUEQxaFE1OFFQX2tHeXk4ZU0wMTV3ZlZ0VWxzbC1pemdkM3pGOXRvakE1U3h0TjJUQUtiMkZ6UnI1RkNoeks5bkJZZVc0ZmU0R3hnRHFtRnA0NG5sRy1NSE1hWHY4VlVIMDYzRGFWYkV2bFhxc3BraGpBTnJiaHJ3U25zaDlTZUJQSWRxOEdTeGQzc2ZzdW41U0FaM0tRM0xiUFk?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxORUdqSzZ6R0h2MERHYXRacTFrbVd2dG5GZWtRRy1VLUl0bGRPUS1vWnNLQzF1Wkl0QTB6emcyaWdVYllDYWlOel95c25OMUU4dThrYXBDblFoMVcycVhQeExhc09vS3o0RmZXOWkwRUpkOFVRVWZaaFZ3YWk3NTdoTzhrUnY5NHg4R2d4MDFoemstY3pmeXBfeHlFNFhOa3pucF85T2FmOA?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxNd09KVEw0ZUFQcm5OWFdaY0VxMTV1YW9xVFZnOU9ZbERDS2MtaWN6bFFJN3FsbXJRS2NPY2ZwMGZqVm9oSS1aUjdzZDdEc3VXZWRUT1VDZERVeVg5T0xPblFtZnUxZjBIbElKZ2tiWFpGUnRpbVlUdjF0cUx6YWNiMVQxRDU?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxOUl9OTjV3ak52UDhNeENtTG9GOElJUF9fWWNtZ0dIN1Bzb0R5QUt4WG5tZHEwbHJmM0ZvQnVaWktvaGw5OW9YUFhvSGxodC1yM1B5RVRWNXFNSGJmT2lINGFHazkwSy1zWl9ya2FtVkJmbGJwSThnTmZCeWFraDAwdXE0TG45Q0lucGc?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxON3V1T0l4QmtndUVSMHM1RzJWalliN3BIaDlFTExiQnpELUI4Y2Yyc2UzVk9XbnczcGx3RzFjN3BPN3dhTWotOG42MWQybE5iQW5NTEE3Y19ZTzFBbV9weW9tcnRocmdEdWlfY0RlT0M5Q1R3SlRwbmRxWWhFZUZQcmVLS1VUbFNnUVpaV0EzamJUZjhPU3pvd0o3WQ?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxNS1JVYW1TU2RuaUI5S1Z6YmE0WktQa3NKWTJtc0cycVBuMnNhTi0ydTNLeEc1eEhzUENMa3U0TG9tUmMwZW9QM3M0Q2tlRG1PSmRGZTd0UU15SjZhUlhSVEh6blJCeGpaU01PRnVBOXRNbkZaMldTQU02azBwb016RHd1RXFybk54QW94MnFCQkREZUJlUFlfOXRKLUZLc19GQkxxbF9hbzFZMTRPMW9v?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPUjUxQVlLLUhQRlhhbDhiazlZempiRGR3ZnNRT2JmWmdsTG9sUWpHN1UyS29rRHVEVGNQUjR4eEpGZ3BpcnFBVmV6Vnp3RDNuS0Y4ZXZCWGVRVEV4Y24wRUtyYmhWemVsRXFRa1JRdVBaRTNYNktHWi1zaVVSTTdSTTFkMUpPUDRnSExpM3hnRDh0bnluZDR2UQ?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxOaHFra2Y3LUFrdVY3ejF4TnptNmhHOVFXV0Z0c1RYQ0s2eXlWYmJ1YzZfTG9aeFNyN3ZoVHhZZGZmdjhwaVZ3dTNGY3dpWUNWbEJGd1RQNklnVVE3LUJ3TGVubzIwZWxfNTdhUE1CbXAxd21lZ3JIR1I2ZE1XanRxemx1anlfU0xFN2VR?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxNN3J5SkhiTk5hdmRyUTVuREItYmxSMEszWWFCS29RTHVWZ001WTlaa2tUZ1V2c0hoVDBQNTROYTBMU2dRQWpSRzVnTXVzVnlLclZ6VnNEbDJuUUtjYlNtWWM2SkhfYVo3ZXpBSk0tS1VjTjRfUU5iZldJUl9rQ3lMMTBGbzVUZUJEUG9CV2xlSExYQ3FFRkhkOGNwLWZLdjBWN1VFSHN0NkdkYzV3cFo0NkNEbVdtWTYxQ2F2Ry1EOUpqcVVwekJBeWJJZGdpQ0tmcmdGZm9n0gHbAUFVX3lxTE1yM2NwbDYySThYQzJzTHNvYVJWbkY4dnFoZUNaVmZ1bTRlY2JCRzkyeEU0TS12RngzejdzR0I1S1FvY3JMYnBIU3E0UjlGUUhwY0ZmWVJxbXd6QWI0bTdvOVI4cjJGVFdqX043MzdhTThBX1E1NDlnVmtBQmIzdGU2bGxSRWRSRnBZME1nVlNCZFZ4cjB2M085d1VhYWljYmhoU3RXb2xsdWhmb2JLSjJVN0JOX0NzbXBSMlo4QXlNMzIzRWpmTTdBZkNqRlczTjdFNzNJRVFzMWdnVQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQOWY1cDlwVWExLTUwUHFTUXpTa0ZUVDMtRkxVaExqdHNWY0FZMDByWXdVaXpUTV9pTmdqN3d1S2VMTUtmR0VvRWxnWENxRnE2TUhfQktYNm5LNlFaUUZzSGlvZHVYb1FYSDRveE5YTE04S3ZmSy1KMjZHR1ZhZzF2cTdLd05aN1ZQd1dKamh5Y2FnaXk4QUpR?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPWkVYLVdQT2FraHBaeEROTEJULVRkY0w0U29jR3V6dEFpZVhhVWpTZlkwNWIza2xVR01sRC04dFNtbFd1Z2NUUHZxb3piOXg5MEdza2JFS3d0OWEtYy01UFpIdF9mM2lkN1ktUEp4ekFhem42Qm5ZVEVfaDhZTG1VRTZwdnNNeVowU2x1WFJVY1hIMXVoVlZtaG1WTQ?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxQdVZwbVE1aVRaU3ZtWGJ3eU9RclpRcHJhRW9BT2JxTXN0MkE0VjV1WktZeEVJaERIekhCaHh6dHBGMEZ1T0xOUXBkVGhhSk1tanlPLXk0V3c1SHkxcC02ZEtnNWJERFFzMlAzR2hLdExFbHFhTTBxRFFuaTlPQ3NEVTk4TXBGNDJF?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxPQ2k2akpvZmZOUmZWU0NISUNxLWNHMDFIbUtsckd3dGI0S1Nhczd3M2pGOGgtRWVIeGN4Wjk4ZXh4LWY1aGFrTFlVQXBZSWh3ZGxmMGs2YjJxd0J2NnpObTc3SUdXV0R1UUF0YV9UUDBOdjVGSEN1T1dQTFg0NzdaOG9VQUFKR3puZU5LdjN1ZlVkbU1GSmNub045bUt3emxGbmhwWHFhMFBLV0hlaWRpREdZTk9yNXZkNDUtLWRNOE1MOHZsMWk0bi1n?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
