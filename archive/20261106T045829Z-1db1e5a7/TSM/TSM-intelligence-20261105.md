# TSM Intelligence Report

- ticker: **TSM**
- Report as_of: **2026-11-05**
- Market data as_of: **2026-11-05**
- Quant sources: https://finance.yahoo.com/quote/TSM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TSM/key-statistics/
- AI analysis snapshot as_of: **2026-11-05**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-06T05:09:15.049262+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 0, 'ai': 13, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261105T045846Z-bde0a1fe/TSM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 10 named publishers; 3 exact duplicates; 22 HTTPS source links; largest publisher share 45.45%; oldest publication 2026-10-31

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 353.1000 |
| Return 1D (%) | -10.7770 |
| Return 1W (%) | -18.2279 |
| Return 1M (%) | -27.3158 |
| Return YTD (%) | 17.1070 |
| Return 1Y (%) | 21.5220 |
| Annualized volatility (%) | 41.1402 |
| Beta vs SPY | 2.1602 |
| Max drawdown (%) | -27.3158 |
| Sharpe (rf=0) | 0.6816 |
| Downside deviation (rf=0, %) | 28.7693 |
| Sortino (rf=0) | 0.9747 |
| Historical VaR 95% (1D, %) | 4.2423 |
| Historical ES 95% (1D, %) | 5.7594 |
| Correlation vs SPY | 0.7138 |
| Tracking error vs SPY (%) | 32.8477 |
| P/E (trailing) | 22.88 |
| P/B | 67.39 |
| EV/EBITDA | 3.17 |
| Revenue growth (%) | 50.90 |
| Forward P/E (estimate) | 15.10 |
| Gross margin (%) | 65.85 |
| Operating margin (%) | 58.66 |
| Return on equity (%) | 41.85 |
| Free cash flow yield (%) | N/A |
| MA50 | 432.3857 |
| Close vs MA50 (%) | -18.3368 |
| MA200 | 399.7760 |
| Close vs MA200 (%) | -11.6755 |
| RSI (14, Wilder) | 26.4668 |
| MACD (12,26) | -13.9421 |
| MACD signal (9) | -7.5433 |
| MACD histogram | -6.3989 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TSM': 276, 'SPY': 276}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 353.1000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -10.7770 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -18.2279 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -27.3158 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 17.1070 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 21.5220 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 41.1402 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 28.7693 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.9747 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.2423 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.7594 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.7138 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.8477 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.1602 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.3158 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.6816 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.0992 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 65.8460 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 58.6550 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 41.8550 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 22.8840 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 26.4668 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -6.3989 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -18.3368 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -11.6755 -> Clearly below the moving-average trend level.

## TAILWINDS

### Why Did Taiwan Semiconductor Manufacturing (NYSE:TSM) Shares Drop?
- Summary: Explores reasons behind recent TSM share price decline, analyzing market factors and company performance.
- Date: 2026-11-01 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxNUWxQTWdUN0RiZ1RWclVYTGU4T2plYkhPRWFNb1N0aTZGOWF6eVpGSEQxUGVLZEVDNEt3MENjSzcxcGxyRWs3b0NWX1RQSHVIRlRla1RrcG9VTVBCVzdUVXA4ekxydklCMGVTbVNrODRQLWxDUmlwdXlEX2xIdFZSSjVqRm52aEN0d1MzcW9OdWx4TmY4aHNhWVJnRU1zdWVBdDJzUUpaOTZieDQ?oc=5>

### TSMC Is Down 18%: The 2nm Ramp Should Change That (NYSE:TSM)
- Summary: TSMC’s 2nm ramp expected to lift stock after 18% decline.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQSm9ZUm5aN3VpLUFlOUd1eGRTVTJaMGdlVl9fNjgtRldkUDMxVUw5TFIzRlZuX3N4Zl9MTVBDYmNBQ3BUb1hmMVVLdThJTDVBQzF1ZzY5bGh1M2lqRkFRdnpRWEtRWDR1bF9iMGlJbm0td1BoNHVVT0M0MXhfaGpOZmNoVW04a0NVNWY0NnNKY1dQaFdLNXIwbmpKaGI?oc=5>

### The Zacks Analyst Blog Highlights Analog Devices, Taiwan Semiconductor Manufacturing, Texas Instruments and NVIDIA
- Summary: Analyst blog spotlights TSM, indicating positive analyst sentiment.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPc2FZSXhYc2dhbFFnSEZUSnh1M0tKUXB3cHpsbktOX3FaaHFPXzBCMmtxNEJ2dnZLX09UZURCSkRiSy00X2ZtbzJpblVseXpMQjg2cDhkV1Fmd2FCT0NENGI5bFBtek14RG4xMnBxbXZzWG9ac1BCSWIxaWNBWVltZm1oYVc0eHZZYmJOYU9iZ2dBb1JaRVEyZWVtRkxfSlhVNGxN?oc=5>

### Until Next Gen Computing Implodes I’ll Keep Buying Taiwan Semiconductor
- Summary: Investor bullish stance on TSM, suggesting positive market sentiment.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPQVBWRUIwVGJjVUVaczRjckFQc3QtTlFqNWk4eXlQTEk0MHhGZmMtd3NkbDkzdTlHUDBIVHREbGZRTHdqNG8tbjd4S1l5SGN3VzUxNDJOUC1JSmZBbUZqQWx6U0RrS3JlMktBRUJ4TUhNVVFTSTBpSkRBdTFvYVNYVGVQMUtQaXp3dDlCb3N3TFFhMUNQNUhmRGRmN0FZcDg?oc=5>

## HEADWINDS

### 8 ETFs Cut Taiwan Semiconductor (TSM) Holdings on Thursday
- Summary: Eight ETFs reduced TSM holdings, signaling potential market caution.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOUkY5cnBtaDA0VDRiSWpibDAzVzktck92aXA0dkR4VENJal9URjhETVo4V05yLVExVGhpaU1JTnllNUxvcGxDdnVvUzFGQmZGQURpVWNhaU5jSGUwejhCY3FKVzFOekNyYnJBeWJwaWYxYkFseWJTV3BUaWoyLTYyVk15b29mdkRoQjdZTndkdWlfa2Q2bXpDdXZGa00?oc=5>

### TSMC Stocks Move Lower as November Sales Data Face a $53.3 Billion Quarterly Hurdle
- Summary: TSM shares fell due to challenging sales outlook.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNN21ieWNIWmt1ZzdET1pneEZqX0hEbTRkSE1MTUlLbDhHYUhTRlVhM1lQbEFuSVl4YVA3Mko3YjJWREduclIyT3NUV1RuSXhSbTdwV0xZbFgxLTZoTk8wSG40ejRxUlZpRGJTc2VOV1pQUHpPcjA5dmEzTlJPMUJneUNCNzBUbHFsbzByWEJwbFU2T013d1pyRXplY3M?oc=5>

### Taiwan Semiconductor Manufacturing Co Ltd Stock (TSM) Opened Down by 5.32% on Nov 5: Key Drivers Unveiled
- Summary: TSM stock opened lower, indicating negative market reaction.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxQbmxEY0NfQTVvQVItaXItREIteFliTVVHV3NDeEJjTVliRFllSlZtdzk4NG4ySjE4dUlhc095TFRGaTFmUTYyTmdxRTNGV3dwNU00TGhVc2JSV3VrdW5GR0ZHQlppUkd1bE5FVWRlWFZ1TFhvd2YzekZreGFoa29FVXRILU4tdGxrS0E?oc=5>

## CATALYSTS

### Taiwan Semiconductor (TSM) Sees $146.2 Million in Net ETF Buying on Nov. 3
- Summary: Net ETF buying of $146.2M indicates institutional confidence in TSM.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOTHZJQ3FxWHdoRHdCWW50TmE3bzNNVGpiVDFKenBjZEdfWHpWaU16QlFCWmZaejVIcDFlNnFFY0tCQ19vZXczbURkd0p0M3h5YktDRWxhbk94R0Qwd3lldGdlazcwbzdwY1NibnRtdFJRdFhidmJnY1BUMG42VnBYZmFLclZYY0hDbDcyYUlNRGMxWUxPVnNHME9uMVFzNEk?oc=5>

### Nvidia vs. Taiwan Semiconductor: The AI Revolution Is Big Enough for Both. Here's the Better Buy.
- Summary: Analysis compares TSM and Nvidia, suggesting TSM as a strong AI chip investment.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPTDNYN2cxV2pHRDRoZm0tUEFobGpnYzBKMUtlbUgwMFF1TklfMU9ZbkpFQnZCamZYVXY4dWFpTVRWUFhmczRvSi1TRnpNOUlpMlZGNnRQaWNpYzBzY1VqaVhUeVBpR0tYOXpuTGlZejhkVlZ5d18takN1ZGdTSkV5MHFTZm1FYVdNYUl0NW9RS3JMMWVJc3MwWA?oc=5>

### Better AI Semiconductor Monopoly Stock: Taiwan Semiconductor vs. ASML
- Summary: Article positions TSM as a superior AI semiconductor monopoly over ASML.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPa1lfNFpRZnVfNGpLMmNNdlBieUY5SFkyM0d3cE9zY2NTb25XaFAyblVSSnljcXc1c1RGd05PUmI1R3g5UFBkZ01ub0trS3ZCM24zMWJpdThlZ2gtZEdicVdkNWJIRWtxc29rMlZpaXZCYm1wYl93R0RnRE1jYlFzb2I1YnVCME9sRlF2V3gwR3Q0TmR6VlZ2WnBDQTRvaEJoaWdWQg?oc=5>

### Broadcom vs. Taiwan Semiconductor: Two AI Powerhouses, but One Offers a Better Value for 2027
- Summary: Comparison of TSM and Broadcom, highlighting TSM's better 2027 value.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQQVVOOWFKcmk0YzBPd3l0Z1hMNTJqNmRIUEQ5aXVPdjlsYTlOVXFUMExFVmRtNUFDUEZqeWNvTThqQ2gzLVR2eDhvYXg5WWFDYlZ4cHNiVGVXcDRBUmotbk5aYlVEdEtqS2JGY0ZIMkxpYjRXcWs3cDVwRElxRVFHMXpnWkROdmFmX1JDclNUZjdqMGNPZmQyQW9ud3oxa19RblE?oc=5>

### TSMC’s AI Opportunity Is Expanding. Here’s the Question That Matters for Its Stock Price
- Summary: Explores TSMC's growing AI prospects and their impact on stock valuation.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxQTE91N3lqQmhwTnRpMEdqcC1WTFk1blNhSzZHVHRZOUd3dGhUNEU5TGFWZUxVb3FmNWJKazVvY095RS1nV0tGWWdJR0ZPYWxFT2MycURzeXN6aEpkeENCcFYwYXVUSjRqbS1sMl9GQWtSdGZySXdjQ0tXb1dOTmxoZXo5RGlTX016bGhxSTFoYk9VS3pnaEdDc2FMa3J5THNmNDNrVkpLSGdKOEs2ZjJ4ODVqeEUydFdtQUpZdmN1aVlXdWI2THZDZw?oc=5>

### Taiwan Semiconductor Manufacturing (NYSE:TSM) Stock Price Down 11% - Should You Sell?
- Summary: Discusses recent 11% drop in TSM stock and selling considerations.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxORkxuSFVnRUg0RGl2cTd3Q1ZxUjlWaGt0YUdCckphYkpBRGtYQmp5UVZveUZOaWdXUWhoSHNuMklEQXEwLV9ZZndiaFJMQnhmUWtNdXE2TW5NQk82emRFX3V5TmlPM1hlU2JTUUtIOFFPMjdoWWw4eC10cENRR2tqWHFNODRfRGI5cjdOakwwcXZjRm93WHNDX3NzSnFoVWZtcy13bjhjSVc5TWtDOGY5eGUwamtSMXUyOTYtcXZYQ1IzVmY5dm9fYUNLVjhsMU44R0d1QjZn?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TSM** | **22.88** | **67.39** | **3.17** | **50.90** | **1,831,344,013,312.00 USD** | **21.52** |
| UMC | 15.20 | 2.31 | -0.32 | 25.60 | 33,554,282,496.00 USD | 75.46 |
| GFS | 103.89 | 1.68 | 9.52 | 12.50 | 20,268,836,864.00 USD | 2.45 |
| INTC | N/A | 2.41 | 15.18 | 20.90 | 277,708,734,464.00 USD | 36.14 |

Peers fetched as_of: 2026-11-05; TSM reuses existing data (market data as_of: 2026-11-05); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-05

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
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPc2FZSXhYc2dhbFFnSEZUSnh1M0tKUXB3cHpsbktOX3FaaHFPXzBCMmtxNEJ2dnZLX09UZURCSkRiSy00X2ZtbzJpblVseXpMQjg2cDhkV1Fmd2FCT0NENGI5bFBtek14RG4xMnBxbXZzWG9ac1BCSWIxaWNBWVltZm1oYVc0eHZZYmJOYU9iZ2dBb1JaRVEyZWVtRkxfSlhVNGxN?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPQVBWRUIwVGJjVUVaczRjckFQc3QtTlFqNWk4eXlQTEk0MHhGZmMtd3NkbDkzdTlHUDBIVHREbGZRTHdqNG8tbjd4S1l5SGN3VzUxNDJOUC1JSmZBbUZqQWx6U0RrS3JlMktBRUJ4TUhNVVFTSTBpSkRBdTFvYVNYVGVQMUtQaXp3dDlCb3N3TFFhMUNQNUhmRGRmN0FZcDg?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOUkY5cnBtaDA0VDRiSWpibDAzVzktck92aXA0dkR4VENJal9URjhETVo4V05yLVExVGhpaU1JTnllNUxvcGxDdnVvUzFGQmZGQURpVWNhaU5jSGUwejhCY3FKVzFOekNyYnJBeWJwaWYxYkFseWJTV3BUaWoyLTYyVk15b29mdkRoQjdZTndkdWlfa2Q2bXpDdXZGa00?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNN21ieWNIWmt1ZzdET1pneEZqX0hEbTRkSE1MTUlLbDhHYUhTRlVhM1lQbEFuSVl4YVA3Mko3YjJWREduclIyT3NUV1RuSXhSbTdwV0xZbFgxLTZoTk8wSG40ejRxUlZpRGJTc2VOV1pQUHpPcjA5dmEzTlJPMUJneUNCNzBUbHFsbzByWEJwbFU2T013d1pyRXplY3M?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxQbmxEY0NfQTVvQVItaXItREIteFliTVVHV3NDeEJjTVliRFllSlZtdzk4NG4ySjE4dUlhc095TFRGaTFmUTYyTmdxRTNGV3dwNU00TGhVc2JSV3VrdW5GR0ZHQlppUkd1bE5FVWRlWFZ1TFhvd2YzekZreGFoa29FVXRILU4tdGxrS0E?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOTHZJQ3FxWHdoRHdCWW50TmE3bzNNVGpiVDFKenBjZEdfWHpWaU16QlFCWmZaejVIcDFlNnFFY0tCQ19vZXczbURkd0p0M3h5YktDRWxhbk94R0Qwd3lldGdlazcwbzdwY1NibnRtdFJRdFhidmJnY1BUMG42VnBYZmFLclZYY0hDbDcyYUlNRGMxWUxPVnNHME9uMVFzNEk?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPTDNYN2cxV2pHRDRoZm0tUEFobGpnYzBKMUtlbUgwMFF1TklfMU9ZbkpFQnZCamZYVXY4dWFpTVRWUFhmczRvSi1TRnpNOUlpMlZGNnRQaWNpYzBzY1VqaVhUeVBpR0tYOXpuTGlZejhkVlZ5d18takN1ZGdTSkV5MHFTZm1FYVdNYUl0NW9RS3JMMWVJc3MwWA?oc=5
- https://news.google.com/rss/articles/CBMihwJBVV95cUxNaWtmM0FIRDYwcnVxZlVYOFk3OUI1Y3pLbzlhWURKSl94b1NHQldCaUdMN1pjclNQUEd6Sko1OXBGUGdpRk9ITVNPeWlzMVk5VDc4VkUtWVJtQ1B4VTVVS1RpaXRIbkxSVFdrNFFjdXZ3YnFyazJ1ZDU1ZmtTTmZYRlJuWkFvQ0M5N2kyUmJ4U09zSVFPZ2lEUFRDRXN1b04zbm5HLTRMMTZJTkpSWXEza1ZDZ0htMW80cExPeS1hclhCVXRnNEVseVg4WXJOUjY0OE00QXRHWE1sdnhtcHdQX3Y5cGYtM2JaRV8wenJkMGxLZzN1OE1RQXhscnVCQ0cwdkhfRG1FYw?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPa1lfNFpRZnVfNGpLMmNNdlBieUY5SFkyM0d3cE9zY2NTb25XaFAyblVSSnljcXc1c1RGd05PUmI1R3g5UFBkZ01ub0trS3ZCM24zMWJpdThlZ2gtZEdicVdkNWJIRWtxc29rMlZpaXZCYm1wYl93R0RnRE1jYlFzb2I1YnVCME9sRlF2V3gwR3Q0TmR6VlZ2WnBDQTRvaEJoaWdWQg?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOTGltQ1laWTRjdVRfcGJwWTZHVkE0Y0J5MlJtd015amczUnFLLWs2c1RNSXNsdHppUlI4WHp3MHdCdWtYOVVQVEZScWRaenhtdzl6eWJ1TEpOaEJkWWRyaS1PZ1lGTkVZVEVxTjN1T3NLRHBRLTRac2w4YTJGOU4ydmZWUGZDb0xTODBPeXJmZkh3QkFJQjZoUg?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQQVVOOWFKcmk0YzBPd3l0Z1hMNTJqNmRIUEQ5aXVPdjlsYTlOVXFUMExFVmRtNUFDUEZqeWNvTThqQ2gzLVR2eDhvYXg5WWFDYlZ4cHNiVGVXcDRBUmotbk5aYlVEdEtqS2JGY0ZIMkxpYjRXcWs3cDVwRElxRVFHMXpnWkROdmFmX1JDclNUZjdqMGNPZmQyQW9ud3oxa19RblE?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxQTE91N3lqQmhwTnRpMEdqcC1WTFk1blNhSzZHVHRZOUd3dGhUNEU5TGFWZUxVb3FmNWJKazVvY095RS1nV0tGWWdJR0ZPYWxFT2MycURzeXN6aEpkeENCcFYwYXVUSjRqbS1sMl9GQWtSdGZySXdjQ0tXb1dOTmxoZXo5RGlTX016bGhxSTFoYk9VS3pnaEdDc2FMa3J5THNmNDNrVkpLSGdKOEs2ZjJ4ODVqeEUydFdtQUpZdmN1aVlXdWI2THZDZw?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxORkxuSFVnRUg0RGl2cTd3Q1ZxUjlWaGt0YUdCckphYkpBRGtYQmp5UVZveUZOaWdXUWhoSHNuMklEQXEwLV9ZZndiaFJMQnhmUWtNdXE2TW5NQk82emRFX3V5TmlPM1hlU2JTUUtIOFFPMjdoWWw4eC10cENRR2tqWHFNODRfRGI5cjdOakwwcXZjRm93WHNDX3NzSnFoVWZtcy13bjhjSVc5TWtDOGY5eGUwamtSMXUyOTYtcXZYQ1IzVmY5dm9fYUNLVjhsMU44R0d1QjZn?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
