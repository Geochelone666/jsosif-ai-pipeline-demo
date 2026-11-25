# V Intelligence Report

- ticker: **V**
- Report as_of: **2026-11-24**
- Market data as_of: **2026-11-24**
- Quant sources: https://finance.yahoo.com/quote/V/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/V/key-statistics/
- AI analysis snapshot as_of: **2026-11-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-25T07:24:04.314020+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 2, 'ai': 16, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **14** exact headline/source/date matches; prior report **20261124T081701Z-6c335e3d/V** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 9 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 44.0%; oldest publication 2026-11-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 416.7800 |
| Return 1D (%) | 1.8026 |
| Return 1W (%) | 0.0024 |
| Return 1M (%) | 2.3611 |
| Return YTD (%) | 19.7738 |
| Return 1Y (%) | 27.5611 |
| Annualized volatility (%) | 23.2434 |
| Beta vs SPY | 0.3313 |
| Max drawdown (%) | -17.1805 |
| Sharpe (rf=0) | 1.1668 |
| Downside deviation (rf=0, %) | 14.4533 |
| Sortino (rf=0) | 1.8764 |
| Historical VaR 95% (1D, %) | 1.8407 |
| Historical ES 95% (1D, %) | 2.9273 |
| Correlation vs SPY | 0.2131 |
| Tracking error vs SPY (%) | 24.8139 |
| P/E (trailing) | 33.83 |
| P/B | 21.74 |
| EV/EBITDA | 24.27 |
| Revenue growth (%) | 13.20 |
| Forward P/E (estimate) | 24.32 |
| Gross margin (%) | 97.68 |
| Operating margin (%) | 66.31 |
| Return on equity (%) | 63.51 |
| Free cash flow yield (%) | 2.70 |
| MA50 | 395.5818 |
| Close vs MA50 (%) | 5.3587 |
| MA200 | 348.8190 |
| Close vs MA200 (%) | 19.4832 |
| RSI (14, Wilder) | 54.7682 |
| MACD (12,26) | 3.5468 |
| MACD signal (9) | 6.4559 |
| MACD histogram | -2.9091 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'V': 289, 'SPY': 289}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 416.7800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.8026 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.0024 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 2.3611 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 19.7738 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 27.5611 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 23.2434 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.4533 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.8764 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.8407 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.9273 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2131 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.8139 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3313 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -17.1805 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1668 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 24.3157 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 97.6780 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 66.3070 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 63.5070 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.6984 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 33.8295 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 54.7682 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -2.9091 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 5.3587 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 19.4832 -> Clearly above the moving-average trend level.

## TAILWINDS

### Visa (NYSE:V) Stock Jumps 2.1% - What's Next?
- Summary: Visa (NYSE:V) Stock Jumps 2.1% - What's Next?
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPNTNUbEtEN3lTRHcwNHFQY2ZpZVk0LU1GbWkxR2JKWXRya1QxUFBNeFFqdFNTS3VMQ0I5T2NOQ20zM0wzaF9sTHV4cGNOSmUzSEVhUEhMZWxuZjhqRndOcFdEQVAzVlVIY3N3VmxQODZZRVV1NGhnUm1rd3dDYll6dWx3MTJpaExEdS0yakpHNUM3UW1ZRkI0X0YwVTJQUQ?oc=5>

### Visa (V) Broadens Checkout Options On Its Acceptance Platform
- Summary: Visa expands checkout options on its acceptance platform, enhancing merchant and consumer experience.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQR0l4YWhRNmVPRURfekdGVU9OQmhqSXh2RWt2OWk0SmhINW9WMkU2ZlFhWVVPUmx3ZEgtU05lMG0tUDJRWFdEY3ZHWlVBbnBRQm1qeDBiRFpHSGVtMmRReXVCMkluTlh1MzluR1h5TDVmUTJCMjJESzFuT3RCVFdlR3V3Z19PV0hjNi1MMWhtSFVZMjBTNHZPMW1qUEtOQQ?oc=5>

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

### V: Visa Inc. filed SEC Form 8-K: Leadership Update
- Summary: Visa filed a Form 8‑K announcing a leadership update.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxPQjNWMGhQZ0dmX3pPWFRmNVZSUnBlTkVnb1V0TmZCLU5fN25QNWgwUUgtaVFWSmU1aUM5emdGalY5MUFRM2RrZkJRRzV5QVBBbVA4OWhPZDZ5M2ZPSTItMUpPUkxGQW0yRXozWG5TQWNROW5GT2t5dXk5N0xNYlBFWFBfTEI3dWdvTzEwX25XVl81Zw?oc=5>

### Visa (V) CEO Ryan McInerney gets options to buy shares at $402.25, some tied to stock-price targets.
- Summary: CEO granted options tied to performance, potentially boosting morale and aligning incentives.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPYkZ5dERDS09kNHU2ODRjbkpZR0U0N1lZekNVN1phRHVwVGY0NVZPTlEyWVFTa2ljXzZpajZBNTZpZ3k2Z2diQ1NPVHZadTNLLURCb0M5eGNzUFl3djRCaDdXNEJvY0VHeUY4WVJuN19zQlN0YlVPMTJWSHNmLVhGaFpJVlNycm94U1hsMWllMEIzbkxhSURrUjFISWE3bW45?oc=5>

### Visa (V) grants its vice chair 23,434 options with a $402.25 exercise price and a 2036 expiration.
- Summary: Vice chair awarded options, reinforcing executive alignment with company performance.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPck1yVkQyYUg0aUN5OUtxV2l4ZGktMTFnZnhZdTVkcUxna1ItNnR4bHJhTmFvV3pHSzYtNUx2QmJlQnRELUN4cEp0dU9IdWpISHhCajZtN2xUYTNueWhycUJhWG9WV2tiME1hTWE3eEN1eHpaRXdZQ2FXc05ua3loWFZmd29JakY2YmN4QXpwNlkyTGZ4SV9ra0pVQ1BGWmhG?oc=5>

### Visa (V) grants Julie B. Rottenberg 22,201 stock options with a $402.25 exercise price.
- Summary: Executive granted options, supporting retention and incentive alignment.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOc1BrQUxiTl91cThBREhMNzVaVnVPS2VkRG11Nm0xVThiUEd3dHk4ZW5WSGpOaWprb3d3X2J5blhMZVl5T3EzUFhGZGdmZlRvclM2aS1vMHF5dlRCTDRfOFF2N2tVRmVFMXc5TTlwOW10LVU2d0puazEzR0NWelpxcXY0aUFRWVh4RC1wM0VOazBITk5BVmg0MlJyQ3BfQzdZ?oc=5>

### Visa Inc Stock (V) Moved Down by 3.45% on Nov 19: What Signal Does It Send?
- Summary: Visa stock fell 3.45% on Nov 19, indicating potential short‑term weakness.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxOY1FrekJiSXVObHpDVjY1ZzVxMzZ1ME5hN2hPMFN5X3N6MXBXOWlWSFAwalNDbzhYbEE1WjliZFI2aEN6VDBkbzJobUFPQ0gwSmUwdFJSNXBlX2VYQkNhWHF6NllLXzdjaXJYak1DdFBoT2l6Q0hlMEpLYXJqc3lzaG9KeGY0Qk0?oc=5>

### Visa Approves Performance Stock Award for CEO
- Summary: CEO receives performance-based stock award, reflecting executive compensation strategy.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxQeXhIejFMVG9jQzVfR0UxSGVBUEFmYW13NG5yeXByT0xxREdTcG13Y0thTVpPcElfR3ExYktseXRVRThUcE56Zlk3MVVpTUUyYTc4OGxwVTBBdTNYcHJPQjcwa1c4aUh4eFUwcEJxSXhMX25IeUZ3SEl3Slp5ZkMzdFJ0bEJXd2g0Y3poZ081NUJkNTZpMkstMGxueTl1dl8yUXNDaXNEMldFTXpESVluNUNBNjJVU0Z4YjR0dnc3MTJuZmdWSXc?oc=5>

### Visa awards to CEO $50M stock grant linked to stock performance (V:NYSE)
- Summary: CEO granted $50M stock award tied to performance, indicating incentive alignment.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxOYV8wLUxVOEZjaXE5aGY4UjNnLW9ZNTRJUGtORl9OeEtxSm04dk5RbUp6SmUzUFJQbjFzNlBZdjl0VUxqQjVnYkxlN2w5NWxuUm5US0NJdzZGNlY4TUZRSTlaRmxSX09TTGJLLUtXWlVLUzlhWlpGWUZyV1lQc3VKeGc1cHRvYzduYmh5RFNpOHp5U2tTelJRSHdpUGxTd2dyMlE?oc=5>

### A proposed $348K sale by Visa (V) officer Paul D. Fabara covers 852 shares from vested stock awards.
- Summary: Officer proposes sale of 852 shares, a routine share transaction.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxQeDFXTGg0Y0ctbzNBdzVKQVFXdEI1cmtDVGZMY1lXQXNsMk02cVBkMk1qV1dOSUVhWkdvQUdJNS11TDNxSXZMd3pfVWNzVDZjTDFZTl9WYkZRVkd2RzQtZFRPV1NwOVpqTXBMc25CQUhuZ2ZsOFFnQjhINndEdkYtU1RFaTVYM3NuRFE?oc=5>

### A Visa (V) officer proposes another stock sale after two November sales topped $14M each.
- Summary: Visa officer plans additional share sale after two large November sales.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxPdUp6T0RSdzhLVGxKY1hZRlhvaGtpMFlZbnJXZE1NaDBXSjJocFlrRGtITklvXzBEaXlIczAzOEVSYlNDalUtRFZNWWk2dlJYcThpcmxVYllla1RaMU1EMGNlcFBnazlYTjdHZHRLTTFvUW94bnpaYXFaWm9TQ0tsYWFjRm82c3lTTlE?oc=5>

### Visa: The Market Is Waking Up To New Growth Levels (NYSE:V)
- Summary: Visa highlights rising market expectations for growth.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxOcjk3UXRibVNNZWpZTVNGcERDQzZTeExqYmQ3MUFFVDZ1ZTc0QnppV0lFMlJJaE44M095STNSSUo2eHVkaVVfN0tGMGdLTjlHRnJYVlg5NnRSZmxUdkQ3b3dfMDZjczNqYV9DZTFHLXlWc0syOGFaalIzaVFhMmNNZU9USllDOGdqRFNBcnkxWmxXeU5aYUpkU0dlTFZoNjdjWGF0Q1ZlRVhOclpnMXpWcDdQcW43QQ?oc=5>

### Visa Inc. $V Stock: Edgewood Management LLC Trims Holdings
- Summary: Edgewood Management reduces its Visa holdings.
- Date: 2026-11-21 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxPdWNSSWQwZk0zbUZXb3NsVzFYU0gxOWtQSE9XTUZtWEtyd2p3TzNSbWNuU0ZQQjUwMzRqVHhrZTNZZk15WmEyUjZ5d2VIYzk3UDVRTGJvbDdDTTRvTXE0S1JscHNOWGw3XzQtZGUwbTJtaEU1NEkwV3RuaWpNMndhWG1qbzltcWJJaG1rbDFvX0pyZDN5SG95VWw1UHFORUlocnE2VTlucU53YmxkeFZZT2ZSbnJRVlE?oc=5>

## RISKS

### Visa: Paying A Pretty Penny For Stability (Rating Downgrade) (NYSE:V)
- Summary: Visa received a rating downgrade, indicating potential credit risk.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQMXJUSGZtR1ZhcTcyLVcyejBYaUN6Q3AwTnVaOGFDOThqUm1PTjNTb1N0YmRDVk8yQW1ZVW1tYVlkZDctekJVMV9zcTd6aWM4TURYV1NrVExYdEdTYlpyZFp3aDQyamVsYk5jZFExMWNZR01sb05wR05EVmx2TmZTM0xueFVQS2ktSDRtaV90NVk1eVl1Mnc?oc=5>

### Visa: The Market Finally Recognizes Its Strength (Rating Downgrade) (NYSE:V)
- Summary: Credit rating downgrade signals potential credit risk and market concerns for Visa.
- Date: 2026-11-24 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOUVZxdjdndTdJYVJGRlBKMFNYZmlFcExERDRUeUF5cTc2MUN2a3JETk1iekxRQlZnMDBwVmZITUItd0FrbEFpTVA2SEhFMnNGZHhPcV9ZQ1NDZnVXa0tmWHdwMGxGb0psSkliYVl4QnN6eFp0MW01VDd1OXluX1FPRW9rMmtHWWpuYk9RT2pPV2pTNWdjT0hMWTdSRnB4dk0?oc=5>

### Visa (V) Could Be 70% Overvalued After Its Stablecoin Payments Tie Up
- Summary: Visa may be overvalued due to stablecoin payment issues.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNbHBpMXJPZ3BPM0tDUGpaZDNCWExEVUdRaU54YjBoMDllajMyc1hzYnd6UHlDcGR4WW9vM05vMkEzMHlhSjhUSUNNWjJmck9rektfU19hYUpzb0xaR1ExNFRsM3U2aVEtODVxSUxxSVY0WGdJMXV6U3doTi0zWTNuZC1Nc3JfSUhzZXQtcmh1dEdDQW83RHc?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **V** | **33.83** | **21.74** | **24.27** | **13.20** | **777,628,155,904.00 USD** | **27.56** |
| MA | 33.88 | 83.62 | 25.08 | 14.00 | 564,034,273,280.00 USD | 21.15 |
| PYPL | 10.72 | 2.41 | 7.76 | 2.00 | 46,658,076,672.00 USD | -6.43 |
| AXP | 17.39 | 5.79 | N/A | 11.30 | 206,952,464,384.00 USD | -12.31 |

Peers fetched as_of: 2026-11-24; V reuses existing data (market data as_of: 2026-11-24); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-27
- Next expected earnings: 2027-01-26 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-24

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

- https://news.google.com/rss/articles/CBMingFBVV95cUxPNTNUbEtEN3lTRHcwNHFQY2ZpZVk0LU1GbWkxR2JKWXRya1QxUFBNeFFqdFNTS3VMQ0I5T2NOQ20zM0wzaF9sTHV4cGNOSmUzSEVhUEhMZWxuZjhqRndOcFdEQVAzVlVIY3N3VmxQODZZRVV1NGhnUm1rd3dDYll6dWx3MTJpaExEdS0yakpHNUM3UW1ZRkI0X0YwVTJQUQ?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQR0l4YWhRNmVPRURfekdGVU9OQmhqSXh2RWt2OWk0SmhINW9WMkU2ZlFhWVVPUmx3ZEgtU05lMG0tUDJRWFdEY3ZHWlVBbnBRQm1qeDBiRFpHSGVtMmRReXVCMkluTlh1MzluR1h5TDVmUTJCMjJESzFuT3RCVFdlR3V3Z19PV0hjNi1MMWhtSFVZMjBTNHZPMW1qUEtOQQ?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxNVy1wQkk0NXV5MHJ5S2tIOWdrVFNZLS1RYllGU1FCM2lNMW1ySG5fNXo3RTVwVmVqY3FaLURZUGtvM1FBVUZuZFhyRFN1ZVBvdEZZT010Snpfd1FGbUdLRlExT1FuaWNtMjlqdmVtWjVNM0RId01kTy1XQUEzX2J1UWh0WGplSWE2SGRYTXVyUQ?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQWmh6NkxzdmlTb21FUHlTbTI3VzV6YTRMYXFMc09ValZGYTlnU1h1T2M4N1FiVEI0QjRtZ1VRcTlJMWN4RVVlUXJMa2hROVpKV0pRUzJpNk4yYUFod0tPVFZVSUhtMWNrZUFjaWtaNkU1QnAwWnRWU1pIcmF5UDNxTEdUVmRlWmdubjl4dF9nTDVUc1JIQV84YzVEYnl5SXdr?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxPQjNWMGhQZ0dmX3pPWFRmNVZSUnBlTkVnb1V0TmZCLU5fN25QNWgwUUgtaVFWSmU1aUM5emdGalY5MUFRM2RrZkJRRzV5QVBBbVA4OWhPZDZ5M2ZPSTItMUpPUkxGQW0yRXozWG5TQWNROW5GT2t5dXk5N0xNYlBFWFBfTEI3dWdvTzEwX25XVl81Zw?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPYkZ5dERDS09kNHU2ODRjbkpZR0U0N1lZekNVN1phRHVwVGY0NVZPTlEyWVFTa2ljXzZpajZBNTZpZ3k2Z2diQ1NPVHZadTNLLURCb0M5eGNzUFl3djRCaDdXNEJvY0VHeUY4WVJuN19zQlN0YlVPMTJWSHNmLVhGaFpJVlNycm94U1hsMWllMEIzbkxhSURrUjFISWE3bW45?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPck1yVkQyYUg0aUN5OUtxV2l4ZGktMTFnZnhZdTVkcUxna1ItNnR4bHJhTmFvV3pHSzYtNUx2QmJlQnRELUN4cEp0dU9IdWpISHhCajZtN2xUYTNueWhycUJhWG9WV2tiME1hTWE3eEN1eHpaRXdZQ2FXc05ua3loWFZmd29JakY2YmN4QXpwNlkyTGZ4SV9ra0pVQ1BGWmhG?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOc1BrQUxiTl91cThBREhMNzVaVnVPS2VkRG11Nm0xVThiUEd3dHk4ZW5WSGpOaWprb3d3X2J5blhMZVl5T3EzUFhGZGdmZlRvclM2aS1vMHF5dlRCTDRfOFF2N2tVRmVFMXc5TTlwOW10LVU2d0puazEzR0NWelpxcXY0aUFRWVh4RC1wM0VOazBITk5BVmg0MlJyQ3BfQzdZ?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxOY1FrekJiSXVObHpDVjY1ZzVxMzZ1ME5hN2hPMFN5X3N6MXBXOWlWSFAwalNDbzhYbEE1WjliZFI2aEN6VDBkbzJobUFPQ0gwSmUwdFJSNXBlX2VYQkNhWHF6NllLXzdjaXJYak1DdFBoT2l6Q0hlMEpLYXJqc3lzaG9KeGY0Qk0?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxQeXhIejFMVG9jQzVfR0UxSGVBUEFmYW13NG5yeXByT0xxREdTcG13Y0thTVpPcElfR3ExYktseXRVRThUcE56Zlk3MVVpTUUyYTc4OGxwVTBBdTNYcHJPQjcwa1c4aUh4eFUwcEJxSXhMX25IeUZ3SEl3Slp5ZkMzdFJ0bEJXd2g0Y3poZ081NUJkNTZpMkstMGxueTl1dl8yUXNDaXNEMldFTXpESVluNUNBNjJVU0Z4YjR0dnc3MTJuZmdWSXc?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOYV8wLUxVOEZjaXE5aGY4UjNnLW9ZNTRJUGtORl9OeEtxSm04dk5RbUp6SmUzUFJQbjFzNlBZdjl0VUxqQjVnYkxlN2w5NWxuUm5US0NJdzZGNlY4TUZRSTlaRmxSX09TTGJLLUtXWlVLUzlhWlpGWUZyV1lQc3VKeGc1cHRvYzduYmh5RFNpOHp5U2tTelJRSHdpUGxTd2dyMlE?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxQeDFXTGg0Y0ctbzNBdzVKQVFXdEI1cmtDVGZMY1lXQXNsMk02cVBkMk1qV1dOSUVhWkdvQUdJNS11TDNxSXZMd3pfVWNzVDZjTDFZTl9WYkZRVkd2RzQtZFRPV1NwOVpqTXBMc25CQUhuZ2ZsOFFnQjhINndEdkYtU1RFaTVYM3NuRFE?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxPdUp6T0RSdzhLVGxKY1hZRlhvaGtpMFlZbnJXZE1NaDBXSjJocFlrRGtITklvXzBEaXlIczAzOEVSYlNDalUtRFZNWWk2dlJYcThpcmxVYllla1RaMU1EMGNlcFBnazlYTjdHZHRLTTFvUW94bnpaYXFaWm9TQ0tsYWFjRm82c3lTTlE?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxOcjk3UXRibVNNZWpZTVNGcERDQzZTeExqYmQ3MUFFVDZ1ZTc0QnppV0lFMlJJaE44M095STNSSUo2eHVkaVVfN0tGMGdLTjlHRnJYVlg5NnRSZmxUdkQ3b3dfMDZjczNqYV9DZTFHLXlWc0syOGFaalIzaVFhMmNNZU9USllDOGdqRFNBcnkxWmxXeU5aYUpkU0dlTFZoNjdjWGF0Q1ZlRVhOclpnMXpWcDdQcW43QQ?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxPdWNSSWQwZk0zbUZXb3NsVzFYU0gxOWtQSE9XTUZtWEtyd2p3TzNSbWNuU0ZQQjUwMzRqVHhrZTNZZk15WmEyUjZ5d2VIYzk3UDVRTGJvbDdDTTRvTXE0S1JscHNOWGw3XzQtZGUwbTJtaEU1NEkwV3RuaWpNMndhWG1qbzltcWJJaG1rbDFvX0pyZDN5SG95VWw1UHFORUlocnE2VTlucU53YmxkeFZZT2ZSbnJRVlE?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQMXJUSGZtR1ZhcTcyLVcyejBYaUN6Q3AwTnVaOGFDOThqUm1PTjNTb1N0YmRDVk8yQW1ZVW1tYVlkZDctekJVMV9zcTd6aWM4TURYV1NrVExYdEdTYlpyZFp3aDQyamVsYk5jZFExMWNZR01sb05wR05EVmx2TmZTM0xueFVQS2ktSDRtaV90NVk1eVl1Mnc?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOUVZxdjdndTdJYVJGRlBKMFNYZmlFcExERDRUeUF5cTc2MUN2a3JETk1iekxRQlZnMDBwVmZITUItd0FrbEFpTVA2SEhFMnNGZHhPcV9ZQ1NDZnVXa0tmWHdwMGxGb0psSkliYVl4QnN6eFp0MW01VDd1OXluX1FPRW9rMmtHWWpuYk9RT2pPV2pTNWdjT0hMWTdSRnB4dk0?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNbHBpMXJPZ3BPM0tDUGpaZDNCWExEVUdRaU54YjBoMDllajMyc1hzYnd6UHlDcGR4WW9vM05vMkEzMHlhSjhUSUNNWjJmck9rektfU19hYUpzb0xaR1ExNFRsM3U2aVEtODVxSUxxSVY0WGdJMXV6U3doTi0zWTNuZC1Nc3JfSUhzZXQtcmh1dEdDQW83RHc?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
