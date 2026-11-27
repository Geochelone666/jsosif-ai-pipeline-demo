# ASML Intelligence Report

- ticker: **ASML**
- Report as_of: **2026-11-26**
- Market data as_of: **2026-11-25**
- Quant sources: https://finance.yahoo.com/quote/ASML/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ASML/key-statistics/
- AI analysis snapshot as_of: **2026-11-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-27T06:44:59.182840+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 4, 'ai': 11, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **10** exact headline/source/date matches; prior report **20261126T064454Z-dbdd6f45/ASML** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 11 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 20.83%; oldest publication 2026-11-22

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 1303.0800 |
| Return 1D (%) | -2.4685 |
| Return 1W (%) | -6.6073 |
| Return 1M (%) | -16.9870 |
| Return YTD (%) | 22.5457 |
| Return 1Y (%) | 30.6859 |
| Annualized volatility (%) | 50.1032 |
| Beta vs SPY | 2.2424 |
| Max drawdown (%) | -36.1866 |
| Sharpe (rf=0) | 0.7858 |
| Downside deviation (rf=0, %) | 33.9159 |
| Sortino (rf=0) | 1.1608 |
| Historical VaR 95% (1D, %) | 5.0034 |
| Historical ES 95% (1D, %) | 6.6569 |
| Correlation vs SPY | 0.6682 |
| Tracking error vs SPY (%) | 41.6356 |
| P/E (trailing) | 32.06 |
| P/B | 1118.89 |
| EV/EBITDA | 1713.31 |
| Revenue growth (%) | 55.20 |
| Forward P/E (estimate) | 20.55 |
| Gross margin (%) | 54.34 |
| Operating margin (%) | 38.55 |
| Return on equity (%) | 65.64 |
| Free cash flow yield (%) | N/A |
| MA50 | 1608.5563 |
| Close vs MA50 (%) | -18.9907 |
| MA200 | 1596.5158 |
| Close vs MA200 (%) | -18.3798 |
| RSI (14, Wilder) | 36.2526 |
| MACD (12,26) | -81.3646 |
| MACD signal (9) | -72.6784 |
| MACD histogram | -8.6862 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ASML': 290, 'SPY': 290}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 1303.0800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.4685 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -6.6073 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -16.9870 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 22.5457 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 30.6859 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 50.1032 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 33.9159 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.1608 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 5.0034 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.6569 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6682 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 41.6356 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.2424 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -36.1866 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.7858 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 20.5535 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.3370 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 38.5520 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 65.6360 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 32.0640 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 36.2526 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -8.6862 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -18.9907 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -18.3798 -> Clearly below the moving-average trend level.

## TAILWINDS

### ASML Holding NV Stock (ASML) Moved Up by 10.09% on Nov 23: Facts Behind the Movement
- Summary: ASML Holding NV Stock (ASML) Moved Up by 10.09% on Nov 23: Facts Behind the Movement
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNUUw1aUVCMGN4bUpXamVoaUdhOGtvSGxZcFR4c2g5SGJwRWpsNzEzUFI5cmFoNDl2VkF3RWhIa2xBRGh3SEwwUV9wRzNkaGplU1hmZGxtdmpaWV9OTkFjcXRRdVM0Wi02MzdPbFFxcUV0OUEtcGstcUM0eTJRUlNtOUhEZnAyRGdNa2ZR?oc=5>

### ASML Holding NV Q3FY26 Results: Net profit €5bn, sales beat estimates
- Summary: ASML Holding NV Q3FY26 Results: Net profit €5bn, sales beat estimates
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxNeWxIdnZLMEVZXzhmbVBpcXB3WXk5emFOa2w5dkh3YmV6TktkWkxySEFuRXZ1VjM0amlRSVhGRUpvQzRWYko4YWRSZlAydmxBMDZwMWlQTWZVM2tmRHdfT1BJTTJjRFBkbFhONVY4T3VvUTZPeEhFZElYQmgyZmY4MmtWbWp3ZThFdGZtUFhOZ0xVZS1aNFVLbVp0WUpGLWpNMmtZR05pLTdQVks5MkVmZm83WjlNTFlwallWakgtbFA?oc=5>

### ASML Holding N.V. (NASDAQ: ASML): Powering the AI Semiconductor Supercycle Through EUV Leadership, Pricing Strength and Expanding Capacity
- Summary: ASML’s EUV leadership and pricing power drive AI semiconductor demand, boosting growth prospects.
- Date: 2026-11-23 | Impact: high | Horizon: medium | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMi_wFBVV95cUxNa1Y3STZGTno4elRMSF9GS292V1pteXFUZjF3RmJZcXZlWDFtWERmQkc4WExsNHFfeE1IcnRUbm9sQzhRV1dwbC1wcVo3ZE1sNGZZTDBSMDVPREYwdzFWOEhrZUZxc2hPWUtndjVQcU1LbjAxZUlUMWY2c3FGZV9Vdm4wUXdZdUFseW1OWEJCZ1VOMEowcGhoWlNhdFNjdGlNNkN6bFRfb3doSjRmZTk0OGhwQ3NMV2RMaFdqb25fbzVKM0JFRjlnTjhOekF4bXFJRkpfNTQ5eVdLbEw4VkZ0b0oyNkdiTFJqRC1pbjJFbm5wY3U5NFI2N19panVkVmc?oc=5>

## HEADWINDS

### ASML Stock Fell 25% In The AI Selloff, But Its Outlook Hasn’t Budged (NASDAQ:ASML)
- Summary: ASML Stock Fell 25% In The AI Selloff, But Its Outlook Hasn’t Budged (NASDAQ:ASML)
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxNS0xMdThabnAwMURidkl0a3A3alJKVzN2bnJTdThoMUZFQWdaZEEyNGh6OXJmQWQzSXlKM0Y4ZTN0bmNUdmVxRDY2MUlXWmVnNVNuU1VYZEhUMHdKcXlQbHZzMDBER2hlTHhfd0NWVmRkQnA5cHhBb25FTHUwTkpnU3JhQzF5dlNKZ3ZPd1RSR09lZXZkZERYc1FORkhCSlZERlBQM2xPQkg5ai1YMHF1MGFGeV8?oc=5>

### ASML Holding NV Stock (ASML) Moved Down by 7.01% on Nov 25: Drivers Behind the Movement
- Summary: ASML Holding NV Stock (ASML) Moved Down by 7.01% on Nov 25: Drivers Behind the Movement
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxOU0g5ZEFIeE9tY2hvbW02TjZ2akZKQXllWlUzTFVsclJfUi1nQU5XT3lrQWhOUV9iWHBZTk5IVkxqaElLYUpZTUQweE1CeTFhQlR2R01FMzVRTGFGYnc3Q183bUM2T2V1aW41MVJhYk96S1F0ZUg3VElOVUFuZ3hIamptNjA0UF9QLXdz?oc=5>

### ASML Stock And 3 Non US Chip Equipment Names Investors May Be Missing
- Summary: ASML and other chip equipment stocks may be undervalued, suggesting potential upside.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxQN2pMMFBHQnFUQ2Z4TUlZUnAzMnc5NW1xanBvRHhtWmoyeUVVSnMxa2xoc2FJUmJPcjFiTTZyU2lUajZMSkFLbld2ajJpRXFnaXRUZTh3eG9mWF80VU43SHQ1Z3ZlU1pscGptZUhEOE9iWVFJSk0xRjI2UjhHMHVHb2FnTnJtekhqV29MUVA5TENIMldWSGxuMmhVVHp0ZWdvSktrcjFPaG9rUmM0MXgzVFNkWm5kbm1aUWlYbENiOExYMWRZTjRDWlE4QnFIaUY2MDJ1V05MVUdmb1dvZGF4cC14bkJHUks3NVZEVtIB8gFBVV95cUxQX1F3elZsN1VZa3pXdk5uZ3AtdFZJVUVMNzE5SkJ4T05TQ2lvWUZLNUtIUUc2bHBoRnJsLVVXQ2FlVkFtWGpEVzE3RnhsWjdzcFRjRjNkUjdleDNzMXBuMXFPZXFkWTZQRU5qVG1TQkdzLUNnUVBwMXBDMUFSLXBrVjZFamRGSXhsYnpIcTdTd1NyN3o3blZWVzd2alJ4SXNTZ3JiRF92eUFjcmMyb2x2cUhzREFXQjdfajhtT2xoS09WcTh4Y09ydnFMQ3RmX3pCQUhEeFlGaTlsb1pTdlc5ZDY1aW5QMkdfTTJtallLVHBQQQ?oc=5>

### ASML Sinks 7% in a Week: Dutch Lawmaker Warns the MATCH Act Is “Disastrous for ASML.” Time to Buy?
- Summary: Lawmaker warns MATCH Act could harm ASML, causing a 7% share drop.
- Date: 2026-11-26 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxQWV9sdldyOUpkRzVfRVUwZ3JrLURudVBwZU1lazgyQkxxS0ZEc0d0Nk9mVEdsUDRjUDdUUExROE5KbFlHWi16MXpwSXFCdU5lQUJ5MUl0cXpNNV8ybzZWV0c5NlFkSXhDcW1qaE5ua2lBaVg5elZlblhDSnRmSFExbWpRU01XQndTcEt5ZUJJTkMzM3RqYmpoaDY4bHREQWFudjd6dS1rell4RDVHRFZ2NnFQTjl4RjAtSG9MWXZETkF5TEdiZW9yRU82Zw?oc=5>

### ASML Stock’s Sell-Off Looks Excessive Against Its Growth Outlook
- Summary: Shares falling more than expected versus growth prospects.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNdm52d3d6elJwRHkxakZPOHRXOUE0UXlON29sVF9SUTBvT2dHc2t4NHZWVkRWa1dMNklCWWZkS0JnNTZiOHJSb2FrUXo0NlF4Z3FOWVA3N0dBbmk5djRnNWRFVnY1cnBQTU9VQnlIX2pDQUtxZ1RNWlIyR0xseTFzQlFreGZpaGNiV0dOeWtnRVdreTBM?oc=5>

### Netherlands Tells Washington It Won't Take Orders on ASML's China Sales
- Summary: Policy limits orders for ASML’s China sales, restricting revenue.
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPTWNSb29ZQlBNclFMV3dUQ1hVUGVEQ0Nxa2JZV2paemtnVDFzWXZXbENnT0JRUWJGZjZFckd5STBNakpkZk5NMnh2U29mNHA4amlUdEFDRmJjNUpmWU9pTUgxbUUyUnFOMFNGN2wzWHZ5ZWxlTmVhZnNuVUJPVHdjTklqUE9zYlVwc2l1SkZndXF3UkFsaTBMRm5qVDlzdw?oc=5>

### ASML Sinks 6% in Chip Rout as Dutch Lawmaker Warns MATCH Act Is “Disastrous for ASML”
- Summary: Regulatory concerns over the MATCH Act threaten ASML’s market position, causing a sharp share decline.
- Date: 2026-11-26 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxPRGY0bnNMWWxIaDJBMy16Z1JZSTE5b0FRZkVrbC1KZE5GX0NUbmMxb0pwWEV4VjdETUtKQlh2clpackJmSWJXSmZhd1g3U1VJUW5ZVzdlU1FrZkhZaWcyWEdCUmd5RnNSa05rNnUwRjBZNzNuRVRTWm9xZDZVWTVPcXZSM2plQ3Y2UnJPUkktVENBLVo0V2JfSnFoOXhvMXpSUlR6MDMxMDk0TmR5?oc=5>

### Forget ASML: Tokyo Electron Has More China Sales at Stake in the MATCH Act
- Summary: Competitive pressure from Tokyo Electron in China could erode ASML’s sales under the MATCH Act.
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxNRlhraXlxbFAzbWVsVTFEeUtXNGd2V0RESHg4MlVTekt0U1Y2NlRGU1hrQnZ1Mk9UUXRIM2cxbWxrMHhTV01SQXgtTVFydmhjWXdXaW9NQjBnb2VScHB1MVpFUnRINTF1RHZYQkRyUmQtd25UQzhhUjV6NjNlSldVeE00VlVMUC1sVVJ1dXR3emVpd2x6ZnNuYXlNS0pldTRC?oc=5>

## CATALYSTS

### ASML surges 9% as chip stocks rally (ASML:NASDAQ)
- Summary: ASML shares jumped 9% amid broader chip market rally.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMifEFVX3lxTFBDTHVWdFhBU1B6Y0RWNmxFZG13akZXdjZGUXkxb1F5cGY3cVExejRnNmQ1bi0tUGl1akRvNDR5Y0o3UmlPaFp4c1hfbEV5eWdyOVhrN3FXTzl0SThHeU9KeFVpNkJBRG54Rnp2THdTRk0za3hsUlI4eWtoWDk?oc=5>

## RISKS

### ‘Disastrous' for ASML: Dutch Lawmakers Revolt Against US Push to Tighten China Chip Curbs
- Summary: Dutch lawmakers oppose US chip export restrictions, creating regulatory uncertainty for ASML’s China business.
- Date: 2026-11-25 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxQdi1yQ1BMQ0FZeTFWcTN3RWtjaG1fWTJScHZidExKTWxqeVFxNGthTHNXa0NxMXNuRlAzU0F4Z2NlUzA2bEdPOTE2NXlRWmtEbEpZQV9aSW9pMklxN1FrSWpOODF1czN5QU5LbVE5RWZiYjY2b1otSHlmbE1OOVZqMmp1X1VfV3B4WnVV?oc=5>

### ASML (ASML) Can’t Meet Demand. Is That a Strength or Risk?
- Summary: Demand shortfall may signal capacity risk.
- Date: 2026-11-26 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxQVzlaZGR2OUNRV1AtMXNtNWw2Rm0zN21ldGM4WTV4dmlqQ05iODV6X2x1OVlPdlhyOHlvZG9EcHFtckpiUzlhbl9qbXNPRFBJdWRVbW1ZM2NCaHNnX0t2YW9hOXVrWEl1NHIyOHhmT3IxdktYSGlSelNkcHVGMF9DNnlPTHY3TjdxT0JXVmFEc2RPUQ?oc=5>

### ASML Can’t Build Enough Machines for 2028. Is a 20% China Risk a Reason to Sell, or Buy More?
- Summary: Capacity limits and China risk threaten 2028 supply.
- Date: 2026-11-26 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi6wFBVV95cUxOdEhBMWNBMmE3SzYzelhQaHNSNlNWSWMzV0hUc1pNNGFoNlBzbC0wQnVmeXpCVkJMbkgyT0l3bWl0N1EtZzlZNG5uNHJ3dnREaFhGbUlQMjF6Vkh5Z0IyeDhKNU5PS25ma0xFNDAxdU1DcUZTMlJYYzNlRXphY1dORkxrSGRuSFRxamxQcnJydF83NndlRXd0Ylh0dzdSRzJPaFBLc0FfeVN2dDQyMHJoeTZXVnlSNTExM0NNT2xIc3NXb1dWU3lLUWR1V28zUldQdXpHSlBGLU5GVHNwVjc1TVV3NEhfWHZJSG0w?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ASML** | **32.06** | **1,118.89** | **1,713.31** | **55.20** | **502,230,122,496.00 USD** | **30.69** |
| AMAT | 24.66 | 9.45 | 20.47 | 53.10 | 246,951,641,088.00 USD | 28.99 |
| LRCX | 27.57 | 16.62 | 22.48 | 54.40 | 231,109,115,904.00 USD | 22.34 |
| KLAC | 33.63 | 26.81 | 26.77 | 28.90 | 174,857,551,872.00 USD | 17.73 |

Peers fetched as_of: 2026-11-26; ASML reuses existing data (market data as_of: 2026-11-25); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-14
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-26

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: N/A
- Filing date: N/A
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: N/A

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNUUw1aUVCMGN4bUpXamVoaUdhOGtvSGxZcFR4c2g5SGJwRWpsNzEzUFI5cmFoNDl2VkF3RWhIa2xBRGh3SEwwUV9wRzNkaGplU1hmZGxtdmpaWV9OTkFjcXRRdVM0Wi02MzdPbFFxcUV0OUEtcGstcUM0eTJRUlNtOUhEZnAyRGdNa2ZR?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxNeWxIdnZLMEVZXzhmbVBpcXB3WXk5emFOa2w5dkh3YmV6TktkWkxySEFuRXZ1VjM0amlRSVhGRUpvQzRWYko4YWRSZlAydmxBMDZwMWlQTWZVM2tmRHdfT1BJTTJjRFBkbFhONVY4T3VvUTZPeEhFZElYQmgyZmY4MmtWbWp3ZThFdGZtUFhOZ0xVZS1aNFVLbVp0WUpGLWpNMmtZR05pLTdQVks5MkVmZm83WjlNTFlwallWakgtbFA?oc=5
- https://news.google.com/rss/articles/CBMi_wFBVV95cUxNa1Y3STZGTno4elRMSF9GS292V1pteXFUZjF3RmJZcXZlWDFtWERmQkc4WExsNHFfeE1IcnRUbm9sQzhRV1dwbC1wcVo3ZE1sNGZZTDBSMDVPREYwdzFWOEhrZUZxc2hPWUtndjVQcU1LbjAxZUlUMWY2c3FGZV9Vdm4wUXdZdUFseW1OWEJCZ1VOMEowcGhoWlNhdFNjdGlNNkN6bFRfb3doSjRmZTk0OGhwQ3NMV2RMaFdqb25fbzVKM0JFRjlnTjhOekF4bXFJRkpfNTQ5eVdLbEw4VkZ0b0oyNkdiTFJqRC1pbjJFbm5wY3U5NFI2N19panVkVmc?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxNS0xMdThabnAwMURidkl0a3A3alJKVzN2bnJTdThoMUZFQWdaZEEyNGh6OXJmQWQzSXlKM0Y4ZTN0bmNUdmVxRDY2MUlXWmVnNVNuU1VYZEhUMHdKcXlQbHZzMDBER2hlTHhfd0NWVmRkQnA5cHhBb25FTHUwTkpnU3JhQzF5dlNKZ3ZPd1RSR09lZXZkZERYc1FORkhCSlZERlBQM2xPQkg5ai1YMHF1MGFGeV8?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxOU0g5ZEFIeE9tY2hvbW02TjZ2akZKQXllWlUzTFVsclJfUi1nQU5XT3lrQWhOUV9iWHBZTk5IVkxqaElLYUpZTUQweE1CeTFhQlR2R01FMzVRTGFGYnc3Q183bUM2T2V1aW41MVJhYk96S1F0ZUg3VElOVUFuZ3hIamptNjA0UF9QLXdz?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxQN2pMMFBHQnFUQ2Z4TUlZUnAzMnc5NW1xanBvRHhtWmoyeUVVSnMxa2xoc2FJUmJPcjFiTTZyU2lUajZMSkFLbld2ajJpRXFnaXRUZTh3eG9mWF80VU43SHQ1Z3ZlU1pscGptZUhEOE9iWVFJSk0xRjI2UjhHMHVHb2FnTnJtekhqV29MUVA5TENIMldWSGxuMmhVVHp0ZWdvSktrcjFPaG9rUmM0MXgzVFNkWm5kbm1aUWlYbENiOExYMWRZTjRDWlE4QnFIaUY2MDJ1V05MVUdmb1dvZGF4cC14bkJHUks3NVZEVtIB8gFBVV95cUxQX1F3elZsN1VZa3pXdk5uZ3AtdFZJVUVMNzE5SkJ4T05TQ2lvWUZLNUtIUUc2bHBoRnJsLVVXQ2FlVkFtWGpEVzE3RnhsWjdzcFRjRjNkUjdleDNzMXBuMXFPZXFkWTZQRU5qVG1TQkdzLUNnUVBwMXBDMUFSLXBrVjZFamRGSXhsYnpIcTdTd1NyN3o3blZWVzd2alJ4SXNTZ3JiRF92eUFjcmMyb2x2cUhzREFXQjdfajhtT2xoS09WcTh4Y09ydnFMQ3RmX3pCQUhEeFlGaTlsb1pTdlc5ZDY1aW5QMkdfTTJtallLVHBQQQ?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxQWV9sdldyOUpkRzVfRVUwZ3JrLURudVBwZU1lazgyQkxxS0ZEc0d0Nk9mVEdsUDRjUDdUUExROE5KbFlHWi16MXpwSXFCdU5lQUJ5MUl0cXpNNV8ybzZWV0c5NlFkSXhDcW1qaE5ua2lBaVg5elZlblhDSnRmSFExbWpRU01XQndTcEt5ZUJJTkMzM3RqYmpoaDY4bHREQWFudjd6dS1rell4RDVHRFZ2NnFQTjl4RjAtSG9MWXZETkF5TEdiZW9yRU82Zw?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNdm52d3d6elJwRHkxakZPOHRXOUE0UXlON29sVF9SUTBvT2dHc2t4NHZWVkRWa1dMNklCWWZkS0JnNTZiOHJSb2FrUXo0NlF4Z3FOWVA3N0dBbmk5djRnNWRFVnY1cnBQTU9VQnlIX2pDQUtxZ1RNWlIyR0xseTFzQlFreGZpaGNiV0dOeWtnRVdreTBM?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPTWNSb29ZQlBNclFMV3dUQ1hVUGVEQ0Nxa2JZV2paemtnVDFzWXZXbENnT0JRUWJGZjZFckd5STBNakpkZk5NMnh2U29mNHA4amlUdEFDRmJjNUpmWU9pTUgxbUUyUnFOMFNGN2wzWHZ5ZWxlTmVhZnNuVUJPVHdjTklqUE9zYlVwc2l1SkZndXF3UkFsaTBMRm5qVDlzdw?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxPRGY0bnNMWWxIaDJBMy16Z1JZSTE5b0FRZkVrbC1KZE5GX0NUbmMxb0pwWEV4VjdETUtKQlh2clpackJmSWJXSmZhd1g3U1VJUW5ZVzdlU1FrZkhZaWcyWEdCUmd5RnNSa05rNnUwRjBZNzNuRVRTWm9xZDZVWTVPcXZSM2plQ3Y2UnJPUkktVENBLVo0V2JfSnFoOXhvMXpSUlR6MDMxMDk0TmR5?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxNRlhraXlxbFAzbWVsVTFEeUtXNGd2V0RESHg4MlVTekt0U1Y2NlRGU1hrQnZ1Mk9UUXRIM2cxbWxrMHhTV01SQXgtTVFydmhjWXdXaW9NQjBnb2VScHB1MVpFUnRINTF1RHZYQkRyUmQtd25UQzhhUjV6NjNlSldVeE00VlVMUC1sVVJ1dXR3emVpd2x6ZnNuYXlNS0pldTRC?oc=5
- https://news.google.com/rss/articles/CBMifEFVX3lxTFBDTHVWdFhBU1B6Y0RWNmxFZG13akZXdjZGUXkxb1F5cGY3cVExejRnNmQ1bi0tUGl1akRvNDR5Y0o3UmlPaFp4c1hfbEV5eWdyOVhrN3FXTzl0SThHeU9KeFVpNkJBRG54Rnp2THdTRk0za3hsUlI4eWtoWDk?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxQdi1yQ1BMQ0FZeTFWcTN3RWtjaG1fWTJScHZidExKTWxqeVFxNGthTHNXa0NxMXNuRlAzU0F4Z2NlUzA2bEdPOTE2NXlRWmtEbEpZQV9aSW9pMklxN1FrSWpOODF1czN5QU5LbVE5RWZiYjY2b1otSHlmbE1OOVZqMmp1X1VfV3B4WnVV?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxQVzlaZGR2OUNRV1AtMXNtNWw2Rm0zN21ldGM4WTV4dmlqQ05iODV6X2x1OVlPdlhyOHlvZG9EcHFtckpiUzlhbl9qbXNPRFBJdWRVbW1ZM2NCaHNnX0t2YW9hOXVrWEl1NHIyOHhmT3IxdktYSGlSelNkcHVGMF9DNnlPTHY3TjdxT0JXVmFEc2RPUQ?oc=5
- https://news.google.com/rss/articles/CBMi6wFBVV95cUxOdEhBMWNBMmE3SzYzelhQaHNSNlNWSWMzV0hUc1pNNGFoNlBzbC0wQnVmeXpCVkJMbkgyT0l3bWl0N1EtZzlZNG5uNHJ3dnREaFhGbUlQMjF6Vkh5Z0IyeDhKNU5PS25ma0xFNDAxdU1DcUZTMlJYYzNlRXphY1dORkxrSGRuSFRxamxQcnJydF83NndlRXd0Ylh0dzdSRzJPaFBLc0FfeVN2dDQyMHJoeTZXVnlSNTExM0NNT2xIc3NXb1dWU3lLUWR1V28zUldQdXpHSlBGLU5GVHNwVjc1TVV3NEhfWHZJSG0w?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
