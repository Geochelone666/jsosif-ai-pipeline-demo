# NVO Intelligence Report

- ticker: **NVO**
- Report as_of: **2026-10-29**
- Market data as_of: **2026-10-29**
- Quant sources: https://finance.yahoo.com/quote/NVO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVO/key-statistics/
- AI analysis snapshot as_of: **2026-10-29**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-30T02:32:21.376905+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 4, 'rule': 0, 'ai': 1, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261029T020157Z-688a53f0/NVO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 4 unique headlines; 4 named publishers; 0 exact duplicates; 4 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-10-22

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 39.1400 |
| Return 1D (%) | 2.2199 |
| Return 1W (%) | -0.7355 |
| Return 1M (%) | 2.1665 |
| Return YTD (%) | -19.2336 |
| Return 1Y (%) | -20.0040 |
| Annualized volatility (%) | 45.6109 |
| Beta vs SPY | 0.9937 |
| Max drawdown (%) | -43.6699 |
| Sharpe (rf=0) | -0.2587 |
| Downside deviation (rf=0, %) | 34.1067 |
| Sortino (rf=0) | -0.3460 |
| Historical VaR 95% (1D, %) | 3.1060 |
| Historical ES 95% (1D, %) | 7.1341 |
| Correlation vs SPY | 0.2769 |
| Tracking error vs SPY (%) | 43.8273 |
| P/E (trailing) | 9.57 |
| P/B | 5.21 |
| EV/EBITDA | 1.55 |
| Revenue growth (%) | 2.10 |
| Forward P/E (estimate) | 11.38 |
| Gross margin (%) | 81.99 |
| Operating margin (%) | 42.54 |
| Return on equity (%) | 59.81 |
| Free cash flow yield (%) | N/A |
| MA50 | 41.3542 |
| Close vs MA50 (%) | -5.3542 |
| MA200 | 43.4530 |
| Close vs MA200 (%) | -9.9256 |
| RSI (14, Wilder) | 47.9269 |
| MACD (12,26) | -0.5038 |
| MACD signal (9) | -0.7534 |
| MACD histogram | 0.2496 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVO': 271, 'SPY': 271}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 39.1400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.2199 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.7355 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 2.1665 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -19.2336 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -20.0040 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 45.6109 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 34.1067 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.3460 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.1060 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 7.1341 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2769 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 43.8273 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.9937 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -43.6699 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.2587 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 11.3794 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 81.9870 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 42.5400 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 59.8150 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 9.5697 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 47.9269 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.2496 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -5.3542 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -9.9256 -> Clearly below the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Novo Nordisk Vs. Eli Lilly Q3 Preview: I'd (Now) Buy Both, But Lilly Is My Top Pick (NVO)
- Summary: An analyst preview suggests buying both Novo Nordisk and Eli Lilly, with a preference for Lilly, indicating a neutral market view.
- Date: 2026-10-27 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxOdThxQ3V4b1RqMXktQklBMTg0ZjRMLUxaLWtGcndLT2toU2g2czNoQnJnWWJYV3R6ZjJLR01YSFd3bTVmVTZhVE5tVnpFbjI5RFF2VDJFTlJoWVdmNEdIcmoxRS03VnZBaVVFUUF6TVNTbkhIOExhWF9Ed19mRGFTQ2tORWpBQ2JWNExHQ21yeG80aHZYTU55cmtaU3o1bm9BUGZLTjZsM3JNMEN2Q3hkWnV2cVB3Y3loVVE?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVO** | **9.57** | **5.21** | **1.55** | **2.10** | **172,634,210,304.00 USD** | **-20.00** |
| LLY | 46.11 | 46.32 | 30.46 | 47.70 | 1,224,985,149,440.00 USD | 69.92 |
| ROG.SW | N/A | N/A | N/A | N/A | N/A unknown currency | N/A |
| SAN.PA | 23.29 | 1.32 | 8.04 | 14.60 | 91,232,935,936.00 EUR | -8.62 |

Peers fetched as_of: 2026-10-29; NVO reuses existing data (market data as_of: 2026-10-29); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-04
- Next expected earnings: 2026-11-04 (yfinance; expected dates may change)

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

- https://news.google.com/rss/articles/CBMiugFBVV95cUxOdThxQ3V4b1RqMXktQklBMTg0ZjRMLUxaLWtGcndLT2toU2g2czNoQnJnWWJYV3R6ZjJLR01YSFd3bTVmVTZhVE5tVnpFbjI5RFF2VDJFTlJoWVdmNEdIcmoxRS03VnZBaVVFUUF6TVNTbkhIOExhWF9Ed19mRGFTQ2tORWpBQ2JWNExHQ21yeG80aHZYTU55cmtaU3o1bm9BUGZLTjZsM3JNMEN2Q3hkWnV2cVB3Y3loVVE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
