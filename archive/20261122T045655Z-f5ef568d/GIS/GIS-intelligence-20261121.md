# GIS Intelligence Report

- ticker: **GIS**
- Report as_of: **2026-11-21**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/GIS/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/GIS/key-statistics/
- AI analysis snapshot as_of: **2026-11-21**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-22T05:09:19.585617+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 13, 'rule': 1, 'ai': 1, 'unknown': 0, 'irrelevant': 11})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261121T053104Z-422ce34b/GIS** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 13 unique headlines; 10 named publishers; 0 exact duplicates; 13 HTTPS source links; largest publisher share 23.08%; oldest publication 2026-11-15

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 35.7400 |
| Return 1D (%) | 3.6543 |
| Return 1W (%) | 4.1375 |
| Return 1M (%) | 6.9100 |
| Return YTD (%) | -17.8370 |
| Return 1Y (%) | -20.0883 |
| Annualized volatility (%) | 31.2427 |
| Beta vs SPY | -0.4174 |
| Max drawdown (%) | -33.2524 |
| Sharpe (rf=0) | -0.5654 |
| Downside deviation (rf=0, %) | 21.6857 |
| Sortino (rf=0) | -0.8146 |
| Historical VaR 95% (1D, %) | 2.9959 |
| Historical ES 95% (1D, %) | 3.8866 |
| Correlation vs SPY | -0.1910 |
| Tracking error vs SPY (%) | 36.7567 |
| P/E (trailing) | N/A |
| P/B | 2.56 |
| EV/EBITDA | 9.46 |
| Revenue growth (%) | -2.80 |
| Forward P/E (estimate) | 11.35 |
| Gross margin (%) | 33.73 |
| Operating margin (%) | 15.62 |
| Return on equity (%) | -10.49 |
| Free cash flow yield (%) | 6.82 |
| MA50 | 33.7980 |
| Close vs MA50 (%) | 5.7458 |
| MA200 | 35.6489 |
| Close vs MA200 (%) | 0.2556 |
| RSI (14, Wilder) | 57.8779 |
| MACD (12,26) | 0.3040 |
| MACD signal (9) | 0.2570 |
| MACD histogram | 0.0470 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'GIS': 287, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 35.7400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 3.6543 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 4.1375 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 6.9100 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -17.8370 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -20.0883 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 31.2427 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.6857 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.8146 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9959 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.8866 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1910 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 36.7567 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.4174 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -33.2524 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.5654 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 11.3549 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 33.7280 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 15.6240 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: -10.4950 -> Adjusted price fell over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 6.8165 -> No interpretation rule is available for this metric.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 57.8779 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.0470 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 5.7458 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 0.2556 -> Slightly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### General Mills, Inc. (NYSE:GIS) Stock Has Consensus Price Target of $36.24
- Summary: General Mills, Inc. (NYSE:GIS) Stock Has Consensus Price Target of $36.24
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxQblFIQ2szTS0wOHZoeDdqYXI5QUYwQ0ZmS3RNZkVOX3AzZGo5bUpzV2VKLVhpeEJfSUNfb1BVLXVvM2ZpVXRlQjZTbGlHTzlyaThIZHpnMmdWX0lqc0hXVlJxT1BJMFRaYUZIX2t5bUc1ZmZUME1UZkdXY1ZvdzhKRnpRVUtzbTRrN3lLSzhzaEFhU0JkVmk2bXBCWURSdFRLOXctLVNDNlZmaUZwb1pxc0RKYnI1Ym9jSzNlWndhUGhqamJDTnV1ZTN0bw?oc=5>

## RISKS

### Does Three Segment Reorganization Change The Bull Case For General Mills (GIS)?
- Summary: Reorganization may alter growth prospects, affecting investor sentiment.
- Date: 2026-11-15 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxPdUJZQ3RkQzhxZVJUbW9xWHNUN25rTmJSeHRWWElTdktVVV9oVG9xVEtPZFdqU0xOT0JRejQxMnFxUHBzcmlMcEZUMTZYdW9maS1nYjF1QlA0TjRrUWVpTndQUEQ4Z3BicFlxcnlaSC0xNDFpcE9xVFl5ZmgtajgxbS1xbG5NNTI5a1NKV3FzWXhIR3BrM2lmNmNwYWc4WENhSmxJTHVJNmtUV0x3SDdUblJ6QXY1al9RNV9ZRzktRlZmdVBGSEptbjA4NlRTbmppZE5kTUtKRVd6QdIB3wFBVV95cUxOQnNvNkhSVVJxbWlzRVdiYkI5WnNZRVhNeDRRam9UVEs5RE1aNmxlVDc2UXB1RWEwZG9oZzlOdGRiYVJBQXVuQXJYVWR1YjRPZTVydW50Qk14UG11dDRLUHB6YUI5RWpmNXJNS1MwaUtHODZkMGhMVUpnSkkwVnVCckN4amZZekhTZ1pWeC1LcEc3UlBtLXhuTnNEVEQ2Y3BuR0thdlkySElOWWNPbnA0dGM2Qk1IcXNseXVodWxiV0dydEdwRlFjYnhTQjhJblJuWjlwUnRZeFdUZXJnUkRR?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **GIS** | **N/A** | **2.56** | **9.46** | **-2.80** | **19,109,720,064.00 USD** | **-20.09** |
| KHC | N/A | 0.84 | 8.57 | -2.00 | 30,057,416,704.00 USD | 8.60 |
| CPB | 18.15 | 1.84 | 8.92 | -7.90 | 7,109,184,512.00 USD | -17.85 |
| SJM | 62.47 | 2.48 | 9.35 | 5.00 | 14,280,122,368.00 USD | 33.95 |

Peers fetched as_of: 2026-11-21; GIS reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-23
- Next expected earnings: 2026-12-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-21

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-09-23
- Revenue (latest available single quarter): 4,389,500,000.00 USD; period 2026-06-01/2026-08-30; fiscal year/reporting period 2027/Q1
- Net income (latest available single quarter): 397,000,000.00 USD; period 2026-06-01/2026-08-30; fiscal year/reporting period 2027/Q1
- SEC link: https://www.sec.gov/Archives/edgar/data/40704/000162828026063201/gis-20260830.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiywFBVV95cUxQblFIQ2szTS0wOHZoeDdqYXI5QUYwQ0ZmS3RNZkVOX3AzZGo5bUpzV2VKLVhpeEJfSUNfb1BVLXVvM2ZpVXRlQjZTbGlHTzlyaThIZHpnMmdWX0lqc0hXVlJxT1BJMFRaYUZIX2t5bUc1ZmZUME1UZkdXY1ZvdzhKRnpRVUtzbTRrN3lLSzhzaEFhU0JkVmk2bXBCWURSdFRLOXctLVNDNlZmaUZwb1pxc0RKYnI1Ym9jSzNlWndhUGhqamJDTnV1ZTN0bw?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxPdUJZQ3RkQzhxZVJUbW9xWHNUN25rTmJSeHRWWElTdktVVV9oVG9xVEtPZFdqU0xOT0JRejQxMnFxUHBzcmlMcEZUMTZYdW9maS1nYjF1QlA0TjRrUWVpTndQUEQ4Z3BicFlxcnlaSC0xNDFpcE9xVFl5ZmgtajgxbS1xbG5NNTI5a1NKV3FzWXhIR3BrM2lmNmNwYWc4WENhSmxJTHVJNmtUV0x3SDdUblJ6QXY1al9RNV9ZRzktRlZmdVBGSEptbjA4NlRTbmppZE5kTUtKRVd6QdIB3wFBVV95cUxOQnNvNkhSVVJxbWlzRVdiYkI5WnNZRVhNeDRRam9UVEs5RE1aNmxlVDc2UXB1RWEwZG9oZzlOdGRiYVJBQXVuQXJYVWR1YjRPZTVydW50Qk14UG11dDRLUHB6YUI5RWpmNXJNS1MwaUtHODZkMGhMVUpnSkkwVnVCckN4amZZekhTZ1pWeC1LcEc3UlBtLXhuTnNEVEQ2Y3BuR0thdlkySElOWWNPbnA0dGM2Qk1IcXNseXVodWxiV0dydEdwRlFjYnhTQjhJblJuWjlwUnRZeFdUZXJnUkRR?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
