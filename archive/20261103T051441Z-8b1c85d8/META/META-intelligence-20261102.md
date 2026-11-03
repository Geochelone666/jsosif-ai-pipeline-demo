# META Intelligence Report

- ticker: **META**
- Report as_of: **2026-11-02**
- Market data as_of: **2026-11-02**
- Quant sources: https://finance.yahoo.com/quote/META/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/META/key-statistics/
- AI analysis snapshot as_of: **2026-11-02**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-03T05:15:34.838365+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 21, 'rule': 4, 'ai': 7, 'unknown': 0, 'irrelevant': 10})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261102T041627Z-c84a7052/META** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 1, 'positive_sentiment_in_headwinds': 1}
- RSS source audit (metadata only, not article fact-checking): 21 unique headlines; 12 named publishers; 4 exact duplicates; 21 HTTPS source links; largest publisher share 19.05%; oldest publication 2026-10-29

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 606.7300 |
| Return 1D (%) | -1.3431 |
| Return 1W (%) | -3.7792 |
| Return 1M (%) | -16.6671 |
| Return YTD (%) | -7.8471 |
| Return 1Y (%) | -6.1019 |
| Annualized volatility (%) | 41.2605 |
| Beta vs SPY | 1.4240 |
| Max drawdown (%) | -28.7332 |
| Sharpe (rf=0) | 0.0906 |
| Downside deviation (rf=0, %) | 27.4549 |
| Sortino (rf=0) | 0.1362 |
| Historical VaR 95% (1D, %) | 3.6378 |
| Historical ES 95% (1D, %) | 5.6251 |
| Correlation vs SPY | 0.4425 |
| Tracking error vs SPY (%) | 37.3982 |
| P/E (trailing) | 20.98 |
| P/B | 5.69 |
| EV/EBITDA | 13.63 |
| Revenue growth (%) | 26.10 |
| Forward P/E (estimate) | 17.05 |
| Gross margin (%) | 81.03 |
| Operating margin (%) | 35.41 |
| Return on equity (%) | 32.26 |
| Free cash flow yield (%) | 1.09 |
| MA50 | 670.9340 |
| Close vs MA50 (%) | -9.5694 |
| MA200 | 631.2130 |
| Close vs MA200 (%) | -3.8787 |
| RSI (14, Wilder) | 31.7407 |
| MACD (12,26) | -22.6711 |
| MACD signal (9) | -9.9780 |
| MACD histogram | -12.6930 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'META': 273, 'SPY': 273}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 606.7300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.3431 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -3.7792 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -16.6671 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -7.8471 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -6.1019 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 41.2605 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 27.4549 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.1362 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.6378 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.6251 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4425 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.3982 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.4240 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.7332 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.0906 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.0488 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 81.0340 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 35.4140 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 32.2640 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.0861 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 20.9796 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 31.7407 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -12.6930 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -9.5694 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -3.8787 -> Slightly below the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

### Meta Stock Fell 15% in October, Then S&P Forecasts a $71 Billion Cash Flow Deficit. Here’s Where the Stock Could Go by 2030
- Summary: Meta Stock Fell 15% in October, Then S&P Forecasts a $71 Billion Cash Flow Deficit. Here’s Where the Stock Could Go by 2030
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2wFBVV95cUxOak1tdG5hZlI5U2VkdzlDcWtuUjhTZ1lGSWNUR0pLbXRfVXJxZ3VraXRPNy1iQWNiWVcyaTFqeVltMG10Tmc3bEFTZkRoMFI3eVBvUVI4dU9hTW9hQXF4Z29VTExteHRwNkxSbVlIUzZzQ3c4cGItMGdfdUFYODFlTmpCdUJIWGNkSUFTd3VMbU10UUx2dV9aV1psSnQtZ0FWUlpjcW9JUjBjYndaZHZ1LTF3RXVmcl9uOFJkNEMwVHU2Uk9XZW1fd0tyamZuRkI2NzN1bVpsSXdGV00?oc=5>

### Meta Shares Are Down Since Earnings. Is the Stock a Buy?
- Summary: Meta Shares Are Down Since Earnings. Is the Stock a Buy?
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPSGxSb3duSnNNQzRDS2QwQ01KVUJKRHVIeDU1SFNiU2NwX3N5eWkxWkNEekxFVC11eWNGUnNMd19Fa1U3eGljTEFCZXZRbllGNVBUVnExbEU2RW9KWDZtb1FCSlNZQ0h5cjFsMkpMRFhKazhpZktZMnA0V2FCdzluSDBtSzhZZzIzSllTNjRzNmRVV01tVW5B?oc=5>

### Meta Stock Slips as S&P Delivers Stark Warning Over AI Spending
- Summary: Meta Stock Slips as S&P Delivers Stark Warning Over AI Spending
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxNM0tTajVlck0wTDZTRk8zN2tTQndHRFNLd0I2OGFfdU5TTjZ2WHE4SXVFTkZiT0tJN2RQb1RLcURQRnlEeWVFZHhXR0FlbHZlQ2d2OFE0NkdTUFQ0OUhkMkEwMmQ2R0cyZWdleV9hWXJKRkIxSW1OQXd5RldaMDl3LWZFXzZ2Mm1kX0lSakRVeHEzT0VvRkFvZlY2cW1FRHNwX3RKTUEzSUE5MUJWaDJOZHVMWXFaZWpleG9oUkRuX1E?oc=5>

### Is Meta Stock’s Fall A Bargain Or A Warning?
- Summary: Meta’s stock decline raises concerns about valuation and future performance.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQdHR6ZEd6RloxRHdXdUk4cDVPUmJuX3ltU1NiZjh3RHFQc0R2LVdUaVZPdEYzelIxQ1JrZUpMampCVFM1ZGhOeXZoajJZdVlWb2p3SS1lbWlQMFlYVnVxYnpNdE1EeVUxeFlNZEhsVE9jQzQwQU5GdEVvcDhudnd2WXdNNEhwN3BPSDVFZGNBXzdxenhqT1hyMVdBMjM0M1lWclhxcWtB?oc=5>

### Here’s Why Janus Henderson is Bullish On Meta Platforms, Inc. (META)
- Summary: Janus Henderson expresses bullish stance on Meta.
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQYmJCSzlYVVhsNE1DOE04aDhGR1hCLUtyaGR0MXdFa0N6M0JzbFVuZll6RmJoWHJyQ3FxMFpQTFhyOE9lVXRJOFQ0UTdmZGYxWllTd2FZcmVORGhWa0U2ODk5ZnhMQnllazBaaFhheHpuQkJfRDduSk43OE9BTjBteEgzbUtzWklFR2Q4QmZqeUpTWWlSNzlHRHg1RlplQQ?oc=5>

## CATALYSTS

### Meta (META) Stock Sees Modest Fair Value Lift As Muse And Financing Drive Debate
- Summary: Meta (META) Stock Sees Modest Fair Value Lift As Muse And Financing Drive Debate
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNSzVnUFl0aGpRRFVlalhrS21zWkJYNmVMMmtldEpsaTR1djVpNFNqWEpfWVN1bzRELU50b0xDLUNzUGhZVjJTS3NZQURWblJCMF9vdDdmd3FzcHl2NWp5SlV5anNKWWthSG9HVk1TVVcyMGhkWWExQmlDZndUdElGSVNoamdSN0pjMlJ5ZmZvZDZYSVNPeFl3?oc=5>

### Meta Platforms (META) stock price forecast: AI funding and dilution risks after Q3 earnings
- Summary: Forecast warns of AI funding and dilution risks post-Q3 earnings.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxOS0FRMjYzYmNENmdZSkQ5TEdXdXBPeUFXUkc4WDBWcG91a3dJQTlQbVNpQ3ZTLVl6UUZLM1BVUEZ1dnBlc2steXQ3clVEb2paeWV6eWlRem9pbWkwUVVueFN0TU5rWE93MnZyb2tNNkdueXJoLU0wSUFZM3EtTWJWUTRPZG42UExzUS1DXzh3?oc=5>

### Will AI Equity Raise Change Meta (META) Stock Narrative
- Summary: Unclear impact of AI equity on Meta’s stock narrative.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQZXRZVmM5ZUlJbG5hVmFnb2Z3bjB1ZHBVLTRYd0g5QXZ4TnJPLTZycXlCMmNnMmVMVG9HMzR2OVJpSmhsVG4wVE1ER2dKWGtWLWxNT1FzOE5pVkFXdEl3ek9lZUYxZHQyb3h3VjRZV3g1VEZCX1htNmNULVhOMFZRbE5OeDFteTR2MERDZzJ3Z3Vva2owZFE4?oc=5>

### META: 6.5% Preferreds Issuance (NASDAQ:META)
- Summary: Meta issues 6.5% preferred shares to raise capital.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMigwFBVV95cUxORXlORFlTRUw5NS16UmFwam5TOGdmRzRmWnZ3ZGRaTlhabEdfNEFOaThfdm50LXYwcFhGUDRXTWs0d0RabDJaM3dqYndqYzdYaDc4ZE8tWXZFMWdydkloR0x1UW1YZ3AwTWJWb3dwei1ibWlxeml4Yi1NTVlGM2o5eXJ4dw?oc=5>

### Meta to raise $20B from bond offering -- Bloomberg (META:NASDAQ)
- Summary: Meta plans a $20B bond issuance to fund operations.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxQcWhSS2lqVEM2VjJ1TFlBQlY1LWtUNEhrSnFxOW5zN21wbXVUTFNzWmg0RW1RemE5d0g5MW9SVHZlN25MS1BBd2NqeTlXZFl2cEdHS3ZTVlEta3V4dk5CX05felQ2QzdZZE9YMlNWaEUyeDNENnFlVlpSX1RUQUIzX2s0OGhPWlcyaDJXZVNPUQ?oc=5>

### ETFs Are Net Sellers of Meta Platforms (META) on Thursday
- Summary: ETFs sold Meta shares, indicating negative market sentiment.
- Date: 2026-11-02 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOZ2ItaERBamlLbk94ZjhjQy1BcnBCcGd6UTEyaU9XQXVEREdtNE8tYnZhYWxMc1k0a3pEMnI5VE0yR1dFeHByVGNmSGNlcXNQUVFRSTFTa05HeC1LZHdTdHlIei1oVFpBc1JzMGZWVF9HSXp0M243OEFqREpBMlhLVzh2YlRqcVp1WHJJU3BkMms4ZG9QZUN4dGtpNDQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **META** | **20.98** | **5.69** | **13.63** | **26.10** | **1,551,307,243,520.00 USD** | **-6.10** |
| GOOGL | 14.57 | 5.20 | 17.97 | 24.70 | 3,429,902,843,904.00 USD | -0.52 |
| SNAP | N/A | 4.76 | -73.72 | 18.90 | 9,217,027,072.00 USD | -30.13 |
| PINS | 81.24 | 3.75 | 38.41 | 11.90 | 11,647,943,680.00 USD | -38.64 |

Peers fetched as_of: 2026-11-02; META reuses existing data (market data as_of: 2026-11-02); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-02

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMi2wFBVV95cUxOak1tdG5hZlI5U2VkdzlDcWtuUjhTZ1lGSWNUR0pLbXRfVXJxZ3VraXRPNy1iQWNiWVcyaTFqeVltMG10Tmc3bEFTZkRoMFI3eVBvUVI4dU9hTW9hQXF4Z29VTExteHRwNkxSbVlIUzZzQ3c4cGItMGdfdUFYODFlTmpCdUJIWGNkSUFTd3VMbU10UUx2dV9aV1psSnQtZ0FWUlpjcW9JUjBjYndaZHZ1LTF3RXVmcl9uOFJkNEMwVHU2Uk9XZW1fd0tyamZuRkI2NzN1bVpsSXdGV00?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPSGxSb3duSnNNQzRDS2QwQ01KVUJKRHVIeDU1SFNiU2NwX3N5eWkxWkNEekxFVC11eWNGUnNMd19Fa1U3eGljTEFCZXZRbllGNVBUVnExbEU2RW9KWDZtb1FCSlNZQ0h5cjFsMkpMRFhKazhpZktZMnA0V2FCdzluSDBtSzhZZzIzSllTNjRzNmRVV01tVW5B?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxNM0tTajVlck0wTDZTRk8zN2tTQndHRFNLd0I2OGFfdU5TTjZ2WHE4SXVFTkZiT0tJN2RQb1RLcURQRnlEeWVFZHhXR0FlbHZlQ2d2OFE0NkdTUFQ0OUhkMkEwMmQ2R0cyZWdleV9hWXJKRkIxSW1OQXd5RldaMDl3LWZFXzZ2Mm1kX0lSakRVeHEzT0VvRkFvZlY2cW1FRHNwX3RKTUEzSUE5MUJWaDJOZHVMWXFaZWpleG9oUkRuX1E?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQdHR6ZEd6RloxRHdXdUk4cDVPUmJuX3ltU1NiZjh3RHFQc0R2LVdUaVZPdEYzelIxQ1JrZUpMampCVFM1ZGhOeXZoajJZdVlWb2p3SS1lbWlQMFlYVnVxYnpNdE1EeVUxeFlNZEhsVE9jQzQwQU5GdEVvcDhudnd2WXdNNEhwN3BPSDVFZGNBXzdxenhqT1hyMVdBMjM0M1lWclhxcWtB?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQYmJCSzlYVVhsNE1DOE04aDhGR1hCLUtyaGR0MXdFa0N6M0JzbFVuZll6RmJoWHJyQ3FxMFpQTFhyOE9lVXRJOFQ0UTdmZGYxWllTd2FZcmVORGhWa0U2ODk5ZnhMQnllazBaaFhheHpuQkJfRDduSk43OE9BTjBteEgzbUtzWklFR2Q4QmZqeUpTWWlSNzlHRHg1RlplQQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNSzVnUFl0aGpRRFVlalhrS21zWkJYNmVMMmtldEpsaTR1djVpNFNqWEpfWVN1bzRELU50b0xDLUNzUGhZVjJTS3NZQURWblJCMF9vdDdmd3FzcHl2NWp5SlV5anNKWWthSG9HVk1TVVcyMGhkWWExQmlDZndUdElGSVNoamdSN0pjMlJ5ZmZvZDZYSVNPeFl3?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxOS0FRMjYzYmNENmdZSkQ5TEdXdXBPeUFXUkc4WDBWcG91a3dJQTlQbVNpQ3ZTLVl6UUZLM1BVUEZ1dnBlc2steXQ3clVEb2paeWV6eWlRem9pbWkwUVVueFN0TU5rWE93MnZyb2tNNkdueXJoLU0wSUFZM3EtTWJWUTRPZG42UExzUS1DXzh3?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQZXRZVmM5ZUlJbG5hVmFnb2Z3bjB1ZHBVLTRYd0g5QXZ4TnJPLTZycXlCMmNnMmVMVG9HMzR2OVJpSmhsVG4wVE1ER2dKWGtWLWxNT1FzOE5pVkFXdEl3ek9lZUYxZHQyb3h3VjRZV3g1VEZCX1htNmNULVhOMFZRbE5OeDFteTR2MERDZzJ3Z3Vva2owZFE4?oc=5
- https://news.google.com/rss/articles/CBMigwFBVV95cUxORXlORFlTRUw5NS16UmFwam5TOGdmRzRmWnZ3ZGRaTlhabEdfNEFOaThfdm50LXYwcFhGUDRXTWs0d0RabDJaM3dqYndqYzdYaDc4ZE8tWXZFMWdydkloR0x1UW1YZ3AwTWJWb3dwei1ibWlxeml4Yi1NTVlGM2o5eXJ4dw?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxQcWhSS2lqVEM2VjJ1TFlBQlY1LWtUNEhrSnFxOW5zN21wbXVUTFNzWmg0RW1RemE5d0g5MW9SVHZlN25MS1BBd2NqeTlXZFl2cEdHS3ZTVlEta3V4dk5CX05felQ2QzdZZE9YMlNWaEUyeDNENnFlVlpSX1RUQUIzX2s0OGhPWlcyaDJXZVNPUQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOZ2ItaERBamlLbk94ZjhjQy1BcnBCcGd6UTEyaU9XQXVEREdtNE8tYnZhYWxMc1k0a3pEMnI5VE0yR1dFeHByVGNmSGNlcXNQUVFRSTFTa05HeC1LZHdTdHlIei1oVFpBc1JzMGZWVF9HSXp0M243OEFqREpBMlhLVzh2YlRqcVp1WHJJU3BkMms4ZG9QZUN4dGtpNDQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
