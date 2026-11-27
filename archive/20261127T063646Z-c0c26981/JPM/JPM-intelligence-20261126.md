# JPM Intelligence Report

- ticker: **JPM**
- Report as_of: **2026-11-26**
- Market data as_of: **2026-11-25**
- Quant sources: https://finance.yahoo.com/quote/JPM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/JPM/key-statistics/
- AI analysis snapshot as_of: **2026-11-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-27T06:53:07.434859+00:00**
- AI status: **Partial: 1 headline remains unclassified and excluded from research conclusions**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 20, 'rule': 2, 'ai': 10, 'unknown': 1, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **10** exact headline/source/date matches; prior report **20261126T064454Z-dbdd6f45/JPM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 20 unique headlines; 7 named publishers; 0 exact duplicates; 20 HTTPS source links; largest publisher share 45.0%; oldest publication 2026-11-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 316.7400 |
| Return 1D (%) | -0.1135 |
| Return 1W (%) | -2.2739 |
| Return 1M (%) | -4.4755 |
| Return YTD (%) | 0.1925 |
| Return 1Y (%) | 6.5480 |
| Annualized volatility (%) | 23.1021 |
| Beta vs SPY | 0.7656 |
| Max drawdown (%) | -15.4717 |
| Sharpe (rf=0) | 0.3911 |
| Downside deviation (rf=0, %) | 16.7435 |
| Sortino (rf=0) | 0.5396 |
| Historical VaR 95% (1D, %) | 2.4552 |
| Historical ES 95% (1D, %) | 3.3659 |
| Correlation vs SPY | 0.4948 |
| Tracking error vs SPY (%) | 20.3787 |
| P/E (trailing) | 13.29 |
| P/B | 2.39 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 10.20 |
| Forward P/E (estimate) | 12.39 |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 44.79 |
| Return on equity (%) | 18.01 |
| Free cash flow yield (%) | N/A |
| MA50 | 334.8915 |
| Close vs MA50 (%) | -5.4201 |
| MA200 | 322.8898 |
| Close vs MA200 (%) | -1.9046 |
| RSI (14, Wilder) | 37.0805 |
| MACD (12,26) | -5.7823 |
| MACD signal (9) | -3.1242 |
| MACD histogram | -2.6581 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'JPM': 290, 'SPY': 290}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 316.7400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.1135 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.2739 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -4.4755 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 0.1925 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 6.5480 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 23.1021 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.7435 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.5396 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.4552 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.3659 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4948 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 20.3787 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.7656 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.4717 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3911 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 12.3857 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 44.7880 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 18.0130 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 13.2861 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 37.0805 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -2.6581 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -5.4201 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -1.9046 -> Slightly below the moving-average trend level.

## TAILWINDS

### JPMorgan Chase (JPM) Stock Still Looks Like A Bargain On Its 122% Run
- Summary: Stock appears undervalued, suggesting potential upside.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPQzVkNFFCMi1sUzRfQkxuRzdhLWRjaGw2N3N6ZEY3OU9EX0JLLUNRQktEekxYM1JmUlc3TWFGaXZFY0ZlbjNtdHoyVTc4WTdyaDl1eVFkVUlacXFSMHYwNWxNYjlVUTM3WHBjbVBiUnFRRlJoTWlWamF1UlROZVkzbGpwMTlLLUh6V0hJa1dZVlNqdVdER2xFOS1Xbw?oc=5>

### JPMorgan, HSBC, StoneX complete first digital gold trade in London (JPM:NYSE)
- Summary: First digital gold trade in London involving JPMorgan, HSBC, and StoneX, marking a new product launch.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxQWnZJeTlaTFFpSS0xZXlZSENJVTM5Z3Q0Wm52NF9ia2RfZ3c1YTViNzBQSE1TUWs2amFWVXl3VjFFVmRmWk8tS0hIVFRWTG02a2hSTmJTSmVjZHU5STZJSHhmNFM1VnV4enBoTUlKajdMdGNsRUhUVWpuZFFzUi0zS3otSEdVeEVCUEZQU0VWNXlTSFhwcm9ueTJfMVpZTnQ4Tng2cg?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### JPMorgan Chase & Co. $JPM Shares Acquired by State Board of Administration of Florida Retirement System
- Summary: JPMorgan Chase & Co. $JPM Shares Acquired by State Board of Administration of Florida Retirement System
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi8gFBVV95cUxNNWNKYjV2UWxQSnkzZkFDMFpzd1FzeENVR1ZrUnpLY3V6bm1jRWZneDVmNWM3cDZJaTUzZU0xLU5rRWYxT2ZFVERNSkZqOFhUSzRab0dCa2RJX2V0NTd6QndMc1ZmQUs5UnFSMndFMWZNZHBzWWdhWDRKejMzc1EzdUlPc3lVdFJYQUs5WVBpYlJKdGZURkEzaHpSWkJjbFN4RnVFNWpuRlJRbnVZLUVwSFIyVHNLRm9oNlZfRWw2VkVBTG9hdzZ5ZlN0V281Tl9mM1cyckF3a05QeFVlbUllVHVFTDBhcHU3dFJQSk90WFRQQQ?oc=5>

### JPMorgan Chase & Co. $JPM Stock Purchased by Bessemer Group Inc.
- Summary: JPMorgan Chase & Co. $JPM Stock Purchased by Bessemer Group Inc.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxNSlNkM3FYeXlxdDY1TXZKcDJlR1pJX2ZadGoyODNRQTNqMzkxUFNoLVBILVEzR3RhbURJVUd4eWo4NF9RNmlkeS12eVMyS0RZTnAtNFhBYlFiOGhsMlcyblc5WWRIRjZhMlpuYTZOcS1uRm5BcWdxY1VyQ1Iyc19Cek1EUWNtVm5ENUNpa3IxNjVSMnIxMmZhVkIwVl9tbU8yVGdrOHJuMmVKeHBEZTZheTl0V0ZRMEVHbDNyQw?oc=5>

### JPMorgan Chase & Co. (NYSE:JPM) Stock Sale Revealed by Rep. Harriet M. Hageman
- Summary: Rep. Hageman disclosed JPM stock sale.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxNSGdMSGN5TXhMemE4WWxpNm5td2JRS0ZiVFFuWlMwR1c4NS1BdnRIUDlYNFhhOXFOdmx0WXYxMnhNa1JSalU3bmdvV0ZCOFZETFBnamJqVXdfWTBjYmk5UVZXbXJ2QzJzeXplXzRmbUlnRzN0bUFyNzF0SmIzQVB5RS14d2NJM3pZVElwMEhLaGdEcnpBR0RuQ2w3SVJTem9PLWplSHJXRXp6OFl3c25HdnJOdTlncVBDWmJ2dk1NamZJSThCYUZHRmV5azhGakU?oc=5>

### JPMorgan Chase & Co. $JPM Stock Holdings Lifted by Steward Partners Investment Advisory LLC
- Summary: Steward Partners increased JPM holdings.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4gFBVV95cUxQMk1RX2tWaHFQY05LZjdvVE9vUndzS2NENkhHeG1rQXNrVWZIRFhvSzItVmpOMHJ6Ul9Fck1OaHlTLURpTE1Hd0xSdlRXSzZZVEF6ZVJXdGN0MUVKb0NLSTVGQ0c1YkhRZURaQ3ROTFQxOGxoaW9wN3QtSHA1YU9UUDRic1FqYVJJZE5lbXYyOE5ocEZEMmxXLUhHUDl5NmI2bWlpMl8wcEhrdExzY0FPcm9OWHROdWZvQ21OamhHRFJEdmNObFRlZ2xfYUEtNUFyTDllQ2JDQ0t6bVdGYVp1SFdR?oc=5>

### JPMorgan Chase (JPM) Says Vendor Cyberattack Exposed Customer Data
- Summary: Vendor cyberattack exposed customer data.
- Date: 2026-11-22 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxNcGZsSnc2NEFiS2tDdllhMmJ2V243b2lyQ0pUdkQ4SUpEVjlZakFtTlg3bUxVanlBWWh2RnFEd3dyaXBtOS1Eb2xmbDdWQWk1SWVoay1RS1FCQ2VYdXhzLUQzc0lCUGZySWdQY3EtOFVKc0FPV1h5dTd1MXFieW9sUkFPa1VST3NwZ3NKM0d2U0U3Rm1sOUpuOF9fV0E5WW0wenp5N1hTNmZqU1NCRTNNRGZReXFTTWtNQUQ3bmFmNjMxRnZj0gHKAUFVX3lxTE9lUXloUGRvaXRMdVhyc0NNVnVGYmVaVERkdGpLbEFCUGQ1dG9Rc3IxZUZVNHFOZWJYZmNXMUxudFc2dEZHYk5hY0lDSG9QRk92LWszOUhyeHl0YnljYzhtRlhiS0pLSTdlUkNVWkhfTDZQVlBIS0tjSzFxd0hCYVV0blM1OEg0NTZQWFJlc0FZaXlRN2ptOEZBR0hiUi1xSmZ0MVozUkpKa3BaM1VRZy1IZkpqdkFocmE5MlRreENpSjdUN0hONjFYeHc?oc=5>

### JPMorgan Chase & Co. (NYSE:JPM) Shares Unloaded by Rep. Harriet M. Hageman
- Summary: Rep. Hageman unloaded JPM shares.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxNSTVaNEtRcTNHUUFHQzZDT2dKUFVBNnVSWndEZzRQTktMNkI5TWdlQTJiRmNrYkJhbXdnM3NOZmJHbFY5Nk8xQ29iVDAySV9xRUl0V2xlNnBPTV94dDJiOWtoemtDRndQTWZOTTdQaC1vcUxONVhoNFNnSThQUlR0amc0d2ZLenZCRkUteGxCNE9VM3NRT1d4c3phN0F2Snk5amR2T25TcENhcC01eVkxelJ6M0Q0bk85bmdVYkJVLWtBZm1sRnZib29B?oc=5>

### 105,134 JPMorgan Chase & Co. $JPM Shares Bought by Private Advisor Group LLC
- Summary: Private advisor group purchased 105,134 JPM shares, indicating institutional interest.
- Date: 2026-11-22 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxNOGtpX1VWZm9ELWJOcFdFZ29pajNkSmJoWjBRNHZkVVdpQXJ5WE9wMlFtdDh0eFV1NlhKajZ4cXl0aHJuTEZPMFdNVVdqelduN0RxN2NnTkpxUjljNDN5RmlWZU5MS3ZXNEVvS1dPTC1HTHFOVjdRTkhqcTd4TDNwZDgtMTR3ZW9XMHk5N1V0TFBrRVV6ajgzUVVCWHZfQUJtdzBITWh2MHdlUVZrZnE2NEJwbGdoeC1kckdRUWlBYjVGWmhlYUVhblRFN1k?oc=5>

### 115,612 JPMorgan Chase & Co. $JPM Shares Bought by Banco Santander S.A.
- Summary: Banco Santander purchased 115,612 JPM shares, indicating a short‑term market move. No direct impact on JPM’s operations.
- Date: 2026-11-21 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxPX0RZYWJycXFWMjlLRTVxVHhnTjRNNkljbFVfRW9lRVEtMXp1ZHJYRmNIMHpFRXB5QzVENm9GUllySkl2Yy1uUXkwQTVjSllUR29WOUNyZDJpLVFzb2VSb1FxcU56N1M1dUpYbHFKalk3THVYaTZ4OGVOcFh0ZHhZWVhVYkduNWxXbVFNMWE4SjcybGdwUk9SaWFnTjFEQkNRb1ZZbkN3ZDNQeGI5ZVQ5N3VINHRXV3lRZDJfbkMwYkhiUzg?oc=5>

## RISKS

### JPMorgan Chase (JPM) CEO Warns UK Tax Rise Could Threaten £3 Billion HQ
- Summary: CEO warns UK tax increase could threaten £3B of headquarters investment.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNUC02Wm1pYmVvVF9tU3VTaXcyMFBSdUdwbW5NajJoendLYmUxX05oMGRqbmVZRXctTHVhV0JHYUdPNElCMV9jSjhIT2JIdlpDUk5zdXpfUE1yT2pBWk5SR3M4UUtkTy12VWt0RHBrdDBNVDJDSWo5cWpLOGMwZlZSQlQxbzhWWDJjM0FHUmlNNUllNUE2VVlLcA?oc=5>

### 311,218 Shares in JPMorgan Chase & Co. $JPM Acquired by Advisors Asset Management Inc.
- Summary: An advisor acquired 311,218 JPM shares.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxOdjdkTFlBUVE0aEZERmt3QVY2UDlTQXU2WV9sUkdRRmNlU3FnU2MxUTRwSVM2YnNpbmxwYkRqSmpOR1BZZ3BTUEhMZ1FyNjFWNXZuT2NKNVBOOHZocUR5RUVkVzY5TC1md0RqSkU0aWtlRHRpZDhYZGdQMTlaNEdJQ2w5ZVM0aG1jQ3RzcHIzbjBqbjF1ZDNMNm1BcXdlTjJLSlExM0lVbHlvXzVHaGxxUWk5eDY4elBKNWxoZHlDRGJ2eVIzODFhNUY3Rklzb2RkMm81OW41bTE?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **JPM** | **13.29** | **2.39** | **N/A** | **10.20** | **841,137,782,784.00 USD** | **6.55** |
| BAC | 11.58 | 1.24 | N/A | 3.40 | 334,936,145,920.00 USD | -5.54 |
| C | 11.05 | 0.98 | N/A | 8.00 | 187,584,331,776.00 USD | 14.34 |
| WFC | 11.42 | 1.53 | N/A | 0.40 | 242,969,772,032.00 USD | -2.75 |

Peers fetched as_of: 2026-11-26; JPM reuses existing data (market data as_of: 2026-11-25); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-13
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-26

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

- https://news.google.com/rss/articles/CBMimwFBVV95cUxPQzVkNFFCMi1sUzRfQkxuRzdhLWRjaGw2N3N6ZEY3OU9EX0JLLUNRQktEekxYM1JmUlc3TWFGaXZFY0ZlbjNtdHoyVTc4WTdyaDl1eVFkVUlacXFSMHYwNWxNYjlVUTM3WHBjbVBiUnFRRlJoTWlWamF1UlROZVkzbGpwMTlLLUh6V0hJa1dZVlNqdVdER2xFOS1Xbw?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxQWnZJeTlaTFFpSS0xZXlZSENJVTM5Z3Q0Wm52NF9ia2RfZ3c1YTViNzBQSE1TUWs2amFWVXl3VjFFVmRmWk8tS0hIVFRWTG02a2hSTmJTSmVjZHU5STZJSHhmNFM1VnV4enBoTUlKajdMdGNsRUhUVWpuZFFzUi0zS3otSEdVeEVCUEZQU0VWNXlTSFhwcm9ueTJfMVpZTnQ4Tng2cg?oc=5
- https://news.google.com/rss/articles/CBMi8gFBVV95cUxNNWNKYjV2UWxQSnkzZkFDMFpzd1FzeENVR1ZrUnpLY3V6bm1jRWZneDVmNWM3cDZJaTUzZU0xLU5rRWYxT2ZFVERNSkZqOFhUSzRab0dCa2RJX2V0NTd6QndMc1ZmQUs5UnFSMndFMWZNZHBzWWdhWDRKejMzc1EzdUlPc3lVdFJYQUs5WVBpYlJKdGZURkEzaHpSWkJjbFN4RnVFNWpuRlJRbnVZLUVwSFIyVHNLRm9oNlZfRWw2VkVBTG9hdzZ5ZlN0V281Tl9mM1cyckF3a05QeFVlbUllVHVFTDBhcHU3dFJQSk90WFRQQQ?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxNSlNkM3FYeXlxdDY1TXZKcDJlR1pJX2ZadGoyODNRQTNqMzkxUFNoLVBILVEzR3RhbURJVUd4eWo4NF9RNmlkeS12eVMyS0RZTnAtNFhBYlFiOGhsMlcyblc5WWRIRjZhMlpuYTZOcS1uRm5BcWdxY1VyQ1Iyc19Cek1EUWNtVm5ENUNpa3IxNjVSMnIxMmZhVkIwVl9tbU8yVGdrOHJuMmVKeHBEZTZheTl0V0ZRMEVHbDNyQw?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxNSGdMSGN5TXhMemE4WWxpNm5td2JRS0ZiVFFuWlMwR1c4NS1BdnRIUDlYNFhhOXFOdmx0WXYxMnhNa1JSalU3bmdvV0ZCOFZETFBnamJqVXdfWTBjYmk5UVZXbXJ2QzJzeXplXzRmbUlnRzN0bUFyNzF0SmIzQVB5RS14d2NJM3pZVElwMEhLaGdEcnpBR0RuQ2w3SVJTem9PLWplSHJXRXp6OFl3c25HdnJOdTlncVBDWmJ2dk1NamZJSThCYUZHRmV5azhGakU?oc=5
- https://news.google.com/rss/articles/CBMi4gFBVV95cUxQMk1RX2tWaHFQY05LZjdvVE9vUndzS2NENkhHeG1rQXNrVWZIRFhvSzItVmpOMHJ6Ul9Fck1OaHlTLURpTE1Hd0xSdlRXSzZZVEF6ZVJXdGN0MUVKb0NLSTVGQ0c1YkhRZURaQ3ROTFQxOGxoaW9wN3QtSHA1YU9UUDRic1FqYVJJZE5lbXYyOE5ocEZEMmxXLUhHUDl5NmI2bWlpMl8wcEhrdExzY0FPcm9OWHROdWZvQ21OamhHRFJEdmNObFRlZ2xfYUEtNUFyTDllQ2JDQ0t6bVdGYVp1SFdR?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxNcGZsSnc2NEFiS2tDdllhMmJ2V243b2lyQ0pUdkQ4SUpEVjlZakFtTlg3bUxVanlBWWh2RnFEd3dyaXBtOS1Eb2xmbDdWQWk1SWVoay1RS1FCQ2VYdXhzLUQzc0lCUGZySWdQY3EtOFVKc0FPV1h5dTd1MXFieW9sUkFPa1VST3NwZ3NKM0d2U0U3Rm1sOUpuOF9fV0E5WW0wenp5N1hTNmZqU1NCRTNNRGZReXFTTWtNQUQ3bmFmNjMxRnZj0gHKAUFVX3lxTE9lUXloUGRvaXRMdVhyc0NNVnVGYmVaVERkdGpLbEFCUGQ1dG9Rc3IxZUZVNHFOZWJYZmNXMUxudFc2dEZHYk5hY0lDSG9QRk92LWszOUhyeHl0YnljYzhtRlhiS0pLSTdlUkNVWkhfTDZQVlBIS0tjSzFxd0hCYVV0blM1OEg0NTZQWFJlc0FZaXlRN2ptOEZBR0hiUi1xSmZ0MVozUkpKa3BaM1VRZy1IZkpqdkFocmE5MlRreENpSjdUN0hONjFYeHc?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxNSTVaNEtRcTNHUUFHQzZDT2dKUFVBNnVSWndEZzRQTktMNkI5TWdlQTJiRmNrYkJhbXdnM3NOZmJHbFY5Nk8xQ29iVDAySV9xRUl0V2xlNnBPTV94dDJiOWtoemtDRndQTWZOTTdQaC1vcUxONVhoNFNnSThQUlR0amc0d2ZLenZCRkUteGxCNE9VM3NRT1d4c3phN0F2Snk5amR2T25TcENhcC01eVkxelJ6M0Q0bk85bmdVYkJVLWtBZm1sRnZib29B?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxNOGtpX1VWZm9ELWJOcFdFZ29pajNkSmJoWjBRNHZkVVdpQXJ5WE9wMlFtdDh0eFV1NlhKajZ4cXl0aHJuTEZPMFdNVVdqelduN0RxN2NnTkpxUjljNDN5RmlWZU5MS3ZXNEVvS1dPTC1HTHFOVjdRTkhqcTd4TDNwZDgtMTR3ZW9XMHk5N1V0TFBrRVV6ajgzUVVCWHZfQUJtdzBITWh2MHdlUVZrZnE2NEJwbGdoeC1kckdRUWlBYjVGWmhlYUVhblRFN1k?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxPX0RZYWJycXFWMjlLRTVxVHhnTjRNNkljbFVfRW9lRVEtMXp1ZHJYRmNIMHpFRXB5QzVENm9GUllySkl2Yy1uUXkwQTVjSllUR29WOUNyZDJpLVFzb2VSb1FxcU56N1M1dUpYbHFKalk3THVYaTZ4OGVOcFh0ZHhZWVhVYkduNWxXbVFNMWE4SjcybGdwUk9SaWFnTjFEQkNRb1ZZbkN3ZDNQeGI5ZVQ5N3VINHRXV3lRZDJfbkMwYkhiUzg?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNUC02Wm1pYmVvVF9tU3VTaXcyMFBSdUdwbW5NajJoendLYmUxX05oMGRqbmVZRXctTHVhV0JHYUdPNElCMV9jSjhIT2JIdlpDUk5zdXpfUE1yT2pBWk5SR3M4UUtkTy12VWt0RHBrdDBNVDJDSWo5cWpLOGMwZlZSQlQxbzhWWDJjM0FHUmlNNUllNUE2VVlLcA?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxOdjdkTFlBUVE0aEZERmt3QVY2UDlTQXU2WV9sUkdRRmNlU3FnU2MxUTRwSVM2YnNpbmxwYkRqSmpOR1BZZ3BTUEhMZ1FyNjFWNXZuT2NKNVBOOHZocUR5RUVkVzY5TC1md0RqSkU0aWtlRHRpZDhYZGdQMTlaNEdJQ2w5ZVM0aG1jQ3RzcHIzbjBqbjF1ZDNMNm1BcXdlTjJLSlExM0lVbHlvXzVHaGxxUWk5eDY4elBKNWxoZHlDRGJ2eVIzODFhNUY3Rklzb2RkMm81OW41bTE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
