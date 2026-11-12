# NVO Intelligence Report

- ticker: **NVO**
- Report as_of: **2026-11-11**
- Market data as_of: **2026-11-11**
- Quant sources: https://finance.yahoo.com/quote/NVO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVO/key-statistics/
- AI analysis snapshot as_of: **2026-11-11**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-12T05:47:02.304862+00:00**
- AI status: **Partial: 1 headline remains unclassified and excluded from research conclusions**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 4, 'ai': 8, 'unknown': 1, 'irrelevant': 11})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261111T043601Z-d14951e6/NVO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 14 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 20.83%; oldest publication 2026-11-04

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 41.0900 |
| Return 1D (%) | 0.9582 |
| Return 1W (%) | -2.5842 |
| Return 1M (%) | 6.3406 |
| Return YTD (%) | -15.2097 |
| Return 1Y (%) | -12.2253 |
| Annualized volatility (%) | 45.4088 |
| Beta vs SPY | 0.9570 |
| Max drawdown (%) | -43.6699 |
| Sharpe (rf=0) | -0.0566 |
| Downside deviation (rf=0, %) | 33.9886 |
| Sortino (rf=0) | -0.0757 |
| Historical VaR 95% (1D, %) | 3.1060 |
| Historical ES 95% (1D, %) | 7.1674 |
| Correlation vs SPY | 0.2893 |
| Tracking error vs SPY (%) | 43.4705 |
| P/E (trailing) | 10.38 |
| P/B | 5.54 |
| EV/EBITDA | 1.48 |
| Revenue growth (%) | 5.60 |
| Forward P/E (estimate) | 12.03 |
| Gross margin (%) | 83.33 |
| Operating margin (%) | 50.78 |
| Return on equity (%) | 58.38 |
| Free cash flow yield (%) | N/A |
| MA50 | 40.3268 |
| Close vs MA50 (%) | 1.8925 |
| MA200 | 42.6680 |
| Close vs MA200 (%) | -3.6984 |
| RSI (14, Wilder) | 55.9116 |
| MACD (12,26) | 0.3201 |
| MACD signal (9) | 0.0405 |
| MACD histogram | 0.2796 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVO': 280, 'SPY': 280}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 41.0900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.9582 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.5842 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 6.3406 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -15.2097 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -12.2253 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 45.4088 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 33.9886 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.0757 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.1060 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 7.1674 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2893 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 43.4705 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.9570 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -43.6699 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.0566 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 12.0348 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 83.3330 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 50.7790 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 58.3840 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 10.3763 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 55.9116 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.2796 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 1.8925 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -3.6984 -> Slightly below the moving-average trend level.

## TAILWINDS

### Novo Nordisk Stocks Rise 5.65% While Higher Guidance Meets Diverging Profit Measures
- Summary: Novo Nordisk Stocks Rise 5.65% While Higher Guidance Meets Diverging Profit Measures
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxNNWlBYzJsdjNrckRCVWZYQUJmbWFhX1pwSlRtRjRzZDFOMWNjZUZYWTJjRmJoNjNIMzBpb2k2TG1YWWxhYzRSZ3lIV1p0NTh3akp5anExOTdwQ0hjekhHdUU1Z0twNGFESkszMDE3c0ZSMUZleXZteHd5SlZoZ3VwMjF2ejBFU2FlRHJObzdMWGY?oc=5>

### Novo Nordisk Stock Jumps 6% as Wegovy Hits a Stunning 80% Milestone
- Summary: Novo Nordisk Stock Jumps 6% as Wegovy Hits a Stunning 80% Milestone
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxQVmVmUEUzalZRY3YzMjBaQVRYb2ZDTDV3ZHp1aW1EcVVvdUNWcGlScnhuQWJ6Ym9PUnFKbldXNFlkZUFFbjdVdUREajZhdnZ3SjB1WkFvNExZTEZTZC1lV05yS2tNNnFzazB2VXk4WFhNUVhpcGpnYmc3WnBlZk0tamxJNjZLRWd5OHJOQzVDRGVTbldKSnA4cUFqdXAxVW5CcmgzUTU2Q2JvRXlsQnc?oc=5>

### Novo Nordisk upgraded to Strong Buy on strong Q...
- Summary: Novo Nordisk upgraded to Strong Buy on strong Q...
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPT2NvczhHVlZVNVdFZkp0eWZ3a2todmh1dEE0ekpOUm9iYjhQYUtvOE5fVzNfZ0xPbjczNHVXUXA4MHVsdG1vWkhLTEpFZlBiaExQdjNwMkEwaWRkSE9takRuNUJSaWZFbGtLOVljeEMtN0JPM2YwRmNtbGZuQ0IxenpiY2c0M1cwWTZHSENqX3ZNQmRlTGpwUmhSQUdWbzA?oc=5>

### Novo Nordisk Owns The Oral Weight Loss Market At 7.8x Operating Income (NYSE:NVO)
- Summary: Novo Nordisk dominates oral weight‑loss market with 7.8x operating income.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQTGd2UlczdTBsWVFoUDR2WjVSemxablRhaDFtTkw4LTBTYzVHUE96b190LUJlRXZENmtHVkJXaU1GekJKdVFLY19xLVpBbFUzRExGOGtvWUtHcXc1OUZtdkstX0k2MjlxeG9WVmdRdW1SZUFXOE9sTGZKLWw3SjAwSzhMaXY2ZmRaaDRremE0M0Z1ZldVTWlEZGlkRzR1Ukx2RFFwdkt1LVlTUFJLSXVmSg?oc=5>

### Novo Nordisk: The Recovery Is Gaining Traction. Here's Why I'm Staying On Hold (NYSE:NVO)
- Summary: Positive market sentiment as recovery gains traction, prompting a hold recommendation.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxOZUQxZ1JZTUZIZy1WZ01MMzdLd0dCZS1LdV9aazV6V1JhcVUxWHpMMGwwdEltWlRuUUxEWk9xRnUybEdwei1ObE90RFZabElxaVVzNWw1MTNnSF9kZTNiSVU0YlNmUHRxaW9ZcnFRUk1BSHpTRUlud3RNVkVScTdyNWZnLWlHd1F0enFxdndtSHVmV0ZQYjdwNVlwUFFkNzBMeVlaNG0zZU5KcHg0dl9sQXp4RjhVUQ?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Stocks making the biggest moves premarket: Trump Media, Tesla, CoreWeave, Novo Nordisk and more
- Summary: Stocks making the biggest moves premarket: Trump Media, Tesla, CoreWeave, Novo Nordisk and more
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNbVRCTEpta2pxRWE4NkRKdlVFb3hOZmJReEp5MDRSRTRXVEZUdi1qMnlJT3o0aURDNFBaVy1Hc09JOWJ3ZW1uZWFNVzVxNGdWck80TW1VVG45MzJSQXkzcTBSaS1nYUZqRW1UOENuZnlTSkJESFJja3N3WE43NTZYcWVQcjJTTW95ckt5Z1M4WGhlQTJqOXhDcm12TG4?oc=5>

### Novo Nordisk: Q3 Earnings Bust The Cannibalization Myth
- Summary: Q3 earnings reported, challenging cannibalization concerns.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPOWdicklaV2NyS2RyQkc0allwR3ppLTlwQ3Z3a3Z0a2Q2aVF5ekl0Z1RZbnpWX3hCbDRjdGNRZFpkTGR4TS0yZHljZnZURUFWWmNMOUlrUFZGdFM2SXVLdVBOdWVyTXVLNFNxTm9GcUZaWVdGOG1vcllPeWh6VEJLM3Y5Znk4RXRXWVpqenpNVlRIMktZYnlja2F4cFA?oc=5>

### Novo Nordisk reports liver improvements with Wegovy in some patients
- Summary: Novo Nordisk reports liver function improvements in some patients using Wegovy, indicating potential benefits of its obesity drug.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxOcEk4cnBpT1YyWTZiNXRoNktIcTJ1NjdLb0ZPREZ5M1pSNUdmNjc1S0FfcktLRV9fQlVKN2RNRDFJeGJES0x5SnZiSDNYeUo1LTFVLXhfZnYyUWtwY3EwTjd6ZXZueEJjS0RtTmk0dnJ3RjQ2UkhROG1uT3R3NlZDVVVoeV9GUWJiLW5rZVF1eHpxdGdBd0pLbWxCTDFWbzV2LTNGbl9QMkZYQQ?oc=5>

### A buyback of up to DKK 15B continues at Novo Nordisk (NVO).
- Summary: Novo Nordisk continues a share buyback program up to DKK 15B, signaling confidence in its financial position.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxNbGo1U2FJanhqbURNTDRicG1ZN0JXU1dSc3Y1VlByZGJ6QkVEeEpSSVJSQ3RZcTZNdVhYbVk4WW9KbWJvdlB6QUl2c3VYSGREWFE1SWlUWGNOUVpudWtsSW9vOGluZlBKQWlBeUxKeFNWc0Vta1N2ai1FbjN5ZXA2QVU4QzNoblFqdzZKa2FNem4zUlBqSTUtbXg0NGdxcWJrQXFQSEJmZTZsb1hyN0dCYg?oc=5>

### Novo Nordisk: Valuations Are Blind To The Upside (NYSE:NVO)
- Summary: Analysts argue valuations ignore upside potential, suggesting possible upside for investors.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxQSWE0ekhNR3pzUHBMWjhIR3JwVG1QeThWWUxlSDU3dHEyY0xzLUIwTnZKR0FXTllJbDJJZk5HSzdBWUltZC1FWmJzR1ZGazZXTWJGQmRuSGJwcUJrakt5SXI4cU9FcV9ENUtZNElzUmtRNmNFa1RyX25JVkFPSHNMUHo1c2Z3eWRZQVJUMzRuT1hGUQ?oc=5>

### Wegovy linked to 18.9 pounds of average weight loss in six months versus another treatment
- Summary: Product performance data shows Wegovy’s superior weight loss results.
- Date: 2026-11-06 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxNa3FDOTVPNUdvSEdsWHlsTVdDeHRjaDk5eU9TMW5uQjlQZ1M0dFp2NnQ5RDdCRGR2dUhjX05HX2p6RUJaZUZKWFc3UWt0ZmVoMEE5ckFYSWJ0X1FaUWZfazIzdVdOX0N2N3lUOENVYlJqOFJwYXJhZVlnU25LcGpoVGZPc3VrN1Jjdi1lcWlHczRLNWF1Zlp0MVJ5NVJoTXFNSG1UTGRWTXFWUzdyVktFN0NvYXNYZlYzR0dV?oc=5>

## RISKS

### Novo Nordisk hit by FDA warning on Ozempic: Can NVO avoid further decline?
- Summary: FDA warning on Ozempic may trigger further decline in shares.
- Date: 2026-11-11 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxQOC1MYXFoRzRtTjFmSVRpTVdFVkF0T1d1Q3VRYnRWRE1mcUg1V3gxMjJYSnNYNGVVNFFLdVE3eEJ6RUxDTE4tZEg5WlI0c0ZSZW5FZnRabFZqLVdCTkY2LXlsbmczeXNQN3Y4UE9VS1VGckFmY1NvS2dHSUNYNkhHLTVTWXpCOGMtdlAyOTNpMno2dw?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVO** | **10.38** | **5.54** | **1.48** | **5.60** | **181,139,324,928.00 USD** | **-12.23** |
| LLY | 46.65 | 31.81 | 28.50 | 38.60 | 1,280,258,998,272.00 USD | 46.30 |
| ROG.SW | N/A | N/A | N/A | N/A | N/A unknown currency | N/A |
| SAN.PA | 25.03 | 1.43 | 8.00 | 15.70 | 103,764,738,048.00 EUR | 4.54 |

Peers fetched as_of: 2026-11-11; NVO reuses existing data (market data as_of: 2026-11-11); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-04
- Next expected earnings: 2027-02-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-11

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

- https://news.google.com/rss/articles/CBMikAFBVV95cUxNNWlBYzJsdjNrckRCVWZYQUJmbWFhX1pwSlRtRjRzZDFOMWNjZUZYWTJjRmJoNjNIMzBpb2k2TG1YWWxhYzRSZ3lIV1p0NTh3akp5anExOTdwQ0hjekhHdUU1Z0twNGFESkszMDE3c0ZSMUZleXZteHd5SlZoZ3VwMjF2ejBFU2FlRHJObzdMWGY?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxQVmVmUEUzalZRY3YzMjBaQVRYb2ZDTDV3ZHp1aW1EcVVvdUNWcGlScnhuQWJ6Ym9PUnFKbldXNFlkZUFFbjdVdUREajZhdnZ3SjB1WkFvNExZTEZTZC1lV05yS2tNNnFzazB2VXk4WFhNUVhpcGpnYmc3WnBlZk0tamxJNjZLRWd5OHJOQzVDRGVTbldKSnA4cUFqdXAxVW5CcmgzUTU2Q2JvRXlsQnc?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPT2NvczhHVlZVNVdFZkp0eWZ3a2todmh1dEE0ekpOUm9iYjhQYUtvOE5fVzNfZ0xPbjczNHVXUXA4MHVsdG1vWkhLTEpFZlBiaExQdjNwMkEwaWRkSE9takRuNUJSaWZFbGtLOVljeEMtN0JPM2YwRmNtbGZuQ0IxenpiY2c0M1cwWTZHSENqX3ZNQmRlTGpwUmhSQUdWbzA?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxQTGd2UlczdTBsWVFoUDR2WjVSemxablRhaDFtTkw4LTBTYzVHUE96b190LUJlRXZENmtHVkJXaU1GekJKdVFLY19xLVpBbFUzRExGOGtvWUtHcXc1OUZtdkstX0k2MjlxeG9WVmdRdW1SZUFXOE9sTGZKLWw3SjAwSzhMaXY2ZmRaaDRremE0M0Z1ZldVTWlEZGlkRzR1Ukx2RFFwdkt1LVlTUFJLSXVmSg?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxOZUQxZ1JZTUZIZy1WZ01MMzdLd0dCZS1LdV9aazV6V1JhcVUxWHpMMGwwdEltWlRuUUxEWk9xRnUybEdwei1ObE90RFZabElxaVVzNWw1MTNnSF9kZTNiSVU0YlNmUHRxaW9ZcnFRUk1BSHpTRUlud3RNVkVScTdyNWZnLWlHd1F0enFxdndtSHVmV0ZQYjdwNVlwUFFkNzBMeVlaNG0zZU5KcHg0dl9sQXp4RjhVUQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNbVRCTEpta2pxRWE4NkRKdlVFb3hOZmJReEp5MDRSRTRXVEZUdi1qMnlJT3o0aURDNFBaVy1Hc09JOWJ3ZW1uZWFNVzVxNGdWck80TW1VVG45MzJSQXkzcTBSaS1nYUZqRW1UOENuZnlTSkJESFJja3N3WE43NTZYcWVQcjJTTW95ckt5Z1M4WGhlQTJqOXhDcm12TG4?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPOWdicklaV2NyS2RyQkc0allwR3ppLTlwQ3Z3a3Z0a2Q2aVF5ekl0Z1RZbnpWX3hCbDRjdGNRZFpkTGR4TS0yZHljZnZURUFWWmNMOUlrUFZGdFM2SXVLdVBOdWVyTXVLNFNxTm9GcUZaWVdGOG1vcllPeWh6VEJLM3Y5Znk4RXRXWVpqenpNVlRIMktZYnlja2F4cFA?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxOcEk4cnBpT1YyWTZiNXRoNktIcTJ1NjdLb0ZPREZ5M1pSNUdmNjc1S0FfcktLRV9fQlVKN2RNRDFJeGJES0x5SnZiSDNYeUo1LTFVLXhfZnYyUWtwY3EwTjd6ZXZueEJjS0RtTmk0dnJ3RjQ2UkhROG1uT3R3NlZDVVVoeV9GUWJiLW5rZVF1eHpxdGdBd0pLbWxCTDFWbzV2LTNGbl9QMkZYQQ?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNbGo1U2FJanhqbURNTDRicG1ZN0JXU1dSc3Y1VlByZGJ6QkVEeEpSSVJSQ3RZcTZNdVhYbVk4WW9KbWJvdlB6QUl2c3VYSGREWFE1SWlUWGNOUVpudWtsSW9vOGluZlBKQWlBeUxKeFNWc0Vta1N2ai1FbjN5ZXA2QVU4QzNoblFqdzZKa2FNem4zUlBqSTUtbXg0NGdxcWJrQXFQSEJmZTZsb1hyN0dCYg?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxQSWE0ekhNR3pzUHBMWjhIR3JwVG1QeThWWUxlSDU3dHEyY0xzLUIwTnZKR0FXTllJbDJJZk5HSzdBWUltZC1FWmJzR1ZGazZXTWJGQmRuSGJwcUJrakt5SXI4cU9FcV9ENUtZNElzUmtRNmNFa1RyX25JVkFPSHNMUHo1c2Z3eWRZQVJUMzRuT1hGUQ?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxNa3FDOTVPNUdvSEdsWHlsTVdDeHRjaDk5eU9TMW5uQjlQZ1M0dFp2NnQ5RDdCRGR2dUhjX05HX2p6RUJaZUZKWFc3UWt0ZmVoMEE5ckFYSWJ0X1FaUWZfazIzdVdOX0N2N3lUOENVYlJqOFJwYXJhZVlnU25LcGpoVGZPc3VrN1Jjdi1lcWlHczRLNWF1Zlp0MVJ5NVJoTXFNSG1UTGRWTXFWUzdyVktFN0NvYXNYZlYzR0dV?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxQOC1MYXFoRzRtTjFmSVRpTVdFVkF0T1d1Q3VRYnRWRE1mcUg1V3gxMjJYSnNYNGVVNFFLdVE3eEJ6RUxDTE4tZEg5WlI0c0ZSZW5FZnRabFZqLVdCTkY2LXlsbmczeXNQN3Y4UE9VS1VGckFmY1NvS2dHSUNYNkhHLTVTWXpCOGMtdlAyOTNpMno2dw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
