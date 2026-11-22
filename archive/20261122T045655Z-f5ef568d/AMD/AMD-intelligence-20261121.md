# AMD Intelligence Report

- ticker: **AMD**
- Report as_of: **2026-11-21**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/AMD/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMD/key-statistics/
- AI analysis snapshot as_of: **2026-11-21**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-22T05:01:46.828384+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 2, 'ai': 15, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261121T053104Z-422ce34b/AMD** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 10 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 43.48%; oldest publication 2026-11-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 424.3900 |
| Return 1D (%) | -13.2464 |
| Return 1W (%) | -20.5351 |
| Return 1M (%) | -20.6362 |
| Return YTD (%) | 98.1649 |
| Return 1Y (%) | 105.9946 |
| Annualized volatility (%) | 74.7962 |
| Beta vs SPY | 3.4249 |
| Max drawdown (%) | -37.7290 |
| Sharpe (rf=0) | 1.3448 |
| Downside deviation (rf=0, %) | 49.5199 |
| Sortino (rf=0) | 2.0313 |
| Historical VaR 95% (1D, %) | 6.9676 |
| Historical ES 95% (1D, %) | 10.1271 |
| Correlation vs SPY | 0.6546 |
| Tracking error vs SPY (%) | 66.3253 |
| P/E (trailing) | 90.68 |
| P/B | 10.18 |
| EV/EBITDA | 61.88 |
| Revenue growth (%) | 44.70 |
| Forward P/E (estimate) | 24.06 |
| Gross margin (%) | 56.00 |
| Operating margin (%) | 17.82 |
| Return on equity (%) | 11.96 |
| Free cash flow yield (%) | 1.05 |
| MA50 | 553.0976 |
| Close vs MA50 (%) | -23.2703 |
| MA200 | 429.7861 |
| Close vs MA200 (%) | -1.2555 |
| RSI (14, Wilder) | 38.4158 |
| MACD (12,26) | -16.2917 |
| MACD signal (9) | -12.8229 |
| MACD histogram | -3.4688 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMD': 287, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 424.3900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -13.2464 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -20.5351 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -20.6362 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 98.1649 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 105.9946 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 74.7962 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 49.5199 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.0313 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 6.9676 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 10.1271 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6546 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 66.3253 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.4249 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -37.7290 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.3448 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 24.0608 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 56.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 17.8210 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 11.9600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.0474 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 90.6816 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 38.4158 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.4688 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -23.2703 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -1.2555 -> Slightly below the moving-average trend level.

## TAILWINDS

### AMD’s Data Center Sales Jumped 97%. Is the Stock a Buy?
- Summary: AMD’s Data Center Sales Jumped 97%. Is the Stock a Buy?
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOeGVYdV9Ga0hQQzdiZ0NxZ1l4Nk1aZ2stV0N3M0RvLVY0U2FKM1M4b1BfVnMzSWk0Wm5LRkJIN3ItSkJoVV9Ia2UyM2t6QUloOFctcXJ4ajViTWpNUUl4V2V4YTZzUGdfLUkyN2NIQ1paeFVlcThHcEFveEduaDlueFdjSDd1RGcyYkpCVWMxM2N1UXZtWVlBaw?oc=5>

### This Is Incredible News for AMD Stock Investors (Hint: It’s Bad News for Intel)
- Summary: Positive news for AMD investors, suggesting a favorable market shift against Intel.
- Date: 2026-11-19 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQb1ZvQ1FxeEdyXzBkd3hNZ0ZydlpCdkI3T3gwR01QSHNfUHNaNDFBRTZaMmtyc2dUa0NhYXlQMXNybXEySDRzdWZFd2hOY2hOU3RoREVRcTEyT1ZKc1hBYlI1ZnMwS2NPVVZER3IxOHZZSE5zRWdfMmdwZ3dnT2oxM0M4bzFYamFsU2Y0cEhlMGE1UWJPMVhJMThFbkdnRllLa3c?oc=5>

### AMD (AMD) Stock Could Be 12% Undervalued After AI Chip Progress News
- Summary: AMD may be undervalued by 12% following AI chip advancements.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMie0FVX3lxTFBnUU5wSm1najNrS3pqZDAxUlQyOHVtaGFBdnBBQlNUUmlobG9XT290d2Zha2ppSVgtU2E5amhwSHFTRkZ5RzV1ZXJnYmNHTGFET0JmeHZVVWthbm5nbF9HR181djRCZkQtQVVvdHNxU1RZcWlCZW5VQktoVQ?oc=5>

### AMD vs. Nvidia: Which AI Chip Stock Is the Better Buy on the Dip?
- Summary: Comparative analysis of AMD and Nvidia stocks during a dip.
- Date: 2026-11-21 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxNdDJjTUItNjhtVWNMb0FRa3hKZThKYXNDbWxweWdZTXVtUXBCalAwMC15d3M2LU1Ta216M3poTmo4eTVyQ0xqMGFTX2VHd0Z3LW9EZFJEaWVDaEtVdXFsWTBReFk4dlI2RE9BQVJDb0Z0a3A3dGpGNGtxaWlvdU93VW1TSy1OVFlIYkV3UkNDYk5mZnBpQWUxMzF5cm1HT2FJejlEY1hmYVU?oc=5>

## HEADWINDS

### Why Is AMD Stock Falling on Friday?
- Summary: Investors concerned about recent performance and market conditions, leading to a decline in AMD shares.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPakd6RUtYYTBuV2dfQVE4SWpBendrV1B4UmdxOUt4R2djNzVkbWo5VV9qTmZ5YjRHaUJwSXhHb0dZMG5RMTJGQVNhcWZyT1prN3JFdFBWN1JWQ0twS3RDc3ZDVjVWbDltUVZWOURuTHZ6V1MxRkhGN3NCZ1V2N1NRX0FPUnRPamJOVU1EYnVRWkRXR2N2TWZUdnJ4WQ?oc=5>

### Is NVIDIA’s Turmoil Advanced Micro Devices’ (AMD) Biggest Opening Yet?
- Summary: Nvidia turmoil may negatively impact AMD’s market performance.
- Date: 2026-11-17 | Impact: low | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPeE4zN25uZ3h5c01LT2hKdFVrSncwaTlUWXpTUmNKZnpBZnB6b01JQTFIaW9IRms3NFVMS1lTLWZPNWVFajh5Vl90WXdjdEwxX29aTWhjLWtLeExZelZXRkpaZmV3VzVzakN2VzgwRjFkbi1BZkVESTlXZGx5d05LYm1SNnZRdlRhUW9NQ2d6UEh1R05TRFA0Q1MxcmJ6LXFmclRVbg?oc=5>

## CATALYSTS

### Advanced Micro Devices (AMD) Closes $8.2 Billion World Labs Acquisition
- Summary: Advanced Micro Devices (AMD) Closes $8.2 Billion World Labs Acquisition
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxQZkNtckk5TW0wbDQzTkxSU3JQNVJROTBBdE5OMjlyWDZMcHR5VE1BemMxOFZxSXNZR2dQS2JNWDRSN2VJYkxDU1FTLVlielg5SW5IOXdibDEzcmNzZU16ekxGNkhoWDRnX0xRcWVzaFBpUmpRMFRmSllnM2pfaGRzYWFXSl9nRmlzUUE?oc=5>

### AMD Shares Slump After Shortseller Raises China Concerns
- Summary: Shortseller’s China concerns triggered a sharp decline in AMD shares.
- Date: 2026-11-19 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxPbkp6di1ZYkMzQlhjTmkxbHFwNzIzLWMyc3NKXzBqSV9hZ05wODRRYUhjYl9pSmIyNENPaHpXWmlScUpaYXhfT3AyQ1hKYVhWZnhHRVp1a0g2dkVGWmpYa2lXdmdjaE1TUTQwbFlyNjJVNjVkRmlIbWt3WHhWYjNJWXNGSG9RcFkwYUFRZzdYMVNpQXVnZllfU0ZlZEc0QnFsQ1RnWk9tUmc5d2luUVVSaWRKMA?oc=5>

### Why Is Advanced Micro Devices Stock Rising Today?
- Summary: Explores reasons behind AMD's recent price increase.
- Date: 2026-11-18 | Impact: low | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPUkNPRlQ0VWdjd0dOeVdRWVVDZlUwOTg0YkFDRE9UXzJHOWFuVEVFMmIwU2xOSl9Ibi1vMTFPX0liLU80SzdaeVdWLTgtamhuSS1nMlV6QjZBMVN2N1ZjN2xqYmR3NHlWYm5kY1l6a0lQUGo1UVdycjNhbzV5cmZjYlRGNGxvTVpDRXpRMGpRWkxkaVA1bm9KcTBBaTg4QQ?oc=5>

### Is AMD the Stock to Buy With Nvidia in Limbo?
- Summary: Investors weigh AMD as a potential buy while Nvidia faces uncertainty.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQTURWcmloUmY4UlNoemdLU2V1dUhhZzJKaGFDbEFNQnk4dmFVQWpvUW5lYUJPQ2kwUTJhY3ljcWFha21yLS02SThucmEzMVdLOFZ4bm5rc1lCOHRVanBnVERUMmxYME8yT2hSZ2hnN3NJZUxqVnlSY2FuU0w0bVI3cVRyYm1aNlNQWDYwYXpVR0FZVmE5N1E?oc=5>

### Why AMD Stock Was Plunging on Thursday
- Summary: AMD shares fell sharply on Thursday, prompting concerns about valuation.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxOX3BLVnZVVDhkQ1I2LTdZRjZJdHBWU2dKVTlOS2U5bmNaTms4SUY1WndRRmF0TDcyN0VuanVjcFhyQnRyWVlOMGQzS21rSnJCUnRoalZqc3M5N3lwSGQ5S2hjN1BMV3BYTlhNcDBvZlZ1X1dfT2JqMmpXN05fYzJJWm5wTERHME1s?oc=5>

### Is AMD Stock a Buy Amid the Uncertainty Around Nvidia?
- Summary: Analysts discuss AMD as a buy amid Nvidia's uncertain outlook.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQV0RabkRYQjV0NTd3aHhnNzhPN0pWbGE3WklWaWNsNHNqdG8tVGNpS0JzSGNXS09IcmNwQXVRUHAwVHphVXh0QzBRWFJidGZwaWgxaWdmQTRQWl9vN0NNbE1aWmtkSzBIZzNzMVRIX0dMRjZvaE1tbi1uSGJtdEJLZXY4SjNfWi1HS2pLU0NTWS1PUFpOZG5KWDFqUQ?oc=5>

### Why Is AMD Stock Rising Overnight?
- Summary: AMD shares increased overnight, indicating positive market sentiment.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOOERqVlNqV0JSeWxUeTJDTVVBeWlsV1pKaVFNVEI4dXZkTWc1REdueTJRenlWay1vbW9SbVhBUE5wQUk1b1FzWGVvYW5kT0dZS210UFBNWG14VE1YeUhLa0kxRl96eE0zb2tqWWVnam9KaEN0YmN4X2JCM3RDak1nOUdCeGx2a1VYc3Nud0xPLVh2V3RzT2t6R09vOA?oc=5>

### Advanced Micro Devices, Inc. (AMD) Stock Forecasts
- Summary: Forecasts predict AMD stock performance based on current market trends.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxQS2VNNWN1VEh0eU1ubnJrcG5LNjlaYkY5Q3RKQ2JrWGN6V1p6dy1DQlZvZXQ3Y1FvYXByZkR6Y0tQRmMxWVk0cEY4aFR6RjhyQkRDTC1kblBUVEFONkViUGt5RjdtWm00bVlwY0dmUXdGdS1EVWhOR0dNbjZLMlZkeEU5SXBHSjREemMzbg?oc=5>

### Why Is AMD Stock Gaining Wednesday?
- Summary: AMD shares rise on Wednesday, driven by positive market sentiment and investor confidence.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxON2RaQi02LUlDczh1N2hWUGZ5cHRjQXlBeERuNkRJSmlVaDNWc3EtUTVTNUtqM29kU1p5ekxlOWc1akxwU2VZcEFzYzJPQlExdFN1aFlQVFdudjJLMm5nRkViY3ZRRkNuRzc0dHRZSklFSHZfRFk5MllOVEo1dXJvWDhMQkdWLV9fWnlTX3h0d00?oc=5>

## RISKS

### Advanced Micro Devices Hit By Short Seller Report
- Summary: Short seller report alleges issues, causing market concern.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxORlEzaVhnbzU2MDRZdG1SZzhnUkxtcEZpaEQyZzJmc0ZuamxQZ0wwSUZKVUExVTk1QldUQmN1bkpJQXBmWnQzN3lySWRaYW1fQk1mQlpYaFAwU1ZGVWM4TS1xUjZoM204TFUtQjNNVW1PQnBxM3p6WnpuaDFtdjhCMUlkdEZGZDF3VHE3QVFvbGhodHA2MTR0ZE5DWVdRQ2NHTER4TUt5V0ppMlhZb2hZclNfaVBQaGFPZG1ieFZOQ0tseUJkMUxpT3piZmQyZw?oc=5>

### AMD Stocks Plunge 7.72% as Short Seller Questions China Firmware Ties
- Summary: Short seller questions firmware ties, leading to stock drop.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxONXEwS21FSEp3ZllMRDk0enF1d0Z3bnppTlVMZDJuMVZMNU90N1lnLUNqRlAtUzgyUnBaMDh5dGd3bVNDeC0zbWxwT3pVYzI5OUFJeDh6NDlOV1lPUnBfVlhES1hzTHcySDhIMDgtU2wyRFRZXy1SbGlkZ0ZMNVpOam9ZZndObjFVZlVLMUs0MUk?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMD** | **90.68** | **10.18** | **61.88** | **44.70** | **702,393,286,656.00 USD** | **105.99** |
| NVDA | 13.48 | 11.35 | 12.19 | 103.20 | 3,031,172,907,008.00 USD | -30.34 |
| INTC | N/A | 2.37 | 14.91 | 20.90 | 272,553,181,184.00 USD | 52.53 |
| AVGO | 38.88 | 14.58 | 28.48 | 85.50 | 1,453,140,738,048.00 USD | -11.58 |

Peers fetched as_of: 2026-11-21; AMD reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-03
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-21

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 1,584,000,000.00 USD; period 2017-07-02/2017-09-30; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 2,428,000,000.00 USD; period 2026-06-28/2026-09-26; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimAFBVV95cUxOeGVYdV9Ga0hQQzdiZ0NxZ1l4Nk1aZ2stV0N3M0RvLVY0U2FKM1M4b1BfVnMzSWk0Wm5LRkJIN3ItSkJoVV9Ia2UyM2t6QUloOFctcXJ4ajViTWpNUUl4V2V4YTZzUGdfLUkyN2NIQ1paeFVlcThHcEFveEduaDlueFdjSDd1RGcyYkpCVWMxM2N1UXZtWVlBaw?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQb1ZvQ1FxeEdyXzBkd3hNZ0ZydlpCdkI3T3gwR01QSHNfUHNaNDFBRTZaMmtyc2dUa0NhYXlQMXNybXEySDRzdWZFd2hOY2hOU3RoREVRcTEyT1ZKc1hBYlI1ZnMwS2NPVVZER3IxOHZZSE5zRWdfMmdwZ3dnT2oxM0M4bzFYamFsU2Y0cEhlMGE1UWJPMVhJMThFbkdnRllLa3c?oc=5
- https://news.google.com/rss/articles/CBMie0FVX3lxTFBnUU5wSm1najNrS3pqZDAxUlQyOHVtaGFBdnBBQlNUUmlobG9XT290d2Zha2ppSVgtU2E5amhwSHFTRkZ5RzV1ZXJnYmNHTGFET0JmeHZVVWthbm5nbF9HR181djRCZkQtQVVvdHNxU1RZcWlCZW5VQktoVQ?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxNdDJjTUItNjhtVWNMb0FRa3hKZThKYXNDbWxweWdZTXVtUXBCalAwMC15d3M2LU1Ta216M3poTmo4eTVyQ0xqMGFTX2VHd0Z3LW9EZFJEaWVDaEtVdXFsWTBReFk4dlI2RE9BQVJDb0Z0a3A3dGpGNGtxaWlvdU93VW1TSy1OVFlIYkV3UkNDYk5mZnBpQWUxMzF5cm1HT2FJejlEY1hmYVU?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPakd6RUtYYTBuV2dfQVE4SWpBendrV1B4UmdxOUt4R2djNzVkbWo5VV9qTmZ5YjRHaUJwSXhHb0dZMG5RMTJGQVNhcWZyT1prN3JFdFBWN1JWQ0twS3RDc3ZDVjVWbDltUVZWOURuTHZ6V1MxRkhGN3NCZ1V2N1NRX0FPUnRPamJOVU1EYnVRWkRXR2N2TWZUdnJ4WQ?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPeE4zN25uZ3h5c01LT2hKdFVrSncwaTlUWXpTUmNKZnpBZnB6b01JQTFIaW9IRms3NFVMS1lTLWZPNWVFajh5Vl90WXdjdEwxX29aTWhjLWtLeExZelZXRkpaZmV3VzVzakN2VzgwRjFkbi1BZkVESTlXZGx5d05LYm1SNnZRdlRhUW9NQ2d6UEh1R05TRFA0Q1MxcmJ6LXFmclRVbg?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxQZkNtckk5TW0wbDQzTkxSU3JQNVJROTBBdE5OMjlyWDZMcHR5VE1BemMxOFZxSXNZR2dQS2JNWDRSN2VJYkxDU1FTLVlielg5SW5IOXdibDEzcmNzZU16ekxGNkhoWDRnX0xRcWVzaFBpUmpRMFRmSllnM2pfaGRzYWFXSl9nRmlzUUE?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxPbkp6di1ZYkMzQlhjTmkxbHFwNzIzLWMyc3NKXzBqSV9hZ05wODRRYUhjYl9pSmIyNENPaHpXWmlScUpaYXhfT3AyQ1hKYVhWZnhHRVp1a0g2dkVGWmpYa2lXdmdjaE1TUTQwbFlyNjJVNjVkRmlIbWt3WHhWYjNJWXNGSG9RcFkwYUFRZzdYMVNpQXVnZllfU0ZlZEc0QnFsQ1RnWk9tUmc5d2luUVVSaWRKMA?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPUkNPRlQ0VWdjd0dOeVdRWVVDZlUwOTg0YkFDRE9UXzJHOWFuVEVFMmIwU2xOSl9Ibi1vMTFPX0liLU80SzdaeVdWLTgtamhuSS1nMlV6QjZBMVN2N1ZjN2xqYmR3NHlWYm5kY1l6a0lQUGo1UVdycjNhbzV5cmZjYlRGNGxvTVpDRXpRMGpRWkxkaVA1bm9KcTBBaTg4QQ?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQTURWcmloUmY4UlNoemdLU2V1dUhhZzJKaGFDbEFNQnk4dmFVQWpvUW5lYUJPQ2kwUTJhY3ljcWFha21yLS02SThucmEzMVdLOFZ4bm5rc1lCOHRVanBnVERUMmxYME8yT2hSZ2hnN3NJZUxqVnlSY2FuU0w0bVI3cVRyYm1aNlNQWDYwYXpVR0FZVmE5N1E?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxOdE52LXZkNFlqNVpPbjZ4WUtZdGJxQ1lHMnh1TmJUblpMazhIZzlvNF96MXF3dmJtRzRBYUxWTDc1ZzhjUllIRkhQWVl6MzVsZnc0aVhqcFQ5bUJKMjZsWTBGdTZtNVFGLW9FOVZLbHlBMFd5bjhDS1JZTTRqYXJjekVZVklVWlV5MzJDVEpaZmRUM242N1RsNGpMQWQtTW5vXzY1dFVpU1pwZ2J2ZEEzaXU3NWVvUTdLd3prU0hjSEhiek9vc2JJ?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxOX3BLVnZVVDhkQ1I2LTdZRjZJdHBWU2dKVTlOS2U5bmNaTms4SUY1WndRRmF0TDcyN0VuanVjcFhyQnRyWVlOMGQzS21rSnJCUnRoalZqc3M5N3lwSGQ5S2hjN1BMV3BYTlhNcDBvZlZ1X1dfT2JqMmpXN05fYzJJWm5wTERHME1s?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQV0RabkRYQjV0NTd3aHhnNzhPN0pWbGE3WklWaWNsNHNqdG8tVGNpS0JzSGNXS09IcmNwQXVRUHAwVHphVXh0QzBRWFJidGZwaWgxaWdmQTRQWl9vN0NNbE1aWmtkSzBIZzNzMVRIX0dMRjZvaE1tbi1uSGJtdEJLZXY4SjNfWi1HS2pLU0NTWS1PUFpOZG5KWDFqUQ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOOERqVlNqV0JSeWxUeTJDTVVBeWlsV1pKaVFNVEI4dXZkTWc1REdueTJRenlWay1vbW9SbVhBUE5wQUk1b1FzWGVvYW5kT0dZS210UFBNWG14VE1YeUhLa0kxRl96eE0zb2tqWWVnam9KaEN0YmN4X2JCM3RDak1nOUdCeGx2a1VYc3Nud0xPLVh2V3RzT2t6R09vOA?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxQS2VNNWN1VEh0eU1ubnJrcG5LNjlaYkY5Q3RKQ2JrWGN6V1p6dy1DQlZvZXQ3Y1FvYXByZkR6Y0tQRmMxWVk0cEY4aFR6RjhyQkRDTC1kblBUVEFONkViUGt5RjdtWm00bVlwY0dmUXdGdS1EVWhOR0dNbjZLMlZkeEU5SXBHSjREemMzbg?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxON2RaQi02LUlDczh1N2hWUGZ5cHRjQXlBeERuNkRJSmlVaDNWc3EtUTVTNUtqM29kU1p5ekxlOWc1akxwU2VZcEFzYzJPQlExdFN1aFlQVFdudjJLMm5nRkViY3ZRRkNuRzc0dHRZSklFSHZfRFk5MllOVEo1dXJvWDhMQkdWLV9fWnlTX3h0d00?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxORlEzaVhnbzU2MDRZdG1SZzhnUkxtcEZpaEQyZzJmc0ZuamxQZ0wwSUZKVUExVTk1QldUQmN1bkpJQXBmWnQzN3lySWRaYW1fQk1mQlpYaFAwU1ZGVWM4TS1xUjZoM204TFUtQjNNVW1PQnBxM3p6WnpuaDFtdjhCMUlkdEZGZDF3VHE3QVFvbGhodHA2MTR0ZE5DWVdRQ2NHTER4TUt5V0ppMlhZb2hZclNfaVBQaGFPZG1ieFZOQ0tseUJkMUxpT3piZmQyZw?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxONXEwS21FSEp3ZllMRDk0enF1d0Z3bnppTlVMZDJuMVZMNU90N1lnLUNqRlAtUzgyUnBaMDh5dGd3bVNDeC0zbWxwT3pVYzI5OUFJeDh6NDlOV1lPUnBfVlhES1hzTHcySDhIMDgtU2wyRFRZXy1SbGlkZ0ZMNVpOam9ZZndObjFVZlVLMUs0MUk?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
