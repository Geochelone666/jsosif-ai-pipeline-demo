# NVO Intelligence Report

- ticker: **NVO**
- Report as_of: **2026-11-24**
- Market data as_of: **2026-11-24**
- Quant sources: https://finance.yahoo.com/quote/NVO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVO/key-statistics/
- AI analysis snapshot as_of: **2026-11-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-25T07:19:42.037026+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 4, 'ai': 11, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **11** exact headline/source/date matches; prior report **20261124T081701Z-6c335e3d/NVO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 11 named publishers; 1 exact duplicates; 22 HTTPS source links; largest publisher share 22.73%; oldest publication 2026-11-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 40.3100 |
| Return 1D (%) | 2.9893 |
| Return 1W (%) | -0.9582 |
| Return 1M (%) | 3.2266 |
| Return YTD (%) | -16.8193 |
| Return 1Y (%) | -5.8876 |
| Annualized volatility (%) | 45.2550 |
| Beta vs SPY | 0.9316 |
| Max drawdown (%) | -43.6699 |
| Sharpe (rf=0) | 0.0962 |
| Downside deviation (rf=0, %) | 33.6003 |
| Sortino (rf=0) | 0.1295 |
| Historical VaR 95% (1D, %) | 3.1053 |
| Historical ES 95% (1D, %) | 6.9779 |
| Correlation vs SPY | 0.3079 |
| Tracking error vs SPY (%) | 43.0692 |
| P/E (trailing) | 10.18 |
| P/B | 5.43 |
| EV/EBITDA | 1.46 |
| Revenue growth (%) | 5.60 |
| Forward P/E (estimate) | 11.48 |
| Gross margin (%) | 83.33 |
| Operating margin (%) | 50.78 |
| Return on equity (%) | 58.38 |
| Free cash flow yield (%) | N/A |
| MA50 | 39.4566 |
| Close vs MA50 (%) | 2.1629 |
| MA200 | 42.2026 |
| Close vs MA200 (%) | -4.4846 |
| RSI (14, Wilder) | 51.6420 |
| MACD (12,26) | -0.0948 |
| MACD signal (9) | 0.0611 |
| MACD histogram | -0.1559 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVO': 289, 'SPY': 289}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 40.3100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.9893 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.9582 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 3.2266 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -16.8193 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -5.8876 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 45.2550 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 33.6003 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.1295 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.1053 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.9779 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3079 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 43.0692 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.9316 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -43.6699 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.0962 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 11.4764 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 83.3330 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 50.7790 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 58.3840 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 10.1793 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 51.6420 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.1559 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 2.1629 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -4.4846 -> Slightly below the moving-average trend level.

## TAILWINDS

### Novo Nordisk stock advances as weak momentum tempers recent gains
- Summary: Novo Nordisk stock advances as weak momentum tempers recent gains
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxPMk1tMTY4QmtJRGpxWllQZTZRNlpIeDN5enNfdDk3c043TVpTTlRsbEZjU0EwRVJFaktPX0ZkVm1mdjlXZ0FOd2JCbXlXdE5WTDJmWTR5c2tqa1h0cUswTUJZVGJONHBVMHV3LUF2UXJNM3hROWNVN0p4WXVLektDNFRueWxoc1VkQjZsSQ?oc=5>

### Novo Nordisk's Wegovy Pill Is Capturing 80% of New Oral Obesity Prescriptions. Is NVO Stock a Buy?
- Summary: Wegovy captures majority of new prescriptions, indicating strong demand.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxOZDBGdWNCLUg1eGlGWDRnVXdGbzEzUU5hMXRHd2t1endJMlhQby1Jd0lXSFZnNGdLNHVvSHFZdlNETlQzU0U2VmxqczVPUlM1aTFLLWdJMmNNc0ctTmpaNFRrTnVwWlh3RDNuWmZxQnMxcWZoWXBwVXh0dHhQNjVsUTIzUGF0bXJMc1EyWWwwbk9iT0ZvaENtVmNVcWV5a1lJR1RScm5FMVdmOF9BME5UV1JwdElrS0RYOUFJRkVINkZ2YW5UdFc4VDFpSGlSWUhPUFFB?oc=5>

### Novo Nordisk: A Return To Growth May Be Just Around The Corner (NYSE:NVO)
- Summary: Anticipated return to growth signals favorable outlook for the company.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNYi1OZnF4N2hudHlDM1lRQjVwd2xHOG1UamNXX1pKLVBjMTBaVWVoWTkwdXZQV0YtVy1EYy0xYzJ6Q2Vwc1BqR3FKYnNFZk83TjBXdE1QdDh3a2RZYmNiZ1NZdUd6Q2R3akttNnk3dGhaOXNUeVJJV0hEMGFIc2tQOE4wQVlqa0k0cWNvUWZOZEdmTmpkaDhfRkxsVFJDaEpqRks5Vg?oc=5>

### Novo Nordisk (NYSE: NVO) Trades At A Decade-Low Valuation Even As Its Wegovy Pill Dominates Oral GLP-1 Market
- Summary: Low valuation coupled with Wegovy market dominance signals potential upside.
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi6wFBVV95cUxPUkItU0xjMHAtejlZR1oybGZSOVhMd1VhRHZqS2pPSGx0ZmxzT1hRSHFZQ0tqVFNJeTVDaER1eXgxeTk5Slp5a05oZUhvc0xubm9TZ1Q1U0tTdnBwb1ROeklqQWZOSTIwaGhYckpCSHVSRmRSTXVLNUd3WE1acGJYcnZwMkRleWc2TWk2dEZjUmxScFB5aDlZY0xhTkpjN0tuZXFBazRXRzJjSHdqNjlvYy11Q2NUcnJjZUJ4VUIwbS03aWtrQTZDNTlYTWY5ekdoTm5MN1J6dUNXQ2pUN213Z1NBYWJRZm8wLUZJ?oc=5>

### Novo Nordisk (NYSE: NVO) Targets Underserved Pediatric Patients As Weekly Sogroya Clears FDA Hurdle
- Summary: Novo Nordisk announces Sogroya FDA clearance, targeting underserved pediatric patients, indicating product expansion and potential revenue growth.
- Date: 2026-11-24 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMi3gFBVV95cUxPcm1NaWN5SEV1VVFwdHhCaXMzNndhcVlnNTltZmx0anN2QURxejJqSnlfczEtNjNSZDhDMjdKaTcweFNaeUp1VDhyckpGX0xmVEp1RGlDSWFHWDlPNFJsM2t5UnNIRGlEaFFHWnVmRC0weTk1bFpMSDdydEEzMVhKNld4anUtdGhUMEw2TE4tR2dvNjBwNWxZaFNxT2tGaVdDRGtsU1hZbkh2cjRDdmRKdTBGSzA0czl1dXJ1bmhLaTJWZmw1VE9zT0hGLXQ4QS0yMlAxeTgteWxJUGl2UFE?oc=5>

## HEADWINDS

### Novo Nordisk (NVO) Could Be 47% Below Fair Value Following Its AI Push
- Summary: AI push may have led to undervaluation, suggesting a short‑term headwind.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxNVVh1Z1RmUDEwd3JUV3J0V3VqeGVGaks0RGVhMVFjcDFveEVQX0xuQjhrbTNoazVzZVhFNGJUR3FlNTZUUG5xWmduaTVfQWF4akYzbEItc1BRYXlfb1N6TG5xaXZfcmlKUGJJOWJCbE9felhCd3ZRRUNtSGhDU2dpRnl1Q1lGZHBYVlh1RXotNA?oc=5>

## CATALYSTS

### Novo Nordisk stock gains more than 2% after FDA greenlights SOGROYA and repurchase plan advances
- Summary: Novo Nordisk stock gains more than 2% after FDA greenlights SOGROYA and repurchase plan advances
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxOcjB1NlROdkt0RnhrUUZpSHBHSUJqX2paVVNHNVlCdTdpS3I3WGlxSUZ2UUc4dVB6ek1LSFNtNEhiMTU3YWFyZ1BRU0g5LVlBY1dkN1ZnNUJsY01zTTRTV0gxSzM1WHcwTlo0TDduM21adGw0OUtpQ3FQeEp0TWhhOEktY1Utc0FWYUFaS09HNHo?oc=5>

### Novo Nordisk A/S - share repurchase programme
- Summary: Novo Nordisk A/S - share repurchase programme
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxOTlRFSGxyelpHekxRM0RWaXpjb3lid3RNTXNiZGQyTXFpS0tEZEk2QkRsdEhqa1FuUmNDb1lORDlyWEZ0cl9oUWcxME9SVTRSaEw1X1ZNWVo5SThIeHUybWk1aldRVno2Ujlmb0pPS2pMSzVxNEZFRFZWMjRGZkR2clBzRFU3R2tkTHFhbjVBVmk?oc=5>

### Novo Nordisk Details Share Repurchases Through November 13
- Summary: Novo Nordisk Details Share Repurchases Through November 13
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxQY2FUTUpIWjZ3VnpzdWtKTjlxWEViNVpES3R3dFktSVJ0eE5FRTdrOFNvOW9CR2FtUzhJNnRDWTdubzl3NW1iTUg2YmlvemRWYnZCRlNkTlU0ZWFxUVJDdmFfcW5YZEpMOTBBUng5ZW1taXlQSkd6a2I1QWkzVnJaRmFRRllSM0ZMYTg5WG5pTnNyMzMzNlM2T0gyYlR2NktOR3JINUhwS2x4WGNEOW9zUWxRWDBQZndfNnA4UnJ0T25YQ1N5RVg5Z2hvWDNCcnlyYnNnZkdLTkJGZw?oc=5>

### Novo Nordisk (NVO) Stock May Be Undervalued On Raised 2026 Outlook
- Summary: Guidance raised for 2026, suggesting potential upside.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPUjdvcEhtYlZIR3g0VTVGSlV6ZmpoQjV5cUJ6Q0ZYYTQwdFRaUFQwMk1TMm1rczkwQXRyZzhwSGh5TzY2OU5fT3BqcXpPZWtwSkIwSl9KX21PbUtjYllST1VQQl85SlltQmk0VHNPZnlDYnNaTFpTTG5tUEJsVzRabW52eFZHdkMwQk03alFSaUlSd192bVE?oc=5>

### Novo Nordisk: The Wegovy Pill Opportunity Is Just Beginning (NYSE:NVO)
- Summary: Novo Nordisk highlights expanding Wegovy market potential, signaling growth prospects.
- Date: 2026-11-23 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxNejZkQ0NRNVZJNmdTUjVEZmQtZkxSVlFKM2Z4WUdRaXJaLUY2Q21QN2NBSDc5WllXOTNNaVBTcmhpb1lJbWpUaENCNnY2UWotdHJrb1FFVWpsczE0ejBjd3VocFplRkNJUGlGbVlkemlzcl9rU3ViOHZBc1gtNy00blJ5cmdVX24zcm5PS00wbFF1SURHMjB0VWxab2ZJU3Ez?oc=5>

### Will Novo Nordisk stock hold $35.78 support amid persistent downward momentum?
- Summary: Analysts question NVO's ability to maintain $35.78 support amid declining trend.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNd3ZTQzZNNUFpT0x5cXpTSldFMG1wVnJQejZQcWJQSzFBUkVMTUM2VGFDcHFJT0RLUWp0T3lhTHAxaEVnZWxFNXJFUHZNWjhRQVI1M0hmcTlqRzZzdXNsMmZNVi1vQmRENlZUT1F2MzQ3SW9BaEpBQzhWN0FnbTVBODY5RGUwYlA2SHhVWTJTMG02QQ?oc=5>

### Novo Nordisk: The Worst May Be Behind (NYSE:NVO)
- Summary: Positive outlook suggesting improvement for Novo Nordisk.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigwFBVV95cUxQeng0TGVnR1BPRG5ENFZNNE1OX2JaTmlOMTFKNlBqcVhtaHF3aWRtaGVuQXZWUjItUG43T1RBWEtTaElFbXVuVURaem1tWmlwaWlRTHBlcGJGdmhYU3VzMTdDLU5oakdwUFVsU1EyYjFRMl9zSDh6QmpBdjFDcVUtT1pvZw?oc=5>

### Will Novo Nordisk stock avoid deeper losses amid seller dominance?
- Summary: Question on potential stock decline amid seller dominance.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxNQWV5aHNUNlVtV1ItQkpyRDkyc2dUSTFtSHp1THl3cEZzT0dqaTcxakFIUjZ2eEJ0ZVNSN1lJQzdzLXVVcTJyc2dnNjZlWUNIS0loQzdBXzRfUFBQaW83bTAyVEtYOVhjVVUxZ2FaX0l0djNFN25ZR2RPdnVkdElLcTVMRnZ3WWxUVkhEMw?oc=5>

## RISKS

### NVO slides as weak momentum and sellers dominate intraday trading
- Summary: Intraday slide due to weak momentum and selling pressure.
- Date: 2026-11-20 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxPVU1ITHR6ZTFDWGNqMjhmSjdJampnaUVLc0tLQXBaRmZueldXcFJxUFpHbTl5NDZCa3dMRG9xaDZZdlFvWVdyWE11WkxEekllV2hXUHZrQVNxRzlvUTlwNEJnMHBybXNlYVdxdVBjSS1GY0oxdlVoQWVXNVM1YlBEYTFmMWREU3Jld2doQ1V1ZGw5UQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVO** | **10.18** | **5.43** | **1.46** | **5.60** | **177,615,732,736.00 USD** | **-5.89** |
| LLY | 45.69 | 31.15 | 27.93 | 38.60 | 1,253,803,819,008.00 USD | 32.33 |
| ROG.SW | N/A | N/A | N/A | N/A | N/A unknown currency | N/A |
| SAN.PA | 27.05 | 1.54 | 8.56 | 15.70 | 112,352,739,328.00 EUR | 4.29 |

Peers fetched as_of: 2026-11-24; NVO reuses existing data (market data as_of: 2026-11-24); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-04
- Next expected earnings: 2027-02-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-24

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

- https://news.google.com/rss/articles/CBMijAFBVV95cUxPMk1tMTY4QmtJRGpxWllQZTZRNlpIeDN5enNfdDk3c043TVpTTlRsbEZjU0EwRVJFaktPX0ZkVm1mdjlXZ0FOd2JCbXlXdE5WTDJmWTR5c2tqa1h0cUswTUJZVGJONHBVMHV3LUF2UXJNM3hROWNVN0p4WXVLektDNFRueWxoc1VkQjZsSQ?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxOZDBGdWNCLUg1eGlGWDRnVXdGbzEzUU5hMXRHd2t1endJMlhQby1Jd0lXSFZnNGdLNHVvSHFZdlNETlQzU0U2VmxqczVPUlM1aTFLLWdJMmNNc0ctTmpaNFRrTnVwWlh3RDNuWmZxQnMxcWZoWXBwVXh0dHhQNjVsUTIzUGF0bXJMc1EyWWwwbk9iT0ZvaENtVmNVcWV5a1lJR1RScm5FMVdmOF9BME5UV1JwdElrS0RYOUFJRkVINkZ2YW5UdFc4VDFpSGlSWUhPUFFB?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNYi1OZnF4N2hudHlDM1lRQjVwd2xHOG1UamNXX1pKLVBjMTBaVWVoWTkwdXZQV0YtVy1EYy0xYzJ6Q2Vwc1BqR3FKYnNFZk83TjBXdE1QdDh3a2RZYmNiZ1NZdUd6Q2R3akttNnk3dGhaOXNUeVJJV0hEMGFIc2tQOE4wQVlqa0k0cWNvUWZOZEdmTmpkaDhfRkxsVFJDaEpqRks5Vg?oc=5
- https://news.google.com/rss/articles/CBMi6wFBVV95cUxPUkItU0xjMHAtejlZR1oybGZSOVhMd1VhRHZqS2pPSGx0ZmxzT1hRSHFZQ0tqVFNJeTVDaER1eXgxeTk5Slp5a05oZUhvc0xubm9TZ1Q1U0tTdnBwb1ROeklqQWZOSTIwaGhYckpCSHVSRmRSTXVLNUd3WE1acGJYcnZwMkRleWc2TWk2dEZjUmxScFB5aDlZY0xhTkpjN0tuZXFBazRXRzJjSHdqNjlvYy11Q2NUcnJjZUJ4VUIwbS03aWtrQTZDNTlYTWY5ekdoTm5MN1J6dUNXQ2pUN213Z1NBYWJRZm8wLUZJ?oc=5
- https://news.google.com/rss/articles/CBMi3gFBVV95cUxPcm1NaWN5SEV1VVFwdHhCaXMzNndhcVlnNTltZmx0anN2QURxejJqSnlfczEtNjNSZDhDMjdKaTcweFNaeUp1VDhyckpGX0xmVEp1RGlDSWFHWDlPNFJsM2t5UnNIRGlEaFFHWnVmRC0weTk1bFpMSDdydEEzMVhKNld4anUtdGhUMEw2TE4tR2dvNjBwNWxZaFNxT2tGaVdDRGtsU1hZbkh2cjRDdmRKdTBGSzA0czl1dXJ1bmhLaTJWZmw1VE9zT0hGLXQ4QS0yMlAxeTgteWxJUGl2UFE?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxNVVh1Z1RmUDEwd3JUV3J0V3VqeGVGaks0RGVhMVFjcDFveEVQX0xuQjhrbTNoazVzZVhFNGJUR3FlNTZUUG5xWmduaTVfQWF4akYzbEItc1BRYXlfb1N6TG5xaXZfcmlKUGJJOWJCbE9felhCd3ZRRUNtSGhDU2dpRnl1Q1lGZHBYVlh1RXotNA?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxOcjB1NlROdkt0RnhrUUZpSHBHSUJqX2paVVNHNVlCdTdpS3I3WGlxSUZ2UUc4dVB6ek1LSFNtNEhiMTU3YWFyZ1BRU0g5LVlBY1dkN1ZnNUJsY01zTTRTV0gxSzM1WHcwTlo0TDduM21adGw0OUtpQ3FQeEp0TWhhOEktY1Utc0FWYUFaS09HNHo?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxOTlRFSGxyelpHekxRM0RWaXpjb3lid3RNTXNiZGQyTXFpS0tEZEk2QkRsdEhqa1FuUmNDb1lORDlyWEZ0cl9oUWcxME9SVTRSaEw1X1ZNWVo5SThIeHUybWk1aldRVno2Ujlmb0pPS2pMSzVxNEZFRFZWMjRGZkR2clBzRFU3R2tkTHFhbjVBVmk?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxQY2FUTUpIWjZ3VnpzdWtKTjlxWEViNVpES3R3dFktSVJ0eE5FRTdrOFNvOW9CR2FtUzhJNnRDWTdubzl3NW1iTUg2YmlvemRWYnZCRlNkTlU0ZWFxUVJDdmFfcW5YZEpMOTBBUng5ZW1taXlQSkd6a2I1QWkzVnJaRmFRRllSM0ZMYTg5WG5pTnNyMzMzNlM2T0gyYlR2NktOR3JINUhwS2x4WGNEOW9zUWxRWDBQZndfNnA4UnJ0T25YQ1N5RVg5Z2hvWDNCcnlyYnNnZkdLTkJGZw?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPUjdvcEhtYlZIR3g0VTVGSlV6ZmpoQjV5cUJ6Q0ZYYTQwdFRaUFQwMk1TMm1rczkwQXRyZzhwSGh5TzY2OU5fT3BqcXpPZWtwSkIwSl9KX21PbUtjYllST1VQQl85SlltQmk0VHNPZnlDYnNaTFpTTG5tUEJsVzRabW52eFZHdkMwQk03alFSaUlSd192bVE?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxNejZkQ0NRNVZJNmdTUjVEZmQtZkxSVlFKM2Z4WUdRaXJaLUY2Q21QN2NBSDc5WllXOTNNaVBTcmhpb1lJbWpUaENCNnY2UWotdHJrb1FFVWpsczE0ejBjd3VocFplRkNJUGlGbVlkemlzcl9rU3ViOHZBc1gtNy00blJ5cmdVX24zcm5PS00wbFF1SURHMjB0VWxab2ZJU3Ez?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNd3ZTQzZNNUFpT0x5cXpTSldFMG1wVnJQejZQcWJQSzFBUkVMTUM2VGFDcHFJT0RLUWp0T3lhTHAxaEVnZWxFNXJFUHZNWjhRQVI1M0hmcTlqRzZzdXNsMmZNVi1vQmRENlZUT1F2MzQ3SW9BaEpBQzhWN0FnbTVBODY5RGUwYlA2SHhVWTJTMG02QQ?oc=5
- https://news.google.com/rss/articles/CBMigwFBVV95cUxQeng0TGVnR1BPRG5ENFZNNE1OX2JaTmlOMTFKNlBqcVhtaHF3aWRtaGVuQXZWUjItUG43T1RBWEtTaElFbXVuVURaem1tWmlwaWlRTHBlcGJGdmhYU3VzMTdDLU5oakdwUFVsU1EyYjFRMl9zSDh6QmpBdjFDcVUtT1pvZw?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxNQWV5aHNUNlVtV1ItQkpyRDkyc2dUSTFtSHp1THl3cEZzT0dqaTcxakFIUjZ2eEJ0ZVNSN1lJQzdzLXVVcTJyc2dnNjZlWUNIS0loQzdBXzRfUFBQaW83bTAyVEtYOVhjVVUxZ2FaX0l0djNFN25ZR2RPdnVkdElLcTVMRnZ3WWxUVkhEMw?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxPVU1ITHR6ZTFDWGNqMjhmSjdJampnaUVLc0tLQXBaRmZueldXcFJxUFpHbTl5NDZCa3dMRG9xaDZZdlFvWVdyWE11WkxEekllV2hXUHZrQVNxRzlvUTlwNEJnMHBybXNlYVdxdVBjSS1GY0oxdlVoQWVXNVM1YlBEYTFmMWREU3Jld2doQ1V1ZGw5UQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
