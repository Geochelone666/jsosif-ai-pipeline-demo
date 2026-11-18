# ACN Intelligence Report

- ticker: **ACN**
- Report as_of: **2026-11-17**
- Market data as_of: **2026-11-17**
- Quant sources: https://finance.yahoo.com/quote/ACN/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ACN/key-statistics/
- AI analysis snapshot as_of: **2026-11-17**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-18T06:07:26.803498+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 8, 'ai': 12, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261117T062519Z-6171f6c2/ACN** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 6 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 60.0%; oldest publication 2026-11-11

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 239.2800 |
| Return 1D (%) | -3.3993 |
| Return 1W (%) | -7.4388 |
| Return 1M (%) | 4.1797 |
| Return YTD (%) | -8.2483 |
| Return 1Y (%) | 2.0055 |
| Annualized volatility (%) | 50.1194 |
| Beta vs SPY | -0.0239 |
| Max drawdown (%) | -56.5068 |
| Sharpe (rf=0) | 0.2913 |
| Downside deviation (rf=0, %) | 34.8760 |
| Sortino (rf=0) | 0.4186 |
| Historical VaR 95% (1D, %) | 4.5949 |
| Historical ES 95% (1D, %) | 6.8005 |
| Correlation vs SPY | -0.0066 |
| Tracking error vs SPY (%) | 52.0669 |
| P/E (trailing) | 18.27 |
| P/B | 4.51 |
| EV/EBITDA | 10.70 |
| Revenue growth (%) | 6.20 |
| Forward P/E (estimate) | 15.04 |
| Gross margin (%) | 32.05 |
| Operating margin (%) | 16.42 |
| Return on equity (%) | 26.02 |
| Free cash flow yield (%) | 7.56 |
| MA50 | 218.3910 |
| Close vs MA50 (%) | 9.5650 |
| MA200 | 187.3008 |
| Close vs MA200 (%) | 27.7517 |
| RSI (14, Wilder) | 48.7676 |
| MACD (12,26) | 8.1225 |
| MACD signal (9) | 12.0064 |
| MACD histogram | -3.8838 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ACN': 284, 'SPY': 284}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 239.2800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -3.3993 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -7.4388 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 4.1797 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -8.2483 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 2.0055 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 50.1194 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 34.8760 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4186 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.5949 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.8005 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.0066 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 52.0669 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.0239 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -56.5068 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2913 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.0410 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 32.0500 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 16.4190 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 26.0250 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 7.5588 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 18.2656 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 48.7676 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.8838 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 9.5650 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 27.7517 -> Clearly above the moving-average trend level.

## TAILWINDS

### Accenture: Market Sentiment Is Aligning With Fundamentals
- Summary: Positive market sentiment matches fundamentals, supporting stock outlook.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOT01yM1M0N3ZyYVBxcFVKS19lY242eEFlT2RzbV94WWhoZUlxaVFqMi01Y2c2Sm5SSlA4RGVPVGw4MGZ1UEhCVHZoLVBFR2luWVY3RHJpUWZwYTdWUWdBVEQxUkd5UHlHRndYTW5NdVlHMDBnaVNscnVGYUh4YUZiemFTWW9OV0FYcEF0WXQ4TEJYcm1SbHdLV1Z3?oc=5>

### Dividend-linked grant gives Accenture (ACN) Americas CEO John F. Walsh 93 stock units.
- Summary: CEO receives 93 stock units tied to dividends, supporting shareholder value.
- Date: 2026-11-17 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPTWpFOHZqTW1WOTdxUHM0NklBN3F4azJpQmk5Y0h3UkF3VVpvNUhnd3RhU1BYaWJiWmRYeUc0amNqZjh0eFc2SFFQYnJmLWFOWVlxendjYmxxdmVCMVY0Wk5MQzVRbjNiRmxhNC1EU0VoM0hPeUhVS19ObXRlVk52WnZtTWdLQTJUTGQzdUZDazQzSjk0cl9RVVUwVFF2dFFBdThlMmVvSXJFUQ?oc=5>

### Dividend-linked stock grant gives Accenture (ACN) director Paula A. Price 11 shares.
- Summary: Director receives 11 shares linked to dividends, enhancing retention.
- Date: 2026-11-17 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxOcWhsc1VYMnlVSXB2ZllPOXVPUzRCRUdiaG44MGNBZ2dxbVpuSEF3XzhTM1BYb0s5aHA0OG1lY3Nud0JQdVNMbDZVQ0o2RXFMUG9zVzZvWkY3UHI1VFEzUEw2WElhWkFOcERQV2lORFZ1SnB1a0ttZko2RmlHWEdJb1FmTnQtU3g0VDR4Nl9Ub0YzZXBERUN0N0cxYm5henkxbkRkTWVCU3VzQQ?oc=5>

## HEADWINDS

### Accenture (ACN) Stock May Trade At A Discount On Fresh AI Outsourcing News
- Summary: Potential discount on ACN shares due to new AI outsourcing news.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQQUNjcFJ4bU91ZlFkTDQ4cmI4dEs2X0lvaGY0cDFOcmFSMzFleWlwRThZU2pfZVVfd2VQa21CdDIyOS1XQkVNZ2VjOFBNNjJoaG5WM2lPZGFOaVlkdGR5LWYtMkNoY1ZJMVNDbUUzQWpHczEtQ2loQnhDWl9xU0kwNm92Y0pSa3RNaUNnZm40VW15VkdiS2FhVkln?oc=5>

### Accenture PLC Stock (ACN) Closed Down by 3.40% on Nov 17: A Full Analysis
- Summary: ACN shares fell 3.40% on Nov 17, indicating a short‑term decline.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxQMUI3RDNCY2tnZHkwSFhaU3J4M2o0b3VDVzhtaGJqMS1wWEN5Umt2ekpVZDQ2NlVrVDlLaWQ1X05EcVd2d3FTVmh1aE5Qd29xdThpeVJ6aW9BM3ZGNkQ1dkxZbkZvZGFmM1hUaFM1X0RPZ18tUm43ZjByMWp3cmpWcWRZbE4tTmlVcVE?oc=5>

## CATALYSTS

### Accenture (ACN) CFO receives 24 stock units tied to a cash dividend.
- Summary: Accenture (ACN) CFO receives 24 stock units tied to a cash dividend.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxOeHI3NDNkWEtMUnpsc1FVVXdhZUp4a3hobTY3aEhxRGpUTFptWVZQdkNTS3JwZEF6RUFrRGVsNmxjRHF5aktEclZhUHB4Z0dfTGdRXzc3TVNEUlViSmpUcGhFTkJMVFNaVTVCaFNySVFYM1VRamxTQ1pGYjdmTkJFMHJTQzM2b3Q5cExGVTVaRGRHN01vX0xWWThJTXZodjF1Uzg4b1ZSOWRidw?oc=5>

### Accenture (ACN) EMEA CEO receives 23 shares in a dividend-linked stock grant.
- Summary: Accenture (ACN) EMEA CEO receives 23 shares in a dividend-linked stock grant.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxNSXdqemlaeTF2bmt4bmNvbDJRWDRtNmhqd2dyV0N3NzU1bHE1Q2FPTkFuVGtuZ0JYdUNFREtZWGRDU0dqR3ZIZmpjdjZrdEY1YndWbWdkSWZTQjNaaFdmY2xIM2dCZ19HcGM3Sm9nNEh3MHFGZDFISHJxZ2sxZnZPMFAyVE9oSTNSWWhmTUVtRHY1Umtoc3g5UktFTVNZMHhsd0VvMnZPTElQdw?oc=5>

### Accenture (ACN) grants Jennifer Nason 7 stock units to reflect its cash dividend.
- Summary: Accenture (ACN) grants Jennifer Nason 7 stock units to reflect its cash dividend.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxQVHZsS2RUa20tTG9XYWJ4d0xHX3JyNHNEWGZ2MTBiSEpFYXpvekRXNkdhQzlGRzdVS0dOcFR6NHA1VlBtcWFTdmtYTThnc0s5TVRhenhqRl9rUDJXZHV2ZGtOWnFTX2VzZE51ZzBMMHNXVDVGbDZlcGlhMjFneW5CdC11Q1Y1LTk2Qk1CdTE2ODVZY0pCeWZWNFp5aHFmc3FzRFZTZlU2ckdQUQ?oc=5>

### Accenture (ACN) officer receives 88 stock units tied to its cash dividend.
- Summary: Accenture (ACN) officer receives 88 stock units tied to its cash dividend.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPRHFWNEhMOUxsZDF5QXRSaGpYOVMzX1UtanJnVUEzdExTMXl5cVBLRTJBYUZHRTNIZXh4OUFDRlZ5a0RBSjBhdDFjSG84NElNR0xSV1Y1a2ZvZ0lBVjl5cm1HbnY2MjM0TVZLV3QxaEV4TzlNM3RPU0s5QkVoa2N0VDRNcWFteWNfbGhEeE1uZFowYVRtRWFnTDBOdDBWVERKWDU0bVdDUTFrUQ?oc=5>

### Accenture (ACN) director receives 7 stock units tied to a cash dividend.
- Summary: Accenture (ACN) director receives 7 stock units tied to a cash dividend.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxOQnp5S19rQ1pPRlhGaER2aFJtclBrTm9NbDVVS3ZRZDV0cTIzUkp6UUhyLVFqNUZMUUJSUEZ0REhwTTlzUTNKOUlTVnpZSUZRUDAxaFFRRFhpZU5KS0dzbzJNd1BaVEl6SXJvcldYbV9JN1VDSTF2SFJlcmVQbGZ6cnJCZExKdVVySjVIX1NneU1zcEJyTnloNVRSek5PQjRCWVo2UldUdmdsQQ?oc=5>

### Accenture (ACN) CEO receives a dividend-linked grant of 313 stock units.
- Summary: Accenture (ACN) CEO receives a dividend-linked grant of 313 stock units.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxOSWxPUkFkRmhpQ3VQdzhqRlpUaVVKNVExZ1Z4eWdyTUtmR3hDSjZLMUMtMzVXU3JydmtnOGtNekNpamtaZm9Cb3hQMXdIREdscHZ0ZWZhbXNYY1c5Y0NYRDdxaWZQMjZKSkotcXNFMzdhazVwc2tDQXQ1a1lCVEN4OVFIS21iWkhNX2NKazh0aXpsMW9ublRuOXBucGY2NUU4MmlBQXVLM1Zkdw?oc=5>

### Accenture (ACN) grants HR chief 40 shares tied to its cash dividend.
- Summary: Accenture (ACN) grants HR chief 40 shares tied to its cash dividend.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxNeDRZT3BoZnZCY2dUYkM0aHlFVlM4c3dxRWdrN2RhdjQwWlBUQ1pxMEJoclh3TmFKcjFDMnJMejNUZHU3RWJaOUFFNGJ4Zk1DejF6YVRoNy1RLV9hRHktaDlzNjhBeTRtdk43bDNROXJOTzU1dTktSzhWbGhkR2ZBSTlVSjI3RURlc3hSR0xiVnlaZVJna3gxZFJJR3NsZXczUHhmMG9OZXluZw?oc=5>

### Accenture (ACN) counsel receives 129 shares tied to its cash dividend.
- Summary: Accenture (ACN) counsel receives 129 shares tied to its cash dividend.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxNdmlmT19ELV9BRGZtMVdDWHRzYWEwajZMS1lyVDYxT3dZTUFpbnpvdGM0WXp1TDhaYzZtU3hnNXZ1T21hWW1SZmVPM3ZZNm9idVc4dDY4cGJfNWNtdHhJMTZweHFJUzR1b2l1alVCOTgyTzdONjA0YzNMRGtsYmdGQVFZU0Y1TXJ1NnRvai1yOFNHazNRcVBJd3lneFRWdEpLMU5ROWhUbGE2Zw?oc=5>

### Should You Buy Accenture Stock For Its Cash Flow?
- Summary: Analysis of Accenture's cash flow suggests potential investment value.
- Date: 2026-11-13 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxQeWRaeWgyRkxxM2l2ZG1QbmhNcTQ2MkVLc0RYT2RPdVd1aV83LWVyYUNTVkcwNGlvTklWRVIyczNJTUJic0tBUEZHODBrTVltbkU0elQzN29CTnk5aWdLNkttckFtck1UNE5USXMyZmhsWWxGVWhFdE9sMU94eEVxZUhjbjExTGxRX0htbF8zX1lJbWQ1M3k1SVpYVzEyazRLenhkLTg2RWpGUktD?oc=5>

### Accenture: Sold On AI While AI Makes It Grow
- Summary: Examines Accenture's AI strategy and growth prospects.
- Date: 2026-11-13 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxPdTBKb19fWFdlSGhTenE3VkNwWXpCMHVnMU43ZW9kUi1DYnNqTXpwZ0dqYURJemRiN1pZbDJxeVFaZTF1bTUwbmdYc3l2Q25uSGtwRl9OS1QyMEtWX3p2V1FBNzNVSnQwcU1CQWVfZ1gyakFhS2hBM2JjRElhUVB4S09VLVhJNy1rQWFUSA?oc=5>

### A dividend adjustment gives Accenture (ACN) director Nancy McKinstry a 9-unit stock grant.
- Summary: Dividend adjustment awards 9 restricted stock units to director Nancy McKinstry.
- Date: 2026-11-17 | Impact: low | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxOdmUyVkh0UEptV0w0Wm16YWo2dDB6M0hoWHFIT3FXOTBvWUZvYjkxQ1g2V0tjTVRqWFZ0MUtlWFNXa0JCbUo3cnJVNUJtTkZfUGhVbmtLQXE5S1B1c1dqRHlINGlOU0I0NHhfQlg4YlpoTUgtVmVJMGtxYS1MQkpkbjUyaWtadmNYOVdITGJRVF9yRHBpWHU3c2ltX3ZOTDdVal96SzkxZ0JQZw?oc=5>

### A dividend-linked award brings Accenture (ACN) director's reported direct holdings to 1,697 shares.
- Summary: Dividend-linked award increases director's holdings to 1,697 shares.
- Date: 2026-11-17 | Impact: low | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxQZklVcnRFS0pLTC0zejRvOFpwaWc1RDRCbWZPU3NpZjlpVlJRcjY0Rjg5cjVHU1Qxck1yemU3aVNOakVzcm0wNG5BU3FuLXEweDVDVEpNYVNuTWZYdHI5X3haZENnR3RBVzk3eXJaTXhDM2Uyd0tNUXJGNTI5R0NwZlllMmh0d3ZzX0tuTFRsaG96aUZSZHM4NTVMblhXTTRkZkF0RjUtRWFxUQ?oc=5>

### Dividend adjustment brings 33-share grant for Accenture (ACN) chief accounting officer.
- Summary: Dividend adjustment grants 33 shares to chief accounting officer.
- Date: 2026-11-17 | Impact: low | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxOUG9TR3hMbXNWb3A2MTFHSEQza0lNQ2NQZnhTSk1zSHJWU3BGR3ZETUwtVUF1Znlha0Z1emJtdVc5RDltM1BBcXpZNmdXeEdxQnQ1Ym1pRWRfMGduT0ZUVUFmRU9WSFVYTER1SDVDRFRTT3hnWmpqN1VSMEU4YnJla1ZqSElOb1JrcnE3OWxtTDh4Xy1URTJLQVlFTUpYeGNwX1lVd1hfUGljdw?oc=5>

### Dividend-related grant adds 12 shares to Accenture (ACN) director's reported holding of 9,841.
- Summary: Dividend-related grant adds 12 shares to director's holdings.
- Date: 2026-11-17 | Impact: low | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxOMHNiN1dXRUtkaUhHTkVmQlRydDFMTmp2SEdLTVNSUk9QRk9lOTFMbXFDVExoZXpzdThQZzNDX2duSGhRU2ZFWmZqYUFBejVwNG5ZVnF5dGJ0eENNRmdaNmRtZWN5VHRNVmhnaVNxTlpIYXdOUUdSaHFSQ1ozemdTRDRGc0JTTWk3SVh5cHNOMTBhSGV1M3FnT18wTzdsZVJKdWtIbzdPelZvUQ?oc=5>

### Dividend adjustment gives Accenture (ACN) director Arun Sarin 10 restricted stock units.
- Summary: Dividend adjustment awards 10 restricted stock units to director Arun Sarin.
- Date: 2026-11-17 | Impact: low | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxQRnJoWUFodmo4MVpnTGx2V0tkeTFQSDJMT2VmNnR1SXRXdXBkTHZwa2Fmc0FFQ2Rha1JQaTdHNWdNckpKT0dvNnNKSGw1VlhGVVhScldxQ2Zrb3ZzZWQ3Y0F6YTk0V3BIWm1DSTFEZzM3Z2VfNVFUQnd4d0ljYXlnUmxGZ2hONlVLQTZia0dXT2toTVJGNzhBRTVpdTBlR2dJblRLY0c5MWlBZw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ACN** | **18.27** | **4.51** | **10.70** | **6.20** | **141,351,665,664.00 USD** | **2.01** |
| IBM | 20.69 | 6.15 | 16.54 | 4.70 | 218,407,976,960.00 USD | -20.10 |
| CTSH | 10.95 | 1.83 | 6.67 | 4.60 | 26,821,826,560.00 USD | -13.34 |
| INFY | 15.28 | 9.46 | 19.34 | 1.40 | 48,888,041,472.00 USD | -26.47 |

Peers fetched as_of: 2026-11-17; ACN reuses existing data (market data as_of: 2026-11-17); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-01
- Next expected earnings: 2026-12-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-17

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-10-16
- Revenue (latest available single quarter): 18,679,110,000.00 USD; period 2026-06-01/2026-08-31; fiscal year/reporting period 2026/FY
- Net income (latest available single quarter): 1,991,267,000.00 USD; period 2026-06-01/2026-08-31; fiscal year/reporting period 2026/FY
- SEC link: https://www.sec.gov/Archives/edgar/data/1467373/000146737326000049/acn-20260831.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimgFBVV95cUxOT01yM1M0N3ZyYVBxcFVKS19lY242eEFlT2RzbV94WWhoZUlxaVFqMi01Y2c2Sm5SSlA4RGVPVGw4MGZ1UEhCVHZoLVBFR2luWVY3RHJpUWZwYTdWUWdBVEQxUkd5UHlHRndYTW5NdVlHMDBnaVNscnVGYUh4YUZiemFTWW9OV0FYcEF0WXQ4TEJYcm1SbHdLV1Z3?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPTWpFOHZqTW1WOTdxUHM0NklBN3F4azJpQmk5Y0h3UkF3VVpvNUhnd3RhU1BYaWJiWmRYeUc0amNqZjh0eFc2SFFQYnJmLWFOWVlxendjYmxxdmVCMVY0Wk5MQzVRbjNiRmxhNC1EU0VoM0hPeUhVS19ObXRlVk52WnZtTWdLQTJUTGQzdUZDazQzSjk0cl9RVVUwVFF2dFFBdThlMmVvSXJFUQ?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxOcWhsc1VYMnlVSXB2ZllPOXVPUzRCRUdiaG44MGNBZ2dxbVpuSEF3XzhTM1BYb0s5aHA0OG1lY3Nud0JQdVNMbDZVQ0o2RXFMUG9zVzZvWkY3UHI1VFEzUEw2WElhWkFOcERQV2lORFZ1SnB1a0ttZko2RmlHWEdJb1FmTnQtU3g0VDR4Nl9Ub0YzZXBERUN0N0cxYm5henkxbkRkTWVCU3VzQQ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQQUNjcFJ4bU91ZlFkTDQ4cmI4dEs2X0lvaGY0cDFOcmFSMzFleWlwRThZU2pfZVVfd2VQa21CdDIyOS1XQkVNZ2VjOFBNNjJoaG5WM2lPZGFOaVlkdGR5LWYtMkNoY1ZJMVNDbUUzQWpHczEtQ2loQnhDWl9xU0kwNm92Y0pSa3RNaUNnZm40VW15VkdiS2FhVkln?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxQMUI3RDNCY2tnZHkwSFhaU3J4M2o0b3VDVzhtaGJqMS1wWEN5Umt2ekpVZDQ2NlVrVDlLaWQ1X05EcVd2d3FTVmh1aE5Qd29xdThpeVJ6aW9BM3ZGNkQ1dkxZbkZvZGFmM1hUaFM1X0RPZ18tUm43ZjByMWp3cmpWcWRZbE4tTmlVcVE?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxOeHI3NDNkWEtMUnpsc1FVVXdhZUp4a3hobTY3aEhxRGpUTFptWVZQdkNTS3JwZEF6RUFrRGVsNmxjRHF5aktEclZhUHB4Z0dfTGdRXzc3TVNEUlViSmpUcGhFTkJMVFNaVTVCaFNySVFYM1VRamxTQ1pGYjdmTkJFMHJTQzM2b3Q5cExGVTVaRGRHN01vX0xWWThJTXZodjF1Uzg4b1ZSOWRidw?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxNSXdqemlaeTF2bmt4bmNvbDJRWDRtNmhqd2dyV0N3NzU1bHE1Q2FPTkFuVGtuZ0JYdUNFREtZWGRDU0dqR3ZIZmpjdjZrdEY1YndWbWdkSWZTQjNaaFdmY2xIM2dCZ19HcGM3Sm9nNEh3MHFGZDFISHJxZ2sxZnZPMFAyVE9oSTNSWWhmTUVtRHY1Umtoc3g5UktFTVNZMHhsd0VvMnZPTElQdw?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxQVHZsS2RUa20tTG9XYWJ4d0xHX3JyNHNEWGZ2MTBiSEpFYXpvekRXNkdhQzlGRzdVS0dOcFR6NHA1VlBtcWFTdmtYTThnc0s5TVRhenhqRl9rUDJXZHV2ZGtOWnFTX2VzZE51ZzBMMHNXVDVGbDZlcGlhMjFneW5CdC11Q1Y1LTk2Qk1CdTE2ODVZY0pCeWZWNFp5aHFmc3FzRFZTZlU2ckdQUQ?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPRHFWNEhMOUxsZDF5QXRSaGpYOVMzX1UtanJnVUEzdExTMXl5cVBLRTJBYUZHRTNIZXh4OUFDRlZ5a0RBSjBhdDFjSG84NElNR0xSV1Y1a2ZvZ0lBVjl5cm1HbnY2MjM0TVZLV3QxaEV4TzlNM3RPU0s5QkVoa2N0VDRNcWFteWNfbGhEeE1uZFowYVRtRWFnTDBOdDBWVERKWDU0bVdDUTFrUQ?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxOQnp5S19rQ1pPRlhGaER2aFJtclBrTm9NbDVVS3ZRZDV0cTIzUkp6UUhyLVFqNUZMUUJSUEZ0REhwTTlzUTNKOUlTVnpZSUZRUDAxaFFRRFhpZU5KS0dzbzJNd1BaVEl6SXJvcldYbV9JN1VDSTF2SFJlcmVQbGZ6cnJCZExKdVVySjVIX1NneU1zcEJyTnloNVRSek5PQjRCWVo2UldUdmdsQQ?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxOSWxPUkFkRmhpQ3VQdzhqRlpUaVVKNVExZ1Z4eWdyTUtmR3hDSjZLMUMtMzVXU3JydmtnOGtNekNpamtaZm9Cb3hQMXdIREdscHZ0ZWZhbXNYY1c5Y0NYRDdxaWZQMjZKSkotcXNFMzdhazVwc2tDQXQ1a1lCVEN4OVFIS21iWkhNX2NKazh0aXpsMW9ublRuOXBucGY2NUU4MmlBQXVLM1Zkdw?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxNeDRZT3BoZnZCY2dUYkM0aHlFVlM4c3dxRWdrN2RhdjQwWlBUQ1pxMEJoclh3TmFKcjFDMnJMejNUZHU3RWJaOUFFNGJ4Zk1DejF6YVRoNy1RLV9hRHktaDlzNjhBeTRtdk43bDNROXJOTzU1dTktSzhWbGhkR2ZBSTlVSjI3RURlc3hSR0xiVnlaZVJna3gxZFJJR3NsZXczUHhmMG9OZXluZw?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxNdmlmT19ELV9BRGZtMVdDWHRzYWEwajZMS1lyVDYxT3dZTUFpbnpvdGM0WXp1TDhaYzZtU3hnNXZ1T21hWW1SZmVPM3ZZNm9idVc4dDY4cGJfNWNtdHhJMTZweHFJUzR1b2l1alVCOTgyTzdONjA0YzNMRGtsYmdGQVFZU0Y1TXJ1NnRvai1yOFNHazNRcVBJd3lneFRWdEpLMU5ROWhUbGE2Zw?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxQeWRaeWgyRkxxM2l2ZG1QbmhNcTQ2MkVLc0RYT2RPdVd1aV83LWVyYUNTVkcwNGlvTklWRVIyczNJTUJic0tBUEZHODBrTVltbkU0elQzN29CTnk5aWdLNkttckFtck1UNE5USXMyZmhsWWxGVWhFdE9sMU94eEVxZUhjbjExTGxRX0htbF8zX1lJbWQ1M3k1SVpYVzEyazRLenhkLTg2RWpGUktD?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxPdTBKb19fWFdlSGhTenE3VkNwWXpCMHVnMU43ZW9kUi1DYnNqTXpwZ0dqYURJemRiN1pZbDJxeVFaZTF1bTUwbmdYc3l2Q25uSGtwRl9OS1QyMEtWX3p2V1FBNzNVSnQwcU1CQWVfZ1gyakFhS2hBM2JjRElhUVB4S09VLVhJNy1rQWFUSA?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxOdmUyVkh0UEptV0w0Wm16YWo2dDB6M0hoWHFIT3FXOTBvWUZvYjkxQ1g2V0tjTVRqWFZ0MUtlWFNXa0JCbUo3cnJVNUJtTkZfUGhVbmtLQXE5S1B1c1dqRHlINGlOU0I0NHhfQlg4YlpoTUgtVmVJMGtxYS1MQkpkbjUyaWtadmNYOVdITGJRVF9yRHBpWHU3c2ltX3ZOTDdVal96SzkxZ0JQZw?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxQZklVcnRFS0pLTC0zejRvOFpwaWc1RDRCbWZPU3NpZjlpVlJRcjY0Rjg5cjVHU1Qxck1yemU3aVNOakVzcm0wNG5BU3FuLXEweDVDVEpNYVNuTWZYdHI5X3haZENnR3RBVzk3eXJaTXhDM2Uyd0tNUXJGNTI5R0NwZlllMmh0d3ZzX0tuTFRsaG96aUZSZHM4NTVMblhXTTRkZkF0RjUtRWFxUQ?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxOUG9TR3hMbXNWb3A2MTFHSEQza0lNQ2NQZnhTSk1zSHJWU3BGR3ZETUwtVUF1Znlha0Z1emJtdVc5RDltM1BBcXpZNmdXeEdxQnQ1Ym1pRWRfMGduT0ZUVUFmRU9WSFVYTER1SDVDRFRTT3hnWmpqN1VSMEU4YnJla1ZqSElOb1JrcnE3OWxtTDh4Xy1URTJLQVlFTUpYeGNwX1lVd1hfUGljdw?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxOMHNiN1dXRUtkaUhHTkVmQlRydDFMTmp2SEdLTVNSUk9QRk9lOTFMbXFDVExoZXpzdThQZzNDX2duSGhRU2ZFWmZqYUFBejVwNG5ZVnF5dGJ0eENNRmdaNmRtZWN5VHRNVmhnaVNxTlpIYXdOUUdSaHFSQ1ozemdTRDRGc0JTTWk3SVh5cHNOMTBhSGV1M3FnT18wTzdsZVJKdWtIbzdPelZvUQ?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxQRnJoWUFodmo4MVpnTGx2V0tkeTFQSDJMT2VmNnR1SXRXdXBkTHZwa2Fmc0FFQ2Rha1JQaTdHNWdNckpKT0dvNnNKSGw1VlhGVVhScldxQ2Zrb3ZzZWQ3Y0F6YTk0V3BIWm1DSTFEZzM3Z2VfNVFUQnd4d0ljYXlnUmxGZ2hONlVLQTZia0dXT2toTVJGNzhBRTVpdTBlR2dJblRLY0c5MWlBZw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
