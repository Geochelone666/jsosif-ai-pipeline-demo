# VRTX Intelligence Report

- ticker: **VRTX**
- Report as_of: **2026-10-24**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/VRTX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/VRTX/key-statistics/
- AI analysis snapshot as_of: **2026-10-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-25T01:27:48.797100+00:00**
- AI status: **N/A: AI unavailable: Groq application daily budget exhausted (tokens)**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 15, 'rule': 1, 'ai': 0, 'unknown': 14})
- AI model(s) actually used: **N/A (no successful AI classification call)**
- RSS source audit (metadata only, not article fact-checking): 15 unique headlines; 8 named publishers; 1 exact duplicates; 15 HTTPS source links; largest publisher share 46.67%; oldest publication 2026-10-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 523.9300 |
| Return 1D (%) | -2.1003 |
| Return 1W (%) | 4.8405 |
| Return 1M (%) | 1.4700 |
| Return YTD (%) | 15.5660 |
| Return 1Y (%) | 23.9690 |
| Annualized volatility (%) | 29.0832 |
| Beta vs SPY | 0.4894 |
| Max drawdown (%) | -15.2113 |
| Sharpe (rf=0) | 0.8854 |
| Downside deviation (rf=0, %) | 17.8484 |
| Sortino (rf=0) | 1.4428 |
| Historical VaR 95% (1D, %) | 2.6839 |
| Historical ES 95% (1D, %) | 3.4058 |
| Correlation vs SPY | 0.2145 |
| Tracking error vs SPY (%) | 29.1424 |
| P/E (trailing) | 29.90 |
| P/B | 6.56 |
| EV/EBITDA | 24.88 |
| Revenue growth (%) | 12.50 |
| Forward P/E (estimate) | 25.66 |
| Gross margin (%) | 54.96 |
| Operating margin (%) | 38.05 |
| Return on equity (%) | 23.54 |
| Free cash flow yield (%) | 1.98 |
| MA50 | 522.7088 |
| Close vs MA50 (%) | 0.2336 |
| MA200 | 477.3702 |
| Close vs MA200 (%) | 9.7534 |
| RSI (14, Wilder) | 55.0729 |
| MACD (12,26) | 0.7421 |
| MACD signal (9) | -2.6775 |
| MACD histogram | 3.4196 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'VRTX': 267, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 523.9300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.1003 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 4.8405 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 1.4700 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 15.5660 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 23.9690 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 29.0832 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 17.8484 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.4428 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.6839 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.4058 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2145 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 29.1424 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.4894 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.2113 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.8854 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 25.6598 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.9570 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 38.0550 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 23.5430 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.9789 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 29.9047 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 55.0729 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 3.4196 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 0.2336 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 9.7534 -> Clearly above the moving-average trend level.

## TAILWINDS

### Vertex Pharmaceuticals (VRTX) Outpaces Stock Market Gains: What You Should Know
- Summary: Vertex Pharmaceuticals (VRTX) Outpaces Stock Market Gains: What You Should Know
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxOUFgyYVJvNnAxN1I1bmZmcnZIQXIzVC1uNlZGUzZqR3ozSEEtYnV3T1p4ZG1TRGRhRUhRY1NJZllOUzBqTjVRUmdNelBKMV9BZ1dtcUk2bng3NlJFdjlEV0ZIUEg2TVFuZUNJZHFCQXRmNFVza2FidlZOLXZhbEFlM3QyY2pMNTJKLVJ5Z3A0T2VzLUs3Y19zVWtHWURmMnVXSzd5cWVDUEt1Njg?oc=5>

## HEADWINDS

N/A: AI unavailable: Groq application daily budget exhausted (tokens)

## CATALYSTS

N/A: AI unavailable: Groq application daily budget exhausted (tokens)

## RISKS

N/A: AI unavailable: Groq application daily budget exhausted (tokens)

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **VRTX** | **29.90** | **6.56** | **24.88** | **12.50** | **132,795,785,216.00 USD** | **23.97** |
| REGN | 19.91 | 2.55 | 15.97 | 16.70 | 82,880,831,488.00 USD | 40.55 |
| BIIB | 44.53 | 1.96 | 13.13 | 3.40 | 37,040,451,584.00 USD | 67.04 |
| AMGN | 27.28 | 20.32 | 16.26 | 9.50 | 237,478,019,072.00 USD | 54.13 |

Peers fetched as_of: 2026-10-24; VRTX reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-03
- Next expected earnings: 2026-11-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-24

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-04
- Revenue (latest available single quarter): 640,799,000.00 USD; period 2018-01-01/2018-03-31; fiscal year/reporting period 2018/Q1
- Net income (latest available single quarter): 1,099,800,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/875320/000087532026000259/vrtx-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiqwFBVV95cUxOUFgyYVJvNnAxN1I1bmZmcnZIQXIzVC1uNlZGUzZqR3ozSEEtYnV3T1p4ZG1TRGRhRUhRY1NJZllOUzBqTjVRUmdNelBKMV9BZ1dtcUk2bng3NlJFdjlEV0ZIUEg2TVFuZUNJZHFCQXRmNFVza2FidlZOLXZhbEFlM3QyY2pMNTJKLVJ5Z3A0T2VzLUs3Y19zVWtHWURmMnVXSzd5cWVDUEt1Njg?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
