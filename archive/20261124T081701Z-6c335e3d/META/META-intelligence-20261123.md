# META Intelligence Report

- ticker: **META**
- Report as_of: **2026-11-23**
- Market data as_of: **2026-11-23**
- Quant sources: https://finance.yahoo.com/quote/META/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/META/key-statistics/
- AI analysis snapshot as_of: **2026-11-23**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-24T08:40:33.754444+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 1, 'ai': 18, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261123T053847Z-45053549/META** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **6**; {'directional_claim_without_event_type': 5, 'negative_sentiment_in_tailwinds': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 12 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 41.67%; oldest publication 2026-11-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 597.6000 |
| Return 1D (%) | 6.5544 |
| Return 1W (%) | -4.5992 |
| Return 1M (%) | -7.0057 |
| Return YTD (%) | -9.2338 |
| Return 1Y (%) | 0.9048 |
| Annualized volatility (%) | 42.7237 |
| Beta vs SPY | 1.4043 |
| Max drawdown (%) | -28.7332 |
| Sharpe (rf=0) | 0.1591 |
| Downside deviation (rf=0, %) | 28.3783 |
| Sortino (rf=0) | 0.2395 |
| Historical VaR 95% (1D, %) | 3.9010 |
| Historical ES 95% (1D, %) | 5.8049 |
| Correlation vs SPY | 0.4922 |
| Tracking error vs SPY (%) | 37.6792 |
| P/E (trailing) | 20.39 |
| P/B | 5.61 |
| EV/EBITDA | 13.43 |
| Revenue growth (%) | 26.10 |
| Forward P/E (estimate) | 16.75 |
| Gross margin (%) | 81.03 |
| Operating margin (%) | 37.78 |
| Return on equity (%) | 32.26 |
| Free cash flow yield (%) | 1.10 |
| MA50 | 675.2511 |
| Close vs MA50 (%) | -11.4996 |
| MA200 | 627.5817 |
| Close vs MA200 (%) | -4.7773 |
| RSI (14, Wilder) | 41.7534 |
| MACD (12,26) | -19.6679 |
| MACD signal (9) | -17.4339 |
| MACD histogram | -2.2340 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'META': 288, 'SPY': 288}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 597.6000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 6.5544 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -4.5992 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -7.0057 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -9.2338 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 0.9048 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 42.7237 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 28.3783 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.2395 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.9010 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.8049 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4922 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.6792 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.4043 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.7332 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1591 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.7511 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 81.0340 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 37.7770 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 32.2640 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.1029 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 20.3889 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 41.7534 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -2.2340 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -11.4996 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -4.7773 -> Slightly below the moving-average trend level.

## TAILWINDS

### Here’s What Reinforcing Meta Platforms (META) New Monetization Opportunities
- Summary: Meta announces new monetization strategies to boost revenue.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxObUh6T2dfRFFGWldXUTFaaVJ4TE5pMF9CSGxGY0RfSGZWcXRPNFVmVUxGYWRlNlBEeTZzR3pydGVpc2FqdzlKTjJtaTh3VWU1V042VVRYY1pwRkJKNHVkS29sOUF2NWl3bWlCaFFleU5XVC1nN1V3bEpHN0I0WDFmN2hTMEJHdGM3ZFloTHBNbnBXSzE2VElwaUM4VGFQeWp5cVNFNHBPMjl6TkZGZHc?oc=5>

### Navigating Meta Platforms’ (META) Journey from July Dip to New 52-Week High
- Summary: Meta’s stock climbs to a new 52‑week high after a July dip.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOU0JKZmRKWEdaRGhjdElFQ3dKUVhqVW1NT0JwMGFLYkdTaVI4SUx3cWU4VFd2M1huQnlmNmxfWUczYTFIT3M2WU81cG03aUt3SVVIRU5FV0dnaTBPQTdDMmNRM2M3UGlQem13MUVIbUVwQkdxUjBGUFFkbFZ3UGZkOWdtZWlsdzdyYkZlVEhvXzN3ZW53RWlFbFdYZFBBcU1ESE1GNTRR?oc=5>

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

### If You Invested $1000 In Meta Platforms Stock 10 Years Ago, You Would Have This Much Today
- Summary: Illustrates Meta's long-term growth for $1,000 investment.
- Date: 2026-11-23 | Impact: low | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxOVmZDQVN3R3VsVy0xQlJHSW14OGlMWFlLLWhVV3A5bVdTZU9wQldkVG5rdUtEcEdNYWM5VElQWXdJeFdvdHU1d3FPemVfeE5yT01TaWVvalN2QnZ6a1lFaWlySzJvUnJhMTdLMi1WOWlTWktXRm51NlFqWE9NcG1RcFliTHdCWmhPeXpnS2hLd0VOcUEwdHVVV2xvS3NfRW1GYVMtR0J0UVpFcmtiZ3Y4MXFFN2M0TVAxVkJwLTFGbkxCU3M?oc=5>

## HEADWINDS

### Meta’s (META) AI Spending Spree Looks Risky, but There’s More to the Story
- Summary: Meta’s heavy AI spend raises risk concerns, but potential upside remains.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQQm1Od0F5OXJYZ0Q4OWI5d1Z0X1FrQU5KX2hPeFotZTZfUFN5cUY5X0dHQWZFamNtejIwSG40c20xdWJUcUd1ZGdWVWhqVGE1bGxkZVpCR3NZX1FaX2ZHdXd0MFNJV21pVS1xN2l6bC1HUl9ETWZZa1JNcFVkTzlPME4zQWNGRmRiaktpVDRKRWNDaGNMNlE?oc=5>

### Meta Platforms (META) Down 8.1% Since Last Earnings Report: Can It Rebound?
- Summary: Meta's share price fell 8.1% after earnings, raising concerns about a rebound.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMigAFBVV95cUxNYk5tSmtVOHlocG5sQXpiLXBUU08xQjVVQXJQRE8xU0xxM2gwWk1MNG5KYmFfWU11RFdSaF9VOGRQTTZ5V1V5UmNKUDdaUWxlaGFmOWxrcjBONC03eDNKQmVQdHp1U3drNi1vaU9PUkx1UWwyUFpfYm4yenFvZGwyRw?oc=5>

### Meta Platforms faces rising AI costs and profitability doubts: Can META avoid further losses?
- Summary: Rising AI expenses and profit doubts threaten Meta's financial outlook.
- Date: 2026-11-23 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxOQVRHSzlYbE9pZGFzU1JKNThnOTBSejJESFc2a0UwVUpkeWpjWTZYYVJ4TmNXWGczYzRqblRueHlVTG1pbkVydFhYeGhTTE84TVowUklmUnNKclN2UzBVQlBiNkQ5VmZYdTM5Tkx5OWItOW9hWUhFRDFKQ0Z5Y29TSjB2djhjdmdwSFQwNXRtMA?oc=5>

## CATALYSTS

### George Soros Raised His Meta (META) Stake by 596%. Then the Stock Fell
- Summary: George Soros increased his Meta stake by 596%, triggering a stock decline. The move signals significant shareholder activity but its long-term impact remains uncertain.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOMmQycHY2WjJ6V3FuT0FNb1R1SktTQmVUQlZpeVloeXdsZl8ycEdfcmtrcU8teGExbndnVFJkTnZUSWdMdGx5b1lOVFZCdFBibmwtdWw2ZDJIM1hyV3FVSU1UTGo3UnlLcHhxU0VXVDlBU0JrdnpyVDdSNjh3Wl9RWUxza2c4a2FIeW04dFFEWE1HYVRRb0FWRVNn?oc=5>

### Meta Platforms (META) Rethinks 2030 Climate Goals After 45% AI Emissions Jump
- Summary: Meta revises 2030 climate targets following AI emissions increase.
- Date: 2026-11-21 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPam9WWTlDT0JsdTFGNWVPMmtWeVMyLVhpQ2haZXQydG1yQUU3YVloaDBsNTZvNmlqOFlyVFJkTUxtb1MxUW0yMzRINEdGU0tvVkVBNW11N0pwMnZMUGxYZjl0aTN0bEN6UmFGX2V1MFRfU205WHJTalBvd1RoUFRwbnNCRnRibEstcUxGbkJPNWZHc3ROeHNfa0JyRVhYdw?oc=5>

### Mark Zuckerberg’s Meta Platforms Is Pouring Up to $145 Billion Into AI This Year. Investors Should Watch This 1 Number.
- Summary: Meta plans to invest $145B in AI this year, signaling strong commitment to AI development.
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi9AFBVV95cUxPTTdpZEszbEFkamptNXBGc1c2NF9fVnNJZ0tMUUI0ek94cFNpcy1sOF9hVWFRRFU3UzdfNDVGMElzengtRlczN0Z5bWozb1hpUXhJaUJYN3o3M21LWnZ5aDdqSURURnJxdC05a0ZpdWdFeXQybmJYTEtfMXA1SGotYVIwQXBpbW1ZdzZkZVVXX0haMklpbC1sR3EtWFQ4cDl1WVNiYmhnMkY5amFjWUVqS3EzclB1cVROSHhrNEtJZzNvZ1hGNjlIY0lHd3plR1l2U1RTNGJmUVp5eVRvc2ZYQ3UwOXQybGR0LUpzbnFVeVhVUHRG?oc=5>

### How to Play META Stock as Meta Platforms Tests a New Prediction Markets App
- Summary: Meta Platforms is testing a new prediction markets application, potentially expanding its product offerings.
- Date: 2026-11-18 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQOUk1bWJIcDlxSUs5b3RqeFdlbFVLckdqeUdwLVZkMnQ4WDJUNEdTWm0yMWtQckFubzZOR0tCVUU3dnFKOF9WbmotZl9wTWFuNzlfOVFPYzZHUlVSQzFfcVY0ZDJId3ptQVVXaFpPVV9HT2g3YVFCY2Z3SUdIU2NCeWtuRzBfbDEyYWs1VW0wQ002RXYyR3Jrb3hHOA?oc=5>

### George Soros, Cathie Wood and 45 Other Big Funds Bought Meta Last Quarter. It’s Down 18% Since. Time to Buy?
- Summary: Major funds purchased Meta shares last quarter, signaling confidence.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPQ1FYbHVoSDE0bWpYSlcyYzhsMjQ1a0RDNHhpVU5GbUdrb0xFWmp1b1V2RUsxdE15ZFFXNGczTHhnUzZPQklmQjNTdHpaRXFveFdQVE5NbXRqNE82U1hpVVRxOGd1T3lVTUc5cE1ZSHNnaEEzWjQwWlBHZHNkYVhuRnB5V0pBVWNhcWZDRmdaTDIteWVaYWJZ?oc=5>

### Daniel Loeb's Meta Stock Bet Stands Out as Tiger Global Trims
- Summary: Daniel Loeb increased holdings while Tiger Global reduced its stake.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNeXFXazFEX3JKcGdMbTNRX3BlYlJWaWhkQk43dzlvLUEtR0N3RDZmYVNDM0JTQjlCd1ZCWDhuODlsaEMxUW9CWjV2bzY0WjRGVTkzRVpab2QxM19HMGtJQkl2Y2tQNlJpQU1mb082MDlsbm1LR1BNdnB6SXUzbnJLcXVNcEhBOXUtM0t6aTU5REdtRzFscGlr?oc=5>

## RISKS

### Meta Platforms Stocks Rebound 6.13% After 12.6% Weekly Slide on Class C Lawsuit
- Summary: Meta Platforms Stocks Rebound 6.13% After 12.6% Weekly Slide on Class C Lawsuit
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxOM0NKdE1fWGlxRGVFQlNxMWhpVEQ1UlhjcEpyd2RUam9EMW51SEhpaXNmcmgtSHV0NlBSRjI2d1lFUXFHVlA3QWh0NlM2TDFfbEIzNEEwc0JVckNOQXZyY0xmMk9VdmZYTi04M3hkdlM4Y0RPMF9HbDhPTXhaelBuMjk1a1pIMC1ZTGxiUXJaQ2xhX2g1TzFGMEJYVktRZWJxUUlEc3c5eThTZ00ybTRhQW1kTVV0UXpMY0FHSE9sSjB2UEpUSjByOFVkTlRxZExiRWt3?oc=5>

### Morgan Stanley cuts Meta stock price target on higher cloud spending outlook
- Summary: Morgan Stanley lowered Meta’s price target citing increased cloud spending, indicating potential valuation concerns.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxNdlEzbXR4dEtINnF4TFVJS1gwRXFSa1VXWXlrTW51cmEyYkkzT1hKVW9TU25qdmZlbnVXbXhERUJ1Qmc0TjFWaVRlQmtEcUkzdFdFVTRkMEZSOGtJYTgtQlNWekg1MkV3dlFjc0NOTGRoT1BSUFJ5TXN4MldqSEZYVEV5UlA4eWdiR0VYbkxIMFJnYWVFTEplcUV2bzItVmhwUF9TY1lFU1M0SXZpYkJWMVYxcElYRXl6WlM1eHdyamdwRjNvSHFndTQyWXlZVG83VlE?oc=5>

### Meta Platforms Pauses Class C Share Issuance Amid Delaware Litigation
- Summary: Meta halts Class C share issuance due to Delaware litigation, potentially affecting capital structure and investor confidence.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxNQ3o0VmJhMm9SbUxpYUlXb3JKRFNxbnZReERTNUdNYWRwMmQyaUI5MWVnVDVIZ0xNQnVwQTY1Q2ludlNMWUhMMDVRcmRpUGN5WXlEdEtLQ0tCakwtcUdKTFF3UFNlUDloLU54OVBPcnpZcnE2eVZkajFua2pHaXB2d01LTkFKenNzMElMa1pySUN1QXNmNTBsWXhaRC1RQV9Mc1VZVTlJdVNZYWltSWU2WDZ3RVpPNEItc21oNjRHVHBhck9UWHRBNnhFQQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **META** | **20.39** | **5.61** | **13.43** | **26.10** | **1,527,609,688,064.00 USD** | **0.90** |
| GOOGL | 14.73 | 5.26 | 18.17 | 24.70 | 3,468,137,332,736.00 USD | -5.62 |
| SNAP | N/A | 3.79 | 52.01 | 14.30 | 8,494,757,888.00 USD | -36.02 |
| PINS | 70.42 | 3.12 | 31.80 | 11.90 | 9,692,281,856.00 USD | -32.29 |

Peers fetched as_of: 2026-11-23; META reuses existing data (market data as_of: 2026-11-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

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
- Filing date: 2026-10-22
- Revenue (latest available single quarter): 13,727,000,000.00 USD; period 2018-07-01/2018-09-30; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 9,860,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMirgFBVV95cUxObUh6T2dfRFFGWldXUTFaaVJ4TE5pMF9CSGxGY0RfSGZWcXRPNFVmVUxGYWRlNlBEeTZzR3pydGVpc2FqdzlKTjJtaTh3VWU1V042VVRYY1pwRkJKNHVkS29sOUF2NWl3bWlCaFFleU5XVC1nN1V3bEpHN0I0WDFmN2hTMEJHdGM3ZFloTHBNbnBXSzE2VElwaUM4VGFQeWp5cVNFNHBPMjl6TkZGZHc?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOU0JKZmRKWEdaRGhjdElFQ3dKUVhqVW1NT0JwMGFLYkdTaVI4SUx3cWU4VFd2M1huQnlmNmxfWUczYTFIT3M2WU81cG03aUt3SVVIRU5FV0dnaTBPQTdDMmNRM2M3UGlQem13MUVIbUVwQkdxUjBGUFFkbFZ3UGZkOWdtZWlsdzdyYkZlVEhvXzN3ZW53RWlFbFdYZFBBcU1ESE1GNTRR?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxNYy1PUTRsNjA0REdicy0zYzZfLTZHbnV2ZGFXUDhSY3g5NHhqaEd1bWItZWpUY0toSV80QWh1bmtMX3NSaFJmQ09sY29sYUs5Njd3RHNHV0xQYXVRMHlfODc3dGZhcnVLT21fajl2QkwxZllZa3hVQkdtM1RzNE4xUEctYUQzdmts?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOSXhId0NFZWluMWd5TWo4Z01OVGsxTWRPT0hrRWdkczVSUUtxXzg2OFNnY0lpYnhOTmc1ODdxeW9wdWFtUU1SVFJuSGhabERLZkZha0JTNlFQSjFQMzlVMm5hQlM5ZDNoamNIbmIxWFQtUmRJek1PQnRtZlRER0VsdEIwS2pCMXRsUG1lZ1d1YmJBMU41VC1CMg?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQOGFiY1Nic3hFMjIxNWxSb1VGQXd2Q0x5VWxQLWJHUE9zTzIxOTNySGVlZVR1Q2tLWE1SVjhDMmlEb0wxQ3hXaHd5S0hiclNxNENTUjg3aXBIaUM0QS1wb0RFTEdkaVVnN0Rya2ZxOXRHQzhzVGhlbkRkQWtJLXlXN0k0ZWhlNnhndnplMFMxWVVXQzZCR1NZaFA3LURTQQ?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPQzNSUm1CYUdCcGRiaUNEWGdhdVJHamVydVFHZC1yVC1CMnBzRXdkQ01uX3VpTnM4THV5T1hBSGdPQXFtZFpQdDd4c1A3WjlsdmMzRU9BMW5WY0I3RUFQQzVOaUh3ckxLZFhUdUR4SFJiOS1YeUtTNkRlTjJzUVZJYnZEODVnNERXZmpsVHUwWGFhdGpiaEdwRnJMUHpGbTZOSUFvMzR3?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxOVmZDQVN3R3VsVy0xQlJHSW14OGlMWFlLLWhVV3A5bVdTZU9wQldkVG5rdUtEcEdNYWM5VElQWXdJeFdvdHU1d3FPemVfeE5yT01TaWVvalN2QnZ6a1lFaWlySzJvUnJhMTdLMi1WOWlTWktXRm51NlFqWE9NcG1RcFliTHdCWmhPeXpnS2hLd0VOcUEwdHVVV2xvS3NfRW1GYVMtR0J0UVpFcmtiZ3Y4MXFFN2M0TVAxVkJwLTFGbkxCU3M?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQQm1Od0F5OXJYZ0Q4OWI5d1Z0X1FrQU5KX2hPeFotZTZfUFN5cUY5X0dHQWZFamNtejIwSG40c20xdWJUcUd1ZGdWVWhqVGE1bGxkZVpCR3NZX1FaX2ZHdXd0MFNJV21pVS1xN2l6bC1HUl9ETWZZa1JNcFVkTzlPME4zQWNGRmRiaktpVDRKRWNDaGNMNlE?oc=5
- https://news.google.com/rss/articles/CBMigAFBVV95cUxNYk5tSmtVOHlocG5sQXpiLXBUU08xQjVVQXJQRE8xU0xxM2gwWk1MNG5KYmFfWU11RFdSaF9VOGRQTTZ5V1V5UmNKUDdaUWxlaGFmOWxrcjBONC03eDNKQmVQdHp1U3drNi1vaU9PUkx1UWwyUFpfYm4yenFvZGwyRw?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxOQVRHSzlYbE9pZGFzU1JKNThnOTBSejJESFc2a0UwVUpkeWpjWTZYYVJ4TmNXWGczYzRqblRueHlVTG1pbkVydFhYeGhTTE84TVowUklmUnNKclN2UzBVQlBiNkQ5VmZYdTM5Tkx5OWItOW9hWUhFRDFKQ0Z5Y29TSjB2djhjdmdwSFQwNXRtMA?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOMmQycHY2WjJ6V3FuT0FNb1R1SktTQmVUQlZpeVloeXdsZl8ycEdfcmtrcU8teGExbndnVFJkTnZUSWdMdGx5b1lOVFZCdFBibmwtdWw2ZDJIM1hyV3FVSU1UTGo3UnlLcHhxU0VXVDlBU0JrdnpyVDdSNjh3Wl9RWUxza2c4a2FIeW04dFFEWE1HYVRRb0FWRVNn?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPam9WWTlDT0JsdTFGNWVPMmtWeVMyLVhpQ2haZXQydG1yQUU3YVloaDBsNTZvNmlqOFlyVFJkTUxtb1MxUW0yMzRINEdGU0tvVkVBNW11N0pwMnZMUGxYZjl0aTN0bEN6UmFGX2V1MFRfU205WHJTalBvd1RoUFRwbnNCRnRibEstcUxGbkJPNWZHc3ROeHNfa0JyRVhYdw?oc=5
- https://news.google.com/rss/articles/CBMi9AFBVV95cUxPTTdpZEszbEFkamptNXBGc1c2NF9fVnNJZ0tMUUI0ek94cFNpcy1sOF9hVWFRRFU3UzdfNDVGMElzengtRlczN0Z5bWozb1hpUXhJaUJYN3o3M21LWnZ5aDdqSURURnJxdC05a0ZpdWdFeXQybmJYTEtfMXA1SGotYVIwQXBpbW1ZdzZkZVVXX0haMklpbC1sR3EtWFQ4cDl1WVNiYmhnMkY5amFjWUVqS3EzclB1cVROSHhrNEtJZzNvZ1hGNjlIY0lHd3plR1l2U1RTNGJmUVp5eVRvc2ZYQ3UwOXQybGR0LUpzbnFVeVhVUHRG?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQOUk1bWJIcDlxSUs5b3RqeFdlbFVLckdqeUdwLVZkMnQ4WDJUNEdTWm0yMWtQckFubzZOR0tCVUU3dnFKOF9WbmotZl9wTWFuNzlfOVFPYzZHUlVSQzFfcVY0ZDJId3ptQVVXaFpPVV9HT2g3YVFCY2Z3SUdIU2NCeWtuRzBfbDEyYWs1VW0wQ002RXYyR3Jrb3hHOA?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPQ1FYbHVoSDE0bWpYSlcyYzhsMjQ1a0RDNHhpVU5GbUdrb0xFWmp1b1V2RUsxdE15ZFFXNGczTHhnUzZPQklmQjNTdHpaRXFveFdQVE5NbXRqNE82U1hpVVRxOGd1T3lVTUc5cE1ZSHNnaEEzWjQwWlBHZHNkYVhuRnB5V0pBVWNhcWZDRmdaTDIteWVaYWJZ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNeXFXazFEX3JKcGdMbTNRX3BlYlJWaWhkQk43dzlvLUEtR0N3RDZmYVNDM0JTQjlCd1ZCWDhuODlsaEMxUW9CWjV2bzY0WjRGVTkzRVpab2QxM19HMGtJQkl2Y2tQNlJpQU1mb082MDlsbm1LR1BNdnB6SXUzbnJLcXVNcEhBOXUtM0t6aTU5REdtRzFscGlr?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxOM0NKdE1fWGlxRGVFQlNxMWhpVEQ1UlhjcEpyd2RUam9EMW51SEhpaXNmcmgtSHV0NlBSRjI2d1lFUXFHVlA3QWh0NlM2TDFfbEIzNEEwc0JVckNOQXZyY0xmMk9VdmZYTi04M3hkdlM4Y0RPMF9HbDhPTXhaelBuMjk1a1pIMC1ZTGxiUXJaQ2xhX2g1TzFGMEJYVktRZWJxUUlEc3c5eThTZ00ybTRhQW1kTVV0UXpMY0FHSE9sSjB2UEpUSjByOFVkTlRxZExiRWt3?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxNdlEzbXR4dEtINnF4TFVJS1gwRXFSa1VXWXlrTW51cmEyYkkzT1hKVW9TU25qdmZlbnVXbXhERUJ1Qmc0TjFWaVRlQmtEcUkzdFdFVTRkMEZSOGtJYTgtQlNWekg1MkV3dlFjc0NOTGRoT1BSUFJ5TXN4MldqSEZYVEV5UlA4eWdiR0VYbkxIMFJnYWVFTEplcUV2bzItVmhwUF9TY1lFU1M0SXZpYkJWMVYxcElYRXl6WlM1eHdyamdwRjNvSHFndTQyWXlZVG83VlE?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxNQ3o0VmJhMm9SbUxpYUlXb3JKRFNxbnZReERTNUdNYWRwMmQyaUI5MWVnVDVIZ0xNQnVwQTY1Q2ludlNMWUhMMDVRcmRpUGN5WXlEdEtLQ0tCakwtcUdKTFF3UFNlUDloLU54OVBPcnpZcnE2eVZkajFua2pHaXB2d01LTkFKenNzMElMa1pySUN1QXNmNTBsWXhaRC1RQV9Mc1VZVTlJdVNZYWltSWU2WDZ3RVpPNEItc21oNjRHVHBhck9UWHRBNnhFQQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
