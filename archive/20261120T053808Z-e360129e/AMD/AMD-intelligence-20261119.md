# AMD Intelligence Report

- ticker: **AMD**
- Report as_of: **2026-11-19**
- Market data as_of: **2026-11-19**
- Quant sources: https://finance.yahoo.com/quote/AMD/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMD/key-statistics/
- AI analysis snapshot as_of: **2026-11-19**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-20T06:00:28.664668+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 1, 'ai': 6, 'unknown': 0, 'irrelevant': 16})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261119T054856Z-9eb86811/AMD** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'negative_sentiment_in_tailwinds': 1}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 14 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 39.13%; oldest publication 2026-11-16

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 489.1900 |
| Return 1D (%) | -7.7244 |
| Return 1W (%) | -16.4206 |
| Return 1M (%) | -9.0809 |
| Return YTD (%) | 128.4227 |
| Return 1Y (%) | 118.8280 |
| Annualized volatility (%) | 73.9940 |
| Beta vs SPY | 3.4281 |
| Max drawdown (%) | -37.7290 |
| Sharpe (rf=0) | 1.4327 |
| Downside deviation (rf=0, %) | 48.3507 |
| Sortino (rf=0) | 2.1926 |
| Historical VaR 95% (1D, %) | 6.9676 |
| Historical ES 95% (1D, %) | 9.7114 |
| Correlation vs SPY | 0.6439 |
| Tracking error vs SPY (%) | 65.9073 |
| P/E (trailing) | 113.24 |
| P/B | 11.73 |
| EV/EBITDA | 71.41 |
| Revenue growth (%) | 44.70 |
| Forward P/E (estimate) | 27.73 |
| Gross margin (%) | 56.00 |
| Operating margin (%) | 17.82 |
| Return on equity (%) | 11.96 |
| Free cash flow yield (%) | 0.91 |
| MA50 | 554.9324 |
| Close vs MA50 (%) | -11.8469 |
| MA200 | 428.6267 |
| Close vs MA200 (%) | 14.1296 |
| RSI (14, Wilder) | 45.1559 |
| MACD (12,26) | -9.8282 |
| MACD signal (9) | -11.9557 |
| MACD histogram | 2.1275 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMD': 286, 'SPY': 286}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 489.1900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -7.7244 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -16.4206 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -9.0809 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 128.4227 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 118.8280 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 73.9940 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 48.3507 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.1926 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 6.9676 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 9.7114 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6439 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 65.9073 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.4281 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -37.7290 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.4327 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 27.7346 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 56.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 17.8210 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 11.9600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.9087 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 113.2384 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 45.1559 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 2.1275 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -11.8469 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 14.1296 -> Clearly above the moving-average trend level.

## TAILWINDS

### Why AMD Stock Was Sliding Today
- Summary: AMD shares fell today, indicating short-term weakness for the company.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNb2ctVEw4Q2ZFLXlpc2ZpeUFwaS0xSDI2Q2tRc2dtMzJmaGJwZjNoakZiTGxZVDhXUUJsWjRwR0dFamttd25sZWk4b0h6bDJZa3llbFE0YV9ub3NfbnItZ0xRejR0MzZoSy02bzh5bXVGWHJBLXVsQjN3ZHhmOXRWQlZJSEtONzQ5cXpsX0dxTGtuZWpnTDBn?oc=5>

### AMD (AMD) Stock Could Be 12% Undervalued After AI Chip Progress News
- Summary: AI chip progress suggests AMD may be undervalued by 12%.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMie0FVX3lxTFBnUU5wSm1najNrS3pqZDAxUlQyOHVtaGFBdnBBQlNUUmlobG9XT290d2Zha2ppSVgtU2E5amhwSHFTRkZ5RzV1ZXJnYmNHTGFET0JmeHZVVWthbm5nbF9HR181djRCZkQtQVVvdHNxU1RZcWlCZW5VQktoVQ?oc=5>

## HEADWINDS

### Is NVIDIA’s Turmoil Advanced Micro Devices’ (AMD) Biggest Opening Yet?
- Summary: Nvidia turmoil may negatively impact AMD’s market performance.
- Date: 2026-11-17 | Impact: low | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPeE4zN25uZ3h5c01LT2hKdFVrSncwaTlUWXpTUmNKZnpBZnB6b01JQTFIaW9IRms3NFVMS1lTLWZPNWVFajh5Vl90WXdjdEwxX29aTWhjLWtLeExZelZXRkpaZmV3VzVzakN2VzgwRjFkbi1BZkVESTlXZGx5d05LYm1SNnZRdlRhUW9NQ2d6UEh1R05TRFA0Q1MxcmJ6LXFmclRVbg?oc=5>

### First Nvidia, Now AMD: A Short Seller Just Put Its China Business Under the Microscope
- Summary: Short seller targets AMD’s China business, indicating potential downside pressure.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNd2V1VjBYTHAxeHRjWWtjOFk0ejRqY3VwdjZ6MmVPZHFvSmZDb0ItTnR5WHBGWEhwNEIteEpHYUFvUXozSndzbHkzcWxzZ1JscDdZSkI1aDZpNlRaVWF3dlpoNVF5b1BTVXVuVDkxQlFnb1JCakRtUWo2UUxKbElIemZnTV9wQ2x2UVJjcHVGd1l1V0VlVFE?oc=5>

## CATALYSTS

### Advanced Micro Devices (AMD) Closes $8.2 Billion World Labs Acquisition
- Summary: Advanced Micro Devices (AMD) Closes $8.2 Billion World Labs Acquisition
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxQZkNtckk5TW0wbDQzTkxSU3JQNVJROTBBdE5OMjlyWDZMcHR5VE1BemMxOFZxSXNZR2dQS2JNWDRSN2VJYkxDU1FTLVlielg5SW5IOXdibDEzcmNzZU16ekxGNkhoWDRnX0xRcWVzaFBpUmpRMFRmSllnM2pfaGRzYWFXSl9nRmlzUUE?oc=5>

### Why Is Advanced Micro Devices Stock Rising Today?
- Summary: Explores reasons behind AMD's recent price increase.
- Date: 2026-11-18 | Impact: low | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPUkNPRlQ0VWdjd0dOeVdRWVVDZlUwOTg0YkFDRE9UXzJHOWFuVEVFMmIwU2xOSl9Ibi1vMTFPX0liLU80SzdaeVdWLTgtamhuSS1nMlV6QjZBMVN2N1ZjN2xqYmR3NHlWYm5kY1l6a0lQUGo1UVdycjNhbzV5cmZjYlRGNGxvTVpDRXpRMGpRWkxkaVA1bm9KcTBBaTg4QQ?oc=5>

### AMD Shares Slump After Shortseller Raises China Concerns
- Summary: Shortseller’s China concerns triggered a sharp decline in AMD shares.
- Date: 2026-11-19 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxPbkp6di1ZYkMzQlhjTmkxbHFwNzIzLWMyc3NKXzBqSV9hZ05wODRRYUhjYl9pSmIyNENPaHpXWmlScUpaYXhfT3AyQ1hKYVhWZnhHRVp1a0g2dkVGWmpYa2lXdmdjaE1TUTQwbFlyNjJVNjVkRmlIbWt3WHhWYjNJWXNGSG9RcFkwYUFRZzdYMVNpQXVnZllfU0ZlZEc0QnFsQ1RnWk9tUmc5d2luUVVSaWRKMA?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMD** | **113.24** | **11.73** | **71.41** | **44.70** | **809,641,574,400.00 USD** | **118.83** |
| NVDA | 15.68 | 13.20 | 14.22 | 103.20 | 3,524,978,802,688.00 USD | -21.55 |
| INTC | N/A | 2.57 | 16.14 | 20.90 | 296,151,810,048.00 USD | 58.70 |
| AVGO | 44.27 | 16.60 | 32.34 | 85.50 | 1,654,778,757,120.00 USD | -1.47 |

Peers fetched as_of: 2026-11-19; AMD reuses existing data (market data as_of: 2026-11-19); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-03
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-19

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 1,584,000,000.00 USD; period 2017-07-02/2017-09-30; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 2,428,000,000.00 USD; period 2026-06-28/2026-09-26; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMilwFBVV95cUxNb2ctVEw4Q2ZFLXlpc2ZpeUFwaS0xSDI2Q2tRc2dtMzJmaGJwZjNoakZiTGxZVDhXUUJsWjRwR0dFamttd25sZWk4b0h6bDJZa3llbFE0YV9ub3NfbnItZ0xRejR0MzZoSy02bzh5bXVGWHJBLXVsQjN3ZHhmOXRWQlZJSEtONzQ5cXpsX0dxTGtuZWpnTDBn?oc=5
- https://news.google.com/rss/articles/CBMie0FVX3lxTFBnUU5wSm1najNrS3pqZDAxUlQyOHVtaGFBdnBBQlNUUmlobG9XT290d2Zha2ppSVgtU2E5amhwSHFTRkZ5RzV1ZXJnYmNHTGFET0JmeHZVVWthbm5nbF9HR181djRCZkQtQVVvdHNxU1RZcWlCZW5VQktoVQ?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPeE4zN25uZ3h5c01LT2hKdFVrSncwaTlUWXpTUmNKZnpBZnB6b01JQTFIaW9IRms3NFVMS1lTLWZPNWVFajh5Vl90WXdjdEwxX29aTWhjLWtLeExZelZXRkpaZmV3VzVzakN2VzgwRjFkbi1BZkVESTlXZGx5d05LYm1SNnZRdlRhUW9NQ2d6UEh1R05TRFA0Q1MxcmJ6LXFmclRVbg?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNd2V1VjBYTHAxeHRjWWtjOFk0ejRqY3VwdjZ6MmVPZHFvSmZDb0ItTnR5WHBGWEhwNEIteEpHYUFvUXozSndzbHkzcWxzZ1JscDdZSkI1aDZpNlRaVWF3dlpoNVF5b1BTVXVuVDkxQlFnb1JCakRtUWo2UUxKbElIemZnTV9wQ2x2UVJjcHVGd1l1V0VlVFE?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxQZkNtckk5TW0wbDQzTkxSU3JQNVJROTBBdE5OMjlyWDZMcHR5VE1BemMxOFZxSXNZR2dQS2JNWDRSN2VJYkxDU1FTLVlielg5SW5IOXdibDEzcmNzZU16ekxGNkhoWDRnX0xRcWVzaFBpUmpRMFRmSllnM2pfaGRzYWFXSl9nRmlzUUE?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPUkNPRlQ0VWdjd0dOeVdRWVVDZlUwOTg0YkFDRE9UXzJHOWFuVEVFMmIwU2xOSl9Ibi1vMTFPX0liLU80SzdaeVdWLTgtamhuSS1nMlV6QjZBMVN2N1ZjN2xqYmR3NHlWYm5kY1l6a0lQUGo1UVdycjNhbzV5cmZjYlRGNGxvTVpDRXpRMGpRWkxkaVA1bm9KcTBBaTg4QQ?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxPbkp6di1ZYkMzQlhjTmkxbHFwNzIzLWMyc3NKXzBqSV9hZ05wODRRYUhjYl9pSmIyNENPaHpXWmlScUpaYXhfT3AyQ1hKYVhWZnhHRVp1a0g2dkVGWmpYa2lXdmdjaE1TUTQwbFlyNjJVNjVkRmlIbWt3WHhWYjNJWXNGSG9RcFkwYUFRZzdYMVNpQXVnZllfU0ZlZEc0QnFsQ1RnWk9tUmc5d2luUVVSaWRKMA?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
