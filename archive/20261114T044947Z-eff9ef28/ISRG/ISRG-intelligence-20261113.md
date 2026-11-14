# ISRG Intelligence Report

- ticker: **ISRG**
- Report as_of: **2026-11-13**
- Market data as_of: **2026-11-13**
- Quant sources: https://finance.yahoo.com/quote/ISRG/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ISRG/key-statistics/
- AI analysis snapshot as_of: **2026-11-13**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-14T04:58:03.241052+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 19, 'rule': 3, 'ai': 7, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **13** exact headline/source/date matches; prior report **20261113T045636Z-34122c9a/ISRG** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 19 unique headlines; 11 named publishers; 0 exact duplicates; 19 HTTPS source links; largest publisher share 21.05%; oldest publication 2026-11-06

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
| P/E (trailing) | 53.19 |
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
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 53.1882 -> High trailing earnings multiple under the research bands.
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

### Intuitive Surgical (ISRG) Stock Fair Value Edges Higher After Mixed Q3 Analyst Revisions
- Summary: Intuitive Surgical (ISRG) Stock Fair Value Edges Higher After Mixed Q3 Analyst Revisions
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPQW1hV1lMNFBYRmJWdW9OTDVTTDV6QktCT3hhMGFteTFYdGJ5dGxSci1TNk1pdkVBUUhuRlJJamNodjcya3o1NXh5aVZTUWU3b1NNekM5YWdyd2IxU00xZ3hRRXdWdG96YmRRZXhIWUF0aGZfR2FfNC0zR21JZ05KSzNhckdBQlBFcFctbDVRV0o5cUplWXpuMjhSaTNSVFlR?oc=5>

### Intuitive Surgical (ISRG) Just Grew Revenue 22%. Why Is the Stock Still Down This Year?
- Summary: Intuitive Surgical (ISRG) Just Grew Revenue 22%. Why Is the Stock Still Down This Year?
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOV1JDa3pWOXNYTDdmclZzOG0yMVlIUElneWlQU05HbzZKQWdTdHZrVlZaaVhtMFcwT1RoUjMzaVdQY2tYeThqXzEtNWxNZGxZNUFDbEhCOU5WeFptd3ltY2lmTTVBR3NnLXlnS2RwUFNpUkJPVXBTQ1d2Zk5jWFJfLVYxelNTcFV1ajA0RDh6cjhLbm5ISkRsLWxQN29xb3M?oc=5>

### Is Intuitive Surgical (ISRG) a Solid Growth Stock? 3 Reasons to Think "Yes"
- Summary: Analyst article highlighting growth potential for ISRG.
- Date: 2026-11-11 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPQnpLTmE0dklyYmp0MGJRU2hzQmQ2T2luWnppTmJFWl9rSWhXS3djTWNyS29RUTlpYXpXemF0SkdHUGZNOEp3ZXRiTnBlSHl3Nnp0Z01EcWhuekZ1OW0xX0hpdVpIS29PaHc5cG5VTDhLcHQ0d2RYU3ZYd3IzYnJfQ05ac3hlM0pudHY5QlZIU1haUHlYU0ZwWDBvSUk5eF9vckFn?oc=5>

### Intuitive Surgical (ISRG) Dropped, So What Is Driving Attention Now?
- Summary: Explores reasons behind recent price decline of ISRG.
- Date: 2026-11-11 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxOY0xpOFlBYVhVVWlXR3F0eC16UU9SYUdfLTFDM2JPVDAySjlPb0FycHNQTE84MEI2Y3ZucFFiSjU3S3RHa2p4d1doTk5VVWxuN25hNFlRYmp4VWV6U3l6WjVjSE5CNG9EM2daSlhCS2FGTTd3dmNmaVpiWnRhdUg0RVZ6cUF2akw4WlpCa01LanF4dw?oc=5>

### How Earnings Upgrades At Intuitive Surgical Stock Have Changed Its Investment Story
- Summary: Recent earnings upgrades improve investment outlook.
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOWDU2bmdzM1BVb3E5VzZYWDJnOUhoZE1jOW1kQlBBSW1KMU5TYUplWi1sUDduVk9VSHlLandVdkh4MTY0UTExU05lZVR4QkFfTS0yZ0ZsLW1mZ2Z6OTFoYzRtUzRMSVowd2FGcXRlYUxUanVnOTRBLWEwVzVsbkJLU0J0RUlLdmRNMWhTdTQwZW9sSU9KREROR1ZuS2w2RWNFaUhZSlNB?oc=5>

### Can Intuitive Surgical Stock Hit $700?
- Summary: Analysts speculate a $700 target, reflecting bullish sentiment on future earnings and market positioning.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNb0xHeHE2cUExVEN3V3U2V3RIOHUwNVY0OXZMX3ptYm9pUzV2dnpScmkwWFVhdzZGQWFXOTMwTUtac3BkV2FxYy1ZOENtSElINFQ3UWkxRkxzZGxEd0pCY2hPZ1lBUWVSc3JRQTljZmFGTkQ5NnhsY0ltQVlpQy1kRy1Wb1c3TzNrSm5yVkl1dEU2NkxWZXFYaHVvQWg3Zw?oc=5>

### ISRG Gains 7.8% in 6 Months: Will the Share Price Recovery Continue?
- Summary: ISRG shares up 7.8% over six months, prompting a review of price recovery.
- Date: 2026-11-09 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxOS0p0TFpDX1JNWG8xV2pYbUhidC1PTHoySVVCMkV3Wm9hdFhJZV92VGxlZnVYZURkQmpTMDI4SEpITEI1SldVOWpnZ1F4aUgtMUYtMGgzVURVOF9KNGlFdkUtcVJlemRoSVVweFNVWGUyM0RBRFVhOUpaR0xyT1ZfQTRxdmpabGk1NWdwQVJmdWN0MjFxSXB5OVhTSUJfdUhzOUcyN1o5MUMtQlJuOU8zc3k2VlgtSEl4UGlrVXBn?oc=5>

### Intuitive Surgical (ISRG) Moved, What Is Catching Investors’ Attention?
- Summary: Investors focus on recent company movements, though specifics are unclear.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxQS01JMGgyemdnckljSE01MnM0QnV2R2RVcGo5SkctZzZPQ1BKYktnOE9KcVUxS09PT01xODVsdFlKdzVjb1VZWnBQajMtMWlJOWRjRDh3TmJtazhQZHM3UzA3aUFKd2ZfRDlxWnBHVDhiekcwRFgyMEptMHJwVUI4MlFUZDVnelJUMHZOZlpReGxPbnA3SnJNVEVQLTZheXJIaWF5VnEyQ3VQcnNpUFNHQlE3X0ZaTnhiZ3ZpaGhqQUJmSFdGeFllN2V2dkFnRHdYbmpRTmp30gHbAUFVX3lxTFA1TlUxWlVEN3g1Y2RKd1RwV0t4MldtSmUxVUR4X3RhSFBrUmdYZE1EMzdsVlVhaXdIdTIxamw1Yk9ZTzN4VDZsXzVEWFZlSE5OLUZBbU9zTVIxcHhOa2tXMkx3S0tIT0ZCUmlrZXM5S3k4MHJWekRVcDdHeDlZNDkwenV0cEFKdmVxSVdkZ1d3U1JsSzRnWVo4UnkxTlpzODlNOEdYamJkQjJ6TkFuVW9pOHUzQk1MZE95RjVFZFdBZ01VQ3RkbWdmZDRxTEJnY0lQZWZfTXJPOEtlSQ?oc=5>

### Intuitive Surgical (ISRG) Stock Looks In Line With Cash Flow After A 45% Run
- Summary: ISRG stock aligns with cash flow after a 45% run, indicating strong financial health.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxPLXU0OUM4LWFjWXZGN0hScU9GQkxULVJoT256bEZocFV0WjRpUGlwSnZlbDJDampJM256QVFKcnU4VGVJQ3hXM3lLZXFrYTJjX2o3OUlBbXBLYlV0dHdqV0ZsNFJ5OUhUZFo3SGJIY3VwU2tBbC1sYjg3WWhEVk1oQlY2aGdxVTQxUzB0dDJfVTFtM01PbTY3clZqVk1YM0t5MmZiRW42R29fY194Q2I5cFREMnFra2NTaXpLOUFxRXI0d1VKamFad0YzektQcmtXb0hlZkRn0gHbAUFVX3lxTE5VNTVxX08tUDh3SmNHdl9Ca2tpQ3RoM0g4dGtiMHZrdXkzeXZsZmFwOFE0UWtpY2Y1ZmxhMWJLU09yaWQzdnZxMG13WU9IYWNyY2FtWE9WdVpHVjMxYWxFUzZaUWM4UmRYYUdXYjRyVC1TZ3ZucmFzZEJkdDdqcmFKblJlWnRrSWNZYUdsUXIyU1BPclM5VmpnaUVES3FLZmFpR29ob0RSRHVhWWdvWjNFWDVNTXJUUGJlN1huaE9ILTMtckc3MHJrb2xqRVIxOUdvdWg4VkdpcjB6aw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ISRG** | **53.19** | **9.62** | **33.52** | **21.70** | **153,767,690,240.00 USD** | **-21.56** |
| MDT | 24.79 | 2.62 | 14.58 | 13.70 | 131,572,129,792.00 USD | 10.54 |
| SYK | 33.26 | 5.03 | 17.32 | 7.60 | 117,877,170,176.00 USD | -16.16 |
| BSX | 18.63 | 2.51 | 13.62 | 1.40 | 64,269,643,776.00 USD | -57.76 |

Peers fetched as_of: 2026-11-13; ISRG reuses existing data (market data as_of: 2026-11-13); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-20
- Next expected earnings: 2027-01-21 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-13

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
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPQW1hV1lMNFBYRmJWdW9OTDVTTDV6QktCT3hhMGFteTFYdGJ5dGxSci1TNk1pdkVBUUhuRlJJamNodjcya3o1NXh5aVZTUWU3b1NNekM5YWdyd2IxU00xZ3hRRXdWdG96YmRRZXhIWUF0aGZfR2FfNC0zR21JZ05KSzNhckdBQlBFcFctbDVRV0o5cUplWXpuMjhSaTNSVFlR?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOV1JDa3pWOXNYTDdmclZzOG0yMVlIUElneWlQU05HbzZKQWdTdHZrVlZaaVhtMFcwT1RoUjMzaVdQY2tYeThqXzEtNWxNZGxZNUFDbEhCOU5WeFptd3ltY2lmTTVBR3NnLXlnS2RwUFNpUkJPVXBTQ1d2Zk5jWFJfLVYxelNTcFV1ajA0RDh6cjhLbm5ISkRsLWxQN29xb3M?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPQnpLTmE0dklyYmp0MGJRU2hzQmQ2T2luWnppTmJFWl9rSWhXS3djTWNyS29RUTlpYXpXemF0SkdHUGZNOEp3ZXRiTnBlSHl3Nnp0Z01EcWhuekZ1OW0xX0hpdVpIS29PaHc5cG5VTDhLcHQ0d2RYU3ZYd3IzYnJfQ05ac3hlM0pudHY5QlZIU1haUHlYU0ZwWDBvSUk5eF9vckFn?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxOY0xpOFlBYVhVVWlXR3F0eC16UU9SYUdfLTFDM2JPVDAySjlPb0FycHNQTE84MEI2Y3ZucFFiSjU3S3RHa2p4d1doTk5VVWxuN25hNFlRYmp4VWV6U3l6WjVjSE5CNG9EM2daSlhCS2FGTTd3dmNmaVpiWnRhdUg0RVZ6cUF2akw4WlpCa01LanF4dw?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOWDU2bmdzM1BVb3E5VzZYWDJnOUhoZE1jOW1kQlBBSW1KMU5TYUplWi1sUDduVk9VSHlLandVdkh4MTY0UTExU05lZVR4QkFfTS0yZ0ZsLW1mZ2Z6OTFoYzRtUzRMSVowd2FGcXRlYUxUanVnOTRBLWEwVzVsbkJLU0J0RUlLdmRNMWhTdTQwZW9sSU9KREROR1ZuS2w2RWNFaUhZSlNB?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxNb0xHeHE2cUExVEN3V3U2V3RIOHUwNVY0OXZMX3ptYm9pUzV2dnpScmkwWFVhdzZGQWFXOTMwTUtac3BkV2FxYy1ZOENtSElINFQ3UWkxRkxzZGxEd0pCY2hPZ1lBUWVSc3JRQTljZmFGTkQ5NnhsY0ltQVlpQy1kRy1Wb1c3TzNrSm5yVkl1dEU2NkxWZXFYaHVvQWg3Zw?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxOS0p0TFpDX1JNWG8xV2pYbUhidC1PTHoySVVCMkV3Wm9hdFhJZV92VGxlZnVYZURkQmpTMDI4SEpITEI1SldVOWpnZ1F4aUgtMUYtMGgzVURVOF9KNGlFdkUtcVJlemRoSVVweFNVWGUyM0RBRFVhOUpaR0xyT1ZfQTRxdmpabGk1NWdwQVJmdWN0MjFxSXB5OVhTSUJfdUhzOUcyN1o5MUMtQlJuOU8zc3k2VlgtSEl4UGlrVXBn?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxQS01JMGgyemdnckljSE01MnM0QnV2R2RVcGo5SkctZzZPQ1BKYktnOE9KcVUxS09PT01xODVsdFlKdzVjb1VZWnBQajMtMWlJOWRjRDh3TmJtazhQZHM3UzA3aUFKd2ZfRDlxWnBHVDhiekcwRFgyMEptMHJwVUI4MlFUZDVnelJUMHZOZlpReGxPbnA3SnJNVEVQLTZheXJIaWF5VnEyQ3VQcnNpUFNHQlE3X0ZaTnhiZ3ZpaGhqQUJmSFdGeFllN2V2dkFnRHdYbmpRTmp30gHbAUFVX3lxTFA1TlUxWlVEN3g1Y2RKd1RwV0t4MldtSmUxVUR4X3RhSFBrUmdYZE1EMzdsVlVhaXdIdTIxamw1Yk9ZTzN4VDZsXzVEWFZlSE5OLUZBbU9zTVIxcHhOa2tXMkx3S0tIT0ZCUmlrZXM5S3k4MHJWekRVcDdHeDlZNDkwenV0cEFKdmVxSVdkZ1d3U1JsSzRnWVo4UnkxTlpzODlNOEdYamJkQjJ6TkFuVW9pOHUzQk1MZE95RjVFZFdBZ01VQ3RkbWdmZDRxTEJnY0lQZWZfTXJPOEtlSQ?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxPLXU0OUM4LWFjWXZGN0hScU9GQkxULVJoT256bEZocFV0WjRpUGlwSnZlbDJDampJM256QVFKcnU4VGVJQ3hXM3lLZXFrYTJjX2o3OUlBbXBLYlV0dHdqV0ZsNFJ5OUhUZFo3SGJIY3VwU2tBbC1sYjg3WWhEVk1oQlY2aGdxVTQxUzB0dDJfVTFtM01PbTY3clZqVk1YM0t5MmZiRW42R29fY194Q2I5cFREMnFra2NTaXpLOUFxRXI0d1VKamFad0YzektQcmtXb0hlZkRn0gHbAUFVX3lxTE5VNTVxX08tUDh3SmNHdl9Ca2tpQ3RoM0g4dGtiMHZrdXkzeXZsZmFwOFE0UWtpY2Y1ZmxhMWJLU09yaWQzdnZxMG13WU9IYWNyY2FtWE9WdVpHVjMxYWxFUzZaUWM4UmRYYUdXYjRyVC1TZ3ZucmFzZEJkdDdqcmFKblJlWnRrSWNZYUdsUXIyU1BPclM5VmpnaUVES3FLZmFpR29ob0RSRHVhWWdvWjNFWDVNTXJUUGJlN1huaE9ILTMtckc3MHJrb2xqRVIxOUdvdWg4VkdpcjB6aw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
