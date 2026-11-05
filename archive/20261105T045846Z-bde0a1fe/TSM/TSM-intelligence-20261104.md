# TSM Intelligence Report

- ticker: **TSM**
- Report as_of: **2026-11-04**
- Market data as_of: **2026-11-04**
- Quant sources: https://finance.yahoo.com/quote/TSM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TSM/key-statistics/
- AI analysis snapshot as_of: **2026-11-04**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-05T05:22:17.907967+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 4, 'ai': 8, 'unknown': 0, 'irrelevant': 10})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261104T044411Z-6b13f9ec/TSM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 9 named publishers; 3 exact duplicates; 22 HTTPS source links; largest publisher share 22.73%; oldest publication 2026-10-29

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 395.7500 |
| Return 1D (%) | -2.2357 |
| Return 1W (%) | -9.9565 |
| Return 1M (%) | -16.2930 |
| Return YTD (%) | 31.2520 |
| Return 1Y (%) | 36.0104 |
| Annualized volatility (%) | 39.6563 |
| Beta vs SPY | 2.1236 |
| Max drawdown (%) | -21.5466 |
| Sharpe (rf=0) | 0.9764 |
| Downside deviation (rf=0, %) | 26.6661 |
| Sortino (rf=0) | 1.4521 |
| Historical VaR 95% (1D, %) | 4.2163 |
| Historical ES 95% (1D, %) | 5.2559 |
| Correlation vs SPY | 0.6875 |
| Tracking error vs SPY (%) | 32.2078 |
| P/E (trailing) | 25.65 |
| P/B | 75.53 |
| EV/EBITDA | 3.66 |
| Revenue growth (%) | 50.90 |
| Forward P/E (estimate) | 16.89 |
| Gross margin (%) | 65.85 |
| Operating margin (%) | 58.66 |
| Return on equity (%) | 41.85 |
| Free cash flow yield (%) | N/A |
| MA50 | 433.6552 |
| Close vs MA50 (%) | -8.7409 |
| MA200 | 399.6284 |
| Close vs MA200 (%) | -0.9705 |
| RSI (14, Wilder) | 36.4079 |
| MACD (12,26) | -9.5779 |
| MACD signal (9) | -5.9436 |
| MACD histogram | -3.6344 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TSM': 275, 'SPY': 275}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 395.7500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.2357 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -9.9565 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -16.2930 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 31.2520 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 36.0104 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 39.6563 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.6661 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.4521 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.2163 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.2559 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6875 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.2078 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.1236 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -21.5466 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9764 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.8877 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 65.8460 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 58.6550 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 41.8550 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 25.6481 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 36.4079 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.6344 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -8.7409 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -0.9705 -> Slightly below the moving-average trend level.

## TAILWINDS

### Why Did Taiwan Semiconductor Manufacturing (NYSE:TSM) Shares Drop?
- Summary: Explores reasons behind recent TSM share price decline, analyzing market factors and company performance.
- Date: 2026-11-01 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxNUWxQTWdUN0RiZ1RWclVYTGU4T2plYkhPRWFNb1N0aTZGOWF6eVpGSEQxUGVLZEVDNEt3MENjSzcxcGxyRWs3b0NWX1RQSHVIRlRla1RrcG9VTVBCVzdUVXA4ekxydklCMGVTbVNrODRQLWxDUmlwdXlEX2xIdFZSSjVqRm52aEN0d1MzcW9OdWx4TmY4aHNhWVJnRU1zdWVBdDJzUUpaOTZieDQ?oc=5>

### TSMC Is Down 18%: The 2nm Ramp Should Change That (NYSE:TSM)
- Summary: TSMC’s 2nm ramp expected to lift stock after 18% decline.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQSm9ZUm5aN3VpLUFlOUd1eGRTVTJaMGdlVl9fNjgtRldkUDMxVUw5TFIzRlZuX3N4Zl9MTVBDYmNBQ3BUb1hmMVVLdThJTDVBQzF1ZzY5bGh1M2lqRkFRdnpRWEtRWDR1bF9iMGlJbm0td1BoNHVVT0M0MXhfaGpOZmNoVW04a0NVNWY0NnNKY1dQaFdLNXIwbmpKaGI?oc=5>

### Here’s What a $10,000 Investment in TSMC Stock Will Be Worth by 2030
- Summary: Projected $10,000 TSMC investment could grow significantly by 2030, indicating strong long‑term potential.
- Date: 2026-10-30 | Impact: high | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxOU1hNeUxiYWNYT2JHOHRZVm9JOEx2RmtSU1I3SUV6emRrUmgzUmtvR2k0clBENDlDRTF6SEtIQTRGOVZ4Tm9wTVlDam01bklqRzljU1U0akEzNW5iOGY0cmZVU21QTWJkMlZvTVBHWVpVanhlTVFRQXAteGJ5SzlLcG9ublZqQkw1SlRVZ1BjUjkxWl92dXJvT3VaWWQ2R2lhU29BOVpBUGRXMnNzWGpsakRVRQ?oc=5>

## HEADWINDS

### Taiwan Semiconductor Manufacturing (NYSE:TSM) Stock Price Down 2.5% - Here's Why
- Summary: Taiwan Semiconductor Manufacturing (NYSE:TSM) Stock Price Down 2.5% - Here's Why
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxPTEJ0aVBPTUtYQTR1Zm9wc29zQjZ3T1V6SzRscDV4NEFNLW5PYS1JTXBjaHE3cEFTVTlRWXdWaEg3OEtvcnotejh4VlR5VUJYMDBfdzhRck84MlZMVkYyN3Q1Nl84aklDa0R2cFdiSl9lVXRKSkxPXzhRcXh2VldLcWV2RW5SOE05Tlo5c1lLcnpEUUZVRjZWcVBSdmFNNk9Ya3h2THJLVUlXMlV6bE1ELTNFd3pNTW5ienJyb0NkOUhkZHMwRldybkUzNGxoQQ?oc=5>

### Taiwan Semiconductor Manufacturing Co Ltd (TSM) Stock Down 6.0% but Still Overvalued -- GF Score: 98/100
- Summary: Taiwan Semiconductor Manufacturing Co Ltd (TSM) Stock Down 6.0% but Still Overvalued -- GF Score: 98/100
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxNanJjTkhQMUhmbFpvaGxmRzhsWTdNVDl2T1R2Ml82b0o2NGV3MjRhTy1neFlDSjR5dUlxSlg0c3RWUkhSWEY5UDI3UmFFXzk0cFNHOVRoUXdUUkh1MWNfbEwzMFhVRmpKVHJSbElOMm5JODdVcHhTMDVncURVQnVBT0ZaVlIwemc1ZTZKVDllSGVha3otWjVELVdBbHhzYWt2dTlrbFNIcUVnT19nZHhzbkVucmhPRmhLWkRmdi1GOEZlMUpCWEVuaVo2ZjZWMXc?oc=5>

### 8 ETFs Cut Taiwan Semiconductor (TSM) Holdings on Thursday
- Summary: Eight ETFs reduced TSM holdings, signaling potential market caution.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOUkY5cnBtaDA0VDRiSWpibDAzVzktck92aXA0dkR4VENJal9URjhETVo4V05yLVExVGhpaU1JTnllNUxvcGxDdnVvUzFGQmZGQURpVWNhaU5jSGUwejhCY3FKVzFOekNyYnJBeWJwaWYxYkFseWJTV3BUaWoyLTYyVk15b29mdkRoQjdZTndkdWlfa2Q2bXpDdXZGa00?oc=5>

## CATALYSTS

### Taiwan Semiconductor Manufacturing Company Ltd. $TSM Stock: Provenance Wealth Advisors LLC Increases Stake
- Summary: Taiwan Semiconductor Manufacturing Company Ltd. $TSM Stock: Provenance Wealth Advisors LLC Increases Stake
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi9wFBVV95cUxPSU9DNTV1QXk3clN0bC1rSFp3MU1FbW9tQ2pnRjZZeXE3ckNOZ3NKN0xwM0M4WHVpbnJIQW91LTVDdlVmcUhBTTRpZjN2cVlwR2FzUnpXQURRWWJaWk9kMnlPNFozRU45c0hvM0JDbGFqQkJQcjVyOGV4X1FxTEk1YlpYMVhtejN4LTlOTklhc0hWWXo0MXFaZTRKN2NCLTN0TzVKb0lUZjlVQ1lSYlFPMk83MlBqVUdVc1NTOXhUb0tSaXFSZW1UTE1OaHozSXNiYTdnMllYVjd5U0VpbVFlOHNwbVk2RXVKMnRSYm05ZS1ra1cwUy13?oc=5>

### Taiwan Semiconductor Manufacturing Company Ltd. $TSM Stock Sold by Factory Mutual Insurance Co.
- Summary: Taiwan Semiconductor Manufacturing Company Ltd. $TSM Stock Sold by Factory Mutual Insurance Co.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi6AFBVV95cUxPTzdWb1pqYXQxM3R1bS11eHhvVDdXNG9iZG15VmQzaTZIbjNoX0E4NUFRbmtTa2d0NHpIYm9ZRWNOWlN0V3RMci1xc0o5MS1HUjNyMzM2bl9LZ1Q0TTRkVXBJM2hhRzRNeWw5dUU3R1VsbzlvRUt2T0dYV0tfVk1NU29iQTRxQ29HbFFfOURxS0oySU5sekk2NTRpekdjbEdSNTNSd3hGSTc5NTJsejRmXzFKanVzZkkteWJUOFZqMWtpb281Mkp3WlZXU0xyVVlhLTBEWFhtUmVzenk1YjVmYUFOR3ctTmlD?oc=5>

### TSM Stock Price — TSMC Chart
- Summary: Chart showing TSM stock price movements.
- Date: 2026-11-03 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiWEFVX3lxTE1tRVZtNDVDbFpBRlpSbnY4LWY1X0NpUF8wejJBVU1EOEpDZDh1SmYtR3hmblhjYWk0ZzV5UkcwTW9MWlhWVGt4MFZMX3l1T092VC1QNWFxR08?oc=5>

### Taiwan Semiconductor Manufacturing Company Ltd. $TSM Stock: Third View Private Wealth LLC Boosts Stake
- Summary: Third View Private Wealth LLC increased its stake in TSM, signaling confidence in the company.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi8gFBVV95cUxObFRoVHBDSkpVOUp0SWNBQm15ZWJVV0FfMWpVcmQ0ZlFnenN5RHhDSjN6dVBKb3pqMzc1MGl2NGJkeVRtSzFpcWZDclZoWTQwa3ZTZTFyUHFjYW8tRVlJS2FaQ3FZUG1jaWJLRUdZODd5ZTdBTFpOTUFOMkhtQk1sT09ELVBZVjhHTUNxdzJkbzJLRjNQVVNDaUlEc3lJTDdLUFJKUktqRWhHOFYzcWFFRlVJalNPS21hdUZ0UmN4Y21DRmdPa01DVFM4a2dCYUQxVVZKMThRcWZHT2REek1Ganc1d2VsVV9ick9GTUdqSEJJZw?oc=5>

### Cathie Wood Just Sold $24.6 Million of Surging Chip Stock
- Summary: Cathie Wood sold $24.6M of TSM shares, indicating a divestment decision.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxNTHFaVXFoWTRsSDBsMDE5Rzl2ODZRVEdJeHNCY1FNNmU1UVBFb2U0WG9RTGEtX3hBbGpiN3gtZXR0V0VUMlZqUjdYQ0VYOVVuRDNhWGVKMDFZZXNKV2ZrY3BUUTkxWWxkLUxqbEFib1o2aG56UXBxR0Q3Y0RITTJxV2dtdjNab21TbTA3ZlFPWUpURzExdWFOUHNFM0Z6SUNUbEJPanRDY2M4VE5CdlV6VVBaWF9IM3c?oc=5>

### 1,409 Taiwan Semiconductor Manufacturing Company Ltd. $TSM Shares Sold by Torray Investment Partners LLC
- Summary: Torray Investment Partners LLC sold 1,409 TSM shares, reflecting a portfolio adjustment.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi9AFBVV95cUxNMnpqbXBib2kwQkE4RHFHZG1qOVJBSkJnVEZnbW13U294M1FqWGNVYTBVSHc0aGRGaDRILXRpRTVlVHg2bmJJbzQ4S1FVcDNfNHFPMmlNcURTa2Q4WWEzNGJZaUNnQjV3MzdscmIwdWNYcVFlYmllRHlzSGVmS196SS1jYVp2WlRSU19LYm9PWkc5VlE1VUJMbGJKU0QxMnJvY0RKZmFXN3Nvc2JXSXdqMWZkZ1ZJbG1FQm9fa2E2dFhmaUZDN1NOQXV2ZGNzR29GcHYtRE5GM3pIV2NCSVdOR1RjeEthaDlZYlo5UUhVYVAtOHFq?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TSM** | **25.65** | **75.53** | **3.66** | **50.90** | **2,052,547,018,752.00 USD** | **36.01** |
| UMC | 15.44 | 2.77 | -0.27 | 25.60 | 40,275,169,280.00 USD | 115.03 |
| GFS | 115.26 | 1.88 | 11.57 | 5.80 | 22,486,267,904.00 USD | 17.66 |
| INTC | N/A | 2.69 | 16.85 | 20.90 | 309,705,048,064.00 USD | 57.36 |

Peers fetched as_of: 2026-11-04; TSM reuses existing data (market data as_of: 2026-11-04); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

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

- https://news.google.com/rss/articles/CBMiqwFBVV95cUxNUWxQTWdUN0RiZ1RWclVYTGU4T2plYkhPRWFNb1N0aTZGOWF6eVpGSEQxUGVLZEVDNEt3MENjSzcxcGxyRWs3b0NWX1RQSHVIRlRla1RrcG9VTVBCVzdUVXA4ekxydklCMGVTbVNrODRQLWxDUmlwdXlEX2xIdFZSSjVqRm52aEN0d1MzcW9OdWx4TmY4aHNhWVJnRU1zdWVBdDJzUUpaOTZieDQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQSm9ZUm5aN3VpLUFlOUd1eGRTVTJaMGdlVl9fNjgtRldkUDMxVUw5TFIzRlZuX3N4Zl9MTVBDYmNBQ3BUb1hmMVVLdThJTDVBQzF1ZzY5bGh1M2lqRkFRdnpRWEtRWDR1bF9iMGlJbm0td1BoNHVVT0M0MXhfaGpOZmNoVW04a0NVNWY0NnNKY1dQaFdLNXIwbmpKaGI?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxOU1hNeUxiYWNYT2JHOHRZVm9JOEx2RmtSU1I3SUV6emRrUmgzUmtvR2k0clBENDlDRTF6SEtIQTRGOVZ4Tm9wTVlDam01bklqRzljU1U0akEzNW5iOGY0cmZVU21QTWJkMlZvTVBHWVpVanhlTVFRQXAteGJ5SzlLcG9ublZqQkw1SlRVZ1BjUjkxWl92dXJvT3VaWWQ2R2lhU29BOVpBUGRXMnNzWGpsakRVRQ?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxPTEJ0aVBPTUtYQTR1Zm9wc29zQjZ3T1V6SzRscDV4NEFNLW5PYS1JTXBjaHE3cEFTVTlRWXdWaEg3OEtvcnotejh4VlR5VUJYMDBfdzhRck84MlZMVkYyN3Q1Nl84aklDa0R2cFdiSl9lVXRKSkxPXzhRcXh2VldLcWV2RW5SOE05Tlo5c1lLcnpEUUZVRjZWcVBSdmFNNk9Ya3h2THJLVUlXMlV6bE1ELTNFd3pNTW5ienJyb0NkOUhkZHMwRldybkUzNGxoQQ?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxNanJjTkhQMUhmbFpvaGxmRzhsWTdNVDl2T1R2Ml82b0o2NGV3MjRhTy1neFlDSjR5dUlxSlg0c3RWUkhSWEY5UDI3UmFFXzk0cFNHOVRoUXdUUkh1MWNfbEwzMFhVRmpKVHJSbElOMm5JODdVcHhTMDVncURVQnVBT0ZaVlIwemc1ZTZKVDllSGVha3otWjVELVdBbHhzYWt2dTlrbFNIcUVnT19nZHhzbkVucmhPRmhLWkRmdi1GOEZlMUpCWEVuaVo2ZjZWMXc?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOUkY5cnBtaDA0VDRiSWpibDAzVzktck92aXA0dkR4VENJal9URjhETVo4V05yLVExVGhpaU1JTnllNUxvcGxDdnVvUzFGQmZGQURpVWNhaU5jSGUwejhCY3FKVzFOekNyYnJBeWJwaWYxYkFseWJTV3BUaWoyLTYyVk15b29mdkRoQjdZTndkdWlfa2Q2bXpDdXZGa00?oc=5
- https://news.google.com/rss/articles/CBMi9wFBVV95cUxPSU9DNTV1QXk3clN0bC1rSFp3MU1FbW9tQ2pnRjZZeXE3ckNOZ3NKN0xwM0M4WHVpbnJIQW91LTVDdlVmcUhBTTRpZjN2cVlwR2FzUnpXQURRWWJaWk9kMnlPNFozRU45c0hvM0JDbGFqQkJQcjVyOGV4X1FxTEk1YlpYMVhtejN4LTlOTklhc0hWWXo0MXFaZTRKN2NCLTN0TzVKb0lUZjlVQ1lSYlFPMk83MlBqVUdVc1NTOXhUb0tSaXFSZW1UTE1OaHozSXNiYTdnMllYVjd5U0VpbVFlOHNwbVk2RXVKMnRSYm05ZS1ra1cwUy13?oc=5
- https://news.google.com/rss/articles/CBMi6AFBVV95cUxPTzdWb1pqYXQxM3R1bS11eHhvVDdXNG9iZG15VmQzaTZIbjNoX0E4NUFRbmtTa2d0NHpIYm9ZRWNOWlN0V3RMci1xc0o5MS1HUjNyMzM2bl9LZ1Q0TTRkVXBJM2hhRzRNeWw5dUU3R1VsbzlvRUt2T0dYV0tfVk1NU29iQTRxQ29HbFFfOURxS0oySU5sekk2NTRpekdjbEdSNTNSd3hGSTc5NTJsejRmXzFKanVzZkkteWJUOFZqMWtpb281Mkp3WlZXU0xyVVlhLTBEWFhtUmVzenk1YjVmYUFOR3ctTmlD?oc=5
- https://news.google.com/rss/articles/CBMiWEFVX3lxTE1tRVZtNDVDbFpBRlpSbnY4LWY1X0NpUF8wejJBVU1EOEpDZDh1SmYtR3hmblhjYWk0ZzV5UkcwTW9MWlhWVGt4MFZMX3l1T092VC1QNWFxR08?oc=5
- https://news.google.com/rss/articles/CBMi8gFBVV95cUxObFRoVHBDSkpVOUp0SWNBQm15ZWJVV0FfMWpVcmQ0ZlFnenN5RHhDSjN6dVBKb3pqMzc1MGl2NGJkeVRtSzFpcWZDclZoWTQwa3ZTZTFyUHFjYW8tRVlJS2FaQ3FZUG1jaWJLRUdZODd5ZTdBTFpOTUFOMkhtQk1sT09ELVBZVjhHTUNxdzJkbzJLRjNQVVNDaUlEc3lJTDdLUFJKUktqRWhHOFYzcWFFRlVJalNPS21hdUZ0UmN4Y21DRmdPa01DVFM4a2dCYUQxVVZKMThRcWZHT2REek1Ganc1d2VsVV9ick9GTUdqSEJJZw?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxNTHFaVXFoWTRsSDBsMDE5Rzl2ODZRVEdJeHNCY1FNNmU1UVBFb2U0WG9RTGEtX3hBbGpiN3gtZXR0V0VUMlZqUjdYQ0VYOVVuRDNhWGVKMDFZZXNKV2ZrY3BUUTkxWWxkLUxqbEFib1o2aG56UXBxR0Q3Y0RITTJxV2dtdjNab21TbTA3ZlFPWUpURzExdWFOUHNFM0Z6SUNUbEJPanRDY2M4VE5CdlV6VVBaWF9IM3c?oc=5
- https://news.google.com/rss/articles/CBMi9AFBVV95cUxNMnpqbXBib2kwQkE4RHFHZG1qOVJBSkJnVEZnbW13U294M1FqWGNVYTBVSHc0aGRGaDRILXRpRTVlVHg2bmJJbzQ4S1FVcDNfNHFPMmlNcURTa2Q4WWEzNGJZaUNnQjV3MzdscmIwdWNYcVFlYmllRHlzSGVmS196SS1jYVp2WlRSU19LYm9PWkc5VlE1VUJMbGJKU0QxMnJvY0RKZmFXN3Nvc2JXSXdqMWZkZ1ZJbG1FQm9fa2E2dFhmaUZDN1NOQXV2ZGNzR29GcHYtRE5GM3pIV2NCSVdOR1RjeEthaDlZYlo5UUhVYVAtOHFq?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
