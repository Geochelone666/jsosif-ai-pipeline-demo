# MU Intelligence Report

- ticker: **MU**
- Report as_of: **2026-11-05**
- Market data as_of: **2026-11-05**
- Quant sources: https://finance.yahoo.com/quote/MU/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MU/key-statistics/
- AI analysis snapshot as_of: **2026-11-05**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-06T05:03:31.231954+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 0, 'ai': 16, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261105T045846Z-bde0a1fe/MU** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 8 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 45.83%; oldest publication 2026-11-02

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 656.3900 |
| Return 1D (%) | -17.4591 |
| Return 1W (%) | -29.7430 |
| Return 1M (%) | -38.2972 |
| Return YTD (%) | 130.1497 |
| Return 1Y (%) | 176.6886 |
| Annualized volatility (%) | 83.5698 |
| Beta vs SPY | 3.3481 |
| Max drawdown (%) | -45.8952 |
| Sharpe (rf=0) | 1.6379 |
| Downside deviation (rf=0, %) | 52.7372 |
| Sortino (rf=0) | 2.5955 |
| Historical VaR 95% (1D, %) | 7.0090 |
| Historical ES 95% (1D, %) | 10.3312 |
| Correlation vs SPY | 0.5446 |
| Tracking error vs SPY (%) | 77.0153 |
| P/E (trailing) | 8.83 |
| P/B | 5.36 |
| EV/EBITDA | 6.47 |
| Revenue growth (%) | 379.30 |
| Forward P/E (estimate) | 3.16 |
| Gross margin (%) | 80.72 |
| Operating margin (%) | 80.68 |
| Return on equity (%) | 88.26 |
| Free cash flow yield (%) | 3.92 |
| MA50 | 966.4385 |
| Close vs MA50 (%) | -32.0816 |
| MA200 | 755.0643 |
| Close vs MA200 (%) | -13.0683 |
| RSI (14, Wilder) | 27.0523 |
| MACD (12,26) | -54.3653 |
| MACD signal (9) | -34.1661 |
| MACD histogram | -20.1992 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MU': 276, 'SPY': 276}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 656.3900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -17.4591 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -29.7430 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -38.2972 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 130.1497 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 176.6886 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 83.5698 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 52.7372 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.5955 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 7.0090 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 10.3312 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5446 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 77.0153 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.3481 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -45.8952 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.6379 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 3.1594 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 80.7160 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 80.6780 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 88.2600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 3.9238 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 8.8308 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 27.0523 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -20.1992 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -32.0816 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -13.0683 -> Clearly below the moving-average trend level.

## TAILWINDS

### Micron: Buy The Panic Before The Market Wakes Up (NASDAQ:MU)
- Summary: Analyst urges buying before market rebound.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxQU2REbjB6bHZPTGpVRTlQNW5pclVCdjRBU09tYzdhYzUtaUVNWDRIbnBwenB2TEV6RTR3MFN0WUxFdkRIRk9yaW9vanFUMXhRZUxRQUZvdmFiNUk5eXlQRUtuSjEybldsMXFZRVJoT1VxeWVtMnI1WG92RUgwWmZ4UWdfaFBuek5YVmlFVzBhSGNaZw?oc=5>

### Micron's Selloff Is A Once-In-A-Decade Opportunity (NASDAQ:MU)
- Summary: Selloff seen as a rare buying opportunity for investors.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxONk5hLVZLVGVod0hrUmtVSlN5UXN2NWFXMmQ2NmJYNWVYc3NDem1aRnYxTmFtLTlKUFpDcW1jdTRLSDlNVlViVjVCQjhPU19wQTFFVDREUmlQOHE1cDF1TVpoOVBHRHdaX0tkY20wRi1UWTk2OWhQSFBqcGltOHpYUzYyTG9zQWYtemlwclpyWHRZU1k?oc=5>

### Micron (MU) Stock Looks Near Fair Value Despite AI Optimism
- Summary: Stock near fair value amid positive AI sentiment.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOc0hlazlrNjNkX2pzMTVxOTlZT0xQNDBXZnBoX3VJWHNXQ1NVcWI1THJ1eTNVYU16b1F6Z3h2X0JoMjF6bFBDZXlsZlZvOFZVMWlzVkVUeTJpcXgxbWVpQkkxSTk5X1NCWFRjOFB6VHhvRVQtUkZqdnpkdnVhQTNYcldBVjRocDNZdWloTlF0ODY5ZTlmRXc?oc=5>

## HEADWINDS

### Why Micron Stock Is Falling Today
- Summary: Stock decline attributed to recent factors.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPU0RwVjVWeDQ2RENzVzNYZXRJT0E4ZWtkWE5VcXdnbm5Fb0VpTksyVG92UXFNNWpybVBoMFJ3WWtZZGQ4ZGoxM2YyRzkxLWI0SnNnQ3UtbnRCQmpsQ0V6WkpQdE1PNDRnWFhEVUZTbndmNktZeVlwdW03bzJLand6Ri1STm9VTHkzU083bHZSM2VJYnFWUWJJeW9EYw?oc=5>

### Micron (MU) Stock Sinks As Market Gains: Here's Why
- Summary: Micron shares decline amid market gains.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQc3NNb1RNWmpjTFRUWWdBOC1mampaLWQ1YWFoYW9aRlNCcndUWXBWSkJEb2RnWWFPMVhkTS1mSG5sNmFNS0RmaEJ1aXFPVnBhTzdHc1hyUDA5enpSeFgzUjBqRnBhSURweGtoNHRNNTA5MWpabi1MMHpxTE91MFdJSzRDUGdmVkNCbERuV21fYVZMdUFyS2FHcg?oc=5>

### Micron Technology (MU) Pulls Back Amid Broader AI Memory Sell-Off; Underweight Position Aids Relative Returns
- Summary: Pullback due to AI memory sell-off, underweight stance helps returns.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNcmV6OW9ld041cUU0MWl4QU9wN3pGcnhKZER4NmlYYnI3R3NvWDcxbGFGTTNEdFBYX2ItY0JpY2RveHcxUzktNDBCRllGQmw4U29jMkJyY0pFcy1YUmhpbzhuLVhBMHlHdXhsdjh4VFhfRHdETU9pUTFDR1ByUHNrM0ZWb21nM1NPZGJtbHZ0VW00dGw0M192dGtqZ3o?oc=5>

### Why is Micron Technology stock sliding today?
- Summary: Micron shares are falling today.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPZjJoVEs0aDhFUndVU1duMmtTVEc4aVFEV1lWTTNtSlNDYlVOQ0RYOVY1Y1l1Y0FkRG9oZWFlcmNkOXZrNDh3X25kZ1hvOWtqaWZ1Nk5VQk9kMnYtRjNfZFZ3bHpyeXpTUnpJRWRQUEN1T0RCbkJkUXJyUDhrdUV6aDRVTmFSQ002TmRwWDRaSlFBeHg2eTF2X1NxMzlUaEl6bzJuUndnNXRPZw?oc=5>

### Micron Stock Hits 3-Month Low. Is MU a Buy at These Levels?
- Summary: Stock at 3‑month low, raising concerns.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxPVExmbVgwRmdpZEUxb0J1U2tqcUtPdHVxUUhwZ3NUWXkwYWJIQkJCeEV5LW1ETHJub0RQcGFIeWdhVFViNU9rdVJBNk9TWWhzUFF5OFg1VFBXU2ticzFqR0hVSzFaUl9ZazIwX0F1akpVVDI5V1hwNTJwVlh6MkczSFhn?oc=5>

### Micron Stock Gets Crushed by AI Selloff. Don’t Ignore the $200 Billion Silver Lining.
- Summary: AI selloff hits Micron stock.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMic0FVX3lxTE15TVY0YUJZQXZIYUpKcWRPci1VWGZlbFRXT3pmNkJUcF9MbVFtUWdhdnNnRDRGU1ktWXZ5SExlRjViYkpZSGtrTEtadE1TdDJjWk51eDV5eE1lMi03bTFxb0YxdFIteEU5OWFyZ0s4cnlrTTA?oc=5>

### Micron Stock Plunges As Memory-Chip Shortages Cause Ripple Effects
- Summary: Memory‑chip shortages trigger plunge.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxPX0lGaFVmall4RXFtb05Ud0FrYk4wdVVPZ1pMaURhckZhZE41VktXclRSV2FNZW1uLVFfQUNITTFIZ25WNkFSX3ZzQzJMOFBEUUE1YV9Qc3A2Q0E4SGwzZkZ5LV9BcnRHdzQwbF9SSUlscUxlQ1RmVGpiRE56VXJxSVpUUV9Ud3BzVjcxUTFR?oc=5>

### Why Micron Stock Keeps Going Down
- Summary: Continued decline signals ongoing pressure.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxQbjBleVA1OXJDbThsRkhnRUZzWTZDYUFtS3VCTUllTDlWSWpneURNVkd2M0dJa2dxaXZSclRWU1JIVEk5aE5SdmY0SlNlc1U5Q3VnOGdRUkZjNHBlWnhqTVgwMzZ3Z3BIRkowMURSTlZLSFpHWHEyNjMxdFdGbWFQMkhB?oc=5>

### Micron Technology plunges 17% amid chip selloff, Taiwan plant halt (MU:NASDAQ)
- Summary: 17% drop due to chip selloff and Taiwan plant halt.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNRDhzVlRiSVpJay1TNlJ4c0ZnUzRBUjZ4TFJZaEVFbjVIZmJVbzVzR0RWUGFjUS1rTXdmWjdlRjlSd2VpVFN1WVBDeWd1Z2FXYlNqbkdxbFkyM3NGbTNROG90MV9HR0Q4aFUxeWhyWllCdGYwV2FSNEtISnpaZWpBUTZCZUx4OE9SUmRaRHBsdVdYLUZRZy1jZ1NTZEUyWEZlX3c1Uw?oc=5>

### Micron Technology: Is This a Sign That Its Stock Has Already Peaked?
- Summary: Questioning whether stock has peaked, implying potential decline.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxNbUlIQ1BMdlgxYlhFb2FjMG82dlhFYnhHZk1oUnYtQXVmU25IeS0wa2pvbWFpT0lseW8xdmZSZWRmU0F0WU95ZHk5MktaOHJoa21MSEtYdGlCb2RCTlJkd2liTF9HMmw3bVFqbVk0WlFDUFMyakN0clQ3LTE2WExCamJobUlTeU00ampOZUVYR0g3N0pZMURnRXRtdW4xNlEtQm1R?oc=5>

## CATALYSTS

### Micron Investors: Mark December 9 On Your Calendar (NASDAQ:MU)
- Summary: Scheduled investor event may influence MU’s short‑term outlook.
- Date: 2026-11-03 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNM2hSczhyTDFGck50RmRLOWFyT0VEbGxYYkhQQVpRUEFIVlpYdVBOVzJteXhUX054SVhlazIzS3NXR1VxWkJaclpYcDZkRW1zWVEwamd2Y2R6ZnJhaVNNRENEVDUycE1iU1JmN25HUzJGVEFuU1lMZEU3eXJwUXZNdVdURmNOMUtHZTQxS19lWG83SkhT?oc=5>

### What Wall Street is Missing About Micron’s (MU) Ultra-Low Earnings Multiple
- Summary: Earnings multiple lower than expected, analysts may overlook.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOZm5OcG9fOWsxbGR6RGlCZXVQRFdDNFZYb1dWUVZqNUw3UUdKcWd6Rk1XVkFZVFZTc0RKMUZuRTVIZmxZSUhFTVZZYm81al9uT3B4QXQzUzRKR3FjdXVhOW55WF94enVWdWpha3RJUHJPZ0JGUEtvTjNxbmtmNTQzOEdNbldicGtjNXU1TGd4dzJqeld2bjZEalV3?oc=5>

### Are Wall Street Analysts Predicting Micron Technology Stock Will Climb or Sink?
- Summary: Analyst predictions may influence future stock direction.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNMlRjajRncUFXWGJweWVDNUpCMVZRaVhCTEFGZkloOXdwY0RKLTNKN3I1U0ZzcHZNWXFXWGY3ZXYxLW9WejZFV3VOLTVCOFFYU1dPSG9ISGpRX1Y2RjQ4THlzX3dReTNGc29WZ0N0T1g5NFZMeG02MmpKSHB3N3E4Z2psRGJIZWhuWWgweXU5b1h2NkJhNjVFbHBDVXZDVk1SVVRBQW5n?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MU** | **8.83** | **5.36** | **6.47** | **379.30** | **742,654,935,040.00 USD** | **176.69** |
| WDC | 9.41 | 10.71 | 15.81 | 55.50 | 100,180,140,032.00 USD | 67.48 |
| STX | 29.21 | 31.04 | 18.50 | 61.00 | 107,097,145,344.00 USD | 70.17 |
| NXPI | 20.86 | 5.10 | 12.81 | 19.30 | 61,609,312,256.00 USD | 18.20 |

Peers fetched as_of: 2026-11-05; MU reuses existing data (market data as_of: 2026-11-05); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-30
- Next expected earnings: 2026-12-23 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-05

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-10-09
- Revenue (latest available single quarter): 8,440,000,000.00 USD; period 2018-06-01/2018-08-30; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 28,243,000,000.00 USD; period 2026-02-27/2026-05-28; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/723125/000072312526000023/mu-20260903.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMikgFBVV95cUxQU2REbjB6bHZPTGpVRTlQNW5pclVCdjRBU09tYzdhYzUtaUVNWDRIbnBwenB2TEV6RTR3MFN0WUxFdkRIRk9yaW9vanFUMXhRZUxRQUZvdmFiNUk5eXlQRUtuSjEybldsMXFZRVJoT1VxeWVtMnI1WG92RUgwWmZ4UWdfaFBuek5YVmlFVzBhSGNaZw?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxONk5hLVZLVGVod0hrUmtVSlN5UXN2NWFXMmQ2NmJYNWVYc3NDem1aRnYxTmFtLTlKUFpDcW1jdTRLSDlNVlViVjVCQjhPU19wQTFFVDREUmlQOHE1cDF1TVpoOVBHRHdaX0tkY20wRi1UWTk2OWhQSFBqcGltOHpYUzYyTG9zQWYtemlwclpyWHRZU1k?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOc0hlazlrNjNkX2pzMTVxOTlZT0xQNDBXZnBoX3VJWHNXQ1NVcWI1THJ1eTNVYU16b1F6Z3h2X0JoMjF6bFBDZXlsZlZvOFZVMWlzVkVUeTJpcXgxbWVpQkkxSTk5X1NCWFRjOFB6VHhvRVQtUkZqdnpkdnVhQTNYcldBVjRocDNZdWloTlF0ODY5ZTlmRXc?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPU0RwVjVWeDQ2RENzVzNYZXRJT0E4ZWtkWE5VcXdnbm5Fb0VpTksyVG92UXFNNWpybVBoMFJ3WWtZZGQ4ZGoxM2YyRzkxLWI0SnNnQ3UtbnRCQmpsQ0V6WkpQdE1PNDRnWFhEVUZTbndmNktZeVlwdW03bzJLand6Ri1STm9VTHkzU083bHZSM2VJYnFWUWJJeW9EYw?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQc3NNb1RNWmpjTFRUWWdBOC1mampaLWQ1YWFoYW9aRlNCcndUWXBWSkJEb2RnWWFPMVhkTS1mSG5sNmFNS0RmaEJ1aXFPVnBhTzdHc1hyUDA5enpSeFgzUjBqRnBhSURweGtoNHRNNTA5MWpabi1MMHpxTE91MFdJSzRDUGdmVkNCbERuV21fYVZMdUFyS2FHcg?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNcmV6OW9ld041cUU0MWl4QU9wN3pGcnhKZER4NmlYYnI3R3NvWDcxbGFGTTNEdFBYX2ItY0JpY2RveHcxUzktNDBCRllGQmw4U29jMkJyY0pFcy1YUmhpbzhuLVhBMHlHdXhsdjh4VFhfRHdETU9pUTFDR1ByUHNrM0ZWb21nM1NPZGJtbHZ0VW00dGw0M192dGtqZ3o?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPZjJoVEs0aDhFUndVU1duMmtTVEc4aVFEV1lWTTNtSlNDYlVOQ0RYOVY1Y1l1Y0FkRG9oZWFlcmNkOXZrNDh3X25kZ1hvOWtqaWZ1Nk5VQk9kMnYtRjNfZFZ3bHpyeXpTUnpJRWRQUEN1T0RCbkJkUXJyUDhrdUV6aDRVTmFSQ002TmRwWDRaSlFBeHg2eTF2X1NxMzlUaEl6bzJuUndnNXRPZw?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxPVExmbVgwRmdpZEUxb0J1U2tqcUtPdHVxUUhwZ3NUWXkwYWJIQkJCeEV5LW1ETHJub0RQcGFIeWdhVFViNU9rdVJBNk9TWWhzUFF5OFg1VFBXU2ticzFqR0hVSzFaUl9ZazIwX0F1akpVVDI5V1hwNTJwVlh6MkczSFhn?oc=5
- https://news.google.com/rss/articles/CBMic0FVX3lxTE15TVY0YUJZQXZIYUpKcWRPci1VWGZlbFRXT3pmNkJUcF9MbVFtUWdhdnNnRDRGU1ktWXZ5SExlRjViYkpZSGtrTEtadE1TdDJjWk51eDV5eE1lMi03bTFxb0YxdFIteEU5OWFyZ0s4cnlrTTA?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxPX0lGaFVmall4RXFtb05Ud0FrYk4wdVVPZ1pMaURhckZhZE41VktXclRSV2FNZW1uLVFfQUNITTFIZ25WNkFSX3ZzQzJMOFBEUUE1YV9Qc3A2Q0E4SGwzZkZ5LV9BcnRHdzQwbF9SSUlscUxlQ1RmVGpiRE56VXJxSVpUUV9Ud3BzVjcxUTFR?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxQbjBleVA1OXJDbThsRkhnRUZzWTZDYUFtS3VCTUllTDlWSWpneURNVkd2M0dJa2dxaXZSclRWU1JIVEk5aE5SdmY0SlNlc1U5Q3VnOGdRUkZjNHBlWnhqTVgwMzZ3Z3BIRkowMURSTlZLSFpHWHEyNjMxdFdGbWFQMkhB?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNRDhzVlRiSVpJay1TNlJ4c0ZnUzRBUjZ4TFJZaEVFbjVIZmJVbzVzR0RWUGFjUS1rTXdmWjdlRjlSd2VpVFN1WVBDeWd1Z2FXYlNqbkdxbFkyM3NGbTNROG90MV9HR0Q4aFUxeWhyWllCdGYwV2FSNEtISnpaZWpBUTZCZUx4OE9SUmRaRHBsdVdYLUZRZy1jZ1NTZEUyWEZlX3c1Uw?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxNbUlIQ1BMdlgxYlhFb2FjMG82dlhFYnhHZk1oUnYtQXVmU25IeS0wa2pvbWFpT0lseW8xdmZSZWRmU0F0WU95ZHk5MktaOHJoa21MSEtYdGlCb2RCTlJkd2liTF9HMmw3bVFqbVk0WlFDUFMyakN0clQ3LTE2WExCamJobUlTeU00ampOZUVYR0g3N0pZMURnRXRtdW4xNlEtQm1R?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNM2hSczhyTDFGck50RmRLOWFyT0VEbGxYYkhQQVpRUEFIVlpYdVBOVzJteXhUX054SVhlazIzS3NXR1VxWkJaclpYcDZkRW1zWVEwamd2Y2R6ZnJhaVNNRENEVDUycE1iU1JmN25HUzJGVEFuU1lMZEU3eXJwUXZNdVdURmNOMUtHZTQxS19lWG83SkhT?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOZm5OcG9fOWsxbGR6RGlCZXVQRFdDNFZYb1dWUVZqNUw3UUdKcWd6Rk1XVkFZVFZTc0RKMUZuRTVIZmxZSUhFTVZZYm81al9uT3B4QXQzUzRKR3FjdXVhOW55WF94enVWdWpha3RJUHJPZ0JGUEtvTjNxbmtmNTQzOEdNbldicGtjNXU1TGd4dzJqeld2bjZEalV3?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNMlRjajRncUFXWGJweWVDNUpCMVZRaVhCTEFGZkloOXdwY0RKLTNKN3I1U0ZzcHZNWXFXWGY3ZXYxLW9WejZFV3VOLTVCOFFYU1dPSG9ISGpRX1Y2RjQ4THlzX3dReTNGc29WZ0N0T1g5NFZMeG02MmpKSHB3N3E4Z2psRGJIZWhuWWgweXU5b1h2NkJhNjVFbHBDVXZDVk1SVVRBQW5n?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
