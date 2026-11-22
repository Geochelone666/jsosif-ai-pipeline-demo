# META Intelligence Report

- ticker: **META**
- Report as_of: **2026-11-21**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/META/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/META/key-statistics/
- AI analysis snapshot as_of: **2026-11-21**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-22T05:11:28.283209+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 3, 'ai': 17, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **15** exact headline/source/date matches; prior report **20261121T053104Z-422ce34b/META** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 2}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 12 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 52.0%; oldest publication 2026-11-14

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 560.8400 |
| Return 1D (%) | -5.9340 |
| Return 1W (%) | -12.5995 |
| Return 1M (%) | -19.2164 |
| Return YTD (%) | -14.8171 |
| Return 1Y (%) | -4.4823 |
| Annualized volatility (%) | 42.2571 |
| Beta vs SPY | 1.4106 |
| Max drawdown (%) | -28.7332 |
| Sharpe (rf=0) | 0.1002 |
| Downside deviation (rf=0, %) | 28.3217 |
| Sortino (rf=0) | 0.1495 |
| Historical VaR 95% (1D, %) | 3.8949 |
| Historical ES 95% (1D, %) | 5.8049 |
| Correlation vs SPY | 0.4772 |
| Tracking error vs SPY (%) | 37.5965 |
| P/E (trailing) | 19.13 |
| P/B | 5.26 |
| EV/EBITDA | 12.62 |
| Revenue growth (%) | 26.10 |
| Forward P/E (estimate) | 15.72 |
| Gross margin (%) | 81.03 |
| Operating margin (%) | 37.78 |
| Return on equity (%) | 32.26 |
| Free cash flow yield (%) | 1.18 |
| MA50 | 676.6007 |
| Close vs MA50 (%) | -17.1092 |
| MA200 | 627.8925 |
| Close vs MA200 (%) | -10.6790 |
| RSI (14, Wilder) | 30.2693 |
| MACD (12,26) | -19.8666 |
| MACD signal (9) | -16.8754 |
| MACD histogram | -2.9912 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'META': 287, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 560.8400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -5.9340 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -12.5995 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -19.2164 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -14.8171 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -4.4823 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 42.2571 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 28.3217 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.1495 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.8949 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.8049 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4772 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.5965 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.4106 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.7332 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1002 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.7207 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 81.0340 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 37.7770 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 32.2640 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.1752 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 19.1348 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 30.2693 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -2.9912 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -17.1092 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -10.6790 -> Clearly below the moving-average trend level.

## TAILWINDS

### Meta Platforms (META) Surges as AI Ranking Models Accelerate U.S. Ad Revenue Growth to 31%
- Summary: Meta Platforms (META) Surges as AI Ranking Models Accelerate U.S. Ad Revenue Growth to 31%
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOajhtMTV2NGZ2MExsOHhtT0U3VUtUNG1jZGg5SW1TTWZCOW9OVWpiTmRaeUZHdy1CT1p6R29ieFBNNVZkZ3UxVWFWa0lMUDZjNE1xQ3I1aHFDVi10aVdMNDJXZ1JEWTdHNEVWLW9SOFFzbEJBSjUwZkNFRWtURUhqVEtralp1ZFJSNjl4M3ZPeHk2WTE1VWJhM3RR?oc=5>

### How to Play META Stock as Meta Platforms Tests a New Prediction Markets App
- Summary: Meta launches a prediction markets app, potentially expanding its product offerings.
- Date: 2026-11-18 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxQY1pIcENNWE1fdjdWTzhuUzdkTUVra21hbzZLbjNFa1ptTm4wSXQ0UTNpUno2bzdueHg4WllFY1BiS09lTEVkMHVJVFl5Q0I4MllsUFJfWFlkM3d5N1BRdUZGRWo1VDdHT2E4RXBIc3dDSThOVDZqQmJyS2I1RUs4ckF5SGc2TUthQVoyUnY0TGV0MUt5eWNaUlVza0NTbDZuMlJCdEg1MUZPVWJRZWg2T25aekNacWNIWS1Z?oc=5>

### Here’s What Reinforcing Meta Platforms (META) New Monetization Opportunities
- Summary: Meta announces new monetization strategies to boost revenue.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxObUh6T2dfRFFGWldXUTFaaVJ4TE5pMF9CSGxGY0RfSGZWcXRPNFVmVUxGYWRlNlBEeTZzR3pydGVpc2FqdzlKTjJtaTh3VWU1V042VVRYY1pwRkJKNHVkS29sOUF2NWl3bWlCaFFleU5XVC1nN1V3bEpHN0I0WDFmN2hTMEJHdGM3ZFloTHBNbnBXSzE2VElwaUM4VGFQeWp5cVNFNHBPMjl6TkZGZHc?oc=5>

### Navigating Meta Platforms’ (META) Journey from July Dip to New 52-Week High
- Summary: Meta’s stock climbs to a new 52‑week high after a July dip.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOU0JKZmRKWEdaRGhjdElFQ3dKUVhqVW1NT0JwMGFLYkdTaVI4SUx3cWU4VFd2M1huQnlmNmxfWUczYTFIT3M2WU81cG03aUt3SVVIRU5FV0dnaTBPQTdDMmNRM2M3UGlQem13MUVIbUVwQkdxUjBGUFFkbFZ3UGZkOWdtZWlsdzdyYkZlVEhvXzN3ZW53RWlFbFdYZFBBcU1ESE1GNTRR?oc=5>

### Will ETF Buying Change Meta Stock Narrative
- Summary: ETF buying could shift Meta’s stock narrative, potentially boosting investor interest.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNUnhObF9vcWxydnRua1J4T2hsVjhTOExiYjFWYUJhTmxGazE1ZS1zTzVBN3JuUTkwaHVKM3h0bm95ZXU4NlBLQkFmbkk1cnlYVTBlc1F4Rk9VaVV4cnhtd1Y1QnVETzNjbkZvM3FObVc5Y182VjVjc1B4SXBIbjAwSUp3WUZlVXpqOHpFbkkxT2pqbGhKQWxEMw?oc=5>

### Meta: Buy The AI Payoff Before The Capex Fear Fades
- Summary: Investors encouraged to capitalize on AI gains before capex concerns ease.
- Date: 2026-11-19 | Impact: medium | Horizon: medium | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPRzR4YjRJeDVrMnZtYWplUWVJNjhkTXpQWkhQeS1YcVFqUVQ1NHo0a3pLU2NId3V3LUR4MmpnZUFjbE8ydmlQVlRxSXBBZG1pYmROaXBic0N1UkhkSEI2YVBSVUJYbUowQ0hDYklhN2tNTUJSR1VLenNqNHhXNHF6djJuazAxYzU4VV9CR0Qtd0ZwLTMzM1E?oc=5>

### The Zacks Analyst Blog Highlights Meta, Amazon's, Microsoft's and Alphabet's
- Summary: Zacks blog spotlights Meta among major tech firms.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxPaTd1ZHc3dU12QUgxQWsweWhoWTFZTG9TVkoxVEtadjVuX3lZUUVHSXZrQkFnUzIxZnQxdUJaQnc1WmtNZm1KTmlfbXNuTkRreWdUa08zdjM1OTAtMkJTRVpMYzZyQjIwSUd0ZkVtdksxalpPeWZmRmFPaXdoSkpsUEdsdVh1VFZmUDk5RnczMzNZTGxkemF6Yi1ZZ09VRFVKMnRqdG9vb2Jaam1lYzJlOXF3bWhBeGVBcjdNQXFDMEM0ckltcUtoWTBGYkRMNkstVVpxT0dqbEVmRkcycXpqUk9qU0xFVm9YS0c3Rg?oc=5>

### If the AI Trade Blows Up, Meta’s Saving Grace Is That Its Social Media Business Still “Generates a Ton of Cash”
- Summary: Meta’s cash flow remains strong amid AI concerns.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxQU3dHR2Z6SG5GOF9IMkVicFFjYnV5NFByWEhaLXpseldjdnpXQUhUSkxDWWozVzlNUU41akFTY0ZBXzBvUzl1MlRtS3NIcmRrcktOYlo3eFBZdmo4cDZiUy1lSGc4VWw4X3dwVnZ3RUEtNWlfdHhuOTZZeXVMT1BBcTJKbmxrajN0VkFMTkhrek9HYVZIYXJRbkhCREFERTZwZGZFdzRnV1FySHVkdmNBTlhPZnJvMi12OHBYQlljd0tpTGJzdjl2ZjZZdEhRdw?oc=5>

## HEADWINDS

### Meta shares drop about 2.5% after pausing non-voting Class C stock dividend due to Delaware lawsuit
- Summary: Meta shares drop about 2.5% after pausing non-voting Class C stock dividend due to Delaware lawsuit
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxOczNZUTFMeUdjSHo5SFVJemx0OEVISzZpWHRkUnhDWnVxS0M2QmROb1FOYVh0a2hxR1M1eDNLaDV2cllXd1RNWWJXZEZfa2p2d2E1ZGFzeGhDUzdBcWdnNGRLMDJGbHVuZFlNeEk0NFlWY0J3amw0Ynh0VkRuM1MwWUJjNlVlUWpwR3ZV?oc=5>

### Meta Platforms falls 5.93% in Friday's session
- Summary: Meta Platforms falls 5.93% in Friday's session
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigwFBVV95cUxQam9EaWRaZTBuQy14bHJuLXpkdjhGMnZfNndyNzZoR1Y1Z3FVajhvaUIzOWxqWU9SVWo5VVNSUG5GRTVKTlpYUjZTRm9FY2ZhZkVZeEtZTldnQy14dFpqeEJGbjF4Njc2Q3NKUm01MVpBYnVmWjhHbXdBRmhVNWQ2UVlrVQ?oc=5>

### Meta Pauses Zuckerberg Share Plan During Investor Legal Fight
- Summary: Meta suspends Zuckerberg’s share plan amid investor legal dispute.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNNVVZam9QRXJjREgtaGhPdlJxdmxiSW9yS0Jqa0d2Uk1UekxmYU01akxSYVBzdjV5TmJoNnFqSmpWdkF2cklrRG15UWFZc1NTOW1kRFVRbTd2cTR2M0x5RDkzY3ctc1J3MnFPZTJSOTRNWldFSDF6YlVrVW9rRUU0TWhzUXBRZDN4NEozSWJmOGkxdzkzQjRHTmNURmdNMGs?oc=5>

### Meta Platforms (META) Down 8.1% Since Last Earnings Report: Can It Rebound?
- Summary: Stock fell 8.1% post-earnings, questioning rebound prospects.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNTXZrckF0RXcxajVLS3l0NkdlUEZER1ZiVjdTbmhyZ0dUR3ZvSUJYMGVZVDQ3NW5hQ25INERESDlkbjZtbUZESnJUSThHNHZ1SEtyS2lOSkVpRklvcDV3c1JYZUl3ZlVVTUJxMV81bnZIWm83Skxia0FLTGtHazhUbXdoXzBKREFlLWdzLWV1V3hmNlhWX2c?oc=5>

### Meta’s (META) AI Spending Spree Looks Risky, but There’s More to the Story
- Summary: Meta’s heavy AI spend raises risk concerns, but potential upside remains.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQQm1Od0F5OXJYZ0Q4OWI5d1Z0X1FrQU5KX2hPeFotZTZfUFN5cUY5X0dHQWZFamNtejIwSG40c20xdWJUcUd1ZGdWVWhqVGE1bGxkZVpCR3NZX1FaX2ZHdXd0MFNJV21pVS1xN2l6bC1HUl9ETWZZa1JNcFVkTzlPME4zQWNGRmRiaktpVDRKRWNDaGNMNlE?oc=5>

## CATALYSTS

### Why is Meta stock down today? About 6% lower as the AI sell-off and an Apple agent report hit
- Summary: Meta shares fell 6% amid AI sell‑off and Apple agent report, reflecting market sentiment rather than company fundamentals.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxOaGZCNXlLOTdxUUFWd2JBOWRNVmlmeFUwd0V2c1cySXdvRk1XNjJvWTJnZnlETDJDdFh0OVI2eXY1VTEyUXVPTkw2NDVKWlY5eTFaM2tYV1JWb0xGbC0yNlZDT0FqNjNsdnZMN1dDOG5ERHA1QkpKQzNkMy0xN2VHOEZXVEVDYlVSN0JxRlJpQjJtYVVab3g0VEtFZDRDdDVVZU5LaW92VHU4RTNoMmJER2N3cXlNOWZ2UVE?oc=5>

### Daniel Loeb's Meta Stock Bet Stands Out as Tiger Global Trims
- Summary: Daniel Loeb maintains a strong Meta stake while Tiger Global reduces holdings.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.88
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNeXFXazFEX3JKcGdMbTNRX3BlYlJWaWhkQk43dzlvLUEtR0N3RDZmYVNDM0JTQjlCd1ZCWDhuODlsaEMxUW9CWjV2bzY0WjRGVTkzRVpab2QxM19HMGtJQkl2Y2tQNlJpQU1mb082MDlsbm1LR1BNdnB6SXUzbnJLcXVNcEhBOXUtM0t6aTU5REdtRzFscGlr?oc=5>

### Meta Stock Has Fallen 3% YTD. Its Cheapest AI Model Could Change Everything.
- Summary: Meta shares down 3% YTD amid AI model speculation.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxOeHFlaXBvVWhiTmtvbkJleXlOQnVNNWladTcwdWtFbDF0MFJ3OENoZWxsRHpsZVNabVVyZzZOdHJDZUR4QmZCOVdicG5lOVdGcEVxR1FvRzRuMTZJMGZGdGpFMHRwWWpSVmVWa2o2Y0xmRjlwSGZtQWVWVmhYQW5lcVJwZ2ZCYVJ6aC1nNHVCbXQ?oc=5>

### Meta Platforms is Cheap at 18.78X P/E: Buy, Sell or Hold the Stock?
- Summary: Analyst notes Meta’s low P/E ratio, suggesting potential upside or downside depending on strategy.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPbnEycDVUY09YNUpselQtRk0zcm45R0t3UGJveUhxdWxPV1F3OHMtY05lc2g4RU1lSnNTSV9NTG9kSjd3d3BKU0tRVEtWZXF0T3doWmxPbkR3Rjk0QWtYM3BGakY2NGFXVFRfT3V3TDh6Z0sza1lsYlZVV09KYW1SdDUwMFVCUVdkTXhIVEYzUlZHanZWWFVDa0llOW1PMERnblo4T1N3?oc=5>

### Meta Platforms (META) Rethinks 2030 Climate Goals After 45% AI Emissions Jump
- Summary: Meta revises 2030 climate targets following AI emissions increase.
- Date: 2026-11-21 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPam9WWTlDT0JsdTFGNWVPMmtWeVMyLVhpQ2haZXQydG1yQUU3YVloaDBsNTZvNmlqOFlyVFJkTUxtb1MxUW0yMzRINEdGU0tvVkVBNW11N0pwMnZMUGxYZjl0aTN0bEN6UmFGX2V1MFRfU205WHJTalBvd1RoUFRwbnNCRnRibEstcUxGbkJPNWZHc3ROeHNfa0JyRVhYdw?oc=5>

### George Soros Raised His Meta (META) Stake by 596%. Then the Stock Fell
- Summary: George Soros increased his Meta stake by 596%, triggering a stock decline. The move signals significant shareholder activity but its long-term impact remains uncertain.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOMmQycHY2WjJ6V3FuT0FNb1R1SktTQmVUQlZpeVloeXdsZl8ycEdfcmtrcU8teGExbndnVFJkTnZUSWdMdGx5b1lOVFZCdFBibmwtdWw2ZDJIM1hyV3FVSU1UTGo3UnlLcHhxU0VXVDlBU0JrdnpyVDdSNjh3Wl9RWUxza2c4a2FIeW04dFFEWE1HYVRRb0FWRVNn?oc=5>

## RISKS

### AI May Have Just Broken Meta’s Climate Promise
- Summary: Meta may have violated its climate commitments due to AI emissions surge.
- Date: 2026-11-21 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxPZmdwSHhkb2ZBd3dUZmtnNU9ZcUZZU2I4YnlUcXZZcmlZSG5lV2R3LUtjY0Q1VHU2TnRnc2ZiWU9xOFBrSTBVbzBWNHN1Wm9WV1FlNWYwNVdpNlFxc3NDa2RqR1lRTTdqdGVNWkRrNFZUTFNtZDRMaDhxU2d3R1kxSG9fSGhsZDJGUVpIRE91LW8?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **META** | **19.13** | **5.26** | **12.62** | **26.10** | **1,433,642,336,256.00 USD** | **-4.48** |
| GOOGL | 13.85 | 4.95 | 17.06 | 24.70 | 3,261,475,323,904.00 USD | -8.11 |
| SNAP | N/A | 3.50 | 48.64 | 14.30 | 7,855,924,736.00 USD | -41.52 |
| PINS | 68.04 | 3.01 | 30.70 | 11.90 | 9,365,383,168.00 USD | -34.18 |

Peers fetched as_of: 2026-11-21; META reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-21

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
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxQY1pIcENNWE1fdjdWTzhuUzdkTUVra21hbzZLbjNFa1ptTm4wSXQ0UTNpUno2bzdueHg4WllFY1BiS09lTEVkMHVJVFl5Q0I4MllsUFJfWFlkM3d5N1BRdUZGRWo1VDdHT2E4RXBIc3dDSThOVDZqQmJyS2I1RUs4ckF5SGc2TUthQVoyUnY0TGV0MUt5eWNaUlVza0NTbDZuMlJCdEg1MUZPVWJRZWg2T25aekNacWNIWS1Z?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxObUh6T2dfRFFGWldXUTFaaVJ4TE5pMF9CSGxGY0RfSGZWcXRPNFVmVUxGYWRlNlBEeTZzR3pydGVpc2FqdzlKTjJtaTh3VWU1V042VVRYY1pwRkJKNHVkS29sOUF2NWl3bWlCaFFleU5XVC1nN1V3bEpHN0I0WDFmN2hTMEJHdGM3ZFloTHBNbnBXSzE2VElwaUM4VGFQeWp5cVNFNHBPMjl6TkZGZHc?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOU0JKZmRKWEdaRGhjdElFQ3dKUVhqVW1NT0JwMGFLYkdTaVI4SUx3cWU4VFd2M1huQnlmNmxfWUczYTFIT3M2WU81cG03aUt3SVVIRU5FV0dnaTBPQTdDMmNRM2M3UGlQem13MUVIbUVwQkdxUjBGUFFkbFZ3UGZkOWdtZWlsdzdyYkZlVEhvXzN3ZW53RWlFbFdYZFBBcU1ESE1GNTRR?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNUnhObF9vcWxydnRua1J4T2hsVjhTOExiYjFWYUJhTmxGazE1ZS1zTzVBN3JuUTkwaHVKM3h0bm95ZXU4NlBLQkFmbkk1cnlYVTBlc1F4Rk9VaVV4cnhtd1Y1QnVETzNjbkZvM3FObVc5Y182VjVjc1B4SXBIbjAwSUp3WUZlVXpqOHpFbkkxT2pqbGhKQWxEMw?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPRzR4YjRJeDVrMnZtYWplUWVJNjhkTXpQWkhQeS1YcVFqUVQ1NHo0a3pLU2NId3V3LUR4MmpnZUFjbE8ydmlQVlRxSXBBZG1pYmROaXBic0N1UkhkSEI2YVBSVUJYbUowQ0hDYklhN2tNTUJSR1VLenNqNHhXNHF6djJuazAxYzU4VV9CR0Qtd0ZwLTMzM1E?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxPaTd1ZHc3dU12QUgxQWsweWhoWTFZTG9TVkoxVEtadjVuX3lZUUVHSXZrQkFnUzIxZnQxdUJaQnc1WmtNZm1KTmlfbXNuTkRreWdUa08zdjM1OTAtMkJTRVpMYzZyQjIwSUd0ZkVtdksxalpPeWZmRmFPaXdoSkpsUEdsdVh1VFZmUDk5RnczMzNZTGxkemF6Yi1ZZ09VRFVKMnRqdG9vb2Jaam1lYzJlOXF3bWhBeGVBcjdNQXFDMEM0ckltcUtoWTBGYkRMNkstVVpxT0dqbEVmRkcycXpqUk9qU0xFVm9YS0c3Rg?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxQU3dHR2Z6SG5GOF9IMkVicFFjYnV5NFByWEhaLXpseldjdnpXQUhUSkxDWWozVzlNUU41akFTY0ZBXzBvUzl1MlRtS3NIcmRrcktOYlo3eFBZdmo4cDZiUy1lSGc4VWw4X3dwVnZ3RUEtNWlfdHhuOTZZeXVMT1BBcTJKbmxrajN0VkFMTkhrek9HYVZIYXJRbkhCREFERTZwZGZFdzRnV1FySHVkdmNBTlhPZnJvMi12OHBYQlljd0tpTGJzdjl2ZjZZdEhRdw?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxOczNZUTFMeUdjSHo5SFVJemx0OEVISzZpWHRkUnhDWnVxS0M2QmROb1FOYVh0a2hxR1M1eDNLaDV2cllXd1RNWWJXZEZfa2p2d2E1ZGFzeGhDUzdBcWdnNGRLMDJGbHVuZFlNeEk0NFlWY0J3amw0Ynh0VkRuM1MwWUJjNlVlUWpwR3ZV?oc=5
- https://news.google.com/rss/articles/CBMigwFBVV95cUxQam9EaWRaZTBuQy14bHJuLXpkdjhGMnZfNndyNzZoR1Y1Z3FVajhvaUIzOWxqWU9SVWo5VVNSUG5GRTVKTlpYUjZTRm9FY2ZhZkVZeEtZTldnQy14dFpqeEJGbjF4Njc2Q3NKUm01MVpBYnVmWjhHbXdBRmhVNWQ2UVlrVQ?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNNVVZam9QRXJjREgtaGhPdlJxdmxiSW9yS0Jqa0d2Uk1UekxmYU01akxSYVBzdjV5TmJoNnFqSmpWdkF2cklrRG15UWFZc1NTOW1kRFVRbTd2cTR2M0x5RDkzY3ctc1J3MnFPZTJSOTRNWldFSDF6YlVrVW9rRUU0TWhzUXBRZDN4NEozSWJmOGkxdzkzQjRHTmNURmdNMGs?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNTXZrckF0RXcxajVLS3l0NkdlUEZER1ZiVjdTbmhyZ0dUR3ZvSUJYMGVZVDQ3NW5hQ25INERESDlkbjZtbUZESnJUSThHNHZ1SEtyS2lOSkVpRklvcDV3c1JYZUl3ZlVVTUJxMV81bnZIWm83Skxia0FLTGtHazhUbXdoXzBKREFlLWdzLWV1V3hmNlhWX2c?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQQm1Od0F5OXJYZ0Q4OWI5d1Z0X1FrQU5KX2hPeFotZTZfUFN5cUY5X0dHQWZFamNtejIwSG40c20xdWJUcUd1ZGdWVWhqVGE1bGxkZVpCR3NZX1FaX2ZHdXd0MFNJV21pVS1xN2l6bC1HUl9ETWZZa1JNcFVkTzlPME4zQWNGRmRiaktpVDRKRWNDaGNMNlE?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxOaGZCNXlLOTdxUUFWd2JBOWRNVmlmeFUwd0V2c1cySXdvRk1XNjJvWTJnZnlETDJDdFh0OVI2eXY1VTEyUXVPTkw2NDVKWlY5eTFaM2tYV1JWb0xGbC0yNlZDT0FqNjNsdnZMN1dDOG5ERHA1QkpKQzNkMy0xN2VHOEZXVEVDYlVSN0JxRlJpQjJtYVVab3g0VEtFZDRDdDVVZU5LaW92VHU4RTNoMmJER2N3cXlNOWZ2UVE?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNeXFXazFEX3JKcGdMbTNRX3BlYlJWaWhkQk43dzlvLUEtR0N3RDZmYVNDM0JTQjlCd1ZCWDhuODlsaEMxUW9CWjV2bzY0WjRGVTkzRVpab2QxM19HMGtJQkl2Y2tQNlJpQU1mb082MDlsbm1LR1BNdnB6SXUzbnJLcXVNcEhBOXUtM0t6aTU5REdtRzFscGlr?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxOeHFlaXBvVWhiTmtvbkJleXlOQnVNNWladTcwdWtFbDF0MFJ3OENoZWxsRHpsZVNabVVyZzZOdHJDZUR4QmZCOVdicG5lOVdGcEVxR1FvRzRuMTZJMGZGdGpFMHRwWWpSVmVWa2o2Y0xmRjlwSGZtQWVWVmhYQW5lcVJwZ2ZCYVJ6aC1nNHVCbXQ?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPbnEycDVUY09YNUpselQtRk0zcm45R0t3UGJveUhxdWxPV1F3OHMtY05lc2g4RU1lSnNTSV9NTG9kSjd3d3BKU0tRVEtWZXF0T3doWmxPbkR3Rjk0QWtYM3BGakY2NGFXVFRfT3V3TDh6Z0sza1lsYlZVV09KYW1SdDUwMFVCUVdkTXhIVEYzUlZHanZWWFVDa0llOW1PMERnblo4T1N3?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPam9WWTlDT0JsdTFGNWVPMmtWeVMyLVhpQ2haZXQydG1yQUU3YVloaDBsNTZvNmlqOFlyVFJkTUxtb1MxUW0yMzRINEdGU0tvVkVBNW11N0pwMnZMUGxYZjl0aTN0bEN6UmFGX2V1MFRfU205WHJTalBvd1RoUFRwbnNCRnRibEstcUxGbkJPNWZHc3ROeHNfa0JyRVhYdw?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOMmQycHY2WjJ6V3FuT0FNb1R1SktTQmVUQlZpeVloeXdsZl8ycEdfcmtrcU8teGExbndnVFJkTnZUSWdMdGx5b1lOVFZCdFBibmwtdWw2ZDJIM1hyV3FVSU1UTGo3UnlLcHhxU0VXVDlBU0JrdnpyVDdSNjh3Wl9RWUxza2c4a2FIeW04dFFEWE1HYVRRb0FWRVNn?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxPZmdwSHhkb2ZBd3dUZmtnNU9ZcUZZU2I4YnlUcXZZcmlZSG5lV2R3LUtjY0Q1VHU2TnRnc2ZiWU9xOFBrSTBVbzBWNHN1Wm9WV1FlNWYwNVdpNlFxc3NDa2RqR1lRTTdqdGVNWkRrNFZUTFNtZDRMaDhxU2d3R1kxSG9fSGhsZDJGUVpIRE91LW8?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
