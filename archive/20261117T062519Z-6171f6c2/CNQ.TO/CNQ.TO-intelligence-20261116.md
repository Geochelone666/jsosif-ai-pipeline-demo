# CNQ.TO Intelligence Report

- ticker: **CNQ.TO**
- Report as_of: **2026-11-16**
- Market data as_of: **2026-11-16**
- Quant sources: https://finance.yahoo.com/quote/CNQ.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CNQ.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-16**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-17T06:54:41.027565+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 10, 'rule': 5, 'ai': 2, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261116T043911Z-b81cfeb4/CNQ.TO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 10 unique headlines; 8 named publishers; 0 exact duplicates; 10 HTTPS source links; largest publisher share 30.0%; oldest publication 2026-11-11

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 68.9600 |
| Return 1D (%) | -2.7500 |
| Return 1W (%) | 1.6060 |
| Return 1M (%) | -9.3824 |
| Return YTD (%) | 52.6357 |
| Return 1Y (%) | 52.7558 |
| Annualized volatility (%) | 31.8508 |
| Beta vs SPY | -0.5506 |
| Max drawdown (%) | -18.6770 |
| Sharpe (rf=0) | 1.5146 |
| Downside deviation (rf=0, %) | 22.4786 |
| Sortino (rf=0) | 2.1460 |
| Historical VaR 95% (1D, %) | 3.3063 |
| Historical ES 95% (1D, %) | 4.7931 |
| Correlation vs SPY | -0.2387 |
| Tracking error vs SPY (%) | 37.6904 |
| P/E (trailing) | 9.89 |
| P/B | 3.01 |
| EV/EBITDA | 6.96 |
| Revenue growth (%) | 34.40 |
| Forward P/E (estimate) | 10.99 |
| Gross margin (%) | 52.92 |
| Operating margin (%) | 30.67 |
| Return on equity (%) | 32.38 |
| Free cash flow yield (%) | 8.68 |
| MA50 | 71.1646 |
| Close vs MA50 (%) | -3.0979 |
| MA200 | 64.0399 |
| Close vs MA200 (%) | 7.6829 |
| RSI (14, Wilder) | 41.0192 |
| MACD (12,26) | -0.8115 |
| MACD signal (9) | -0.1707 |
| MACD histogram | -0.6408 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CNQ.TO': 282, 'SPY': 283}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 68.9600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.7500 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.6060 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -9.3824 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 52.6357 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 52.7558 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 31.8508 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 22.4786 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.1460 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.3063 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.7931 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.2387 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.6904 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.5506 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -18.6770 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.5146 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 10.9851 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 52.9160 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 30.6740 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 32.3850 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 8.6772 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 9.8938 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 41.0192 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.6408 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -3.0979 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 7.6829 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Canadian Natural Resources to buy Advantage Energy in $1.77 billion deal
- Summary: Canadian Natural Resources to buy Advantage Energy in $1.77 billion deal
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxQWVlkSEdUTG11TUMzMTctOExYOVE0ZUh0amNlazF6RmNjS1FLT1VjLWxRdmYwTnBySVRzU1BvUm1EQmFidnZici0tbFdXMGVQTGxJZEFDbGt5M1dQZ2ZHbEw1cVQ4bk1nNUVsZTNwdVJDaUFsY2dCaUpXTUlZYWNRZTh1b0FtaVJYeWRqT3d2WEs1VDI0bjhCclNPWHpNVjA0Si1Cak5VT0VrNXRkSDcwb1cxdzZOYnhfV09PRg?oc=5>

### Canadian Natural Resources to buy Advantage Energy in $1.7B deal (CNQ:NYSE)
- Summary: Canadian Natural Resources to buy Advantage Energy in $1.7B deal (CNQ:NYSE)
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPeFNFZFFpaG4xV3FhU3JGU0tMSk4zbXp1a1hGWTd4MHlUQ0o4SmtIdW9OT25wc0lHV3F4WGJ0UXdiQnBPaHJ0TGZLYWRwU3J1XzUwdVpuVWtFdDU0WWlyRUlsRkc5VkVtQkJ2Z3NUSl9XNHZrblFTTGV3elRHbzlCNFFKRTBDdWJKLUxqbHBzSFQ0X2N3TmRYd0M5Z2dFY2Ny?oc=5>

### Canadian Natural Resources Limited (CNQ) to Acquire Advantage Energy for $2.53B
- Summary: Canadian Natural Resources Limited (CNQ) to Acquire Advantage Energy for $2.53B
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxPSTFhTURwLS16LVpzSkVMalptMGFGRUpzMmNZaTZMWkQzVVVqN3pnLTM5NUd6dmVnN2NsOHYtX2lFM0tEeHpmNFUtaWpXck12UDhNM0E0bDFhaGU0Ri1hdzBadHcxUmM3LU9CVHVDdEExV1JMWDJoNzhmU1ZHVkduLXVLX1A1R2NjNFI4MEJQWmw5Z2NYbzRqNmV1NUFoYlFkNlVod2xpYTBSc2FHTk5nLVU3RlNKcXZfWGJxc1FGVlNWaGdkX1FqT25WalpzR0Y4d3hTdQ?oc=5>

### Canadian Natural Resources Limited Enters into Agreement to Acquire Advantage Energy Ltd.
- Summary: Canadian Natural Resources Limited Enters into Agreement to Acquire Advantage Energy Ltd.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxPYlE0UkQwN0ltcXJxTjhzazltcGhhRU1nbUxGRGZEa3BCQ3F1Z1lWMmNxVl82YWpwbmtkWGRYaDQyRWRZMmM0d3Q5ZTZna3VyR3ByemxmSW9yTHhXUklQQ2dLOTM5Slp6ejNwNk15UGZXWm9NaW1RT2tQeDloNnRwaDJ5N294WkpzM3JJVzE0TlVyejliTHVwb2IwdEw4ZS03bmxSdWF1LWVUQ3dFSUFtbjNiblZQczBaYVFEZg?oc=5>

### Canadian Natural Resources (CNQ) to Acquire Advantage Energy in $2.53B Deal
- Summary: Canadian Natural Resources (CNQ) to Acquire Advantage Energy in $2.53B Deal
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxPVVF2by1IckRhUDM3ejhLS0lnTUxXOUNNSzkwSFJCazVLdTFRemFXS1NjeFA5YUV1UzZuRmpSQ2xucVdKMklrZUZSRld5YkpUSC1zZTQwZmYyV0pZWE5LYnRFbTAtOXAxWU04Ynh6QTdONzgtX2FCMDE1clVPWGM0NTVxcXlPcGp1SG9kcFVlcXQzY2pGV0VLeHhZV0xjMlpBT05qd2lUb2V5cllSV2Uw?oc=5>

### How Earnings And Buybacks Will Impact Canadian Natural Resources Stock Investors
- Summary: Discusses how earnings and buybacks could affect CNQ investors.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPLXRydHlQUnZjaDdTWVFNaDh0Wl9xbjVHajdURWZYT1hXVEhLSHZyS1ROVUZncFpOdVA2OEFuSHNnbG8tZ215MTlfQ0hnT1p4eGlWeElncEVyakF2LXExSkZtMENBRkZwLW52eUYzbmR3Q2dQeWhtMTZ6ZjlSckQ4YUxiSjJzc0xLSldzX3Zta1M0ekxTa0J2NUMtaWRkUy1uSmdpNW9vakpsUQ?oc=5>

### Canadian Natural Goes Big on Alberta Oil and Gas With Advantage Energy Deal
- Summary: Canadian Natural Resources announced a strategic acquisition of Advantage Energy, expanding its Alberta oil and gas portfolio and strengthening its production base.
- Date: 2026-11-16 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxPVmJINjdEMUIyUVd4WVdlUEF0YTQxTHpEWjluaHFWZUpaX1BpcElsR1JHQjR0QzFBdDMtbExYTFpMXzV1WXVfaGFqanZYX24yQktod1k1MjZpdVZpcXJBd1VQbWNqVUNWUXRRQVkzX1lEd2hyU0VBYS02QWtnOVNLV1M2V0NFY2NWNHV2Z2V2Q0JqZmIzVUI4dUpMMHRjMWVBRnJjVFdUWE5kMDF1OHlRaUFvNDVWdV9FU05V?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CNQ.TO** | **9.89** | **3.01** | **6.96** | **34.40** | **140,342,558,720.00 CAD** | **52.76** |
| SU.TO | 10.09 | 2.27 | 5.10 | 50.40 | 111,968,067,584.00 CAD | 61.29 |
| IMO.TO | 13.77 | 3.44 | 8.34 | 34.90 | 84,192,747,520.00 CAD | 31.09 |
| CVE.TO | 8.39 | 2.07 | 4.59 | 21.10 | 73,070,034,944.00 CAD | 63.15 |

Peers fetched as_of: 2026-11-16; CNQ.TO reuses existing data (market data as_of: 2026-11-16); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-05
- Next expected earnings: 2027-03-04 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-16

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMivAFBVV95cUxQWVlkSEdUTG11TUMzMTctOExYOVE0ZUh0amNlazF6RmNjS1FLT1VjLWxRdmYwTnBySVRzU1BvUm1EQmFidnZici0tbFdXMGVQTGxJZEFDbGt5M1dQZ2ZHbEw1cVQ4bk1nNUVsZTNwdVJDaUFsY2dCaUpXTUlZYWNRZTh1b0FtaVJYeWRqT3d2WEs1VDI0bjhCclNPWHpNVjA0Si1Cak5VT0VrNXRkSDcwb1cxdzZOYnhfV09PRg?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPeFNFZFFpaG4xV3FhU3JGU0tMSk4zbXp1a1hGWTd4MHlUQ0o4SmtIdW9OT25wc0lHV3F4WGJ0UXdiQnBPaHJ0TGZLYWRwU3J1XzUwdVpuVWtFdDU0WWlyRUlsRkc5VkVtQkJ2Z3NUSl9XNHZrblFTTGV3elRHbzlCNFFKRTBDdWJKLUxqbHBzSFQ0X2N3TmRYd0M5Z2dFY2Ny?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxPSTFhTURwLS16LVpzSkVMalptMGFGRUpzMmNZaTZMWkQzVVVqN3pnLTM5NUd6dmVnN2NsOHYtX2lFM0tEeHpmNFUtaWpXck12UDhNM0E0bDFhaGU0Ri1hdzBadHcxUmM3LU9CVHVDdEExV1JMWDJoNzhmU1ZHVkduLXVLX1A1R2NjNFI4MEJQWmw5Z2NYbzRqNmV1NUFoYlFkNlVod2xpYTBSc2FHTk5nLVU3RlNKcXZfWGJxc1FGVlNWaGdkX1FqT25WalpzR0Y4d3hTdQ?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxPYlE0UkQwN0ltcXJxTjhzazltcGhhRU1nbUxGRGZEa3BCQ3F1Z1lWMmNxVl82YWpwbmtkWGRYaDQyRWRZMmM0d3Q5ZTZna3VyR3ByemxmSW9yTHhXUklQQ2dLOTM5Slp6ejNwNk15UGZXWm9NaW1RT2tQeDloNnRwaDJ5N294WkpzM3JJVzE0TlVyejliTHVwb2IwdEw4ZS03bmxSdWF1LWVUQ3dFSUFtbjNiblZQczBaYVFEZg?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxPVVF2by1IckRhUDM3ejhLS0lnTUxXOUNNSzkwSFJCazVLdTFRemFXS1NjeFA5YUV1UzZuRmpSQ2xucVdKMklrZUZSRld5YkpUSC1zZTQwZmYyV0pZWE5LYnRFbTAtOXAxWU04Ynh6QTdONzgtX2FCMDE1clVPWGM0NTVxcXlPcGp1SG9kcFVlcXQzY2pGV0VLeHhZV0xjMlpBT05qd2lUb2V5cllSV2Uw?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPLXRydHlQUnZjaDdTWVFNaDh0Wl9xbjVHajdURWZYT1hXVEhLSHZyS1ROVUZncFpOdVA2OEFuSHNnbG8tZ215MTlfQ0hnT1p4eGlWeElncEVyakF2LXExSkZtMENBRkZwLW52eUYzbmR3Q2dQeWhtMTZ6ZjlSckQ4YUxiSjJzc0xLSldzX3Zta1M0ekxTa0J2NUMtaWRkUy1uSmdpNW9vakpsUQ?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxPVmJINjdEMUIyUVd4WVdlUEF0YTQxTHpEWjluaHFWZUpaX1BpcElsR1JHQjR0QzFBdDMtbExYTFpMXzV1WXVfaGFqanZYX24yQktod1k1MjZpdVZpcXJBd1VQbWNqVUNWUXRRQVkzX1lEd2hyU0VBYS02QWtnOVNLV1M2V0NFY2NWNHV2Z2V2Q0JqZmIzVUI4dUpMMHRjMWVBRnJjVFdUWE5kMDF1OHlRaUFvNDVWdV9FU05V?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
