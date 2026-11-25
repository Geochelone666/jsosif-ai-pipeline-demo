# GIS Intelligence Report

- ticker: **GIS**
- Report as_of: **2026-11-24**
- Market data as_of: **2026-11-24**
- Quant sources: https://finance.yahoo.com/quote/GIS/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/GIS/key-statistics/
- AI analysis snapshot as_of: **2026-11-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-25T07:10:06.246586+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 5, 'rule': 0, 'ai': 1, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261124T081701Z-6c335e3d/GIS** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 5 unique headlines; 4 named publishers; 0 exact duplicates; 5 HTTPS source links; largest publisher share 40.0%; oldest publication 2026-11-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 35.5900 |
| Return 1D (%) | 1.4828 |
| Return 1W (%) | 2.6240 |
| Return 1M (%) | 3.4894 |
| Return YTD (%) | -18.1819 |
| Return 1Y (%) | -18.9661 |
| Annualized volatility (%) | 31.1872 |
| Beta vs SPY | -0.4101 |
| Max drawdown (%) | -33.2524 |
| Sharpe (rf=0) | -0.5222 |
| Downside deviation (rf=0, %) | 21.5781 |
| Sortino (rf=0) | -0.7547 |
| Historical VaR 95% (1D, %) | 2.9959 |
| Historical ES 95% (1D, %) | 3.8866 |
| Correlation vs SPY | -0.1966 |
| Tracking error vs SPY (%) | 37.1441 |
| P/E (trailing) | N/A |
| P/B | 2.55 |
| EV/EBITDA | 9.44 |
| Revenue growth (%) | -2.80 |
| Forward P/E (estimate) | 11.32 |
| Gross margin (%) | 33.73 |
| Operating margin (%) | 15.62 |
| Return on equity (%) | -10.49 |
| Free cash flow yield (%) | 6.85 |
| MA50 | 33.7775 |
| Close vs MA50 (%) | 5.3660 |
| MA200 | 35.5470 |
| Close vs MA200 (%) | 0.1210 |
| RSI (14, Wilder) | 56.3133 |
| MACD (12,26) | 0.3520 |
| MACD signal (9) | 0.2844 |
| MACD histogram | 0.0676 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'GIS': 289, 'SPY': 289}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 35.5900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.4828 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.6240 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 3.4894 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -18.1819 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -18.9661 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 31.1872 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.5781 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.7547 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9959 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.8866 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1966 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.1441 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.4101 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -33.2524 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.5222 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 11.3224 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 33.7280 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 15.6240 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: -10.4950 -> Adjusted price fell over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 6.8452 -> No interpretation rule is available for this metric.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 56.3133 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.0676 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 5.3660 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 0.1210 -> Slightly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

No items in this run

## RISKS

### How Operating Reorganization Will Impact General Mills (GIS) Investors
- Summary: General Mills’ operating reorganization may affect investor outlook, potentially altering financial performance and market perception.
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxObVRwSkFzd3Y1Z282MkowT1hNNmh6VzNraXdkNGpTNWtYN1g0TGxYVW5vTzMtU2pGOW9XYUw2Z0tOWDBvSi15WUNKMDU2WGY4WHJZUVZvczhITjVTVHA3dWRzNWswMEVPZmFIQjdZdjlsVldBc2pYZVdNZzZoUHFXUno5ZUhBOWMxeW5aOEo0bnZWU0Zyd1hfZ2taMmNwaDV4a2xPel9vR3g5bUMwUzZuMzhzeS1fTWxDcml4akhjV1JpcGllM3I5OVFDZTBISzg3OWxBM2F4TUk4QdIB3wFBVV95cUxPZEk5TmhKX3BnTll4bEFwVThvQlNSNENscnNFYVRlR2ZhTFREdGVoZ0stbDBveFE3b1JCU0lqRVhZZTFVWkZkSUtuQnVqNTdjYzFST05rSEREbXB4MV9ZOXdwR0t1azFPLWJ4N1ZfREd6WUZUek8xNmNZck96NEpmSXFmSnNKUnRpME9CWUhSbUNxOXBwczZHOXBLX2U1eXluVV85aHRkQnlIaTBFMWpPSFdjcmxzdlJFQ2x2d0V3OHdhLUFZTG5WRUxPdmZaZzhLYk5TeU9tMkRVRklPMjc0?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **GIS** | **N/A** | **2.55** | **9.44** | **-2.80** | **19,029,514,240.00 USD** | **-18.97** |
| KHC | N/A | 0.84 | 8.61 | -2.00 | 30,270,507,008.00 USD | 8.29 |
| CPB | 18.02 | 1.83 | 8.89 | -7.90 | 7,058,361,856.00 USD | -17.94 |
| SJM | 61.14 | 2.43 | 9.22 | 5.00 | 13,977,814,016.00 USD | 30.46 |

Peers fetched as_of: 2026-11-24; GIS reuses existing data (market data as_of: 2026-11-24); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-23
- Next expected earnings: 2026-12-17 (yfinance; expected dates may change)

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
- Filing date: 2026-09-23
- Revenue (latest available single quarter): 4,389,500,000.00 USD; period 2026-06-01/2026-08-30; fiscal year/reporting period 2027/Q1
- Net income (latest available single quarter): 397,000,000.00 USD; period 2026-06-01/2026-08-30; fiscal year/reporting period 2027/Q1
- SEC link: https://www.sec.gov/Archives/edgar/data/40704/000162828026063201/gis-20260830.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi2gFBVV95cUxObVRwSkFzd3Y1Z282MkowT1hNNmh6VzNraXdkNGpTNWtYN1g0TGxYVW5vTzMtU2pGOW9XYUw2Z0tOWDBvSi15WUNKMDU2WGY4WHJZUVZvczhITjVTVHA3dWRzNWswMEVPZmFIQjdZdjlsVldBc2pYZVdNZzZoUHFXUno5ZUhBOWMxeW5aOEo0bnZWU0Zyd1hfZ2taMmNwaDV4a2xPel9vR3g5bUMwUzZuMzhzeS1fTWxDcml4akhjV1JpcGllM3I5OVFDZTBISzg3OWxBM2F4TUk4QdIB3wFBVV95cUxPZEk5TmhKX3BnTll4bEFwVThvQlNSNENscnNFYVRlR2ZhTFREdGVoZ0stbDBveFE3b1JCU0lqRVhZZTFVWkZkSUtuQnVqNTdjYzFST05rSEREbXB4MV9ZOXdwR0t1azFPLWJ4N1ZfREd6WUZUek8xNmNZck96NEpmSXFmSnNKUnRpME9CWUhSbUNxOXBwczZHOXBLX2U1eXluVV85aHRkQnlIaTBFMWpPSFdjcmxzdlJFQ2x2d0V3OHdhLUFZTG5WRUxPdmZaZzhLYk5TeU9tMkRVRklPMjc0?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
