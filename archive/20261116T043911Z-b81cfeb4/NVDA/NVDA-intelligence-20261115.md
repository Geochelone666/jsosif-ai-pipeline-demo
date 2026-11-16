# NVDA Intelligence Report

- ticker: **NVDA**
- Report as_of: **2026-11-15**
- Market data as_of: **2026-11-13**
- Quant sources: https://finance.yahoo.com/quote/NVDA/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVDA/key-statistics/
- AI analysis snapshot as_of: **2026-11-15**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-16T04:39:19.653132+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 8, 'ai': 15, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **4**; {'directional_claim_without_event_type': 2, 'low_uncalibrated_model_confidence': 2}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 9 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 62.5%; oldest publication 2026-11-12

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
- Summary: Retail investors are buying Nvidia shares heavily after a crash, indicating renewed confidence.
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

### Needham, DA Davidson Lower Nvidia Stock (NVDA) Price Targets but Stay Bullish Despite CEO Transition Concerns
- Summary: Analysts cut price targets yet remain bullish amid CEO transition concerns.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxQaW1SOWRFa21MNXFyblpuUFpzSzZIZDYzLVp5QnRlYUtzeEZ3cDFoSDE2QTNPVGljeXVsLUlJZUtyX19rYWo5b21sS2tURFpPRWNBMVdSYjdfWGFKQ1AwTmJUVUk1NWsyV1FZX0hJZ2ptMlJMOEYzWm5CN2xwTGRpSWJjVVJEcF9YM0JfTkZRa0JpRENIMHlOVEFDTDdLZ1pMZ29zTWlCbVVpclZpUFgtWndQWG4tb1hsTDZhbGVnYjMwTnRrQ3FJVjFDVmpGZHMwVFE?oc=5>

### Jensen Huang Is Out at Nvidia. Where Does NVDA Stock Go From Here?
- Summary: NVIDIA CEO Jensen Huang resigns, raising uncertainty about future strategy and stock performance.
- Date: 2026-11-12 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNSm54cFIzY0lRUW93M3lxbXp3TERlTHd5ZmFwSTRTam94ZFJmTnRlUEFWWGhSYTNLbm5OVFR1MnZIU204ZW5femJoMHo4RkpiVngzR3hoZ3F4UHgyUWdlQmxPaW1idHFQLWFwZ3hjcGZfMG94bFNiVTUxXzJSaDR2aWRacnMyN3NfUUJyVEl6ZTRnUTZqSVFyTmtDM1ZROE0wNlE?oc=5>

### 'Massive shoes to fill': Wall Street sours on Nvidia stock after Jensen Huang's exit
- Summary: Wall Street reacts negatively to CEO departure, expecting potential strategic shifts and stock volatility.
- Date: 2026-11-15 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxQSUhad2VoUnU5VjNDX3N6UW5WX1FFaFA1eUU2V1kxX3BTQlpVX2twdVVaUHEtTWozYWZBRzRwbHZ6NE1OdHpQWXV2cml5b2R5bGY0bVk1Y19qM0pFcjk1V1NWUFNuX2lHOUlVLXVpeVRJam9mSjdiMTI2OG1KS3FvcmVQVGV0Uzh0TldXa2NLUmhNeTQtZS1oS3dydFJHTWNDcHdDLUtpakNCcV85eDdKTG15M3hqNnZOUko5RVB3aHhvbEJuVVE?oc=5>

## CATALYSTS

### NVDA Stock Alert: Why Baird Just Slashed Its Nvidia Price Target from $500 to $200
- Summary: NVDA Stock Alert: Why Baird Just Slashed Its Nvidia Price Target from $500 to $200
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxPVXNwX1BMQ2xudnlVbE5GQmJoZ1JZZnlpZncydE5BZXo0Y2tmOHlRdV9ybm9EbjlTcVAxSEhkYkprNlVLNW91OG5HQjFtLUJaVEFscXlqOVFZRGRQcklCTmQyQWZ4amlsQlFVeEdobXNYelUzWGNyZTRmWXU4dmFtSXB0bzliZFMzQzdLNmlIRFE0ZUdRakgwUjNFd2VHMVUzLTBaNVpjUTVFX013OGpiSjRqLV81VlpIMmo2Q3dveWw?oc=5>

### Nvidia Q3 Earnings Preview: What Options Traders Expect After Jensen Huang’s Sudden Exit
- Summary: Nvidia Q3 Earnings Preview: What Options Traders Expect After Jensen Huang’s Sudden Exit
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQTGJpT1kwd1M1SjBUNjVPejAyYWgyazlCYWZzY055VmNiQ2I1bjV5dVpHbzJrdjFiVjRtc21DQU1tMXBta0dxaFlrQmF1X2hiTDN5RlktSUtwV1UxbnFlNTZxaV8tVGtWTS1JZWpkT3lXM29FSlhqWE83QWpKRVpfSkxnd3Z5MkxwbGlycEZTUV9VamRWM3l1M1ZvazFBSE1PR0E?oc=5>

### Nvidia Reports Earnings on Nov. 17. Here's What Investors Should Be Watching.
- Summary: Nvidia Reports Earnings on Nov. 17. Here's What Investors Should Be Watching.
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNX21BUzJKcno4QV9IY3F5QVlpNTVYaUVlbmpUeVlzQmdjcUVrQU5ucUNTdEFBaXF2VnBRaWxDcHIzSlJKNGpDdmlNdHJweGJpN1p1cWN3TFVPZmp3Z1BQb29uQjJqSm9ENGZzTEF3a0d1V3NkOWMyMjFhdjQ1UHlBanhhN0gwSU80T19IWEpQWmN4OTk3MkRvY2F6dw?oc=5>

### Nvidia's first post-Jensen earnings and Anthropic's IPO: What to watch this week
- Summary: Nvidia's first post-Jensen earnings and Anthropic's IPO: What to watch this week
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxPRGowX3ljRUhFOUtMR2diRUJHR2xTalpGZExTNFRKTExUQTQ2cUtNQXZfWEVRM3BMYldsOEh2czRtSmJZVExCakN0Q2VaWVRWWmFSYjRsRFBqNzRucXh1c2pIcW84aDUzdkhjY3pyZFFkVjRSN2gzU0dNM1NEWXI2WHIxdXl0OTB4OVM3QVVsSXg5V2NUQVVLVmZJWURyaWhXOUxyTWE3cm1qVXRQTFktZWQ0Y3hmaWlaenFrTi1jc3ZPSTFlWUVEbXRaYUVQOU0?oc=5>

### Nvidia (NVDA) Stock Gets Fair Value Trim As Analyst Views Turn More Divided
- Summary: Nvidia (NVDA) Stock Gets Fair Value Trim As Analyst Views Turn More Divided
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPRElTSFhVQUZmVlR1QXFPRko3NkRfbUMwdWRTdWxpcjBmenpxbnJja0ZEOFVQU19DZURySnM2NDZJc25wMFQtdV9jd21RYVNXT2tNaHl4eU9nSmw1TzhWTF9GdmhwMlFnMloxOC1hZEMwa3VtdG9WY1dRTVdpQXdvQlQ0NjJaakUtd0JzcUZ6OTRLRzNvU0I0?oc=5>

### NVDA Stock Rout: Another Analyst Slashes Rating, Beijing Warns US Against Tech Curbs
- Summary: NVDA Stock Rout: Another Analyst Slashes Rating, Beijing Warns US Against Tech Curbs
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQNVc4amE3bzV1cWF4SGlwOVd4UnNZVTZ6c09GZE42VDZiMGRkTXhiMDN6MS1lYzlfRzVHWlF2eVA4R0VlVlBBakREZ3hzSy1PVjBXWFdhSzEzbkVqdUtOc2tMUUN1eXJLNmhlNnJhSWE1Yk9PS2FhemlWalE2clE4aHB4T1NGcEJyeFVKNUdSbUY0UmMtMTh6aEIyR18?oc=5>

### Should you buy Nvidia stock right now?
- Summary: Investor query about current Nvidia stock purchase.
- Date: 2026-11-15 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxNOWk5b2U5UXB0UncwYlJpQWRFZXFLMjZVSE9JS0JtUEVpQ2E3SjBVRS1EdzkwUW9RTWRHbVpEMzhtQldCTXJJZ180aVVUVGg0Q01XN3FhdFMyMGN3TGJoSk1CY1J1Vm9BWEN6dmVpbVotR3NKT3RJNWJJWkY1UllFSUQ1VGtQa0JKV0N4V1J6eHZNc1FwZmk2VmdpbXRJX3BtTWhF?oc=5>

### Nvidia CEO Jensen Huang Resigns as Stock Tanks. Here Are the Next Steps for Investors.
- Summary: CEO resignation amid falling stock price.
- Date: 2026-11-15 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxPaFpwMHBHOFV1MGlTNjNSTDdpcFplOWZZTS12a25wak1qTHJwNEZWX2w3WkxPUFpLMlJYNUkwajlWZ1pPWFVaODFjTDJval9PT3QyTmRqN0FyeTZ6U29VanRSTUtxdVE2bVplTFF6N0FfMU43dzhwRURIOWVDNGl4MjdNX3FtZ0dGV0ljMGJzenFmM19TeHRiQ2FPOWM3QnRVV0poOXBFVnFXMHBycGpxakJtbkwtczBONXNKekxsdTNUclBMUlE?oc=5>

### Nvidia closes below $4T market cap for first time since July 2025 in Huang fallout
- Summary: Market cap dips below $4 trillion for first time since July 2025.
- Date: 2026-11-13 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxQeHRJRmZaWDY1TDNwelllbWd6OUZiV1NzaEllNG9aekhVYVVGWWhOREZuczlHQzJEZXFoeUotM2wwOW5ZTEJTOWlkb2JqSV82U2hmU01GeVhzYVlmZDZVYVFMZFo4UTNBenhOa0N4ejd0bkczZ0Nsa0I5YThHbk9iVGFkWlHSAYoBQVVfeXFMTlpCeWpuYTJhM2NHaUxJc2dkRlVSQUZ4TWxuUjh1QU1NOFE0WjJ2QUVlc0E1VWhjLUZZeGJGdEw1emRmWHM1aUNXSDdjWGRXMUhGLXJXMEpqaWlZSjUzTmY3b3lVTWhSTENiV0M0WjNZeGJTREpab09JczdLejZRTzh3SGNZWGxGVUZB?oc=5>

### Nvidia Stock $162.85: Q3 Results 17 Nov, Bull $187 Bear $149
- Summary: Q3 earnings release with price targets.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxOQ3dVdFpzWVhUTWdtVnNVUlBUNVJLVnpQOW95eWRuc1FxZkJIUGdUMkwzeThoU0QxWFFDLVBHbkgxWUhlZjNGQmZnREdzWTVscU04MjNJM1NzQXJKaEl5TlllRU52NGJPaU9jTWMxMnozeVVnVEtjU3NzZGJCN09nR1J5dTdrVG0tb3ZEWjE3Y3pjWHo0a2kzNFB5SXZfR2hlaWwzLVpBTEZHVWFPZWJWS0Zqei1qS1pIZ2M1ekF2NjhCNVJSbC1BZQ?oc=5>

### Jensen Huang leaves Nvidia with a $132 billion stake — here's when he can sell and why investors may not know when he does: Chart of the Day
- Summary: CEO departure with large stake; sale timing uncertain.
- Date: 2026-11-15 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingJBVV95cUxNVjJKRThIRnJiTkxmT2NTMlJKbjhMWXhOSlhVcWRDUFNwYXRwUUlwRzJYZ1lJWFpqOVk0RUFqTFRtdmY3cVNscUxMRDVyVFFnLUxfdFoxX29KeW1iODB1d0cwVlVObjlIU3RvaUdDMFpJUzd5OXhfZUZCWkhKZkFRMEl6M3o2S2tIbkVVdngzVE5wcDR2d0Q4eWFqVXZScGlPQmFTTTNsdExXNWNDZXlXdF9UQ3ZfX3lweU1aMU9FOWthV1pYNEJabUNvb0Fna2dnM000dUdJbEFTOWU4UHhtZTExU1VqSi00V2EzUWwyemk3R3FlN3pEeWo1Uy1nU0V5ODhSMlh0SG1pMXpZS2FYLUJ1V1FtLTZDSnFOS3RB?oc=5>

### Equities close lower as Nvidia drop outweighs energy gains
- Summary: Nvidia shares fell, dragging down broader equity markets.
- Date: 2026-11-12 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQY01YWkJBY3Roa2hlWkVsbHhpcHplMm5NX09pWEJlMC1rWTY1ZDJoTUh0elc0WTZvdmpDOXJhS04tN2J5Y0N4NmZPdGk0aUhKdVZLT2RMSTk4S2EyZEJMYzY3WnpMMklfRjF3ZEJXZzU3d1VBTmlWS3Y1cllaYURseVQ4Nl93RFVLOXB4M1J6bnM1YVQ5QXBaSDZCOXEwUQ?oc=5>

### Jensen Huang Reportedly Wants Back In As Nvidia CEO. How Will Stock React?
- Summary: Rumors of Jensen Huang returning as CEO could influence investor sentiment.
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPUHhPNUFLeEpOMmNseG40aV9MMzVpTlhDNUxqOGo2b2lkUjVrUTlqRkQ4QTNxWDJGcTZuM3I5OUJGZzdSLU4yVnVsNkltdUxTQmRFeGNTaUctYUVFNkJ2cFJ4MEkyTHN6Tk9EQXVwcDdEV0RCaUZpaTJDTmVDYjdOdERVVVQ2ZWNLa2d5ZjdvTjRyRVJTZ19lYVoyUHlZYjZ5?oc=5>

### Nvidia Stock Could Have Its First Losing Year Since 2022. Here's What It Did After Its Last 7.
- Summary: Analysis of Nvidia's potential first annual loss since 2022 and historical performance.
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNbzB5dGpZSkhYa3cwUHkyT19vMUNERzA5MXJhUWtjZFFfWDYtXy1vLU16S0huQzhBSzVCXzBjdmpQUlVNOGFzUlN6RndocmtyQ2V0WF9KTmdoYkQtWkVmVVNYYVM1NFVNN210aHJCZWU2cnA3d0o2ZHB1LWgzOTZqbUZjYUdfMVRFclU3UFhtVHV4ZXlzTkZ1YVd5aGI?oc=5>

### After the Nvidia stock crash, here’s what I’m doing in my ISA and SIPP
- Summary: Investor strategy following Nvidia's recent stock decline.
- Date: 2026-11-15 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMigAFBVV95cUxPekh0UHV1WThuLTRORUgtZ3k5QnUtTnhnOGQyS3h3MUNvbi1LRmtINmJsSWgtUWdSakZmR0lLeHkzcTJNRTBZcDFqTkJjTlBPRjJLbF81VmJfTkljdU5Vb1pyWDg5NWhYVFVSUHBybkRjTlRRa0p4UFFPbkpHY2ZreA?oc=5>

### Jensen Huang Reportedly Weighing Return to Nvidia as Elon Musk Warns “Critical Deals Will Be Lost” Without Him
- Summary: Rumors of Huang's return amid Musk's warning about lost deals.
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxPZVdZcFBSMGkxLVlwRWhHVDNnSkxsLThrQlBNYUJWbVpoWlg3a0w3amZPZ1RwQUVPVkUxemVxSVdXdVRIUkRHcy13enFGM3NiU1ZXOU5YaVA0M2g2amk0T0NSSW1QREc5bUhzbEJMOURZMXhoR3ZIVHFzaWQtMHVQT3lOSkpDTFhHb1NLMU8zR0xvMjRJbmRGZzhEbHE5WUY5N0l1MnFfWQ?oc=5>

## RISKS

### 'Nothing has changed': Why some Nvidia stock bulls aren't wavering after Jensen Huang ouster
- Summary: Despite Jensen Huang's ouster, some bulls remain unchanged, suggesting stability but potential leadership concerns.
- Date: 2026-11-13 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi4gFBVV95cUxPNElWbE1lOVJadXoxSXhxYy04M3B4ZG9PeWhIaW1lZE9maF91M3N1OXd6eFhSSDJZcVlkMm5oZFdoeDJiaVRqYnJBRVkzczJ0TG1kSjFVT0Y1dG5iV1JMS0NPTW9oeVNlYXZZS0haUThFQVNlcnhJbTlMTjAtZ1pQaFc5WDNhd1VDTFVqY1dDOF9NYlRhTE9xamFUdkpBVVo2MlIyOXJsYVdRYVNDV0RCTDRBS2dKRFc1YkR1Tnczc0VSbGNUX21pRTFsWUpDR0dNMmpLT2V4UmtheUs0WWs2YXRB?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVDA** | **20.59** | **17.17** | **19.38** | **105.90** | **3,932,339,044,352.00 USD** | **-12.64** |
| AMD | 114.12 | 12.81 | 78.02 | 44.70 | 875,905,024,000.00 USD | 115.38 |
| AVGO | 44.32 | 16.62 | 32.38 | 85.50 | 1,656,497,373,184.00 USD | 2.83 |
| INTC | N/A | 2.76 | 17.24 | 20.90 | 317,092,888,576.00 USD | 66.14 |

Peers fetched as_of: 2026-11-15; NVDA reuses existing data (market data as_of: 2026-11-13); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-26
- Next expected earnings: 2026-11-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-15

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
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxQaW1SOWRFa21MNXFyblpuUFpzSzZIZDYzLVp5QnRlYUtzeEZ3cDFoSDE2QTNPVGljeXVsLUlJZUtyX19rYWo5b21sS2tURFpPRWNBMVdSYjdfWGFKQ1AwTmJUVUk1NWsyV1FZX0hJZ2ptMlJMOEYzWm5CN2xwTGRpSWJjVVJEcF9YM0JfTkZRa0JpRENIMHlOVEFDTDdLZ1pMZ29zTWlCbVVpclZpUFgtWndQWG4tb1hsTDZhbGVnYjMwTnRrQ3FJVjFDVmpGZHMwVFE?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNSm54cFIzY0lRUW93M3lxbXp3TERlTHd5ZmFwSTRTam94ZFJmTnRlUEFWWGhSYTNLbm5OVFR1MnZIU204ZW5femJoMHo4RkpiVngzR3hoZ3F4UHgyUWdlQmxPaW1idHFQLWFwZ3hjcGZfMG94bFNiVTUxXzJSaDR2aWRacnMyN3NfUUJyVEl6ZTRnUTZqSVFyTmtDM1ZROE0wNlE?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxQSUhad2VoUnU5VjNDX3N6UW5WX1FFaFA1eUU2V1kxX3BTQlpVX2twdVVaUHEtTWozYWZBRzRwbHZ6NE1OdHpQWXV2cml5b2R5bGY0bVk1Y19qM0pFcjk1V1NWUFNuX2lHOUlVLXVpeVRJam9mSjdiMTI2OG1KS3FvcmVQVGV0Uzh0TldXa2NLUmhNeTQtZS1oS3dydFJHTWNDcHdDLUtpakNCcV85eDdKTG15M3hqNnZOUko5RVB3aHhvbEJuVVE?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxPVXNwX1BMQ2xudnlVbE5GQmJoZ1JZZnlpZncydE5BZXo0Y2tmOHlRdV9ybm9EbjlTcVAxSEhkYkprNlVLNW91OG5HQjFtLUJaVEFscXlqOVFZRGRQcklCTmQyQWZ4amlsQlFVeEdobXNYelUzWGNyZTRmWXU4dmFtSXB0bzliZFMzQzdLNmlIRFE0ZUdRakgwUjNFd2VHMVUzLTBaNVpjUTVFX013OGpiSjRqLV81VlpIMmo2Q3dveWw?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQTGJpT1kwd1M1SjBUNjVPejAyYWgyazlCYWZzY055VmNiQ2I1bjV5dVpHbzJrdjFiVjRtc21DQU1tMXBta0dxaFlrQmF1X2hiTDN5RlktSUtwV1UxbnFlNTZxaV8tVGtWTS1JZWpkT3lXM29FSlhqWE83QWpKRVpfSkxnd3Z5MkxwbGlycEZTUV9VamRWM3l1M1ZvazFBSE1PR0E?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNX21BUzJKcno4QV9IY3F5QVlpNTVYaUVlbmpUeVlzQmdjcUVrQU5ucUNTdEFBaXF2VnBRaWxDcHIzSlJKNGpDdmlNdHJweGJpN1p1cWN3TFVPZmp3Z1BQb29uQjJqSm9ENGZzTEF3a0d1V3NkOWMyMjFhdjQ1UHlBanhhN0gwSU80T19IWEpQWmN4OTk3MkRvY2F6dw?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxPRGowX3ljRUhFOUtMR2diRUJHR2xTalpGZExTNFRKTExUQTQ2cUtNQXZfWEVRM3BMYldsOEh2czRtSmJZVExCakN0Q2VaWVRWWmFSYjRsRFBqNzRucXh1c2pIcW84aDUzdkhjY3pyZFFkVjRSN2gzU0dNM1NEWXI2WHIxdXl0OTB4OVM3QVVsSXg5V2NUQVVLVmZJWURyaWhXOUxyTWE3cm1qVXRQTFktZWQ0Y3hmaWlaenFrTi1jc3ZPSTFlWUVEbXRaYUVQOU0?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPRElTSFhVQUZmVlR1QXFPRko3NkRfbUMwdWRTdWxpcjBmenpxbnJja0ZEOFVQU19DZURySnM2NDZJc25wMFQtdV9jd21RYVNXT2tNaHl4eU9nSmw1TzhWTF9GdmhwMlFnMloxOC1hZEMwa3VtdG9WY1dRTVdpQXdvQlQ0NjJaakUtd0JzcUZ6OTRLRzNvU0I0?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQNVc4amE3bzV1cWF4SGlwOVd4UnNZVTZ6c09GZE42VDZiMGRkTXhiMDN6MS1lYzlfRzVHWlF2eVA4R0VlVlBBakREZ3hzSy1PVjBXWFdhSzEzbkVqdUtOc2tMUUN1eXJLNmhlNnJhSWE1Yk9PS2FhemlWalE2clE4aHB4T1NGcEJyeFVKNUdSbUY0UmMtMTh6aEIyR18?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxNOWk5b2U5UXB0UncwYlJpQWRFZXFLMjZVSE9JS0JtUEVpQ2E3SjBVRS1EdzkwUW9RTWRHbVpEMzhtQldCTXJJZ180aVVUVGg0Q01XN3FhdFMyMGN3TGJoSk1CY1J1Vm9BWEN6dmVpbVotR3NKT3RJNWJJWkY1UllFSUQ1VGtQa0JKV0N4V1J6eHZNc1FwZmk2VmdpbXRJX3BtTWhF?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxPaFpwMHBHOFV1MGlTNjNSTDdpcFplOWZZTS12a25wak1qTHJwNEZWX2w3WkxPUFpLMlJYNUkwajlWZ1pPWFVaODFjTDJval9PT3QyTmRqN0FyeTZ6U29VanRSTUtxdVE2bVplTFF6N0FfMU43dzhwRURIOWVDNGl4MjdNX3FtZ0dGV0ljMGJzenFmM19TeHRiQ2FPOWM3QnRVV0poOXBFVnFXMHBycGpxakJtbkwtczBONXNKekxsdTNUclBMUlE?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQNTJucVZFZS1YZmtjQmcyeDNKV2dXN0o0cThVZW1IWFQ1SU5KOXR1QlNSM1lEeTUwSDEwcTlrdlZsRjRNZ1pqb0JSWVVfal84YkhDUFpTUWFSM3VjYnN0UEpVX2Mxdmd2bUdhUXBKYU9GWWNBYWZFNnp0VkRlcXprZUtrQWYzS2htNDI3b0ZMQkF4QXJXV0ZQRDJjRk0?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxQeHRJRmZaWDY1TDNwelllbWd6OUZiV1NzaEllNG9aekhVYVVGWWhOREZuczlHQzJEZXFoeUotM2wwOW5ZTEJTOWlkb2JqSV82U2hmU01GeVhzYVlmZDZVYVFMZFo4UTNBenhOa0N4ejd0bkczZ0Nsa0I5YThHbk9iVGFkWlHSAYoBQVVfeXFMTlpCeWpuYTJhM2NHaUxJc2dkRlVSQUZ4TWxuUjh1QU1NOFE0WjJ2QUVlc0E1VWhjLUZZeGJGdEw1emRmWHM1aUNXSDdjWGRXMUhGLXJXMEpqaWlZSjUzTmY3b3lVTWhSTENiV0M0WjNZeGJTREpab09JczdLejZRTzh3SGNZWGxGVUZB?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxOQ3dVdFpzWVhUTWdtVnNVUlBUNVJLVnpQOW95eWRuc1FxZkJIUGdUMkwzeThoU0QxWFFDLVBHbkgxWUhlZjNGQmZnREdzWTVscU04MjNJM1NzQXJKaEl5TlllRU52NGJPaU9jTWMxMnozeVVnVEtjU3NzZGJCN09nR1J5dTdrVG0tb3ZEWjE3Y3pjWHo0a2kzNFB5SXZfR2hlaWwzLVpBTEZHVWFPZWJWS0Zqei1qS1pIZ2M1ekF2NjhCNVJSbC1BZQ?oc=5
- https://news.google.com/rss/articles/CBMingJBVV95cUxNVjJKRThIRnJiTkxmT2NTMlJKbjhMWXhOSlhVcWRDUFNwYXRwUUlwRzJYZ1lJWFpqOVk0RUFqTFRtdmY3cVNscUxMRDVyVFFnLUxfdFoxX29KeW1iODB1d0cwVlVObjlIU3RvaUdDMFpJUzd5OXhfZUZCWkhKZkFRMEl6M3o2S2tIbkVVdngzVE5wcDR2d0Q4eWFqVXZScGlPQmFTTTNsdExXNWNDZXlXdF9UQ3ZfX3lweU1aMU9FOWthV1pYNEJabUNvb0Fna2dnM000dUdJbEFTOWU4UHhtZTExU1VqSi00V2EzUWwyemk3R3FlN3pEeWo1Uy1nU0V5ODhSMlh0SG1pMXpZS2FYLUJ1V1FtLTZDSnFOS3RB?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQY01YWkJBY3Roa2hlWkVsbHhpcHplMm5NX09pWEJlMC1rWTY1ZDJoTUh0elc0WTZvdmpDOXJhS04tN2J5Y0N4NmZPdGk0aUhKdVZLT2RMSTk4S2EyZEJMYzY3WnpMMklfRjF3ZEJXZzU3d1VBTmlWS3Y1cllaYURseVQ4Nl93RFVLOXB4M1J6bnM1YVQ5QXBaSDZCOXEwUQ?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPUHhPNUFLeEpOMmNseG40aV9MMzVpTlhDNUxqOGo2b2lkUjVrUTlqRkQ4QTNxWDJGcTZuM3I5OUJGZzdSLU4yVnVsNkltdUxTQmRFeGNTaUctYUVFNkJ2cFJ4MEkyTHN6Tk9EQXVwcDdEV0RCaUZpaTJDTmVDYjdOdERVVVQ2ZWNLa2d5ZjdvTjRyRVJTZ19lYVoyUHlZYjZ5?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNbzB5dGpZSkhYa3cwUHkyT19vMUNERzA5MXJhUWtjZFFfWDYtXy1vLU16S0huQzhBSzVCXzBjdmpQUlVNOGFzUlN6RndocmtyQ2V0WF9KTmdoYkQtWkVmVVNYYVM1NFVNN210aHJCZWU2cnA3d0o2ZHB1LWgzOTZqbUZjYUdfMVRFclU3UFhtVHV4ZXlzTkZ1YVd5aGI?oc=5
- https://news.google.com/rss/articles/CBMigAFBVV95cUxPekh0UHV1WThuLTRORUgtZ3k5QnUtTnhnOGQyS3h3MUNvbi1LRmtINmJsSWgtUWdSakZmR0lLeHkzcTJNRTBZcDFqTkJjTlBPRjJLbF81VmJfTkljdU5Vb1pyWDg5NWhYVFVSUHBybkRjTlRRa0p4UFFPbkpHY2ZreA?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPZVdZcFBSMGkxLVlwRWhHVDNnSkxsLThrQlBNYUJWbVpoWlg3a0w3amZPZ1RwQUVPVkUxemVxSVdXdVRIUkRHcy13enFGM3NiU1ZXOU5YaVA0M2g2amk0T0NSSW1QREc5bUhzbEJMOURZMXhoR3ZIVHFzaWQtMHVQT3lOSkpDTFhHb1NLMU8zR0xvMjRJbmRGZzhEbHE5WUY5N0l1MnFfWQ?oc=5
- https://news.google.com/rss/articles/CBMi4gFBVV95cUxPNElWbE1lOVJadXoxSXhxYy04M3B4ZG9PeWhIaW1lZE9maF91M3N1OXd6eFhSSDJZcVlkMm5oZFdoeDJiaVRqYnJBRVkzczJ0TG1kSjFVT0Y1dG5iV1JMS0NPTW9oeVNlYXZZS0haUThFQVNlcnhJbTlMTjAtZ1pQaFc5WDNhd1VDTFVqY1dDOF9NYlRhTE9xamFUdkpBVVo2MlIyOXJsYVdRYVNDV0RCTDRBS2dKRFc1YkR1Tnczc0VSbGNUX21pRTFsWUpDR0dNMmpLT2V4UmtheUs0WWs2YXRB?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
