# AMD Intelligence Report

- ticker: **AMD**
- Report as_of: **2026-11-26**
- Market data as_of: **2026-11-25**
- Quant sources: https://finance.yahoo.com/quote/AMD/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMD/key-statistics/
- AI analysis snapshot as_of: **2026-11-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-27T06:43:57.295398+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 4, 'ai': 16, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **11** exact headline/source/date matches; prior report **20261126T064454Z-dbdd6f45/AMD** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **5**; {'low_uncalibrated_model_confidence': 3, 'negative_sentiment_in_tailwinds': 1, 'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 11 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 32.0%; oldest publication 2026-11-23

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 406.0300 |
| Return 1D (%) | -1.7519 |
| Return 1W (%) | -23.4108 |
| Return 1M (%) | -21.4323 |
| Return YTD (%) | 89.5919 |
| Return 1Y (%) | 96.9776 |
| Annualized volatility (%) | 75.3517 |
| Beta vs SPY | 3.2927 |
| Max drawdown (%) | -37.7290 |
| Sharpe (rf=0) | 1.2808 |
| Downside deviation (rf=0, %) | 50.1568 |
| Sortino (rf=0) | 1.9242 |
| Historical VaR 95% (1D, %) | 7.1739 |
| Historical ES 95% (1D, %) | 10.2670 |
| Correlation vs SPY | 0.6524 |
| Tracking error vs SPY (%) | 66.5793 |
| P/E (trailing) | 86.76 |
| P/B | 9.74 |
| EV/EBITDA | 59.17 |
| Revenue growth (%) | 44.70 |
| Forward P/E (estimate) | 23.06 |
| Gross margin (%) | 56.00 |
| Operating margin (%) | 17.82 |
| Return on equity (%) | 11.96 |
| Free cash flow yield (%) | 1.09 |
| MA50 | 548.3506 |
| Close vs MA50 (%) | -25.9543 |
| MA200 | 432.9599 |
| Close vs MA200 (%) | -6.2199 |
| RSI (14, Wilder) | 38.0128 |
| MACD (12,26) | -28.0677 |
| MACD signal (9) | -18.4074 |
| MACD histogram | -9.6603 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMD': 290, 'SPY': 290}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 406.0300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.7519 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -23.4108 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -21.4323 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 89.5919 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 96.9776 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 75.3517 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 50.1568 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.9242 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 7.1739 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 10.2670 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6524 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 66.5793 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.2927 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -37.7290 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.2808 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 23.0608 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 56.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 17.8210 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 11.9600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.0948 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 86.7585 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 38.0128 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -9.6603 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -25.9543 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -6.2199 -> Clearly below the moving-average trend level.

## TAILWINDS

### AMD Stock Would Need to Rise About 57% to Get Back to Its Record. History Says How Long Past Comebacks Took.
- Summary: AMD Stock Would Need to Rise About 57% to Get Back to Its Record. History Says How Long Past Comebacks Took.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxQbWdrc3pFdTJ2OEVfc0FWQ3dtRWFWc0V5b1Rrb2RodkJhM0Zva0lfNjdmU1lWU3FlTTN2V2lLZnczbkRvQnRZMjFCR1ktUFUzcVhhcTF5ekhUTmJuUXRXOFlrVGVucXRmMGlWOTRPUWg1U2NMTzc0OFdLbld1NU1tZ2xyQTRGN0VIVFJoMmZkODE?oc=5>

### OpenAI and Meta Could Get 320 Million AMD Shares for a Penny Each
- Summary: Potential sale of AMD shares to OpenAI and Meta, indicating partnership opportunity.
- Date: 2026-11-24 | Impact: medium | Horizon: medium | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxPWm5YRk9KTTJXTGJKeHhFaWtKbS0xamJVR0VHZS1wb2hfR2hjOVR2bW1JY0R5bmxWOFcxVi1tWWFGNkVJVUh1UDBSOS1fUUt3ekdPcTd2c1F3cnFsM0FKOVRHSEJpR0h2UlhNNWRlZ1FqakZUZk1GRktXMTFNdHJ6SUExMTRQVERrMGxFRHZMOVNLWlAtZjlBTEN0bHk4bXJDVmNKRGFSZFFmYnUzQmc?oc=5>

### Nvidia, AMD, and Micron stocks trim steep losses amid jittery AI trade
- Summary: Stocks of Nvidia, AMD, and Micron trimmed losses amid AI market volatility.
- Date: 2026-11-25 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxOVk9mVUxsUll4NmpxRklUb1dFaHduU3ZURXZRV2ktV0pDM2ZMNElPb3RrV0NiS0JlLTVXQXJKNnpTV1JmV1k2NGMtdzNLa0F0c2tsY2xRMmJKZHhwY1dueWZXb0l4VXhWNkl4NmJ6QUlTNjBpZUItN0xkX21JUXJ5WGlUbWdON0E0V2FOT2lGYkozcm9VSjlXVjR3SDc5WWQ3VzJhWm5mb29YbjBQSU1hQURkYw?oc=5>

### Cathie Wood and Philippe Laffont Are on Opposite Sides of AMD Stock. Here's Who I Think Is Right.
- Summary: Analyst opinions diverge on AMD stock direction.
- Date: 2026-11-26 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxNclFJWkVlR0txRlk0VUFfSGRLNlFOY3JIRVFfNVM4cnVoMkZEOF9hTU95T29rSGhJcFl4cTFmeTJwd1JQV1ZrS294ZHZxRUdUV1VOUVdlNVBzMjYwTmVqUTV5SHZ6a2FaSzFYaTZWbE5tYjN6cFNBSFRka2s5WHlMbVR3QjhIcllzRjJZNVJydEZCZXh0M09xRGhiYnd3VmNtNXFTWEFiUVN4cEM5Ty1rc2w5NUpnWnJaOEQwcURLQWtrYVdXMkQ4dFBmNU11ZUF4QjBfSA?oc=5>

### Advanced Micro Devices falls amid Hunterbrook post on X (update)
- Summary: AMD shares fell following a Hunterbrook post on X.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxNOC1TMnJ4ZEFqaXY5ekZzemVYLTh1ekgzYWp2Yk1fMm5HVjdoMUtPMG83UUdZVkdsa3ZET2tyX2ZFRDhteTlDZnp5QVFZTUFReUlIS1hva0YwbVJlM3Q4YUV2YllCeWpodmt1TWRBWVQ1SUZ0WFVReW9raHptNzlVZW5BZllkZ2g2NHEtUzdfSXZMZGMyVWc2NXNqd1FTS2dtQWJmNWFQOEtZWEV0WWh0NnZjOWVtOEF4VUZtMWFwa2Y1aWM?oc=5>

### Chip Stocks Pull Back Again — Is AMD or Nvidia the Better Bet Right Now?
- Summary: Chip stocks pull back; debate over better bet between AMD and Nvidia.
- Date: 2026-11-25 | Impact: low | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOSGU1V3E5VDJnSVd3RG14V0E0aU1YQ3p1NGFRczh2SU1zbkJlLS1KdFFzOFFOUTNoektZNTlhVloyRE9iNlVlX1VvTFBZa1FqekZmU1ZNQ1poY1lnVGpGSGJoSzIxMFVDUHN0T0k1WnRqZWhkekRTcEpWX0ZrZ2JzZ19VYV84THZXNlVJeWFnVmMtcUg3M1lLVHRzZjdQeHZS?oc=5>

### AMD Stock Quote Price and Forecast
- Summary: Current AMD stock price and forecast information.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiT0FVX3lxTFBndUxfbjJEeVZYMi1wd2lPajZ3LTVYZkF0NVZ2Q1RuNDBPWkhGN184UlFoQ09FdmNBdl8wNFYtMURTNUU0Qm14aWVwcXFuV28?oc=5>

### Why Is AMD Stock Surging on Monday?
- Summary: AMD shares rise on Monday, indicating positive market sentiment.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQQnUyRHJUVmlNUWFHdUlKQko5OHl1azVBdU1OVlRqMkpqV0ltVjlHUVA4M3E1YmotSTNzeHp4NmExMkIzcUppQ0lReTdhQ1k1VUJ3Wk5zT0s3VFdOR3hOXzNING5GYlFHeU1ndEVkTFFJcVh2WVJMa0ZfVHBEbmlZMDhVR1JEMDJUTm02ckdiYVVsdlZmRlRkb2h1VWduZw?oc=5>

## HEADWINDS

### AMD shares slide as compliance questions emerge with Chinese blacklist server link and regulatory scrutiny risk
- Summary: AMD shares slide as compliance questions emerge with Chinese blacklist server link and regulatory scrutiny risk
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxQVGFnTm10MEdyUDc5LVhDOUljbFJLMjBQdTVkSExwMW9tNDhuZzk4NHViY3gxNVowaGZhM1dkV19KZjJjcXRIYTZBelV5a3piWVFCOGxCNTFiYjBoV1hUTnRQM1Vqb0Z2cEtYdkVORXpvWU1uODVXU2pzcFVfeEF1WGFZMS04VU1jeWZYLUNB?oc=5>

### AMD Stocks Slip 1.75% After Filing Registers 337 Million Shares for Resale
- Summary: AMD Stocks Slip 1.75% After Filing Registers 337 Million Shares for Resale
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxPcUt4YTdrRGJSaFhyT1BZdzJTbW4wTWR2dnJHZ1dWR2hLcGxKbDFmLS12VjFFQTVOaWQxNU9xaTdmRW40NWU4SXR3eWRscUphelBRRjJYUEVVM3JQUkJSVXpKM2RQb2ozaFVPMHhHM1RXYU9ad3dicktUalpLdERGM1haZkhJS2RCRHl3MkVjVTNLMmRYS0dBbzIzbDJwdkpWc014TVlVbDU0a2ZYdXF6TDh6Nmo0RzFQYmdFb3M2THNtQi1pNjN3WGlOeGFrUQ?oc=5>

### AMD Stock Shows the Market Has Stopped Making Sense After Huang’s Dramatic Return
- Summary: Stock volatility following CEO Huang’s return, negative market reaction.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxQZFZiUXAwenUzWFNOTXVsanB4ZEdoeU1nMFozQTF5T0NNRnZGZG1UVnhuWXFwb3Rhc2ZlU1h5dVc1aXUydlcxdEl3ZUZGY2p5MzBQUEZGSzNWb1ZkZ2tDQnh4NTJLX2FJUUtfSmVvQllMY3FESV9uc0g5Z25fTlpBV2FHMjhJY3M?oc=5>

### Is The Client Unit Still Carrying AMD Stock?
- Summary: Uncertainty about client holdings may weigh on AMD stock.
- Date: 2026-11-26 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNRGhOWkxLNFdXUlZ4bWtxSm5rTW95RlFLWFp5WTRsUndiYzZHZjJwWmE1YXh0MnhsTS1CWTA4S0VsWU00REdfa2FRdlVtRjQ3NGNJaU1JV0x4UUVaMTRKWmN6X1hqbThpUG1pVXNtWVBJOUhzUjlDbVIzclVyNy1DSjFRWUNQV21aQURXdkM3UmFheUZuY3dLa3NSSDhwU2ZUckFvdXl3?oc=5>

### Own AMD Stock? Watch Its Pile Of Unsold Chips
- Summary: Unsold chips suggest potential inventory issues for AMD.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxOaEEzTUFadDRsLTBrbTB0VzRwWXdyY2gzSEg2OTY5RWx2NDdRQ2s0WXQ5Mm5vaVBScGhLYVMzVU1iQWdRdk5pSzR2MFl0Tmh4dDJYZ0tKUXJYbU5tVDJscW5ZSFR6cGlOUGxGR0VNSmg1Y2JTZTBWS3F6ZUJoS255VnE0REVQUS1fYVRsU1NGQzFObXpPNlp3V0FwWXR2VHBKaGR6REpxaw?oc=5>

### Why Is AMD Stock Plunging Today Despite Strong Wall Street Buy Ratings?
- Summary: AMD shares fall today despite positive analyst ratings.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxNN1BDblNZcFJ1ZnhVV2drcVlxUEpmNk9KZWhWNU9wZXlaRWxSOGtJUXEzRG5XQ0dzX3NucTZLTE8yYkd5TmNQdTlRaVlycm1PUTYzcUtfcXFLbTBBSkJ2QldYaElpV0ZxQ2xYWFhrLVNWZDl3TXJLcnR3SXVBZm9hYTZqWlZYdGVxYk9Tb0c5THQ4dlNVUXItbnA5MTJkZERQU1cwWXlLN3ZKOWZPbWFZS3pJb1Q2clZFR2xoaVpuRU5fS3ZCc1Jual9DTQ?oc=5>

### Is AMD's Stock in Trouble After a Concerning Short-Seller Report?
- Summary: Short-seller report raises concerns about AMD's stock stability.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxPclhvdTVuOXdjb2dEZmc4YTNGUk5DZllnVzkzWTQwbl9NM1VxVGtsNjBLRnZUX1lXT196clVESUFZVXhUMzB3YzhZSUFSY0VWV2ZuckhkMW54dzV2aU9MVFJoLUpGVVZMNEFFaWszOENUR1Z4WUlxNDc1R2lmenhJRHQ1a0Y0ZXdPaXFwUW1CS2EtYU1UY3BQWlliVWlaX3lmaWRQUmhVNkZJdkE?oc=5>

## CATALYSTS

### Advanced Micro Devices, Inc. $AMD Stock Sold by Cunning Capital Partners LP
- Summary: Advanced Micro Devices, Inc. $AMD Stock Sold by Cunning Capital Partners LP
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxONGpMaDRBVGh4TWVKRDFsRUZKaC1LclpkUVJiN2N5TEM4QUZlMDhuUEZwd3NvaFRkOGxIVWpxeXdiX3N4SGVnVlZRcUlGZnRoMllGdkxiSENFWmlYOUpGQVBXUUdvMkNwY3lsYVlfN0xPXzhTY1BWZERLS2daZ29MUUEwb3prX0F2UEtEY2RvZ3Y0OGUtdXQzckJXNVdfTm8yaEJweVRrcUE1Z0pKYVJkd29FMlRBdkk3UFFfNURvdHpHeU14RTNNREswR0pEZw?oc=5>

### Stock Market Today, Nov. 23: Advanced Micro Devices Climbs on AI-Chip Rebound After Nvidia Reinstates Jensen Huang as CEO
- Summary: AMD shares rose on AI-chip rebound, linked to Nvidia CEO change.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwJBVV95cUxQeWlXazZSREdHVFpCWDBzdG1YTHQwU2JmZXc5Y0dqamhsaTV0YWo5UzFqbUk2aVM0Q0p6TWtxb3kzdUQtdVVySWg0V3lNRm1SSlNuMmx3V09SVGhvZUh6bS1hNmFHR05ENGdHSjRDR1o1SmxnTXJMYmQ0ZWdTRmhBbk0xTjBENHdoRUQ3RG1waTZNYkNodEFMdHZrQjRkRmJUUkxPWkxLR3dkUXdyaTNGcmwxdlp5SlFtRmxpMENLRTBoWDV3aE45cktrVU94Rnk2cXdlXzg1d3hQZ2g3NWgxbmxjc2trcEtvN1o1S3VHNThuS2dnTmZSVU15aUF2ZWFaaTdwU0ZKOWsyTnc?oc=5>

### Advanced Micro Devices, Inc. (AMD) is Attracting Investor Attention: Here is What You Should Know
- Summary: Investor attention highlighted, no specific event disclosed.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOZkZxQzNLc04tWGhod0c2ZmRjeW9pNHdhekQyOENwZ3A5YjhocURDeFpjUFZSNHNnUzRWQktUcGhZUnlmTGZBdTJVcVBxTFM0bC1DRWJidVlKemJlUktpYTQxTGtsUk1xSUZTRmdFRVhEbDdDakFyWl9YSHZ0NkRnaEszRGpZQ3VXM0JyQUxZUlFjS0ZvUGRkbVM4bw?oc=5>

### Advanced Micro Devices (AMD) Expands Into Quantum AI Computing With Drug Discovery Focus
- Summary: AMD announces expansion into quantum AI computing for drug discovery, signaling new product development and potential market growth.
- Date: 2026-11-25 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQMTdjc01MdVpRajNSamdRY1Jjd3ZZVE5La0oyX2tLZXQyZlg2cVp1Q0VhSXBIbl9ZVW1nN2ZGY2xndTY0NE5uX0FTNU85TlpEMTJjUDhaamFOaXZPNWNhVEZvV0hrb2FXOUprcDhKVmgydXl4TnlYNG5KSjZxQm1Ta0F4SGRUN1ZXdlVyVWw3VEQyRk54VVQ0YkRDMGNiVVE?oc=5>

## RISKS

### David Tepper Sold All of His AMD Stock. His Biggest Position Is Micron.
- Summary: Investor David Tepper liquidated his entire AMD position, potentially signaling negative sentiment.
- Date: 2026-11-25 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxPTGl1bWtTekVZUlZjbHA2eERfTFVwdnRyYldoVlNkUjYtOHBYVlBobEZBTXZIRkRQNGZyT3BaYk1vc0N0YUtzLXhrYTlGTk9lT0o5bEZaeDNaSUxHLVZQcy01REF3VDRDRUpleV9pMTEzbG5qM2JDclZnQjJWMUY5eTBLTTgzbVdlRXFuZ052WTNpU1AzRDFfRm9FWEhySzhzZzhBVFBrT2VTWnhuZVlpUnBR?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMD** | **86.76** | **9.74** | **59.17** | **44.70** | **672,006,275,072.00 USD** | **96.98** |
| NVDA | 16.04 | 13.50 | 14.55 | 103.20 | 3,605,147,156,480.00 USD | -15.84 |
| INTC | N/A | 2.52 | 15.80 | 20.90 | 289,508,032,512.00 USD | 52.02 |
| AVGO | 38.42 | 14.41 | 28.16 | 85.50 | 1,436,194,177,024.00 USD | -21.28 |

Peers fetched as_of: 2026-11-26; AMD reuses existing data (market data as_of: 2026-11-25); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-03
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-26

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 1,584,000,000.00 USD; period 2017-07-02/2017-09-30; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 2,428,000,000.00 USD; period 2026-06-28/2026-09-26; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMikAFBVV95cUxQbWdrc3pFdTJ2OEVfc0FWQ3dtRWFWc0V5b1Rrb2RodkJhM0Zva0lfNjdmU1lWU3FlTTN2V2lLZnczbkRvQnRZMjFCR1ktUFUzcVhhcTF5ekhUTmJuUXRXOFlrVGVucXRmMGlWOTRPUWg1U2NMTzc0OFdLbld1NU1tZ2xyQTRGN0VIVFJoMmZkODE?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxPWm5YRk9KTTJXTGJKeHhFaWtKbS0xamJVR0VHZS1wb2hfR2hjOVR2bW1JY0R5bmxWOFcxVi1tWWFGNkVJVUh1UDBSOS1fUUt3ekdPcTd2c1F3cnFsM0FKOVRHSEJpR0h2UlhNNWRlZ1FqakZUZk1GRktXMTFNdHJ6SUExMTRQVERrMGxFRHZMOVNLWlAtZjlBTEN0bHk4bXJDVmNKRGFSZFFmYnUzQmc?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxOVk9mVUxsUll4NmpxRklUb1dFaHduU3ZURXZRV2ktV0pDM2ZMNElPb3RrV0NiS0JlLTVXQXJKNnpTV1JmV1k2NGMtdzNLa0F0c2tsY2xRMmJKZHhwY1dueWZXb0l4VXhWNkl4NmJ6QUlTNjBpZUItN0xkX21JUXJ5WGlUbWdON0E0V2FOT2lGYkozcm9VSjlXVjR3SDc5WWQ3VzJhWm5mb29YbjBQSU1hQURkYw?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxNclFJWkVlR0txRlk0VUFfSGRLNlFOY3JIRVFfNVM4cnVoMkZEOF9hTU95T29rSGhJcFl4cTFmeTJwd1JQV1ZrS294ZHZxRUdUV1VOUVdlNVBzMjYwTmVqUTV5SHZ6a2FaSzFYaTZWbE5tYjN6cFNBSFRka2s5WHlMbVR3QjhIcllzRjJZNVJydEZCZXh0M09xRGhiYnd3VmNtNXFTWEFiUVN4cEM5Ty1rc2w5NUpnWnJaOEQwcURLQWtrYVdXMkQ4dFBmNU11ZUF4QjBfSA?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxNOC1TMnJ4ZEFqaXY5ekZzemVYLTh1ekgzYWp2Yk1fMm5HVjdoMUtPMG83UUdZVkdsa3ZET2tyX2ZFRDhteTlDZnp5QVFZTUFReUlIS1hva0YwbVJlM3Q4YUV2YllCeWpodmt1TWRBWVQ1SUZ0WFVReW9raHptNzlVZW5BZllkZ2g2NHEtUzdfSXZMZGMyVWc2NXNqd1FTS2dtQWJmNWFQOEtZWEV0WWh0NnZjOWVtOEF4VUZtMWFwa2Y1aWM?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOSGU1V3E5VDJnSVd3RG14V0E0aU1YQ3p1NGFRczh2SU1zbkJlLS1KdFFzOFFOUTNoektZNTlhVloyRE9iNlVlX1VvTFBZa1FqekZmU1ZNQ1poY1lnVGpGSGJoSzIxMFVDUHN0T0k1WnRqZWhkekRTcEpWX0ZrZ2JzZ19VYV84THZXNlVJeWFnVmMtcUg3M1lLVHRzZjdQeHZS?oc=5
- https://news.google.com/rss/articles/CBMiT0FVX3lxTFBndUxfbjJEeVZYMi1wd2lPajZ3LTVYZkF0NVZ2Q1RuNDBPWkhGN184UlFoQ09FdmNBdl8wNFYtMURTNUU0Qm14aWVwcXFuV28?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQQnUyRHJUVmlNUWFHdUlKQko5OHl1azVBdU1OVlRqMkpqV0ltVjlHUVA4M3E1YmotSTNzeHp4NmExMkIzcUppQ0lReTdhQ1k1VUJ3Wk5zT0s3VFdOR3hOXzNING5GYlFHeU1ndEVkTFFJcVh2WVJMa0ZfVHBEbmlZMDhVR1JEMDJUTm02ckdiYVVsdlZmRlRkb2h1VWduZw?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxQVGFnTm10MEdyUDc5LVhDOUljbFJLMjBQdTVkSExwMW9tNDhuZzk4NHViY3gxNVowaGZhM1dkV19KZjJjcXRIYTZBelV5a3piWVFCOGxCNTFiYjBoV1hUTnRQM1Vqb0Z2cEtYdkVORXpvWU1uODVXU2pzcFVfeEF1WGFZMS04VU1jeWZYLUNB?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxPcUt4YTdrRGJSaFhyT1BZdzJTbW4wTWR2dnJHZ1dWR2hLcGxKbDFmLS12VjFFQTVOaWQxNU9xaTdmRW40NWU4SXR3eWRscUphelBRRjJYUEVVM3JQUkJSVXpKM2RQb2ozaFVPMHhHM1RXYU9ad3dicktUalpLdERGM1haZkhJS2RCRHl3MkVjVTNLMmRYS0dBbzIzbDJwdkpWc014TVlVbDU0a2ZYdXF6TDh6Nmo0RzFQYmdFb3M2THNtQi1pNjN3WGlOeGFrUQ?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxQZFZiUXAwenUzWFNOTXVsanB4ZEdoeU1nMFozQTF5T0NNRnZGZG1UVnhuWXFwb3Rhc2ZlU1h5dVc1aXUydlcxdEl3ZUZGY2p5MzBQUEZGSzNWb1ZkZ2tDQnh4NTJLX2FJUUtfSmVvQllMY3FESV9uc0g5Z25fTlpBV2FHMjhJY3M?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNRGhOWkxLNFdXUlZ4bWtxSm5rTW95RlFLWFp5WTRsUndiYzZHZjJwWmE1YXh0MnhsTS1CWTA4S0VsWU00REdfa2FRdlVtRjQ3NGNJaU1JV0x4UUVaMTRKWmN6X1hqbThpUG1pVXNtWVBJOUhzUjlDbVIzclVyNy1DSjFRWUNQV21aQURXdkM3UmFheUZuY3dLa3NSSDhwU2ZUckFvdXl3?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxOaEEzTUFadDRsLTBrbTB0VzRwWXdyY2gzSEg2OTY5RWx2NDdRQ2s0WXQ5Mm5vaVBScGhLYVMzVU1iQWdRdk5pSzR2MFl0Tmh4dDJYZ0tKUXJYbU5tVDJscW5ZSFR6cGlOUGxGR0VNSmg1Y2JTZTBWS3F6ZUJoS255VnE0REVQUS1fYVRsU1NGQzFObXpPNlp3V0FwWXR2VHBKaGR6REpxaw?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxNN1BDblNZcFJ1ZnhVV2drcVlxUEpmNk9KZWhWNU9wZXlaRWxSOGtJUXEzRG5XQ0dzX3NucTZLTE8yYkd5TmNQdTlRaVlycm1PUTYzcUtfcXFLbTBBSkJ2QldYaElpV0ZxQ2xYWFhrLVNWZDl3TXJLcnR3SXVBZm9hYTZqWlZYdGVxYk9Tb0c5THQ4dlNVUXItbnA5MTJkZERQU1cwWXlLN3ZKOWZPbWFZS3pJb1Q2clZFR2xoaVpuRU5fS3ZCc1Jual9DTQ?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxPclhvdTVuOXdjb2dEZmc4YTNGUk5DZllnVzkzWTQwbl9NM1VxVGtsNjBLRnZUX1lXT196clVESUFZVXhUMzB3YzhZSUFSY0VWV2ZuckhkMW54dzV2aU9MVFJoLUpGVVZMNEFFaWszOENUR1Z4WUlxNDc1R2lmenhJRHQ1a0Y0ZXdPaXFwUW1CS2EtYU1UY3BQWlliVWlaX3lmaWRQUmhVNkZJdkE?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxONGpMaDRBVGh4TWVKRDFsRUZKaC1LclpkUVJiN2N5TEM4QUZlMDhuUEZwd3NvaFRkOGxIVWpxeXdiX3N4SGVnVlZRcUlGZnRoMllGdkxiSENFWmlYOUpGQVBXUUdvMkNwY3lsYVlfN0xPXzhTY1BWZERLS2daZ29MUUEwb3prX0F2UEtEY2RvZ3Y0OGUtdXQzckJXNVdfTm8yaEJweVRrcUE1Z0pKYVJkd29FMlRBdkk3UFFfNURvdHpHeU14RTNNREswR0pEZw?oc=5
- https://news.google.com/rss/articles/CBMiiwJBVV95cUxQeWlXazZSREdHVFpCWDBzdG1YTHQwU2JmZXc5Y0dqamhsaTV0YWo5UzFqbUk2aVM0Q0p6TWtxb3kzdUQtdVVySWg0V3lNRm1SSlNuMmx3V09SVGhvZUh6bS1hNmFHR05ENGdHSjRDR1o1SmxnTXJMYmQ0ZWdTRmhBbk0xTjBENHdoRUQ3RG1waTZNYkNodEFMdHZrQjRkRmJUUkxPWkxLR3dkUXdyaTNGcmwxdlp5SlFtRmxpMENLRTBoWDV3aE45cktrVU94Rnk2cXdlXzg1d3hQZ2g3NWgxbmxjc2trcEtvN1o1S3VHNThuS2dnTmZSVU15aUF2ZWFaaTdwU0ZKOWsyTnc?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOZkZxQzNLc04tWGhod0c2ZmRjeW9pNHdhekQyOENwZ3A5YjhocURDeFpjUFZSNHNnUzRWQktUcGhZUnlmTGZBdTJVcVBxTFM0bC1DRWJidVlKemJlUktpYTQxTGtsUk1xSUZTRmdFRVhEbDdDakFyWl9YSHZ0NkRnaEszRGpZQ3VXM0JyQUxZUlFjS0ZvUGRkbVM4bw?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQMTdjc01MdVpRajNSamdRY1Jjd3ZZVE5La0oyX2tLZXQyZlg2cVp1Q0VhSXBIbl9ZVW1nN2ZGY2xndTY0NE5uX0FTNU85TlpEMTJjUDhaamFOaXZPNWNhVEZvV0hrb2FXOUprcDhKVmgydXl4TnlYNG5KSjZxQm1Ta0F4SGRUN1ZXdlVyVWw3VEQyRk54VVQ0YkRDMGNiVVE?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxPTGl1bWtTekVZUlZjbHA2eERfTFVwdnRyYldoVlNkUjYtOHBYVlBobEZBTXZIRkRQNGZyT3BaYk1vc0N0YUtzLXhrYTlGTk9lT0o5bEZaeDNaSUxHLVZQcy01REF3VDRDRUpleV9pMTEzbG5qM2JDclZnQjJWMUY5eTBLTTgzbVdlRXFuZ052WTNpU1AzRDFfRm9FWEhySzhzZzhBVFBrT2VTWnhuZVlpUnBR?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
