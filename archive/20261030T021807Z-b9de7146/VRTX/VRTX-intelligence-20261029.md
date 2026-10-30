# VRTX Intelligence Report

- ticker: **VRTX**
- Report as_of: **2026-10-29**
- Market data as_of: **2026-10-29**
- Quant sources: https://finance.yahoo.com/quote/VRTX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/VRTX/key-statistics/
- AI analysis snapshot as_of: **2026-10-29**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-30T02:37:45.561141+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 19, 'rule': 0, 'ai': 13, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **13** exact headline/source/date matches; prior report **20261029T020157Z-688a53f0/VRTX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **6**; {'directional_claim_without_event_type': 4, 'low_uncalibrated_model_confidence': 2}
- RSS source audit (metadata only, not article fact-checking): 19 unique headlines; 10 named publishers; 0 exact duplicates; 19 HTTPS source links; largest publisher share 36.84%; oldest publication 2026-10-23

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 540.0000 |
| Return 1D (%) | 1.9464 |
| Return 1W (%) | 0.9025 |
| Return 1M (%) | 2.5193 |
| Return YTD (%) | 19.1106 |
| Return 1Y (%) | 29.4312 |
| Annualized volatility (%) | 29.1804 |
| Beta vs SPY | 0.4905 |
| Max drawdown (%) | -15.2113 |
| Sharpe (rf=0) | 1.0320 |
| Downside deviation (rf=0, %) | 17.8438 |
| Sortino (rf=0) | 1.6876 |
| Historical VaR 95% (1D, %) | 2.6839 |
| Historical ES 95% (1D, %) | 3.4058 |
| Correlation vs SPY | 0.2137 |
| Tracking error vs SPY (%) | 29.2328 |
| P/E (trailing) | 31.45 |
| P/B | 6.76 |
| EV/EBITDA | 25.68 |
| Revenue growth (%) | 12.50 |
| Forward P/E (estimate) | 26.48 |
| Gross margin (%) | 54.96 |
| Operating margin (%) | 38.05 |
| Return on equity (%) | 23.54 |
| Free cash flow yield (%) | 1.92 |
| MA50 | 522.8420 |
| Close vs MA50 (%) | 3.2817 |
| MA200 | 478.6672 |
| Close vs MA200 (%) | 12.8132 |
| RSI (14, Wilder) | 61.4565 |
| MACD (12,26) | 3.9119 |
| MACD signal (9) | 0.3242 |
| MACD histogram | 3.5877 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'VRTX': 271, 'SPY': 271}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 540.0000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.9464 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.9025 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 2.5193 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 19.1106 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 29.4312 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 29.1804 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 17.8438 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.6876 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.6839 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.4058 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2137 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 29.2328 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.4905 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.2113 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.0320 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 26.4750 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.9570 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 38.0550 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 23.5430 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.9200 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 31.4502 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 61.4565 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 3.5877 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 3.2817 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 12.8132 -> Clearly above the moving-average trend level.

## TAILWINDS

### Here is What to Know Beyond Why Vertex Pharmaceuticals Incorporated (VRTX) is a Trending Stock
- Summary: General information about Vertex’s trending status.
- Date: 2026-10-28 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQQVdrekpkclVkTF93RUxySVd2Tm0tYmJibzdpUUNLdlZuZTlwM1A3NWxjcWpxbkNaOEhBUkVSaTcyOVdSd3Zvd29xT3dFMXpYb0N4eEl0MkN0U25BdERES0ZpbG5tTVdOemQxc0lwaVBOVjI3WTB5aERPbndUYWVqMVpzRW1rQnoyVlo4N2VrbzhIZHlXQk9YZExXQnBtMjJFZ0VrUzZR?oc=5>

### Vertex Pharmaceuticals (VRTX) Posts Positive Phase 3 Results For Povetacicept
- Summary: Positive Phase 3 results for Povetacicept indicate strong clinical progress.
- Date: 2026-10-25 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNZHJ3T19LVjBFdDc3RUxicks1UUFqdjlYNEZDZ19CNmRZeWdJc0tjbkZiNjY5NlZCSlhUaUtWSzNKbEhValJ1aWtiS2h6SzlyN3hVNzgzMlNzNTVPRzNXZTFlV1BPUHB3U1dUZy1IMWM4c3dDQ2k2bk5mZkd6VDUtazd5aUZVMGpjUTMtVW9reDk4aTBIcWFvUWNxLUFmN2lBR0FDOG1R?oc=5>

### Vertex Pharmaceuticals Incorpor (VRTX) Stock Forecasts
- Summary: Forecasts predict future stock performance for Vertex.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxQc0VzMGtueUtMc3NJN09ZTVpOUTJSaHY1WmdrV3VCTzQ1V0lnVVhFX2ZId2VSV1ZtcTN2aG4zN1pRVVVuSGx6STFzRExxY1lQaGxSN0F0Sm42QTNvMERLRFhZN2ZjdmJrdWlETFpZYThPbVpvYldjYTFZMDdwNDFpS0VsX0lqblM4RUFsYg?oc=5>

### Vertex Pharmaceuticals Gets 96% of Product Sales From Treatments for 1 Disease. Here's Why That's About to Change.
- Summary: Diversification of product sales expected to reduce reliance on a single disease, boosting revenue stability.
- Date: 2026-10-24 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNVlJHemhWaVI4enI0cXRkMTZncnRaMEN3Und6NndBTHFoQ1FaOUZseFZBTmNJaDZUVzd1MHdkd1dPYmd3WDR6M2M3X1BrZ0ZSb053blZYNUpQMWtKTnBack9wdFRNX3g1TnNvTHN3UTVWUGtIQmp1RHFVRDEtX014Tkx0ZDZ6bTMxT3NrTHJXVV9wdkdpSkNBSw?oc=5>

### Is Vertex Pharmaceuticals (VRTX) A Bargain After Its Phase 3 Kidney Trial Win?
- Summary: Phase 3 kidney trial success suggests undervaluation and potential upside.
- Date: 2026-10-25 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxQZG5hRkFwbDdac3BTellXczFoU3QxVG5vbGlua09JYzlDTVZlV1l1aENQNjV3blp6WWRQazdwSV9GLWVJRUJnVnNEdTNqTl9zLU1wc3NIS3RfeXJ0OUgyNHhILWFBdTVVVzFMOU1qeGJicDRTa1pNMmtrVTZxcnJreDhKa0RiS0Q0WDRwbDBXN2thT1o3NlpzZW5xQVh0bnJaRWVmb3dCam9PdjRlanpyUnNVV3FkU2MxZU0zd3hyRlRHQ0Rlckk2UzFpNm5MWjlaUUVOTHlpMkhnb1hYN2otYU5KVnBWaGxNVjlqa9IB8gFBVV95cUxNSlRkeFoxU2Q0T0hhTGZLVEVrdlIzWW9fZW9JcnJ3SnlTREE5ejIyVW9mb0tmWVZ0NG1xZUxiaTZMUlVrck90RUlXbHByWE9uWlVZVTFiV1JoWjZXc0JvWVFkQXp4bWRTdjFyQWtRSHF0NWNaa2c4dWlOVkhGSm9POGxFTDdhTDZZenc3c3pDeURBaU5YZjBPOVpHOGhpN3BPWDVJUFZ0M1FTaWxXYlAydW9aLVV0UFk4T3BTZ1h2bllEY2ZLNHlqMzhlb0ZZRmtXamN5Qmg0ZnRxWUliSVY5NGVCS1lMWFIxX0FRQ3dlUXVSZw?oc=5>

### Here’s How Much You Would Have Made Owning Vertex Pharmaceuticals Stock In The Last 20 Years
- Summary: Shows 20-year performance of VRTX stock.
- Date: 2026-10-29 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxPT1ZxaXJESVV2dnZLaWJLQlNLVU1MNDdVbFF3M1U1WHE4MUJyWm5LQjVWN3RHMFRrQngxTDNqRUVsTS1XQnlKa2NQZERSRFJnak9DSkNOMktZRVlzRk95NjZldTJ6dGpFNjFKSm5wWmpQZHZPNW9LQkk0SWEwUFhxXzkyLTV3V2ZNbU9yZ3lXa0RGYU83dTQ3NWNQN1VYMVMzb2N1U2x0cm4tSW1hVmlVNWRfeU5rS3c4anVqZk1hRDkzV3VhU1dENlBn?oc=5>

### Vertex Pharmaceuticals (VRTX) Stock Could Stay Below Fair Value Despite Its 173% Run
- Summary: Predicts VRTX stock may remain undervalued.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxPaHpyVVgwQjlCOElOZjJKN3ZLbHJVVV9MMFVoVF8xVWFmUVVzOGlDem9FMnNDek9uSVFKRWd6RGRzTWRRNXFYd0xLQXNjcldEQS1UQ2N6c0NGV2ZobUNOaEVvMFhyZ0ZxU2x2c0psbUdtTi1XY2hvb3VLSFBnQk9JZXdGS1ZfeFdCcE5yVGlTS3JDYlJQS0lPcW13U0JqdkI4eEdIN243dW1QLUpnWU1SaDNNeVFHX2dSZ2lSeGJLYnVOOXdzOGdvbnJvak5jai1nWHJDVmstY2JWSjJWa2VxTkhOMExCVUp5cGdiZNIB8gFBVV95cUxORVdwSVByZlRQa3ZpVVhVVFFRbDIyQ0dMYmdRT3BOTE41RnQ0V0dRdDZNdEFIYmkyRnJzdWwyV3BDUzJFTkhkQUtydzVNYnVJRl9lTUZLU1pZR3hfOVBXVWVYMERTS1M0bDdJdVFfMk1uaU05dkl5ZFRRV2pSTW1wZlpEZlJkeDJWeWE4NGM1TFhaUWQwVHBpajBqVkx0dFltbFpvZzlTeG9nTUFFdWNnOHNLcUpEOGxvUXEtSm56VXliU29SVHl2aHlzQUc0U0JpcWluN1VXSzRRYUM1di1jREd2RkRhX3NLaTlFS1JkVzR2QQ?oc=5>

### Vertex Pharmaceuticals (VRTX) CEO Jeff Leiden's Leadership Journ
- Summary: Discusses CEO Jeff Leiden's leadership.
- Date: 2026-10-27 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPczJ2MDdLWFRNVjdRYm41cFN3M0ZQdmRnT01pbWcwOVQxNUlKNHpYNWlXdmgzYlktVmhsanlSY2tWOU5tSWZSaDRnNUpoN25UTUFJRXJvTmpNMVZXSzlfNkY0Q1RYa1hsdkt1VHRDRWlSdlJMci1yZXU0eXhKbHF0MUdjUExGZXUwV1J4ODBuM3owWTYyTWhxMm1FTWZZX21DMVVITA?oc=5>

### ETFs Are Net Sellers of Vertex Pharmaceuticals (VRTX) on Oct. 22
- Summary: ETFs selling VRTX shares on Oct 22.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxQbndOUXd4aTItWm1PVnktT1RfalhfVGdBY3lRUGx1b0ZRaGUwd3VnelQ0bzAxa3VCNENEMFVZSEVZZEtIM1JmWnV1eWUxNUF0Z2N6TVhTa1IySk5ROGRCQ19hR3N1T2I3c2djejFMc2psT1hJelg2bHVib3BzRmRjZkp1RTZmQmtNSTE2MFVOOU1RZDUtczlxVTA1djZQV25QbXJTaXNHVQ?oc=5>

### Vertex Pharmaceuticals Incorporated Estimates – NASDAQ:VRTX
- Summary: Provides earnings estimates for VRTX.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMieEFVX3lxTE5GOHRJNC1Yems2S1BMVXZEWWhWU0hpMHVPTm1YenpFbmZyVERKNmZZbHB2dHNCUDBDZFZRZ0lWV0gzQ2VzZjdiM05uNFdwUURxTG15N1YxRl9yNU9xUUFSMmdSN1I1aksxNkcxWXZiNmUyN2VqMkZ0dw?oc=5>

## HEADWINDS

### Vertex Pharmaceuticals (VRTX) Stock Sinks As Market Gains: Here's Why
- Summary: Stock price decline amid broader market gains indicates negative sentiment for the company.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxPOEVKaXlSbjNjRTEwSDRGODcyR0VTV1B3bmZPbU45ejBOZ0E0RERDRmdwVVBySUZkN0NmOWxjQS10QWNyOVhWWTZJaE5VSWppZVhDMnhGSUs3bFZtUHhSLUlHbVRuOEo1bmdCTkk2cENuV1doMGZmTXJ4cXozMXo4S25MeHB5V3JqVlBnVXlRM19kbTlMdno5SVlTQUgwSXRPZjI5Q0szQQ?oc=5>

## CATALYSTS

### Ahead of Vertex (VRTX) Q3 Earnings: Get Ready With Wall Street Estimates for Key Metrics
- Summary: Upcoming Q3 earnings estimates.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQdXJROFhGNXJCQTZoUDlrdDJoU2FieHZidWZmNTY0X2I3WVRoVDYtaEY4ZnhUdTc4VEpmekVJTlh1V3ZFeVd4VjcwdVdhZkpiaDlXdXlxc2ZfQ1NsUm43cl9oRTlONXVyYkp3Z0hXbE9zOG5EdThfM3F4amhWM0RyUHFwN3M5bGVxcUR3R3R4NUxKVG5KSDZVMmhn?oc=5>

### Kidney Trial Win Could Be A Game Changer For Vertex Pharmaceuticals (VRTX)
- Summary: Successful kidney trial could expand product portfolio and revenue.
- Date: 2026-10-26 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxNRjY1MTFrN0lZLXdzNVBJRW4tY2VtQUowMDllMWlIOV9pS1QxUWF6R3h1dVRxUktwa0xkVk1UaGFvbnktX1RXUGtwel9hWDFaRzJpNGxJd1E1Q2JMZmFvdmhsd1pncjJ2UG1FVUVjX0w0Vy15YV9NaW1Id3ZldGg5NmctNmppdTAwSUZ1bFB2NUx5QTgtT05xclBTbDdCMDR5WHp3LXZhNnJiRWg5aV9uNlBGUU5raFF0aTdoTUFpRDZKeksyNlRoa1doOXVlQmVielNjZmxyRGQwVXBoUlFaSUFLREY3cEJ6bE1aZdIB8gFBVV95cUxOdnlmaTJPM2VXamFoN2JQSjAwV05YNEhrQmROXzUwdWdMWURqaUY4RjhXZ1dldmJiR3EwaDNXWGgtMWh0aUhkWlplVXFKY0VxTXgxSHdsZUNFcG5Fb0JCWE9Pd0M1RnJfd2lVMGd0d3A3Ql9keVNKWkNUa3VodnVZVjZpWmFkd0xvNWx5LTFzbk4tTkdDM0tsSHFMNWt3UWlqQVBtazBuOUxoVXNZeEprZ2cyLXRLNGo5a3RBeFlVbGRQTTJrZFFuS2lld2t2TkJ5TW9BRkJzWVpRNHlrbWFlOURKaWEzd0QycEplSmxiVS05Zw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **VRTX** | **31.45** | **6.76** | **25.68** | **12.50** | **136,868,904,960.00 USD** | **29.43** |
| REGN | 20.25 | 2.59 | 16.26 | 16.70 | 84,296,458,240.00 USD | 26.05 |
| BIIB | 108.07 | 1.95 | 15.57 | 10.60 | 36,903,317,504.00 USD | 68.84 |
| AMGN | 28.62 | 21.31 | 16.93 | 9.50 | 249,085,394,944.00 USD | 62.29 |

Peers fetched as_of: 2026-10-29; VRTX reuses existing data (market data as_of: 2026-10-29); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-03
- Next expected earnings: 2026-11-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-29

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-04
- Revenue (latest available single quarter): 640,799,000.00 USD; period 2018-01-01/2018-03-31; fiscal year/reporting period 2018/Q1
- Net income (latest available single quarter): 1,099,800,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/875320/000087532026000259/vrtx-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMipgFBVV95cUxQQVdrekpkclVkTF93RUxySVd2Tm0tYmJibzdpUUNLdlZuZTlwM1A3NWxjcWpxbkNaOEhBUkVSaTcyOVdSd3Zvd29xT3dFMXpYb0N4eEl0MkN0U25BdERES0ZpbG5tTVdOemQxc0lwaVBOVjI3WTB5aERPbndUYWVqMVpzRW1rQnoyVlo4N2VrbzhIZHlXQk9YZExXQnBtMjJFZ0VrUzZR?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNZHJ3T19LVjBFdDc3RUxicks1UUFqdjlYNEZDZ19CNmRZeWdJc0tjbkZiNjY5NlZCSlhUaUtWSzNKbEhValJ1aWtiS2h6SzlyN3hVNzgzMlNzNTVPRzNXZTFlV1BPUHB3U1dUZy1IMWM4c3dDQ2k2bk5mZkd6VDUtazd5aUZVMGpjUTMtVW9reDk4aTBIcWFvUWNxLUFmN2lBR0FDOG1R?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxQc0VzMGtueUtMc3NJN09ZTVpOUTJSaHY1WmdrV3VCTzQ1V0lnVVhFX2ZId2VSV1ZtcTN2aG4zN1pRVVVuSGx6STFzRExxY1lQaGxSN0F0Sm42QTNvMERLRFhZN2ZjdmJrdWlETFpZYThPbVpvYldjYTFZMDdwNDFpS0VsX0lqblM4RUFsYg?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNVlJHemhWaVI4enI0cXRkMTZncnRaMEN3Und6NndBTHFoQ1FaOUZseFZBTmNJaDZUVzd1MHdkd1dPYmd3WDR6M2M3X1BrZ0ZSb053blZYNUpQMWtKTnBack9wdFRNX3g1TnNvTHN3UTVWUGtIQmp1RHFVRDEtX014Tkx0ZDZ6bTMxT3NrTHJXVV9wdkdpSkNBSw?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxQZG5hRkFwbDdac3BTellXczFoU3QxVG5vbGlua09JYzlDTVZlV1l1aENQNjV3blp6WWRQazdwSV9GLWVJRUJnVnNEdTNqTl9zLU1wc3NIS3RfeXJ0OUgyNHhILWFBdTVVVzFMOU1qeGJicDRTa1pNMmtrVTZxcnJreDhKa0RiS0Q0WDRwbDBXN2thT1o3NlpzZW5xQVh0bnJaRWVmb3dCam9PdjRlanpyUnNVV3FkU2MxZU0zd3hyRlRHQ0Rlckk2UzFpNm5MWjlaUUVOTHlpMkhnb1hYN2otYU5KVnBWaGxNVjlqa9IB8gFBVV95cUxNSlRkeFoxU2Q0T0hhTGZLVEVrdlIzWW9fZW9JcnJ3SnlTREE5ejIyVW9mb0tmWVZ0NG1xZUxiaTZMUlVrck90RUlXbHByWE9uWlVZVTFiV1JoWjZXc0JvWVFkQXp4bWRTdjFyQWtRSHF0NWNaa2c4dWlOVkhGSm9POGxFTDdhTDZZenc3c3pDeURBaU5YZjBPOVpHOGhpN3BPWDVJUFZ0M1FTaWxXYlAydW9aLVV0UFk4T3BTZ1h2bllEY2ZLNHlqMzhlb0ZZRmtXamN5Qmg0ZnRxWUliSVY5NGVCS1lMWFIxX0FRQ3dlUXVSZw?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxPT1ZxaXJESVV2dnZLaWJLQlNLVU1MNDdVbFF3M1U1WHE4MUJyWm5LQjVWN3RHMFRrQngxTDNqRUVsTS1XQnlKa2NQZERSRFJnak9DSkNOMktZRVlzRk95NjZldTJ6dGpFNjFKSm5wWmpQZHZPNW9LQkk0SWEwUFhxXzkyLTV3V2ZNbU9yZ3lXa0RGYU83dTQ3NWNQN1VYMVMzb2N1U2x0cm4tSW1hVmlVNWRfeU5rS3c4anVqZk1hRDkzV3VhU1dENlBn?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxPaHpyVVgwQjlCOElOZjJKN3ZLbHJVVV9MMFVoVF8xVWFmUVVzOGlDem9FMnNDek9uSVFKRWd6RGRzTWRRNXFYd0xLQXNjcldEQS1UQ2N6c0NGV2ZobUNOaEVvMFhyZ0ZxU2x2c0psbUdtTi1XY2hvb3VLSFBnQk9JZXdGS1ZfeFdCcE5yVGlTS3JDYlJQS0lPcW13U0JqdkI4eEdIN243dW1QLUpnWU1SaDNNeVFHX2dSZ2lSeGJLYnVOOXdzOGdvbnJvak5jai1nWHJDVmstY2JWSjJWa2VxTkhOMExCVUp5cGdiZNIB8gFBVV95cUxORVdwSVByZlRQa3ZpVVhVVFFRbDIyQ0dMYmdRT3BOTE41RnQ0V0dRdDZNdEFIYmkyRnJzdWwyV3BDUzJFTkhkQUtydzVNYnVJRl9lTUZLU1pZR3hfOVBXVWVYMERTS1M0bDdJdVFfMk1uaU05dkl5ZFRRV2pSTW1wZlpEZlJkeDJWeWE4NGM1TFhaUWQwVHBpajBqVkx0dFltbFpvZzlTeG9nTUFFdWNnOHNLcUpEOGxvUXEtSm56VXliU29SVHl2aHlzQUc0U0JpcWluN1VXSzRRYUM1di1jREd2RkRhX3NLaTlFS1JkVzR2QQ?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPczJ2MDdLWFRNVjdRYm41cFN3M0ZQdmRnT01pbWcwOVQxNUlKNHpYNWlXdmgzYlktVmhsanlSY2tWOU5tSWZSaDRnNUpoN25UTUFJRXJvTmpNMVZXSzlfNkY0Q1RYa1hsdkt1VHRDRWlSdlJMci1yZXU0eXhKbHF0MUdjUExGZXUwV1J4ODBuM3owWTYyTWhxMm1FTWZZX21DMVVITA?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxQbndOUXd4aTItWm1PVnktT1RfalhfVGdBY3lRUGx1b0ZRaGUwd3VnelQ0bzAxa3VCNENEMFVZSEVZZEtIM1JmWnV1eWUxNUF0Z2N6TVhTa1IySk5ROGRCQ19hR3N1T2I3c2djejFMc2psT1hJelg2bHVib3BzRmRjZkp1RTZmQmtNSTE2MFVOOU1RZDUtczlxVTA1djZQV25QbXJTaXNHVQ?oc=5
- https://news.google.com/rss/articles/CBMieEFVX3lxTE5GOHRJNC1Yems2S1BMVXZEWWhWU0hpMHVPTm1YenpFbmZyVERKNmZZbHB2dHNCUDBDZFZRZ0lWV0gzQ2VzZjdiM05uNFdwUURxTG15N1YxRl9yNU9xUUFSMmdSN1I1aksxNkcxWXZiNmUyN2VqMkZ0dw?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPOEVKaXlSbjNjRTEwSDRGODcyR0VTV1B3bmZPbU45ejBOZ0E0RERDRmdwVVBySUZkN0NmOWxjQS10QWNyOVhWWTZJaE5VSWppZVhDMnhGSUs3bFZtUHhSLUlHbVRuOEo1bmdCTkk2cENuV1doMGZmTXJ4cXozMXo4S25MeHB5V3JqVlBnVXlRM19kbTlMdno5SVlTQUgwSXRPZjI5Q0szQQ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQdXJROFhGNXJCQTZoUDlrdDJoU2FieHZidWZmNTY0X2I3WVRoVDYtaEY4ZnhUdTc4VEpmekVJTlh1V3ZFeVd4VjcwdVdhZkpiaDlXdXlxc2ZfQ1NsUm43cl9oRTlONXVyYkp3Z0hXbE9zOG5EdThfM3F4amhWM0RyUHFwN3M5bGVxcUR3R3R4NUxKVG5KSDZVMmhn?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxNRjY1MTFrN0lZLXdzNVBJRW4tY2VtQUowMDllMWlIOV9pS1QxUWF6R3h1dVRxUktwa0xkVk1UaGFvbnktX1RXUGtwel9hWDFaRzJpNGxJd1E1Q2JMZmFvdmhsd1pncjJ2UG1FVUVjX0w0Vy15YV9NaW1Id3ZldGg5NmctNmppdTAwSUZ1bFB2NUx5QTgtT05xclBTbDdCMDR5WHp3LXZhNnJiRWg5aV9uNlBGUU5raFF0aTdoTUFpRDZKeksyNlRoa1doOXVlQmVielNjZmxyRGQwVXBoUlFaSUFLREY3cEJ6bE1aZdIB8gFBVV95cUxOdnlmaTJPM2VXamFoN2JQSjAwV05YNEhrQmROXzUwdWdMWURqaUY4RjhXZ1dldmJiR3EwaDNXWGgtMWh0aUhkWlplVXFKY0VxTXgxSHdsZUNFcG5Fb0JCWE9Pd0M1RnJfd2lVMGd0d3A3Ql9keVNKWkNUa3VodnVZVjZpWmFkd0xvNWx5LTFzbk4tTkdDM0tsSHFMNWt3UWlqQVBtazBuOUxoVXNZeEprZ2cyLXRLNGo5a3RBeFlVbGRQTTJrZFFuS2lld2t2TkJ5TW9BRkJzWVpRNHlrbWFlOURKaWEzd0QycEplSmxiVS05Zw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
