# META Intelligence Report

- ticker: **META**
- Report as_of: **2026-11-19**
- Market data as_of: **2026-11-18**
- Quant sources: https://finance.yahoo.com/quote/META/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/META/key-statistics/
- AI analysis snapshot as_of: **2026-11-19**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-20T05:43:38.894234+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 3, 'ai': 20, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261118T054934Z-e0d070d9/META** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 2}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 14 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-11-14

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 616.3800 |
| Return 1D (%) | -0.4023 |
| Return 1W (%) | -1.9705 |
| Return 1M (%) | -13.1039 |
| Return YTD (%) | -6.3814 |
| Return 1Y (%) | 3.4768 |
| Annualized volatility (%) | 41.7188 |
| Beta vs SPY | 1.3706 |
| Max drawdown (%) | -28.7332 |
| Sharpe (rf=0) | 0.2885 |
| Downside deviation (rf=0, %) | 27.5244 |
| Sortino (rf=0) | 0.4373 |
| Historical VaR 95% (1D, %) | 3.7761 |
| Historical ES 95% (1D, %) | 5.6434 |
| Correlation vs SPY | 0.4520 |
| Tracking error vs SPY (%) | 37.5624 |
| P/E (trailing) | 20.34 |
| P/B | 5.59 |
| EV/EBITDA | 13.40 |
| Revenue growth (%) | 26.10 |
| Forward P/E (estimate) | 16.71 |
| Gross margin (%) | 81.03 |
| Operating margin (%) | 37.78 |
| Return on equity (%) | 32.26 |
| Free cash flow yield (%) | 1.11 |
| MA50 | 679.2873 |
| Close vs MA50 (%) | -9.2608 |
| MA200 | 628.7861 |
| Close vs MA200 (%) | -1.9730 |
| RSI (14, Wilder) | 41.4330 |
| MACD (12,26) | -14.6344 |
| MACD signal (9) | -16.1374 |
| MACD histogram | 1.5030 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'META': 285, 'SPY': 286}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 616.3800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.4023 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.9705 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -13.1039 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -6.3814 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 3.4768 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 41.7188 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 27.5244 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4373 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.7761 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.6434 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4520 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.5624 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.3706 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.7332 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2885 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.7125 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 81.0340 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 37.7770 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 32.2640 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.1055 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 20.3419 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 41.4330 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.5030 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -9.2608 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -1.9730 -> Slightly below the moving-average trend level.

## TAILWINDS

### Meta Platforms (META) Surges as AI Ranking Models Accelerate U.S. Ad Revenue Growth to 31%
- Summary: Meta Platforms (META) Surges as AI Ranking Models Accelerate U.S. Ad Revenue Growth to 31%
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOajhtMTV2NGZ2MExsOHhtT0U3VUtUNG1jZGg5SW1TTWZCOW9OVWpiTmRaeUZHdy1CT1p6R29ieFBNNVZkZ3UxVWFWa0lMUDZjNE1xQ3I1aHFDVi10aVdMNDJXZ1JEWTdHNEVWLW9SOFFzbEJBSjUwZkNFRWtURUhqVEtralp1ZFJSNjl4M3ZPeHk2WTE1VWJhM3RR?oc=5>

### Will ETF Buying Change Meta Stock Narrative
- Summary: ETF buying could shift Meta’s stock narrative, potentially boosting investor interest.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNUnhObF9vcWxydnRua1J4T2hsVjhTOExiYjFWYUJhTmxGazE1ZS1zTzVBN3JuUTkwaHVKM3h0bm95ZXU4NlBLQkFmbkk1cnlYVTBlc1F4Rk9VaVV4cnhtd1Y1QnVETzNjbkZvM3FObVc5Y182VjVjc1B4SXBIbjAwSUp3WUZlVXpqOHpFbkkxT2pqbGhKQWxEMw?oc=5>

### Meta Platforms, Inc. (META): Strong Advertising Growth Supports Its Long-Term Investment Case
- Summary: Positive analyst view on Meta’s advertising growth and long-term value.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQTWVldU50RklZVlZIS3ZFanQxVWZ2Wmt2TXVlVTU3OVpoTWN6aThIYmFCYXJYd3l0NDNQVWU4enZlWWcySXYtWjBadFdZSEx1MF9TQjFfcU1nOW5UeHBiaDNGbWhNZExZOFA0MlRxN1BrazVuLXktVTA0b3NFNXl3TF8tekROcmdtZTQwMGlQdjRwMWxyamc?oc=5>

### How to Play META Stock as Meta Platforms Tests a New Prediction Markets App
- Summary: Meta launches a prediction markets app, potentially expanding its product offerings.
- Date: 2026-11-18 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxQY1pIcENNWE1fdjdWTzhuUzdkTUVra21hbzZLbjNFa1ptTm4wSXQ0UTNpUno2bzdueHg4WllFY1BiS09lTEVkMHVJVFl5Q0I4MllsUFJfWFlkM3d5N1BRdUZGRWo1VDdHT2E4RXBIc3dDSThOVDZqQmJyS2I1RUs4ckF5SGc2TUthQVoyUnY0TGV0MUt5eWNaUlVza0NTbDZuMlJCdEg1MUZPVWJRZWg2T25aekNacWNIWS1Z?oc=5>

### Meta’s Advertising Business Could Drive Another Major Earnings Surprise
- Summary: Meta’s ad revenue may boost earnings beyond expectations.
- Date: 2026-11-19 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxNMlV5UW5BeEE5QTNqYnhUNTFteHg3UFl4Z2YwZGY0Y0s3QndOWUpWQ090M2huSk1OY0hLQWVhTnlKRWFnVFkwN3FCRU9kS1lmbVFycVgxVmFSUllRSFdSU0N6ajBaSWcybDB6UWtyUU5DN096Z2VfOXE4VkRQdHJtS3ZoU09Ra0VpVHF2VV85aDk1MHpualVva3RKcGpfb1VUTEZzQktSdlB0ZUxCQ1R5V1Y4Wng?oc=5>

### Meta: Buy The AI Payoff Before The Capex Fear Fades
- Summary: Investors encouraged to capitalize on AI gains before capex concerns ease.
- Date: 2026-11-19 | Impact: medium | Horizon: medium | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPRzR4YjRJeDVrMnZtYWplUWVJNjhkTXpQWkhQeS1YcVFqUVQ1NHo0a3pLU2NId3V3LUR4MmpnZUFjbE8ydmlQVlRxSXBBZG1pYmROaXBic0N1UkhkSEI2YVBSVUJYbUowQ0hDYklhN2tNTUJSR1VLenNqNHhXNHF6djJuazAxYzU4VV9CR0Qtd0ZwLTMzM1E?oc=5>

### Navigating Meta Platforms’ (META) Journey from July Dip to New 52-Week High
- Summary: Meta’s stock climbs to a new 52‑week high after a July dip.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOU0JKZmRKWEdaRGhjdElFQ3dKUVhqVW1NT0JwMGFLYkdTaVI4SUx3cWU4VFd2M1huQnlmNmxfWUczYTFIT3M2WU81cG03aUt3SVVIRU5FV0dnaTBPQTdDMmNRM2M3UGlQem13MUVIbUVwQkdxUjBGUFFkbFZ3UGZkOWdtZWlsdzdyYkZlVEhvXzN3ZW53RWlFbFdYZFBBcU1ESE1GNTRR?oc=5>

## HEADWINDS

### Meta shares drop about 2.5% after pausing non-voting Class C stock dividend due to Delaware lawsuit
- Summary: Meta shares drop about 2.5% after pausing non-voting Class C stock dividend due to Delaware lawsuit
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxOczNZUTFMeUdjSHo5SFVJemx0OEVISzZpWHRkUnhDWnVxS0M2QmROb1FOYVh0a2hxR1M1eDNLaDV2cllXd1RNWWJXZEZfa2p2d2E1ZGFzeGhDUzdBcWdnNGRLMDJGbHVuZFlNeEk0NFlWY0J3amw0Ynh0VkRuM1MwWUJjNlVlUWpwR3ZV?oc=5>

### Should You Be Worried About Meta Stock?
- Summary: Negative sentiment questioning Meta’s stability.
- Date: 2026-11-16 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQSEEtMlFKdlpSZkhPeUpYMThkT2ZmZHVZYjhpOEc2QXJSbUN1dm9lRnhvUEpqb0psX2hGTUtQR0Fla0g5U051ZTBQS1VUS0wzdjNlNldhOXFPTmV6YjZoVXVMYlpJQUVpWDliZnh3WUxoeUVjYlBZdHU1eExFT3l3V0xna2NTbGQwT2t1Y2RlUzJLOWdQVGFyd0hreWt3M3VT?oc=5>

### ANT, META Stock Slip After-Hours Amid Reports That Apple Is Working On Its Own AI Agent
- Summary: Meta shares fall after hours following reports of Apple's AI agent development.
- Date: 2026-11-19 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi4AFBVV95cUxQeTJ6NFlTUEVrSzlSZ2Q1UVNDakdTR2NkM3JuSHVVbkFfX3BWNnUyTE9pY1MwbTRDdmpndEoxOHRTeVR1TWdZb05PelJPd1FVVzZzMTdLbVNBeldwb2o0UGZTS0t2dUF0UUswZ3ozTWptalJwM3pRQXlDSXJQNjFnRG1IV1BJSWVHZjRBX2x2MUdHVzN1anNaXzhuWVVGbkVUQ3BpN2lya2x5V2diTHNHekNrTV9Ic0xMVUozS1ZhblgxWjkxdHBqYkFON3I5YWdKZXNjS2JHRk1aMW1ta2xuRA?oc=5>

### Meta Platforms Inc Stock (META) Closed Down by 3.27% on Nov 19: Drivers Behind the Movement
- Summary: Meta shares dropped 3.27% on Nov 19, driven by market factors.
- Date: 2026-11-19 | Impact: high | Horizon: short | Confidence: 0.92
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxQWC12R044UTVfYlFPZ3EwTFVRd1daV1dWazZER1dXdklDVTlIaEUwYmhrTENoeGtaWHNxNXhyNEVFN2R2SG14SlhNNDRzZXlBaldiZ09TNnc4Ymx4eWtIdVV1MnQzQ29neWJJT0ZUd0dWeE9rRTNoeWVITnFieVNrMXBQWkVwcWh6aDRJ?oc=5>

### Meta Pauses Zuckerberg Share Plan During Investor Legal Fight
- Summary: Meta suspends Zuckerberg’s share plan amid investor legal dispute.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNNVVZam9QRXJjREgtaGhPdlJxdmxiSW9yS0Jqa0d2Uk1UekxmYU01akxSYVBzdjV5TmJoNnFqSmpWdkF2cklrRG15UWFZc1NTOW1kRFVRbTd2cTR2M0x5RDkzY3ctc1J3MnFPZTJSOTRNWldFSDF6YlVrVW9rRUU0TWhzUXBRZDN4NEozSWJmOGkxdzkzQjRHTmNURmdNMGs?oc=5>

### Meta Agrees to Hold Off on Issuing New Stock Until Court Decision
- Summary: Meta delays new stock issuance pending court outcome.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxNX3V0a1JQSHotVWRkNFpvbWZmeHJKd29JZE5ibWtwZlNxRk5mY3AxYlV3OFZFeUZJb3J4aVpkQ1JYbl9WZV9lOWdpREhHcFVrQnplSl9YdC14SmhtT2FyOXpUbEIxV2VuWkNWMUJCZ3J3UGRrMThDMVNHMmRGR3FsOHRPN1RjSDFsdkYzMlUyTWZadzVyTDh3OUdBbEd1UGtTalNCeHNmLS00RE85NloyMEtNZU1wX2RQZkE?oc=5>

## CATALYSTS

### Meta AI Momentum Offsetting Spending Concerns, Says UBS — Analyst Sees 30% Potential Upside
- Summary: Meta AI Momentum Offsetting Spending Concerns, Says UBS — Analyst Sees 30% Potential Upside
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4gFBVV95cUxNU1NVb3ZzTC1qdVNoWUFfbXRCSG1sVG8tU0RpbXlsQmRhYjlPTWxHUldSZlRXNmdrZHY2NmE2YUZMTy02ZDNsRzNUbTFPOTBxdWJsQjU4WDltQzRtYmtRbFZValpGUGQ0V2h3MUVTN2JNcmdBY21XaV9PQi1KT2lXdi1TQ3pNZEptdHRrUEpaaFFPb0hIUnNWajdTaXBCV3JtSEFjLUE4eDBPRWJOZDFGbkVKTEdBMS1BT19nbnNWeFlxeC1MNzRzTmxDV2pSd3RwTXpzcVlyVlk3ZDk4ZWdNMG5B?oc=5>

### Is Trending Stock Meta Platforms, Inc. (META) a Buy Now?
- Summary: Analyst recommends buying Meta stock.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPSTBYOEhPRmxzaDFtY3Q0TDZwWWtnTHZNbF9JeWhabWt0NVllMHQ5ZTJQVDZYTkpzTHZ6Yi1iVkNiaGpmV0dlQXVIZlgxc2V4RnRUcHFRZDB2TldsTk5Lb1FONEZVRFN3ZmZaNERLall3LXM1VzVMd29BLXlCWXpvdTBHOGdoc0JWNm1Nb3E3SDdsTGlCUjNlVHhXc1AzWFk?oc=5>

### Meta Stock Has Fallen 3% YTD. Its Cheapest AI Model Could Change Everything.
- Summary: Meta shares down 3% YTD amid AI model speculation.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxOeHFlaXBvVWhiTmtvbkJleXlOQnVNNWladTcwdWtFbDF0MFJ3OENoZWxsRHpsZVNabVVyZzZOdHJDZUR4QmZCOVdicG5lOVdGcEVxR1FvRzRuMTZJMGZGdGpFMHRwWWpSVmVWa2o2Y0xmRjlwSGZtQWVWVmhYQW5lcVJwZ2ZCYVJ6aC1nNHVCbXQ?oc=5>

### UBS assumes coverage on Meta stock with buy rating on AI momentum
- Summary: UBS upgrades Meta to buy, citing AI momentum.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxPYWh1UVdtSVlJRXVPckZzbjRqQU1kNnBiNzRxZ0NWVThQclFRV2VZM3I3VFBtcG1sN3VwdTdoOVBZZHV1YXlZUEZ3aEQ5WTlOdkpkTDJ0cVlCY0hmSlhXR3BGNFBEdFFabVBteHNUbXRWTF9Ha1NRUmZyRy1fZ1RFb2t4QWhEYVN6djZzQ3JZckNIeTh1SldRbnFJNzRjLUFvTlpPYnBUR0NaWjMtVEZxcFdzT0ViNjJ6ZFhvMVZQWlhsZkU?oc=5>

### Daniel Loeb's Meta Stock Bet Stands Out as Tiger Global Trims
- Summary: Daniel Loeb maintains a strong Meta stake while Tiger Global reduces holdings.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.88
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNeXFXazFEX3JKcGdMbTNRX3BlYlJWaWhkQk43dzlvLUEtR0N3RDZmYVNDM0JTQjlCd1ZCWDhuODlsaEMxUW9CWjV2bzY0WjRGVTkzRVpab2QxM19HMGtJQkl2Y2tQNlJpQU1mb082MDlsbm1LR1BNdnB6SXUzbnJLcXVNcEhBOXUtM0t6aTU5REdtRzFscGlr?oc=5>

### Meta Platforms is Cheap at 18.78X P/E: Buy, Sell or Hold the Stock?
- Summary: Analyst notes Meta’s low P/E ratio, suggesting potential upside or downside depending on strategy.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPbnEycDVUY09YNUpselQtRk0zcm45R0t3UGJveUhxdWxPV1F3OHMtY05lc2g4RU1lSnNTSV9NTG9kSjd3d3BKU0tRVEtWZXF0T3doWmxPbkR3Rjk0QWtYM3BGakY2NGFXVFRfT3V3TDh6Z0sza1lsYlZVV09KYW1SdDUwMFVCUVdkTXhIVEYzUlZHanZWWFVDa0llOW1PMERnblo4T1N3?oc=5>

### The Zacks Analyst Blog Highlights Meta, Amazon's, Microsoft's and Alphabet's
- Summary: Zacks blog highlights Meta among top tech stocks, indicating analyst interest.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxPaTd1ZHc3dU12QUgxQWsweWhoWTFZTG9TVkoxVEtadjVuX3lZUUVHSXZrQkFnUzIxZnQxdUJaQnc1WmtNZm1KTmlfbXNuTkRreWdUa08zdjM1OTAtMkJTRVpMYzZyQjIwSUd0ZkVtdksxalpPeWZmRmFPaXdoSkpsUEdsdVh1VFZmUDk5RnczMzNZTGxkemF6Yi1ZZ09VRFVKMnRqdG9vb2Jaam1lYzJlOXF3bWhBeGVBcjdNQXFDMEM0ckltcUtoWTBGYkRMNkstVVpxT0dqbEVmRkcycXpqUk9qU0xFVm9YS0c3Rg?oc=5>

### META Plans To Reportedly Charge $300 For Muse Charm Gadget In Hope To Revive Hardware Business
- Summary: Meta may launch a $300 hardware gadget to boost its hardware division.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi6gFBVV95cUxQemNNSVJ4ZGhKRmZsc0ZJT3htUkFnY0xiaFNPOXNoMVJvbk5iMTE3ZzhUdERuRGZ0WGg4MzZqM3FJTzROMmZzODR5TnFJY0dmOXlPVjRHTC1TY0pNZ24yaEtCSTdPellxaWwtb0lFLTZsclJONzBlNzZiZlNISnVHanZLbzN4LWxudGYxV3YzbjV5cTlyeXFIeWhZb2k1a3hDYWp0VnhDcXRkekxnVEEwUmU3QlBQbGp5bkx0ZkR5X0RVWHRjLW1rS3NONDIxaTR6VlZpVXF6OVpMY29nZV9BSktVT1JrZE4wR0E?oc=5>

### Meta Platforms (META) Pauses Class C Share Issuance After Delaware Legal Challenge
- Summary: Meta halts Class C share issuance following a Delaware legal challenge.
- Date: 2026-11-19 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxQVmpkVzlGMXdJOThqR2NfQU9FNTZ6QXRJVEV1TUZFQ1NmS24zTnVwYUNsYTI5empTanhOU0JfeWxtanBPS3lwd0dNV3NDbTQzNWZOZmVWN0dSenZCQ2tOSUtGbEZWd3dzblJjMWt0dEdtdERyNkVpeVF6WWQydlFQSEluandORnphOFVYUTdLd3lRcGRBNW1pVkd0WlZBNVNNMTNUNjZrUWlkVlRiaElGTmNDUjFpNDdVRjNneEVJSmZaSU5RNnJNdk1R0gHPAUFVX3lxTE43bldfcHN6UjQ0eDV0QjB6Nko2THR2SHB4dzZueEJoVnduUzMwZ2cyUzZFSG5xX2pGZGlwdXZyNzNBaGZNN1hlY0w3ZWVyYk1rSXgwTVM1Z3FDOUJ1Mi0zZlNfNUFVdm1XMUlxNVNLaEgtMjlPRU9fXzZad2o2Q25OdW9FZlVMeFpzWkZES2l2a05KSzcyQS1yVjBQOHpJLW5XdXRiOVYxaWllX2p1YW1ZZy1oMHREcG0wNC1xRGZ5OVJzc1RCQzgxOG9xWkNfcw?oc=5>

## RISKS

### Is Meta Stock Still a Buy After Borrowing About $25 Billion This Month?
- Summary: Meta's recent $25B borrowing raises questions about its stock attractiveness.
- Date: 2026-11-15 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxOX3VnN3lfRkVjaVdFejdqMU5FRTdWalgzeDlRa2FxVVJmVjgwTElnS3lZMVVMWl9vY29KSEpyX3FMQ0l6MXFwLUZRYm5WaGUwSk9kbzlKWEVMU3JwSjA1UDZzai1obVI2YkVMb0hDc2x2T3hvd1pLRFpOX3A5R3cwWE5IcG1ybmo2TmlZUktfRXU2aW5CM1hyRmstWkpTRU12bUd4bzRJRC1EeVZaWWhHTy1MMFZSdw?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **META** | **20.34** | **5.59** | **13.40** | **26.10** | **1,524,082,016,256.00 USD** | **3.48** |
| GOOGL | 14.24 | 5.08 | 17.55 | 24.70 | 3,352,081,989,632.00 USD | -6.64 |
| SNAP | N/A | 3.94 | 53.84 | 14.30 | 8,840,073,216.00 USD | -34.06 |
| PINS | 73.43 | 3.12 | 31.79 | 11.90 | 9,686,547,456.00 USD | -31.35 |

Peers fetched as_of: 2026-11-19; META reuses existing data (market data as_of: 2026-11-18); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-19

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

- https://news.google.com/rss/articles/CBMimgFBVV95cUxOajhtMTV2NGZ2MExsOHhtT0U3VUtUNG1jZGg5SW1TTWZCOW9OVWpiTmRaeUZHdy1CT1p6R29ieFBNNVZkZ3UxVWFWa0lMUDZjNE1xQ3I1aHFDVi10aVdMNDJXZ1JEWTdHNEVWLW9SOFFzbEJBSjUwZkNFRWtURUhqVEtralp1ZFJSNjl4M3ZPeHk2WTE1VWJhM3RR?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNUnhObF9vcWxydnRua1J4T2hsVjhTOExiYjFWYUJhTmxGazE1ZS1zTzVBN3JuUTkwaHVKM3h0bm95ZXU4NlBLQkFmbkk1cnlYVTBlc1F4Rk9VaVV4cnhtd1Y1QnVETzNjbkZvM3FObVc5Y182VjVjc1B4SXBIbjAwSUp3WUZlVXpqOHpFbkkxT2pqbGhKQWxEMw?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQTWVldU50RklZVlZIS3ZFanQxVWZ2Wmt2TXVlVTU3OVpoTWN6aThIYmFCYXJYd3l0NDNQVWU4enZlWWcySXYtWjBadFdZSEx1MF9TQjFfcU1nOW5UeHBiaDNGbWhNZExZOFA0MlRxN1BrazVuLXktVTA0b3NFNXl3TF8tekROcmdtZTQwMGlQdjRwMWxyamc?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxQY1pIcENNWE1fdjdWTzhuUzdkTUVra21hbzZLbjNFa1ptTm4wSXQ0UTNpUno2bzdueHg4WllFY1BiS09lTEVkMHVJVFl5Q0I4MllsUFJfWFlkM3d5N1BRdUZGRWo1VDdHT2E4RXBIc3dDSThOVDZqQmJyS2I1RUs4ckF5SGc2TUthQVoyUnY0TGV0MUt5eWNaUlVza0NTbDZuMlJCdEg1MUZPVWJRZWg2T25aekNacWNIWS1Z?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxNMlV5UW5BeEE5QTNqYnhUNTFteHg3UFl4Z2YwZGY0Y0s3QndOWUpWQ090M2huSk1OY0hLQWVhTnlKRWFnVFkwN3FCRU9kS1lmbVFycVgxVmFSUllRSFdSU0N6ajBaSWcybDB6UWtyUU5DN096Z2VfOXE4VkRQdHJtS3ZoU09Ra0VpVHF2VV85aDk1MHpualVva3RKcGpfb1VUTEZzQktSdlB0ZUxCQ1R5V1Y4Wng?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPRzR4YjRJeDVrMnZtYWplUWVJNjhkTXpQWkhQeS1YcVFqUVQ1NHo0a3pLU2NId3V3LUR4MmpnZUFjbE8ydmlQVlRxSXBBZG1pYmROaXBic0N1UkhkSEI2YVBSVUJYbUowQ0hDYklhN2tNTUJSR1VLenNqNHhXNHF6djJuazAxYzU4VV9CR0Qtd0ZwLTMzM1E?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOU0JKZmRKWEdaRGhjdElFQ3dKUVhqVW1NT0JwMGFLYkdTaVI4SUx3cWU4VFd2M1huQnlmNmxfWUczYTFIT3M2WU81cG03aUt3SVVIRU5FV0dnaTBPQTdDMmNRM2M3UGlQem13MUVIbUVwQkdxUjBGUFFkbFZ3UGZkOWdtZWlsdzdyYkZlVEhvXzN3ZW53RWlFbFdYZFBBcU1ESE1GNTRR?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxOczNZUTFMeUdjSHo5SFVJemx0OEVISzZpWHRkUnhDWnVxS0M2QmROb1FOYVh0a2hxR1M1eDNLaDV2cllXd1RNWWJXZEZfa2p2d2E1ZGFzeGhDUzdBcWdnNGRLMDJGbHVuZFlNeEk0NFlWY0J3amw0Ynh0VkRuM1MwWUJjNlVlUWpwR3ZV?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQSEEtMlFKdlpSZkhPeUpYMThkT2ZmZHVZYjhpOEc2QXJSbUN1dm9lRnhvUEpqb0psX2hGTUtQR0Fla0g5U051ZTBQS1VUS0wzdjNlNldhOXFPTmV6YjZoVXVMYlpJQUVpWDliZnh3WUxoeUVjYlBZdHU1eExFT3l3V0xna2NTbGQwT2t1Y2RlUzJLOWdQVGFyd0hreWt3M3VT?oc=5
- https://news.google.com/rss/articles/CBMi4AFBVV95cUxQeTJ6NFlTUEVrSzlSZ2Q1UVNDakdTR2NkM3JuSHVVbkFfX3BWNnUyTE9pY1MwbTRDdmpndEoxOHRTeVR1TWdZb05PelJPd1FVVzZzMTdLbVNBeldwb2o0UGZTS0t2dUF0UUswZ3ozTWptalJwM3pRQXlDSXJQNjFnRG1IV1BJSWVHZjRBX2x2MUdHVzN1anNaXzhuWVVGbkVUQ3BpN2lya2x5V2diTHNHekNrTV9Ic0xMVUozS1ZhblgxWjkxdHBqYkFON3I5YWdKZXNjS2JHRk1aMW1ta2xuRA?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxQWC12R044UTVfYlFPZ3EwTFVRd1daV1dWazZER1dXdklDVTlIaEUwYmhrTENoeGtaWHNxNXhyNEVFN2R2SG14SlhNNDRzZXlBaldiZ09TNnc4Ymx4eWtIdVV1MnQzQ29neWJJT0ZUd0dWeE9rRTNoeWVITnFieVNrMXBQWkVwcWh6aDRJ?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNNVVZam9QRXJjREgtaGhPdlJxdmxiSW9yS0Jqa0d2Uk1UekxmYU01akxSYVBzdjV5TmJoNnFqSmpWdkF2cklrRG15UWFZc1NTOW1kRFVRbTd2cTR2M0x5RDkzY3ctc1J3MnFPZTJSOTRNWldFSDF6YlVrVW9rRUU0TWhzUXBRZDN4NEozSWJmOGkxdzkzQjRHTmNURmdNMGs?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxNX3V0a1JQSHotVWRkNFpvbWZmeHJKd29JZE5ibWtwZlNxRk5mY3AxYlV3OFZFeUZJb3J4aVpkQ1JYbl9WZV9lOWdpREhHcFVrQnplSl9YdC14SmhtT2FyOXpUbEIxV2VuWkNWMUJCZ3J3UGRrMThDMVNHMmRGR3FsOHRPN1RjSDFsdkYzMlUyTWZadzVyTDh3OUdBbEd1UGtTalNCeHNmLS00RE85NloyMEtNZU1wX2RQZkE?oc=5
- https://news.google.com/rss/articles/CBMi4gFBVV95cUxNU1NVb3ZzTC1qdVNoWUFfbXRCSG1sVG8tU0RpbXlsQmRhYjlPTWxHUldSZlRXNmdrZHY2NmE2YUZMTy02ZDNsRzNUbTFPOTBxdWJsQjU4WDltQzRtYmtRbFZValpGUGQ0V2h3MUVTN2JNcmdBY21XaV9PQi1KT2lXdi1TQ3pNZEptdHRrUEpaaFFPb0hIUnNWajdTaXBCV3JtSEFjLUE4eDBPRWJOZDFGbkVKTEdBMS1BT19nbnNWeFlxeC1MNzRzTmxDV2pSd3RwTXpzcVlyVlk3ZDk4ZWdNMG5B?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPSTBYOEhPRmxzaDFtY3Q0TDZwWWtnTHZNbF9JeWhabWt0NVllMHQ5ZTJQVDZYTkpzTHZ6Yi1iVkNiaGpmV0dlQXVIZlgxc2V4RnRUcHFRZDB2TldsTk5Lb1FONEZVRFN3ZmZaNERLall3LXM1VzVMd29BLXlCWXpvdTBHOGdoc0JWNm1Nb3E3SDdsTGlCUjNlVHhXc1AzWFk?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxOeHFlaXBvVWhiTmtvbkJleXlOQnVNNWladTcwdWtFbDF0MFJ3OENoZWxsRHpsZVNabVVyZzZOdHJDZUR4QmZCOVdicG5lOVdGcEVxR1FvRzRuMTZJMGZGdGpFMHRwWWpSVmVWa2o2Y0xmRjlwSGZtQWVWVmhYQW5lcVJwZ2ZCYVJ6aC1nNHVCbXQ?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxPYWh1UVdtSVlJRXVPckZzbjRqQU1kNnBiNzRxZ0NWVThQclFRV2VZM3I3VFBtcG1sN3VwdTdoOVBZZHV1YXlZUEZ3aEQ5WTlOdkpkTDJ0cVlCY0hmSlhXR3BGNFBEdFFabVBteHNUbXRWTF9Ha1NRUmZyRy1fZ1RFb2t4QWhEYVN6djZzQ3JZckNIeTh1SldRbnFJNzRjLUFvTlpPYnBUR0NaWjMtVEZxcFdzT0ViNjJ6ZFhvMVZQWlhsZkU?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNeXFXazFEX3JKcGdMbTNRX3BlYlJWaWhkQk43dzlvLUEtR0N3RDZmYVNDM0JTQjlCd1ZCWDhuODlsaEMxUW9CWjV2bzY0WjRGVTkzRVpab2QxM19HMGtJQkl2Y2tQNlJpQU1mb082MDlsbm1LR1BNdnB6SXUzbnJLcXVNcEhBOXUtM0t6aTU5REdtRzFscGlr?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPbnEycDVUY09YNUpselQtRk0zcm45R0t3UGJveUhxdWxPV1F3OHMtY05lc2g4RU1lSnNTSV9NTG9kSjd3d3BKU0tRVEtWZXF0T3doWmxPbkR3Rjk0QWtYM3BGakY2NGFXVFRfT3V3TDh6Z0sza1lsYlZVV09KYW1SdDUwMFVCUVdkTXhIVEYzUlZHanZWWFVDa0llOW1PMERnblo4T1N3?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxPaTd1ZHc3dU12QUgxQWsweWhoWTFZTG9TVkoxVEtadjVuX3lZUUVHSXZrQkFnUzIxZnQxdUJaQnc1WmtNZm1KTmlfbXNuTkRreWdUa08zdjM1OTAtMkJTRVpMYzZyQjIwSUd0ZkVtdksxalpPeWZmRmFPaXdoSkpsUEdsdVh1VFZmUDk5RnczMzNZTGxkemF6Yi1ZZ09VRFVKMnRqdG9vb2Jaam1lYzJlOXF3bWhBeGVBcjdNQXFDMEM0ckltcUtoWTBGYkRMNkstVVpxT0dqbEVmRkcycXpqUk9qU0xFVm9YS0c3Rg?oc=5
- https://news.google.com/rss/articles/CBMi6gFBVV95cUxQemNNSVJ4ZGhKRmZsc0ZJT3htUkFnY0xiaFNPOXNoMVJvbk5iMTE3ZzhUdERuRGZ0WGg4MzZqM3FJTzROMmZzODR5TnFJY0dmOXlPVjRHTC1TY0pNZ24yaEtCSTdPellxaWwtb0lFLTZsclJONzBlNzZiZlNISnVHanZLbzN4LWxudGYxV3YzbjV5cTlyeXFIeWhZb2k1a3hDYWp0VnhDcXRkekxnVEEwUmU3QlBQbGp5bkx0ZkR5X0RVWHRjLW1rS3NONDIxaTR6VlZpVXF6OVpMY29nZV9BSktVT1JrZE4wR0E?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxQVmpkVzlGMXdJOThqR2NfQU9FNTZ6QXRJVEV1TUZFQ1NmS24zTnVwYUNsYTI5empTanhOU0JfeWxtanBPS3lwd0dNV3NDbTQzNWZOZmVWN0dSenZCQ2tOSUtGbEZWd3dzblJjMWt0dEdtdERyNkVpeVF6WWQydlFQSEluandORnphOFVYUTdLd3lRcGRBNW1pVkd0WlZBNVNNMTNUNjZrUWlkVlRiaElGTmNDUjFpNDdVRjNneEVJSmZaSU5RNnJNdk1R0gHPAUFVX3lxTE43bldfcHN6UjQ0eDV0QjB6Nko2THR2SHB4dzZueEJoVnduUzMwZ2cyUzZFSG5xX2pGZGlwdXZyNzNBaGZNN1hlY0w3ZWVyYk1rSXgwTVM1Z3FDOUJ1Mi0zZlNfNUFVdm1XMUlxNVNLaEgtMjlPRU9fXzZad2o2Q25OdW9FZlVMeFpzWkZES2l2a05KSzcyQS1yVjBQOHpJLW5XdXRiOVYxaWllX2p1YW1ZZy1oMHREcG0wNC1xRGZ5OVJzc1RCQzgxOG9xWkNfcw?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxOX3VnN3lfRkVjaVdFejdqMU5FRTdWalgzeDlRa2FxVVJmVjgwTElnS3lZMVVMWl9vY29KSEpyX3FMQ0l6MXFwLUZRYm5WaGUwSk9kbzlKWEVMU3JwSjA1UDZzai1obVI2YkVMb0hDc2x2T3hvd1pLRFpOX3A5R3cwWE5IcG1ybmo2TmlZUktfRXU2aW5CM1hyRmstWkpTRU12bUd4bzRJRC1EeVZaWWhHTy1MMFZSdw?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQOTdPWXF1LXZSeEZuUEp6VXo2dWF2VDBCN1E4aEZ4dXg1OURyTFZuSXM2MFFwa1I4MHoxbkRtQkRQTTU1TDQwQW5FYjl4RnpSOHVXZERfV2QyWllTVm45SEY4Sk9iN3JXUFBCOW9penZlNEdYRXVwc0pnVDhUYmhlVWd2WjdEY2UxN0FFRi1jUFJJYzlVcHl4QXJYdw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
