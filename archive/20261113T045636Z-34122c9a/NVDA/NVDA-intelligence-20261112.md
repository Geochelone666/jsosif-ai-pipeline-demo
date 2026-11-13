# NVDA Intelligence Report

- ticker: **NVDA**
- Report as_of: **2026-11-12**
- Market data as_of: **2026-11-12**
- Quant sources: https://finance.yahoo.com/quote/NVDA/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVDA/key-statistics/
- AI analysis snapshot as_of: **2026-11-12**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-13T05:18:41.525282+00:00**
- AI status: **Partial: 5 headlines remain unclassified and excluded from research conclusions**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 10, 'ai': 3, 'unknown': 5, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261112T054014Z-6c47e7f9/NVDA** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 11 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 48.0%; oldest publication 2026-11-10

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 166.1900 |
| Return 1D (%) | -4.3401 |
| Return 1W (%) | -8.4857 |
| Return 1M (%) | -26.5686 |
| Return YTD (%) | -10.6816 |
| Return 1Y (%) | -14.0412 |
| Annualized volatility (%) | 38.7764 |
| Beta vs SPY | 1.7785 |
| Max drawdown (%) | -30.5342 |
| Sharpe (rf=0) | -0.1982 |
| Downside deviation (rf=0, %) | 27.8979 |
| Sortino (rf=0) | -0.2755 |
| Historical VaR 95% (1D, %) | 4.1932 |
| Historical ES 95% (1D, %) | 5.1243 |
| Correlation vs SPY | 0.6300 |
| Tracking error vs SPY (%) | 31.9565 |
| P/E (trailing) | 21.01 |
| P/B | 17.53 |
| EV/EBITDA | 19.78 |
| Revenue growth (%) | 105.90 |
| Forward P/E (estimate) | 10.49 |
| Gross margin (%) | 74.67 |
| Operating margin (%) | 65.21 |
| Return on equity (%) | 117.21 |
| Free cash flow yield (%) | 1.04 |
| MA50 | 215.9389 |
| Close vs MA50 (%) | -23.0384 |
| MA200 | 204.0663 |
| Close vs MA200 (%) | -18.5608 |
| RSI (14, Wilder) | 25.9930 |
| MACD (12,26) | -13.2350 |
| MACD signal (9) | -9.0695 |
| MACD histogram | -4.1655 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVDA': 281, 'SPY': 281}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 166.1900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -4.3401 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -8.4857 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -26.5686 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -10.6816 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -14.0412 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 38.7764 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 27.8979 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.2755 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.1932 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1243 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6300 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.9565 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.7785 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -30.5342 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.1982 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 10.4854 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.6740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 65.2140 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 117.2110 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.0419 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 21.0101 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 25.9930 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -4.1655 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -23.0384 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -18.5608 -> Clearly below the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

### Nvidia stock tumbles as CEO Jensen Huang steps down, dragging down other AI names
- Summary: Nvidia stock tumbles as CEO Jensen Huang steps down, dragging down other AI names
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxPVlcxMGw2ZjlXTThMWHdjWmJyRVloWUl4eVEwMWZ2M1NSdThQLUZ4YXd5RUNZdllfSkdaY1dJamE0SEFNLXZjRE0xcHFLQUpzSW0zWlBTYWIyZnBHZnBSenZOeDVWNWEwY2hyR0JOR0JLT1FEaXhzdnpoRk5Xai03Q1hPci03UHdZc3NLbzdWQVlJZkZGclp6Qno5b2lvSFd0bTNVbFpNQQ?oc=5>

### NVDA Stock Price Forecast — Top Analysts Give Multiple Downgrades Ahead of November 17 Earnings amid CEO Jensen Huang Fiasco
- Summary: NVDA Stock Price Forecast — Top Analysts Give Multiple Downgrades Ahead of November 17 Earnings amid CEO Jensen Huang Fiasco
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQTzU2YmpfQXpJMHVJel9uQWFUc1NVa2tySzllZUdfbUVSeFFFcmQwZkNLNFFVQTNtQkc0QS1LQzVTcEd6N21qNjZqVzc1Y3BRcFFOWW5hX3hMeENBTG1pUFV5UDZ5RjR1ZUtZa29mNlRmRlVUMVNUNVZVTFZDS01xaVhBMzUtdlVIVHVObEZlOXcwaFZuWExrUTlR?oc=5>

### Nvidia Stock Just Got Downgraded After Jensen Huang's Exit. Should You Sell?
- Summary: Nvidia Stock Just Got Downgraded After Jensen Huang's Exit. Should You Sell?
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxQOU93dVdhWGJWMVU4Q09jeUxPSEZHd2pKREZlSzliNWNrazBJSFloRUJ2WVkzNE1zd3ZQQzRrTE9NejQtNUZlYTZDVzBsUkhaT25NT1RBaTZLdmNhZ2NmMW10ZEY1cGpYc3BjOC1Td3FHeUFkdnJOTzRvTzNRcGFTa2FrWXJ3enRiSWJYUm11cTUyeHhfQTZoS1ZDSjNjajhIeDdoRzFjck5vLTV5RVdSTVNMMjQzbC1Q?oc=5>

### NVDA Stock Set For Best Day In Over 2 Months – Baird Downgrades Shares, Flags Slower AI Spending, Jensen Huang Risk
- Summary: NVDA Stock Set For Best Day In Over 2 Months – Baird Downgrades Shares, Flags Slower AI Spending, Jensen Huang Risk
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxORkgwN3diRWtuWWpxMjBhMEtyblJOTGJzclZ0N0JfVExQaWpkLTVzQ0tJTHpVMkFOcHdNVlE4RlV3Z2N5ckI2V0dLM2ItM3l6a1hMRzVXQk5VWlZsb2JneVVFY1NnRmh4bEgya2tyTXFZeEpScDJVX2VoMm1QZWkzSTFiU3JzOHVjdFVyLW8yUm5IQQ?oc=5>

### Nvidia stock drops 3%, extending decline on report alleged Chinese spy linked to Nvidia CEO aided $7.5 billion in China chip shipments
- Summary: Nvidia stock drops 3%, extending decline on report alleged Chinese spy linked to Nvidia CEO aided $7.5 billion in China chip shipments
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgJBVV95cUxQaTMzXy1sdW5VeFphNTFTbjYzWUZmdHJLNmhXMTE3cVBybWQ1NFhBUU5lUEZqcWUzNnBMN0J2RmdoYWtidXBQc1pPbFNhZV8zcGVJX2VxX3pzU01JZTV1cFpKanZVWHhSVE5IbWUyaVo5bXoxaUdkQ2Jwd0poWXNrX1VrOGI4SlBNOVExdUMyT0NDeS15dHY3N3FRZ1YyMHpZWmRtOC1MTXFhVEFvMm1xREZmb0xBSWpJTUt1aHdMVTl4NHY5TFY3QjZPSWFqNDNCM2xfeFJDM1FLN18zbmZfMG5OeS1lQ25jWUs1R3hIVkc5amVmMHBIS3kyQl8wS3B3T0d5bjFqM2lYQkt1UDk5Rm9kdlMtZw?oc=5>

### NVDA Stock Slides To Fresh 7-Month Low Amid CEO Turmoil: Ross Gerber Calls Selloff A Chance To Buy Shares At ‘Absurdly Low Price’
- Summary: NVDA Stock Slides To Fresh 7-Month Low Amid CEO Turmoil: Ross Gerber Calls Selloff A Chance To Buy Shares At ‘Absurdly Low Price’
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNdnhmZl90TXVGZmFxb3kzTThoajJldGNoTThOWDhzME9Md0M1VTdnWldSRHJZWXFES1NzWlA1b09xWUtHcmZUd0ctc1V0TzBkSUlFWS1pZVI4RXloeVcwMDRMT1RGRzQzTzMySHlBeC0yWThNNlQwTUx3VV8wMVNESVg2Z0RRTVJrLUpndVh5N3lJY25T?oc=5>

### Nvidia Stock Tumbles as Company Prepares To Remove Huang Following Second Affair (UPDATED) - NVIDIA (NASD
- Summary: Nvidia Stock Tumbles as Company Prepares To Remove Huang Following Second Affair (UPDATED) - NVIDIA (NASD
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3AFBVV95cUxQZHlaTGY4SGtwcU5ubTlUalpjZW42UDVnd2hGTlFMTUMxSm80MjNILUZ5SXd1ZXNaRzdqeGg1X3R1YzloUnhHZXZvTl9zRm9RNF9DUlQyU3JlN3hKMjVTZGVCc1FIYklaOEVia0k3Z2Zncy01TmpyOW1fRkhaZW85VTJMQzdFMlpsM0xJN2RvdHdYV1dFSHFxU3dQNzNTU3JVdUdreG45bFFkaHJWV3IxdzJBM19DSk1CekEzNkMyVVBsYjd1UkNiR2plVEtWNWZYZEozVmczOWVsTThz?oc=5>

## CATALYSTS

### NVDA Stock Alert: Why Baird Just Slashed Its Nvidia Price Target from $500 to $200
- Summary: NVDA Stock Alert: Why Baird Just Slashed Its Nvidia Price Target from $500 to $200
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxPVXNwX1BMQ2xudnlVbE5GQmJoZ1JZZnlpZncydE5BZXo0Y2tmOHlRdV9ybm9EbjlTcVAxSEhkYkprNlVLNW91OG5HQjFtLUJaVEFscXlqOVFZRGRQcklCTmQyQWZ4amlsQlFVeEdobXNYelUzWGNyZTRmWXU4dmFtSXB0bzliZFMzQzdLNmlIRFE0ZUdRakgwUjNFd2VHMVUzLTBaNVpjUTVFX013OGpiSjRqLV81VlpIMmo2Q3dveWw?oc=5>

### Nvidia Stock’s 'Very Sad Day,' Analyst Cuts Price Target by $100
- Summary: Nvidia Stock’s 'Very Sad Day,' Analyst Cuts Price Target by $100
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxNMVMtc1Y3eXhUNk5mRWs4LUlZTmNGUEp3NGRmRzEycDdaQ2hCbmN6WUJLZEx2MWozS3ZmQ3lHME83aTVseGNWaTUzeE9fckpMTklyaE1SVEhJelBDRDFVS2xseWJMdjlLc2dCWFdudGgyVzlFMHZnNUdCby1QdnZuSkhkeXR3S3ptSVc4WlM2OHNXTm1JbUJWRjZ3NGxwa3JESmNHaGx0VTF3dFFlSzQxR2pXU2drbzFCbkduNjNZOTNLZ2NYZE1kbHZ5eUc?oc=5>

### NVDA Stock Rout: Another Analyst Slashes Rating, Beijing Warns US Against Tech Curbs
- Summary: NVDA Stock Rout: Another Analyst Slashes Rating, Beijing Warns US Against Tech Curbs
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQNVc4amE3bzV1cWF4SGlwOVd4UnNZVTZ6c09GZE42VDZiMGRkTXhiMDN6MS1lYzlfRzVHWlF2eVA4R0VlVlBBakREZ3hzSy1PVjBXWFdhSzEzbkVqdUtOc2tMUUN1eXJLNmhlNnJhSWE1Yk9PS2FhemlWalE2clE4aHB4T1NGcEJyeFVKNUdSbUY0UmMtMTh6aEIyR18?oc=5>

### 'Icarus' rise and fall': Analyst downgrades Nvidia stock amid Jensen Huang woes, highlights risks
- Summary: Analyst downgrade citing Jensen Huang concerns, indicating potential downside pressure.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi4wFBVV95cUxOUFJBOGQzQXE2NFkxd21JeE9YUml1MHdrVUo3c2wxRVhYal9YU1NPUllYR3Q0QUdMSG5iRFRGb3l4SE1iT2NWc2tLcXpUZktPMUs2SUdPSmRwWjR0ZVM4STdtNjNGbzhDX3FGNE9QYjR5M2o3NjdNTmRvNEo3S283Wk15Vk4zVnBQSlM3X09VR3lXb1RRN09GUkRCVTFnc1UzNXg5VlhqazV2WXhFdnNzSzJSaGc2cmRXYmtuRnhJYjB1QVY1RjhNTnlTRWd0ODItRjBHSjE1LWt4WWlxMHpTTzhBRQ?oc=5>

### NVIDIA Announces CEO Transition
- Summary: NVIDIA announces a transition in its CEO position, signaling a leadership change within the company.
- Date: 2026-11-12 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMidEFVX3lxTE1ZNXBiTEpIYWNHT2hlMWVfSXJ1UWd6eEVKUW1URllFTkpERzVyRWpBOEgyaU90Sk5KVm9VZXRseUlXSEswU1JSNHhzeVhRN2lxQXRUbVk1cTBLZXRjSHFNWTNQRWNXb2FrQno3TzNzQTg2UXA1?oc=5>

## RISKS

### Prediction: After Losing Over $1.7 Trillion in Market Cap This Year, Nvidia Stock Will Rebound in Epic Fashion. Here's Why.
- Summary: Despite massive market cap loss, a predicted rebound indicates high upside potential.
- Date: 2026-11-11 | Impact: high | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi9wFBVV95cUxNUk5yd1l5YjdaOTM2dDFiWmQ4U0V2QTd3ZHlkLWtnVV9zUzN1SXZYSE93NzQyVWZ1Rk5BZldqZ1BiQmp0YXNKb19Zc2lxanhqQUViWGtPeWhjWUt0WHgyVTd5QmhKUmZlSXhHbmtMRDJlZlBXLW9PYUZoMEF2ZkdJa2RKUlJRV2FlR244MGp5OUFmSEc5UmlEOFh6MncwNENJOG1hSVlxUk80dFVDM3BGc1A5RmY3MFM1OFFvdU5VWmpHRmlxb0hCYmh0c0JBZ3Y1aVNKM2Z3ZFlVbjhKYWM2LTFGbFY3Smt3R2ZoZm13UExrU3o3N0RN?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVDA** | **21.01** | **17.53** | **19.78** | **105.90** | **4,012,989,743,104.00 USD** | **-14.04** |
| AMD | 125.06 | 14.04 | 85.56 | 44.70 | 959,943,081,984.00 USD | 126.08 |
| AVGO | 46.53 | 17.45 | 33.96 | 85.50 | 1,739,319,803,904.00 USD | 3.34 |
| INTC | N/A | 2.83 | 17.67 | 20.90 | 325,278,007,296.00 USD | 61.52 |

Peers fetched as_of: 2026-11-12; NVDA reuses existing data (market data as_of: 2026-11-12); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-26
- Next expected earnings: 2026-11-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-12

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

- https://news.google.com/rss/articles/CBMipwFBVV95cUxPVlcxMGw2ZjlXTThMWHdjWmJyRVloWUl4eVEwMWZ2M1NSdThQLUZ4YXd5RUNZdllfSkdaY1dJamE0SEFNLXZjRE0xcHFLQUpzSW0zWlBTYWIyZnBHZnBSenZOeDVWNWEwY2hyR0JOR0JLT1FEaXhzdnpoRk5Xai03Q1hPci03UHdZc3NLbzdWQVlJZkZGclp6Qno5b2lvSFd0bTNVbFpNQQ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQTzU2YmpfQXpJMHVJel9uQWFUc1NVa2tySzllZUdfbUVSeFFFcmQwZkNLNFFVQTNtQkc0QS1LQzVTcEd6N21qNjZqVzc1Y3BRcFFOWW5hX3hMeENBTG1pUFV5UDZ5RjR1ZUtZa29mNlRmRlVUMVNUNVZVTFZDS01xaVhBMzUtdlVIVHVObEZlOXcwaFZuWExrUTlR?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxQOU93dVdhWGJWMVU4Q09jeUxPSEZHd2pKREZlSzliNWNrazBJSFloRUJ2WVkzNE1zd3ZQQzRrTE9NejQtNUZlYTZDVzBsUkhaT25NT1RBaTZLdmNhZ2NmMW10ZEY1cGpYc3BjOC1Td3FHeUFkdnJOTzRvTzNRcGFTa2FrWXJ3enRiSWJYUm11cTUyeHhfQTZoS1ZDSjNjajhIeDdoRzFjck5vLTV5RVdSTVNMMjQzbC1Q?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxORkgwN3diRWtuWWpxMjBhMEtyblJOTGJzclZ0N0JfVExQaWpkLTVzQ0tJTHpVMkFOcHdNVlE4RlV3Z2N5ckI2V0dLM2ItM3l6a1hMRzVXQk5VWlZsb2JneVVFY1NnRmh4bEgya2tyTXFZeEpScDJVX2VoMm1QZWkzSTFiU3JzOHVjdFVyLW8yUm5IQQ?oc=5
- https://news.google.com/rss/articles/CBMilgJBVV95cUxQaTMzXy1sdW5VeFphNTFTbjYzWUZmdHJLNmhXMTE3cVBybWQ1NFhBUU5lUEZqcWUzNnBMN0J2RmdoYWtidXBQc1pPbFNhZV8zcGVJX2VxX3pzU01JZTV1cFpKanZVWHhSVE5IbWUyaVo5bXoxaUdkQ2Jwd0poWXNrX1VrOGI4SlBNOVExdUMyT0NDeS15dHY3N3FRZ1YyMHpZWmRtOC1MTXFhVEFvMm1xREZmb0xBSWpJTUt1aHdMVTl4NHY5TFY3QjZPSWFqNDNCM2xfeFJDM1FLN18zbmZfMG5OeS1lQ25jWUs1R3hIVkc5amVmMHBIS3kyQl8wS3B3T0d5bjFqM2lYQkt1UDk5Rm9kdlMtZw?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNdnhmZl90TXVGZmFxb3kzTThoajJldGNoTThOWDhzME9Md0M1VTdnWldSRHJZWXFES1NzWlA1b09xWUtHcmZUd0ctc1V0TzBkSUlFWS1pZVI4RXloeVcwMDRMT1RGRzQzTzMySHlBeC0yWThNNlQwTUx3VV8wMVNESVg2Z0RRTVJrLUpndVh5N3lJY25T?oc=5
- https://news.google.com/rss/articles/CBMi3AFBVV95cUxQZHlaTGY4SGtwcU5ubTlUalpjZW42UDVnd2hGTlFMTUMxSm80MjNILUZ5SXd1ZXNaRzdqeGg1X3R1YzloUnhHZXZvTl9zRm9RNF9DUlQyU3JlN3hKMjVTZGVCc1FIYklaOEVia0k3Z2Zncy01TmpyOW1fRkhaZW85VTJMQzdFMlpsM0xJN2RvdHdYV1dFSHFxU3dQNzNTU3JVdUdreG45bFFkaHJWV3IxdzJBM19DSk1CekEzNkMyVVBsYjd1UkNiR2plVEtWNWZYZEozVmczOWVsTThz?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxPVXNwX1BMQ2xudnlVbE5GQmJoZ1JZZnlpZncydE5BZXo0Y2tmOHlRdV9ybm9EbjlTcVAxSEhkYkprNlVLNW91OG5HQjFtLUJaVEFscXlqOVFZRGRQcklCTmQyQWZ4amlsQlFVeEdobXNYelUzWGNyZTRmWXU4dmFtSXB0bzliZFMzQzdLNmlIRFE0ZUdRakgwUjNFd2VHMVUzLTBaNVpjUTVFX013OGpiSjRqLV81VlpIMmo2Q3dveWw?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxNMVMtc1Y3eXhUNk5mRWs4LUlZTmNGUEp3NGRmRzEycDdaQ2hCbmN6WUJLZEx2MWozS3ZmQ3lHME83aTVseGNWaTUzeE9fckpMTklyaE1SVEhJelBDRDFVS2xseWJMdjlLc2dCWFdudGgyVzlFMHZnNUdCby1QdnZuSkhkeXR3S3ptSVc4WlM2OHNXTm1JbUJWRjZ3NGxwa3JESmNHaGx0VTF3dFFlSzQxR2pXU2drbzFCbkduNjNZOTNLZ2NYZE1kbHZ5eUc?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQNVc4amE3bzV1cWF4SGlwOVd4UnNZVTZ6c09GZE42VDZiMGRkTXhiMDN6MS1lYzlfRzVHWlF2eVA4R0VlVlBBakREZ3hzSy1PVjBXWFdhSzEzbkVqdUtOc2tMUUN1eXJLNmhlNnJhSWE1Yk9PS2FhemlWalE2clE4aHB4T1NGcEJyeFVKNUdSbUY0UmMtMTh6aEIyR18?oc=5
- https://news.google.com/rss/articles/CBMi4wFBVV95cUxOUFJBOGQzQXE2NFkxd21JeE9YUml1MHdrVUo3c2wxRVhYal9YU1NPUllYR3Q0QUdMSG5iRFRGb3l4SE1iT2NWc2tLcXpUZktPMUs2SUdPSmRwWjR0ZVM4STdtNjNGbzhDX3FGNE9QYjR5M2o3NjdNTmRvNEo3S283Wk15Vk4zVnBQSlM3X09VR3lXb1RRN09GUkRCVTFnc1UzNXg5VlhqazV2WXhFdnNzSzJSaGc2cmRXYmtuRnhJYjB1QVY1RjhNTnlTRWd0ODItRjBHSjE1LWt4WWlxMHpTTzhBRQ?oc=5
- https://news.google.com/rss/articles/CBMidEFVX3lxTE1ZNXBiTEpIYWNHT2hlMWVfSXJ1UWd6eEVKUW1URllFTkpERzVyRWpBOEgyaU90Sk5KVm9VZXRseUlXSEswU1JSNHhzeVhRN2lxQXRUbVk1cTBLZXRjSHFNWTNQRWNXb2FrQno3TzNzQTg2UXA1?oc=5
- https://news.google.com/rss/articles/CBMi9wFBVV95cUxNUk5yd1l5YjdaOTM2dDFiWmQ4U0V2QTd3ZHlkLWtnVV9zUzN1SXZYSE93NzQyVWZ1Rk5BZldqZ1BiQmp0YXNKb19Zc2lxanhqQUViWGtPeWhjWUt0WHgyVTd5QmhKUmZlSXhHbmtMRDJlZlBXLW9PYUZoMEF2ZkdJa2RKUlJRV2FlR244MGp5OUFmSEc5UmlEOFh6MncwNENJOG1hSVlxUk80dFVDM3BGc1A5RmY3MFM1OFFvdU5VWmpHRmlxb0hCYmh0c0JBZ3Y1aVNKM2Z3ZFlVbjhKYWM2LTFGbFY3Smt3R2ZoZm13UExrU3o3N0RN?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
