# AMD Intelligence Report

- ticker: **AMD**
- Report as_of: **2026-11-16**
- Market data as_of: **2026-11-16**
- Quant sources: https://finance.yahoo.com/quote/AMD/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMD/key-statistics/
- AI analysis snapshot as_of: **2026-11-16**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-17T06:47:04.959201+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 5, 'ai': 9, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261116T043911Z-b81cfeb4/AMD** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 15 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 17.39%; oldest publication 2026-11-12

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 504.2800 |
| Return 1D (%) | -5.5762 |
| Return 1W (%) | -0.8455 |
| Return 1M (%) | -4.6279 |
| Return YTD (%) | 135.4688 |
| Return 1Y (%) | 104.3191 |
| Annualized volatility (%) | 73.7482 |
| Beta vs SPY | 3.4428 |
| Max drawdown (%) | -37.7290 |
| Sharpe (rf=0) | 1.3805 |
| Downside deviation (rf=0, %) | 48.1023 |
| Sortino (rf=0) | 2.1165 |
| Historical VaR 95% (1D, %) | 6.7196 |
| Historical ES 95% (1D, %) | 9.6472 |
| Correlation vs SPY | 0.6427 |
| Tracking error vs SPY (%) | 65.7516 |
| P/E (trailing) | 107.75 |
| P/B | 12.09 |
| EV/EBITDA | 73.63 |
| Revenue growth (%) | 44.70 |
| Forward P/E (estimate) | 28.59 |
| Gross margin (%) | 56.00 |
| Operating margin (%) | 17.82 |
| Return on equity (%) | 11.96 |
| Free cash flow yield (%) | 0.89 |
| MA50 | 555.0864 |
| Close vs MA50 (%) | -9.1529 |
| MA200 | 424.4558 |
| Close vs MA200 (%) | 18.8062 |
| RSI (14, Wilder) | 46.7311 |
| MACD (12,26) | -9.1796 |
| MACD signal (9) | -14.5527 |
| MACD histogram | 5.3731 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMD': 283, 'SPY': 283}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 504.2800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -5.5762 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.8455 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -4.6279 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 135.4688 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 104.3191 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 73.7482 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 48.1023 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.1165 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 6.7196 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 9.6472 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6427 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 65.7516 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.4428 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -37.7290 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.3805 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 28.5901 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 56.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 17.8210 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 11.9600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.8895 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 107.7521 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 46.7311 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 5.3731 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -9.1529 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 18.8062 -> Clearly above the moving-average trend level.

## TAILWINDS

### AMD Soars 19% in a Week on Oppenheimer’s Upgrade and Nvidia’s Turmoil: “Demand Is Higher Than Supply”
- Summary: AMD Soars 19% in a Week on Oppenheimer’s Upgrade and Nvidia’s Turmoil: “Demand Is Higher Than Supply”
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxPcmVMTGswUS0wN3NIX3JINlBfam5uWUhmZURPNC1Tbkl6dk5GRF92LW54dGNRWGlCQjVmWml6QnBhQkZYRkpOVGMzenZnMkIwMDEyQ3JRMF9RVWR5SXkyLUVmSEY3MlN1cHRfdnpwM2FBbkhXTkJpQ2h6OVVKUXllbm56NVNXcndqdTFqdklwdEZhUEdEd3Zyb0o3dW1wMFBBLXRUbE1adnR5Rk5XYmhSQlNVa0NYS3Vra255TkNHcw?oc=5>

## HEADWINDS

### AMD Stock Is Falling Monday: What's Going On?
- Summary: AMD Stock Is Falling Monday: What's Going On?
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNVEx2ZDZhQ3JoM0s1WnlsUE9icG5hQjRnT1pIR250WkNWU0ZkclVubEMwWmNOSFBSX3M3dGpsSHltWVdSRWZka3plbnlodFRVdTZTRFIzcUluNnJnRlVScFBtcEFkVXVPQkpmMVZabXZFRXlSUEotNnA5cWw2MnVFb0RNZTMxQThjS3pNNVBESl9ueUVjQm9jOHRkNA?oc=5>

### AMD Stock Slips After the Chipmaker Completed Its World Labs Acquisition
- Summary: AMD Stock Slips After the Chipmaker Completed Its World Labs Acquisition
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNNHgyRkhVVUoxX0ZHTzI1d05ORklOaDgwTndmYWNFSDY4NC02ZVVSN01FMEpYV00tb1l3SDg1R2RoZFllbmhnSEt2cHpnT05BaEQ2Vzk1bmFrSUE4amo0eG41Nm5yN3lpeXgxUDY3c2FqbnhVOGoySVZtN0s5WkRFajhOc0t2ajhkZkN2Zkk3VWFRUy1aQzNfbGVDeU1UYWhvQ2EtTw?oc=5>

### Advanced Micro Devices (NASDAQ:AMD) Stock Falls 5.6% After Insider Selling
- Summary: Advanced Micro Devices (NASDAQ:AMD) Stock Falls 5.6% After Insider Selling
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxQWmt4NXdpU0pJWDNIUHgwNDNnZlQ5RVZZb3QxVnZ3X0tyaFQwSnhSZ3puS3hEZlFaTHp6Tl9HN20xRTJPT3ItRXhHZHpTbTBhNmJuWDZwZUFaa19zX1MxM2laV0x4dDdZeUVReXBQbllfR2duYm5lVkVEZ1E4bzA0RGxpdUtXYVV5cTktbndndnk2b2tLdEtVNlRaWkE2blZHcnN2MDJWMXhnTDBwclczVXB1dkRsMWJDTF9oOWhuMWoyeE54ZHh2Z19R?oc=5>

### AMD Stock Falls 11.8% as Intel’s PC Warning Triggers Chip Selloff Ahead of Nov. 3 Results
- Summary: AMD Stock Falls 11.8% as Intel’s PC Warning Triggers Chip Selloff Ahead of Nov. 3 Results
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxQekZqN1pObDV4WVdQVmVhb0lMVnY2NXhpbWdaUmc3STdBWWNPTnhQQzBWWl9qOUNXaHg2TGVHX0p3SVpWLVpGSTVDcXp4dzlqWHdOVDZ1MmZacmotR1hYV3czVWdES21BRnh2aDRPQ0JqNGg4WC0wOGwxSkw5LWVYRzlMMXUtUmg3UmtUVHY4MUVGdkFOaWZmQ1FTeGpRam9DcEgtbDZoZ3ltemJLcXQxT0xyUDA?oc=5>

## CATALYSTS

### Is AMD Stock Still a Buy After Its Post-Earnings Jump?
- Summary: Analyst review of AMD’s post‑earnings performance and future outlook.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxNV3pfTDhZVFA2X1AzQVFxNGREbHlmdk9KRF9SeTkwakhtcXlsNnAwUzVSSnZYbkdHbGxDb21LY2hXTGFoN1NWZ2FpOFF3Q2RrR0VNZnFtaFFyNGkzOHFwWjRHX3ZDVmFOV19ENWJHOUZQd0lsQ1M1MVpUTVpWNE1iS2IwQi1wZ2FuMmhfQmM0M0NrcVhVTFQ4am5ZRG9WcmZhNTVEVUYzcjdnSHZpZG1FUWp4cw?oc=5>

### AMD Will Capture More Market Share Than Broadcom to End November as Nvidia's Leadership Vacuum Persists
- Summary: Forecast that AMD will overtake Broadcom in market share by end of November.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi3wFBVV95cUxNUEtFa05wLWJTVmlmb3NGOWhSem8wTEZzaS1SYThoRGJSU0I5azhlVndSQkx0MnZueEM0NnF5UjIya09zckRrNzVvUHpNM2hwS2J6ZjVXTUZBX19LaWEzcDRFOWVDbkNkRFdGSklueUQ3ckxYNHJRSTQ1YUVkZjRWaHhldlpBemd5VXdkUFpzMk1mZUJmeUhYRFUyR1BaTkRMQ3dZZjJ3Z2dnZjFEOW1TTVhwY1k0ck5ZblRyTU85aC1FM1pqYXBJaklxb0hLSGR6QmtHa0l4aXNvdHBJSUFB?oc=5>

### Broadcom Is Better Positioned Than AMD As Nvidia Struggles (NASDAQ:AMD)
- Summary: Analyst comparison favoring Broadcom over AMD amid Nvidia challenges.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPeVNvOVdabnY3cFlGR0MtVm9ZcTRSRjlKS2t5WVBYbElRelBic3VORTdpYkZoclg3c3gxOHJ6b0NRLVNnbFUyTGdaMl9RQzREaWc4cl9wUEpCRXlyT1hoZkFzQkdsV3pvQ0F3V0FUWkw5dnkzUGVUYkVMM1N1RExBYUw5clJiVUN1UEJOQ0N1Z2I4cWVQcmpDREpWYkdEZFZm?oc=5>

### Why Are AMD, Broadcom and Nvidia Stocks Falling Today? New US Chip Restrictions Hit AI Stocks
- Summary: Market move: stocks fall due to new US chip restrictions affecting AI sector.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTE0zdFZiOUY0aEh4MjJvNXp4anNwaGd0SXU3OXczdTVBamZ2dE1lVThQTTh2R3BpcWhPMEFhZGJDWHBpbHVhbFdNdHVGVHRkdC1PRjJBZkQxVk8wVmNGc05NS3dsdFZuVkhvaFowV3V6alhIQkdwR1NwanBEVlQ2Zw?oc=5>

### Why AMD Stock Was Sliding Today
- Summary: AMD shares fell today, reflecting market concerns.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNb2ctVEw4Q2ZFLXlpc2ZpeUFwaS0xSDI2Q2tRc2dtMzJmaGJwZjNoakZiTGxZVDhXUUJsWjRwR0dFamttd25sZWk4b0h6bDJZa3llbFE0YV9ub3NfbnItZ0xRejR0MzZoSy02bzh5bXVGWHJBLXVsQjN3ZHhmOXRWQlZJSEtONzQ5cXpsX0dxTGtuZWpnTDBn?oc=5>

### Advanced Micro Devices vs. Broadcom: One Stock Has a $27 Billion Advantage Investors Shouldn't Ignore
- Summary: AMD outperforms Broadcom with a $27B advantage.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi6gFBVV95cUxNRzNNRXMtVjVTc3RiVHcyaTAxcDZjOUlLbFp0X205cUZqajRQV2c5X3NqNkwxS1dZck11VndPRi1SZllZVk5oLVpTNEc3NDV5cnd4WmpsUWM4Z1ZoTWVMbVdKTFJETlJLZUhUZEhvck9uRUM4LW8xOEh2OGNMaEtZYzZnWHJia2tETDNFR09Qd29kOERTVW5rSXJqTm5PS2ZNdFp4aXAzUFV4S0djSktTVEV2d0Y1UE52YnZGREZUaUtnakliMEpuTVJHYmc4Z3pCbVpSSlFFVGNLUDI0c2hBc1F5NUh3c3NDaEE?oc=5>

### Advanced Micro Devices And 2 Other High Growth Stocks
- Summary: AMD highlighted among high-growth picks.
- Date: 2026-11-16 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNTUhzLTRyOXRpNzlWd2hJcmhOS3A3MUtUUXdJQU4wOFpsWFktU0M5RHJMM1pHaDhTNEFLSFp6TEN2SzNVeTQtZ3czSXFqWVlldkJsQnJfLXViWWg5anBQMTdsb2JnTEZwcGFaZHQ0aHk3S2ZLM2VmZ0lBanp4Z1FDN3pUVXgyTTFrSVZxcnhTOUh6U0p1U1Q1d2FKRQ?oc=5>

### Why Did AMD Stock Fall Nearly 9%?
- Summary: AMD shares fell nearly 9% amid market concerns and negative sentiment.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPNmtGWUNXRkFFeVJ2R05jV21rOUhNakxMaF9pcm5UemVZaF9qbVBGeUg2SHhKV3EwX2diNC1kV3lVLTBVaEJNY0xxU3VPTmxhbjlJbk90VEhmWUtlWWpWbWZVZEdfM1NYNmVaWDNsa2JUV0xSalh5LWZsVVFMZ3JpT0dSQ0Q4SUc0MEk3Uk5kX0VsQmZuU0c1MUNXOFZldlZibE9HR2V5TXhtZw?oc=5>

### Advanced Micro Devices (AMD) Stock Jumped, What Is Driving Attention Today?
- Summary: AMD shares surged, driven by positive market attention and favorable sentiment.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOZXNNdTVSVWJDXzBCZFQ2bHh5a0k1Vzd2Y1Y2SzhuRXN1T1F4dHY0M2tQRzVOc3FxX1NqN19rOHA3WWpjT2RDU1UxMDMxcmx0ZlREVHBtTXo3ajNzTEpGb3FUTGFYaTBDZ25LVGNmaXBtOG4xcDlMckoyeUlvbHdqSXVna0tfLTNGQldrSjFLR3lGaXZnN195ZV9QcXZVUQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMD** | **107.75** | **12.09** | **73.63** | **44.70** | **827,063,205,888.00 USD** | **104.32** |
| NVDA | 19.74 | 16.47 | 18.58 | 105.90 | 3,770,312,556,544.00 USD | -17.70 |
| INTC | N/A | 2.56 | 16.07 | 20.90 | 294,823,034,880.00 USD | 56.17 |
| AVGO | 42.58 | 15.97 | 31.13 | 85.50 | 1,591,528,259,584.00 USD | -1.92 |

Peers fetched as_of: 2026-11-16; AMD reuses existing data (market data as_of: 2026-11-16); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-03
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-16

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 1,584,000,000.00 USD; period 2017-07-02/2017-09-30; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 2,428,000,000.00 USD; period 2026-06-28/2026-09-26; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMivwFBVV95cUxPcmVMTGswUS0wN3NIX3JINlBfam5uWUhmZURPNC1Tbkl6dk5GRF92LW54dGNRWGlCQjVmWml6QnBhQkZYRkpOVGMzenZnMkIwMDEyQ3JRMF9RVWR5SXkyLUVmSEY3MlN1cHRfdnpwM2FBbkhXTkJpQ2h6OVVKUXllbm56NVNXcndqdTFqdklwdEZhUEdEd3Zyb0o3dW1wMFBBLXRUbE1adnR5Rk5XYmhSQlNVa0NYS3Vra255TkNHcw?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNVEx2ZDZhQ3JoM0s1WnlsUE9icG5hQjRnT1pIR250WkNWU0ZkclVubEMwWmNOSFBSX3M3dGpsSHltWVdSRWZka3plbnlodFRVdTZTRFIzcUluNnJnRlVScFBtcEFkVXVPQkpmMVZabXZFRXlSUEotNnA5cWw2MnVFb0RNZTMxQThjS3pNNVBESl9ueUVjQm9jOHRkNA?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNNHgyRkhVVUoxX0ZHTzI1d05ORklOaDgwTndmYWNFSDY4NC02ZVVSN01FMEpYV00tb1l3SDg1R2RoZFllbmhnSEt2cHpnT05BaEQ2Vzk1bmFrSUE4amo0eG41Nm5yN3lpeXgxUDY3c2FqbnhVOGoySVZtN0s5WkRFajhOc0t2ajhkZkN2Zkk3VWFRUy1aQzNfbGVDeU1UYWhvQ2EtTw?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxQWmt4NXdpU0pJWDNIUHgwNDNnZlQ5RVZZb3QxVnZ3X0tyaFQwSnhSZ3puS3hEZlFaTHp6Tl9HN20xRTJPT3ItRXhHZHpTbTBhNmJuWDZwZUFaa19zX1MxM2laV0x4dDdZeUVReXBQbllfR2duYm5lVkVEZ1E4bzA0RGxpdUtXYVV5cTktbndndnk2b2tLdEtVNlRaWkE2blZHcnN2MDJWMXhnTDBwclczVXB1dkRsMWJDTF9oOWhuMWoyeE54ZHh2Z19R?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxQekZqN1pObDV4WVdQVmVhb0lMVnY2NXhpbWdaUmc3STdBWWNPTnhQQzBWWl9qOUNXaHg2TGVHX0p3SVpWLVpGSTVDcXp4dzlqWHdOVDZ1MmZacmotR1hYV3czVWdES21BRnh2aDRPQ0JqNGg4WC0wOGwxSkw5LWVYRzlMMXUtUmg3UmtUVHY4MUVGdkFOaWZmQ1FTeGpRam9DcEgtbDZoZ3ltemJLcXQxT0xyUDA?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxNV3pfTDhZVFA2X1AzQVFxNGREbHlmdk9KRF9SeTkwakhtcXlsNnAwUzVSSnZYbkdHbGxDb21LY2hXTGFoN1NWZ2FpOFF3Q2RrR0VNZnFtaFFyNGkzOHFwWjRHX3ZDVmFOV19ENWJHOUZQd0lsQ1M1MVpUTVpWNE1iS2IwQi1wZ2FuMmhfQmM0M0NrcVhVTFQ4am5ZRG9WcmZhNTVEVUYzcjdnSHZpZG1FUWp4cw?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxNY2tWSWpSOG1mdjFDTWhTM3JFN19TcnhMRE9uZVFzTjREdTExeXh2QlN3NnhZSmtDd0ZtdTMtNGlTay1yR3NYVUZQVlN4ZlUweWk3WTdpcWpJU096Wmhfemcza1BUZllCeDl0eWlCUl9QMmQyai1RME5tRkl0M3BMeTZxM2JhSW8xR3RqcVlxcVQ3OHF2RmQ5SnV1NkNaWVRORkRwREs0V1hfaXZHd2tmQmE5ZnkzZ0hEYVd5UWpMVHRsT1BtOVB1a3RBNWhNbW9yS1Rr?oc=5
- https://news.google.com/rss/articles/CBMi3wFBVV95cUxNUEtFa05wLWJTVmlmb3NGOWhSem8wTEZzaS1SYThoRGJSU0I5azhlVndSQkx0MnZueEM0NnF5UjIya09zckRrNzVvUHpNM2hwS2J6ZjVXTUZBX19LaWEzcDRFOWVDbkNkRFdGSklueUQ3ckxYNHJRSTQ1YUVkZjRWaHhldlpBemd5VXdkUFpzMk1mZUJmeUhYRFUyR1BaTkRMQ3dZZjJ3Z2dnZjFEOW1TTVhwY1k0ck5ZblRyTU85aC1FM1pqYXBJaklxb0hLSGR6QmtHa0l4aXNvdHBJSUFB?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPeVNvOVdabnY3cFlGR0MtVm9ZcTRSRjlKS2t5WVBYbElRelBic3VORTdpYkZoclg3c3gxOHJ6b0NRLVNnbFUyTGdaMl9RQzREaWc4cl9wUEpCRXlyT1hoZkFzQkdsV3pvQ0F3V0FUWkw5dnkzUGVUYkVMM1N1RExBYUw5clJiVUN1UEJOQ0N1Z2I4cWVQcmpDREpWYkdEZFZm?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTE0zdFZiOUY0aEh4MjJvNXp4anNwaGd0SXU3OXczdTVBamZ2dE1lVThQTTh2R3BpcWhPMEFhZGJDWHBpbHVhbFdNdHVGVHRkdC1PRjJBZkQxVk8wVmNGc05NS3dsdFZuVkhvaFowV3V6alhIQkdwR1NwanBEVlQ2Zw?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNb2ctVEw4Q2ZFLXlpc2ZpeUFwaS0xSDI2Q2tRc2dtMzJmaGJwZjNoakZiTGxZVDhXUUJsWjRwR0dFamttd25sZWk4b0h6bDJZa3llbFE0YV9ub3NfbnItZ0xRejR0MzZoSy02bzh5bXVGWHJBLXVsQjN3ZHhmOXRWQlZJSEtONzQ5cXpsX0dxTGtuZWpnTDBn?oc=5
- https://news.google.com/rss/articles/CBMif0FVX3lxTE9IOUNQbENMZy1MWld4LV90Y2o5cThZbG9uVU96R3dOWVFMTGlRZzhqa2lfZzhTUEZ5X2lQRjM0bVZmbTBiVEJxaWdqQ3pqOXR0dENTbVA3VGpseXJQZVlwMjNVTkNFOUUzRTREMTQxU3gxUVpLaXZ3UmdkZ1hYd2c?oc=5
- https://news.google.com/rss/articles/CBMi6gFBVV95cUxNRzNNRXMtVjVTc3RiVHcyaTAxcDZjOUlLbFp0X205cUZqajRQV2c5X3NqNkwxS1dZck11VndPRi1SZllZVk5oLVpTNEc3NDV5cnd4WmpsUWM4Z1ZoTWVMbVdKTFJETlJLZUhUZEhvck9uRUM4LW8xOEh2OGNMaEtZYzZnWHJia2tETDNFR09Qd29kOERTVW5rSXJqTm5PS2ZNdFp4aXAzUFV4S0djSktTVEV2d0Y1UE52YnZGREZUaUtnakliMEpuTVJHYmc4Z3pCbVpSSlFFVGNLUDI0c2hBc1F5NUh3c3NDaEE?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNTUhzLTRyOXRpNzlWd2hJcmhOS3A3MUtUUXdJQU4wOFpsWFktU0M5RHJMM1pHaDhTNEFLSFp6TEN2SzNVeTQtZ3czSXFqWVlldkJsQnJfLXViWWg5anBQMTdsb2JnTEZwcGFaZHQ0aHk3S2ZLM2VmZ0lBanp4Z1FDN3pUVXgyTTFrSVZxcnhTOUh6U0p1U1Q1d2FKRQ?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPNmtGWUNXRkFFeVJ2R05jV21rOUhNakxMaF9pcm5UemVZaF9qbVBGeUg2SHhKV3EwX2diNC1kV3lVLTBVaEJNY0xxU3VPTmxhbjlJbk90VEhmWUtlWWpWbWZVZEdfM1NYNmVaWDNsa2JUV0xSalh5LWZsVVFMZ3JpT0dSQ0Q4SUc0MEk3Uk5kX0VsQmZuU0c1MUNXOFZldlZibE9HR2V5TXhtZw?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOZXNNdTVSVWJDXzBCZFQ2bHh5a0k1Vzd2Y1Y2SzhuRXN1T1F4dHY0M2tQRzVOc3FxX1NqN19rOHA3WWpjT2RDU1UxMDMxcmx0ZlREVHBtTXo3ajNzTEpGb3FUTGFYaTBDZ25LVGNmaXBtOG4xcDlMckoyeUlvbHdqSXVna0tfLTNGQldrSjFLR3lGaXZnN195ZV9QcXZVUQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
