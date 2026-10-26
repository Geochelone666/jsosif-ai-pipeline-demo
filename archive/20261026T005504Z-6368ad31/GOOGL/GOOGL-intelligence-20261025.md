# GOOGL Intelligence Report

- ticker: **GOOGL**
- Report as_of: **2026-10-25**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/GOOGL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/GOOGL/key-statistics/
- AI analysis snapshot as_of: **2026-10-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-26T01:26:36.727887+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 4, 'ai': 11, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 10 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 58.33%; oldest publication 2026-10-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 320.2100 |
| Return 1D (%) | -1.2368 |
| Return 1W (%) | -5.9837 |
| Return 1M (%) | -5.2156 |
| Return YTD (%) | 2.5025 |
| Return 1Y (%) | 26.8543 |
| Annualized volatility (%) | 31.6747 |
| Beta vs SPY | 1.3882 |
| Max drawdown (%) | -21.0472 |
| Sharpe (rf=0) | 0.9109 |
| Downside deviation (rf=0, %) | 20.0535 |
| Sortino (rf=0) | 1.4387 |
| Historical VaR 95% (1D, %) | 2.6868 |
| Historical ES 95% (1D, %) | 3.9692 |
| Correlation vs SPY | 0.5586 |
| Tracking error vs SPY (%) | 26.7332 |
| P/E (trailing) | 16.07 |
| P/B | 6.29 |
| EV/EBITDA | 22.02 |
| Revenue growth (%) | 24.20 |
| Forward P/E (estimate) | 20.85 |
| Gross margin (%) | 60.90 |
| Operating margin (%) | 34.03 |
| Return on equity (%) | 48.68 |
| Free cash flow yield (%) | 0.58 |
| MA50 | 342.8769 |
| Close vs MA50 (%) | -6.6108 |
| MA200 | 340.9851 |
| Close vs MA200 (%) | -6.0927 |
| RSI (14, Wilder) | 31.3016 |
| MACD (12,26) | -3.7771 |
| MACD signal (9) | -0.7553 |
| MACD histogram | -3.0218 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'GOOGL': 267, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 320.2100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.2368 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -5.9837 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -5.2156 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 2.5025 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 26.8543 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 31.6747 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 20.0535 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.4387 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.6868 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.9692 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5586 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.7332 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.3882 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -21.0472 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9109 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 20.8488 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 60.8970 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 34.0330 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 48.6760 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.5788 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 16.0667 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 31.3016 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.0218 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -6.6108 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -6.0927 -> Clearly below the moving-average trend level.

## TAILWINDS

### Alphabet Stock Is Up 26.5% Over the Past Year. Still a Buy at $320?
- Summary: Alphabet Stock Is Up 26.5% Over the Past Year. Still a Buy at $320?
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxOVkRDc1djQWtCNDdVX1R1NmkwOU04M0drZW8xTUp6VWhsV1hkRGVCQXZnT1UyWEQxT2JQNS1mWExRWHJWNlJMdGVUckZJNlF3VlVNb2o3NkQtYjgtZTlvYlJnbHBRSlBnT29WMHprekNNd04tN2J0dHJRM3R6WkxMMkVWdmZ6clFxbE90YnNIbzR2Ync?oc=5>

### Google Hits Major Quantum Breakthrough. This Could Be a Game-Changer for GOOGL Stock.
- Summary: Quantum breakthrough could boost GOOGL stock.
- Date: 2026-10-22 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxNc1RiSHJLQ3VMeXVXZnpxWktxY3cwbG1Bb1J5Zkp3VjB1dHJvNTVia2I3ZkpGWVpOcmpJMDF2M1RXSEY5YUdvem9ERTJOTWJPUjVPc3lOYWFEUkc3YkY2cFh3NDFRSnVxTVFCWTlJcjdKQkxhSl9yLU8wRFRSWEJtdktEYXU2V3dqZVBTU2NHQW83bzlZU2RLUlNLMy01M0poZEhGaHpRWXFkNFlHSTFPYjFHTlh0TVBxTHlOQm1HNDNCdGxaT1E?oc=5>

### Alphabet (GOOGL): Investing Behind AI Demand and TPU Growth
- Summary: Alphabet is investing in AI and TPU growth, indicating product development and potential revenue expansion.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPdnYtdmdRMm4wZFI5MzNBaFRmQkotSlFQZEJicWFaYUstMHphSmE3dDhNeWVKUmtpSGdUQlFnYlVrSnh1QXl5bGo2aHhRUFhhSi1DRzZTWUs3VjY3a1gxcEFPR3hxQXhCQk1fUHdyVTNMX2tCazBWY3l4U3c3RUswQ1NTQ2ZZWTVXeHJmWUF4eGRmYS04T05kamxoa3R2YnM?oc=5>

## HEADWINDS

### Alphabet Slips 2% Despite NASDAQ Rally as Pichai Says Google Cloud Is Giving Up Revenue for AI Capacity; Amazon Dips, Microsoft Holds Steady
- Summary: Alphabet stock fell due to cloud revenue loss for AI.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijgJBVV95cUxNUmFwTzgtN0FOZDRWNFQzWTZtd3VJUXdzeG1wcVVMWG02NFg3cWxTUFY4R0xINzNkV0h5a1lkX2VURW5CMVNuZkNYOXVjaHZ6c3paVUJQQlV0NDNQeXdLWHRiWC0xd3VsTUlfUG9GV1BwZTdNd3ZyTXp3dmNxOGxnRVdYLWE0bk8wd3JMejBrLVFzazExcXJmWTM2ank0dmppSk9uOTlDMDJQNmdmWHE2V282VnJqUWYweFdCelpzZEIyRFQzU2d6R0VPblBvZ2VqQlhVelExdEtBOFY1ZjVuSy1TcHBObkgtSXU3X3RVOFBOa0ZkWG9tUG0tQTZPNEViZmpjRlhaSGUza05mVVE?oc=5>

### Alphabet Inc. (GOOG) Stock Drops Despite Market Gains: Important Facts to Note
- Summary: Alphabet’s share price fell amid broader market gains.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOZjdZRVByR1ZDYnp2bzJBdHFhcmRUOERON1R5cHhuWkFQUE9HcGlIa19oUWl3OU5HMS02Q01RWlFLNWdYSHdySDBrMDJxZFF6cFVHQWI4dzJyZmVnenVwQjIzazc5dTVHMV84U0o0MmNaSC1PYW9EOU4yMmpneFIwdFV2ZUpvb3BTRzM5bUs1NXRZb21IbW5yX2ZR?oc=5>

### Alphabet (GOOGL) Stock Declines While Market Improves: Some Information for Investors
- Summary: Alphabet’s stock fell despite broader market gains, signaling a short‑term headwind for investors.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxNVzQ3LW5QS3JVcUV0cUZfLTBaamkybGZtRzVnOGRtSl9UTEVkam96ZWM3cjgzV2RiS3czS3U5UHY4RERqNEpNM25qM1JWUk4wWW1vS2pWWmxYN25WOVVsM2Y5Um9oSHo1QlpZazBqTGFrWVFRR3RtM3ViM0dmTGNmek5McXFtdDZydEx6dA?oc=5>

## CATALYSTS

### Alphabet (GOOGL) Stock Looks Below Fair Value After AI Spending Plans
- Summary: Alphabet (GOOGL) Stock Looks Below Fair Value After AI Spending Plans
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNTXJqRWlqNkRWekQ3dkJteHJzSjRZZlZvTkJjU3FDQ0kwRzlaQWNqWXRqaVFPQzZJemVXajRrYVBaWUtrSUpVNHZuQjZFdjdNOWIwVUVpSzVpSnUwdF9SUXJXWnVwUjZMMTVrWWJ1WEg2STNjTDRkdTJuLWZ3SWYyQ2lrRDBObHphRUQxSU16M0c5WW9SVTlsWkVCYWNBUQ?oc=5>

### GOOGL Stock Earnings Preview: What to Expect From Alphabet’s Q3 2026 Report
- Summary: GOOGL Stock Earnings Preview: What to Expect From Alphabet’s Q3 2026 Report
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQTHQ1Tkw0WFV1UUlJX09HcDBlMzVIZzVEUGZ2TEk5Z09LaFZPNDdicUlPNWp2a1F3MlhzMzNfNW9MdVpkaTVYVzB6a2xvV0hDWmhsaS1mVWppamplTGd4NXB4NUhQYS1OSmE5RlowUHNKN3RuRU1MbDRPNG0tYXcxZGpJSVU3Q2hFVFdBcF9FaGZ0MUZzMWsyR0FXa2ZKOFhGQlE?oc=5>

### Alphabet Stocks Face Wednesday Earnings Test After 82% Cloud Revenue Growth
- Summary: Alphabet Stocks Face Wednesday Earnings Test After 82% Cloud Revenue Growth
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxQM3pzYVczS0J4WFQ1UzhPOElxTU85QkVoNE9RS2w4R1RYQlFBQjdHTXMzam1mMzAtWHVFcmN5UWVqUmtmWmRBT0ZCd080R0NQcEtYVTJ2UEZDdWd6VG1aX2haYUppTEhJNGptTkYwZmtsd0o2dmFLOExJN2F6aER0UzBFUktGdGZFMUw1RFpTUm05Zmx2bHRBY0d4MFhuY05CZ1JLRmI0NA?oc=5>

### Alphabet (GOOGL) Stock Price Forecast 2026: Cloud Hit $20B But FCF Collapsed — Buy or Short?
- Summary: 2026 forecast: cloud revenue $20B, FCF collapsed.
- Date: 2026-10-24 | Impact: medium | Horizon: long | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxQeXNna0FPVFVzVTBlNUM5NVVCNU9TLVhBazdFMVhkaFpBelZTMHBGV2ZqWTBwdFhwUVp3ajJLWXVaNTZURlFrRlhVQ010NDZzVTFhblZESDlvME0wWkhhemJBaXlyREZDLXhpckVRM3QxUlA2dW1idHlFQkEtT3FlbEdIb05UT1QtOFcySkRlc0pwRzc2Z25JQXE2YU8zS2JvLUh1ZUxEd3c5a2lETlItcXo3UEN6ZnA0c185SjNlN1J1QzI2VkE?oc=5>

### Countdown to Alphabet (GOOGL) Q3 Earnings: Wall Street Forecasts for Key Metrics
- Summary: Upcoming Q3 earnings release with analyst forecasts.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxOWURST1VUYy1jU0NIYXBHa2VYbDF2ZXNDTlU2ZU9DN2tIcHRTemJaV3d6ZWlnME9lSnJlQkg1eDVqWjdXbEJiYnBrY1IwZ3BaSWNGQXNSam5KMmI0UU9uOGZYeWd1M2JJZlJHTEhMaWJpUlkxS3RrOFVCdGlBaWl4aE9HQ1V5Y0dNbTVOSVR5U25HU0VxS202ZVZnZXdwdzhDSTl3?oc=5>

### Alphabet Inc. (GOOG) Earnings Expected to Grow: Should You Buy?
- Summary: Anticipated earnings growth could boost investor confidence and drive the stock higher.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQMTJKS0pucEFua01YbEJ0d1d4S2FUN25ZUXhyRDVPUVJvX2FLeUZCbHBJeDZvbHRVeDR2UXpqM1hRbTBycjgzZFgzQjRraXl1QlZPX1NfZC04YzZhb3dRTWdQblBDNE5qOUp2THlraW1ud3N5X1FrV19jWXJwdElMY1p5ckJlaURKZVdVeVdYalA2MHFIOFNVNExZNDNDd2hxRFE?oc=5>

### Alphabet (GOOGL) Earnings Expected to Grow: What to Know Ahead of Next Week's Release
- Summary: Upcoming earnings release is expected to show growth, potentially supporting the stock price.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxOUWhLTjNFeWdtVFptVXRWM3h3MW1jaVRwU2RqMTNLZnFNYV9JVHlYTXlMcVYwZ2Z4QzBSZGFLZTFPQllnOWgzQjNuU3NmTnZJVkxjWVJKU0YtcFNNRWRlTFdiVVZ1N1pydmh5bEFIcEVHVEw0VU9jRUJzdTE5Vy1YYUpUSlVpWDBPOEpvWWhjU2hHemllLXFHYmstZmRSQzhweEM5UQ?oc=5>

## RISKS

### Alphabet (GOOGL): Does Its Valuation Account for Waymo’s Potential?
- Summary: Uncertainty whether current valuation reflects Waymo’s future value, posing a potential risk to investors.
- Date: 2026-10-21 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNTUUtU2RKajFqZW9PeFl0cGh5RlRUdmxZekNvakJTT2piU19lRGJraVNzaUpaNFdYX1JpUlFIa1d6bGRYUXZZM0MwQ0d3eFZjSmVQMGRoT2FkODc3NVptUkRSMHdOSlk5RFgtSndpOGJ0T0dJRlYzRVRGNk9jaXlVLV9TZmtZVHg4SjFiYkFHOF9pV2xydE5wNjNtX1NicEJzMl9CQg?oc=5>

### Alphabet (GOOGL) Cloud Outage And Share Token Fight Put Regulation In Focus
- Summary: Alphabet faces a cloud outage and token dispute, raising regulatory scrutiny and operational risk.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQbVN6MDc4a3piaVFsaE1vcUZFR0dzTk1lQ1VZMDdvU28zWlFLY0E4ZUxvbGJrdGw4dllmc0hDOEhpVWpHUDBpaE9DcU5waThIMmlZMHhibjBaejNSMUpaY1FxZ3VZUHdqb2RzVk5mLVFuUnk1TlZMWHFXcFhLeEZhS0RuNnpjbml4M2pVYWx4R0JTbUJ4Rmt4Tkh3?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **GOOGL** | **16.07** | **6.29** | **22.02** | **24.20** | **3,916,147,458,048.00 USD** | **26.85** |
| META | 21.92 | 6.03 | 14.42 | 26.10 | 1,637,078,401,024.00 USD | -12.15 |
| MSFT | 29.22 | 8.81 | 20.32 | 17.70 | 3,894,773,022,720.00 USD | 1.59 |
| AMZN | 19.95 | 4.85 | 16.60 | 19.60 | 2,675,005,718,528.00 USD | 12.17 |

Peers fetched as_of: 2026-10-25; GOOGL reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-07-22
- Next expected earnings: 2026-10-28 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-25

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-07-23
- Revenue (latest available single quarter): 119,796,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): 112,193,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000071/goog-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMikwFBVV95cUxOVkRDc1djQWtCNDdVX1R1NmkwOU04M0drZW8xTUp6VWhsV1hkRGVCQXZnT1UyWEQxT2JQNS1mWExRWHJWNlJMdGVUckZJNlF3VlVNb2o3NkQtYjgtZTlvYlJnbHBRSlBnT29WMHprekNNd04tN2J0dHJRM3R6WkxMMkVWdmZ6clFxbE90YnNIbzR2Ync?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxNc1RiSHJLQ3VMeXVXZnpxWktxY3cwbG1Bb1J5Zkp3VjB1dHJvNTVia2I3ZkpGWVpOcmpJMDF2M1RXSEY5YUdvem9ERTJOTWJPUjVPc3lOYWFEUkc3YkY2cFh3NDFRSnVxTVFCWTlJcjdKQkxhSl9yLU8wRFRSWEJtdktEYXU2V3dqZVBTU2NHQW83bzlZU2RLUlNLMy01M0poZEhGaHpRWXFkNFlHSTFPYjFHTlh0TVBxTHlOQm1HNDNCdGxaT1E?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPdnYtdmdRMm4wZFI5MzNBaFRmQkotSlFQZEJicWFaYUstMHphSmE3dDhNeWVKUmtpSGdUQlFnYlVrSnh1QXl5bGo2aHhRUFhhSi1DRzZTWUs3VjY3a1gxcEFPR3hxQXhCQk1fUHdyVTNMX2tCazBWY3l4U3c3RUswQ1NTQ2ZZWTVXeHJmWUF4eGRmYS04T05kamxoa3R2YnM?oc=5
- https://news.google.com/rss/articles/CBMijgJBVV95cUxNUmFwTzgtN0FOZDRWNFQzWTZtd3VJUXdzeG1wcVVMWG02NFg3cWxTUFY4R0xINzNkV0h5a1lkX2VURW5CMVNuZkNYOXVjaHZ6c3paVUJQQlV0NDNQeXdLWHRiWC0xd3VsTUlfUG9GV1BwZTdNd3ZyTXp3dmNxOGxnRVdYLWE0bk8wd3JMejBrLVFzazExcXJmWTM2ank0dmppSk9uOTlDMDJQNmdmWHE2V282VnJqUWYweFdCelpzZEIyRFQzU2d6R0VPblBvZ2VqQlhVelExdEtBOFY1ZjVuSy1TcHBObkgtSXU3X3RVOFBOa0ZkWG9tUG0tQTZPNEViZmpjRlhaSGUza05mVVE?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOZjdZRVByR1ZDYnp2bzJBdHFhcmRUOERON1R5cHhuWkFQUE9HcGlIa19oUWl3OU5HMS02Q01RWlFLNWdYSHdySDBrMDJxZFF6cFVHQWI4dzJyZmVnenVwQjIzazc5dTVHMV84U0o0MmNaSC1PYW9EOU4yMmpneFIwdFV2ZUpvb3BTRzM5bUs1NXRZb21IbW5yX2ZR?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxNVzQ3LW5QS3JVcUV0cUZfLTBaamkybGZtRzVnOGRtSl9UTEVkam96ZWM3cjgzV2RiS3czS3U5UHY4RERqNEpNM25qM1JWUk4wWW1vS2pWWmxYN25WOVVsM2Y5Um9oSHo1QlpZazBqTGFrWVFRR3RtM3ViM0dmTGNmek5McXFtdDZydEx6dA?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxNTXJqRWlqNkRWekQ3dkJteHJzSjRZZlZvTkJjU3FDQ0kwRzlaQWNqWXRqaVFPQzZJemVXajRrYVBaWUtrSUpVNHZuQjZFdjdNOWIwVUVpSzVpSnUwdF9SUXJXWnVwUjZMMTVrWWJ1WEg2STNjTDRkdTJuLWZ3SWYyQ2lrRDBObHphRUQxSU16M0c5WW9SVTlsWkVCYWNBUQ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQTHQ1Tkw0WFV1UUlJX09HcDBlMzVIZzVEUGZ2TEk5Z09LaFZPNDdicUlPNWp2a1F3MlhzMzNfNW9MdVpkaTVYVzB6a2xvV0hDWmhsaS1mVWppamplTGd4NXB4NUhQYS1OSmE5RlowUHNKN3RuRU1MbDRPNG0tYXcxZGpJSVU3Q2hFVFdBcF9FaGZ0MUZzMWsyR0FXa2ZKOFhGQlE?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxQM3pzYVczS0J4WFQ1UzhPOElxTU85QkVoNE9RS2w4R1RYQlFBQjdHTXMzam1mMzAtWHVFcmN5UWVqUmtmWmRBT0ZCd080R0NQcEtYVTJ2UEZDdWd6VG1aX2haYUppTEhJNGptTkYwZmtsd0o2dmFLOExJN2F6aER0UzBFUktGdGZFMUw1RFpTUm05Zmx2bHRBY0d4MFhuY05CZ1JLRmI0NA?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxQeXNna0FPVFVzVTBlNUM5NVVCNU9TLVhBazdFMVhkaFpBelZTMHBGV2ZqWTBwdFhwUVp3ajJLWXVaNTZURlFrRlhVQ010NDZzVTFhblZESDlvME0wWkhhemJBaXlyREZDLXhpckVRM3QxUlA2dW1idHlFQkEtT3FlbEdIb05UT1QtOFcySkRlc0pwRzc2Z25JQXE2YU8zS2JvLUh1ZUxEd3c5a2lETlItcXo3UEN6ZnA0c185SjNlN1J1QzI2VkE?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxOWURST1VUYy1jU0NIYXBHa2VYbDF2ZXNDTlU2ZU9DN2tIcHRTemJaV3d6ZWlnME9lSnJlQkg1eDVqWjdXbEJiYnBrY1IwZ3BaSWNGQXNSam5KMmI0UU9uOGZYeWd1M2JJZlJHTEhMaWJpUlkxS3RrOFVCdGlBaWl4aE9HQ1V5Y0dNbTVOSVR5U25HU0VxS202ZVZnZXdwdzhDSTl3?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQMTJKS0pucEFua01YbEJ0d1d4S2FUN25ZUXhyRDVPUVJvX2FLeUZCbHBJeDZvbHRVeDR2UXpqM1hRbTBycjgzZFgzQjRraXl1QlZPX1NfZC04YzZhb3dRTWdQblBDNE5qOUp2THlraW1ud3N5X1FrV19jWXJwdElMY1p5ckJlaURKZVdVeVdYalA2MHFIOFNVNExZNDNDd2hxRFE?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxOUWhLTjNFeWdtVFptVXRWM3h3MW1jaVRwU2RqMTNLZnFNYV9JVHlYTXlMcVYwZ2Z4QzBSZGFLZTFPQllnOWgzQjNuU3NmTnZJVkxjWVJKU0YtcFNNRWRlTFdiVVZ1N1pydmh5bEFIcEVHVEw0VU9jRUJzdTE5Vy1YYUpUSlVpWDBPOEpvWWhjU2hHemllLXFHYmstZmRSQzhweEM5UQ?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNTUUtU2RKajFqZW9PeFl0cGh5RlRUdmxZekNvakJTT2piU19lRGJraVNzaUpaNFdYX1JpUlFIa1d6bGRYUXZZM0MwQ0d3eFZjSmVQMGRoT2FkODc3NVptUkRSMHdOSlk5RFgtSndpOGJ0T0dJRlYzRVRGNk9jaXlVLV9TZmtZVHg4SjFiYkFHOF9pV2xydE5wNjNtX1NicEJzMl9CQg?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQbVN6MDc4a3piaVFsaE1vcUZFR0dzTk1lQ1VZMDdvU28zWlFLY0E4ZUxvbGJrdGw4dllmc0hDOEhpVWpHUDBpaE9DcU5waThIMmlZMHhibjBaejNSMUpaY1FxZ3VZUHdqb2RzVk5mLVFuUnk1TlZMWHFXcFhLeEZhS0RuNnpjbml4M2pVYWx4R0JTbUJ4Rmt4Tkh3?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
