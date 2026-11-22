# NVO Intelligence Report

- ticker: **NVO**
- Report as_of: **2026-11-21**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/NVO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVO/key-statistics/
- AI analysis snapshot as_of: **2026-11-21**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-22T05:14:55.203401+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 17, 'rule': 3, 'ai': 10, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **11** exact headline/source/date matches; prior report **20261121T053104Z-422ce34b/NVO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 17 unique headlines; 8 named publishers; 1 exact duplicates; 17 HTTPS source links; largest publisher share 35.29%; oldest publication 2026-11-16

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 37.8200 |
| Return 1D (%) | -2.7013 |
| Return 1W (%) | -9.1521 |
| Return 1M (%) | -3.8882 |
| Return YTD (%) | -21.9575 |
| Return 1Y (%) | -16.5797 |
| Annualized volatility (%) | 45.3653 |
| Beta vs SPY | 0.9074 |
| Max drawdown (%) | -43.6699 |
| Sharpe (rf=0) | -0.1697 |
| Downside deviation (rf=0, %) | 34.0631 |
| Sortino (rf=0) | -0.2260 |
| Historical VaR 95% (1D, %) | 3.1211 |
| Historical ES 95% (1D, %) | 7.1674 |
| Correlation vs SPY | 0.2859 |
| Tracking error vs SPY (%) | 43.4916 |
| P/E (trailing) | 9.55 |
| P/B | 5.09 |
| EV/EBITDA | 1.40 |
| Revenue growth (%) | 5.60 |
| Forward P/E (estimate) | 10.77 |
| Gross margin (%) | 83.33 |
| Operating margin (%) | 50.78 |
| Return on equity (%) | 58.38 |
| Free cash flow yield (%) | N/A |
| MA50 | 39.5872 |
| Close vs MA50 (%) | -4.4641 |
| MA200 | 42.2674 |
| Close vs MA200 (%) | -10.5220 |
| RSI (14, Wilder) | 38.0236 |
| MACD (12,26) | -0.0922 |
| MACD signal (9) | 0.1618 |
| MACD histogram | -0.2541 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVO': 287, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 37.8200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.7013 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -9.1521 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -3.8882 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -21.9575 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -16.5797 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 45.3653 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 34.0631 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.2260 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.1211 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 7.1674 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2859 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 43.4916 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.9074 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -43.6699 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.1697 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 10.7674 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 83.3330 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 50.7790 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 58.3840 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 9.5505 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 38.0236 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.2541 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -4.4641 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -10.5220 -> Clearly below the moving-average trend level.

## TAILWINDS

### Novo Nordisk Stock Rises on Obesity Drug Breakthrough
- Summary: Novo Nordisk Stock Rises on Obesity Drug Breakthrough
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxNZGxiUVdwbzlQREQxVHRjYTUzNFFTZ1FWd3FlTE1ma0tkVUJRb0dyVENkMWcwNHVDMXc1eWV3QUk5bGtKZktHQXhRbTBXbVJJcHFQZWxzRnBkZ1Q2a294ZHVITE90M0VZbGs4V3JHMEVEUE5sSTRIc0JfWUg4bEoxVGNoVTk3M3VNWWljQXZCUzZvRzB3Z213TXYxV19xUnQyZGZ6bTFiT0hwcjd4Q2ZYX0pUaw?oc=5>

### Novo Nordisk: A Return To Growth May Be Just Around The Corner (NYSE:NVO)
- Summary: Anticipated return to growth signals favorable outlook for the company.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNYi1OZnF4N2hudHlDM1lRQjVwd2xHOG1UamNXX1pKLVBjMTBaVWVoWTkwdXZQV0YtVy1EYy0xYzJ6Q2Vwc1BqR3FKYnNFZk83TjBXdE1QdDh3a2RZYmNiZ1NZdUd6Q2R3akttNnk3dGhaOXNUeVJJV0hEMGFIc2tQOE4wQVlqa0k0cWNvUWZOZEdmTmpkaDhfRkxsVFJDaEpqRks5Vg?oc=5>

## HEADWINDS

### Novo Nordisk stock falls as sellers keep control and support remains in focus
- Summary: Novo Nordisk stock falls as sellers keep control and support remains in focus
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxNNmM1ZzlMd1F4THI0VHI3LVA0c0hUU2xEX3A1dUxSMzFyeFcwUzNmNVhIRWhpbGl1SXN3N184NDhoR0hNRzNLWWNmM3hSeGVUMXhwRndCeXVlVnE5bDVxcGFYV0pjS0M0a1dDdTRHeFQyNDZSVllXVWpTUUdEUzJLZHQzU2tuc2gwaVd5UWx3?oc=5>

### What's behind Novo Nordisk's latest 2.8% stock pullback?
- Summary: Recent 2.8% stock pullback indicates short‑term market pressure.
- Date: 2026-11-18 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxORTZKTGNsM29zVEpQbW4ySjVRZ0pGN0VOVG9aNjdqaWpPUDJpaEQ0MHVqVENLdV9hU1ZLaXFDcFVsNk9CSE50M2hzY1Q1V0xHRDR0dTNEd2JqdXBVOUhodlI5Sl91TndCbnh3aVAzZk0xLUdLZmRtU3NwcGl2cFF6cmVMdVQ0MDlWNlQ0UXN0a3A?oc=5>

### Novo Nordisk (NVO) Could Be 47% Below Fair Value Following Its AI Push
- Summary: AI push may have led to undervaluation, suggesting a short‑term headwind.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxNVVh1Z1RmUDEwd3JUV3J0V3VqeGVGaks0RGVhMVFjcDFveEVQX0xuQjhrbTNoazVzZVhFNGJUR3FlNTZUUG5xWmduaTVfQWF4akYzbEItc1BRYXlfb1N6TG5xaXZfcmlKUGJJOWJCbE9felhCd3ZRRUNtSGhDU2dpRnl1Q1lGZHBYVlh1RXotNA?oc=5>

## CATALYSTS

### Novo Nordisk Details Share Repurchases Through November 13
- Summary: Novo Nordisk Details Share Repurchases Through November 13
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxQY2FUTUpIWjZ3VnpzdWtKTjlxWEViNVpES3R3dFktSVJ0eE5FRTdrOFNvOW9CR2FtUzhJNnRDWTdubzl3NW1iTUg2YmlvemRWYnZCRlNkTlU0ZWFxUVJDdmFfcW5YZEpMOTBBUng5ZW1taXlQSkd6a2I1QWkzVnJaRmFRRllSM0ZMYTg5WG5pTnNyMzMzNlM2T0gyYlR2NktOR3JINUhwS2x4WGNEOW9zUWxRWDBQZndfNnA4UnJ0T25YQ1N5RVg5Z2hvWDNCcnlyYnNnZkdLTkJGZw?oc=5>

### Novo Nordisk (NVO) Stock May Be Undervalued On Raised 2026 Outlook
- Summary: Guidance raised for 2026, suggesting potential upside.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPUjdvcEhtYlZIR3g0VTVGSlV6ZmpoQjV5cUJ6Q0ZYYTQwdFRaUFQwMk1TMm1rczkwQXRyZzhwSGh5TzY2OU5fT3BqcXpPZWtwSkIwSl9KX21PbUtjYllST1VQQl85SlltQmk0VHNPZnlDYnNaTFpTTG5tUEJsVzRabW52eFZHdkMwQk03alFSaUlSd192bVE?oc=5>

### Novo Nordisk: The Worst May Be Behind (NYSE:NVO)
- Summary: Positive outlook suggesting improvement for Novo Nordisk.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigwFBVV95cUxQeng0TGVnR1BPRG5ENFZNNE1OX2JaTmlOMTFKNlBqcVhtaHF3aWRtaGVuQXZWUjItUG43T1RBWEtTaElFbXVuVURaem1tWmlwaWlRTHBlcGJGdmhYU3VzMTdDLU5oakdwUFVsU1EyYjFRMl9zSDh6QmpBdjFDcVUtT1pvZw?oc=5>

### Will Novo Nordisk stock avoid deeper losses amid seller dominance?
- Summary: Question on potential stock decline amid seller dominance.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxNQWV5aHNUNlVtV1ItQkpyRDkyc2dUSTFtSHp1THl3cEZzT0dqaTcxakFIUjZ2eEJ0ZVNSN1lJQzdzLXVVcTJyc2dnNjZlWUNIS0loQzdBXzRfUFBQaW83bTAyVEtYOVhjVVUxZ2FaX0l0djNFN25ZR2RPdnVkdElLcTVMRnZ3WWxUVkhEMw?oc=5>

### Novo Nordisk A/S Stock (NVO) Moved Down by 3.12% on Nov 18: What Investors Need To Know
- Summary: Stock fell 3.12% on Nov 18, investors advised.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxONGNNMV9xVGhZcUlCa0VIWEI1S1ZPZFY4R05nbGNURHNOb294YldzYVRGUEVYMXpRd19STWsxWGNfQ0xNZ2p6clZ1Q1dpYmVna0NJOG0tVU00NVVQRDc3dlFISS1VSGlnQWhWS2NZanRLV3o0Z2hERGZ2TVl1X2plbjQwYk1oU0dUcnc?oc=5>

### Novo Nordisk's Wegovy Pill Is Capturing 80% of New Oral Obesity Prescriptions. Is NVO Stock a Buy?
- Summary: Novo Nordisk’s Wegovy pill dominates new oral obesity prescriptions, indicating strong market uptake and potential revenue growth.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQS1VMdlhIZGFnWEIwMk5yci0ySGpKTjlmeXJRUVF4S1RJa3Bkdy1keS1MNVV1OEVIMGh3V1hyYTVPU2owZmptbkk5Yjc4Vi12UjQ0ZjZQS1kycE9xeWt3RjRHTF9Ma25hcUdHVlI2V3cxWVJacTFKQUQzQXNXdXJRSEtIb0h3S2RVS0xOOEEzSmVkbnVHdVg4b3ZwY0o?oc=5>

### Forget the Headlines: Novo Nordisk's (NVO) 4.6% Dividend Yield Is the Real Story for Patient Investors
- Summary: Novo Nordisk announces a 4.6% dividend yield, highlighting shareholder value and stable returns.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNek1PY1YtNFZIWnlLTmNXWHdKbWJENkN5UWE0MmhYRWpINzUwY2tralIyOWQxX2pLRU44LUdxUF92aHNFLVFKdzl0ckk0dTVhdWZtaFdmYy03bll3SW41TWlMSHR1Z2xydHU1dWwwN0QtYzRJN3ZnUGRyeGl2Ty1VcC1mQkJScGo0eDFNUE9wcW5qbE0tQTNrSg?oc=5>

## RISKS

### NVO slides as weak momentum and sellers dominate intraday trading
- Summary: Intraday slide due to weak momentum and selling pressure.
- Date: 2026-11-20 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxPVU1ITHR6ZTFDWGNqMjhmSjdJampnaUVLc0tLQXBaRmZueldXcFJxUFpHbTl5NDZCa3dMRG9xaDZZdlFvWVdyWE11WkxEekllV2hXUHZrQVNxRzlvUTlwNEJnMHBybXNlYVdxdVBjSS1GY0oxdlVoQWVXNVM1YlBEYTFmMWREU3Jld2doQ1V1ZGw5UQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVO** | **9.55** | **5.09** | **1.40** | **5.60** | **166,686,162,944.00 USD** | **-16.58** |
| LLY | 43.72 | 29.81 | 26.77 | 38.60 | 1,199,931,523,072.00 USD | 29.90 |
| ROG.SW | N/A | N/A | N/A | N/A | N/A unknown currency | N/A |
| SAN.PA | 24.54 | 1.40 | 7.86 | 15.70 | 101,955,485,696.00 EUR | 5.10 |

Peers fetched as_of: 2026-11-21; NVO reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-04
- Next expected earnings: 2027-02-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-21

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

- https://news.google.com/rss/articles/CBMiswFBVV95cUxNZGxiUVdwbzlQREQxVHRjYTUzNFFTZ1FWd3FlTE1ma0tkVUJRb0dyVENkMWcwNHVDMXc1eWV3QUk5bGtKZktHQXhRbTBXbVJJcHFQZWxzRnBkZ1Q2a294ZHVITE90M0VZbGs4V3JHMEVEUE5sSTRIc0JfWUg4bEoxVGNoVTk3M3VNWWljQXZCUzZvRzB3Z213TXYxV19xUnQyZGZ6bTFiT0hwcjd4Q2ZYX0pUaw?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNYi1OZnF4N2hudHlDM1lRQjVwd2xHOG1UamNXX1pKLVBjMTBaVWVoWTkwdXZQV0YtVy1EYy0xYzJ6Q2Vwc1BqR3FKYnNFZk83TjBXdE1QdDh3a2RZYmNiZ1NZdUd6Q2R3akttNnk3dGhaOXNUeVJJV0hEMGFIc2tQOE4wQVlqa0k0cWNvUWZOZEdmTmpkaDhfRkxsVFJDaEpqRks5Vg?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxNNmM1ZzlMd1F4THI0VHI3LVA0c0hUU2xEX3A1dUxSMzFyeFcwUzNmNVhIRWhpbGl1SXN3N184NDhoR0hNRzNLWWNmM3hSeGVUMXhwRndCeXVlVnE5bDVxcGFYV0pjS0M0a1dDdTRHeFQyNDZSVllXVWpTUUdEUzJLZHQzU2tuc2gwaVd5UWx3?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxORTZKTGNsM29zVEpQbW4ySjVRZ0pGN0VOVG9aNjdqaWpPUDJpaEQ0MHVqVENLdV9hU1ZLaXFDcFVsNk9CSE50M2hzY1Q1V0xHRDR0dTNEd2JqdXBVOUhodlI5Sl91TndCbnh3aVAzZk0xLUdLZmRtU3NwcGl2cFF6cmVMdVQ0MDlWNlQ0UXN0a3A?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxNVVh1Z1RmUDEwd3JUV3J0V3VqeGVGaks0RGVhMVFjcDFveEVQX0xuQjhrbTNoazVzZVhFNGJUR3FlNTZUUG5xWmduaTVfQWF4akYzbEItc1BRYXlfb1N6TG5xaXZfcmlKUGJJOWJCbE9felhCd3ZRRUNtSGhDU2dpRnl1Q1lGZHBYVlh1RXotNA?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxQY2FUTUpIWjZ3VnpzdWtKTjlxWEViNVpES3R3dFktSVJ0eE5FRTdrOFNvOW9CR2FtUzhJNnRDWTdubzl3NW1iTUg2YmlvemRWYnZCRlNkTlU0ZWFxUVJDdmFfcW5YZEpMOTBBUng5ZW1taXlQSkd6a2I1QWkzVnJaRmFRRllSM0ZMYTg5WG5pTnNyMzMzNlM2T0gyYlR2NktOR3JINUhwS2x4WGNEOW9zUWxRWDBQZndfNnA4UnJ0T25YQ1N5RVg5Z2hvWDNCcnlyYnNnZkdLTkJGZw?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPUjdvcEhtYlZIR3g0VTVGSlV6ZmpoQjV5cUJ6Q0ZYYTQwdFRaUFQwMk1TMm1rczkwQXRyZzhwSGh5TzY2OU5fT3BqcXpPZWtwSkIwSl9KX21PbUtjYllST1VQQl85SlltQmk0VHNPZnlDYnNaTFpTTG5tUEJsVzRabW52eFZHdkMwQk03alFSaUlSd192bVE?oc=5
- https://news.google.com/rss/articles/CBMigwFBVV95cUxQeng0TGVnR1BPRG5ENFZNNE1OX2JaTmlOMTFKNlBqcVhtaHF3aWRtaGVuQXZWUjItUG43T1RBWEtTaElFbXVuVURaem1tWmlwaWlRTHBlcGJGdmhYU3VzMTdDLU5oakdwUFVsU1EyYjFRMl9zSDh6QmpBdjFDcVUtT1pvZw?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxNQWV5aHNUNlVtV1ItQkpyRDkyc2dUSTFtSHp1THl3cEZzT0dqaTcxakFIUjZ2eEJ0ZVNSN1lJQzdzLXVVcTJyc2dnNjZlWUNIS0loQzdBXzRfUFBQaW83bTAyVEtYOVhjVVUxZ2FaX0l0djNFN25ZR2RPdnVkdElLcTVMRnZ3WWxUVkhEMw?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxONGNNMV9xVGhZcUlCa0VIWEI1S1ZPZFY4R05nbGNURHNOb294YldzYVRGUEVYMXpRd19STWsxWGNfQ0xNZ2p6clZ1Q1dpYmVna0NJOG0tVU00NVVQRDc3dlFISS1VSGlnQWhWS2NZanRLV3o0Z2hERGZ2TVl1X2plbjQwYk1oU0dUcnc?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQS1VMdlhIZGFnWEIwMk5yci0ySGpKTjlmeXJRUVF4S1RJa3Bkdy1keS1MNVV1OEVIMGh3V1hyYTVPU2owZmptbkk5Yjc4Vi12UjQ0ZjZQS1kycE9xeWt3RjRHTF9Ma25hcUdHVlI2V3cxWVJacTFKQUQzQXNXdXJRSEtIb0h3S2RVS0xOOEEzSmVkbnVHdVg4b3ZwY0o?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNek1PY1YtNFZIWnlLTmNXWHdKbWJENkN5UWE0MmhYRWpINzUwY2tralIyOWQxX2pLRU44LUdxUF92aHNFLVFKdzl0ckk0dTVhdWZtaFdmYy03bll3SW41TWlMSHR1Z2xydHU1dWwwN0QtYzRJN3ZnUGRyeGl2Ty1VcC1mQkJScGo0eDFNUE9wcW5qbE0tQTNrSg?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPQU0zVGJtSm1jLWFQZlY4M1E4ZFJzODcxdG9xU2UzUFZOVXpaQzdLYlRjdGdtTjdxc2pETlJrbzJHZk0ydnFMSEdERk9HQl92ZzdZZVczSnhLaTZhY2laRW41NG8wdmNvcWNyTS1JNXBvQi1QTWE0LVdCbEpXUUNaS2VXNnB5YzN5OTVwSHYzRWxJNHFaTUFqcDJwcw?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxPVU1ITHR6ZTFDWGNqMjhmSjdJampnaUVLc0tLQXBaRmZueldXcFJxUFpHbTl5NDZCa3dMRG9xaDZZdlFvWVdyWE11WkxEekllV2hXUHZrQVNxRzlvUTlwNEJnMHBybXNlYVdxdVBjSS1GY0oxdlVoQWVXNVM1YlBEYTFmMWREU3Jld2doQ1V1ZGw5UQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
