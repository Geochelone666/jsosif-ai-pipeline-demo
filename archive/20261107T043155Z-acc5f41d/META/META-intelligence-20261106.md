# META Intelligence Report

- ticker: **META**
- Report as_of: **2026-11-06**
- Market data as_of: **2026-11-06**
- Quant sources: https://finance.yahoo.com/quote/META/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/META/key-statistics/
- AI analysis snapshot as_of: **2026-11-06**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-07T04:50:59.962460+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 2, 'ai': 15, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **10** exact headline/source/date matches; prior report **20261106T045829Z-1db1e5a7/META** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 13 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 29.17%; oldest publication 2026-11-01

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 610.1500 |
| Return 1D (%) | 0.8379 |
| Return 1W (%) | -0.7870 |
| Return 1M (%) | -17.4223 |
| Return YTD (%) | -7.3277 |
| Return 1Y (%) | -1.0858 |
| Annualized volatility (%) | 41.3261 |
| Beta vs SPY | 1.3542 |
| Max drawdown (%) | -28.7332 |
| Sharpe (rf=0) | 0.1779 |
| Downside deviation (rf=0, %) | 27.5069 |
| Sortino (rf=0) | 0.2672 |
| Historical VaR 95% (1D, %) | 3.7761 |
| Historical ES 95% (1D, %) | 5.6434 |
| Correlation vs SPY | 0.4440 |
| Tracking error vs SPY (%) | 37.3384 |
| P/E (trailing) | 20.82 |
| P/B | 5.73 |
| EV/EBITDA | 13.70 |
| Revenue growth (%) | 26.10 |
| Forward P/E (estimate) | 17.14 |
| Gross margin (%) | 81.03 |
| Operating margin (%) | 35.41 |
| Return on equity (%) | 32.26 |
| Free cash flow yield (%) | 1.08 |
| MA50 | 674.7689 |
| Close vs MA50 (%) | -9.5764 |
| MA200 | 631.1514 |
| Close vs MA200 (%) | -3.3275 |
| RSI (14, Wilder) | 36.7401 |
| MACD (12,26) | -23.6586 |
| MACD signal (9) | -17.7685 |
| MACD histogram | -5.8900 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'META': 277, 'SPY': 277}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 610.1500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.8379 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.7870 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -17.4223 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -7.3277 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -1.0858 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 41.3261 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 27.5069 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.2672 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.7761 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.6434 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4440 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.3384 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.3542 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.7332 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1779 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.1449 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 81.0340 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 35.4140 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 32.2640 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.0800 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 20.8171 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 36.7401 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -5.8900 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -9.5764 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -3.3275 -> Slightly below the moving-average trend level.

## TAILWINDS

### Investors Are Beginning to Say That Meta Is The Best Buy And Hold Stock Through 2030
- Summary: Highlights investor sentiment favoring Meta as a long-term hold.
- Date: 2026-11-03 | Impact: low | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQekVac0tXM3pEX253R1RuMlJoeXlHUEc5T0dIeHEwVkJQOHZ0SWI1XzlNWk5EZURWbl9xOEQ2Um5mTE1KeDhuMkIzTG83aGhPQ2R4WGFSMmctT0laR2VIOVRUUXg0NllPMU9TMlRpRWx5TUJPcVNLc1U5SWp2WnJEdHlqZHdZU0FLYk9Lc2h5OFMyMjEyUWdrSS1BMWpKa1U?oc=5>

### What Is Going On With Meta Platforms Stock on Monday?
- Summary: Meta’s stock movement on Monday is discussed, highlighting potential market dynamics.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQWW1uaWJkbk9BMm5MZnh4RG5IVGFsTV81MFJyRFhKR3k1N3c0OVRWRlkzSFJUY1FheGpmVkplZ0xCN1JMMVFhSDhqdHIxN0Q3bEw3ZnBSSWxpV3BJMzN2UDVqMGRfRDRaSFJXWXZheU8zeXVRX1VmcmI2WG9HdVpuRDcyVmVFMEJNZzAzVUlCZGRRcUNFUU1BUTRwSzkxaEk?oc=5>

### ETFs Are Buying Meta Platforms (META) on Monday
- Summary: ETF purchases of Meta shares on Monday indicate institutional interest.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxObXlMMUZPdTgwelhHYnVDZXBuMHlFNGNWZHp5ZTNpTE5iVkxTODFRcWoyNUtrOHRlcC01QmxOZ0JOS0RzS1J1c0RwdkpBcFoxMW8xRVNTVllXbGVjUjd6eFNKdThtVnhHQmV0alRrM0REQUVBbW1lZDlITEJhWlZndjJqTi1uRFRBamxPaG51Sktld3ZRVkRtYVlqZEs?oc=5>

## HEADWINDS

### Meta Shares Are Down Since Earnings. Is the Stock a Buy?
- Summary: Meta Shares Are Down Since Earnings. Is the Stock a Buy?
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNTEpWRWszazhBX3BaNmN2eWE0TzZEdVFtZmdlamRQWnlLRUxOb3FZSXRHTlVKWnJYRlRWaGNOOGpobHZ5bjZrVTdZZVFRTXlRVmpiMzktUU93RzJ1LVcxV0lsdWg4UUhRVVgtVDhyMXBOeGZoTm91aGZRUktZWWcwNVNIT0gxQ3hraVMxSk92UUZyMEVWMm1r?oc=5>

### As Meta Stock Suffers Its Worst Month in Years, S&P Delivers a Brutal $39 Billion Cash Flow Warning
- Summary: Meta stock worst month; S&P warns of cash flow issues.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNU3VvajNzS2xKY0VxU2ZhdXNXX3RMelRqeGxPWDZOQmhTYWFqMnRtZ1JFd2dxQkozT210dk00b3VVMU9NcklMM0xIUjRKOG40ZzU2VFlnd2dfTWhVc2xLQ3RiTWJJUW5vR0hTRndyczZDblhIamx2ekhoZzU1cDlyRVhoSUVfOG9oMkdtWUhPSmJCci1ILWs3Q3lLMA?oc=5>

### Apple, Meta reject OKX–ICE tokenized stock plans, leaving crypto firms as the ones to watch
- Summary: Meta and Apple declined OKX‑ICE tokenized stock plans, limiting crypto exposure.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxPbFdQRy1WbjNxQk90c1ZBTlpxY3o5QUhKQXF3TndFY0d5WTVYUkFEczhsdktBenRkXzdudFZ5dTUyNk5nbUlWbklnTnFidmNyRUo1ZVBTTmhoVU5HOUZTQVFKdHVHWUVRcGJuMVZleWJtZkdndlZ5VmdDTEw3b0oySDNJVlh3ZlBXdHN2dXNyNDI3QW1UNnpHZWFOZTdnSFpMMV9QeWlBcnFPQ3NZaU1SMWtYMEpZWXBwOExmWUtvaWtmVzRQSWN5Wl9BYnY?oc=5>

## CATALYSTS

### Meta Platforms, Inc. $META Stock: State of Wyoming Reduces Stake
- Summary: Meta Platforms, Inc. $META Stock: State of Wyoming Reduces Stake
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxNTkZhbHQtX0Njc2F6elpyVVRSWUdkOWR4bElFMm0xOFBqeTZBSERzUzdmVTBaSUJpWjdlT3V4X3ZZUktVRnE4MU9wbVhpNTBpVDE2ZUpWS3Z2YXJtZHF2Q2FXTFJwdUZmV1RtTEdEZWRXVXVYb0dkZkFrcFlDX3BZczdqcTNDR3ZvaXNGOUt2b1RjcXBiZ2hwRExHRHFxM0pzdWN3Uy1KaktlTWduUHFGVXFnaV8tYjR3cXprXzBR?oc=5>

### Here's Where I Think Meta Stock Will Be in 2030
- Summary: Long‑term price projection for Meta shares.
- Date: 2026-11-01 | Impact: low | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPclByLUdFWGlDVHB2TmloYlpXdUdJRlJwc2lhQzl5YmR5Q3VraFJGQU4wVzhGN1hKbFhhN1ZWTGhCTnN4UGZfcU5XbUtmd21uaHFOdk5FdDBhWE5MamFjU3VOZlROQVZZMlY0VGtLamRmbHBlZ2FQaWY1MXVtRTNJalpjQjNBRmJpZzl4REh3c0w3cHp1?oc=5>

### Meta Stock Forecast: AI Funding Push Puts $648.82 in Focus
- Summary: Forecast emphasizes AI funding push, projecting a $648.82 target price for Meta shares.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxQMHR2WWZZanFiZEZVa2RZZ2VSZXFrNE9RSGk2WXZ2S21aQnNyRnJwanh5ejU2ajFOR3FHQXRuVGlVdi1RWThmbFdGdGJVMVBkcHhEaDhtOTJvUzE4SDRqek5KYURBTFRodFJXT1dtZHJmRFhfekFRcmlsYTdoRF9NNUdGVTFOM3JDV0VhREFQNVhSUjVMYkhZX3YxbURkb283cldUYW4xb0g2aVFjX2w3Y3c3OFEzUDMtQ1Y4?oc=5>

### What Are Wall Street Analysts' Target Price for Meta Platforms Stock?
- Summary: Analysts provide target price estimates for Meta, reflecting market expectations.
- Date: 2026-11-02 | Impact: low | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPTlJYeVhYSENXbTJPTXRLZ0xFdkp3S1dKaGFNYUh5alQyd3BUc3dXb005Szh1R1VjQWg4bXVKY2diMmRWT3l2cXE3cmY5aU9Ib19JTllMMFp0ODFfS04zbGJDYks0VjNOaUNTOGY4OFdvb1FqR0FwRUM3S3hHNXJYQldya0RoRGlnMFJzMlRKeXM3RFZ4d3JZZ2Mwei1sQUU?oc=5>

### ETFs Are Net Sellers of Meta Platforms (META) on Thursday
- Summary: ETFs sold Meta shares, indicating negative market sentiment.
- Date: 2026-11-02 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOZ2ItaERBamlLbk94ZjhjQy1BcnBCcGd6UTEyaU9XQXVEREdtNE8tYnZhYWxMc1k0a3pEMnI5VE0yR1dFeHByVGNmSGNlcXNQUVFRSTFTa05HeC1LZHdTdHlIei1oVFpBc1JzMGZWVF9HSXp0M243OEFqREpBMlhLVzh2YlRqcVp1WHJJU3BkMms4ZG9QZUN4dGtpNDQ?oc=5>

### Stock-Split Watch: Is Meta Platforms Next?
- Summary: Speculation about a potential Meta stock split.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNMU1LTnl2SWZBc1ZNZGtuWEdFNE42SFVGR2RycEs3Qm1GWXIzRDBBNWw1X3plUGtVSzY3c25XRVJKOS1mRE5HTGgwNWJKQWxnQlNPNTMzR3VFMF9Gd0JlNkp3RGduMTFfMGxPQWRnTXZXN0RHdFAtd3d6VUxpdHdaWmluc2hwOGJrcHln?oc=5>

### What Is Going on With Meta Platforms Stock on Tuesday? - Meta Platforms (NASDAQ:META)
- Summary: Discussion of Meta stock movement on a specific day.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxOSHZNbkpUWEwzeC1QOW9idTNpVjI2U29mTGFpYTBLYjhJMGZZNEhVVi1KOWVDcVRiUTNXZU4yLXBqaXpaUnVuX19vdDE2SFZvZ1B6Mk82eExLR28yUUVzYzRVdFB4MThVc3hfN0RHRU51d1RLMThnOVF6XzJlUjl2ZGdVN1JRMEhPd0h6dVY3WFhBczVCbGRodHNrYV8zWTRYVE5lN3RxZXVXdw?oc=5>

### Meta Platforms, Inc. (META) Stock Price, News, Quote & History
- Summary: General information on Meta stock price and history.
- Date: 2026-11-06 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiUkFVX3lxTE9NdF9xWW1RaDk2MmNFdk5acnJHSVhGM0dqcF90M081cUplRkpyVjZmakJsdS11TFhOcnVVRnM0T1RXcEo5ZzBITzA1N1BsaWVacVE?oc=5>

### Meta (META) Stock May Be A Bargain After Huge AI Fundraising
- Summary: Meta stock seen as attractive after large AI fundraising.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQYWo4WHVSb0lrclRUVUZ6N1VJb3dERjlDQVFRSnFDMVNJRkU5NlFkQVRDTEdNRkMtZFB3dEFuMkdEUHdZLVM3a1IxdkNJbGY4ZGUwcWxwTmZEWkpzTzQ1Z19wX204ZUdzTjZmNjhlRDRXeXJYZFZZT0hCdXRtTm1aeGZuVDdEcVFtWHZ1bUlQOUVlOUFCOHRB?oc=5>

### Meta Platforms: Record Ad Growth, But There's A Costly Catch (NASDAQ:META)
- Summary: Meta reports record ad growth with associated costs.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOV0NjcEN4WWM2LXBockRnR1pQSEdsVnVOWTJQOVZ4eUFoWFlmNzVZb3dXRFlJODVQWjRfak83RlYzeFg2Zk83MzZlbHZoYlhSdS1NR1BST2JQUkl4TDZYaHVqQlRYOFlfYVRKbGNmZzVUMEZGY3FreC1DeHEyc05tY3NreV9FalV6YVAtMHhlaWI4X0JyaHhSNGx1dm10Tjg?oc=5>

### Meta Platforms, Inc. (META) is Attracting Investor Attention: Here is What You Should Know
- Summary: Meta draws investor interest, signaling potential positive market perception.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxQMnBnOXljSUJNR3FtalQwSGlBMTd6YXg4RWNMajBudUxNa1hJWlJ5WEFIWTVKVDhLS1ROaGJSUUJSQy1EaGFiLXNsdnR5NU9iTHZrQTFUS0Yydl9id2RrQlFiUjhtVE5XUXB0eXJMbXZ5emdGVUkzdnFNN29Ed3l0VW81TWxIUV9FektV?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **META** | **20.82** | **5.73** | **13.70** | **26.10** | **1,560,051,712,000.00 USD** | **-1.09** |
| GOOGL | 14.87 | 5.31 | 18.35 | 24.70 | 3,501,085,163,520.00 USD | 0.27 |
| SNAP | N/A | 3.72 | -79.15 | 18.90 | 8,518,854,144.00 USD | -38.08 |
| PINS | 79.00 | 3.50 | 35.80 | 11.90 | 10,873,708,544.00 USD | -27.85 |

Peers fetched as_of: 2026-11-06; META reuses existing data (market data as_of: 2026-11-06); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-06

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMinwFBVV95cUxQekVac0tXM3pEX253R1RuMlJoeXlHUEc5T0dIeHEwVkJQOHZ0SWI1XzlNWk5EZURWbl9xOEQ2Um5mTE1KeDhuMkIzTG83aGhPQ2R4WGFSMmctT0laR2VIOVRUUXg0NllPMU9TMlRpRWx5TUJPcVNLc1U5SWp2WnJEdHlqZHdZU0FLYk9Lc2h5OFMyMjEyUWdrSS1BMWpKa1U?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQWW1uaWJkbk9BMm5MZnh4RG5IVGFsTV81MFJyRFhKR3k1N3c0OVRWRlkzSFJUY1FheGpmVkplZ0xCN1JMMVFhSDhqdHIxN0Q3bEw3ZnBSSWxpV3BJMzN2UDVqMGRfRDRaSFJXWXZheU8zeXVRX1VmcmI2WG9HdVpuRDcyVmVFMEJNZzAzVUlCZGRRcUNFUU1BUTRwSzkxaEk?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxObXlMMUZPdTgwelhHYnVDZXBuMHlFNGNWZHp5ZTNpTE5iVkxTODFRcWoyNUtrOHRlcC01QmxOZ0JOS0RzS1J1c0RwdkpBcFoxMW8xRVNTVllXbGVjUjd6eFNKdThtVnhHQmV0alRrM0REQUVBbW1lZDlITEJhWlZndjJqTi1uRFRBamxPaG51Sktld3ZRVkRtYVlqZEs?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNTEpWRWszazhBX3BaNmN2eWE0TzZEdVFtZmdlamRQWnlLRUxOb3FZSXRHTlVKWnJYRlRWaGNOOGpobHZ5bjZrVTdZZVFRTXlRVmpiMzktUU93RzJ1LVcxV0lsdWg4UUhRVVgtVDhyMXBOeGZoTm91aGZRUktZWWcwNVNIT0gxQ3hraVMxSk92UUZyMEVWMm1r?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNU3VvajNzS2xKY0VxU2ZhdXNXX3RMelRqeGxPWDZOQmhTYWFqMnRtZ1JFd2dxQkozT210dk00b3VVMU9NcklMM0xIUjRKOG40ZzU2VFlnd2dfTWhVc2xLQ3RiTWJJUW5vR0hTRndyczZDblhIamx2ekhoZzU1cDlyRVhoSUVfOG9oMkdtWUhPSmJCci1ILWs3Q3lLMA?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxPbFdQRy1WbjNxQk90c1ZBTlpxY3o5QUhKQXF3TndFY0d5WTVYUkFEczhsdktBenRkXzdudFZ5dTUyNk5nbUlWbklnTnFidmNyRUo1ZVBTTmhoVU5HOUZTQVFKdHVHWUVRcGJuMVZleWJtZkdndlZ5VmdDTEw3b0oySDNJVlh3ZlBXdHN2dXNyNDI3QW1UNnpHZWFOZTdnSFpMMV9QeWlBcnFPQ3NZaU1SMWtYMEpZWXBwOExmWUtvaWtmVzRQSWN5Wl9BYnY?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxNTkZhbHQtX0Njc2F6elpyVVRSWUdkOWR4bElFMm0xOFBqeTZBSERzUzdmVTBaSUJpWjdlT3V4X3ZZUktVRnE4MU9wbVhpNTBpVDE2ZUpWS3Z2YXJtZHF2Q2FXTFJwdUZmV1RtTEdEZWRXVXVYb0dkZkFrcFlDX3BZczdqcTNDR3ZvaXNGOUt2b1RjcXBiZ2hwRExHRHFxM0pzdWN3Uy1KaktlTWduUHFGVXFnaV8tYjR3cXprXzBR?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPclByLUdFWGlDVHB2TmloYlpXdUdJRlJwc2lhQzl5YmR5Q3VraFJGQU4wVzhGN1hKbFhhN1ZWTGhCTnN4UGZfcU5XbUtmd21uaHFOdk5FdDBhWE5MamFjU3VOZlROQVZZMlY0VGtLamRmbHBlZ2FQaWY1MXVtRTNJalpjQjNBRmJpZzl4REh3c0w3cHp1?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxQMHR2WWZZanFiZEZVa2RZZ2VSZXFrNE9RSGk2WXZ2S21aQnNyRnJwanh5ejU2ajFOR3FHQXRuVGlVdi1RWThmbFdGdGJVMVBkcHhEaDhtOTJvUzE4SDRqek5KYURBTFRodFJXT1dtZHJmRFhfekFRcmlsYTdoRF9NNUdGVTFOM3JDV0VhREFQNVhSUjVMYkhZX3YxbURkb283cldUYW4xb0g2aVFjX2w3Y3c3OFEzUDMtQ1Y4?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPTlJYeVhYSENXbTJPTXRLZ0xFdkp3S1dKaGFNYUh5alQyd3BUc3dXb005Szh1R1VjQWg4bXVKY2diMmRWT3l2cXE3cmY5aU9Ib19JTllMMFp0ODFfS04zbGJDYks0VjNOaUNTOGY4OFdvb1FqR0FwRUM3S3hHNXJYQldya0RoRGlnMFJzMlRKeXM3RFZ4d3JZZ2Mwei1sQUU?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOZ2ItaERBamlLbk94ZjhjQy1BcnBCcGd6UTEyaU9XQXVEREdtNE8tYnZhYWxMc1k0a3pEMnI5VE0yR1dFeHByVGNmSGNlcXNQUVFRSTFTa05HeC1LZHdTdHlIei1oVFpBc1JzMGZWVF9HSXp0M243OEFqREpBMlhLVzh2YlRqcVp1WHJJU3BkMms4ZG9QZUN4dGtpNDQ?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNMU1LTnl2SWZBc1ZNZGtuWEdFNE42SFVGR2RycEs3Qm1GWXIzRDBBNWw1X3plUGtVSzY3c25XRVJKOS1mRE5HTGgwNWJKQWxnQlNPNTMzR3VFMF9Gd0JlNkp3RGduMTFfMGxPQWRnTXZXN0RHdFAtd3d6VUxpdHdaWmluc2hwOGJrcHln?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxPYUdsLTg3ZFZMMWpuNE82em9WRHNKR2hoQWdMVXVYY0xDN2ttX3N6M0hGREtkM1NiSUt3dGozVXlnRFc0Um01azFVdVRRMEpkd211ZnRfOWFzdVBYX2VqMjAwMUJuQW9VM3pDZkx5X3QwVGllUmptTEprX19SbEVnNUQ5Z1RYQ2FkY1pBUjEzSjdYVm9rSW5UZ3RnM1IzajBvU0tGdHZmeWlwVWd5YnZiRzBOdEhvWTNzRFJqeVF4SnBHMWs?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxOSHZNbkpUWEwzeC1QOW9idTNpVjI2U29mTGFpYTBLYjhJMGZZNEhVVi1KOWVDcVRiUTNXZU4yLXBqaXpaUnVuX19vdDE2SFZvZ1B6Mk82eExLR28yUUVzYzRVdFB4MThVc3hfN0RHRU51d1RLMThnOVF6XzJlUjl2ZGdVN1JRMEhPd0h6dVY3WFhBczVCbGRodHNrYV8zWTRYVE5lN3RxZXVXdw?oc=5
- https://news.google.com/rss/articles/CBMiUkFVX3lxTE9NdF9xWW1RaDk2MmNFdk5acnJHSVhGM0dqcF90M081cUplRkpyVjZmakJsdS11TFhOcnVVRnM0T1RXcEo5ZzBITzA1N1BsaWVacVE?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQYWo4WHVSb0lrclRUVUZ6N1VJb3dERjlDQVFRSnFDMVNJRkU5NlFkQVRDTEdNRkMtZFB3dEFuMkdEUHdZLVM3a1IxdkNJbGY4ZGUwcWxwTmZEWkpzTzQ1Z19wX204ZUdzTjZmNjhlRDRXeXJYZFZZT0hCdXRtTm1aeGZuVDdEcVFtWHZ1bUlQOUVlOUFCOHRB?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOV0NjcEN4WWM2LXBockRnR1pQSEdsVnVOWTJQOVZ4eUFoWFlmNzVZb3dXRFlJODVQWjRfak83RlYzeFg2Zk83MzZlbHZoYlhSdS1NR1BST2JQUkl4TDZYaHVqQlRYOFlfYVRKbGNmZzVUMEZGY3FreC1DeHEyc05tY3NreV9FalV6YVAtMHhlaWI4X0JyaHhSNGx1dm10Tjg?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxQMnBnOXljSUJNR3FtalQwSGlBMTd6YXg4RWNMajBudUxNa1hJWlJ5WEFIWTVKVDhLS1ROaGJSUUJSQy1EaGFiLXNsdnR5NU9iTHZrQTFUS0Yydl9id2RrQlFiUjhtVE5XUXB0eXJMbXZ5emdGVUkzdnFNN29Ed3l0VW81TWxIUV9FektV?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
