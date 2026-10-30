# SYY Intelligence Report

- ticker: **SYY**
- Report as_of: **2026-10-29**
- Market data as_of: **2026-10-29**
- Quant sources: https://finance.yahoo.com/quote/SYY/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SYY/key-statistics/
- AI analysis snapshot as_of: **2026-10-29**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-30T02:35:43.447580+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 4, 'rule': 1, 'ai': 2, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261029T020157Z-688a53f0/SYY** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 4 unique headlines; 3 named publishers; 0 exact duplicates; 4 HTTPS source links; largest publisher share 50.0%; oldest publication 2026-10-27

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 82.5200 |
| Return 1D (%) | 0.4504 |
| Return 1W (%) | -1.7268 |
| Return 1M (%) | 5.8832 |
| Return YTD (%) | 15.2280 |
| Return 1Y (%) | 14.2974 |
| Annualized volatility (%) | 27.3354 |
| Beta vs SPY | 0.1514 |
| Max drawdown (%) | -23.9798 |
| Sharpe (rf=0) | 0.6306 |
| Downside deviation (rf=0, %) | 20.2333 |
| Sortino (rf=0) | 0.8519 |
| Historical VaR 95% (1D, %) | 2.1089 |
| Historical ES 95% (1D, %) | 3.7604 |
| Correlation vs SPY | 0.0704 |
| Tracking error vs SPY (%) | 29.3233 |
| P/E (trailing) | 22.55 |
| P/B | 14.81 |
| EV/EBITDA | 11.75 |
| Revenue growth (%) | 4.70 |
| Forward P/E (estimate) | 15.32 |
| Gross margin (%) | 18.50 |
| Operating margin (%) | 4.84 |
| Return on equity (%) | 77.69 |
| Free cash flow yield (%) | 4.72 |
| MA50 | 80.2053 |
| Close vs MA50 (%) | 2.8860 |
| MA200 | 79.4744 |
| Close vs MA200 (%) | 3.8322 |
| RSI (14, Wilder) | 58.1906 |
| MACD (12,26) | 0.9019 |
| MACD signal (9) | 0.6822 |
| MACD histogram | 0.2197 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SYY': 271, 'SPY': 271}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 82.5200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.4504 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.7268 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 5.8832 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 15.2280 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 14.2974 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 27.3354 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 20.2333 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.8519 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.1089 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.7604 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0704 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 29.3233 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.1514 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -23.9798 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.6306 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.3217 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 18.4960 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 4.8450 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 77.6920 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.7151 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 22.5464 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 58.1906 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.2197 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 2.8860 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 3.8322 -> Slightly above the moving-average trend level.

## TAILWINDS

### Sysco (SYY) Stock May Look Reasonable As Its 34% Run Continues
- Summary: Sysco’s stock continues a 34% run, suggesting potential value for investors.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxONE9XTDdrQVZHa2RabTFUQ21rZnh5WW5JRm15NTJJNjdjNENaQ0x6bF9JSm02aDRDMFEwQmJRcEV6Q1J3YlYyMU1aT2VKSEpOeHdhTklEZmRzajdjOEdIampQSzdMdE1DTHE2eUJsYjJlbXpMRWgzcHFhdTRkMGg4QnU3Nzd2NFJIbGNGM3h2RUdIRUV1M3BBMF9CTm9CblRtUjRQdDkycFFLeG9BM1o3Zm42VTY5WmNPb0lYWmZyallMSTdJMjYxeUNB0gHPAUFVX3lxTE1mYXVvbVFFaTJWZ2xxZmJwRnlyclBKRVNubFBNYWRVRXF1a05OTFFsa29SWi03ekpNM1VXZlJRUmgtQVR0WjN2ZksxRTlPV0dzYlRzWjhfRERBWV8yMzVFS19tczloVGlIUEwtZUZVTjV3LVFVMTV2VGI5clRPN1lpQTdCRkRfYjlKOWs2aWJmVDg4VDlmN1ZUTjFIMERvdW45azFvWk4yMHVxenhYX2E3bUVlSS1ZMEZvTkdQTjBlVlluamJoWVdOcWhoWnQ4MA?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Sysco Earnings Preview: High Debt Levels Overshadow Everything (NYSE:SYY)
- Summary: Sysco Earnings Preview: High Debt Levels Overshadow Everything (NYSE:SYY)
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxOMllybjY0dGtTSEJqNE5sVm84Z3U2OUtFZlkzZVhvTXdwelpPYkNiUzU4dF95VkltejhzcGpTSkZPQUZ4RDIzZERkcW1lV0ViSEZnbXJXQ3V1bXRWa1pmcV9sbm0tbVdUMmZoYkN6d1BXUHRrOWRMbHRqRkdBaUZ6SmJDQm43YUZrNmtPdmJ0NEdVQnNSbkVSNWRSbC1FcVhYSHVVRg?oc=5>

### Sysco (SYY) Earnings Expected to Grow: Should You Buy?
- Summary: Sysco forecasts higher earnings, suggesting potential upside for investors.
- Date: 2026-10-27 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPQW1hNVdrVXZzS0w1OG5NYmhxN3BvdkFTak5UNm53cGdkRkc5a0NzZnIzaE11MGRaQnVlMURGQWJwSmZjNHVobU42V2UwSWxhSHRtb094RE1wLWJ1YmxmS2xJcDBjWHVvUlBqd3NnQ096Y1hlcFQzN2VKRkxMbGFCaTZBZzJFZGtBM05BRFIteTV6d3ZLYS1qMTNfX2FUUQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SYY** | **22.55** | **14.81** | **11.75** | **4.70** | **40,592,736,256.00 USD** | **14.30** |
| USFD | 31.64 | 5.20 | 15.47 | 4.50 | 22,243,125,248.00 USD | 40.77 |
| PFGC | 42.59 | 3.11 | 13.55 | 7.30 | 15,319,277,568.00 USD | -0.84 |
| CHEF | 43.59 | 5.74 | N/A | 11.20 | 4,414,091,776.00 USD | 62.89 |

Peers fetched as_of: 2026-10-29; SYY reuses existing data (market data as_of: 2026-10-29); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-04
- Next expected earnings: 2026-11-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-29

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

- https://news.google.com/rss/articles/CBMiygFBVV95cUxONE9XTDdrQVZHa2RabTFUQ21rZnh5WW5JRm15NTJJNjdjNENaQ0x6bF9JSm02aDRDMFEwQmJRcEV6Q1J3YlYyMU1aT2VKSEpOeHdhTklEZmRzajdjOEdIampQSzdMdE1DTHE2eUJsYjJlbXpMRWgzcHFhdTRkMGg4QnU3Nzd2NFJIbGNGM3h2RUdIRUV1M3BBMF9CTm9CblRtUjRQdDkycFFLeG9BM1o3Zm42VTY5WmNPb0lYWmZyallMSTdJMjYxeUNB0gHPAUFVX3lxTE1mYXVvbVFFaTJWZ2xxZmJwRnlyclBKRVNubFBNYWRVRXF1a05OTFFsa29SWi03ekpNM1VXZlJRUmgtQVR0WjN2ZksxRTlPV0dzYlRzWjhfRERBWV8yMzVFS19tczloVGlIUEwtZUZVTjV3LVFVMTV2VGI5clRPN1lpQTdCRkRfYjlKOWs2aWJmVDg4VDlmN1ZUTjFIMERvdW45azFvWk4yMHVxenhYX2E3bUVlSS1ZMEZvTkdQTjBlVlluamJoWVdOcWhoWnQ4MA?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxOMllybjY0dGtTSEJqNE5sVm84Z3U2OUtFZlkzZVhvTXdwelpPYkNiUzU4dF95VkltejhzcGpTSkZPQUZ4RDIzZERkcW1lV0ViSEZnbXJXQ3V1bXRWa1pmcV9sbm0tbVdUMmZoYkN6d1BXUHRrOWRMbHRqRkdBaUZ6SmJDQm43YUZrNmtPdmJ0NEdVQnNSbkVSNWRSbC1FcVhYSHVVRg?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPQW1hNVdrVXZzS0w1OG5NYmhxN3BvdkFTak5UNm53cGdkRkc5a0NzZnIzaE11MGRaQnVlMURGQWJwSmZjNHVobU42V2UwSWxhSHRtb094RE1wLWJ1YmxmS2xJcDBjWHVvUlBqd3NnQ096Y1hlcFQzN2VKRkxMbGFCaTZBZzJFZGtBM05BRFIteTV6d3ZLYS1qMTNfX2FUUQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
