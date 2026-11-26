# META Intelligence Report

- ticker: **META**
- Report as_of: **2026-11-25**
- Market data as_of: **2026-11-25**
- Quant sources: https://finance.yahoo.com/quote/META/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/META/key-statistics/
- AI analysis snapshot as_of: **2026-11-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-26T06:50:17.357793+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 4, 'ai': 14, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **11** exact headline/source/date matches; prior report **20261125T065354Z-0b3565c6/META** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **4**; {'directional_claim_without_event_type': 3, 'negative_sentiment_in_tailwinds': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 13 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 16.67%; oldest publication 2026-11-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 609.8900 |
| Return 1D (%) | 3.4027 |
| Return 1W (%) | -1.0529 |
| Return 1M (%) | -5.0932 |
| Return YTD (%) | -7.3672 |
| Return 1Y (%) | -3.8133 |
| Annualized volatility (%) | 42.6272 |
| Beta vs SPY | 1.3899 |
| Max drawdown (%) | -28.7332 |
| Sharpe (rf=0) | 0.1192 |
| Downside deviation (rf=0, %) | 28.3518 |
| Sortino (rf=0) | 0.1793 |
| Historical VaR 95% (1D, %) | 3.8949 |
| Historical ES 95% (1D, %) | 5.8049 |
| Correlation vs SPY | 0.4868 |
| Tracking error vs SPY (%) | 37.6873 |
| P/E (trailing) | 20.81 |
| P/B | 5.72 |
| EV/EBITDA | 13.70 |
| Revenue growth (%) | 26.10 |
| Forward P/E (estimate) | 17.10 |
| Gross margin (%) | 81.03 |
| Operating margin (%) | 37.78 |
| Return on equity (%) | 32.26 |
| Free cash flow yield (%) | 1.08 |
| MA50 | 672.3955 |
| Close vs MA50 (%) | -9.2959 |
| MA200 | 626.8579 |
| Close vs MA200 (%) | -2.7068 |
| RSI (14, Wilder) | 45.7004 |
| MACD (12,26) | -18.2695 |
| MACD signal (9) | -17.9970 |
| MACD histogram | -0.2725 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'META': 290, 'SPY': 290}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 609.8900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 3.4027 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.0529 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -5.0932 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -7.3672 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -3.8133 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 42.6272 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 28.3518 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.1793 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.8949 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.8049 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4868 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.6873 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.3899 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.7332 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1192 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.0956 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 81.0340 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 37.7770 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 32.2640 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.0807 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 20.8083 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 45.7004 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.2725 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -9.2959 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -2.7068 -> Slightly below the moving-average trend level.

## TAILWINDS

### What Explains The Fall In Meta Stock?
- Summary: Analysis seeks reasons for Meta share decline.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQOGFiY1Nic3hFMjIxNWxSb1VGQXd2Q0x5VWxQLWJHUE9zTzIxOTNySGVlZVR1Q2tLWE1SVjhDMmlEb0wxQ3hXaHd5S0hiclNxNENTUjg3aXBIaUM0QS1wb0RFTEdkaVVnN0Rya2ZxOXRHQzhzVGhlbkRkQWtJLXlXN0k0ZWhlNnhndnplMFMxWVVXQzZCR1NZaFA3LURTQQ?oc=5>

### Don’t Rush to Buy Meta Stock Yet Despite the Crash
- Summary: Advice cautions against buying Meta during market downturn.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOSXhId0NFZWluMWd5TWo4Z01OVGsxTWRPT0hrRWdkczVSUUtxXzg2OFNnY0lpYnhOTmc1ODdxeW9wdWFtUU1SVFJuSGhabERLZkZha0JTNlFQSjFQMzlVMm5hQlM5ZDNoamNIbmIxWFQtUmRJek1PQnRtZlRER0VsdEIwS2pCMXRsUG1lZ1d1YmJBMU41VC1CMg?oc=5>

### Tech surge sends Meta Platforms higher by 7% (META:NASDAQ)
- Summary: Meta shares jump 7% amid broader tech rally.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxNYy1PUTRsNjA0REdicy0zYzZfLTZHbnV2ZGFXUDhSY3g5NHhqaEd1bWItZWpUY0toSV80QWh1bmtMX3NSaFJmQ09sY29sYUs5Njd3RHNHV0xQYXVRMHlfODc3dGZhcnVLT21fajl2QkwxZllZa3hVQkdtM1RzNE4xUEctYUQzdmts?oc=5>

### Meta Platforms (META) Expands Muse Shopping In The UK, Is The Stock Still A Bargain?
- Summary: Meta launches Muse Shopping in the UK, expanding e-commerce presence.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOdjEyTVRlcWZuVV9PRHBXVFFkUGRqem8zWVh6R2tqb0lfb19HR1BpaTgtZ185eGFKWXpsakNra2dwMWNtU25sYlNaTjJOSjYxRS1YbERkZ0I4UHlEa0JJUHBLOVlOd0hoWTJpOGF1U25pTGVldl9pbzhfclFacXE1T056SXVqbUdsTnV0c2k2RHJDU0t6dTlLLXlTU1NFZw?oc=5>

## HEADWINDS

### META Stock Is Down 24% From Peak: JPMorgan Sees ‘Attractive Buying Opportunity’ — But 2027 Spending, Capex Remain An Overhang
- Summary: META Stock Is Down 24% From Peak: JPMorgan Sees ‘Attractive Buying Opportunity’ — But 2027 Spending, Capex Remain An Overhang
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigJBVV95cUxNQy1aZXN6YnZtWGtxbjFadjliTk5FWG9rbkN5WWRMT0pSLXFZQnlhbW5Fd0FueVFvbno0OFZqMUtvRkFvQjlDUEVqal8zTzltamJPTm9NQXFCYkVweng3SEpYLWwzZGo2bGJGcXZpb1gtYXpqQjRVbUtIZFpISG5maVpxR1YzYmJYck91cG5jTFlsNHE0NWV1TUJHY2wyMF9mdk5IS2ZIZEFQTEQ0ZGpKaElMVFRhdGl5Z0hLcHFqN0xwSVNrX0NsUkt6NnRIWFNvTWRYWVhLb0ViOWFWaTM5UHhsS01yeWdmNDZBUlNwZ25fUGhLbUtDbjN0SDNYN1dFOXd1aW4tR0hhZw?oc=5>

### Meta stock falls as Class C share delay raises questions over AI funding
- Summary: Meta stock falls as Class C share delay raises questions over AI funding
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxPMFdMWm1xOWhlXzdJbW13djlYT3VEWWhKOWp3WnR1Z25Oci1UN2RXZ1Z0SXlld2ZyYTE4UHBnTmM4Rm84N3Nrcm80MTU3bkdBbVNNaHFYLVRtMmgyM213b0tuV0pEcjUxY1pnWDhaVkdLeXBSMk82ejlwYUpGZmplNHVabnAtZ2sxTFVlaFZKRjJRb3VpbVlwQVMwcXBnN1h6S2RJam1VWFgwMXlWckFza2lpSVp2TnNCNWZOSEhVc2Q5em1VMWhvSw?oc=5>

### Meta Platforms Stocks Fall 2.91% as Big Tech Selloff Spreads
- Summary: Meta Platforms Stocks Fall 2.91% as Big Tech Selloff Spreads
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxOZGVYd29wLVlqNlpUTFJnZlkyZGpGRE1KVjlBR2tjLTJBN1N4QjliQWVVcGpabXFrdXFDcTVjUTFOVFpBZkQ4ZmhqZUxhcXFYQjRUZVFoUVZUNk5lT3JyVnJ2Sm9WWGtFWmE1QVlJcGRmOE56Mll0Z1FBSGJMdnYtc2lHMUdZXzk0YnkwRmNWMFVJbmJFaW5UOG45VjdXMmxnQ25JY2JKaE1pSnFqWloxV0pidHdEZlZGT1lF?oc=5>

### Meta Stock Dips Premarket As Class C Share Pause Delays $60 Billion AI Funding Plan
- Summary: Class C pause delays $60B AI funding, causing premarket dip.
- Date: 2026-11-24 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxQNURCWEpIbFQ1TVVkdzRSWGxQUWRPS2pyRmxYdXRvT2FTNDVCMUJ5SG9vaEZ2YXh5cS1EWEEtQnFQdE9Lb2xUdnAzRlZzUU5FOWxfLXpnZFJwSjhOY2x4MHU5endNWHNuQjZjc3l0M24yZFNzSkFUNUtOMFZhdlNHbllNWVhsbXlfZ2VfbUp3Q25iTWtEeWI5cmxDU1FhUG9LQ2tSbHFDbkhxQ3lzbWt4NElsUGtablh6R1g1OG5SUExhWjBET1dUM25xSkhpdUhFTzdodXhn?oc=5>

### Why is Meta Platforms stock sliding today?
- Summary: Meta stock experiencing a decline, indicating market concerns.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPZDhvWjk4QWhGdVJpM1JuQVRYbkc5Z0tpNGxSZWgzLWdPRE5LaHpvMW1lVV9VSFljNXlUaTVVYk0xZEtvamZDVnR4RERGOVdoQlJSdjhhVHgzLWNIOTNNZ1JGWkI0NEtVcHUxbW8xYUVyMFozREVDZXZXVWVtS0lDa3piQ3FUa29kQVg3TlZrdVBEWHpHb3F1MGVDZWRNMlNEZlBFdWhR?oc=5>

### Will Meta Platforms sustain gains with ongoing debate over AI strategy and risk appetite?
- Summary: Uncertainty over Meta's AI strategy may hinder future gains.
- Date: 2026-11-25 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMihgFBVV95cUxPVWRndzl1YkJMdDh6MEZLMHlKVzhNYXdJQTdpZnRtNXo5dXRyNU1FdjZjcGhMVWgyTFdmelBMbVU3WExiM0lXZjhBWWI0Tl9VMFN5VnVyVmRyeUp5S1RtZWlSZndZT09EVXRTZnNuazk0LXloYTQ4cm1OWms1UUNqNEFmQ1pHZw?oc=5>

## CATALYSTS

### Meta Stock Dips: What's Going On?
- Summary: Meta shares fell, prompting analysis of causes.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxONG1USC01dW5MV05MYS0tLU45d2lZeUJBc0Z1LWVxSHBtMk9SUEhvN2I0WDBBMG90bWpFQ1dNbmlKUWxzN2xoTnZaa2dMakRsZkxVZWRxdXdmT3pfRXpDUUtQSHFUdXFZQnhDNjNtYUxCa3UwRlRRZ3F6cGZMdVN2bXlUbTVuaTUwWFhuMk9tcE1rcGFVYkE?oc=5>

### What Moved Meta Stock?
- Summary: Factors behind recent Meta share movement examined.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxOVzNJQmsyN0VLTFFUNmNBS2VXYzhrdnFFa2J5Mi0zSGxCaHFFWlRRZEhZWklGT3c4SGVlcmhFY2RkNkNTbHYxRUZnem1sRHU3Wkp2c2s0dzRiRjlHaUFDNkdrWC1QQlZpeXVkYkZYeDkxRUtUVnNaazVubFNNZXlrdzE2MTBYVWZMbmc?oc=5>

### Meta Says Muse “Raises Conversions for Advertisers.” It Already Places 51% of AI Agent Orders
- Summary: Meta’s Muse AI tool boosts advertiser conversions, handling 51% of AI agent orders, signaling stronger ad performance and product innovation.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxQVkpCOFRMbmZiUk9ZVUtmbXpuSnR4OGZ2aDBlRzdfSGc0WlB2UE52TTQyYl9mdTZyZnFjYUdVRGpqaS1rSE4yVUxERHZURVVkdTFQTHpub3Z2bGN1Nmg5d3kwbDZ6b0QzVDd6alJVR2dLYklIaGRxRGxRYV8zcENnaVctRzZqaUZfS0RGbjAtQmZYSUl1MjJSMXJZTXhsZm9fcUxv?oc=5>

### Meta Platforms (META) Down 8.1% Since Last Earnings Report: Can It Rebound?
- Summary: Meta’s stock fell 8.1% post-earnings, raising concerns about short-term performance and investor sentiment.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigAFBVV95cUxNYk5tSmtVOHlocG5sQXpiLXBUU08xQjVVQXJQRE8xU0xxM2gwWk1MNG5KYmFfWU11RFdSaF9VOGRQTTZ5V1V5UmNKUDdaUWxlaGFmOWxrcjBONC03eDNKQmVQdHp1U3drNi1vaU9PUkx1UWwyUFpfYm4yenFvZGwyRw?oc=5>

### Meta Platforms Inc Stock (META) Moved Up by 3.04% on Nov 25: What Signal Does It Send?
- Summary: META shares rose 3.04% on Nov 25, indicating a potential short-term positive market reaction.
- Date: 2026-11-25 | Impact: low | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNT0RTTDc3WmVkaEVJLUtiT1BuSTVWZnRDY0xqbHpTaGdONHhzUHpaZTRmQzhNcFZRdVBoQnBsRFZrRUFUbGZkZ1lnbjAxVEtZdkNGNWwyWXRrWl9ETEcybXNMaFJVZmloWDRxSGYzMVZTY3lTclp5cW1HTm5PSGQzTm5zNk1XdHVvc3pR?oc=5>

### How to Play META Stock as Meta Platforms Tests a New Prediction Markets App
- Summary: Meta is testing a prediction markets app, suggesting new product experimentation and potential future revenue streams.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.88
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQOUk1bWJIcDlxSUs5b3RqeFdlbFVLckdqeUdwLVZkMnQ4WDJUNEdTWm0yMWtQckFubzZOR0tCVUU3dnFKOF9WbmotZl9wTWFuNzlfOVFPYzZHUlVSQzFfcVY0ZDJId3ptQVVXaFpPVV9HT2g3YVFCY2Z3SUdIU2NCeWtuRzBfbDEyYWs1VW0wQ002RXYyR3Jrb3hHOA?oc=5>

## RISKS

### Meta Platforms stock falls amid support pressure and ongoing recapitalization lawsuit
- Summary: Meta Platforms stock falls amid support pressure and ongoing recapitalization lawsuit
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQTUVJejJ3UkFON2U3SzZsb1lxSFNEMS03MkN5NlRvQ3Y1TnVOeG0ySk1fMFR4ektxeDBGLVNvLXVWY1RROU10VVV4eUV4VzNUR01IVkxXYV83Y1RreW5aZU5JbkxUb3ZrelBCMmdTUXJpRFh1MkdBbVF3blVUWTdvMzlyOGFDOVRWaXZ6b0hORzNaeE96?oc=5>

### JPMorgan cuts Meta stock price target on 2027 spending concerns
- Summary: JPMorgan lowers price target due to 2027 spending worries.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxNbG11c2VCMzN0eFo5ZHRBN0doX1lqYWc4MlRVZDBCQTFsX2VGdjkxT0JwWW9PWURXaHRnNEhRT2ZCN3hwdHRXaFh2SDllLTNzMW5LalF5dHlNRk5jb0ZuLWxkOEo1akNDMFU2LUpCU08xemV0WkZTVC1meERzLVVZRDdJMnA2THp0WnJsWE8xVGEzZHNjQS14Y0NreEV5Nmo4QTlOOTVSbmpaWENHWlFzMVNWWHBrSXk3U0JGSWVpWTA?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **META** | **20.81** | **5.72** | **13.70** | **26.10** | **1,559,025,942,528.00 USD** | **-3.81** |
| GOOGL | 14.26 | 5.09 | 17.58 | 24.70 | 3,357,491,331,072.00 USD | -15.34 |
| SNAP | N/A | 3.88 | 53.11 | 14.30 | 8,701,946,880.00 USD | -34.03 |
| PINS | 82.12 | 3.64 | 37.25 | 11.90 | 11,303,838,720.00 USD | -22.74 |

Peers fetched as_of: 2026-11-25; META reuses existing data (market data as_of: 2026-11-25); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-25

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

- https://news.google.com/rss/articles/CBMingFBVV95cUxQOGFiY1Nic3hFMjIxNWxSb1VGQXd2Q0x5VWxQLWJHUE9zTzIxOTNySGVlZVR1Q2tLWE1SVjhDMmlEb0wxQ3hXaHd5S0hiclNxNENTUjg3aXBIaUM0QS1wb0RFTEdkaVVnN0Rya2ZxOXRHQzhzVGhlbkRkQWtJLXlXN0k0ZWhlNnhndnplMFMxWVVXQzZCR1NZaFA3LURTQQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOSXhId0NFZWluMWd5TWo4Z01OVGsxTWRPT0hrRWdkczVSUUtxXzg2OFNnY0lpYnhOTmc1ODdxeW9wdWFtUU1SVFJuSGhabERLZkZha0JTNlFQSjFQMzlVMm5hQlM5ZDNoamNIbmIxWFQtUmRJek1PQnRtZlRER0VsdEIwS2pCMXRsUG1lZ1d1YmJBMU41VC1CMg?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxNYy1PUTRsNjA0REdicy0zYzZfLTZHbnV2ZGFXUDhSY3g5NHhqaEd1bWItZWpUY0toSV80QWh1bmtMX3NSaFJmQ09sY29sYUs5Njd3RHNHV0xQYXVRMHlfODc3dGZhcnVLT21fajl2QkwxZllZa3hVQkdtM1RzNE4xUEctYUQzdmts?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOdjEyTVRlcWZuVV9PRHBXVFFkUGRqem8zWVh6R2tqb0lfb19HR1BpaTgtZ185eGFKWXpsakNra2dwMWNtU25sYlNaTjJOSjYxRS1YbERkZ0I4UHlEa0JJUHBLOVlOd0hoWTJpOGF1U25pTGVldl9pbzhfclFacXE1T056SXVqbUdsTnV0c2k2RHJDU0t6dTlLLXlTU1NFZw?oc=5
- https://news.google.com/rss/articles/CBMiigJBVV95cUxNQy1aZXN6YnZtWGtxbjFadjliTk5FWG9rbkN5WWRMT0pSLXFZQnlhbW5Fd0FueVFvbno0OFZqMUtvRkFvQjlDUEVqal8zTzltamJPTm9NQXFCYkVweng3SEpYLWwzZGo2bGJGcXZpb1gtYXpqQjRVbUtIZFpISG5maVpxR1YzYmJYck91cG5jTFlsNHE0NWV1TUJHY2wyMF9mdk5IS2ZIZEFQTEQ0ZGpKaElMVFRhdGl5Z0hLcHFqN0xwSVNrX0NsUkt6NnRIWFNvTWRYWVhLb0ViOWFWaTM5UHhsS01yeWdmNDZBUlNwZ25fUGhLbUtDbjN0SDNYN1dFOXd1aW4tR0hhZw?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNSk9fRUN4RmFOTWdZSWVDRzFCTVU3akVWVldXOFhSWkhvdm5WUlFQczhPc2h0b1JHSHM4WU0xZk1FYkdkSmJ4Y3pXVTZ0UVZOV1JKVF9TcGFmbFU5VDJwTUF3QTJGN3pZbHVTQl9PVFVzTlVKR2lRSnhfY1UteTU0UzI5WjI3cG1vQW1uVloxcHZpdw?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxPMFdMWm1xOWhlXzdJbW13djlYT3VEWWhKOWp3WnR1Z25Oci1UN2RXZ1Z0SXlld2ZyYTE4UHBnTmM4Rm84N3Nrcm80MTU3bkdBbVNNaHFYLVRtMmgyM213b0tuV0pEcjUxY1pnWDhaVkdLeXBSMk82ejlwYUpGZmplNHVabnAtZ2sxTFVlaFZKRjJRb3VpbVlwQVMwcXBnN1h6S2RJam1VWFgwMXlWckFza2lpSVp2TnNCNWZOSEhVc2Q5em1VMWhvSw?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxOZGVYd29wLVlqNlpUTFJnZlkyZGpGRE1KVjlBR2tjLTJBN1N4QjliQWVVcGpabXFrdXFDcTVjUTFOVFpBZkQ4ZmhqZUxhcXFYQjRUZVFoUVZUNk5lT3JyVnJ2Sm9WWGtFWmE1QVlJcGRmOE56Mll0Z1FBSGJMdnYtc2lHMUdZXzk0YnkwRmNWMFVJbmJFaW5UOG45VjdXMmxnQ25JY2JKaE1pSnFqWloxV0pidHdEZlZGT1lF?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxQNURCWEpIbFQ1TVVkdzRSWGxQUWRPS2pyRmxYdXRvT2FTNDVCMUJ5SG9vaEZ2YXh5cS1EWEEtQnFQdE9Lb2xUdnAzRlZzUU5FOWxfLXpnZFJwSjhOY2x4MHU5endNWHNuQjZjc3l0M24yZFNzSkFUNUtOMFZhdlNHbllNWVhsbXlfZ2VfbUp3Q25iTWtEeWI5cmxDU1FhUG9LQ2tSbHFDbkhxQ3lzbWt4NElsUGtablh6R1g1OG5SUExhWjBET1dUM25xSkhpdUhFTzdodXhn?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPZDhvWjk4QWhGdVJpM1JuQVRYbkc5Z0tpNGxSZWgzLWdPRE5LaHpvMW1lVV9VSFljNXlUaTVVYk0xZEtvamZDVnR4RERGOVdoQlJSdjhhVHgzLWNIOTNNZ1JGWkI0NEtVcHUxbW8xYUVyMFozREVDZXZXVWVtS0lDa3piQ3FUa29kQVg3TlZrdVBEWHpHb3F1MGVDZWRNMlNEZlBFdWhR?oc=5
- https://news.google.com/rss/articles/CBMihgFBVV95cUxPVWRndzl1YkJMdDh6MEZLMHlKVzhNYXdJQTdpZnRtNXo5dXRyNU1FdjZjcGhMVWgyTFdmelBMbVU3WExiM0lXZjhBWWI0Tl9VMFN5VnVyVmRyeUp5S1RtZWlSZndZT09EVXRTZnNuazk0LXloYTQ4cm1OWms1UUNqNEFmQ1pHZw?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxONG1USC01dW5MV05MYS0tLU45d2lZeUJBc0Z1LWVxSHBtMk9SUEhvN2I0WDBBMG90bWpFQ1dNbmlKUWxzN2xoTnZaa2dMakRsZkxVZWRxdXdmT3pfRXpDUUtQSHFUdXFZQnhDNjNtYUxCa3UwRlRRZ3F6cGZMdVN2bXlUbTVuaTUwWFhuMk9tcE1rcGFVYkE?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxOVzNJQmsyN0VLTFFUNmNBS2VXYzhrdnFFa2J5Mi0zSGxCaHFFWlRRZEhZWklGT3c4SGVlcmhFY2RkNkNTbHYxRUZnem1sRHU3Wkp2c2s0dzRiRjlHaUFDNkdrWC1QQlZpeXVkYkZYeDkxRUtUVnNaazVubFNNZXlrdzE2MTBYVWZMbmc?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQVkpCOFRMbmZiUk9ZVUtmbXpuSnR4OGZ2aDBlRzdfSGc0WlB2UE52TTQyYl9mdTZyZnFjYUdVRGpqaS1rSE4yVUxERHZURVVkdTFQTHpub3Z2bGN1Nmg5d3kwbDZ6b0QzVDd6alJVR2dLYklIaGRxRGxRYV8zcENnaVctRzZqaUZfS0RGbjAtQmZYSUl1MjJSMXJZTXhsZm9fcUxv?oc=5
- https://news.google.com/rss/articles/CBMigAFBVV95cUxNYk5tSmtVOHlocG5sQXpiLXBUU08xQjVVQXJQRE8xU0xxM2gwWk1MNG5KYmFfWU11RFdSaF9VOGRQTTZ5V1V5UmNKUDdaUWxlaGFmOWxrcjBONC03eDNKQmVQdHp1U3drNi1vaU9PUkx1UWwyUFpfYm4yenFvZGwyRw?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNT0RTTDc3WmVkaEVJLUtiT1BuSTVWZnRDY0xqbHpTaGdONHhzUHpaZTRmQzhNcFZRdVBoQnBsRFZrRUFUbGZkZ1lnbjAxVEtZdkNGNWwyWXRrWl9ETEcybXNMaFJVZmloWDRxSGYzMVZTY3lTclp5cW1HTm5PSGQzTm5zNk1XdHVvc3pR?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQOUk1bWJIcDlxSUs5b3RqeFdlbFVLckdqeUdwLVZkMnQ4WDJUNEdTWm0yMWtQckFubzZOR0tCVUU3dnFKOF9WbmotZl9wTWFuNzlfOVFPYzZHUlVSQzFfcVY0ZDJId3ptQVVXaFpPVV9HT2g3YVFCY2Z3SUdIU2NCeWtuRzBfbDEyYWs1VW0wQ002RXYyR3Jrb3hHOA?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQTUVJejJ3UkFON2U3SzZsb1lxSFNEMS03MkN5NlRvQ3Y1TnVOeG0ySk1fMFR4ektxeDBGLVNvLXVWY1RROU10VVV4eUV4VzNUR01IVkxXYV83Y1RreW5aZU5JbkxUb3ZrelBCMmdTUXJpRFh1MkdBbVF3blVUWTdvMzlyOGFDOVRWaXZ6b0hORzNaeE96?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxNbG11c2VCMzN0eFo5ZHRBN0doX1lqYWc4MlRVZDBCQTFsX2VGdjkxT0JwWW9PWURXaHRnNEhRT2ZCN3hwdHRXaFh2SDllLTNzMW5LalF5dHlNRk5jb0ZuLWxkOEo1akNDMFU2LUpCU08xemV0WkZTVC1meERzLVVZRDdJMnA2THp0WnJsWE8xVGEzZHNjQS14Y0NreEV5Nmo4QTlOOTVSbmpaWENHWlFzMVNWWHBrSXk3U0JGSWVpWTA?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
