# ISRG Intelligence Report

- ticker: **ISRG**
- Report as_of: **2026-11-14**
- Market data as_of: **2026-11-13**
- Quant sources: https://finance.yahoo.com/quote/ISRG/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ISRG/key-statistics/
- AI analysis snapshot as_of: **2026-11-14**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-15T04:59:59.090592+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 3, 'rule': 2, 'ai': 0, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 3 unique headlines; 3 named publishers; 0 exact duplicates; 3 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-11-09

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 443.5900 |
| Return 1D (%) | 0.8411 |
| Return 1W (%) | -2.0340 |
| Return 1M (%) | 5.1012 |
| Return YTD (%) | -21.6770 |
| Return 1Y (%) | -21.5593 |
| Annualized volatility (%) | 35.5675 |
| Beta vs SPY | 0.9111 |
| Max drawdown (%) | -43.9960 |
| Sharpe (rf=0) | -0.5058 |
| Downside deviation (rf=0, %) | 26.3356 |
| Sortino (rf=0) | -0.6831 |
| Historical VaR 95% (1D, %) | 3.2143 |
| Historical ES 95% (1D, %) | 5.1297 |
| Correlation vs SPY | 0.3492 |
| Tracking error vs SPY (%) | 33.3502 |
| P/E (trailing) | 53.64 |
| P/B | 9.62 |
| EV/EBITDA | 33.52 |
| Revenue growth (%) | 21.70 |
| Forward P/E (estimate) | 35.58 |
| Gross margin (%) | 66.64 |
| Operating margin (%) | 31.70 |
| Return on equity (%) | 17.93 |
| Free cash flow yield (%) | 2.23 |
| MA50 | 417.5936 |
| Close vs MA50 (%) | 6.2253 |
| MA200 | 429.3807 |
| Close vs MA200 (%) | 3.3093 |
| RSI (14, Wilder) | 52.0777 |
| MACD (12,26) | 8.4543 |
| MACD signal (9) | 11.2069 |
| MACD histogram | -2.7526 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ISRG': 282, 'SPY': 282}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 443.5900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.8411 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.0340 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 5.1012 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -21.6770 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -21.5593 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 35.5675 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.3356 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.6831 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.2143 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1297 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3492 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 33.3502 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.9111 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -43.9960 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.5058 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 35.5761 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 66.6420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 31.7020 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 17.9320 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.2338 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 53.6384 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 52.0777 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -2.7526 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 6.2253 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 3.3093 -> Slightly above the moving-average trend level.

## TAILWINDS

### Intuitive Surgical price target raised to $500 from $470 at BofA
- Summary: Intuitive Surgical price target raised to $500 from $470 at BofA
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxQVHU5UEh1ckhOS3VzSVVZb0czZU1WdXpKa1Nkd2I1NEpFZC1zMkRMQnpESWZ5UUdzb0VkQU9RUVlsRTJkMl9adTIzTzBCbzkwclhnc2UwczAzaTQzaHBXNk85TGZWNF92eU5mY0V3UVhLX2xES1NpckZfTHA2R0szODRiV19xWlVjVGY4NlNmOXdxUXhJMU9Obk1fTnliOFpLWmJ2RUNmVG5QVGhJTFZHSkNn?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Intuitive Surgical (ISRG) Just Grew Revenue 22%. Why Is the Stock Still Down This Year?
- Summary: Intuitive Surgical (ISRG) Just Grew Revenue 22%. Why Is the Stock Still Down This Year?
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOV1JDa3pWOXNYTDdmclZzOG0yMVlIUElneWlQU05HbzZKQWdTdHZrVlZaaVhtMFcwT1RoUjMzaVdQY2tYeThqXzEtNWxNZGxZNUFDbEhCOU5WeFptd3ltY2lmTTVBR3NnLXlnS2RwUFNpUkJPVXBTQ1d2Zk5jWFJfLVYxelNTcFV1ajA0RDh6cjhLbm5ISkRsLWxQN29xb3M?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ISRG** | **53.64** | **9.62** | **33.52** | **21.70** | **153,767,690,240.00 USD** | **-21.56** |
| MDT | 25.27 | 2.62 | 14.58 | 13.70 | 131,572,129,792.00 USD | 10.54 |
| SYK | 32.98 | 5.03 | 17.32 | 7.60 | 117,877,170,176.00 USD | -16.16 |
| BSX | 18.71 | 2.51 | 13.62 | 1.40 | 64,269,643,776.00 USD | -57.76 |

Peers fetched as_of: 2026-11-14; ISRG reuses existing data (market data as_of: 2026-11-13); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-20
- Next expected earnings: 2027-01-21 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-14

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 3,048,700,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 522,800,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1035267/000103526726000071/isrg-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMisgFBVV95cUxQVHU5UEh1ckhOS3VzSVVZb0czZU1WdXpKa1Nkd2I1NEpFZC1zMkRMQnpESWZ5UUdzb0VkQU9RUVlsRTJkMl9adTIzTzBCbzkwclhnc2UwczAzaTQzaHBXNk85TGZWNF92eU5mY0V3UVhLX2xES1NpckZfTHA2R0szODRiV19xWlVjVGY4NlNmOXdxUXhJMU9Obk1fTnliOFpLWmJ2RUNmVG5QVGhJTFZHSkNn?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOV1JDa3pWOXNYTDdmclZzOG0yMVlIUElneWlQU05HbzZKQWdTdHZrVlZaaVhtMFcwT1RoUjMzaVdQY2tYeThqXzEtNWxNZGxZNUFDbEhCOU5WeFptd3ltY2lmTTVBR3NnLXlnS2RwUFNpUkJPVXBTQ1d2Zk5jWFJfLVYxelNTcFV1ajA0RDh6cjhLbm5ISkRsLWxQN29xb3M?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
