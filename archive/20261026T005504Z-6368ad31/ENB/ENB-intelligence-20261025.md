# ENB Intelligence Report

- ticker: **ENB**
- Report as_of: **2026-10-25**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/ENB/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ENB/key-statistics/
- AI analysis snapshot as_of: **2026-10-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-26T01:24:23.506317+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 18, 'rule': 4, 'ai': 7, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **4**; {'directional_claim_without_event_type': 4}
- RSS source audit (metadata only, not article fact-checking): 18 unique headlines; 11 named publishers; 2 exact duplicates; 18 HTTPS source links; largest publisher share 27.78%; oldest publication 2026-10-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 48.1500 |
| Return 1D (%) | 0.2916 |
| Return 1W (%) | 0.1040 |
| Return 1M (%) | 0.6270 |
| Return YTD (%) | 4.7377 |
| Return 1Y (%) | 6.1807 |
| Annualized volatility (%) | 18.0922 |
| Beta vs SPY | -0.1681 |
| Max drawdown (%) | -19.8462 |
| Sharpe (rf=0) | 0.4230 |
| Downside deviation (rf=0, %) | 12.6365 |
| Sortino (rf=0) | 0.6056 |
| Historical VaR 95% (1D, %) | 1.7452 |
| Historical ES 95% (1D, %) | 2.4474 |
| Correlation vs SPY | -0.1184 |
| Tracking error vs SPY (%) | 23.3332 |
| P/E (trailing) | 25.75 |
| P/B | 2.52 |
| EV/EBITDA | 12.98 |
| Revenue growth (%) | 97.10 |
| Forward P/E (estimate) | 21.32 |
| Gross margin (%) | 32.59 |
| Operating margin (%) | 10.16 |
| Return on equity (%) | 9.22 |
| Free cash flow yield (%) | N/A |
| MA50 | 48.4792 |
| Close vs MA50 (%) | -0.6791 |
| MA200 | 51.2448 |
| Close vs MA200 (%) | -6.0392 |
| RSI (14, Wilder) | 54.2020 |
| MACD (12,26) | -0.1115 |
| MACD signal (9) | -0.4047 |
| MACD histogram | 0.2932 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ENB': 267, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 48.1500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.2916 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.1040 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 0.6270 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 4.7377 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 6.1807 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 18.0922 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 12.6365 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.6056 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.7452 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.4474 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1184 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.3332 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1681 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -19.8462 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.4230 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 21.3179 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 32.5940 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 10.1610 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.2210 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 25.7487 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 54.2020 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.2932 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -0.6791 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -6.0392 -> Clearly below the moving-average trend level.

## TAILWINDS

### Enbridge stock trades flat amid recent US gas utility acquisitions and rising cash flow
- Summary: Enbridge stock trades flat amid recent US gas utility acquisitions and rising cash flow
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQN2JWSVVkQzdjSVZqbGF5OER2SDVJaGVaVUlZaDJVb2V0X215Tjdja1hYcjVOSHUtalFxaWtxMTlkSU00Q3RjYjNPbHpNOUF3NVkyYVFLV3ZWRlNIMEs3N0ZyaUQ2Z1d6YUxQU2lqTDBnUm5nbTBkdFZ1ZG9XYjhPUVJsU0ZSc28zeXBRb252dE1PcmJw?oc=5>

### Why Is Enbridge (ENB) 18% Below Its High While Revenue Nearly Doubled?
- Summary: Revenue nearly doubled, indicating strong operational performance, potentially boosting investor confidence.
- Date: 2026-10-20 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNVVJVc29MSS1uR0s1T3ltWkluZ1RLbFJPTkZYSWdneEx2bmh6SnV2Q05QY3JmYmdzQmN6UTQ0RmJoajFabDhkdWhzSEhQaUFEUEVGdngyNEt2Skd1d3lMYXA3c1pxUzNnTDJuZzRrNmtPOFgxNTdHS1BKNkwtblYwT1lvRDJQWTRHWEt1VTQtSXJCbS14?oc=5>

### Enbridge (TSX:ENB) Stock Could Be Priced Richly As Pipeline Volumes Draw Focus
- Summary: Investors eye Enbridge’s pipeline volumes, suggesting potential upside in stock pricing.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxOall0Z255RzFxU1JHRlR1OHNyUmFEQUxtbDRuUzd2M0FqMzVwaXNPdTg0Qm1qS0lFeXhqdnphTVhqMFNJUGN5QlJXaXU0bE5YVkRZWDVvRHhsUzdnMWQ4R1c5WkJNUjJqcW44RGVxdFhuWEJTc3pYZEE0QVRnT3dhNnd4S2lldkxSNTJQbVFDSEVQV2ZNU3NGNTFfa3hSeUFlRGNfTkVaYmdtbFRwUkZyNmM2cmstTk1YX2FZV0JtQ195Z1pfWTJz0gHMAUFVX3lxTE1zSDgwUkp4R0Vsb1pXMDJjcjlMMmFENWJKZ1lVTFZCNHV1YXFURVdUanpnalk4bU9PV3paUGdfQnV0dWVXT3dobUdVUkNjZE03alFDSkhrci1uYmJwMnNZQzZERzBTVFJBcnQ5Z3dfNjFuQTZiTzFzcHdhVjBwQTJMakhSN1hkYkZNc0k5dU9nSlhWdFVPeE1nR19xdFhDbWtCak9hdmd3V09tNzVERDRrNnF2VFc5Y045bE02XzBZUldyWWszRFJYVDc1Mg?oc=5>

### Enbridge Inc. (TSX:ENB) Common Shares Advance as Regulated Utility Integration and Continental Pipeline Utilization Support Market Sentiment
- Summary: Enbridge shares rise due to integration and pipeline utilization, boosting market sentiment.
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMihwJBVV95cUxNbUVaeUtncFF2Wlh4UVJBeWVicUt5M1JNM2pBNmNwTVBOVnVwa2xydW9Tc1ZGd2I4OEtIT0hnY3BVUVhEcURZWXBHLV9PVG9CN094aWlFaGdJQ3hNSTNHS2ZJZ1NqZ3RhUWd3RnJ0U2V0dE5yMVRLNnNNZDhQSlJPdGg5U1F2M2k2T3JZU2wtLVp4OUpVVzRyQTdKQS14c3VQR20wSFRLRVFDd2IzdTh6WkdkdHZGdU5veFZJeFlWY1VFNVBGNWFycW5jbHpBc2lqa2VFYjBGY1FJWjlPRHpJMXprZGlrSF9JVEZjQkhjYU5XUGdTOGFnVEJTVjE2ZnR4Zi1ZdjdYYw?oc=5>

### Is Enbridge (TSX:ENB) Emerging As A Key Dividend Stock?
- Summary: Enbridge considered a key dividend stock, attracting income-focused investors.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNbm96QTZna3ZUT09yQUlSaDZIeFNLMU5ydHRkNDZWWkdUcmRFclhKU201bFlkQVphY0FmUDBKN3IwTC1EZlpzSkpLT2VGWVVzMG51czl1UzZ2TFFlSTQzN084Q0tGeTRwXzdIZFpWOTh6aE1vVVl4Qm02cGYxNThJOE5VeDVaNmFvbm9OUnBiR3JqMEdoV0VtZkZaZw?oc=5>

### Will Enbridge stock break higher as momentum builds near resistance?
- Summary: Enbridge stock may break resistance, driven by recent momentum.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOX09ELUplNWNaUVc1VU5sdDkyU2FmdGxWeDhfYUpLb2ZIS1h4bGVkNW1GcXB1a3BxRXozRVp3dXRlN3V6T0RlOWZvXzBnbHl0NksxQkxFNHFIeFhQQ2JiTHdacUNWNGZ0Mkd5eXhYYTNZZE8tWGswRi00NkhBTk85S3ZYVW1tUW9xOW1Bc0NFbTBQV2Ju?oc=5>

## HEADWINDS

### Enbridge Stock Is Down 15% and Yields 5.7%: Here’s How I’d Buy it for Income
- Summary: Enbridge Stock Is Down 15% and Yields 5.7%: Here’s How I’d Buy it for Income
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOV2hrNVpLZi1scENIRGV1UmJmbnFXTTRNbHBSZnBMYnJ6cE5mZnEzazlYY1RDYWNUMFRmaGZ0UC1YSC1iYlBBWUdaZDhSRHhvWTlqMDZWWXZrRUcwOVI3Y2xBZlJCd3FHOTZ6TlFKSmJPRU1CbG8zVkNkQXp1X0drdWNTVGlLWFlBVzNmRURGcnJFTkotdklJVktIX3V4OE9UVlU3YWp3?oc=5>

### Enbridge (ENB) Stock Declines While Market Improves: Some Information for Investors
- Summary: ENB shares fell despite broader market gains, suggesting short-term investor concern.
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQc2hwZURvNlhMdHhGY1dJNW9KMnYtVzl3T2RjazBUX3BWSjBhS3drdGhHeVVsbi0tbUw2Vklad2hpMGNFMG10cG1weTFqMTlwMTMxNHlwWEJLR2Zhams0SEdaU3lkSXV6d1lwQTgxSTdLSWprT0N2REppWFJGMFI4dGw0cnBwRXFWeG5PTkNfZzZpLXhCNC15c3RzWXBGZU0?oc=5>

## CATALYSTS

### Enbridge Inc $ENB Stock Purchased by Foster Victor Wealth Advisors LLC
- Summary: Enbridge Inc $ENB Stock Purchased by Foster Victor Wealth Advisors LLC
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxOdzhCQjVMbjlieFVKWldTRFlUYVB3T1pOSmQzRXpBVE9uWEVXR2hFODRuS1g1VWVleERoUkdqbllMWklOVk55b01GUVBBUXZRUVhsQUhuTE82bWV5SGUybTlMcG1CYmx5Z2VWRExlekZHbldCTmFvY0RPSGRTaGdWZXpQdldhNk1CT2NvMHg2UUU3XzNLTmNoLWp2UmZlaWt2Q0kxT1FnbnZGQjZ1QjdvSElOd0k5bHdZbnEtUDg2b0dfYko3QkxsZjVB?oc=5>

### Enbridge raises dividend for 31st year: ENB consolidates after modest daily gain
- Summary: Enbridge raises dividend for 31st year: ENB consolidates after modest daily gain
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNdGVGdDZsbkx3cXVVdVNRRUhGTGROMVB1Nkw4YURWZ3V5dUkyWlFKZ1UzVU11WFI5X1dBTkpiWXFBbGZUa1dCTEJvYW9KWG9PSTdCVUVtMXl5bkV4UEw0enZITGtBcjlEa1ZEWF9Edk84Z2Z1Qm42bmhmT1IzZFEzbkVnUk1nWEx6N0pn?oc=5>

## RISKS

### Enbridge: Risks Lurking Beneath Its 5.8% Dividend Yield (NYSE:ENB)
- Summary: Potential risks associated with maintaining a 5.8% dividend yield may affect future payouts.
- Date: 2026-10-22 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPZTdFcllrMDZkTy1WN29DMGdhbjZKcWJaSXUxS0VGdFc2aUUydDBxZzNuaVFrQzZQRkdLeTFIZEZMbVdHakRzWWhidHNieGcwaHdxOV9JYTlOUkVRZTNOSks4eVhmRXBkVE9FVGw5QkxqMlBHOC1FejhKTXBxdlhlVnFIQS1lUHJ5TmpVdUp4el9jTU9DNV9xTmdYTlU0enRCT0ZMUw?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ENB** | **25.75** | **2.52** | **12.98** | **97.10** | **107,318,820,864.00 USD** | **6.18** |
| TRP.TO | 24.88 | 3.57 | 16.16 | 5.70 | 90,967,089,152.00 CAD | 27.54 |
| KMI | 21.25 | 2.43 | 14.38 | 9.30 | 76,700,237,824.00 USD | 36.43 |
| EPD | 12.88 | 2.65 | 11.15 | 60.80 | 80,073,416,704.00 USD | 27.56 |

Peers fetched as_of: 2026-10-25; ENB reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-07-31
- Next expected earnings: 2026-11-06 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-25

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-07-31
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: https://www.sec.gov/Archives/edgar/data/895728/000119312526326752/enb-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMilAFBVV95cUxQN2JWSVVkQzdjSVZqbGF5OER2SDVJaGVaVUlZaDJVb2V0X215Tjdja1hYcjVOSHUtalFxaWtxMTlkSU00Q3RjYjNPbHpNOUF3NVkyYVFLV3ZWRlNIMEs3N0ZyaUQ2Z1d6YUxQU2lqTDBnUm5nbTBkdFZ1ZG9XYjhPUVJsU0ZSc28zeXBRb252dE1PcmJw?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNVVJVc29MSS1uR0s1T3ltWkluZ1RLbFJPTkZYSWdneEx2bmh6SnV2Q05QY3JmYmdzQmN6UTQ0RmJoajFabDhkdWhzSEhQaUFEUEVGdngyNEt2Skd1d3lMYXA3c1pxUzNnTDJuZzRrNmtPOFgxNTdHS1BKNkwtblYwT1lvRDJQWTRHWEt1VTQtSXJCbS14?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxOall0Z255RzFxU1JHRlR1OHNyUmFEQUxtbDRuUzd2M0FqMzVwaXNPdTg0Qm1qS0lFeXhqdnphTVhqMFNJUGN5QlJXaXU0bE5YVkRZWDVvRHhsUzdnMWQ4R1c5WkJNUjJqcW44RGVxdFhuWEJTc3pYZEE0QVRnT3dhNnd4S2lldkxSNTJQbVFDSEVQV2ZNU3NGNTFfa3hSeUFlRGNfTkVaYmdtbFRwUkZyNmM2cmstTk1YX2FZV0JtQ195Z1pfWTJz0gHMAUFVX3lxTE1zSDgwUkp4R0Vsb1pXMDJjcjlMMmFENWJKZ1lVTFZCNHV1YXFURVdUanpnalk4bU9PV3paUGdfQnV0dWVXT3dobUdVUkNjZE03alFDSkhrci1uYmJwMnNZQzZERzBTVFJBcnQ5Z3dfNjFuQTZiTzFzcHdhVjBwQTJMakhSN1hkYkZNc0k5dU9nSlhWdFVPeE1nR19xdFhDbWtCak9hdmd3V09tNzVERDRrNnF2VFc5Y045bE02XzBZUldyWWszRFJYVDc1Mg?oc=5
- https://news.google.com/rss/articles/CBMihwJBVV95cUxNbUVaeUtncFF2Wlh4UVJBeWVicUt5M1JNM2pBNmNwTVBOVnVwa2xydW9Tc1ZGd2I4OEtIT0hnY3BVUVhEcURZWXBHLV9PVG9CN094aWlFaGdJQ3hNSTNHS2ZJZ1NqZ3RhUWd3RnJ0U2V0dE5yMVRLNnNNZDhQSlJPdGg5U1F2M2k2T3JZU2wtLVp4OUpVVzRyQTdKQS14c3VQR20wSFRLRVFDd2IzdTh6WkdkdHZGdU5veFZJeFlWY1VFNVBGNWFycW5jbHpBc2lqa2VFYjBGY1FJWjlPRHpJMXprZGlrSF9JVEZjQkhjYU5XUGdTOGFnVEJTVjE2ZnR4Zi1ZdjdYYw?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNbm96QTZna3ZUT09yQUlSaDZIeFNLMU5ydHRkNDZWWkdUcmRFclhKU201bFlkQVphY0FmUDBKN3IwTC1EZlpzSkpLT2VGWVVzMG51czl1UzZ2TFFlSTQzN084Q0tGeTRwXzdIZFpWOTh6aE1vVVl4Qm02cGYxNThJOE5VeDVaNmFvbm9OUnBiR3JqMEdoV0VtZkZaZw?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOX09ELUplNWNaUVc1VU5sdDkyU2FmdGxWeDhfYUpLb2ZIS1h4bGVkNW1GcXB1a3BxRXozRVp3dXRlN3V6T0RlOWZvXzBnbHl0NksxQkxFNHFIeFhQQ2JiTHdacUNWNGZ0Mkd5eXhYYTNZZE8tWGswRi00NkhBTk85S3ZYVW1tUW9xOW1Bc0NFbTBQV2Ju?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOV2hrNVpLZi1scENIRGV1UmJmbnFXTTRNbHBSZnBMYnJ6cE5mZnEzazlYY1RDYWNUMFRmaGZ0UC1YSC1iYlBBWUdaZDhSRHhvWTlqMDZWWXZrRUcwOVI3Y2xBZlJCd3FHOTZ6TlFKSmJPRU1CbG8zVkNkQXp1X0drdWNTVGlLWFlBVzNmRURGcnJFTkotdklJVktIX3V4OE9UVlU3YWp3?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQc2hwZURvNlhMdHhGY1dJNW9KMnYtVzl3T2RjazBUX3BWSjBhS3drdGhHeVVsbi0tbUw2Vklad2hpMGNFMG10cG1weTFqMTlwMTMxNHlwWEJLR2Zhams0SEdaU3lkSXV6d1lwQTgxSTdLSWprT0N2REppWFJGMFI4dGw0cnBwRXFWeG5PTkNfZzZpLXhCNC15c3RzWXBGZU0?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxOdzhCQjVMbjlieFVKWldTRFlUYVB3T1pOSmQzRXpBVE9uWEVXR2hFODRuS1g1VWVleERoUkdqbllMWklOVk55b01GUVBBUXZRUVhsQUhuTE82bWV5SGUybTlMcG1CYmx5Z2VWRExlekZHbldCTmFvY0RPSGRTaGdWZXpQdldhNk1CT2NvMHg2UUU3XzNLTmNoLWp2UmZlaWt2Q0kxT1FnbnZGQjZ1QjdvSElOd0k5bHdZbnEtUDg2b0dfYko3QkxsZjVB?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNdGVGdDZsbkx3cXVVdVNRRUhGTGROMVB1Nkw4YURWZ3V5dUkyWlFKZ1UzVU11WFI5X1dBTkpiWXFBbGZUa1dCTEJvYW9KWG9PSTdCVUVtMXl5bkV4UEw0enZITGtBcjlEa1ZEWF9Edk84Z2Z1Qm42bmhmT1IzZFEzbkVnUk1nWEx6N0pn?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPZTdFcllrMDZkTy1WN29DMGdhbjZKcWJaSXUxS0VGdFc2aUUydDBxZzNuaVFrQzZQRkdLeTFIZEZMbVdHakRzWWhidHNieGcwaHdxOV9JYTlOUkVRZTNOSks4eVhmRXBkVE9FVGw5QkxqMlBHOC1FejhKTXBxdlhlVnFIQS1lUHJ5TmpVdUp4el9jTU9DNV9xTmdYTlU0enRCT0ZMUw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
