# JPM Intelligence Report

- ticker: **JPM**
- Report as_of: **2026-10-25**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/JPM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/JPM/key-statistics/
- AI analysis snapshot as_of: **2026-10-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-26T01:31:18.050378+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 19, 'rule': 5, 'ai': 3, 'unknown': 0, 'irrelevant': 11})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 19 unique headlines; 7 named publishers; 1 exact duplicates; 19 HTTPS source links; largest publisher share 47.37%; oldest publication 2026-10-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 331.5800 |
| Return 1D (%) | -1.4738 |
| Return 1W (%) | -2.3961 |
| Return 1M (%) | -1.2727 |
| Return YTD (%) | 4.8868 |
| Return 1Y (%) | 14.7437 |
| Annualized volatility (%) | 22.1025 |
| Beta vs SPY | 0.7373 |
| Max drawdown (%) | -15.4717 |
| Sharpe (rf=0) | 0.7353 |
| Downside deviation (rf=0, %) | 15.8824 |
| Sortino (rf=0) | 1.0233 |
| Historical VaR 95% (1D, %) | 2.3879 |
| Historical ES 95% (1D, %) | 3.2600 |
| Correlation vs SPY | 0.4252 |
| Tracking error vs SPY (%) | 20.2832 |
| P/E (trailing) | 13.91 |
| P/B | 2.51 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 10.20 |
| Forward P/E (estimate) | 12.99 |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 42.58 |
| Return on equity (%) | 18.01 |
| Free cash flow yield (%) | N/A |
| MA50 | 344.1581 |
| Close vs MA50 (%) | -3.6548 |
| MA200 | 319.7489 |
| Close vs MA200 (%) | 3.7001 |
| RSI (14, Wilder) | 41.9724 |
| MACD (12,26) | -2.2374 |
| MACD signal (9) | -2.9915 |
| MACD histogram | 0.7541 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'JPM': 267, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 331.5800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.4738 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.3961 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -1.2727 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 4.8868 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 14.7437 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 22.1025 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 15.8824 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.0233 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.3879 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.2600 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4252 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 20.2832 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.7373 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.4717 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.7353 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 12.9872 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 42.5840 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 18.0130 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 13.9086 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 41.9724 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.7541 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -3.6548 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 3.7001 -> Slightly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

### JPMorgan Chase & Co. (NYSE:JPM) Stock Price Down 1.4% - What's Next?
- Summary: JPMorgan Chase & Co. (NYSE:JPM) Stock Price Down 1.4% - What's Next?
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxQb3VYMHhoSXpoQ3BLS2RHZkE3Zks1cnBsMnEtUTJESGJfYnVBLTV1ZWJuREJCRHM2TmJVcmFtZGJzZlZZcDFIQW1NdjV0LWVIMTlMdHd3aVFTWDBxOHVZRFhybFU1RzBpcXpUcTZqMXJ5M2JkbGVHejgtOVhjSkotUEktTWtKcG1VbW1vWmF5T1ZfU3NpMnhnRFpfOTFnc0lUYnd2YWNfTEJ3Wko5a0NQNGtlQjhtWTNn?oc=5>

## CATALYSTS

### JPMorgan Chase & Co. $JPM Stock Sold by Arvest Investments Inc.
- Summary: JPMorgan Chase & Co. $JPM Stock Sold by Arvest Investments Inc.
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxPMHhtUGxlUnBQcWJhTC1BdnZtaS1TMnJJUVpqZkQ2VkhpWDZ5OUlXWUJQRnpOM0pROXhwZXQ3TlFvZkE0cnhxbTgyc2ROczFZNHROWG5UUU5BTUQ5YWVzSnNyWW11YUt4d1pQTGpqU2diUy1JNmtTU1NrWWI5VVoyd2VZam5OQVhpNnBTRTVidTI5OWdOZU5sOEZFcDJUNGZWLUg3Y0M1aGJvenZCVTgzY09SclRlSEZ3b0Jz?oc=5>

### JPMorgan Chase & Co. $JPM Stock Sold by Hosking Partners LLP
- Summary: JPMorgan Chase & Co. $JPM Stock Sold by Hosking Partners LLP
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxPTVBTZmJ3Vk9acUQ5M09uVjA3V3plM0xwOWhkcURiVkl6cE5WY2JMbXUyTmkwTkE1RmltaGM4MkQ2VzVsYl9xdkhBbS03NGh3OTY4UllVSkpzbWVocWpkcElOQTQxQ1hDQUs3cG4xdzlwQThOMjZ5RU1KYVVfZEY1MFFLSWhvMVNoeGJzWHZQcHBESlVfSXc0LThNLWMyd2hjQTBVXzg2VXlFamh4bW5WcW5STm5nMGlt?oc=5>

### JPMorgan Chase & Co. $JPM Stock Sold by Grandview Asset Management LLC
- Summary: JPMorgan Chase & Co. $JPM Stock Sold by Grandview Asset Management LLC
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxPenV1WDJlV0Q5VE1pQmkyUWtoa0F2WFVHQnRpU1NoWjdJUFozVU9US1psSUg2M1I3Um1KQXRUYVRhV1VNVHYzMDhGdHZSR1lEV29UUGVOVFdWcWlhRmlCV2daWks4ZzBzMFNLdGZDMWhlcEdWLV9XcTJaMmRYVDN3NXI5RGQ4TzlLV2txSXlKSzkwVVlOZ2VPZHVmNXMtaDc3REh2eUdMZTA5b1E2R3R0NEVPa0tFMjUyS1QwTXhfQUx5c1p5TlE?oc=5>

### JPMorgan Chase & Co. $JPM Stock: Focused Alpha LLC Increases Position
- Summary: JPMorgan Chase & Co. $JPM Stock: Focused Alpha LLC Increases Position
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxQNDRjM3pvVV95enBYUUx3LTBLNG05S195UG91VHZRMUsyUXF4X0RFYjdjNGU3ZTBHRnlxbkl5Z1NybmpqTW5EWVliY25uUWY3aGEwUTRBYnB3eFNsOXZuaHVXTDg3N3RtdThmb2VhY09WNFgtUlFzcTc0LTY0eDMzSWtYbFdHcHhiaHFRYVI0R0JFdEZDeUxwdlVfcGVxT204RzdxLXBTZkRuRE95cTl4UnVJb1NDMWg2d01lSkNTZE81Vms?oc=5>

### JPMorgan Chase & Co. $JPM Stock Holdings Cut by Pinnacle Associates Ltd.
- Summary: Pinnacle Associates reduced its JPM holdings, indicating a potential shift in analyst sentiment.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxPTkM2bmlrQjZwX2ZHNko4eEhUZGZvTm9CUDNXaWVLdUJOVVRfa1huZVZxRUdmcGRjZzl3ZGtSc0x2Q05zczI5TUpWMGcydVJMbTJYUWR0R2ZtT1hVbHctNlExNlRPVnpFOVZ2RTZHbXhEUTVSUUlWWXI5aHlLXzNEOWpfMkNyX0hTSW9qdVo3clRIZVBBMGFhTnNnY05tQW1qOTUyS0VtSnNxSXRkVzl0WU04QVRla01idlpHLWZ2c1JUQWZNeFVv?oc=5>

### JPMorgan Chase & Co. $JPM Stock: Carnegie Investment Counsel Trims Holdings
- Summary: Carnegie Investment Counsel decreased its JPM holdings, reflecting a change in analyst view.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxOeWRoUlFSZEtLTnhOSVNTM214TDlNSVV1ZXdQdFdYb3BJU0lJSnlhMGdtNHdSS3Q1UXpwRmdPREhvWExQZ1Y5QkQweDM0VF81TVduS29IbXZvNnlrekZueWV6UTc0YTlYX0Vtdk9Yam83VmdBc2dwVFdjdTgzR0N5MkM1WHRNdFFjcTdSQ0pCMklhQUV2ZWkyNGNibjhCeTkyVFJ1eldTS2Y3TUhLc1V5bWRVTl9pVm9pYnZTNzA2UjcwSGU0c1R6aDhIaw?oc=5>

## RISKS

### Jamie Dimon Just Listed 5 Market Risks Hiding 'Under the Surface.' JPMorgan Is Already Feeling The Heat.
- Summary: Jamie Dimon identifies five hidden market risks affecting JPMorgan.
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOU3g4a0pTeGFlLUk3c3JNcDRiaDE4OVJJdkNWUkNYSmZTWllIb2QxcGQ3RXBIQkZlSUktYWdVc1drVTZpUnRoVmJDa1QzT3hkaG5BQXFvaE1fR0d3aENVYmpvNTRDQS1hUVZQRGlHaS1mM19NUDFnYXpCZkZXUkxrXzNFc1dWYy1HcWRMWnhEZm56SmlM?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **JPM** | **13.91** | **2.51** | **N/A** | **10.20** | **880,543,858,688.00 USD** | **14.74** |
| BAC | 12.07 | 1.29 | N/A | 7.10 | 350,011,490,304.00 USD | -0.24 |
| C | 11.76 | 1.04 | N/A | 8.00 | 199,650,230,272.00 USD | 27.39 |
| WFC | 11.62 | 1.56 | N/A | 0.40 | 247,305,027,584.00 USD | -0.32 |

Peers fetched as_of: 2026-10-25; JPM reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-13
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-25

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-06
- Revenue (latest available single quarter): 24,246,000,000.00 USD; period 2014-07-01/2014-09-30; fiscal year/reporting period 2014/Q3
- Net income (latest available single quarter): 21,155,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/19617/000162828026054343/jpm-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiuAFBVV95cUxQb3VYMHhoSXpoQ3BLS2RHZkE3Zks1cnBsMnEtUTJESGJfYnVBLTV1ZWJuREJCRHM2TmJVcmFtZGJzZlZZcDFIQW1NdjV0LWVIMTlMdHd3aVFTWDBxOHVZRFhybFU1RzBpcXpUcTZqMXJ5M2JkbGVHejgtOVhjSkotUEktTWtKcG1VbW1vWmF5T1ZfU3NpMnhnRFpfOTFnc0lUYnd2YWNfTEJ3Wko5a0NQNGtlQjhtWTNn?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxPMHhtUGxlUnBQcWJhTC1BdnZtaS1TMnJJUVpqZkQ2VkhpWDZ5OUlXWUJQRnpOM0pROXhwZXQ3TlFvZkE0cnhxbTgyc2ROczFZNHROWG5UUU5BTUQ5YWVzSnNyWW11YUt4d1pQTGpqU2diUy1JNmtTU1NrWWI5VVoyd2VZam5OQVhpNnBTRTVidTI5OWdOZU5sOEZFcDJUNGZWLUg3Y0M1aGJvenZCVTgzY09SclRlSEZ3b0Jz?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxPTVBTZmJ3Vk9acUQ5M09uVjA3V3plM0xwOWhkcURiVkl6cE5WY2JMbXUyTmkwTkE1RmltaGM4MkQ2VzVsYl9xdkhBbS03NGh3OTY4UllVSkpzbWVocWpkcElOQTQxQ1hDQUs3cG4xdzlwQThOMjZ5RU1KYVVfZEY1MFFLSWhvMVNoeGJzWHZQcHBESlVfSXc0LThNLWMyd2hjQTBVXzg2VXlFamh4bW5WcW5STm5nMGlt?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxPenV1WDJlV0Q5VE1pQmkyUWtoa0F2WFVHQnRpU1NoWjdJUFozVU9US1psSUg2M1I3Um1KQXRUYVRhV1VNVHYzMDhGdHZSR1lEV29UUGVOVFdWcWlhRmlCV2daWks4ZzBzMFNLdGZDMWhlcEdWLV9XcTJaMmRYVDN3NXI5RGQ4TzlLV2txSXlKSzkwVVlOZ2VPZHVmNXMtaDc3REh2eUdMZTA5b1E2R3R0NEVPa0tFMjUyS1QwTXhfQUx5c1p5TlE?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxQNDRjM3pvVV95enBYUUx3LTBLNG05S195UG91VHZRMUsyUXF4X0RFYjdjNGU3ZTBHRnlxbkl5Z1NybmpqTW5EWVliY25uUWY3aGEwUTRBYnB3eFNsOXZuaHVXTDg3N3RtdThmb2VhY09WNFgtUlFzcTc0LTY0eDMzSWtYbFdHcHhiaHFRYVI0R0JFdEZDeUxwdlVfcGVxT204RzdxLXBTZkRuRE95cTl4UnVJb1NDMWg2d01lSkNTZE81Vms?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxPTkM2bmlrQjZwX2ZHNko4eEhUZGZvTm9CUDNXaWVLdUJOVVRfa1huZVZxRUdmcGRjZzl3ZGtSc0x2Q05zczI5TUpWMGcydVJMbTJYUWR0R2ZtT1hVbHctNlExNlRPVnpFOVZ2RTZHbXhEUTVSUUlWWXI5aHlLXzNEOWpfMkNyX0hTSW9qdVo3clRIZVBBMGFhTnNnY05tQW1qOTUyS0VtSnNxSXRkVzl0WU04QVRla01idlpHLWZ2c1JUQWZNeFVv?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxOeWRoUlFSZEtLTnhOSVNTM214TDlNSVV1ZXdQdFdYb3BJU0lJSnlhMGdtNHdSS3Q1UXpwRmdPREhvWExQZ1Y5QkQweDM0VF81TVduS29IbXZvNnlrekZueWV6UTc0YTlYX0Vtdk9Yam83VmdBc2dwVFdjdTgzR0N5MkM1WHRNdFFjcTdSQ0pCMklhQUV2ZWkyNGNibjhCeTkyVFJ1eldTS2Y3TUhLc1V5bWRVTl9pVm9pYnZTNzA2UjcwSGU0c1R6aDhIaw?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOU3g4a0pTeGFlLUk3c3JNcDRiaDE4OVJJdkNWUkNYSmZTWllIb2QxcGQ3RXBIQkZlSUktYWdVc1drVTZpUnRoVmJDa1QzT3hkaG5BQXFvaE1fR0d3aENVYmpvNTRDQS1hUVZQRGlHaS1mM19NUDFnYXpCZkZXUkxrXzNFc1dWYy1HcWRMWnhEZm56SmlM?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
