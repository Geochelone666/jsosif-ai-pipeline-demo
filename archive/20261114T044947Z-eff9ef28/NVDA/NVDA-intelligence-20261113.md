# NVDA Intelligence Report

- ticker: **NVDA**
- Report as_of: **2026-11-13**
- Market data as_of: **2026-11-13**
- Quant sources: https://finance.yahoo.com/quote/NVDA/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVDA/key-statistics/
- AI analysis snapshot as_of: **2026-11-13**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-14T04:49:55.458140+00:00**
- AI status: **Partial: 1 headline remains unclassified and excluded from research conclusions**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 8, 'ai': 13, 'unknown': 1, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261112T054014Z-6c47e7f9/NVDA** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 13 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 44.0%; oldest publication 2026-11-10

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 162.8500 |
| Return 1D (%) | -2.0097 |
| Return 1W (%) | -12.7465 |
| Return 1M (%) | -28.7371 |
| Return YTD (%) | -12.4766 |
| Return 1Y (%) | -12.6404 |
| Annualized volatility (%) | 38.6631 |
| Beta vs SPY | 1.7766 |
| Max drawdown (%) | -31.9303 |
| Sharpe (rf=0) | -0.1580 |
| Downside deviation (rf=0, %) | 27.7394 |
| Sortino (rf=0) | -0.2202 |
| Historical VaR 95% (1D, %) | 4.1931 |
| Historical ES 95% (1D, %) | 5.1243 |
| Correlation vs SPY | 0.6265 |
| Tracking error vs SPY (%) | 31.9417 |
| P/E (trailing) | 21.01 |
| P/B | 17.17 |
| EV/EBITDA | 19.38 |
| Revenue growth (%) | 105.90 |
| Forward P/E (estimate) | 10.27 |
| Gross margin (%) | 74.67 |
| Operating margin (%) | 65.21 |
| Return on equity (%) | 117.21 |
| Free cash flow yield (%) | 1.06 |
| MA50 | 214.6320 |
| Close vs MA50 (%) | -24.1259 |
| MA200 | 203.9202 |
| Close vs MA200 (%) | -20.1403 |
| RSI (14, Wilder) | 24.8596 |
| MACD (12,26) | -14.2249 |
| MACD signal (9) | -10.1006 |
| MACD histogram | -4.1243 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVDA': 282, 'SPY': 282}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 162.8500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.0097 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -12.7465 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -28.7371 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -12.4766 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -12.6404 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 38.6631 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 27.7394 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.2202 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.1931 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1243 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6265 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.9417 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.7766 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -31.9303 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.1580 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 10.2721 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.6740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 65.2140 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 117.2110 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.0632 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 21.0129 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 24.8596 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -4.1243 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -24.1259 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -20.1403 -> Clearly below the moving-average trend level.

## TAILWINDS

### Retail investors are buying Nvidia’s stock crash like never before — history urges patience
- Summary: Retail buying surge after crash, indicating confidence.
- Date: 2026-11-12 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3wFBVV95cUxQdlRYZU5hQlFBOFpaU25UaEN4NGg5aGVNcXE2SkdhN0JZajBfd25paFhOcGExckxEYzR5MmkxMmVhWjdqLTVHQTd5bnZqb20ybzhoNE1KWFUteXJIQnRPd2d1X2Vpc1pWLWFOMmJEcVFuTnIxTGtOQ1Y3X1ZXTkZiempmbHpwSDdORzl2TjVuTGFQZWdSZ2NjZVRJQVR6cDJhUjVYMUtLQjd2ZjBXZ0c2ckFXRWlrS2ZTRmUtRWk1WUhZbkZhUVlNTHBJcWNya1hUVXRpNmJFNHBvbjM5Wkl3?oc=5>

## HEADWINDS

### Nvidia stock slips as investors digest CEO exit, broader chip sell-off accelerates
- Summary: Nvidia stock slips as investors digest CEO exit, broader chip sell-off accelerates
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxPT1FhU3E0MEFkQjV4aHZ4WXk5cktoTzhKbE9Sd1ZKTS11dE5raks5bXA0dk5IOGZ1bzBfT2Y5LUluVTZENml5cnBxcVEyOWh6eU9UU0lIS3FNbmdxVnpvdVUyTkdRNlU0REJGYjhaQzhpZHlpWGV1U1pfRjFLVE5wb3h3NGxWbFJmSlRJNDktSENjNVVpUFlHbnNrcW1BMk9vN2NsNzFjQURkeUtGQXBrSWRsMzctNmRzWlhvSUJVQjk5aHZkeUNtYTh3?oc=5>

### NVDA Stock Price Forecast — Top Analysts Give Multiple Downgrades Ahead of November 17 Earnings amid CEO Jensen Huang Fiasco
- Summary: NVDA Stock Price Forecast — Top Analysts Give Multiple Downgrades Ahead of November 17 Earnings amid CEO Jensen Huang Fiasco
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQTzU2YmpfQXpJMHVJel9uQWFUc1NVa2tySzllZUdfbUVSeFFFcmQwZkNLNFFVQTNtQkc0QS1LQzVTcEd6N21qNjZqVzc1Y3BRcFFOWW5hX3hMeENBTG1pUFV5UDZ5RjR1ZUtZa29mNlRmRlVUMVNUNVZVTFZDS01xaVhBMzUtdlVIVHVObEZlOXcwaFZuWExrUTlR?oc=5>

### NVDA Stock Slides To Fresh 7-Month Low Amid CEO Turmoil: Ross Gerber Calls Selloff A Chance To Buy Shares At ‘Absurdly Low Price’
- Summary: NVDA Stock Slides To Fresh 7-Month Low Amid CEO Turmoil: Ross Gerber Calls Selloff A Chance To Buy Shares At ‘Absurdly Low Price’
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNdnhmZl90TXVGZmFxb3kzTThoajJldGNoTThOWDhzME9Md0M1VTdnWldSRHJZWXFES1NzWlA1b09xWUtHcmZUd0ctc1V0TzBkSUlFWS1pZVI4RXloeVcwMDRMT1RGRzQzTzMySHlBeC0yWThNNlQwTUx3VV8wMVNESVg2Z0RRTVJrLUpndVh5N3lJY25T?oc=5>

### NVDA Stock Set For Best Day In Over 2 Months – Baird Downgrades Shares, Flags Slower AI Spending, Jensen Huang Risk
- Summary: NVDA Stock Set For Best Day In Over 2 Months – Baird Downgrades Shares, Flags Slower AI Spending, Jensen Huang Risk
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxORkgwN3diRWtuWWpxMjBhMEtyblJOTGJzclZ0N0JfVExQaWpkLTVzQ0tJTHpVMkFOcHdNVlE4RlV3Z2N5ckI2V0dLM2ItM3l6a1hMRzVXQk5VWlZsb2JneVVFY1NnRmh4bEgya2tyTXFZeEpScDJVX2VoMm1QZWkzSTFiU3JzOHVjdFVyLW8yUm5IQQ?oc=5>

### Nvidia Shares Sink 8.61% Premarket - NVIDIA (NASDAQ:NVDA)
- Summary: Nvidia Shares Sink 8.61% Premarket - NVIDIA (NASDAQ:NVDA)
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxOZmhocjZQQUdLMl80X2VqVHRvVGxDaVZfWGZ5aXJCUkJucXFTQzJ0TjNMWTNoQXNUVzR0SU00ekxDVEtZWmFUWDhwV2p2a25ROGg4YzNwY0xiY19kb2xkazhQQnYtdVY3b2FXTXVLNl8yZ254OUVlNHNGeTRTVHZhWXJocU5Yck96UE9ZODVYOVZNc0xJU0JsLVMyZ2NCQnFIUjBFamtJSUhoY21heFRfT2ZR?oc=5>

### Nvidia closes below $4T market cap for first time since July 2025 in Huang fallout
- Summary: Market cap dips below $4T amid leadership fallout.
- Date: 2026-11-13 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxQeHRJRmZaWDY1TDNwelllbWd6OUZiV1NzaEllNG9aekhVYVVGWWhOREZuczlHQzJEZXFoeUotM2wwOW5ZTEJTOWlkb2JqSV82U2hmU01GeVhzYVlmZDZVYVFMZFo4UTNBenhOa0N4ejd0bkczZ0Nsa0I5YThHbk9iVGFkWlHSAYoBQVVfeXFMTlpCeWpuYTJhM2NHaUxJc2dkRlVSQUZ4TWxuUjh1QU1NOFE0WjJ2QUVlc0E1VWhjLUZZeGJGdEw1emRmWHM1aUNXSDdjWGRXMUhGLXJXMEpqaWlZSjUzTmY3b3lVTWhSTENiV0M0WjNZeGJTREpab09JczdLejZRTzh3SGNZWGxGVUZB?oc=5>

### Nvidia (NVDA) Stock: $170 Friday After Jensen Huang Resigns and Colette Kress Steps In, Bull $187, Bear $149
- Summary: Stock price at $170 after CEO resignation, with bullish and bearish targets.
- Date: 2026-11-13 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxNZUNUYzhuM0Zmak1YOWFyMEZoTnR3b2dsS3RZcDh2VEdoWUJXWWRrVEF4cXNpSHllV0NfTEwtWENQTXd0enNDWENQTlBZUUk4azBTb1hjVjBLVE5fVnYxdHlpdlRaeFpNbmtkQWdDaURqNXc5bVIwZFpWbGptSzVmVWd0cldoOXhSY29sUHVmZ1JDX2tyOXJKR2tiaV9qNWJEaVVEcGdYRFM3X0dEM18xRTd5T0xraTBn?oc=5>

## CATALYSTS

### NVDA Stock Alert: Why Baird Just Slashed Its Nvidia Price Target from $500 to $200
- Summary: NVDA Stock Alert: Why Baird Just Slashed Its Nvidia Price Target from $500 to $200
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxPVXNwX1BMQ2xudnlVbE5GQmJoZ1JZZnlpZncydE5BZXo0Y2tmOHlRdV9ybm9EbjlTcVAxSEhkYkprNlVLNW91OG5HQjFtLUJaVEFscXlqOVFZRGRQcklCTmQyQWZ4amlsQlFVeEdobXNYelUzWGNyZTRmWXU4dmFtSXB0bzliZFMzQzdLNmlIRFE0ZUdRakgwUjNFd2VHMVUzLTBaNVpjUTVFX013OGpiSjRqLV81VlpIMmo2Q3dveWw?oc=5>

### Nvidia (NVDA) Stock Gets Fair Value Trim As Analyst Views Turn More Divided
- Summary: Nvidia (NVDA) Stock Gets Fair Value Trim As Analyst Views Turn More Divided
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPRElTSFhVQUZmVlR1QXFPRko3NkRfbUMwdWRTdWxpcjBmenpxbnJja0ZEOFVQU19DZURySnM2NDZJc25wMFQtdV9jd21RYVNXT2tNaHl4eU9nSmw1TzhWTF9GdmhwMlFnMloxOC1hZEMwa3VtdG9WY1dRTVdpQXdvQlQ0NjJaakUtd0JzcUZ6OTRLRzNvU0I0?oc=5>

### NVDA Stock Rout: Another Analyst Slashes Rating, Beijing Warns US Against Tech Curbs
- Summary: NVDA Stock Rout: Another Analyst Slashes Rating, Beijing Warns US Against Tech Curbs
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQNVc4amE3bzV1cWF4SGlwOVd4UnNZVTZ6c09GZE42VDZiMGRkTXhiMDN6MS1lYzlfRzVHWlF2eVA4R0VlVlBBakREZ3hzSy1PVjBXWFdhSzEzbkVqdUtOc2tMUUN1eXJLNmhlNnJhSWE1Yk9PS2FhemlWalE2clE4aHB4T1NGcEJyeFVKNUdSbUY0UmMtMTh6aEIyR18?oc=5>

### 'Icarus' rise and fall': Analyst downgrades Nvidia stock amid Jensen Huang woes, highlights risks
- Summary: Analyst downgrade citing Jensen Huang concerns, indicating potential downside pressure.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi4wFBVV95cUxOUFJBOGQzQXE2NFkxd21JeE9YUml1MHdrVUo3c2wxRVhYal9YU1NPUllYR3Q0QUdMSG5iRFRGb3l4SE1iT2NWc2tLcXpUZktPMUs2SUdPSmRwWjR0ZVM4STdtNjNGbzhDX3FGNE9QYjR5M2o3NjdNTmRvNEo3S283Wk15Vk4zVnBQSlM3X09VR3lXb1RRN09GUkRCVTFnc1UzNXg5VlhqazV2WXhFdnNzSzJSaGc2cmRXYmtuRnhJYjB1QVY1RjhNTnlTRWd0ODItRjBHSjE1LWt4WWlxMHpTTzhBRQ?oc=5>

### Michael Burry Sees A ‘Mechanical Bid’ Under NVDA Stock – Even As He Questions Nvidia’s Succession Plan And Asia Sales
- Summary: Analyst Burry notes a mechanical bid and raises concerns about succession and sales.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQcnhfVE1scE5nTUJyNWhaYXZPMTA3bGlVVy1LY3RWZ0ltczdZNklGUHZicENiTU9PdkdMT0prcldrdUxpZXZCX3ZCbFo2ay1RWmxmNVNIeDBSQUtRczhFYVZzTVRaSDhkV2hiS1FYcGUxd05FWFd4dGNzWWRnNFVPd2VuRmxZaEhKOUppN0REa3l5V2NwZl9CRGFHSVA2bmc?oc=5>

### Here’s How Much Traders Expect Nvidia Stock to Move After Earnings Next Week
- Summary: Traders gauge potential price swings for Nvidia following upcoming earnings.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxNQVhIYXNZbFpjNVdYNUQ1VUdubkR5WmNvRlIxZGg0X1V2dWpiS1JBMXRxU1ZlRzVkaVNfZXZMV1Uza2o1SlFlRGdWMkt0dU9ia3VxNmNXb2RzM0NocHhReHlQVTJPbFBHYXpEc0NLcGRJQ2JjSjFEei1XRHdkc1ZfZ2dsQkxIZ2VFMG1WTnZvZGZ6Xzh3SnNOUmdOdjJSRUtqRWlYNEdOU1UtNUlqLXc?oc=5>

### Equities close lower as Nvidia drop outweighs energy gains
- Summary: Nvidia shares fell, dragging overall market lower.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQY01YWkJBY3Roa2hlWkVsbHhpcHplMm5NX09pWEJlMC1rWTY1ZDJoTUh0elc0WTZvdmpDOXJhS04tN2J5Y0N4NmZPdGk0aUhKdVZLT2RMSTk4S2EyZEJMYzY3WnpMMklfRjF3ZEJXZzU3d1VBTmlWS3Y1cllaYURseVQ4Nl93RFVLOXB4M1J6bnM1YVQ5QXBaSDZCOXEwUQ?oc=5>

### Nvidia: A House Of Cards (Rating Downgrade) (NASDAQ:NVDA)
- Summary: Analyst downgrades Nvidia, calling it a 'House of Cards'.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxPVkIwa3NOQkR0YlJNdlB6NUU5YzNkaklQOFJvcVcxVnY1M1dVdUVNT2hsUFV4cmo4bTNxbmtiZXl2VWtEUnVtWGdRZFB3bU1oWEVYckpac3J5SjBLZkFwWlRnX0ZfemJUQ2Z4cDFuOTEySU1RNkFidS1mR0hnNDBXOXlncWJ0dWlq?oc=5>

### Cantor Cuts Nvidia Target by $100: 'A Very Sad Day' - NVIDIA (NASDAQ:NVDA)
- Summary: Cantor lowers Nvidia price target by $100, labeling the day sad.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxNMVMtc1Y3eXhUNk5mRWs4LUlZTmNGUEp3NGRmRzEycDdaQ2hCbmN6WUJLZEx2MWozS3ZmQ3lHME83aTVseGNWaTUzeE9fckpMTklyaE1SVEhJelBDRDFVS2xseWJMdjlLc2dCWFdudGgyVzlFMHZnNUdCby1QdnZuSkhkeXR3S3ptSVc4WlM2OHNXTm1JbUJWRjZ3NGxwa3JESmNHaGx0VTF3dFFlSzQxR2pXU2drbzFCbkduNjNZOTNLZ2NYZE1kbHZ5eUc?oc=5>

### Jensen Huang Is Out at Nvidia. Where Does NVDA Stock Go From Here?
- Summary: Founder Jensen Huang resigns from Nvidia, raising uncertainty about future direction.
- Date: 2026-11-12 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNSm54cFIzY0lRUW93M3lxbXp3TERlTHd5ZmFwSTRTam94ZFJmTnRlUEFWWGhSYTNLbm5OVFR1MnZIU204ZW5femJoMHo4RkpiVngzR3hoZ3F4UHgyUWdlQmxPaW1idHFQLWFwZ3hjcGZfMG94bFNiVTUxXzJSaDR2aWRacnMyN3NfUUJyVEl6ZTRnUTZqSVFyTmtDM1ZROE0wNlE?oc=5>

### 'Nothing has changed': Why some Nvidia stock bulls aren't wavering after Jensen Huang ouster
- Summary: Analyst commentary on unchanged bullish stance post-ouster.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi4gFBVV95cUxPNElWbE1lOVJadXoxSXhxYy04M3B4ZG9PeWhIaW1lZE9maF91M3N1OXd6eFhSSDJZcVlkMm5oZFdoeDJiaVRqYnJBRVkzczJ0TG1kSjFVT0Y1dG5iV1JMS0NPTW9oeVNlYXZZS0haUThFQVNlcnhJbTlMTjAtZ1pQaFc5WDNhd1VDTFVqY1dDOF9NYlRhTE9xamFUdkpBVVo2MlIyOXJsYVdRYVNDV0RCTDRBS2dKRFc1YkR1Tnczc0VSbGNUX21pRTFsWUpDR0dNMmpLT2V4UmtheUs0WWs2YXRB?oc=5>

### NVDA Stock On Track To Hit Lowest Level In Over A Year: Dan Ives Values Nvidia At $225 Without Jensen Huang
- Summary: NVDA shares may fall to a new low, reflecting market concerns and a valuation drop to $225 per share.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPcFNTc21RYmNfVmRuQWJNRW0tc2tqbnFQY1c4R1pKUmw2QWY2WERYZVQ5WHNpejJhLXEwR0thQzYzaEppcWVlOUNua1ZGLW5SeW5NUE43M0dLSVp3MzhWMmVPM3dLZVowWXdkc1BGd3Vud3RBNm5KWlBIWm11Y0dycUo4c0RKSHJaRlRvdmtHcXplQ1JFTzBV?oc=5>

## RISKS

### Nvidia stock closes down over 4% after CEO Jensen Huang announces resignation
- Summary: Stock fell 4% following CEO resignation announcement.
- Date: 2026-11-12 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMigAFBVV95cUxQVFBOVnFZT1F2M3oteUktWm1qb29oLW5DLW9MZ2pBRzhEenlNZWFERC1NRXJlSV9saDN5MmNRZzdzQm0xQ0hWSzVpSktBSy00aDZlUTcyQzd2Vmlia1F1UTlEdE11anNMVE10RDNEVlc4cUlMcW5CRlpxaWFEbDh2Mg?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVDA** | **21.01** | **17.17** | **19.38** | **105.90** | **3,932,339,044,352.00 USD** | **-12.64** |
| AMD | 125.07 | 12.81 | 78.02 | 44.70 | 875,905,024,000.00 USD | 115.38 |
| AVGO | 44.32 | 16.62 | 32.38 | 85.50 | 1,656,497,373,184.00 USD | 2.83 |
| INTC | N/A | 2.76 | 17.24 | 20.90 | 317,092,888,576.00 USD | 66.14 |

Peers fetched as_of: 2026-11-13; NVDA reuses existing data (market data as_of: 2026-11-13); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-26
- Next expected earnings: 2026-11-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-13

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

- https://news.google.com/rss/articles/CBMi3wFBVV95cUxQdlRYZU5hQlFBOFpaU25UaEN4NGg5aGVNcXE2SkdhN0JZajBfd25paFhOcGExckxEYzR5MmkxMmVhWjdqLTVHQTd5bnZqb20ybzhoNE1KWFUteXJIQnRPd2d1X2Vpc1pWLWFOMmJEcVFuTnIxTGtOQ1Y3X1ZXTkZiempmbHpwSDdORzl2TjVuTGFQZWdSZ2NjZVRJQVR6cDJhUjVYMUtLQjd2ZjBXZ0c2ckFXRWlrS2ZTRmUtRWk1WUhZbkZhUVlNTHBJcWNya1hUVXRpNmJFNHBvbjM5Wkl3?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxPT1FhU3E0MEFkQjV4aHZ4WXk5cktoTzhKbE9Sd1ZKTS11dE5raks5bXA0dk5IOGZ1bzBfT2Y5LUluVTZENml5cnBxcVEyOWh6eU9UU0lIS3FNbmdxVnpvdVUyTkdRNlU0REJGYjhaQzhpZHlpWGV1U1pfRjFLVE5wb3h3NGxWbFJmSlRJNDktSENjNVVpUFlHbnNrcW1BMk9vN2NsNzFjQURkeUtGQXBrSWRsMzctNmRzWlhvSUJVQjk5aHZkeUNtYTh3?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQTzU2YmpfQXpJMHVJel9uQWFUc1NVa2tySzllZUdfbUVSeFFFcmQwZkNLNFFVQTNtQkc0QS1LQzVTcEd6N21qNjZqVzc1Y3BRcFFOWW5hX3hMeENBTG1pUFV5UDZ5RjR1ZUtZa29mNlRmRlVUMVNUNVZVTFZDS01xaVhBMzUtdlVIVHVObEZlOXcwaFZuWExrUTlR?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNdnhmZl90TXVGZmFxb3kzTThoajJldGNoTThOWDhzME9Md0M1VTdnWldSRHJZWXFES1NzWlA1b09xWUtHcmZUd0ctc1V0TzBkSUlFWS1pZVI4RXloeVcwMDRMT1RGRzQzTzMySHlBeC0yWThNNlQwTUx3VV8wMVNESVg2Z0RRTVJrLUpndVh5N3lJY25T?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxORkgwN3diRWtuWWpxMjBhMEtyblJOTGJzclZ0N0JfVExQaWpkLTVzQ0tJTHpVMkFOcHdNVlE4RlV3Z2N5ckI2V0dLM2ItM3l6a1hMRzVXQk5VWlZsb2JneVVFY1NnRmh4bEgya2tyTXFZeEpScDJVX2VoMm1QZWkzSTFiU3JzOHVjdFVyLW8yUm5IQQ?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxOZmhocjZQQUdLMl80X2VqVHRvVGxDaVZfWGZ5aXJCUkJucXFTQzJ0TjNMWTNoQXNUVzR0SU00ekxDVEtZWmFUWDhwV2p2a25ROGg4YzNwY0xiY19kb2xkazhQQnYtdVY3b2FXTXVLNl8yZ254OUVlNHNGeTRTVHZhWXJocU5Yck96UE9ZODVYOVZNc0xJU0JsLVMyZ2NCQnFIUjBFamtJSUhoY21heFRfT2ZR?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxQeHRJRmZaWDY1TDNwelllbWd6OUZiV1NzaEllNG9aekhVYVVGWWhOREZuczlHQzJEZXFoeUotM2wwOW5ZTEJTOWlkb2JqSV82U2hmU01GeVhzYVlmZDZVYVFMZFo4UTNBenhOa0N4ejd0bkczZ0Nsa0I5YThHbk9iVGFkWlHSAYoBQVVfeXFMTlpCeWpuYTJhM2NHaUxJc2dkRlVSQUZ4TWxuUjh1QU1NOFE0WjJ2QUVlc0E1VWhjLUZZeGJGdEw1emRmWHM1aUNXSDdjWGRXMUhGLXJXMEpqaWlZSjUzTmY3b3lVTWhSTENiV0M0WjNZeGJTREpab09JczdLejZRTzh3SGNZWGxGVUZB?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxNZUNUYzhuM0Zmak1YOWFyMEZoTnR3b2dsS3RZcDh2VEdoWUJXWWRrVEF4cXNpSHllV0NfTEwtWENQTXd0enNDWENQTlBZUUk4azBTb1hjVjBLVE5fVnYxdHlpdlRaeFpNbmtkQWdDaURqNXc5bVIwZFpWbGptSzVmVWd0cldoOXhSY29sUHVmZ1JDX2tyOXJKR2tiaV9qNWJEaVVEcGdYRFM3X0dEM18xRTd5T0xraTBn?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxPVXNwX1BMQ2xudnlVbE5GQmJoZ1JZZnlpZncydE5BZXo0Y2tmOHlRdV9ybm9EbjlTcVAxSEhkYkprNlVLNW91OG5HQjFtLUJaVEFscXlqOVFZRGRQcklCTmQyQWZ4amlsQlFVeEdobXNYelUzWGNyZTRmWXU4dmFtSXB0bzliZFMzQzdLNmlIRFE0ZUdRakgwUjNFd2VHMVUzLTBaNVpjUTVFX013OGpiSjRqLV81VlpIMmo2Q3dveWw?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPRElTSFhVQUZmVlR1QXFPRko3NkRfbUMwdWRTdWxpcjBmenpxbnJja0ZEOFVQU19DZURySnM2NDZJc25wMFQtdV9jd21RYVNXT2tNaHl4eU9nSmw1TzhWTF9GdmhwMlFnMloxOC1hZEMwa3VtdG9WY1dRTVdpQXdvQlQ0NjJaakUtd0JzcUZ6OTRLRzNvU0I0?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQNVc4amE3bzV1cWF4SGlwOVd4UnNZVTZ6c09GZE42VDZiMGRkTXhiMDN6MS1lYzlfRzVHWlF2eVA4R0VlVlBBakREZ3hzSy1PVjBXWFdhSzEzbkVqdUtOc2tMUUN1eXJLNmhlNnJhSWE1Yk9PS2FhemlWalE2clE4aHB4T1NGcEJyeFVKNUdSbUY0UmMtMTh6aEIyR18?oc=5
- https://news.google.com/rss/articles/CBMi4wFBVV95cUxOUFJBOGQzQXE2NFkxd21JeE9YUml1MHdrVUo3c2wxRVhYal9YU1NPUllYR3Q0QUdMSG5iRFRGb3l4SE1iT2NWc2tLcXpUZktPMUs2SUdPSmRwWjR0ZVM4STdtNjNGbzhDX3FGNE9QYjR5M2o3NjdNTmRvNEo3S283Wk15Vk4zVnBQSlM3X09VR3lXb1RRN09GUkRCVTFnc1UzNXg5VlhqazV2WXhFdnNzSzJSaGc2cmRXYmtuRnhJYjB1QVY1RjhNTnlTRWd0ODItRjBHSjE1LWt4WWlxMHpTTzhBRQ?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQcnhfVE1scE5nTUJyNWhaYXZPMTA3bGlVVy1LY3RWZ0ltczdZNklGUHZicENiTU9PdkdMT0prcldrdUxpZXZCX3ZCbFo2ay1RWmxmNVNIeDBSQUtRczhFYVZzTVRaSDhkV2hiS1FYcGUxd05FWFd4dGNzWWRnNFVPd2VuRmxZaEhKOUppN0REa3l5V2NwZl9CRGFHSVA2bmc?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxNQVhIYXNZbFpjNVdYNUQ1VUdubkR5WmNvRlIxZGg0X1V2dWpiS1JBMXRxU1ZlRzVkaVNfZXZMV1Uza2o1SlFlRGdWMkt0dU9ia3VxNmNXb2RzM0NocHhReHlQVTJPbFBHYXpEc0NLcGRJQ2JjSjFEei1XRHdkc1ZfZ2dsQkxIZ2VFMG1WTnZvZGZ6Xzh3SnNOUmdOdjJSRUtqRWlYNEdOU1UtNUlqLXc?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQY01YWkJBY3Roa2hlWkVsbHhpcHplMm5NX09pWEJlMC1rWTY1ZDJoTUh0elc0WTZvdmpDOXJhS04tN2J5Y0N4NmZPdGk0aUhKdVZLT2RMSTk4S2EyZEJMYzY3WnpMMklfRjF3ZEJXZzU3d1VBTmlWS3Y1cllaYURseVQ4Nl93RFVLOXB4M1J6bnM1YVQ5QXBaSDZCOXEwUQ?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxPVkIwa3NOQkR0YlJNdlB6NUU5YzNkaklQOFJvcVcxVnY1M1dVdUVNT2hsUFV4cmo4bTNxbmtiZXl2VWtEUnVtWGdRZFB3bU1oWEVYckpac3J5SjBLZkFwWlRnX0ZfemJUQ2Z4cDFuOTEySU1RNkFidS1mR0hnNDBXOXlncWJ0dWlq?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxNMVMtc1Y3eXhUNk5mRWs4LUlZTmNGUEp3NGRmRzEycDdaQ2hCbmN6WUJLZEx2MWozS3ZmQ3lHME83aTVseGNWaTUzeE9fckpMTklyaE1SVEhJelBDRDFVS2xseWJMdjlLc2dCWFdudGgyVzlFMHZnNUdCby1QdnZuSkhkeXR3S3ptSVc4WlM2OHNXTm1JbUJWRjZ3NGxwa3JESmNHaGx0VTF3dFFlSzQxR2pXU2drbzFCbkduNjNZOTNLZ2NYZE1kbHZ5eUc?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNSm54cFIzY0lRUW93M3lxbXp3TERlTHd5ZmFwSTRTam94ZFJmTnRlUEFWWGhSYTNLbm5OVFR1MnZIU204ZW5femJoMHo4RkpiVngzR3hoZ3F4UHgyUWdlQmxPaW1idHFQLWFwZ3hjcGZfMG94bFNiVTUxXzJSaDR2aWRacnMyN3NfUUJyVEl6ZTRnUTZqSVFyTmtDM1ZROE0wNlE?oc=5
- https://news.google.com/rss/articles/CBMi4gFBVV95cUxPNElWbE1lOVJadXoxSXhxYy04M3B4ZG9PeWhIaW1lZE9maF91M3N1OXd6eFhSSDJZcVlkMm5oZFdoeDJiaVRqYnJBRVkzczJ0TG1kSjFVT0Y1dG5iV1JMS0NPTW9oeVNlYXZZS0haUThFQVNlcnhJbTlMTjAtZ1pQaFc5WDNhd1VDTFVqY1dDOF9NYlRhTE9xamFUdkpBVVo2MlIyOXJsYVdRYVNDV0RCTDRBS2dKRFc1YkR1Tnczc0VSbGNUX21pRTFsWUpDR0dNMmpLT2V4UmtheUs0WWs2YXRB?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPcFNTc21RYmNfVmRuQWJNRW0tc2tqbnFQY1c4R1pKUmw2QWY2WERYZVQ5WHNpejJhLXEwR0thQzYzaEppcWVlOUNua1ZGLW5SeW5NUE43M0dLSVp3MzhWMmVPM3dLZVowWXdkc1BGd3Vud3RBNm5KWlBIWm11Y0dycUo4c0RKSHJaRlRvdmtHcXplQ1JFTzBV?oc=5
- https://news.google.com/rss/articles/CBMigAFBVV95cUxQVFBOVnFZT1F2M3oteUktWm1qb29oLW5DLW9MZ2pBRzhEenlNZWFERC1NRXJlSV9saDN5MmNRZzdzQm0xQ0hWSzVpSktBSy00aDZlUTcyQzd2Vmlia1F1UTlEdE11anNMVE10RDNEVlc4cUlMcW5CRlpxaWFEbDh2Mg?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
