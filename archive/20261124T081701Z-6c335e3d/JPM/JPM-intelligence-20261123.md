# JPM Intelligence Report

- ticker: **JPM**
- Report as_of: **2026-11-23**
- Market data as_of: **2026-11-23**
- Quant sources: https://finance.yahoo.com/quote/JPM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/JPM/key-statistics/
- AI analysis snapshot as_of: **2026-11-23**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-24T08:38:19.963975+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 3, 'ai': 19, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **11** exact headline/source/date matches; prior report **20261123T053847Z-45053549/JPM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **3**; {'short_term_price_move_in_structural_risks': 3}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 12 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 20.83%; oldest publication 2026-11-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 316.6600 |
| Return 1D (%) | 1.9740 |
| Return 1W (%) | -6.3718 |
| Return 1M (%) | -4.4997 |
| Return YTD (%) | 0.1672 |
| Return 1Y (%) | 8.3011 |
| Annualized volatility (%) | 23.2064 |
| Beta vs SPY | 0.7708 |
| Max drawdown (%) | -15.4717 |
| Sharpe (rf=0) | 0.4626 |
| Downside deviation (rf=0, %) | 16.7766 |
| Sortino (rf=0) | 0.6399 |
| Historical VaR 95% (1D, %) | 2.4568 |
| Historical ES 95% (1D, %) | 3.3659 |
| Correlation vs SPY | 0.4974 |
| Tracking error vs SPY (%) | 20.4226 |
| P/E (trailing) | 13.28 |
| P/B | 2.39 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 10.20 |
| Forward P/E (estimate) | 12.38 |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 44.79 |
| Return on equity (%) | 18.01 |
| Free cash flow yield (%) | N/A |
| MA50 | 336.1733 |
| Close vs MA50 (%) | -5.8045 |
| MA200 | 322.8761 |
| Close vs MA200 (%) | -1.9252 |
| RSI (14, Wilder) | 36.8736 |
| MACD (12,26) | -4.8268 |
| MACD signal (9) | -1.7294 |
| MACD histogram | -3.0973 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'JPM': 288, 'SPY': 288}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 316.6600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.9740 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -6.3718 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -4.4997 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 0.1672 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 8.3011 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 23.2064 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.7766 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.6399 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.4568 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.3659 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4974 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 20.4226 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.7708 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.4717 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.4626 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 12.3826 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 44.7880 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 18.0130 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 13.2827 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 36.8736 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.0973 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -5.8045 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -1.9252 -> Slightly below the moving-average trend level.

## TAILWINDS

### A property insurer puts $250 million into J.P. Morgan's new global stock fund
- Summary: Insurer invests $250M in JPM's global stock fund, supporting capital growth.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxQQTkyOEx3VGhEZDlSckZqUl85UzY1NmthY1p2V2dKWnBlTDNiM0FNczFCaENucVZTdWszNTU4QzNaTC1xT0w2LXhZakVGbXplQ2V2c0lyOTFrYWM1OWdvS3lxZ3lHeWFNX3FBTjcxVGJmTmFoNE9vc1hmMTNFY3ZXbFRYZGIxSjIxemJmMXlUbnJ3UExQc3dDUENDMmxlS0xXdjVTYjJ3TnViOTNvVW0wVE9GMUxsYlVfTnFnLWlR?oc=5>

### 105,134 JPMorgan Chase & Co. $JPM Shares Bought by Private Advisor Group LLC
- Summary: Private advisor buys 105,134 JPM shares, indicating confidence in the bank.
- Date: 2026-11-22 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxNOGtpX1VWZm9ELWJOcFdFZ29pajNkSmJoWjBRNHZkVVdpQXJ5WE9wMlFtdDh0eFV1NlhKajZ4cXl0aHJuTEZPMFdNVVdqelduN0RxN2NnTkpxUjljNDN5RmlWZU5MS3ZXNEVvS1dPTC1HTHFOVjdRTkhqcTd4TDNwZDgtMTR3ZW9XMHk5N1V0TFBrRVV6ajgzUVVCWHZfQUJtdzBITWh2MHdlUVZrZnE2NEJwbGdoeC1kckdRUWlBYjVGWmhlYUVhblRFN1k?oc=5>

## HEADWINDS

### JPMorgan Chase (JPM) Stock Falls 1.20%: Near a 3-Month Low
- Summary: JPMorgan Chase (JPM) Stock Falls 1.20%: Near a 3-Month Low
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNUFNUUHBZUmtqMHgzWXVaNGU2WWJOdXdiVElSVTRjZERZWjNPdldzQVVTamh4OTNwOE5fc2RDTDhLVGZoMTQ3UXJHVkR1ekd2aHB3OEJkdVRaMUl1dndrS1RIZV93RzRMall0aXAxa09jYWpMOUFPU1pyRHJHSUtRMW5qaHQxdVpfQU0wdWYzZGdXY2ViblZZaA?oc=5>

### JPMorgan Chase (JPM) Stock Price Prediction: JPMorgan slips back toward support as analysts stay constructive but momentum softens
- Summary: Analysts predict a dip toward support, signaling a short‑term headwind.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQZndENWhIclE5Z2ZvZDhzSmt6WHVLR3dkMkNCcC0yV2VqTVRmY3h5OUxEOWhOd3F1UkFJMGtEeE9JWnRNZmNWRkhQMmFZdVRMMkROcC1pNndpZ19hQzlNQVYtUnlFY0xXZTFPell1Smw4ZVhBNnpLYlJqaXZrQy1SR2w3bFNfT2trZjZCVjY2UlVQaG1CMWthZ29JTUQ?oc=5>

### JPMorgan Stock Slides: What's Going On?
- Summary: JPM stock is declining, raising concerns about its short-term performance.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPY25wTkZqdFZDWF93OFdXcFRsSmJWM0oybzR3b3N1OHZ1bURYVjlFZkoySHhQVkxrNjluVTBqQzNIQ2pGWGQwN0ZheXhvbk8yT18xQzYtaDhnSVJYTVA4VVQ4eUNkZDFzNDc5TW1fMXZsMzRGR0FnelpUaVZLeEhkNnpPd2RVLTNncEY4SGluTVA5dE5IbnF3aFFFdFFSQQ?oc=5>

### Third-party vendors of JPMorgan Chase, Visa, Mastercard reportedly faced cyberattacks (JPM:NYSE)
- Summary: Cyberattacks on third‑party vendors threaten JPM operations.
- Date: 2026-11-19 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxNS1daVEN0SlZtVGhOUjZxSTI3TmhybWJYN3dIMkdOVUtYck1LQjhyRUNsMkdhMXo5dWFtUWRxUnVROFloQzI1Y3ZNRWpURFZwakNWM041ekhjTTc2c0JJN1FjRDdST3E4OUdWSk1SdERfWW00aUp6QVl0Q1dHTnNYMFlXQ3JNd0szM2hvSGpyOXM2dlFfR2NwV1VpVXRaS21FLUxzQ19DOHJkNXpNV3V2Uw?oc=5>

### JPMorgan Chase (JPM) Says Vendor Cyberattack Exposed Customer Data
- Summary: Vendor cyberattack exposed customer data, raising security concerns.
- Date: 2026-11-22 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxNcGZsSnc2NEFiS2tDdllhMmJ2V243b2lyQ0pUdkQ4SUpEVjlZakFtTlg3bUxVanlBWWh2RnFEd3dyaXBtOS1Eb2xmbDdWQWk1SWVoay1RS1FCQ2VYdXhzLUQzc0lCUGZySWdQY3EtOFVKc0FPV1h5dTd1MXFieW9sUkFPa1VST3NwZ3NKM0d2U0U3Rm1sOUpuOF9fV0E5WW0wenp5N1hTNmZqU1NCRTNNRGZReXFTTWtNQUQ3bmFmNjMxRnZj0gHKAUFVX3lxTE9lUXloUGRvaXRMdVhyc0NNVnVGYmVaVERkdGpLbEFCUGQ1dG9Rc3IxZUZVNHFOZWJYZmNXMUxudFc2dEZHYk5hY0lDSG9QRk92LWszOUhyeHl0YnljYzhtRlhiS0pLSTdlUkNVWkhfTDZQVlBIS0tjSzFxd0hCYVV0blM1OEg0NTZQWFJlc0FZaXlRN2ptOEZBR0hiUi1xSmZ0MVozUkpKa3BaM1VRZy1IZkpqdkFocmE5MlRreENpSjdUN0hONjFYeHc?oc=5>

## CATALYSTS

### JPMorgan Chase (JPM) Receives a Rating Update from a Top Analyst
- Summary: JPMorgan Chase (JPM) Receives a Rating Update from a Top Analyst
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3wFBVV95cUxOWjcyUFpnWTZMQVFNdFcwaUhIak9LQnczREtpTjNLLTlYblJvZWp2ZFhWWS02VDdmZTFKMHVDcFFkaEk2S2RwYlFLVzV0ODkyUnNQeS1oeG52T0lSWXVnQk5rR3R1bThpYWVzVG1Dc0s3NkNhRmtHMzJBTUVyRHFyYzZ2dEJXcHVZRk5JVzdkeWN3ZDhyUU9HSWlUdjBZQTVaNTNIR1ZLcV9yM28tRUZmUmJ2UmRHeHBlaldQRXIzdnU4WnFnMy14RTFoNG5IWWJGM3ozNE01b3RISk8wM1RB?oc=5>

### JPMorgan Chase & Co. $JPM Stock: Cibc World Market Inc. Cuts Position
- Summary: JPMorgan Chase & Co. $JPM Stock: Cibc World Market Inc. Cuts Position
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxOVG1uRXlnZExYY3JUM3hUbzM5SVdzbmZncnJyZEZZWXUwd1JWZ01hWE0wckVPYVlKNGpRMUxMWmw0cGs5eXc2dnZUd3I3SUtVSDN1U3dod1J6WFhtclVZczBUYk9hcDV2Z0JoTzIwWS1XcW5aeng4R3V4dWh5UmlRaWtmMlZMZkI1bWVCQ2I2d1lVb0R5dS1jdmNWMEdGVWpVTndnRnBhVGxpOWRpRzNaMGR2MFVNUkQ1OThrbU1nVHVlUQ?oc=5>

### JPMorgan names Bregje de Best as next CFO, succeeding Barnum
- Summary: JPM appoints Bregje de Best as CFO, succeeding Barnum.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxOX0tJbXd0el94UVZKU2p6S21CdUVKUHRsWHlkajRucjlZZkt0SjRRdWFER3E1aWFNMFNQUTN5T3oxV2hKVmZuVFFuaVNUVFFUQnd6S0NCTUN0V0xweVRMT2VOYVoxeDR5aF9qem9hZ0RJamhPVDZhQ2tUREpucHBHWnZ6eGozRUxNUjJqSENtNTUyWDhramFOQWV1RldqNXczME5USE83cWYzMWQ5WXhqUnF0dw?oc=5>

### Why Is JPMorgan Chase (JPM) Naming Bregje De Best As Its Next CFO?
- Summary: Appointment of Bregje De Best as CFO signals leadership change.
- Date: 2026-11-19 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxQU1ctTHZIMkJYenpSU2NxUHkxbGVHbzFaUEM1czlaVG5sN1F6VWpwbEpPd0NxTjFUUGlLc1ZVZDBLVGdEa21zTDRET195R29IM3U4TkdlWDFNWjlFeTBYZVM5aFVkM0prdGI4RWJUUUtrYm43a1BjdlFGSkpRRXJlbDlUbnpkSXl0NUJlcGp2aWZCR1k5eHFmOVB6VFgyTG10MWRqMXc1ajRMZ294ZUN4MUpJWnR1MXVmMUJHOG5GM09DbmZi0gHKAUFVX3lxTFB2Y1poVVNOaVk3cHE1eExtbW91cFQtQ3JmRXRoMVIxb3kxRVo5QXctNUJSNDl4dVFRejIzTndFMUVKd0hJMDZ4d2d1NG9sRktXUTdRc1A0d1psSkRaNWJuRUVEQm1VX1ZaRF8yMEN1MWVDTVQ0U1RtVWFEMDlCLWd5N3FvQWJreXFXaENUWENkYlM4ZWpkNlFFRnJrYzFJalhsdndERE1LUkNxeVQ0SWN0bGdCOWdpRWs5MjZiOUo3MzVLbDFPVktMN1E?oc=5>

### Investors Heavily Search JPMorgan Chase & Co. (JPM): Here is What You Need to Know
- Summary: Search interest spikes for JPM, indicating heightened investor attention.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxOTi1Qa21zWU1iRlVjR0ZvUTNYYnNHQjNucnBpWFZlYU5MSmZuTkxJZ3c5ZGFlRWJRODl1cWs2dzBNLUMxNlhpckotWmNua3NQMlN2OVdCTXVUMGQyN3R5SExOM2RpOUJ0QURHeUFYN2dpeWxBUVowZ21Sc2lpcTh2d1lfRGl1YXpETGE2cjR1NHBvUmJIa0hBSURUY0dmUFpDZVVOMFZvRQ?oc=5>

### How Many JPMorgan Chase Shares You Need to Collect $6,000 a Year in Dividends
- Summary: Dividend yield calculation for JPM shares to reach $6,000 annually.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxOc1o0Ymh6eXVPYVpva3lEMWYxTmF5eTFRZnFWMGI0VEVHR1dGTERpSlZlS2RzZXhYajlreEZmeTVkSHl3dEVyZzllWFdPZG9HX3lrNWNMeFhtcGl3Y0RGeGZHTkNrN184XzFLazVEcDc2M1NQOERrRkJDSUxYR2lXQ1ptT1BOY3lSV1paeHdpaURHVEJTbVNneDhQVmpjMENoV244aU1mUER5RDNYS3VwRVdPRm1PT2NNVUVr?oc=5>

### JPMorgan's bond fund will leave the NYSE on Dec. 16
- Summary: JPM bond fund delisting from NYSE scheduled for December 16.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxQX1dLNXlUSHBhdVg2NGoxcFQtSEtoc3lQSWpFNm1UVDM0LTItbVBfajBHY0ZzdS1kcTJFU3RuYTk4SDRrdXBkbzNpaG14QUJNTWhmUE1pdGphVUF1d2xnOE5NT0h6Q2lXb1FQakYwTWFJWnBoTTNyRDQ3N3FUTzNPeGRfVnluc0t3bDJuOXpidVZlMHJhLTBuV0dQNEsxWkxESWVjQXRMY3kyOUVaTkZ2SGl0Z1V0bE5iZVdV?oc=5>

### JP Morgan Chase & (JPM): Auto-callable note tied to lowest of three indices, due 2029
- Summary: New auto-callable note linked to three indices, maturing 2029.
- Date: 2026-11-20 | Impact: low | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxQMzdFRGdmS3hBaDZSZ0xKRW5sZmJkVDdqbEVtTVJrblZveHlpbVRlZzc1OWhDSVBsNlVNQUxmM0x3dUpScmVfNTRqT2hncFpZU1U2U0Vnc3g5TEVjLXlreHcwdkFUWVhibktJa0xKWm0zZWw0ZHRUemV5aEgzdVpqVjZnWXJUMHBHalRJ?oc=5>

### JPMorgan Chase (JPM) Stock Price Prediction: JPM trades below key moving averages as earnings and analyst targets frame the setup
- Summary: Analyst predictions suggest JPM may rebound after earnings and moving average analysis.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOdldqM3RqTTAwTWMyZWl4OWhvUjcyVkFSVXdsRDZYVlNPbEpzUFJSd092RFoxNXhJanFhVzMyb01aaWoxSUVwc2p1N1Q1a1Z6dE5POFY0d25uVTFCbWE3QXJqaTRJbUl5SEdmWHBjelBRY2xEUFRpR2xlRGtsdlU0VVNEc1FpQWt2OXFaU0g5SEFfSTNFX3RUOUlsOA?oc=5>

## RISKS

### JPM: SEC Form FWP filed by JP Morgan Chase & Co.
- Summary: JPM filed a Form FWP with the SEC, indicating a regulatory filing that may affect compliance or operational oversight.
- Date: 2026-11-20 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxOYmVEU3hCOWtMa2E2SEFnQXp3M0ticXpjMm5zY2tPWHNNWGt0MTBncTFlbUh6VnJhRWpFazBLbU5Kd3RMSURiMWI5Z0N5WnFVbFI4cHlvTVZhQmU4U2tTSVVPa1MzWWtLUG9xdGsyWlBGaEFtYWxrNWloLWZ4VEpsSUdYempUSUdidjN3?oc=5>

### JPMorgan Chase (JPM) Stock Price Prediction: JPMorgan Chase slips below near-term trend as analysts stay constructive
- Summary: Stock price dips below near-term trend, analysts remain constructive.
- Date: 2026-11-19 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPWTNzZ3lKRnN2X0JxRWRNVXJwSmRPcGxEbWtkQkNEUGdhbjdaTWdLRU5OVkd1ZGZ5c3NzNHR1ZE5xQjk5RHpZTVIzZTVYM0dPSkE4cTJqU21nVVZWTTdHOFhCek13QnRDa1BKV25jemlaSFRxWEh6S3NwRkI2cG1keXdYOTV0aWQ5cGJ5djZKWE1uWW91MHFHaC1zNA?oc=5>

### JPMorgan Chase (JPM) Stock Price Prediction: JPM slips below short-term averages as buyers test support
- Summary: Stock falls below short-term averages, buyers test support.
- Date: 2026-11-18 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOWkRKU0VmTHNZVTEyVTBlSzFJTDhLOTJZbGpSc0V6bTZOOTFlOHl0QlgyQlI3aFUtQTNWdG9pN0dRTFQ3OC1CaV9nTXB0c2NCSWVVTG1QVkwwelZiX1M2SkpuNDRjR3FBaDBqMW55RzlUYnRFaWd6ZENsb1pzLVBCQ1JleVdyUXdUMlZNSVZDZGxVTUJLZ3JLS1hB?oc=5>

### JPMorgan Chase (JPM) Stock Price Prediction: pullback tests near-term support after strong quarterly results
- Summary: Pullback tests near-term support post strong quarterly results.
- Date: 2026-11-17 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxORUE0cjF1UmlhQzgxRWFFbk1Ud3JZRjc0a1RvY2gxTXh3ZWdONTNIZUVHcU5WODZjc1FBLThXRzItNjdXWnZuRUJiYzZVYjFSYmF6b0dSa2hwLThLN2FDdmx4ZTRwQkdaRHhkNmQ0ZFRKUlZlVHVmWlFrZ2NDbXh5QkEzUUhsYklTWHBZd01zTDRtOVZKdkVsY0tBcTUyQQ?oc=5>

### JPMorgan Chase (JPM) CEO Warns UK Tax Rise Could Threaten £3 Billion HQ
- Summary: JPM CEO warns UK tax increase could jeopardize £3B headquarters investment.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNUC02Wm1pYmVvVF9tU3VTaXcyMFBSdUdwbW5NajJoendLYmUxX05oMGRqbmVZRXctTHVhV0JHYUdPNElCMV9jSjhIT2JIdlpDUk5zdXpfUE1yT2pBWk5SR3M4UUtkTy12VWt0RHBrdDBNVDJDSWo5cWpLOGMwZlZSQlQxbzhWWDJjM0FHUmlNNUllNUE2VVlLcA?oc=5>

### Visa, Mastercard, JPMorgan Hit By Reported Data Leak, Payment Information Not Affected
- Summary: Data leak reported affecting JPMorgan, Visa, Mastercard; payment data safe.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNemtoLTNrQVB1M1loZGQyaUtzUkdiZDVHNDBkRF8waURYakthUVpueGRSUTZGMnc1VVlscGVLeEtZRl93V1hXNzR5VkhNcmg2SUtyOXBQQWlJZnFnU2FwYzZlNktrM3NReXJCVEtaYTV1b0g2ZHVZUFVZY3FPMHlfRWVrNHVVeTZKWWt3QnM2LW45ZVU3QmxzelF4SmRRYUE?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **JPM** | **13.28** | **2.39** | **N/A** | **10.20** | **840,925,315,072.00 USD** | **8.30** |
| BAC | 11.49 | 1.23 | N/A | 3.40 | 332,176,064,512.00 USD | -4.64 |
| C | 11.15 | 0.99 | N/A | 8.00 | 189,272,637,440.00 USD | 18.25 |
| WFC | 11.28 | 1.51 | N/A | 0.40 | 240,148,021,248.00 USD | -1.58 |

Peers fetched as_of: 2026-11-23; JPM reuses existing data (market data as_of: 2026-11-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-13
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

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
- Filing date: 2026-11-03
- Revenue (latest available single quarter): 24,246,000,000.00 USD; period 2014-07-01/2014-09-30; fiscal year/reporting period 2014/Q3
- Net income (latest available single quarter): 15,305,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/19617/000162828026069523/jpm-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMivgFBVV95cUxQQTkyOEx3VGhEZDlSckZqUl85UzY1NmthY1p2V2dKWnBlTDNiM0FNczFCaENucVZTdWszNTU4QzNaTC1xT0w2LXhZakVGbXplQ2V2c0lyOTFrYWM1OWdvS3lxZ3lHeWFNX3FBTjcxVGJmTmFoNE9vc1hmMTNFY3ZXbFRYZGIxSjIxemJmMXlUbnJ3UExQc3dDUENDMmxlS0xXdjVTYjJ3TnViOTNvVW0wVE9GMUxsYlVfTnFnLWlR?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxNOGtpX1VWZm9ELWJOcFdFZ29pajNkSmJoWjBRNHZkVVdpQXJ5WE9wMlFtdDh0eFV1NlhKajZ4cXl0aHJuTEZPMFdNVVdqelduN0RxN2NnTkpxUjljNDN5RmlWZU5MS3ZXNEVvS1dPTC1HTHFOVjdRTkhqcTd4TDNwZDgtMTR3ZW9XMHk5N1V0TFBrRVV6ajgzUVVCWHZfQUJtdzBITWh2MHdlUVZrZnE2NEJwbGdoeC1kckdRUWlBYjVGWmhlYUVhblRFN1k?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNUFNUUHBZUmtqMHgzWXVaNGU2WWJOdXdiVElSVTRjZERZWjNPdldzQVVTamh4OTNwOE5fc2RDTDhLVGZoMTQ3UXJHVkR1ekd2aHB3OEJkdVRaMUl1dndrS1RIZV93RzRMall0aXAxa09jYWpMOUFPU1pyRHJHSUtRMW5qaHQxdVpfQU0wdWYzZGdXY2ViblZZaA?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQZndENWhIclE5Z2ZvZDhzSmt6WHVLR3dkMkNCcC0yV2VqTVRmY3h5OUxEOWhOd3F1UkFJMGtEeE9JWnRNZmNWRkhQMmFZdVRMMkROcC1pNndpZ19hQzlNQVYtUnlFY0xXZTFPell1Smw4ZVhBNnpLYlJqaXZrQy1SR2w3bFNfT2trZjZCVjY2UlVQaG1CMWthZ29JTUQ?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPY25wTkZqdFZDWF93OFdXcFRsSmJWM0oybzR3b3N1OHZ1bURYVjlFZkoySHhQVkxrNjluVTBqQzNIQ2pGWGQwN0ZheXhvbk8yT18xQzYtaDhnSVJYTVA4VVQ4eUNkZDFzNDc5TW1fMXZsMzRGR0FnelpUaVZLeEhkNnpPd2RVLTNncEY4SGluTVA5dE5IbnF3aFFFdFFSQQ?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNS1daVEN0SlZtVGhOUjZxSTI3TmhybWJYN3dIMkdOVUtYck1LQjhyRUNsMkdhMXo5dWFtUWRxUnVROFloQzI1Y3ZNRWpURFZwakNWM041ekhjTTc2c0JJN1FjRDdST3E4OUdWSk1SdERfWW00aUp6QVl0Q1dHTnNYMFlXQ3JNd0szM2hvSGpyOXM2dlFfR2NwV1VpVXRaS21FLUxzQ19DOHJkNXpNV3V2Uw?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxNcGZsSnc2NEFiS2tDdllhMmJ2V243b2lyQ0pUdkQ4SUpEVjlZakFtTlg3bUxVanlBWWh2RnFEd3dyaXBtOS1Eb2xmbDdWQWk1SWVoay1RS1FCQ2VYdXhzLUQzc0lCUGZySWdQY3EtOFVKc0FPV1h5dTd1MXFieW9sUkFPa1VST3NwZ3NKM0d2U0U3Rm1sOUpuOF9fV0E5WW0wenp5N1hTNmZqU1NCRTNNRGZReXFTTWtNQUQ3bmFmNjMxRnZj0gHKAUFVX3lxTE9lUXloUGRvaXRMdVhyc0NNVnVGYmVaVERkdGpLbEFCUGQ1dG9Rc3IxZUZVNHFOZWJYZmNXMUxudFc2dEZHYk5hY0lDSG9QRk92LWszOUhyeHl0YnljYzhtRlhiS0pLSTdlUkNVWkhfTDZQVlBIS0tjSzFxd0hCYVV0blM1OEg0NTZQWFJlc0FZaXlRN2ptOEZBR0hiUi1xSmZ0MVozUkpKa3BaM1VRZy1IZkpqdkFocmE5MlRreENpSjdUN0hONjFYeHc?oc=5
- https://news.google.com/rss/articles/CBMi3wFBVV95cUxOWjcyUFpnWTZMQVFNdFcwaUhIak9LQnczREtpTjNLLTlYblJvZWp2ZFhWWS02VDdmZTFKMHVDcFFkaEk2S2RwYlFLVzV0ODkyUnNQeS1oeG52T0lSWXVnQk5rR3R1bThpYWVzVG1Dc0s3NkNhRmtHMzJBTUVyRHFyYzZ2dEJXcHVZRk5JVzdkeWN3ZDhyUU9HSWlUdjBZQTVaNTNIR1ZLcV9yM28tRUZmUmJ2UmRHeHBlaldQRXIzdnU4WnFnMy14RTFoNG5IWWJGM3ozNE01b3RISk8wM1RB?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxOVG1uRXlnZExYY3JUM3hUbzM5SVdzbmZncnJyZEZZWXUwd1JWZ01hWE0wckVPYVlKNGpRMUxMWmw0cGs5eXc2dnZUd3I3SUtVSDN1U3dod1J6WFhtclVZczBUYk9hcDV2Z0JoTzIwWS1XcW5aeng4R3V4dWh5UmlRaWtmMlZMZkI1bWVCQ2I2d1lVb0R5dS1jdmNWMEdGVWpVTndnRnBhVGxpOWRpRzNaMGR2MFVNUkQ1OThrbU1nVHVlUQ?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxOX0tJbXd0el94UVZKU2p6S21CdUVKUHRsWHlkajRucjlZZkt0SjRRdWFER3E1aWFNMFNQUTN5T3oxV2hKVmZuVFFuaVNUVFFUQnd6S0NCTUN0V0xweVRMT2VOYVoxeDR5aF9qem9hZ0RJamhPVDZhQ2tUREpucHBHWnZ6eGozRUxNUjJqSENtNTUyWDhramFOQWV1RldqNXczME5USE83cWYzMWQ5WXhqUnF0dw?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxQU1ctTHZIMkJYenpSU2NxUHkxbGVHbzFaUEM1czlaVG5sN1F6VWpwbEpPd0NxTjFUUGlLc1ZVZDBLVGdEa21zTDRET195R29IM3U4TkdlWDFNWjlFeTBYZVM5aFVkM0prdGI4RWJUUUtrYm43a1BjdlFGSkpRRXJlbDlUbnpkSXl0NUJlcGp2aWZCR1k5eHFmOVB6VFgyTG10MWRqMXc1ajRMZ294ZUN4MUpJWnR1MXVmMUJHOG5GM09DbmZi0gHKAUFVX3lxTFB2Y1poVVNOaVk3cHE1eExtbW91cFQtQ3JmRXRoMVIxb3kxRVo5QXctNUJSNDl4dVFRejIzTndFMUVKd0hJMDZ4d2d1NG9sRktXUTdRc1A0d1psSkRaNWJuRUVEQm1VX1ZaRF8yMEN1MWVDTVQ0U1RtVWFEMDlCLWd5N3FvQWJreXFXaENUWENkYlM4ZWpkNlFFRnJrYzFJalhsdndERE1LUkNxeVQ0SWN0bGdCOWdpRWs5MjZiOUo3MzVLbDFPVktMN1E?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxOTi1Qa21zWU1iRlVjR0ZvUTNYYnNHQjNucnBpWFZlYU5MSmZuTkxJZ3c5ZGFlRWJRODl1cWs2dzBNLUMxNlhpckotWmNua3NQMlN2OVdCTXVUMGQyN3R5SExOM2RpOUJ0QURHeUFYN2dpeWxBUVowZ21Sc2lpcTh2d1lfRGl1YXpETGE2cjR1NHBvUmJIa0hBSURUY0dmUFpDZVVOMFZvRQ?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxOc1o0Ymh6eXVPYVpva3lEMWYxTmF5eTFRZnFWMGI0VEVHR1dGTERpSlZlS2RzZXhYajlreEZmeTVkSHl3dEVyZzllWFdPZG9HX3lrNWNMeFhtcGl3Y0RGeGZHTkNrN184XzFLazVEcDc2M1NQOERrRkJDSUxYR2lXQ1ptT1BOY3lSV1paeHdpaURHVEJTbVNneDhQVmpjMENoV244aU1mUER5RDNYS3VwRVdPRm1PT2NNVUVr?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOMnBkT3FUcVYtT0FqZFQzMDlyVXJvTEdTbURIcko1MDBIT3VSVUpvWkRVTXl3ay1DSDJnVWlHNEIzZXpxTVJhX0l2Mm1nTXljMEtBdU1VakI3RFNfRjJyUXQzX3EwdndnNi1qYUszRmJLbWhMb0hNeGdWR2tjVDF2ZWNXNVBVVFhIaEhaTDVlazMzeHlFdVBYN3VoX2dhVVli?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxQX1dLNXlUSHBhdVg2NGoxcFQtSEtoc3lQSWpFNm1UVDM0LTItbVBfajBHY0ZzdS1kcTJFU3RuYTk4SDRrdXBkbzNpaG14QUJNTWhmUE1pdGphVUF1d2xnOE5NT0h6Q2lXb1FQakYwTWFJWnBoTTNyRDQ3N3FUTzNPeGRfVnluc0t3bDJuOXpidVZlMHJhLTBuV0dQNEsxWkxESWVjQXRMY3kyOUVaTkZ2SGl0Z1V0bE5iZVdV?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxQMzdFRGdmS3hBaDZSZ0xKRW5sZmJkVDdqbEVtTVJrblZveHlpbVRlZzc1OWhDSVBsNlVNQUxmM0x3dUpScmVfNTRqT2hncFpZU1U2U0Vnc3g5TEVjLXlreHcwdkFUWVhibktJa0xKWm0zZWw0ZHRUemV5aEgzdVpqVjZnWXJUMHBHalRJ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOdldqM3RqTTAwTWMyZWl4OWhvUjcyVkFSVXdsRDZYVlNPbEpzUFJSd092RFoxNXhJanFhVzMyb01aaWoxSUVwc2p1N1Q1a1Z6dE5POFY0d25uVTFCbWE3QXJqaTRJbUl5SEdmWHBjelBRY2xEUFRpR2xlRGtsdlU0VVNEc1FpQWt2OXFaU0g5SEFfSTNFX3RUOUlsOA?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxOYmVEU3hCOWtMa2E2SEFnQXp3M0ticXpjMm5zY2tPWHNNWGt0MTBncTFlbUh6VnJhRWpFazBLbU5Kd3RMSURiMWI5Z0N5WnFVbFI4cHlvTVZhQmU4U2tTSVVPa1MzWWtLUG9xdGsyWlBGaEFtYWxrNWloLWZ4VEpsSUdYempUSUdidjN3?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPWTNzZ3lKRnN2X0JxRWRNVXJwSmRPcGxEbWtkQkNEUGdhbjdaTWdLRU5OVkd1ZGZ5c3NzNHR1ZE5xQjk5RHpZTVIzZTVYM0dPSkE4cTJqU21nVVZWTTdHOFhCek13QnRDa1BKV25jemlaSFRxWEh6S3NwRkI2cG1keXdYOTV0aWQ5cGJ5djZKWE1uWW91MHFHaC1zNA?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOWkRKU0VmTHNZVTEyVTBlSzFJTDhLOTJZbGpSc0V6bTZOOTFlOHl0QlgyQlI3aFUtQTNWdG9pN0dRTFQ3OC1CaV9nTXB0c2NCSWVVTG1QVkwwelZiX1M2SkpuNDRjR3FBaDBqMW55RzlUYnRFaWd6ZENsb1pzLVBCQ1JleVdyUXdUMlZNSVZDZGxVTUJLZ3JLS1hB?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxORUE0cjF1UmlhQzgxRWFFbk1Ud3JZRjc0a1RvY2gxTXh3ZWdONTNIZUVHcU5WODZjc1FBLThXRzItNjdXWnZuRUJiYzZVYjFSYmF6b0dSa2hwLThLN2FDdmx4ZTRwQkdaRHhkNmQ0ZFRKUlZlVHVmWlFrZ2NDbXh5QkEzUUhsYklTWHBZd01zTDRtOVZKdkVsY0tBcTUyQQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNUC02Wm1pYmVvVF9tU3VTaXcyMFBSdUdwbW5NajJoendLYmUxX05oMGRqbmVZRXctTHVhV0JHYUdPNElCMV9jSjhIT2JIdlpDUk5zdXpfUE1yT2pBWk5SR3M4UUtkTy12VWt0RHBrdDBNVDJDSWo5cWpLOGMwZlZSQlQxbzhWWDJjM0FHUmlNNUllNUE2VVlLcA?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNemtoLTNrQVB1M1loZGQyaUtzUkdiZDVHNDBkRF8waURYakthUVpueGRSUTZGMnc1VVlscGVLeEtZRl93V1hXNzR5VkhNcmg2SUtyOXBQQWlJZnFnU2FwYzZlNktrM3NReXJCVEtaYTV1b0g2ZHVZUFVZY3FPMHlfRWVrNHVVeTZKWWt3QnM2LW45ZVU3QmxzelF4SmRRYUE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
