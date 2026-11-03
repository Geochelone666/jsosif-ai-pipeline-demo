# SYY Intelligence Report

- ticker: **SYY**
- Report as_of: **2026-11-02**
- Market data as_of: **2026-11-02**
- Quant sources: https://finance.yahoo.com/quote/SYY/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SYY/key-statistics/
- AI analysis snapshot as_of: **2026-11-02**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-03T05:25:49.247410+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 14, 'rule': 4, 'ai': 3, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261102T041627Z-c84a7052/SYY** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 14 unique headlines; 8 named publishers; 0 exact duplicates; 14 HTTPS source links; largest publisher share 28.57%; oldest publication 2026-10-27

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 81.7400 |
| Return 1D (%) | -1.3993 |
| Return 1W (%) | -0.5112 |
| Return 1M (%) | 5.4846 |
| Return YTD (%) | 14.1388 |
| Return 1Y (%) | 13.2322 |
| Annualized volatility (%) | 27.3526 |
| Beta vs SPY | 0.1559 |
| Max drawdown (%) | -23.9798 |
| Sharpe (rf=0) | 0.6670 |
| Downside deviation (rf=0, %) | 20.2287 |
| Sortino (rf=0) | 0.9018 |
| Historical VaR 95% (1D, %) | 2.1091 |
| Historical ES 95% (1D, %) | 3.7604 |
| Correlation vs SPY | 0.0731 |
| Tracking error vs SPY (%) | 29.3480 |
| P/E (trailing) | 22.64 |
| P/B | 14.67 |
| EV/EBITDA | 11.67 |
| Revenue growth (%) | 4.70 |
| Forward P/E (estimate) | 15.24 |
| Gross margin (%) | 18.50 |
| Operating margin (%) | 4.84 |
| Return on equity (%) | 77.69 |
| Free cash flow yield (%) | 4.76 |
| MA50 | 80.1785 |
| Close vs MA50 (%) | 1.9475 |
| MA200 | 79.5325 |
| Close vs MA200 (%) | 2.7756 |
| RSI (14, Wilder) | 53.5456 |
| MACD (12,26) | 0.8480 |
| MACD signal (9) | 0.7549 |
| MACD histogram | 0.0931 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SYY': 273, 'SPY': 273}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 81.7400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.3993 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.5112 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 5.4846 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 14.1388 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 13.2322 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 27.3526 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 20.2287 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.9018 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.1091 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.7604 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0731 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 29.3480 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.1559 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -23.9798 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.6670 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.2420 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 18.4960 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 4.8450 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 77.6920 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.7601 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 22.6427 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 53.5456 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.0931 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 1.9475 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 2.7756 -> Slightly above the moving-average trend level.

## TAILWINDS

### How Investors May Respond To Sysco (SYY) Los Angeles Strike Ends
- Summary: Strike ends, likely boosting investor confidence and stock performance.
- Date: 2026-10-27 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOQVFEU1JiUkJwQ0VIemhIdnNpOU9YYmhhbmp2aDAwdXJCeFpIQWZ5ckt5TExHc2EyMmFFLXF3cDJCTGwtWGk4NGEzSXpCQkRfZHh3RHZPSmRyRFloNHZabjJJc05GSTc0aGZLejY5blhSMmZvd2JRcTZkTGVOMTl6QjJOVU1JOXl4ZW1YSUc0YmZhNnlhOExyRFZaMEU?oc=5>

### Sysco (SYY) Stock May Look Reasonable As Its 34% Run Continues
- Summary: Sysco’s stock continues a 34% run, suggesting potential value for investors.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxONE9XTDdrQVZHa2RabTFUQ21rZnh5WW5JRm15NTJJNjdjNENaQ0x6bF9JSm02aDRDMFEwQmJRcEV6Q1J3YlYyMU1aT2VKSEpOeHdhTklEZmRzajdjOEdIampQSzdMdE1DTHE2eUJsYjJlbXpMRWgzcHFhdTRkMGg4QnU3Nzd2NFJIbGNGM3h2RUdIRUV1M3BBMF9CTm9CblRtUjRQdDkycFFLeG9BM1o3Zm42VTY5WmNPb0lYWmZyallMSTdJMjYxeUNB0gHPAUFVX3lxTE1mYXVvbVFFaTJWZ2xxZmJwRnlyclBKRVNubFBNYWRVRXF1a05OTFFsa29SWi03ekpNM1VXZlJRUmgtQVR0WjN2ZksxRTlPV0dzYlRzWjhfRERBWV8yMzVFS19tczloVGlIUEwtZUZVTjV3LVFVMTV2VGI5clRPN1lpQTdCRkRfYjlKOWs2aWJmVDg4VDlmN1ZUTjFIMERvdW45azFvWk4yMHVxenhYX2E3bUVlSS1ZMEZvTkdQTjBlVlluamJoWVdOcWhoWnQ4MA?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Sysco earnings: what to look for from SYY
- Summary: Sysco earnings: what to look for from SYY
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPSDJ0T3dUSGVRYWtaMnNZYU9YZklSX3dNNnByNHRFQWdWVDltNWJvLU1iWm9MMk55SHp3NGgzLUJQbmZyeWd1LU1ZVk9TdXRGdTZsT3dvLXJkbHlfSFpKM1hnMGNCNmw1dUIzRC1RYkJVd1VENHJjd3FfNG5MT1pEa2EzUjVYTk1JMnFBckluWWRTMGF1UWFlQlJFeXhrTWdxTDRV?oc=5>

### Sysco Earnings Preview: High Debt Levels Overshadow Everything (NYSE:SYY)
- Summary: Sysco Earnings Preview: High Debt Levels Overshadow Everything (NYSE:SYY)
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxOMllybjY0dGtTSEJqNE5sVm84Z3U2OUtFZlkzZVhvTXdwelpPYkNiUzU4dF95VkltejhzcGpTSkZPQUZ4RDIzZERkcW1lV0ViSEZnbXJXQ3V1bXRWa1pmcV9sbm0tbVdUMmZoYkN6d1BXUHRrOWRMbHRqRkdBaUZ6SmJDQm43YUZrNmtPdmJ0NEdVQnNSbkVSNWRSbC1FcVhYSHVVRg?oc=5>

### Sysco Q1 Earnings on the Horizon: Essential Insights for Investors
- Summary: Sysco Q1 Earnings on the Horizon: Essential Insights for Investors
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxNQk5HNnFVSkhkUVY4d3pfODNKSFlRR1Zsb01EcWN6SVZPV0FndlJDbkFiOWZVYVBwMlVCaDFvUVZtanl3QU0tZUtwZnJwXzZIOFZEOUhjeDl3OEJoUi13RTVvbkpndkxzOUZZcXdILWNXWGpVeWNrQk1wX0ZmRmNKMDc4SXpVOXdRdXIyOWpzeEdBMTRmRktSYktleExvVTJLMk53SnFVNXY5Y0wzdWl4cTNiRFJteUZ4NWFkbQ?oc=5>

### Sysco Corporation $SYY Stock: VIRGINIA RETIREMENT SYSTEMS ET Al Lowers Position
- Summary: Sysco Corporation $SYY Stock: VIRGINIA RETIREMENT SYSTEMS ET Al Lowers Position
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxNZk8yMk1mcVozeklUZzZpd1N6WE5VYnVjXzlEU3RKZFNvME9OU3RaampvSWFudXMwdDM0REFlNUZuUFdoUFRuQ3F1eTZIN2tSTld0WVZZaXRIdjlaQ0MxUU5hUERyR0s2aU5kemU2ZGJLNC1mLTdHZnBmWUtqZEpmV3ZnaVdxY0VqWjRheTR5dkh6STRUTW5hSUpnMUUyWUFEeVg0R1A5QTBIQjcwNlZvUkw5cUpnSWR0MHdnbkxRRGNEWEZnbVNjRWctMmRZVGlpU0NyVw?oc=5>

### Sysco (SYY) Earnings Expected to Grow: Should You Buy?
- Summary: Sysco forecasts higher earnings, suggesting potential upside for investors.
- Date: 2026-10-27 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPQW1hNVdrVXZzS0w1OG5NYmhxN3BvdkFTak5UNm53cGdkRkc5a0NzZnIzaE11MGRaQnVlMURGQWJwSmZjNHVobU42V2UwSWxhSHRtb094RE1wLWJ1YmxmS2xJcDBjWHVvUlBqd3NnQ096Y1hlcFQzN2VKRkxMbGFCaTZBZzJFZGtBM05BRFIteTV6d3ZLYS1qMTNfX2FUUQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SYY** | **22.64** | **14.67** | **11.67** | **4.70** | **40,209,043,456.00 USD** | **13.23** |
| USFD | 31.87 | 5.35 | 15.84 | 4.50 | 22,887,790,592.00 USD | 45.69 |
| PFGC | 43.28 | 3.21 | 13.86 | 7.30 | 15,839,186,944.00 USD | 4.24 |
| CHEF | 44.30 | 6.13 | 19.20 | 11.20 | 4,486,674,944.00 USD | 74.97 |

Peers fetched as_of: 2026-11-02; SYY reuses existing data (market data as_of: 2026-11-02); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-04
- Next expected earnings: 2026-11-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-02

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMinAFBVV95cUxOQVFEU1JiUkJwQ0VIemhIdnNpOU9YYmhhbmp2aDAwdXJCeFpIQWZ5ckt5TExHc2EyMmFFLXF3cDJCTGwtWGk4NGEzSXpCQkRfZHh3RHZPSmRyRFloNHZabjJJc05GSTc0aGZLejY5blhSMmZvd2JRcTZkTGVOMTl6QjJOVU1JOXl4ZW1YSUc0YmZhNnlhOExyRFZaMEU?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxONE9XTDdrQVZHa2RabTFUQ21rZnh5WW5JRm15NTJJNjdjNENaQ0x6bF9JSm02aDRDMFEwQmJRcEV6Q1J3YlYyMU1aT2VKSEpOeHdhTklEZmRzajdjOEdIampQSzdMdE1DTHE2eUJsYjJlbXpMRWgzcHFhdTRkMGg4QnU3Nzd2NFJIbGNGM3h2RUdIRUV1M3BBMF9CTm9CblRtUjRQdDkycFFLeG9BM1o3Zm42VTY5WmNPb0lYWmZyallMSTdJMjYxeUNB0gHPAUFVX3lxTE1mYXVvbVFFaTJWZ2xxZmJwRnlyclBKRVNubFBNYWRVRXF1a05OTFFsa29SWi03ekpNM1VXZlJRUmgtQVR0WjN2ZksxRTlPV0dzYlRzWjhfRERBWV8yMzVFS19tczloVGlIUEwtZUZVTjV3LVFVMTV2VGI5clRPN1lpQTdCRkRfYjlKOWs2aWJmVDg4VDlmN1ZUTjFIMERvdW45azFvWk4yMHVxenhYX2E3bUVlSS1ZMEZvTkdQTjBlVlluamJoWVdOcWhoWnQ4MA?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPSDJ0T3dUSGVRYWtaMnNZYU9YZklSX3dNNnByNHRFQWdWVDltNWJvLU1iWm9MMk55SHp3NGgzLUJQbmZyeWd1LU1ZVk9TdXRGdTZsT3dvLXJkbHlfSFpKM1hnMGNCNmw1dUIzRC1RYkJVd1VENHJjd3FfNG5MT1pEa2EzUjVYTk1JMnFBckluWWRTMGF1UWFlQlJFeXhrTWdxTDRV?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxOMllybjY0dGtTSEJqNE5sVm84Z3U2OUtFZlkzZVhvTXdwelpPYkNiUzU4dF95VkltejhzcGpTSkZPQUZ4RDIzZERkcW1lV0ViSEZnbXJXQ3V1bXRWa1pmcV9sbm0tbVdUMmZoYkN6d1BXUHRrOWRMbHRqRkdBaUZ6SmJDQm43YUZrNmtPdmJ0NEdVQnNSbkVSNWRSbC1FcVhYSHVVRg?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxNQk5HNnFVSkhkUVY4d3pfODNKSFlRR1Zsb01EcWN6SVZPV0FndlJDbkFiOWZVYVBwMlVCaDFvUVZtanl3QU0tZUtwZnJwXzZIOFZEOUhjeDl3OEJoUi13RTVvbkpndkxzOUZZcXdILWNXWGpVeWNrQk1wX0ZmRmNKMDc4SXpVOXdRdXIyOWpzeEdBMTRmRktSYktleExvVTJLMk53SnFVNXY5Y0wzdWl4cTNiRFJteUZ4NWFkbQ?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxNZk8yMk1mcVozeklUZzZpd1N6WE5VYnVjXzlEU3RKZFNvME9OU3RaampvSWFudXMwdDM0REFlNUZuUFdoUFRuQ3F1eTZIN2tSTld0WVZZaXRIdjlaQ0MxUU5hUERyR0s2aU5kemU2ZGJLNC1mLTdHZnBmWUtqZEpmV3ZnaVdxY0VqWjRheTR5dkh6STRUTW5hSUpnMUUyWUFEeVg0R1A5QTBIQjcwNlZvUkw5cUpnSWR0MHdnbkxRRGNEWEZnbVNjRWctMmRZVGlpU0NyVw?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPQW1hNVdrVXZzS0w1OG5NYmhxN3BvdkFTak5UNm53cGdkRkc5a0NzZnIzaE11MGRaQnVlMURGQWJwSmZjNHVobU42V2UwSWxhSHRtb094RE1wLWJ1YmxmS2xJcDBjWHVvUlBqd3NnQ096Y1hlcFQzN2VKRkxMbGFCaTZBZzJFZGtBM05BRFIteTV6d3ZLYS1qMTNfX2FUUQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
