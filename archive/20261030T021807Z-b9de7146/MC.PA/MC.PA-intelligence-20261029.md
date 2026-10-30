# MC.PA Intelligence Report

- ticker: **MC.PA**
- Report as_of: **2026-10-29**
- Market data as_of: **2026-10-28**
- Quant sources: https://finance.yahoo.com/quote/MC.PA/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MC.PA/key-statistics/
- AI analysis snapshot as_of: **2026-10-29**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-30T02:27:43.989846+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 5, 'rule': 0, 'ai': 2, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261029T020157Z-688a53f0/MC.PA** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 5 unique headlines; 3 named publishers; 0 exact duplicates; 5 HTTPS source links; largest publisher share 60.0%; oldest publication 2026-10-24

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 385.0000 |
| Return 1D (%) | -0.8371 |
| Return 1W (%) | -0.9264 |
| Return 1M (%) | -3.4604 |
| Return YTD (%) | -39.3368 |
| Return 1Y (%) | -35.7867 |
| Annualized volatility (%) | 26.9654 |
| Beta vs SPY | 0.6055 |
| Max drawdown (%) | -41.0025 |
| Sharpe (rf=0) | -1.4872 |
| Downside deviation (rf=0, %) | 20.5336 |
| Sortino (rf=0) | -1.9531 |
| Historical VaR 95% (1D, %) | 2.7422 |
| Historical ES 95% (1D, %) | 3.9949 |
| Correlation vs SPY | 0.2871 |
| Tracking error vs SPY (%) | 26.2897 |
| P/E (trailing) | 17.64 |
| P/B | 2.78 |
| EV/EBITDA | 10.76 |
| Revenue growth (%) | -2.90 |
| Forward P/E (estimate) | 15.90 |
| Gross margin (%) | 66.36 |
| Operating margin (%) | 22.52 |
| Return on equity (%) | 16.59 |
| Free cash flow yield (%) | 6.10 |
| MA50 | 408.1400 |
| Close vs MA50 (%) | -5.6696 |
| MA200 | 468.7807 |
| Close vs MA200 (%) | -17.8721 |
| RSI (14, Wilder) | 41.3673 |
| MACD (12,26) | -5.6057 |
| MACD signal (9) | -7.1655 |
| MACD histogram | 1.5598 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MC.PA': 274, 'SPY': 271}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 385.0000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.8371 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.9264 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -3.4604 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -39.3368 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -35.7867 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 26.9654 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 20.5336 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -1.9531 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.7422 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.9949 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2871 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.2897 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.6055 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -41.0025 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -1.4872 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.9011 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 66.3650 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 22.5210 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 16.5860 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 6.0971 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 17.6402 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 41.3673 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.5598 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -5.6696 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -17.8721 -> Clearly below the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

### LVMH, Kering and Hermès shares fall as France riots damage 3,000 shops and bond yields surge to 2002 highs
- Summary: Shares of LVMH and peers dropped amid France riots damaging thousands of shops and rising bond yields.
- Date: 2026-10-24 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOVVhfTkd1UzBZWGxSOVRKTDN6TUJqYmc4TlllcUJMQnd2OHFHT1VSWjlueEtkSEdINmwxRG9aMVVYME5XeXNYNjBtelhySVdVUlBhVXZYQnVHWFpRM3BQbERXR0ZkaC1Vc3F2Y0Zac1RSLWFHSlhxUzdqcnZfeG1fU2VFaXdEZGNGZHJBbXF2WlUxYzVpNHA0NQ?oc=5>

## CATALYSTS

No items in this run

## RISKS

### LVMH (ENXTPA:MC) Faces Fresh France Riot Risk To Tourism And Luxury Demand
- Summary: LVMH warns of potential impact on tourism and luxury demand due to recent France riots.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPRUlEaDV3N3NNeWdFUDJQdEJ1NU50OGNEVmtzbEJuLWlFYU9JXzNOVUhvSkQtdmRlejFNR2Z5ajlkc2pZdnk5dEZqcDZxa0xzZkR3cTh0UHpTZl9XaXBrdEp5WnkwRXczeDJiak9TaUkxR0Rkd0RFbDhWUHNxdDBGeGZ5QTc4bW1XQnVEZjZKVEdpLXcxSnc?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MC.PA** | **17.64** | **2.78** | **10.76** | **-2.90** | **189,224,697,856.00 EUR** | **-35.79** |
| RMS.PA | 29.66 | 6.97 | 17.37 | 1.60 | 132,595,212,288.00 EUR | -42.20 |
| CFR.SW | 30.00 | 4.34 | 17.37 | 4.20 | 96,657,383,424.00 CHF | 4.21 |
| KER.PA | N/A | 1.49 | 12.68 | -2.90 | 21,615,118,336.00 EUR | -45.32 |

Peers fetched as_of: 2026-10-29; MC.PA reuses existing data (market data as_of: 2026-10-28); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: N/A
- Next expected earnings: 2027-01-26 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-29

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: N/A
- Filing date: N/A
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: N/A

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimAFBVV95cUxOVVhfTkd1UzBZWGxSOVRKTDN6TUJqYmc4TlllcUJMQnd2OHFHT1VSWjlueEtkSEdINmwxRG9aMVVYME5XeXNYNjBtelhySVdVUlBhVXZYQnVHWFpRM3BQbERXR0ZkaC1Vc3F2Y0Zac1RSLWFHSlhxUzdqcnZfeG1fU2VFaXdEZGNGZHJBbXF2WlUxYzVpNHA0NQ?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPRUlEaDV3N3NNeWdFUDJQdEJ1NU50OGNEVmtzbEJuLWlFYU9JXzNOVUhvSkQtdmRlejFNR2Z5ajlkc2pZdnk5dEZqcDZxa0xzZkR3cTh0UHpTZl9XaXBrdEp5WnkwRXczeDJiak9TaUkxR0Rkd0RFbDhWUHNxdDBGeGZ5QTc4bW1XQnVEZjZKVEdpLXcxSnc?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
