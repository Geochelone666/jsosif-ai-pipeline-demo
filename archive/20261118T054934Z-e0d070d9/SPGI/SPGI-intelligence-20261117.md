# SPGI Intelligence Report

- ticker: **SPGI**
- Report as_of: **2026-11-17**
- Market data as_of: **2026-11-17**
- Quant sources: https://finance.yahoo.com/quote/SPGI/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SPGI/key-statistics/
- AI analysis snapshot as_of: **2026-11-17**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-18T06:02:10.968320+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 3, 'ai': 13, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261117T062519Z-6171f6c2/SPGI** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **3**; {'directional_claim_without_event_type': 3}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 14 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 28.0%; oldest publication 2026-11-10

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 452.3500 |
| Return 1D (%) | -4.0798 |
| Return 1W (%) | -4.4425 |
| Return 1M (%) | 5.2858 |
| Return YTD (%) | -7.8743 |
| Return 1Y (%) | -1.3425 |
| Annualized volatility (%) | 31.1634 |
| Beta vs SPY | 0.3847 |
| Max drawdown (%) | -28.4781 |
| Sharpe (rf=0) | 0.1138 |
| Downside deviation (rf=0, %) | 23.3831 |
| Sortino (rf=0) | 0.1517 |
| Historical VaR 95% (1D, %) | 2.9286 |
| Historical ES 95% (1D, %) | 4.7258 |
| Correlation vs SPY | 0.1701 |
| Tracking error vs SPY (%) | 31.8581 |
| P/E (trailing) | 27.02 |
| P/B | 6.65 |
| EV/EBITDA | 17.58 |
| Revenue growth (%) | 6.80 |
| Forward P/E (estimate) | 22.42 |
| Gross margin (%) | 70.99 |
| Operating margin (%) | 44.09 |
| Return on equity (%) | 17.88 |
| Free cash flow yield (%) | 4.61 |
| MA50 | 429.5862 |
| Close vs MA50 (%) | 5.2990 |
| MA200 | 413.9713 |
| Close vs MA200 (%) | 9.2709 |
| RSI (14, Wilder) | 49.0753 |
| MACD (12,26) | 10.8643 |
| MACD signal (9) | 13.4039 |
| MACD histogram | -2.5396 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SPGI': 284, 'SPY': 284}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 452.3500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -4.0798 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -4.4425 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 5.2858 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -7.8743 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -1.3425 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 31.1634 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 23.3831 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.1517 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9286 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.7258 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1701 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.8581 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3847 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.4781 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1138 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 22.4215 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 70.9940 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 44.0930 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 17.8760 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.6050 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 27.0221 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 49.0753 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -2.5396 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 5.2990 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 9.2709 -> Clearly above the moving-average trend level.

## TAILWINDS

### SPGI Stock Jumps 13% in 3 Months: Here's What You Should Know
- Summary: SPGI Stock Jumps 13% in 3 Months: Here's What You Should Know
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxNY1VNM0FETkYwWVRQbmtVY2gzNVdVa0ZHbHVFZlNGbXV0RklTb2pncFFDVW5Udl9MWkxVamZtMWZ5b3RVTmxoTkFlV3d3T1dnVnlpSWg1OUVNLXhSbjFYcUpfc3NSR3pfc2IxRlF1V041dldDV0lfdnAxLThzTGpmOWNQN21XTFF0dnI1MWgybncwSGFvT3M1YklJRlZhdHFYMDJGdHA3aTlBMDZPSlU3YVd2OUJUUQ?oc=5>

### S&P Global (SPGI) Stock Rises 1.08% (November 13, 2026): Up 10.2% in a Month
- Summary: S&P Global (SPGI) Stock Rises 1.08% (November 13, 2026): Up 10.2% in a Month
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxQcGZ2Tk9HYjAxZ0FUSUxQb2VGdmZvVW5uRFNTM1U4UkFiOW5LZ1B0eVBHRlZPbVh1WUpaaE1WdDRwS2pIM0Jlb19ZMXRsZE9aWFVNSFF5NDdDVVVRUGltd0JGSVhpT3VsSGN1eFdMQnk5WmNubTlQOTgtVVNJNS1nZ21Xc1M4WmVCcXhFRm84NHRPcWdOTnQtejJmSjRrM0dNbHpkS291ZlFHdw?oc=5>

### S&P Global Adds Kfir Godrich to its Board of Directors
- Summary: Board addition of Kfir Godrich enhances governance and leadership depth.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNaWxmdHIwRkRNbmpiODROUC1RdkQtbncyRW5ISV84S2tmaXZFVjAwb1hOaklncTh3UHNFeVhNT3BoSnpGQl9fekZwNENGU3R4ZTNraXN5N21Ubm5aMDFJazFfOWxGX01xaURZZVZmOVN2d0lqaXpCTnlNSjN6dWlCbHZwcVZpNnlMRmEwRGJfNkd4Tnpz?oc=5>

### S&P Global (SPGI) Could Be 9% Undervalued As Capital IQ Review Unfolds
- Summary: Valuation review suggests SPGI may be undervalued by 9%.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxNVnoya2xjeE4zUzlQelFXQkhTYmF0RlQ3aEJoN1VmYWVaakN2cEZzVzRvUzZZV3QxX0JrOFA5MlZXS1ExV3RXOTJYcURDbHJfa09EMWw0TlJMeWR0UTRPY3A4bTRUSGtuRnZUY0N3UGh6b2F2aWlpTmxHMUM5QjBNcFN5a0QzQ0VFLXVuQnNBXzlpcVpaa2hOaTJqeU9JTjc0ZEJ4UGg4XzE4LWR5Z3ZrYjlKWWZOV0hSbHM0RFNxVUZ5QXRlbmZLekRVYzB2QmFDeXZaYUVjWdIB3AFBVV95cUxPbTNlbnB6bHJOdDhVWXpnWU1KcS1vbjh5d2lucHNIRnZnOUNWdEJrUHBIRmJsZ3BiNU1NOXFBOURoNTBqVmVISHBnUWtRc3A1enRDTzYtRW52MGxxTDRqVFJsTU5CeXdyYWRpd1Y2S1Q4SkRVNTBVblgtbEJWcU5sN2JPQUlxem5ZV1VaTTRpTDlubmlrd3RMTjNRSEhHSmpRLWlSRV9yOHFpQkdEWW1rLTl1T0VMLXk1U0tpVWxjdE5zZ3dhcmtaSHlLemJLQXppSDY1NUdNTVBpZk52?oc=5>

## HEADWINDS

### S&P Global Inc Stock (SPGI) Moved Down by 3.38% on Nov 17: Drivers Behind the Movement
- Summary: Stock fell 3.38% on Nov 17, indicating short‑term negative market sentiment.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxPQVJhZjVzSkFPMFdROWtfajY2QWFPTlBYQnlURTVoTzFTa2Rhbnl1dGhPOGEwMTdhcG54dldITWV6czBjODFBWjZUbjAyd2gyclNzWUwwUi1jeUEweTdHYVk1TU92N2c2dndKSXV6Yy1SWE90dHBjaWpaVHBBQnVYcC0tcERtTkYzMlpN?oc=5>

### Is S&P Global (SPGI) Stock Starting To Look Pricey Now?
- Summary: Questioning whether SPGI stock is overvalued.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxNLUlMWHFxdjMwZkRiZTQ5RGI5aVphSGN4Zk9VOTk3amc2dnNsdEcwRGE1WFk5cmRsRVFuN21zR05UWDdGLWZaZ240YmFNR0VvdXMtX1JoTHZXRXJjdkk3LTJteWZHbGJmNXNJT0Y1YkpJS2laclZRU1piTTJpenV3MVlIWmtiWjNZMU5saFUtZlFYeWlNV3kxRmVhbjNjU1Q0R1VlbkxnNmFSMk1sUHBZcnJnOFdNQUwwUVRUU2xpekFnellWWVhCU3ZwNNIB0AFBVV95cUxQOFl3VXlXUkVCbWMxWXFEQlcySmFldndHektGaHFMYVpjSUQ3Z056YVd3RmFsMzBWOGdOckVFcGZjYTg0X1E1RWk4OWJ3TG5TYTVCblQ2SWk5OEZNMmVoSE5EUFVUNE9Bc3Azc2hfQThQZTVVc1ZHWUtZZWZWbnM3UFQ2UEFZUjlHR043UnBLYlg1OE1Vem5FMFRiWVJ0cmxFNXhVWUpEaW9SRkJxejNFVUY1WkwycEdJelNLVXV5Ui1ERGFzSGJfV1I1UzA0VEJr?oc=5>

## CATALYSTS

### S&P Global (SPGI) Stock Trades At A Premium To Its Earnings Power
- Summary: S&P Global (SPGI) Stock Trades At A Premium To Its Earnings Power
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQSkk4Z0g1VkNPLUhfbm9CQ3hxSWNlMnVQMndvemY2S1F0bUdmdVJMczl1R0lpcVU5RGg0bU9ZVjA5U05Vb1o2RWRLU2JXUU5QdGd1MXZxOHZzdklCdW81ZzhpcHBpeWVvbGk4eGoyY3dqTHhFTW84Mlk2Z3JZZk04SXNYLV9BU3pORWotR3M2aVlIYlZ0anc?oc=5>

### S&P Global Announces Public Offering of Senior Notes
- Summary: S&P Global plans to issue new senior notes, expanding its debt capacity.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxNc1lLdFdJbjFRXzBkaS1xa3dqdE9uVFlVcDBYQXlOX1FaWEtaWFB2dHBjb19BanRDSUlRODdEcFNQNGY3QU1tQzY0TTJTelZyemEzZklZMHVVWFM5cXVDVngxUGF4RGJlYWhTcEdvQXA4ZWFwY3ZOMWlvNkJkOEN2ZktRVTFFS3FpSUdyT0JzdE1tNjJWVVg3ZmtXTFB6MFo2Wktr?oc=5>

### New S&P Global (SPGI) notes won't be exchange-listed; no public market currently exists.
- Summary: The new notes lack an exchange listing, limiting immediate market liquidity.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxQMXQ1NkxjTkxyOEU2Wk9HU0hCcnVqZTNiQUpiWWxldmRhaXVudVIzcDFraG5tLTRzaU5sWW9YNUtaZ2VfUFVnaDZoN3VEUWVhVGVtZmEzb1ZFLVpmX0I1Y3JNN2g3QTE2cDZlaERhZVV0bG5pVXZHWXA0Uk0wV3BkWTNxdEZKbHZEM1hWVWMzejBpVTRSSUNHMjNVdEs1VlpBX3RkZy1TWQ?oc=5>

### Three series carry 5.6%, 5.8% and 6% rates in S&P Global (SPGI)'s $2B note offering.
- Summary: SPGI issues $2B notes with 5.6%-6% rates, expanding debt capacity.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxOblJrcHVXT1psMVVjTXo1aE1hVEg4Z3doNEZ3eUNURkNmTVlseGNzTUdkcUFOZU1PZVVZWXVUeTQxZmxyM1NVbERWbTFrUTJmdk5TdGFzaE5aUUIxck1tY3JsaHZqVXE5YThSQkpDN0RKdzZRakpZaGlrSjVfQkFHWVE4ekthMGFfYlU0QlJPeHZEaFhHMmtPekxuN1V5bzk2UGpHOWVOYWVTUkpWdlp5M3FidTk4R1dzUHZBZg?oc=5>

### BlackRock's former technology chief will join S&P Global's board Jan. 1
- Summary: New board member from BlackRock joins SPGI, enhancing governance.
- Date: 2026-11-17 | Impact: low | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPa1VOWVBNaUluY2xDNG1TcVM2RmVkeDlKdlE4WG1kLXhVa2tQcVYycmNnME1ScHVfSHVvUHJ2SDZsLV8tZ0g2aTI4dVRGNnNqbkpJNmd0RlpnRDRKV3JoY2otTGtLS3VvV092WWNnODJpTjJRazU5emJueVE1Z3BQWWNydFRMMDJwNDZpQmtIQ0FmRXhQUVlfeDZhY09zVlg1?oc=5>

### S&P Global: Admitting Defeat, Looking To Spin Off More Assets
- Summary: SPGI plans to spin off additional assets after admitting strategic setbacks.
- Date: 2026-11-13 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxQemNxR0tTajU0akxQdG5fak54S1I0WUt4UWhtOV96cUJVQzlfVlhQeVFWZXpFMlQyM0VwNUZWcUViUGxJcjJMNjJyQ0tXQXpHWGlmT2xvQ3hVX2x1MVkzS2ZzaXR2X3FyNWpFT2VRVnRkZzZpVEdyUGNET3h2NUlUS2RMSExZQ01UN3ljdjI5eDM3eFU1Skk5MHZ6REk5VnB0TVNtRlVoTQ?oc=5>

### AI Ready Data Push Could Be A Key Test For S&P Global Stock
- Summary: AI data initiative may boost SPGI stock performance.
- Date: 2026-11-14 | Impact: high | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxOV3BZYzdMbDNBUWtrTml5WDJzeU1HTDdCWldsQmU2WE5KTzM0b3VpWi03a19IQ2gwYXMwWEhUQ3c0ZnppM05LbGM3ZkZNNUg5OVJkQlc2VHhBMDBQSm5PeG43cnhNWElXZDBsa2NESk5pZWdObWZ2N1A1eDAyLXhyaDBOU1BkTm9tZkRVUHdXTUphSVlBSUZ1dFUxVW16UlprUnV1X2NnTUh4c0FfRDZORGN2OENmcENpNENWMnA2MFRFeVFjYWRqalRZQXFhNlJtejU1M9IB2gFBVV95cUxNSXg2UlNnejZjMHlGVHlfWHR5TWlmd09KV0ZtZE1NRTRfYnVSRzFsX29IMnU1Q1BxUU50Qko5eWxnWmk2dkdIZ1pBejg5X252YjkzZ0FNbFY4LUlybUJaazNrNWJDc1RQT0ppYTlhU2tIeFFWNXQwVUpud1V1T1ZXZXA3bElVYmMtbVR3b2VhVjNnXzNDWkU1S3Vfamo3TjA2ckw1VTd2ODlQT18tOFY5OHp4elVLYXhhbUFpb2xaTm83Vmd3VFBtS1hsVzhyQ1dGU3I1TFBWQ2VrQQ?oc=5>

### S&P Global (SPGI) will expand its board to 11 as Kfir Godrich joins on January 1, 2027.
- Summary: Board expansion signals governance strengthening.
- Date: 2026-11-17 | Impact: medium | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQNnllYUFoNHVPRU1tTEtFNW11OWt3UlBYZDhvcWJCQjJGeGw2X1pHS0ZjLXY2WUZodVBvWFVVcXNDUmtNaWhjRlJ0a3JVazNMcnliamhkUXgxenNUMFNNZWY4WlkwOVJFQUVLQXVfOGZzbTk1bHF6U0JaWE9mU2xILS1jZlFlTjdibEdrMzFXLW05UjdRSXF5Qk1nTk1ldHd1clpFM1JR?oc=5>

### SPGI: S&P Global Inc. filed SEC Form 8-K: Leadership Update, Financial Statements and Exhibits
- Summary: S&P Global filed an 8-K reporting leadership changes and financial statements, providing updated corporate governance and financial data.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPZTY4a3FkS0dZLUhxN0ZVbUNVNkpnemtlc01UazhWUTByN3h6djRaaEpsR28zcXp0eDBBdkdSMWl2MmFHUXBmcmc5dm9fQk9BckpWaXQzZno2cTBNcVNadi1Pai1MaVUtVDVNR0JINTFuSmJZazg3V1pCRUFxY0t4UFBURFF1Y0dnWVE1TWxUSExDZEhjX3NjNkF1TV9yUGtnQ194eHhn?oc=5>

## RISKS

### A $650 million S&P Global bond issue comes due in 2036.
- Summary: A $650M bond matures in 2036, affecting future cash flows.
- Date: 2026-11-16 | Impact: low | Horizon: long | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxQRk1lNnpvWnprc0lKSUtXQkhscklWRTlnbmpPbkNpSTJ2bTdXSmVOelVLYjVHdi1sTms0UlNHUTNOVHVNb2RSYXNQZ3VvUVFBdEpYcmpqM3ZRX3RsVlAwaHkyaWtXTVZnQkc1NUlyank4R2kxZEM4NWxqQmQ5UUFHVUVKc1JDQ3hBOWpGUmFITGRpdDg0SGdWaGhVVGVvWUF2eVZERWJyWFZiUUFJdURHVm42eFZtWWNm?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SPGI** | **27.02** | **6.65** | **17.58** | **6.80** | **131,136,266,240.00 USD** | **-1.34** |
| MCO | 29.56 | 25.56 | 22.14 | 0.80 | 83,523,952,640.00 USD | 3.49 |
| MSCI | 33.66 | -15.13 | 25.84 | 12.40 | 45,515,472,896.00 USD | 15.74 |
| FDS | 21.70 | 5.57 | 13.80 | 6.30 | 11,144,313,856.00 USD | 17.58 |

Peers fetched as_of: 2026-11-17; SPGI reuses existing data (market data as_of: 2026-11-17); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-27
- Next expected earnings: 2027-02-09 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-17

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-28
- Revenue (latest available single quarter): 1,567,000,000.00 USD; period 2018-01-01/2018-03-31; fiscal year/reporting period 2018/Q1
- Net income (latest available single quarter): 1,240,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/64040/000006404026000058/spgi-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMitgFBVV95cUxNY1VNM0FETkYwWVRQbmtVY2gzNVdVa0ZHbHVFZlNGbXV0RklTb2pncFFDVW5Udl9MWkxVamZtMWZ5b3RVTmxoTkFlV3d3T1dnVnlpSWg1OUVNLXhSbjFYcUpfc3NSR3pfc2IxRlF1V041dldDV0lfdnAxLThzTGpmOWNQN21XTFF0dnI1MWgybncwSGFvT3M1YklJRlZhdHFYMDJGdHA3aTlBMDZPSlU3YVd2OUJUUQ?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxQcGZ2Tk9HYjAxZ0FUSUxQb2VGdmZvVW5uRFNTM1U4UkFiOW5LZ1B0eVBHRlZPbVh1WUpaaE1WdDRwS2pIM0Jlb19ZMXRsZE9aWFVNSFF5NDdDVVVRUGltd0JGSVhpT3VsSGN1eFdMQnk5WmNubTlQOTgtVVNJNS1nZ21Xc1M4WmVCcXhFRm84NHRPcWdOTnQtejJmSjRrM0dNbHpkS291ZlFHdw?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNaWxmdHIwRkRNbmpiODROUC1RdkQtbncyRW5ISV84S2tmaXZFVjAwb1hOaklncTh3UHNFeVhNT3BoSnpGQl9fekZwNENGU3R4ZTNraXN5N21Ubm5aMDFJazFfOWxGX01xaURZZVZmOVN2d0lqaXpCTnlNSjN6dWlCbHZwcVZpNnlMRmEwRGJfNkd4Tnpz?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxNVnoya2xjeE4zUzlQelFXQkhTYmF0RlQ3aEJoN1VmYWVaakN2cEZzVzRvUzZZV3QxX0JrOFA5MlZXS1ExV3RXOTJYcURDbHJfa09EMWw0TlJMeWR0UTRPY3A4bTRUSGtuRnZUY0N3UGh6b2F2aWlpTmxHMUM5QjBNcFN5a0QzQ0VFLXVuQnNBXzlpcVpaa2hOaTJqeU9JTjc0ZEJ4UGg4XzE4LWR5Z3ZrYjlKWWZOV0hSbHM0RFNxVUZ5QXRlbmZLekRVYzB2QmFDeXZaYUVjWdIB3AFBVV95cUxPbTNlbnB6bHJOdDhVWXpnWU1KcS1vbjh5d2lucHNIRnZnOUNWdEJrUHBIRmJsZ3BiNU1NOXFBOURoNTBqVmVISHBnUWtRc3A1enRDTzYtRW52MGxxTDRqVFJsTU5CeXdyYWRpd1Y2S1Q4SkRVNTBVblgtbEJWcU5sN2JPQUlxem5ZV1VaTTRpTDlubmlrd3RMTjNRSEhHSmpRLWlSRV9yOHFpQkdEWW1rLTl1T0VMLXk1U0tpVWxjdE5zZ3dhcmtaSHlLemJLQXppSDY1NUdNTVBpZk52?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxPQVJhZjVzSkFPMFdROWtfajY2QWFPTlBYQnlURTVoTzFTa2Rhbnl1dGhPOGEwMTdhcG54dldITWV6czBjODFBWjZUbjAyd2gyclNzWUwwUi1jeUEweTdHYVk1TU92N2c2dndKSXV6Yy1SWE90dHBjaWpaVHBBQnVYcC0tcERtTkYzMlpN?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxNLUlMWHFxdjMwZkRiZTQ5RGI5aVphSGN4Zk9VOTk3amc2dnNsdEcwRGE1WFk5cmRsRVFuN21zR05UWDdGLWZaZ240YmFNR0VvdXMtX1JoTHZXRXJjdkk3LTJteWZHbGJmNXNJT0Y1YkpJS2laclZRU1piTTJpenV3MVlIWmtiWjNZMU5saFUtZlFYeWlNV3kxRmVhbjNjU1Q0R1VlbkxnNmFSMk1sUHBZcnJnOFdNQUwwUVRUU2xpekFnellWWVhCU3ZwNNIB0AFBVV95cUxQOFl3VXlXUkVCbWMxWXFEQlcySmFldndHektGaHFMYVpjSUQ3Z056YVd3RmFsMzBWOGdOckVFcGZjYTg0X1E1RWk4OWJ3TG5TYTVCblQ2SWk5OEZNMmVoSE5EUFVUNE9Bc3Azc2hfQThQZTVVc1ZHWUtZZWZWbnM3UFQ2UEFZUjlHR043UnBLYlg1OE1Vem5FMFRiWVJ0cmxFNXhVWUpEaW9SRkJxejNFVUY1WkwycEdJelNLVXV5Ui1ERGFzSGJfV1I1UzA0VEJr?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQSkk4Z0g1VkNPLUhfbm9CQ3hxSWNlMnVQMndvemY2S1F0bUdmdVJMczl1R0lpcVU5RGg0bU9ZVjA5U05Vb1o2RWRLU2JXUU5QdGd1MXZxOHZzdklCdW81ZzhpcHBpeWVvbGk4eGoyY3dqTHhFTW84Mlk2Z3JZZk04SXNYLV9BU3pORWotR3M2aVlIYlZ0anc?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxNc1lLdFdJbjFRXzBkaS1xa3dqdE9uVFlVcDBYQXlOX1FaWEtaWFB2dHBjb19BanRDSUlRODdEcFNQNGY3QU1tQzY0TTJTelZyemEzZklZMHVVWFM5cXVDVngxUGF4RGJlYWhTcEdvQXA4ZWFwY3ZOMWlvNkJkOEN2ZktRVTFFS3FpSUdyT0JzdE1tNjJWVVg3ZmtXTFB6MFo2Wktr?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxQMXQ1NkxjTkxyOEU2Wk9HU0hCcnVqZTNiQUpiWWxldmRhaXVudVIzcDFraG5tLTRzaU5sWW9YNUtaZ2VfUFVnaDZoN3VEUWVhVGVtZmEzb1ZFLVpmX0I1Y3JNN2g3QTE2cDZlaERhZVV0bG5pVXZHWXA0Uk0wV3BkWTNxdEZKbHZEM1hWVWMzejBpVTRSSUNHMjNVdEs1VlpBX3RkZy1TWQ?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxOblJrcHVXT1psMVVjTXo1aE1hVEg4Z3doNEZ3eUNURkNmTVlseGNzTUdkcUFOZU1PZVVZWXVUeTQxZmxyM1NVbERWbTFrUTJmdk5TdGFzaE5aUUIxck1tY3JsaHZqVXE5YThSQkpDN0RKdzZRakpZaGlrSjVfQkFHWVE4ekthMGFfYlU0QlJPeHZEaFhHMmtPekxuN1V5bzk2UGpHOWVOYWVTUkpWdlp5M3FidTk4R1dzUHZBZg?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPa1VOWVBNaUluY2xDNG1TcVM2RmVkeDlKdlE4WG1kLXhVa2tQcVYycmNnME1ScHVfSHVvUHJ2SDZsLV8tZ0g2aTI4dVRGNnNqbkpJNmd0RlpnRDRKV3JoY2otTGtLS3VvV092WWNnODJpTjJRazU5emJueVE1Z3BQWWNydFRMMDJwNDZpQmtIQ0FmRXhQUVlfeDZhY09zVlg1?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxQemNxR0tTajU0akxQdG5fak54S1I0WUt4UWhtOV96cUJVQzlfVlhQeVFWZXpFMlQyM0VwNUZWcUViUGxJcjJMNjJyQ0tXQXpHWGlmT2xvQ3hVX2x1MVkzS2ZzaXR2X3FyNWpFT2VRVnRkZzZpVEdyUGNET3h2NUlUS2RMSExZQ01UN3ljdjI5eDM3eFU1Skk5MHZ6REk5VnB0TVNtRlVoTQ?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxOV3BZYzdMbDNBUWtrTml5WDJzeU1HTDdCWldsQmU2WE5KTzM0b3VpWi03a19IQ2gwYXMwWEhUQ3c0ZnppM05LbGM3ZkZNNUg5OVJkQlc2VHhBMDBQSm5PeG43cnhNWElXZDBsa2NESk5pZWdObWZ2N1A1eDAyLXhyaDBOU1BkTm9tZkRVUHdXTUphSVlBSUZ1dFUxVW16UlprUnV1X2NnTUh4c0FfRDZORGN2OENmcENpNENWMnA2MFRFeVFjYWRqalRZQXFhNlJtejU1M9IB2gFBVV95cUxNSXg2UlNnejZjMHlGVHlfWHR5TWlmd09KV0ZtZE1NRTRfYnVSRzFsX29IMnU1Q1BxUU50Qko5eWxnWmk2dkdIZ1pBejg5X252YjkzZ0FNbFY4LUlybUJaazNrNWJDc1RQT0ppYTlhU2tIeFFWNXQwVUpud1V1T1ZXZXA3bElVYmMtbVR3b2VhVjNnXzNDWkU1S3Vfamo3TjA2ckw1VTd2ODlQT18tOFY5OHp4elVLYXhhbUFpb2xaTm83Vmd3VFBtS1hsVzhyQ1dGU3I1TFBWQ2VrQQ?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQNnllYUFoNHVPRU1tTEtFNW11OWt3UlBYZDhvcWJCQjJGeGw2X1pHS0ZjLXY2WUZodVBvWFVVcXNDUmtNaWhjRlJ0a3JVazNMcnliamhkUXgxenNUMFNNZWY4WlkwOVJFQUVLQXVfOGZzbTk1bHF6U0JaWE9mU2xILS1jZlFlTjdibEdrMzFXLW05UjdRSXF5Qk1nTk1ldHd1clpFM1JR?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPZTY4a3FkS0dZLUhxN0ZVbUNVNkpnemtlc01UazhWUTByN3h6djRaaEpsR28zcXp0eDBBdkdSMWl2MmFHUXBmcmc5dm9fQk9BckpWaXQzZno2cTBNcVNadi1Pai1MaVUtVDVNR0JINTFuSmJZazg3V1pCRUFxY0t4UFBURFF1Y0dnWVE1TWxUSExDZEhjX3NjNkF1TV9yUGtnQ194eHhn?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxQRk1lNnpvWnprc0lKSUtXQkhscklWRTlnbmpPbkNpSTJ2bTdXSmVOelVLYjVHdi1sTms0UlNHUTNOVHVNb2RSYXNQZ3VvUVFBdEpYcmpqM3ZRX3RsVlAwaHkyaWtXTVZnQkc1NUlyank4R2kxZEM4NWxqQmQ5UUFHVUVKc1JDQ3hBOWpGUmFITGRpdDg0SGdWaGhVVGVvWUF2eVZERWJyWFZiUUFJdURHVm42eFZtWWNm?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
