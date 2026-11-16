# META Intelligence Report

- ticker: **META**
- Report as_of: **2026-11-15**
- Market data as_of: **2026-11-13**
- Quant sources: https://finance.yahoo.com/quote/META/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/META/key-statistics/
- AI analysis snapshot as_of: **2026-11-15**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-16T04:55:22.104883+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 11, 'ai': 10, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261115T044154Z-6abfba73/META** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 9 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 40.0%; oldest publication 2026-11-08

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 641.6900 |
| Return 1D (%) | 2.8993 |
| Return 1W (%) | 5.1692 |
| Return 1M (%) | -15.8439 |
| Return YTD (%) | -2.5372 |
| Return 1Y (%) | 5.5709 |
| Annualized volatility (%) | 41.6526 |
| Beta vs SPY | 1.3720 |
| Max drawdown (%) | -28.7332 |
| Sharpe (rf=0) | 0.3367 |
| Downside deviation (rf=0, %) | 27.4282 |
| Sortino (rf=0) | 0.5112 |
| Historical VaR 95% (1D, %) | 3.7761 |
| Historical ES 95% (1D, %) | 5.6434 |
| Correlation vs SPY | 0.4491 |
| Tracking error vs SPY (%) | 37.5602 |
| P/E (trailing) | 21.89 |
| P/B | 6.02 |
| EV/EBITDA | 14.40 |
| Revenue growth (%) | 26.10 |
| Forward P/E (estimate) | 17.99 |
| Gross margin (%) | 81.03 |
| Operating margin (%) | 37.78 |
| Return on equity (%) | 32.26 |
| Free cash flow yield (%) | 1.03 |
| MA50 | 679.7032 |
| Close vs MA50 (%) | -5.5926 |
| MA200 | 630.0237 |
| Close vs MA200 (%) | 1.8517 |
| RSI (14, Wilder) | 47.8020 |
| MACD (12,26) | -15.2194 |
| MACD signal (9) | -17.5739 |
| MACD histogram | 2.3545 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'META': 282, 'SPY': 282}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 641.6900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.8993 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 5.1692 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -15.8439 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -2.5372 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 5.5709 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 41.6526 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 27.4282 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.5112 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.7761 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.6434 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4491 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.5602 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.3720 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.7332 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3367 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.9870 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 81.0340 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 37.7770 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 32.2640 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.0272 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 21.8932 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 47.8020 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 2.3545 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -5.5926 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 1.8517 -> Slightly above the moving-average trend level.

## TAILWINDS

### Will ETF Buying Change Meta Stock Narrative
- Summary: ETF buying could shift Meta’s stock narrative, potentially boosting investor interest.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNUnhObF9vcWxydnRua1J4T2hsVjhTOExiYjFWYUJhTmxGazE1ZS1zTzVBN3JuUTkwaHVKM3h0bm95ZXU4NlBLQkFmbkk1cnlYVTBlc1F4Rk9VaVV4cnhtd1Y1QnVETzNjbkZvM3FObVc5Y182VjVjc1B4SXBIbjAwSUp3WUZlVXpqOHpFbkkxT2pqbGhKQWxEMw?oc=5>

## HEADWINDS

### Meta Platforms, Inc. $META Stock Holdings Lowered by International Assets Investment Management LLC
- Summary: Meta Platforms, Inc. $META Stock Holdings Lowered by International Assets Investment Management LLC
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7gFBVV95cUxOUjB1S0xQcjFOMWlCWmtxNFU1Y1lOMXdxajBMMndod1dzZ19pYndGTkJERlZaQ3prOEx6UWFEV19iRXgtem9LM2lyanJMbFR6NFlVdmdycmsyUXBOWFotdUc4MjZaSUgzaUloODBfY0RmYWxBUXhrVG5XVFp0OGJHb2RIRDN6aTk2cmdoMlM5THJMOXRtcWhNcnUyR2JTa0tVVGRGeGNEdDc0VjRYMmQ4bzJRWmJqTXdMcWM2S3ZRVExGWHRBeGswSUMwQmwzUGlpQnFENjFjeEpYTUFBWk9RckN1ZUtsRzhwaXV0dW5B?oc=5>

### Meta Stock Falls 2.0% After United Bans AI Agents (Nov 11)
- Summary: Meta Stock Falls 2.0% After United Bans AI Agents (Nov 11)
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTFBleko1R3FEX09GVkl1OVZ1UGtvckx5c2lMZ0dpZ0VvbVpiWnV1UkFJczZCRzM1ODZQbV9SZWlfU0ZfUENEME5aTTlWdHpmRVlCZV9CelFrYVRSZTJja3Y5Z0VjWVZrQUdRb054VWFjX09HQndpbVVFTm9Md29vQQ?oc=5>

### Meta Stock: Midterm Election Results Raise Concerns Over AI Data Center Expansion
- Summary: Election outcomes may hinder Meta’s AI data center expansion plans.
- Date: 2026-11-11 | Impact: high | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQcVlqaXUwYkwwcHFqNjdaSk95ZEhFNlpBdmRsV1ZsM2loSExqZzh0TVhka3ZtQ2ljWGpULVlrTXU2SlpGM19LalpDV0dIZlZ6bVZmOWJaalFvcVFqRjJRUjMxVG5QUlFRYWR2RFplZ1FzYnNKRXowd1owNl9qZ2NHRHVDWHRZVnY4TENuSkZHaHJHLU43ZTlNR3pfcjllbTVC?oc=5>

### Meta Platforms, Inc. (META) May Need Hundreds of Billions for AI: What Does This Mean for Investors?
- Summary: Meta may require massive AI investment, raising concerns about future profitability and shareholder returns.
- Date: 2026-11-10 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNOHBTVFl0X0c1STJ6b2JOTElOUlhucUlDcTZwVUZoQ2ZNSUo0WXJQZWsyd0ZVWVZFam9hWUdRVEE1VThUT1JrVTN3RnEzemQ4YnJyTnlYenYxdm9zb0JSeVNuelA2R1dxeGNoaml0ZEtsREh1WFNkWDB4U2lNSGxyQjJETkFFdTRRVkZFWHBFLXdxUFZ2MUtZ?oc=5>

## CATALYSTS

### Meta Platforms Stock: Is it a Steal of a Deal at $650?
- Summary: Meta Platforms Stock: Is it a Steal of a Deal at $650?
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNakxvaEdiTzR5M0tqcm5KeE1mVDFYUTVuZlhCdzl6MHdXV0tiek90QU1qZHBxdktxWjNIaHNoRDhPNTVrN0F5OGx1VUtiTWhObkJRcl9pVXFDbzFsT2cxcTRwaHBKZF93cEgzM0JHd3VkVVpIZ0theFMxdEJIY2FvQ0xtSlQyNTMwNmlMRzVKYS0yRjZVMkR6cGln?oc=5>

### Meta Platforms, Inc. $META Stock: M&G PLC Lowers Position
- Summary: Meta Platforms, Inc. $META Stock: M&G PLC Lowers Position
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxPd192eEU5cUFfVGdqNVRGcTJiNTlCcnFXLV9vcnJjNTEwcTJrRHpwdVVGQmhMNHVQaDFtbDJ2M3UzNm9tZmszMnNsRm1tY05pZXJocUpTcm1kWGhneEJLdTFqbzRHNnRkRU5sUmRpeFZxSWJaU2RnTWo5RjFRWm9rTXpSRjJvOXlYRmVZLXoya05aUVU4ZUdNb25USzBrQkdvWHhONHNGTGpmVFdVQUcwa0IyTQ?oc=5>

### Meta's $27B Off-Balance-Sheet AI Deal Reminds Steve Eisman of Enron— Joseph Carlson Disagrees
- Summary: Meta's $27B Off-Balance-Sheet AI Deal Reminds Steve Eisman of Enron— Joseph Carlson Disagrees
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxOSXNzTXNzTW41Yl9aT0RqYm5SVnNuOXdMVTlQZUFOV3Z4LWNjOTdnR1p0UFBWMGU0RFRXMXZxdHVmeWNhQVVGSXlOMEJLeUhlb0hueVptNUJIcVFod05wemlNOHI5OUdwaWlubGhzSGdLc1E5dElVOUxpNnIxRHh5ZFBPd2RXOXM?oc=5>

### Meta Platforms, Inc. $META Stock: New York Life Investment Management LLC Raises Position
- Summary: Meta Platforms, Inc. $META Stock: New York Life Investment Management LLC Raises Position
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3wFBVV95cUxQVFJGOVU4aDFQQUhTZnEtWkhURm5MdGxMVVlwX2xDV0ZzVTk5SkVTcndETVRIdlZsa1hEZHowMklDa01TU2JkXzZCQUtJd0VSaXBPOFBfd3NrTXBPTWdNTEcyaDlSTmhfX2E4by1Ja09DaGlxX1ZvM2NWcEdBY0wwTmRNRFRpSUhTZEV5VmZXVHFma2pfZ21jM2s1WXA2T3V3aVlCeTlJX0xnYnpTV0QxTGVvNjJMTm5pNndJdXlfR0VnYWx5UmJValdiVTZXN2VvbDF2eDFjbFhFVkNyRTNz?oc=5>

### Meta Platforms, Inc. $META Stock Sold by Balentine LLC
- Summary: Meta Platforms, Inc. $META Stock Sold by Balentine LLC
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxPZ0Q1Smd1TTl5WWlITDQ5dW13OFB6REFDekpoSXNDSGZHNElRY3E2Zk1ESGkxS2ZhaU42cTRicUJpQUJZd1hxYm9UcXVXU2JDM0IyZ0VZVkFBb2duZk94YmNObGsxbUhlNzJPdFF0b2xYem5IZzQwTERuV3YyeVJPNVBmb3lRa1FuY2QwZERZME4yY3hfdElYYzQzNl9qLXh6MFliZDJxVmlmeVJTbzFkZGpR?oc=5>

### Meta Platforms, Inc. $META Stock: Cullinan Associates Inc. Lowers Stake
- Summary: Meta Platforms, Inc. $META Stock: Cullinan Associates Inc. Lowers Stake
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxNZTlUNVZVX3NOZ19Yb0VZOGJ5cFJ1bndRX25xRE9sWjFzWEJuSXdNOExsMWxUUWhMeFVuQ0s2OVFnSjhnTkZsZUlpVTY4VElLZW9tc1pCNGtvN2tUSjVEMEw3dkJOVjNkTEQta2ZrQUNRbGhLeGZUbU5hSG9RVG9BT3BoaHVmU2FUZEljVFRXSUZTZV9SQndZbzVONjhGWmFMSEFQZjVUSEpjVlI5VVNQRnlrcnExTGU2TVkwR2xmeXNWNWlfU3c?oc=5>

### Meta Platforms, Inc. $META Stock: Lockheed Martin Investment Management Co. Lowers Holdings
- Summary: Meta Platforms, Inc. $META Stock: Lockheed Martin Investment Management Co. Lowers Holdings
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4AFBVV95cUxPREtoRE8xTG0wYjJXeGdYWTJkN2FubkZpcU00aGcwNHVKS3pjSW9uWExsRndka3ZEWExJeTZRYWtZTmNVQTRZbndSS3NPdGJmZldlNC1nMTdtWURsZjFab3ZFajRwQVNMRGNpd2tjUkNwNEIwc2FTZGU5SzNmbnN2U3U1aXZ3UEdRQlE1aW5yNFFIRjVoM1hITzBHSFBQR0g4a1NLMENrUkJ2dE4xaWdMZUdZVnJlelBOWkY1SmF4cm4wUWhRUldjeDRyVTQ3eXFzWWRUM3FfT2h2RVlTSmFveQ?oc=5>

### Meta Platforms, Inc. $META Stock: Formidable Asset Management LLC Reduces Stake
- Summary: Meta Platforms, Inc. $META Stock: Formidable Asset Management LLC Reduces Stake
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxPYWFjbHBRdUhfNmFBcVNJM1RCNlQ4bGZCbDRISlQ1SUdaN01GbmdFQ2E0QXh0RERzc3F3bklvY1hJSWtSajBCMDNuc2xaTVluT2xJLWk2TUhSeHVqN3RHelVibFVqNjB1d2k0QmJabkxfbm91MXpNZzJaTVU4VWlnLW5jSGVjUFRYOFlmUUk3T3lveUhLWVMteHV5dUdrRmR0cW5NZ21zeUZYdTJzZmVTZDNMZHFFSXZ5eHFCdmlQNW5GWkdONHFfY2cyU2twMnF0U1E?oc=5>

### Meta Platforms, Inc. $META Stock: Carmel Capital Partners LLC Reduces Position
- Summary: Meta Platforms, Inc. $META Stock: Carmel Capital Partners LLC Reduces Position
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxOUFBWb1MtSUpfYTVQNTJ4QV9mZ2VSbXN5SkwzZm1MMmpsV0Z3UksybEdPYkc2ZXR5SW5LNWk4Z1FhT0wxS0w0T0RNSW10NEhsQUhFWE81QWIxeHJxLU95am52SENzZUNlSUs1SlRjZ0lHaVhGZUNteEZCWWJnR0R1Mmp2TG82bFp5QlF2c3FZQVowSGUzQjhzYVJmVDlXMFJCaTlKMi1ickw0bEdLRm8zcUJKdzhkdGU4dENCNEZIYWppQlpwT2J6N3NvMm00OUk2?oc=5>

### As Meta Platforms Buys Conductor, Here’s How to Play META Stock
- Summary: Meta acquires Conductor, potentially expanding its offerings.
- Date: 2026-11-08 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNNUstX3dpZlZvUHdaWndNVlVrakVBdVpncUk0a1BBVHA3WWpFRld6VUxlRGhxajF0b0dLMF9OM2hhSl83ekhfRkh2bWNPekRTcFVxbzJkczZfUWNMbkpvRmJNb1BkRHU4Z0U5ejlOUV90LXFSVmR1YTRDZHM5MXVPTXZJVzJ6Z0RlZDJaWndxYUlnTXF4RDlMdkl5bkxxMGM?oc=5>

### What To Expect Out of Meta By The End of 2026 With an Announced January Stock Split
- Summary: Meta announced a January stock split, potentially boosting liquidity and investor interest.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxQMmthUjhJbXlFYm9uQWJxYzR2QlpoaHJESEJaWmV2MHF3YnhjRVhLVTBoWEFETHE5X2hnVkRJMlZQSUVtTzYzN2tIclQ2bVRGWW91ekxreXduQWRZYThIc05tQjBOeXhNSnNiRkJSdlMwMDktclpOQlc0LVI3WmpMREVCWFlOLVdaNGoxdTVWcW5IMHNCc0pyVVFRVlVFa3FyM2RScmxXSXVUenIzbmxJVVpKZG9kNnJFZlZwS2pPeUdrd3BEblE?oc=5>

### Fund Update: 250,968 META PLATFORMS (META) shares added to ARK Investment Management LLC portfolio
- Summary: ARK Investment Management added 250,968 META shares to its portfolio.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxQLVBvNjBtVVBKNXhQR0ZlTm41UzBlRFo1WlRXNUVub1hsZ0VtSjhCYjZLeEdNZzlJVDBkMTdqSTRMTVh3TUtFOWdrU2l3SzVTMzB2SVMzSnNpOHhLTDRwN0I0UnBrX0htdDZxSEQxa2d3aUNnLVJVdjc2YXdRUjVQakw2Wk9pZ1FrRklqN0VTUnFWWmZPVDJ5QUo4LXhYU1ZXcmJEeENmcGRyR2FJbHpZX2JQdThJd25sRTd6VkZzaDNkcTF2dnoyU0RnbXZWYWFLLVlGZjNB?oc=5>

### Big Tech Stocks Today: Nvidia and Meta Fall as Microsoft Rises Amid AI Selloff
- Summary: Meta shares fell amid AI selloff, affecting market sentiment.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQak13ZzlDaWs2bElSYkFkaGFROC0zbzRXRGNGUDRORTFNSl9QcGNvLUFnVDRkTWFRRldiV2pGMVB1OTFTTjhwTHRRN0RVV1JqSnJUa3hzNzNYTFR3ZjB2VjVEcjlQaXNHX2ZEQlBTZEh1aUNNbVlTdXVQUUtEQXRtU0d4T0ExVFJhVUxVZDhUMjBYUEJwQ0V2RHhPcWJ5UjIydk5DZFEzNTI?oc=5>

### 10,795 Meta Platforms, Inc. $META Shares Bought by Ethic Inc.
- Summary: Ethic Inc. purchased 10,795 META shares.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxNUFBZc1RsN2FBZUprd1hzYTg1VXhfNzlOeVo2M2h5UDVPb2lHSllnUDRTaklIdEdOVTB2XzZNS1hVaXk1ZW43M0J4MzMtSDJtd0tCaG1LWFR4TTMycGkwMElnLWcwbW9QVzVmTWZLRGprZ2JLTmVURW9VVXU3ZXZSdDZtME1BVjhfZFVzOWFZOW1tOHZnYzV4TkxSUVFEZ29Pa3d0M1BSWkFvcHltR3hFR1Bha0xRSW5q?oc=5>

### 965 Meta Platforms, Inc. $META Shares Acquired by Pinion Investment Advisors LLC
- Summary: Pinion Investment Advisors acquired 965 META shares.
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxOWGFBTjJ4a080RFJSbEh5bmE1cTZiS3VUTDBRRnNSNUwxS1RBZ3lEUkNvNW9UeTRoVVJuYUpqSE4wbEd1bDR4bW55WTBIaWlWYjVoX0JRaFJ3cmVrRFE3aG9EWXJnVkpsLUlpOHdLbnJVcGZqTGlQdFN0LVI2Z3V2MklDWmk4Y3VBUWo5UE0yVkxNczJTcG5KS1VrM2QwNmhfLTVKQTNleFllUFFVNDVHelh0ZVV1Y3FRWWJVMjVPY1RlVHJvLWUweDVDeFVval8yVGtQMw?oc=5>

## RISKS

### Meta (META) Faces $880 Million Italy Fine Over User Photo Access
- Summary: Meta fined $880M in Italy for user photo access violations, posing regulatory and financial risk.
- Date: 2026-11-15 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxOTUdFQ3JuakFLZUxCSzVwSDIzRmcxR0lVX1V0Tks5eVdXNkRKM21EaWh5dXh6T2lzTnQtWkNjLThJTC1oeElFU2wyLXNGM3dzMGhGd2RULXQ2TEhkaUJVU284Wk9YeXNkdmJ2cDdsSHB5ZGd6VjBybXRkU1JiR0xOZE82ZVB0bVl5NzY5OUFjN2s4QQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **META** | **21.89** | **6.02** | **14.40** | **26.10** | **1,640,314,437,632.00 USD** | **5.57** |
| GOOGL | 15.44 | 5.51 | 19.08 | 24.70 | 3,636,196,016,128.00 USD | 6.45 |
| SNAP | N/A | 4.05 | 55.11 | 14.30 | 9,081,794,560.00 USD | -38.69 |
| PINS | 79.79 | 3.53 | 36.16 | 11.90 | 10,982,674,432.00 USD | -28.46 |

Peers fetched as_of: 2026-11-15; META reuses existing data (market data as_of: 2026-11-13); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-15

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-22
- Revenue (latest available single quarter): 13,727,000,000.00 USD; period 2018-07-01/2018-09-30; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 9,860,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimAFBVV95cUxNUnhObF9vcWxydnRua1J4T2hsVjhTOExiYjFWYUJhTmxGazE1ZS1zTzVBN3JuUTkwaHVKM3h0bm95ZXU4NlBLQkFmbkk1cnlYVTBlc1F4Rk9VaVV4cnhtd1Y1QnVETzNjbkZvM3FObVc5Y182VjVjc1B4SXBIbjAwSUp3WUZlVXpqOHpFbkkxT2pqbGhKQWxEMw?oc=5
- https://news.google.com/rss/articles/CBMi7gFBVV95cUxOUjB1S0xQcjFOMWlCWmtxNFU1Y1lOMXdxajBMMndod1dzZ19pYndGTkJERlZaQ3prOEx6UWFEV19iRXgtem9LM2lyanJMbFR6NFlVdmdycmsyUXBOWFotdUc4MjZaSUgzaUloODBfY0RmYWxBUXhrVG5XVFp0OGJHb2RIRDN6aTk2cmdoMlM5THJMOXRtcWhNcnUyR2JTa0tVVGRGeGNEdDc0VjRYMmQ4bzJRWmJqTXdMcWM2S3ZRVExGWHRBeGswSUMwQmwzUGlpQnFENjFjeEpYTUFBWk9RckN1ZUtsRzhwaXV0dW5B?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTFBleko1R3FEX09GVkl1OVZ1UGtvckx5c2lMZ0dpZ0VvbVpiWnV1UkFJczZCRzM1ODZQbV9SZWlfU0ZfUENEME5aTTlWdHpmRVlCZV9CelFrYVRSZTJja3Y5Z0VjWVZrQUdRb054VWFjX09HQndpbVVFTm9Md29vQQ?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQcVlqaXUwYkwwcHFqNjdaSk95ZEhFNlpBdmRsV1ZsM2loSExqZzh0TVhka3ZtQ2ljWGpULVlrTXU2SlpGM19LalpDV0dIZlZ6bVZmOWJaalFvcVFqRjJRUjMxVG5QUlFRYWR2RFplZ1FzYnNKRXowd1owNl9qZ2NHRHVDWHRZVnY4TENuSkZHaHJHLU43ZTlNR3pfcjllbTVC?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNOHBTVFl0X0c1STJ6b2JOTElOUlhucUlDcTZwVUZoQ2ZNSUo0WXJQZWsyd0ZVWVZFam9hWUdRVEE1VThUT1JrVTN3RnEzemQ4YnJyTnlYenYxdm9zb0JSeVNuelA2R1dxeGNoaml0ZEtsREh1WFNkWDB4U2lNSGxyQjJETkFFdTRRVkZFWHBFLXdxUFZ2MUtZ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNakxvaEdiTzR5M0tqcm5KeE1mVDFYUTVuZlhCdzl6MHdXV0tiek90QU1qZHBxdktxWjNIaHNoRDhPNTVrN0F5OGx1VUtiTWhObkJRcl9pVXFDbzFsT2cxcTRwaHBKZF93cEgzM0JHd3VkVVpIZ0theFMxdEJIY2FvQ0xtSlQyNTMwNmlMRzVKYS0yRjZVMkR6cGln?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxPd192eEU5cUFfVGdqNVRGcTJiNTlCcnFXLV9vcnJjNTEwcTJrRHpwdVVGQmhMNHVQaDFtbDJ2M3UzNm9tZmszMnNsRm1tY05pZXJocUpTcm1kWGhneEJLdTFqbzRHNnRkRU5sUmRpeFZxSWJaU2RnTWo5RjFRWm9rTXpSRjJvOXlYRmVZLXoya05aUVU4ZUdNb25USzBrQkdvWHhONHNGTGpmVFdVQUcwa0IyTQ?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxOSXNzTXNzTW41Yl9aT0RqYm5SVnNuOXdMVTlQZUFOV3Z4LWNjOTdnR1p0UFBWMGU0RFRXMXZxdHVmeWNhQVVGSXlOMEJLeUhlb0hueVptNUJIcVFod05wemlNOHI5OUdwaWlubGhzSGdLc1E5dElVOUxpNnIxRHh5ZFBPd2RXOXM?oc=5
- https://news.google.com/rss/articles/CBMi3wFBVV95cUxQVFJGOVU4aDFQQUhTZnEtWkhURm5MdGxMVVlwX2xDV0ZzVTk5SkVTcndETVRIdlZsa1hEZHowMklDa01TU2JkXzZCQUtJd0VSaXBPOFBfd3NrTXBPTWdNTEcyaDlSTmhfX2E4by1Ja09DaGlxX1ZvM2NWcEdBY0wwTmRNRFRpSUhTZEV5VmZXVHFma2pfZ21jM2s1WXA2T3V3aVlCeTlJX0xnYnpTV0QxTGVvNjJMTm5pNndJdXlfR0VnYWx5UmJValdiVTZXN2VvbDF2eDFjbFhFVkNyRTNz?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxPZ0Q1Smd1TTl5WWlITDQ5dW13OFB6REFDekpoSXNDSGZHNElRY3E2Zk1ESGkxS2ZhaU42cTRicUJpQUJZd1hxYm9UcXVXU2JDM0IyZ0VZVkFBb2duZk94YmNObGsxbUhlNzJPdFF0b2xYem5IZzQwTERuV3YyeVJPNVBmb3lRa1FuY2QwZERZME4yY3hfdElYYzQzNl9qLXh6MFliZDJxVmlmeVJTbzFkZGpR?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxNZTlUNVZVX3NOZ19Yb0VZOGJ5cFJ1bndRX25xRE9sWjFzWEJuSXdNOExsMWxUUWhMeFVuQ0s2OVFnSjhnTkZsZUlpVTY4VElLZW9tc1pCNGtvN2tUSjVEMEw3dkJOVjNkTEQta2ZrQUNRbGhLeGZUbU5hSG9RVG9BT3BoaHVmU2FUZEljVFRXSUZTZV9SQndZbzVONjhGWmFMSEFQZjVUSEpjVlI5VVNQRnlrcnExTGU2TVkwR2xmeXNWNWlfU3c?oc=5
- https://news.google.com/rss/articles/CBMi4AFBVV95cUxPREtoRE8xTG0wYjJXeGdYWTJkN2FubkZpcU00aGcwNHVKS3pjSW9uWExsRndka3ZEWExJeTZRYWtZTmNVQTRZbndSS3NPdGJmZldlNC1nMTdtWURsZjFab3ZFajRwQVNMRGNpd2tjUkNwNEIwc2FTZGU5SzNmbnN2U3U1aXZ3UEdRQlE1aW5yNFFIRjVoM1hITzBHSFBQR0g4a1NLMENrUkJ2dE4xaWdMZUdZVnJlelBOWkY1SmF4cm4wUWhRUldjeDRyVTQ3eXFzWWRUM3FfT2h2RVlTSmFveQ?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxPYWFjbHBRdUhfNmFBcVNJM1RCNlQ4bGZCbDRISlQ1SUdaN01GbmdFQ2E0QXh0RERzc3F3bklvY1hJSWtSajBCMDNuc2xaTVluT2xJLWk2TUhSeHVqN3RHelVibFVqNjB1d2k0QmJabkxfbm91MXpNZzJaTVU4VWlnLW5jSGVjUFRYOFlmUUk3T3lveUhLWVMteHV5dUdrRmR0cW5NZ21zeUZYdTJzZmVTZDNMZHFFSXZ5eHFCdmlQNW5GWkdONHFfY2cyU2twMnF0U1E?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxOUFBWb1MtSUpfYTVQNTJ4QV9mZ2VSbXN5SkwzZm1MMmpsV0Z3UksybEdPYkc2ZXR5SW5LNWk4Z1FhT0wxS0w0T0RNSW10NEhsQUhFWE81QWIxeHJxLU95am52SENzZUNlSUs1SlRjZ0lHaVhGZUNteEZCWWJnR0R1Mmp2TG82bFp5QlF2c3FZQVowSGUzQjhzYVJmVDlXMFJCaTlKMi1ickw0bEdLRm8zcUJKdzhkdGU4dENCNEZIYWppQlpwT2J6N3NvMm00OUk2?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNNUstX3dpZlZvUHdaWndNVlVrakVBdVpncUk0a1BBVHA3WWpFRld6VUxlRGhxajF0b0dLMF9OM2hhSl83ekhfRkh2bWNPekRTcFVxbzJkczZfUWNMbkpvRmJNb1BkRHU4Z0U5ejlOUV90LXFSVmR1YTRDZHM5MXVPTXZJVzJ6Z0RlZDJaWndxYUlnTXF4RDlMdkl5bkxxMGM?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxQMmthUjhJbXlFYm9uQWJxYzR2QlpoaHJESEJaWmV2MHF3YnhjRVhLVTBoWEFETHE5X2hnVkRJMlZQSUVtTzYzN2tIclQ2bVRGWW91ekxreXduQWRZYThIc05tQjBOeXhNSnNiRkJSdlMwMDktclpOQlc0LVI3WmpMREVCWFlOLVdaNGoxdTVWcW5IMHNCc0pyVVFRVlVFa3FyM2RScmxXSXVUenIzbmxJVVpKZG9kNnJFZlZwS2pPeUdrd3BEblE?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxQLVBvNjBtVVBKNXhQR0ZlTm41UzBlRFo1WlRXNUVub1hsZ0VtSjhCYjZLeEdNZzlJVDBkMTdqSTRMTVh3TUtFOWdrU2l3SzVTMzB2SVMzSnNpOHhLTDRwN0I0UnBrX0htdDZxSEQxa2d3aUNnLVJVdjc2YXdRUjVQakw2Wk9pZ1FrRklqN0VTUnFWWmZPVDJ5QUo4LXhYU1ZXcmJEeENmcGRyR2FJbHpZX2JQdThJd25sRTd6VkZzaDNkcTF2dnoyU0RnbXZWYWFLLVlGZjNB?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQak13ZzlDaWs2bElSYkFkaGFROC0zbzRXRGNGUDRORTFNSl9QcGNvLUFnVDRkTWFRRldiV2pGMVB1OTFTTjhwTHRRN0RVV1JqSnJUa3hzNzNYTFR3ZjB2VjVEcjlQaXNHX2ZEQlBTZEh1aUNNbVlTdXVQUUtEQXRtU0d4T0ExVFJhVUxVZDhUMjBYUEJwQ0V2RHhPcWJ5UjIydk5DZFEzNTI?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxNUFBZc1RsN2FBZUprd1hzYTg1VXhfNzlOeVo2M2h5UDVPb2lHSllnUDRTaklIdEdOVTB2XzZNS1hVaXk1ZW43M0J4MzMtSDJtd0tCaG1LWFR4TTMycGkwMElnLWcwbW9QVzVmTWZLRGprZ2JLTmVURW9VVXU3ZXZSdDZtME1BVjhfZFVzOWFZOW1tOHZnYzV4TkxSUVFEZ29Pa3d0M1BSWkFvcHltR3hFR1Bha0xRSW5q?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxOWGFBTjJ4a080RFJSbEh5bmE1cTZiS3VUTDBRRnNSNUwxS1RBZ3lEUkNvNW9UeTRoVVJuYUpqSE4wbEd1bDR4bW55WTBIaWlWYjVoX0JRaFJ3cmVrRFE3aG9EWXJnVkpsLUlpOHdLbnJVcGZqTGlQdFN0LVI2Z3V2MklDWmk4Y3VBUWo5UE0yVkxNczJTcG5KS1VrM2QwNmhfLTVKQTNleFllUFFVNDVHelh0ZVV1Y3FRWWJVMjVPY1RlVHJvLWUweDVDeFVval8yVGtQMw?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxOTUdFQ3JuakFLZUxCSzVwSDIzRmcxR0lVX1V0Tks5eVdXNkRKM21EaWh5dXh6T2lzTnQtWkNjLThJTC1oeElFU2wyLXNGM3dzMGhGd2RULXQ2TEhkaUJVU284Wk9YeXNkdmJ2cDdsSHB5ZGd6VjBybXRkU1JiR0xOZE82ZVB0bVl5NzY5OUFjN2s4QQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
