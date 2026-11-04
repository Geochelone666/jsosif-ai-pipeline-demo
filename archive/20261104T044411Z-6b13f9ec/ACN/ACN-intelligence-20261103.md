# ACN Intelligence Report

- ticker: **ACN**
- Report as_of: **2026-11-03**
- Market data as_of: **2026-11-03**
- Quant sources: https://finance.yahoo.com/quote/ACN/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ACN/key-statistics/
- AI analysis snapshot as_of: **2026-11-03**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-04T04:50:14.744322+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 14, 'rule': 2, 'ai': 6, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261103T051441Z-8b1c85d8/ACN** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 14 unique headlines; 7 named publishers; 0 exact duplicates; 14 HTTPS source links; largest publisher share 28.57%; oldest publication 2026-10-28

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 254.5600 |
| Return 1D (%) | -2.4450 |
| Return 1W (%) | 8.2497 |
| Return 1M (%) | 29.0106 |
| Return YTD (%) | -2.3892 |
| Return 1Y (%) | 5.4137 |
| Annualized volatility (%) | 49.9339 |
| Beta vs SPY | -0.0004 |
| Max drawdown (%) | -56.5068 |
| Sharpe (rf=0) | 0.3566 |
| Downside deviation (rf=0, %) | 34.7179 |
| Sortino (rf=0) | 0.5129 |
| Historical VaR 95% (1D, %) | 4.5949 |
| Historical ES 95% (1D, %) | 6.8005 |
| Correlation vs SPY | -0.0001 |
| Tracking error vs SPY (%) | 51.5492 |
| P/E (trailing) | 18.77 |
| P/B | 4.80 |
| EV/EBITDA | 11.37 |
| Revenue growth (%) | 6.20 |
| Forward P/E (estimate) | 16.02 |
| Gross margin (%) | 32.05 |
| Operating margin (%) | 17.83 |
| Return on equity (%) | 26.02 |
| Free cash flow yield (%) | 6.86 |
| MA50 | 204.6096 |
| Close vs MA50 (%) | 24.4125 |
| MA200 | 187.8891 |
| Close vs MA200 (%) | 35.4842 |
| RSI (14, Wilder) | 66.2732 |
| MACD (12,26) | 16.0487 |
| MACD signal (9) | 15.2361 |
| MACD histogram | 0.8126 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ACN': 274, 'SPY': 274}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 254.5600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.4450 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 8.2497 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 29.0106 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -2.3892 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 5.4137 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 49.9339 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 34.7179 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.5129 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.5949 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.8005 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.0001 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 51.5492 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.0004 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -56.5068 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3566 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.0224 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 32.0500 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 17.8280 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 26.0250 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 6.8589 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 18.7729 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 66.2732 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.8126 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 24.4125 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 35.4842 -> Clearly above the moving-average trend level.

## TAILWINDS

### Accenture PLC (ACN) Shares Surge 4.5% -- What GF Score of 91 Tel
- Summary: Accenture PLC (ACN) Shares Surge 4.5% -- What GF Score of 91 Tel
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxNZlRfSHNlSTlBaWhBdkdGUjBGTmxSR1dxaExZclpvNEVuWDdKZDZmbmdyQ1U4VWQtVkFTSXdELWdSQmljQVItSmVLd0V0aTFnMTEyck9jVzBFUXBqV2s2eTZzWmhUOXdLNWM5OU8yME5sa2xDZDV3aEdNTmFObHA4TmMtV1JVN0luUFZQbFp2akk5LWZTVVU1UFg5S3R0dHp3czlfb19YM1VmWEps?oc=5>

### Accenture PLC Stock (ACN) Closed Up by 4.46% on Oct 30: Facts Behind the Movement
- Summary: Accenture shares closed 4.46% higher on Oct 30, indicating a positive price movement.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxOT1ZmaHVvYVhiUHNncFhEcTZSUGxCeERXZXlSbHNOR2FZNkFCOFJFU2o2eGE1b0FVczJfWHBTR012bndna2JOYTFQSzMxTHFQUXFjekVvWmt1QU9SNGNsa25rbUxrMjNwZGU0NTIyVmhkRFpwUW1PNC1UR1VrRlBibHdvV2tqaGFoMnc?oc=5>

### Accenture PLC Stock (ACN) Moved Up by 4.43% on Oct 28: A Full Analysis
- Summary: Positive price movement indicates favorable market sentiment.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxNNXk1MVNuS3ktZW9oOUFuazFHZkgxU0h6MWhjZ213aGN4d01RZFZJMkY5N3RSTDZXdUVIY1dzYS1LQ3pMeGFvUmYwYjBaWWEyanprTHBReU4ycTI2a2lITlhuOW5sLTRjbzRXRjRRWDJTSW9VaEhYZ2x4ejQ2Z0h0QkRyMFFiaGNFLVE?oc=5>

### Why Accenture (ACN) Stock Is Up Today
- Summary: Accenture shares rise today, driven by market sentiment.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMif0FVX3lxTFB1Z3QySzFfYUdnd2dDVjV2VVhINWNlLXV6WUt2bHlXUjRETHJBWHpKRWM0TkQwZC1aMURPWl8tc3NJejVCOUtwRU5SN0VWN0Y5YUVZV0RaNlVLaWRtdWZ2UERod0J5dnQzQlhFeTkwOC1wMG1NYVFrY19wQVBWbmc?oc=5>

## HEADWINDS

### Accenture (ACN) Sees $560 Million in Net ETF Selling on Oct. 30
- Summary: Accenture ETF shares sold $560M, indicating investor pullback.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNRnllLVVSX2k1WXdXX1dmcjI0eERpbHZLejJsM2pKS0Q5cGUxLTY2aTFDTUloV3cydXlsYkxhWEI4M0psRS1EYzRMN3hjWGZHbElEQkZrbGdTLWltcnEtX0N4WTdNb2R0Y2JYV1FOUUcxbm1CbGNGN0xLYVJBNVJ0MW9ZUk05SHNFaTk5Y2tyQWtRTGwzUGp0WVF1RQ?oc=5>

## CATALYSTS

### Accenture (ACN) Stock Looks Fairly Valued After Fresh AI Launch News
- Summary: Accenture (ACN) Stock Looks Fairly Valued After Fresh AI Launch News
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOSVVTUVJRenRtUXpyRThiN3A5X0NiZnUyTHFvZjRaNFdPa3BpMFp1M0U5cVh1Q0o4bWRKSk1pWXhkWVZGN1lCWnJSeXZuWlVaQ1V3eXhNbUxubnVJMWJzNHphZVpxMGpvQ1JOQXBFSmQ0aXZDRkNua1NTRVNiZnNiamFWR2hVaVVXQ2h4VkladENSa1hncWg3X3lCekkxZw?oc=5>

### Accenture (ACN) Increases Despite Market Slip: Here's What You Need to Know
- Summary: Accenture shares rise amid broader market decline, indicating resilience and potential upside.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOTHpaZ0RYVTJfbm5Hd3JueTYwNDFYZm1pLXpyRExoek5uaTZESUlNSWJPSkc1Mm5tSnd3blBRWjlLSHZqdFdUMWxOQU15dE03SmdPdmFSZ2tSczgxUjJoREZGUW91dG5OZHJlT3FmUDFmVmFQY3dfTDhqZWNrcGFIam9NNi1hcUVJYmRWNThTZWlaLWFfbWRnekYtMmNzc2piQWEyOGhn?oc=5>

### Fund Update: 912,506 ACCENTURE (ACN) Shares Added to PZENA INVESTMENT MANAGEMENT LLC Portfolio
- Summary: PZENA Investment Management added 912,506 ACN shares to its portfolio, indicating confidence in the company.
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxPTVc5ZmFyc1dhYnRocUJQdVIxd0padXlUNDRmWlZvUG9oYUJKVVlQQmVLXy1XV25PclB5V2Z6NXhISGszSWFDMHEzVDVGZUpZbmh6aDVZQkY0Zk04NGttb3k2ZVIwQnpVbk9NN2Y0d3V1TElsQlN5VW14bTRGZFJYMGNBblFYQU5mbWhGUU1uMjRHZkhJeE5MdUs5YkEwVVBfRDBjVHVvc3l3dW9kclE?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ACN** | **18.77** | **4.80** | **11.37** | **6.20** | **155,775,975,424.00 USD** | **5.41** |
| IBM | 21.54 | 6.65 | 17.62 | 4.70 | 236,317,999,104.00 USD | -15.81 |
| CTSH | 11.86 | 1.94 | 7.09 | 4.60 | 28,533,952,512.00 USD | -10.26 |
| INFY | 14.73 | 9.35 | 20.75 | 1.40 | 48,320,991,232.00 USD | -25.73 |

Peers fetched as_of: 2026-11-03; ACN reuses existing data (market data as_of: 2026-11-03); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-01
- Next expected earnings: 2026-12-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-03

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-10-16
- Revenue (latest available single quarter): 18,679,110,000.00 USD; period 2026-06-01/2026-08-31; fiscal year/reporting period 2026/FY
- Net income (latest available single quarter): 1,991,267,000.00 USD; period 2026-06-01/2026-08-31; fiscal year/reporting period 2026/FY
- SEC link: https://www.sec.gov/Archives/edgar/data/1467373/000146737326000049/acn-20260831.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMirAFBVV95cUxNZlRfSHNlSTlBaWhBdkdGUjBGTmxSR1dxaExZclpvNEVuWDdKZDZmbmdyQ1U4VWQtVkFTSXdELWdSQmljQVItSmVLd0V0aTFnMTEyck9jVzBFUXBqV2s2eTZzWmhUOXdLNWM5OU8yME5sa2xDZDV3aEdNTmFObHA4TmMtV1JVN0luUFZQbFp2akk5LWZTVVU1UFg5S3R0dHp3czlfb19YM1VmWEps?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxOT1ZmaHVvYVhiUHNncFhEcTZSUGxCeERXZXlSbHNOR2FZNkFCOFJFU2o2eGE1b0FVczJfWHBTR012bndna2JOYTFQSzMxTHFQUXFjekVvWmt1QU9SNGNsa25rbUxrMjNwZGU0NTIyVmhkRFpwUW1PNC1UR1VrRlBibHdvV2tqaGFoMnc?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxNNXk1MVNuS3ktZW9oOUFuazFHZkgxU0h6MWhjZ213aGN4d01RZFZJMkY5N3RSTDZXdUVIY1dzYS1LQ3pMeGFvUmYwYjBaWWEyanprTHBReU4ycTI2a2lITlhuOW5sLTRjbzRXRjRRWDJTSW9VaEhYZ2x4ejQ2Z0h0QkRyMFFiaGNFLVE?oc=5
- https://news.google.com/rss/articles/CBMif0FVX3lxTFB1Z3QySzFfYUdnd2dDVjV2VVhINWNlLXV6WUt2bHlXUjRETHJBWHpKRWM0TkQwZC1aMURPWl8tc3NJejVCOUtwRU5SN0VWN0Y5YUVZV0RaNlVLaWRtdWZ2UERod0J5dnQzQlhFeTkwOC1wMG1NYVFrY19wQVBWbmc?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNRnllLVVSX2k1WXdXX1dmcjI0eERpbHZLejJsM2pKS0Q5cGUxLTY2aTFDTUloV3cydXlsYkxhWEI4M0psRS1EYzRMN3hjWGZHbElEQkZrbGdTLWltcnEtX0N4WTdNb2R0Y2JYV1FOUUcxbm1CbGNGN0xLYVJBNVJ0MW9ZUk05SHNFaTk5Y2tyQWtRTGwzUGp0WVF1RQ?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOSVVTUVJRenRtUXpyRThiN3A5X0NiZnUyTHFvZjRaNFdPa3BpMFp1M0U5cVh1Q0o4bWRKSk1pWXhkWVZGN1lCWnJSeXZuWlVaQ1V3eXhNbUxubnVJMWJzNHphZVpxMGpvQ1JOQXBFSmQ0aXZDRkNua1NTRVNiZnNiamFWR2hVaVVXQ2h4VkladENSa1hncWg3X3lCekkxZw?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOTHpaZ0RYVTJfbm5Hd3JueTYwNDFYZm1pLXpyRExoek5uaTZESUlNSWJPSkc1Mm5tSnd3blBRWjlLSHZqdFdUMWxOQU15dE03SmdPdmFSZ2tSczgxUjJoREZGUW91dG5OZHJlT3FmUDFmVmFQY3dfTDhqZWNrcGFIam9NNi1hcUVJYmRWNThTZWlaLWFfbWRnekYtMmNzc2piQWEyOGhn?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxPTVc5ZmFyc1dhYnRocUJQdVIxd0padXlUNDRmWlZvUG9oYUJKVVlQQmVLXy1XV25PclB5V2Z6NXhISGszSWFDMHEzVDVGZUpZbmh6aDVZQkY0Zk04NGttb3k2ZVIwQnpVbk9NN2Y0d3V1TElsQlN5VW14bTRGZFJYMGNBblFYQU5mbWhGUU1uMjRHZkhJeE5MdUs5YkEwVVBfRDBjVHVvc3l3dW9kclE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
