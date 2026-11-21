# DIS Intelligence Report

- ticker: **DIS**
- Report as_of: **2026-11-20**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/DIS/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/DIS/key-statistics/
- AI analysis snapshot as_of: **2026-11-20**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-21T05:49:28.302085+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 1, 'ai': 13, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **12** exact headline/source/date matches; prior report **20261120T053808Z-e360129e/DIS** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 12 named publishers; 3 exact duplicates; 22 HTTPS source links; largest publisher share 45.45%; oldest publication 2026-11-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 117.9800 |
| Return 1D (%) | -1.8877 |
| Return 1W (%) | -0.8321 |
| Return 1M (%) | 5.6506 |
| Return YTD (%) | 4.4951 |
| Return 1Y (%) | 16.5418 |
| Annualized volatility (%) | 26.5130 |
| Beta vs SPY | 0.5365 |
| Max drawdown (%) | -20.2451 |
| Sharpe (rf=0) | 0.7117 |
| Downside deviation (rf=0, %) | 17.6548 |
| Sortino (rf=0) | 1.0689 |
| Historical VaR 95% (1D, %) | 2.3418 |
| Historical ES 95% (1D, %) | 3.3566 |
| Correlation vs SPY | 0.2893 |
| Tracking error vs SPY (%) | 26.2300 |
| P/E (trailing) | 20.96 |
| P/B | 1.83 |
| EV/EBITDA | 11.07 |
| Revenue growth (%) | 15.50 |
| Forward P/E (estimate) | 13.83 |
| Gross margin (%) | 38.02 |
| Operating margin (%) | 16.57 |
| Return on equity (%) | 9.13 |
| Free cash flow yield (%) | 3.70 |
| MA50 | 110.5866 |
| Close vs MA50 (%) | 6.6856 |
| MA200 | 103.6894 |
| Close vs MA200 (%) | 13.7821 |
| RSI (14, Wilder) | 56.4230 |
| MACD (12,26) | 2.6793 |
| MACD signal (9) | 2.7557 |
| MACD histogram | -0.0764 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'DIS': 287, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 117.9800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.8877 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.8321 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 5.6506 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 4.4951 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 16.5418 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 26.5130 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 17.6548 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.0689 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.3418 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.3566 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2893 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.2300 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5365 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -20.2451 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.7117 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 13.8335 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 38.0230 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 16.5650 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.1270 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 3.6977 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 20.9556 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 56.4230 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.0764 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 6.6856 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 13.7821 -> Clearly above the moving-average trend level.

## TAILWINDS

### Walt Disney (DIS) Beats Q4 Earnings and Revenue Estimates
- Summary: Walt Disney (DIS) Beats Q4 Earnings and Revenue Estimates
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxQZ2hDaXFGQUsyQkpHOUJ3UWRLRXNxWWdSdmljN0pFOEZxNFZpNzNjSW94bjRwSmFMOHRJSUdqR3RodDBodl9tUFo0Wl9RVVhrVGsyVTdkbHV5alZfeERRdjhRTHhCVkxrbXVWOUFweGpCbGFMeTNNWGtsUDhIeEN1eG14bkF0ME5yTXo2SmtxdWRzNVU?oc=5>

### Disney, Target Among A Dozen Top Growth Stocks To Watch
- Summary: Analyst highlights Disney as a top growth stock, suggesting potential upside.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPVHVyMFJ1NU9GMW16RDVralJfUjVMRF9RSEdtUGt0Qk5EcXpkdzRJdWJfb3BYeXpoRGRUcVJycGd0ZWxZdUkxNnRmSjNOdzR1bmZ2Ymt3Sk9WWVBBcU1UbTloX0NjSmRLcnFpSlNndXBvWWZkQlpwMjZCXzIxbDFSOEJLb0xUWUFPUXpaQW03RzE3VUE0?oc=5>

### Walt Disney (DIS) Says Its In House AI Cuts Film Compute Costs 30%
- Summary: Disney claims AI reduces film compute costs by 30%.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOdmNST0kxV1dNQzBPWWgwLXdtMDQxQWxidWx1SjROaW85N0VpNjVST1kxb21FSHJ0aG0tQWFlQTN5V2w0Q3pZT3JhT0NzTnZmY0xiUDlpSVh2V2tDZGRTamMxQXU3Q0tUcGJ2VzdSTHNyczcxbk9NYUd4eG1RMmlSRG9mQnpxYUFyZml0YlllVjFOSVdG?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Disney (DIS) Stock Looks Fully Priced Following Q4 Earnings Beat
- Summary: Disney’s Q4 earnings beat suggests stock is fully priced, indicating potential short‑term upside.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOQkZvSUplV09USFNrSTY5N05ROUhsRmFmREhnM0NtVjNrclE4ODJibkV3dTU3SDEtaXZESjBUZU5PUVVCd1JBVk4zeGRBbzI5azAtLVc1dmVxZXdRdkc0X3hsTV96ZGpOMlEtSW5YQTZ1ZHRyRGMxTG5tMk5vRjFQMlg0eThCUm5wbGIwSlVxcm1Ea1gycDR5Wg?oc=5>

### Disney (DIS) Stock Slips As Q4 Earnings Contrast Margin Compression
- Summary: Margin compression in Q4 earnings leads to a stock decline.
- Date: 2026-11-18 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOZ2VGTzJFbDNmLV9HcDNCekJ4ODh6Q0ZVaXZENUNtR2o5Sm5BamdyQnhJZlpfWG9HeWxCMmp3TlFmQnI4TkZCS0pXVDJqdGlXN2cxSnNidnI4aklkYUo0XzB1MjhhX1M1YmhBYlQ1ckhCd1BmaDIwc3RJYlhuWmZNd3BseV9QYWN3dS1nMURMS0tyRGFo?oc=5>

### The Walt Disney Company Q4 2026 Earnings Call Summary
- Summary: Summarizes Disney’s Q4 2026 earnings call, highlighting key financial metrics and management commentary.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQQWRXWEl0Nk5obGhZeU1nTkNmaXR0aTFsMk9LN29ZMHg1ajRxNmZpTUFUM1paemxlY3o5c3dmSF9KNXlZTVZ4YUo5ZHdXbktyVzZsX0hPdk52cXVZWUI3ejBKa3FiN0FSSnB1OXhQTkxPb3JtcVhWNnB5RlY1LWVrOWxURWZsc0Eyai1Seks1Ykt4cXIwQ0xz?oc=5>

### Earnings Beat Might Change The Bull Case For Disney Stock (DIS)
- Summary: Disney's earnings beat could alter bullish outlook.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxOVXJlTVp4ZkxpWXdlSXNoTjZIdWZMbVEtVFFwT3VTdnVham41Ylh4Qk1oTVFrWGRXV3BZbzdneVpud3RqQURhX0FSRkJkZWI5LXY1U1M5SVY3ZkdGdVRjMTRiU25JYlhjQkd3cURHckt6QkNDU0hxWk8weW9YMkR5Nl9wYkk2aU0?oc=5>

### Disney (DIS) Reports Q4 Earnings: What Key Metrics Have to Say
- Summary: Details Disney’s Q4 earnings results and key performance indicators, informing investor decisions.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQa1Rvc2FwcklkT2VTcGs0U0xvVGMxOGI1OUIwb21wWmxVX3BqNWVzVDdnYjFMaTJIUTJEWWF1YWpRYWJvSVJfV04zNlVFNW1GdE1IbDdMajVWbXdGUlVDNGNJX1Q4cXdrNW4zTjN5OWg3Zk1BcS1CY25pbDJRZXROWGh3dFl5QTJwRFNkUDlXNFBseElvM1ZjTkJKUQ?oc=5>

### Walt Disney Co Stock (DIS) Moved Up by 3.24% on Nov 18: Drivers Behind the Movement
- Summary: Positive market movement driven by recent catalysts.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxPWjliTFhvcTNZbk81UmJub3JEOGJrbllZbUpoNmxaZHNOWm5tZ2FHNmlaZVZDM3ZOWFl5WDZTLVlyZHREaWZscC1IcklhR05pUktfYnRtM3JCcEhiZnJKejlycVoweUVCZEN6eUIyVzVfSnE4N2JXeERJZUd4YU5tSExxZzhud1JpcFE?oc=5>

### Disney Bets On Streaming And Content To Drive FY27 Growth — Raises Dividend, Targets $9B Buyback
- Summary: Disney raises dividend and plans a $9B buyback to boost FY27 growth via streaming and content.
- Date: 2026-11-17 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQQkt5anZTOFhFdm1tamxybjltWmF4Wk1GQkJtMlAxcWRhWE0yTkNtbjFLVlM3ZVNGdUkwMVhueFZTT0hXWU81Y3BneVM2TkFiUUlDNWRQUkJYSnk0eS1XYkI3RlJqMmdPVUY4VGRpNGc2TU5sTkY4dGJTb29XbXVKalM0OXcyRUVwenFtZUFPUjRvTmRrVjY0cDZ4akg5X181ejEwTGV3?oc=5>

### Disney Just Boosted Its Dividend by 33%. That Gives DIS Stock Investors a Real Reason to Stick Around.
- Summary: Disney increased dividend by 33%.
- Date: 2026-11-20 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi2wFBVV95cUxPSlowejN5VDB0OWxkUnJIMmhHclNmWWNaM3M5SE9FTFJHb09JYnRiQjNZSWxha3JrUUw4SFQ3UXhJQkhBbDJMYkg1dEw2Ym1IdG1tZDIwTWZicVhfLW0zQlVzanVGaUppNm54SlphanNyZ3ZEanhPQ0hhc2Y2Q0lQWGFlUVgtZEhPOXB5ODQ4ejI2QlV3TktSZFZZdVFGV1ZnaURiSU1HdklOc0tpYjBVb1Y0aUV2cjhOeE9SU0R2Zi13czNYemVkSFI3RW0zWnliYUR3MjFJYmp5QUk?oc=5>

### Disney Stock Hits New Highs After Strong Q4 Earnings: Time to Buy DIS?
- Summary: DIS shares rise after strong Q4 earnings.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNMy1vczBlNUd2RGtCVlBzVl9qYUs4Ty1ubk1WTFVVRjBHUFRfTDJKZU9LWVdVS3BPU3phTEV6cVhKTlpJQWtPdE9mV180VXRiSlRhVEd4YlUtVURScF9sOFFmSllsaTlBTGQ0aG0yNHY3c1lFb2tqVkxEQ1M3c2pmZGdxWUtPZ3RwcEd4UzhValc2ODlYZUNJbHd1MA?oc=5>

### Disney (DIS) executive Horacio Gutierrez sold 2,568 shares at $120 each under a preset trading plan.
- Summary: Executive sold shares under preset plan, indicating routine insider trading activity.
- Date: 2026-11-20 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxPbERTMXZUODB4RzE0UjFrc2EtaGx6ZHFjeGRZeGxJWnAwUzgwWFc1V3M0eG9MQzhnQ0tQZzlwQU4zRnh3d0h3Q051QWlwX3BhUzdXcTBkbVRpOG9vdTF0TURPZnFHOWFoS2J0M202R3JmOFZEWlQ3NkxHejlaaTJFMWFmLWx2R1huYm01T2x1NFNYTElGQ3pXNjN2QkVOa2NYZnMtR3IyTWtJTEk?oc=5>

### Robert Iger sold Walt Disney (DIS) shares the same day he exercised options at $105.21 a share.
- Summary: CEO sold shares after exercising options, routine insider transaction.
- Date: 2026-11-20 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxQUnJzak9ramRVeGNRMnhWX2IzNXRvM0xqY1NxRndwQ3RYMHViR1lPYzd6LXhBM0J3a0djTnJsVkRPeEEwUGRSSXlrUUw5eWtLTXZaWFJrTjVHZUttTnlndGhRVEVZUFVnT2dkaDl6UTlTa1BIV2NVWEZWbXc5bWVCR1FYRDVQYTFPOGZWaUR2OThaWldLNkNFMGRXNVNQblk0OHdvQXRMUDJpc00?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **DIS** | **20.96** | **1.83** | **11.07** | **15.50** | **201,513,353,216.00 USD** | **16.54** |
| NFLX | 16.88 | 7.95 | 15.18 | 11.80 | 232,951,873,536.00 USD | -46.31 |
| WBD | N/A | 2.36 | 13.79 | -11.20 | 77,595,885,568.00 USD | N/A |
| PSKY | N/A | 0.93 | 7.95 | 0.90 | 10,992,190,464.00 USD | N/A |

Peers fetched as_of: 2026-11-20; DIS reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-17
- Next expected earnings: 2027-02-01 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-20

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-11-17
- Revenue (latest available single quarter): 25,248,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 2,638,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1744489/000174448926000066/dis-20261003.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMikwFBVV95cUxQZ2hDaXFGQUsyQkpHOUJ3UWRLRXNxWWdSdmljN0pFOEZxNFZpNzNjSW94bjRwSmFMOHRJSUdqR3RodDBodl9tUFo0Wl9RVVhrVGsyVTdkbHV5alZfeERRdjhRTHhCVkxrbXVWOUFweGpCbGFMeTNNWGtsUDhIeEN1eG14bkF0ME5yTXo2SmtxdWRzNVU?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPVHVyMFJ1NU9GMW16RDVralJfUjVMRF9RSEdtUGt0Qk5EcXpkdzRJdWJfb3BYeXpoRGRUcVJycGd0ZWxZdUkxNnRmSjNOdzR1bmZ2Ymt3Sk9WWVBBcU1UbTloX0NjSmRLcnFpSlNndXBvWWZkQlpwMjZCXzIxbDFSOEJLb0xUWUFPUXpaQW03RzE3VUE0?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOdmNST0kxV1dNQzBPWWgwLXdtMDQxQWxidWx1SjROaW85N0VpNjVST1kxb21FSHJ0aG0tQWFlQTN5V2w0Q3pZT3JhT0NzTnZmY0xiUDlpSVh2V2tDZGRTamMxQXU3Q0tUcGJ2VzdSTHNyczcxbk9NYUd4eG1RMmlSRG9mQnpxYUFyZml0YlllVjFOSVdG?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOQkZvSUplV09USFNrSTY5N05ROUhsRmFmREhnM0NtVjNrclE4ODJibkV3dTU3SDEtaXZESjBUZU5PUVVCd1JBVk4zeGRBbzI5azAtLVc1dmVxZXdRdkc0X3hsTV96ZGpOMlEtSW5YQTZ1ZHRyRGMxTG5tMk5vRjFQMlg0eThCUm5wbGIwSlVxcm1Ea1gycDR5Wg?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOZ2VGTzJFbDNmLV9HcDNCekJ4ODh6Q0ZVaXZENUNtR2o5Sm5BamdyQnhJZlpfWG9HeWxCMmp3TlFmQnI4TkZCS0pXVDJqdGlXN2cxSnNidnI4aklkYUo0XzB1MjhhX1M1YmhBYlQ1ckhCd1BmaDIwc3RJYlhuWmZNd3BseV9QYWN3dS1nMURMS0tyRGFo?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQQWRXWEl0Nk5obGhZeU1nTkNmaXR0aTFsMk9LN29ZMHg1ajRxNmZpTUFUM1paemxlY3o5c3dmSF9KNXlZTVZ4YUo5ZHdXbktyVzZsX0hPdk52cXVZWUI3ejBKa3FiN0FSSnB1OXhQTkxPb3JtcVhWNnB5RlY1LWVrOWxURWZsc0Eyai1Seks1Ykt4cXIwQ0xz?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxOVXJlTVp4ZkxpWXdlSXNoTjZIdWZMbVEtVFFwT3VTdnVham41Ylh4Qk1oTVFrWGRXV3BZbzdneVpud3RqQURhX0FSRkJkZWI5LXY1U1M5SVY3ZkdGdVRjMTRiU25JYlhjQkd3cURHckt6QkNDU0hxWk8weW9YMkR5Nl9wYkk2aU0?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQa1Rvc2FwcklkT2VTcGs0U0xvVGMxOGI1OUIwb21wWmxVX3BqNWVzVDdnYjFMaTJIUTJEWWF1YWpRYWJvSVJfV04zNlVFNW1GdE1IbDdMajVWbXdGUlVDNGNJX1Q4cXdrNW4zTjN5OWg3Zk1BcS1CY25pbDJRZXROWGh3dFl5QTJwRFNkUDlXNFBseElvM1ZjTkJKUQ?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxPWjliTFhvcTNZbk81UmJub3JEOGJrbllZbUpoNmxaZHNOWm5tZ2FHNmlaZVZDM3ZOWFl5WDZTLVlyZHREaWZscC1IcklhR05pUktfYnRtM3JCcEhiZnJKejlycVoweUVCZEN6eUIyVzVfSnE4N2JXeERJZUd4YU5tSExxZzhud1JpcFE?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQQkt5anZTOFhFdm1tamxybjltWmF4Wk1GQkJtMlAxcWRhWE0yTkNtbjFLVlM3ZVNGdUkwMVhueFZTT0hXWU81Y3BneVM2TkFiUUlDNWRQUkJYSnk0eS1XYkI3RlJqMmdPVUY4VGRpNGc2TU5sTkY4dGJTb29XbXVKalM0OXcyRUVwenFtZUFPUjRvTmRrVjY0cDZ4akg5X181ejEwTGV3?oc=5
- https://news.google.com/rss/articles/CBMi2wFBVV95cUxPSlowejN5VDB0OWxkUnJIMmhHclNmWWNaM3M5SE9FTFJHb09JYnRiQjNZSWxha3JrUUw4SFQ3UXhJQkhBbDJMYkg1dEw2Ym1IdG1tZDIwTWZicVhfLW0zQlVzanVGaUppNm54SlphanNyZ3ZEanhPQ0hhc2Y2Q0lQWGFlUVgtZEhPOXB5ODQ4ejI2QlV3TktSZFZZdVFGV1ZnaURiSU1HdklOc0tpYjBVb1Y0aUV2cjhOeE9SU0R2Zi13czNYemVkSFI3RW0zWnliYUR3MjFJYmp5QUk?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNMy1vczBlNUd2RGtCVlBzVl9qYUs4Ty1ubk1WTFVVRjBHUFRfTDJKZU9LWVdVS3BPU3phTEV6cVhKTlpJQWtPdE9mV180VXRiSlRhVEd4YlUtVURScF9sOFFmSllsaTlBTGQ0aG0yNHY3c1lFb2tqVkxEQ1M3c2pmZGdxWUtPZ3RwcEd4UzhValc2ODlYZUNJbHd1MA?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxPZ3l2LUo4Uy1TVnYwa28zNEpVb0tCcnRoM1FlQ3VQMW5IQnNsLUhKVlhiUWxSbm1wVnNpV3hqMGY4SjdackliOWs5dXdfZ1c4Q1RNN3RtNVl1WTU4WFRvYkhaUmVQdzI5NElrb3M0S09oYm1TYm8zVEJmUmR0Mm44TnUxYllzVUNfNG5hUEVaSTlWRVNuSEZnRGthRUJDeTBIMGhPdmNCVVV5SVp0VVE?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxPbERTMXZUODB4RzE0UjFrc2EtaGx6ZHFjeGRZeGxJWnAwUzgwWFc1V3M0eG9MQzhnQ0tQZzlwQU4zRnh3d0h3Q051QWlwX3BhUzdXcTBkbVRpOG9vdTF0TURPZnFHOWFoS2J0M202R3JmOFZEWlQ3NkxHejlaaTJFMWFmLWx2R1huYm01T2x1NFNYTElGQ3pXNjN2QkVOa2NYZnMtR3IyTWtJTEk?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxQUnJzak9ramRVeGNRMnhWX2IzNXRvM0xqY1NxRndwQ3RYMHViR1lPYzd6LXhBM0J3a0djTnJsVkRPeEEwUGRSSXlrUUw5eWtLTXZaWFJrTjVHZUttTnlndGhRVEVZUFVnT2dkaDl6UTlTa1BIV2NVWEZWbXc5bWVCR1FYRDVQYTFPOGZWaUR2OThaWldLNkNFMGRXNVNQblk0OHdvQXRMUDJpc00?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
