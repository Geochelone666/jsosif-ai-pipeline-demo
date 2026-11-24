# GOOGL Intelligence Report

- ticker: **GOOGL**
- Report as_of: **2026-11-23**
- Market data as_of: **2026-11-23**
- Quant sources: https://finance.yahoo.com/quote/GOOGL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/GOOGL/key-statistics/
- AI analysis snapshot as_of: **2026-11-23**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-24T08:35:06.945666+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 10, 'ai': 12, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261123T053847Z-45053549/GOOGL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 14 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 28.0%; oldest publication 2026-11-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 282.1000 |
| Return 1D (%) | 6.3365 |
| Return 1W (%) | -0.5710 |
| Return 1M (%) | -11.9016 |
| Return YTD (%) | -9.6969 |
| Return 1Y (%) | -5.6151 |
| Annualized volatility (%) | 33.6479 |
| Beta vs SPY | 1.2572 |
| Max drawdown (%) | -34.0273 |
| Sharpe (rf=0) | -0.1877 |
| Downside deviation (rf=0, %) | 24.2789 |
| Sortino (rf=0) | -0.2601 |
| Historical VaR 95% (1D, %) | 3.1840 |
| Historical ES 95% (1D, %) | 4.8274 |
| Correlation vs SPY | 0.5595 |
| Tracking error vs SPY (%) | 28.1529 |
| P/E (trailing) | 14.73 |
| P/B | 5.26 |
| EV/EBITDA | 18.17 |
| Revenue growth (%) | 24.70 |
| Forward P/E (estimate) | 18.44 |
| Gross margin (%) | 60.86 |
| Operating margin (%) | 33.32 |
| Return on equity (%) | 44.29 |
| Free cash flow yield (%) | -0.03 |
| MA50 | 320.9548 |
| Close vs MA50 (%) | -12.1060 |
| MA200 | 336.5087 |
| Close vs MA200 (%) | -16.1686 |
| RSI (14, Wilder) | 41.0376 |
| MACD (12,26) | -12.7405 |
| MACD signal (9) | -12.9928 |
| MACD histogram | 0.2523 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'GOOGL': 288, 'SPY': 288}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 282.1000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 6.3365 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.5710 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -11.9016 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -9.6969 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -5.6151 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 33.6479 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 24.2789 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.2601 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.1840 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.8274 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5595 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 28.1529 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.2572 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -34.0273 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.1877 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 18.4411 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 60.8570 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 33.3210 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 44.2860 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: -0.0335 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 14.7311 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 41.0376 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.2523 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -12.1060 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -16.1686 -> Clearly below the moving-average trend level.

## TAILWINDS

### Alphabet Stock Pops: What's Going On?
- Summary: Alphabet Stock Pops: What's Going On?
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOc1RxLWU5d3g3QTUxMk1LUm5fRjhnYlJ6UnVVb2VMVmtOemZFU0RGUjBaQVpwYkUwa052R0pFUFZReE00RWRxdjB1UnlROE5VNS1CVDVuSEhLdThDeElCVmd0bGYwS01yX1g1QXlWeE1FZV9OaWNCWXlraXd2ZmQ2SlJJdkhOMlR3WjllY2I2NDl5RXFWOFgtVXl1aw?oc=5>

### Alphabet rises 6% as broad market rally lifts shares (GOOG:NASDAQ)
- Summary: Alphabet rises 6% as broad market rally lifts shares (GOOG:NASDAQ)
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOVWhOYkM3RENzRGRqaGJWR1o2THE0eGFBZHlpRHBiWWU4SjRUejJpZkVJZkhsenB6SmM4UDVOWUp5anJ2cWpVSkd1cktRZ0J5Y2VwNFYxd1dpYlY5NFEzQTdteWFsUlJIRDBZbmkxaUROaDlEcFVTTWpXQUdDNW9ab1VpQkVuRDhUbHQzWWFoWkVjTU82MWs5T3dlME9TUQ?oc=5>

### Alphabet Stock Is Jumping. 2 Reasons the Comeback Starts Now.
- Summary: Alphabet Stock Is Jumping. 2 Reasons the Comeback Starts Now.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMieEFVX3lxTE10WDdwclZjV3ltY3NHVm9ia044N0huUnBJZGgtN1FkalNkajRpS1R4XzFjYjg3ajRXS0hwWDdvbHdPQ0k5eWxhSHBuOS1Da2x5S285MFJ1QVVwN2Nob2pLQlZmYVlwQ1ljT2VOaXBPMWMzU3dkaE5Wbg?oc=5>

### Alphabet Stock Jumps 6.8% as Nvidia's Huang Return Reignites AI Trade
- Summary: Alphabet Stock Jumps 6.8% as Nvidia's Huang Return Reignites AI Trade
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMidkFVX3lxTFAwWHZ2V1dxQ2l4anlaY196R19jS0NQcWFIa1B2LWJPSFgzY041MEZqZUV1b2tPcTlaVC16dkw0S2ppR09nLUxrTEpvbk8zQzlMQndZS3FsSEpaS2t4elRxcm1qVEhEYlVIYVhZUlp4RmhwZlE5b1E?oc=5>

### Alphabet Stock Risks Breakdown Below $270 Support as Anthropic Deal, Gemini Expansion and Rising Costs Weigh on GOOG
- Summary: Alphabet Stock Risks Breakdown Below $270 Support as Anthropic Deal, Gemini Expansion and Rising Costs Weigh on GOOG
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7gFBVV95cUxPX2Vtd1RONnpHYk5ia01paUJUNlEtc3BMUk9wNVRoTV91dHdVRkNKZDZ2UEl6X0M0d25MLVhzdFdyWk9zTF9tWm1Xa04wQndpa0RTS28yaHgtaktYajE0MHlVTmVwY20tZEZkM2RGV3dfV2Z5NzNIVXk3ZEZqLUpnNTN1UmNPWTE0cWE0VDBKakdFaWNwRnd2bXBhSTZucWNXNVVNOVcyaDFkd0JZYVpwZmhRTVhTd2s5Q2NHWHlsaHYzdlBiYlVUZHJzQTFHalBBYWFmbmpITjdTN3F3ZmNPdDY1X0d2c2YyTENqaDVB?oc=5>

### Alphabet shares climb as AI trade rebounds around Anthropic IPO
- Summary: Alphabet shares climb as AI trade rebounds around Anthropic IPO
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPYjFPbkJ5QWFsT3Z5NzdtbDNQa1BqNmVwVGF0cmFKQjNWTmlTbERHS215SUNXNHVkajFTXzVlRm1ZdDEwa0RRVktyeUFnVmVSN3pIOXVPTk03OVBzTVlaVFZCblI1bVpzV25wQzF0S0M3SHVSZ1ppUHpJRzdGOXk1ejRRQzBXQ3FGZDF0Ry01ZUUzMjBtelNDeU5VOTM?oc=5>

### If I Could Only Own 1 Trillion-Dollar Artificial Intelligence (AI) Stock Through 2030, It Would Be Anthropic, Nvidia, or Alphabet. Here’s My Top Pick.
- Summary: Analyst highlights Alphabet as top AI stock pick for 2030, citing strong AI prospects.
- Date: 2026-11-20 | Impact: medium | Horizon: long | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilAJBVV95cUxOWHEwZzB6MUFKZDF0OW41SjF6OGtoOWs3N3RhZ2NRVzBVVkhjV1hhVFhEeWtteTZxVjVVVVY0Zk96LUw4SlNiMEFsRnM1eXhDRi1ULTh0UXpicWYzZHlCTXlsVmhLSVp4YjByeHluMWpVYUNkbFBRN3dueGdrVzh3R0RGeGlITGFacmNDZkhzM28yNEdVMTlDRl9IY1BiTXEzLU9yeExrTXlGcVZsemVkQTlsRi1EVVNaYUdoOXdqVDJBX0lfbmJ2ZFc3aHZUcmM2MjViZXVFNFJydHJOODZzUmJnMHd4UTZoYUR2bEF4MjRGbHp1eFRDZF9jUDlPZFZrZnF5QlkzMzBkQTl3VllnbTFUVWU?oc=5>

### Alphabet (GOOGL) Nears $84.8 Billion Raise As It Weighs $3 Billion Settlement
- Summary: Alphabet is close to raising $84.8B while considering a $3B settlement, potentially boosting capital and investor confidence.
- Date: 2026-11-21 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQeFJwUjdDUXhMVWJrTzJJaks0b3I5ZDlJWGdHMnVxZ1FyVndOVmhCdVFsbUZFSG9OYWtJZHlZNDhOSGJsazlQc0xPczdqM3lhczJhX2E4SEtvb0M2dThmcUpHMDBWeU9IVlByc25aclZvSHhQMXR4V24wZkhDRUU4NHE1OWNfVE00T1YyNlBzelhGdmt6?oc=5>

### Why Alphabet Stock Popped Today
- Summary: Alphabet shares experienced a notable rise, reflecting investor optimism and positive market sentiment.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQM3R1cDUtT05XY2ttV01jTDF1WFZlZy16UUt5aTVNdXVfdXJRMXJuU3c2SnlNckdqdHRTLWxfUkJCQzktT3hhRElBZHNWM2pQLWlRa081YThFRGcwTjVwdWdXb0ZCU3EybG9JUmhJbnJpVkVXSHFISnplRDZNUWZwUUZlOEQ1dzFOa0x4Z1FSSWtJVDFUeUN1SkphUHQ?oc=5>

### Alphabet’s (GOOGL) AI Investment Is Surging – Here’s Why the Funding Matters
- Summary: Details Alphabet’s increasing AI investment and its strategic importance.
- Date: 2026-11-20 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxQTEpBaHhwRlV4dTFyUkFsZjI0TF9oZzBLNEt6QmdhU01sMHVoQjJ4am1QSlY3RWp2Mk5oREJxZ1VTc3BJNml1eVBUdkNaa3JkMDJlN0l6N1VNTUpfSmNfX25ZM2RwYUZOY0sxV3hHRHJtLXl2N2taZkJtSS10ZHlRVXZIUHJfTWZMbl9oaS1n?oc=5>

## HEADWINDS

### Alphabet Stocks Fall 3.46% Even as Anthropic Debut Values Its Stake at $172 Billion
- Summary: Alphabet Stocks Fall 3.46% Even as Anthropic Debut Values Its Stake at $172 Billion
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNLW1yYUxsRnJGcnFEQzJhSGJWV0JHeUNEN1prTXBhQzI1eXdSc292OEVVSjNpUDBCMk93TUU2U3B3Y19RYU9qWVJsa1NuNHpORnFHSTV1QnRvYjRtNE9tY2ZHZ3B3UnJZWVJWZUNpeEdUSm1KZ2pnYjJrQlBGTS1LTmo5Z1dmRFo0Q0FDNlY2Ui01eW9M?oc=5>

### Alphabet (GOOGL) Stock Could Be 47% Undervalued As AI Spending Fears Bite
- Summary: Analyst warns AI spending fears may undervalue Alphabet, suggesting a medium‑term headwind.
- Date: 2026-11-19 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNT1ZWV245S1M1R2I2RVIyNHprYlZwcGN1eGlRWE9ZNTJYd0Q3V2xyb0FFZWdNcFRhVHVPVUtKdEdrYmd4bDlNbkRkdTNFazJLUU1wS0g1WlVFd3U3YU1pbkl4R09QVmFkVEZYMTNjU1FJbnU0bGY5Mk9zNWxFcWV2Y0h1aDF1aGlnYjBmNk53LU5TaHVwdTBmRjd3?oc=5>

### Alphabet Stock Just Hit a 1-Year Low. Why Is Google's Parent Borrowing So Much Money?
- Summary: Alphabet's stock fell to a 1-year low amid concerns over high borrowing levels.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxOZWlMZ2JfQi1mSmxiLS00Mml1VDR1Q0tuVjZSaks4dHh6bU5Ld0oxQ01QUVhtN0x6c3Q0cmtFVzBoUC1jNzB3TTRUdmU5TTJZUk01blptY09QV0o5UHpxdzRPUzVrSWNsaTkwMktGLUhNYktFNWVIb0pYc2Riemt4WnlSd01oZFMtYVpFUHlIT2lUT1FJalJVQ2lKalpfY2dtS0VrS2xnRDl0NzhqUFdjVGxUQlFEUXItd0ctM1BNTXJiaU9p?oc=5>

## CATALYSTS

### Alphabet (GOOGL) Stock Gets Fair Value Trim As Analysts Weigh AI Spending And Monetization
- Summary: Alphabet (GOOGL) Stock Gets Fair Value Trim As Analysts Weigh AI Spending And Monetization
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxON3V6WEZ5MTczaE84bktQaVNVMWY0d1ZBTDZhZW92R2pQX2RzUnZZYVJ4bzVCMTA4R0Mtbk9hUWV0cnJSdkh2MktNVjAyaFJMTVB1NEFram1EcnlqOVRHdWRMa1kwUDBJWEhRZ0ZVRkxVV0FabGtVa1NCREhWMjBkZ1N2c29mYzVodFV4T2RXdUJCMGRzQmF1MzEzTQ?oc=5>

### Alphabet (GOOGL) Stock Trades Below Fair Value Despite AI Chip Expansion
- Summary: Alphabet (GOOGL) Stock Trades Below Fair Value Despite AI Chip Expansion
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxOQ0V4Y1NuZ05CT1FXd0pOZ0dIdFJnY1V4YzB0MUk3dmhkaTVNaVIyc1lFaTRVb1lid294WUxYeTZxR29uWk5QMk5SY0hCTFVSRVlQdlo5VVV6dFpGTnFiN0IzdzNFcENvRTktUHZlSjZ1enJOcmpvYjhmb3NMR0RYS09SbWVQdWJOT0Jsc0VOS19EREljTEJuc3J3MklINDQ3MnBSY05TNjRBUmR2RTNyLUczRC04MGRLRHBhTER5ZkN4YXfSAcgBQVVfeXFMT09xeUxVdGlSQzBOQlNERlVRQjJTX3pPQVJqZFA1SEtlWGllaldnN21CNnRiMzNXSHN0c2p0ZTRNaEk1Z2hVZWxISHhRNWw2ZlZ2TmN0THN5Q2ZTV1RsVVE0a1p0VTYwNjJRMjYtXzdQMmMySnR4TzE5ZG82Z2R2YjJTUl9YTk1EYTNZZFFsVTBsMk16dHEzd2hFVUxUQTlMcC1HVldrc0RubWRyOUdEN3lWRUJTc1BDeV9HaWNYZGtPUW11UnpRWW8?oc=5>

### Alphabet Stock GOOGL Rebounds From Support as Anthropic Stake Pre IPO and Nvidia Earnings Lift GOOG
- Summary: Alphabet Stock GOOGL Rebounds From Support as Anthropic Stake Pre IPO and Nvidia Earnings Lift GOOG
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxPSl8yMUJzOEtDTzBiejNkWEFmZUktVW12Wk1vQm1NZVlUb3hxSUZ1MVJPczM2MmlvZC1YOTBaVk5Xdm42bzlVMnp2WGNfSkZDYjdvdDhUV1hkMEg2NE0xd1ltOExMSjZnekRxZ3FCaXRhMmF4ZWdNSzB0REFrbzJKd2VCRTBiNlhJYmRISjNjU2Fzc2VGNUFSU1puOUtNdXVzNkE1ODAwbFRyYWRlZWRaaTlvdndmdWE0VmtLMFItVjZaUzFTVlkwRHgwUUpDWHoxVGtjdDlfR0UxUQ?oc=5>

### Why Is Google Stock Up Today? Alphabet Jumps 6.3% as Nvidia's Huang Return Sparks AI Rally
- Summary: Alphabet shares rise 6.3% amid AI rally triggered by Nvidia CEO return.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxNMk80VUp2ZGs5bVJLVG55OVJ5VnhwRXNvY1I0RGloZzBvRTlfRWVQZGpFeVdGbmIwbzlyWnJGSnQtdWY5a3JOTWVPWG4yVVlGT25BSGxFUl9Jb2VNczlTYnlpSXFuT05pN2ZiQndudm9zTVk4bEN2M3RRZVM2am56a2hQQ1BaVDJwYm40YjFNbngxck11UEd1eDVtakFjTEhqX1JBYTR1cWljeTNNMmtJUVl3RHI?oc=5>

### Why Alphabet stock is trading up today
- Summary: Alphabet shares are up today, reflecting positive market sentiment.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPcFptQ3RmT1VCa1htc21fY09VX3pyeU9YT0NXeU1UX3JxUFlTMFc1TG1nd3RCVlhPRUdMeTNGNUJTaDVCb2VSb3haQ2lycUFtdUllVmtUVW5rUXhBRmdNMnAzWU9vU2dTYVZZRFdiU0NBYnc3X0J4MlhYTkNIWEw2S0JIWHJKMFk0R0E3WENJWDZhU2lqS0dPX3RsUGh6RDM0?oc=5>

### Alphabet, AMD among AI stocks hedge funds are cutting - Goldman (SPY:NYSEARCA)
- Summary: Hedge funds are reducing positions in Alphabet and AMD AI stocks.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNSnRqZEd2YXN5WktjUlRXQkVOY3dZenpNam1ZTzZEZFNLWks5NnI5X0VTUHhHUUVYT1I4eWNGeHJjem9tcXRZN1VERERpRkUtbU9TSFRob1EzeDBkY0tVNjBOcUJtM2QyNGptMS15U1NsSG9RNWo3eWIzV2ZfaG11VTFxaV9OZkwtNzlWSnRoT3ZJaEM3aFpicW5RTzBEZ3c?oc=5>

### Stock Market Today, Nov. 19: Alphabet Shares Fall as Anthropic Nasdaq Debut Puts Fresh Value on Google's Stake
- Summary: Alphabet shares fall after Anthropic's Nasdaq debut boosts competition.
- Date: 2026-11-19 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQVDF4Sm92d3dlRThhcXhmdHItbXd5N2E3bVlFLXpzVnEzXzhwQzlTM2ZnMl80VnZQWGNRQnhBY2J5VGx3NHRxMDhRSEpONWtWV1MzMjZpRjJFQzhkQzMwUUFFSDMwb21oNDk1SktveTF6alBMcGEtMjVLWmJWejdQS1otSnZPMzlvRWVKRzJIRlZLZ01K?oc=5>

### Alphabet Inc Class A Stock (GOOGL) Opened Up by 4.63% on Nov 23: Drivers Behind the Movement
- Summary: Alphabet stock opened up 4.63% on Nov 23, citing various drivers behind the movement.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxPZUJIRDh4bVZNcnFhTFQyR3F6a3pCQWl2M2RvWEVxX0hYSFRKbGYwVE5OUzRrTHREbDgtTVo2WFptZ0FCQTBTM183bnNFcnNxVnNBQ01KUHphYlF4WmNfM2tTLTZHTmtKU3JyVGlMNGU1enQ5VFczTDVDYVdDYk5aZmQxamNGYjZGS09URg?oc=5>

## RISKS

### Alphabet (GOOGL) Nears $3 Billion Settlement as Freeway Ban Hits Robotaxis
- Summary: Alphabet nears $3B settlement over freeway ban affecting robotaxis.
- Date: 2026-11-21 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxNMjEtVUx4LWxTQXhNZVFfUDI4TFNLQTNGX0dEM3dYdk5DSk1pZUVoZExsUFRDOG1wQ0IwbUpmcFBUa1pJdl9zbnVEdURCaTkybHh5Qmdpb1RRQmVxeVAwMklrUWFSUUtTS2JNc0tEdFN2ak9FQjdMTGt3Q1EwT1pINnZqT1ZSMUJEWk5JZGNVYXhvRXZkMG56ZlhqbGJzRkxWalV3NkRvS1dEbVpkUTB3ZGt1LVBlakx1bm15cERQLVl5b2PSAcgBQVVfeXFMUFVpTGFObnprV3h3WDhjM3VXT3RTTzBkcEZ2TFgzSmlxZzNCQlpNcE16MkVHN2dYbUd6eG1yRFVWY1NBTnRua1VHTWxsS1VoYVg3ck4yZVJkakxQSHBLUXVkbzdHbGpNejVVbDI2SkNRZzVqSmtGdDBXZ1FSM3I0T0Flb3I5R2NLdXNxd0FIUTlTbVBpVTQwckVUQTBMdnhlQ0wzakk2LXNYOTJDZ1RFbkdHWWo0YU1abmZLdDIzbXFvcVVvMmNVYjU?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **GOOGL** | **14.73** | **5.26** | **18.17** | **24.70** | **3,468,137,332,736.00 USD** | **-5.62** |
| META | 20.39 | 5.61 | 13.43 | 26.10 | 1,527,609,688,064.00 USD | 0.90 |
| MSFT | 25.70 | 7.77 | 18.12 | 18.80 | 3,657,400,844,288.00 USD | 5.18 |
| AMZN | 20.65 | 4.50 | 16.07 | 12.10 | 2,761,567,240,192.00 USD | 15.72 |

Peers fetched as_of: 2026-11-23; GOOGL reuses existing data (market data as_of: 2026-11-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-28
- Next expected earnings: 2027-02-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-23

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-29
- Revenue (latest available single quarter): 127,577,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 26,468,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000084/goog-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimwFBVV95cUxOc1RxLWU5d3g3QTUxMk1LUm5fRjhnYlJ6UnVVb2VMVmtOemZFU0RGUjBaQVpwYkUwa052R0pFUFZReE00RWRxdjB1UnlROE5VNS1CVDVuSEhLdThDeElCVmd0bGYwS01yX1g1QXlWeE1FZV9OaWNCWXlraXd2ZmQ2SlJJdkhOMlR3WjllY2I2NDl5RXFWOFgtVXl1aw?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOVWhOYkM3RENzRGRqaGJWR1o2THE0eGFBZHlpRHBiWWU4SjRUejJpZkVJZkhsenB6SmM4UDVOWUp5anJ2cWpVSkd1cktRZ0J5Y2VwNFYxd1dpYlY5NFEzQTdteWFsUlJIRDBZbmkxaUROaDlEcFVTTWpXQUdDNW9ab1VpQkVuRDhUbHQzWWFoWkVjTU82MWs5T3dlME9TUQ?oc=5
- https://news.google.com/rss/articles/CBMieEFVX3lxTE10WDdwclZjV3ltY3NHVm9ia044N0huUnBJZGgtN1FkalNkajRpS1R4XzFjYjg3ajRXS0hwWDdvbHdPQ0k5eWxhSHBuOS1Da2x5S285MFJ1QVVwN2Nob2pLQlZmYVlwQ1ljT2VOaXBPMWMzU3dkaE5Wbg?oc=5
- https://news.google.com/rss/articles/CBMidkFVX3lxTFAwWHZ2V1dxQ2l4anlaY196R19jS0NQcWFIa1B2LWJPSFgzY041MEZqZUV1b2tPcTlaVC16dkw0S2ppR09nLUxrTEpvbk8zQzlMQndZS3FsSEpaS2t4elRxcm1qVEhEYlVIYVhZUlp4RmhwZlE5b1E?oc=5
- https://news.google.com/rss/articles/CBMi7gFBVV95cUxPX2Vtd1RONnpHYk5ia01paUJUNlEtc3BMUk9wNVRoTV91dHdVRkNKZDZ2UEl6X0M0d25MLVhzdFdyWk9zTF9tWm1Xa04wQndpa0RTS28yaHgtaktYajE0MHlVTmVwY20tZEZkM2RGV3dfV2Z5NzNIVXk3ZEZqLUpnNTN1UmNPWTE0cWE0VDBKakdFaWNwRnd2bXBhSTZucWNXNVVNOVcyaDFkd0JZYVpwZmhRTVhTd2s5Q2NHWHlsaHYzdlBiYlVUZHJzQTFHalBBYWFmbmpITjdTN3F3ZmNPdDY1X0d2c2YyTENqaDVB?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPYjFPbkJ5QWFsT3Z5NzdtbDNQa1BqNmVwVGF0cmFKQjNWTmlTbERHS215SUNXNHVkajFTXzVlRm1ZdDEwa0RRVktyeUFnVmVSN3pIOXVPTk03OVBzTVlaVFZCblI1bVpzV25wQzF0S0M3SHVSZ1ppUHpJRzdGOXk1ejRRQzBXQ3FGZDF0Ry01ZUUzMjBtelNDeU5VOTM?oc=5
- https://news.google.com/rss/articles/CBMilAJBVV95cUxOWHEwZzB6MUFKZDF0OW41SjF6OGtoOWs3N3RhZ2NRVzBVVkhjV1hhVFhEeWtteTZxVjVVVVY0Zk96LUw4SlNiMEFsRnM1eXhDRi1ULTh0UXpicWYzZHlCTXlsVmhLSVp4YjByeHluMWpVYUNkbFBRN3dueGdrVzh3R0RGeGlITGFacmNDZkhzM28yNEdVMTlDRl9IY1BiTXEzLU9yeExrTXlGcVZsemVkQTlsRi1EVVNaYUdoOXdqVDJBX0lfbmJ2ZFc3aHZUcmM2MjViZXVFNFJydHJOODZzUmJnMHd4UTZoYUR2bEF4MjRGbHp1eFRDZF9jUDlPZFZrZnF5QlkzMzBkQTl3VllnbTFUVWU?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQeFJwUjdDUXhMVWJrTzJJaks0b3I5ZDlJWGdHMnVxZ1FyVndOVmhCdVFsbUZFSG9OYWtJZHlZNDhOSGJsazlQc0xPczdqM3lhczJhX2E4SEtvb0M2dThmcUpHMDBWeU9IVlByc25aclZvSHhQMXR4V24wZkhDRUU4NHE1OWNfVE00T1YyNlBzelhGdmt6?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQM3R1cDUtT05XY2ttV01jTDF1WFZlZy16UUt5aTVNdXVfdXJRMXJuU3c2SnlNckdqdHRTLWxfUkJCQzktT3hhRElBZHNWM2pQLWlRa081YThFRGcwTjVwdWdXb0ZCU3EybG9JUmhJbnJpVkVXSHFISnplRDZNUWZwUUZlOEQ1dzFOa0x4Z1FSSWtJVDFUeUN1SkphUHQ?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxQTEpBaHhwRlV4dTFyUkFsZjI0TF9oZzBLNEt6QmdhU01sMHVoQjJ4am1QSlY3RWp2Mk5oREJxZ1VTc3BJNml1eVBUdkNaa3JkMDJlN0l6N1VNTUpfSmNfX25ZM2RwYUZOY0sxV3hHRHJtLXl2N2taZkJtSS10ZHlRVXZIUHJfTWZMbl9oaS1n?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNLW1yYUxsRnJGcnFEQzJhSGJWV0JHeUNEN1prTXBhQzI1eXdSc292OEVVSjNpUDBCMk93TUU2U3B3Y19RYU9qWVJsa1NuNHpORnFHSTV1QnRvYjRtNE9tY2ZHZ3B3UnJZWVJWZUNpeEdUSm1KZ2pnYjJrQlBGTS1LTmo5Z1dmRFo0Q0FDNlY2Ui01eW9M?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNT1ZWV245S1M1R2I2RVIyNHprYlZwcGN1eGlRWE9ZNTJYd0Q3V2xyb0FFZWdNcFRhVHVPVUtKdEdrYmd4bDlNbkRkdTNFazJLUU1wS0g1WlVFd3U3YU1pbkl4R09QVmFkVEZYMTNjU1FJbnU0bGY5Mk9zNWxFcWV2Y0h1aDF1aGlnYjBmNk53LU5TaHVwdTBmRjd3?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxOZWlMZ2JfQi1mSmxiLS00Mml1VDR1Q0tuVjZSaks4dHh6bU5Ld0oxQ01QUVhtN0x6c3Q0cmtFVzBoUC1jNzB3TTRUdmU5TTJZUk01blptY09QV0o5UHpxdzRPUzVrSWNsaTkwMktGLUhNYktFNWVIb0pYc2Riemt4WnlSd01oZFMtYVpFUHlIT2lUT1FJalJVQ2lKalpfY2dtS0VrS2xnRDl0NzhqUFdjVGxUQlFEUXItd0ctM1BNTXJiaU9p?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxON3V6WEZ5MTczaE84bktQaVNVMWY0d1ZBTDZhZW92R2pQX2RzUnZZYVJ4bzVCMTA4R0Mtbk9hUWV0cnJSdkh2MktNVjAyaFJMTVB1NEFram1EcnlqOVRHdWRMa1kwUDBJWEhRZ0ZVRkxVV0FabGtVa1NCREhWMjBkZ1N2c29mYzVodFV4T2RXdUJCMGRzQmF1MzEzTQ?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxOQ0V4Y1NuZ05CT1FXd0pOZ0dIdFJnY1V4YzB0MUk3dmhkaTVNaVIyc1lFaTRVb1lid294WUxYeTZxR29uWk5QMk5SY0hCTFVSRVlQdlo5VVV6dFpGTnFiN0IzdzNFcENvRTktUHZlSjZ1enJOcmpvYjhmb3NMR0RYS09SbWVQdWJOT0Jsc0VOS19EREljTEJuc3J3MklINDQ3MnBSY05TNjRBUmR2RTNyLUczRC04MGRLRHBhTER5ZkN4YXfSAcgBQVVfeXFMT09xeUxVdGlSQzBOQlNERlVRQjJTX3pPQVJqZFA1SEtlWGllaldnN21CNnRiMzNXSHN0c2p0ZTRNaEk1Z2hVZWxISHhRNWw2ZlZ2TmN0THN5Q2ZTV1RsVVE0a1p0VTYwNjJRMjYtXzdQMmMySnR4TzE5ZG82Z2R2YjJTUl9YTk1EYTNZZFFsVTBsMk16dHEzd2hFVUxUQTlMcC1HVldrc0RubWRyOUdEN3lWRUJTc1BDeV9HaWNYZGtPUW11UnpRWW8?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxPSl8yMUJzOEtDTzBiejNkWEFmZUktVW12Wk1vQm1NZVlUb3hxSUZ1MVJPczM2MmlvZC1YOTBaVk5Xdm42bzlVMnp2WGNfSkZDYjdvdDhUV1hkMEg2NE0xd1ltOExMSjZnekRxZ3FCaXRhMmF4ZWdNSzB0REFrbzJKd2VCRTBiNlhJYmRISjNjU2Fzc2VGNUFSU1puOUtNdXVzNkE1ODAwbFRyYWRlZWRaaTlvdndmdWE0VmtLMFItVjZaUzFTVlkwRHgwUUpDWHoxVGtjdDlfR0UxUQ?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxNMk80VUp2ZGs5bVJLVG55OVJ5VnhwRXNvY1I0RGloZzBvRTlfRWVQZGpFeVdGbmIwbzlyWnJGSnQtdWY5a3JOTWVPWG4yVVlGT25BSGxFUl9Jb2VNczlTYnlpSXFuT05pN2ZiQndudm9zTVk4bEN2M3RRZVM2am56a2hQQ1BaVDJwYm40YjFNbngxck11UEd1eDVtakFjTEhqX1JBYTR1cWljeTNNMmtJUVl3RHI?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPcFptQ3RmT1VCa1htc21fY09VX3pyeU9YT0NXeU1UX3JxUFlTMFc1TG1nd3RCVlhPRUdMeTNGNUJTaDVCb2VSb3haQ2lycUFtdUllVmtUVW5rUXhBRmdNMnAzWU9vU2dTYVZZRFdiU0NBYnc3X0J4MlhYTkNIWEw2S0JIWHJKMFk0R0E3WENJWDZhU2lqS0dPX3RsUGh6RDM0?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNSnRqZEd2YXN5WktjUlRXQkVOY3dZenpNam1ZTzZEZFNLWks5NnI5X0VTUHhHUUVYT1I4eWNGeHJjem9tcXRZN1VERERpRkUtbU9TSFRob1EzeDBkY0tVNjBOcUJtM2QyNGptMS15U1NsSG9RNWo3eWIzV2ZfaG11VTFxaV9OZkwtNzlWSnRoT3ZJaEM3aFpicW5RTzBEZ3c?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQVDF4Sm92d3dlRThhcXhmdHItbXd5N2E3bVlFLXpzVnEzXzhwQzlTM2ZnMl80VnZQWGNRQnhBY2J5VGx3NHRxMDhRSEpONWtWV1MzMjZpRjJFQzhkQzMwUUFFSDMwb21oNDk1SktveTF6alBMcGEtMjVLWmJWejdQS1otSnZPMzlvRWVKRzJIRlZLZ01K?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxPZUJIRDh4bVZNcnFhTFQyR3F6a3pCQWl2M2RvWEVxX0hYSFRKbGYwVE5OUzRrTHREbDgtTVo2WFptZ0FCQTBTM183bnNFcnNxVnNBQ01KUHphYlF4WmNfM2tTLTZHTmtKU3JyVGlMNGU1enQ5VFczTDVDYVdDYk5aZmQxamNGYjZGS09URg?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxNMjEtVUx4LWxTQXhNZVFfUDI4TFNLQTNGX0dEM3dYdk5DSk1pZUVoZExsUFRDOG1wQ0IwbUpmcFBUa1pJdl9zbnVEdURCaTkybHh5Qmdpb1RRQmVxeVAwMklrUWFSUUtTS2JNc0tEdFN2ak9FQjdMTGt3Q1EwT1pINnZqT1ZSMUJEWk5JZGNVYXhvRXZkMG56ZlhqbGJzRkxWalV3NkRvS1dEbVpkUTB3ZGt1LVBlakx1bm15cERQLVl5b2PSAcgBQVVfeXFMUFVpTGFObnprV3h3WDhjM3VXT3RTTzBkcEZ2TFgzSmlxZzNCQlpNcE16MkVHN2dYbUd6eG1yRFVWY1NBTnRua1VHTWxsS1VoYVg3ck4yZVJkakxQSHBLUXVkbzdHbGpNejVVbDI2SkNRZzVqSmtGdDBXZ1FSM3I0T0Flb3I5R2NLdXNxd0FIUTlTbVBpVTQwckVUQTBMdnhlQ0wzakk2LXNYOTJDZ1RFbkdHWWo0YU1abmZLdDIzbXFvcVVvMmNVYjU?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
