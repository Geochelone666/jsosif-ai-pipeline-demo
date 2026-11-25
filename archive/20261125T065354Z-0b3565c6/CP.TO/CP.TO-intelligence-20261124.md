# CP.TO Intelligence Report

- ticker: **CP.TO**
- Report as_of: **2026-11-24**
- Market data as_of: **2026-11-24**
- Quant sources: https://finance.yahoo.com/quote/CP.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CP.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-25T07:07:37.503902+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 3, 'rule': 0, 'ai': 2, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261124T081701Z-6c335e3d/CP.TO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 3 unique headlines; 3 named publishers; 0 exact duplicates; 3 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-11-23

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 132.4900 |
| Return 1D (%) | 1.7198 |
| Return 1W (%) | -0.6077 |
| Return 1M (%) | 5.5529 |
| Return YTD (%) | 31.9586 |
| Return 1Y (%) | 35.3902 |
| Annualized volatility (%) | 22.1525 |
| Beta vs SPY | 0.3459 |
| Max drawdown (%) | -11.9692 |
| Sharpe (rf=0) | 1.4842 |
| Downside deviation (rf=0, %) | 14.5271 |
| Sortino (rf=0) | 2.2633 |
| Historical VaR 95% (1D, %) | 1.8632 |
| Historical ES 95% (1D, %) | 2.9374 |
| Correlation vs SPY | 0.2330 |
| Tracking error vs SPY (%) | 23.8415 |
| P/E (trailing) | 31.10 |
| P/B | 2.52 |
| EV/EBITDA | 16.77 |
| Revenue growth (%) | 15.20 |
| Forward P/E (estimate) | 22.44 |
| Gross margin (%) | 52.76 |
| Operating margin (%) | 39.78 |
| Return on equity (%) | 8.27 |
| Free cash flow yield (%) | 2.38 |
| MA50 | 126.0730 |
| Close vs MA50 (%) | 5.0899 |
| MA200 | 121.5664 |
| Close vs MA200 (%) | 8.9857 |
| RSI (14, Wilder) | 57.0174 |
| MACD (12,26) | 1.6679 |
| MACD signal (9) | 2.0734 |
| MACD histogram | -0.4056 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CP.TO': 288, 'SPY': 289}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 132.4900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.7198 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.6077 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 5.5529 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 31.9586 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 35.3902 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 22.1525 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.5271 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.2633 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.8632 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.9374 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2330 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.8415 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3459 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -11.9692 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.4842 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 22.4371 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 52.7640 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 39.7760 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 8.2680 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.3780 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 31.1009 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 57.0174 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.4056 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 5.0899 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 8.9857 -> Clearly above the moving-average trend level.

## TAILWINDS

### Canadian Pacific Kansas City (TSX:CP) Stock Looks Fully Priced Following Its 48% Run
- Summary: Stock appears fully priced after a 48% rally.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQX3gyVkdfTVJNOUlla2VlOFVqVG94Smw4YmpFcFBYRUxoQVhrRExDbU9KSFhOOEtlXzhUVFk5dEJ3b0NfRWdGWl9lUU5qVzgyZTVLN3R6WHpNREpSOTlwQU1SQWF3NnM0SC1rdFg1WEp6RlBtaUZSWlhzRFc4c1ZLUU9LbkdZYUpBcFRPLVNZemg3UVRfY0FwSnU1MDBsdw?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### S&P upgrades Canadian Pacific Kansas City to A- on cross-border growth momentum
- Summary: S&P raises CP.TO rating to A- citing cross-border growth momentum.
- Date: 2026-11-24 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxPc2dCRS1WQWhHM2lzaWVzMFkzb0ZkODhIWEl4aEtqMHpxMVp5MzZkVFhia3BPVnJvSTc0ZUxyUVFTMGxhOHl1czRxQWNaWTNuejFZSHJiZWtvNlVtQ3BPdUU4YVQ1Q0QxWHNZcndFakRzY1puektnbXlSQ3lyMEdNTHd1M2pRbk5Na1JmTFdaaXcwNzZlN3hTTjlsODNlanMzLVZ0MmZydDM5VkhJMmZLTm8zZFZpLTNqMjdHQ3dteVcxWFA3dGd2ZWVGYVluZw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CP.TO** | **31.10** | **2.52** | **16.77** | **15.20** | **115,207,315,456.00 CAD** | **35.39** |
| CNR.TO | 22.48 | 4.90 | 13.88 | 14.60 | 107,292,319,744.00 CAD | 43.02 |
| UNP | 22.69 | 7.85 | 15.12 | 15.30 | 172,825,837,568.00 USD | 32.28 |
| NSC | 26.68 | 4.27 | 15.03 | 13.60 | 71,482,015,744.00 USD | 14.31 |

Peers fetched as_of: 2026-11-24; CP.TO reuses existing data (market data as_of: 2026-11-24); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-28
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-24

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-29
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: https://www.sec.gov/Archives/edgar/data/16875/000001687526000033/cp-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMingFBVV95cUxQX3gyVkdfTVJNOUlla2VlOFVqVG94Smw4YmpFcFBYRUxoQVhrRExDbU9KSFhOOEtlXzhUVFk5dEJ3b0NfRWdGWl9lUU5qVzgyZTVLN3R6WHpNREpSOTlwQU1SQWF3NnM0SC1rdFg1WEp6RlBtaUZSWlhzRFc4c1ZLUU9LbkdZYUpBcFRPLVNZemg3UVRfY0FwSnU1MDBsdw?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxPc2dCRS1WQWhHM2lzaWVzMFkzb0ZkODhIWEl4aEtqMHpxMVp5MzZkVFhia3BPVnJvSTc0ZUxyUVFTMGxhOHl1czRxQWNaWTNuejFZSHJiZWtvNlVtQ3BPdUU4YVQ1Q0QxWHNZcndFakRzY1puektnbXlSQ3lyMEdNTHd1M2pRbk5Na1JmTFdaaXcwNzZlN3hTTjlsODNlanMzLVZ0MmZydDM5VkhJMmZLTm8zZFZpLTNqMjdHQ3dteVcxWFA3dGd2ZWVGYVluZw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
