# ENB Intelligence Report

- ticker: **ENB**
- Report as_of: **2026-10-28**
- Market data as_of: **2026-10-28**
- Quant sources: https://finance.yahoo.com/quote/ENB/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ENB/key-statistics/
- AI analysis snapshot as_of: **2026-10-28**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-29T02:15:56.965652+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 9, 'rule': 1, 'ai': 7, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261028T015717Z-533e470c/ENB** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 9 unique headlines; 6 named publishers; 1 exact duplicates; 9 HTTPS source links; largest publisher share 44.44%; oldest publication 2026-10-21

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 48.5500 |
| Return 1D (%) | 0.3514 |
| Return 1W (%) | 1.1248 |
| Return 1M (%) | 3.3638 |
| Return YTD (%) | 5.6078 |
| Return 1Y (%) | 7.2674 |
| Annualized volatility (%) | 18.0674 |
| Beta vs SPY | -0.1690 |
| Max drawdown (%) | -19.8462 |
| Sharpe (rf=0) | 0.4799 |
| Downside deviation (rf=0, %) | 12.6177 |
| Sortino (rf=0) | 0.6872 |
| Historical VaR 95% (1D, %) | 1.7452 |
| Historical ES 95% (1D, %) | 2.4474 |
| Correlation vs SPY | -0.1188 |
| Tracking error vs SPY (%) | 23.2875 |
| P/E (trailing) | 25.82 |
| P/B | 2.54 |
| EV/EBITDA | 13.03 |
| Revenue growth (%) | 97.10 |
| Forward P/E (estimate) | 21.44 |
| Gross margin (%) | 32.59 |
| Operating margin (%) | 10.16 |
| Return on equity (%) | 9.22 |
| Free cash flow yield (%) | N/A |
| MA50 | 48.3254 |
| Close vs MA50 (%) | 0.4648 |
| MA200 | 51.3134 |
| Close vs MA200 (%) | -5.3854 |
| RSI (14, Wilder) | 57.6310 |
| MACD (12,26) | 0.0747 |
| MACD signal (9) | -0.1961 |
| MACD histogram | 0.2708 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ENB': 270, 'SPY': 270}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 48.5500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.3514 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.1248 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 3.3638 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 5.6078 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 7.2674 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 18.0674 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 12.6177 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.6872 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.7452 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.4474 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1188 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.2875 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1690 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -19.8462 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.4799 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 21.4435 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 32.5940 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 10.1610 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.2210 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 25.8245 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 57.6310 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.2708 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 0.4648 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -5.3854 -> Clearly below the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Enbridge Inc $ENB Stock Purchased by Foster Victor Wealth Advisors LLC
- Summary: Enbridge Inc $ENB Stock Purchased by Foster Victor Wealth Advisors LLC
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxOdzhCQjVMbjlieFVKWldTRFlUYVB3T1pOSmQzRXpBVE9uWEVXR2hFODRuS1g1VWVleERoUkdqbllMWklOVk55b01GUVBBUXZRUVhsQUhuTE82bWV5SGUybTlMcG1CYmx5Z2VWRExlekZHbldCTmFvY0RPSGRTaGdWZXpQdldhNk1CT2NvMHg2UUU3XzNLTmNoLWp2UmZlaWt2Q0kxT1FnbnZGQjZ1QjdvSElOd0k5bHdZbnEtUDg2b0dfYko3QkxsZjVB?oc=5>

### Enbridge Stock: 3 Things to Look for in Its Q3 Results
- Summary: Highlights key metrics for upcoming earnings.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigwFBVV95cUxNZ3VuR2ZHZlZjWFBiVlRId2hyTmJIeHRfd2NwUHI5RWtRaXk3MUZqUEJVc3EwN2lqaUhsQUhVS3NORkxnWFdMSHFzTlVxbGV0Vk85RUxqNXF6akQyZkFsMVZfR1VKdmU3NnBuc193Qlk4bklqN2RJcEVILVpnX2w0d21YTQ?oc=5>

### 24,314 Enbridge Inc $ENB Shares Bought by Tectonic Advisors LLC
- Summary: Shares of ENB were purchased by Tectonic Advisors LLC, indicating investor activity but no direct company action.
- Date: 2026-10-24 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxNdjh2azJVREhUcThocHVEejMxaENic2xYb1ZPc2w5c0liZmFiWko4bXVtQUpHQks5U3dCRVNBT0ZYb3F1TVdIaC14SURPLW5wY25uaC1UM29VWm9PNENtaHZQRHNxcWFKanBZZTM5dTUtS19Damxyb043OWdwMGlSdUFRTU9NcDUwR0NFRGxFZER0bmFhak1mM21OMmk5dTZVUXJDRWtIdF9vWEJHcXhYR3hEcWpUeTQ5WjBBZXo4TQ?oc=5>

### Investors Heavily Search Enbridge Inc (ENB): Here is What You Need to Know
- Summary: Investors are actively researching Enbridge, indicating growing interest and potential positive sentiment.
- Date: 2026-10-28 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxPQzBzUFVBMHNRb2Y1YS1OYktvekxLUWxKc0VJbzRKdDFrdG5EdklBVnVaRFdXeGctLUZsNzJud2pMMjh2T01IZE5xX1Q5QlJFcWR1Q1lHTjZrM0NCVWQwZy1MSTRua1dpNnVDTHctYnVqWjRyaHVVRzRRbFVjbnZTNGM5bTdSM0Z6Skd0STVlNA?oc=5>

### Here's How Much Enbridge (ENB) Stock You'd Need to Earn $1,000 in Dividend Income Each Year.
- Summary: Calculates required Enbridge shares for $1,000 annual dividend, highlighting dividend yield importance.
- Date: 2026-10-21 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPdlZaTlRHajNxTEQ5Y2ZYb1dLZTZqd2RudTlZWWZ4MWsyZmt0SFl2TnYxcTI4bzNNZkZnUnRaNEF3ZDJQMU1aRVE2SGwzSlNxc1cxQ2pZQkRnaHBzZGlGMS1BYnV2MjVaMkdkN1ZNaExUdEhMSjRPd0xuX2trOTc4dW85dWpuY19PcWdCX0VOOVNId0cwYnc?oc=5>

### 41,197 Enbridge Inc $ENB Shares Bought by Oppenheimer & Co. Inc.
- Summary: Oppenheimer purchased 41,197 Enbridge shares, reflecting institutional interest.
- Date: 2026-10-27 | Impact: low | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxPd21wZG5lRWlFUmZ4TXpHYnMxNkplYTlrVkhwX1RLVmlKVmt0MEE4VG5uSFM4UnV6eXJJTERwWHoxTk5NcC1uYzd4b19vWURjSk44eGk1ZDl1MFFHRmtrT3RhMV9rWFpOeVZWcEJNVFJESUdhemxLLS1wcnppY0E3d0I4OTdWM0pLdGNFaEU2ejN3R0tRV0ZpQ2xGM25aejRSZVZhNEgyb0diMjhsallKbUdiVTZhZk5ERXBV?oc=5>

### Trading Near Its 52-Week Low, Is Enbridge Stock a Buy?
- Summary: Enbridge shares near 52-week low, prompting buy‑or‑sell considerations.
- Date: 2026-10-21 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxNNzhWS0Q2WUdYNE1nSTExS2ZpVWtuczBtU1RsX2hQeVJPRUpPZEVYR2RRV2Z5bWZITkI0dHE5ZDBvNjhQWHJEeVhLSVphUkxRVndvekxodHJzRHpuNEJiMDRWbTRlbVhjeUpiRWtMWDBqUVFKNGh4TWRLcGFDbW9DWjd6WU5oQnRfSmRYMVotbS1ERnpFQ3dZZ2VfdEQ4Y1BXR2FxMFNBZGNqTE5XemhlY1Nn?oc=5>

## RISKS

### Enbridge: Risks Lurking Beneath Its 5.8% Dividend Yield (NYSE:ENB)
- Summary: Potential risks associated with maintaining a 5.8% dividend yield may affect future payouts.
- Date: 2026-10-22 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPZTdFcllrMDZkTy1WN29DMGdhbjZKcWJaSXUxS0VGdFc2aUUydDBxZzNuaVFrQzZQRkdLeTFIZEZMbVdHakRzWWhidHNieGcwaHdxOV9JYTlOUkVRZTNOSks4eVhmRXBkVE9FVGw5QkxqMlBHOC1FejhKTXBxdlhlVnFIQS1lUHJ5TmpVdUp4el9jTU9DNV9xTmdYTlU0enRCT0ZMUw?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ENB** | **25.82** | **2.54** | **13.03** | **97.10** | **108,210,348,032.00 USD** | **7.27** |
| TRP.TO | 25.16 | 3.61 | 16.26 | 5.70 | 92,008,849,408.00 CAD | 29.84 |
| KMI | 20.84 | 2.37 | 14.12 | 9.30 | 74,762,133,504.00 USD | 33.85 |
| EPD | 12.90 | 2.72 | 11.35 | 60.80 | 82,189,705,216.00 USD | 29.80 |

Peers fetched as_of: 2026-10-28; ENB reuses existing data (market data as_of: 2026-10-28); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-07-31
- Next expected earnings: 2026-11-06 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-28

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

- https://news.google.com/rss/articles/CBMiygFBVV95cUxOdzhCQjVMbjlieFVKWldTRFlUYVB3T1pOSmQzRXpBVE9uWEVXR2hFODRuS1g1VWVleERoUkdqbllMWklOVk55b01GUVBBUXZRUVhsQUhuTE82bWV5SGUybTlMcG1CYmx5Z2VWRExlekZHbldCTmFvY0RPSGRTaGdWZXpQdldhNk1CT2NvMHg2UUU3XzNLTmNoLWp2UmZlaWt2Q0kxT1FnbnZGQjZ1QjdvSElOd0k5bHdZbnEtUDg2b0dfYko3QkxsZjVB?oc=5
- https://news.google.com/rss/articles/CBMigwFBVV95cUxNZ3VuR2ZHZlZjWFBiVlRId2hyTmJIeHRfd2NwUHI5RWtRaXk3MUZqUEJVc3EwN2lqaUhsQUhVS3NORkxnWFdMSHFzTlVxbGV0Vk85RUxqNXF6akQyZkFsMVZfR1VKdmU3NnBuc193Qlk4bklqN2RJcEVILVpnX2w0d21YTQ?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxNdjh2azJVREhUcThocHVEejMxaENic2xYb1ZPc2w5c0liZmFiWko4bXVtQUpHQks5U3dCRVNBT0ZYb3F1TVdIaC14SURPLW5wY25uaC1UM29VWm9PNENtaHZQRHNxcWFKanBZZTM5dTUtS19Damxyb043OWdwMGlSdUFRTU9NcDUwR0NFRGxFZER0bmFhak1mM21OMmk5dTZVUXJDRWtIdF9vWEJHcXhYR3hEcWpUeTQ5WjBBZXo4TQ?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxPQzBzUFVBMHNRb2Y1YS1OYktvekxLUWxKc0VJbzRKdDFrdG5EdklBVnVaRFdXeGctLUZsNzJud2pMMjh2T01IZE5xX1Q5QlJFcWR1Q1lHTjZrM0NCVWQwZy1MSTRua1dpNnVDTHctYnVqWjRyaHVVRzRRbFVjbnZTNGM5bTdSM0Z6Skd0STVlNA?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPdlZaTlRHajNxTEQ5Y2ZYb1dLZTZqd2RudTlZWWZ4MWsyZmt0SFl2TnYxcTI4bzNNZkZnUnRaNEF3ZDJQMU1aRVE2SGwzSlNxc1cxQ2pZQkRnaHBzZGlGMS1BYnV2MjVaMkdkN1ZNaExUdEhMSjRPd0xuX2trOTc4dW85dWpuY19PcWdCX0VOOVNId0cwYnc?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOOEREM2xtM2E3em1od0thbmF3RjcyWlBzRWlEeXJqQmJzVHJfNDBtSzUtQXRTVDhmTHZRQlRuSG5EdGhvQ3NHeFRwLVA5VlBveFBYNUpaMTFPOXNWbHF2RjJuS0lvblhwQUhOdmtqTkdnYmNhdTcxMGFDVnY1M2FWeVhKWC1kOEl0MGpNZ2ExNVJudzZKN29idUFn?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxPd21wZG5lRWlFUmZ4TXpHYnMxNkplYTlrVkhwX1RLVmlKVmt0MEE4VG5uSFM4UnV6eXJJTERwWHoxTk5NcC1uYzd4b19vWURjSk44eGk1ZDl1MFFHRmtrT3RhMV9rWFpOeVZWcEJNVFJESUdhemxLLS1wcnppY0E3d0I4OTdWM0pLdGNFaEU2ejN3R0tRV0ZpQ2xGM25aejRSZVZhNEgyb0diMjhsallKbUdiVTZhZk5ERXBV?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxNNzhWS0Q2WUdYNE1nSTExS2ZpVWtuczBtU1RsX2hQeVJPRUpPZEVYR2RRV2Z5bWZITkI0dHE5ZDBvNjhQWHJEeVhLSVphUkxRVndvekxodHJzRHpuNEJiMDRWbTRlbVhjeUpiRWtMWDBqUVFKNGh4TWRLcGFDbW9DWjd6WU5oQnRfSmRYMVotbS1ERnpFQ3dZZ2VfdEQ4Y1BXR2FxMFNBZGNqTE5XemhlY1Nn?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPZTdFcllrMDZkTy1WN29DMGdhbjZKcWJaSXUxS0VGdFc2aUUydDBxZzNuaVFrQzZQRkdLeTFIZEZMbVdHakRzWWhidHNieGcwaHdxOV9JYTlOUkVRZTNOSks4eVhmRXBkVE9FVGw5QkxqMlBHOC1FejhKTXBxdlhlVnFIQS1lUHJ5TmpVdUp4el9jTU9DNV9xTmdYTlU0enRCT0ZMUw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
