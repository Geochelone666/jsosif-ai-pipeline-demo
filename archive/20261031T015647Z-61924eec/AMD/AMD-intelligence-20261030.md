# AMD Intelligence Report

- ticker: **AMD**
- Report as_of: **2026-10-30**
- Market data as_of: **2026-10-30**
- Quant sources: https://finance.yahoo.com/quote/AMD/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMD/key-statistics/
- AI analysis snapshot as_of: **2026-10-30**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-31T02:09:31.906148+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 9, 'ai': 3, 'unknown': 0, 'irrelevant': 13})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261030T021807Z-b9de7146/AMD** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 18 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 20.0%; oldest publication 2026-10-27

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 504.8000 |
| Return 1D (%) | -10.8789 |
| Return 1W (%) | -2.3201 |
| Return 1M (%) | -17.4840 |
| Return YTD (%) | 135.7116 |
| Return 1Y (%) | 98.0851 |
| Annualized volatility (%) | 69.0333 |
| Beta vs SPY | 3.3070 |
| Max drawdown (%) | -26.4672 |
| Sharpe (rf=0) | 1.3371 |
| Downside deviation (rf=0, %) | 44.0678 |
| Sortino (rf=0) | 2.0946 |
| Historical VaR 95% (1D, %) | 6.0407 |
| Historical ES 95% (1D, %) | 8.5986 |
| Correlation vs SPY | 0.6127 |
| Tracking error vs SPY (%) | 62.0271 |
| P/E (trailing) | 128.78 |
| P/B | 12.26 |
| EV/EBITDA | 85.26 |
| Revenue growth (%) | 50.10 |
| Forward P/E (estimate) | 31.74 |
| Gross margin (%) | 55.72 |
| Operating margin (%) | 17.25 |
| Return on equity (%) | 10.20 |
| Free cash flow yield (%) | 1.07 |
| MA50 | 548.2902 |
| Close vs MA50 (%) | -7.9320 |
| MA200 | 410.4887 |
| Close vs MA200 (%) | 22.9754 |
| RSI (14, Wilder) | 39.6668 |
| MACD (12,26) | -9.0587 |
| MACD signal (9) | -4.0359 |
| MACD histogram | -5.0229 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMD': 272, 'SPY': 272}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 504.8000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -10.8789 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.3201 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -17.4840 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 135.7116 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 98.0851 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 69.0333 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 44.0678 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.0946 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 6.0407 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 8.5986 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6127 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 62.0271 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.3070 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -26.4672 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.3371 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 31.7366 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 55.7240 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 17.2500 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 10.1960 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.0729 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 128.7755 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 39.6668 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -5.0229 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -7.9320 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 22.9754 -> Clearly above the moving-average trend level.

## TAILWINDS

### AMD Stock Faces $500 Support as Big Tech Earnings Shake Semiconductor Rally
- Summary: AMD Stock Faces $500 Support as Big Tech Earnings Shake Semiconductor Rally
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxPWG1FY1J3WGRYTTNpWGo0dEE3empady1CclVyM2JiZk1sYk9oQlVzaHhPYjFNRU5faDBaVGwzcXdEMVJvLUE4dVl3V1h3eUEwVS13YXV6VkhERTQtUmdqc3AwQUhkbzQ1Z1MzV2RlTW5aMUsxX2tfbWY1cXUxOE05TEdIMEVWRm5saVl2UmFLLVhyZy1mTEhlNGJTbHA1ZjUtWnRDVWF2TVpvZkdNY2VjZ3Vma3FkajFn?oc=5>

### AMD Shares Fall 6.5% as Intel’s Weak PC Market Forecast Raises Semiconductor Demand Concerns
- Summary: AMD Shares Fall 6.5% as Intel’s Weak PC Market Forecast Raises Semiconductor Demand Concerns
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxQeUoycS1rbkxSeHhVdV9DR3ZpQkhGem5HUGJNQ3pqM0ctRkE4a0tHdjl4Zi1mZG51dGpQTEdvN0RSTmFVUDJwZ0hYbkpGS2pRVnJIYzBRWWx2S29VajhNeEhZRmJuZmhWeVhzWXdjRFliQ0lybnpVbkd4UFBsUm1NWEFTV1ExbUxBZ0ZNNw?oc=5>

### Was There Any Sign AMD Stock Would Run?
- Summary: Questioning potential upward movement of AMD stock.
- Date: 2026-10-29 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOS3R6ZFFtLVFoNFc1dldRRHZRa2F0RmdpSjF5OGJXVEFtUzcwczVESkZyb05PWVJ2Zkd4NEEzbXFHSGp0ckF6ZXdWNHBSN2JIV0I3c0tFUzRQdmxudDhGeGdibnNuVzVfV3Q1Ul9MNTRma0l5SVRqTENYLTJraGxGUnhwZkYwUGJib0U0bmhEYk5FYWNVSDgyRUViVHdXMnc?oc=5>

### AMD Expands AI Footprint With Meta: Can It Outpace NVDA & AVGO?
- Summary: AMD partners with Meta to expand AI capabilities, aiming to compete with Nvidia and Broadcom.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQcUpTZzVzQVN3dHRNS3Q1M2JxMklqTFhsVUxXUmptSEhPZEVFZmR1RzBpR0dKb0xHaHlJR0ZpdVJodnAyVE1XWEFiUHk2a2tmMy05X2FrRjUwR3ItVnBCbmtwM0VEXzBSaWVuSE53U0ZmRnk0Sm02bHhZZGNoZDlFV3VyTl9fNm1OcHVrczJ0OTVHeEVvUkNGOA?oc=5>

## HEADWINDS

### AMD Stock Drops 8% Ahead of Earnings Despite Wall Street’s 17% Upside Forecast
- Summary: AMD Stock Drops 8% Ahead of Earnings Despite Wall Street’s 17% Upside Forecast
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxPY0I4T0FGOXN0bXFBMkIwb2lQZHViVXZySmhpRVIzbmw0T19fYXZLRC0weUY3QktVY2NIcVI2UG5OeEhZSXpQd0ZnOEhRUGo3bjJRY2kzT016MHFNOEZtMXM1YmJMNFkyVGp0NE90ZloxV3dnY2ZOc3gwQTFjbzAtMFFCLVlVUEM4QS04cG04N0twcl84aVZXcks3ZzdHZzA4WWJFZVV1Tk0?oc=5>

### AMD’s stock slides after Intel earnings reveal two big issues
- Summary: AMD’s stock slides after Intel earnings reveal two big issues
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQSG1ER3NBSmVWMHJlelZ0akVNa1FTVDFlM1J3b2ZMOWZXanV1cVdDblB6dDlHRmJYZDRVZ2JKWTRfRDIyTkZaNENTZVQ2MGFJUjk2X0ZfU2ZTVjZEcm02VlJZXzQyYmlVdHY2Mm5BaEVvUmN0Tm1rQUF2NWlIQTdLMFpWNVl3QUNvX05MRlg0cmw5d1JQWjAxeUtDeHpVandzY2tDZGxn?oc=5>

### AMD Stocks Drop 11% With a $13 Billion Revenue Test Approaching
- Summary: AMD Stocks Drop 11% With a $13 Billion Revenue Test Approaching
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxPcnVwXzVmcFBWcHRxaUVLN3lqallOWWFIanBvM041QV9PTkV5Y0ZvUTNWWTlKTUw1ZFdQYVNYd01lMkR0VUx4WXM1X3FZcEoyTlBsUHZNcEhkTnpLUTdjTGoyNE5lclI3dlEwbVpEVXlhVmMtX29JMjhfRUY2NjhYR2F3MXhKVWdjcE15TmlwcXUybjJJN2V0MnRCeFF3YjJSN2c?oc=5>

### Advanced Micro Devices (NASDAQ:AMD) Stock Price Down 10.9% - What's Next?
- Summary: Advanced Micro Devices (NASDAQ:AMD) Stock Price Down 10.9% - What's Next?
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxPanJaekRUOWdJRFBIV3NJRG5NQWRHUTVLN19GMHN5S0hpTGduck4xTnU1dHlRNU16RWlDeWpqMVNUTzNfUU5fX3FxQUpleThUbkVPeE5RbjBFRzZrY2ZZdkFyM1JheTZkTXhETXo0ZHpZRnIwdjNuTzg0czhHckI4c09mR1M2cHc5RnRNNGZPU2VHMm9JZ1hYLTN0NjdmNkJqdVpRQWdrVWE3LTBiZXJRSzQ2ODdLS2g5TEZlMy1UOGQ5RUE?oc=5>

### AMD stock slides as overbought conditions cap further upside
- Summary: AMD stock slides as overbought conditions cap further upside
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxNTnlmUUZONERYUm5YNmRHSGgxNnNMWFdNb0xUMjVZRXdLVFJCSVlzdjFuZTFjZllVMnNSWXgtZlBLbHVXd21YUGo2SE5zVzk0YkEwMDdEREFsYlJwN0VieFkxQXEzQUx1TkJVN3JWZVI3ODlNd1NyR2hKakljOWM4VDZzTmlzNXhaTDl1V1BESQ?oc=5>

### AMD Stock Falls 11.8% as Intel’s PC Warning Triggers Chip Selloff Ahead of Nov. 3 Results
- Summary: AMD Stock Falls 11.8% as Intel’s PC Warning Triggers Chip Selloff Ahead of Nov. 3 Results
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxNZTl4THRtRklSLWlIcUgxWDJZaktfYUlTN19NM0FsUEdGQk8wQ1RMbVhDSjJSQml4d1JkTzdvTGJxSGsyNnNjMGozX1dfQ0lFMFFtUFR6aXVGeW1DZHBGaXJ1T2Y0dlllQVRjcUl6azVzTGJSYkJnQ3ZHVGtjamduTHJNRXNXU2JTTS1KWUUxa1Bxbll3Rk9JcFFhRWlOTWh2b2Z1cmFUU1Ztem1uZC1Eb0Vn?oc=5>

### Advanced Micro Devices slides 13% as part of tech selloff (AMD:NASDAQ)
- Summary: AMD stock fell 13% amid broader tech selloff, indicating short-term downside pressure.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPWGV3V2xDR1l0WWdPb1JuRk9WYm81cDQxdFB3NHFXUGZUamIxQzk2MTZ3MFFYSkx1c0VPQTNrT09mdmh5UERtTjZvVTBKRXVPc2NwMHJYMVlfZldGNW9CY2xobXpsTmZjUFRtcDE3dTJwemxHNVRRcU1vcG1uZUZZN1lidjJyWnRXRkVlX2w3ZnVmbEkxcG0yX3FB?oc=5>

## CATALYSTS

### AMD Earnings Preview: The Bull Case Is Largely Priced In (NASDAQ:AMD)
- Summary: AMD Earnings Preview: The Bull Case Is Largely Priced In (NASDAQ:AMD)
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxON3lGMDBoeWdCeklWb0RtZGxfSHZMb29uUTUxM1Q5dHgxOWxiaWpOak42R0Q2NzVWMXozbmFKWG5UMmlsOTNQai1aT3l6a1o3UzhXeFZKRFpMTWJwbDg3WnZaUS1DbTNDdHR4ZlRxMi1pVE51QktWQ0Vvay0zZW1HUDE5eFZJVlBPS1dhLVV4Ym1jXzdySDB6ZlJmOFk?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMD** | **128.78** | **12.26** | **85.26** | **50.10** | **824,073,388,032.00 USD** | **98.09** |
| NVDA | 25.87 | 21.58 | 24.41 | 105.90 | 4,941,441,662,976.00 USD | 1.10 |
| INTC | N/A | 2.87 | 29.74 | 25.40 | 349,185,605,632.00 USD | 63.75 |
| AVGO | 41.64 | 15.62 | 30.46 | 85.50 | 1,556,585,250,816.00 USD | -12.74 |

Peers fetched as_of: 2026-10-30; AMD reuses existing data (market data as_of: 2026-10-30); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-04
- Next expected earnings: 2026-11-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-30

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-05
- Revenue (latest available single quarter): 1,584,000,000.00 USD; period 2017-07-02/2017-09-30; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 2,297,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/2488/000000248826000123/amd-20260627.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiuAFBVV95cUxPWG1FY1J3WGRYTTNpWGo0dEE3empady1CclVyM2JiZk1sYk9oQlVzaHhPYjFNRU5faDBaVGwzcXdEMVJvLUE4dVl3V1h3eUEwVS13YXV6VkhERTQtUmdqc3AwQUhkbzQ1Z1MzV2RlTW5aMUsxX2tfbWY1cXUxOE05TEdIMEVWRm5saVl2UmFLLVhyZy1mTEhlNGJTbHA1ZjUtWnRDVWF2TVpvZkdNY2VjZ3Vma3FkajFn?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxQeUoycS1rbkxSeHhVdV9DR3ZpQkhGem5HUGJNQ3pqM0ctRkE4a0tHdjl4Zi1mZG51dGpQTEdvN0RSTmFVUDJwZ0hYbkpGS2pRVnJIYzBRWWx2S29VajhNeEhZRmJuZmhWeVhzWXdjRFliQ0lybnpVbkd4UFBsUm1NWEFTV1ExbUxBZ0ZNNw?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOS3R6ZFFtLVFoNFc1dldRRHZRa2F0RmdpSjF5OGJXVEFtUzcwczVESkZyb05PWVJ2Zkd4NEEzbXFHSGp0ckF6ZXdWNHBSN2JIV0I3c0tFUzRQdmxudDhGeGdibnNuVzVfV3Q1Ul9MNTRma0l5SVRqTENYLTJraGxGUnhwZkYwUGJib0U0bmhEYk5FYWNVSDgyRUViVHdXMnc?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQcUpTZzVzQVN3dHRNS3Q1M2JxMklqTFhsVUxXUmptSEhPZEVFZmR1RzBpR0dKb0xHaHlJR0ZpdVJodnAyVE1XWEFiUHk2a2tmMy05X2FrRjUwR3ItVnBCbmtwM0VEXzBSaWVuSE53U0ZmRnk0Sm02bHhZZGNoZDlFV3VyTl9fNm1OcHVrczJ0OTVHeEVvUkNGOA?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxPY0I4T0FGOXN0bXFBMkIwb2lQZHViVXZySmhpRVIzbmw0T19fYXZLRC0weUY3QktVY2NIcVI2UG5OeEhZSXpQd0ZnOEhRUGo3bjJRY2kzT016MHFNOEZtMXM1YmJMNFkyVGp0NE90ZloxV3dnY2ZOc3gwQTFjbzAtMFFCLVlVUEM4QS04cG04N0twcl84aVZXcks3ZzdHZzA4WWJFZVV1Tk0?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQSG1ER3NBSmVWMHJlelZ0akVNa1FTVDFlM1J3b2ZMOWZXanV1cVdDblB6dDlHRmJYZDRVZ2JKWTRfRDIyTkZaNENTZVQ2MGFJUjk2X0ZfU2ZTVjZEcm02VlJZXzQyYmlVdHY2Mm5BaEVvUmN0Tm1rQUF2NWlIQTdLMFpWNVl3QUNvX05MRlg0cmw5d1JQWjAxeUtDeHpVandzY2tDZGxn?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxPcnVwXzVmcFBWcHRxaUVLN3lqallOWWFIanBvM041QV9PTkV5Y0ZvUTNWWTlKTUw1ZFdQYVNYd01lMkR0VUx4WXM1X3FZcEoyTlBsUHZNcEhkTnpLUTdjTGoyNE5lclI3dlEwbVpEVXlhVmMtX29JMjhfRUY2NjhYR2F3MXhKVWdjcE15TmlwcXUybjJJN2V0MnRCeFF3YjJSN2c?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxPanJaekRUOWdJRFBIV3NJRG5NQWRHUTVLN19GMHN5S0hpTGduck4xTnU1dHlRNU16RWlDeWpqMVNUTzNfUU5fX3FxQUpleThUbkVPeE5RbjBFRzZrY2ZZdkFyM1JheTZkTXhETXo0ZHpZRnIwdjNuTzg0czhHckI4c09mR1M2cHc5RnRNNGZPU2VHMm9JZ1hYLTN0NjdmNkJqdVpRQWdrVWE3LTBiZXJRSzQ2ODdLS2g5TEZlMy1UOGQ5RUE?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxNTnlmUUZONERYUm5YNmRHSGgxNnNMWFdNb0xUMjVZRXdLVFJCSVlzdjFuZTFjZllVMnNSWXgtZlBLbHVXd21YUGo2SE5zVzk0YkEwMDdEREFsYlJwN0VieFkxQXEzQUx1TkJVN3JWZVI3ODlNd1NyR2hKakljOWM4VDZzTmlzNXhaTDl1V1BESQ?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxNZTl4THRtRklSLWlIcUgxWDJZaktfYUlTN19NM0FsUEdGQk8wQ1RMbVhDSjJSQml4d1JkTzdvTGJxSGsyNnNjMGozX1dfQ0lFMFFtUFR6aXVGeW1DZHBGaXJ1T2Y0dlllQVRjcUl6azVzTGJSYkJnQ3ZHVGtjamduTHJNRXNXU2JTTS1KWUUxa1Bxbll3Rk9JcFFhRWlOTWh2b2Z1cmFUU1Ztem1uZC1Eb0Vn?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPWGV3V2xDR1l0WWdPb1JuRk9WYm81cDQxdFB3NHFXUGZUamIxQzk2MTZ3MFFYSkx1c0VPQTNrT09mdmh5UERtTjZvVTBKRXVPc2NwMHJYMVlfZldGNW9CY2xobXpsTmZjUFRtcDE3dTJwemxHNVRRcU1vcG1uZUZZN1lidjJyWnRXRkVlX2w3ZnVmbEkxcG0yX3FB?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxON3lGMDBoeWdCeklWb0RtZGxfSHZMb29uUTUxM1Q5dHgxOWxiaWpOak42R0Q2NzVWMXozbmFKWG5UMmlsOTNQai1aT3l6a1o3UzhXeFZKRFpMTWJwbDg3WnZaUS1DbTNDdHR4ZlRxMi1pVE51QktWQ0Vvay0zZW1HUDE5eFZJVlBPS1dhLVV4Ym1jXzdySDB6ZlJmOFk?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
