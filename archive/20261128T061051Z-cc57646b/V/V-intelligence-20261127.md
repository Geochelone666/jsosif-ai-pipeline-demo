# V Intelligence Report

- ticker: **V**
- Report as_of: **2026-11-27**
- Market data as_of: **2026-11-27**
- Quant sources: https://finance.yahoo.com/quote/V/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/V/key-statistics/
- AI analysis snapshot as_of: **2026-11-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-28T06:33:40.797184+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 5, 'ai': 7, 'unknown': 0, 'irrelevant': 13})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **15** exact headline/source/date matches; prior report **20261127T063646Z-c0c26981/V** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 11 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 20.0%; oldest publication 2026-11-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 429.5600 |
| Return 1D (%) | 1.2182 |
| Return 1W (%) | 6.8903 |
| Return 1M (%) | 7.0908 |
| Return YTD (%) | 23.4465 |
| Return 1Y (%) | 29.7041 |
| Annualized volatility (%) | 23.3306 |
| Beta vs SPY | 0.3298 |
| Max drawdown (%) | -17.1805 |
| Sharpe (rf=0) | 1.2312 |
| Downside deviation (rf=0, %) | 14.4805 |
| Sortino (rf=0) | 1.9836 |
| Historical VaR 95% (1D, %) | 1.8438 |
| Historical ES 95% (1D, %) | 2.9273 |
| Correlation vs SPY | 0.2123 |
| Tracking error vs SPY (%) | 24.9228 |
| P/E (trailing) | 34.87 |
| P/B | 22.41 |
| EV/EBITDA | 25.00 |
| Revenue growth (%) | 13.20 |
| Forward P/E (estimate) | 25.06 |
| Gross margin (%) | 97.68 |
| Operating margin (%) | 66.31 |
| Return on equity (%) | 63.51 |
| Free cash flow yield (%) | 2.62 |
| MA50 | 397.8710 |
| Close vs MA50 (%) | 7.9646 |
| MA200 | 349.8206 |
| Close vs MA200 (%) | 22.7944 |
| RSI (14, Wilder) | 62.0321 |
| MACD (12,26) | 4.8964 |
| MACD signal (9) | 5.7668 |
| MACD histogram | -0.8704 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'V': 291, 'SPY': 291}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 429.5600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.2182 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 6.8903 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 7.0908 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 23.4465 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 29.7041 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 23.3306 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.4805 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.9836 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.8438 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.9273 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2123 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.9228 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3298 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -17.1805 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.2312 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 25.0613 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 97.6780 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 66.3070 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 63.5070 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.6181 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 34.8669 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 62.0321 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.8704 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 7.9646 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 22.7944 -> Clearly above the moving-average trend level.

## TAILWINDS

### Visa (NYSE:V) Stock Price Up 2% - Still a Buy?
- Summary: Visa (NYSE:V) Stock Price Up 2% - Still a Buy?
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNb0txc0pfOU9wa0Rrd3hxbXJmSHA5dExXR0RpcGs4N3p1NkREX2taSDU5YW5WbUczU3lqVjB5aTNreWlTR0Noc1o2c2VMalM2T2wzTVlMLWRrajgwU2FzY19STUpSV1NRZHkxR1ZGV2hJMkJlOTF4bkdpbklPSHp0bXAtOTNhSE8ydnpmckRJSVM0VXc3MEhtMHlrZWpaWVJyUUE?oc=5>

### Visa (NYSE:V) Stock Jumps 2.1% - What's Next?
- Summary: Visa (NYSE:V) Stock Jumps 2.1% - What's Next?
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPNTNUbEtEN3lTRHcwNHFQY2ZpZVk0LU1GbWkxR2JKWXRya1QxUFBNeFFqdFNTS3VMQ0I5T2NOQ20zM0wzaF9sTHV4cGNOSmUzSEVhUEhMZWxuZjhqRndOcFdEQVAzVlVIY3N3VmxQODZZRVV1NGhnUm1rd3dDYll6dWx3MTJpaExEdS0yakpHNUM3UW1ZRkI0X0YwVTJQUQ?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Visa Paid About $335 per Share to Buy Back $20.5 Billion of Its Stock Last Year. Would You Pay $400?
- Summary: Visa Paid About $335 per Share to Buy Back $20.5 Billion of Its Stock Last Year. Would You Pay $400?
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4AFBVV95cUxOMUQ3UEh2ekRkV19vY3ZyX0t0ZHo5czVrSjlzSnpwS29oVzFpckZIZUltZC1nY3IxVGw4a0NxaWVucHZNcDVVejdEdXRJWHEwLTY0c2hUdFd2aFBERlNmOTlYdDFCeDJldlZ6VFBaem8yeXdTbXVuVEhCV3A5Zk1wTmlSb2s5QmdEQkFkMFphOXM3VVBmM1RJeE05V1J1a29ZT3BNWlRFNTlEd1BTUkdXRjMzTnJocEx3b3pQaUZqSEpmekRoN09VRTdtNkNsS3dTVGxaUl9hWnlQa01yc3dlVQ?oc=5>

### Visa Inc. $V Stock Purchased by Toronto Dominion Bank
- Summary: Visa Inc. $V Stock Purchased by Toronto Dominion Bank
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxQVjdVTTNkdlhLYklHSjlGT19ubTAzUk9tMHZZell6aUt6WHh0MEJBdThsWjE4SzE1ZG5Lc1hpcV9WR0hhN0FsZkZQZTgwN0NQelA0SmNQeTBKMEpqYjBQZEN4SGc1eDVuejMxd0l6X1JjUjZMTnJsZ0pRMFBOaDR5X2tfXzlhZFlaeFZYOGJhSDl2TnlQTlJIOS0tb0RxU3Rqb0pIZVdESlpMNzlTbnRKZFh3?oc=5>

### Visa grants CEO Ryan McInerney performance stock option valued at about $50 million
- Summary: Visa grants CEO Ryan McInerney performance stock option valued at about $50 million
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3AFBVV95cUxNNVpXejg4bmNOOVg3V3A1em9OVkN5VHVnMjZfMVRkSHJXTUo4SkRlMkJubkVidGhwRXBieS1rSzdWZUhEenRjbzVXNTZiUElHNkhiUHpwZjhOd3BrNGRCXzNMNE80Q1BwdlJYN0FySnRDUkVaUE5JMkVHLTJpSjBrNUx0TUxDZzZaNktMdmgwOHBqUkdsM1M5VGdSQmpyN052NlZTTlAyUFN0OG5VbmxmYmR3YkJOclN1MUdmbXExdzBULXZOWDNrSjNDOXM2YTlLRktYb1RqWC1WWk5K?oc=5>

### Visa (V) Stock May Be 15% Undervalued After Swipe Fee Delay
- Summary: Visa’s stock may be undervalued due to a delay in swipe fee implementation, potentially affecting investor perception.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxPNzRKVWJlZDl6aDM3dHFBQ05oanJ2QURnR25lUDh1RVdUZGlwTUR1OVU5SEd5bUFEU0pCVDg3NGZ2azRoUzRBOHEycWlZa1Ftam95NmMwWnE4S0J2cWY1ajd5SEJtM2tGTS1YcW90VjNtMlNTWlFSa3NPVEFXNExiRU9WSHNCNzIzb01YTQ?oc=5>

### Visa awards to CEO $50M stock grant linked to stock performance (V:NYSE)
- Summary: CEO granted $50M stock award tied to performance, indicating incentive alignment.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxOYV8wLUxVOEZjaXE5aGY4UjNnLW9ZNTRJUGtORl9OeEtxSm04dk5RbUp6SmUzUFJQbjFzNlBZdjl0VUxqQjVnYkxlN2w5NWxuUm5US0NJdzZGNlY4TUZRSTlaRmxSX09TTGJLLUtXWlVLUzlhWlpGWUZyV1lQc3VKeGc1cHRvYzduYmh5RFNpOHp5U2tTelJRSHdpUGxTd2dyMlE?oc=5>

### Visa Approves Performance Stock Award for CEO
- Summary: CEO receives performance-based stock award, reflecting executive compensation strategy.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxQeXhIejFMVG9jQzVfR0UxSGVBUEFmYW13NG5yeXByT0xxREdTcG13Y0thTVpPcElfR3ExYktseXRVRThUcE56Zlk3MVVpTUUyYTc4OGxwVTBBdTNYcHJPQjcwa1c4aUh4eFUwcEJxSXhMX25IeUZ3SEl3Slp5ZkMzdFJ0bEJXd2g0Y3poZ081NUJkNTZpMkstMGxueTl1dl8yUXNDaXNEMldFTXpESVluNUNBNjJVU0Z4YjR0dnc3MTJuZmdWSXc?oc=5>

### Visa (V) grants Julie B. Rottenberg 22,201 stock options with a $402.25 exercise price.
- Summary: Executive granted options, supporting retention and incentive alignment.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOc1BrQUxiTl91cThBREhMNzVaVnVPS2VkRG11Nm0xVThiUEd3dHk4ZW5WSGpOaWprb3d3X2J5blhMZVl5T3EzUFhGZGdmZlRvclM2aS1vMHF5dlRCTDRfOFF2N2tVRmVFMXc5TTlwOW10LVU2d0puazEzR0NWelpxcXY0aUFRWVh4RC1wM0VOazBITk5BVmg0MlJyQ3BfQzdZ?oc=5>

### Visa (V) grants its vice chair 23,434 options with a $402.25 exercise price and a 2036 expiration.
- Summary: Vice chair awarded options, reinforcing executive alignment with company performance.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPck1yVkQyYUg0aUN5OUtxV2l4ZGktMTFnZnhZdTVkcUxna1ItNnR4bHJhTmFvV3pHSzYtNUx2QmJlQnRELUN4cEp0dU9IdWpISHhCajZtN2xUYTNueWhycUJhWG9WV2tiME1hTWE3eEN1eHpaRXdZQ2FXc05ua3loWFZmd29JakY2YmN4QXpwNlkyTGZ4SV9ra0pVQ1BGWmhG?oc=5>

## RISKS

### Visa: Paying A Pretty Penny For Stability (Rating Downgrade) (NYSE:V)
- Summary: Visa received a rating downgrade, indicating potential credit risk.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQMXJUSGZtR1ZhcTcyLVcyejBYaUN6Q3AwTnVaOGFDOThqUm1PTjNTb1N0YmRDVk8yQW1ZVW1tYVlkZDctekJVMV9zcTd6aWM4TURYV1NrVExYdEdTYlpyZFp3aDQyamVsYk5jZFExMWNZR01sb05wR05EVmx2TmZTM0xueFVQS2ktSDRtaV90NVk1eVl1Mnc?oc=5>

### Visa: The Market Finally Recognizes Its Strength (Rating Downgrade) (NYSE:V)
- Summary: Credit rating downgrade signals potential credit risk and market concerns for Visa.
- Date: 2026-11-24 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOUVZxdjdndTdJYVJGRlBKMFNYZmlFcExERDRUeUF5cTc2MUN2a3JETk1iekxRQlZnMDBwVmZITUItd0FrbEFpTVA2SEhFMnNGZHhPcV9ZQ1NDZnVXa0tmWHdwMGxGb0psSkliYVl4QnN6eFp0MW01VDd1OXluX1FPRW9rMmtHWWpuYk9RT2pPV2pTNWdjT0hMWTdSRnB4dk0?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **V** | **34.87** | **22.41** | **25.00** | **13.20** | **801,473,101,824.00 USD** | **29.70** |
| MA | 34.90 | 86.14 | 25.82 | 14.00 | 581,039,620,096.00 USD | 23.18 |
| PYPL | 11.29 | 2.54 | 8.14 | 2.00 | 49,125,130,240.00 USD | -3.51 |
| AXP | 17.83 | 5.93 | N/A | 11.30 | 212,162,641,920.00 USD | -12.09 |

Peers fetched as_of: 2026-11-27; V reuses existing data (market data as_of: 2026-11-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-27
- Next expected earnings: 2027-01-26 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-27

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-11-05
- Revenue (latest available single quarter): 5,840,000,000.00 USD; period 2019-04-01/2019-06-30; fiscal year/reporting period 2019/Q3
- Net income (latest available single quarter): 5,628,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1403161/000140316126000134/v-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiogFBVV95cUxNb0txc0pfOU9wa0Rrd3hxbXJmSHA5dExXR0RpcGs4N3p1NkREX2taSDU5YW5WbUczU3lqVjB5aTNreWlTR0Noc1o2c2VMalM2T2wzTVlMLWRrajgwU2FzY19STUpSV1NRZHkxR1ZGV2hJMkJlOTF4bkdpbklPSHp0bXAtOTNhSE8ydnpmckRJSVM0VXc3MEhtMHlrZWpaWVJyUUE?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPNTNUbEtEN3lTRHcwNHFQY2ZpZVk0LU1GbWkxR2JKWXRya1QxUFBNeFFqdFNTS3VMQ0I5T2NOQ20zM0wzaF9sTHV4cGNOSmUzSEVhUEhMZWxuZjhqRndOcFdEQVAzVlVIY3N3VmxQODZZRVV1NGhnUm1rd3dDYll6dWx3MTJpaExEdS0yakpHNUM3UW1ZRkI0X0YwVTJQUQ?oc=5
- https://news.google.com/rss/articles/CBMi4AFBVV95cUxOMUQ3UEh2ekRkV19vY3ZyX0t0ZHo5czVrSjlzSnpwS29oVzFpckZIZUltZC1nY3IxVGw4a0NxaWVucHZNcDVVejdEdXRJWHEwLTY0c2hUdFd2aFBERlNmOTlYdDFCeDJldlZ6VFBaem8yeXdTbXVuVEhCV3A5Zk1wTmlSb2s5QmdEQkFkMFphOXM3VVBmM1RJeE05V1J1a29ZT3BNWlRFNTlEd1BTUkdXRjMzTnJocEx3b3pQaUZqSEpmekRoN09VRTdtNkNsS3dTVGxaUl9hWnlQa01yc3dlVQ?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxQVjdVTTNkdlhLYklHSjlGT19ubTAzUk9tMHZZell6aUt6WHh0MEJBdThsWjE4SzE1ZG5Lc1hpcV9WR0hhN0FsZkZQZTgwN0NQelA0SmNQeTBKMEpqYjBQZEN4SGc1eDVuejMxd0l6X1JjUjZMTnJsZ0pRMFBOaDR5X2tfXzlhZFlaeFZYOGJhSDl2TnlQTlJIOS0tb0RxU3Rqb0pIZVdESlpMNzlTbnRKZFh3?oc=5
- https://news.google.com/rss/articles/CBMi3AFBVV95cUxNNVpXejg4bmNOOVg3V3A1em9OVkN5VHVnMjZfMVRkSHJXTUo4SkRlMkJubkVidGhwRXBieS1rSzdWZUhEenRjbzVXNTZiUElHNkhiUHpwZjhOd3BrNGRCXzNMNE80Q1BwdlJYN0FySnRDUkVaUE5JMkVHLTJpSjBrNUx0TUxDZzZaNktMdmgwOHBqUkdsM1M5VGdSQmpyN052NlZTTlAyUFN0OG5VbmxmYmR3YkJOclN1MUdmbXExdzBULXZOWDNrSjNDOXM2YTlLRktYb1RqWC1WWk5K?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxPNzRKVWJlZDl6aDM3dHFBQ05oanJ2QURnR25lUDh1RVdUZGlwTUR1OVU5SEd5bUFEU0pCVDg3NGZ2azRoUzRBOHEycWlZa1Ftam95NmMwWnE4S0J2cWY1ajd5SEJtM2tGTS1YcW90VjNtMlNTWlFSa3NPVEFXNExiRU9WSHNCNzIzb01YTQ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOYV8wLUxVOEZjaXE5aGY4UjNnLW9ZNTRJUGtORl9OeEtxSm04dk5RbUp6SmUzUFJQbjFzNlBZdjl0VUxqQjVnYkxlN2w5NWxuUm5US0NJdzZGNlY4TUZRSTlaRmxSX09TTGJLLUtXWlVLUzlhWlpGWUZyV1lQc3VKeGc1cHRvYzduYmh5RFNpOHp5U2tTelJRSHdpUGxTd2dyMlE?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxQeXhIejFMVG9jQzVfR0UxSGVBUEFmYW13NG5yeXByT0xxREdTcG13Y0thTVpPcElfR3ExYktseXRVRThUcE56Zlk3MVVpTUUyYTc4OGxwVTBBdTNYcHJPQjcwa1c4aUh4eFUwcEJxSXhMX25IeUZ3SEl3Slp5ZkMzdFJ0bEJXd2g0Y3poZ081NUJkNTZpMkstMGxueTl1dl8yUXNDaXNEMldFTXpESVluNUNBNjJVU0Z4YjR0dnc3MTJuZmdWSXc?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOc1BrQUxiTl91cThBREhMNzVaVnVPS2VkRG11Nm0xVThiUEd3dHk4ZW5WSGpOaWprb3d3X2J5blhMZVl5T3EzUFhGZGdmZlRvclM2aS1vMHF5dlRCTDRfOFF2N2tVRmVFMXc5TTlwOW10LVU2d0puazEzR0NWelpxcXY0aUFRWVh4RC1wM0VOazBITk5BVmg0MlJyQ3BfQzdZ?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPck1yVkQyYUg0aUN5OUtxV2l4ZGktMTFnZnhZdTVkcUxna1ItNnR4bHJhTmFvV3pHSzYtNUx2QmJlQnRELUN4cEp0dU9IdWpISHhCajZtN2xUYTNueWhycUJhWG9WV2tiME1hTWE3eEN1eHpaRXdZQ2FXc05ua3loWFZmd29JakY2YmN4QXpwNlkyTGZ4SV9ra0pVQ1BGWmhG?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQMXJUSGZtR1ZhcTcyLVcyejBYaUN6Q3AwTnVaOGFDOThqUm1PTjNTb1N0YmRDVk8yQW1ZVW1tYVlkZDctekJVMV9zcTd6aWM4TURYV1NrVExYdEdTYlpyZFp3aDQyamVsYk5jZFExMWNZR01sb05wR05EVmx2TmZTM0xueFVQS2ktSDRtaV90NVk1eVl1Mnc?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOUVZxdjdndTdJYVJGRlBKMFNYZmlFcExERDRUeUF5cTc2MUN2a3JETk1iekxRQlZnMDBwVmZITUItd0FrbEFpTVA2SEhFMnNGZHhPcV9ZQ1NDZnVXa0tmWHdwMGxGb0psSkliYVl4QnN6eFp0MW01VDd1OXluX1FPRW9rMmtHWWpuYk9RT2pPV2pTNWdjT0hMWTdSRnB4dk0?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
