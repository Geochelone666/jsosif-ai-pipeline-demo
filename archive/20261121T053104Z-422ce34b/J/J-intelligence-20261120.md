# J Intelligence Report

- ticker: **J**
- Report as_of: **2026-11-20**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/J/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/J/key-statistics/
- AI analysis snapshot as_of: **2026-11-20**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-21T05:53:12.920981+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 7, 'rule': 1, 'ai': 3, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261120T053808Z-e360129e/J** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 7 unique headlines; 6 named publishers; 0 exact duplicates; 7 HTTPS source links; largest publisher share 28.57%; oldest publication 2026-11-13

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 150.6200 |
| Return 1D (%) | -2.5618 |
| Return 1W (%) | -4.8095 |
| Return 1M (%) | 7.8399 |
| Return YTD (%) | 14.6444 |
| Return 1Y (%) | 17.8483 |
| Annualized volatility (%) | 32.1178 |
| Beta vs SPY | 0.7699 |
| Max drawdown (%) | -28.8516 |
| Sharpe (rf=0) | 0.6744 |
| Downside deviation (rf=0, %) | 22.7478 |
| Sortino (rf=0) | 0.9521 |
| Historical VaR 95% (1D, %) | 2.9549 |
| Historical ES 95% (1D, %) | 4.8028 |
| Correlation vs SPY | 0.3427 |
| Tracking error vs SPY (%) | 30.3520 |
| P/E (trailing) | 50.04 |
| P/B | 5.40 |
| EV/EBITDA | 19.39 |
| Revenue growth (%) | 34.50 |
| Forward P/E (estimate) | 18.29 |
| Gross margin (%) | 22.07 |
| Operating margin (%) | 5.93 |
| Return on equity (%) | 8.00 |
| Free cash flow yield (%) | 3.66 |
| MA50 | 146.3796 |
| Close vs MA50 (%) | 2.8968 |
| MA200 | 134.8016 |
| Close vs MA200 (%) | 11.7346 |
| RSI (14, Wilder) | 47.2418 |
| MACD (12,26) | 2.7037 |
| MACD signal (9) | 3.4955 |
| MACD histogram | -0.7919 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'J': 287, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 150.6200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.5618 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -4.8095 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 7.8399 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 14.6444 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 17.8483 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 32.1178 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 22.7478 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.9521 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9549 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.8028 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3427 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 30.3520 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.7699 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.8516 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.6744 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 18.2860 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 22.0670 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 5.9290 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 7.9980 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 3.6627 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 50.0399 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 47.2418 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.7919 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 2.8968 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 11.7346 -> Clearly above the moving-average trend level.

## TAILWINDS

### Jacobs Solutions (J) Stock Forecast and Price Target 2026 $J
- Summary: Analysts project a 2026 price target for Jacobs Solutions, indicating potential upside for investors.
- Date: 2026-11-13 | Impact: medium | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiX0FVX3lxTFBmTzJ4N00xU3lwTUV2dWRERWh4TXR4S3RLQkwwN21kN01lNVk4NDJYeVExaUFhVk5ZbWNNbFlkX1Via2puX1QxcHhLY3cybHRWa3VwSXNPNGNqdjVGc3Zv?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Jacobs Solutions (J) Lands Sanofi Project Following Questions Over Whether Shares Are Fully Valued
- Summary: Jacobs Solutions (J) Lands Sanofi Project Following Questions Over Whether Shares Are Fully Valued
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQdzIzTGlKLTN0UXBlZzRZaVI1LWtNOERTdjdqZ1RmRTR1Y192TFdyWDRYUWJTeF9vYW5Zb1hJX3JPUzlxR3VyTE02bHJQY3ZhVTZldUt3eGpkRUx6ZTM2YjZRM0daMF9TRmJuWDhfU3FlMXotODV1S1p5X3Vid3J4QWhwNDQ2ay0yLVVyVHVVNVBDbXZmdEFLRVhlTWQ?oc=5>

### Jacobs to Report Q4 Earnings: What to Expect From the Stock?
- Summary: Jacobs Solutions will release Q4 earnings, providing insight into financial performance and guidance for the upcoming quarter.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxOR0hmTWdYV1lWM3FWSDN5enJ0XzFfMUZuWUs3eFpVdXNtQ0RFOC0zZkRIYVY4Q2llVTdtQVZhbFE1akxtV1FoU2VQRnBzREtmbnpxc2g3U0U0Q3ViREdvcmwtVTVqU2FpMmRMMmk4QW5uNTVrVTlCbUViRk9vN0E4UThMMnhYb1B1YkVHQUtmQ082RTBfMjZOSUJpT1NZY2JqUUNrWTRTeGVFcnhoZVVXTG9kQ3Y?oc=5>

### Jacobs (J) Stock May Be A Bargain Despite Fresh Airport Upgrade Wins
- Summary: Jacobs stock appears undervalued amid recent airport upgrade contracts, suggesting potential upside for investors.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPZ3Vlay1FSHB2aVZSN3dOMVRzel9xVWJfV1hvZmwtMmhCQ0FaSkVRS1FydUNqeE83MzduLXgxMDg0QU9KQy16TDhabHpDNUdBc0EyTFR5TmdGS2hjSkNHVy1NbW9iR09OOW5ZMVNZMm5POVFnUjN2Ui12SzlVa3FpX3FjMUhiZTdvUS11WFFjNUhwNFhVcUE?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **J** | **50.04** | **5.40** | **19.39** | **34.50** | **17,628,354,560.00 USD** | **17.85** |
| ACM | 27.69 | 4.62 | 13.21 | -7.10 | 10,130,911,232.00 USD | -24.67 |
| FLR | N/A | 2.20 | 9.31 | 10.50 | 5,590,115,328.00 USD | 7.55 |
| KBR | 9.30 | 2.25 | 9.07 | 5.00 | 3,964,866,560.00 USD | -19.58 |

Peers fetched as_of: 2026-11-20; J reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-04
- Next expected earnings: 2026-11-23 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-20

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-04
- Revenue (latest available single quarter): 4,142,644,000.00 USD; period 2018-06-30/2018-09-28; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 136,553,000.00 USD; period 2026-03-28/2026-06-26; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/52988/000162828026052573/jec-20260626.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiX0FVX3lxTFBmTzJ4N00xU3lwTUV2dWRERWh4TXR4S3RLQkwwN21kN01lNVk4NDJYeVExaUFhVk5ZbWNNbFlkX1Via2puX1QxcHhLY3cybHRWa3VwSXNPNGNqdjVGc3Zv?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQdzIzTGlKLTN0UXBlZzRZaVI1LWtNOERTdjdqZ1RmRTR1Y192TFdyWDRYUWJTeF9vYW5Zb1hJX3JPUzlxR3VyTE02bHJQY3ZhVTZldUt3eGpkRUx6ZTM2YjZRM0daMF9TRmJuWDhfU3FlMXotODV1S1p5X3Vid3J4QWhwNDQ2ay0yLVVyVHVVNVBDbXZmdEFLRVhlTWQ?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxOR0hmTWdYV1lWM3FWSDN5enJ0XzFfMUZuWUs3eFpVdXNtQ0RFOC0zZkRIYVY4Q2llVTdtQVZhbFE1akxtV1FoU2VQRnBzREtmbnpxc2g3U0U0Q3ViREdvcmwtVTVqU2FpMmRMMmk4QW5uNTVrVTlCbUViRk9vN0E4UThMMnhYb1B1YkVHQUtmQ082RTBfMjZOSUJpT1NZY2JqUUNrWTRTeGVFcnhoZVVXTG9kQ3Y?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPZ3Vlay1FSHB2aVZSN3dOMVRzel9xVWJfV1hvZmwtMmhCQ0FaSkVRS1FydUNqeE83MzduLXgxMDg0QU9KQy16TDhabHpDNUdBc0EyTFR5TmdGS2hjSkNHVy1NbW9iR09OOW5ZMVNZMm5POVFnUjN2Ui12SzlVa3FpX3FjMUhiZTdvUS11WFFjNUhwNFhVcUE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
