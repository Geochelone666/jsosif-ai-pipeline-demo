# AMZN Intelligence Report

- ticker: **AMZN**
- Report as_of: **2026-11-16**
- Market data as_of: **2026-11-16**
- Quant sources: https://finance.yahoo.com/quote/AMZN/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMZN/key-statistics/
- AI analysis snapshot as_of: **2026-11-16**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-17T06:48:19.624432+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 9, 'ai': 11, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261116T043911Z-b81cfeb4/AMZN** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **3**; {'low_uncalibrated_model_confidence': 2, 'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 9 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 37.5%; oldest publication 2026-11-12

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 257.7500 |
| Return 1D (%) | -3.3413 |
| Return 1W (%) | -3.4391 |
| Return 1M (%) | 3.1000 |
| Return YTD (%) | 11.6671 |
| Return 1Y (%) | 9.8257 |
| Annualized volatility (%) | 34.0915 |
| Beta vs SPY | 1.3315 |
| Max drawdown (%) | -19.6419 |
| Sharpe (rf=0) | 0.4668 |
| Downside deviation (rf=0, %) | 21.0911 |
| Sortino (rf=0) | 0.7545 |
| Historical VaR 95% (1D, %) | 3.0804 |
| Historical ES 95% (1D, %) | 4.0960 |
| Correlation vs SPY | 0.5377 |
| Tracking error vs SPY (%) | 29.1041 |
| P/E (trailing) | 20.84 |
| P/B | 4.54 |
| EV/EBITDA | 16.21 |
| Revenue growth (%) | 12.10 |
| Forward P/E (estimate) | 23.59 |
| Gross margin (%) | 51.37 |
| Operating margin (%) | 13.09 |
| Return on equity (%) | 27.42 |
| Free cash flow yield (%) | -1.25 |
| MA50 | 254.7964 |
| Close vs MA50 (%) | 1.1592 |
| MA200 | 244.6878 |
| Close vs MA200 (%) | 5.3383 |
| RSI (14, Wilder) | 49.6298 |
| MACD (12,26) | 2.9141 |
| MACD signal (9) | 2.0225 |
| MACD histogram | 0.8916 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMZN': 283, 'SPY': 283}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 257.7500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -3.3413 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -3.4391 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 3.1000 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 11.6671 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 9.8257 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 34.0915 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.0911 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.7545 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.0804 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.0960 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5377 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 29.1041 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.3315 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -19.6419 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.4668 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 23.5903 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 51.3740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 13.0870 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 27.4160 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: -1.2462 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 20.8367 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 49.6298 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.8916 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 1.1592 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 5.3383 -> Clearly above the moving-average trend level.

## TAILWINDS

### Amazon's Zoox robotaxis available in Las Vegas on Uber app (AMZN:NASDAQ)
- Summary: Amazon launches Zoox robotaxis in Las Vegas via Uber app, expanding autonomous vehicle presence.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPYlZzWFQ4TjNseTgtc2pLNjRiR3VjT1pYZzcwU0VvR3ZhTERHdjk4MjQzVHR0Y2lXYldLajFFRzVoUTlVLXgwVUlIRzlDNVBpZ1UxX0NWeXRxeGo0anBEcUVXV2tuTzM1c3Vpbk1XTjItT0JYQl95WEt0Ml9fQkp4dE5mbVVyeHcyTF9QclFSZ0FqMW1mLXp6djNoQQ?oc=5>

## HEADWINDS

### Amazon (AMZN) Stock Price Prediction: Pullback Holds Near Support as Bulls Defend the $260s
- Summary: Analysts predict a pullback near support, with bulls defending $260 levels, indicating potential short-term volatility.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNYXJzYWNUNkx1eFd5aElDY1RPZWM4b1l4TV9GNkZ4dEU2XzBBNnM1SkxXV2VPLUd3WnItQmhmREpudWJqOXVLTTJzQjJqSjVaNWxlY1gwU0wzTzRHRTlteVVrSUFLN0JqSXByUzExQzhPNkF5YmgyamNtRTZHSFdBLVJtSUlxd3ZXY0F6blBBM2JyTmtLSDJ4Tk9NNk8?oc=5>

## CATALYSTS

### Amazon (AMZN) Has Its First Binding Union Contract In North America
- Summary: Amazon (AMZN) Has Its First Binding Union Contract In North America
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxORjJSY19uVEtwcExrMnJnbUlhRWVRWWF3Mm42VkRLbk5HdGxOeXh1U0VTb1d4dF94dDZXT2tHbDVXSi1JYnVpM0dvaEw1dkVwOFdjRUtyR2lISTF1S1pHNW95R1VXeEtiOFJoZ1FLV0Y2akZ6Z2FPNGk5UHdCUmdOMFN3TGFfVnpwQno5YVVsVktGQk9aQWZLTm0xeWU?oc=5>

### Amazon Has Quietly Recouped Its Post Q3 Earnings Losses. AMZN Stock Could Hit $300 Next.
- Summary: Amazon Has Quietly Recouped Its Post Q3 Earnings Losses. AMZN Stock Could Hit $300 Next.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxNVDFMMWpzTHFWNVpraFphOVZad0Rza2psdnFrb3UwU2FES3JEZ2VaNHNudE80T2NOejIwTDJUaXJBMFdFSzNQZjFNYXZmc2tucTlPUXFobVpRLUJva2lGb0ItbVR1SkktLWhuaXRaUDA2VVV5SlJpSE5zaldBd19fSE5LNDFRbWZuLUZNT3l4VkRtTVRjRFIwNy15ZzdNWXZSSkg2TVFtUmN6Y2ZwbF9oaFJoby1ORER1UmRXVkNhQjRVaTF6b3dqMg?oc=5>

### Amazon's AWS Strikes $5B Data Center Deal With Blackstone Digital — A Look At Some Key Highlights
- Summary: Amazon's AWS Strikes $5B Data Center Deal With Blackstone Digital — A Look At Some Key Highlights
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi6wFBVV95cUxQYWpDWEtMSURuaFB3c0R0TlNfOHlXSG1WbXlxejNYQl9YQjdXNjFxLVhGYU9lUlhQMjJyY3hORlFjZ3hBVHhyVmdtWlpmQmcxUEtrMnItVFdqYVFkVEVaMDdnUC0yTVhkYklkcGFWZVFlV2JxSFlUZ1lXVlFqSDNWZXY2LWlONlR3WFpObUtXc1V6N2x5TXFFbXdfOG5HeloydHdYQmZCMDlwN0pUWUc4V0pESGZ5N2tYVUk5cWtmSE9JbEotQVoxanFaVEQzYW5XNWVzSHJiVDZCdEFYZ0pZa2dtREp5OHRBNVkw?oc=5>

### Amazon.com, Inc. $AMZN Stock Bought by Choreo LLC
- Summary: Amazon.com, Inc. $AMZN Stock Bought by Choreo LLC
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxQLTVpeDlvVDBRTU5UaC1ya1RxOWFzcnppYjE4MEdRZ2hJYkc3dEJIaE5qT1dzUG0tSTZ6WHEzdUFNeDdCdUw0cW9FZF94cE1SNkFzQU1NcHZZeFQtcnZJUmFNM1h3TUsyUkZzOVNUZk9iTVhtNTgtOHhXT3p2dG13dXQ1aTIxR0tjQmR5ai1idHlaOGFsX3JSejdTYzlvOWJ6b1ZlTHptQjhNZw?oc=5>

### Amazon.com, Inc. $AMZN Shares Sold by Crystal Rock Capital Management
- Summary: Amazon.com, Inc. $AMZN Shares Sold by Crystal Rock Capital Management
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxOMnBndVV6UWNNNGE2SUd1VnV1Z0RqZVRYWnhUVzdpS21tTDVwM25HUjE2cDlvNXplaG9MV0JTbU13c3dCTmZEbXRZTk9MdUFybERqMV9qbzFKdFJ0cTZ2Sy1SQm55STZsVF9RNGNNVEZadk5XY29oRDQ2azRvNGJSdDFXaElIRnJra1hyMEFTWFhZOEtqaTFseFVHOGRtTXdYZVR0ZElVeWt6N2c3dEI5LUJzRmg0VWlya2cxVVV0eTRocjRP?oc=5>

### Amazon.com, Inc. $AMZN Shares Sold by Fishman Jay A Ltd. MI
- Summary: Amazon.com, Inc. $AMZN Shares Sold by Fishman Jay A Ltd. MI
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxOZ01fZmpmTEdCTENCWE1IZm9rbGpQZXllT0VMOHJ2aGVCYktMOEJvd0VUTXVuNXRIYzcybWRiclVlSnhHUzg2c25YcU9LSGp4UndIZ25OZUU4NVlMZi0tZHA3UWRtRGNDUW5tN3loNlplQXl3WFI0UWc5SkJPd1ROa21QNThKejIyeHlSR1liTml2d19fNlBkRnNtTVRvWW9hdWM1STFIM2pIal9HejJneUxOcEIzUQ?oc=5>

### Amazon.com, Inc. $AMZN Stock: VestGen Advisors LLC Reduces Stake
- Summary: Amazon.com, Inc. $AMZN Stock: VestGen Advisors LLC Reduces Stake
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxQQ2NYcEpZVmJ4VnhJcFgtRlVSZHh2VmxLS2QzZ0pIbUpjU0liS1Zvb1JFX3dJblc2MzdBeXY4QlRoRlA0bTZncmpNUG5jUjNxamN2OG5UU2k5YnRQdXd6U3Q1SE5tMHB3T3EyVFF5a3pEQzFySUp5MFdCV2Q0Y1FWWm9uc1kzWFRNRWtpbFh0ZzJJUm90TVNMdEZiWEhSZS1jZV9ZSC1tSU52aTF5NXB4bjdhWGNMTWZSN1Z4QQ?oc=5>

### Amazon.com, Inc. $AMZN Stock: WestEnd Advisors LLC Reduces Stake
- Summary: Amazon.com, Inc. $AMZN Stock: WestEnd Advisors LLC Reduces Stake
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxQM3AyVmJoNy02Wnczek52endTSkZJaHVGNmszR2dtbTZLX3VxRG1SNVVmYTI4bDhqLTVweW1jdW8tYW85Nmgzc25qcmNCWEFmaUtBR3BaR05ZWnhNWEt3NXIyaFNOaEZxbVZNRHlRcWZ4QU40S3JpWmtCS19Obl9aSTNwSkNmR3IxQmtxSUVOQ0s5ZFBVR0FLR1NJYnNzUW9yU0RhOGtzeWJUTm9NbUcwcUFCNzEzQlVJZjF1SQ?oc=5>

### Amazon.com, Inc. $AMZN Shares Sold by ICW Investment Advisors LLC
- Summary: Amazon.com, Inc. $AMZN Shares Sold by ICW Investment Advisors LLC
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxQOVItUFd1MFJQV2l6WElQLWFJNnpXZ01TNVhRdXE3WWNmTEg2d1ZTTmlzU0xsZHAxNUEwRlY4UXVMY1dHMllacjdsdkJidjI5bW9DLXJRemVXQUlHeXQzVnRwTUo4d25fOUxqd1BJQ2ZTQnhvTVhOY0VGSFdRcHhxSUZZTV9KZUFJUHE4MHdTdVJBZ1E0YXlQcnRSenBlTFg5SmktUFdPUWZxU2c3LXlBUnoyR01neW0wUjU1aG9FZw?oc=5>

### Amazon.com, Inc. $AMZN Stock: Sigma Investment Counselors Inc. Grows Position
- Summary: Investment firm increases Amazon holdings, signaling confidence.
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxNRFhzZ3ljMXpNQU54ZzVEN0kzWV9wVjVWUnZLSTdSa0xkS1FnVEFDdWd1QVZzc3RraEZ6VHVjcnVrODgyMmVmbDMzX2lSZlp0QkRiRThmN2V1OTBmR0xiZXZmcWFSajg2SHRaeVpLMTFtSU8wMUp3NmYyakg1VkIzYnNhOVdrM3p2MjNabmwxb2txcmNzWG01anVCR0gyOHV0VzVrMUFrQjhSQmV1eDB3YkpQWlVNSFFDeHhqSldjTjBJNTg5TWlHTF9BZXU?oc=5>

### What's Wrong With Amazon.com (AMZN) Stock, and Is It a Buy in November?
- Summary: Analysis questioning Amazon's valuation and potential upside.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOMFl3MDR4U2RDeG1zaEdBOFNtN2dHYnVZYTNwdkIwVk1YaVVEaFFJR0dSM19kaUVzbU1PQVVRcHZIWEZLb0czYXZlUXJzOU1ybWtlTWRyR3ducktjeG5NS08xTXJTTkNfMjNrM2h6UHk3ekNvNWNwTHhrQzBwd1JLZjdKSzdrYWhQZXZPNjBFZGJhemlUMlE4?oc=5>

### 007 watch: Amazon MGM Studios picks Robert Pattinson as the new James Bond (AMZN:NASDAQ)
- Summary: Amazon MGM Studios announces Robert Pattinson as new James Bond, expanding its film portfolio.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxPazJNWUw5MENoN0loUXJCblNqSUFYV3N2ekFaQ1VXaVVReU1WVTdiNWg3a0VQTlNUeS1pNHBuZFU4NmpELXFhZ3RJc0o4WHZ4ZzFBeDBkcWJSN0RfTVpaWC14UHE3UF82OGIxN1JnYWlRcWJJaW01bDMwcTUzbjdzdEJrX2hvQUk4ZElTRjlfczUzTGRwdGdLWUNOLUFsQjI4OWN2WUUtX3R4eVh1T0RuMQ?oc=5>

### Something Is Changing at Amazon, and Investors Should Pay Attention
- Summary: Article highlights upcoming changes at Amazon, suggesting potential positive developments.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxOXzRxVXc5QXUxaFlGVFQwSmpUSXdFTjJRdWV6YnNWYUFYZnBBQ0tZRW5famE0cS1kc1h1dGpkSzdIUzg1TnVGTGMzT0ZQdDdNZmZDVEk1RDNBRnQzM2RxeUFEa0QxVWp2d3plM1V5YXBqSGh0ckhUbVFtLUxQYXlsbEJ1azRGcGZFSnpWMEFTempvWW1HVnVlV3NGd0ZlWlhuckhGQ1R5XzJ0dmJfclRF?oc=5>

### What Could Lift Amazon Stock From Here?
- Summary: Speculative piece on factors that could boost Amazon's stock performance.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPdnhpdEhzanE4RkFZb3FsR1hjYl93aktwY3hjV0NCQ1EtQzBBbDRMSzgzYjZoVEdKS2c1ZWU0RTRoMVd5Si1pSlR5R0VaOXQwRVByX1YzdUhLV1djN2ZoSmF1OTAycm5kanF1Y014ZXBSbVp0Q3Nqd0RmWjdJaEFtM3ptUDZsT25temNOTEY3YncxMU1SOHpzSU5fU0JNbjRT?oc=5>

## RISKS

### Amazon: AI Bet Getting Riskier (NASDAQ:AMZN)
- Summary: Amazon is increasing its AI investment, raising potential risks to its operations and financials.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiekFVX3lxTE1COEZ0M0p2RHl5US1uaEtOckxaRlRXUXRMc1hlR01pNE4yV0NGTHJIb0Vma3FzZUtKX3RCbVg3ZmpUNHpnaHJZeTBjVFV0YmdFWDc0R2N5RFRObTY0bllEUU15N0J0aGFkUWdNdF9HOHg0WWtMSDJpdTl3?oc=5>

### Rocket failure destroys 40 Amazon satellites, threatening broadband rollout (AMZN:NASDAQ)
- Summary: Satellite launch failure threatens Amazon's broadband expansion.
- Date: 2026-11-15 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxPWDhBeDRCZ21nOExrVzluVTk3dWpYQlE2VGgtSVUyRFdXSUI0VVJybVNQTms5V2czZjNtRE1QZ0xTM2NwUWwyUmNsSS10dm5CVE5PeGJ1QVl2djlXNFI2NVhKN0F6YVVfdEF1aE1lWUw2ZFEyT1B5VWM4WVF6VUVncDVfSGE0bzA2RjZrSjdwX3ZlSDhISVRQT2Vzc3pFZlVKVFNmRDNJaG5vcGxVTjhZX2h3?oc=5>

### Amazon: The Age Of Inference (And Big E-Commerce Profits) (NASDAQ:AMZN)
- Summary: Amazon's inference tech promises growth but may face execution risk.
- Date: 2026-11-16 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNQnRLX2xlM3NNZ3ctbTl3OF9OdlRwYktiRHBTeUN1bjZNRG0yTFBYaGw5OTdaVXRHcEVrMWt6WlRJWXpLT05xVEJoSFJnUEgxSDg0R1pmYXFMMWlYX2U2QU5kWlZtTUx0eWpWVjFxSnNaNWhRS0tIWUdOUkRkZk5td2dRanFxR1ZyNklUS2hpUXJKS1hT?oc=5>

### Amazon.com (NASDAQ:AMZN) Stock Price Down 3.3% - Should You Sell?
- Summary: AMZN shares fell 3.3%, raising concerns about short-term valuation.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxOS05wcnAyTFFOemYzZjloNG1NMkM3UFU5ZThNZnlCMy1Tc0JiYVNsYW5VdEljYmdod2hKdGwzZTU1UzV6WU5uNUNBVGxhb2xKdS12enBrSWdFakRnczQzb1FzSWVaLUNqTGo2a1FSNk1mMzBLRnpTbGZXci01LUdMam1wY1N5b3JTdURKakFRSjQ0cHlPaDc4Ynk4Z0d6dFdPSG1iZjZuSXVOaUZXcTVwRUxscktxZnV6?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMZN** | **20.84** | **4.54** | **16.21** | **12.10** | **2,787,086,172,160.00 USD** | **9.83** |
| WMT | 46.53 | 10.38 | 24.71 | 5.90 | 1,021,896,949,760.00 USD | 26.36 |
| MSFT | 27.03 | 8.18 | 19.04 | 18.80 | 3,846,694,502,400.00 USD | 2.37 |
| GOOGL | 14.82 | 5.29 | 18.28 | 24.70 | 3,488,053,460,992.00 USD | 2.91 |

Peers fetched as_of: 2026-11-16; AMZN reuses existing data (market data as_of: 2026-11-16); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-29
- Next expected earnings: 2027-02-04 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-16

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-30
- Revenue (latest available single quarter): 201,944,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 20,685,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimwFBVV95cUxPYlZzWFQ4TjNseTgtc2pLNjRiR3VjT1pYZzcwU0VvR3ZhTERHdjk4MjQzVHR0Y2lXYldLajFFRzVoUTlVLXgwVUlIRzlDNVBpZ1UxX0NWeXRxeGo0anBEcUVXV2tuTzM1c3Vpbk1XTjItT0JYQl95WEt0Ml9fQkp4dE5mbVVyeHcyTF9QclFSZ0FqMW1mLXp6djNoQQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNYXJzYWNUNkx1eFd5aElDY1RPZWM4b1l4TV9GNkZ4dEU2XzBBNnM1SkxXV2VPLUd3WnItQmhmREpudWJqOXVLTTJzQjJqSjVaNWxlY1gwU0wzTzRHRTlteVVrSUFLN0JqSXByUzExQzhPNkF5YmgyamNtRTZHSFdBLVJtSUlxd3ZXY0F6blBBM2JyTmtLSDJ4Tk9NNk8?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxORjJSY19uVEtwcExrMnJnbUlhRWVRWWF3Mm42VkRLbk5HdGxOeXh1U0VTb1d4dF94dDZXT2tHbDVXSi1JYnVpM0dvaEw1dkVwOFdjRUtyR2lISTF1S1pHNW95R1VXeEtiOFJoZ1FLV0Y2akZ6Z2FPNGk5UHdCUmdOMFN3TGFfVnpwQno5YVVsVktGQk9aQWZLTm0xeWU?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxNVDFMMWpzTHFWNVpraFphOVZad0Rza2psdnFrb3UwU2FES3JEZ2VaNHNudE80T2NOejIwTDJUaXJBMFdFSzNQZjFNYXZmc2tucTlPUXFobVpRLUJva2lGb0ItbVR1SkktLWhuaXRaUDA2VVV5SlJpSE5zaldBd19fSE5LNDFRbWZuLUZNT3l4VkRtTVRjRFIwNy15ZzdNWXZSSkg2TVFtUmN6Y2ZwbF9oaFJoby1ORER1UmRXVkNhQjRVaTF6b3dqMg?oc=5
- https://news.google.com/rss/articles/CBMi6wFBVV95cUxQYWpDWEtMSURuaFB3c0R0TlNfOHlXSG1WbXlxejNYQl9YQjdXNjFxLVhGYU9lUlhQMjJyY3hORlFjZ3hBVHhyVmdtWlpmQmcxUEtrMnItVFdqYVFkVEVaMDdnUC0yTVhkYklkcGFWZVFlV2JxSFlUZ1lXVlFqSDNWZXY2LWlONlR3WFpObUtXc1V6N2x5TXFFbXdfOG5HeloydHdYQmZCMDlwN0pUWUc4V0pESGZ5N2tYVUk5cWtmSE9JbEotQVoxanFaVEQzYW5XNWVzSHJiVDZCdEFYZ0pZa2dtREp5OHRBNVkw?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxQLTVpeDlvVDBRTU5UaC1ya1RxOWFzcnppYjE4MEdRZ2hJYkc3dEJIaE5qT1dzUG0tSTZ6WHEzdUFNeDdCdUw0cW9FZF94cE1SNkFzQU1NcHZZeFQtcnZJUmFNM1h3TUsyUkZzOVNUZk9iTVhtNTgtOHhXT3p2dG13dXQ1aTIxR0tjQmR5ai1idHlaOGFsX3JSejdTYzlvOWJ6b1ZlTHptQjhNZw?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxOMnBndVV6UWNNNGE2SUd1VnV1Z0RqZVRYWnhUVzdpS21tTDVwM25HUjE2cDlvNXplaG9MV0JTbU13c3dCTmZEbXRZTk9MdUFybERqMV9qbzFKdFJ0cTZ2Sy1SQm55STZsVF9RNGNNVEZadk5XY29oRDQ2azRvNGJSdDFXaElIRnJra1hyMEFTWFhZOEtqaTFseFVHOGRtTXdYZVR0ZElVeWt6N2c3dEI5LUJzRmg0VWlya2cxVVV0eTRocjRP?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxOZ01fZmpmTEdCTENCWE1IZm9rbGpQZXllT0VMOHJ2aGVCYktMOEJvd0VUTXVuNXRIYzcybWRiclVlSnhHUzg2c25YcU9LSGp4UndIZ25OZUU4NVlMZi0tZHA3UWRtRGNDUW5tN3loNlplQXl3WFI0UWc5SkJPd1ROa21QNThKejIyeHlSR1liTml2d19fNlBkRnNtTVRvWW9hdWM1STFIM2pIal9HejJneUxOcEIzUQ?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxQQ2NYcEpZVmJ4VnhJcFgtRlVSZHh2VmxLS2QzZ0pIbUpjU0liS1Zvb1JFX3dJblc2MzdBeXY4QlRoRlA0bTZncmpNUG5jUjNxamN2OG5UU2k5YnRQdXd6U3Q1SE5tMHB3T3EyVFF5a3pEQzFySUp5MFdCV2Q0Y1FWWm9uc1kzWFRNRWtpbFh0ZzJJUm90TVNMdEZiWEhSZS1jZV9ZSC1tSU52aTF5NXB4bjdhWGNMTWZSN1Z4QQ?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxQM3AyVmJoNy02Wnczek52endTSkZJaHVGNmszR2dtbTZLX3VxRG1SNVVmYTI4bDhqLTVweW1jdW8tYW85Nmgzc25qcmNCWEFmaUtBR3BaR05ZWnhNWEt3NXIyaFNOaEZxbVZNRHlRcWZ4QU40S3JpWmtCS19Obl9aSTNwSkNmR3IxQmtxSUVOQ0s5ZFBVR0FLR1NJYnNzUW9yU0RhOGtzeWJUTm9NbUcwcUFCNzEzQlVJZjF1SQ?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxQOVItUFd1MFJQV2l6WElQLWFJNnpXZ01TNVhRdXE3WWNmTEg2d1ZTTmlzU0xsZHAxNUEwRlY4UXVMY1dHMllacjdsdkJidjI5bW9DLXJRemVXQUlHeXQzVnRwTUo4d25fOUxqd1BJQ2ZTQnhvTVhOY0VGSFdRcHhxSUZZTV9KZUFJUHE4MHdTdVJBZ1E0YXlQcnRSenBlTFg5SmktUFdPUWZxU2c3LXlBUnoyR01neW0wUjU1aG9FZw?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxNRFhzZ3ljMXpNQU54ZzVEN0kzWV9wVjVWUnZLSTdSa0xkS1FnVEFDdWd1QVZzc3RraEZ6VHVjcnVrODgyMmVmbDMzX2lSZlp0QkRiRThmN2V1OTBmR0xiZXZmcWFSajg2SHRaeVpLMTFtSU8wMUp3NmYyakg1VkIzYnNhOVdrM3p2MjNabmwxb2txcmNzWG01anVCR0gyOHV0VzVrMUFrQjhSQmV1eDB3YkpQWlVNSFFDeHhqSldjTjBJNTg5TWlHTF9BZXU?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOMFl3MDR4U2RDeG1zaEdBOFNtN2dHYnVZYTNwdkIwVk1YaVVEaFFJR0dSM19kaUVzbU1PQVVRcHZIWEZLb0czYXZlUXJzOU1ybWtlTWRyR3ducktjeG5NS08xTXJTTkNfMjNrM2h6UHk3ekNvNWNwTHhrQzBwd1JLZjdKSzdrYWhQZXZPNjBFZGJhemlUMlE4?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQcUx4anBZX18yWlJYR2QzZ2ZUNHhubUJLWHU0MkplNFRDb1RXMFB6d0VmcVhwSGszbWV1MWFLZURwa2RRZTNQYl8tMVRVa2ZiWXVDOVlfZ0dEZDFPdGEtODl5cTUtSE1JdnVyNWlFWkRNVHk2TXlDNjZWeHR5YzZ1d0xjMlZQVGlYcGdVSFNIdXJJTzQzU29v?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxPazJNWUw5MENoN0loUXJCblNqSUFYV3N2ekFaQ1VXaVVReU1WVTdiNWg3a0VQTlNUeS1pNHBuZFU4NmpELXFhZ3RJc0o4WHZ4ZzFBeDBkcWJSN0RfTVpaWC14UHE3UF82OGIxN1JnYWlRcWJJaW01bDMwcTUzbjdzdEJrX2hvQUk4ZElTRjlfczUzTGRwdGdLWUNOLUFsQjI4OWN2WUUtX3R4eVh1T0RuMQ?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxOXzRxVXc5QXUxaFlGVFQwSmpUSXdFTjJRdWV6YnNWYUFYZnBBQ0tZRW5famE0cS1kc1h1dGpkSzdIUzg1TnVGTGMzT0ZQdDdNZmZDVEk1RDNBRnQzM2RxeUFEa0QxVWp2d3plM1V5YXBqSGh0ckhUbVFtLUxQYXlsbEJ1azRGcGZFSnpWMEFTempvWW1HVnVlV3NGd0ZlWlhuckhGQ1R5XzJ0dmJfclRF?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPdnhpdEhzanE4RkFZb3FsR1hjYl93aktwY3hjV0NCQ1EtQzBBbDRMSzgzYjZoVEdKS2c1ZWU0RTRoMVd5Si1pSlR5R0VaOXQwRVByX1YzdUhLV1djN2ZoSmF1OTAycm5kanF1Y014ZXBSbVp0Q3Nqd0RmWjdJaEFtM3ptUDZsT25temNOTEY3YncxMU1SOHpzSU5fU0JNbjRT?oc=5
- https://news.google.com/rss/articles/CBMiekFVX3lxTE1COEZ0M0p2RHl5US1uaEtOckxaRlRXUXRMc1hlR01pNE4yV0NGTHJIb0Vma3FzZUtKX3RCbVg3ZmpUNHpnaHJZeTBjVFV0YmdFWDc0R2N5RFRObTY0bllEUU15N0J0aGFkUWdNdF9HOHg0WWtMSDJpdTl3?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxPWDhBeDRCZ21nOExrVzluVTk3dWpYQlE2VGgtSVUyRFdXSUI0VVJybVNQTms5V2czZjNtRE1QZ0xTM2NwUWwyUmNsSS10dm5CVE5PeGJ1QVl2djlXNFI2NVhKN0F6YVVfdEF1aE1lWUw2ZFEyT1B5VWM4WVF6VUVncDVfSGE0bzA2RjZrSjdwX3ZlSDhISVRQT2Vzc3pFZlVKVFNmRDNJaG5vcGxVTjhZX2h3?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNQnRLX2xlM3NNZ3ctbTl3OF9OdlRwYktiRHBTeUN1bjZNRG0yTFBYaGw5OTdaVXRHcEVrMWt6WlRJWXpLT05xVEJoSFJnUEgxSDg0R1pmYXFMMWlYX2U2QU5kWlZtTUx0eWpWVjFxSnNaNWhRS0tIWUdOUkRkZk5td2dRanFxR1ZyNklUS2hpUXJKS1hT?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxOS05wcnAyTFFOemYzZjloNG1NMkM3UFU5ZThNZnlCMy1Tc0JiYVNsYW5VdEljYmdod2hKdGwzZTU1UzV6WU5uNUNBVGxhb2xKdS12enBrSWdFakRnczQzb1FzSWVaLUNqTGo2a1FSNk1mMzBLRnpTbGZXci01LUdMam1wY1N5b3JTdURKakFRSjQ0cHlPaDc4Ynk4Z0d6dFdPSG1iZjZuSXVOaUZXcTVwRUxscktxZnV6?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
