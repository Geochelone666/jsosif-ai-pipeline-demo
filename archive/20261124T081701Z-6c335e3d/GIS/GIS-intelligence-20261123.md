# GIS Intelligence Report

- ticker: **GIS**
- Report as_of: **2026-11-23**
- Market data as_of: **2026-11-23**
- Quant sources: https://finance.yahoo.com/quote/GIS/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/GIS/key-statistics/
- AI analysis snapshot as_of: **2026-11-23**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-24T08:18:27.604019+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 12, 'rule': 1, 'ai': 5, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261122T045655Z-f5ef568d/GIS** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 12 unique headlines; 9 named publishers; 0 exact duplicates; 12 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-11-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 35.0700 |
| Return 1D (%) | -1.8747 |
| Return 1W (%) | -0.4824 |
| Return 1M (%) | 1.9773 |
| Return YTD (%) | -19.3773 |
| Return 1Y (%) | -22.4300 |
| Annualized volatility (%) | 31.2108 |
| Beta vs SPY | -0.4069 |
| Max drawdown (%) | -33.2524 |
| Sharpe (rf=0) | -0.5717 |
| Downside deviation (rf=0, %) | 21.6212 |
| Sortino (rf=0) | -0.8253 |
| Historical VaR 95% (1D, %) | 2.9986 |
| Historical ES 95% (1D, %) | 3.8866 |
| Correlation vs SPY | -0.1952 |
| Tracking error vs SPY (%) | 37.1600 |
| P/E (trailing) | N/A |
| P/B | 2.52 |
| EV/EBITDA | 9.36 |
| Revenue growth (%) | -2.80 |
| Forward P/E (estimate) | 11.16 |
| Gross margin (%) | 33.73 |
| Operating margin (%) | 15.62 |
| Return on equity (%) | -10.49 |
| Free cash flow yield (%) | 6.95 |
| MA50 | 33.7837 |
| Close vs MA50 (%) | 3.8076 |
| MA200 | 35.5972 |
| Close vs MA200 (%) | -1.4809 |
| RSI (14, Wilder) | 53.6393 |
| MACD (12,26) | 0.3096 |
| MACD signal (9) | 0.2675 |
| MACD histogram | 0.0421 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'GIS': 288, 'SPY': 288}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 35.0700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.8747 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.4824 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 1.9773 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -19.3773 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -22.4300 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 31.2108 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.6212 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.8253 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9986 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.8866 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1952 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.1600 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.4069 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -33.2524 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.5717 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 11.1570 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 33.7280 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 15.6240 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: -10.4950 -> Adjusted price fell over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 6.9467 -> No interpretation rule is available for this metric.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 53.6393 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.0421 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 3.8076 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -1.4809 -> Slightly below the moving-average trend level.

## TAILWINDS

### General Mills (GIS) is Suddenly Drawing Wall Street’s Attention
- Summary: Wall Street attention signals market movement.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOMGJ2RGZIMlVrUGM0TGxWV0F2STRMb3l3aEFnZDc2VGxsSXZkc2RwOWc1MWlsT2Y4QUlHU1dSbW1USHNuWkROUjEtcWZwd1BxX1FiZXRYN1lad284R2RwS1JELVQ4QjR2M2J1TjJPSUg5dlRJVHRGdERUcGZKYklyb2JsclQyTncyRnZGQTFfQ09yaDhSWG1QUmh0NUpRSUtW?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### General Mills, Inc. (NYSE:GIS) Stock Has Consensus Price Target of $36.24
- Summary: General Mills, Inc. (NYSE:GIS) Stock Has Consensus Price Target of $36.24
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxQblFIQ2szTS0wOHZoeDdqYXI5QUYwQ0ZmS3RNZkVOX3AzZGo5bUpzV2VKLVhpeEJfSUNfb1BVLXVvM2ZpVXRlQjZTbGlHTzlyaThIZHpnMmdWX0lqc0hXVlJxT1BJMFRaYUZIX2t5bUc1ZmZUME1UZkdXY1ZvdzhKRnpRVUtzbTRrN3lLSzhzaEFhU0JkVmk2bXBCWURSdFRLOXctLVNDNlZmaUZwb1pxc0RKYnI1Ym9jSzNlWndhUGhqamJDTnV1ZTN0bw?oc=5>

### Better Dividend Stock: General Mills vs. Molson Coors
- Summary: GIS offers better dividend yield than Molson Coors.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQSnI3NTM0OXZvYWFEMUJTbzE5SjhWT2FpSzFHRUpHUkJFZUdHSUtKWE45c2t3ZGEzd0JBZ2JoZ3pGcUdXMWZGdGJsa1l1RkxuMmFOTkV2Q25VX0M3Qnd2amZmUXVEbXp6WTU1XzExNERyV2F3eklBRVZuM1hKem9xbVpaZkNyYWYzZVNabkJXNXQyVmc3?oc=5>

### Better High-Yield Dividend Stock: BP vs. General Mills
- Summary: GIS outperforms BP in high-yield dividend comparison.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxNWGZ2RURYRW1aRVJyYXl2c0MzblYwcEFMdUhCVjVlS3lORmVyWW5ZQmJHOVNLMWUwZzVOLUVReV9IdVJuT1RYdmtzbXpJdGtXVVNfYzJGZ0ZoNFQ5b0M4RlplcV84Q19jRXdTdW92M3NRWndBc2wxMzdyV0NFUXRpTUZpNlQ?oc=5>

### Analysts Offer Insights on Consumer Goods Companies: Target (TGT), JM Smucker (SJM) and General Mills (GIS)
- Summary: Analysts provide insights on GIS and peers.
- Date: 2026-11-20 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMikwJBVV95cUxOVmFYY3RVWXNKQklsMk93ZjNObmQxM09DWTNxUXI1dnQzLTlEbjR6VW9BeTF5VmlEUFJXUEFDVXB2eHBYMXhrZm95X0hQSWV1cjE4TFpJWnVuZ0RWbG1pT2lKUnc1VUdEWEhvbkRlenM1bURWZy1SMFFuTFJ6TTdHeUxTb1dLS0JKOFlxaFVpcjVXU3pmM09XcmxFTFlCakREZVRfS3UwTjhUTEwzYlpWU19BUDZtb2pTdm8zeHdpX2tzUmFBdzRzd2lQc0NfdHFnRmdaSkl5b0VLclVPa1BVRkhPR1Roak1Rd1Y3bEpsaHgyYmdFZ0JhWDNTV2l4cWl4a2lhMHl6S08tak5BUlBDcUw5NA?oc=5>

## RISKS

### How Operating Reorganization Will Impact General Mills (GIS) Investors
- Summary: General Mills’ operating reorganization may affect investor outlook, potentially altering financial performance and market perception.
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxObVRwSkFzd3Y1Z282MkowT1hNNmh6VzNraXdkNGpTNWtYN1g0TGxYVW5vTzMtU2pGOW9XYUw2Z0tOWDBvSi15WUNKMDU2WGY4WHJZUVZvczhITjVTVHA3dWRzNWswMEVPZmFIQjdZdjlsVldBc2pYZVdNZzZoUHFXUno5ZUhBOWMxeW5aOEo0bnZWU0Zyd1hfZ2taMmNwaDV4a2xPel9vR3g5bUMwUzZuMzhzeS1fTWxDcml4akhjV1JpcGllM3I5OVFDZTBISzg3OWxBM2F4TUk4QdIB3wFBVV95cUxPZEk5TmhKX3BnTll4bEFwVThvQlNSNENscnNFYVRlR2ZhTFREdGVoZ0stbDBveFE3b1JCU0lqRVhZZTFVWkZkSUtuQnVqNTdjYzFST05rSEREbXB4MV9ZOXdwR0t1azFPLWJ4N1ZfREd6WUZUek8xNmNZck96NEpmSXFmSnNKUnRpME9CWUhSbUNxOXBwczZHOXBLX2U1eXluVV85aHRkQnlIaTBFMWpPSFdjcmxzdlJFQ2x2d0V3OHdhLUFZTG5WRUxPdmZaZzhLYk5TeU9tMkRVRklPMjc0?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **GIS** | **N/A** | **2.52** | **9.36** | **-2.80** | **18,751,477,760.00 USD** | **-22.43** |
| KHC | N/A | 0.83 | 8.51 | -2.00 | 29,714,108,416.00 USD | 6.04 |
| CPB | 17.54 | 1.78 | 8.78 | -7.90 | 6,870,019,072.00 USD | -22.77 |
| SJM | 62.05 | 2.47 | 9.31 | 5.00 | 14,183,982,080.00 USD | 30.80 |

Peers fetched as_of: 2026-11-23; GIS reuses existing data (market data as_of: 2026-11-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-23
- Next expected earnings: 2026-12-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-23

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

- https://news.google.com/rss/articles/CBMioAFBVV95cUxOMGJ2RGZIMlVrUGM0TGxWV0F2STRMb3l3aEFnZDc2VGxsSXZkc2RwOWc1MWlsT2Y4QUlHU1dSbW1USHNuWkROUjEtcWZwd1BxX1FiZXRYN1lad284R2RwS1JELVQ4QjR2M2J1TjJPSUg5dlRJVHRGdERUcGZKYklyb2JsclQyTncyRnZGQTFfQ09yaDhSWG1QUmh0NUpRSUtW?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxQblFIQ2szTS0wOHZoeDdqYXI5QUYwQ0ZmS3RNZkVOX3AzZGo5bUpzV2VKLVhpeEJfSUNfb1BVLXVvM2ZpVXRlQjZTbGlHTzlyaThIZHpnMmdWX0lqc0hXVlJxT1BJMFRaYUZIX2t5bUc1ZmZUME1UZkdXY1ZvdzhKRnpRVUtzbTRrN3lLSzhzaEFhU0JkVmk2bXBCWURSdFRLOXctLVNDNlZmaUZwb1pxc0RKYnI1Ym9jSzNlWndhUGhqamJDTnV1ZTN0bw?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQSnI3NTM0OXZvYWFEMUJTbzE5SjhWT2FpSzFHRUpHUkJFZUdHSUtKWE45c2t3ZGEzd0JBZ2JoZ3pGcUdXMWZGdGJsa1l1RkxuMmFOTkV2Q25VX0M3Qnd2amZmUXVEbXp6WTU1XzExNERyV2F3eklBRVZuM1hKem9xbVpaZkNyYWYzZVNabkJXNXQyVmc3?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxNWGZ2RURYRW1aRVJyYXl2c0MzblYwcEFMdUhCVjVlS3lORmVyWW5ZQmJHOVNLMWUwZzVOLUVReV9IdVJuT1RYdmtzbXpJdGtXVVNfYzJGZ0ZoNFQ5b0M4RlplcV84Q19jRXdTdW92M3NRWndBc2wxMzdyV0NFUXRpTUZpNlQ?oc=5
- https://news.google.com/rss/articles/CBMikwJBVV95cUxOVmFYY3RVWXNKQklsMk93ZjNObmQxM09DWTNxUXI1dnQzLTlEbjR6VW9BeTF5VmlEUFJXUEFDVXB2eHBYMXhrZm95X0hQSWV1cjE4TFpJWnVuZ0RWbG1pT2lKUnc1VUdEWEhvbkRlenM1bURWZy1SMFFuTFJ6TTdHeUxTb1dLS0JKOFlxaFVpcjVXU3pmM09XcmxFTFlCakREZVRfS3UwTjhUTEwzYlpWU19BUDZtb2pTdm8zeHdpX2tzUmFBdzRzd2lQc0NfdHFnRmdaSkl5b0VLclVPa1BVRkhPR1Roak1Rd1Y3bEpsaHgyYmdFZ0JhWDNTV2l4cWl4a2lhMHl6S08tak5BUlBDcUw5NA?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxObVRwSkFzd3Y1Z282MkowT1hNNmh6VzNraXdkNGpTNWtYN1g0TGxYVW5vTzMtU2pGOW9XYUw2Z0tOWDBvSi15WUNKMDU2WGY4WHJZUVZvczhITjVTVHA3dWRzNWswMEVPZmFIQjdZdjlsVldBc2pYZVdNZzZoUHFXUno5ZUhBOWMxeW5aOEo0bnZWU0Zyd1hfZ2taMmNwaDV4a2xPel9vR3g5bUMwUzZuMzhzeS1fTWxDcml4akhjV1JpcGllM3I5OVFDZTBISzg3OWxBM2F4TUk4QdIB3wFBVV95cUxPZEk5TmhKX3BnTll4bEFwVThvQlNSNENscnNFYVRlR2ZhTFREdGVoZ0stbDBveFE3b1JCU0lqRVhZZTFVWkZkSUtuQnVqNTdjYzFST05rSEREbXB4MV9ZOXdwR0t1azFPLWJ4N1ZfREd6WUZUek8xNmNZck96NEpmSXFmSnNKUnRpME9CWUhSbUNxOXBwczZHOXBLX2U1eXluVV85aHRkQnlIaTBFMWpPSFdjcmxzdlJFQ2x2d0V3OHdhLUFZTG5WRUxPdmZaZzhLYk5TeU9tMkRVRklPMjc0?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
