# META Intelligence Report

- ticker: **META**
- Report as_of: **2026-11-24**
- Market data as_of: **2026-11-24**
- Quant sources: https://finance.yahoo.com/quote/META/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/META/key-statistics/
- AI analysis snapshot as_of: **2026-11-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-25T07:15:03.394220+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 3, 'ai': 17, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261124T081701Z-6c335e3d/META** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **8**; {'directional_claim_without_event_type': 4, 'low_uncalibrated_model_confidence': 1, 'negative_sentiment_in_tailwinds': 1, 'short_term_price_move_in_structural_risks': 2}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 13 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 20.0%; oldest publication 2026-11-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 589.8200 |
| Return 1D (%) | -1.3019 |
| Return 1W (%) | -4.6940 |
| Return 1M (%) | -8.2164 |
| Return YTD (%) | -10.4155 |
| Return 1Y (%) | -3.4629 |
| Annualized volatility (%) | 42.6590 |
| Beta vs SPY | 1.4057 |
| Max drawdown (%) | -28.7332 |
| Sharpe (rf=0) | 0.1280 |
| Downside deviation (rf=0, %) | 28.3518 |
| Sortino (rf=0) | 0.1926 |
| Historical VaR 95% (1D, %) | 3.8949 |
| Historical ES 95% (1D, %) | 5.8049 |
| Correlation vs SPY | 0.4928 |
| Tracking error vs SPY (%) | 37.6123 |
| P/E (trailing) | 20.12 |
| P/B | 5.53 |
| EV/EBITDA | 13.26 |
| Revenue growth (%) | 26.10 |
| Forward P/E (estimate) | 16.53 |
| Gross margin (%) | 81.03 |
| Operating margin (%) | 37.78 |
| Return on equity (%) | 32.26 |
| Free cash flow yield (%) | 1.12 |
| MA50 | 673.6533 |
| Close vs MA50 (%) | -12.4446 |
| MA200 | 627.1534 |
| Close vs MA200 (%) | -5.9528 |
| RSI (14, Wilder) | 40.2428 |
| MACD (12,26) | -19.9087 |
| MACD signal (9) | -17.9289 |
| MACD histogram | -1.9799 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'META': 289, 'SPY': 289}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 589.8200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.3019 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -4.6940 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -8.2164 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -10.4155 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -3.4629 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 42.6590 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 28.3518 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.1926 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.8949 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.8049 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4928 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.6123 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.4057 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.7332 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1280 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.5331 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 81.0340 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 37.7770 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 32.2640 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.1175 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 20.1235 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 40.2428 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.9799 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -12.4446 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -5.9528 -> Clearly below the moving-average trend level.

## TAILWINDS

### Tech surge sends Meta Platforms higher by 7% (META:NASDAQ)
- Summary: Meta shares jump 7% amid broader tech rally.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxNYy1PUTRsNjA0REdicy0zYzZfLTZHbnV2ZGFXUDhSY3g5NHhqaEd1bWItZWpUY0toSV80QWh1bmtMX3NSaFJmQ09sY29sYUs5Njd3RHNHV0xQYXVRMHlfODc3dGZhcnVLT21fajl2QkwxZllZa3hVQkdtM1RzNE4xUEctYUQzdmts?oc=5>

### Don’t Rush to Buy Meta Stock Yet Despite the Crash
- Summary: Advice cautions against buying Meta during market downturn.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOSXhId0NFZWluMWd5TWo4Z01OVGsxTWRPT0hrRWdkczVSUUtxXzg2OFNnY0lpYnhOTmc1ODdxeW9wdWFtUU1SVFJuSGhabERLZkZha0JTNlFQSjFQMzlVMm5hQlM5ZDNoamNIbmIxWFQtUmRJek1PQnRtZlRER0VsdEIwS2pCMXRsUG1lZ1d1YmJBMU41VC1CMg?oc=5>

### What Explains The Fall In Meta Stock?
- Summary: Analysis seeks reasons for Meta share decline.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQOGFiY1Nic3hFMjIxNWxSb1VGQXd2Q0x5VWxQLWJHUE9zTzIxOTNySGVlZVR1Q2tLWE1SVjhDMmlEb0wxQ3hXaHd5S0hiclNxNENTUjg3aXBIaUM0QS1wb0RFTEdkaVVnN0Rya2ZxOXRHQzhzVGhlbkRkQWtJLXlXN0k0ZWhlNnhndnplMFMxWVVXQzZCR1NZaFA3LURTQQ?oc=5>

### Why is Meta Platforms stock surging today?
- Summary: Explores factors behind Meta's current price surge.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPQzNSUm1CYUdCcGRiaUNEWGdhdVJHamVydVFHZC1yVC1CMnBzRXdkQ01uX3VpTnM4THV5T1hBSGdPQXFtZFpQdDd4c1A3WjlsdmMzRU9BMW5WY0I3RUFQQzVOaUh3ckxLZFhUdUR4SFJiOS1YeUtTNkRlTjJzUVZJYnZEODVnNERXZmpsVHUwWGFhdGpiaEdwRnJMUHpGbTZOSUFvMzR3?oc=5>

### David Abrams’ Meta Platforms, Inc. (META) Bet Is Backed by Strong Cash Flow and AI Growth
- Summary: Strong cash flow and AI growth support Meta's bet.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQbnR4ME9vMnJkeFdoXzVueFpWNk1Bb04zMm9QM1lLa2ZXdXlyeUJ2Q21qMEpYLVEyRDI0Xy1lUHVubWZneEdKWk9nb2lmQ1B0WEI5WEtJeE9pVHg4b0l0MHliWEtURVV4OG9jY0tTMU5Pb1N3c09JMmVvdE9FTXQzVnZzVjNKQi1Bb0U3QjJCVEtUTVZTNmhGU0ZsV2k?oc=5>

## HEADWINDS

### META Stock Is Down 24% From Peak: JPMorgan Sees ‘Attractive Buying Opportunity’ — But 2027 Spending, Capex Remain An Overhang
- Summary: META Stock Is Down 24% From Peak: JPMorgan Sees ‘Attractive Buying Opportunity’ — But 2027 Spending, Capex Remain An Overhang
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNSk9fRUN4RmFOTWdZSWVDRzFCTVU3akVWVldXOFhSWkhvdm5WUlFQczhPc2h0b1JHSHM4WU0xZk1FYkdkSmJ4Y3pXVTZ0UVZOV1JKVF9TcGFmbFU5VDJwTUF3QTJGN3pZbHVTQl9PVFVzTlVKR2lRSnhfY1UteTU0UzI5WjI3cG1vQW1uVloxcHZpdw?oc=5>

### Meta Platforms: Funding Uncertainty Is Burying The Muse Option (Rating Upgrade) (META)
- Summary: Funding uncertainty hampers Meta's Muse option, despite rating upgrade.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxNUkRmUklIeGQ2aVB1Tk1ZaXAtVVlyMzVMQWsxY21lZW5ENDRsRUNXR2s4Sm1ZR2tmZUVyNzlycU0yVF9iQkFLdkhjRlJjVkZWZmF6YmlJVmRVX3h4WF9taUJnYzZKeE1zSFNWQ0hMZGI0RGlzcW5SLW9tcG9WcVNiOHhNN0dMOGZ0YWtqdmM0WFhGZ1luVnFWV0R3MkJOU21qR3NsRW1TUkp6RG9RNGFYcjA2M0ZuOVNE?oc=5>

### Meta Stock Dips Premarket As Class C Share Pause Delays $60 Billion AI Funding Plan
- Summary: Class C pause delays $60B AI funding, causing premarket dip.
- Date: 2026-11-24 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxQNURCWEpIbFQ1TVVkdzRSWGxQUWRPS2pyRmxYdXRvT2FTNDVCMUJ5SG9vaEZ2YXh5cS1EWEEtQnFQdE9Lb2xUdnAzRlZzUU5FOWxfLXpnZFJwSjhOY2x4MHU5endNWHNuQjZjc3l0M24yZFNzSkFUNUtOMFZhdlNHbllNWVhsbXlfZ2VfbUp3Q25iTWtEeWI5cmxDU1FhUG9LQ2tSbHFDbkhxQ3lzbWt4NElsUGtablh6R1g1OG5SUExhWjBET1dUM25xSkhpdUhFTzdodXhn?oc=5>

## CATALYSTS

### Meta Platforms, Inc. $META Stock Acquired by Sumitomo Life Insurance Co.
- Summary: Meta Platforms, Inc. $META Stock Acquired by Sumitomo Life Insurance Co.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxOYjVZbVRDMGFMdU1oQkhvUC1YWFhiMFFNem9iOW9BbWc4ZVN6REhOX0taaFJkQjBEWUZRVU16RVVUc1VRb0tWOGFWTUZOWUxKR05NUWdZT2FYdldBLWRta0ktREFQb1BydU1PSUhVclhyaEZlUXdqcWNvUnJyRE83RXpJeFFWTFFrSldNeElZOTFrQ2hEeVkweU94ckJOUlJHdENERWNwdnpaaFNUOWxHalM0QXh3Ymo0WkxIS2Fqc3Z2NFlkMFBlWQ?oc=5>

### Mark Zuckerberg’s Meta Platforms Is Pouring Up to $145 Billion Into AI This Year. Investors Should Watch This 1 Number.
- Summary: Meta plans to invest $145B in AI this year, signaling strong commitment to AI development.
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi9AFBVV95cUxPTTdpZEszbEFkamptNXBGc1c2NF9fVnNJZ0tMUUI0ek94cFNpcy1sOF9hVWFRRFU3UzdfNDVGMElzengtRlczN0Z5bWozb1hpUXhJaUJYN3o3M21LWnZ5aDdqSURURnJxdC05a0ZpdWdFeXQybmJYTEtfMXA1SGotYVIwQXBpbW1ZdzZkZVVXX0haMklpbC1sR3EtWFQ4cDl1WVNiYmhnMkY5amFjWUVqS3EzclB1cVROSHhrNEtJZzNvZ1hGNjlIY0lHd3plR1l2U1RTNGJmUVp5eVRvc2ZYQ3UwOXQybGR0LUpzbnFVeVhVUHRG?oc=5>

### Meta Platforms (META) Rethinks 2030 Climate Goals After 45% AI Emissions Jump
- Summary: Meta revises 2030 climate targets following AI emissions increase.
- Date: 2026-11-21 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPam9WWTlDT0JsdTFGNWVPMmtWeVMyLVhpQ2haZXQydG1yQUU3YVloaDBsNTZvNmlqOFlyVFJkTUxtb1MxUW0yMzRINEdGU0tvVkVBNW11N0pwMnZMUGxYZjl0aTN0bEN6UmFGX2V1MFRfU205WHJTalBvd1RoUFRwbnNCRnRibEstcUxGbkJPNWZHc3ROeHNfa0JyRVhYdw?oc=5>

### Meta Stock Dips: What's Going On?
- Summary: Meta shares fell, prompting analysis of causes.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxONG1USC01dW5MV05MYS0tLU45d2lZeUJBc0Z1LWVxSHBtMk9SUEhvN2I0WDBBMG90bWpFQ1dNbmlKUWxzN2xoTnZaa2dMakRsZkxVZWRxdXdmT3pfRXpDUUtQSHFUdXFZQnhDNjNtYUxCa3UwRlRRZ3F6cGZMdVN2bXlUbTVuaTUwWFhuMk9tcE1rcGFVYkE?oc=5>

### What Moved Meta Stock?
- Summary: Factors behind recent Meta share movement examined.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxOVzNJQmsyN0VLTFFUNmNBS2VXYzhrdnFFa2J5Mi0zSGxCaHFFWlRRZEhZWklGT3c4SGVlcmhFY2RkNkNTbHYxRUZnem1sRHU3Wkp2c2s0dzRiRjlHaUFDNkdrWC1QQlZpeXVkYkZYeDkxRUtUVnNaazVubFNNZXlrdzE2MTBYVWZMbmc?oc=5>

### OpenAI and Meta Could Get 320 Million AMD Shares for a Penny Each
- Summary: Meta may acquire 320M AMD shares at $0.01 each.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxPWm5YRk9KTTJXTGJKeHhFaWtKbS0xamJVR0VHZS1wb2hfR2hjOVR2bW1JY0R5bmxWOFcxVi1tWWFGNkVJVUh1UDBSOS1fUUt3ekdPcTd2c1F3cnFsM0FKOVRHSEJpR0h2UlhNNWRlZ1FqakZUZk1GRktXMTFNdHJ6SUExMTRQVERrMGxFRHZMOVNLWlAtZjlBTEN0bHk4bXJDVmNKRGFSZFFmYnUzQmc?oc=5>

### David Tepper, George Soros and 5 Other Famous Investors Own Meta. Here’s Who Bought and Sold Recently
- Summary: Famous investors are buying and selling Meta shares, indicating active ownership changes.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNOFRwcnRWSERWQzlUVThvVEdaVmtma3lSN2tVeXcxVFFPSjdTck9hYjV5UDVyblNWT2daVEhsNTV2bHpZcGdFQWlSaDhMT3RKNVlKYWEtVnVqOVJUTm1UY09vQTVxelZkb2haTlBxcEpHYzJXVFpRZDF4T0phWmNIWVJMZnAyMEZZc04yTndzVVlwaVNsS0Fz?oc=5>

## RISKS

### Meta pauses Class C share issuance amid shareholder lawsuit
- Summary: Meta pauses Class C share issuance amid shareholder lawsuit
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxNN2g3TFJ5emdHN3NnLVJ6TTFuUThTVW42UmthQXkzLWtkaUUxN3hyOWRtZWttRGdaOVFZMjZoOFJwYmJfa1ZtX0RfZ0hEai14NXFBX0s5ei1EMDhiQmhDaTQ4WHNNNEJsLVNaS25fQVh5eGpnektkOG9xSTJncXVNRjI3U3ZRLVBFTUJuOVR4TGdSbllaZ29MRUxxcU1ZbUxYcDc3MHdEV2l0Q3ZzdlpBZV9kZFcwZw?oc=5>

### Meta Fell 8% Over the Last 30 Days: Mutiple Wall Street Desks Expect 67% Returns From Here
- Summary: Meta down 8% last month; analysts expect 67% upside.
- Date: 2026-11-24 | Impact: high | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxQa012QkliREw1ajZjTmVNS0RqUUlqUk1BVFJJZVZlaEYtTFh0dHl0cjRkb2dDa0RfWVVyV0JDTnptdzZSbmJOZmcxcTdQNVFuUFYwR3VmY1NyS3YtQmo2YXRTU3dwazlyVVhHZ0hyakM3MUdGOEtqSVZLT1RIeDF1YXZHUjBlSm9FbTBWZ1Q3Z2NVeHVHZlBQZ1hub1JVekJFbzE5dkZBcl9XWHZqRldFS21BME9IWFdueTh2TE55SWo0MUlDWXM3bVpQZw?oc=5>

### Dan Loeb’s Third Point Takes $475 Million Stake in Meta as Institutional Investors Concentrate Their Wealth in Tech Winners
- Summary: Institutional investor Dan Loeb’s stake signals significant ownership concentration.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi-AFBVV95cUxOSEdSZDFpaUI4MVhuMlBUUlNGeXlTYXQ0SVRGa0syeDBwOVplbzVQbmM4Tm85NXFackh2dU5LbUl2XzVobkwyOUxYejJTaXhlSFF4T0FuUlY5VW1SS3JFS0Q0aU5PTWNHUlVJV2R1V2ZZeFJCTmVndGVieE5RelJlYXVfS1N6c2RGeXg4NGItUmxEYnRicVU2cXJDVlBqanJOREtxN1A3YUQ5TDV0N1B2S1M0LXJPVGVEYnBWOTllWWZlNmhqNkw1Slp1ckRvaTBRNlNWYWk5UXlmUVVzczBZdUo4amYxTFN4amhra0JwUi0tZG15MXI4Rg?oc=5>

### META Rides on Strong Demand in Ad Business: Can It Beat RDDT and SNAP?
- Summary: Meta’s ad demand performance may affect future revenue growth.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxQbXI3MlJiUWZtNjdaczllY1A0N1R4UUpoN3kwaVZ4eWlVZk1UWFd3SlF5bDIxY0dYTkpCWkI5YkthUWQxWVBVRms5cnlUcmFBSm5TRUNGWVE0bGkwWXhlZzMtcTNDZFFSRmQxTTdPdzZJakFyRlUwRVdScHl4RlZjWEY4X0RPZTMwZzl3ZUY3UTZzMm5SLWQyMFJYaGVpR2tGVENjanpoU1BXUHg2UDZGdlY3aklYck5QNmlPenhGekZvQQ?oc=5>

### JPMorgan cuts Meta stock price target on 2027 spending concerns
- Summary: JPMorgan lowers price target due to 2027 spending worries.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxNbG11c2VCMzN0eFo5ZHRBN0doX1lqYWc4MlRVZDBCQTFsX2VGdjkxT0JwWW9PWURXaHRnNEhRT2ZCN3hwdHRXaFh2SDllLTNzMW5LalF5dHlNRk5jb0ZuLWxkOEo1akNDMFU2LUpCU08xemV0WkZTVC1meERzLVVZRDdJMnA2THp0WnJsWE8xVGEzZHNjQS14Y0NreEV5Nmo4QTlOOTVSbmpaWENHWlFzMVNWWHBrSXk3U0JGSWVpWTA?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **META** | **20.12** | **5.53** | **13.26** | **26.10** | **1,507,722,133,504.00 USD** | **-3.46** |
| GOOGL | 14.57 | 5.20 | 17.97 | 24.70 | 3,430,640,517,120.00 USD | -12.18 |
| SNAP | N/A | 3.76 | 51.74 | 14.30 | 8,442,960,384.00 USD | -36.33 |
| PINS | 77.08 | 3.41 | 34.90 | 11.90 | 10,609,895,424.00 USD | -25.37 |

Peers fetched as_of: 2026-11-24; META reuses existing data (market data as_of: 2026-11-24); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

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
- Filing date: 2026-10-22
- Revenue (latest available single quarter): 13,727,000,000.00 USD; period 2018-07-01/2018-09-30; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 9,860,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiiAFBVV95cUxNYy1PUTRsNjA0REdicy0zYzZfLTZHbnV2ZGFXUDhSY3g5NHhqaEd1bWItZWpUY0toSV80QWh1bmtMX3NSaFJmQ09sY29sYUs5Njd3RHNHV0xQYXVRMHlfODc3dGZhcnVLT21fajl2QkwxZllZa3hVQkdtM1RzNE4xUEctYUQzdmts?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOSXhId0NFZWluMWd5TWo4Z01OVGsxTWRPT0hrRWdkczVSUUtxXzg2OFNnY0lpYnhOTmc1ODdxeW9wdWFtUU1SVFJuSGhabERLZkZha0JTNlFQSjFQMzlVMm5hQlM5ZDNoamNIbmIxWFQtUmRJek1PQnRtZlRER0VsdEIwS2pCMXRsUG1lZ1d1YmJBMU41VC1CMg?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQOGFiY1Nic3hFMjIxNWxSb1VGQXd2Q0x5VWxQLWJHUE9zTzIxOTNySGVlZVR1Q2tLWE1SVjhDMmlEb0wxQ3hXaHd5S0hiclNxNENTUjg3aXBIaUM0QS1wb0RFTEdkaVVnN0Rya2ZxOXRHQzhzVGhlbkRkQWtJLXlXN0k0ZWhlNnhndnplMFMxWVVXQzZCR1NZaFA3LURTQQ?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPQzNSUm1CYUdCcGRiaUNEWGdhdVJHamVydVFHZC1yVC1CMnBzRXdkQ01uX3VpTnM4THV5T1hBSGdPQXFtZFpQdDd4c1A3WjlsdmMzRU9BMW5WY0I3RUFQQzVOaUh3ckxLZFhUdUR4SFJiOS1YeUtTNkRlTjJzUVZJYnZEODVnNERXZmpsVHUwWGFhdGpiaEdwRnJMUHpGbTZOSUFvMzR3?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQbnR4ME9vMnJkeFdoXzVueFpWNk1Bb04zMm9QM1lLa2ZXdXlyeUJ2Q21qMEpYLVEyRDI0Xy1lUHVubWZneEdKWk9nb2lmQ1B0WEI5WEtJeE9pVHg4b0l0MHliWEtURVV4OG9jY0tTMU5Pb1N3c09JMmVvdE9FTXQzVnZzVjNKQi1Bb0U3QjJCVEtUTVZTNmhGU0ZsV2k?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNSk9fRUN4RmFOTWdZSWVDRzFCTVU3akVWVldXOFhSWkhvdm5WUlFQczhPc2h0b1JHSHM4WU0xZk1FYkdkSmJ4Y3pXVTZ0UVZOV1JKVF9TcGFmbFU5VDJwTUF3QTJGN3pZbHVTQl9PVFVzTlVKR2lRSnhfY1UteTU0UzI5WjI3cG1vQW1uVloxcHZpdw?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxNUkRmUklIeGQ2aVB1Tk1ZaXAtVVlyMzVMQWsxY21lZW5ENDRsRUNXR2s4Sm1ZR2tmZUVyNzlycU0yVF9iQkFLdkhjRlJjVkZWZmF6YmlJVmRVX3h4WF9taUJnYzZKeE1zSFNWQ0hMZGI0RGlzcW5SLW9tcG9WcVNiOHhNN0dMOGZ0YWtqdmM0WFhGZ1luVnFWV0R3MkJOU21qR3NsRW1TUkp6RG9RNGFYcjA2M0ZuOVNE?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxQNURCWEpIbFQ1TVVkdzRSWGxQUWRPS2pyRmxYdXRvT2FTNDVCMUJ5SG9vaEZ2YXh5cS1EWEEtQnFQdE9Lb2xUdnAzRlZzUU5FOWxfLXpnZFJwSjhOY2x4MHU5endNWHNuQjZjc3l0M24yZFNzSkFUNUtOMFZhdlNHbllNWVhsbXlfZ2VfbUp3Q25iTWtEeWI5cmxDU1FhUG9LQ2tSbHFDbkhxQ3lzbWt4NElsUGtablh6R1g1OG5SUExhWjBET1dUM25xSkhpdUhFTzdodXhn?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxOYjVZbVRDMGFMdU1oQkhvUC1YWFhiMFFNem9iOW9BbWc4ZVN6REhOX0taaFJkQjBEWUZRVU16RVVUc1VRb0tWOGFWTUZOWUxKR05NUWdZT2FYdldBLWRta0ktREFQb1BydU1PSUhVclhyaEZlUXdqcWNvUnJyRE83RXpJeFFWTFFrSldNeElZOTFrQ2hEeVkweU94ckJOUlJHdENERWNwdnpaaFNUOWxHalM0QXh3Ymo0WkxIS2Fqc3Z2NFlkMFBlWQ?oc=5
- https://news.google.com/rss/articles/CBMi9AFBVV95cUxPTTdpZEszbEFkamptNXBGc1c2NF9fVnNJZ0tMUUI0ek94cFNpcy1sOF9hVWFRRFU3UzdfNDVGMElzengtRlczN0Z5bWozb1hpUXhJaUJYN3o3M21LWnZ5aDdqSURURnJxdC05a0ZpdWdFeXQybmJYTEtfMXA1SGotYVIwQXBpbW1ZdzZkZVVXX0haMklpbC1sR3EtWFQ4cDl1WVNiYmhnMkY5amFjWUVqS3EzclB1cVROSHhrNEtJZzNvZ1hGNjlIY0lHd3plR1l2U1RTNGJmUVp5eVRvc2ZYQ3UwOXQybGR0LUpzbnFVeVhVUHRG?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPam9WWTlDT0JsdTFGNWVPMmtWeVMyLVhpQ2haZXQydG1yQUU3YVloaDBsNTZvNmlqOFlyVFJkTUxtb1MxUW0yMzRINEdGU0tvVkVBNW11N0pwMnZMUGxYZjl0aTN0bEN6UmFGX2V1MFRfU205WHJTalBvd1RoUFRwbnNCRnRibEstcUxGbkJPNWZHc3ROeHNfa0JyRVhYdw?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxONG1USC01dW5MV05MYS0tLU45d2lZeUJBc0Z1LWVxSHBtMk9SUEhvN2I0WDBBMG90bWpFQ1dNbmlKUWxzN2xoTnZaa2dMakRsZkxVZWRxdXdmT3pfRXpDUUtQSHFUdXFZQnhDNjNtYUxCa3UwRlRRZ3F6cGZMdVN2bXlUbTVuaTUwWFhuMk9tcE1rcGFVYkE?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxOVzNJQmsyN0VLTFFUNmNBS2VXYzhrdnFFa2J5Mi0zSGxCaHFFWlRRZEhZWklGT3c4SGVlcmhFY2RkNkNTbHYxRUZnem1sRHU3Wkp2c2s0dzRiRjlHaUFDNkdrWC1QQlZpeXVkYkZYeDkxRUtUVnNaazVubFNNZXlrdzE2MTBYVWZMbmc?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxPWm5YRk9KTTJXTGJKeHhFaWtKbS0xamJVR0VHZS1wb2hfR2hjOVR2bW1JY0R5bmxWOFcxVi1tWWFGNkVJVUh1UDBSOS1fUUt3ekdPcTd2c1F3cnFsM0FKOVRHSEJpR0h2UlhNNWRlZ1FqakZUZk1GRktXMTFNdHJ6SUExMTRQVERrMGxFRHZMOVNLWlAtZjlBTEN0bHk4bXJDVmNKRGFSZFFmYnUzQmc?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNOFRwcnRWSERWQzlUVThvVEdaVmtma3lSN2tVeXcxVFFPSjdTck9hYjV5UDVyblNWT2daVEhsNTV2bHpZcGdFQWlSaDhMT3RKNVlKYWEtVnVqOVJUTm1UY09vQTVxelZkb2haTlBxcEpHYzJXVFpRZDF4T0phWmNIWVJMZnAyMEZZc04yTndzVVlwaVNsS0Fz?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxNN2g3TFJ5emdHN3NnLVJ6TTFuUThTVW42UmthQXkzLWtkaUUxN3hyOWRtZWttRGdaOVFZMjZoOFJwYmJfa1ZtX0RfZ0hEai14NXFBX0s5ei1EMDhiQmhDaTQ4WHNNNEJsLVNaS25fQVh5eGpnektkOG9xSTJncXVNRjI3U3ZRLVBFTUJuOVR4TGdSbllaZ29MRUxxcU1ZbUxYcDc3MHdEV2l0Q3ZzdlpBZV9kZFcwZw?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxQa012QkliREw1ajZjTmVNS0RqUUlqUk1BVFJJZVZlaEYtTFh0dHl0cjRkb2dDa0RfWVVyV0JDTnptdzZSbmJOZmcxcTdQNVFuUFYwR3VmY1NyS3YtQmo2YXRTU3dwazlyVVhHZ0hyakM3MUdGOEtqSVZLT1RIeDF1YXZHUjBlSm9FbTBWZ1Q3Z2NVeHVHZlBQZ1hub1JVekJFbzE5dkZBcl9XWHZqRldFS21BME9IWFdueTh2TE55SWo0MUlDWXM3bVpQZw?oc=5
- https://news.google.com/rss/articles/CBMi-AFBVV95cUxOSEdSZDFpaUI4MVhuMlBUUlNGeXlTYXQ0SVRGa0syeDBwOVplbzVQbmM4Tm85NXFackh2dU5LbUl2XzVobkwyOUxYejJTaXhlSFF4T0FuUlY5VW1SS3JFS0Q0aU5PTWNHUlVJV2R1V2ZZeFJCTmVndGVieE5RelJlYXVfS1N6c2RGeXg4NGItUmxEYnRicVU2cXJDVlBqanJOREtxN1A3YUQ5TDV0N1B2S1M0LXJPVGVEYnBWOTllWWZlNmhqNkw1Slp1ckRvaTBRNlNWYWk5UXlmUVVzczBZdUo4amYxTFN4amhra0JwUi0tZG15MXI4Rg?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxQbXI3MlJiUWZtNjdaczllY1A0N1R4UUpoN3kwaVZ4eWlVZk1UWFd3SlF5bDIxY0dYTkpCWkI5YkthUWQxWVBVRms5cnlUcmFBSm5TRUNGWVE0bGkwWXhlZzMtcTNDZFFSRmQxTTdPdzZJakFyRlUwRVdScHl4RlZjWEY4X0RPZTMwZzl3ZUY3UTZzMm5SLWQyMFJYaGVpR2tGVENjanpoU1BXUHg2UDZGdlY3aklYck5QNmlPenhGekZvQQ?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxNbG11c2VCMzN0eFo5ZHRBN0doX1lqYWc4MlRVZDBCQTFsX2VGdjkxT0JwWW9PWURXaHRnNEhRT2ZCN3hwdHRXaFh2SDllLTNzMW5LalF5dHlNRk5jb0ZuLWxkOEo1akNDMFU2LUpCU08xemV0WkZTVC1meERzLVVZRDdJMnA2THp0WnJsWE8xVGEzZHNjQS14Y0NreEV5Nmo4QTlOOTVSbmpaWENHWlFzMVNWWHBrSXk3U0JGSWVpWTA?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
