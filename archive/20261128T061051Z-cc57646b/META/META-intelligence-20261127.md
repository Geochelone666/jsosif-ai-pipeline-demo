# META Intelligence Report

- ticker: **META**
- Report as_of: **2026-11-27**
- Market data as_of: **2026-11-27**
- Quant sources: https://finance.yahoo.com/quote/META/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/META/key-statistics/
- AI analysis snapshot as_of: **2026-11-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-28T06:25:01.033222+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 4, 'ai': 9, 'unknown': 0, 'irrelevant': 11})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **10** exact headline/source/date matches; prior report **20261127T063646Z-c0c26981/META** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 12 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-11-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 628.9600 |
| Return 1D (%) | 3.1268 |
| Return 1W (%) | 12.1461 |
| Return 1M (%) | 1.4141 |
| Return YTD (%) | -4.4707 |
| Return 1Y (%) | -0.3972 |
| Annualized volatility (%) | 42.7651 |
| Beta vs SPY | 1.3968 |
| Max drawdown (%) | -28.7332 |
| Sharpe (rf=0) | 0.1494 |
| Downside deviation (rf=0, %) | 28.4054 |
| Sortino (rf=0) | 0.2249 |
| Historical VaR 95% (1D, %) | 3.9010 |
| Historical ES 95% (1D, %) | 5.8049 |
| Correlation vs SPY | 0.4906 |
| Tracking error vs SPY (%) | 37.7377 |
| P/E (trailing) | 20.75 |
| P/B | 5.90 |
| EV/EBITDA | 14.12 |
| Revenue growth (%) | 26.10 |
| Forward P/E (estimate) | 17.69 |
| Gross margin (%) | 81.03 |
| Operating margin (%) | 37.78 |
| Return on equity (%) | 32.26 |
| Free cash flow yield (%) | 1.05 |
| MA50 | 671.3393 |
| Close vs MA50 (%) | -6.3126 |
| MA200 | 626.6678 |
| Close vs MA200 (%) | 0.3658 |
| RSI (14, Wilder) | 50.3413 |
| MACD (12,26) | -15.2557 |
| MACD signal (9) | -17.4487 |
| MACD histogram | 2.1930 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'META': 291, 'SPY': 291}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 628.9600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 3.1268 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 12.1461 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 1.4141 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -4.4707 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -0.3972 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 42.7651 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 28.4054 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.2249 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.9010 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.8049 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4906 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.7377 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.3968 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.7332 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1494 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.6883 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 81.0340 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 37.7770 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 32.2640 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.0479 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 20.7509 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 50.3413 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 2.1930 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -6.3126 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 0.3658 -> Slightly above the moving-average trend level.

## TAILWINDS

### Meta Stock Climbs: What's Going On?
- Summary: Meta Stock Climbs: What's Going On?
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNbjFJTkRlT3l6WjFMc3hyNWNISGpoemg3S0FROWtKRnU3ck5YY2hTSzRQdnVVTnpabVR4M3d4NEdoVXMtdmdJU0ZkYk45cVBKdjNfSkpXX3VFQjhiZ3dtNVFYOVBtS2xJWFk4OHNxaXNnUWx5Vnh6WVZCUkhnSUx1eWo2UVJjdlMzR2d1R1pmRVJvM0tCNnJ0ZA?oc=5>

### Meta Platforms Inc Stock (META) Moved Up by 3.52% on Nov 27: Facts Behind the Movement
- Summary: Meta Platforms Inc Stock (META) Moved Up by 3.52% on Nov 27: Facts Behind the Movement
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxPamIxN3Z6LVNiZzBvVzUxZFVGLURpb094al9sNm9TckQ2RjlUNjZVdVVuNVBhUE1Gc3Y4ZUpwLUFwWEx2MTRIS1pGaVJVMGdOMnc1TGdtTXVJQ2hfX1FVNTZiTjc4a01RMDI0dUFMSV9MSjRwX0UxczQxc1NfUHNnMEU5aFpUM19iX1NF?oc=5>

### Meta Platforms (META) Expands Muse Shopping In The UK, Is The Stock Still A Bargain?
- Summary: Meta launches Muse Shopping in the UK, expanding e-commerce presence.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOdjEyTVRlcWZuVV9PRHBXVFFkUGRqem8zWVh6R2tqb0lfb19HR1BpaTgtZ185eGFKWXpsakNra2dwMWNtU25sYlNaTjJOSjYxRS1YbERkZ0I4UHlEa0JJUHBLOVlOd0hoWTJpOGF1U25pTGVldl9pbzhfclFacXE1T056SXVqbUdsTnV0c2k2RHJDU0t6dTlLLXlTU1NFZw?oc=5>

### Meta Platforms Just Partnered With Walmart. Here's Why Investors Should Pay Attention
- Summary: Meta partners with Walmart, expanding retail reach and e-commerce integration.
- Date: 2026-11-26 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxOR0ZSZzdRU1E0Y05jU21DdC0yZUltMGpXYnFITXBBeTRaXzZXU3I1Y2tCeTNPSjdXbjlSVFVfUWxrcTNITXRKakQzSzM5S1dKcG5GTDdndk9lRy1FdGNlN3Z3U2JYdFZaNUxjendwbVVKdVllMm1CUUxMOTZnN3hORy1TdDk4RERmdEhIcjVQTjAzVnhzOU9BRFJVbmM2ZldpWDRV?oc=5>

## HEADWINDS

### META Stock Is Down 24% From Peak: JPMorgan Sees ‘Attractive Buying Opportunity’ — But 2027 Spending, Capex Remain An Overhang
- Summary: META Stock Is Down 24% From Peak: JPMorgan Sees ‘Attractive Buying Opportunity’ — But 2027 Spending, Capex Remain An Overhang
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNSk9fRUN4RmFOTWdZSWVDRzFCTVU3akVWVldXOFhSWkhvdm5WUlFQczhPc2h0b1JHSHM4WU0xZk1FYkdkSmJ4Y3pXVTZ0UVZOV1JKVF9TcGFmbFU5VDJwTUF3QTJGN3pZbHVTQl9PVFVzTlVKR2lRSnhfY1UteTU0UzI5WjI3cG1vQW1uVloxcHZpdw?oc=5>

### Why is Meta Platforms stock sliding today?
- Summary: Meta stock experiencing a decline, indicating market concerns.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPZDhvWjk4QWhGdVJpM1JuQVRYbkc5Z0tpNGxSZWgzLWdPRE5LaHpvMW1lVV9VSFljNXlUaTVVYk0xZEtvamZDVnR4RERGOVdoQlJSdjhhVHgzLWNIOTNNZ1JGWkI0NEtVcHUxbW8xYUVyMFozREVDZXZXVWVtS0lDa3piQ3FUa29kQVg3TlZrdVBEWHpHb3F1MGVDZWRNMlNEZlBFdWhR?oc=5>

## CATALYSTS

### Meta Platforms, Inc. $META Stock Sold by EP Wealth Advisors LLC
- Summary: Meta Platforms, Inc. $META Stock Sold by EP Wealth Advisors LLC
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxOcTFBVzNRQ2VraXNkaXpGeGY4NVE2MmFOTXZ4bFBSbWxHWVdid05FZzF4QkJ0Nmw4cC1zSTJ0S2xHQ2FNQWZ5OW5YTEVyT25lRjN4TDc2ODdLQmVwVkRZNmY5UC1JSUpkNHNJS0NYajNaSFhsYTlnTExDN05VM09TdG9xRm1uQzQwN2J4SGl0Q0dqSXprSkUwODdPNGVMOXhBNFZiSVhnQU1kN0swOVBYU0pybjNjbF84M1k1RjJR?oc=5>

### What Moved Meta Stock?
- Summary: Factors behind recent Meta share movement examined.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxOVzNJQmsyN0VLTFFUNmNBS2VXYzhrdnFFa2J5Mi0zSGxCaHFFWlRRZEhZWklGT3c4SGVlcmhFY2RkNkNTbHYxRUZnem1sRHU3Wkp2c2s0dzRiRjlHaUFDNkdrWC1QQlZpeXVkYkZYeDkxRUtUVnNaazVubFNNZXlrdzE2MTBYVWZMbmc?oc=5>

### Meta Stock Dips: What's Going On?
- Summary: Meta shares fell, prompting analysis of causes.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxONG1USC01dW5MV05MYS0tLU45d2lZeUJBc0Z1LWVxSHBtMk9SUEhvN2I0WDBBMG90bWpFQ1dNbmlKUWxzN2xoTnZaa2dMakRsZkxVZWRxdXdmT3pfRXpDUUtQSHFUdXFZQnhDNjNtYUxCa3UwRlRRZ3F6cGZMdVN2bXlUbTVuaTUwWFhuMk9tcE1rcGFVYkE?oc=5>

### Meta Says Muse “Raises Conversions for Advertisers.” It Already Places 51% of AI Agent Orders
- Summary: Meta’s Muse AI tool boosts advertiser conversions, handling 51% of AI agent orders, signaling stronger ad performance and product innovation.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxQVkpCOFRMbmZiUk9ZVUtmbXpuSnR4OGZ2aDBlRzdfSGc0WlB2UE52TTQyYl9mdTZyZnFjYUdVRGpqaS1rSE4yVUxERHZURVVkdTFQTHpub3Z2bGN1Nmg5d3kwbDZ6b0QzVDd6alJVR2dLYklIaGRxRGxRYV8zcENnaVctRzZqaUZfS0RGbjAtQmZYSUl1MjJSMXJZTXhsZm9fcUxv?oc=5>

### Meta Platforms (NASDAQ:META) Stock Price Up 3.2% - Time to Buy?
- Summary: Meta shares rise 3.2%, indicating positive market sentiment.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxNMzR4cjhpMHNZRDJ6QlhPM3NkSlRCMzFwUThDZ3RCZ0VuaGFRSm1HUHVBN1BaSVJ5eUF3bXVNUDRyZmJkVnltMFNhRW0yeU9aM2dPYmp1MGV0clY0TGxYcGduakpsN01sZWhPUFhERU9vUnhHRUNrV2IycDA5cEE2OXAzVW1uTjZGcFd0cFNHYVBPbkhpR2tBOFhGdW1PTno3X1NkNm9QeXQ3eGFqMTJIenlWYkJpbGM?oc=5>

### Could Meta Actually Climb 30%? Or Is J.P. Morgan Totally Wrong?
- Summary: Analyst speculation on Meta’s potential upside versus JPMorgan’s view.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPTldyek1ZUXRseDBnejUwbTVtakZCbTR3QXVYNDA1TlJVd1pGaXpmNzRsaFV6S1R0YzB1QXNtNE80Z2FxOUtEaEVZTXc0T0R5bXliYTlpT054MG4tUnNSRFUwVUwzTWVEWVp4Q3NCVEJobjVhWnBCWjB2d3hlYUxGYUlCS0tDa2gxSVJjNGRMNnFhSWMyTjVPZQ?oc=5>

### Top Stock Reports for Alphabet, Meta & Bank of America
- Summary: Analyst reports covering Meta among other firms.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNRVRGbHZBMVR5U0hMbnEweGRkMjk0NGtKcTcxaGc0aW1CVlBZNThuVldyOW1EV1l3VzlnOWZkVWNXcDlYaWZkYy1ZRVBab05sSWtwVmJoN0RmSWp2eGlBTHdnUE5VVm1GMVY0MXZpZG91cS1jQUZMb2o2cjFxWk9rM09ZYUp4OUNLWnVZZFFValZkajU2MEZJazVGTW0?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **META** | **20.75** | **5.90** | **14.12** | **26.10** | **1,607,773,454,336.00 USD** | **-0.40** |
| GOOGL | 14.36 | 5.13 | 17.70 | 24.70 | 3,380,358,152,192.00 USD | -13.84 |
| SNAP | N/A | 4.00 | 54.47 | 14.30 | 8,960,933,888.00 USD | -31.80 |
| PINS | 84.67 | 3.75 | 38.43 | 11.90 | 11,653,679,104.00 USD | -20.53 |

Peers fetched as_of: 2026-11-27; META reuses existing data (market data as_of: 2026-11-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-27

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-22
- Revenue (latest available single quarter): 13,727,000,000.00 USD; period 2018-07-01/2018-09-30; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 9,860,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimAFBVV95cUxNbjFJTkRlT3l6WjFMc3hyNWNISGpoemg3S0FROWtKRnU3ck5YY2hTSzRQdnVVTnpabVR4M3d4NEdoVXMtdmdJU0ZkYk45cVBKdjNfSkpXX3VFQjhiZ3dtNVFYOVBtS2xJWFk4OHNxaXNnUWx5Vnh6WVZCUkhnSUx1eWo2UVJjdlMzR2d1R1pmRVJvM0tCNnJ0ZA?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxPamIxN3Z6LVNiZzBvVzUxZFVGLURpb094al9sNm9TckQ2RjlUNjZVdVVuNVBhUE1Gc3Y4ZUpwLUFwWEx2MTRIS1pGaVJVMGdOMnc1TGdtTXVJQ2hfX1FVNTZiTjc4a01RMDI0dUFMSV9MSjRwX0UxczQxc1NfUHNnMEU5aFpUM19iX1NF?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOdjEyTVRlcWZuVV9PRHBXVFFkUGRqem8zWVh6R2tqb0lfb19HR1BpaTgtZ185eGFKWXpsakNra2dwMWNtU25sYlNaTjJOSjYxRS1YbERkZ0I4UHlEa0JJUHBLOVlOd0hoWTJpOGF1U25pTGVldl9pbzhfclFacXE1T056SXVqbUdsTnV0c2k2RHJDU0t6dTlLLXlTU1NFZw?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxOR0ZSZzdRU1E0Y05jU21DdC0yZUltMGpXYnFITXBBeTRaXzZXU3I1Y2tCeTNPSjdXbjlSVFVfUWxrcTNITXRKakQzSzM5S1dKcG5GTDdndk9lRy1FdGNlN3Z3U2JYdFZaNUxjendwbVVKdVllMm1CUUxMOTZnN3hORy1TdDk4RERmdEhIcjVQTjAzVnhzOU9BRFJVbmM2ZldpWDRV?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxPV2ozQV9ELWd0VnN0Y0VXUENOLXo3aUZZRXpIaU9XcG5jMXdLNksxZ1JDb0JiR2V1N3dLTGNfQS1SZ2hhb0ZwdDM0Z09EOWlOdU1MQmNjTlFvc3dYNnRlN2wxNnZjLUhkdW1kQl9uR2JuT2lJSGNSUW1qdTdPbTRMTmoza1pkc2ljNnpKNnNWTE9URFlaSnd4eDN2TXgyQjRtVVlBOW5hWXl4S1lCRk1EX2hwVTU2N1VJQnllT1ppQ2E2ZzhRT3c?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNSk9fRUN4RmFOTWdZSWVDRzFCTVU3akVWVldXOFhSWkhvdm5WUlFQczhPc2h0b1JHSHM4WU0xZk1FYkdkSmJ4Y3pXVTZ0UVZOV1JKVF9TcGFmbFU5VDJwTUF3QTJGN3pZbHVTQl9PVFVzTlVKR2lRSnhfY1UteTU0UzI5WjI3cG1vQW1uVloxcHZpdw?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPZDhvWjk4QWhGdVJpM1JuQVRYbkc5Z0tpNGxSZWgzLWdPRE5LaHpvMW1lVV9VSFljNXlUaTVVYk0xZEtvamZDVnR4RERGOVdoQlJSdjhhVHgzLWNIOTNNZ1JGWkI0NEtVcHUxbW8xYUVyMFozREVDZXZXVWVtS0lDa3piQ3FUa29kQVg3TlZrdVBEWHpHb3F1MGVDZWRNMlNEZlBFdWhR?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxOcTFBVzNRQ2VraXNkaXpGeGY4NVE2MmFOTXZ4bFBSbWxHWVdid05FZzF4QkJ0Nmw4cC1zSTJ0S2xHQ2FNQWZ5OW5YTEVyT25lRjN4TDc2ODdLQmVwVkRZNmY5UC1JSUpkNHNJS0NYajNaSFhsYTlnTExDN05VM09TdG9xRm1uQzQwN2J4SGl0Q0dqSXprSkUwODdPNGVMOXhBNFZiSVhnQU1kN0swOVBYU0pybjNjbF84M1k1RjJR?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxOVzNJQmsyN0VLTFFUNmNBS2VXYzhrdnFFa2J5Mi0zSGxCaHFFWlRRZEhZWklGT3c4SGVlcmhFY2RkNkNTbHYxRUZnem1sRHU3Wkp2c2s0dzRiRjlHaUFDNkdrWC1QQlZpeXVkYkZYeDkxRUtUVnNaazVubFNNZXlrdzE2MTBYVWZMbmc?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxONG1USC01dW5MV05MYS0tLU45d2lZeUJBc0Z1LWVxSHBtMk9SUEhvN2I0WDBBMG90bWpFQ1dNbmlKUWxzN2xoTnZaa2dMakRsZkxVZWRxdXdmT3pfRXpDUUtQSHFUdXFZQnhDNjNtYUxCa3UwRlRRZ3F6cGZMdVN2bXlUbTVuaTUwWFhuMk9tcE1rcGFVYkE?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQVkpCOFRMbmZiUk9ZVUtmbXpuSnR4OGZ2aDBlRzdfSGc0WlB2UE52TTQyYl9mdTZyZnFjYUdVRGpqaS1rSE4yVUxERHZURVVkdTFQTHpub3Z2bGN1Nmg5d3kwbDZ6b0QzVDd6alJVR2dLYklIaGRxRGxRYV8zcENnaVctRzZqaUZfS0RGbjAtQmZYSUl1MjJSMXJZTXhsZm9fcUxv?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxNMzR4cjhpMHNZRDJ6QlhPM3NkSlRCMzFwUThDZ3RCZ0VuaGFRSm1HUHVBN1BaSVJ5eUF3bXVNUDRyZmJkVnltMFNhRW0yeU9aM2dPYmp1MGV0clY0TGxYcGduakpsN01sZWhPUFhERU9vUnhHRUNrV2IycDA5cEE2OXAzVW1uTjZGcFd0cFNHYVBPbkhpR2tBOFhGdW1PTno3X1NkNm9QeXQ3eGFqMTJIenlWYkJpbGM?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPTldyek1ZUXRseDBnejUwbTVtakZCbTR3QXVYNDA1TlJVd1pGaXpmNzRsaFV6S1R0YzB1QXNtNE80Z2FxOUtEaEVZTXc0T0R5bXliYTlpT054MG4tUnNSRFUwVUwzTWVEWVp4Q3NCVEJobjVhWnBCWjB2d3hlYUxGYUlCS0tDa2gxSVJjNGRMNnFhSWMyTjVPZQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNRVRGbHZBMVR5U0hMbnEweGRkMjk0NGtKcTcxaGc0aW1CVlBZNThuVldyOW1EV1l3VzlnOWZkVWNXcDlYaWZkYy1ZRVBab05sSWtwVmJoN0RmSWp2eGlBTHdnUE5VVm1GMVY0MXZpZG91cS1jQUZMb2o2cjFxWk9rM09ZYUp4OUNLWnVZZFFValZkajU2MEZJazVGTW0?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
