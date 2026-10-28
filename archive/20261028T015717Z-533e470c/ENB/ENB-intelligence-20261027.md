# ENB Intelligence Report

- ticker: **ENB**
- Report as_of: **2026-10-27**
- Market data as_of: **2026-10-27**
- Quant sources: https://finance.yahoo.com/quote/ENB/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ENB/key-statistics/
- AI analysis snapshot as_of: **2026-10-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-28T02:22:08.412974+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 15, 'rule': 3, 'ai': 8, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261027T014607Z-b66f6bd5/ENB** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **3**; {'directional_claim_without_event_type': 2, 'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 15 unique headlines; 8 named publishers; 2 exact duplicates; 15 HTTPS source links; largest publisher share 26.67%; oldest publication 2026-10-21

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 48.3800 |
| Return 1D (%) | 0.2487 |
| Return 1W (%) | 1.0232 |
| Return 1M (%) | 3.5088 |
| Return YTD (%) | 5.2380 |
| Return 1Y (%) | 6.4847 |
| Annualized volatility (%) | 18.0694 |
| Beta vs SPY | -0.1701 |
| Max drawdown (%) | -19.8462 |
| Sharpe (rf=0) | 0.4392 |
| Downside deviation (rf=0, %) | 12.6235 |
| Sortino (rf=0) | 0.6286 |
| Historical VaR 95% (1D, %) | 1.7452 |
| Historical ES 95% (1D, %) | 2.4474 |
| Correlation vs SPY | -0.1196 |
| Tracking error vs SPY (%) | 23.2960 |
| P/E (trailing) | 25.87 |
| P/B | 2.54 |
| EV/EBITDA | 13.01 |
| Revenue growth (%) | 97.10 |
| Forward P/E (estimate) | 21.47 |
| Gross margin (%) | 32.59 |
| Operating margin (%) | 10.16 |
| Return on equity (%) | 9.22 |
| Free cash flow yield (%) | N/A |
| MA50 | 48.3822 |
| Close vs MA50 (%) | -0.0045 |
| MA200 | 51.2911 |
| Close vs MA200 (%) | -5.6756 |
| RSI (14, Wilder) | 56.1476 |
| MACD (12,26) | 0.0138 |
| MACD signal (9) | -0.2637 |
| MACD histogram | 0.2775 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ENB': 269, 'SPY': 269}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 48.3800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.2487 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.0232 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 3.5088 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 5.2380 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 6.4847 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 18.0694 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 12.6235 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.6286 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.7452 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.4474 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1196 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.2960 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1701 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -19.8462 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.4392 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 21.4695 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 32.5940 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 10.1610 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.2210 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 25.8717 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 56.1476 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.2775 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -0.0045 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -5.6756 -> Clearly below the moving-average trend level.

## TAILWINDS

### Enbridge stock trades flat amid recent US gas utility acquisitions and rising cash flow
- Summary: Enbridge stock trades flat amid recent US gas utility acquisitions and rising cash flow
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQN2JWSVVkQzdjSVZqbGF5OER2SDVJaGVaVUlZaDJVb2V0X215Tjdja1hYcjVOSHUtalFxaWtxMTlkSU00Q3RjYjNPbHpNOUF3NVkyYVFLV3ZWRlNIMEs3N0ZyaUQ2Z1d6YUxQU2lqTDBnUm5nbTBkdFZ1ZG9XYjhPUVJsU0ZSc28zeXBRb252dE1PcmJw?oc=5>

### Is Enbridge (TSX:ENB) Emerging As A Key Dividend Stock?
- Summary: Enbridge considered a key dividend stock, attracting income-focused investors.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNbm96QTZna3ZUT09yQUlSaDZIeFNLMU5ydHRkNDZWWkdUcmRFclhKU201bFlkQVphY0FmUDBKN3IwTC1EZlpzSkpLT2VGWVVzMG51czl1UzZ2TFFlSTQzN084Q0tGeTRwXzdIZFpWOTh6aE1vVVl4Qm02cGYxNThJOE5VeDVaNmFvbm9OUnBiR3JqMEdoV0VtZkZaZw?oc=5>

### Will Enbridge stock break higher as momentum builds near resistance?
- Summary: Enbridge stock may break resistance, driven by recent momentum.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOX09ELUplNWNaUVc1VU5sdDkyU2FmdGxWeDhfYUpLb2ZIS1h4bGVkNW1GcXB1a3BxRXozRVp3dXRlN3V6T0RlOWZvXzBnbHl0NksxQkxFNHFIeFhQQ2JiTHdacUNWNGZ0Mkd5eXhYYTNZZE8tWGswRi00NkhBTk85S3ZYVW1tUW9xOW1Bc0NFbTBQV2Ju?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Enbridge Inc $ENB Stock Purchased by Foster Victor Wealth Advisors LLC
- Summary: Enbridge Inc $ENB Stock Purchased by Foster Victor Wealth Advisors LLC
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxOdzhCQjVMbjlieFVKWldTRFlUYVB3T1pOSmQzRXpBVE9uWEVXR2hFODRuS1g1VWVleERoUkdqbllMWklOVk55b01GUVBBUXZRUVhsQUhuTE82bWV5SGUybTlMcG1CYmx5Z2VWRExlekZHbldCTmFvY0RPSGRTaGdWZXpQdldhNk1CT2NvMHg2UUU3XzNLTmNoLWp2UmZlaWt2Q0kxT1FnbnZGQjZ1QjdvSElOd0k5bHdZbnEtUDg2b0dfYko3QkxsZjVB?oc=5>

### Enbridge raises dividend for 31st year: ENB consolidates after modest daily gain
- Summary: Enbridge raises dividend for 31st year: ENB consolidates after modest daily gain
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNdGVGdDZsbkx3cXVVdVNRRUhGTGROMVB1Nkw4YURWZ3V5dUkyWlFKZ1UzVU11WFI5X1dBTkpiWXFBbGZUa1dCTEJvYW9KWG9PSTdCVUVtMXl5bkV4UEw0enZITGtBcjlEa1ZEWF9Edk84Z2Z1Qm42bmhmT1IzZFEzbkVnUk1nWEx6N0pn?oc=5>

### Enbridge Stock: 3 Things to Look for in Its Q3 Results
- Summary: Highlights key metrics for upcoming earnings.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigwFBVV95cUxNZ3VuR2ZHZlZjWFBiVlRId2hyTmJIeHRfd2NwUHI5RWtRaXk3MUZqUEJVc3EwN2lqaUhsQUhVS3NORkxnWFdMSHFzTlVxbGV0Vk85RUxqNXF6akQyZkFsMVZfR1VKdmU3NnBuc193Qlk4bklqN2RJcEVILVpnX2w0d21YTQ?oc=5>

### CIBC cuts Enbridge target from CAD 79 to CAD 75 for Enbridge stock
- Summary: Downgrade reduces target price, signals caution.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxPaVhEOG04Nm5fenoxLW1WN1pDSWpOLTJYUVpYS0ZoOTg2cGtkYkJoOTh5aVVSM1Z2VjJJTmtfZUNTVG1CMk1NSFdlM1JSX0hUOGk0MFRfeXUtbV9LSHM0U1Fjc3ZsdjVMd3ZTaktCUnpxaHg5OW0xdFlEU0xmMG4ybElPSzFPY3g3VVNzTU5vT1FTVDNwMDhXNzF6OWhVdmtFNi11Ri1taC1wRzZPOWd3cndTeGpwYXE5cHNRdzFFREE5MEN0RlNUUw?oc=5>

### Here's How Much Enbridge (ENB) Stock You'd Need to Earn $1,000 in Dividend Income Each Year.
- Summary: Calculates shares needed for $1,000 annual dividend, highlighting dividend yield and potential income for investors.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPdlZaTlRHajNxTEQ5Y2ZYb1dLZTZqd2RudTlZWWZ4MWsyZmt0SFl2TnYxcTI4bzNNZkZnUnRaNEF3ZDJQMU1aRVE2SGwzSlNxc1cxQ2pZQkRnaHBzZGlGMS1BYnV2MjVaMkdkN1ZNaExUdEhMSjRPd0xuX2trOTc4dW85dWpuY19PcWdCX0VOOVNId0cwYnc?oc=5>

### 24,314 Enbridge Inc $ENB Shares Bought by Tectonic Advisors LLC
- Summary: Shares of ENB were purchased by Tectonic Advisors LLC, indicating investor activity but no direct company action.
- Date: 2026-10-24 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxNdjh2azJVREhUcThocHVEejMxaENic2xYb1ZPc2w5c0liZmFiWko4bXVtQUpHQks5U3dCRVNBT0ZYb3F1TVdIaC14SURPLW5wY25uaC1UM29VWm9PNENtaHZQRHNxcWFKanBZZTM5dTUtS19Damxyb043OWdwMGlSdUFRTU9NcDUwR0NFRGxFZER0bmFhak1mM21OMmk5dTZVUXJDRWtIdF9vWEJHcXhYR3hEcWpUeTQ5WjBBZXo4TQ?oc=5>

## RISKS

### Enbridge: Risks Lurking Beneath Its 5.8% Dividend Yield (NYSE:ENB)
- Summary: Potential risks associated with maintaining a 5.8% dividend yield may affect future payouts.
- Date: 2026-10-22 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPZTdFcllrMDZkTy1WN29DMGdhbjZKcWJaSXUxS0VGdFc2aUUydDBxZzNuaVFrQzZQRkdLeTFIZEZMbVdHakRzWWhidHNieGcwaHdxOV9JYTlOUkVRZTNOSks4eVhmRXBkVE9FVGw5QkxqMlBHOC1FejhKTXBxdlhlVnFIQS1lUHJ5TmpVdUp4el9jTU9DNV9xTmdYTlU0enRCT0ZMUw?oc=5>

### Trading Near Its 52-Week Low, Is Enbridge Stock a Buy?
- Summary: Shows current price near 52-week low, indicating potential downside risk and market uncertainty.
- Date: 2026-10-21 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTE5NdWxWbFdCcVBSS3RNaXFNOXBVOWpuMUoxdDNQLVNhV1dhSm5scDZ5MkZrdW9vUzJ4cFVZbGRleDVUcHN2UTBhWDZ5MlZDRG1ENzhXU0ZTcjhnMFBYd1RQU3NndUFjVGtBMEJoVGpPRVVKWF9oc3ZrUUZ5MFBMZw?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ENB** | **25.87** | **2.54** | **13.01** | **97.10** | **107,831,451,648.00 USD** | **6.48** |
| TRP.TO | 25.15 | 3.61 | 16.25 | 5.70 | 91,956,764,672.00 CAD | 30.09 |
| KMI | 20.90 | 2.39 | 14.21 | 9.30 | 75,408,162,816.00 USD | 34.65 |
| EPD | 12.91 | 2.65 | 11.17 | 60.80 | 80,267,763,712.00 USD | 26.97 |

Peers fetched as_of: 2026-10-27; ENB reuses existing data (market data as_of: 2026-10-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-07-31
- Next expected earnings: 2026-11-06 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-27

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
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNbm96QTZna3ZUT09yQUlSaDZIeFNLMU5ydHRkNDZWWkdUcmRFclhKU201bFlkQVphY0FmUDBKN3IwTC1EZlpzSkpLT2VGWVVzMG51czl1UzZ2TFFlSTQzN084Q0tGeTRwXzdIZFpWOTh6aE1vVVl4Qm02cGYxNThJOE5VeDVaNmFvbm9OUnBiR3JqMEdoV0VtZkZaZw?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOX09ELUplNWNaUVc1VU5sdDkyU2FmdGxWeDhfYUpLb2ZIS1h4bGVkNW1GcXB1a3BxRXozRVp3dXRlN3V6T0RlOWZvXzBnbHl0NksxQkxFNHFIeFhQQ2JiTHdacUNWNGZ0Mkd5eXhYYTNZZE8tWGswRi00NkhBTk85S3ZYVW1tUW9xOW1Bc0NFbTBQV2Ju?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxOdzhCQjVMbjlieFVKWldTRFlUYVB3T1pOSmQzRXpBVE9uWEVXR2hFODRuS1g1VWVleERoUkdqbllMWklOVk55b01GUVBBUXZRUVhsQUhuTE82bWV5SGUybTlMcG1CYmx5Z2VWRExlekZHbldCTmFvY0RPSGRTaGdWZXpQdldhNk1CT2NvMHg2UUU3XzNLTmNoLWp2UmZlaWt2Q0kxT1FnbnZGQjZ1QjdvSElOd0k5bHdZbnEtUDg2b0dfYko3QkxsZjVB?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNdGVGdDZsbkx3cXVVdVNRRUhGTGROMVB1Nkw4YURWZ3V5dUkyWlFKZ1UzVU11WFI5X1dBTkpiWXFBbGZUa1dCTEJvYW9KWG9PSTdCVUVtMXl5bkV4UEw0enZITGtBcjlEa1ZEWF9Edk84Z2Z1Qm42bmhmT1IzZFEzbkVnUk1nWEx6N0pn?oc=5
- https://news.google.com/rss/articles/CBMigwFBVV95cUxNZ3VuR2ZHZlZjWFBiVlRId2hyTmJIeHRfd2NwUHI5RWtRaXk3MUZqUEJVc3EwN2lqaUhsQUhVS3NORkxnWFdMSHFzTlVxbGV0Vk85RUxqNXF6akQyZkFsMVZfR1VKdmU3NnBuc193Qlk4bklqN2RJcEVILVpnX2w0d21YTQ?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxPaVhEOG04Nm5fenoxLW1WN1pDSWpOLTJYUVpYS0ZoOTg2cGtkYkJoOTh5aVVSM1Z2VjJJTmtfZUNTVG1CMk1NSFdlM1JSX0hUOGk0MFRfeXUtbV9LSHM0U1Fjc3ZsdjVMd3ZTaktCUnpxaHg5OW0xdFlEU0xmMG4ybElPSzFPY3g3VVNzTU5vT1FTVDNwMDhXNzF6OWhVdmtFNi11Ri1taC1wRzZPOWd3cndTeGpwYXE5cHNRdzFFREE5MEN0RlNUUw?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPdlZaTlRHajNxTEQ5Y2ZYb1dLZTZqd2RudTlZWWZ4MWsyZmt0SFl2TnYxcTI4bzNNZkZnUnRaNEF3ZDJQMU1aRVE2SGwzSlNxc1cxQ2pZQkRnaHBzZGlGMS1BYnV2MjVaMkdkN1ZNaExUdEhMSjRPd0xuX2trOTc4dW85dWpuY19PcWdCX0VOOVNId0cwYnc?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTE1ubWgwaVhNYzAwWXBnNDNzdUs5Zi1hRW1EMUxDZE9mYWpTMDBLU1VzSzdlXzRtWDdJYjRDT2ZkaVNJN2F3ZmpzcXhWWXVXVXRkY2xNM2oyeE85a2t4STNNR2t4dndSb25fMWRzeHJ1LUpyVS1jcFFfeTNONFNpQQ?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxNdjh2azJVREhUcThocHVEejMxaENic2xYb1ZPc2w5c0liZmFiWko4bXVtQUpHQks5U3dCRVNBT0ZYb3F1TVdIaC14SURPLW5wY25uaC1UM29VWm9PNENtaHZQRHNxcWFKanBZZTM5dTUtS19Damxyb043OWdwMGlSdUFRTU9NcDUwR0NFRGxFZER0bmFhak1mM21OMmk5dTZVUXJDRWtIdF9vWEJHcXhYR3hEcWpUeTQ5WjBBZXo4TQ?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPZTdFcllrMDZkTy1WN29DMGdhbjZKcWJaSXUxS0VGdFc2aUUydDBxZzNuaVFrQzZQRkdLeTFIZEZMbVdHakRzWWhidHNieGcwaHdxOV9JYTlOUkVRZTNOSks4eVhmRXBkVE9FVGw5QkxqMlBHOC1FejhKTXBxdlhlVnFIQS1lUHJ5TmpVdUp4el9jTU9DNV9xTmdYTlU0enRCT0ZMUw?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTE5NdWxWbFdCcVBSS3RNaXFNOXBVOWpuMUoxdDNQLVNhV1dhSm5scDZ5MkZrdW9vUzJ4cFVZbGRleDVUcHN2UTBhWDZ5MlZDRG1ENzhXU0ZTcjhnMFBYd1RQU3NndUFjVGtBMEJoVGpPRVVKWF9oc3ZrUUZ5MFBMZw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
