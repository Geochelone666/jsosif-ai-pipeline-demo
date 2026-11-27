# V Intelligence Report

- ticker: **V**
- Report as_of: **2026-11-26**
- Market data as_of: **2026-11-25**
- Quant sources: https://finance.yahoo.com/quote/V/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/V/key-statistics/
- AI analysis snapshot as_of: **2026-11-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-27T06:41:16.146890+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 4, 'ai': 10, 'unknown': 0, 'irrelevant': 11})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **16** exact headline/source/date matches; prior report **20261126T064454Z-dbdd6f45/V** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 10 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 32.0%; oldest publication 2026-11-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 424.3900 |
| Return 1D (%) | 1.8259 |
| Return 1W (%) | 2.2085 |
| Return 1M (%) | 4.2301 |
| Return YTD (%) | 21.9608 |
| Return 1Y (%) | 27.8596 |
| Annualized volatility (%) | 23.2599 |
| Beta vs SPY | 0.3238 |
| Max drawdown (%) | -17.1805 |
| Sharpe (rf=0) | 1.1763 |
| Downside deviation (rf=0, %) | 14.4533 |
| Sortino (rf=0) | 1.8930 |
| Historical VaR 95% (1D, %) | 1.8407 |
| Historical ES 95% (1D, %) | 2.9273 |
| Correlation vs SPY | 0.2078 |
| Tracking error vs SPY (%) | 24.8918 |
| P/E (trailing) | 34.45 |
| P/B | 22.14 |
| EV/EBITDA | 24.71 |
| Revenue growth (%) | 13.20 |
| Forward P/E (estimate) | 24.76 |
| Gross margin (%) | 97.68 |
| Operating margin (%) | 66.31 |
| Return on equity (%) | 63.51 |
| Free cash flow yield (%) | 2.65 |
| MA50 | 396.6647 |
| Close vs MA50 (%) | 6.9896 |
| MA200 | 349.3095 |
| Close vs MA200 (%) | 21.4940 |
| RSI (14, Wilder) | 59.2684 |
| MACD (12,26) | 4.0985 |
| MACD signal (9) | 5.9844 |
| MACD histogram | -1.8859 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'V': 290, 'SPY': 290}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 424.3900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.8259 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.2085 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 4.2301 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 21.9608 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 27.8596 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 23.2599 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.4533 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.8930 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.8407 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.9273 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2078 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.8918 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3238 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -17.1805 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1763 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 24.7596 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 97.6780 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 66.3070 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 63.5070 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.6500 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 34.4472 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 59.2684 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.8859 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 6.9896 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 21.4940 -> Clearly above the moving-average trend level.

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

### Visa stock extends downward price move as seller pressure outweighs oversold signals
- Summary: Visa stock extends downward price move as seller pressure outweighs oversold signals
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxNVy1wQkk0NXV5MHJ5S2tIOWdrVFNZLS1RYllGU1FCM2lNMW1ySG5fNXo3RTVwVmVqY3FaLURZUGtvM1FBVUZuZFhyRFN1ZVBvdEZZT010Snpfd1FGbUdLRlExT1FuaWNtMjlqdmVtWjVNM0RId01kTy1XQUEzX2J1UWh0WGplSWE2SGRYTXVyUQ?oc=5>

### Under a trading plan, Visa (V) technology president Rajat Taneja sold 4,005 shares at $405 each.
- Summary: Insider sale may signal negative outlook for Visa shares.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQWmh6NkxzdmlTb21FUHlTbTI3VzV6YTRMYXFMc09ValZGYTlnU1h1T2M4N1FiVEI0QjRtZ1VRcTlJMWN4RVVlUXJMa2hROVpKV0pRUzJpNk4yYUFod0tPVFZVSUhtMWNrZUFjaWtaNkU1QnAwWnRWU1pIcmF5UDNxTEdUVmRlWmdubjl4dF9nTDVUc1JIQV84YzVEYnl5SXdr?oc=5>

## CATALYSTS

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

### A proposed $348K sale by Visa (V) officer Paul D. Fabara covers 852 shares from vested stock awards.
- Summary: Officer proposes sale of 852 shares, a routine share transaction.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxQeDFXTGg0Y0ctbzNBdzVKQVFXdEI1cmtDVGZMY1lXQXNsMk02cVBkMk1qV1dOSUVhWkdvQUdJNS11TDNxSXZMd3pfVWNzVDZjTDFZTl9WYkZRVkd2RzQtZFRPV1NwOVpqTXBMc25CQUhuZ2ZsOFFnQjhINndEdkYtU1RFaTVYM3NuRFE?oc=5>

### Visa (V) CEO Ryan McInerney gets options to buy shares at $402.25, some tied to stock-price targets.
- Summary: CEO granted options tied to performance, potentially boosting morale and aligning incentives.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPYkZ5dERDS09kNHU2ODRjbkpZR0U0N1lZekNVN1phRHVwVGY0NVZPTlEyWVFTa2ljXzZpajZBNTZpZ3k2Z2diQ1NPVHZadTNLLURCb0M5eGNzUFl3djRCaDdXNEJvY0VHeUY4WVJuN19zQlN0YlVPMTJWSHNmLVhGaFpJVlNycm94U1hsMWllMEIzbkxhSURrUjFISWE3bW45?oc=5>

## RISKS

### Visa: The Market Finally Recognizes Its Strength (Rating Downgrade) (NYSE:V)
- Summary: Credit rating downgrade signals potential credit risk and market concerns for Visa.
- Date: 2026-11-24 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOUVZxdjdndTdJYVJGRlBKMFNYZmlFcExERDRUeUF5cTc2MUN2a3JETk1iekxRQlZnMDBwVmZITUItd0FrbEFpTVA2SEhFMnNGZHhPcV9ZQ1NDZnVXa0tmWHdwMGxGb0psSkliYVl4QnN6eFp0MW01VDd1OXluX1FPRW9rMmtHWWpuYk9RT2pPV2pTNWdjT0hMWTdSRnB4dk0?oc=5>

### Visa: Paying A Pretty Penny For Stability (Rating Downgrade) (NYSE:V)
- Summary: Visa received a rating downgrade, indicating potential credit risk.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQMXJUSGZtR1ZhcTcyLVcyejBYaUN6Q3AwTnVaOGFDOThqUm1PTjNTb1N0YmRDVk8yQW1ZVW1tYVlkZDctekJVMV9zcTd6aWM4TURYV1NrVExYdEdTYlpyZFp3aDQyamVsYk5jZFExMWNZR01sb05wR05EVmx2TmZTM0xueFVQS2ktSDRtaV90NVk1eVl1Mnc?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **V** | **34.45** | **22.14** | **24.71** | **13.20** | **791,826,923,520.00 USD** | **27.86** |
| MA | 34.54 | 85.23 | 25.55 | 14.00 | 574,950,080,512.00 USD | 21.55 |
| PYPL | 11.03 | 2.48 | 7.97 | 2.00 | 48,020,357,120.00 USD | -4.74 |
| AXP | 17.60 | 5.86 | N/A | 11.30 | 209,473,748,992.00 USD | -12.89 |

Peers fetched as_of: 2026-11-26; V reuses existing data (market data as_of: 2026-11-25); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-27
- Next expected earnings: 2027-01-26 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-26

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
- https://news.google.com/rss/articles/CBMijwFBVV95cUxNVy1wQkk0NXV5MHJ5S2tIOWdrVFNZLS1RYllGU1FCM2lNMW1ySG5fNXo3RTVwVmVqY3FaLURZUGtvM1FBVUZuZFhyRFN1ZVBvdEZZT010Snpfd1FGbUdLRlExT1FuaWNtMjlqdmVtWjVNM0RId01kTy1XQUEzX2J1UWh0WGplSWE2SGRYTXVyUQ?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQWmh6NkxzdmlTb21FUHlTbTI3VzV6YTRMYXFMc09ValZGYTlnU1h1T2M4N1FiVEI0QjRtZ1VRcTlJMWN4RVVlUXJMa2hROVpKV0pRUzJpNk4yYUFod0tPVFZVSUhtMWNrZUFjaWtaNkU1QnAwWnRWU1pIcmF5UDNxTEdUVmRlWmdubjl4dF9nTDVUc1JIQV84YzVEYnl5SXdr?oc=5
- https://news.google.com/rss/articles/CBMi3AFBVV95cUxNNVpXejg4bmNOOVg3V3A1em9OVkN5VHVnMjZfMVRkSHJXTUo4SkRlMkJubkVidGhwRXBieS1rSzdWZUhEenRjbzVXNTZiUElHNkhiUHpwZjhOd3BrNGRCXzNMNE80Q1BwdlJYN0FySnRDUkVaUE5JMkVHLTJpSjBrNUx0TUxDZzZaNktMdmgwOHBqUkdsM1M5VGdSQmpyN052NlZTTlAyUFN0OG5VbmxmYmR3YkJOclN1MUdmbXExdzBULXZOWDNrSjNDOXM2YTlLRktYb1RqWC1WWk5K?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxPNzRKVWJlZDl6aDM3dHFBQ05oanJ2QURnR25lUDh1RVdUZGlwTUR1OVU5SEd5bUFEU0pCVDg3NGZ2azRoUzRBOHEycWlZa1Ftam95NmMwWnE4S0J2cWY1ajd5SEJtM2tGTS1YcW90VjNtMlNTWlFSa3NPVEFXNExiRU9WSHNCNzIzb01YTQ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOYV8wLUxVOEZjaXE5aGY4UjNnLW9ZNTRJUGtORl9OeEtxSm04dk5RbUp6SmUzUFJQbjFzNlBZdjl0VUxqQjVnYkxlN2w5NWxuUm5US0NJdzZGNlY4TUZRSTlaRmxSX09TTGJLLUtXWlVLUzlhWlpGWUZyV1lQc3VKeGc1cHRvYzduYmh5RFNpOHp5U2tTelJRSHdpUGxTd2dyMlE?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxQeXhIejFMVG9jQzVfR0UxSGVBUEFmYW13NG5yeXByT0xxREdTcG13Y0thTVpPcElfR3ExYktseXRVRThUcE56Zlk3MVVpTUUyYTc4OGxwVTBBdTNYcHJPQjcwa1c4aUh4eFUwcEJxSXhMX25IeUZ3SEl3Slp5ZkMzdFJ0bEJXd2g0Y3poZ081NUJkNTZpMkstMGxueTl1dl8yUXNDaXNEMldFTXpESVluNUNBNjJVU0Z4YjR0dnc3MTJuZmdWSXc?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOc1BrQUxiTl91cThBREhMNzVaVnVPS2VkRG11Nm0xVThiUEd3dHk4ZW5WSGpOaWprb3d3X2J5blhMZVl5T3EzUFhGZGdmZlRvclM2aS1vMHF5dlRCTDRfOFF2N2tVRmVFMXc5TTlwOW10LVU2d0puazEzR0NWelpxcXY0aUFRWVh4RC1wM0VOazBITk5BVmg0MlJyQ3BfQzdZ?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPck1yVkQyYUg0aUN5OUtxV2l4ZGktMTFnZnhZdTVkcUxna1ItNnR4bHJhTmFvV3pHSzYtNUx2QmJlQnRELUN4cEp0dU9IdWpISHhCajZtN2xUYTNueWhycUJhWG9WV2tiME1hTWE3eEN1eHpaRXdZQ2FXc05ua3loWFZmd29JakY2YmN4QXpwNlkyTGZ4SV9ra0pVQ1BGWmhG?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxQeDFXTGg0Y0ctbzNBdzVKQVFXdEI1cmtDVGZMY1lXQXNsMk02cVBkMk1qV1dOSUVhWkdvQUdJNS11TDNxSXZMd3pfVWNzVDZjTDFZTl9WYkZRVkd2RzQtZFRPV1NwOVpqTXBMc25CQUhuZ2ZsOFFnQjhINndEdkYtU1RFaTVYM3NuRFE?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPYkZ5dERDS09kNHU2ODRjbkpZR0U0N1lZekNVN1phRHVwVGY0NVZPTlEyWVFTa2ljXzZpajZBNTZpZ3k2Z2diQ1NPVHZadTNLLURCb0M5eGNzUFl3djRCaDdXNEJvY0VHeUY4WVJuN19zQlN0YlVPMTJWSHNmLVhGaFpJVlNycm94U1hsMWllMEIzbkxhSURrUjFISWE3bW45?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOUVZxdjdndTdJYVJGRlBKMFNYZmlFcExERDRUeUF5cTc2MUN2a3JETk1iekxRQlZnMDBwVmZITUItd0FrbEFpTVA2SEhFMnNGZHhPcV9ZQ1NDZnVXa0tmWHdwMGxGb0psSkliYVl4QnN6eFp0MW01VDd1OXluX1FPRW9rMmtHWWpuYk9RT2pPV2pTNWdjT0hMWTdSRnB4dk0?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQMXJUSGZtR1ZhcTcyLVcyejBYaUN6Q3AwTnVaOGFDOThqUm1PTjNTb1N0YmRDVk8yQW1ZVW1tYVlkZDctekJVMV9zcTd6aWM4TURYV1NrVExYdEdTYlpyZFp3aDQyamVsYk5jZFExMWNZR01sb05wR05EVmx2TmZTM0xueFVQS2ktSDRtaV90NVk1eVl1Mnc?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
