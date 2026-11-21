# AMZN Intelligence Report

- ticker: **AMZN**
- Report as_of: **2026-11-20**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/AMZN/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMZN/key-statistics/
- AI analysis snapshot as_of: **2026-11-20**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-21T05:43:01.921789+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 4, 'ai': 10, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261120T053808Z-e360129e/AMZN** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 12 named publishers; 3 exact duplicates; 22 HTTPS source links; largest publisher share 27.27%; oldest publication 2026-11-13

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 246.8200 |
| Return 1D (%) | -4.0992 |
| Return 1W (%) | -7.4402 |
| Return 1M (%) | -6.0199 |
| Return YTD (%) | 6.9318 |
| Return 1Y (%) | 13.6686 |
| Annualized volatility (%) | 34.3207 |
| Beta vs SPY | 1.2990 |
| Max drawdown (%) | -19.6419 |
| Sharpe (rf=0) | 0.5426 |
| Downside deviation (rf=0, %) | 21.1905 |
| Sortino (rf=0) | 0.8788 |
| Historical VaR 95% (1D, %) | 3.2202 |
| Historical ES 95% (1D, %) | 4.1300 |
| Correlation vs SPY | 0.5410 |
| Tracking error vs SPY (%) | 29.1782 |
| P/E (trailing) | 19.95 |
| P/B | 4.35 |
| EV/EBITDA | 15.56 |
| Revenue growth (%) | 12.10 |
| Forward P/E (estimate) | 22.59 |
| Gross margin (%) | 51.37 |
| Operating margin (%) | 13.09 |
| Return on equity (%) | 27.42 |
| Free cash flow yield (%) | -1.30 |
| MA50 | 255.0320 |
| Close vs MA50 (%) | -3.2200 |
| MA200 | 245.1506 |
| Close vs MA200 (%) | 0.6810 |
| RSI (14, Wilder) | 42.3032 |
| MACD (12,26) | 0.9425 |
| MACD signal (9) | 1.9857 |
| MACD histogram | -1.0432 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMZN': 287, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 246.8200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -4.0992 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -7.4402 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -6.0199 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 6.9318 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 13.6686 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 34.3207 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.1905 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.8788 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.2202 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.1300 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5410 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 29.1782 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.2990 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -19.6419 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.5426 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 22.5900 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 51.3740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 13.0870 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 27.4160 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: -1.3014 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 19.9531 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 42.3032 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.0432 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -3.2200 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 0.6810 -> Slightly above the moving-average trend level.

## TAILWINDS

### Amazon Stock Moves Higher: What's Going On?
- Summary: Amazon Stock Moves Higher: What's Going On?
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOd3EzOU9yRkc4NDAwWmxwN0dpeF9DdHJpNFpmN1hfV2poTUZkY21xcW1jNXAyR1BIU3NDZnpPQ0M3Z2NYMG1xeTAzRXpwTUplOTB5SHZ0R2xtNjNmajRrVWxCTVl0ZGpiUEtnS1FRRFpIMUE2dFlYZUo2WXFEVXNkM1JEYU1DdW5vS05YbXdwcW10dWJwS0ltdDVQd0xBLXVfOENXRUdn?oc=5>

### Amazon.com (NASDAQ:AMZN) Stock Price Target Raised at Oppenheimer
- Summary: Amazon.com (NASDAQ:AMZN) Stock Price Target Raised at Oppenheimer
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxPUENIZzZ3ZEZURzJfdzgteDlHYTJZckpaZWZQeFhXeXhfdWlaSzhxZ1pURG1UckNleDFEZVU3V2l1X3dlZkFLdE5EbXJyWTh3Y2Q4VmhkbmtubXhWZVB3NEVNeUtZSVloYXpoejdlMTNERHFhUXg4WU5RM3hONlo4TlNkM0ctTFpEN0ZJZElfcGtoNGFTbEFwVkc1Z3d2c0tuM2NIQWZMcVBzbVE5WG9rN3hNSW1GazhGaVpxV2kycF9KUQ?oc=5>

### The Amazon Kindle begins its 20th year of upending the bookstore model (AMZN:NASDAQ)
- Summary: Amazon’s Kindle celebrates 20 years, continuing to disrupt traditional bookstores.
- Date: 2026-11-19 | Impact: medium | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxQMENycjlaSV9FRXRpTkNqM09GYVZKZ3FOQlFNM0xDTGZ2TUJLN0t4R0txOGcybHVOYnJQbXpHa1NUQmp3OFM1Y0kyUWE0MEZjYlphUDRMM1VydTR3WXEzOEFOcFY5QktKTDRLUlNtLTZ2dWJfTTc3WE5MZDExOFlLZ1VxWlkySC1QTlJrY0dFb2ZHVUZvWF9QVVZhYm04VW9lZ192WnpoajBmMEVy?oc=5>

### AMZN Stock Rebounds Despite the UBS Downgrade, as Amazon Anthropic Investment Could Be Worth $150B
- Summary: Amazon's potential Anthropic investment boosts confidence, driving stock rebound.
- Date: 2026-11-19 | Impact: high | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxOZFNiUFJsMmw0dEhwOTdjNWtNRU54Z3hrSmV4LXNOMnMtTnZLcUNod1VNcUNjOVNCY0pvWWZKLXdHRTNVOVI2RzR0bDJEdlhuRzRvTUhLYUJ4a1hCcEdRRXRDakNPak02RnRUOGZ5cHRuRjZWSUsxV003ZVFveUFVTFlVc2M4VTZPWWs5aEJSQzZ6bGlmLWt0V2E2S2ZZR0VlSW5wdko1c2REM3pvUnl4X1hscjVBN29hZmJJZUZsR1FyUTd5RlgyTHNCQU41OExSLWIwaGRn?oc=5>

### Amazon (AMZN) and Big Tech Are Spending Heavily on AI – Here’s Why Investors Aren’t Panicking
- Summary: Amazon’s heavy AI investment signals continued innovation, reassuring investors.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOMXdBQUpoQ2EwOFVBdW5HQWtaTXdVVTJqbjJZczdqRFZJdDJ3bHMzQmVQU2RVTF9ISmNxcFRXV2VJeWdDNURIZ0duc2pTX0lVZmE4WTREb3NaQmIyM1JfMzBqNFpENlBjTEhoVlZPc3I1bHdkVFowWEkyWXFib1hDbWF6bUJKS2pobVg1OW5pZFZqUElibGNJVQ?oc=5>

## HEADWINDS

### Amazon Stock (AMZN) Falls 3.9% After Anthropic IPO Debut (Nov 19)
- Summary: Amazon Stock (AMZN) Falls 3.9% After Anthropic IPO Debut (Nov 19)
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigAFBVV95cUxOejFaODVKV0NVTXhtWFRJTjNhVmh5SFhiRl85T3VIYm1hUWZJeUF4RENfNFlQc2NLN2NBUFROSk9aRE8wN3dsdUNrTFJHR0h2NDZGTTczNld3NVRsRlBYY1lldHYxckZnODF5TTZHRm12Qk5RNThEVWxhZWVFYlpNbQ?oc=5>

### Will Amazon stock avoid deeper losses amid overbought warning and weak momentum?
- Summary: Amazon stock may face deeper losses due to overbought warning and weak momentum.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxOdWVNdkhlSWIxTzZFeU16ZC1MV3NENEtiME1BVDA4WWx4NWRqeG5EaU9KdnlvWnZSV0F4VUV4cG1lWldPMHF5TGF2WW0tOXhsdE8wbU4wVWZhNnJEdlI0TjY5OURGeFBvZ3VBZXJid3ZNeVVvd1R3RkZJcVY1YW5JVWRyLV9VN1d2cE5MNndlaFFSQQ?oc=5>

### New York City legislation could upend Amazon's delivery model (AMZN:NASDAQ)
- Summary: NYC legislation could disrupt Amazon's delivery model.
- Date: 2026-11-19 | Impact: high | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQMm14N0pvX2NlNEJxQW5UZWJqX3pyQVVoNzJZdGpFTG9WeWZUTVNtTnZRZWZ5SkxPUVNMQ2EwM3I5SFllM042QVhXd0c3a3JuM2ozeTVlX2JnTk9mT1VDNkdBVExxZnF2UFRqYjJTUmx5bDRfLWFfM1FEZEQ2UkM5V2R6N19Ibm1TS294Z3M4cFhIVEMwckwxN05qSG9QSkE?oc=5>

### Stock Market Today, Nov. 20: Amazon Shares Slide on AI and Mega-Cap Tech Sell-Off
- Summary: Amazon shares fell amid broader tech sell‑off.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxOZ3Q4VjNVRWVxOW90cDAtdDVDc1V0eXZGZ3gxbHhCQlhGUC1aTFNqTmtrU055TklQUjZreGR5NkRHU1FvblFOajBsWnVncTVhVnA3NTEzaWlQUFh0UjZMR0FDa2pINmlZSnItYmtHMDJ4TnhRclBFbnJzVXFvalg2UEJhQlZkTmJMQnc1dkJ2MVF5dTBFM3RYY3VBanF1blJOYzUxbGF2cHhvY2FBV3hXcURYb0VWamxSZVRxN3BWSGZoQWtqMEtaaWJ6SFFXNjBjbmtvOVFB?oc=5>

## CATALYSTS

### Amazon (AMZN) Stock Trades Below Fair Value As Its 82% Run Continues
- Summary: Amazon (AMZN) Stock Trades Below Fair Value As Its 82% Run Continues
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQUUtfMDhmNWV5dFk3RkdyTDhlTi1NZ2U1QmVMXzBhWmZwWHlGWktLSk1kbUFJUTVEUjYybDFxT2NJMjFRa2lySmw2bkVSdXFtcnpxaEFsbWF1MEhPX3FVLUxFSXAyTmM4LXJwVUVSS29KTWtxejlYYjZVejNGTW9FbXpmUFBzRE53Yi11TnBUVnAyYTBLNllfQ2E2OA?oc=5>

### Anthropic’s New IPO Filing Shows Amazon, Google Will Own Over A Quarter Of The Claude Maker
- Summary: Amazon will own over 25% of Anthropic after its IPO filing, indicating a significant partnership and potential AI collaboration.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNWnBIQWE0a2JUME11UzNpeTZUa0lqOEg0aFNMT05BV29YVldtdzNISHM1OWtrdHZsYkRHc2xTZmFjekh4dTltVEpROVRsZlFjcW8xR21QZ2t2aXpNcHNpb2QyU0lkdU5aZXV6bFVkdXNES09NRnh2MHJTeER1R2hud3o1UWdkSmR5ZnZoQmpRQjhvQk5nTlZtVnBMS1FGUDA?oc=5>

### Amazon and Alphabet Will Own Over 28% of Anthropic After Its IPO. Here’s What That Means for Their Stocks.
- Summary: Amazon’s stake in Anthropic enhances AI capabilities and market influence.
- Date: 2026-11-18 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxOYU1Lcy0yRzhtLVRmZ003M0VQVVJTbUF3ZEFXMVItd3JjdElrZVdYalkzWjNsVXNvaDkzcHYtZHBEWnRVREw5T2YzaHZNUEQtRVJEeVVWUlE0WDUwMF9PXy1zS05FMFlaS0Myc3ZCVHFWVmVsYXd0VXBHQl9qOXhXMFFNQm9iaWUtbjl4VW9ZUFg1Y3VnSWIwZHl6c2dscnNUMWhFRklQZGc?oc=5>

## RISKS

### Amazon: The Age Of Inference (And Big E-Commerce Profits) (NASDAQ:AMZN)
- Summary: Amazon's inference tech promises growth but may face execution risk.
- Date: 2026-11-16 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNQnRLX2xlM3NNZ3ctbTl3OF9OdlRwYktiRHBTeUN1bjZNRG0yTFBYaGw5OTdaVXRHcEVrMWt6WlRJWXpLT05xVEJoSFJnUEgxSDg0R1pmYXFMMWlYX2U2QU5kWlZtTUx0eWpWVjFxSnNaNWhRS0tIWUdOUkRkZk5td2dRanFxR1ZyNklUS2hpUXJKS1hT?oc=5>

### Can Amazon's Ad Revenue Growth Continue to Underpin the Stock's Value?
- Summary: Uncertain ad revenue growth may limit future valuation support.
- Date: 2026-11-20 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi7gFBVV95cUxNTE5US1pSWHk3ZXZ4ZkZyX1hRVExHTmowUmtQajBLN3h5Qlo4Qjk5bWVMYXdrUFU1cXlEejd4UTNhTnhVLUIxRE91cnM1YkJ4akMtQlE0YUhaN0VnWnlqX3hMRWNRcnBrX1kwZUVKX2lmeDFJY29xYXF4UlNUMjdmSWxXRG5MS0tDMG9VV3poYkpKWjZGWUt1TUVfVlpUM1gtTmdQU0FEUXlXOFBTOWMtYTZWVElrOXVGZ05oWGoySEw1cHVMSjUwYTB2RlFUMll1WFBhcG1ZT19TYU9yMzRFTGF1NWlHXzdZY2NZVVhn?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMZN** | **19.95** | **4.35** | **15.56** | **12.10** | **2,668,898,811,904.00 USD** | **13.67** |
| WMT | 46.36 | 10.34 | 24.52 | 5.90 | 1,018,236,174,336.00 USD | 20.46 |
| MSFT | 25.29 | 7.65 | 17.83 | 18.80 | 3,598,139,523,072.00 USD | 2.11 |
| GOOGL | 13.85 | 4.95 | 17.06 | 24.70 | 3,261,475,323,904.00 USD | -8.11 |

Peers fetched as_of: 2026-11-20; AMZN reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-29
- Next expected earnings: 2027-02-04 (yfinance; expected dates may change)

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
- Filing date: 2026-10-30
- Revenue (latest available single quarter): 201,944,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 20,685,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMipgFBVV95cUxOd3EzOU9yRkc4NDAwWmxwN0dpeF9DdHJpNFpmN1hfV2poTUZkY21xcW1jNXAyR1BIU3NDZnpPQ0M3Z2NYMG1xeTAzRXpwTUplOTB5SHZ0R2xtNjNmajRrVWxCTVl0ZGpiUEtnS1FRRFpIMUE2dFlYZUo2WXFEVXNkM1JEYU1DdW5vS05YbXdwcW10dWJwS0ltdDVQd0xBLXVfOENXRUdn?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOMlZzcndHVHcxM3A0VFVKY2NVZUhMejNRLXJJVjZBV1RiR3o1cXk3c28xcnRNbjAtTl8wUmtsUVFxc1RUZGxtNzVza3Y5cmNoZTF5dExRNUNuWnRSV0RFU1BFaFVxeHd2VHljbW5iUTVQMFR2QmR6VDN0Q1VLazNjZXRwVU81b0M2MHVXY3AydVpXb1FXQTBiMnpQLXBrR1MxQTVXZUJn?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxPUENIZzZ3ZEZURzJfdzgteDlHYTJZckpaZWZQeFhXeXhfdWlaSzhxZ1pURG1UckNleDFEZVU3V2l1X3dlZkFLdE5EbXJyWTh3Y2Q4VmhkbmtubXhWZVB3NEVNeUtZSVloYXpoejdlMTNERHFhUXg4WU5RM3hONlo4TlNkM0ctTFpEN0ZJZElfcGtoNGFTbEFwVkc1Z3d2c0tuM2NIQWZMcVBzbVE5WG9rN3hNSW1GazhGaVpxV2kycF9KUQ?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxQMENycjlaSV9FRXRpTkNqM09GYVZKZ3FOQlFNM0xDTGZ2TUJLN0t4R0txOGcybHVOYnJQbXpHa1NUQmp3OFM1Y0kyUWE0MEZjYlphUDRMM1VydTR3WXEzOEFOcFY5QktKTDRLUlNtLTZ2dWJfTTc3WE5MZDExOFlLZ1VxWlkySC1QTlJrY0dFb2ZHVUZvWF9QVVZhYm04VW9lZ192WnpoajBmMEVy?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxOZFNiUFJsMmw0dEhwOTdjNWtNRU54Z3hrSmV4LXNOMnMtTnZLcUNod1VNcUNjOVNCY0pvWWZKLXdHRTNVOVI2RzR0bDJEdlhuRzRvTUhLYUJ4a1hCcEdRRXRDakNPak02RnRUOGZ5cHRuRjZWSUsxV003ZVFveUFVTFlVc2M4VTZPWWs5aEJSQzZ6bGlmLWt0V2E2S2ZZR0VlSW5wdko1c2REM3pvUnl4X1hscjVBN29hZmJJZUZsR1FyUTd5RlgyTHNCQU41OExSLWIwaGRn?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOMXdBQUpoQ2EwOFVBdW5HQWtaTXdVVTJqbjJZczdqRFZJdDJ3bHMzQmVQU2RVTF9ISmNxcFRXV2VJeWdDNURIZ0duc2pTX0lVZmE4WTREb3NaQmIyM1JfMzBqNFpENlBjTEhoVlZPc3I1bHdkVFowWEkyWXFib1hDbWF6bUJKS2pobVg1OW5pZFZqUElibGNJVQ?oc=5
- https://news.google.com/rss/articles/CBMigAFBVV95cUxOejFaODVKV0NVTXhtWFRJTjNhVmh5SFhiRl85T3VIYm1hUWZJeUF4RENfNFlQc2NLN2NBUFROSk9aRE8wN3dsdUNrTFJHR0h2NDZGTTczNld3NVRsRlBYY1lldHYxckZnODF5TTZHRm12Qk5RNThEVWxhZWVFYlpNbQ?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxOdWVNdkhlSWIxTzZFeU16ZC1MV3NENEtiME1BVDA4WWx4NWRqeG5EaU9KdnlvWnZSV0F4VUV4cG1lWldPMHF5TGF2WW0tOXhsdE8wbU4wVWZhNnJEdlI0TjY5OURGeFBvZ3VBZXJid3ZNeVVvd1R3RkZJcVY1YW5JVWRyLV9VN1d2cE5MNndlaFFSQQ?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQMm14N0pvX2NlNEJxQW5UZWJqX3pyQVVoNzJZdGpFTG9WeWZUTVNtTnZRZWZ5SkxPUVNMQ2EwM3I5SFllM042QVhXd0c3a3JuM2ozeTVlX2JnTk9mT1VDNkdBVExxZnF2UFRqYjJTUmx5bDRfLWFfM1FEZEQ2UkM5V2R6N19Ibm1TS294Z3M4cFhIVEMwckwxN05qSG9QSkE?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxOZ3Q4VjNVRWVxOW90cDAtdDVDc1V0eXZGZ3gxbHhCQlhGUC1aTFNqTmtrU055TklQUjZreGR5NkRHU1FvblFOajBsWnVncTVhVnA3NTEzaWlQUFh0UjZMR0FDa2pINmlZSnItYmtHMDJ4TnhRclBFbnJzVXFvalg2UEJhQlZkTmJMQnc1dkJ2MVF5dTBFM3RYY3VBanF1blJOYzUxbGF2cHhvY2FBV3hXcURYb0VWamxSZVRxN3BWSGZoQWtqMEtaaWJ6SFFXNjBjbmtvOVFB?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQUUtfMDhmNWV5dFk3RkdyTDhlTi1NZ2U1QmVMXzBhWmZwWHlGWktLSk1kbUFJUTVEUjYybDFxT2NJMjFRa2lySmw2bkVSdXFtcnpxaEFsbWF1MEhPX3FVLUxFSXAyTmM4LXJwVUVSS29KTWtxejlYYjZVejNGTW9FbXpmUFBzRE53Yi11TnBUVnAyYTBLNllfQ2E2OA?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNWnBIQWE0a2JUME11UzNpeTZUa0lqOEg0aFNMT05BV29YVldtdzNISHM1OWtrdHZsYkRHc2xTZmFjekh4dTltVEpROVRsZlFjcW8xR21QZ2t2aXpNcHNpb2QyU0lkdU5aZXV6bFVkdXNES09NRnh2MHJTeER1R2hud3o1UWdkSmR5ZnZoQmpRQjhvQk5nTlZtVnBMS1FGUDA?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxOYU1Lcy0yRzhtLVRmZ003M0VQVVJTbUF3ZEFXMVItd3JjdElrZVdYalkzWjNsVXNvaDkzcHYtZHBEWnRVREw5T2YzaHZNUEQtRVJEeVVWUlE0WDUwMF9PXy1zS05FMFlaS0Myc3ZCVHFWVmVsYXd0VXBHQl9qOXhXMFFNQm9iaWUtbjl4VW9ZUFg1Y3VnSWIwZHl6c2dscnNUMWhFRklQZGc?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQaV9WVUdzMk5hM0tDU1FaeFB0dkpRenRRaUFFWWdFaVZCVUdpT3hVc3cxeWZfeTlQNjVBVHJjRzdxS1dsclRZeHBIblVhQWkzMEliOU5vUzVFODgtQUI3VHJjVnVVZGd4V1lnNUVvWVdBc0hzUW5wX1JlZ2FMV0hVOXViZEFfTE1WcDFpVE1ySXRrZkVGRk5F?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNQnRLX2xlM3NNZ3ctbTl3OF9OdlRwYktiRHBTeUN1bjZNRG0yTFBYaGw5OTdaVXRHcEVrMWt6WlRJWXpLT05xVEJoSFJnUEgxSDg0R1pmYXFMMWlYX2U2QU5kWlZtTUx0eWpWVjFxSnNaNWhRS0tIWUdOUkRkZk5td2dRanFxR1ZyNklUS2hpUXJKS1hT?oc=5
- https://news.google.com/rss/articles/CBMi7gFBVV95cUxNTE5US1pSWHk3ZXZ4ZkZyX1hRVExHTmowUmtQajBLN3h5Qlo4Qjk5bWVMYXdrUFU1cXlEejd4UTNhTnhVLUIxRE91cnM1YkJ4akMtQlE0YUhaN0VnWnlqX3hMRWNRcnBrX1kwZUVKX2lmeDFJY29xYXF4UlNUMjdmSWxXRG5MS0tDMG9VV3poYkpKWjZGWUt1TUVfVlpUM1gtTmdQU0FEUXlXOFBTOWMtYTZWVElrOXVGZ05oWGoySEw1cHVMSjUwYTB2RlFUMll1WFBhcG1ZT19TYU9yMzRFTGF1NWlHXzdZY2NZVVhn?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
