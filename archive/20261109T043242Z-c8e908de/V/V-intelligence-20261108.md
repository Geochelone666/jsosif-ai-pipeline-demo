# V Intelligence Report

- ticker: **V**
- Report as_of: **2026-11-08**
- Market data as_of: **2026-11-06**
- Quant sources: https://finance.yahoo.com/quote/V/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/V/key-statistics/
- AI analysis snapshot as_of: **2026-11-08**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-09T04:41:15.616543+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 11, 'ai': 12, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **11** exact headline/source/date matches; prior report **20261108T041758Z-43fb2458/V** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 7 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 48.0%; oldest publication 2026-11-02

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 422.6500 |
| Return 1D (%) | 0.0142 |
| Return 1W (%) | 2.1906 |
| Return 1M (%) | 14.0325 |
| Return YTD (%) | 21.2363 |
| Return 1Y (%) | 26.4335 |
| Annualized volatility (%) | 22.9514 |
| Beta vs SPY | 0.3425 |
| Max drawdown (%) | -17.1805 |
| Sharpe (rf=0) | 1.1398 |
| Downside deviation (rf=0, %) | 14.1440 |
| Sortino (rf=0) | 1.8496 |
| Historical VaR 95% (1D, %) | 1.8026 |
| Historical ES 95% (1D, %) | 2.7901 |
| Correlation vs SPY | 0.2022 |
| Tracking error vs SPY (%) | 24.1789 |
| P/E (trailing) | 34.31 |
| P/B | 22.05 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 13.20 |
| Forward P/E (estimate) | 24.65 |
| Gross margin (%) | 97.68 |
| Operating margin (%) | 63.73 |
| Return on equity (%) | 63.51 |
| Free cash flow yield (%) | 2.66 |
| MA50 | 385.8428 |
| Close vs MA50 (%) | 9.5394 |
| MA200 | 343.9748 |
| Close vs MA200 (%) | 22.8724 |
| RSI (14, Wilder) | 63.2784 |
| MACD (12,26) | 11.9670 |
| MACD signal (9) | 10.9330 |
| MACD histogram | 1.0341 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'V': 277, 'SPY': 277}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 422.6500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.0142 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.1906 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 14.0325 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 21.2363 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 26.4335 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 22.9514 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.1440 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.8496 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.8026 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.7901 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2022 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.1789 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3425 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -17.1805 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1398 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 24.6550 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 97.6780 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 63.7280 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 63.5070 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.6609 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 34.3060 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 63.2784 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.0341 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 9.5394 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 22.8724 -> Clearly above the moving-average trend level.

## TAILWINDS

### Visa Inc Stock (V) Moved Up by 3.14% on Nov 2: What Investors Need To Know
- Summary: Shares rose 3.14% on Nov 2, indicating positive market sentiment.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxQbHJiazdqS3VVeVJpS2Rob2dNRUV2c3Y3WS0tSExLZzFkSVBmbWw3ZERwT05GLVRCcjctMnh6WWxlV2pWNzJldlJjUUVoa1dtMHJoS0RFTkhrNUJSVmR3M1diVkhkR2pTNEg0eTdtakRwSC1pOUw3bzRYRkw5MVQ5RElxQ2JKZjQ?oc=5>

### Visa Stock And Other Safe Havens for Crypto Flight to Safety
- Summary: Visa stock viewed as a safe haven amid crypto market volatility.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxQcmJGdUxpQUtVS3ZXZWIyRWtpSGk1S2RJQlhObjBWbXU3U044ZVhKeUV5dFl2MTg2cVpoUFJsdzh5eXBZeGFSU3NqU1BSY2JER1pxQ0E2aFFZRUNLcFZpVm16NFRfSVZZOTZwWTluSFdFLURCRFFIb2FaZjN3YTdtUUhhWks5YUw1ZUdfVGtIZFJfX05qZzk0YXRydTk3azN6U3pXQk9BQXptV1ZqWTlVS2xfaTJuT0ZVX0wtUG9VdjBHQdIBxwFBVV95cUxORGxqRlJjTnlJU0hwSU1va3o0Z3pqRFhUNmJGY2VfcGVoeDJiM2tSd25hSUN5ZkZaSFdBQzFTRlZXcWwzREZtTmxpNmRacmdUSFBBWm1QY1RmNGJvQmFQSHprTXdpLWNETHd3ZGlGR0d6dTRQSGl2d2tINV9wUFdnQUpwWGQ5WnpDUnpwalJrRWtiek1kT2hjNzAxc09Na0FQYWlaM0diMTJjUUs4S3dQM3lOZTBmOEdxUjVkYXh3QnZuSFdxa01J?oc=5>

## HEADWINDS

### Visa Stock Drops 3.8%, Shedding Nearly $28 Billion in One Session
- Summary: Visa Stock Drops 3.8%, Shedding Nearly $28 Billion in One Session
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTE5fT1NLR3lPeDJtLWNPQkQzM1Y2eEUweWx5Y3BPZHJfeXFCQVhWOW5JUHcycmRjNmlwWDhGRU4wVFRmbVZTU3ZLdEhaU2VVcHNtUWlZTEJnUk9rRlk2di1iamJnbmdONGtVSjBvOFRJNk5iV2ZMR0NSZmdBb2gzQQ?oc=5>

### Visa (NYSE:V) Stock Falls 3.3% - Here's Why
- Summary: Visa (NYSE:V) Stock Falls 3.3% - Here's Why
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQUEpYckR2d0x3OXIwaXhxajhOQ0Z6RzZ5VjNHM19GTDBsVTZ2YlMzMGNzRXR3TUYtcjJqeVNTcUFhbUdZZl9JdnhVeVpNMEdEZWtHQ1F6MlIxeVRDQTI2VkFscm9UbWF3Y19uOU9DXzJ3azNSVEFaTUJUQmI4M0lZWjZkV243ZHRoWTJlZlhIM21LNTBrZHBhRWhabVI?oc=5>

### Visa Inc Stock (V) Closed Down by 3.20% on Nov 5: Key Drivers Unveiled
- Summary: Visa stock fell 3.2% on Nov 5, citing key drivers.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxNLU9BLS1xM1p6VEFhS1dPejBMM3V0LWVkOVFSRUc3ajNKaGNFOHpIQmt1UzQtcXpQSjFxa2hOb210aEJkZ016M2VqeU1tUjB5cXVYQVBCa0ZfWTJqVTk0Z2dlMWNlU3oxZUJhN2szR2FkVHZGZUNremlFcmZrY2dIR0w2OFBjVGs?oc=5>

## CATALYSTS

### Visa (V) Q4 Earnings Justified Strong Growth But Left Valuation Questions
- Summary: Visa (V) Q4 Earnings Justified Strong Growth But Left Valuation Questions
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNakZsMnhhamx5d1UzNGRHMW9Ic2Nnc0VFNE1BRVd3QUt1UHlnbEUzMGdvaHdSUUNmcFhTQmhoVk1nVWR2WDRHOVRyZ1N0c1BBMmVSVjZxMXc3TFE2R0RHV3ZGV3ljTjViZ1ZrU0kzV0FydlZPb25OZjhyc1dReGM0MU5oaUJVMnBzLW1QS0x6YzVWc1ZWWDMzWg?oc=5>

### Visa (V) Stock Price Stalls After Q4 Earnings Beat
- Summary: Visa (V) Stock Price Stalls After Q4 Earnings Beat
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxQRmYzcXpPN1dXRkl4M2ZBOWhmR3QxVUZwR2hTTlpLRjczMnJ1Q1BybWpGT0VvYVBvSHNlZk5IUlQzYkVYdllLVXViSGVhS2dHbXUxZE1wVmkzanV6SXNrZTVwbGtiT0hYZC01ZVN6MDBIcUV5NV85WHI0bXJ6Z1laNS1mcGRJel9TQ2U5UGlxaV9RVGEzSGV6S1F5eVg2dnptQnNqSzBnZ0JOMXcxcEhYOHhUUTRiTlhubjIyY9IBwgFBVV95cUxQakl0U1FCSGgtcG5LVFJhcE5GOVZrVDdfZG1qNFpwekFuclhDSDZHYWFFX0VkeXAwdUx0NnBfUHRZM1o4MG5odVR6c0NqbFZFTmRSeWZpTV9NVWRUd3dyTzNvR29uZHQ0X2s2TU1Eb21VcFB1TGFVTXZHaWEyZy1YaWNiLXBHUWJvLU9qUE5PM1Vnd2NxMWdwMmZZTFJxN3pwZXlnMDBvVEpuWndHNm5GSUtHekJXVnk0S09wbFlEQkNkQQ?oc=5>

### Visa (V) Stock Looks Like A Bargain On Earnings Power
- Summary: Visa (V) Stock Looks Like A Bargain On Earnings Power
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxOVlhWMVR4dW4xc2NRdWdQYUpzYUZLQWthOXM0ZmNfaldOQzlGT1FvZG1RcUE5UkYycjNEUF9YbUkwYVVwUWY3OEZkMWk1ZXZEbkd3Z1hYc0ZzMVVkSTluOGYyLV9lbl9TQm1FbEY1Rk1hZU9YS2Q5ZU1ZSE5HWE05eEFfNmtKNVNTeU1YQVVyQUtvNTlrV2ZaTEU2cVJXcGhrSUc4cllybUQ2NEVrYzFaWWxLZ2F2NzFCbWtNc21DOE_SAcYBQVVfeXFMTkMtN1lFQmJIeHAyTjMwMzhLbDMyWUNkQ3RLSDBPUTBuMkFZb09mY0laQWdNSzlPS2Y3N0RubVY2eUlZaEtHdEY4SjBFMFhDcE85cF9XaXFlRDNkWk5SZU5BRXQ1cmxuM2c3UDhRcnJJVFQ2MDFEajMxbksybHo5LVhxSGpWVTRDY2ZSWHdRejZNVHd5VVRBSmJRSEtvOFRrcGNUMFdfLUNCT1Eya2pjOWlHZUc5X3diZmtvcU45NjZ6MmtoRXFn?oc=5>

### Visa Inc. $V Stock Acquired by Ascent Group LLC
- Summary: Visa Inc. $V Stock Acquired by Ascent Group LLC
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxQMjBibkFsOGNKNGI4d3JUOWdzTm52ZURlUnlZRzlIUUlUbEdqTG1IU2hWZzh5Zy1GX3lBbjNRQkZxWUNaLU5oT05iNDdPaHkyRk1tYmNuVVVPck44enVWcVQtQ1IzRElqc1R5ZUpaMElia2FOQTNrNnE3cFhMYkF0ZHVBWlJ3alIzWHpHbllBN09jSXB0MVZlNkZHOVNQZ2x4ZjZHbVktYXc3UQ?oc=5>

### Visa Inc. $V Stock Bought by Candriam S.C.A.
- Summary: Visa Inc. $V Stock Bought by Candriam S.C.A.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNakp3ajlGaUhIRUh4S3I2ajNFRE5iX1ZXMGhCTzNfVjRnRHliSDk3emxabWcwWl9zY05tM1FqZUwwSkk0cEkzT1hidVZ2WmNhU1A2OG9tekxZSm9pbnFjYldBbGhKekZQdjVYTzNGb3V5MTR1Qk5waWZHMnQ4V0Z6WnJTMHJoeDVBR1JzVmFhWmZwX0FldTZtTlQtM083bnZNU3c?oc=5>

### Visa Inc. $V Stock Sold by Boston Trust Walden Corp
- Summary: Visa Inc. $V Stock Sold by Boston Trust Walden Corp
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxPdTFpTHN3R2tBTE00anZLdkJTVm9wcUtKYi0xMDBhOVVGNnVITzc1aGVLU1FyazhJb0RwQ04yU0oydktJbXJZTDBkVzRqZGRTeVEwVUp0T3RLRzFyUnl1ZWpDYzlJRm1Ocy12bXRTSUV4SFplV2M2MVgyc0tjWU1TWVpTaWtob2dJTFV4ZEl4dE5oSV9WY0dfZkc5Znd2dFk0TE14S21yYzRjZHhiQlBF?oc=5>

### Visa Inc. $V Stock: AIA Group Ltd Increases Stake
- Summary: Visa Inc. $V Stock: AIA Group Ltd Increases Stake
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxOa01kRk1xSWNvSktKYmRhNUp1Y1J2RkN4YUEyVzhmLTBGYXpBOGVvclBPU3pkc0hfaU9lZWJUNjhqUjRtUmwzMjBtdEYxUFhjQVZYV3NtYkVVU2R2dEVmdDZCQWdyT3JuMy1mOVB2dnRCM3MzOXViX3AweDVWS2dLSWYtMk1rb05ycTZWQV9obXJQcnR0M1VhRFh5M0tnREdzOG9XeXRXZHdxRGc?oc=5>

### Visa Inc. $V Stock Sold by Trek Financial LLC
- Summary: Visa Inc. $V Stock Sold by Trek Financial LLC
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxQWE5ma3d5bFNlbDVmdDVTdkhReWd2YXVXTGRYS0F3RTdBRElOdXBxcXBDalIwY19CTXh4UzI4b2tLVWdmMnVHXzF4VFVIMFZwbDhLNkNjS1RHcEpoU1c0bmU4Z3FtVl80V05IWnJRcTZsVXhWNzJMeXVxRDVsRm5rWGZlMjB6ZExITDRjLWQwMkpwdjd5eXd5VklKVVhxeEFEbXNZaTFhbw?oc=5>

### Visa Inc. $V Stock Sold by Aware Super Pty Ltd as trustee of Aware Super
- Summary: Visa Inc. $V Stock Sold by Aware Super Pty Ltd as trustee of Aware Super
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxNUFdaRDVpczYwQVY5WFdKMGtJS0hzNVVZVkhuWjZPaFVVbkozUUhEOXdwV3RsdGRPVWljZTBURnBXa09mZXNtR0FwVF90aXY2T3BtVHd5azF5RFRuZ0k0TFRvV0lTb1BWODZRZDFhR0JmZDhvN1RNV2trV3RaWlpkbGM4bDRiZHhVVjRIWGM0ekpGdnJkcjlSZkhLTkc0V3VhM2JrdDFuUnVpM3lvTmprdkg1S0EyZ0l0U1p0ZDZKOU1XVElTbTl3a2F1QQ?oc=5>

### 48 ETFs Add to Visa (V) Holdings on Nov. 4
- Summary: Forty-eight ETFs increased Visa holdings.
- Date: 2026-11-06 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxOb05BZjhDQXlTWmVXcEEyLWtrVlpPTnppc2w0RXUzMHloMzNfMVlwZU9VQ0R2U2d3NDVDanB6Q2tLOTNzc1oxMWZBdFlQTGRYdF9JRHZJVWRaZXVYNnVVeThGS0hnMFR2RFBlMjZ6R3pCbnQ2N29FSXRGVm50RXMybWtoQkdIRTFkb2M4?oc=5>

### Visa's Solid Q4 Masks Rising Incentives: Is V Still Worth Buying?
- Summary: Analyst questions Visa's value amid Q4 results.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNSFN2WGVha3pNRTRuWWhYcUtERmFWWGZLUXFIR0dJWV9iU0NKMTBYY0s4RVg5Y0k3OHlJcFQ2cEhJYjMzZjJYajA3MlY1a3FleUU2UWdac2RucVZHU010T0lZWXFmcUU2cGIxLUV5UzVjYUNuVlE1YVZubElQQVl2VFBveFRHcEpGOWh4Sm5taTRHcFVKX2xz?oc=5>

### Truist Financial Issues Positive Forecast for Visa (NYSE:V) Stock Price
- Summary: Truist Financial predicts a positive outlook for Visa's stock, indicating potential upside.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxPZURreXZYSVNkWWNHZkxrbnFJc1oyQXBNeEhkcWJvN0pnVHc5WW80VGR0VUlad1cwdGlUWTBBamtQM25HYmI2NlJmUy10aWZ4V2IxY3MteWRpb00yUi16dGJMN1hvVXA3TWZvTFMyQm1oUndTWkVDT0c0dXFQNlFWUmhlT3RDbVdZZGpFUFQ5RDZfQkRUZ040Uk9WSkdKY3J2V2JyUVlFVnhGWjVzSjl4STBSd1dhOEhnaENyUy1uUW01UDM4WHFkdHA1RQ?oc=5>

### Visa Inc. $V Stock: Hikari Power Ltd Decreases Stake
- Summary: Hikari Power decreased its Visa holdings.
- Date: 2026-11-04 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxQLTRHdlVXZnN6NVk2Tmx5U1lhRk5Mb2JRXzJ4Q3BHRlZiblUwdlJBQkd4SWM3Ty14dDBVQUlXRGZ2Qm9BT1l2c25MY3NCYXBfSWxVaE56YzZCODQ3NFhYZ2tSRUM4OFJGOXlFejdqYnE3VGNiMjkyMW91dFQyUXU4YzBneXNGZkJTX2VKdi1UaFdGVXVQWVdPSkVuTkFLSTBkN1dRMkd5aXdDdW5zTnc4?oc=5>

### Visa Inc. $V Stock: Alps Advisors Inc. Trims Position
- Summary: Alps Advisors reduced its Visa stake.
- Date: 2026-11-07 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxPcG1tQ3RjVmZzcXRIZFd1M2lSNThra3JHRDJOUWNaTV9nMGZkeFVjX1p1MERWZkpRa1BMNnBoSTZ1YUlRdTJpaFR1YV9RcVhNT3lYWlFHUjk0UXVUaU11aGk5Ny1KMXhkakU1bU5NSTJpbVA4WU9TZG9OblgwQ1UxeW5GQTBLeTZDUFBZR21UUnBhNDBBbUlZeVpacTFUS3Vfa0gyZVJ1cUpadkFmUEFN?oc=5>

### Holiday shoppers plan an average of $777 for gifts as Visa says travel costs steer spending toward physical presents.
- Summary: Visa notes holiday shoppers plan $777 on gifts, attributing shift to travel costs driving physical present purchases.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxQT21EZE5vTW9oa0gwa0JXTkt1UUtFRlVtOHpPek0wZjNkQlhSS3QzTkpRSUhabUx0U3lrTExxcEhyU0FYZDQ4VVhzUl9xUjUtdHhycWdZdUJweWk3Mk8ycmRDeklnemRkYzVDN2lGNjRYYV83ZW9YMU4wUWVlSEFzMUxCU3pWcEgtbXFoVjNscnV0cXBhV1dwZGdfcnpNbHNIanVTZVVUWDV1WndYOHd1YmVEeGVrNHpt?oc=5>

### Insider trades: Netflix, Intel, Visa among notable names (V:NYSE)
- Summary: Insider trading activity involving Visa noted.
- Date: 2026-11-07 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPU1FaN0dLTS0xR2F6NmtmajJrblZBaHV2MGFEbURkU0x5Si1Jd2RadThjZWxIYjVwM0sxcHBsWGdtN2UwWHJvbGNvTkJzUkFLNkU5SXVESGNBWHZDUlZVSFR1QlF4R21yU3JUT25MUWNBLXBkSHVsdnBoTjVaMWpZVTBmV01JclZ6RWk4WlFIbFR1QlJNV1E?oc=5>

### Visa Inc. $V Stock: Ethic Inc. Boosts Stake
- Summary: Ethic Inc. increased its stake in Visa.
- Date: 2026-11-08 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNMnZ5SkpVSERZVWFFa1pfUXVFVkRydDNFVTYzVkNTeVpsVDR2QkRRakh4WXlUZmthaEwtcGM4VHpMNlVwSkUtcTVaZy1oeGE1aUwxMTlpdzFKUTc4ZXBWa3BvRWlULVRwaDliZ2Jqc0t2Zmo0Zk5keklpNzVWeklCUmI1Smp2YVluREtVUmg4TDJZRGsya1hMTUxkS3ZHWVBYVWc?oc=5>

### AI failed 42.8% of shopping test runs, Visa finds
- Summary: Visa reports high failure rate in AI shopping tests.
- Date: 2026-11-05 | Impact: low | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxQQ0x3UVNPbUo2OFN1TnczU3BId1QxYm5oQ1hRZEhjdkVjLWtxNElKTGRkNXJMSEd3ZVlVdmdtVTRKeXBVYUtTbnBqdm1MVU1PUDBhZm9ONmxGbm1ENEYwTGFIZTlPa3lGS0JIWEd4WWh3d2ZvX1BTclFwZmNSNC1nWVFnWlJYYWVyTVpRQWdDOEZhZHBfemc5dDZ4U2Y1ZlppUkxtbWptQWd3OS1aTnFDQzV1aDVhZGhoLVE?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **V** | **34.31** | **22.05** | **N/A** | **13.20** | **788,580,401,152.00 USD** | **26.43** |
| MA | 34.15 | 84.30 | 25.28 | 14.00 | 568,616,681,472.00 USD | 18.73 |
| PYPL | 11.31 | 2.55 | 8.15 | 2.00 | 49,208,201,216.00 USD | -9.60 |
| AXP | 18.08 | 6.02 | N/A | 11.30 | 215,240,474,624.00 USD | -11.24 |

Peers fetched as_of: 2026-11-08; V reuses existing data (market data as_of: 2026-11-06); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-27
- Next expected earnings: 2027-01-26 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-08

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-11-05
- Revenue (latest available single quarter): 5,840,000,000.00 USD; period 2019-04-01/2019-06-30; fiscal year/reporting period 2019/Q3
- Net income (latest available single quarter): 5,628,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1403161/000140316126000134/v-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMihwFBVV95cUxQbHJiazdqS3VVeVJpS2Rob2dNRUV2c3Y3WS0tSExLZzFkSVBmbWw3ZERwT05GLVRCcjctMnh6WWxlV2pWNzJldlJjUUVoa1dtMHJoS0RFTkhrNUJSVmR3M1diVkhkR2pTNEg0eTdtakRwSC1pOUw3bzRYRkw5MVQ5RElxQ2JKZjQ?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxQcmJGdUxpQUtVS3ZXZWIyRWtpSGk1S2RJQlhObjBWbXU3U044ZVhKeUV5dFl2MTg2cVpoUFJsdzh5eXBZeGFSU3NqU1BSY2JER1pxQ0E2aFFZRUNLcFZpVm16NFRfSVZZOTZwWTluSFdFLURCRFFIb2FaZjN3YTdtUUhhWks5YUw1ZUdfVGtIZFJfX05qZzk0YXRydTk3azN6U3pXQk9BQXptV1ZqWTlVS2xfaTJuT0ZVX0wtUG9VdjBHQdIBxwFBVV95cUxORGxqRlJjTnlJU0hwSU1va3o0Z3pqRFhUNmJGY2VfcGVoeDJiM2tSd25hSUN5ZkZaSFdBQzFTRlZXcWwzREZtTmxpNmRacmdUSFBBWm1QY1RmNGJvQmFQSHprTXdpLWNETHd3ZGlGR0d6dTRQSGl2d2tINV9wUFdnQUpwWGQ5WnpDUnpwalJrRWtiek1kT2hjNzAxc09Na0FQYWlaM0diMTJjUUs4S3dQM3lOZTBmOEdxUjVkYXh3QnZuSFdxa01J?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTE5fT1NLR3lPeDJtLWNPQkQzM1Y2eEUweWx5Y3BPZHJfeXFCQVhWOW5JUHcycmRjNmlwWDhGRU4wVFRmbVZTU3ZLdEhaU2VVcHNtUWlZTEJnUk9rRlk2di1iamJnbmdONGtVSjBvOFRJNk5iV2ZMR0NSZmdBb2gzQQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQUEpYckR2d0x3OXIwaXhxajhOQ0Z6RzZ5VjNHM19GTDBsVTZ2YlMzMGNzRXR3TUYtcjJqeVNTcUFhbUdZZl9JdnhVeVpNMEdEZWtHQ1F6MlIxeVRDQTI2VkFscm9UbWF3Y19uOU9DXzJ3azNSVEFaTUJUQmI4M0lZWjZkV243ZHRoWTJlZlhIM21LNTBrZHBhRWhabVI?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxNLU9BLS1xM1p6VEFhS1dPejBMM3V0LWVkOVFSRUc3ajNKaGNFOHpIQmt1UzQtcXpQSjFxa2hOb210aEJkZ016M2VqeU1tUjB5cXVYQVBCa0ZfWTJqVTk0Z2dlMWNlU3oxZUJhN2szR2FkVHZGZUNremlFcmZrY2dIR0w2OFBjVGs?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNakZsMnhhamx5d1UzNGRHMW9Ic2Nnc0VFNE1BRVd3QUt1UHlnbEUzMGdvaHdSUUNmcFhTQmhoVk1nVWR2WDRHOVRyZ1N0c1BBMmVSVjZxMXc3TFE2R0RHV3ZGV3ljTjViZ1ZrU0kzV0FydlZPb25OZjhyc1dReGM0MU5oaUJVMnBzLW1QS0x6YzVWc1ZWWDMzWg?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxQRmYzcXpPN1dXRkl4M2ZBOWhmR3QxVUZwR2hTTlpLRjczMnJ1Q1BybWpGT0VvYVBvSHNlZk5IUlQzYkVYdllLVXViSGVhS2dHbXUxZE1wVmkzanV6SXNrZTVwbGtiT0hYZC01ZVN6MDBIcUV5NV85WHI0bXJ6Z1laNS1mcGRJel9TQ2U5UGlxaV9RVGEzSGV6S1F5eVg2dnptQnNqSzBnZ0JOMXcxcEhYOHhUUTRiTlhubjIyY9IBwgFBVV95cUxQakl0U1FCSGgtcG5LVFJhcE5GOVZrVDdfZG1qNFpwekFuclhDSDZHYWFFX0VkeXAwdUx0NnBfUHRZM1o4MG5odVR6c0NqbFZFTmRSeWZpTV9NVWRUd3dyTzNvR29uZHQ0X2s2TU1Eb21VcFB1TGFVTXZHaWEyZy1YaWNiLXBHUWJvLU9qUE5PM1Vnd2NxMWdwMmZZTFJxN3pwZXlnMDBvVEpuWndHNm5GSUtHekJXVnk0S09wbFlEQkNkQQ?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxOVlhWMVR4dW4xc2NRdWdQYUpzYUZLQWthOXM0ZmNfaldOQzlGT1FvZG1RcUE5UkYycjNEUF9YbUkwYVVwUWY3OEZkMWk1ZXZEbkd3Z1hYc0ZzMVVkSTluOGYyLV9lbl9TQm1FbEY1Rk1hZU9YS2Q5ZU1ZSE5HWE05eEFfNmtKNVNTeU1YQVVyQUtvNTlrV2ZaTEU2cVJXcGhrSUc4cllybUQ2NEVrYzFaWWxLZ2F2NzFCbWtNc21DOE_SAcYBQVVfeXFMTkMtN1lFQmJIeHAyTjMwMzhLbDMyWUNkQ3RLSDBPUTBuMkFZb09mY0laQWdNSzlPS2Y3N0RubVY2eUlZaEtHdEY4SjBFMFhDcE85cF9XaXFlRDNkWk5SZU5BRXQ1cmxuM2c3UDhRcnJJVFQ2MDFEajMxbksybHo5LVhxSGpWVTRDY2ZSWHdRejZNVHd5VVRBSmJRSEtvOFRrcGNUMFdfLUNCT1Eya2pjOWlHZUc5X3diZmtvcU45NjZ6MmtoRXFn?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxQMjBibkFsOGNKNGI4d3JUOWdzTm52ZURlUnlZRzlIUUlUbEdqTG1IU2hWZzh5Zy1GX3lBbjNRQkZxWUNaLU5oT05iNDdPaHkyRk1tYmNuVVVPck44enVWcVQtQ1IzRElqc1R5ZUpaMElia2FOQTNrNnE3cFhMYkF0ZHVBWlJ3alIzWHpHbllBN09jSXB0MVZlNkZHOVNQZ2x4ZjZHbVktYXc3UQ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNakp3ajlGaUhIRUh4S3I2ajNFRE5iX1ZXMGhCTzNfVjRnRHliSDk3emxabWcwWl9zY05tM1FqZUwwSkk0cEkzT1hidVZ2WmNhU1A2OG9tekxZSm9pbnFjYldBbGhKekZQdjVYTzNGb3V5MTR1Qk5waWZHMnQ4V0Z6WnJTMHJoeDVBR1JzVmFhWmZwX0FldTZtTlQtM083bnZNU3c?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxPdTFpTHN3R2tBTE00anZLdkJTVm9wcUtKYi0xMDBhOVVGNnVITzc1aGVLU1FyazhJb0RwQ04yU0oydktJbXJZTDBkVzRqZGRTeVEwVUp0T3RLRzFyUnl1ZWpDYzlJRm1Ocy12bXRTSUV4SFplV2M2MVgyc0tjWU1TWVpTaWtob2dJTFV4ZEl4dE5oSV9WY0dfZkc5Znd2dFk0TE14S21yYzRjZHhiQlBF?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxOa01kRk1xSWNvSktKYmRhNUp1Y1J2RkN4YUEyVzhmLTBGYXpBOGVvclBPU3pkc0hfaU9lZWJUNjhqUjRtUmwzMjBtdEYxUFhjQVZYV3NtYkVVU2R2dEVmdDZCQWdyT3JuMy1mOVB2dnRCM3MzOXViX3AweDVWS2dLSWYtMk1rb05ycTZWQV9obXJQcnR0M1VhRFh5M0tnREdzOG9XeXRXZHdxRGc?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxQWE5ma3d5bFNlbDVmdDVTdkhReWd2YXVXTGRYS0F3RTdBRElOdXBxcXBDalIwY19CTXh4UzI4b2tLVWdmMnVHXzF4VFVIMFZwbDhLNkNjS1RHcEpoU1c0bmU4Z3FtVl80V05IWnJRcTZsVXhWNzJMeXVxRDVsRm5rWGZlMjB6ZExITDRjLWQwMkpwdjd5eXd5VklKVVhxeEFEbXNZaTFhbw?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxNUFdaRDVpczYwQVY5WFdKMGtJS0hzNVVZVkhuWjZPaFVVbkozUUhEOXdwV3RsdGRPVWljZTBURnBXa09mZXNtR0FwVF90aXY2T3BtVHd5azF5RFRuZ0k0TFRvV0lTb1BWODZRZDFhR0JmZDhvN1RNV2trV3RaWlpkbGM4bDRiZHhVVjRIWGM0ekpGdnJkcjlSZkhLTkc0V3VhM2JrdDFuUnVpM3lvTmprdkg1S0EyZ0l0U1p0ZDZKOU1XVElTbTl3a2F1QQ?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxOb05BZjhDQXlTWmVXcEEyLWtrVlpPTnppc2w0RXUzMHloMzNfMVlwZU9VQ0R2U2d3NDVDanB6Q2tLOTNzc1oxMWZBdFlQTGRYdF9JRHZJVWRaZXVYNnVVeThGS0hnMFR2RFBlMjZ6R3pCbnQ2N29FSXRGVm50RXMybWtoQkdIRTFkb2M4?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNSFN2WGVha3pNRTRuWWhYcUtERmFWWGZLUXFIR0dJWV9iU0NKMTBYY0s4RVg5Y0k3OHlJcFQ2cEhJYjMzZjJYajA3MlY1a3FleUU2UWdac2RucVZHU010T0lZWXFmcUU2cGIxLUV5UzVjYUNuVlE1YVZubElQQVl2VFBveFRHcEpGOWh4Sm5taTRHcFVKX2xz?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxPZURreXZYSVNkWWNHZkxrbnFJc1oyQXBNeEhkcWJvN0pnVHc5WW80VGR0VUlad1cwdGlUWTBBamtQM25HYmI2NlJmUy10aWZ4V2IxY3MteWRpb00yUi16dGJMN1hvVXA3TWZvTFMyQm1oUndTWkVDT0c0dXFQNlFWUmhlT3RDbVdZZGpFUFQ5RDZfQkRUZ040Uk9WSkdKY3J2V2JyUVlFVnhGWjVzSjl4STBSd1dhOEhnaENyUy1uUW01UDM4WHFkdHA1RQ?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxQLTRHdlVXZnN6NVk2Tmx5U1lhRk5Mb2JRXzJ4Q3BHRlZiblUwdlJBQkd4SWM3Ty14dDBVQUlXRGZ2Qm9BT1l2c25MY3NCYXBfSWxVaE56YzZCODQ3NFhYZ2tSRUM4OFJGOXlFejdqYnE3VGNiMjkyMW91dFQyUXU4YzBneXNGZkJTX2VKdi1UaFdGVXVQWVdPSkVuTkFLSTBkN1dRMkd5aXdDdW5zTnc4?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxPcG1tQ3RjVmZzcXRIZFd1M2lSNThra3JHRDJOUWNaTV9nMGZkeFVjX1p1MERWZkpRa1BMNnBoSTZ1YUlRdTJpaFR1YV9RcVhNT3lYWlFHUjk0UXVUaU11aGk5Ny1KMXhkakU1bU5NSTJpbVA4WU9TZG9OblgwQ1UxeW5GQTBLeTZDUFBZR21UUnBhNDBBbUlZeVpacTFUS3Vfa0gyZVJ1cUpadkFmUEFN?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxQT21EZE5vTW9oa0gwa0JXTkt1UUtFRlVtOHpPek0wZjNkQlhSS3QzTkpRSUhabUx0U3lrTExxcEhyU0FYZDQ4VVhzUl9xUjUtdHhycWdZdUJweWk3Mk8ycmRDeklnemRkYzVDN2lGNjRYYV83ZW9YMU4wUWVlSEFzMUxCU3pWcEgtbXFoVjNscnV0cXBhV1dwZGdfcnpNbHNIanVTZVVUWDV1WndYOHd1YmVEeGVrNHpt?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPU1FaN0dLTS0xR2F6NmtmajJrblZBaHV2MGFEbURkU0x5Si1Jd2RadThjZWxIYjVwM0sxcHBsWGdtN2UwWHJvbGNvTkJzUkFLNkU5SXVESGNBWHZDUlZVSFR1QlF4R21yU3JUT25MUWNBLXBkSHVsdnBoTjVaMWpZVTBmV01JclZ6RWk4WlFIbFR1QlJNV1E?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNMnZ5SkpVSERZVWFFa1pfUXVFVkRydDNFVTYzVkNTeVpsVDR2QkRRakh4WXlUZmthaEwtcGM4VHpMNlVwSkUtcTVaZy1oeGE1aUwxMTlpdzFKUTc4ZXBWa3BvRWlULVRwaDliZ2Jqc0t2Zmo0Zk5keklpNzVWeklCUmI1Smp2YVluREtVUmg4TDJZRGsya1hMTUxkS3ZHWVBYVWc?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxQQ0x3UVNPbUo2OFN1TnczU3BId1QxYm5oQ1hRZEhjdkVjLWtxNElKTGRkNXJMSEd3ZVlVdmdtVTRKeXBVYUtTbnBqdm1MVU1PUDBhZm9ONmxGbm1ENEYwTGFIZTlPa3lGS0JIWEd4WWh3d2ZvX1BTclFwZmNSNC1nWVFnWlJYYWVyTVpRQWdDOEZhZHBfemc5dDZ4U2Y1ZlppUkxtbWptQWd3OS1aTnFDQzV1aDVhZGhoLVE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
