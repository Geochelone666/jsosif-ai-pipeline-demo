# J Intelligence Report

- ticker: **J**
- Report as_of: **2026-11-09**
- Market data as_of: **2026-11-09**
- Quant sources: https://finance.yahoo.com/quote/J/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/J/key-statistics/
- AI analysis snapshot as_of: **2026-11-09**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-10T06:06:15.819249+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 9, 'rule': 2, 'ai': 4, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **N/A (no successful AI classification call)**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261109T043242Z-c8e908de/J** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 9 unique headlines; 5 named publishers; 0 exact duplicates; 9 HTTPS source links; largest publisher share 55.56%; oldest publication 2026-11-02

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 156.3900 |
| Return 1D (%) | 5.0302 |
| Return 1W (%) | -2.4026 |
| Return 1M (%) | 12.3895 |
| Return YTD (%) | 19.0362 |
| Return 1Y (%) | 3.0622 |
| Annualized volatility (%) | 34.1753 |
| Beta vs SPY | 0.8824 |
| Max drawdown (%) | -30.2983 |
| Sharpe (rf=0) | 0.2437 |
| Downside deviation (rf=0, %) | 25.5118 |
| Sortino (rf=0) | 0.3265 |
| Historical VaR 95% (1D, %) | 3.0536 |
| Historical ES 95% (1D, %) | 5.4729 |
| Correlation vs SPY | 0.3535 |
| Tracking error vs SPY (%) | 32.0089 |
| P/E (trailing) | 51.96 |
| P/B | 5.61 |
| EV/EBITDA | 20.03 |
| Revenue growth (%) | 34.50 |
| Forward P/E (estimate) | 18.99 |
| Gross margin (%) | 22.07 |
| Operating margin (%) | 7.39 |
| Return on equity (%) | 8.00 |
| Free cash flow yield (%) | 3.53 |
| MA50 | 144.2324 |
| Close vs MA50 (%) | 8.4292 |
| MA200 | 133.8854 |
| Close vs MA200 (%) | 16.8089 |
| RSI (14, Wilder) | 61.0617 |
| MACD (12,26) | 3.5994 |
| MACD signal (9) | 3.1825 |
| MACD histogram | 0.4169 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'J': 278, 'SPY': 278}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 156.3900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 5.0302 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.4026 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 12.3895 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 19.0362 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 3.0622 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 34.1753 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 25.5118 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.3265 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.0536 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.4729 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3535 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.0089 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.8824 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -30.2983 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2437 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 18.9865 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 22.0670 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 7.3870 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 7.9980 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 3.5276 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 51.9568 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 61.0617 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.4169 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 8.4292 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 16.8089 -> Clearly above the moving-average trend level.

## TAILWINDS

### Jacobs wins $2.1B design contract for New Zealand highway (J:NYSE)
- Summary: Jacobs wins $2.1B design contract for New Zealand highway (J:NYSE)
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPNWFMR0I1SHFWSU5VSDZIM0VHQXYzS0kxaUJETXhJOUtEM1lwMy1oRU80SEdiWU1EaXZIRHNoeGdsTkUxLVZmaDRaXzZOTUhBQ09GVXJ4MVBtVU1pQ3JJNnJJbWZlYl9LRFNBNV9kSFdreFE5MnFkcnRVRGtvX3lZXzhjQWtrTnhLYXFqSEY2Q2Fva0w2c2doTm9B?oc=5>

### Jacobs Solutions (NYSE:J) Reaches New 12-Month High - Here's Why
- Summary: Shares hit a new 12‑month peak, driven by strong earnings and positive market sentiment.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxNNndtbkl3Nm9CajZiQ1hzNVJyc0MwM3NndXRCQUhXX05saF9RalNXT29PMUh4blhkUlI3OVJkQm53UEVHQUZveEdENG91bnp5X3BQZ0FTVlgxNHVRVG9GbTJrUXEzTS1VZ2Joc093a0FFQWZZNG5xMkZ0cmlseVdMbEZYSDl1TWZiM0hDY0kwTkNGQXVrS3ZUX3VoaGJzNm5WVk13bzlZRFQ1bTdJcWdvNng1SlhxSmRMR3Aw?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Jacobs Solutions Inc. $J Stock Sold by Bryn Mawr Trust Advisors LLC
- Summary: Jacobs Solutions Inc. $J Stock Sold by Bryn Mawr Trust Advisors LLC
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxPeUF0VzAtMHNqYWd2R3haLWllMnFUQ24wdl9hb2d0VVRoa3NqWjNJdGNaVUxDTkUzN2lUNW1KZ3p4dDRERTJIZUlTWWlyeUV3N3NhbUY5VmhVQU9WUlpyaGw2ZGZPQTk3LTBBRDBRREVwVFlqemptN3ZhSDlzamlmUXhIRjJma0VSTzl3cXE4M1d3Q3dWYmxMUE5Td01aZ2FvdVRhQnJKc083dWdmYmZiSE1xWFd3VDlZOEJoNUhsVVhIaFFw?oc=5>

### Should Jacobs Stock’s New High Stop You From Buying?
- Summary: Jacobs stock hitting new highs may deter buyers, indicating potential overvaluation.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxNWVJhYWlRc3FYS2d3cDBfZG5GQ3lfUHFsUmIzTlR0ZmtaM1R1aUZTTXNTVWJQM3F2aDFxcTNHMEpKdWZlVS0xRFREVUhhbERQLWpQWG1OMGVVR3Y4cVNkWV9aeVBRaXdaN2h6alpwU1RuVEhVN1hWY0ZZN1VLWXljSk5ZSzBSTmtFbHFIS1FkaHc1UURIdFo4WDFaSXVoVW1qOS1UOGEzejhfVnRi?oc=5>

### Jacobs Solutions (J) Lands New Zealand Highway Role, Is The Stock Still Trading At A Discount?
- Summary: Jacobs Solutions secures a new highway contract in New Zealand, potentially boosting revenue and market presence.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxQRFZIMUQ3d3RzLXBMTVJZRVY5TVFNbGhleUdVQWFWWTg0ZHFRalRyblA5T2RWc1FlaEo3aXlPSkxwby1tZkxUWWRLWlZkLTk0MUNvcEVpR050RUpxVWptbDFzb01KTHRCNXRlRVliQ0FGTl90cThaTUlfNEprNHMtY2lzazhiaUktN0phMTd1NGhEYzNNNjN3cUFFSEVaZmVhNGQ4c1ozcjlXNjQzbFVkejlJYndPcDVkZHhDcHV0dWpJZ3BMcnNaWU1qTlNxNjVobUNlTVhvT1_SAd4BQVVfeXFMTTVqNGt5TFlJbHRjQ3ZPRG9oalVET1ZrZ0RyY0czeFpHeVJQdzdMa1F1THZhYjd3UDBoQUVESDB0dEh4SWlPN3hjV0FYREJOaGxxT3BBa09Udk1CSzJjdi1HUmMwaGpSa1pnVDZFWElTaklkTmg3OGc4YTVCT1NuakdXRUx1Tmd0dUIzbXpGbE9VWnpIRnFhV0xseEJyTEN6OVUzU1JkMUt5Uzh5LUtNX3BVak10UkxLZzZuMEtsYTdfZm9SWTViTlcwQ2RNMGNMRW5MQm9UZGUzenRQcjR3?oc=5>

### Jacobs Solutions (J) Secures $2.1B New Zealand Highway Project C
- Summary: Jacobs wins a $2.1B highway project in New Zealand, boosting revenue prospects.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxOY0plSS1oM3NSdVRkMm56YzBfbEZPVGpmX0xVRTUtc1hYQnRsUUQ4bnBDZVNocTlFNTlhRVA3d21nTzlxMlZmQm1GSkpFbFFmZEdIalVVTWcyWEJMWTZEVUxHTTlzZnBZQjVfbmJLcExSRml1dUs5Umt3WGhzVUNUUHRqc0czX1VfN3ZzUFNyZGg0Y3RZNmxGeXpxVDV3bU9jc281a3lkdXBRZw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **J** | **51.96** | **5.61** | **20.03** | **34.50** | **18,303,668,224.00 USD** | **3.06** |
| ACM | 24.72 | 4.12 | 12.40 | -14.20 | 9,035,776,000.00 USD | -45.41 |
| FLR | N/A | 2.54 | 11.48 | 10.50 | 6,451,513,856.00 USD | 10.08 |
| KBR | 11.24 | 2.76 | 10.38 | 5.00 | 4,874,112,512.00 USD | -7.72 |

Peers fetched as_of: 2026-11-09; J reuses existing data (market data as_of: 2026-11-09); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-04
- Next expected earnings: 2026-11-23 (yfinance; expected dates may change)

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
- Filing date: 2026-08-04
- Revenue (latest available single quarter): 4,142,644,000.00 USD; period 2018-06-30/2018-09-28; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 136,553,000.00 USD; period 2026-03-28/2026-06-26; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/52988/000162828026052573/jec-20260626.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimgFBVV95cUxPNWFMR0I1SHFWSU5VSDZIM0VHQXYzS0kxaUJETXhJOUtEM1lwMy1oRU80SEdiWU1EaXZIRHNoeGdsTkUxLVZmaDRaXzZOTUhBQ09GVXJ4MVBtVU1pQ3JJNnJJbWZlYl9LRFNBNV9kSFdreFE5MnFkcnRVRGtvX3lZXzhjQWtrTnhLYXFqSEY2Q2Fva0w2c2doTm9B?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxNNndtbkl3Nm9CajZiQ1hzNVJyc0MwM3NndXRCQUhXX05saF9RalNXT29PMUh4blhkUlI3OVJkQm53UEVHQUZveEdENG91bnp5X3BQZ0FTVlgxNHVRVG9GbTJrUXEzTS1VZ2Joc093a0FFQWZZNG5xMkZ0cmlseVdMbEZYSDl1TWZiM0hDY0kwTkNGQXVrS3ZUX3VoaGJzNm5WVk13bzlZRFQ1bTdJcWdvNng1SlhxSmRMR3Aw?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxPeUF0VzAtMHNqYWd2R3haLWllMnFUQ24wdl9hb2d0VVRoa3NqWjNJdGNaVUxDTkUzN2lUNW1KZ3p4dDRERTJIZUlTWWlyeUV3N3NhbUY5VmhVQU9WUlpyaGw2ZGZPQTk3LTBBRDBRREVwVFlqemptN3ZhSDlzamlmUXhIRjJma0VSTzl3cXE4M1d3Q3dWYmxMUE5Td01aZ2FvdVRhQnJKc083dWdmYmZiSE1xWFd3VDlZOEJoNUhsVVhIaFFw?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxNWVJhYWlRc3FYS2d3cDBfZG5GQ3lfUHFsUmIzTlR0ZmtaM1R1aUZTTXNTVWJQM3F2aDFxcTNHMEpKdWZlVS0xRFREVUhhbERQLWpQWG1OMGVVR3Y4cVNkWV9aeVBRaXdaN2h6alpwU1RuVEhVN1hWY0ZZN1VLWXljSk5ZSzBSTmtFbHFIS1FkaHc1UURIdFo4WDFaSXVoVW1qOS1UOGEzejhfVnRi?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxQRFZIMUQ3d3RzLXBMTVJZRVY5TVFNbGhleUdVQWFWWTg0ZHFRalRyblA5T2RWc1FlaEo3aXlPSkxwby1tZkxUWWRLWlZkLTk0MUNvcEVpR050RUpxVWptbDFzb01KTHRCNXRlRVliQ0FGTl90cThaTUlfNEprNHMtY2lzazhiaUktN0phMTd1NGhEYzNNNjN3cUFFSEVaZmVhNGQ4c1ozcjlXNjQzbFVkejlJYndPcDVkZHhDcHV0dWpJZ3BMcnNaWU1qTlNxNjVobUNlTVhvT1_SAd4BQVVfeXFMTTVqNGt5TFlJbHRjQ3ZPRG9oalVET1ZrZ0RyY0czeFpHeVJQdzdMa1F1THZhYjd3UDBoQUVESDB0dEh4SWlPN3hjV0FYREJOaGxxT3BBa09Udk1CSzJjdi1HUmMwaGpSa1pnVDZFWElTaklkTmg3OGc4YTVCT1NuakdXRUx1Tmd0dUIzbXpGbE9VWnpIRnFhV0xseEJyTEN6OVUzU1JkMUt5Uzh5LUtNX3BVak10UkxLZzZuMEtsYTdfZm9SWTViTlcwQ2RNMGNMRW5MQm9UZGUzenRQcjR3?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxOY0plSS1oM3NSdVRkMm56YzBfbEZPVGpmX0xVRTUtc1hYQnRsUUQ4bnBDZVNocTlFNTlhRVA3d21nTzlxMlZmQm1GSkpFbFFmZEdIalVVTWcyWEJMWTZEVUxHTTlzZnBZQjVfbmJLcExSRml1dUs5Umt3WGhzVUNUUHRqc0czX1VfN3ZzUFNyZGg0Y3RZNmxGeXpxVDV3bU9jc281a3lkdXBRZw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
