# MCO Intelligence Report

- ticker: **MCO**
- Report as_of: **2026-11-05**
- Market data as_of: **2026-11-05**
- Quant sources: https://finance.yahoo.com/quote/MCO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MCO/key-statistics/
- AI analysis snapshot as_of: **2026-11-05**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-06T05:01:06.162608+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 12, 'rule': 2, 'ai': 7, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261105T045846Z-bde0a1fe/MCO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 12 unique headlines; 4 named publishers; 2 exact duplicates; 12 HTTPS source links; largest publisher share 75.0%; oldest publication 2026-10-31

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 515.3400 |
| Return 1D (%) | -2.4605 |
| Return 1W (%) | 5.4232 |
| Return 1M (%) | 14.9928 |
| Return YTD (%) | 1.5524 |
| Return 1Y (%) | 6.8556 |
| Annualized volatility (%) | 28.5280 |
| Beta vs SPY | 0.5179 |
| Max drawdown (%) | -23.6059 |
| Sharpe (rf=0) | 0.3760 |
| Downside deviation (rf=0, %) | 20.1607 |
| Sortino (rf=0) | 0.5321 |
| Historical VaR 95% (1D, %) | 2.4637 |
| Historical ES 95% (1D, %) | 3.8509 |
| Correlation vs SPY | 0.2468 |
| Tracking error vs SPY (%) | 28.4118 |
| P/E (trailing) | 32.23 |
| P/B | 27.19 |
| EV/EBITDA | 23.46 |
| Revenue growth (%) | 0.80 |
| Forward P/E (estimate) | 27.64 |
| Gross margin (%) | 74.63 |
| Operating margin (%) | 46.27 |
| Return on equity (%) | 76.74 |
| Free cash flow yield (%) | 2.85 |
| MA50 | 477.5494 |
| Close vs MA50 (%) | 7.9134 |
| MA200 | 465.2209 |
| Close vs MA200 (%) | 10.7732 |
| RSI (14, Wilder) | 63.9939 |
| MACD (12,26) | 11.1109 |
| MACD signal (9) | 6.6010 |
| MACD histogram | 4.5099 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MCO': 276, 'SPY': 276}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 515.3400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.4605 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 5.4232 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 14.9928 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 1.5524 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 6.8556 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 28.5280 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 20.1607 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.5321 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.4637 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.8509 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2468 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 28.4118 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5179 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -23.6059 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3760 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 27.6436 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.6330 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 46.2680 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 76.7410 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.8525 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 32.2289 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 63.9939 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 4.5099 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 7.9134 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 10.7732 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

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

### Moody's (NYSE:MCO) Stock: Insider Michael West Sells 185 Shares
- Summary: Insider Michael West sold 185 shares of Moody's stock.
- Date: 2026-11-03 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxNa2NSYW1VUFE3YUFRQkU1Q19sVTNIaHVZWEhuMTlqTU9IV3hEMjJvRVhXb1R2SC13X3NJVWV3X3B0TEN6NjJtN1lFSzRsTHpUeFJjQWpVY0xta1BUNEVSRFJlTzMtN1NNUDJUVXYwQnBzblRpV0hPQ0xORjFxMG1ISzF2bEJHQ2Nha1FqM2ROUUlhc0poNmh1QjlINHlKcW9ydExQUERFQlJpdFZXQU5TdWpLa3p6SmVKeHpaOTFn?oc=5>

### Insider Selling: Moody's (NYSE:MCO) Insider Sells $99,299.85 in Stock
- Summary: An insider sold shares worth $99,299.85 of Moody's stock.
- Date: 2026-11-03 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxQSlpDVG4xU3lvUXh3dnVPTUQyd0VHcGVYeUg5VEVickNfWFhMSFB2N0JLS3Rrc1VmeWh5eDY0X1RCcG94MmtTMXAybkZsUWh6RU45c3g4WVRyVENOV2YxajE5YXJOMnhlXzZSeHNXbklqcFNzSmlxUThGWE1OQjJQQVFmQWtaZlVBa0h1M1VWLTNsWmlJUkZFMmdlUXJ6cTVaN2VtNHF6bXE4cHp5WENCNE41TGRJVkQ2bVI5ZmZ1Qk0wUQ?oc=5>

### Moody's Corporation $MCO Stock Holdings Boosted by Rakuten Investment Management Inc.
- Summary: Rakuten Investment Management increased its stake in Moody's, potentially signaling confidence in the company.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2wFBVV95cUxOekdseXMxbGhJVmZReHhITDlZaTRibl9XdGtXaWRBNnduWEYtbFVsX2JsX2dSbEI5NWpLSExDRkJwdmJVQVAydFZ0OGE3eERRV0FaVnNhVEF1OUsxa3NUdzNkTUhwUFRkSWNJU2psczhaMFVqTHIzWDFkZmJCZ0J0RmZMV2dTUnhPUU1jMTVrYmJQZ3p6RjZSTE1BQmN3TXdiNW9VcHdONy1qQ2V2TC1JeGR4c2p2ZGVzUHFBSzlhN1hZY1dxZEJVUFE0SWI0QlU4dzNfckxzMWpsZ0U?oc=5>

### Moody's (NYSE:MCO) CEO Sells $103,199.85 in Stock
- Summary: Moody's CEO sold shares, indicating a personal liquidity move rather than a corporate decision.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxPa1MzQUZFRTU5OVhQRnpWZS1EUTBQVC11bTh1eHh5enpFdTVYeFdkRjM5enRMSjgyU2ZzaFdlaUJyYUxQMW5BUHdNNEliZ3JkNk5wSXJSR0lfUEpGMUJQeU85NVFIRnBZa25HbW9tRVA4WndFN2NOQllEX1gyRnZUYmpRVUZJYW5KQ3p5N1F1Qzh6WjBPTEMtQUFtOGpJUkJxNGlDYWFzV0o?oc=5>

### Associated Banc Corp Makes New $4.81 Million Investment in Moody's Corporation $MCO
- Summary: Associated Banc Corp invests $4.81 million in MCO, strengthening its equity position and signaling confidence in Moody's future prospects.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxPaGtzTjBDME1xVi14NHJOajZvdDhNNGpqY1QteGRzd3pmMnJtVS05TmlvMmNIc3l0aTNDN0dWOVF3S2lYSWZOZlpZQTdUczVYYWlpYlFEclQzRFZOd3k2dXVrakJhRE5rNVh4dVh0eWpSci01eWVNcVdLMnp6cGs0XzhaRE1uWEpiaktNSlBTeWhpLWItZDBjcVo3VXRub0N2T3hNazlfUE9NYnJ3WFlBRGk3UG5BWjdXQnBZSEpueUZDWU9VNjRiTUJGQ0tLclByOHdBRFJCVQ?oc=5>

### Moody's Corporation $MCO Holdings Boosted by International Assets Investment Management LLC
- Summary: International Assets Investment Management LLC increases its holdings in MCO, reflecting bullish outlook and potential for long-term value creation.
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi5AFBVV95cUxQbEdINGZlSlEyT2Q3Mjg3R04wRWx3YkVSSF9HcUpTVXpBdDRvQXdHTkc0YS1TNXJKSjd6by1RZUdUOEdjWVRMRnB2alp0X2lRS1lnelMyU1hSNjZzQ2c0NXZkYmtyTzJ3YmZjaFVTSTk5RGthV0M0ekhvZ2hVQllYbnFwN0ZRTmJzZ21JeWtadWYwUWt6QlVzcjJEcFAxTWd6VlNaLXNkQ0tPUS1RYWo0bFpocGVLVUlVaXRjMmFsZ1EtandoYzBEWm8zTVU4MzhIakw0UWV3THVjSkVHaS1MeWs5R2w?oc=5>

## RISKS

### Sumitomo Mitsui Trust Group Inc. Sells 13,537 Shares of Moody's Corporation $MCO
- Summary: Sumitomo Mitsui Trust Group sells 13,537 MCO shares, possibly indicating a short-term liquidity move or market sentiment shift.
- Date: 2026-11-02 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxNTnE3cFNIRm5SWVlDTU0yRmRyeVJJdGJlOGZMV3hKenVuSUc2U1Q1QmtKQjVUXzRRWkhENDkwT09HU3dhRHR1NUNjSmVvemxDRkpqNURfWEU1Q3ZlZFprYW05b2hTN2FhX0g5b3FwXzB0WTVyNGM0WXJsZEV0eldXS1h2alBnN0ZzSld2b1AxalpNeEl2YU5SLU5VdWxPODBPWkVZQjV5YlM5LTQ3QVBRV3I5WC1sZGVFMnJGYzdMQlZYeWhWaUpBSzF5RS1Rbkk3V0l3?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MCO** | **32.23** | **27.19** | **23.46** | **0.80** | **88,857,026,560.00 USD** | **6.86** |
| SPGI | 28.77 | 6.95 | 18.27 | 6.80 | 136,951,660,544.00 USD | 1.34 |
| MSCI | 35.67 | -15.59 | 26.52 | 12.40 | 47,684,653,056.00 USD | 16.33 |
| FDS | 23.48 | 6.00 | 14.75 | 6.30 | 12,008,333,312.00 USD | 32.71 |

Peers fetched as_of: 2026-11-05; MCO reuses existing data (market data as_of: 2026-11-05); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-02-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-05

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

- https://news.google.com/rss/articles/CBMivAFBVV95cUxQeC1iZGxnLUw5Rko1U3FoZ2FvVTE3RjNiU3YyWkx3OEdWVmd6RTVxcXR5SzBpd2xuWE42TnpwZ0diamZidTFibVdad0xmejcyTVM3RDRFbFQ3Q0JEejlQXzJDb1hmcnlTdHBSZ2pfenotdU1VSFZ4M2xudDBCVElRTUJldEl4NXI3LWpLZHRuVElzUEZhSDRaMW9RUUVzWUY5dXhnampVQ3BRSWl6ZHZQcnFPWDZxd2QtRHdvUg?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxPYV80TGdncl9yaDQ1eHN3aFZjOTJ5cTd2NlYzYmp5cDBfeTFOazVRQ1VTZHBORmVza2xsQko2bjNreTVFUjNORG9WRXRXbmFUdHlwdXZCTl9VdWNTbmJZM2dVMllsY05SYXNSSWpwVE5PWlJlU1RmS3FwVGhjallBbm53STRpRDhTSjl2MmpMZklTQXI3TEhqcXhSWkVmQjNmV1NPWWtuUHJ5V2JlMXlDQXpVRTd0Q0NIZ2JId1Mwc29NWER1RmlVaEln?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxNa2NSYW1VUFE3YUFRQkU1Q19sVTNIaHVZWEhuMTlqTU9IV3hEMjJvRVhXb1R2SC13X3NJVWV3X3B0TEN6NjJtN1lFSzRsTHpUeFJjQWpVY0xta1BUNEVSRFJlTzMtN1NNUDJUVXYwQnBzblRpV0hPQ0xORjFxMG1ISzF2bEJHQ2Nha1FqM2ROUUlhc0poNmh1QjlINHlKcW9ydExQUERFQlJpdFZXQU5TdWpLa3p6SmVKeHpaOTFn?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxQSlpDVG4xU3lvUXh3dnVPTUQyd0VHcGVYeUg5VEVickNfWFhMSFB2N0JLS3Rrc1VmeWh5eDY0X1RCcG94MmtTMXAybkZsUWh6RU45c3g4WVRyVENOV2YxajE5YXJOMnhlXzZSeHNXbklqcFNzSmlxUThGWE1OQjJQQVFmQWtaZlVBa0h1M1VWLTNsWmlJUkZFMmdlUXJ6cTVaN2VtNHF6bXE4cHp5WENCNE41TGRJVkQ2bVI5ZmZ1Qk0wUQ?oc=5
- https://news.google.com/rss/articles/CBMi2wFBVV95cUxOekdseXMxbGhJVmZReHhITDlZaTRibl9XdGtXaWRBNnduWEYtbFVsX2JsX2dSbEI5NWpLSExDRkJwdmJVQVAydFZ0OGE3eERRV0FaVnNhVEF1OUsxa3NUdzNkTUhwUFRkSWNJU2psczhaMFVqTHIzWDFkZmJCZ0J0RmZMV2dTUnhPUU1jMTVrYmJQZ3p6RjZSTE1BQmN3TXdiNW9VcHdONy1qQ2V2TC1JeGR4c2p2ZGVzUHFBSzlhN1hZY1dxZEJVUFE0SWI0QlU4dzNfckxzMWpsZ0U?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxPa1MzQUZFRTU5OVhQRnpWZS1EUTBQVC11bTh1eHh5enpFdTVYeFdkRjM5enRMSjgyU2ZzaFdlaUJyYUxQMW5BUHdNNEliZ3JkNk5wSXJSR0lfUEpGMUJQeU85NVFIRnBZa25HbW9tRVA4WndFN2NOQllEX1gyRnZUYmpRVUZJYW5KQ3p5N1F1Qzh6WjBPTEMtQUFtOGpJUkJxNGlDYWFzV0o?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxPaGtzTjBDME1xVi14NHJOajZvdDhNNGpqY1QteGRzd3pmMnJtVS05TmlvMmNIc3l0aTNDN0dWOVF3S2lYSWZOZlpZQTdUczVYYWlpYlFEclQzRFZOd3k2dXVrakJhRE5rNVh4dVh0eWpSci01eWVNcVdLMnp6cGs0XzhaRE1uWEpiaktNSlBTeWhpLWItZDBjcVo3VXRub0N2T3hNazlfUE9NYnJ3WFlBRGk3UG5BWjdXQnBZSEpueUZDWU9VNjRiTUJGQ0tLclByOHdBRFJCVQ?oc=5
- https://news.google.com/rss/articles/CBMi5AFBVV95cUxQbEdINGZlSlEyT2Q3Mjg3R04wRWx3YkVSSF9HcUpTVXpBdDRvQXdHTkc0YS1TNXJKSjd6by1RZUdUOEdjWVRMRnB2alp0X2lRS1lnelMyU1hSNjZzQ2c0NXZkYmtyTzJ3YmZjaFVTSTk5RGthV0M0ekhvZ2hVQllYbnFwN0ZRTmJzZ21JeWtadWYwUWt6QlVzcjJEcFAxTWd6VlNaLXNkQ0tPUS1RYWo0bFpocGVLVUlVaXRjMmFsZ1EtandoYzBEWm8zTVU4MzhIakw0UWV3THVjSkVHaS1MeWs5R2w?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxNTnE3cFNIRm5SWVlDTU0yRmRyeVJJdGJlOGZMV3hKenVuSUc2U1Q1QmtKQjVUXzRRWkhENDkwT09HU3dhRHR1NUNjSmVvemxDRkpqNURfWEU1Q3ZlZFprYW05b2hTN2FhX0g5b3FwXzB0WTVyNGM0WXJsZEV0eldXS1h2alBnN0ZzSld2b1AxalpNeEl2YU5SLU5VdWxPODBPWkVZQjV5YlM5LTQ3QVBRV3I5WC1sZGVFMnJGYzdMQlZYeWhWaUpBSzF5RS1Rbkk3V0l3?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
