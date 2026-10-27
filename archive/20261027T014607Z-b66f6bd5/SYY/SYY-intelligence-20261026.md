# SYY Intelligence Report

- ticker: **SYY**
- Report as_of: **2026-10-26**
- Market data as_of: **2026-10-26**
- Quant sources: https://finance.yahoo.com/quote/SYY/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SYY/key-statistics/
- AI analysis snapshot as_of: **2026-10-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-27T02:09:57.139994+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 4, 'rule': 1, 'ai': 0, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **N/A (no successful AI classification call)**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261026T005504Z-6368ad31/SYY** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 4 unique headlines; 4 named publishers; 0 exact duplicates; 4 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-10-22

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 82.1600 |
| Return 1D (%) | 0.9709 |
| Return 1W (%) | 0.6986 |
| Return 1M (%) | 5.4616 |
| Return YTD (%) | 14.7253 |
| Return 1Y (%) | 9.2968 |
| Annualized volatility (%) | 27.6130 |
| Beta vs SPY | 0.1494 |
| Max drawdown (%) | -23.9798 |
| Sharpe (rf=0) | 0.4350 |
| Downside deviation (rf=0, %) | 20.5632 |
| Sortino (rf=0) | 0.5842 |
| Historical VaR 95% (1D, %) | 2.1115 |
| Historical ES 95% (1D, %) | 3.8061 |
| Correlation vs SPY | 0.0688 |
| Tracking error vs SPY (%) | 29.5952 |
| P/E (trailing) | 22.45 |
| P/B | 14.75 |
| EV/EBITDA | 11.71 |
| Revenue growth (%) | 4.70 |
| Forward P/E (estimate) | 15.37 |
| Gross margin (%) | 18.50 |
| Operating margin (%) | 4.84 |
| Return on equity (%) | 77.69 |
| Free cash flow yield (%) | 4.74 |
| MA50 | 80.1564 |
| Close vs MA50 (%) | 2.4996 |
| MA200 | 79.3393 |
| Close vs MA200 (%) | 3.5553 |
| RSI (14, Wilder) | 57.0399 |
| MACD (12,26) | 0.8921 |
| MACD signal (9) | 0.4751 |
| MACD histogram | 0.4170 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SYY': 268, 'SPY': 268}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 82.1600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.9709 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.6986 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 5.4616 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 14.7253 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 9.2968 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 27.6130 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 20.5632 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.5842 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.1115 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.8061 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0688 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 29.5952 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.1494 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -23.9798 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.4350 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.3690 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 18.4960 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 4.8450 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 77.6920 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.7358 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 22.4481 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 57.0399 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.4170 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 2.4996 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 3.5553 -> Slightly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

### Sysco Corporation (SYY) Falls 3.10% to $81.37, Testing the Middle of Its Trading Range - Sector Neutral Pair
- Summary: Sysco Corporation (SYY) Falls 3.10% to $81.37, Testing the Middle of Its Trading Range - Sector Neutral Pair
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxOdmN2MGE4WEljTmcybDQ3Nk92UEZKdGV3MGN2Xy1zcjhZbTM1dU8wVURiVTBvYy1jSV9xVXRHRHJXV2ctaEtnSGU0Q3ZvSV9GZnRFU0FLNEFKejFWYm5fZmxoVkozT19iaVFYRnV6YXkyZDYza3JfOGRwRFlSRHV4R0JSYm5FRnV6Um9raDlvUnhQZFBJdUdhRENIaTk3QnhFbllqSmFoLUM2VGc2Z0VlYmtYandwaENkWGZpSUxCT0JGdw?oc=5>

## CATALYSTS

No items in this run

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SYY** | **22.45** | **14.75** | **11.71** | **4.70** | **40,415,653,888.00 USD** | **9.30** |
| USFD | 31.19 | 5.12 | 15.30 | 4.50 | 21,927,282,688.00 USD | 36.44 |
| PFGC | 41.76 | 3.05 | 13.37 | 7.30 | 15,020,838,912.00 USD | -4.62 |
| CHEF | 50.63 | 6.69 | 19.77 | 12.90 | 4,337,847,808.00 USD | 81.64 |

Peers fetched as_of: 2026-10-26; SYY reuses existing data (market data as_of: 2026-10-26); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-04
- Next expected earnings: 2026-11-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-26

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-08-21
- Revenue (latest available single quarter): 20,519,000,000.00 USD; period 2025-12-28/2026-03-28; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 340,000,000.00 USD; period 2025-12-28/2026-03-28; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/96021/000009602126000033/syy-20260627.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiwgFBVV95cUxOdmN2MGE4WEljTmcybDQ3Nk92UEZKdGV3MGN2Xy1zcjhZbTM1dU8wVURiVTBvYy1jSV9xVXRHRHJXV2ctaEtnSGU0Q3ZvSV9GZnRFU0FLNEFKejFWYm5fZmxoVkozT19iaVFYRnV6YXkyZDYza3JfOGRwRFlSRHV4R0JSYm5FRnV6Um9raDlvUnhQZFBJdUdhRENIaTk3QnhFbllqSmFoLUM2VGc2Z0VlYmtYandwaENkWGZpSUxCT0JGdw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
