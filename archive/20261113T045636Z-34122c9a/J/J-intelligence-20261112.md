# J Intelligence Report

- ticker: **J**
- Report as_of: **2026-11-12**
- Market data as_of: **2026-11-12**
- Quant sources: https://finance.yahoo.com/quote/J/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/J/key-statistics/
- AI analysis snapshot as_of: **2026-11-12**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-13T05:13:50.894907+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 7, 'rule': 1, 'ai': 3, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261112T054014Z-6c47e7f9/J** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 7 unique headlines; 5 named publishers; 0 exact duplicates; 7 HTTPS source links; largest publisher share 28.57%; oldest publication 2026-11-05

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 158.6900 |
| Return 1D (%) | 0.7748 |
| Return 1W (%) | 7.5573 |
| Return 1M (%) | 13.8134 |
| Return YTD (%) | 20.7869 |
| Return 1Y (%) | 3.7257 |
| Annualized volatility (%) | 34.1174 |
| Beta vs SPY | 0.8720 |
| Max drawdown (%) | -30.2758 |
| Sharpe (rf=0) | 0.2798 |
| Downside deviation (rf=0, %) | 25.4609 |
| Sortino (rf=0) | 0.3749 |
| Historical VaR 95% (1D, %) | 3.0531 |
| Historical ES 95% (1D, %) | 5.4729 |
| Correlation vs SPY | 0.3510 |
| Tracking error vs SPY (%) | 31.9947 |
| P/E (trailing) | 52.72 |
| P/B | 5.69 |
| EV/EBITDA | 20.29 |
| Revenue growth (%) | 34.50 |
| Forward P/E (estimate) | 19.27 |
| Gross margin (%) | 22.07 |
| Operating margin (%) | 5.93 |
| Return on equity (%) | 8.00 |
| Free cash flow yield (%) | 3.48 |
| MA50 | 144.8486 |
| Close vs MA50 (%) | 9.5558 |
| MA200 | 134.2162 |
| Close vs MA200 (%) | 18.2346 |
| RSI (14, Wilder) | 63.5415 |
| MACD (12,26) | 3.9733 |
| MACD signal (9) | 3.5180 |
| MACD histogram | 0.4553 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'J': 281, 'SPY': 281}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 158.6900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.7748 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 7.5573 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 13.8134 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 20.7869 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 3.7257 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 34.1174 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 25.4609 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.3749 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.0531 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.4729 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3510 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.9947 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.8720 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -30.2758 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2798 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 19.2657 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 22.0670 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 5.9290 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 7.9980 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 3.4765 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 52.7209 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 63.5415 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.4553 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 9.5558 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 18.2346 -> Clearly above the moving-average trend level.

## TAILWINDS

### What Jacobs Solutions Shares Major Contract Wins Mean For Shareholders
- Summary: Jacobs wins major contracts, boosting future revenue prospects.
- Date: 2026-11-11 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxNeUpWeHIxOTRFR0s4TWZfa080U3IzSmZweTZBalUzSHNYSDdkdFo5cG03WW44T21Obm9iOE1mSnhrb3R5RGZBV1JlbWZBWW43bnVsN3d2bjltQ3pOZ3ZvaVlHcVB6MjhTemU1ZHJhVHJtUlM1Q0VmY0dGd1Z5SWhPYU9Jek50VUZyclJqVzFWS1prZFR4eFFzaGJjdUtZeHhjclROeGwtYUN2S2dJTjRQWVNYSFg3SVFWYlc5eUVZM2VFQXVFZWtwWmpqZE1sdHRoVW9UeS1ZdkHSAd4BQVVfeXFMTmV4NjNBOTZkMmZzZm5UcVRiLUNKX05PZ19aZURpWEZoZ2JUV3NqUmtOMXZKZ1JrSzMzcnlFV29LNUp0aGlReVhnUVpmOTE0TVpCX0MwOGZQbEZEQ2loeE5VVk9NRi1tdzBTTHRVaUdkN0htU3YyQUNyNXc3WDVrbEtrSEE1Qm5hMG1IWkdrR2QxZjBLNE5ENDNNZzh2YjN6dlNxUjhKNWZBcjEyc3BReVBDalR1N2FtcVRpckIxLWlMd1JkWV9wV0dMdXNMamF2VElPUEZxUHg1Uk91ZDF3?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Jacobs declares quarterly dividend
- Summary: Jacobs declares quarterly dividend
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigwFBVV95cUxQSWllWERLQ1FfQUlYQnVwU3JNZkQ0UjZScU5ycWduRVhrai1fVWpLUS1Vc3ZuSEpNUlg0NHdBWFhiVndhWXBDZFJ2WDYtOE42NHdhSlRGeFkyMDdydWJYT2dkUWFkTGZFckJJNWVfdmZhLUdLYnZMNWlzVzE2TFdZY1FWNA?oc=5>

### Jacobs Solutions (J) Lands New Zealand Highway Role, Is The Stock Still Trading At A Discount?
- Summary: Jacobs Solutions secures a new highway contract in New Zealand, potentially boosting revenue and market presence.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxQRFZIMUQ3d3RzLXBMTVJZRVY5TVFNbGhleUdVQWFWWTg0ZHFRalRyblA5T2RWc1FlaEo3aXlPSkxwby1tZkxUWWRLWlZkLTk0MUNvcEVpR050RUpxVWptbDFzb01KTHRCNXRlRVliQ0FGTl90cThaTUlfNEprNHMtY2lzazhiaUktN0phMTd1NGhEYzNNNjN3cUFFSEVaZmVhNGQ4c1ozcjlXNjQzbFVkejlJYndPcDVkZHhDcHV0dWpJZ3BMcnNaWU1qTlNxNjVobUNlTVhvT1_SAd4BQVVfeXFMTTVqNGt5TFlJbHRjQ3ZPRG9oalVET1ZrZ0RyY0czeFpHeVJQdzdMa1F1THZhYjd3UDBoQUVESDB0dEh4SWlPN3hjV0FYREJOaGxxT3BBa09Udk1CSzJjdi1HUmMwaGpSa1pnVDZFWElTaklkTmg3OGc4YTVCT1NuakdXRUx1Tmd0dUIzbXpGbE9VWnpIRnFhV0xseEJyTEN6OVUzU1JkMUt5Uzh5LUtNX3BVak10UkxLZzZuMEtsYTdfZm9SWTViTlcwQ2RNMGNMRW5MQm9UZGUzenRQcjR3?oc=5>

### A New Zealand highway project includes 15 bridges and twin tunnels. Jacobs will design them.
- Summary: Jacobs will design 15 bridges and twin tunnels for a New Zealand highway project, expanding its infrastructure portfolio.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOcWhuamZKb09FVVljX3pPOEl3UDVCMm16TEdnRUJqQjVXLTZJTWdQcUd6a1hsWHJrTS1aWmZxNmxpSnpZbW8wLXdSN2ozUEJGalZ5dElYMkprOHJ3WWFONzZLUnRTX3YwdGctZkY5UUg2aFluby1oMGJqeHVlSXpLNjVubndCRHJVN1pzOEdQTG9qYjdoVmZTZFdYbnhudw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **J** | **52.72** | **5.69** | **20.29** | **34.50** | **18,572,857,344.00 USD** | **3.73** |
| ACM | 24.69 | 4.11 | 12.38 | -14.20 | 9,022,906,368.00 USD | -46.30 |
| FLR | N/A | 2.49 | 11.22 | 10.50 | 6,347,684,352.00 USD | 8.29 |
| KBR | 10.27 | 2.53 | 9.77 | 5.00 | 4,454,169,088.00 USD | -15.49 |

Peers fetched as_of: 2026-11-12; J reuses existing data (market data as_of: 2026-11-12); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-04
- Next expected earnings: 2026-11-23 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-12

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMi2AFBVV95cUxNeUpWeHIxOTRFR0s4TWZfa080U3IzSmZweTZBalUzSHNYSDdkdFo5cG03WW44T21Obm9iOE1mSnhrb3R5RGZBV1JlbWZBWW43bnVsN3d2bjltQ3pOZ3ZvaVlHcVB6MjhTemU1ZHJhVHJtUlM1Q0VmY0dGd1Z5SWhPYU9Jek50VUZyclJqVzFWS1prZFR4eFFzaGJjdUtZeHhjclROeGwtYUN2S2dJTjRQWVNYSFg3SVFWYlc5eUVZM2VFQXVFZWtwWmpqZE1sdHRoVW9UeS1ZdkHSAd4BQVVfeXFMTmV4NjNBOTZkMmZzZm5UcVRiLUNKX05PZ19aZURpWEZoZ2JUV3NqUmtOMXZKZ1JrSzMzcnlFV29LNUp0aGlReVhnUVpmOTE0TVpCX0MwOGZQbEZEQ2loeE5VVk9NRi1tdzBTTHRVaUdkN0htU3YyQUNyNXc3WDVrbEtrSEE1Qm5hMG1IWkdrR2QxZjBLNE5ENDNNZzh2YjN6dlNxUjhKNWZBcjEyc3BReVBDalR1N2FtcVRpckIxLWlMd1JkWV9wV0dMdXNMamF2VElPUEZxUHg1Uk91ZDF3?oc=5
- https://news.google.com/rss/articles/CBMigwFBVV95cUxQSWllWERLQ1FfQUlYQnVwU3JNZkQ0UjZScU5ycWduRVhrai1fVWpLUS1Vc3ZuSEpNUlg0NHdBWFhiVndhWXBDZFJ2WDYtOE42NHdhSlRGeFkyMDdydWJYT2dkUWFkTGZFckJJNWVfdmZhLUdLYnZMNWlzVzE2TFdZY1FWNA?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxQRFZIMUQ3d3RzLXBMTVJZRVY5TVFNbGhleUdVQWFWWTg0ZHFRalRyblA5T2RWc1FlaEo3aXlPSkxwby1tZkxUWWRLWlZkLTk0MUNvcEVpR050RUpxVWptbDFzb01KTHRCNXRlRVliQ0FGTl90cThaTUlfNEprNHMtY2lzazhiaUktN0phMTd1NGhEYzNNNjN3cUFFSEVaZmVhNGQ4c1ozcjlXNjQzbFVkejlJYndPcDVkZHhDcHV0dWpJZ3BMcnNaWU1qTlNxNjVobUNlTVhvT1_SAd4BQVVfeXFMTTVqNGt5TFlJbHRjQ3ZPRG9oalVET1ZrZ0RyY0czeFpHeVJQdzdMa1F1THZhYjd3UDBoQUVESDB0dEh4SWlPN3hjV0FYREJOaGxxT3BBa09Udk1CSzJjdi1HUmMwaGpSa1pnVDZFWElTaklkTmg3OGc4YTVCT1NuakdXRUx1Tmd0dUIzbXpGbE9VWnpIRnFhV0xseEJyTEN6OVUzU1JkMUt5Uzh5LUtNX3BVak10UkxLZzZuMEtsYTdfZm9SWTViTlcwQ2RNMGNMRW5MQm9UZGUzenRQcjR3?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOcWhuamZKb09FVVljX3pPOEl3UDVCMm16TEdnRUJqQjVXLTZJTWdQcUd6a1hsWHJrTS1aWmZxNmxpSnpZbW8wLXdSN2ozUEJGalZ5dElYMkprOHJ3WWFONzZLUnRTX3YwdGctZkY5UUg2aFluby1oMGJqeHVlSXpLNjVubndCRHJVN1pzOEdQTG9qYjdoVmZTZFdYbnhudw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
