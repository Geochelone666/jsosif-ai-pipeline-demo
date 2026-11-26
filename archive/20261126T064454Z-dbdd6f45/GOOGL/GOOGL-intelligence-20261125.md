# GOOGL Intelligence Report

- ticker: **GOOGL**
- Report as_of: **2026-11-25**
- Market data as_of: **2026-11-25**
- Quant sources: https://finance.yahoo.com/quote/GOOGL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/GOOGL/key-statistics/
- AI analysis snapshot as_of: **2026-11-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-26T06:46:39.486702+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 7, 'ai': 6, 'unknown': 0, 'irrelevant': 10})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261125T065354Z-0b3565c6/GOOGL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 14 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 21.74%; oldest publication 2026-11-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 273.1000 |
| Return 1D (%) | -2.1322 |
| Return 1W (%) | -3.3069 |
| Return 1M (%) | -14.7122 |
| Return YTD (%) | -12.5779 |
| Return 1Y (%) | -15.3443 |
| Annualized volatility (%) | 33.6265 |
| Beta vs SPY | 1.2588 |
| Max drawdown (%) | -34.0273 |
| Sharpe (rf=0) | -0.3286 |
| Downside deviation (rf=0, %) | 24.3486 |
| Sortino (rf=0) | -0.4538 |
| Historical VaR 95% (1D, %) | 3.1807 |
| Historical ES 95% (1D, %) | 4.8274 |
| Correlation vs SPY | 0.5589 |
| Tracking error vs SPY (%) | 28.1501 |
| P/E (trailing) | 14.26 |
| P/B | 5.09 |
| EV/EBITDA | 17.58 |
| Revenue growth (%) | 24.70 |
| Forward P/E (estimate) | 17.86 |
| Gross margin (%) | 60.86 |
| Operating margin (%) | 33.32 |
| Return on equity (%) | 44.29 |
| Free cash flow yield (%) | -0.03 |
| MA50 | 318.2408 |
| Close vs MA50 (%) | -14.1845 |
| MA200 | 336.0612 |
| Close vs MA200 (%) | -18.7350 |
| RSI (14, Wilder) | 36.9305 |
| MACD (12,26) | -12.0675 |
| MACD signal (9) | -12.6769 |
| MACD histogram | 0.6093 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'GOOGL': 290, 'SPY': 290}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 273.1000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.1322 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -3.3069 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -14.7122 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -12.5779 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -15.3443 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 33.6265 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 24.3486 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.4538 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.1807 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.8274 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5589 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 28.1501 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.2588 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -34.0273 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.3286 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.8555 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 60.8570 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 33.3210 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 44.2860 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: -0.0346 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 14.2611 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 36.9305 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.6093 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -14.1845 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -18.7350 -> Clearly below the moving-average trend level.

## TAILWINDS

### Alphabet Stock Pops: What's Going On?
- Summary: Alphabet Stock Pops: What's Going On?
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOc1RxLWU5d3g3QTUxMk1LUm5fRjhnYlJ6UnVVb2VMVmtOemZFU0RGUjBaQVpwYkUwa052R0pFUFZReE00RWRxdjB1UnlROE5VNS1CVDVuSEhLdThDeElCVmd0bGYwS01yX1g1QXlWeE1FZV9OaWNCWXlraXd2ZmQ2SlJJdkhOMlR3WjllY2I2NDl5RXFWOFgtVXl1aw?oc=5>

### Google Parent Alphabet Stock Is Jumping. 2 Reasons the Comeback Starts Today.
- Summary: Google Parent Alphabet Stock Is Jumping. 2 Reasons the Comeback Starts Today.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMieEFVX3lxTE10WDdwclZjV3ltY3NHVm9ia044N0huUnBJZGgtN1FkalNkajRpS1R4XzFjYjg3ajRXS0hwWDdvbHdPQ0k5eWxhSHBuOS1Da2x5S285MFJ1QVVwN2Nob2pLQlZmYVlwQ1ljT2VOaXBPMWMzU3dkaE5Wbg?oc=5>

### Alphabet (GOOGL) Expands AI Search With Wallet Data
- Summary: Alphabet launches AI search using wallet data, enhancing user experience and monetization.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOSThiNzctTzdySGZNYlM1bWNra1lQbXNMclhNZm5kR3NtaFdsOXNiOTBPN2F3LVhWb08wdXZPVkxEU015Mkk3M2FTQkg3c3ZrS2dXN1E0NlVWcjJBdjlkUEJhSHd1MzFrTUY2M0wxVDFJLXpzbHpOcUxKbkJ3UmtrUDQzdy1obi1CSHBuMzNSYWVnX2xzMGIwWUJHWFA?oc=5>

### Billionaire Stephen Mandel’s Lone Pine Raised Its Alphabet Stake 901% to $743 Million
- Summary: Major investor increases stake, signaling confidence in Alphabet’s prospects.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxPbTVLOFBhWHBFTnlIelplSmg4dTNhcmtYX2pyUXY1ZE1Kd09qa0xrNHphaG9MRFNJVEJlLTVPMGIxSVJHRlMwc2hfXzc2Q3NaLWh6VlhLOFRDZHo0bmZIUFFjdnpkcjRzN2otT0FBTWNpNEh5WnpXeVQ3ejlVX3ZCUXA4TUdkZmMyM29YSjRLbm5ZVjg0YU5MWlJFVXFZTjhzd2FTYnBQNFF2cHRIblhobkM2Mm5HMmd2RlNxb3JFbXl4RmNp?oc=5>

## HEADWINDS

### Alphabet Stock Slips: What's Going On?
- Summary: Alphabet Stock Slips: What's Going On?
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxONzV3WFpHQl90VnFfWjdzeTQ5VVNhMkVaNVFzTHZfZWE4VGd6UFNzNHF0Y2JsbkJqMVNod05lLWZIUlVXUEtKY0ctQ2kycXRwSVVscVpvcjhlNlplXzhkYVlKbHd6ZmJ0UWFXLTNHSEpBbXkyVFFkWFdXN01TT054SUNndVNJbW9uT2lOLTZJTlQ3Vlh2d1VNbU5lRVc?oc=5>

### Alphabet falls while renewed AI stock selling and tariff proposals rattle market sentiment
- Summary: Alphabet falls while renewed AI stock selling and tariff proposals rattle market sentiment
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxPN1k5S1ctdmt6QmxRSEJ4eHdxMndHcFBEeC03UHRHdERzd1BZX3hYRkc0WjF3Qzg1QXhWZHZPUzFyYmRrR3FaZklFUTdKR29ZYml0RW9pTDVWT1o2dGRvWWhEQlcwVEhEWDF4TG9jZ0Z5dnFqZ3BmQUpOMDFPS2VNMFZEUkNCZHd5ak84?oc=5>

### Alphabet Stocks Drop 5.56% as Credit Default Swaps Hit Record
- Summary: Alphabet Stocks Drop 5.56% as Credit Default Swaps Hit Record
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxOSEtyWTJmZGZ3d0VpOVJtOGlSdWo2OEVoVmxsbkdnR0pENjZSd2VmMklGaFRacjlBQVNueWpQamllRVBha09IM3BVcjVrZ2g1bEMyYko3NVFvTGJCNWwtd25taGhSeVI3ZDBOWFZ4d3IzeHEwNXY4WXRtaGZWQS1BNWtiOGcySTl4ZE15d1ktQUJjN2h3UHZyNW1qS0IxYk93amxFcE5ZbjY3QzRJVF9MRjZCOW1vYkxGanl2RQ?oc=5>

### Alphabet (GOOGL) Stock Could Be 47% Undervalued As AI Spending Fears Bite
- Summary: Analyst warns AI spending fears may undervalue Alphabet, suggesting a medium‑term headwind.
- Date: 2026-11-19 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNT1ZWV245S1M1R2I2RVIyNHprYlZwcGN1eGlRWE9ZNTJYd0Q3V2xyb0FFZWdNcFRhVHVPVUtKdEdrYmd4bDlNbkRkdTNFazJLUU1wS0g1WlVFd3U3YU1pbkl4R09QVmFkVEZYMTNjU1FJbnU0bGY5Mk9zNWxFcWV2Y0h1aDF1aGlnYjBmNk53LU5TaHVwdTBmRjd3?oc=5>

### Alphabet Stock Just Hit a 1-Year Low. Why Is Google's Parent Borrowing So Much Money?
- Summary: Alphabet's stock fell to a 1-year low amid concerns over high borrowing levels.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxOZWlMZ2JfQi1mSmxiLS00Mml1VDR1Q0tuVjZSaks4dHh6bU5Ld0oxQ01QUVhtN0x6c3Q0cmtFVzBoUC1jNzB3TTRUdmU5TTJZUk01blptY09QV0o5UHpxdzRPUzVrSWNsaTkwMktGLUhNYktFNWVIb0pYc2Riemt4WnlSd01oZFMtYVpFUHlIT2lUT1FJalJVQ2lKalpfY2dtS0VrS2xnRDl0NzhqUFdjVGxUQlFEUXItd0ctM1BNTXJiaU9p?oc=5>

### Why Alphabet Stock Is Down Today
- Summary: Alphabet shares decline today, reflecting market concerns.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTE5oaTFTRjBXY0FMeFFPa0lVSnF5VHFYVEx5MmIxLWJuZXJMN2xINVkwSDdqS0FmQXhYbGM3d2lxcjh4bVJjcnhsZXlOZFRYbHJxdVVvbzlRbk5tWDRfVXpCb2l6TDBnRDZtd1BGdFhucnR5SkpxTUZ6bHZsaEpXZw?oc=5>

### Why Alphabet Stock Fell Today (Hint: It's AI-Related)
- Summary: Alphabet shares fall, likely due to AI-related market reactions.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMifEFVX3lxTFBkeThCOUJKVXM5alhlRV9IV08ycTRLZmdwWDlWVkJ1M1ViVnhOSG9tNkxtVkhoRW15VG1hUUthYmNwUEpCYTVwOG9nWGYzdFQyZUthaHhULXJFdDhsLUQwWU9tdjhPQzQ2eXl2QVBIUTQyRXEwYlpZVWhtdjI?oc=5>

## CATALYSTS

### Alphabet stock plunges as Google walks away from a big Australian news deal
- Summary: Alphabet stock plunges as Google walks away from a big Australian news deal
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxNRHppYVF4UlRjVERuWnA5WUNMVTNTUVJNNWY5Q2RzZmZUNGJXNFZ3SW5XdkJ4cXZORFdxbEZ2R1dSN3BrVGhtcENqUC12bm9fNGlueE50S3BiNDNDdHZId1FmQjZ1Rkx0MnFiMVpZYndnQmsybEQ4Rnk2RlZiay0tdmdJd3JKVi1aVmpkQ2V4M2VrcW4xbGpHUDNPWkhEcmxlVW04OGRwUTRRaUNxclNMUjFiVEhnQ1lnZ1JhNnZ6clVIbWV0clZ3U1hzNDJDWFVC?oc=5>

### Alphabet (GOOGL) Stock Gets Fair Value Trim As Analysts Weigh AI Spending And Monetization
- Summary: Alphabet (GOOGL) Stock Gets Fair Value Trim As Analysts Weigh AI Spending And Monetization
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxON3V6WEZ5MTczaE84bktQaVNVMWY0d1ZBTDZhZW92R2pQX2RzUnZZYVJ4bzVCMTA4R0Mtbk9hUWV0cnJSdkh2MktNVjAyaFJMTVB1NEFram1EcnlqOVRHdWRMa1kwUDBJWEhRZ0ZVRkxVV0FabGtVa1NCREhWMjBkZ1N2c29mYzVodFV4T2RXdUJCMGRzQmF1MzEzTQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **GOOGL** | **14.26** | **5.09** | **17.58** | **24.70** | **3,357,491,331,072.00 USD** | **-15.34** |
| META | 20.81 | 5.72 | 13.70 | 26.10 | 1,559,025,942,528.00 USD | -3.81 |
| MSFT | 25.57 | 7.73 | 18.03 | 18.80 | 3,638,315,450,368.00 USD | 3.56 |
| AMZN | 19.76 | 4.31 | 15.42 | 12.10 | 2,643,055,345,664.00 USD | 6.43 |

Peers fetched as_of: 2026-11-25; GOOGL reuses existing data (market data as_of: 2026-11-25); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-28
- Next expected earnings: 2027-02-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-25

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-29
- Revenue (latest available single quarter): 127,577,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 26,468,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000084/goog-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimwFBVV95cUxOc1RxLWU5d3g3QTUxMk1LUm5fRjhnYlJ6UnVVb2VMVmtOemZFU0RGUjBaQVpwYkUwa052R0pFUFZReE00RWRxdjB1UnlROE5VNS1CVDVuSEhLdThDeElCVmd0bGYwS01yX1g1QXlWeE1FZV9OaWNCWXlraXd2ZmQ2SlJJdkhOMlR3WjllY2I2NDl5RXFWOFgtVXl1aw?oc=5
- https://news.google.com/rss/articles/CBMieEFVX3lxTE10WDdwclZjV3ltY3NHVm9ia044N0huUnBJZGgtN1FkalNkajRpS1R4XzFjYjg3ajRXS0hwWDdvbHdPQ0k5eWxhSHBuOS1Da2x5S285MFJ1QVVwN2Nob2pLQlZmYVlwQ1ljT2VOaXBPMWMzU3dkaE5Wbg?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOSThiNzctTzdySGZNYlM1bWNra1lQbXNMclhNZm5kR3NtaFdsOXNiOTBPN2F3LVhWb08wdXZPVkxEU015Mkk3M2FTQkg3c3ZrS2dXN1E0NlVWcjJBdjlkUEJhSHd1MzFrTUY2M0wxVDFJLXpzbHpOcUxKbkJ3UmtrUDQzdy1obi1CSHBuMzNSYWVnX2xzMGIwWUJHWFA?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxPbTVLOFBhWHBFTnlIelplSmg4dTNhcmtYX2pyUXY1ZE1Kd09qa0xrNHphaG9MRFNJVEJlLTVPMGIxSVJHRlMwc2hfXzc2Q3NaLWh6VlhLOFRDZHo0bmZIUFFjdnpkcjRzN2otT0FBTWNpNEh5WnpXeVQ3ejlVX3ZCUXA4TUdkZmMyM29YSjRLbm5ZVjg0YU5MWlJFVXFZTjhzd2FTYnBQNFF2cHRIblhobkM2Mm5HMmd2RlNxb3JFbXl4RmNp?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxONzV3WFpHQl90VnFfWjdzeTQ5VVNhMkVaNVFzTHZfZWE4VGd6UFNzNHF0Y2JsbkJqMVNod05lLWZIUlVXUEtKY0ctQ2kycXRwSVVscVpvcjhlNlplXzhkYVlKbHd6ZmJ0UWFXLTNHSEpBbXkyVFFkWFdXN01TT054SUNndVNJbW9uT2lOLTZJTlQ3Vlh2d1VNbU5lRVc?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxPN1k5S1ctdmt6QmxRSEJ4eHdxMndHcFBEeC03UHRHdERzd1BZX3hYRkc0WjF3Qzg1QXhWZHZPUzFyYmRrR3FaZklFUTdKR29ZYml0RW9pTDVWT1o2dGRvWWhEQlcwVEhEWDF4TG9jZ0Z5dnFqZ3BmQUpOMDFPS2VNMFZEUkNCZHd5ak84?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxOSEtyWTJmZGZ3d0VpOVJtOGlSdWo2OEVoVmxsbkdnR0pENjZSd2VmMklGaFRacjlBQVNueWpQamllRVBha09IM3BVcjVrZ2g1bEMyYko3NVFvTGJCNWwtd25taGhSeVI3ZDBOWFZ4d3IzeHEwNXY4WXRtaGZWQS1BNWtiOGcySTl4ZE15d1ktQUJjN2h3UHZyNW1qS0IxYk93amxFcE5ZbjY3QzRJVF9MRjZCOW1vYkxGanl2RQ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNT1ZWV245S1M1R2I2RVIyNHprYlZwcGN1eGlRWE9ZNTJYd0Q3V2xyb0FFZWdNcFRhVHVPVUtKdEdrYmd4bDlNbkRkdTNFazJLUU1wS0g1WlVFd3U3YU1pbkl4R09QVmFkVEZYMTNjU1FJbnU0bGY5Mk9zNWxFcWV2Y0h1aDF1aGlnYjBmNk53LU5TaHVwdTBmRjd3?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxOZWlMZ2JfQi1mSmxiLS00Mml1VDR1Q0tuVjZSaks4dHh6bU5Ld0oxQ01QUVhtN0x6c3Q0cmtFVzBoUC1jNzB3TTRUdmU5TTJZUk01blptY09QV0o5UHpxdzRPUzVrSWNsaTkwMktGLUhNYktFNWVIb0pYc2Riemt4WnlSd01oZFMtYVpFUHlIT2lUT1FJalJVQ2lKalpfY2dtS0VrS2xnRDl0NzhqUFdjVGxUQlFEUXItd0ctM1BNTXJiaU9p?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTE5oaTFTRjBXY0FMeFFPa0lVSnF5VHFYVEx5MmIxLWJuZXJMN2xINVkwSDdqS0FmQXhYbGM3d2lxcjh4bVJjcnhsZXlOZFRYbHJxdVVvbzlRbk5tWDRfVXpCb2l6TDBnRDZtd1BGdFhucnR5SkpxTUZ6bHZsaEpXZw?oc=5
- https://news.google.com/rss/articles/CBMigAFBVV95cUxPMGFXeDBPQXVQOWxaWGJlY2VxMWIxSXJ0U0hTaXNucFktZVBlUENGbXEweUU0VXNSbUFGTEhienE0MmpibTIzeEp1TWFSZjlSb01hZ2pvc2FBQ01OcFE1Smk3MVFQOXhSSEJHeFplTlpOMjBfbzdQS1VtVTh4cWxmTQ?oc=5
- https://news.google.com/rss/articles/CBMifEFVX3lxTFBkeThCOUJKVXM5alhlRV9IV08ycTRLZmdwWDlWVkJ1M1ViVnhOSG9tNkxtVkhoRW15VG1hUUthYmNwUEpCYTVwOG9nWGYzdFQyZUthaHhULXJFdDhsLUQwWU9tdjhPQzQ2eXl2QVBIUTQyRXEwYlpZVWhtdjI?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxNRHppYVF4UlRjVERuWnA5WUNMVTNTUVJNNWY5Q2RzZmZUNGJXNFZ3SW5XdkJ4cXZORFdxbEZ2R1dSN3BrVGhtcENqUC12bm9fNGlueE50S3BiNDNDdHZId1FmQjZ1Rkx0MnFiMVpZYndnQmsybEQ4Rnk2RlZiay0tdmdJd3JKVi1aVmpkQ2V4M2VrcW4xbGpHUDNPWkhEcmxlVW04OGRwUTRRaUNxclNMUjFiVEhnQ1lnZ1JhNnZ6clVIbWV0clZ3U1hzNDJDWFVC?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxON3V6WEZ5MTczaE84bktQaVNVMWY0d1ZBTDZhZW92R2pQX2RzUnZZYVJ4bzVCMTA4R0Mtbk9hUWV0cnJSdkh2MktNVjAyaFJMTVB1NEFram1EcnlqOVRHdWRMa1kwUDBJWEhRZ0ZVRkxVV0FabGtVa1NCREhWMjBkZ1N2c29mYzVodFV4T2RXdUJCMGRzQmF1MzEzTQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
