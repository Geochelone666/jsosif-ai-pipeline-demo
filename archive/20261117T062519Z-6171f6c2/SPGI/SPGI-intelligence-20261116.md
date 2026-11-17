# SPGI Intelligence Report

- ticker: **SPGI**
- Report as_of: **2026-11-16**
- Market data as_of: **2026-11-16**
- Quant sources: https://finance.yahoo.com/quote/SPGI/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SPGI/key-statistics/
- AI analysis snapshot as_of: **2026-11-16**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-17T06:40:41.333825+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 8, 'rule': 1, 'ai': 4, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261116T043911Z-b81cfeb4/SPGI** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 8 unique headlines; 4 named publishers; 0 exact duplicates; 8 HTTPS source links; largest publisher share 50.0%; oldest publication 2026-11-09

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 471.5900 |
| Return 1D (%) | -0.4223 |
| Return 1W (%) | 0.1061 |
| Return 1M (%) | 9.7640 |
| Return YTD (%) | -3.9559 |
| Return 1Y (%) | 1.8230 |
| Annualized volatility (%) | 30.9520 |
| Beta vs SPY | 0.3638 |
| Max drawdown (%) | -28.4781 |
| Sharpe (rf=0) | 0.2479 |
| Downside deviation (rf=0, %) | 23.0690 |
| Sortino (rf=0) | 0.3327 |
| Historical VaR 95% (1D, %) | 2.8767 |
| Historical ES 95% (1D, %) | 4.6345 |
| Correlation vs SPY | 0.1618 |
| Tracking error vs SPY (%) | 31.7753 |
| P/E (trailing) | 28.17 |
| P/B | 6.94 |
| EV/EBITDA | 18.25 |
| Revenue growth (%) | 6.80 |
| Forward P/E (estimate) | 23.38 |
| Gross margin (%) | 70.99 |
| Operating margin (%) | 44.09 |
| Return on equity (%) | 17.88 |
| Free cash flow yield (%) | 4.42 |
| MA50 | 429.1254 |
| Close vs MA50 (%) | 9.8956 |
| MA200 | 414.1884 |
| Close vs MA200 (%) | 13.8588 |
| RSI (14, Wilder) | 62.6712 |
| MACD (12,26) | 13.0696 |
| MACD signal (9) | 14.0388 |
| MACD histogram | -0.9692 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SPGI': 283, 'SPY': 283}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 471.5900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.4223 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.1061 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 9.7640 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -3.9559 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 1.8230 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 30.9520 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 23.0690 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.3327 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8767 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.6345 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1618 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.7753 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3638 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.4781 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2479 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 23.3752 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 70.9940 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 44.0930 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 17.8760 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.4172 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 28.1714 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 62.6712 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.9692 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 9.8956 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 13.8588 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### S&P Global (SPGI) Stock Trades At A Premium To Its Earnings Power
- Summary: S&P Global (SPGI) Stock Trades At A Premium To Its Earnings Power
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQSkk4Z0g1VkNPLUhfbm9CQ3hxSWNlMnVQMndvemY2S1F0bUdmdVJMczl1R0lpcVU5RGg0bU9ZVjA5U05Vb1o2RWRLU2JXUU5QdGd1MXZxOHZzdklCdW81ZzhpcHBpeWVvbGk4eGoyY3dqTHhFTW84Mlk2Z3JZZk04SXNYLV9BU3pORWotR3M2aVlIYlZ0anc?oc=5>

### S&P Global (SPGI) Is Reviewing A Separation Of Capital IQ
- Summary: Capital IQ separation could reshape business structure and focus.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQZ3lTZHM1bDZHRHVhZzlGTXBpYkZSX1JQTzF6WVJPR0toek9mVks0MWRrSkxxZ1FCZlVXSW5TUjBGMnZueXRObWxHYVBHN3FBQ29kMFVGbTN0bXJzUEhpZlIzTDdNQnktLXNWMFZ0VUkxMG8zMkg2MlNtVThPVG96dnFGNkswVlRwY2x6VEZfbFpRVlRUMlpncm1XS3NVWWFl?oc=5>

### S&P Global Announces Public Offering of Senior Notes
- Summary: S&P Global plans to issue new senior notes, expanding its debt capacity.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxNc1lLdFdJbjFRXzBkaS1xa3dqdE9uVFlVcDBYQXlOX1FaWEtaWFB2dHBjb19BanRDSUlRODdEcFNQNGY3QU1tQzY0TTJTelZyemEzZklZMHVVWFM5cXVDVngxUGF4RGJlYWhTcEdvQXA4ZWFwY3ZOMWlvNkJkOEN2ZktRVTFFS3FpSUdyT0JzdE1tNjJWVVg3ZmtXTFB6MFo2Wktr?oc=5>

### New S&P Global (SPGI) notes won't be exchange-listed; no public market currently exists.
- Summary: The new notes lack an exchange listing, limiting immediate market liquidity.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxQMXQ1NkxjTkxyOEU2Wk9HU0hCcnVqZTNiQUpiWWxldmRhaXVudVIzcDFraG5tLTRzaU5sWW9YNUtaZ2VfUFVnaDZoN3VEUWVhVGVtZmEzb1ZFLVpmX0I1Y3JNN2g3QTE2cDZlaERhZVV0bG5pVXZHWXA0Uk0wV3BkWTNxdEZKbHZEM1hWVWMzejBpVTRSSUNHMjNVdEs1VlpBX3RkZy1TWQ?oc=5>

## RISKS

### A $650 million S&P Global bond issue comes due in 2036.
- Summary: A $650M bond matures in 2036, affecting future cash flows.
- Date: 2026-11-16 | Impact: low | Horizon: long | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxQRk1lNnpvWnprc0lKSUtXQkhscklWRTlnbmpPbkNpSTJ2bTdXSmVOelVLYjVHdi1sTms0UlNHUTNOVHVNb2RSYXNQZ3VvUVFBdEpYcmpqM3ZRX3RsVlAwaHkyaWtXTVZnQkc1NUlyank4R2kxZEM4NWxqQmQ5UUFHVUVKc1JDQ3hBOWpGUmFITGRpdDg0SGdWaGhVVGVvWUF2eVZERWJyWFZiUUFJdURHVm42eFZtWWNm?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SPGI** | **28.17** | **6.94** | **18.25** | **6.80** | **136,713,936,896.00 USD** | **1.82** |
| MCO | 30.89 | 26.71 | 23.08 | 0.80 | 87,294,861,312.00 USD | 6.51 |
| MSCI | 35.14 | -15.79 | 26.82 | 12.40 | 47,511,035,904.00 USD | 19.27 |
| FDS | 22.80 | 5.85 | 14.43 | 6.30 | 11,710,872,576.00 USD | 23.44 |

Peers fetched as_of: 2026-11-16; SPGI reuses existing data (market data as_of: 2026-11-16); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-27
- Next expected earnings: 2027-02-09 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-16

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-28
- Revenue (latest available single quarter): 1,567,000,000.00 USD; period 2018-01-01/2018-03-31; fiscal year/reporting period 2018/Q1
- Net income (latest available single quarter): 1,240,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/64040/000006404026000058/spgi-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMilgFBVV95cUxQSkk4Z0g1VkNPLUhfbm9CQ3hxSWNlMnVQMndvemY2S1F0bUdmdVJMczl1R0lpcVU5RGg0bU9ZVjA5U05Vb1o2RWRLU2JXUU5QdGd1MXZxOHZzdklCdW81ZzhpcHBpeWVvbGk4eGoyY3dqTHhFTW84Mlk2Z3JZZk04SXNYLV9BU3pORWotR3M2aVlIYlZ0anc?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQZ3lTZHM1bDZHRHVhZzlGTXBpYkZSX1JQTzF6WVJPR0toek9mVks0MWRrSkxxZ1FCZlVXSW5TUjBGMnZueXRObWxHYVBHN3FBQ29kMFVGbTN0bXJzUEhpZlIzTDdNQnktLXNWMFZ0VUkxMG8zMkg2MlNtVThPVG96dnFGNkswVlRwY2x6VEZfbFpRVlRUMlpncm1XS3NVWWFl?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxNc1lLdFdJbjFRXzBkaS1xa3dqdE9uVFlVcDBYQXlOX1FaWEtaWFB2dHBjb19BanRDSUlRODdEcFNQNGY3QU1tQzY0TTJTelZyemEzZklZMHVVWFM5cXVDVngxUGF4RGJlYWhTcEdvQXA4ZWFwY3ZOMWlvNkJkOEN2ZktRVTFFS3FpSUdyT0JzdE1tNjJWVVg3ZmtXTFB6MFo2Wktr?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxQMXQ1NkxjTkxyOEU2Wk9HU0hCcnVqZTNiQUpiWWxldmRhaXVudVIzcDFraG5tLTRzaU5sWW9YNUtaZ2VfUFVnaDZoN3VEUWVhVGVtZmEzb1ZFLVpmX0I1Y3JNN2g3QTE2cDZlaERhZVV0bG5pVXZHWXA0Uk0wV3BkWTNxdEZKbHZEM1hWVWMzejBpVTRSSUNHMjNVdEs1VlpBX3RkZy1TWQ?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxQRk1lNnpvWnprc0lKSUtXQkhscklWRTlnbmpPbkNpSTJ2bTdXSmVOelVLYjVHdi1sTms0UlNHUTNOVHVNb2RSYXNQZ3VvUVFBdEpYcmpqM3ZRX3RsVlAwaHkyaWtXTVZnQkc1NUlyank4R2kxZEM4NWxqQmQ5UUFHVUVKc1JDQ3hBOWpGUmFITGRpdDg0SGdWaGhVVGVvWUF2eVZERWJyWFZiUUFJdURHVm42eFZtWWNm?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
