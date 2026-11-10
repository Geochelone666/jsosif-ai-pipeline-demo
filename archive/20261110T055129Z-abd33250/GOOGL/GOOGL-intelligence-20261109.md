# GOOGL Intelligence Report

- ticker: **GOOGL**
- Report as_of: **2026-11-09**
- Market data as_of: **2026-11-09**
- Quant sources: https://finance.yahoo.com/quote/GOOGL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/GOOGL/key-statistics/
- AI analysis snapshot as_of: **2026-11-09**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-10T06:05:28.318263+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 6, 'ai': 10, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261109T043242Z-c8e908de/GOOGL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 2}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 14 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 26.09%; oldest publication 2026-11-04

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 288.1500 |
| Return 1D (%) | 1.1834 |
| Return 1W (%) | 3.2833 |
| Return 1M (%) | -18.0601 |
| Return YTD (%) | -7.7602 |
| Return 1Y (%) | 3.6113 |
| Annualized volatility (%) | 33.6006 |
| Beta vs SPY | 1.2846 |
| Max drawdown (%) | -30.6204 |
| Sharpe (rf=0) | 0.1560 |
| Downside deviation (rf=0, %) | 23.7346 |
| Sortino (rf=0) | 0.2208 |
| Historical VaR 95% (1D, %) | 2.9463 |
| Historical ES 95% (1D, %) | 4.7232 |
| Correlation vs SPY | 0.5235 |
| Tracking error vs SPY (%) | 28.8933 |
| P/E (trailing) | 15.05 |
| P/B | 5.37 |
| EV/EBITDA | 18.57 |
| Revenue growth (%) | 24.70 |
| Forward P/E (estimate) | 18.67 |
| Gross margin (%) | 60.86 |
| Operating margin (%) | 31.80 |
| Return on equity (%) | 44.29 |
| Free cash flow yield (%) | -0.03 |
| MA50 | 331.7418 |
| Close vs MA50 (%) | -13.1403 |
| MA200 | 339.0207 |
| Close vs MA200 (%) | -15.0052 |
| RSI (14, Wilder) | 32.8824 |
| MACD (12,26) | -16.1371 |
| MACD signal (9) | -13.4485 |
| MACD histogram | -2.6886 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'GOOGL': 278, 'SPY': 278}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 288.1500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.1834 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 3.2833 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -18.0601 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -7.7602 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 3.6113 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 33.6006 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 23.7346 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.2208 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9463 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.7232 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5235 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 28.8933 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.2846 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -30.6204 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1560 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 18.6685 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 60.8570 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 31.8050 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 44.2860 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: -0.0328 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 15.0470 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 32.8824 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -2.6886 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -13.1403 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -15.0052 -> Clearly below the moving-average trend level.

## TAILWINDS

### Alphabet (GOOGL) stock is up, what you need to know
- Summary: Alphabet (GOOGL) stock is up, what you need to know
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxNd1lGTmRqT1l4cXdzRi1oZHYtNmlxaTR4RmRybjR1M2FwVlVCLUM2ZWplMGl0RmxrTXZ1c2dUU3B6a0dqeTZPQU9FeS1sVWZhMGVjSmJkbW45enI2RjJrWkFWVWJFczhWb0l1S1RjZV9XcHkyOUljM1RZR1VKMHFCUE5iX05mNmJCMVBiUlVIc3poLW1sb1RYMjNtNTJMTzNucWlKN0pkX2hBRGc3dG1ubE9DbVhSeXZSbEdRcTFWR3Q1Vk1WZXNNekFNclo0M00?oc=5>

### Alphabet stock rises as Google expands AI chip lineup to challenge Nvidia
- Summary: Alphabet stock rises as Google expands AI chip lineup to challenge Nvidia
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxOYW1VVUNLX0RxcFlsYTljOHlybnpxcXpHYldQU25qRjhIZElyTU0xT0xEVjRxQWgwb3hiQ0RFOGMwNGtHNWJpTUlIYmxQTFV1MnZob0d2cDJTZ2F4ODFBd2NZbU1Zc0RnMEM5ZGM2TmNhb1FsRGdsSG0tQWlMdFFINEhRTkVZWHA1NTRBNW44VXdJMUFwaWdETVI4b1V0SEJ6cTFRRkRLMUxXNzZlQ18yTXc0di16VGNNc1kwSWg2aURZOEhmdmJZdzB3?oc=5>

### Alphabet Stock Rises as Google Adds Two New TPU Variants
- Summary: Alphabet Stock Rises as Google Adds Two New TPU Variants
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxPZ2dldldZVUpzNW9ESXAtRnNmTWZFTGpzWnU3RFhJYmtmVDl0ZVVSWDlXdGxMZWRIZ2xBdW5kNzBSaEFscXJadjZLdFNGZG1RZGtWd0lIM3BUZG1xaWYtRmxudGVMNzgydWdoNWFibHJrNzNteVliazhmTHBRUXJHMm5YSW9qYlA2Y2piTlJRR2NFMTQ5RTBoMWlYdjRhTkQtWVJwZEJNOVYwOGdBQ0Jsb2h4YW5NX1E?oc=5>

### Alphabet (GOOGL) Stock Rises 0.78% (November 6, 2026): RSI Oversold
- Summary: Alphabet (GOOGL) Stock Rises 0.78% (November 6, 2026): RSI Oversold
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQWFNiZko2aXFJbmszdmJQaUxVeFM4emRIWkZjaGQyQnoxRGN3M2tlam9ESUtkWmNXMlFNNzdId0pwMk1EdnNIMTgwcU1vMkJuOFpjanVVYTdXZ1lLS3RJV1VidmNCTm5rU2ZadnM0QVhkbFZDaTQ4eFZTNGVPc1VrNWxEWUJIWFMwbVBVSmIyLUFLT2t1Y1gtczgwMjI3ZThY?oc=5>

### Marc Chaikin Sees Alphabet (GOOGL) as a Conglomerate Hiding Three World-Class Businesses
- Summary: Analyst views Alphabet as a conglomerate with hidden top-tier businesses.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOZGUwTUFsMVZQeEZPSnFCZ3dnMDZNTVNFeGVXelVQN1ZtcFo3SnY2dzdmSHhIM2J2OGgwRXZScGYxajZuSDNQd3ZvTGdrMDU5QWNEdWhXM0hnb1lPMmNoQ3ZST0lTcnVDRllVRnpwWG9VdWxxQ1I5R0w5Q3BsZ0NaMkJ1b0FRc05nZnRWdFRhdFBBYVg3aEkwSWd4NlktZw?oc=5>

### Alphabet (GOOGL) Expands SpaceX Stake to $69 Billion and Deepens AI Ties
- Summary: Alphabet increases its stake in SpaceX to $69B, strengthening AI collaborations.
- Date: 2026-11-07 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQWFhmSzc3OTBJVU1QbnBIVFpPZURJc3Bna01BaUJLelVkV1RCcF9NQWFSZURkOHFlNlU4R0NDWUVoWXVpUkFnM2RiRElKMER0a3JBekZkVUlvem42SmtEaWg3VjFvOHZEcnI0dTg2TzRMbF92LUx4Y3ZySXFIZ0h1ZjllcWs4c1g0UEFIYW9sRWVkX2VyOUY5OTZjSFROX05p?oc=5>

### Alphabet Plans to Launch Two New TPUs, May Push Stock Back to $300 Mark
- Summary: Alphabet plans new TPUs, potentially boosting stock to $300.
- Date: 2026-11-09 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxQOUktbVZETHpOYnB4d3Q4Nm5ROXNSM3Y5NnJVNURhbTNtbUp1ckpLTWhuTDJzUWVhSERLNk02V0V2N0hNMHllYmpja0dYc0tCMGFNb0RwVFpRdjV5Y3FwQUxvR0k5c3JnUC03QmNjajJvdXBnYVBYWkx6Sk5GYld1OWlTalE1TXluekE1Tlc4STNMM3d4NWNuUnA2TEZCdG5XZWVQb2U5b0E1dm5POFBIYzlZT3BNZGxBWVNrSmRBSHVYc1NqcDFtQWlkUl9GWTRiV3c?oc=5>

## HEADWINDS

### Has Alphabet (GOOGL) Fallen Far Enough To Back Its Cash Flow Value?
- Summary: Questioning if Alphabet's valuation supports its cash flow value.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQckEtTjZnazV2YS1qTjQxNkxzaXZOU2pjYmZ5S29qRzB5QlJ6Y04wcE9MYzE0c250WjQydHNkeUVDS1Q4RGRTaUFrUkphdFVGYWlqcHNibXNkVFo3QUpKVWZKX29LZTF4NE1INVU1ZkVONnQ3MzVzWXhrQzJ2VVBrZUVkTmVRT0VETVdhUnhWZW9uWFhVaThnbkRJeXEyZw?oc=5>

## CATALYSTS

### Alphabet Stocks Rise 3.16% as Google Unveils Two New TPU Systems
- Summary: Alphabet Stocks Rise 3.16% as Google Unveils Two New TPU Systems
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMif0FVX3lxTFBEcERuUkZ0b2kyZkJNQ0IzR2lOZlM1REVRRkxGblFYQkM4Uk9HRUpIV0xYUHFXQnVqbVhfcjlZTkdWMUdZdDE5MmlnRXF6Tnd5eEwxTXVLT0tsNC1QaTlRTTM0ZGUwRzQtR0NLM3NhMnpHNjJOVW1jRl9taWExOW8?oc=5>

### Alphabet (GOOGL) Jump as Google Unveils Custom AI Silicon to Challenge Nvidia
- Summary: Alphabet (GOOGL) Jump as Google Unveils Custom AI Silicon to Challenge Nvidia
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxNVmstYzVQY05rM2QwZDhKVjdDREgzdVlhMjlQMUU2bGJyS3VrSGhrYmI1c1dCVkdxNkdlcFEzVXB6UGtld042OUNGQzBKX2FUNUtWalRablA1VG8zZEpEVVNLUEFZQjZGQm5vbC14UjJEQW1YNEUwSk1laHM0dHUwTnEtN3VOZXdVdTY5bkFJaGszU3hjbjRjVklLaUdzRUo4TmRxdzhVdVY0by0xMXMyYWljMnk3TjFTWVE?oc=5>

### Alphabet (GOOGL) Sees $35.0 Million in Net ETF Selling on Wednesday
- Summary: Alphabet’s shares saw $35M net ETF selling on Wednesday.
- Date: 2026-11-06 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTFA3cGhXNVBvV2JpbHBkbXNDX251LU9CcEpSaUJ1cnFxUHlraHRFbDlwN1l5bS1FUHBpQ2dKbXhodEx4Ymo2Yy1vUFVGcTAxNTVFRkxkTml3dHhhM3RfUTJFeU43aW9wTjV0bU5JbF9EV0Q1WldkMEJKYWhZMVk3Zw?oc=5>

### Alphabet (GOOGL) Is Spending $15 Billion On Malaysia Data Centers
- Summary: Alphabet invests $15B in Malaysia data centers, expanding infrastructure.
- Date: 2026-11-04 | Impact: high | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOVmZLa0xpaWxxcnJtRTBhMGt4eWpzWEd3NDNvZlNJcWJPeGxmWnNnQ1pLQWNLSENyQ0Uzb3FKS2NyandnbERlQ1A3Y0lCdXpPdm1HeEhlZ2FXTGtiajRiMGlIVXNuVGZ1MUpLYUcxTlVsa2RKZFFYdThQLWxUU2V6T2dtZnpXdUVENGtQcHRJemtpTzZiNFp3NHd6cFJ5RVE?oc=5>

### Josh Brown Warns Alphabet Stock “Could Go Down 50%.” Here’s Where He’d Buy It
- Summary: Analyst Josh Brown warns Alphabet could drop 50% but suggests buying opportunities.
- Date: 2026-11-08 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOWUVUSkFtS21USUFuMlk1THhQTWVjclpwcjdiYndkS3ZJNkdvYzlTOTR1b1h6VU9TbXd3TXBzaVVyand3cVZPaDRIc2VDekRONi1sUjN4RHVhZHlJdkNuOTU3NU5OZG9UNmpWM3ZvOWRHNUtOUEFNc0FST2V3cDJxbmJSM0lremVacXI1YTk5Y2RHNlFVVi1VeTU1LTFXZw?oc=5>

### Alphabet Inc Class A Stock (GOOGL) Opened Up by 3.44% on Nov 9: Facts Behind the Movement
- Summary: Stock opened up 3.44% on Nov 9.
- Date: 2026-11-09 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxPcHVHZjNZeF9QZm1oYkNOTkhpb0hFdU5JWGpZX2ZCRndXSlNZZE1LNFNkSTc4Umlyb0NTLXdQNF95ZUxSZDRWV0tQZ1ZLZllZejFhTk10RW96dnYzNWdaM0xkNXhDTnJVVDFBR25RWm9ZYmNIdjJncGhQV1E4aGVtOGNkNGNqaGF5dHZrMA?oc=5>

### Mapping the Market: Alphabet shares may be ready for a corrective rally
- Summary: Potential short‑term rally for Alphabet shares based on market analysis.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMifEFVX3lxTE9vZGlZeXZzRUlyeHhERkg4UzlnbEFhMHBoZDlLaGN1aS05cWZ5MENHV2xGREkzWjdaMDhyR3JWQTYycjhqVVI3TFkxNldsakNGYUJLNjFobWVSUWpXdzItZ2w4TDFYMVZRMzJTQlNyUF90YkJKQ2FmVzVLdkc?oc=5>

## RISKS

### Google Stock Investors Biggest Risk
- Summary: Investors face significant risk with Google stock.
- Date: 2026-11-08 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxOYkFqanltQlJvenA3UkE0ejM2d0sxckRqV1EtbDZEUWVqblZUSlZ0TEZTT2JLWHJSci0ySmR5UGFLRUJPN3NhNDFneEtBcFNLSWJPZHhEU2hYUVRTMXRPS1JpZTVDdXNaOXY1STMzQWRVOS1RdE41OGVzbGRjT3JKQlc5SDk?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **GOOGL** | **15.05** | **5.37** | **18.57** | **24.70** | **3,542,515,974,144.00 USD** | **3.61** |
| META | 21.88 | 6.02 | 14.39 | 26.10 | 1,639,876,001,792.00 USD | 3.51 |
| MSFT | 28.45 | 8.61 | 20.02 | 18.80 | 4,048,612,753,408.00 USD | 10.64 |
| AMZN | 21.58 | 4.70 | 16.75 | 12.10 | 2,886,350,929,920.00 USD | 9.21 |

Peers fetched as_of: 2026-11-09; GOOGL reuses existing data (market data as_of: 2026-11-09); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-28
- Next expected earnings: 2027-02-03 (yfinance; expected dates may change)

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
- Filing date: 2026-10-29
- Revenue (latest available single quarter): 127,577,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 26,468,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000084/goog-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMizwFBVV95cUxNd1lGTmRqT1l4cXdzRi1oZHYtNmlxaTR4RmRybjR1M2FwVlVCLUM2ZWplMGl0RmxrTXZ1c2dUU3B6a0dqeTZPQU9FeS1sVWZhMGVjSmJkbW45enI2RjJrWkFWVWJFczhWb0l1S1RjZV9XcHkyOUljM1RZR1VKMHFCUE5iX05mNmJCMVBiUlVIc3poLW1sb1RYMjNtNTJMTzNucWlKN0pkX2hBRGc3dG1ubE9DbVhSeXZSbEdRcTFWR3Q1Vk1WZXNNekFNclo0M00?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxOYW1VVUNLX0RxcFlsYTljOHlybnpxcXpHYldQU25qRjhIZElyTU0xT0xEVjRxQWgwb3hiQ0RFOGMwNGtHNWJpTUlIYmxQTFV1MnZob0d2cDJTZ2F4ODFBd2NZbU1Zc0RnMEM5ZGM2TmNhb1FsRGdsSG0tQWlMdFFINEhRTkVZWHA1NTRBNW44VXdJMUFwaWdETVI4b1V0SEJ6cTFRRkRLMUxXNzZlQ18yTXc0di16VGNNc1kwSWg2aURZOEhmdmJZdzB3?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxPZ2dldldZVUpzNW9ESXAtRnNmTWZFTGpzWnU3RFhJYmtmVDl0ZVVSWDlXdGxMZWRIZ2xBdW5kNzBSaEFscXJadjZLdFNGZG1RZGtWd0lIM3BUZG1xaWYtRmxudGVMNzgydWdoNWFibHJrNzNteVliazhmTHBRUXJHMm5YSW9qYlA2Y2piTlJRR2NFMTQ5RTBoMWlYdjRhTkQtWVJwZEJNOVYwOGdBQ0Jsb2h4YW5NX1E?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxOUFFvb1FiNDRFbC1ndFY3MnEtcGs0eGVQNHJsZkRzcGtySV8zQUFmVFg0dHQwcFZlOXhtMmpuZUZuUkx5TUFGcV9jcmxUVnNzejEzUkxsLWh4bEpqTThIYjI1dFJ2d242VUQ1d01UUGdsZmFXeXlZajViU3JSSjMtVVhmLWxvcGhP?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQWFNiZko2aXFJbmszdmJQaUxVeFM4emRIWkZjaGQyQnoxRGN3M2tlam9ESUtkWmNXMlFNNzdId0pwMk1EdnNIMTgwcU1vMkJuOFpjanVVYTdXZ1lLS3RJV1VidmNCTm5rU2ZadnM0QVhkbFZDaTQ4eFZTNGVPc1VrNWxEWUJIWFMwbVBVSmIyLUFLT2t1Y1gtczgwMjI3ZThY?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOZGUwTUFsMVZQeEZPSnFCZ3dnMDZNTVNFeGVXelVQN1ZtcFo3SnY2dzdmSHhIM2J2OGgwRXZScGYxajZuSDNQd3ZvTGdrMDU5QWNEdWhXM0hnb1lPMmNoQ3ZST0lTcnVDRllVRnpwWG9VdWxxQ1I5R0w5Q3BsZ0NaMkJ1b0FRc05nZnRWdFRhdFBBYVg3aEkwSWd4NlktZw?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQWFhmSzc3OTBJVU1QbnBIVFpPZURJc3Bna01BaUJLelVkV1RCcF9NQWFSZURkOHFlNlU4R0NDWUVoWXVpUkFnM2RiRElKMER0a3JBekZkVUlvem42SmtEaWg3VjFvOHZEcnI0dTg2TzRMbF92LUx4Y3ZySXFIZ0h1ZjllcWs4c1g0UEFIYW9sRWVkX2VyOUY5OTZjSFROX05p?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxQOUktbVZETHpOYnB4d3Q4Nm5ROXNSM3Y5NnJVNURhbTNtbUp1ckpLTWhuTDJzUWVhSERLNk02V0V2N0hNMHllYmpja0dYc0tCMGFNb0RwVFpRdjV5Y3FwQUxvR0k5c3JnUC03QmNjajJvdXBnYVBYWkx6Sk5GYld1OWlTalE1TXluekE1Tlc4STNMM3d4NWNuUnA2TEZCdG5XZWVQb2U5b0E1dm5POFBIYzlZT3BNZGxBWVNrSmRBSHVYc1NqcDFtQWlkUl9GWTRiV3c?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQckEtTjZnazV2YS1qTjQxNkxzaXZOU2pjYmZ5S29qRzB5QlJ6Y04wcE9MYzE0c250WjQydHNkeUVDS1Q4RGRTaUFrUkphdFVGYWlqcHNibXNkVFo3QUpKVWZKX29LZTF4NE1INVU1ZkVONnQ3MzVzWXhrQzJ2VVBrZUVkTmVRT0VETVdhUnhWZW9uWFhVaThnbkRJeXEyZw?oc=5
- https://news.google.com/rss/articles/CBMif0FVX3lxTFBEcERuUkZ0b2kyZkJNQ0IzR2lOZlM1REVRRkxGblFYQkM4Uk9HRUpIV0xYUHFXQnVqbVhfcjlZTkdWMUdZdDE5MmlnRXF6Tnd5eEwxTXVLT0tsNC1QaTlRTTM0ZGUwRzQtR0NLM3NhMnpHNjJOVW1jRl9taWExOW8?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxNVmstYzVQY05rM2QwZDhKVjdDREgzdVlhMjlQMUU2bGJyS3VrSGhrYmI1c1dCVkdxNkdlcFEzVXB6UGtld042OUNGQzBKX2FUNUtWalRablA1VG8zZEpEVVNLUEFZQjZGQm5vbC14UjJEQW1YNEUwSk1laHM0dHUwTnEtN3VOZXdVdTY5bkFJaGszU3hjbjRjVklLaUdzRUo4TmRxdzhVdVY0by0xMXMyYWljMnk3TjFTWVE?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTFA3cGhXNVBvV2JpbHBkbXNDX251LU9CcEpSaUJ1cnFxUHlraHRFbDlwN1l5bS1FUHBpQ2dKbXhodEx4Ymo2Yy1vUFVGcTAxNTVFRkxkTml3dHhhM3RfUTJFeU43aW9wTjV0bU5JbF9EV0Q1WldkMEJKYWhZMVk3Zw?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOVmZLa0xpaWxxcnJtRTBhMGt4eWpzWEd3NDNvZlNJcWJPeGxmWnNnQ1pLQWNLSENyQ0Uzb3FKS2NyandnbERlQ1A3Y0lCdXpPdm1HeEhlZ2FXTGtiajRiMGlIVXNuVGZ1MUpLYUcxTlVsa2RKZFFYdThQLWxUU2V6T2dtZnpXdUVENGtQcHRJemtpTzZiNFp3NHd6cFJ5RVE?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOWUVUSkFtS21USUFuMlk1THhQTWVjclpwcjdiYndkS3ZJNkdvYzlTOTR1b1h6VU9TbXd3TXBzaVVyand3cVZPaDRIc2VDekRONi1sUjN4RHVhZHlJdkNuOTU3NU5OZG9UNmpWM3ZvOWRHNUtOUEFNc0FST2V3cDJxbmJSM0lremVacXI1YTk5Y2RHNlFVVi1VeTU1LTFXZw?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxPcHVHZjNZeF9QZm1oYkNOTkhpb0hFdU5JWGpZX2ZCRndXSlNZZE1LNFNkSTc4Umlyb0NTLXdQNF95ZUxSZDRWV0tQZ1ZLZllZejFhTk10RW96dnYzNWdaM0xkNXhDTnJVVDFBR25RWm9ZYmNIdjJncGhQV1E4aGVtOGNkNGNqaGF5dHZrMA?oc=5
- https://news.google.com/rss/articles/CBMifEFVX3lxTE9vZGlZeXZzRUlyeHhERkg4UzlnbEFhMHBoZDlLaGN1aS05cWZ5MENHV2xGREkzWjdaMDhyR3JWQTYycjhqVVI3TFkxNldsakNGYUJLNjFobWVSUWpXdzItZ2w4TDFYMVZRMzJTQlNyUF90YkJKQ2FmVzVLdkc?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxOYkFqanltQlJvenA3UkE0ejM2d0sxckRqV1EtbDZEUWVqblZUSlZ0TEZTT2JLWHJSci0ySmR5UGFLRUJPN3NhNDFneEtBcFNLSWJPZHhEU2hYUVRTMXRPS1JpZTVDdXNaOXY1STMzQWRVOS1RdE41OGVzbGRjT3JKQlc5SDk?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
