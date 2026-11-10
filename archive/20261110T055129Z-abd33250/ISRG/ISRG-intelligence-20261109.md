# ISRG Intelligence Report

- ticker: **ISRG**
- Report as_of: **2026-11-09**
- Market data as_of: **2026-11-09**
- Quant sources: https://finance.yahoo.com/quote/ISRG/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ISRG/key-statistics/
- AI analysis snapshot as_of: **2026-11-09**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-10T06:06:02.720771+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 18, 'rule': 2, 'ai': 10, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **15** exact headline/source/date matches; prior report **20261109T043242Z-c8e908de/ISRG** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 2}
- RSS source audit (metadata only, not article fact-checking): 18 unique headlines; 8 named publishers; 0 exact duplicates; 18 HTTPS source links; largest publisher share 38.89%; oldest publication 2026-11-03

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 460.5600 |
| Return 1D (%) | 1.7138 |
| Return 1W (%) | 5.4227 |
| Return 1M (%) | 8.6329 |
| Return YTD (%) | -18.6807 |
| Return 1Y (%) | -17.7571 |
| Annualized volatility (%) | 35.5203 |
| Beta vs SPY | 0.9097 |
| Max drawdown (%) | -43.9960 |
| Sharpe (rf=0) | -0.4563 |
| Downside deviation (rf=0, %) | 26.2374 |
| Sortino (rf=0) | -0.6178 |
| Historical VaR 95% (1D, %) | 3.2284 |
| Historical ES 95% (1D, %) | 5.1297 |
| Correlation vs SPY | 0.3507 |
| Tracking error vs SPY (%) | 33.2879 |
| P/E (trailing) | 55.69 |
| P/B | 9.99 |
| EV/EBITDA | 34.84 |
| Revenue growth (%) | 21.70 |
| Forward P/E (estimate) | 36.94 |
| Gross margin (%) | 66.64 |
| Operating margin (%) | 33.29 |
| Return on equity (%) | 17.93 |
| Free cash flow yield (%) | 2.15 |
| MA50 | 411.6890 |
| Close vs MA50 (%) | 11.8709 |
| MA200 | 430.8826 |
| Close vs MA200 (%) | 6.8876 |
| RSI (14, Wilder) | 59.7193 |
| MACD (12,26) | 13.3494 |
| MACD signal (9) | 12.8878 |
| MACD histogram | 0.4616 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ISRG': 278, 'SPY': 278}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 460.5600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.7138 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 5.4227 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 8.6329 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -18.6807 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -17.7571 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 35.5203 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.2374 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.6178 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.2284 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1297 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3507 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 33.2879 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.9097 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -43.9960 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.4563 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 36.9371 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 66.6420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 33.2860 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 17.9320 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.1515 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 55.6904 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 59.7193 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.4616 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 11.8709 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 6.8876 -> Clearly above the moving-average trend level.

## TAILWINDS

### Intuitive Surgical Inc. (NASDAQ:ISRG) Stock Analysis — Sharp Gain, Valuation and Momentum Review
- Summary: Intuitive Surgical Inc. (NASDAQ:ISRG) Stock Analysis — Sharp Gain, Valuation and Momentum Review
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxQNXdmQTdVbHVYck4xWE9wMElucXViSUxWMzhJcTRka194a0pYLURJTDVEUUpkLWhHVDJzN2FSWnRMVFFPeGRqSzgtOVM5ajJ4aXhTSU02RTJVcVQ5WTUwVUhHeWlJYzFoYkZMOFVVT3Fid0NSakFMSmw5Y21MOUtET1RXejBRa2xwbmlZOTJpZi1rZGV4cDR4NFplMmx4UE5tYUM2bWU1UWdMSXdWdTMxTjZtdjFEWXhkd2p2NDZfMUlfc2Z2UmFMRmhYZllRYTQ5RWxFaUpsVEc?oc=5>

### Why Intuitive Surgical (ISRG) Just Cracked the Top 10 Best Healthcare Stocks List
- Summary: Intuitive Surgical ranks in top 10 healthcare stocks, boosting investor confidence and market perception.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNa2J6QkthZXhYdW0wV0pTZ3hJSldUMjNCNTBiRXZjSWZaMzhMSGYwRHhDVmRGMHNvNHNxVS1ab1p5NlN2b2U1V0g2V0s2cWZVUi1UVGotaGRRTS1HRERNcTFnUnJkU3RXcWpSVTRwcGRKd3lvWjI0akhLR0JDc3V5ZzI5cEJTV0FGamgyQ2d4ZGljTzBmbUxDXw?oc=5>

### Intuitive Surgical Surges 5.4%, Adding ~$9 Billion in One Session
- Summary: Stock price jumps 5.4%, adding ~$9B in one session.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOYVkwRnFNQk9ZV2VhaHJnMnBIbklPVEd3cHc4elB3VldOSVRwS0RvRm9yQWdWNjR6LThPVlU5ZTNjSzY5N3RqV3hPUkotZWE5VnEyTi1iMDNNengzZ2R5Q1lYWmpOVnI0MWZwLVU0MEFWOUtzT0JNT081dEdwOW5pN3VGNmF1OTMyd3VRVGh1OWNZNEhZ?oc=5>

### ISRG Gains 7.8% in 6 Months: Will the Share Price Recovery Continue?
- Summary: ISRG stock rose 7.8% over the past six months, prompting questions about the sustainability of its recent price recovery.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxPTWUxRVd6d0RtX0JSSmpkcUpIdWpEeHlyZnR1VWNDTWJfcGhoeUhZNVZUbVVDSi0yUF9SYk1pWEhuZm4zWnM0STU3eWlqNlBnaVFOTHV3VTJNcXVoUDFUYkowWWU0TkFDNHd5SXpVTGZzc1pCUlEzTmJJeWppSmRJOXJCRWFTZHdS?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Intuitive Surgical (ISRG) Just Grew Revenue 22%. Why Is the Stock Still Down This Year?
- Summary: Intuitive Surgical (ISRG) Just Grew Revenue 22%. Why Is the Stock Still Down This Year?
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOV1JDa3pWOXNYTDdmclZzOG0yMVlIUElneWlQU05HbzZKQWdTdHZrVlZaaVhtMFcwT1RoUjMzaVdQY2tYeThqXzEtNWxNZGxZNUFDbEhCOU5WeFptd3ltY2lmTTVBR3NnLXlnS2RwUFNpUkJPVXBTQ1d2Zk5jWFJfLVYxelNTcFV1ajA0RDh6cjhLbm5ISkRsLWxQN29xb3M?oc=5>

### Can Intuitive Surgical Stock Hit $700?
- Summary: Analysts speculate a $700 target, reflecting bullish sentiment on future earnings and market positioning.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNb0xHeHE2cUExVEN3V3U2V3RIOHUwNVY0OXZMX3ptYm9pUzV2dnpScmkwWFVhdzZGQWFXOTMwTUtac3BkV2FxYy1ZOENtSElINFQ3UWkxRkxzZGxEd0pCY2hPZ1lBUWVSc3JRQTljZmFGTkQ5NnhsY0ltQVlpQy1kRy1Wb1c3TzNrSm5yVkl1dEU2NkxWZXFYaHVvQWg3Zw?oc=5>

### Is Intuitive Surgical’s Next Big Thing Already Here?
- Summary: Potential new product or technology could boost future growth.
- Date: 2026-11-07 | Impact: medium | Horizon: medium | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQcW1OWkpJQ09Hb1dSZkYxYXhCM0duU0hYcWNEbGx6bldFZk9DRGpGQzIwM0NfNDdhX1AwNUZka0NqQWZibXZsYS1SbGRndzBOSHhhaGg2M0doald6aHZWV1NNYUtvQ1lQZUU2OE52RkZmSDVlMnBQLWVKU2pBZlhvUktSWEF2SERzM3h0TW9fRWJtU1lEN2lqbEpNc1AzSkRONHJCZTZSZ1Jna2pjdFBueQ?oc=5>

### Intuitive Surgical, Inc. (ISRG) is Attracting Investor Attention: Here is What You Should Know
- Summary: Rising investor interest highlights potential growth catalysts and upcoming corporate developments.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPOUlwWU0ySTBLaFd0SW8taV9NMXY4UWIwTTBRUWJQQU9LN0pDMHJIN0VMQjhZUjJSN1FidlRFQ0FUZFFUaFF6bVljREJsSVJsUEFCWVpkbjBvQ29kVEpZNjdJSlg4Z25WT2laQzFicTkwcVVqXzJPYUtfYnNTQ1ViN3A2QWp1T3JBUDVQUmllOGx4YmY4YllVTWx5LTFXMmE0TC1aejZB?oc=5>

### How Earnings Upgrades At Intuitive Surgical Stock Have Changed Its Investment Story
- Summary: Recent earnings upgrades improve investment outlook.
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOWDU2bmdzM1BVb3E5VzZYWDJnOUhoZE1jOW1kQlBBSW1KMU5TYUplWi1sUDduVk9VSHlLandVdkh4MTY0UTExU05lZVR4QkFfTS0yZ0ZsLW1mZ2Z6OTFoYzRtUzRMSVowd2FGcXRlYUxUanVnOTRBLWEwVzVsbkJLU0J0RUlLdmRNMWhTdTQwZW9sSU9KREROR1ZuS2w2RWNFaUhZSlNB?oc=5>

### Intuitive Surgical Inc (ISRG) Stock Down 3.4% -- Now Undervalued? GF Score: 96/100
- Summary: Stock decline prompts debate on valuation; GF score suggests potential undervaluation amid market volatility.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxOY3N6YzA5cFhiUjdPSnN6cjQtXzVUUF9vTkFZSGR5MmxJYmNVTmZzcEtIS0xOdnV6LXFVUWRSZ2huWlhPQ3FfVzJkOXlMQXRjaFZmQUhlSG1TY2Q2QnpkQk9sblFiU1VNSUIya0J0dTZfUzRSVzBYZm1iMHNabllidExxZ25ka0F3eHNPZURPV05QR3RMWlZSYVlHU0Rkc09rc2hhMkE1WVpuVHV5N2JNNQ?oc=5>

### Intuitive Surgical Inc Stock (ISRG) Moved Down by 3.14% on Nov 6: Drivers Behind the Movement
- Summary: Price drop attributed to broader market trends and company-specific factors; investors should assess risk exposure.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNYzRMWnpSQVd0eDlIbnROTzZUekFNN2U3QjRVMEphdTZYM1hVY0JNOEdDem1BUm1CRC1oU0NoNDB2eWJwd2hBTEgtemktYTU3TE8zVU9XWDZXUWc5aDlSU2dMSGo5dlc5Smd2XzBubmFLMFFuZVB4Ml9JbWljbWtsWTBVSHRZUnJmOUdN?oc=5>

### Intuitive Surgical (ISRG) Moved, What Is Catching Investors’ Attention?
- Summary: Investors focus on recent company movements, though specifics are unclear.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxQS01JMGgyemdnckljSE01MnM0QnV2R2RVcGo5SkctZzZPQ1BKYktnOE9KcVUxS09PT01xODVsdFlKdzVjb1VZWnBQajMtMWlJOWRjRDh3TmJtazhQZHM3UzA3aUFKd2ZfRDlxWnBHVDhiekcwRFgyMEptMHJwVUI4MlFUZDVnelJUMHZOZlpReGxPbnA3SnJNVEVQLTZheXJIaWF5VnEyQ3VQcnNpUFNHQlE3X0ZaTnhiZ3ZpaGhqQUJmSFdGeFllN2V2dkFnRHdYbmpRTmp30gHbAUFVX3lxTFA1TlUxWlVEN3g1Y2RKd1RwV0t4MldtSmUxVUR4X3RhSFBrUmdYZE1EMzdsVlVhaXdIdTIxamw1Yk9ZTzN4VDZsXzVEWFZlSE5OLUZBbU9zTVIxcHhOa2tXMkx3S0tIT0ZCUmlrZXM5S3k4MHJWekRVcDdHeDlZNDkwenV0cEFKdmVxSVdkZ1d3U1JsSzRnWVo4UnkxTlpzODlNOEdYamJkQjJ6TkFuVW9pOHUzQk1MZE95RjVFZFdBZ01VQ3RkbWdmZDRxTEJnY0lQZWZfTXJPOEtlSQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ISRG** | **55.69** | **9.99** | **34.84** | **21.70** | **159,650,234,368.00 USD** | **-17.76** |
| MDT | 25.26 | 2.62 | 14.55 | 13.70 | 131,482,591,232.00 USD | 15.18 |
| SYK | 34.69 | 5.29 | 18.13 | 7.60 | 124,002,484,224.00 USD | -7.50 |
| BSX | 18.57 | 2.49 | 13.54 | 1.40 | 63,805,812,736.00 USD | -55.99 |

Peers fetched as_of: 2026-11-09; ISRG reuses existing data (market data as_of: 2026-11-09); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-20
- Next expected earnings: 2027-01-21 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-09

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMi2AFBVV95cUxQNXdmQTdVbHVYck4xWE9wMElucXViSUxWMzhJcTRka194a0pYLURJTDVEUUpkLWhHVDJzN2FSWnRMVFFPeGRqSzgtOVM5ajJ4aXhTSU02RTJVcVQ5WTUwVUhHeWlJYzFoYkZMOFVVT3Fid0NSakFMSmw5Y21MOUtET1RXejBRa2xwbmlZOTJpZi1rZGV4cDR4NFplMmx4UE5tYUM2bWU1UWdMSXdWdTMxTjZtdjFEWXhkd2p2NDZfMUlfc2Z2UmFMRmhYZllRYTQ5RWxFaUpsVEc?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNa2J6QkthZXhYdW0wV0pTZ3hJSldUMjNCNTBiRXZjSWZaMzhMSGYwRHhDVmRGMHNvNHNxVS1ab1p5NlN2b2U1V0g2V0s2cWZVUi1UVGotaGRRTS1HRERNcTFnUnJkU3RXcWpSVTRwcGRKd3lvWjI0akhLR0JDc3V5ZzI5cEJTV0FGamgyQ2d4ZGljTzBmbUxDXw?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOYVkwRnFNQk9ZV2VhaHJnMnBIbklPVEd3cHc4elB3VldOSVRwS0RvRm9yQWdWNjR6LThPVlU5ZTNjSzY5N3RqV3hPUkotZWE5VnEyTi1iMDNNengzZ2R5Q1lYWmpOVnI0MWZwLVU0MEFWOUtzT0JNT081dEdwOW5pN3VGNmF1OTMyd3VRVGh1OWNZNEhZ?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxPTWUxRVd6d0RtX0JSSmpkcUpIdWpEeHlyZnR1VWNDTWJfcGhoeUhZNVZUbVVDSi0yUF9SYk1pWEhuZm4zWnM0STU3eWlqNlBnaVFOTHV3VTJNcXVoUDFUYkowWWU0TkFDNHd5SXpVTGZzc1pCUlEzTmJJeWppSmRJOXJCRWFTZHdS?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOV1JDa3pWOXNYTDdmclZzOG0yMVlIUElneWlQU05HbzZKQWdTdHZrVlZaaVhtMFcwT1RoUjMzaVdQY2tYeThqXzEtNWxNZGxZNUFDbEhCOU5WeFptd3ltY2lmTTVBR3NnLXlnS2RwUFNpUkJPVXBTQ1d2Zk5jWFJfLVYxelNTcFV1ajA0RDh6cjhLbm5ISkRsLWxQN29xb3M?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxNb0xHeHE2cUExVEN3V3U2V3RIOHUwNVY0OXZMX3ptYm9pUzV2dnpScmkwWFVhdzZGQWFXOTMwTUtac3BkV2FxYy1ZOENtSElINFQ3UWkxRkxzZGxEd0pCY2hPZ1lBUWVSc3JRQTljZmFGTkQ5NnhsY0ltQVlpQy1kRy1Wb1c3TzNrSm5yVkl1dEU2NkxWZXFYaHVvQWg3Zw?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxQcW1OWkpJQ09Hb1dSZkYxYXhCM0duU0hYcWNEbGx6bldFZk9DRGpGQzIwM0NfNDdhX1AwNUZka0NqQWZibXZsYS1SbGRndzBOSHhhaGg2M0doald6aHZWV1NNYUtvQ1lQZUU2OE52RkZmSDVlMnBQLWVKU2pBZlhvUktSWEF2SERzM3h0TW9fRWJtU1lEN2lqbEpNc1AzSkRONHJCZTZSZ1Jna2pjdFBueQ?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPOUlwWU0ySTBLaFd0SW8taV9NMXY4UWIwTTBRUWJQQU9LN0pDMHJIN0VMQjhZUjJSN1FidlRFQ0FUZFFUaFF6bVljREJsSVJsUEFCWVpkbjBvQ29kVEpZNjdJSlg4Z25WT2laQzFicTkwcVVqXzJPYUtfYnNTQ1ViN3A2QWp1T3JBUDVQUmllOGx4YmY4YllVTWx5LTFXMmE0TC1aejZB?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOWDU2bmdzM1BVb3E5VzZYWDJnOUhoZE1jOW1kQlBBSW1KMU5TYUplWi1sUDduVk9VSHlLandVdkh4MTY0UTExU05lZVR4QkFfTS0yZ0ZsLW1mZ2Z6OTFoYzRtUzRMSVowd2FGcXRlYUxUanVnOTRBLWEwVzVsbkJLU0J0RUlLdmRNMWhTdTQwZW9sSU9KREROR1ZuS2w2RWNFaUhZSlNB?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxOY3N6YzA5cFhiUjdPSnN6cjQtXzVUUF9vTkFZSGR5MmxJYmNVTmZzcEtIS0xOdnV6LXFVUWRSZ2huWlhPQ3FfVzJkOXlMQXRjaFZmQUhlSG1TY2Q2QnpkQk9sblFiU1VNSUIya0J0dTZfUzRSVzBYZm1iMHNabllidExxZ25ka0F3eHNPZURPV05QR3RMWlZSYVlHU0Rkc09rc2hhMkE1WVpuVHV5N2JNNQ?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNYzRMWnpSQVd0eDlIbnROTzZUekFNN2U3QjRVMEphdTZYM1hVY0JNOEdDem1BUm1CRC1oU0NoNDB2eWJwd2hBTEgtemktYTU3TE8zVU9XWDZXUWc5aDlSU2dMSGo5dlc5Smd2XzBubmFLMFFuZVB4Ml9JbWljbWtsWTBVSHRZUnJmOUdN?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxQS01JMGgyemdnckljSE01MnM0QnV2R2RVcGo5SkctZzZPQ1BKYktnOE9KcVUxS09PT01xODVsdFlKdzVjb1VZWnBQajMtMWlJOWRjRDh3TmJtazhQZHM3UzA3aUFKd2ZfRDlxWnBHVDhiekcwRFgyMEptMHJwVUI4MlFUZDVnelJUMHZOZlpReGxPbnA3SnJNVEVQLTZheXJIaWF5VnEyQ3VQcnNpUFNHQlE3X0ZaTnhiZ3ZpaGhqQUJmSFdGeFllN2V2dkFnRHdYbmpRTmp30gHbAUFVX3lxTFA1TlUxWlVEN3g1Y2RKd1RwV0t4MldtSmUxVUR4X3RhSFBrUmdYZE1EMzdsVlVhaXdIdTIxamw1Yk9ZTzN4VDZsXzVEWFZlSE5OLUZBbU9zTVIxcHhOa2tXMkx3S0tIT0ZCUmlrZXM5S3k4MHJWekRVcDdHeDlZNDkwenV0cEFKdmVxSVdkZ1d3U1JsSzRnWVo4UnkxTlpzODlNOEdYamJkQjJ6TkFuVW9pOHUzQk1MZE95RjVFZFdBZ01VQ3RkbWdmZDRxTEJnY0lQZWZfTXJPOEtlSQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
