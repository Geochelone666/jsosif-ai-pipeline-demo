# NVO Intelligence Report

- ticker: **NVO**
- Report as_of: **2026-11-13**
- Market data as_of: **2026-11-13**
- Quant sources: https://finance.yahoo.com/quote/NVO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVO/key-statistics/
- AI analysis snapshot as_of: **2026-11-13**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-14T05:03:56.475651+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 20, 'rule': 2, 'ai': 12, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **14** exact headline/source/date matches; prior report **20261113T045636Z-34122c9a/NVO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'negative_sentiment_in_tailwinds': 1}
- RSS source audit (metadata only, not article fact-checking): 20 unique headlines; 11 named publishers; 0 exact duplicates; 20 HTTPS source links; largest publisher share 15.0%; oldest publication 2026-11-08

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 41.6300 |
| Return 1D (%) | 2.4108 |
| Return 1W (%) | 3.2746 |
| Return 1M (%) | 9.3799 |
| Return YTD (%) | -14.0954 |
| Return 1Y (%) | -11.0898 |
| Annualized volatility (%) | 45.3764 |
| Beta vs SPY | 0.9470 |
| Max drawdown (%) | -43.6699 |
| Sharpe (rf=0) | -0.0286 |
| Downside deviation (rf=0, %) | 33.9347 |
| Sortino (rf=0) | -0.0382 |
| Historical VaR 95% (1D, %) | 3.1060 |
| Historical ES 95% (1D, %) | 7.1674 |
| Correlation vs SPY | 0.2845 |
| Tracking error vs SPY (%) | 43.5067 |
| P/E (trailing) | 10.25 |
| P/B | 5.61 |
| EV/EBITDA | 1.50 |
| Revenue growth (%) | 5.60 |
| Forward P/E (estimate) | 12.10 |
| Gross margin (%) | 83.33 |
| Operating margin (%) | 50.78 |
| Return on equity (%) | 58.38 |
| Free cash flow yield (%) | N/A |
| MA50 | 40.0868 |
| Close vs MA50 (%) | 3.8496 |
| MA200 | 42.5096 |
| Close vs MA200 (%) | -2.0692 |
| RSI (14, Wilder) | 58.0883 |
| MACD (12,26) | 0.3901 |
| MACD signal (9) | 0.1548 |
| MACD histogram | 0.2353 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVO': 282, 'SPY': 282}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 41.6300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.4108 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 3.2746 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 9.3799 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -14.0954 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -11.0898 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 45.3764 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 33.9347 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.0382 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.1060 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 7.1674 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2845 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 43.5067 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.9470 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -43.6699 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.0286 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 12.1038 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 83.3330 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 50.7790 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 58.3840 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 10.2537 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 58.0883 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.2353 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 3.8496 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -2.0692 -> Slightly below the moving-average trend level.

## TAILWINDS

### Novo Nordisk (NYSE: NVO) Shares Jump 6% After Strong Q3 Earnings Driven By Oral Weight-Loss Pill
- Summary: Novo Nordisk (NYSE: NVO) Shares Jump 6% After Strong Q3 Earnings Driven By Oral Weight-Loss Pill
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxPczBwdmNBSWNjTmJjZ3lPT0k3UEN5alU4TjZ0LVRlb05XZnBGUWhodk1Cd3NGOTJtaERCdDQ3N2dmYnV3RjVYYnlrRDJ5c0hxNktYenpFeGl5SlB3dmpkR3NWR1JNMDl3UjdwUnBZalZlaVJNeDhmUS0xOVFNMGlDak1Ka0p4LV85UTVsa0U0eGJOdngyX0dqcl80VXh6clZHNVA2NTE1OTlGWE9QMUdKeFVYU3BmMEhJOUlCNUtBblU3RHh5RXplNHBVcmFXWW9Fb0FRaVI4cVA?oc=5>

### Novo Nordisk Stock: Better Than It Looks, But Not A Buy Yet (NYSE:NVO)
- Summary: Positive outlook but cautious; stock may rise.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOWjJnYk52YWV1VW1CMWJiRGNOZWpHNDlQVHdtb2g4QWRVRy1FbUN0X2RTMVRVSUJfZHVkODRiZVdPX3VadzB5MGNYeWpyYlVOQmFBNS1QOTNURkZwaHZCYUtVMm4yOHhxSENfWXpBcFF0cjNDQnk1VGpsWXdVQXJDcS1mNGVkT2ttNmRoVld1RU8tTVA2Nmg0?oc=5>

### JPMorgan Predicted Strong Wegovy Pill Sales (and Was Right). Is Novo Nordisk Stock a Buy Now?
- Summary: Analyst forecast confirms strong sales; buy signal.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQeEJzRlF4dndGY3Y3SzZmWlpMQzFqcTc1R1RFeVduRGZ3eG51SFZmRG9TNjZadU1IRXBjX0F3Z0FPYWR6N1JHZlpUazZFZUxnZExDRVlaenVOQ1BHelM5X3o3Zmk4ZWx4NU04ekhlZWhRSTNNT3praVVBcVJfdE9SQldvc2hPV2xlX3Ryalg4TENOcEtCc0l4ZA?oc=5>

### Novo Nordisk's (NYSE: NVO) 70% Stock Decline Creates Value Case As Wegovy Pill Crosses 8 Million Prescriptions
- Summary: Stock drop highlights value; prescriptions strong.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi6gFBVV95cUxNMFV3M2lPNjBpdHBrZC1UZVVIak9rUF9OZzhydVlSSG1vd2twblVLSXc2aU05M3E5dzJ1WHp2VVBXM2RLeGVZWm1jelMtOFVEemlfbC1hdzBwTWNOb3ZRNm5JQWVDR1RQMWxEaDhDZFZaOWlsTVBtNzllV2hyb0hOazRTOWVrTkhZMlkxRlVDZ1dfUlV1OWMxdm1SamxTVFlnc09jZDRYNEZhallINjJQTm5tNU0wOGgzdkR2MmU4ZUlCdjQya0s3dTV3YlB0OE5HOGNOM0xRMGdDY0VpSUtvdjhQUTExTXRfM1E?oc=5>

### Hims & Hers Climbs 6% Despite Five States Joining FTC Suit; Eli Lilly Dips, Novo Nordisk Holds Steady
- Summary: Novo Nordisk holds steady amid market fluctuations.
- Date: 2026-11-11 | Impact: low | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxNcVBlai1aLXh1d0pyRFBLQ1RkUHdxYUE2NEtST01QS2FQNjFvQzlKNk4tN1p3YllqOGhtLWtadzJFOEU3QnRJaUkzdkc4WDh5a1FNX0w0d0xteHotN1ZNUWpaVjJpWXVyZXlCWUZuTXJQTmFmaEtwNHdhblJaUnAxZnFmQTBlcGg4a3Fkd2tmQUEwZVhTaVVzMjkxaEJyQ1ZfVU5WRS1QWlJKdGtvOC1KdzVqQmdBVDJIZ0dWSzRpVGNOWXhUeDEzTVl2aFNQcW84M2RSVERCTQ?oc=5>

### European ADR Selloff Hits Broad Range Of Stocks Tuesday, With Novo Nordisk (NYSE: NVO) And Eni (NYSE: E) Among Hardest Hit
- Summary: Novo Nordisk impacted by European ADR selloff.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi9wFBVV95cUxPYXNRLUU5enFpaXBhZTMyVGdPdWh6eWwyYU1HcVlwQTh5Q1EwMklpc2dhR0psbEdfNlo1OXNKM0kzOEdUcXpXX3ExN0w4SXNhTi0wU1JoNVJKelQzTE81S3JleS1yMndIRGNiUkFxcjdIZWVsSEZqTDdLTnNqTUhDU1JENC1EcEdmRndMeEY0Vk9IYlp4Sm1lOC1BVzRnem91c01mU2gxSDVZaWhUby1nTFZ2ZHB0c0kwZ2s2U3RCUDJMQ1lXbmJGSG1lNl9Cd014OUZ6OWFGWnZCM2ZsSEZLZEYwVVBNSmxSU3hzaUM3WnF0Z1h3Nkxr?oc=5>

### Novo Nordisk: Q3 Earnings Bust The Cannibalization Myth
- Summary: Q3 earnings show strong performance, disproving cannibalization concerns.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPOWdicklaV2NyS2RyQkc0allwR3ppLTlwQ3Z3a3Z0a2Q2aVF5ekl0Z1RZbnpWX3hCbDRjdGNRZFpkTGR4TS0yZHljZnZURUFWWmNMOUlrUFZGdFM2SXVLdVBOdWVyTXVLNFNxTm9GcUZaWVdGOG1vcllPeWh6VEJLM3Y5Znk4RXRXWVpqenpNVlRIMktZYnlja2F4cFA?oc=5>

### Novo Nordisk (NVO) Stock Price Prediction: Rally tests resistance after Novo raises outlook and Binance flows lean long
- Summary: Positive outlook lift and bullish Binance flows support rally.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQbmFVT3pvOVg1Y3dwaXI2cDd0bHpucExkYnZRY2NneUdOclpTczJ2QnUxOV9oWEpjblg1X0xuc2JDS0h0dnZyOWFhNEF6QkZfc1czSFVRc3dEVFNtSGl4NlMxeGVkT0Y0WXBrSlQ0R1I0MzBzVmZkUHF0aVM2R1R2MldqRFVIVnpMb1hwbnF4U3BOa1hwM2FlNXJKcnAxSEJz?oc=5>

### Novo Nordisk (NVO) Stock Price Prediction 2026, 2030, 2040-2060
- Summary: Long‑term price targets set for 2026–2060.
- Date: 2026-11-09 | Impact: medium | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiWkFVX3lxTE5mbUJYcVVhZnVIYmpiS3NFZGhfX1ppYUtIRXdsNC1hXy1sMFg0YjFFLW5DZmx3RGQ4d2JlVEZEYnluSDZjbHJBeEJBODQ2RHZpX25XLWc2ck5YUQ?oc=5>

## HEADWINDS

### Novo Nordisk hit by FDA warning on Ozempic: Can NVO avoid further decline?
- Summary: FDA warning risks further decline.
- Date: 2026-11-11 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxQOC1MYXFoRzRtTjFmSVRpTVdFVkF0T1d1Q3VRYnRWRE1mcUg1V3gxMjJYSnNYNGVVNFFLdVE3eEJ6RUxDTE4tZEg5WlI0c0ZSZW5FZnRabFZqLVdCTkY2LXlsbmczeXNQN3Y4UE9VS1VGckFmY1NvS2dHSUNYNkhHLTVTWXpCOGMtdlAyOTNpMno2dw?oc=5>

## CATALYSTS

### Novo Nordisk Reports DKK 11.8 Billion in Share Buybacks
- Summary: Novo Nordisk Reports DKK 11.8 Billion in Share Buybacks
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxQTC1YVVFBWExGSWs2MVRkM2JuSHhQbFJFUDJWT1Nod2loMEZpdzVhT002MkJqdmJ3dmFxYW9UOTVENDNrRm94RUpDM210b0dnZERLVWR3MXhER2FmOFNSMnI0QjA5elAwbmVnVHpJMWotcFBPLUpLdldtUzRENnliQy1xUVRMSE1BbkpLMTlnOTkyRk4tSUpiX19NMDdRNURrT1ZjRWdFQXNIYzg?oc=5>

### Novo Nordisk: Valuations Are Blind To The Upside (NYSE:NVO)
- Summary: Analyst commentary on valuation outlook.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxQSWE0ekhNR3pzUHBMWjhIR3JwVG1QeThWWUxlSDU3dHEyY0xzLUIwTnZKR0FXTllJbDJJZk5HSzdBWUltZC1FWmJzR1ZGazZXTWJGQmRuSGJwcUJrakt5SXI4cU9FcV9ENUtZNElzUmtRNmNFa1RyX25JVkFPSHNMUHo1c2Z3eWRZQVJUMzRuT1hGUQ?oc=5>

### Novo Nordisk (NVO) Stock May Trade Below Fair Value Following Raised Outlook
- Summary: Novo Nordisk raised its outlook, potentially lowering stock valuation expectations.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxNYkxoWU04N0ZCbWVyM2V4S3RSRFhHNjZZdDBLbGJNb2UzbVhwTnBhdXNhbXMtZWZlUXAxZWpPZUQwUTI5RGF6QklMdGZlSlJ3Qi1TcjZZdmpkTHNIMTE5TEpkTzgxUHFWRy0wb0xMdmZjT21IS051eUpXQkFpTUw2QTJueGpNRnBabDYtbThNam1QeFVyMjVBeGpKS294MlRweTR3THF4TXR1Rm1OSFBXQVNLQ2RudE0ycHNQd242SGY3WXhLeTd6dVZTdG04aDgwSFJyNmptMGxNZ9IB3wFBVV95cUxPNlBZV0xOTnlqSnVzRnZfd0tNZ1UxS3RfNGUxWk1sdXdzVHJhampjT0dkUm02UGlqa0c2TTBwd1B4ZHdHZWJiX0xkZDVPZ29Gdzl4RDZ0RUNGTUJKUHJ6NVFEcXdvSk1Md2FOemg0YmYwa2NReVRJR2Jhckg1QXZvS0c1UjZnVFkyODVncGFibFVkbDFfSGJ3Y19ZQndveDQ5QzlKLWVNOFdNdjUwaVNRYld5NmV0ZE82R1h3RGRXRERmWHhPNXFHRVdnLTdDdjlEQlFhTEdYUHBpMmpOd0Q4?oc=5>

### Shares worth 11.8 billion Danish kroner have been bought back by Novo Nordisk since February.
- Summary: Novo Nordisk has repurchased shares totaling 11.8 bn DKK since February, signaling confidence in its valuation and supporting shareholder value.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxQbnhqS296YUpMMndQMm53NXRPMjRXNDZJOWIyN3BLZ001cE5jcDNfZTdRRlBLbkxOZGRPak9meDI1bWNhNVR5ZXNCRG5VeDNpOWY3MGVsOGRnVEdSVU9zVXRZUktZNGdidG9HY2VEa0Q3Z2VxVzFjcUVxLUJlVDNNYkNTSzJKdlIzNjd5aS1fREs?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVO** | **10.25** | **5.61** | **1.50** | **5.60** | **183,519,838,208.00 USD** | **-11.09** |
| LLY | 46.33 | 31.95 | 28.62 | 38.60 | 1,285,790,498,816.00 USD | 42.18 |
| ROG.SW | N/A | N/A | N/A | N/A | N/A unknown currency | N/A |
| SAN.PA | 24.96 | 1.44 | 8.08 | 15.70 | 104,950,816,768.00 EUR | 3.07 |

Peers fetched as_of: 2026-11-13; NVO reuses existing data (market data as_of: 2026-11-13); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-04
- Next expected earnings: 2027-02-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-13

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

- https://news.google.com/rss/articles/CBMi2AFBVV95cUxPczBwdmNBSWNjTmJjZ3lPT0k3UEN5alU4TjZ0LVRlb05XZnBGUWhodk1Cd3NGOTJtaERCdDQ3N2dmYnV3RjVYYnlrRDJ5c0hxNktYenpFeGl5SlB3dmpkR3NWR1JNMDl3UjdwUnBZalZlaVJNeDhmUS0xOVFNMGlDak1Ka0p4LV85UTVsa0U0eGJOdngyX0dqcl80VXh6clZHNVA2NTE1OTlGWE9QMUdKeFVYU3BmMEhJOUlCNUtBblU3RHh5RXplNHBVcmFXWW9Fb0FRaVI4cVA?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOWjJnYk52YWV1VW1CMWJiRGNOZWpHNDlQVHdtb2g4QWRVRy1FbUN0X2RTMVRVSUJfZHVkODRiZVdPX3VadzB5MGNYeWpyYlVOQmFBNS1QOTNURkZwaHZCYUtVMm4yOHhxSENfWXpBcFF0cjNDQnk1VGpsWXdVQXJDcS1mNGVkT2ttNmRoVld1RU8tTVA2Nmg0?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQeEJzRlF4dndGY3Y3SzZmWlpMQzFqcTc1R1RFeVduRGZ3eG51SFZmRG9TNjZadU1IRXBjX0F3Z0FPYWR6N1JHZlpUazZFZUxnZExDRVlaenVOQ1BHelM5X3o3Zmk4ZWx4NU04ekhlZWhRSTNNT3praVVBcVJfdE9SQldvc2hPV2xlX3Ryalg4TENOcEtCc0l4ZA?oc=5
- https://news.google.com/rss/articles/CBMi6gFBVV95cUxNMFV3M2lPNjBpdHBrZC1UZVVIak9rUF9OZzhydVlSSG1vd2twblVLSXc2aU05M3E5dzJ1WHp2VVBXM2RLeGVZWm1jelMtOFVEemlfbC1hdzBwTWNOb3ZRNm5JQWVDR1RQMWxEaDhDZFZaOWlsTVBtNzllV2hyb0hOazRTOWVrTkhZMlkxRlVDZ1dfUlV1OWMxdm1SamxTVFlnc09jZDRYNEZhallINjJQTm5tNU0wOGgzdkR2MmU4ZUlCdjQya0s3dTV3YlB0OE5HOGNOM0xRMGdDY0VpSUtvdjhQUTExTXRfM1E?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxNcVBlai1aLXh1d0pyRFBLQ1RkUHdxYUE2NEtST01QS2FQNjFvQzlKNk4tN1p3YllqOGhtLWtadzJFOEU3QnRJaUkzdkc4WDh5a1FNX0w0d0xteHotN1ZNUWpaVjJpWXVyZXlCWUZuTXJQTmFmaEtwNHdhblJaUnAxZnFmQTBlcGg4a3Fkd2tmQUEwZVhTaVVzMjkxaEJyQ1ZfVU5WRS1QWlJKdGtvOC1KdzVqQmdBVDJIZ0dWSzRpVGNOWXhUeDEzTVl2aFNQcW84M2RSVERCTQ?oc=5
- https://news.google.com/rss/articles/CBMi9wFBVV95cUxPYXNRLUU5enFpaXBhZTMyVGdPdWh6eWwyYU1HcVlwQTh5Q1EwMklpc2dhR0psbEdfNlo1OXNKM0kzOEdUcXpXX3ExN0w4SXNhTi0wU1JoNVJKelQzTE81S3JleS1yMndIRGNiUkFxcjdIZWVsSEZqTDdLTnNqTUhDU1JENC1EcEdmRndMeEY0Vk9IYlp4Sm1lOC1BVzRnem91c01mU2gxSDVZaWhUby1nTFZ2ZHB0c0kwZ2s2U3RCUDJMQ1lXbmJGSG1lNl9Cd014OUZ6OWFGWnZCM2ZsSEZLZEYwVVBNSmxSU3hzaUM3WnF0Z1h3Nkxr?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPOWdicklaV2NyS2RyQkc0allwR3ppLTlwQ3Z3a3Z0a2Q2aVF5ekl0Z1RZbnpWX3hCbDRjdGNRZFpkTGR4TS0yZHljZnZURUFWWmNMOUlrUFZGdFM2SXVLdVBOdWVyTXVLNFNxTm9GcUZaWVdGOG1vcllPeWh6VEJLM3Y5Znk4RXRXWVpqenpNVlRIMktZYnlja2F4cFA?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQbmFVT3pvOVg1Y3dwaXI2cDd0bHpucExkYnZRY2NneUdOclpTczJ2QnUxOV9oWEpjblg1X0xuc2JDS0h0dnZyOWFhNEF6QkZfc1czSFVRc3dEVFNtSGl4NlMxeGVkT0Y0WXBrSlQ0R1I0MzBzVmZkUHF0aVM2R1R2MldqRFVIVnpMb1hwbnF4U3BOa1hwM2FlNXJKcnAxSEJz?oc=5
- https://news.google.com/rss/articles/CBMiWkFVX3lxTE5mbUJYcVVhZnVIYmpiS3NFZGhfX1ppYUtIRXdsNC1hXy1sMFg0YjFFLW5DZmx3RGQ4d2JlVEZEYnluSDZjbHJBeEJBODQ2RHZpX25XLWc2ck5YUQ?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxQOC1MYXFoRzRtTjFmSVRpTVdFVkF0T1d1Q3VRYnRWRE1mcUg1V3gxMjJYSnNYNGVVNFFLdVE3eEJ6RUxDTE4tZEg5WlI0c0ZSZW5FZnRabFZqLVdCTkY2LXlsbmczeXNQN3Y4UE9VS1VGckFmY1NvS2dHSUNYNkhHLTVTWXpCOGMtdlAyOTNpMno2dw?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxQTC1YVVFBWExGSWs2MVRkM2JuSHhQbFJFUDJWT1Nod2loMEZpdzVhT002MkJqdmJ3dmFxYW9UOTVENDNrRm94RUpDM210b0dnZERLVWR3MXhER2FmOFNSMnI0QjA5elAwbmVnVHpJMWotcFBPLUpLdldtUzRENnliQy1xUVRMSE1BbkpLMTlnOTkyRk4tSUpiX19NMDdRNURrT1ZjRWdFQXNIYzg?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxQSWE0ekhNR3pzUHBMWjhIR3JwVG1QeThWWUxlSDU3dHEyY0xzLUIwTnZKR0FXTllJbDJJZk5HSzdBWUltZC1FWmJzR1ZGazZXTWJGQmRuSGJwcUJrakt5SXI4cU9FcV9ENUtZNElzUmtRNmNFa1RyX25JVkFPSHNMUHo1c2Z3eWRZQVJUMzRuT1hGUQ?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxNYkxoWU04N0ZCbWVyM2V4S3RSRFhHNjZZdDBLbGJNb2UzbVhwTnBhdXNhbXMtZWZlUXAxZWpPZUQwUTI5RGF6QklMdGZlSlJ3Qi1TcjZZdmpkTHNIMTE5TEpkTzgxUHFWRy0wb0xMdmZjT21IS051eUpXQkFpTUw2QTJueGpNRnBabDYtbThNam1QeFVyMjVBeGpKS294MlRweTR3THF4TXR1Rm1OSFBXQVNLQ2RudE0ycHNQd242SGY3WXhLeTd6dVZTdG04aDgwSFJyNmptMGxNZ9IB3wFBVV95cUxPNlBZV0xOTnlqSnVzRnZfd0tNZ1UxS3RfNGUxWk1sdXdzVHJhampjT0dkUm02UGlqa0c2TTBwd1B4ZHdHZWJiX0xkZDVPZ29Gdzl4RDZ0RUNGTUJKUHJ6NVFEcXdvSk1Md2FOemg0YmYwa2NReVRJR2Jhckg1QXZvS0c1UjZnVFkyODVncGFibFVkbDFfSGJ3Y19ZQndveDQ5QzlKLWVNOFdNdjUwaVNRYld5NmV0ZE82R1h3RGRXRERmWHhPNXFHRVdnLTdDdjlEQlFhTEdYUHBpMmpOd0Q4?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxQbnhqS296YUpMMndQMm53NXRPMjRXNDZJOWIyN3BLZ001cE5jcDNfZTdRRlBLbkxOZGRPak9meDI1bWNhNVR5ZXNCRG5VeDNpOWY3MGVsOGRnVEdSVU9zVXRZUktZNGdidG9HY2VEa0Q3Z2VxVzFjcUVxLUJlVDNNYkNTSzJKdlIzNjd5aS1fREs?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
