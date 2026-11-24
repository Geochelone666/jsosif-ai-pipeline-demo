# V Intelligence Report

- ticker: **V**
- Report as_of: **2026-11-23**
- Market data as_of: **2026-11-23**
- Quant sources: https://finance.yahoo.com/quote/V/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/V/key-statistics/
- AI analysis snapshot as_of: **2026-11-23**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-24T08:26:12.088983+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 1, 'ai': 12, 'unknown': 0, 'irrelevant': 11})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261123T053847Z-45053549/V** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 9 named publishers; 0 exact duplicates; 24 HTTPS source links; largest publisher share 41.67%; oldest publication 2026-11-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 409.4000 |
| Return 1D (%) | 1.8737 |
| Return 1W (%) | -4.0004 |
| Return 1M (%) | 0.5486 |
| Return YTD (%) | 17.6530 |
| Return 1Y (%) | 25.8067 |
| Annualized volatility (%) | 23.2273 |
| Beta vs SPY | 0.3357 |
| Max drawdown (%) | -17.1805 |
| Sharpe (rf=0) | 1.0941 |
| Downside deviation (rf=0, %) | 14.4822 |
| Sortino (rf=0) | 1.7547 |
| Historical VaR 95% (1D, %) | 1.8438 |
| Historical ES 95% (1D, %) | 2.9273 |
| Correlation vs SPY | 0.2164 |
| Tracking error vs SPY (%) | 24.7629 |
| P/E (trailing) | 33.23 |
| P/B | 21.36 |
| EV/EBITDA | 23.84 |
| Revenue growth (%) | 13.20 |
| Forward P/E (estimate) | 23.89 |
| Gross margin (%) | 97.68 |
| Operating margin (%) | 66.31 |
| Return on equity (%) | 63.51 |
| Free cash flow yield (%) | 2.75 |
| MA50 | 394.7448 |
| Close vs MA50 (%) | 3.7126 |
| MA200 | 348.3503 |
| Close vs MA200 (%) | 17.5254 |
| RSI (14, Wilder) | 49.7708 |
| MACD (12,26) | 3.5659 |
| MACD signal (9) | 7.1832 |
| MACD histogram | -3.6172 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'V': 288, 'SPY': 288}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 409.4000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.8737 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -4.0004 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 0.5486 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 17.6530 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 25.8067 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 23.2273 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.4822 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.7547 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.8438 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.9273 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2164 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.7629 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3357 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -17.1805 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.0941 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 23.8851 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 97.6780 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 66.3070 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 63.5070 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.7470 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 33.2305 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 49.7708 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.6172 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 3.7126 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 17.5254 -> Clearly above the moving-average trend level.

## TAILWINDS

### Visa (NYSE:V) Stock Jumps 2.1% - What's Next?
- Summary: Visa (NYSE:V) Stock Jumps 2.1% - What's Next?
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPNTNUbEtEN3lTRHcwNHFQY2ZpZVk0LU1GbWkxR2JKWXRya1QxUFBNeFFqdFNTS3VMQ0I5T2NOQ20zM0wzaF9sTHV4cGNOSmUzSEVhUEhMZWxuZjhqRndOcFdEQVAzVlVIY3N3VmxQODZZRVV1NGhnUm1rd3dDYll6dWx3MTJpaExEdS0yakpHNUM3UW1ZRkI0X0YwVTJQUQ?oc=5>

### Visa: The Market Is Waking Up To New Growth Levels (NYSE:V)
- Summary: Market sentiment improves as investors recognize new growth potential for Visa.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxONTdOQUwwdk1Hc1V2ckRqN1l4NnZnZzBYcHloMG0tVVhLN1p3dm1WMjVmcVVjTGJ6NDlhQldncklKNmxPcEthM3JWd0g3TWg5MDFTNHdDN0dDVjJnSUluU09YNWp0T2tibTlNc29vMndidHRyZ1dTUWtjaXE5OVlTTzc5VldjV3pTekhiQWRfMmx2V1lh?oc=5>

### Visa is bringing 140+ organizations together to test purchases made by AI agents.
- Summary: Visa partners with 140+ firms to test AI-driven purchase processes, showcasing innovation and potential market expansion.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxPQ295ak0zS0dUZHdjeEtZNkpCNmNCYnJiLVhkZXV4aS1TN3JLTTBRSmtjenRFSXUybktfbEJOZmV6NVZ1SENaMVdveVRkNEdZd0lPcktjNGRMMVF2eUh0QWZHb2RpenFEN2dWTHJHTkUzdEk0UUJkQ3JVWVByNzRZQTZDaHdTRXNZbzhjLURQZ1h4N0FSM3Z2NzBFR0cxWEZTcTU3aDZrZDk5NkYxaHRUeFRpR2gzZjFL?oc=5>

## HEADWINDS

### Under a trading plan, Visa (V) technology president Rajat Taneja sold 4,005 shares at $405 each.
- Summary: Insider sale may signal negative outlook for Visa shares.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQWmh6NkxzdmlTb21FUHlTbTI3VzV6YTRMYXFMc09ValZGYTlnU1h1T2M4N1FiVEI0QjRtZ1VRcTlJMWN4RVVlUXJMa2hROVpKV0pRUzJpNk4yYUFod0tPVFZVSUhtMWNrZUFjaWtaNkU1QnAwWnRWU1pIcmF5UDNxTEdUVmRlWmdubjl4dF9nTDVUc1JIQV84YzVEYnl5SXdr?oc=5>

## CATALYSTS

### Visa Inc Stock (V) Moved Down by 3.45% on Nov 19: What Signal Does It Send?
- Summary: Visa stock fell 3.45% on Nov 19, indicating potential short‑term weakness.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxOY1FrekJiSXVObHpDVjY1ZzVxMzZ1ME5hN2hPMFN5X3N6MXBXOWlWSFAwalNDbzhYbEE1WjliZFI2aEN6VDBkbzJobUFPQ0gwSmUwdFJSNXBlX2VYQkNhWHF6NllLXzdjaXJYak1DdFBoT2l6Q0hlMEpLYXJqc3lzaG9KeGY0Qk0?oc=5>

### Visa (V) Stock Price Prediction: Visa holds a constructive pullback as analysts stay broadly positive
- Summary: Analysts predict a constructive pullback in Visa stock price.
- Date: 2026-11-18 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOczhnSEFuZExsb0JGb0tyakZPT2RGTmh4eUs3VnlVam1fRnFUeHF2LWQzRlJBNTFSMUhha1dDbzRDUFk1OEdETUZzVGtQRU9IcTB4TGthZHVIb0h0SDN4TmppdGtibkhKVnRWWEZNWHZfYnJvZXYzV0pDQTMzWURZcXZEc1Z1T29VYXh5VGpwVGhxaklnbFA2TzFR?oc=5>

### Visa (V) Stock Price Prediction: Visa Holds Near Key Support After a Choppy Pullback
- Summary: Visa stock near key support after pullback, predicted to hold.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNS1p1WWdSazdtWklLX21EbFRDaG0yREVBYzE3ZVhPdDlzSi1oM21GTk5NNTROLXZuRDA2emxyalpsQnhfWXRnTzFKNFpTSUNiblQ0M2RPbFlKNDU5TDh6Tkh0RTFsZm12d3hFMUtCLXlYOEZxY0RiRWl2Um1vREtUQ1ZJUWE2SWZFMTg0S1ZjamV0YjdR?oc=5>

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

### Visa Approves Performance Stock Award for CEO
- Summary: Visa approved a performance-based stock award for its CEO, recognizing executive achievements and aligning compensation with company performance.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOTXVtNVRkTjl2U0FFVlE5ZHJYV1oxVm5ydU5haHhJMFJpR3JJc3NjcWEzM05GMEF5STlwSF9RQXdWdWtRelFGYWFaUFp0Z1lEVWh5MXYwazJ6RWVRMnVMejQ0bnprODkxOHNtLXZpUWZrUXpGbVloOHA0MlYxYVo3dzJKSVBTdGFPNGxqcE5ZLWUzNDB2YUMzZGwyc3pnZw?oc=5>

## RISKS

### Visa: Paying A Pretty Penny For Stability (Rating Downgrade) (NYSE:V)
- Summary: Visa received a rating downgrade, indicating potential credit risk.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQMXJUSGZtR1ZhcTcyLVcyejBYaUN6Q3AwTnVaOGFDOThqUm1PTjNTb1N0YmRDVk8yQW1ZVW1tYVlkZDctekJVMV9zcTd6aWM4TURYV1NrVExYdEdTYlpyZFp3aDQyamVsYk5jZFExMWNZR01sb05wR05EVmx2TmZTM0xueFVQS2ktSDRtaV90NVk1eVl1Mnc?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **V** | **33.23** | **21.36** | **23.84** | **13.20** | **763,858,518,016.00 USD** | **25.81** |
| MA | 33.25 | 82.07 | 24.62 | 14.00 | 553,614,966,784.00 USD | 18.35 |
| PYPL | 10.54 | 2.37 | 7.65 | 2.00 | 45,885,566,976.00 USD | -8.00 |
| AXP | 17.29 | 5.75 | N/A | 11.30 | 205,792,411,648.00 USD | -12.05 |

Peers fetched as_of: 2026-11-23; V reuses existing data (market data as_of: 2026-11-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-27
- Next expected earnings: 2027-01-26 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-23

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
- https://news.google.com/rss/articles/CBMilAFBVV95cUxONTdOQUwwdk1Hc1V2ckRqN1l4NnZnZzBYcHloMG0tVVhLN1p3dm1WMjVmcVVjTGJ6NDlhQldncklKNmxPcEthM3JWd0g3TWg5MDFTNHdDN0dDVjJnSUluU09YNWp0T2tibTlNc29vMndidHRyZ1dTUWtjaXE5OVlTTzc5VldjV3pTekhiQWRfMmx2V1lh?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxPQ295ak0zS0dUZHdjeEtZNkpCNmNCYnJiLVhkZXV4aS1TN3JLTTBRSmtjenRFSXUybktfbEJOZmV6NVZ1SENaMVdveVRkNEdZd0lPcktjNGRMMVF2eUh0QWZHb2RpenFEN2dWTHJHTkUzdEk0UUJkQ3JVWVByNzRZQTZDaHdTRXNZbzhjLURQZ1h4N0FSM3Z2NzBFR0cxWEZTcTU3aDZrZDk5NkYxaHRUeFRpR2gzZjFL?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQWmh6NkxzdmlTb21FUHlTbTI3VzV6YTRMYXFMc09ValZGYTlnU1h1T2M4N1FiVEI0QjRtZ1VRcTlJMWN4RVVlUXJMa2hROVpKV0pRUzJpNk4yYUFod0tPVFZVSUhtMWNrZUFjaWtaNkU1QnAwWnRWU1pIcmF5UDNxTEdUVmRlWmdubjl4dF9nTDVUc1JIQV84YzVEYnl5SXdr?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxOY1FrekJiSXVObHpDVjY1ZzVxMzZ1ME5hN2hPMFN5X3N6MXBXOWlWSFAwalNDbzhYbEE1WjliZFI2aEN6VDBkbzJobUFPQ0gwSmUwdFJSNXBlX2VYQkNhWHF6NllLXzdjaXJYak1DdFBoT2l6Q0hlMEpLYXJqc3lzaG9KeGY0Qk0?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOczhnSEFuZExsb0JGb0tyakZPT2RGTmh4eUs3VnlVam1fRnFUeHF2LWQzRlJBNTFSMUhha1dDbzRDUFk1OEdETUZzVGtQRU9IcTB4TGthZHVIb0h0SDN4TmppdGtibkhKVnRWWEZNWHZfYnJvZXYzV0pDQTMzWURZcXZEc1Z1T29VYXh5VGpwVGhxaklnbFA2TzFR?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNS1p1WWdSazdtWklLX21EbFRDaG0yREVBYzE3ZVhPdDlzSi1oM21GTk5NNTROLXZuRDA2emxyalpsQnhfWXRnTzFKNFpTSUNiblQ0M2RPbFlKNDU5TDh6Tkh0RTFsZm12d3hFMUtCLXlYOEZxY0RiRWl2Um1vREtUQ1ZJUWE2SWZFMTg0S1ZjamV0YjdR?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxPQjNWMGhQZ0dmX3pPWFRmNVZSUnBlTkVnb1V0TmZCLU5fN25QNWgwUUgtaVFWSmU1aUM5emdGalY5MUFRM2RrZkJRRzV5QVBBbVA4OWhPZDZ5M2ZPSTItMUpPUkxGQW0yRXozWG5TQWNROW5GT2t5dXk5N0xNYlBFWFBfTEI3dWdvTzEwX25XVl81Zw?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPYkZ5dERDS09kNHU2ODRjbkpZR0U0N1lZekNVN1phRHVwVGY0NVZPTlEyWVFTa2ljXzZpajZBNTZpZ3k2Z2diQ1NPVHZadTNLLURCb0M5eGNzUFl3djRCaDdXNEJvY0VHeUY4WVJuN19zQlN0YlVPMTJWSHNmLVhGaFpJVlNycm94U1hsMWllMEIzbkxhSURrUjFISWE3bW45?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPck1yVkQyYUg0aUN5OUtxV2l4ZGktMTFnZnhZdTVkcUxna1ItNnR4bHJhTmFvV3pHSzYtNUx2QmJlQnRELUN4cEp0dU9IdWpISHhCajZtN2xUYTNueWhycUJhWG9WV2tiME1hTWE3eEN1eHpaRXdZQ2FXc05ua3loWFZmd29JakY2YmN4QXpwNlkyTGZ4SV9ra0pVQ1BGWmhG?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOc1BrQUxiTl91cThBREhMNzVaVnVPS2VkRG11Nm0xVThiUEd3dHk4ZW5WSGpOaWprb3d3X2J5blhMZVl5T3EzUFhGZGdmZlRvclM2aS1vMHF5dlRCTDRfOFF2N2tVRmVFMXc5TTlwOW10LVU2d0puazEzR0NWelpxcXY0aUFRWVh4RC1wM0VOazBITk5BVmg0MlJyQ3BfQzdZ?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOTXVtNVRkTjl2U0FFVlE5ZHJYV1oxVm5ydU5haHhJMFJpR3JJc3NjcWEzM05GMEF5STlwSF9RQXdWdWtRelFGYWFaUFp0Z1lEVWh5MXYwazJ6RWVRMnVMejQ0bnprODkxOHNtLXZpUWZrUXpGbVloOHA0MlYxYVo3dzJKSVBTdGFPNGxqcE5ZLWUzNDB2YUMzZGwyc3pnZw?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQMXJUSGZtR1ZhcTcyLVcyejBYaUN6Q3AwTnVaOGFDOThqUm1PTjNTb1N0YmRDVk8yQW1ZVW1tYVlkZDctekJVMV9zcTd6aWM4TURYV1NrVExYdEdTYlpyZFp3aDQyamVsYk5jZFExMWNZR01sb05wR05EVmx2TmZTM0xueFVQS2ktSDRtaV90NVk1eVl1Mnc?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
