# MCO Intelligence Report

- ticker: **MCO**
- Report as_of: **2026-11-03**
- Market data as_of: **2026-11-03**
- Quant sources: https://finance.yahoo.com/quote/MCO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MCO/key-statistics/
- AI analysis snapshot as_of: **2026-11-03**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-04T05:01:09.983590+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 11, 'rule': 3, 'ai': 3, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261103T051441Z-8b1c85d8/MCO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 11 unique headlines; 4 named publishers; 0 exact duplicates; 11 HTTPS source links; largest publisher share 72.73%; oldest publication 2026-10-29

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 503.6900 |
| Return 1D (%) | -0.4605 |
| Return 1W (%) | 6.2637 |
| Return 1M (%) | 14.1223 |
| Return YTD (%) | -0.7434 |
| Return 1Y (%) | 4.5496 |
| Annualized volatility (%) | 27.9986 |
| Beta vs SPY | 0.4652 |
| Max drawdown (%) | -23.6059 |
| Sharpe (rf=0) | 0.2997 |
| Downside deviation (rf=0, %) | 20.0104 |
| Sortino (rf=0) | 0.4193 |
| Historical VaR 95% (1D, %) | 2.4495 |
| Historical ES 95% (1D, %) | 3.8509 |
| Correlation vs SPY | 0.2126 |
| Tracking error vs SPY (%) | 28.2016 |
| P/E (trailing) | 30.88 |
| P/B | 26.58 |
| EV/EBITDA | 22.97 |
| Revenue growth (%) | 0.80 |
| Forward P/E (estimate) | 27.02 |
| Gross margin (%) | 74.63 |
| Operating margin (%) | 46.27 |
| Return on equity (%) | 76.74 |
| Free cash flow yield (%) | 2.92 |
| MA50 | 477.2290 |
| Close vs MA50 (%) | 5.5447 |
| MA200 | 465.1786 |
| Close vs MA200 (%) | 8.2788 |
| RSI (14, Wilder) | 64.0939 |
| MACD (12,26) | 7.4960 |
| MACD signal (9) | 4.2995 |
| MACD histogram | 3.1964 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MCO': 274, 'SPY': 274}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 503.6900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.4605 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 6.2637 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 14.1223 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -0.7434 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 4.5496 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 27.9986 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 20.0104 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4193 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.4495 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.8509 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2126 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 28.2016 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.4652 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -23.6059 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2997 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 27.0187 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.6330 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 46.2680 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 76.7410 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.9185 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 30.8823 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 64.0939 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 3.1964 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 5.5447 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 8.2788 -> Clearly above the moving-average trend level.

## TAILWINDS

### Moody's Corporation $MCO Holdings Boosted by International Assets Investment Management LLC
- Summary: Moody’s partnership with International Assets Investment Management LLC enhances its holdings, potentially strengthening market position.
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi5AFBVV95cUxQbEdINGZlSlEyT2Q3Mjg3R04wRWx3YkVSSF9HcUpTVXpBdDRvQXdHTkc0YS1TNXJKSjd6by1RZUdUOEdjWVRMRnB2alp0X2lRS1lnelMyU1hSNjZzQ2c0NXZkYmtyTzJ3YmZjaFVTSTk5RGthV0M0ekhvZ2hVQllYbnFwN0ZRTmJzZ21JeWtadWYwUWt6QlVzcjJEcFAxTWd6VlNaLXNkQ0tPUS1RYWo0bFpocGVLVUlVaXRjMmFsZ1EtandoYzBEWm8zTVU4MzhIakw0UWV3THVjSkVHaS1MeWs5R2w?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Moody's Corporation $MCO Shares Sold by ProShare Advisors LLC
- Summary: Moody's Corporation $MCO Shares Sold by ProShare Advisors LLC
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxQeC1iZGxnLUw5Rko1U3FoZ2FvVTE3RjNiU3YyWkx3OEdWVmd6RTVxcXR5SzBpd2xuWE42TnpwZ0diamZidTFibVdad0xmejcyTVM3RDRFbFQ3Q0JEejlQXzJDb1hmcnlTdHBSZ2pfenotdU1VSFZ4M2xudDBCVElRTUJldEl4NXI3LWpLZHRuVElzUEZhSDRaMW9RUUVzWUY5dXhnampVQ3BRSWl6ZHZQcnFPWDZxd2QtRHdvUg?oc=5>

### Moody's Corporation $MCO Shares Purchased by Cidel Asset Management Inc.
- Summary: Moody's Corporation $MCO Shares Purchased by Cidel Asset Management Inc.
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxPYV80TGdncl9yaDQ1eHN3aFZjOTJ5cTd2NlYzYmp5cDBfeTFOazVRQ1VTZHBORmVza2xsQko2bjNreTVFUjNORG9WRXRXbmFUdHlwdXZCTl9VdWNTbmJZM2dVMllsY05SYXNSSWpwVE5PWlJlU1RmS3FwVGhjallBbm53STRpRDhTSjl2MmpMZklTQXI3TEhqcXhSWkVmQjNmV1NPWWtuUHJ5V2JlMXlDQXpVRTd0Q0NIZ2JId1Mwc29NWER1RmlVaEln?oc=5>

### Moody's Corporation $MCO Stock: Windmill Hill Asset Management Ltd Cuts Stake
- Summary: Moody's Corporation $MCO Stock: Windmill Hill Asset Management Ltd Cuts Stake
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxPNnRvMUxuOUlRaGZmcklDTUNfWjhCeWhSdUZpTkIyaWNLWmY1WHVrU3FrUDZjTUJHZjk0SEgtY0V4dWVGNlZiRnZwMkZ1OHJJQzM5NG01Qzg5d0UtTVFOWjE2UGh3SW5JUDRiU2pRT1dWNnhtRzYzZVFoN08yeUhoYUFmaV9Mc2piVTRMZlZjamdaa0tyVDBzcGtsMnZUT20wY0JqQkVlcnBGWjZxRmFtWVNGNExtLWtVWG9HUGsybUdUNjRfb1dkaW1UdDIzUU5n?oc=5>

### Moody's (NYSE:MCO) Stock: Insider Michael West Sells 185 Shares
- Summary: Insider Michael West sold 185 shares of Moody's stock.
- Date: 2026-11-03 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxNa2NSYW1VUFE3YUFRQkU1Q19sVTNIaHVZWEhuMTlqTU9IV3hEMjJvRVhXb1R2SC13X3NJVWV3X3B0TEN6NjJtN1lFSzRsTHpUeFJjQWpVY0xta1BUNEVSRFJlTzMtN1NNUDJUVXYwQnBzblRpV0hPQ0xORjFxMG1ISzF2bEJHQ2Nha1FqM2ROUUlhc0poNmh1QjlINHlKcW9ydExQUERFQlJpdFZXQU5TdWpLa3p6SmVKeHpaOTFn?oc=5>

### Insider Selling: Moody's (NYSE:MCO) Insider Sells $99,299.85 in Stock
- Summary: An insider sold shares worth $99,299.85 of Moody's stock.
- Date: 2026-11-03 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxQSlpDVG4xU3lvUXh3dnVPTUQyd0VHcGVYeUg5VEVickNfWFhMSFB2N0JLS3Rrc1VmeWh5eDY0X1RCcG94MmtTMXAybkZsUWh6RU45c3g4WVRyVENOV2YxajE5YXJOMnhlXzZSeHNXbklqcFNzSmlxUThGWE1OQjJQQVFmQWtaZlVBa0h1M1VWLTNsWmlJUkZFMmdlUXJ6cTVaN2VtNHF6bXE4cHp5WENCNE41TGRJVkQ2bVI5ZmZ1Qk0wUQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MCO** | **30.88** | **26.58** | **22.97** | **0.80** | **86,848,282,624.00 USD** | **4.55** |
| SPGI | 28.38 | 6.85 | 18.05 | 6.80 | 135,102,095,360.00 USD | -0.01 |
| MSCI | 33.69 | -15.21 | 25.95 | 12.40 | 46,512,009,216.00 USD | 11.68 |
| FDS | 23.59 | 5.86 | 14.44 | 6.30 | 11,730,406,400.00 USD | 27.96 |

Peers fetched as_of: 2026-11-03; MCO reuses existing data (market data as_of: 2026-11-03); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-02-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-03

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 1,142,100,000.00 USD; period 2019-01-01/2019-03-31; fiscal year/reporting period 2019/Q1
- Net income (latest available single quarter): 734,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1059556/000162828026066731/mco-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi5AFBVV95cUxQbEdINGZlSlEyT2Q3Mjg3R04wRWx3YkVSSF9HcUpTVXpBdDRvQXdHTkc0YS1TNXJKSjd6by1RZUdUOEdjWVRMRnB2alp0X2lRS1lnelMyU1hSNjZzQ2c0NXZkYmtyTzJ3YmZjaFVTSTk5RGthV0M0ekhvZ2hVQllYbnFwN0ZRTmJzZ21JeWtadWYwUWt6QlVzcjJEcFAxTWd6VlNaLXNkQ0tPUS1RYWo0bFpocGVLVUlVaXRjMmFsZ1EtandoYzBEWm8zTVU4MzhIakw0UWV3THVjSkVHaS1MeWs5R2w?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxQeC1iZGxnLUw5Rko1U3FoZ2FvVTE3RjNiU3YyWkx3OEdWVmd6RTVxcXR5SzBpd2xuWE42TnpwZ0diamZidTFibVdad0xmejcyTVM3RDRFbFQ3Q0JEejlQXzJDb1hmcnlTdHBSZ2pfenotdU1VSFZ4M2xudDBCVElRTUJldEl4NXI3LWpLZHRuVElzUEZhSDRaMW9RUUVzWUY5dXhnampVQ3BRSWl6ZHZQcnFPWDZxd2QtRHdvUg?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxPYV80TGdncl9yaDQ1eHN3aFZjOTJ5cTd2NlYzYmp5cDBfeTFOazVRQ1VTZHBORmVza2xsQko2bjNreTVFUjNORG9WRXRXbmFUdHlwdXZCTl9VdWNTbmJZM2dVMllsY05SYXNSSWpwVE5PWlJlU1RmS3FwVGhjallBbm53STRpRDhTSjl2MmpMZklTQXI3TEhqcXhSWkVmQjNmV1NPWWtuUHJ5V2JlMXlDQXpVRTd0Q0NIZ2JId1Mwc29NWER1RmlVaEln?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxPNnRvMUxuOUlRaGZmcklDTUNfWjhCeWhSdUZpTkIyaWNLWmY1WHVrU3FrUDZjTUJHZjk0SEgtY0V4dWVGNlZiRnZwMkZ1OHJJQzM5NG01Qzg5d0UtTVFOWjE2UGh3SW5JUDRiU2pRT1dWNnhtRzYzZVFoN08yeUhoYUFmaV9Mc2piVTRMZlZjamdaa0tyVDBzcGtsMnZUT20wY0JqQkVlcnBGWjZxRmFtWVNGNExtLWtVWG9HUGsybUdUNjRfb1dkaW1UdDIzUU5n?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxNa2NSYW1VUFE3YUFRQkU1Q19sVTNIaHVZWEhuMTlqTU9IV3hEMjJvRVhXb1R2SC13X3NJVWV3X3B0TEN6NjJtN1lFSzRsTHpUeFJjQWpVY0xta1BUNEVSRFJlTzMtN1NNUDJUVXYwQnBzblRpV0hPQ0xORjFxMG1ISzF2bEJHQ2Nha1FqM2ROUUlhc0poNmh1QjlINHlKcW9ydExQUERFQlJpdFZXQU5TdWpLa3p6SmVKeHpaOTFn?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxQSlpDVG4xU3lvUXh3dnVPTUQyd0VHcGVYeUg5VEVickNfWFhMSFB2N0JLS3Rrc1VmeWh5eDY0X1RCcG94MmtTMXAybkZsUWh6RU45c3g4WVRyVENOV2YxajE5YXJOMnhlXzZSeHNXbklqcFNzSmlxUThGWE1OQjJQQVFmQWtaZlVBa0h1M1VWLTNsWmlJUkZFMmdlUXJ6cTVaN2VtNHF6bXE4cHp5WENCNE41TGRJVkQ2bVI5ZmZ1Qk0wUQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
