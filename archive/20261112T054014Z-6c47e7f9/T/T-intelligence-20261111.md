# T Intelligence Report

- ticker: **T**
- Report as_of: **2026-11-11**
- Market data as_of: **2026-11-11**
- Quant sources: https://finance.yahoo.com/quote/T/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/T/key-statistics/
- AI analysis snapshot as_of: **2026-11-11**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-12T05:49:45.949275+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 20, 'rule': 2, 'ai': 10, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **13** exact headline/source/date matches; prior report **20261111T043601Z-d14951e6/T** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 20 unique headlines; 13 named publishers; 1 exact duplicates; 20 HTTPS source links; largest publisher share 20.0%; oldest publication 2026-11-06

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 22.2600 |
| Return 1D (%) | 1.4585 |
| Return 1W (%) | 1.9698 |
| Return 1M (%) | 0.3607 |
| Return YTD (%) | -6.1108 |
| Return 1Y (%) | -7.3785 |
| Annualized volatility (%) | 28.7109 |
| Beta vs SPY | -0.3460 |
| Max drawdown (%) | -28.8854 |
| Sharpe (rf=0) | -0.1231 |
| Downside deviation (rf=0, %) | 21.9799 |
| Sortino (rf=0) | -0.1608 |
| Historical VaR 95% (1D, %) | 2.8546 |
| Historical ES 95% (1D, %) | 4.6484 |
| Correlation vs SPY | -0.1654 |
| Tracking error vs SPY (%) | 33.8115 |
| P/E (trailing) | 11.90 |
| P/B | 1.41 |
| EV/EBITDA | 7.35 |
| Revenue growth (%) | 5.30 |
| Forward P/E (estimate) | 8.58 |
| Gross margin (%) | 59.74 |
| Operating margin (%) | 22.59 |
| Return on equity (%) | 11.61 |
| Free cash flow yield (%) | 7.98 |
| MA50 | 23.5685 |
| Close vs MA50 (%) | -5.5519 |
| MA200 | 24.4091 |
| Close vs MA200 (%) | -8.8046 |
| RSI (14, Wilder) | 49.2889 |
| MACD (12,26) | -0.4505 |
| MACD signal (9) | -0.6296 |
| MACD histogram | 0.1791 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'T': 280, 'SPY': 280}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 22.2600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.4585 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.9698 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 0.3607 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -6.1108 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -7.3785 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 28.7109 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.9799 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.1608 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8546 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.6484 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1654 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 33.8115 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.3460 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.8854 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.1231 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 8.5754 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 59.7420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 22.5930 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 11.6130 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 7.9770 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 11.9037 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 49.2889 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.1791 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -5.5519 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -8.8046 -> Clearly below the moving-average trend level.

## TAILWINDS

### AT&T stock gains satellite handoff milestone as beta nears
- Summary: AT&T stock gains satellite handoff milestone as beta nears
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxPZjM0LW8wSEpEWXNNZVMwZHdUZWV3Z3NubEVjQUlydFl0TnFwQU9sQkRVTnF3MnVLZDZXdWhlcThhb19WSHhxaDEtUVAwMTJOR1R6VURoTzJhYjMzT3lTbjhyUy1FQW9nTWszcGRFYzEzUzdKYzJXVGMxUW5YdUV2Q0R1dzVGNnh6Um95U3MyQnpIbzRBbzFmSng3b19QQWdtb1ptYy04cW92TVQzUDhtdXZXWENQcGFjRU10OVlB?oc=5>

### Is AT&T Stock Stronger Than It Looks?
- Summary: Analysts question AT&T's stock strength, suggesting potential undervaluation.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOV205OXl5UnNZZlVDUUZVNmFvdEVoUnFPYW10RTZROUtpOUpvb211dkVUQ2pMMlkzU0RSSkgtUklLUnc3aXI1Y1VtaTNOX1pVRGtURTBKQ0dvRlVqemhDMk0yYWNqVU5ZWHFxalRrUU9EX29tWlZZVHBFV24zdm5adnBldzNPYXppdWVjTnJqM2ZQREItNWM5OQ?oc=5>

## HEADWINDS

### AT&T Stock Falls 11.8% in a Year: Should You Buy the Dip?
- Summary: AT&T shares dropped 11.8% over the year, raising concerns about valuation.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNeVJqakhwY213N3laR2tsVk5Zam5UbFBhUWVqNEVILTRjdVlEUFJrQ21qV2RwUHNBVmZwQmNZT25JbHo2eFoxUnBGd01Ob1JpWEQzZzBsejJzcjE2X2F3MmJoM2Rpdm5mZ0l1azhKQnZpVnJaN09SdHJVWHUwbVRIaFMwRjhFNFlLY3hj?oc=5>

## CATALYSTS

### AT&T Inc. $T Stock Bought by Vestor Capital LLC
- Summary: AT&T Inc. $T Stock Bought by Vestor Capital LLC
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQVGdGNGU4RU5IRWF6VDMtS0ZQeklodGF1VHdUeHV4eC1XVkdZY3NoRmZROFBZVlZrelkydFNYZHNYRlJzRUprT2VGaVFVTXFPWFN0OURNZUd4cnlaSmx6MXI4Tk55REtaeXRrNVF5aWVhbDZKX3lHeDRraVdPOVpvakNCRGtJblROUmw0ZmdidXF6MkFpbV9qSzJXQk1ZaW1lNktPNmJTNmE?oc=5>

### TELUS Faces Q3 Challenges Amid Strategic Shift; AT&T (T) Dividen
- Summary: AT&T announced a dividend amid TELUS’s Q3 challenges.
- Date: 2026-11-07 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxNSTNSUU9EenFtcnVyRHdYNm5mMXU3MDUwcEJaT3FnaWhSRElpSjVwV1NsQUphRmN4SV9GLTk4cXJFNnFtc1c2dGF0cG91aXFCdXVSc044UWhJdDBPN2VIak5NWXptZHRraUJvRGVvdVVtUF90S2NPejRnWExXNHlLVEp4dF9wMXh5WWdVV2RRVXNDZlZ3cWREOGNyRnJhUTFoeTlhQ2NCSmduNk0zWlFFSlJnZlVjbDhXbnZZZXJhcjlMdw?oc=5>

### AT&T Inc. $T Stock: International Assets Investment Management LLC Decreases Stake
- Summary: International Assets Investment Management LLC reduces its AT&T stake, signaling a shift in institutional ownership.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxNRm54U3l0bWhOVW9VMS1ZTG9RS0I4X3NNc2cxOEtxOVI4NWRLOXpUOHEyTmU1WmZmMmVnS2QyQ2VjQmZkUkpvaXZoNklzeFhvZWZxWVIzaGJnc3loUzRacEY2ZXB3cmVYOTdUUGhaZ3BNUlBGWkdOdjI3VjRKWXl2TG9qN0s3eWV1UTU2WW1WZTFkVWNfdWNmRXc2aUVWb2RST1pyTzJ4RUZuOElPSUFJUVlWWXhnMkVsT1ZpTGh1QzRkdk90MHRkemNFUHoyOVJVVWlYZGV3?oc=5>

### How Investors Are Reacting To AT&T (T) Satellite Phone Handoff
- Summary: Investors react to AT&T's satellite phone handoff, indicating market sentiment on the transition.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxPMndVTWxGVVhEX19hREV1aDRrb2RHS3ZxMzFIa2ZNeXBOcjkxbUVOZm9qRUlKaDZHeXMtSEdFZ3B2QTlGXzVtdXRhaGNTSndNOUxDaTZNdGxXWDI3cXRNVmhCcEl2WS1WbTZOckgzYkhETzNCSmxUTnhhYldrWTJHRkh0LVdtdXVRZzJrcWJtaTRlVll1cEU0RWtNNEpGTGgxYjVtUEZDeFFHZ1F4T1FwaEF1YXhDUdIBuwFBVV95cUxNbGVjdUJJcXVDU01lN1NpOUVST1RjZVI3OHRrWDh0UDZvWFYwa3hoSUVvMlBlWWdSUEcyRkc3dnNFU1I0S2h3eGR0R0hadXBVTnJONm5SeEdqTFZGM0JoOVVlSV82eGYwU2xzMzBIaHExNmVhZk9hM3Q4RkplM2cxbExNS3YxbXlJVFREaVhLTVU4N3ViTTloQmxYX1hUN3BBMC1ISURNNXA1d3FYWWczSUJhUzBzM1JIODRZ?oc=5>

### AT&T Inc. $T Stock Holdings Decreased by International Assets Investment Management LLC
- Summary: International Assets Investment Management LLC reduces its AT&T stake, signaling a shift in institutional ownership.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi3gFBVV95cUxNWngzbGdtalpYRlpjU2w5cUtsTldiLUZMVVcxZElOODVZdkpNc0pJSlYzc0dqc0MyQ0h3enlmbHpJNWZBdDBDRXFRLUNMUjJtSXNRSVJiVjJfT2JhMkF4MS1JY0psQVBFekRwcHgtU3FsSDRyQ1RYWmxibUZvVlV1Y0d1d2RyNUplRElTOUtfaWlFdUNYZ3JlUERyZjI0N19NUTBKY0luTS1YT3I0UmUxU0xZV0xEdmR0Qk5WYnF1R3lmSzlQYUx0Sk1SYnprUXduSFBZOG5SckxTYmpEZ1E?oc=5>

### AT&T Inc. $T Stock Position Lifted by Alps Advisors Inc.
- Summary: Alps Advisors increased its stake in AT&T, signaling confidence in the company’s prospects.
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxNelZ5NTR5S09hQVlkZ2Y3dFdHNG93ZkFOc3ZGckt0UU5VdTVCRGpnT0JYam13bGJveUxMR090anM3RVdmcWNCOV8tSkstWGhPc2dUamVuWWtXeC0xd0JfZ3hkeXRDY2piVzFvVmwwaFlmdUwyckFHVnpDejY4My16YzhzS1NwNTV5OFlRWGpvQ0VoSXlqTHhWazR1TkhTY2xkMlhRbkZjQzhGakZPMFRDbFB5cw?oc=5>

### Fund Update: 1,886,214 AT&T (T) shares added to Cullen Capital Management, LLC portfolio
- Summary: Cullen Capital Management adds 1.9 million AT&T shares, reflecting increased institutional investment.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxQdzJFdmlkdDREMU83VlFHRU80c0FlNmwwcDBjanhiRmczSmFTc2dxemdpV0xocm1yeGRmSlYyWW8xREZVOVdCeGJjQW5YdFd1aHdPdkU3T2RJSVIydnJpM2FJMTV6MDBpYVdDcnJ3LVZSMG1SaTdHZGxxTkFxSU13SmhiT19fTUc0TjdtcUYza0pzNG16QUJTWkltOVN4VmFLeGd3TVNWdkxVem9NUTg0YTdEenB3ZnFVUGduNUpmMXB0ajQwLUtLUWJuQlN1TkxB?oc=5>

### AT&T stock advances as satellite handoff clears beta-testing hurdle
- Summary: AT&T stock rises after satellite handoff passes beta test.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxPRGxRZDFLSG1GNmhmWFFKQThEWC1aSmJNYXpZZ01mZnBzVF9idjhqRC1oX3BmYnI4ZEVhcXZibG4zams2QUtmZWFrcFZqc05sZWFoSVRPTUM4MDQ3Skwzci1RYk5WT3NHRzZWMF8yWDdCUEpQcVdDbk5qb2tza2pVczNfbmVuSWJwd0d0dWE2UHVDeW1hdzlYLWNhQlNCcU1Sd1NxVVM0bExDcjliUmgwX2VWdERIbkRNLWQ0VUdqUUl2VmFVNFFCazBn?oc=5>

### AT&T stock: Satellite handoff moves toward beta testing
- Summary: AT&T stock noted as satellite handoff moves toward beta testing.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxObVpTcjN4dTg2QlpzVTdUazBIdUpFNk9wX1pHZENGZnlCa3pfVnBtMjNqbjVKRnlVbEFraW05NC02LTJqcFRhUVY3ZFEwSDdrS3ZkaWxhREFFaHNPRnVCamUzMElyX0dUS2k1U3RTb2dyTjM5aS1RUENITmplNzM3T2JEWE15QkhSOERVem94ZmdpQm5nUHNSX0V2RkUtUXRwNW5PQU1CcngxY3htS2FGUmxoeDM4TFNs?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **T** | **11.90** | **1.41** | **7.35** | **5.30** | **149,953,904,640.00 USD** | **-7.38** |
| VZ | 11.83 | 1.82 | 7.40 | 1.50 | 193,138,278,400.00 USD | 22.12 |
| TMUS | 16.30 | 3.25 | 8.36 | 7.40 | 182,364,372,992.00 USD | -17.07 |
| BCE | 11.69 | 1.35 | 7.37 | 2.20 | 20,058,630,144.00 USD | -3.19 |

Peers fetched as_of: 2026-11-11; T reuses existing data (market data as_of: 2026-11-11); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-11

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 32,322,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 891,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/732717/000073271726000372/t-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMivgFBVV95cUxPZjM0LW8wSEpEWXNNZVMwZHdUZWV3Z3NubEVjQUlydFl0TnFwQU9sQkRVTnF3MnVLZDZXdWhlcThhb19WSHhxaDEtUVAwMTJOR1R6VURoTzJhYjMzT3lTbjhyUy1FQW9nTWszcGRFYzEzUzdKYzJXVGMxUW5YdUV2Q0R1dzVGNnh6Um95U3MyQnpIbzRBbzFmSng3b19QQWdtb1ptYy04cW92TVQzUDhtdXZXWENQcGFjRU10OVlB?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOV205OXl5UnNZZlVDUUZVNmFvdEVoUnFPYW10RTZROUtpOUpvb211dkVUQ2pMMlkzU0RSSkgtUklLUnc3aXI1Y1VtaTNOX1pVRGtURTBKQ0dvRlVqemhDMk0yYWNqVU5ZWHFxalRrUU9EX29tWlZZVHBFV24zdm5adnBldzNPYXppdWVjTnJqM2ZQREItNWM5OQ?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNeVJqakhwY213N3laR2tsVk5Zam5UbFBhUWVqNEVILTRjdVlEUFJrQ21qV2RwUHNBVmZwQmNZT25JbHo2eFoxUnBGd01Ob1JpWEQzZzBsejJzcjE2X2F3MmJoM2Rpdm5mZ0l1azhKQnZpVnJaN09SdHJVWHUwbVRIaFMwRjhFNFlLY3hj?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQVGdGNGU4RU5IRWF6VDMtS0ZQeklodGF1VHdUeHV4eC1XVkdZY3NoRmZROFBZVlZrelkydFNYZHNYRlJzRUprT2VGaVFVTXFPWFN0OURNZUd4cnlaSmx6MXI4Tk55REtaeXRrNVF5aWVhbDZKX3lHeDRraVdPOVpvakNCRGtJblROUmw0ZmdidXF6MkFpbV9qSzJXQk1ZaW1lNktPNmJTNmE?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxNSTNSUU9EenFtcnVyRHdYNm5mMXU3MDUwcEJaT3FnaWhSRElpSjVwV1NsQUphRmN4SV9GLTk4cXJFNnFtc1c2dGF0cG91aXFCdXVSc044UWhJdDBPN2VIak5NWXptZHRraUJvRGVvdVVtUF90S2NPejRnWExXNHlLVEp4dF9wMXh5WWdVV2RRVXNDZlZ3cWREOGNyRnJhUTFoeTlhQ2NCSmduNk0zWlFFSlJnZlVjbDhXbnZZZXJhcjlMdw?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxNRm54U3l0bWhOVW9VMS1ZTG9RS0I4X3NNc2cxOEtxOVI4NWRLOXpUOHEyTmU1WmZmMmVnS2QyQ2VjQmZkUkpvaXZoNklzeFhvZWZxWVIzaGJnc3loUzRacEY2ZXB3cmVYOTdUUGhaZ3BNUlBGWkdOdjI3VjRKWXl2TG9qN0s3eWV1UTU2WW1WZTFkVWNfdWNmRXc2aUVWb2RST1pyTzJ4RUZuOElPSUFJUVlWWXhnMkVsT1ZpTGh1QzRkdk90MHRkemNFUHoyOVJVVWlYZGV3?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxPMndVTWxGVVhEX19hREV1aDRrb2RHS3ZxMzFIa2ZNeXBOcjkxbUVOZm9qRUlKaDZHeXMtSEdFZ3B2QTlGXzVtdXRhaGNTSndNOUxDaTZNdGxXWDI3cXRNVmhCcEl2WS1WbTZOckgzYkhETzNCSmxUTnhhYldrWTJHRkh0LVdtdXVRZzJrcWJtaTRlVll1cEU0RWtNNEpGTGgxYjVtUEZDeFFHZ1F4T1FwaEF1YXhDUdIBuwFBVV95cUxNbGVjdUJJcXVDU01lN1NpOUVST1RjZVI3OHRrWDh0UDZvWFYwa3hoSUVvMlBlWWdSUEcyRkc3dnNFU1I0S2h3eGR0R0hadXBVTnJONm5SeEdqTFZGM0JoOVVlSV82eGYwU2xzMzBIaHExNmVhZk9hM3Q4RkplM2cxbExNS3YxbXlJVFREaVhLTVU4N3ViTTloQmxYX1hUN3BBMC1ISURNNXA1d3FYWWczSUJhUzBzM1JIODRZ?oc=5
- https://news.google.com/rss/articles/CBMi3gFBVV95cUxNWngzbGdtalpYRlpjU2w5cUtsTldiLUZMVVcxZElOODVZdkpNc0pJSlYzc0dqc0MyQ0h3enlmbHpJNWZBdDBDRXFRLUNMUjJtSXNRSVJiVjJfT2JhMkF4MS1JY0psQVBFekRwcHgtU3FsSDRyQ1RYWmxibUZvVlV1Y0d1d2RyNUplRElTOUtfaWlFdUNYZ3JlUERyZjI0N19NUTBKY0luTS1YT3I0UmUxU0xZV0xEdmR0Qk5WYnF1R3lmSzlQYUx0Sk1SYnprUXduSFBZOG5SckxTYmpEZ1E?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxNelZ5NTR5S09hQVlkZ2Y3dFdHNG93ZkFOc3ZGckt0UU5VdTVCRGpnT0JYam13bGJveUxMR090anM3RVdmcWNCOV8tSkstWGhPc2dUamVuWWtXeC0xd0JfZ3hkeXRDY2piVzFvVmwwaFlmdUwyckFHVnpDejY4My16YzhzS1NwNTV5OFlRWGpvQ0VoSXlqTHhWazR1TkhTY2xkMlhRbkZjQzhGakZPMFRDbFB5cw?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxQdzJFdmlkdDREMU83VlFHRU80c0FlNmwwcDBjanhiRmczSmFTc2dxemdpV0xocm1yeGRmSlYyWW8xREZVOVdCeGJjQW5YdFd1aHdPdkU3T2RJSVIydnJpM2FJMTV6MDBpYVdDcnJ3LVZSMG1SaTdHZGxxTkFxSU13SmhiT19fTUc0TjdtcUYza0pzNG16QUJTWkltOVN4VmFLeGd3TVNWdkxVem9NUTg0YTdEenB3ZnFVUGduNUpmMXB0ajQwLUtLUWJuQlN1TkxB?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxPRGxRZDFLSG1GNmhmWFFKQThEWC1aSmJNYXpZZ01mZnBzVF9idjhqRC1oX3BmYnI4ZEVhcXZibG4zams2QUtmZWFrcFZqc05sZWFoSVRPTUM4MDQ3Skwzci1RYk5WT3NHRzZWMF8yWDdCUEpQcVdDbk5qb2tza2pVczNfbmVuSWJwd0d0dWE2UHVDeW1hdzlYLWNhQlNCcU1Sd1NxVVM0bExDcjliUmgwX2VWdERIbkRNLWQ0VUdqUUl2VmFVNFFCazBn?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxObVpTcjN4dTg2QlpzVTdUazBIdUpFNk9wX1pHZENGZnlCa3pfVnBtMjNqbjVKRnlVbEFraW05NC02LTJqcFRhUVY3ZFEwSDdrS3ZkaWxhREFFaHNPRnVCamUzMElyX0dUS2k1U3RTb2dyTjM5aS1RUENITmplNzM3T2JEWE15QkhSOERVem94ZmdpQm5nUHNSX0V2RkUtUXRwNW5PQU1CcngxY3htS2FGUmxoeDM4TFNs?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
