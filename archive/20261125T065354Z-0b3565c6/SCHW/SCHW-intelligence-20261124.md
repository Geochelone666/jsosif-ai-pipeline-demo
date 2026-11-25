# SCHW Intelligence Report

- ticker: **SCHW**
- Report as_of: **2026-11-24**
- Market data as_of: **2026-11-24**
- Quant sources: https://finance.yahoo.com/quote/SCHW/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SCHW/key-statistics/
- AI analysis snapshot as_of: **2026-11-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-25T07:20:52.425214+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 8, 'rule': 1, 'ai': 5, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261124T081701Z-6c335e3d/SCHW** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 8 unique headlines; 5 named publishers; 0 exact duplicates; 8 HTTPS source links; largest publisher share 37.5%; oldest publication 2026-11-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 93.9100 |
| Return 1D (%) | 1.6672 |
| Return 1W (%) | 2.2539 |
| Return 1M (%) | 4.0393 |
| Return YTD (%) | -4.7412 |
| Return 1Y (%) | 5.1403 |
| Annualized volatility (%) | 25.8789 |
| Beta vs SPY | 0.4237 |
| Max drawdown (%) | -22.5253 |
| Sharpe (rf=0) | 0.3247 |
| Downside deviation (rf=0, %) | 19.4308 |
| Sortino (rf=0) | 0.4324 |
| Historical VaR 95% (1D, %) | 2.5277 |
| Historical ES 95% (1D, %) | 3.9438 |
| Correlation vs SPY | 0.2448 |
| Tracking error vs SPY (%) | 26.5301 |
| P/E (trailing) | 15.78 |
| P/B | 3.58 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 16.90 |
| Forward P/E (estimate) | 12.05 |
| Gross margin (%) | 97.51 |
| Operating margin (%) | 51.11 |
| Return on equity (%) | 21.11 |
| Free cash flow yield (%) | N/A |
| MA50 | 94.4080 |
| Close vs MA50 (%) | -0.5275 |
| MA200 | 95.9766 |
| Close vs MA200 (%) | -2.1533 |
| RSI (14, Wilder) | 54.3818 |
| MACD (12,26) | -0.3804 |
| MACD signal (9) | -0.8285 |
| MACD histogram | 0.4481 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SCHW': 289, 'SPY': 289}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 93.9100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.6672 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.2539 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 4.0393 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -4.7412 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 5.1403 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 25.8789 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 19.4308 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4324 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.5277 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.9438 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2448 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.5301 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.4237 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -22.5253 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3247 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 12.0451 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 97.5060 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 51.1070 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 21.1130 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 15.7832 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 54.3818 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.4481 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -0.5275 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -2.1533 -> Slightly below the moving-average trend level.

## TAILWINDS

### Charles Schwab raised to Strong Buy at Raymond James on macro outlook, strong execution
- Summary: Charles Schwab raised to Strong Buy at Raymond James on macro outlook, strong execution
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxQR0puZTV4YXhUZC1qd3JUN193S1BDYXlza09rUXQ0eW5aSFJiTlNFSlQySmdGaDhtVEFPUW9PN1FtTi1TODRweVFDdzlUclRIemlmM1J1bldwc0RxVWNrNjhTMFV2U1FpVzhlZmxna003WUNjbTNOdmt5RDJEQ0IxQlFreDB2Nk9heWxDR1NPSW5Lc0l1YXFsTDhvTHE4RFQ2cG1rNDRIYU1QcGZpZFhydjRzWFZtU1dNSFIxLTY5MzFMdw?oc=5>

### The Charles Schwab Corporation $SCHW Stock: Barrow Hanley Mewhinney & Strauss LLC Increases Position
- Summary: Barrow Hanley Mewhinney & Strauss increases Schwab stake.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7gFBVV95cUxObXkxM0NoWlFJMWRZZzNkblJkT1ZyVGZBZk1zLXVfM09vTUlvNHdxMkNPM0lWSWFTak5VS2lMdE82YUJpTEpfd1F6LTFIYnRkQWxQQXEtYnJkUWNwcHJadmRJYnJVbEhTSlY3UEZNMWhtMTBaSjJSTEctVno1UXQwYWtaaXhWUHdNVzlDRldhM0hHRmIwemNOYnFxNVRYMndfS3poYmNscl8xTTR6OW5WZEtXY3B3YXlPUTBTQnIyOEdfSUtMYmNMMm9meW52N2lDQzgzaVdScDg5ZWFFTXVDTEpXTjBXeWhqaUZDbnhn?oc=5>

## HEADWINDS

### $13 Trillion Asset Manager Charles Schwab Suffering an “Internal Server Error” – Here Is What We Know So Far
- Summary: Schwab’s platform faced a server error, disrupting services and raising concerns about operational reliability.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQWTBEQ0txMTVyT1dlbUVaa0J2RFh2M0w4ZG9zMFR3VF9MaENCZHQ5TXhyU0s1RTYwOGNLcDd5RE10MU5SV3JpbTI1V1RwdTNmbDFhbG92X25Zdi1YNFVRaHRaclhWOEJadXNZcmJvOGhacWVSLUZ1bHI3cnNoNzlVNWZsQmpVUXpETzZMbTlzdUU4amN5OTFQX3NERU5ta2M?oc=5>

## CATALYSTS

### Charles Schwab (SCHW) Stock Could Be 31% Undervalued Today
- Summary: Analysts suggest Schwab may be undervalued, indicating potential upside for investors.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNQ2RBVldIelIyQllkU2JKVG9Hb3U3T01xUlRRM3pUVUtHVHpFV0dNTjhDMkduOENYZElfNjk3TmxoNC1MaENZYW8xME5nVEJ4Z3BQbzEzWVlNY0VyMG5FSkZ4Nm9HVE1QVmR1dWI1VllEM0p3UEYzQ0hUWXJWWmlzcW44aWwxbm9DSXVhc0lyNmRmbzVTQ3FaajUxTHE?oc=5>

### Barclays Sticks to Their Buy Rating for Charles Schwab (SCHW)
- Summary: Barclays maintains a buy rating on Schwab, supporting a positive outlook.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3AFBVV95cUxQb1RBdTBsNFdnNGQtUmRPNzlKbENWOE5Xa2VQTEdjc2Mybll5YXhFb0djS09tem5JMmdBbEhTZVpuSlRhMjVWWmVkYWJjR25pZklPb29oaEhUQmVCZl92VXVJQUdkSVEtSC0ybmRKQ19sQkRyRk1vZ3JkQTZUck5hZTk2dWRyWGVfUzNlZWtlSEYtVDRrbU16QzBuTjdCeXR3dXlDekt6VnJvejVULUFiWkNBSDYxdU93dzZsRGlGSDdFOWlNNEtsVW9uNUZ0U2M4dzFkS282ejBHRnFF?oc=5>

### Charles Schwab (SCHW) Stock May Be 31% Undervalued Despite Its AI Push
- Summary: Despite AI initiatives, Schwab shares could still be 31% undervalued, indicating growth prospects.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3AFBVV95cUxPSHZvbHFlWHlyVmUxeW5GaGFQQ19JVVhMUE1aNEtTbmNaUGMxUXo5TTRpZTJjalFMZFU4Yllxczc3eGpCd2I4YWotaE05c2l4U1Ewd1ZtRzdiZC0yNlN4RjFlV0Nvc1dfTzE4bVJ0RjAzQ1A4T1QzS2Z6cnU3dl9ZVjJpVG1FaDV1T3BfZmNKTkw2dENTdjlEdGpBSVNVUDhVRkxWTENWd2EtX3lBaHZDTjVrRldVMFg1OFJyemlncGxFc2paRE8yeW9xTE9OTjVCSWQ1U0lqS3k4bGE00gHiAUFVX3lxTFBWNkdaTzBjTXdFeFZ0aUZsZllCWEhiOE1HSzJlUG9GS0tXaHNZaFpUVXFQbzFZblQwb0dCQWxfQWdQby0tV0duSTJrbDhTWmkwMGlXVFhwMkNXdmdCck4xRjMtR0FSa3kwQjVsUnl3b1hySEhabXU3M3JVOXEtMlZ3dE5GTHJkYWxMbXRINXZuRHlIYjI2LWp4a2VGM3ZZMVJVbDFxVTEtczVBLWJubnZqQjJqUWRkYUdZZVZqckducmdBbnpJcGNuZEg2aDlJbDNLeGJ3a0g4ek1XbzhCVlV1ZlE?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SCHW** | **15.78** | **3.58** | **N/A** | **16.90** | **162,089,385,984.00 USD** | **5.14** |
| IBKR | 28.52 | 5.45 | N/A | 13.50 | 127,293,972,480.00 USD | 20.18 |
| HOOD | 30.25 | 5.91 | N/A | 11.80 | 59,117,252,608.00 USD | -42.90 |
| LPLA | 15.60 | 3.67 | N/A | 17.80 | 21,200,455,680.00 USD | -21.51 |

Peers fetched as_of: 2026-11-24; SCHW reuses existing data (market data as_of: 2026-11-24); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-21 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-24

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-06
- Revenue (latest available single quarter): 7,171,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 2,906,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/316709/000031670926000038/schw-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiwgFBVV95cUxQR0puZTV4YXhUZC1qd3JUN193S1BDYXlza09rUXQ0eW5aSFJiTlNFSlQySmdGaDhtVEFPUW9PN1FtTi1TODRweVFDdzlUclRIemlmM1J1bldwc0RxVWNrNjhTMFV2U1FpVzhlZmxna003WUNjbTNOdmt5RDJEQ0IxQlFreDB2Nk9heWxDR1NPSW5Lc0l1YXFsTDhvTHE4RFQ2cG1rNDRIYU1QcGZpZFhydjRzWFZtU1dNSFIxLTY5MzFMdw?oc=5
- https://news.google.com/rss/articles/CBMi7gFBVV95cUxObXkxM0NoWlFJMWRZZzNkblJkT1ZyVGZBZk1zLXVfM09vTUlvNHdxMkNPM0lWSWFTak5VS2lMdE82YUJpTEpfd1F6LTFIYnRkQWxQQXEtYnJkUWNwcHJadmRJYnJVbEhTSlY3UEZNMWhtMTBaSjJSTEctVno1UXQwYWtaaXhWUHdNVzlDRldhM0hHRmIwemNOYnFxNVRYMndfS3poYmNscl8xTTR6OW5WZEtXY3B3YXlPUTBTQnIyOEdfSUtMYmNMMm9meW52N2lDQzgzaVdScDg5ZWFFTXVDTEpXTjBXeWhqaUZDbnhn?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQWTBEQ0txMTVyT1dlbUVaa0J2RFh2M0w4ZG9zMFR3VF9MaENCZHQ5TXhyU0s1RTYwOGNLcDd5RE10MU5SV3JpbTI1V1RwdTNmbDFhbG92X25Zdi1YNFVRaHRaclhWOEJadXNZcmJvOGhacWVSLUZ1bHI3cnNoNzlVNWZsQmpVUXpETzZMbTlzdUU4amN5OTFQX3NERU5ta2M?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNQ2RBVldIelIyQllkU2JKVG9Hb3U3T01xUlRRM3pUVUtHVHpFV0dNTjhDMkduOENYZElfNjk3TmxoNC1MaENZYW8xME5nVEJ4Z3BQbzEzWVlNY0VyMG5FSkZ4Nm9HVE1QVmR1dWI1VllEM0p3UEYzQ0hUWXJWWmlzcW44aWwxbm9DSXVhc0lyNmRmbzVTQ3FaajUxTHE?oc=5
- https://news.google.com/rss/articles/CBMi3AFBVV95cUxQb1RBdTBsNFdnNGQtUmRPNzlKbENWOE5Xa2VQTEdjc2Mybll5YXhFb0djS09tem5JMmdBbEhTZVpuSlRhMjVWWmVkYWJjR25pZklPb29oaEhUQmVCZl92VXVJQUdkSVEtSC0ybmRKQ19sQkRyRk1vZ3JkQTZUck5hZTk2dWRyWGVfUzNlZWtlSEYtVDRrbU16QzBuTjdCeXR3dXlDekt6VnJvejVULUFiWkNBSDYxdU93dzZsRGlGSDdFOWlNNEtsVW9uNUZ0U2M4dzFkS282ejBHRnFF?oc=5
- https://news.google.com/rss/articles/CBMi3AFBVV95cUxPSHZvbHFlWHlyVmUxeW5GaGFQQ19JVVhMUE1aNEtTbmNaUGMxUXo5TTRpZTJjalFMZFU4Yllxczc3eGpCd2I4YWotaE05c2l4U1Ewd1ZtRzdiZC0yNlN4RjFlV0Nvc1dfTzE4bVJ0RjAzQ1A4T1QzS2Z6cnU3dl9ZVjJpVG1FaDV1T3BfZmNKTkw2dENTdjlEdGpBSVNVUDhVRkxWTENWd2EtX3lBaHZDTjVrRldVMFg1OFJyemlncGxFc2paRE8yeW9xTE9OTjVCSWQ1U0lqS3k4bGE00gHiAUFVX3lxTFBWNkdaTzBjTXdFeFZ0aUZsZllCWEhiOE1HSzJlUG9GS0tXaHNZaFpUVXFQbzFZblQwb0dCQWxfQWdQby0tV0duSTJrbDhTWmkwMGlXVFhwMkNXdmdCck4xRjMtR0FSa3kwQjVsUnl3b1hySEhabXU3M3JVOXEtMlZ3dE5GTHJkYWxMbXRINXZuRHlIYjI2LWp4a2VGM3ZZMVJVbDFxVTEtczVBLWJubnZqQjJqUWRkYUdZZVZqckducmdBbnpJcGNuZEg2aDlJbDNLeGJ3a0g4ek1XbzhCVlV1ZlE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
