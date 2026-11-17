# ASML Intelligence Report

- ticker: **ASML**
- Report as_of: **2026-11-16**
- Market data as_of: **2026-11-16**
- Quant sources: https://finance.yahoo.com/quote/ASML/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ASML/key-statistics/
- AI analysis snapshot as_of: **2026-11-16**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-17T06:48:49.915984+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 18, 'rule': 6, 'ai': 5, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 18 unique headlines; 13 named publishers; 0 exact duplicates; 18 HTTPS source links; largest publisher share 16.67%; oldest publication 2026-11-13

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 1406.7900 |
| Return 1D (%) | -5.9104 |
| Return 1W (%) | -7.0352 |
| Return 1M (%) | -14.1865 |
| Return YTD (%) | 32.2989 |
| Return 1Y (%) | 40.5602 |
| Annualized volatility (%) | 49.1253 |
| Beta vs SPY | 2.3077 |
| Max drawdown (%) | -31.6292 |
| Sharpe (rf=0) | 0.9174 |
| Downside deviation (rf=0, %) | 33.4363 |
| Sortino (rf=0) | 1.3479 |
| Historical VaR 95% (1D, %) | 5.0250 |
| Historical ES 95% (1D, %) | 6.5779 |
| Correlation vs SPY | 0.6467 |
| Tracking error vs SPY (%) | 41.5700 |
| P/E (trailing) | 34.62 |
| P/B | 1207.94 |
| EV/EBITDA | 1849.72 |
| Revenue growth (%) | 55.20 |
| Forward P/E (estimate) | 22.19 |
| Gross margin (%) | 54.34 |
| Operating margin (%) | 38.55 |
| Return on equity (%) | 65.64 |
| Free cash flow yield (%) | N/A |
| MA50 | 1652.7539 |
| Close vs MA50 (%) | -14.8821 |
| MA200 | 1598.0219 |
| Close vs MA200 (%) | -11.9668 |
| RSI (14, Wilder) | 36.3067 |
| MACD (12,26) | -59.9195 |
| MACD signal (9) | -56.0496 |
| MACD histogram | -3.8699 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ASML': 283, 'SPY': 283}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 1406.7900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -5.9104 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -7.0352 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -14.1865 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 32.2989 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 40.5602 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 49.1253 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 33.4363 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.3479 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 5.0250 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.5779 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6467 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 41.5700 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.3077 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -31.6292 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9174 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 22.1894 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.3370 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 38.5520 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 65.6360 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 34.6159 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 36.3067 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.8699 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -14.8821 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -11.9668 -> Clearly below the moving-average trend level.

## TAILWINDS

### ASML Soars 10% in a Week as Chip Stocks Bounce and Musk’s Terafab Eyes a Million Wafers
- Summary: ASML shares jumped 10% amid positive market sentiment and optimism about chip demand.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxPaFhnU3VhU3lYbkxKUHRsQUZZN004VXEtbXFmOXpLa0sybHBaLVZPQTQzSVR6cUVCcXJpVUxCckFjVUt4a2FUMlhWQkFpZ2xHLVhyREg4MHAyX1FIX1g3VFo1V3FxcTctZTAyYzVjbGJHSExuZ0V0Ull1NTFKY004eWFKRDlXVFkwT3ZVQ19RUmMtTkZpUl92dVlhX2pYUEVxRmRnblpPbFJ5bmhib0l5Tg?oc=5>

## HEADWINDS

### ASML Holding falls 2.41% in Monday's session
- Summary: ASML Holding falls 2.41% in Monday's session
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxPaEktdGVqODJOdjQxa0x5T3ItTGRwUlFud2xhMWcxblRYVWV6RUpoOFdSbUtoR09VSDJqZVQtWS1XdElya2dydjR6TkU1MlhSdlo2eFNRODFtQUk4ek40QXkxVTZ2czRaeC1kV1NqT2lSQ09YVWRaakE3bGg4SXRyalFjT0E?oc=5>

### ASML slides as broader chip selloff appears to pressure shares
- Summary: ASML slides as broader chip selloff appears to pressure shares
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxON3V1T0l4QmtndUVSMHM1RzJWalliN3BIaDlFTExiQnpELUI4Y2Yyc2UzVk9XbnczcGx3RzFjN3BPN3dhTWotOG42MWQybE5iQW5NTEE3Y19ZTzFBbV9weW9tcnRocmdEdWlfY0RlT0M5Q1R3SlRwbmRxWWhFZUZQcmVLS1VUbFNnUVpaV0EzamJUZjhPU3pvd0o3WQ?oc=5>

### ASML Holding NV (ASML) Shares Fall 5.9% -- What GF Score of 97 T
- Summary: ASML Holding NV (ASML) Shares Fall 5.9% -- What GF Score of 97 T
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxNS1JVYW1TU2RuaUI5S1Z6YmE0WktQa3NKWTJtc0cycVBuMnNhTi0ydTNLeEc1eEhzUENMa3U0TG9tUmMwZW9QM3M0Q2tlRG1PSmRGZTd0UU15SjZhUlhSVEh6blJCeGpaU01PRnVBOXRNbkZaMldTQU02azBwb016RHd1RXFybk54QW94MnFCQkREZUJlUFlfOXRKLUZLc19GQkxxbF9hbzFZMTRPMW9v?oc=5>

### ASML Plunged 17% Lower Over 3 Months: This Wall Street Desk Expects 88% Gains Over the Next 12
- Summary: ASML shares fell 17% over three months, reflecting short‑term negative market pressure.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxNUmtfcVVoWkt3b3VrbzdVM1g2STlWM2lpeXp0Vm5BY2ZsOG51S3dXbVVYZ242S2lnS0ludXFjQzduenc2OHM0alFmY1Rxb3EzRDh5UHpHbU1Ea1oyc0JNVTRreTl2MWxjWDlVamdzRk9mZnZCZ1BNNnl6WTJUTUdLR3lPUGpFLU5NWEtQcFI0bmxLOWliWGd1bF9fWEZ6QWVwdHV3V29TbndCSWpqeTJCVG5qaU95QUI1R0JlM0JmaTVqVXQxZ3FhLUlBLVlxWG95?oc=5>

### ASML Holding NV Stock (ASML) Opened Down by 3.69% on Nov 16: Key Drivers Unveiled
- Summary: ASML stock opened 3.69% lower on Nov 16, indicating short‑term negative market reaction.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxQR2xLMTJ3cHZWbUtmUWdBdEplc3ZqeEJzR0h1TWhLRTZEUzVSQ0ZzN0hObmRtX0ZJdUgzTFJIUHJZLVJ6VFU2U2k5VkhWZllCNXN2Mm1TOXFaam1Yb3BVSHh4NUNQcmo1QUxDcW1wcnJaUHdJVmlIMWVVWHd6b3VuVm0wUENSMnoxTWZj?oc=5>

## CATALYSTS

### ASML reports transactions under its current share buyback program
- Summary: ASML reports transactions under its current share buyback program
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxNYlFVSlRnVHh5eFFNUllxdmVOUWQ4T0NaTFZUYnMzQjRiWmFWdi04N0JDSFNXOGJRaGhhd0JvT2UwblZGcndaS04xY3BqNFBWc2twZnNKQlVKMnJLSjNNbEF6MGFsQWhmcDAzcEF3RTNLbGNoRU5XRkdRc215Zm9xVzJsMTBlOXRDY2tXeUJhbGw5ck4weXludWo5NWE1bFZiMENFbmdVUQ?oc=5>

### ASML's Berkshire Buzz Meets Nvidia's Earnings Test: What Actually Matters for the Stock
- Summary: ASML's Berkshire Buzz Meets Nvidia's Earnings Test: What Actually Matters for the Stock
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7wFBVV95cUxOa2FtdUtaMzNUOXJ1MkZMVlFaSk82RURBRjc0WDZ4Z1pkWmp1MTF4VnFJRHFSVkdxZ1FLNWZDcWhZbmZtNEcyQmc0UUpQODFPdURYdjFkN0xYZnpEa0RNSnVWS2c2cTg2MnkwMjE3Y3U2c3Y1MEZYbU9yRmc3YkI5bXloY3dsd1JIMjFrMnNZRVBka3otcmtsaHhlbFgxdGxUbUpkUTNQUENYLWotN1JwU2FCV2Y2UXRqMTBCTjFiZ0pLWEFweWpQV09WUXg4dkhTT0dKMFVCbkxfU3hSQkpUNmlEaUFicDhBb0tvOERrTQ?oc=5>

### ASML's €563 Million Buyback Runs Alongside a Dutch Labour Rift Investors Can't Ignore
- Summary: ASML's €563 Million Buyback Runs Alongside a Dutch Labour Rift Investors Can't Ignore
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxOaWZZTXc5WW9OS0VjbmV1NEs3V1l4cGhINkFNZUhHMS03dVZCUnZXdG51dWtDN0sxRWJLVE9vOEt1UTlBWC1jd0tSTmRLaXR6WlNiajJRWDN4ak1tLWtoM3d0N3ZIYmtpbS04WTR3ckR1TFg3R0h6TzdiMFVpUVc5UlUzbGw3WXNnejBSaC1vTkRBSDdtLTQ0amVaUENoYTZFWGR1d3J3eDVPdnhGcTlqdVgxdWRrWlBhYU9LdnRRUHNZYVpVbTEwejR2WV9hR1VFQTZlVDVHUzRSOUVQVXNweEVwN2JPbENPTWlyNg?oc=5>

### ASML Stock Price Prediction: AI demand lifts guidance, but price action is still repairing damage
- Summary: AI demand boosts guidance, yet price action remains in recovery phase.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxNNE16OG80X3h6Um83WXp0LWpBVFllcXE0RmlmNjFnNHU2NVVSbV95WmlleXE1bGNuRE1hUVl3T196MDNGZDF6al9NeVlSYnRyUzBFXzdpQWVjaUlLTERteE1aQ0IwSnhtcVpxRlBZdnZiZWgwdXhmYWtCTlp3UHE5ZEdoR3p1c3RUT0JwWHdPdEZ2d3RCZWl5VVc4aVhSYU13VlRF?oc=5>

## RISKS

### A Look at ASML Holding NV (ASML) After 0.1% Decline -- GF Value $1414.08 vs Price $1495.16
- Summary: Minor 0.1% decline in ASML shares, GF value lower than price.
- Date: 2026-11-14 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxPUFN1eXk5V0UzOFNwTEFBMU1DeWFGdXdKc01BaHhjb0NYM18tV3haRThvd0tzUkdQQWc3Q1M2SEF2RzZmRGRCZnFjVGZESUcyU09CWnY3aWt2LVFZMW1wdnQyV3dnOWhGNHg4UF84Y01rYXpvNDktU2lTVUpVTl9iVGNWb1R2d2RENS1rVmgwZFlRUTlCSzBJVTZuYkx5UVRrLU1tcjYyVkE3RWtJbXdSdGxsYThTLU1nSHc?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ASML** | **34.62** | **1,207.94** | **1,849.72** | **55.20** | **542,201,806,848.00 USD** | **40.56** |
| AMAT | 27.75 | 10.64 | 23.07 | 53.10 | 277,957,509,120.00 USD | 55.83 |
| LRCX | 31.42 | 18.94 | 25.67 | 54.40 | 263,362,707,456.00 USD | 42.86 |
| KLAC | 36.08 | 28.76 | 28.70 | 28.90 | 187,574,484,992.00 USD | 27.79 |

Peers fetched as_of: 2026-11-16; ASML reuses existing data (market data as_of: 2026-11-16); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-14
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-16

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

- https://news.google.com/rss/articles/CBMisAFBVV95cUxPaFhnU3VhU3lYbkxKUHRsQUZZN004VXEtbXFmOXpLa0sybHBaLVZPQTQzSVR6cUVCcXJpVUxCckFjVUt4a2FUMlhWQkFpZ2xHLVhyREg4MHAyX1FIX1g3VFo1V3FxcTctZTAyYzVjbGJHSExuZ0V0Ull1NTFKY004eWFKRDlXVFkwT3ZVQ19RUmMtTkZpUl92dVlhX2pYUEVxRmRnblpPbFJ5bmhib0l5Tg?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxPaEktdGVqODJOdjQxa0x5T3ItTGRwUlFud2xhMWcxblRYVWV6RUpoOFdSbUtoR09VSDJqZVQtWS1XdElya2dydjR6TkU1MlhSdlo2eFNRODFtQUk4ek40QXkxVTZ2czRaeC1kV1NqT2lSQ09YVWRaakE3bGg4SXRyalFjT0E?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxON3V1T0l4QmtndUVSMHM1RzJWalliN3BIaDlFTExiQnpELUI4Y2Yyc2UzVk9XbnczcGx3RzFjN3BPN3dhTWotOG42MWQybE5iQW5NTEE3Y19ZTzFBbV9weW9tcnRocmdEdWlfY0RlT0M5Q1R3SlRwbmRxWWhFZUZQcmVLS1VUbFNnUVpaV0EzamJUZjhPU3pvd0o3WQ?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxNS1JVYW1TU2RuaUI5S1Z6YmE0WktQa3NKWTJtc0cycVBuMnNhTi0ydTNLeEc1eEhzUENMa3U0TG9tUmMwZW9QM3M0Q2tlRG1PSmRGZTd0UU15SjZhUlhSVEh6blJCeGpaU01PRnVBOXRNbkZaMldTQU02azBwb016RHd1RXFybk54QW94MnFCQkREZUJlUFlfOXRKLUZLc19GQkxxbF9hbzFZMTRPMW9v?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxNUmtfcVVoWkt3b3VrbzdVM1g2STlWM2lpeXp0Vm5BY2ZsOG51S3dXbVVYZ242S2lnS0ludXFjQzduenc2OHM0alFmY1Rxb3EzRDh5UHpHbU1Ea1oyc0JNVTRreTl2MWxjWDlVamdzRk9mZnZCZ1BNNnl6WTJUTUdLR3lPUGpFLU5NWEtQcFI0bmxLOWliWGd1bF9fWEZ6QWVwdHV3V29TbndCSWpqeTJCVG5qaU95QUI1R0JlM0JmaTVqVXQxZ3FhLUlBLVlxWG95?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxQR2xLMTJ3cHZWbUtmUWdBdEplc3ZqeEJzR0h1TWhLRTZEUzVSQ0ZzN0hObmRtX0ZJdUgzTFJIUHJZLVJ6VFU2U2k5VkhWZllCNXN2Mm1TOXFaam1Yb3BVSHh4NUNQcmo1QUxDcW1wcnJaUHdJVmlIMWVVWHd6b3VuVm0wUENSMnoxTWZj?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxNYlFVSlRnVHh5eFFNUllxdmVOUWQ4T0NaTFZUYnMzQjRiWmFWdi04N0JDSFNXOGJRaGhhd0JvT2UwblZGcndaS04xY3BqNFBWc2twZnNKQlVKMnJLSjNNbEF6MGFsQWhmcDAzcEF3RTNLbGNoRU5XRkdRc215Zm9xVzJsMTBlOXRDY2tXeUJhbGw5ck4weXludWo5NWE1bFZiMENFbmdVUQ?oc=5
- https://news.google.com/rss/articles/CBMi7wFBVV95cUxOa2FtdUtaMzNUOXJ1MkZMVlFaSk82RURBRjc0WDZ4Z1pkWmp1MTF4VnFJRHFSVkdxZ1FLNWZDcWhZbmZtNEcyQmc0UUpQODFPdURYdjFkN0xYZnpEa0RNSnVWS2c2cTg2MnkwMjE3Y3U2c3Y1MEZYbU9yRmc3YkI5bXloY3dsd1JIMjFrMnNZRVBka3otcmtsaHhlbFgxdGxUbUpkUTNQUENYLWotN1JwU2FCV2Y2UXRqMTBCTjFiZ0pLWEFweWpQV09WUXg4dkhTT0dKMFVCbkxfU3hSQkpUNmlEaUFicDhBb0tvOERrTQ?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxOaWZZTXc5WW9OS0VjbmV1NEs3V1l4cGhINkFNZUhHMS03dVZCUnZXdG51dWtDN0sxRWJLVE9vOEt1UTlBWC1jd0tSTmRLaXR6WlNiajJRWDN4ak1tLWtoM3d0N3ZIYmtpbS04WTR3ckR1TFg3R0h6TzdiMFVpUVc5UlUzbGw3WXNnejBSaC1vTkRBSDdtLTQ0amVaUENoYTZFWGR1d3J3eDVPdnhGcTlqdVgxdWRrWlBhYU9LdnRRUHNZYVpVbTEwejR2WV9hR1VFQTZlVDVHUzRSOUVQVXNweEVwN2JPbENPTWlyNg?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxNNE16OG80X3h6Um83WXp0LWpBVFllcXE0RmlmNjFnNHU2NVVSbV95WmlleXE1bGNuRE1hUVl3T196MDNGZDF6al9NeVlSYnRyUzBFXzdpQWVjaUlLTERteE1aQ0IwSnhtcVpxRlBZdnZiZWgwdXhmYWtCTlp3UHE5ZEdoR3p1c3RUT0JwWHdPdEZ2d3RCZWl5VVc4aVhSYU13VlRF?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxPUFN1eXk5V0UzOFNwTEFBMU1DeWFGdXdKc01BaHhjb0NYM18tV3haRThvd0tzUkdQQWc3Q1M2SEF2RzZmRGRCZnFjVGZESUcyU09CWnY3aWt2LVFZMW1wdnQyV3dnOWhGNHg4UF84Y01rYXpvNDktU2lTVUpVTl9iVGNWb1R2d2RENS1rVmgwZFlRUTlCSzBJVTZuYkx5UVRrLU1tcjYyVkE3RWtJbXdSdGxsYThTLU1nSHc?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
