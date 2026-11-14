# XYL Intelligence Report

- ticker: **XYL**
- Report as_of: **2026-11-13**
- Market data as_of: **2026-11-13**
- Quant sources: https://finance.yahoo.com/quote/XYL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/XYL/key-statistics/
- AI analysis snapshot as_of: **2026-11-13**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-14T05:10:06.454125+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 6, 'rule': 5, 'ai': 0, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 6 unique headlines; 6 named publishers; 0 exact duplicates; 6 HTTPS source links; largest publisher share 16.67%; oldest publication 2026-11-09

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 94.1800 |
| Return 1D (%) | 0.1595 |
| Return 1W (%) | -3.7310 |
| Return 1M (%) | -8.1529 |
| Return YTD (%) | -30.0699 |
| Return 1Y (%) | -35.1530 |
| Annualized volatility (%) | 30.7416 |
| Beta vs SPY | 0.6106 |
| Max drawdown (%) | -39.2498 |
| Sharpe (rf=0) | -1.2560 |
| Downside deviation (rf=0, %) | 25.3194 |
| Sortino (rf=0) | -1.5250 |
| Historical VaR 95% (1D, %) | 3.0031 |
| Historical ES 95% (1D, %) | 5.0991 |
| Correlation vs SPY | 0.2708 |
| Tracking error vs SPY (%) | 30.0653 |
| P/E (trailing) | 20.84 |
| P/B | 2.11 |
| EV/EBITDA | 12.29 |
| Revenue growth (%) | -3.00 |
| Forward P/E (estimate) | 16.10 |
| Gross margin (%) | 39.32 |
| Operating margin (%) | 15.51 |
| Return on equity (%) | 9.76 |
| Free cash flow yield (%) | 5.60 |
| MA50 | 102.2788 |
| Close vs MA50 (%) | -7.9184 |
| MA200 | 114.5426 |
| Close vs MA200 (%) | -17.7773 |
| RSI (14, Wilder) | 40.4037 |
| MACD (12,26) | -2.2401 |
| MACD signal (9) | -2.0855 |
| MACD histogram | -0.1546 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'XYL': 282, 'SPY': 282}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 94.1800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.1595 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -3.7310 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -8.1529 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -30.0699 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -35.1530 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 30.7416 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 25.3194 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -1.5250 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.0031 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.0991 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2708 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 30.0653 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.6106 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -39.2498 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -1.2560 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.0980 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 39.3200 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 15.5090 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.7560 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 5.6039 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 20.8363 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 40.4037 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.1546 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -7.9184 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -17.7773 -> Clearly below the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Xylem Declares Fourth Quarter Dividend of 43 Cents per Share
- Summary: Xylem Declares Fourth Quarter Dividend of 43 Cents per Share
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxNUUtKc1RlSjZNcHRCLWllWi1xaXl1X0hkYmx1QkZwSHdHSHpBZHlhSzQ4dlpjVEZyR3l6b2w2QzlPNlJVdmlKUlVBbldkOWVfSXlaVFJJZ2VPZlNKdGlQeW9SRDQ0eFNtc2RweGpUclJZMDhLVHVJbHNOUWc1bk9mZlJkLUNFLXdnMVlXLUl3YU5vdWYwYVFDUzZYaFBiTWZFMkNBV3FZTXQ1SWhucFU2ZUhwWGlaRmhy?oc=5>

### Xylem Acquires Cornell Pump and Roper Pump to Expand Portfolio
- Summary: Xylem Acquires Cornell Pump and Roper Pump to Expand Portfolio
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxOYTk1OVZoRmp6bjF4Q25BSU15Smo3aFJURzk2cUtsOVVWbjhHQWtwTWFXUkpXd25GTGc5UTVTczdqay1TczFjS2JTM3A5OHZiNEI5TkZFSjdKbmlrYUVyYXhtVmdrUW9IcVNhcUF6VExnZkE5a1VKak5vWUxlb0JESXpYM0FNZVpoWEFWSU9UVTNPTktGdFQxdktvdkJlc2g0SkdZYVMzR19yMXkwSDVRd0o1cVkxOUo0d0E?oc=5>

### Xylem Completes Acquisition of Cornell Pump and Roper Pump
- Summary: Xylem Completes Acquisition of Cornell Pump and Roper Pump
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxPbHBjNnVRUHV4RG9lWWVVTDV3cDd5R2R3dHp2NmhFSzlxWi1ZeHBkWmZTcWZtR2hESTBQUTBtVE9BOVRQLThqYVhmSnFEUnpHdERKYVh1ZUxNS0xxSDI0WFp5VDN6emk2Z2ZRaWxNUkZOZHJMM20xU2pXWHdfNWlRc29qZjZFUVNNeHNFQXBvaDNKT2x2dkhPRi1RV3JCdDVWbTQxSFlYUHJYV00?oc=5>

### Xylem (XYL) Launches $1.5 Billion Share Buyback Program
- Summary: Xylem (XYL) Launches $1.5 Billion Share Buyback Program
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQall3WF9mRnhDeUVKcTU1b29pSkhqVWtkdWl4VWtPSExrbFlFbHIyeWFxY012enFEYUVMQTU2LVYtOXdPbF9xZVpZQ3VLYXhfYVlOS25mUWJjTVI4R2ZDeVllbm5WMXNMS05uU0sya1dnSDhDaVJrRTM3S0F4LXZmS2JlUTFLMWJzVnJ0UkFUbDZfeVFG?oc=5>

### Xylem Board Approves $1.5 Billion Share Repurchase Program
- Summary: Xylem Board Approves $1.5 Billion Share Repurchase Program
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxPNFU1Yldnd0pYM0t0ZEtUWHYtR0w1TWl1S0dwUWg4TUNEX0U5ZGdzMnNxQnRrdGlEN2s0eXNKcEdzeVJuUnE3OFpjc1VCcDFYbE12TFZ3Q2FzUE5renRJQU9SdHFHUWdxellwak5FVG1ydC1BNkNQUktiRXhNRmczTUZUbVEzVzdjVkk3ZVBzVzkzbElCVHRyenB1Qmw3OTcxR1BjUVdGbmhCSHluMFE?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **XYL** | **20.84** | **2.11** | **12.29** | **-3.00** | **21,598,732,288.00 USD** | **-35.15** |
| AOS | 17.89 | 4.73 | 11.59 | -0.20 | 8,629,292,032.00 USD | -0.57 |
| PH | 32.91 | 7.55 | 23.03 | 17.90 | 120,508,178,432.00 USD | 14.45 |
| DOV | 24.44 | 3.66 | 15.05 | 7.50 | 27,924,963,328.00 USD | 16.56 |

Peers fetched as_of: 2026-11-13; XYL reuses existing data (market data as_of: 2026-11-13); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-27
- Next expected earnings: 2027-02-09 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-13

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-27
- Revenue (latest available single quarter): 2,201,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 291,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1524472/000152447226000148/xyl-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiuAFBVV95cUxNUUtKc1RlSjZNcHRCLWllWi1xaXl1X0hkYmx1QkZwSHdHSHpBZHlhSzQ4dlpjVEZyR3l6b2w2QzlPNlJVdmlKUlVBbldkOWVfSXlaVFJJZ2VPZlNKdGlQeW9SRDQ0eFNtc2RweGpUclJZMDhLVHVJbHNOUWc1bk9mZlJkLUNFLXdnMVlXLUl3YU5vdWYwYVFDUzZYaFBiTWZFMkNBV3FZTXQ1SWhucFU2ZUhwWGlaRmhy?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxOYTk1OVZoRmp6bjF4Q25BSU15Smo3aFJURzk2cUtsOVVWbjhHQWtwTWFXUkpXd25GTGc5UTVTczdqay1TczFjS2JTM3A5OHZiNEI5TkZFSjdKbmlrYUVyYXhtVmdrUW9IcVNhcUF6VExnZkE5a1VKak5vWUxlb0JESXpYM0FNZVpoWEFWSU9UVTNPTktGdFQxdktvdkJlc2g0SkdZYVMzR19yMXkwSDVRd0o1cVkxOUo0d0E?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxPbHBjNnVRUHV4RG9lWWVVTDV3cDd5R2R3dHp2NmhFSzlxWi1ZeHBkWmZTcWZtR2hESTBQUTBtVE9BOVRQLThqYVhmSnFEUnpHdERKYVh1ZUxNS0xxSDI0WFp5VDN6emk2Z2ZRaWxNUkZOZHJMM20xU2pXWHdfNWlRc29qZjZFUVNNeHNFQXBvaDNKT2x2dkhPRi1RV3JCdDVWbTQxSFlYUHJYV00?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQall3WF9mRnhDeUVKcTU1b29pSkhqVWtkdWl4VWtPSExrbFlFbHIyeWFxY012enFEYUVMQTU2LVYtOXdPbF9xZVpZQ3VLYXhfYVlOS25mUWJjTVI4R2ZDeVllbm5WMXNMS05uU0sya1dnSDhDaVJrRTM3S0F4LXZmS2JlUTFLMWJzVnJ0UkFUbDZfeVFG?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxPNFU1Yldnd0pYM0t0ZEtUWHYtR0w1TWl1S0dwUWg4TUNEX0U5ZGdzMnNxQnRrdGlEN2s0eXNKcEdzeVJuUnE3OFpjc1VCcDFYbE12TFZ3Q2FzUE5renRJQU9SdHFHUWdxellwak5FVG1ydC1BNkNQUktiRXhNRmczTUZUbVEzVzdjVkk3ZVBzVzkzbElCVHRyenB1Qmw3OTcxR1BjUVdGbmhCSHluMFE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
