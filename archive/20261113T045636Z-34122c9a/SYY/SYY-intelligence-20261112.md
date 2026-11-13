# SYY Intelligence Report

- ticker: **SYY**
- Report as_of: **2026-11-12**
- Market data as_of: **2026-11-12**
- Quant sources: https://finance.yahoo.com/quote/SYY/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SYY/key-statistics/
- AI analysis snapshot as_of: **2026-11-12**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-13T05:20:46.468927+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 7, 'rule': 1, 'ai': 2, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261112T054014Z-6c47e7f9/SYY** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 7 unique headlines; 4 named publishers; 0 exact duplicates; 7 HTTPS source links; largest publisher share 42.86%; oldest publication 2026-11-05

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 76.2400 |
| Return 1D (%) | -0.9098 |
| Return 1W (%) | 1.3291 |
| Return 1M (%) | -3.1258 |
| Return YTD (%) | 6.4588 |
| Return 1Y (%) | 4.0168 |
| Annualized volatility (%) | 29.2008 |
| Beta vs SPY | 0.2373 |
| Max drawdown (%) | -23.9798 |
| Sharpe (rf=0) | 0.2850 |
| Downside deviation (rf=0, %) | 22.3988 |
| Sortino (rf=0) | 0.3716 |
| Historical VaR 95% (1D, %) | 2.1606 |
| Historical ES 95% (1D, %) | 4.3236 |
| Correlation vs SPY | 0.1116 |
| Tracking error vs SPY (%) | 30.8511 |
| P/E (trailing) | 20.28 |
| P/B | 9.28 |
| EV/EBITDA | 11.01 |
| Revenue growth (%) | 2.80 |
| Forward P/E (estimate) | 14.13 |
| Gross margin (%) | 18.54 |
| Operating margin (%) | 4.13 |
| Return on equity (%) | 58.74 |
| Free cash flow yield (%) | 6.42 |
| MA50 | 79.3201 |
| Close vs MA50 (%) | -3.8831 |
| MA200 | 79.5184 |
| Close vs MA200 (%) | -4.1228 |
| RSI (14, Wilder) | 41.7043 |
| MACD (12,26) | -0.9278 |
| MACD signal (9) | -0.4428 |
| MACD histogram | -0.4850 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SYY': 281, 'SPY': 281}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 76.2400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.9098 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.3291 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -3.1258 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 6.4588 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 4.0168 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 29.2008 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 22.3988 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.3716 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.1606 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.3236 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1116 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 30.8511 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.2373 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -23.9798 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2850 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 14.1278 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 18.5430 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 4.1330 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 58.7360 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 6.4151 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 20.2766 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 41.7043 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.4850 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -3.8831 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -4.1228 -> Slightly below the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Sysco (NYSE:SYY) Stock Gets Price Target Reduction from Citigroup
- Summary: Sysco (NYSE:SYY) Stock Gets Price Target Reduction from Citigroup
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxNYzlVYndQQWFvNmN5eWtNZ1VYcTJNY0FSUmRRRGpCUy1Wc3duXzEtUmNFQ2NpdU9vSWNUMEp6YjN4WDdyOUNFT3p1R0tVWGFXLVVIa3lETlkxU3ZpSElEdTllQXZFQVlWZkZNT2x6OHVmX3RFWjd3dUFjMXJZUGhaU3ZnWnZNQ1NheGxPVjNsenk1aVR1dF9reGxIbURiVEJwaUFYcXhhU0xmdUl4SUwwRWlCRk1lTmRuTEozY0ozLWhtTGM?oc=5>

### Sysco (SYY) Stock Forecast and Price Target 2026 $SYY
- Summary: Analysts project 2026 price target for Sysco.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiYkFVX3lxTFBRZ2xLeWo3aWlOT2tCV1hiQ2RkTUZfZmNYUjRDeEtaRFRLNEt3bFE1UlVCTkVxcGhHTXg0WU9Hd1VieElDVDh1VXRoYkRCSnRvMEd2cmkxaDZIdlk5NDdESnN3?oc=5>

### Sysco (NYSE:SYY) Director Buys $191,550.00 in Stock
- Summary: A Sysco director purchased $191,550 worth of company shares, indicating personal confidence in the firm.
- Date: 2026-11-05 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxOdW9Xak9Tak83OTlYUGk2dHVrU1E1d3hWZS0wSzZMY2JiYmRSTWJ1cXlIa1hXU05pbTUwaHZhWS1DWXdwaTBCUkJBTUpNV0NjVERPUXNUNXFWYTBDNlhBUzNEZzdheFJxZ3p3VWpRY1FZNUhJZmROUEFLWXdwZGlGRXdZT2NGWGJpVW15R3VTTmplcHBIcG40eTZ6VFFrUTh2RkFhVU9uenI3ejB6?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SYY** | **20.28** | **9.28** | **11.01** | **2.80** | **37,530,722,304.00 USD** | **4.02** |
| USFD | 30.24 | 5.36 | 14.99 | 2.10 | 23,240,382,464.00 USD | 48.49 |
| PFGC | 43.81 | 3.40 | 14.30 | 5.50 | 17,349,986,304.00 USD | 13.87 |
| CHEF | 45.52 | 6.30 | 19.65 | 11.20 | 4,610,109,440.00 USD | 71.77 |

Peers fetched as_of: 2026-11-12; SYY reuses existing data (market data as_of: 2026-11-12); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-03
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-12

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 21,744,000,000.00 USD; period 2026-06-28/2026-09-26; fiscal year/reporting period 2027/Q1
- Net income (latest available single quarter): 526,000,000.00 USD; period 2026-06-28/2026-09-26; fiscal year/reporting period 2027/Q1
- SEC link: https://www.sec.gov/Archives/edgar/data/96021/000009602126000050/syy-20260926.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiwwFBVV95cUxNYzlVYndQQWFvNmN5eWtNZ1VYcTJNY0FSUmRRRGpCUy1Wc3duXzEtUmNFQ2NpdU9vSWNUMEp6YjN4WDdyOUNFT3p1R0tVWGFXLVVIa3lETlkxU3ZpSElEdTllQXZFQVlWZkZNT2x6OHVmX3RFWjd3dUFjMXJZUGhaU3ZnWnZNQ1NheGxPVjNsenk1aVR1dF9reGxIbURiVEJwaUFYcXhhU0xmdUl4SUwwRWlCRk1lTmRuTEozY0ozLWhtTGM?oc=5
- https://news.google.com/rss/articles/CBMiYkFVX3lxTFBRZ2xLeWo3aWlOT2tCV1hiQ2RkTUZfZmNYUjRDeEtaRFRLNEt3bFE1UlVCTkVxcGhHTXg0WU9Hd1VieElDVDh1VXRoYkRCSnRvMEd2cmkxaDZIdlk5NDdESnN3?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxOdW9Xak9Tak83OTlYUGk2dHVrU1E1d3hWZS0wSzZMY2JiYmRSTWJ1cXlIa1hXU05pbTUwaHZhWS1DWXdwaTBCUkJBTUpNV0NjVERPUXNUNXFWYTBDNlhBUzNEZzdheFJxZ3p3VWpRY1FZNUhJZmROUEFLWXdwZGlGRXdZT2NGWGJpVW15R3VTTmplcHBIcG40eTZ6VFFrUTh2RkFhVU9uenI3ejB6?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
