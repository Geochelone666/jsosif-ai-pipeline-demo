# BRK-B Intelligence Report

- ticker: **BRK-B**
- Report as_of: **2026-11-25**
- Market data as_of: **2026-11-25**
- Quant sources: https://finance.yahoo.com/quote/BRK-B/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/BRK-B/key-statistics/
- AI analysis snapshot as_of: **2026-11-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-26T07:07:05.272693+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 0, 'ai': 12, 'unknown': 0, 'irrelevant': 10})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261125T065354Z-0b3565c6/BRK-B** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **5**; {'directional_claim_without_event_type': 5}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 5 named publishers; 3 exact duplicates; 22 HTTPS source links; largest publisher share 54.55%; oldest publication 2026-11-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 579.3200 |
| Return 1D (%) | 0.3655 |
| Return 1W (%) | 0.8179 |
| Return 1M (%) | 6.8482 |
| Return YTD (%) | 15.2532 |
| Return 1Y (%) | 13.9116 |
| Annualized volatility (%) | 15.1487 |
| Beta vs SPY | 0.0784 |
| Max drawdown (%) | -9.4218 |
| Sharpe (rf=0) | 0.9390 |
| Downside deviation (rf=0, %) | 10.2423 |
| Sortino (rf=0) | 1.3888 |
| Historical VaR 95% (1D, %) | 1.4206 |
| Historical ES 95% (1D, %) | 2.0519 |
| Correlation vs SPY | 0.0772 |
| Tracking error vs SPY (%) | 20.4319 |
| P/E (trailing) | 16.21 |
| P/B | 0.00 |
| EV/EBITDA | -2.04 |
| Revenue growth (%) | 11.20 |
| Forward P/E (estimate) | 25.39 |
| Gross margin (%) | 26.60 |
| Operating margin (%) | 26.60 |
| Return on equity (%) | 10.57 |
| Free cash flow yield (%) | 4.26 |
| MA50 | 540.4118 |
| Close vs MA50 (%) | 7.1997 |
| MA200 | 503.6811 |
| Close vs MA200 (%) | 15.0172 |
| RSI (14, Wilder) | 62.7025 |
| MACD (12,26) | 10.4104 |
| MACD signal (9) | 13.0490 |
| MACD histogram | -2.6386 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'BRK-B': 290, 'SPY': 290}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 579.3200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.3655 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.8179 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 6.8482 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 15.2532 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 13.9116 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 15.1487 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 10.2423 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.3888 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.4206 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.0519 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0772 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 20.4319 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.0784 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -9.4218 -> Shallow peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9390 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 25.3903 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 26.6020 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 26.6020 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 10.5740 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.2635 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 16.2138 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 62.7025 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -2.6386 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 7.1997 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 15.0172 -> Clearly above the moving-average trend level.

## TAILWINDS

### I'm Raising My Fair Value Estimate for Berkshire Hathaway Stock. Here's What I Think It's Worth.
- Summary: Analyst raises Berkshire Hathaway fair value estimate, suggesting potential upside for investors.
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxQWHRsZlZodkt5dFpjZzVZaXhVUGxmMXE4S3FuZXlIOTlsUDhRMTVQbGxPd3M3c1FHQ2VIR285dVFyR3hrcktkUVcxQzY2V2dSQ0VKQWlTUHYtSzRWMlI2TGpEN2xMRjN5SFFfWEVmNGFMeUhqRlVWd3pIanBycmVtZy16aHJyakZ0WXlIRVg1dENZemJyUnRBXzJnZVo1aVlCdENXalhfQWVZeFg1dF9XYWhZd2NjWlNNMnpNdzdWdl94NkpNY0l5WjBmSHlVYVNQdWtj?oc=5>

### Is Berkshire Hathaway Stock a Buy if the Fed Keeps Raising Rates?
- Summary: Analyst questions Berkshire’s attractiveness amid rising rates.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxPTHZLVUVOT3BTR0lpekxMbTl5c3FzM3Z2X0lCXzhWLUx3YkJfNG5IY2hXdnJOaHhYVHQwbU5rYkoxQkdiX3M0UlF2Mnp5OE1OQUY4bUpzT3BUTDJlazNfallwcjhlQ185dlRpbHRGTHFtV0QzS3pEWWFIbE1fRGgyUEtUOUw4M2xzakpVYllCYWpTYlNtWEdpYThhUTdLRDUwMzIyMmhfVWJfOVU?oc=5>

### Berkshire Hathaway Is Up 15% in 2026 and Easily Beating the S&P 500. Is Berkshire Stock Better Than an Index Fund Now?
- Summary: Berkshire outperforms S&P 500, prompting comparison to index funds.
- Date: 2026-11-25 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi7wFBVV95cUxPOENwZXVyS0taYmgwWXZlUGJrcklMWWxMNnpHTURxckJfUWk1Z2NEWXQzSFRveUVTTEQ0eXZVWDZCX3ctV2MzRUl0ZlBEbks5eDFuOVZEbFEtaEZpRXlKQ1Z3RlUtdzJUTE9yYzBCU014WkFaaF9WOGFvZmdoMjh5OVN2SUNidHBUbHhtNm8zR09pdENBaVdPS3o4TGhac2c5bmNiazZzMXNxbUlobmd5RFQ3Yk0yUmYxTy1pcThTZExYVHJHWU82WkoyeDdTTl9YZzk4Xy1rdkxTV054WE5iUm9PVnFQRml2NkMzc0VzVQ?oc=5>

### Berkshire Hathaway Beating S&P 500 by 3X: Market Expert Credits Greg Abel - Alphabet (NASDAQ:GOOGL), Berk
- Summary: Berkshire’s returns triple S&P 500, attributed to Greg Abel.
- Date: 2026-11-25 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMijgJBVV95cUxNTGFtbWlFemJiRzAwdFdpY3hXLXBlTDYwNUFlZkI4dnd3QWFGRHkzY1dMOW9OQXBzWkxDLUFHOXdGb0ZYYmZuZU4yb1BjTXlpUWNLeXpOSG1hbXlldWFyc1ZrdGpKNEY0RTkzcFpNeUNZcWZzUFpuUVBBSUF1STh3bW94UXFPNFZTVE4tUVVsZkpLdnEyYUFFc3UwbUZERVRCUnZPN0tyZkp1V3FqaWNVQlhoZ2JIU1dWSWoyV1Y5ZkxKVzF6bXEtaWpEMFhEUlh6VjFkTlJWc25BT3RwejJ2anM2MVUtT0xsZE1RV1Q5Nlo5ek1vVzJtYmM3WTRxdWN1ZG9VOC1DaGhram8xcUE?oc=5>

### Warren Buffett and Greg Abel Collect Billions From These Untouchable Berkshire Hathaway Dividend Stocks
- Summary: Buffett and Abel benefit from high dividend Berkshire stocks.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQOHVHSFBBV1dzME9KU1o1LWFOaGtkVmhodWRXN2hrTnNNVDdXNmtxTkVfeHQ5N2dJQWJIaGlnaXhrb3llbHAwV2ppc3dJeWQyM08tMWJQVVlFdElZV3BVcDd6Zl9FdUhXUnpNUW5YWXlvM2g5MlJSS2hJZzNnWWdaaUY4M25aNC1XSkRIbjdmbEZQOFVWdFlaZUF3MzV4QQ?oc=5>

### Even Without Warren Buffett as CEO, Berkshire Hathaway Is Outperforming the S&P 500, Nasdaq, and Dow by the Widest Margin Since 2022. History Says This Is What Happens Next.
- Summary: Berkshire continues strong performance post-Buffett.
- Date: 2026-11-25 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuwJBVV95cUxPZ292dWJ4c1JyNWJFQ3BOUG00eE1NOWNTSkNOU0J3OWFLZlZqQXVCeE9qek9lTTBGdU42UUNMY0FGUDVlOFFqMFhkcnVLMVBWa05KQXJ5cjBVWXVRRVVKLWNKcWlySE02ZFZaWHVMU3Q0QW1OazdjcldxSmlmMWkwNVY3SUhRU1V6aUgwMElDMHRjSGVWbzVmWS1kT1VySmtzeUYxRUlKZG40Yklpc0psalN1MTNINnk1Y2hPUGUwSThTSlhSeXliMTB3bm0wZDBXSHJZcDVwNUx1ZFRRalJRTldrN0REZkpJVGVXT0Q4Rnk0Q3FSV0NaN0RlSXhQdVhVS19TQnNEeDNwRUNnTHBCeWN0N3d6M3A3Qjh4NTh4SV9rMkNTSUpKQk9tLWFIa1BwMGQ4YkNpQ1BMUVU?oc=5>

### How American Express Turned Berkshire’s $1.3 Billion Bet Into a $576 Million Annual Paycheck
- Summary: Berkshire’s $1.3B investment in American Express yields $576M annual profit, showcasing strong portfolio performance.
- Date: 2026-11-25 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxQOEVVLVYweGEyZnBGWElzb1YwaElRNndpZ0NHRGx1QmNiMVdsSzFPYk1BclNSWUg4WFRGQXlsTkNzMHY1eWhVTlV0SC1NZHlsNVAyMGktRkw5MnBhOHpQVnFLLWR6Q3AzQ2JBMlFCOEJVR1l0TUpoRDZpcmZ0aDdKVUlwU015NHBEMlVmemh0SGt5WmViMEVkWmoxbXJkNEQxN2dtcnA0VlBPRHpVSmVCcS1lVjZVN05RcEdKWFNtcTZzTGM?oc=5>

## HEADWINDS

### Warren Buffett Expects Berkshire Hathaway (BRKA, BRKB) Stock to Drop About 50% Again Someday. Here's What He Says to Do Then.
- Summary: Buffett predicts a future 50% drop in Berkshire stock, signaling potential downside risk.
- Date: 2026-11-19 | Impact: medium | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxQV1FWcTNHWTNfd3pnSmZ2MUJYWXpaWm0taXI3TFE5bmRyV041UjVRSUFiYmF6SENLYVV3ZWZiM2pZZ3FISlNUeS13MDhSaWdOVW10M09XVWVJVDllSkFaby1YYm9hZElMM1huZlU1OEJINmc4Z29QZC12Ri1hUThsWmc3TmdueXNoN3dYWlc0TTRHcDMyX1FjVVA1a21jelVzVmJmZU9LTTZwUQ?oc=5>

## CATALYSTS

### Warren Buffett’s Successor, Greg Abel, Has Invested Nearly 47% of Berkshire Hathaway’s $360 Billion Stock Portfolio in Just 3 Stocks (and None Are AI Hyperscalers)
- Summary: Greg Abel concentrated portfolio in three stocks, excluding AI hyperscalers.
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPam9lcUIybDhzMEFMZkFsU2xZWkdJR19fOGplTllISm95UXQ5SmVkLXlUMnZobzhDMmVWWlAtYjFsVzFfQjhPWGZwSkl2bnFvLTZnajEtYnlyQkFYcFUyYVRDMVoxb25UYmJNdWZnaXlJQzhMdHFZYUl3Z0RxbGxLUWNoeU5fQW85REdLWmMtRmNONnV4MXBWLU8zWVlLV3lF?oc=5>

### Warren Buffett's Successor, Greg Abel, Just Gave Investors a Big Clue as to What's Next for Stocks
- Summary: Greg Abel hints at Berkshire’s future strategy, suggesting potential shifts in investment focus.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxOeEZrZDRQWmV6U3lXSE1LbThlYVdhbVNaTlNacjhwczdJTE9xSF9NTVJIRWNmUXQwZXloLTBSN3lkcVBZQ011WmQ5bXZVU2hWeVBWYVJFeXFFOU0zYmlsUlo2NGNUWHljSE1OYWtpRDlzNlRpaGMxS1FWX1hOcHBuNEtEeWVod1dnUUNza1JVeFl6STE5alJ4enJjS0V4Q0pnLVE?oc=5>

### Warren Buffett's Successor, Greg Abel, Has Quietly Purchased 3 Stocks Since the Start of the Fourth Quarter, Including Shares of a Legal Monopoly
- Summary: Greg Abel quietly bought three stocks, including a legal monopoly, for Berkshire Hathaway.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4gFBVV95cUxNQVVWcmRVUEtYa2pDNVpjOUVqTVVNV3lKcGRXbWZ4SjZ2VmZrYS1Za09RdTAzbVdyMVMzRkNnbXVIMUVUanEydXhpTmtUcnFrVzBaVlgzOXdwdWlWWUNkWHNGSHB6ZDJaeURYOUR4dkhBZTFUM1dUUzNiQW9GZ25VbkVQTGtVa0sxUWNoS1RZTlB2and2c0dtb0VzRThacUpBSkZuRGtWRmVzTmI0YTN1bVFkRlFQVjB1NEZxX0xXQldEVnV5ZmVGcF85NjNYVDQzRDB6RlRhYk9EM1VPVGhEd1hn?oc=5>

## RISKS

### Berkshire Hathaway: Slightly Too Expensive To Be Worth It (Rating Downgrade) (NYSE:BRK.A)
- Summary: Downgrade suggests Berkshire may be overvalued.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxONzFpZ2xoSzlkazFtUkNhX09sQ1k0T2FwT19GenVaR3dwYi03M0s4Vk9GOG5ZTHpsWkxMMnd2U2Z5TXJtUDMwYmxjWnVUSGJ1YWdLcUZ6bXlxTHdiNFlKRjBHM1htejMtN1c2RVhtRDVlZXBlcFAyM3FIREY4MW1BdWVxQ1EyUFZZUjZiUzF6bjVaaUQ0U0R2c3l5WkwtQQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **BRK-B** | **16.21** | **0.00** | **-2.04** | **11.20** | **1,230,776,565,760.00 USD** | **13.91** |
| MKL | 14.09 | 1.31 | 8.10 | -11.20 | 24,207,783,936.00 USD | -4.67 |
| FFH.TO | 9.76 | 1.41 | 8.66 | 1.90 | 55,469,637,632.00 CAD | 10.57 |
| L | 15.37 | 1.23 | 8.71 | 1.90 | 22,471,268,352.00 USD | 3.23 |

Peers fetched as_of: 2026-11-25; BRK-B reuses existing data (market data as_of: 2026-11-25); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-07
- Next expected earnings: 2027-03-01 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-25

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-09
- Revenue (latest available single quarter): 105,647,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 22,112,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1067983/000119312526452412/brka-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi0wFBVV95cUxQWHRsZlZodkt5dFpjZzVZaXhVUGxmMXE4S3FuZXlIOTlsUDhRMTVQbGxPd3M3c1FHQ2VIR285dVFyR3hrcktkUVcxQzY2V2dSQ0VKQWlTUHYtSzRWMlI2TGpEN2xMRjN5SFFfWEVmNGFMeUhqRlVWd3pIanBycmVtZy16aHJyakZ0WXlIRVg1dENZemJyUnRBXzJnZVo1aVlCdENXalhfQWVZeFg1dF9XYWhZd2NjWlNNMnpNdzdWdl94NkpNY0l5WjBmSHlVYVNQdWtj?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxPTHZLVUVOT3BTR0lpekxMbTl5c3FzM3Z2X0lCXzhWLUx3YkJfNG5IY2hXdnJOaHhYVHQwbU5rYkoxQkdiX3M0UlF2Mnp5OE1OQUY4bUpzT3BUTDJlazNfallwcjhlQ185dlRpbHRGTHFtV0QzS3pEWWFIbE1fRGgyUEtUOUw4M2xzakpVYllCYWpTYlNtWEdpYThhUTdLRDUwMzIyMmhfVWJfOVU?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQUmlkSTY1Qmw3N2RZV3FCblNsTmtlR0VRRGNTR0wzNUZvOTVTQkVLNmJGWmxsenpaRWtHNHZoV1R5NEVLUkJOR2phc05ablc2N0dqaGlXN1FRX0NzRFdBOHROYnVhYWZpeXAtT3ZMR2FWTnFhSmlrMmRmZWxwMGlfRU83VEE5dWxrMjhCR1JlNzZzQVZaY2NBVDlILTNJUQ?oc=5
- https://news.google.com/rss/articles/CBMi7wFBVV95cUxPOENwZXVyS0taYmgwWXZlUGJrcklMWWxMNnpHTURxckJfUWk1Z2NEWXQzSFRveUVTTEQ0eXZVWDZCX3ctV2MzRUl0ZlBEbks5eDFuOVZEbFEtaEZpRXlKQ1Z3RlUtdzJUTE9yYzBCU014WkFaaF9WOGFvZmdoMjh5OVN2SUNidHBUbHhtNm8zR09pdENBaVdPS3o4TGhac2c5bmNiazZzMXNxbUlobmd5RFQ3Yk0yUmYxTy1pcThTZExYVHJHWU82WkoyeDdTTl9YZzk4Xy1rdkxTV054WE5iUm9PVnFQRml2NkMzc0VzVQ?oc=5
- https://news.google.com/rss/articles/CBMijgJBVV95cUxNTGFtbWlFemJiRzAwdFdpY3hXLXBlTDYwNUFlZkI4dnd3QWFGRHkzY1dMOW9OQXBzWkxDLUFHOXdGb0ZYYmZuZU4yb1BjTXlpUWNLeXpOSG1hbXlldWFyc1ZrdGpKNEY0RTkzcFpNeUNZcWZzUFpuUVBBSUF1STh3bW94UXFPNFZTVE4tUVVsZkpLdnEyYUFFc3UwbUZERVRCUnZPN0tyZkp1V3FqaWNVQlhoZ2JIU1dWSWoyV1Y5ZkxKVzF6bXEtaWpEMFhEUlh6VjFkTlJWc25BT3RwejJ2anM2MVUtT0xsZE1RV1Q5Nlo5ek1vVzJtYmM3WTRxdWN1ZG9VOC1DaGhram8xcUE?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQOHVHSFBBV1dzME9KU1o1LWFOaGtkVmhodWRXN2hrTnNNVDdXNmtxTkVfeHQ5N2dJQWJIaGlnaXhrb3llbHAwV2ppc3dJeWQyM08tMWJQVVlFdElZV3BVcDd6Zl9FdUhXUnpNUW5YWXlvM2g5MlJSS2hJZzNnWWdaaUY4M25aNC1XSkRIbjdmbEZQOFVWdFlaZUF3MzV4QQ?oc=5
- https://news.google.com/rss/articles/CBMiuwJBVV95cUxPZ292dWJ4c1JyNWJFQ3BOUG00eE1NOWNTSkNOU0J3OWFLZlZqQXVCeE9qek9lTTBGdU42UUNMY0FGUDVlOFFqMFhkcnVLMVBWa05KQXJ5cjBVWXVRRVVKLWNKcWlySE02ZFZaWHVMU3Q0QW1OazdjcldxSmlmMWkwNVY3SUhRU1V6aUgwMElDMHRjSGVWbzVmWS1kT1VySmtzeUYxRUlKZG40Yklpc0psalN1MTNINnk1Y2hPUGUwSThTSlhSeXliMTB3bm0wZDBXSHJZcDVwNUx1ZFRRalJRTldrN0REZkpJVGVXT0Q4Rnk0Q3FSV0NaN0RlSXhQdVhVS19TQnNEeDNwRUNnTHBCeWN0N3d6M3A3Qjh4NTh4SV9rMkNTSUpKQk9tLWFIa1BwMGQ4YkNpQ1BMUVU?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxQOEVVLVYweGEyZnBGWElzb1YwaElRNndpZ0NHRGx1QmNiMVdsSzFPYk1BclNSWUg4WFRGQXlsTkNzMHY1eWhVTlV0SC1NZHlsNVAyMGktRkw5MnBhOHpQVnFLLWR6Q3AzQ2JBMlFCOEJVR1l0TUpoRDZpcmZ0aDdKVUlwU015NHBEMlVmemh0SGt5WmViMEVkWmoxbXJkNEQxN2dtcnA0VlBPRHpVSmVCcS1lVjZVN05RcEdKWFNtcTZzTGM?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxQV1FWcTNHWTNfd3pnSmZ2MUJYWXpaWm0taXI3TFE5bmRyV041UjVRSUFiYmF6SENLYVV3ZWZiM2pZZ3FISlNUeS13MDhSaWdOVW10M09XVWVJVDllSkFaby1YYm9hZElMM1huZlU1OEJINmc4Z29QZC12Ri1hUThsWmc3TmdueXNoN3dYWlc0TTRHcDMyX1FjVVA1a21jelVzVmJmZU9LTTZwUQ?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPam9lcUIybDhzMEFMZkFsU2xZWkdJR19fOGplTllISm95UXQ5SmVkLXlUMnZobzhDMmVWWlAtYjFsVzFfQjhPWGZwSkl2bnFvLTZnajEtYnlyQkFYcFUyYVRDMVoxb25UYmJNdWZnaXlJQzhMdHFZYUl3Z0RxbGxLUWNoeU5fQW85REdLWmMtRmNONnV4MXBWLU8zWVlLV3lF?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOeEZrZDRQWmV6U3lXSE1LbThlYVdhbVNaTlNacjhwczdJTE9xSF9NTVJIRWNmUXQwZXloLTBSN3lkcVBZQ011WmQ5bXZVU2hWeVBWYVJFeXFFOU0zYmlsUlo2NGNUWHljSE1OYWtpRDlzNlRpaGMxS1FWX1hOcHBuNEtEeWVod1dnUUNza1JVeFl6STE5alJ4enJjS0V4Q0pnLVE?oc=5
- https://news.google.com/rss/articles/CBMi4gFBVV95cUxNQVVWcmRVUEtYa2pDNVpjOUVqTVVNV3lKcGRXbWZ4SjZ2VmZrYS1Za09RdTAzbVdyMVMzRkNnbXVIMUVUanEydXhpTmtUcnFrVzBaVlgzOXdwdWlWWUNkWHNGSHB6ZDJaeURYOUR4dkhBZTFUM1dUUzNiQW9GZ25VbkVQTGtVa0sxUWNoS1RZTlB2and2c0dtb0VzRThacUpBSkZuRGtWRmVzTmI0YTN1bVFkRlFQVjB1NEZxX0xXQldEVnV5ZmVGcF85NjNYVDQzRDB6RlRhYk9EM1VPVGhEd1hn?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxONzFpZ2xoSzlkazFtUkNhX09sQ1k0T2FwT19GenVaR3dwYi03M0s4Vk9GOG5ZTHpsWkxMMnd2U2Z5TXJtUDMwYmxjWnVUSGJ1YWdLcUZ6bXlxTHdiNFlKRjBHM1htejMtN1c2RVhtRDVlZXBlcFAyM3FIREY4MW1BdWVxQ1EyUFZZUjZiUzF6bjVaaUQ0U0R2c3l5WkwtQQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
