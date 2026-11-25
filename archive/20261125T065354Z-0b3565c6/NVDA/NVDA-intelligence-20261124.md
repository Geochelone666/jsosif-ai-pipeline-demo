# NVDA Intelligence Report

- ticker: **NVDA**
- Report as_of: **2026-11-24**
- Market data as_of: **2026-11-24**
- Quant sources: https://finance.yahoo.com/quote/NVDA/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVDA/key-statistics/
- AI analysis snapshot as_of: **2026-11-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-25T07:18:04.724753+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 4, 'ai': 12, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261124T081701Z-6c335e3d/NVDA** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 8 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 52.0%; oldest publication 2026-11-23

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 155.3800 |
| Return 1D (%) | -5.8588 |
| Return 1W (%) | -0.0515 |
| Return 1M (%) | -26.3462 |
| Return YTD (%) | -16.4914 |
| Return 1Y (%) | -14.6797 |
| Annualized volatility (%) | 52.2027 |
| Beta vs SPY | 2.4029 |
| Max drawdown (%) | -47.5297 |
| Sharpe (rf=0) | -0.0591 |
| Downside deviation (rf=0, %) | 31.8614 |
| Sortino (rf=0) | -0.0968 |
| Historical VaR 95% (1D, %) | 4.3052 |
| Historical ES 95% (1D, %) | 5.9994 |
| Correlation vs SPY | 0.6884 |
| Tracking error vs SPY (%) | 43.2898 |
| P/E (trailing) | 16.69 |
| P/B | 14.05 |
| EV/EBITDA | 15.15 |
| Revenue growth (%) | 103.20 |
| Forward P/E (estimate) | 9.36 |
| Gross margin (%) | 74.92 |
| Operating margin (%) | 66.08 |
| Return on equity (%) | 117.36 |
| Free cash flow yield (%) | 2.65 |
| MA50 | 204.9464 |
| Close vs MA50 (%) | -24.1851 |
| MA200 | 202.8146 |
| Close vs MA200 (%) | -23.3882 |
| RSI (14, Wilder) | 39.4677 |
| MACD (12,26) | -17.2619 |
| MACD signal (9) | -16.0707 |
| MACD histogram | -1.1912 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVDA': 289, 'SPY': 289}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 155.3800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -5.8588 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.0515 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -26.3462 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -16.4914 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -14.6797 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 52.2027 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 31.8614 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.0968 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.3052 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.9994 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6884 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 43.2898 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.4029 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -47.5297 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.0591 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 9.3573 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.9210 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 66.0820 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 117.3640 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.6451 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 16.6896 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 39.4677 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.1912 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -24.1851 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -23.3882 -> Clearly below the moving-average trend level.

## TAILWINDS

### Nvidia stock jumps as DC makes stunning u-turn on Jensen Huang
- Summary: Nvidia stock jumps as DC makes stunning u-turn on Jensen Huang
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxNYVpaTEFMb19XbmlqTzZRaUtlWGk0TE9wa25vdXF0R3JpRHM4azRDSmxYZ09WYm13RlU0bDlKYk9JR0tqVEJtQkpubV9pcWROeGllektrMUcxYm9ZWkFPMENIMkdSWmlYRWRKUm9pX1RsV2VHaVlBalkweHhNNXg4dDUxZENWbFh3ODFOZFpHLWtPZ0JwZWFyZS1sVV85SElkUDFRZXB6THdrWVJxZmZlM1dXR0hTYlpyLTc0ZVJnbDRtMFRY?oc=5>

### Nvidia stock has best day since May 2003, gaining nearly $1T in market cap after Jensen Huang is reinstated as CEO
- Summary: Nvidia stock has best day since May 2003, gaining nearly $1T in market cap after Jensen Huang is reinstated as CEO
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiggJBVV95cUxPWE52dEljX0cyZVo2a1A1dWJaNXFBemdNUE9jcU94RjNXc1JwMEJyZkpjd3h5cHF0VFUxZWpCOTRpTlRRSzJBTlJGa0tubHEwa3VROU9xRFd4a1czS1Z3d05tMklnTFdESzMyTVRpdVFUQXBoMmkwdE0zd0V4TkcxRnhocTdBSm9fS3pvcksteFlqRGtIMUpjdldDbElVQlgzX3hMNWotbEJXelczemJac2h0TWhKeW9PTmJrZlIwNVBpY2VQVFVaRHFadlNOV0d2bWN2aDl4WlVQeU9IVkFRRUNDSU9tSV9xcjNJcFdJVGhkQWw0cmpJbld3WWE5OHhKcnc?oc=5>

### Nvidia Stock Soars on Jensen Huang Return: Dan Ives Says ‘$300 Stock with Jensen and a $225 Stock Without’
- Summary: Dan Ives links Jensen Huang’s return to a $300 stock price, boosting sentiment.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi9AFBVV95cUxNX0RPUDdQRFZSMF9COVFjQlBnbTA0eDRsMXlGejVob2pCSjFqb19jZUhKTWdCbjZJMDFTejk4Y2p3RERsazdRYjRBZTY2N3BvVXVKdWdvTFZRcjU1WmRzellGZEFpUllHbEwweWF5SFZqUzk5ZENJenBRRjNVRkhiWWRmbnctdUFONXc3RWVPVjFfajRCdnp2akFUZ1ZzcU5BdjBFYkNQN0FHMC1ZNVN4b2g3R3FtU29xM1Vqdy1maXZOWXgtX1BJZ1ptc2FUZ1REcndZZ3lhcGpkMl9ObFZlZU4xbEpxeDZqWWh6VldSQzYxbC1U?oc=5>

## HEADWINDS

### Nvidia live updates: Nvidia stock falls as exuberance fades after Jensen Huang's return as CEO
- Summary: Nvidia live updates: Nvidia stock falls as exuberance fades after Jensen Huang's return as CEO
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi6AFBVV95cUxNYnBZTkhUUGlCUVBvdW9Mam9JbGJueElLNmRUenk3eTZ2YmhXSEJhb3VCTTlrQ0xDZzF1N3pURFZFNDROVkZhOW1Mc0JxQUhGQ25rSjdWZXdxMnZNLWFaNzJfdXdFeEpUMzFQMUl3alZfWVotcFRHRGxSRzNiWHJuSlpyaXVHTld1MDFLSy1rdDJCU1F6ME9vZDB1bzB2bS1PeHpZbTg5czJrQ1lzdFRHbUlmS3JzYlFvQnRjZ2xRT3hoR1FVMUQ2a0hNMXZwNEtYckw1Q0ZYOThJMTlobXZTY3JzdDFESjBN?oc=5>

### Nvidia live updates: Nvidia stock falls 5% following huge rally after board reinstated Jensen Huang as CEO
- Summary: Stock fell 5% after CEO reinstatement, indicating short‑term volatility.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxPSWh4SkxkZkVEYVE0bHF3bzR2azhpV1pRbVJVSzJ2dHYyTEFwcFNFNFlLb25Qa0NnekRUTUlOcXd3SDBfZlJsdDVtOFNTd0VQS0RCWC1WaWZJdURybFFnZFRCM2h1SHA2RXNpWjQzLXNNMURST3dULWp4QVBKMVkycGVmeXN1eXJCWEZkaXg5YmVaTlp2SlpfM0pidU1ZaVExbGxKZXc4VG1vLVZDQTVYSTF3R2RGalo0LWVvcmtzdzVscHl0OEpsUF9RQU1wM0MyRHhQcEQ2ZEg?oc=5>

### Even With Jensen Huang Back as CEO, Nvidia Is Down 31% From Its High, While Broadcom Is Down 35%. Here’s the Better Buy Now.
- Summary: Nvidia shares down 31% from peak, suggesting a buying opportunity.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi8wFBVV95cUxOSXl4eU4zS3NEWWNUc1FZWkVSanFzYzM5VzlYbXBwQVduaFZTMTI2T21TdVZ4OEZpbl9EM21Kb2dTaEZIZHVnWEJURnVpb0NkdmwwT1pVRnhHSTBhMFJ2MzZ2d0JjU0JsX0FvbThyOU9XQVVsWnBGTjdtQnpiUU1YWkVxdjQyMW9xRkpPeXBjRlJKTFBHZ3l2NE9zcnFHZUxzU3FOZkRaQ25KUGZ4SUxweEQ3aU5Lb3ZYUWV0UFliSURBV2VwUm1EcVB2VFdMdWpqUXBpMkk3UDFLNnRKNWFoZDVnNVJlN1ZCZGJnMVMxVmN5UDg?oc=5>

### Nvidia, AMD, Broadcom lead chip stocks lower as AI trade comes under pressure
- Summary: Chip stocks, including Nvidia, fell amid AI trade pressure.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxPZlFHMUxxYkptX1RuUVVSbmwzSTJzY1R3N0VHQnBxakF2TzQwY1lheWFLSVhlSkY5TnJlaVBlZlpMTFo3Sml1M1ZEQnZ5VHZYekVpRHV0YTk3UnNvbUZzVzA1S201NkdCSjRvc0c4NXNtSkFBSFZTYUg0U1dlXzJsMXFrbUFQYm1DN1dHYW00eUR0Mjl2YlBRb3ZTams1ekNlNlBVaFpoaEx6d19mNVlyMmRuanM1Z1JQbmFBdGo0Nm02N2VLZGVBSHA3N0E?oc=5>

## CATALYSTS

### Nvidia (NVDA) Stock Looks Below Fair Value After Recent Turmoil
- Summary: Nvidia (NVDA) Stock Looks Below Fair Value After Recent Turmoil
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQbUpxbnpVNGpTNThJa3dsbWR4R3cyQ3hWbVFydFJ6bW10dldabWVTU3hPMGRoZlFhczNXZWgzbHppOVBIZzNKb1VTNWZ0dFd3S3lHdTJFRkdJOUo2N0FIQ1I3VnVPLVdwSWdmS1NsbWVmVW9WVXdrOFI5TnV2a1JFb0dfVWRjUWxMMUhwT0FQdUdRMEFvVFBjTjZR?oc=5>

### Is the AI Rally Safe With Jensen Huang Back at Nvidia—Here’s What Wall Street Thinks
- Summary: Wall Street assesses AI rally risk with Huang back.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxQeGVqQi1qQ0dvVlVDWXlNVUNSMklhbzdZWFBRWnZMbVlXVkpDZjZxd3dpNm4tM1RSLVF3QjFETHljS05TbHRDWXBXdlFCTlVyZXpGU3lWV21UU0YwU01VT0N5RGl5ZUxieVBUM0xQZkV5cTgzR3JZOXFLNjJPdzdZWHQxdVZDc0dHS2RudXFnU1pLNFpTU19SNWMtWkwtcmF4T1NIbXNaOUUwbkR5RVB6UDFuRTdua2xPejJHR3l1NnJkZXZ2?oc=5>

### Nvidia: Crisis Prices Won't Last (Rating Upgrade) (NASDAQ:NVDA)
- Summary: Analyst upgrades Nvidia rating, signaling confidence.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxPbC1nNWxqaUtsZ3oyOVFoOFJQd0ozS0VvZ1FWZmVmRTNPdm1sZXhCUk9fYTNPdkxXTk9mMGtEX3FqSzM2TXY1dUdLa1hUZ21MOEpBbU5XekQ5U1IyeE5RYWo4WlNJTHNDVERLOFdVLTJ4X2V5X19CV3VDOW90RkJWZ3VGbVFQNTNXaXZoMy1qUQ?oc=5>

### Nvidia stock soars as Trump makes U-turn on Jensen Huang, cheers Huang's return as CEO
- Summary: Jensen Huang returns as CEO, boosting stock sharply.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi4gFBVV95cUxNRXVUaE5oREVIRVpXeWxtcDNPVzl2aklWQXhtQkFCdlUxdDBiNEtjN3hoRFZlRVdENWp2cHFvWnpSOVJtcTN3bjlKYzZPOXhzMUZkVmRqLVlrOHVWTGYzSFA2alhrdFFnRnVEdHZoYnRkTGRzaGRKSWtYMUZZamkwbzdOdDY4R0FNaFhYY0RkMUowX1Y3eEZsRHhsakpzY01KVjZ6eU1nR0I2STVsd2pNMXJhSkFIcmJCU0diemtINklXaFdOd3R6Y3N2WHBKNWxmLW50QTlYOGtVRmxQY1MzRlFB?oc=5>

### Nvidia’s Jensen Huang Is Back. Is the Stock a Buy?
- Summary: Huang’s return prompts debate on Nvidia’s investment potential.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNM29tbkMyLS1Hb0dtRnRPRTg3blN4c0NiXzhhbkQySUJsbk9tel9tUHdIZ0QwVE8zYVFEQ3BFZEo2NTRrd2ZwTnAzVFEwU0ppVjBGajZ3bVNzNnJFdnhKZmlOYUNNUXZOb0dqX19ldzFpNWpQUEprTGR4emt4d09WckV5Ylh2LTBKMWNSSHJ3U09KWkdaRVdqeG1Udw?oc=5>

### Stock Market Today: Dow, Nasdaq Surge As Jensen Huang Makes This Nvidia Promise; Anthropic Falls
- Summary: Jensen Huang’s promise spurred market rally, signaling positive outlook.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.88
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxQbFRJSUJYanAyQ3Z1TzEwdDRnM084bjRZUTJNYlpHMDFZVk9zZzJ1d2NjSVUtcHpGWFpaVEppMzR6N203ZFVyRVRJQlpKSDY3TGMzMkUzMVVZRlFsUl9EdXdvY3FIbVEyVF9lcmdiNWdicl9McXU2NUNFMjIta0RmbEVkQ01nUXZ2NzRZYXJfTExSVVlNRE93SEN6ZFJ5N2Z1NXotbVZWQjNKMVlyYzRpdnNVRQ?oc=5>

### NVDA Stock Alert: What to Know as Nvidia Reinstates Jensen Huang as CEO
- Summary: Nvidia reinstates CEO Jensen Huang, signaling leadership stability and potential strategic shift.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNMk1OdWw0OUNTempyTUxOT19HRkRack4zalNNX014RVRaZXRiX0tvRzZ1ZDY5ZWdCYjlYYjUzNjVuLVJ4Sy0xcTkxMGMyemUtOVNiTDRlcEdyc1NkWHJjay16Q3dpN0ROSFllakIycEQ3U3cwOUw3X3QtTFJGWlU0RjRjSHhTVUdaaXNqc0xZZVVwbkNlQW54VQ?oc=5>

### Nvidia shares fall more than 5% as Huang comeback rally cools
- Summary: Shares drop over 5% amid cooling enthusiasm for CEO's comeback rally.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMieEFVX3lxTE52aUdsdjBXTkFjSkg1UVpmamJ6cXNsRWxPSGRGZXNMOFNuRWFHZEdudVdnQ2pRS0xKbFJvRUJmYldqSEl6UzFseHJWZzdENkNrbEdXd05yWEpyU3NOQjM3TVNjZUcyYVlKZ0RGTFlPVWF2T2hvX0tUVdIBfkFVX3lxTE9jTGJUVzdZamlIUjdnZlVNYkVhaDJ4MzY5MmpTZUpGMl9GRjZDSTNGR2FGenRsN0djalZxbjlrWUNCUXFOME9HdHdVTzdPTE9KT28wei1iTXl3bUxLSTZKRm1VWGhXVlhFQUpRMTV4ak9tUUtGdXZ6b29YNWhCQQ?oc=5>

### Nvidia, Chip Stocks Fall As Data Center Spending Fears Return
- Summary: Nvidia shares fall as fears over data center spending rise.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxQT2pCekFNSWpURGltMk04My1tZnVSaDFXbTFia1Z4a3JlbGpaaDgtRXZnTDdkeDdDSWE5VElWLXItTFIyRkpTaXpjYWhkYWkxaTNBSDUyYlVneGVPYmhYUzlHcHA4eThHeHBzWG5UUTJ2ZHhXR0g3SUdTR2FlME12S0ZEc3laVmF6ODFITFNDRQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVDA** | **16.69** | **14.05** | **15.15** | **103.20** | **3,751,960,903,680.00 USD** | **-14.68** |
| AMD | 88.31 | 9.91 | 60.24 | 44.70 | 683,988,942,848.00 USD | 92.17 |
| AVGO | 38.45 | 14.42 | 28.18 | 85.50 | 1,437,244,456,960.00 USD | -19.75 |
| INTC | N/A | 2.53 | 15.89 | 20.90 | 291,261,972,480.00 USD | 53.12 |

Peers fetched as_of: 2026-11-24; NVDA reuses existing data (market data as_of: 2026-11-24); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-17
- Next expected earnings: 2027-02-24 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-24

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-26
- Revenue (latest available single quarter): 96,221,000,000.00 USD; period 2026-04-27/2026-07-26; fiscal year/reporting period 2027/Q2
- Net income (latest available single quarter): 59,688,000,000.00 USD; period 2026-04-27/2026-07-26; fiscal year/reporting period 2027/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMixAFBVV95cUxNYVpaTEFMb19XbmlqTzZRaUtlWGk0TE9wa25vdXF0R3JpRHM4azRDSmxYZ09WYm13RlU0bDlKYk9JR0tqVEJtQkpubV9pcWROeGllektrMUcxYm9ZWkFPMENIMkdSWmlYRWRKUm9pX1RsV2VHaVlBalkweHhNNXg4dDUxZENWbFh3ODFOZFpHLWtPZ0JwZWFyZS1sVV85SElkUDFRZXB6THdrWVJxZmZlM1dXR0hTYlpyLTc0ZVJnbDRtMFRY?oc=5
- https://news.google.com/rss/articles/CBMiggJBVV95cUxPWE52dEljX0cyZVo2a1A1dWJaNXFBemdNUE9jcU94RjNXc1JwMEJyZkpjd3h5cHF0VFUxZWpCOTRpTlRRSzJBTlJGa0tubHEwa3VROU9xRFd4a1czS1Z3d05tMklnTFdESzMyTVRpdVFUQXBoMmkwdE0zd0V4TkcxRnhocTdBSm9fS3pvcksteFlqRGtIMUpjdldDbElVQlgzX3hMNWotbEJXelczemJac2h0TWhKeW9PTmJrZlIwNVBpY2VQVFVaRHFadlNOV0d2bWN2aDl4WlVQeU9IVkFRRUNDSU9tSV9xcjNJcFdJVGhkQWw0cmpJbld3WWE5OHhKcnc?oc=5
- https://news.google.com/rss/articles/CBMi9AFBVV95cUxNX0RPUDdQRFZSMF9COVFjQlBnbTA0eDRsMXlGejVob2pCSjFqb19jZUhKTWdCbjZJMDFTejk4Y2p3RERsazdRYjRBZTY2N3BvVXVKdWdvTFZRcjU1WmRzellGZEFpUllHbEwweWF5SFZqUzk5ZENJenBRRjNVRkhiWWRmbnctdUFONXc3RWVPVjFfajRCdnp2akFUZ1ZzcU5BdjBFYkNQN0FHMC1ZNVN4b2g3R3FtU29xM1Vqdy1maXZOWXgtX1BJZ1ptc2FUZ1REcndZZ3lhcGpkMl9ObFZlZU4xbEpxeDZqWWh6VldSQzYxbC1U?oc=5
- https://news.google.com/rss/articles/CBMi6AFBVV95cUxNYnBZTkhUUGlCUVBvdW9Mam9JbGJueElLNmRUenk3eTZ2YmhXSEJhb3VCTTlrQ0xDZzF1N3pURFZFNDROVkZhOW1Mc0JxQUhGQ25rSjdWZXdxMnZNLWFaNzJfdXdFeEpUMzFQMUl3alZfWVotcFRHRGxSRzNiWHJuSlpyaXVHTld1MDFLSy1rdDJCU1F6ME9vZDB1bzB2bS1PeHpZbTg5czJrQ1lzdFRHbUlmS3JzYlFvQnRjZ2xRT3hoR1FVMUQ2a0hNMXZwNEtYckw1Q0ZYOThJMTlobXZTY3JzdDFESjBN?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxPSWh4SkxkZkVEYVE0bHF3bzR2azhpV1pRbVJVSzJ2dHYyTEFwcFNFNFlLb25Qa0NnekRUTUlOcXd3SDBfZlJsdDVtOFNTd0VQS0RCWC1WaWZJdURybFFnZFRCM2h1SHA2RXNpWjQzLXNNMURST3dULWp4QVBKMVkycGVmeXN1eXJCWEZkaXg5YmVaTlp2SlpfM0pidU1ZaVExbGxKZXc4VG1vLVZDQTVYSTF3R2RGalo0LWVvcmtzdzVscHl0OEpsUF9RQU1wM0MyRHhQcEQ2ZEg?oc=5
- https://news.google.com/rss/articles/CBMi8wFBVV95cUxOSXl4eU4zS3NEWWNUc1FZWkVSanFzYzM5VzlYbXBwQVduaFZTMTI2T21TdVZ4OEZpbl9EM21Kb2dTaEZIZHVnWEJURnVpb0NkdmwwT1pVRnhHSTBhMFJ2MzZ2d0JjU0JsX0FvbThyOU9XQVVsWnBGTjdtQnpiUU1YWkVxdjQyMW9xRkpPeXBjRlJKTFBHZ3l2NE9zcnFHZUxzU3FOZkRaQ25KUGZ4SUxweEQ3aU5Lb3ZYUWV0UFliSURBV2VwUm1EcVB2VFdMdWpqUXBpMkk3UDFLNnRKNWFoZDVnNVJlN1ZCZGJnMVMxVmN5UDg?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxPZlFHMUxxYkptX1RuUVVSbmwzSTJzY1R3N0VHQnBxakF2TzQwY1lheWFLSVhlSkY5TnJlaVBlZlpMTFo3Sml1M1ZEQnZ5VHZYekVpRHV0YTk3UnNvbUZzVzA1S201NkdCSjRvc0c4NXNtSkFBSFZTYUg0U1dlXzJsMXFrbUFQYm1DN1dHYW00eUR0Mjl2YlBRb3ZTams1ekNlNlBVaFpoaEx6d19mNVlyMmRuanM1Z1JQbmFBdGo0Nm02N2VLZGVBSHA3N0E?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQbUpxbnpVNGpTNThJa3dsbWR4R3cyQ3hWbVFydFJ6bW10dldabWVTU3hPMGRoZlFhczNXZWgzbHppOVBIZzNKb1VTNWZ0dFd3S3lHdTJFRkdJOUo2N0FIQ1I3VnVPLVdwSWdmS1NsbWVmVW9WVXdrOFI5TnV2a1JFb0dfVWRjUWxMMUhwT0FQdUdRMEFvVFBjTjZR?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxQeGVqQi1qQ0dvVlVDWXlNVUNSMklhbzdZWFBRWnZMbVlXVkpDZjZxd3dpNm4tM1RSLVF3QjFETHljS05TbHRDWXBXdlFCTlVyZXpGU3lWV21UU0YwU01VT0N5RGl5ZUxieVBUM0xQZkV5cTgzR3JZOXFLNjJPdzdZWHQxdVZDc0dHS2RudXFnU1pLNFpTU19SNWMtWkwtcmF4T1NIbXNaOUUwbkR5RVB6UDFuRTdua2xPejJHR3l1NnJkZXZ2?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxPbC1nNWxqaUtsZ3oyOVFoOFJQd0ozS0VvZ1FWZmVmRTNPdm1sZXhCUk9fYTNPdkxXTk9mMGtEX3FqSzM2TXY1dUdLa1hUZ21MOEpBbU5XekQ5U1IyeE5RYWo4WlNJTHNDVERLOFdVLTJ4X2V5X19CV3VDOW90RkJWZ3VGbVFQNTNXaXZoMy1qUQ?oc=5
- https://news.google.com/rss/articles/CBMi4gFBVV95cUxNRXVUaE5oREVIRVpXeWxtcDNPVzl2aklWQXhtQkFCdlUxdDBiNEtjN3hoRFZlRVdENWp2cHFvWnpSOVJtcTN3bjlKYzZPOXhzMUZkVmRqLVlrOHVWTGYzSFA2alhrdFFnRnVEdHZoYnRkTGRzaGRKSWtYMUZZamkwbzdOdDY4R0FNaFhYY0RkMUowX1Y3eEZsRHhsakpzY01KVjZ6eU1nR0I2STVsd2pNMXJhSkFIcmJCU0diemtINklXaFdOd3R6Y3N2WHBKNWxmLW50QTlYOGtVRmxQY1MzRlFB?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNM29tbkMyLS1Hb0dtRnRPRTg3blN4c0NiXzhhbkQySUJsbk9tel9tUHdIZ0QwVE8zYVFEQ3BFZEo2NTRrd2ZwTnAzVFEwU0ppVjBGajZ3bVNzNnJFdnhKZmlOYUNNUXZOb0dqX19ldzFpNWpQUEprTGR4emt4d09WckV5Ylh2LTBKMWNSSHJ3U09KWkdaRVdqeG1Udw?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxQbFRJSUJYanAyQ3Z1TzEwdDRnM084bjRZUTJNYlpHMDFZVk9zZzJ1d2NjSVUtcHpGWFpaVEppMzR6N203ZFVyRVRJQlpKSDY3TGMzMkUzMVVZRlFsUl9EdXdvY3FIbVEyVF9lcmdiNWdicl9McXU2NUNFMjIta0RmbEVkQ01nUXZ2NzRZYXJfTExSVVlNRE93SEN6ZFJ5N2Z1NXotbVZWQjNKMVlyYzRpdnNVRQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNMk1OdWw0OUNTempyTUxOT19HRkRack4zalNNX014RVRaZXRiX0tvRzZ1ZDY5ZWdCYjlYYjUzNjVuLVJ4Sy0xcTkxMGMyemUtOVNiTDRlcEdyc1NkWHJjay16Q3dpN0ROSFllakIycEQ3U3cwOUw3X3QtTFJGWlU0RjRjSHhTVUdaaXNqc0xZZVVwbkNlQW54VQ?oc=5
- https://news.google.com/rss/articles/CBMieEFVX3lxTE52aUdsdjBXTkFjSkg1UVpmamJ6cXNsRWxPSGRGZXNMOFNuRWFHZEdudVdnQ2pRS0xKbFJvRUJmYldqSEl6UzFseHJWZzdENkNrbEdXd05yWEpyU3NOQjM3TVNjZUcyYVlKZ0RGTFlPVWF2T2hvX0tUVdIBfkFVX3lxTE9jTGJUVzdZamlIUjdnZlVNYkVhaDJ4MzY5MmpTZUpGMl9GRjZDSTNGR2FGenRsN0djalZxbjlrWUNCUXFOME9HdHdVTzdPTE9KT28wei1iTXl3bUxLSTZKRm1VWGhXVlhFQUpRMTV4ak9tUUtGdXZ6b29YNWhCQQ?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxQT2pCekFNSWpURGltMk04My1tZnVSaDFXbTFia1Z4a3JlbGpaaDgtRXZnTDdkeDdDSWE5VElWLXItTFIyRkpTaXpjYWhkYWkxaTNBSDUyYlVneGVPYmhYUzlHcHA4eThHeHBzWG5UUTJ2ZHhXR0g3SUdTR2FlME12S0ZEc3laVmF6ODFITFNDRQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
