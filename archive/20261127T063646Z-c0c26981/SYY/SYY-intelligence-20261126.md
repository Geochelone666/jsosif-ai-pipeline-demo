# SYY Intelligence Report

- ticker: **SYY**
- Report as_of: **2026-11-26**
- Market data as_of: **2026-11-25**
- Quant sources: https://finance.yahoo.com/quote/SYY/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SYY/key-statistics/
- AI analysis snapshot as_of: **2026-11-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-27T06:39:45.903646+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 4, 'rule': 1, 'ai': 2, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 4 unique headlines; 3 named publishers; 1 exact duplicates; 4 HTTPS source links; largest publisher share 50.0%; oldest publication 2026-11-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 81.7700 |
| Return 1D (%) | 1.9322 |
| Return 1W (%) | 4.9410 |
| Return 1M (%) | 0.4916 |
| Return YTD (%) | 14.1807 |
| Return 1Y (%) | 10.8415 |
| Annualized volatility (%) | 29.2632 |
| Beta vs SPY | 0.2341 |
| Max drawdown (%) | -23.9798 |
| Sharpe (rf=0) | 0.5031 |
| Downside deviation (rf=0, %) | 22.2673 |
| Sortino (rf=0) | 0.6612 |
| Historical VaR 95% (1D, %) | 2.1115 |
| Historical ES 95% (1D, %) | 4.2923 |
| Correlation vs SPY | 0.1194 |
| Tracking error vs SPY (%) | 31.2233 |
| P/E (trailing) | 21.75 |
| P/B | 9.95 |
| EV/EBITDA | 11.62 |
| Revenue growth (%) | 2.80 |
| Forward P/E (estimate) | 15.15 |
| Gross margin (%) | 18.54 |
| Operating margin (%) | 4.13 |
| Return on equity (%) | 58.74 |
| Free cash flow yield (%) | 5.98 |
| MA50 | 79.0023 |
| Close vs MA50 (%) | 3.5033 |
| MA200 | 79.3163 |
| Close vs MA200 (%) | 3.0935 |
| RSI (14, Wilder) | 59.4806 |
| MACD (12,26) | 0.0416 |
| MACD signal (9) | -0.4250 |
| MACD histogram | 0.4666 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SYY': 290, 'SPY': 290}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 81.7700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.9322 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 4.9410 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 0.4916 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 14.1807 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 10.8415 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 29.2632 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 22.2673 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.6612 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.1115 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.2923 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1194 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.2233 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.2341 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -23.9798 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.5031 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.1502 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 18.5430 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 4.1330 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 58.7360 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 5.9812 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 21.7473 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 59.4806 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.4666 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 3.5033 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 3.0935 -> Slightly above the moving-average trend level.

## TAILWINDS

### Why Sysco (SYY) Stock Is Up Today
- Summary: Sysco shares rise today, reflecting positive market sentiment.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigAFBVV95cUxNc0dpMk9nVXpCTmlObVBJYTRvTDM1VGo5dEY5Njk1U3BGYjlDRXdKdURsdGtzWUJrZUI2M3FOUjJYNXVOZmlmb3JmSG9lMFBueElNdHNOcXJqd1U2U25jS0hoVmNnQVcwTVhkek1hbUxhdWI5ZEQwUU56RDBQck9WQw?oc=5>

### Sysco (NYSE:SYY) Stock Breaks Above 200-Day Moving Average - Time to Sell?
- Summary: Sysco stock surpasses 200-day MA, indicating bullish trend.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxPN1R0eW93RTR3MThNbDlZUXRkX0JLanF1SkJFNmwxcTNXb05kWHZXTzYxRmthVmVXSkk4YURucW9LS0o3U05vOE5Iei1YTzlvLXpQaVo4TDlMb3o3T1hsc3RiU21mWk9neVpJdl9RNUloNWNILTdiTG5BQi1YTnNYZ04wSFd5OXZxOHRvc0xUMXFTSER3Skh0bXctaUlHSzYyV2N6ZExfYm5EQklJNHFWVWxYV1Boa3R0M0hkNmNJT3dQUXpBMkt5TQ?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Sysco Corporation $SYY Stock Sold by State Street Corp
- Summary: Sysco Corporation $SYY Stock Sold by State Street Corp
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxQLTNFSXZIYk8zNmZ4el9KRWgxenZVT2dfMUtoVFRQUFdRS3VFOWVKSV9OS1pXdGJoZkdRLTlIb0plSHZjUHNmNjdnSUFlTUFWMXU0OVo2d2NiVGZiQ0oxdzV6OHp4VXAzMWc2NjE4eG9wUFpFbTZxM0hmS0NoeHdxY0luZWZDb01zZkxadHpIU1YtQmg3MDF6dzhwUkctZDBJTV9wSjJUVlNGTnRERFg1LU1sazQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SYY** | **21.75** | **9.95** | **11.62** | **2.80** | **40,252,977,152.00 USD** | **10.84** |
| USFD | 31.19 | 5.53 | 15.38 | 2.10 | 23,972,483,072.00 USD | 41.56 |
| PFGC | 44.16 | 3.42 | 14.38 | 5.50 | 17,488,836,608.00 USD | 14.75 |
| CHEF | 43.42 | 6.01 | 18.87 | 11.20 | 4,396,706,816.00 USD | 62.79 |

Peers fetched as_of: 2026-11-26; SYY reuses existing data (market data as_of: 2026-11-25); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-03
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-26

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

- https://news.google.com/rss/articles/CBMigAFBVV95cUxNc0dpMk9nVXpCTmlObVBJYTRvTDM1VGo5dEY5Njk1U3BGYjlDRXdKdURsdGtzWUJrZUI2M3FOUjJYNXVOZmlmb3JmSG9lMFBueElNdHNOcXJqd1U2U25jS0hoVmNnQVcwTVhkek1hbUxhdWI5ZEQwUU56RDBQck9WQw?oc=5
- https://news.google.com/rss/articles/CBMidEFVX3lxTE9vNlVEb2duRldOdDMtdTFFRXgwVTVndDNQbXg4LXhWUTUzLVBxSFhmeUpKSWpzSk9lVzJNSm9FZjdEYTZ5MDktSFlGdUtPdVJGU3Y4Zlc1Tjh0d0N1bTdiZWlxQngwaHhIS01rQzd4MmRacmxy?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxPN1R0eW93RTR3MThNbDlZUXRkX0JLanF1SkJFNmwxcTNXb05kWHZXTzYxRmthVmVXSkk4YURucW9LS0o3U05vOE5Iei1YTzlvLXpQaVo4TDlMb3o3T1hsc3RiU21mWk9neVpJdl9RNUloNWNILTdiTG5BQi1YTnNYZ04wSFd5OXZxOHRvc0xUMXFTSER3Skh0bXctaUlHSzYyV2N6ZExfYm5EQklJNHFWVWxYV1Boa3R0M0hkNmNJT3dQUXpBMkt5TQ?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxQLTNFSXZIYk8zNmZ4el9KRWgxenZVT2dfMUtoVFRQUFdRS3VFOWVKSV9OS1pXdGJoZkdRLTlIb0plSHZjUHNmNjdnSUFlTUFWMXU0OVo2d2NiVGZiQ0oxdzV6OHp4VXAzMWc2NjE4eG9wUFpFbTZxM0hmS0NoeHdxY0luZWZDb01zZkxadHpIU1YtQmg3MDF6dzhwUkctZDBJTV9wSjJUVlNGTnRERFg1LU1sazQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
