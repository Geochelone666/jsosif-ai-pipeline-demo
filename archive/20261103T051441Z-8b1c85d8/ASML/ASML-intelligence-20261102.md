# ASML Intelligence Report

- ticker: **ASML**
- Report as_of: **2026-11-02**
- Market data as_of: **2026-11-02**
- Quant sources: https://finance.yahoo.com/quote/ASML/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ASML/key-statistics/
- AI analysis snapshot as_of: **2026-11-02**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-03T05:32:48.287333+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 8, 'ai': 6, 'unknown': 0, 'irrelevant': 11})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261102T041627Z-c84a7052/ASML** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **3**; {'low_uncalibrated_model_confidence': 2, 'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 9 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 52.0%; oldest publication 2026-10-29

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 1526.1400 |
| Return 1D (%) | -2.5391 |
| Return 1W (%) | -3.9441 |
| Return 1M (%) | -18.1628 |
| Return YTD (%) | 43.5229 |
| Return 1Y (%) | 44.9633 |
| Annualized volatility (%) | 47.2392 |
| Beta vs SPY | 2.3159 |
| Max drawdown (%) | -23.0874 |
| Sharpe (rf=0) | 1.0124 |
| Downside deviation (rf=0, %) | 31.5926 |
| Sortino (rf=0) | 1.5139 |
| Historical VaR 95% (1D, %) | 4.6584 |
| Historical ES 95% (1D, %) | 6.1344 |
| Correlation vs SPY | 0.6286 |
| Tracking error vs SPY (%) | 40.4287 |
| P/E (trailing) | 37.55 |
| P/B | 1310.42 |
| EV/EBITDA | 2006.71 |
| Revenue growth (%) | 55.20 |
| Forward P/E (estimate) | 24.16 |
| Gross margin (%) | 54.34 |
| Operating margin (%) | 44.36 |
| Return on equity (%) | 65.64 |
| Free cash flow yield (%) | N/A |
| MA50 | 1697.9280 |
| Close vs MA50 (%) | -10.1175 |
| MA200 | 1593.6623 |
| Close vs MA200 (%) | -4.2369 |
| RSI (14, Wilder) | 35.6977 |
| MACD (12,26) | -40.3513 |
| MACD signal (9) | -30.7383 |
| MACD histogram | -9.6130 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ASML': 273, 'SPY': 273}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 1526.1400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.5391 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -3.9441 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -18.1628 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 43.5229 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 44.9633 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 47.2392 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 31.5926 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.5139 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.6584 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.1344 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6286 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 40.4287 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.3159 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -23.0874 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.0124 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 24.1642 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.3370 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 44.3560 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 65.6360 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 37.5527 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 35.6977 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -9.6130 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -10.1175 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -4.2369 -> Slightly below the moving-average trend level.

## TAILWINDS

### ASML's Raised Guidance Meets a Market That Wants Proof, Not Promises
- Summary: ASML's Raised Guidance Meets a Market That Wants Proof, Not Promises
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxNbmJCNXdkMUR5U2pMTmE2SW93WEJ0VGN2VFduWjFPbUI1elZnaUlCcmMxWFk1R0xvM0p6TkMzdmthaXk1ZGZ1NFV4ZjdrcnpmZDNtRkhteThmamtUQktXQVAxdllzaF9SQ0RGaHVVWnY3VGMtX0VwSXFkeUUydzJpUXpoT1ZqX2l5ZTlua3BqOG1YOVo3LXpLMExTeTBKb1VxMlUtTU8zam41NWFaaTdIRVRfeERMeUVqRDlfdnFHRVYxbzNWZl9hU25kbDBBUmpOd0VsOG1B?oc=5>

### ASML Keeps Buying Back Stock While Its Order Book Waits for Answers
- Summary: ASML continues stock buybacks amid pending order book questions, signaling confidence and supporting share price.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxOVHBuVFpCdEQ1QUdraDlKU0lBQXozSndNb091NVBPNlhPSVByNW1EaW1sUnlyQVFQSUJIelFfQW5QaHpkSFZOeFltckJ6NWFvV0JZRUZaenNrRjJ2djNUREIxUVJ6OHVVeDdIU1MwdDk1WWlVUmpnVGlCYW9NYUFzYlJOUFpJN19aeHFyeS1SQlNhV0JoVVFuMkZGUXJneTJsLWVkV3lwTWlWUy1GOGd0dE85NUgyOEc0YXVQOTA5bmY4UFgya2hjelNvMnpWb0JHUFBUOGFB?oc=5>

## HEADWINDS

### ASML Holding (ASML) Ties Pay To Morale Following Pullback But Is The Value Already Priced In
- Summary: Compensation linked to morale after a pullback may dampen investor sentiment, raising concerns about internal cost management.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxOU0lBZDc0MC1ZaWZWeVQ2NEZyS0xfMmI0OTlFSHp3aTcybXo4UGJabDZHRTZpSk04dFdsZkJWZWVZdV9MT2hLUVk3YkI1RXBWUXRNSW51WWFpcWNNdHJ6cndIUHN3anhseEppZDFjUmdTTDlGQmRqZnJyYWRON0ZXeUFaWGl3VEdnTUpFdGE3S01Ib3ZUcWZGT1dIandHUnI0ZmdiWXViWkJPbEVzV3FlM1VENW9Lc18yeDNvNy1oNmlTSzA5c0VSZGRCc3p5eW9YWEHSAdcBQVVfeXFMUDdnQTdKaEJPbFlUTm4wSXRiWEM1cWVBWFoxblVNTTlDeERlZDNmbHBwU2VyWVNWWXQ0cThQcGpzdGdHNW5qdGhUOGN3VEZBRDRIWUJ5ckhpUTJmSC1weV9nZVhlZlpoVnB4R2VQUnBWNDFMS2hNakdtVy0tcGxDYmZDbWtXQWsyNDFJTWQtR3VQcFNoNXF2cmdNWDZMLWVyeVZLR1pOcXcwLXlINE5teXg1SUxjNExDQU9Nb0xValRBMkw3Uzd5RFc1Ml9DSTZOSG5hNGczX1k?oc=5>

### ASML's Friday Swoon Traces Back to Amazon and Intel, Not Its Own Books
- Summary: Share price rally attributed to external tech giants rather than ASML's fundamentals, suggesting limited intrinsic value.
- Date: 2026-11-02 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxNbk9ObjF3b1haR3JJNVNXeGRqYjNhVUtOeXhwTUdvNVpCQzRILWJFWm5aMVA2V3pXa1RjdEE0RU1hSDNsYWJORnJFS1BqWWN5bUtaRjcxcE5tTnVZU0sxaXNJdTJmYkJwMEhyaEFnLTRWVEUxXzg4a0dSNWtocVd0VGtCWVFqRlVQbTZNbHFhTV9LVFVQLUNNaFNXQ1lwTDBnSkZhaWhCYWliNFZucGs1MTc4SE5uVEV1RjRJYngzRFplMENpeVlRNHpNX0hVaFJxZ3lLa2xOQXo?oc=5>

### ASML's Books and Its Share Price Are Telling Two Different Stories
- Summary: Disparity between financial books and market valuation signals potential overvaluation or market mispricing.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.65
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxNMVBCVW1ibVBUSzl1cS11MVpTVzFyT2VoSjZrQWhPNXZjUzJzNEdEY2hELXVjcDkzMTA0WG9jQ1NqQW0tYS05V1hOa2NSN2hydnZFamMzZGc5aDkyNGJuNlB3QVQycm5uQVhKVTctTFI4Yk5sd056aEViRThJNnRJVzB6V2k3MGsyUDJ0RWdQYWRZbTFEdjVfaENIV1BDMzR5TVRORUJxbTVVTVlxWElDMGY1a3RaMHlMYVBlbC12ajNIYmozT2E1Wkg5UlBiT2JsTEdZUQ?oc=5>

## CATALYSTS

### ASML (NasdaqGS:ASML) Stock Looks Fairly Valued On Its 149% Run
- Summary: ASML (NasdaqGS:ASML) Stock Looks Fairly Valued On Its 149% Run
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNcU1hVi13RktuT1dDNXhuM2duR3g2RXEzQUhZYklTR0QybDZ6bmRZY05rTUxoakdTaDNjY1ZlMHJrdGl0dzQtaG43RkxwMmRwVEttdFoyWEZGRVU1OU1BTkpjelNFMWN5NjlyUVo3VktPRjJkbGc3Mm1JSlN5Nmg1Y0xxOXhWZHcwSzBjN0VjMFNEdm95Qy1BQ0ljSQ?oc=5>

### ASML reports transactions under its current share buyback program
- Summary: ASML reports transactions under its current share buyback program
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxPd3FYZ3dxbnh0dmlBdy1XY0o4ZXRPNVJDcWQ4Si1zS095VW1HQXpQY2I1eGtyY1RNSWoyVjRKd19HZlFQeTBUMHJTRHBUYkxuNkFUVHZqM2c5Z0E4VG03SFo5WWI4ZDFUM0tYeGRLRThGMmtEVjI3b1JqZEd0aGw1WldfYWhxYkRFQUNCWGRtMWktb2JTT050SXNjQkh1WnRiM0RHYjlCaw?oc=5>

### ASML Holding stock weighs buybacks against capacity review
- Summary: ASML Holding stock weighs buybacks against capacity review
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxPZDQzRkVjLTdBZXM1VDhYNl9XTTNUTmsxQzM4WVp1UlFEcTM2dGRyYWhJNkRCb2xrczBZb1NIdGpMMjVCS0JuZFpFUnFvc2kwb2gzcnFfdGRidXpvUXBzeGw2bDRPX1J1NU15RS1sYk85aEpyZE81RW1fQ2hTY3hiOHBMclZsaWVsMW9hZ2FKT1lmdXIxWmRHMkRCMi1JZU1VN2hUU3N0enkzcDZPX2dwcVUzRml3U3RLRkdZX3ZR?oc=5>

### ASML Holding stock: Buyback activity keeps capital returns in focus
- Summary: ASML Holding stock: Buyback activity keeps capital returns in focus
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxNVGlYamFyT1ZicTJpdUctZmVBTlNIcWs3NmZRdlhySW9tWkExLXdNN2xvS3ZodXV6TmNadi1PMEVuOVZlUmk3eklNc0V6SU5LVnFzYUM0YVdlYzQ5dGRLaHhHcjhNU0twemM5TjJ6ZUdIdHdFUTJmNFRVVGJiMFRSNEZldkROVGVaUTl2RmdZSU9nU25xVUY1QmkyLXhWRWh5OHgxcjRWSkxjNkc0QVF0bDVoWEtwV3JiSm1YbDNOdHlGZzkyaDhzcw?oc=5>

### ASML's Buyback Is Done. Its Dividend Is Booked. The Rest Is a Forecast.
- Summary: ASML's Buyback Is Done. Its Dividend Is Booked. The Rest Is a Forecast.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxOb3BpSWdDV1duWUU4clFwT3l1VWItX1hZcWRpeUxRQ28wWVdrTVpOc3pWNWJSZHhLdWdDcTJLaTRlU3YwUHNhakRPNm1CVUlkWHpBZHJPaU9vd2ZPeVIxT3NIRE1fc05YSldfazU5alFWbGNldDlaRDc5bUtzcnJsLTNVNmNESzRCMnhJbmI4TEl5ZmwtN3ZjXzA1YzlXMm9iYWpPZlZWWXp3cGhKSldtamJ3dTRUeFpTdkdFdXVyWkRfRHo1MGQzMTJpNkN0djR1azVuQ0Utdw?oc=5>

### ASML Holding stock: Buyback and AI demand shape the weekly outlook
- Summary: ASML Holding stock: Buyback and AI demand shape the weekly outlook
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxNak9MU005bXBpNjNsT0FpdDVVd2FWWFctLVQycXg1b3ZhOF9RVnZtdFhSSDZqN1FiUnUtWS01dFNzc3FCcFA2Q1lWMUV1RTJld2F0WDVPc25PbHNMbmt1QzN1SFMtRFdvWm12YkdVc0JnVWtjazh3NXlhcGlxeG51dTkyLUNGbmRtbUI2QWlCaGpsZmFGcEFrek90NGtCcWdlT1k3ckRLU3pYUVBKeUlLcGJ1cVg0c1RjdExCblc2b05XdDFuMDU0?oc=5>

### ASML's Real Story: A 40% Productivity Target and a Buyback Already in Motion
- Summary: ASML's Real Story: A 40% Productivity Target and a Buyback Already in Motion
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3wFBVV95cUxQdG9Hc19NdnpEWi1xMGpid0JuYVBrbzI1M0l3OUdRTWdFVks0RnUzZ081VjFmU1N5Y1lWbUU1TEoxR0ZweW5XZ3RsbUVtM0EweHNhM2FnaWxlM0EwRzlmTm5CcnUzY1ZYOVN2VjFMWnNSeHZxSmtXcVUyUXlBSVRLelhnbmVZU20yd29WS1FTbmY4X2hKZWl2VjZtd0ZxbDBlSG10VFJvTlB6Vmw4bC1KT3FDY0JMV3ZZVF85eS1EZDlMZHA4VXhnRy1mLS1iQmcydV9ZT2ZJdU51LXpqN3Ew?oc=5>

### ASML's Fourth Quarter Is the Real Verdict on AI Spending Fears
- Summary: Q4 results will clarify AI spending trends, potentially boosting confidence in ASML's growth prospects.
- Date: 2026-10-31 | Impact: high | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxQRDJTcnJiMmJHWDE1MWNzenpPV2ZSVHVyUHhtX3hUc0p3MlJRTjJCb3pYclZmY1ZXQzdzSTYzX3BJeEVpeXpaOEtiaXcxdmhQVzNibE0yQ1o0Mjh4eEEtVktqaVdSWEtKbDhINTNxSFhKZlFnNVBxalh1dzE0X3pfVnc3QllqY3pIZ0pHOW9rN0E4a1gzSy12dW92Mzg5T0xLclBKQlR3UldYNmY2UGtpSHFGOVV0cXl2MGRaN0k2a1VoeXQwUm1BYmlSOEFXdkU?oc=5>

## RISKS

### ASML Holding NV Stock (ASML) Moved Down by 4.83% on Oct 30: Facts Behind the Movement
- Summary: ASML shares fell 4.83% on Oct 30; reasons include market volatility.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxOREdReko5bjFSWkhYemFuREgzaThFTHFFMlpXYTB0WkxLMWpyMmszT2tWY0JCNVRsRWFmTWpuUE9WV2JVLXE2TWM0NTN1ZHd5S1h4YmJTelNseXZZREZXTjhQN09SZnNadnU4MVBLVk1wS0lWS1JSTDVGMjZTOXFsMl9oQU9LZElTRDlJ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ASML** | **37.55** | **1,310.42** | **2,006.71** | **55.20** | **588,201,394,176.00 USD** | **44.96** |
| AMAT | 32.31 | 11.60 | 29.08 | 24.80 | 297,226,043,392.00 USD | 61.56 |
| LRCX | 35.61 | 20.44 | 27.73 | 54.40 | 284,774,137,856.00 USD | 45.19 |
| KLAC | 38.37 | 30.59 | 30.51 | 28.90 | 199,496,581,120.00 USD | 27.35 |

Peers fetched as_of: 2026-11-02; ASML reuses existing data (market data as_of: 2026-11-02); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-14
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-02

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMi1gFBVV95cUxNbmJCNXdkMUR5U2pMTmE2SW93WEJ0VGN2VFduWjFPbUI1elZnaUlCcmMxWFk1R0xvM0p6TkMzdmthaXk1ZGZ1NFV4ZjdrcnpmZDNtRkhteThmamtUQktXQVAxdllzaF9SQ0RGaHVVWnY3VGMtX0VwSXFkeUUydzJpUXpoT1ZqX2l5ZTlua3BqOG1YOVo3LXpLMExTeTBKb1VxMlUtTU8zam41NWFaaTdIRVRfeERMeUVqRDlfdnFHRVYxbzNWZl9hU25kbDBBUmpOd0VsOG1B?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxOVHBuVFpCdEQ1QUdraDlKU0lBQXozSndNb091NVBPNlhPSVByNW1EaW1sUnlyQVFQSUJIelFfQW5QaHpkSFZOeFltckJ6NWFvV0JZRUZaenNrRjJ2djNUREIxUVJ6OHVVeDdIU1MwdDk1WWlVUmpnVGlCYW9NYUFzYlJOUFpJN19aeHFyeS1SQlNhV0JoVVFuMkZGUXJneTJsLWVkV3lwTWlWUy1GOGd0dE85NUgyOEc0YXVQOTA5bmY4UFgya2hjelNvMnpWb0JHUFBUOGFB?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxOU0lBZDc0MC1ZaWZWeVQ2NEZyS0xfMmI0OTlFSHp3aTcybXo4UGJabDZHRTZpSk04dFdsZkJWZWVZdV9MT2hLUVk3YkI1RXBWUXRNSW51WWFpcWNNdHJ6cndIUHN3anhseEppZDFjUmdTTDlGQmRqZnJyYWRON0ZXeUFaWGl3VEdnTUpFdGE3S01Ib3ZUcWZGT1dIandHUnI0ZmdiWXViWkJPbEVzV3FlM1VENW9Lc18yeDNvNy1oNmlTSzA5c0VSZGRCc3p5eW9YWEHSAdcBQVVfeXFMUDdnQTdKaEJPbFlUTm4wSXRiWEM1cWVBWFoxblVNTTlDeERlZDNmbHBwU2VyWVNWWXQ0cThQcGpzdGdHNW5qdGhUOGN3VEZBRDRIWUJ5ckhpUTJmSC1weV9nZVhlZlpoVnB4R2VQUnBWNDFMS2hNakdtVy0tcGxDYmZDbWtXQWsyNDFJTWQtR3VQcFNoNXF2cmdNWDZMLWVyeVZLR1pOcXcwLXlINE5teXg1SUxjNExDQU9Nb0xValRBMkw3Uzd5RFc1Ml9DSTZOSG5hNGczX1k?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxNbk9ObjF3b1haR3JJNVNXeGRqYjNhVUtOeXhwTUdvNVpCQzRILWJFWm5aMVA2V3pXa1RjdEE0RU1hSDNsYWJORnJFS1BqWWN5bUtaRjcxcE5tTnVZU0sxaXNJdTJmYkJwMEhyaEFnLTRWVEUxXzg4a0dSNWtocVd0VGtCWVFqRlVQbTZNbHFhTV9LVFVQLUNNaFNXQ1lwTDBnSkZhaWhCYWliNFZucGs1MTc4SE5uVEV1RjRJYngzRFplMENpeVlRNHpNX0hVaFJxZ3lLa2xOQXo?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxNMVBCVW1ibVBUSzl1cS11MVpTVzFyT2VoSjZrQWhPNXZjUzJzNEdEY2hELXVjcDkzMTA0WG9jQ1NqQW0tYS05V1hOa2NSN2hydnZFamMzZGc5aDkyNGJuNlB3QVQycm5uQVhKVTctTFI4Yk5sd056aEViRThJNnRJVzB6V2k3MGsyUDJ0RWdQYWRZbTFEdjVfaENIV1BDMzR5TVRORUJxbTVVTVlxWElDMGY1a3RaMHlMYVBlbC12ajNIYmozT2E1Wkg5UlBiT2JsTEdZUQ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNcU1hVi13RktuT1dDNXhuM2duR3g2RXEzQUhZYklTR0QybDZ6bmRZY05rTUxoakdTaDNjY1ZlMHJrdGl0dzQtaG43RkxwMmRwVEttdFoyWEZGRVU1OU1BTkpjelNFMWN5NjlyUVo3VktPRjJkbGc3Mm1JSlN5Nmg1Y0xxOXhWZHcwSzBjN0VjMFNEdm95Qy1BQ0ljSQ?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPd3FYZ3dxbnh0dmlBdy1XY0o4ZXRPNVJDcWQ4Si1zS095VW1HQXpQY2I1eGtyY1RNSWoyVjRKd19HZlFQeTBUMHJTRHBUYkxuNkFUVHZqM2c5Z0E4VG03SFo5WWI4ZDFUM0tYeGRLRThGMmtEVjI3b1JqZEd0aGw1WldfYWhxYkRFQUNCWGRtMWktb2JTT050SXNjQkh1WnRiM0RHYjlCaw?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxPZDQzRkVjLTdBZXM1VDhYNl9XTTNUTmsxQzM4WVp1UlFEcTM2dGRyYWhJNkRCb2xrczBZb1NIdGpMMjVCS0JuZFpFUnFvc2kwb2gzcnFfdGRidXpvUXBzeGw2bDRPX1J1NU15RS1sYk85aEpyZE81RW1fQ2hTY3hiOHBMclZsaWVsMW9hZ2FKT1lmdXIxWmRHMkRCMi1JZU1VN2hUU3N0enkzcDZPX2dwcVUzRml3U3RLRkdZX3ZR?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxNVGlYamFyT1ZicTJpdUctZmVBTlNIcWs3NmZRdlhySW9tWkExLXdNN2xvS3ZodXV6TmNadi1PMEVuOVZlUmk3eklNc0V6SU5LVnFzYUM0YVdlYzQ5dGRLaHhHcjhNU0twemM5TjJ6ZUdIdHdFUTJmNFRVVGJiMFRSNEZldkROVGVaUTl2RmdZSU9nU25xVUY1QmkyLXhWRWh5OHgxcjRWSkxjNkc0QVF0bDVoWEtwV3JiSm1YbDNOdHlGZzkyaDhzcw?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxOb3BpSWdDV1duWUU4clFwT3l1VWItX1hZcWRpeUxRQ28wWVdrTVpOc3pWNWJSZHhLdWdDcTJLaTRlU3YwUHNhakRPNm1CVUlkWHpBZHJPaU9vd2ZPeVIxT3NIRE1fc05YSldfazU5alFWbGNldDlaRDc5bUtzcnJsLTNVNmNESzRCMnhJbmI4TEl5ZmwtN3ZjXzA1YzlXMm9iYWpPZlZWWXp3cGhKSldtamJ3dTRUeFpTdkdFdXVyWkRfRHo1MGQzMTJpNkN0djR1azVuQ0Utdw?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxNak9MU005bXBpNjNsT0FpdDVVd2FWWFctLVQycXg1b3ZhOF9RVnZtdFhSSDZqN1FiUnUtWS01dFNzc3FCcFA2Q1lWMUV1RTJld2F0WDVPc25PbHNMbmt1QzN1SFMtRFdvWm12YkdVc0JnVWtjazh3NXlhcGlxeG51dTkyLUNGbmRtbUI2QWlCaGpsZmFGcEFrek90NGtCcWdlT1k3ckRLU3pYUVBKeUlLcGJ1cVg0c1RjdExCblc2b05XdDFuMDU0?oc=5
- https://news.google.com/rss/articles/CBMi3wFBVV95cUxQdG9Hc19NdnpEWi1xMGpid0JuYVBrbzI1M0l3OUdRTWdFVks0RnUzZ081VjFmU1N5Y1lWbUU1TEoxR0ZweW5XZ3RsbUVtM0EweHNhM2FnaWxlM0EwRzlmTm5CcnUzY1ZYOVN2VjFMWnNSeHZxSmtXcVUyUXlBSVRLelhnbmVZU20yd29WS1FTbmY4X2hKZWl2VjZtd0ZxbDBlSG10VFJvTlB6Vmw4bC1KT3FDY0JMV3ZZVF85eS1EZDlMZHA4VXhnRy1mLS1iQmcydV9ZT2ZJdU51LXpqN3Ew?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxQRDJTcnJiMmJHWDE1MWNzenpPV2ZSVHVyUHhtX3hUc0p3MlJRTjJCb3pYclZmY1ZXQzdzSTYzX3BJeEVpeXpaOEtiaXcxdmhQVzNibE0yQ1o0Mjh4eEEtVktqaVdSWEtKbDhINTNxSFhKZlFnNVBxalh1dzE0X3pfVnc3QllqY3pIZ0pHOW9rN0E4a1gzSy12dW92Mzg5T0xLclBKQlR3UldYNmY2UGtpSHFGOVV0cXl2MGRaN0k2a1VoeXQwUm1BYmlSOEFXdkU?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxOREdReko5bjFSWkhYemFuREgzaThFTHFFMlpXYTB0WkxLMWpyMmszT2tWY0JCNVRsRWFmTWpuUE9WV2JVLXE2TWM0NTN1ZHd5S1h4YmJTelNseXZZREZXTjhQN09SZnNadnU4MVBLVk1wS0lWS1JSTDVGMjZTOXFsMl9oQU9LZElTRDlJ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
