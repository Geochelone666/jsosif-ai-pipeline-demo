# JPM Intelligence Report

- ticker: **JPM**
- Report as_of: **2026-11-27**
- Market data as_of: **2026-11-27**
- Quant sources: https://finance.yahoo.com/quote/JPM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/JPM/key-statistics/
- AI analysis snapshot as_of: **2026-11-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-28T06:11:00.236011+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 20, 'rule': 1, 'ai': 9, 'unknown': 0, 'irrelevant': 10})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261126T064454Z-dbdd6f45/JPM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 20 unique headlines; 9 named publishers; 1 exact duplicates; 20 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-11-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 322.9600 |
| Return 1D (%) | 1.9638 |
| Return 1W (%) | 4.0028 |
| Return 1M (%) | -3.8208 |
| Return YTD (%) | 2.1600 |
| Return 1Y (%) | 7.0017 |
| Annualized volatility (%) | 23.1150 |
| Beta vs SPY | 0.7647 |
| Max drawdown (%) | -15.4717 |
| Sharpe (rf=0) | 0.3341 |
| Downside deviation (rf=0, %) | 16.7770 |
| Sortino (rf=0) | 0.4604 |
| Historical VaR 95% (1D, %) | 2.4568 |
| Historical ES 95% (1D, %) | 3.3659 |
| Correlation vs SPY | 0.4969 |
| Tracking error vs SPY (%) | 20.3678 |
| P/E (trailing) | 13.55 |
| P/B | 2.44 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 10.20 |
| Forward P/E (estimate) | 12.63 |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 44.79 |
| Return on equity (%) | 18.01 |
| Free cash flow yield (%) | N/A |
| MA50 | 334.3992 |
| Close vs MA50 (%) | -3.4208 |
| MA200 | 322.9730 |
| Close vs MA200 (%) | -0.0040 |
| RSI (14, Wilder) | 43.3521 |
| MACD (12,26) | -5.5348 |
| MACD signal (9) | -3.6064 |
| MACD histogram | -1.9285 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'JPM': 291, 'SPY': 291}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 322.9600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.9638 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 4.0028 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -3.8208 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 2.1600 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 7.0017 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 23.1150 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.7770 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4604 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.4568 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.3659 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4969 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 20.3678 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.7647 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.4717 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3341 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 12.6289 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 44.7880 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 18.0130 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 13.5470 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 43.3521 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.9285 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -3.4208 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -0.0040 -> Slightly below the moving-average trend level.

## TAILWINDS

### JPMorgan Chase & Co. (JPM) Outpaces Stock Market Gains: What You Should Know
- Summary: JPMorgan Chase & Co. (JPM) Outpaces Stock Market Gains: What You Should Know
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQa01VV2lJTWEyWm1WRTJGZnA4eUQzQUhrUFRLZ1ZETmQ3NnJ1RFdrTnBzQ1BoZVpSelUyZUNaM0JUblpBUHhvRG9FZ0NxYmNjYThCQjRIby10V09SQURmWFFvNmRqV0k5TUQzR0JqbHdkWHg2R0JHNW5hYVVMWnlnLUtLX1Z4MXltRjFDejRwRWFWeEdMMDhQTUVOYw?oc=5>

### JPMorgan Chase (JPM) Stock Still Looks Like A Bargain On Its 122% Run
- Summary: Stock appears undervalued, suggesting potential upside.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPQzVkNFFCMi1sUzRfQkxuRzdhLWRjaGw2N3N6ZEY3OU9EX0JLLUNRQktEekxYM1JmUlc3TWFGaXZFY0ZlbjNtdHoyVTc4WTdyaDl1eVFkVUlacXFSMHYwNWxNYjlVUTM3WHBjbVBiUnFRRlJoTWlWamF1UlROZVkzbGpwMTlLLUh6V0hJa1dZVlNqdVdER2xFOS1Xbw?oc=5>

### JPMorgan, HSBC, StoneX complete first digital gold trade in London (JPM:NYSE)
- Summary: First digital gold trade in London involving JPMorgan, HSBC, and StoneX, marking a new product launch.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxQWnZJeTlaTFFpSS0xZXlZSENJVTM5Z3Q0Wm52NF9ia2RfZ3c1YTViNzBQSE1TUWs2amFWVXl3VjFFVmRmWk8tS0hIVFRWTG02a2hSTmJTSmVjZHU5STZJSHhmNFM1VnV4enBoTUlKajdMdGNsRUhUVWpuZFFzUi0zS3otSEdVeEVCUEZQU0VWNXlTSFhwcm9ueTJfMVpZTnQ4Tng2cg?oc=5>

### JPMorgan Chase Financial Company LLC Declares Quarterly Coupon on Alerian MLP Index ETN
- Summary: JPMorgan Chase LLC declares a quarterly coupon on its Alerian MLP Index ETN, providing dividend income to investors.
- Date: 2026-11-20 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxQOW1jbmc1R3N5QkszczFMYURJNjdMN2NSdE82bXdpaWJhMUFfZ3U0SzEwcVlFdFBlR0Nzdlp1QXdCYXdheXJQcmRVSGFBeGRnd1NxWFBFa2IwTXNwTGNQa0FwQldJV0FaamdiVjBJbjZMdHJtRlE0dW5xSnJsNWNBRmNrUnI4TTdNd2trRUo2cjAzTWEweDcwbXgzR3FnTmRTS3RCMmtfdkw1ODZSelZUd3JKRHZSeVk?oc=5>

### JP Morgan Chase & (JPM): Structured note tied to S&P 500 with 24.5-month term
- Summary: JPM offers a structured note linked to the S&P 500 with a 24.5‑month maturity.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxOaGNpaVF1VXJKY09Cc1Y5cUMzUkwyY2s1VjdaSmJyTHZ2dTRzLVVTN0hiRFJZWVV4OFQzdkI2c1k1am1fZVlOMVFlVmxrV3FaRW8tM0N0MHVISGRKNGRKdXNCbFFOU0JsRk8zNFMzdnpFb2V2cE5Zc3FqU3JWSmptZTRXcklhYW1ieGJB?oc=5>

### What Is JPMorgan Chase (JPM) Saying With Its $450 Billion AI Debt Call?
- Summary: JPM announces a $450 billion debt issuance focused on AI initiatives.
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQZGhBc2I3QjlQXzhURDdwTEp3YlBJQTd2OXNGNzVpUGNBR2NVLW4tRk9GRnhCVlBmVUk5WERiVWVJYWgtaHBqa0diZ1ZjdERYSWRVZ0dnSnRKZmttSWFJN0tOTWdwa2lpTGNFNkg1X0kxYW5Scm9JaUhHa3ZGU0UtRVNidnV4WmJFb0FfVjVLZnR0dW9nRnFWUw?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Investors Heavily Search JPMorgan Chase & Co. (JPM): Here is What You Need to Know
- Summary: Search interest spikes for JPM, indicating heightened investor attention.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxOTi1Qa21zWU1iRlVjR0ZvUTNYYnNHQjNucnBpWFZlYU5MSmZuTkxJZ3c5ZGFlRWJRODl1cWs2dzBNLUMxNlhpckotWmNua3NQMlN2OVdCTXVUMGQyN3R5SExOM2RpOUJ0QURHeUFYN2dpeWxBUVowZ21Sc2lpcTh2d1lfRGl1YXpETGE2cjR1NHBvUmJIa0hBSURUY0dmUFpDZVVOMFZvRQ?oc=5>

### JPMorgan Chase (JPM) Says Vendor Cyberattack Exposed Customer Data
- Summary: Vendor cyberattack exposed customer data.
- Date: 2026-11-22 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxNcGZsSnc2NEFiS2tDdllhMmJ2V243b2lyQ0pUdkQ4SUpEVjlZakFtTlg3bUxVanlBWWh2RnFEd3dyaXBtOS1Eb2xmbDdWQWk1SWVoay1RS1FCQ2VYdXhzLUQzc0lCUGZySWdQY3EtOFVKc0FPV1h5dTd1MXFieW9sUkFPa1VST3NwZ3NKM0d2U0U3Rm1sOUpuOF9fV0E5WW0wenp5N1hTNmZqU1NCRTNNRGZReXFTTWtNQUQ3bmFmNjMxRnZj0gHKAUFVX3lxTE9lUXloUGRvaXRMdVhyc0NNVnVGYmVaVERkdGpLbEFCUGQ1dG9Rc3IxZUZVNHFOZWJYZmNXMUxudFc2dEZHYk5hY0lDSG9QRk92LWszOUhyeHl0YnljYzhtRlhiS0pLSTdlUkNVWkhfTDZQVlBIS0tjSzFxd0hCYVV0blM1OEg0NTZQWFJlc0FZaXlRN2ptOEZBR0hiUi1xSmZ0MVozUkpKa3BaM1VRZy1IZkpqdkFocmE5MlRreENpSjdUN0hONjFYeHc?oc=5>

### JPMorgan Chase Tests Key $310 Support After Multi-Week Pullback (NYSE:JPM)
- Summary: JPM shares tested $310 support after a multi-week pullback, indicating potential short-term resistance. Market participants watch for breakout or reversal.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxPWDMxckhxRk1mR3pQQjVKenJYU1haZ3Nyc2dBR21KdE52MEdvb1lPazdaemJ4RnF3Zk9rd0hPclBIRXZtaHZ0WGhONm1HWkFPZ1NHZ3BudGRFZTk0TmN1ZnVhMjBIQkE2MF84WjdzWGtjOWJwLXdLSklxUVpwSm54RmtRN3ZWZm5tTS1SUHNBeV9GV0ZyMW9zYi1NQjJxZXRfUE5Ob1lrR3JGcGtmaGF4QmUzQUVzMEE?oc=5>

## RISKS

### JPMorgan Chase (JPM) CEO Warns UK Tax Rise Could Threaten £3 Billion HQ
- Summary: CEO warns UK tax increase could threaten £3B of headquarters investment.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNUC02Wm1pYmVvVF9tU3VTaXcyMFBSdUdwbW5NajJoendLYmUxX05oMGRqbmVZRXctTHVhV0JHYUdPNElCMV9jSjhIT2JIdlpDUk5zdXpfUE1yT2pBWk5SR3M4UUtkTy12VWt0RHBrdDBNVDJDSWo5cWpLOGMwZlZSQlQxbzhWWDJjM0FHUmlNNUllNUE2VVlLcA?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **JPM** | **13.55** | **2.44** | **N/A** | **10.20** | **857,655,672,832.00 USD** | **7.00** |
| BAC | 11.71 | 1.25 | N/A | 3.40 | 338,593,251,328.00 USD | -5.42 |
| C | 11.27 | 1.00 | N/A | 8.00 | 191,325,077,504.00 USD | 15.10 |
| WFC | 11.61 | 1.56 | N/A | 0.40 | 246,992,240,640.00 USD | -1.67 |

Peers fetched as_of: 2026-11-27; JPM reuses existing data (market data as_of: 2026-11-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-13
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

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
- Filing date: 2026-11-03
- Revenue (latest available single quarter): 24,246,000,000.00 USD; period 2014-07-01/2014-09-30; fiscal year/reporting period 2014/Q3
- Net income (latest available single quarter): 15,305,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/19617/000162828026069523/jpm-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimwFBVV95cUxQa01VV2lJTWEyWm1WRTJGZnA4eUQzQUhrUFRLZ1ZETmQ3NnJ1RFdrTnBzQ1BoZVpSelUyZUNaM0JUblpBUHhvRG9FZ0NxYmNjYThCQjRIby10V09SQURmWFFvNmRqV0k5TUQzR0JqbHdkWHg2R0JHNW5hYVVMWnlnLUtLX1Z4MXltRjFDejRwRWFWeEdMMDhQTUVOYw?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPQzVkNFFCMi1sUzRfQkxuRzdhLWRjaGw2N3N6ZEY3OU9EX0JLLUNRQktEekxYM1JmUlc3TWFGaXZFY0ZlbjNtdHoyVTc4WTdyaDl1eVFkVUlacXFSMHYwNWxNYjlVUTM3WHBjbVBiUnFRRlJoTWlWamF1UlROZVkzbGpwMTlLLUh6V0hJa1dZVlNqdVdER2xFOS1Xbw?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxQWnZJeTlaTFFpSS0xZXlZSENJVTM5Z3Q0Wm52NF9ia2RfZ3c1YTViNzBQSE1TUWs2amFWVXl3VjFFVmRmWk8tS0hIVFRWTG02a2hSTmJTSmVjZHU5STZJSHhmNFM1VnV4enBoTUlKajdMdGNsRUhUVWpuZFFzUi0zS3otSEdVeEVCUEZQU0VWNXlTSFhwcm9ueTJfMVpZTnQ4Tng2cg?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxQOW1jbmc1R3N5QkszczFMYURJNjdMN2NSdE82bXdpaWJhMUFfZ3U0SzEwcVlFdFBlR0Nzdlp1QXdCYXdheXJQcmRVSGFBeGRnd1NxWFBFa2IwTXNwTGNQa0FwQldJV0FaamdiVjBJbjZMdHJtRlE0dW5xSnJsNWNBRmNrUnI4TTdNd2trRUo2cjAzTWEweDcwbXgzR3FnTmRTS3RCMmtfdkw1ODZSelZUd3JKRHZSeVk?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxOaGNpaVF1VXJKY09Cc1Y5cUMzUkwyY2s1VjdaSmJyTHZ2dTRzLVVTN0hiRFJZWVV4OFQzdkI2c1k1am1fZVlOMVFlVmxrV3FaRW8tM0N0MHVISGRKNGRKdXNCbFFOU0JsRk8zNFMzdnpFb2V2cE5Zc3FqU3JWSmptZTRXcklhYW1ieGJB?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQZGhBc2I3QjlQXzhURDdwTEp3YlBJQTd2OXNGNzVpUGNBR2NVLW4tRk9GRnhCVlBmVUk5WERiVWVJYWgtaHBqa0diZ1ZjdERYSWRVZ0dnSnRKZmttSWFJN0tOTWdwa2lpTGNFNkg1X0kxYW5Scm9JaUhHa3ZGU0UtRVNidnV4WmJFb0FfVjVLZnR0dW9nRnFWUw?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxOTi1Qa21zWU1iRlVjR0ZvUTNYYnNHQjNucnBpWFZlYU5MSmZuTkxJZ3c5ZGFlRWJRODl1cWs2dzBNLUMxNlhpckotWmNua3NQMlN2OVdCTXVUMGQyN3R5SExOM2RpOUJ0QURHeUFYN2dpeWxBUVowZ21Sc2lpcTh2d1lfRGl1YXpETGE2cjR1NHBvUmJIa0hBSURUY0dmUFpDZVVOMFZvRQ?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxNcGZsSnc2NEFiS2tDdllhMmJ2V243b2lyQ0pUdkQ4SUpEVjlZakFtTlg3bUxVanlBWWh2RnFEd3dyaXBtOS1Eb2xmbDdWQWk1SWVoay1RS1FCQ2VYdXhzLUQzc0lCUGZySWdQY3EtOFVKc0FPV1h5dTd1MXFieW9sUkFPa1VST3NwZ3NKM0d2U0U3Rm1sOUpuOF9fV0E5WW0wenp5N1hTNmZqU1NCRTNNRGZReXFTTWtNQUQ3bmFmNjMxRnZj0gHKAUFVX3lxTE9lUXloUGRvaXRMdVhyc0NNVnVGYmVaVERkdGpLbEFCUGQ1dG9Rc3IxZUZVNHFOZWJYZmNXMUxudFc2dEZHYk5hY0lDSG9QRk92LWszOUhyeHl0YnljYzhtRlhiS0pLSTdlUkNVWkhfTDZQVlBIS0tjSzFxd0hCYVV0blM1OEg0NTZQWFJlc0FZaXlRN2ptOEZBR0hiUi1xSmZ0MVozUkpKa3BaM1VRZy1IZkpqdkFocmE5MlRreENpSjdUN0hONjFYeHc?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxPWDMxckhxRk1mR3pQQjVKenJYU1haZ3Nyc2dBR21KdE52MEdvb1lPazdaemJ4RnF3Zk9rd0hPclBIRXZtaHZ0WGhONm1HWkFPZ1NHZ3BudGRFZTk0TmN1ZnVhMjBIQkE2MF84WjdzWGtjOWJwLXdLSklxUVpwSm54RmtRN3ZWZm5tTS1SUHNBeV9GV0ZyMW9zYi1NQjJxZXRfUE5Ob1lrR3JGcGtmaGF4QmUzQUVzMEE?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNUC02Wm1pYmVvVF9tU3VTaXcyMFBSdUdwbW5NajJoendLYmUxX05oMGRqbmVZRXctTHVhV0JHYUdPNElCMV9jSjhIT2JIdlpDUk5zdXpfUE1yT2pBWk5SR3M4UUtkTy12VWt0RHBrdDBNVDJDSWo5cWpLOGMwZlZSQlQxbzhWWDJjM0FHUmlNNUllNUE2VVlLcA?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
