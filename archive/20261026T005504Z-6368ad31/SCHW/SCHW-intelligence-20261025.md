# SCHW Intelligence Report

- ticker: **SCHW**
- Report as_of: **2026-10-25**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/SCHW/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SCHW/key-statistics/
- AI analysis snapshot as_of: **2026-10-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-26T00:57:39.245730+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 20, 'rule': 0, 'ai': 3, 'unknown': 0, 'irrelevant': 17})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 20 unique headlines; 8 named publishers; 0 exact duplicates; 20 HTTPS source links; largest publisher share 45.0%; oldest publication 2026-10-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 90.5800 |
| Return 1D (%) | -0.9405 |
| Return 1W (%) | -1.5006 |
| Return 1M (%) | -8.9648 |
| Return YTD (%) | -8.4396 |
| Return 1Y (%) | -3.0257 |
| Annualized volatility (%) | 25.4483 |
| Beta vs SPY | 0.4252 |
| Max drawdown (%) | -21.1791 |
| Sharpe (rf=0) | 0.0070 |
| Downside deviation (rf=0, %) | 19.6437 |
| Sortino (rf=0) | 0.0091 |
| Historical VaR 95% (1D, %) | 2.5523 |
| Historical ES 95% (1D, %) | 3.9505 |
| Correlation vs SPY | 0.2130 |
| Tracking error vs SPY (%) | 25.9215 |
| P/E (trailing) | 15.48 |
| P/B | 3.05 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 16.90 |
| Forward P/E (estimate) | 11.60 |
| Gross margin (%) | 97.51 |
| Operating margin (%) | 52.67 |
| Return on equity (%) | 21.12 |
| Free cash flow yield (%) | N/A |
| MA50 | 102.6680 |
| Close vs MA50 (%) | -11.7739 |
| MA200 | 97.4725 |
| Close vs MA200 (%) | -7.0712 |
| RSI (14, Wilder) | 30.4836 |
| MACD (12,26) | -3.2002 |
| MACD signal (9) | -2.9827 |
| MACD histogram | -0.2176 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SCHW': 267, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 90.5800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.9405 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.5006 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -8.9648 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -8.4396 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -3.0257 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 25.4483 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 19.6437 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.0091 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.5523 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.9505 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2130 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 25.9215 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.4252 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -21.1791 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.0070 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 11.5988 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 97.5060 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 52.6700 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 21.1220 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 15.4838 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 30.4836 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.2176 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -11.7739 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -7.0712 -> Clearly below the moving-average trend level.

## TAILWINDS

### Schwab Consistently Keeps EOCA Low (NYSE:SCHW)
- Summary: Schwab maintains low expense ratios, benefiting investors.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMigAFBVV95cUxPTHdjcnZuQ0doR1ZwU0VKMHNqV2hzOWdnemtSaV9uWmwyaXZPY01rMUZyZHV6Y1o4OVZ0M2ZtQmFuOXlhckFVMHpLeUZGRWFEZE9zOF94Y3U2MHZka2RiUmx4eV9PcHgwMDVrekxpX09oM0pMLWdyYkl0ZEt2bWw0eQ?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Morgan Stanley Adjusts Price Target on Charles Schwab to $132 From $141
- Summary: Morgan Stanley lowers Schwab price target, indicating a more cautious outlook.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxPN1FETDNmUm1ZcjJUM1Brd2Rqam9jUG9rUlhwYXZkR0dmQ1FQTG4yYjdFaXljZTJVNlFwSldQNFY3SEZwNEVBSU9FMFpLUVF0VzVIdy1pYlEweXU5Ui1mbHpNRklGS25yQmVsd21PcUZSMUNqOC11dm53Q0RJOGdjS0VNZlV1YVdqM2xaVTlOQ1dseXJPcXFuenRwZ0tZTmJBRVE?oc=5>

### Charles Schwab (SCHW) Added An International Bond ETF
- Summary: Schwab expands product offerings by launching an international bond ETF, broadening investment options for clients.
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxOVG5vd19ZbExFb1FrODBpVzJvMVJ5YmtwX3FNTkRXWWl2c0VrbGdZZndPOGNjMTkzeTBXTWMzVExEcjZKdk5wc1BLYnhQTVlPOUNybXpJRHNFOE5EU25PVzNJdFFxX3ZERG1iYkZuN2pLU19fVjRsOHVRWlNOeEI0UW4tdWt4QU9Mek9TekM4NnAyUWw4clNpaFpQejBST1NDTS1NVkVFRQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SCHW** | **15.48** | **3.05** | **N/A** | **16.90** | **156,643,229,696.00 USD** | **-3.03** |
| IBKR | 30.64 | 5.84 | N/A | 13.50 | 136,782,307,328.00 USD | 20.02 |
| HOOD | 41.88 | 9.02 | N/A | 32.30 | 85,475,753,984.00 USD | -29.23 |
| LPLA | 25.11 | 4.34 | N/A | 36.40 | 24,851,853,312.00 USD | -6.37 |

Peers fetched as_of: 2026-10-25; SCHW reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-21 (yfinance; expected dates may change)

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
- Filing date: 2026-08-07
- Revenue (latest available single quarter): 7,072,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): 2,800,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/316709/000031670926000031/schw-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMigAFBVV95cUxPTHdjcnZuQ0doR1ZwU0VKMHNqV2hzOWdnemtSaV9uWmwyaXZPY01rMUZyZHV6Y1o4OVZ0M2ZtQmFuOXlhckFVMHpLeUZGRWFEZE9zOF94Y3U2MHZka2RiUmx4eV9PcHgwMDVrekxpX09oM0pMLWdyYkl0ZEt2bWw0eQ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxPN1FETDNmUm1ZcjJUM1Brd2Rqam9jUG9rUlhwYXZkR0dmQ1FQTG4yYjdFaXljZTJVNlFwSldQNFY3SEZwNEVBSU9FMFpLUVF0VzVIdy1pYlEweXU5Ui1mbHpNRklGS25yQmVsd21PcUZSMUNqOC11dm53Q0RJOGdjS0VNZlV1YVdqM2xaVTlOQ1dseXJPcXFuenRwZ0tZTmJBRVE?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxOVG5vd19ZbExFb1FrODBpVzJvMVJ5YmtwX3FNTkRXWWl2c0VrbGdZZndPOGNjMTkzeTBXTWMzVExEcjZKdk5wc1BLYnhQTVlPOUNybXpJRHNFOE5EU25PVzNJdFFxX3ZERG1iYkZuN2pLU19fVjRsOHVRWlNOeEI0UW4tdWt4QU9Mek9TekM4NnAyUWw4clNpaFpQejBST1NDTS1NVkVFRQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
