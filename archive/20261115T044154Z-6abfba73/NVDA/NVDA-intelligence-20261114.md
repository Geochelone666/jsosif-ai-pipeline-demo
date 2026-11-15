# NVDA Intelligence Report

- ticker: **NVDA**
- Report as_of: **2026-11-14**
- Market data as_of: **2026-11-13**
- Quant sources: https://finance.yahoo.com/quote/NVDA/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVDA/key-statistics/
- AI analysis snapshot as_of: **2026-11-14**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-15T04:42:01.441478+00:00**
- AI status: **Partial: 1 headline remains unclassified and excluded from research conclusions**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 7, 'ai': 15, 'unknown': 1, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'short_term_price_move_in_structural_risks': 2}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 13 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 40.0%; oldest publication 2026-11-11

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
| P/E (trailing) | 20.59 |
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
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 20.5879 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 24.8596 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -4.1243 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -24.1259 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -20.1403 -> Clearly below the moving-average trend level.

## TAILWINDS

### Retail investors are buying Nvidia’s stock crash like never before — history urges patience
- Summary: Retail investors buying Nvidia stock after crash, urging patience.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
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

### Nvidia Shares Sink 8.61% Premarket - NVIDIA (NASDAQ:NVDA)
- Summary: Nvidia Shares Sink 8.61% Premarket - NVIDIA (NASDAQ:NVDA)
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxOZmhocjZQQUdLMl80X2VqVHRvVGxDaVZfWGZ5aXJCUkJucXFTQzJ0TjNMWTNoQXNUVzR0SU00ekxDVEtZWmFUWDhwV2p2a25ROGg4YzNwY0xiY19kb2xkazhQQnYtdVY3b2FXTXVLNl8yZ254OUVlNHNGeTRTVHZhWXJocU5Yck96UE9ZODVYOVZNc0xJU0JsLVMyZ2NCQnFIUjBFamtJSUhoY21heFRfT2ZR?oc=5>

### Nvidia (NVDA) shares plunge as much as 14% levels as Jensen Huang resigns
- Summary: Shares drop 14% after CEO Jensen Huang resigns.
- Date: 2026-11-12 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPQngyY2dkNThLX3JuZElON0ZHOXlMTXNoOHdvU1hQMllrY3c3cWZyLUh3VGt6SXNfNU80QkRSM0s3SGEyWUc4QXZQX2F6b3ZiMUZTT3JjZ0MxOGhNa1J3S3o5MnB6bHUtS292eGFITUw4ZHhVU0pXLU9keVRRUEtSU05FNjFEV0wzQWxLcVZ0NDE4c3Zlc3c?oc=5>

## CATALYSTS

### NVDA Stock Alert: Why Baird Just Slashed Its Nvidia Price Target from $500 to $200
- Summary: NVDA Stock Alert: Why Baird Just Slashed Its Nvidia Price Target from $500 to $200
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxPVXNwX1BMQ2xudnlVbE5GQmJoZ1JZZnlpZncydE5BZXo0Y2tmOHlRdV9ybm9EbjlTcVAxSEhkYkprNlVLNW91OG5HQjFtLUJaVEFscXlqOVFZRGRQcklCTmQyQWZ4amlsQlFVeEdobXNYelUzWGNyZTRmWXU4dmFtSXB0bzliZFMzQzdLNmlIRFE0ZUdRakgwUjNFd2VHMVUzLTBaNVpjUTVFX013OGpiSjRqLV81VlpIMmo2Q3dveWw?oc=5>

### Nvidia (NVDA) Stock Gets Fair Value Trim As Analyst Views Turn More Divided
- Summary: Nvidia (NVDA) Stock Gets Fair Value Trim As Analyst Views Turn More Divided
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPRElTSFhVQUZmVlR1QXFPRko3NkRfbUMwdWRTdWxpcjBmenpxbnJja0ZEOFVQU19DZURySnM2NDZJc25wMFQtdV9jd21RYVNXT2tNaHl4eU9nSmw1TzhWTF9GdmhwMlFnMloxOC1hZEMwa3VtdG9WY1dRTVdpQXdvQlQ0NjJaakUtd0JzcUZ6OTRLRzNvU0I0?oc=5>

### NVIDIA Is Bouncing After a $430 Billion Wipeout. One Analyst Just Downgraded It. Where’s the Price Target?
- Summary: NVIDIA Is Bouncing After a $430 Billion Wipeout. One Analyst Just Downgraded It. Where’s the Price Target?
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNV0Z5M2dseUcyRF95eFhDb05YUVpwbWZyTVZNMFhjTlVibUVNeGdWeXJTdUt0T1hxSDRaaHNnVWZxaHVWeG90M09pemg4RU1wYWF6SkQxVDhUMFI2azBFbWlFc3FocXNWWllVc25yV0VXM1Z2RjIwQXZOSVc1cGtpMUs0VHBtUzVqSWN3alJFb1pmQkNkUnc2M211NFh0bUNUMWc?oc=5>

### NVDA Stock Rout: Another Analyst Slashes Rating, Beijing Warns US Against Tech Curbs
- Summary: NVDA Stock Rout: Another Analyst Slashes Rating, Beijing Warns US Against Tech Curbs
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQNVc4amE3bzV1cWF4SGlwOVd4UnNZVTZ6c09GZE42VDZiMGRkTXhiMDN6MS1lYzlfRzVHWlF2eVA4R0VlVlBBakREZ3hzSy1PVjBXWFdhSzEzbkVqdUtOc2tMUUN1eXJLNmhlNnJhSWE1Yk9PS2FhemlWalE2clE4aHB4T1NGcEJyeFVKNUdSbUY0UmMtMTh6aEIyR18?oc=5>

### Here’s How Much Traders Expect Nvidia Stock to Move After Earnings Next Week
- Summary: Traders forecast post-earnings movement.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxNQVhIYXNZbFpjNVdYNUQ1VUdubkR5WmNvRlIxZGg0X1V2dWpiS1JBMXRxU1ZlRzVkaVNfZXZMV1Uza2o1SlFlRGdWMkt0dU9ia3VxNmNXb2RzM0NocHhReHlQVTJPbFBHYXpEc0NLcGRJQ2JjSjFEei1XRHdkc1ZfZ2dsQkxIZ2VFMG1WTnZvZGZ6Xzh3SnNOUmdOdjJSRUtqRWlYNEdOU1UtNUlqLXc?oc=5>

### Nvidia stock closes down over 4% after CEO Jensen Huang announces resignation
- Summary: Nvidia shares fell 4% following CEO Jensen Huang’s resignation announcement.
- Date: 2026-11-12 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMigAFBVV95cUxQVFBOVnFZT1F2M3oteUktWm1qb29oLW5DLW9MZ2pBRzhEenlNZWFERC1NRXJlSV9saDN5MmNRZzdzQm0xQ0hWSzVpSktBSy00aDZlUTcyQzd2Vmlia1F1UTlEdE11anNMVE10RDNEVlc4cUlMcW5CRlpxaWFEbDh2Mg?oc=5>

### NVDA Stock Alert: Dan Ives Warns Nvidia’s Fair Value Could Tank 25% as Jensen Huang Resigns
- Summary: Analyst Dan Ives warns Nvidia’s fair value may drop 25% after CEO resignation.
- Date: 2026-11-12 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxQUzF2ZnNMdlMzOGwtemlSSmJTVHNEbnJhYTBzdk5PU2xBZ2pNLWxidUNwaEJvSmYzc04xUC1yZE1zMGZ6M3BZRmdOMEtyeFBMVFJPRHduSWJnVE1nQ2VNb0d6TXd4YlItd0duSnZveHY1ZEEtMTJhcTJYaV9Fd0QxQ3RqX1dnNzYzaUZHN0FkZlg3RXRacjVYVW1YM05GTGxTRmNzUFhGZkdyVXZtVlV4SWJ5N250ZVpGWUFqNmNnR2dhWWRKcGh1OGxzT08?oc=5>

### 'Icarus' rise and fall': Analyst downgrades Nvidia stock amid Jensen Huang woes, highlights risks
- Summary: Analyst downgrades Nvidia stock, citing risks amid CEO Jensen Huang’s resignation.
- Date: 2026-11-11 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi4wFBVV95cUxOUFJBOGQzQXE2NFkxd21JeE9YUml1MHdrVUo3c2wxRVhYal9YU1NPUllYR3Q0QUdMSG5iRFRGb3l4SE1iT2NWc2tLcXpUZktPMUs2SUdPSmRwWjR0ZVM4STdtNjNGbzhDX3FGNE9QYjR5M2o3NjdNTmRvNEo3S283Wk15Vk4zVnBQSlM3X09VR3lXb1RRN09GUkRCVTFnc1UzNXg5VlhqazV2WXhFdnNzSzJSaGc2cmRXYmtuRnhJYjB1QVY1RjhNTnlTRWd0ODItRjBHSjE1LWt4WWlxMHpTTzhBRQ?oc=5>

### Nvidia Stock Braces For AI Chipmaker's First Report Without Jensen Huang
- Summary: NVIDIA anticipates its first earnings report post-Jensen Huang, with market adjusting expectations.
- Date: 2026-11-13 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQb09Wd1BaSUZ6eXR5c3B3Si11cjE4NXNmV0pvT21JREtGZ21fUFhUZlNiTGJXc1AyMHJKUnZFLWFucnJoVFRMWGFWVnptcUJ3RXJ4eHN2ZlJ0STQzd1JTZG1oS2pxT3dfekdhdTlMeVZyenZ3cVNKbEFNdDA2emh3ZHlNV0oxV21nYkVZeEtaR1pVeVVoRWdyQk5nTks?oc=5>

### Needham, DA Davidson Lower Nvidia Stock (NVDA) Price Targets but Stay Bullish Despite CEO Transition Concerns
- Summary: Analysts Needham and DA Davidson cut price targets for NVDA but remain bullish amid CEO transition concerns.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxQaW1SOWRFa21MNXFyblpuUFpzSzZIZDYzLVp5QnRlYUtzeEZ3cDFoSDE2QTNPVGljeXVsLUlJZUtyX19rYWo5b21sS2tURFpPRWNBMVdSYjdfWGFKQ1AwTmJUVUk1NWsyV1FZX0hJZ2ptMlJMOEYzWm5CN2xwTGRpSWJjVVJEcF9YM0JfTkZRa0JpRENIMHlOVEFDTDdLZ1pMZ29zTWlCbVVpclZpUFgtWndQWG4tb1hsTDZhbGVnYjMwTnRrQ3FJVjFDVmpGZHMwVFE?oc=5>

## RISKS

### What the Nvidia scandal means for the company's earnings next week
- Summary: Nvidia faces potential earnings impact due to scandal, likely affecting next quarter's results.
- Date: 2026-11-13 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxQamtxZ1JjdTA3UF8zODVhLVE4NDNCZWczZmE1REtITGRpTURvLVpGemMtaGJIRy15U1lQal9CVFBjanlXLW5xUzNuS2x0NVM4REhHVVZadGVrejN2bkdUVHZzTjhDWEpvWnl2RWdGM2Q0UDVGWjZ5TkJCZFB3YlJsa3RPV25LNWxUOGFpNEJRdm9iN3hrbm0tNHphZmRRTGxjV1M4UUJkODdKM21kcktzeUtsREptZDhiRmVmLXd5UmQ2bFk?oc=5>

### Nvidia closes below $4T market cap for first time since July 2025 in Huang fallout
- Summary: Market cap fell below $4T amid leadership fallout, indicating short-term market weakness.
- Date: 2026-11-13 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxQeHRJRmZaWDY1TDNwelllbWd6OUZiV1NzaEllNG9aekhVYVVGWWhOREZuczlHQzJEZXFoeUotM2wwOW5ZTEJTOWlkb2JqSV82U2hmU01GeVhzYVlmZDZVYVFMZFo4UTNBenhOa0N4ejd0bkczZ0Nsa0I5YThHbk9iVGFkWlHSAYoBQVVfeXFMTlpCeWpuYTJhM2NHaUxJc2dkRlVSQUZ4TWxuUjh1QU1NOFE0WjJ2QUVlc0E1VWhjLUZZeGJGdEw1emRmWHM1aUNXSDdjWGRXMUhGLXJXMEpqaWlZSjUzTmY3b3lVTWhSTENiV0M0WjNZeGJTREpab09JczdLejZRTzh3SGNZWGxGVUZB?oc=5>

### Nvidia Has Been the Market’s Golden Goose. Now It’s in Crisis
- Summary: Company faces crisis, raising concerns about future performance and stability.
- Date: 2026-11-12 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxNc1VaLTdKSEJHUTRualBnQ3lrODR6d3lQTWE1a2Fla0IyTjIyYnB4OXRLT2tsZUthUlZXVUNfMWprcDVfazdIMWYwLUNVc1JBX2NEYUNfZG96T19kVnFQckRRWkxxVjlYMGZtdlV2bDBvTUt5M1JEZmVKdDJPaHh4YXRrQkE2VHZnZFVQM01GMA?oc=5>

### Cantor Cuts Nvidia Target by $100: 'A Very Sad Day' - NVIDIA (NASDAQ:NVDA)
- Summary: Analyst downgrade cuts target by $100.
- Date: 2026-11-12 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxNMVMtc1Y3eXhUNk5mRWs4LUlZTmNGUEp3NGRmRzEycDdaQ2hCbmN6WUJLZEx2MWozS3ZmQ3lHME83aTVseGNWaTUzeE9fckpMTklyaE1SVEhJelBDRDFVS2xseWJMdjlLc2dCWFdudGgyVzlFMHZnNUdCby1QdnZuSkhkeXR3S3ptSVc4WlM2OHNXTm1JbUJWRjZ3NGxwa3JESmNHaGx0VTF3dFFlSzQxR2pXU2drbzFCbkduNjNZOTNLZ2NYZE1kbHZ5eUc?oc=5>

### Nvidia Stock $162.85: Q3 Results 17 Nov, Bull $187 Bear $149
- Summary: Q3 results announced with price range.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxOQ3dVdFpzWVhUTWdtVnNVUlBUNVJLVnpQOW95eWRuc1FxZkJIUGdUMkwzeThoU0QxWFFDLVBHbkgxWUhlZjNGQmZnREdzWTVscU04MjNJM1NzQXJKaEl5TlllRU52NGJPaU9jTWMxMnozeVVnVEtjU3NzZGJCN09nR1J5dTdrVG0tb3ZEWjE3Y3pjWHo0a2kzNFB5SXZfR2hlaWwzLVpBTEZHVWFPZWJWS0Zqei1qS1pIZ2M1ekF2NjhCNVJSbC1BZQ?oc=5>

### Jensen Huang Is Out at Nvidia. Where Does NVDA Stock Go From Here?
- Summary: CEO departure raises uncertainty.
- Date: 2026-11-12 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNSm54cFIzY0lRUW93M3lxbXp3TERlTHd5ZmFwSTRTam94ZFJmTnRlUEFWWGhSYTNLbm5OVFR1MnZIU204ZW5femJoMHo4RkpiVngzR3hoZ3F4UHgyUWdlQmxPaW1idHFQLWFwZ3hjcGZfMG94bFNiVTUxXzJSaDR2aWRacnMyN3NfUUJyVEl6ZTRnUTZqSVFyTmtDM1ZROE0wNlE?oc=5>

### NVDA Stock On Track To Hit Lowest Level In Over A Year: Dan Ives Values Nvidia At $225 Without Jensen Huang
- Summary: NVDA stock projected to reach lowest level in over a year, with Dan Ives valuing at $225, reflecting bearish outlook.
- Date: 2026-11-12 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPcFNTc21RYmNfVmRuQWJNRW0tc2tqbnFQY1c4R1pKUmw2QWY2WERYZVQ5WHNpejJhLXEwR0thQzYzaEppcWVlOUNua1ZGLW5SeW5NUE43M0dLSVp3MzhWMmVPM3dLZVowWXdkc1BGd3Vud3RBNm5KWlBIWm11Y0dycUo4c0RKSHJaRlRvdmtHcXplQ1JFTzBV?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVDA** | **20.59** | **17.17** | **19.38** | **105.90** | **3,932,339,044,352.00 USD** | **-12.64** |
| AMD | 114.12 | 12.81 | 78.02 | 44.70 | 875,905,024,000.00 USD | 115.38 |
| AVGO | 44.32 | 16.62 | 32.38 | 85.50 | 1,656,497,373,184.00 USD | 2.83 |
| INTC | N/A | 2.76 | 17.24 | 20.90 | 317,092,888,576.00 USD | 66.14 |

Peers fetched as_of: 2026-11-14; NVDA reuses existing data (market data as_of: 2026-11-13); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-26
- Next expected earnings: 2026-11-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-14

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
- https://news.google.com/rss/articles/CBMisgFBVV95cUxOZmhocjZQQUdLMl80X2VqVHRvVGxDaVZfWGZ5aXJCUkJucXFTQzJ0TjNMWTNoQXNUVzR0SU00ekxDVEtZWmFUWDhwV2p2a25ROGg4YzNwY0xiY19kb2xkazhQQnYtdVY3b2FXTXVLNl8yZ254OUVlNHNGeTRTVHZhWXJocU5Yck96UE9ZODVYOVZNc0xJU0JsLVMyZ2NCQnFIUjBFamtJSUhoY21heFRfT2ZR?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPQngyY2dkNThLX3JuZElON0ZHOXlMTXNoOHdvU1hQMllrY3c3cWZyLUh3VGt6SXNfNU80QkRSM0s3SGEyWUc4QXZQX2F6b3ZiMUZTT3JjZ0MxOGhNa1J3S3o5MnB6bHUtS292eGFITUw4ZHhVU0pXLU9keVRRUEtSU05FNjFEV0wzQWxLcVZ0NDE4c3Zlc3c?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxPVXNwX1BMQ2xudnlVbE5GQmJoZ1JZZnlpZncydE5BZXo0Y2tmOHlRdV9ybm9EbjlTcVAxSEhkYkprNlVLNW91OG5HQjFtLUJaVEFscXlqOVFZRGRQcklCTmQyQWZ4amlsQlFVeEdobXNYelUzWGNyZTRmWXU4dmFtSXB0bzliZFMzQzdLNmlIRFE0ZUdRakgwUjNFd2VHMVUzLTBaNVpjUTVFX013OGpiSjRqLV81VlpIMmo2Q3dveWw?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPRElTSFhVQUZmVlR1QXFPRko3NkRfbUMwdWRTdWxpcjBmenpxbnJja0ZEOFVQU19DZURySnM2NDZJc25wMFQtdV9jd21RYVNXT2tNaHl4eU9nSmw1TzhWTF9GdmhwMlFnMloxOC1hZEMwa3VtdG9WY1dRTVdpQXdvQlQ0NjJaakUtd0JzcUZ6OTRLRzNvU0I0?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNV0Z5M2dseUcyRF95eFhDb05YUVpwbWZyTVZNMFhjTlVibUVNeGdWeXJTdUt0T1hxSDRaaHNnVWZxaHVWeG90M09pemg4RU1wYWF6SkQxVDhUMFI2azBFbWlFc3FocXNWWllVc25yV0VXM1Z2RjIwQXZOSVc1cGtpMUs0VHBtUzVqSWN3alJFb1pmQkNkUnc2M211NFh0bUNUMWc?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQNVc4amE3bzV1cWF4SGlwOVd4UnNZVTZ6c09GZE42VDZiMGRkTXhiMDN6MS1lYzlfRzVHWlF2eVA4R0VlVlBBakREZ3hzSy1PVjBXWFdhSzEzbkVqdUtOc2tMUUN1eXJLNmhlNnJhSWE1Yk9PS2FhemlWalE2clE4aHB4T1NGcEJyeFVKNUdSbUY0UmMtMTh6aEIyR18?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxNQVhIYXNZbFpjNVdYNUQ1VUdubkR5WmNvRlIxZGg0X1V2dWpiS1JBMXRxU1ZlRzVkaVNfZXZMV1Uza2o1SlFlRGdWMkt0dU9ia3VxNmNXb2RzM0NocHhReHlQVTJPbFBHYXpEc0NLcGRJQ2JjSjFEei1XRHdkc1ZfZ2dsQkxIZ2VFMG1WTnZvZGZ6Xzh3SnNOUmdOdjJSRUtqRWlYNEdOU1UtNUlqLXc?oc=5
- https://news.google.com/rss/articles/CBMigAFBVV95cUxQVFBOVnFZT1F2M3oteUktWm1qb29oLW5DLW9MZ2pBRzhEenlNZWFERC1NRXJlSV9saDN5MmNRZzdzQm0xQ0hWSzVpSktBSy00aDZlUTcyQzd2Vmlia1F1UTlEdE11anNMVE10RDNEVlc4cUlMcW5CRlpxaWFEbDh2Mg?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxQUzF2ZnNMdlMzOGwtemlSSmJTVHNEbnJhYTBzdk5PU2xBZ2pNLWxidUNwaEJvSmYzc04xUC1yZE1zMGZ6M3BZRmdOMEtyeFBMVFJPRHduSWJnVE1nQ2VNb0d6TXd4YlItd0duSnZveHY1ZEEtMTJhcTJYaV9Fd0QxQ3RqX1dnNzYzaUZHN0FkZlg3RXRacjVYVW1YM05GTGxTRmNzUFhGZkdyVXZtVlV4SWJ5N250ZVpGWUFqNmNnR2dhWWRKcGh1OGxzT08?oc=5
- https://news.google.com/rss/articles/CBMi4wFBVV95cUxOUFJBOGQzQXE2NFkxd21JeE9YUml1MHdrVUo3c2wxRVhYal9YU1NPUllYR3Q0QUdMSG5iRFRGb3l4SE1iT2NWc2tLcXpUZktPMUs2SUdPSmRwWjR0ZVM4STdtNjNGbzhDX3FGNE9QYjR5M2o3NjdNTmRvNEo3S283Wk15Vk4zVnBQSlM3X09VR3lXb1RRN09GUkRCVTFnc1UzNXg5VlhqazV2WXhFdnNzSzJSaGc2cmRXYmtuRnhJYjB1QVY1RjhNTnlTRWd0ODItRjBHSjE1LWt4WWlxMHpTTzhBRQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQb09Wd1BaSUZ6eXR5c3B3Si11cjE4NXNmV0pvT21JREtGZ21fUFhUZlNiTGJXc1AyMHJKUnZFLWFucnJoVFRMWGFWVnptcUJ3RXJ4eHN2ZlJ0STQzd1JTZG1oS2pxT3dfekdhdTlMeVZyenZ3cVNKbEFNdDA2emh3ZHlNV0oxV21nYkVZeEtaR1pVeVVoRWdyQk5nTks?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxQaW1SOWRFa21MNXFyblpuUFpzSzZIZDYzLVp5QnRlYUtzeEZ3cDFoSDE2QTNPVGljeXVsLUlJZUtyX19rYWo5b21sS2tURFpPRWNBMVdSYjdfWGFKQ1AwTmJUVUk1NWsyV1FZX0hJZ2ptMlJMOEYzWm5CN2xwTGRpSWJjVVJEcF9YM0JfTkZRa0JpRENIMHlOVEFDTDdLZ1pMZ29zTWlCbVVpclZpUFgtWndQWG4tb1hsTDZhbGVnYjMwTnRrQ3FJVjFDVmpGZHMwVFE?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxQamtxZ1JjdTA3UF8zODVhLVE4NDNCZWczZmE1REtITGRpTURvLVpGemMtaGJIRy15U1lQal9CVFBjanlXLW5xUzNuS2x0NVM4REhHVVZadGVrejN2bkdUVHZzTjhDWEpvWnl2RWdGM2Q0UDVGWjZ5TkJCZFB3YlJsa3RPV25LNWxUOGFpNEJRdm9iN3hrbm0tNHphZmRRTGxjV1M4UUJkODdKM21kcktzeUtsREptZDhiRmVmLXd5UmQ2bFk?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxQeHRJRmZaWDY1TDNwelllbWd6OUZiV1NzaEllNG9aekhVYVVGWWhOREZuczlHQzJEZXFoeUotM2wwOW5ZTEJTOWlkb2JqSV82U2hmU01GeVhzYVlmZDZVYVFMZFo4UTNBenhOa0N4ejd0bkczZ0Nsa0I5YThHbk9iVGFkWlHSAYoBQVVfeXFMTlpCeWpuYTJhM2NHaUxJc2dkRlVSQUZ4TWxuUjh1QU1NOFE0WjJ2QUVlc0E1VWhjLUZZeGJGdEw1emRmWHM1aUNXSDdjWGRXMUhGLXJXMEpqaWlZSjUzTmY3b3lVTWhSTENiV0M0WjNZeGJTREpab09JczdLejZRTzh3SGNZWGxGVUZB?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxNc1VaLTdKSEJHUTRualBnQ3lrODR6d3lQTWE1a2Fla0IyTjIyYnB4OXRLT2tsZUthUlZXVUNfMWprcDVfazdIMWYwLUNVc1JBX2NEYUNfZG96T19kVnFQckRRWkxxVjlYMGZtdlV2bDBvTUt5M1JEZmVKdDJPaHh4YXRrQkE2VHZnZFVQM01GMA?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxNMVMtc1Y3eXhUNk5mRWs4LUlZTmNGUEp3NGRmRzEycDdaQ2hCbmN6WUJLZEx2MWozS3ZmQ3lHME83aTVseGNWaTUzeE9fckpMTklyaE1SVEhJelBDRDFVS2xseWJMdjlLc2dCWFdudGgyVzlFMHZnNUdCby1QdnZuSkhkeXR3S3ptSVc4WlM2OHNXTm1JbUJWRjZ3NGxwa3JESmNHaGx0VTF3dFFlSzQxR2pXU2drbzFCbkduNjNZOTNLZ2NYZE1kbHZ5eUc?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxOQ3dVdFpzWVhUTWdtVnNVUlBUNVJLVnpQOW95eWRuc1FxZkJIUGdUMkwzeThoU0QxWFFDLVBHbkgxWUhlZjNGQmZnREdzWTVscU04MjNJM1NzQXJKaEl5TlllRU52NGJPaU9jTWMxMnozeVVnVEtjU3NzZGJCN09nR1J5dTdrVG0tb3ZEWjE3Y3pjWHo0a2kzNFB5SXZfR2hlaWwzLVpBTEZHVWFPZWJWS0Zqei1qS1pIZ2M1ekF2NjhCNVJSbC1BZQ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNSm54cFIzY0lRUW93M3lxbXp3TERlTHd5ZmFwSTRTam94ZFJmTnRlUEFWWGhSYTNLbm5OVFR1MnZIU204ZW5femJoMHo4RkpiVngzR3hoZ3F4UHgyUWdlQmxPaW1idHFQLWFwZ3hjcGZfMG94bFNiVTUxXzJSaDR2aWRacnMyN3NfUUJyVEl6ZTRnUTZqSVFyTmtDM1ZROE0wNlE?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPcFNTc21RYmNfVmRuQWJNRW0tc2tqbnFQY1c4R1pKUmw2QWY2WERYZVQ5WHNpejJhLXEwR0thQzYzaEppcWVlOUNua1ZGLW5SeW5NUE43M0dLSVp3MzhWMmVPM3dLZVowWXdkc1BGd3Vud3RBNm5KWlBIWm11Y0dycUo4c0RKSHJaRlRvdmtHcXplQ1JFTzBV?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
