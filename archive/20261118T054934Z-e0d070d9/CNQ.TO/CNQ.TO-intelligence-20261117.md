# CNQ.TO Intelligence Report

- ticker: **CNQ.TO**
- Report as_of: **2026-11-17**
- Market data as_of: **2026-11-17**
- Quant sources: https://finance.yahoo.com/quote/CNQ.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CNQ.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-17**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-18T06:13:39.472054+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 9, 'rule': 5, 'ai': 3, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 9 unique headlines; 7 named publishers; 0 exact duplicates; 9 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-11-16

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 68.2900 |
| Return 1D (%) | -0.9716 |
| Return 1W (%) | -0.1608 |
| Return 1M (%) | -10.2628 |
| Return YTD (%) | 51.1527 |
| Return 1Y (%) | 51.8849 |
| Annualized volatility (%) | 31.8084 |
| Beta vs SPY | -0.5406 |
| Max drawdown (%) | -18.6770 |
| Sharpe (rf=0) | 1.4799 |
| Downside deviation (rf=0, %) | 22.4549 |
| Sortino (rf=0) | 2.0963 |
| Historical VaR 95% (1D, %) | 3.2969 |
| Historical ES 95% (1D, %) | 4.7931 |
| Correlation vs SPY | -0.2349 |
| Tracking error vs SPY (%) | 37.6136 |
| P/E (trailing) | 9.97 |
| P/B | 2.98 |
| EV/EBITDA | 6.90 |
| Revenue growth (%) | 34.40 |
| Forward P/E (estimate) | 10.89 |
| Gross margin (%) | 52.92 |
| Operating margin (%) | 30.67 |
| Return on equity (%) | 32.38 |
| Free cash flow yield (%) | 8.76 |
| MA50 | 71.1472 |
| Close vs MA50 (%) | -4.0159 |
| MA200 | 64.1353 |
| Close vs MA200 (%) | 6.4780 |
| RSI (14, Wilder) | 39.1986 |
| MACD (12,26) | -0.9469 |
| MACD signal (9) | -0.3259 |
| MACD histogram | -0.6210 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CNQ.TO': 283, 'SPY': 284}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 68.2900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.9716 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.1608 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -10.2628 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 51.1527 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 51.8849 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 31.8084 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 22.4549 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.0963 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.2969 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.7931 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.2349 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.6136 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.5406 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -18.6770 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.4799 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 10.8880 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 52.9160 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 30.6740 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 32.3850 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 8.7623 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 9.9693 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 39.1986 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.6210 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -4.0159 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 6.4780 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Canadian Natural Resources to buy Advantage Energy in $1.77 billion deal
- Summary: Canadian Natural Resources to buy Advantage Energy in $1.77 billion deal
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxQWVlkSEdUTG11TUMzMTctOExYOVE0ZUh0amNlazF6RmNjS1FLT1VjLWxRdmYwTnBySVRzU1BvUm1EQmFidnZici0tbFdXMGVQTGxJZEFDbGt5M1dQZ2ZHbEw1cVQ4bk1nNUVsZTNwdVJDaUFsY2dCaUpXTUlZYWNRZTh1b0FtaVJYeWRqT3d2WEs1VDI0bjhCclNPWHpNVjA0Si1Cak5VT0VrNXRkSDcwb1cxdzZOYnhfV09PRg?oc=5>

### Canadian Natural Resources (TSX:CNQ) Plans To Acquire Advantage Energy
- Summary: Canadian Natural Resources (TSX:CNQ) Plans To Acquire Advantage Energy
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxQVVVzQjRQWVBXSko5N3FoenVCQndhcmM3anN3V3FrVGtLaFU5ZXBxSHNNNUJXbm1VWU9RaEZyX2VWbEhSaW43MzRzaDgxdU9id1NlWHctaDhtMzFFa2R4dDhhVzdYNGxIMVVoNnhFZThvOHl6VHFMQnJCZW1kWkJqcGtiQl9OOUE4d0x3?oc=5>

### Canadian Natural Resources Limited Enters into Agreement to Acquire Advantage Energy Ltd.
- Summary: Canadian Natural Resources Limited Enters into Agreement to Acquire Advantage Energy Ltd.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxPYlE0UkQwN0ltcXJxTjhzazltcGhhRU1nbUxGRGZEa3BCQ3F1Z1lWMmNxVl82YWpwbmtkWGRYaDQyRWRZMmM0d3Q5ZTZna3VyR3ByemxmSW9yTHhXUklQQ2dLOTM5Slp6ejNwNk15UGZXWm9NaW1RT2tQeDloNnRwaDJ5N294WkpzM3JJVzE0TlVyejliTHVwb2IwdEw4ZS03bmxSdWF1LWVUQ3dFSUFtbjNiblZQczBaYVFEZg?oc=5>

### Canadian Natural Resources Limited (CNQ) to Acquire Advantage Energy for $2.53B
- Summary: Canadian Natural Resources Limited (CNQ) to Acquire Advantage Energy for $2.53B
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxPSTFhTURwLS16LVpzSkVMalptMGFGRUpzMmNZaTZMWkQzVVVqN3pnLTM5NUd6dmVnN2NsOHYtX2lFM0tEeHpmNFUtaWpXck12UDhNM0E0bDFhaGU0Ri1hdzBadHcxUmM3LU9CVHVDdEExV1JMWDJoNzhmU1ZHVkduLXVLX1A1R2NjNFI4MEJQWmw5Z2NYbzRqNmV1NUFoYlFkNlVod2xpYTBSc2FHTk5nLVU3RlNKcXZfWGJxc1FGVlNWaGdkX1FqT25WalpzR0Y4d3hTdQ?oc=5>

### Canadian Natural Resources (CNQ) to Acquire Advantage Energy in $2.53B Deal
- Summary: Canadian Natural Resources (CNQ) to Acquire Advantage Energy in $2.53B Deal
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxPVVF2by1IckRhUDM3ejhLS0lnTUxXOUNNSzkwSFJCazVLdTFRemFXS1NjeFA5YUV1UzZuRmpSQ2xucVdKMklrZUZSRld5YkpUSC1zZTQwZmYyV0pZWE5LYnRFbTAtOXAxWU04Ynh6QTdONzgtX2FCMDE1clVPWGM0NTVxcXlPcGp1SG9kcFVlcXQzY2pGV0VLeHhZV0xjMlpBT05qd2lUb2V5cllSV2Uw?oc=5>

### Canadian Natural buying Advantage Energy in deal valued at $2.53B, including debt
- Summary: CNQ acquires Advantage Energy for $2.53B, expanding its gas assets.
- Date: 2026-11-16 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPbUp5MWY2UnJTcWFXZHE5QkgzMEU4REQ1ZDFUVGM4VGxHMzE4bUZ6VFo1Qm96c0RqSkMxOHJ6NkgzUmxXNm5BeVBiSVNQS290OTctTG5wcHFvai1kemF0YjNFcVU1Sk5JXzBfajdaM25JaW1KaDNnclB0N1hHM3d3RWdHQTlremhjYmVLZ1dWVi16REU?oc=5>

### Advantage Energy: Canadian Natural Resources Acquisition Offer
- Summary: CNQ offers to acquire Advantage Energy, adding to its portfolio.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxOXzdGR1cwUzh4ZS1MUUw5UDNRVDRDSVlEaWgxSkNrQWZuQllsRGRKMXVQNWlCUmN5Ym5uV3lWNExTN3ltckVtOW5XU0M2My1xM3RXcjhGMHdRVTJZQm90ZlZ5SVBmdHRuQ0Q1TFdZMEdDdENyYjZjMXpxWjF3X250dGdQUnBKdlVkRHVNOGxkeHpiZndpUWpZTDVIWDRRMzBGdERVcg?oc=5>

### Canadian Natural to Expand Gas Footprint With Advantage Buyout
- Summary: CNQ's buyout of Advantage Energy boosts its gas footprint.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxPMUJENEdWLWItbkkxQUk3eW13REVmM1RsSmI2dHhNaG5yMVVBZjZ5ZkpwZV9LYUlYVF9iOUZZTkF0R1ZpSTVaMEd2Z0t1bV9jMzAtd0g2Yk5BNndleWxvTXZ4bEdRTXAyQWI5X3laSkc3MnhYY0pPcXY0RVNTOWJOLUxmYnFvZnIxSDFyanF2QQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CNQ.TO** | **9.97** | **2.98** | **6.90** | **34.40** | **138,979,033,088.00 CAD** | **51.88** |
| SU.TO | 10.42 | 2.28 | 5.12 | 50.40 | 112,428,556,288.00 CAD | 61.23 |
| IMO.TO | 14.59 | 3.49 | 8.46 | 34.90 | 85,372,772,352.00 CAD | 33.09 |
| CVE.TO | 8.57 | 2.07 | 4.59 | 21.10 | 72,925,446,144.00 CAD | 64.12 |

Peers fetched as_of: 2026-11-17; CNQ.TO reuses existing data (market data as_of: 2026-11-17); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-05
- Next expected earnings: 2027-03-04 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-17

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
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxQVVVzQjRQWVBXSko5N3FoenVCQndhcmM3anN3V3FrVGtLaFU5ZXBxSHNNNUJXbm1VWU9RaEZyX2VWbEhSaW43MzRzaDgxdU9id1NlWHctaDhtMzFFa2R4dDhhVzdYNGxIMVVoNnhFZThvOHl6VHFMQnJCZW1kWkJqcGtiQl9OOUE4d0x3?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxPYlE0UkQwN0ltcXJxTjhzazltcGhhRU1nbUxGRGZEa3BCQ3F1Z1lWMmNxVl82YWpwbmtkWGRYaDQyRWRZMmM0d3Q5ZTZna3VyR3ByemxmSW9yTHhXUklQQ2dLOTM5Slp6ejNwNk15UGZXWm9NaW1RT2tQeDloNnRwaDJ5N294WkpzM3JJVzE0TlVyejliTHVwb2IwdEw4ZS03bmxSdWF1LWVUQ3dFSUFtbjNiblZQczBaYVFEZg?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxPSTFhTURwLS16LVpzSkVMalptMGFGRUpzMmNZaTZMWkQzVVVqN3pnLTM5NUd6dmVnN2NsOHYtX2lFM0tEeHpmNFUtaWpXck12UDhNM0E0bDFhaGU0Ri1hdzBadHcxUmM3LU9CVHVDdEExV1JMWDJoNzhmU1ZHVkduLXVLX1A1R2NjNFI4MEJQWmw5Z2NYbzRqNmV1NUFoYlFkNlVod2xpYTBSc2FHTk5nLVU3RlNKcXZfWGJxc1FGVlNWaGdkX1FqT25WalpzR0Y4d3hTdQ?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxPVVF2by1IckRhUDM3ejhLS0lnTUxXOUNNSzkwSFJCazVLdTFRemFXS1NjeFA5YUV1UzZuRmpSQ2xucVdKMklrZUZSRld5YkpUSC1zZTQwZmYyV0pZWE5LYnRFbTAtOXAxWU04Ynh6QTdONzgtX2FCMDE1clVPWGM0NTVxcXlPcGp1SG9kcFVlcXQzY2pGV0VLeHhZV0xjMlpBT05qd2lUb2V5cllSV2Uw?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPbUp5MWY2UnJTcWFXZHE5QkgzMEU4REQ1ZDFUVGM4VGxHMzE4bUZ6VFo1Qm96c0RqSkMxOHJ6NkgzUmxXNm5BeVBiSVNQS290OTctTG5wcHFvai1kemF0YjNFcVU1Sk5JXzBfajdaM25JaW1KaDNnclB0N1hHM3d3RWdHQTlremhjYmVLZ1dWVi16REU?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxOXzdGR1cwUzh4ZS1MUUw5UDNRVDRDSVlEaWgxSkNrQWZuQllsRGRKMXVQNWlCUmN5Ym5uV3lWNExTN3ltckVtOW5XU0M2My1xM3RXcjhGMHdRVTJZQm90ZlZ5SVBmdHRuQ0Q1TFdZMEdDdENyYjZjMXpxWjF3X250dGdQUnBKdlVkRHVNOGxkeHpiZndpUWpZTDVIWDRRMzBGdERVcg?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxPMUJENEdWLWItbkkxQUk3eW13REVmM1RsSmI2dHhNaG5yMVVBZjZ5ZkpwZV9LYUlYVF9iOUZZTkF0R1ZpSTVaMEd2Z0t1bV9jMzAtd0g2Yk5BNndleWxvTXZ4bEdRTXAyQWI5X3laSkc3MnhYY0pPcXY0RVNTOWJOLUxmYnFvZnIxSDFyanF2QQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
