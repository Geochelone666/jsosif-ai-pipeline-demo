# BMO.TO Intelligence Report

- ticker: **BMO.TO**
- Report as_of: **2026-11-09**
- Market data as_of: **2026-11-09**
- Quant sources: https://finance.yahoo.com/quote/BMO.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/BMO.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-09**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-10T05:59:40.972148+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 6, 'rule': 1, 'ai': 2, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 6 unique headlines; 6 named publishers; 0 exact duplicates; 6 HTTPS source links; largest publisher share 16.67%; oldest publication 2026-11-04

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 245.7800 |
| Return 1D (%) | 1.8060 |
| Return 1W (%) | 1.5494 |
| Return 1M (%) | 6.6344 |
| Return YTD (%) | 42.1978 |
| Return 1Y (%) | 46.1919 |
| Annualized volatility (%) | 19.6411 |
| Beta vs SPY | 0.8514 |
| Max drawdown (%) | -11.4239 |
| Sharpe (rf=0) | 1.9792 |
| Downside deviation (rf=0, %) | 13.3881 |
| Sortino (rf=0) | 2.9036 |
| Historical VaR 95% (1D, %) | 1.9541 |
| Historical ES 95% (1D, %) | 2.6458 |
| Correlation vs SPY | 0.5913 |
| Tracking error vs SPY (%) | 16.1036 |
| P/E (trailing) | 20.40 |
| P/B | 2.02 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 12.00 |
| Forward P/E (estimate) | 14.94 |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 30.50 |
| Return on equity (%) | 10.57 |
| Free cash flow yield (%) | N/A |
| MA50 | 238.2159 |
| Close vs MA50 (%) | 3.1753 |
| MA200 | 220.8668 |
| Close vs MA200 (%) | 11.2797 |
| RSI (14, Wilder) | 58.4121 |
| MACD (12,26) | 1.8892 |
| MACD signal (9) | 1.0668 |
| MACD histogram | 0.8224 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'BMO.TO': 277, 'SPY': 278}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 245.7800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.8060 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.5494 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 6.6344 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 42.1978 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 46.1919 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 19.6411 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 13.3881 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.9036 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.9541 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.6458 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5913 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 16.1036 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.8514 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -11.4239 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.9792 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 14.9361 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 30.4990 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 10.5740 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 20.3967 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 58.4121 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.8224 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 3.1753 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 11.2797 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Bank Of Montreal $BMO Stock: Candriam S.C.A. Cuts Position
- Summary: Bank Of Montreal $BMO Stock: Candriam S.C.A. Cuts Position
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxOT0JZOXlMOU5rellqdGU4NVRidHZjNDFxRUd4dzh2VlpNcXFsYmQ5elpVMXhVR0F6dDBabURoWWgzelpzMWs3MnAxNk5ZMGZnU3hkR09fb1ZZV0FXRjBwbjQ4Vi1EemV2Zmx1Tm14QzJ6Vm00cEdUbkxKTy1HbzlSQktEU3JxcnVRX1ZfQ2J4bUwyZUtCNnUzT1N3WWdNUmZGel90TXlfQ1lockQ2VHFTekpPUmc?oc=5>

### Diamond Estates extends credit facility with BMO to June 2027 By Investing.com
- Summary: Diamond Estates renews its credit line with BMO until June 2027, strengthening the bank’s lending portfolio.
- Date: 2026-11-09 | Impact: medium | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxQNl92ZUpEYkk0cm9UOHZNbUNPdE1yVlhOQ2plNDFTdW9VWVRpTUVTdGZEMFFFb3ppdlp5c1dyZG95VXB4eS0xMWJjS01XV19TWXlRallOX0stRElwdFA5dGw1QnljNVpKTXpSYlEyWW5rZnNZN216QnlQdDBiYXBLXzNDdUZFbmcxM05jemFMNTZLLTczS0VjMEI4eXNLcUE3MFJNSHZReExRckFqSVk3bDh3RmZBa0dObXFDMGZSVQ?oc=5>

### BMO stock: Bank of Montreal sets stage for fiscal 2026 results
- Summary: BMO prepares for fiscal 2026 earnings, signaling upcoming financial disclosures.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxNa09wN1lseFF3V3NyOE5sMU1FX0hKZkhGSEktOGw2UE82TzZkWUVFZHpFWjZMYWVjakhHYWlobXp3RVRfZkJ3dHoxdzhzU1RudEt1SmEwaE54THAyenJrZnFqYlNtX0RFXzN4bHRsWFhlMEtKd2NMU2F0bU0zT25YeHZrenRsWll5SEVyY05OdXc0S3psT05xZTFjMTBoejQzd21mTzZfWERPM18yMXAxSm94cGVnMXZmTVpxMUMySnZJdw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **BMO.TO** | **20.40** | **2.02** | **N/A** | **12.00** | **170,839,769,088.00 CAD** | **46.19** |
| RY.TO | 18.45 | 2.98 | N/A | 8.90 | 399,158,804,480.00 CAD | 45.07 |
| TD.TO | 19.08 | 2.32 | N/A | 11.50 | 286,643,421,184.00 CAD | 59.20 |
| BNS.TO | 17.52 | 1.80 | N/A | 11.70 | 160,605,224,960.00 CAD | 46.65 |

Peers fetched as_of: 2026-11-09; BMO.TO reuses existing data (market data as_of: 2026-11-09); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-25
- Next expected earnings: 2026-12-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-09

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMitAFBVV95cUxOT0JZOXlMOU5rellqdGU4NVRidHZjNDFxRUd4dzh2VlpNcXFsYmQ5elpVMXhVR0F6dDBabURoWWgzelpzMWs3MnAxNk5ZMGZnU3hkR09fb1ZZV0FXRjBwbjQ4Vi1EemV2Zmx1Tm14QzJ6Vm00cEdUbkxKTy1HbzlSQktEU3JxcnVRX1ZfQ2J4bUwyZUtCNnUzT1N3WWdNUmZGel90TXlfQ1lockQ2VHFTekpPUmc?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxQNl92ZUpEYkk0cm9UOHZNbUNPdE1yVlhOQ2plNDFTdW9VWVRpTUVTdGZEMFFFb3ppdlp5c1dyZG95VXB4eS0xMWJjS01XV19TWXlRallOX0stRElwdFA5dGw1QnljNVpKTXpSYlEyWW5rZnNZN216QnlQdDBiYXBLXzNDdUZFbmcxM05jemFMNTZLLTczS0VjMEI4eXNLcUE3MFJNSHZReExRckFqSVk3bDh3RmZBa0dObXFDMGZSVQ?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxNa09wN1lseFF3V3NyOE5sMU1FX0hKZkhGSEktOGw2UE82TzZkWUVFZHpFWjZMYWVjakhHYWlobXp3RVRfZkJ3dHoxdzhzU1RudEt1SmEwaE54THAyenJrZnFqYlNtX0RFXzN4bHRsWFhlMEtKd2NMU2F0bU0zT25YeHZrenRsWll5SEVyY05OdXc0S3psT05xZTFjMTBoejQzd21mTzZfWERPM18yMXAxSm94cGVnMXZmTVpxMUMySnZJdw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
