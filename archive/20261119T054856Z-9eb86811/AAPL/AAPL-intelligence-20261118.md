# AAPL Intelligence Report

- ticker: **AAPL**
- Report as_of: **2026-11-18**
- Market data as_of: **2026-11-18**
- Quant sources: https://finance.yahoo.com/quote/AAPL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AAPL/key-statistics/
- AI analysis snapshot as_of: **2026-11-18**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-19T05:52:26.689294+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 9, 'ai': 7, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261118T054934Z-e0d070d9/AAPL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 12 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 24.0%; oldest publication 2026-11-13

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 352.4500 |
| Return 1D (%) | 0.1535 |
| Return 1W (%) | -0.8189 |
| Return 1M (%) | 2.6955 |
| Return YTD (%) | 30.0956 |
| Return 1Y (%) | 32.2457 |
| Annualized volatility (%) | 24.8817 |
| Beta vs SPY | 0.6133 |
| Max drawdown (%) | -13.7985 |
| Sharpe (rf=0) | 1.2527 |
| Downside deviation (rf=0, %) | 16.8728 |
| Sortino (rf=0) | 1.8473 |
| Historical VaR 95% (1D, %) | 2.0034 |
| Historical ES 95% (1D, %) | 3.4742 |
| Correlation vs SPY | 0.3391 |
| Tracking error vs SPY (%) | 24.0044 |
| P/E (trailing) | 39.25 |
| P/B | 45.70 |
| EV/EBITDA | 30.09 |
| Revenue growth (%) | 11.70 |
| Forward P/E (estimate) | 33.34 |
| Gross margin (%) | 48.79 |
| Operating margin (%) | 33.01 |
| Return on equity (%) | 142.26 |
| Free cash flow yield (%) | 2.06 |
| MA50 | 340.9164 |
| Close vs MA50 (%) | 3.3831 |
| MA200 | 302.0793 |
| Close vs MA200 (%) | 16.6747 |
| RSI (14, Wilder) | 56.7768 |
| MACD (12,26) | 3.9919 |
| MACD signal (9) | 3.6755 |
| MACD histogram | 0.3164 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AAPL': 285, 'SPY': 285}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 352.4500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.1535 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.8189 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 2.6955 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 30.0956 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 32.2457 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 24.8817 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.8728 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.8473 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0034 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.4742 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3391 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.0044 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.6133 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -13.7985 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.2527 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 33.3358 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 48.7860 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 33.0100 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 142.2570 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.0629 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 39.2483 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 56.7768 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.3164 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 3.3831 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 16.6747 -> Clearly above the moving-average trend level.

## TAILWINDS

### Apple targets June 2027 unveiling for AI smart glasses: report (AAPL:NASDAQ)
- Summary: Apple plans to unveil AI smart glasses in June 2027.
- Date: 2026-11-16 | Impact: medium | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOZEhVR1p4SVhoeEFLSTkwSUVoLW5RRG9JRmZxX1k5NVVpbExYRU1WTGw5clM4d2FKNllFMTlROVlVT25HQmdkRHpVZUJqMWptSlhkSk9RdmF4LTlDMlhQazFDU3ZlelhMRkJPMTJkOEl0UHYxZHpOY3lYSG1lU2piV0tzM2lvZXdmaDJTU0RueExWYmNJWU1uQU4tWW83Q1lZ?oc=5>

### Apple updates app store pricing across multiple countries, introduces new California tax rules
- Summary: Apple adjusts app store pricing and adds California tax rules, potentially affecting revenue streams.
- Date: 2026-11-18 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxQNW4yb1NFai1nR3RoRlg0QThXbnpkRTlTQ1BrWG51Wmhrd3dCRnpUWWVSNG55c2k2anJTMUJDNnlSbks2WEpxWk0welhkSzZicklodTdMT0dOSWRqSTNVNjM5WjBYVUkySzJ5Tzh5clJ6b1JxNm9YTkdqRlBYcnN6bV9MTC1taUR5QXd1Y29VRnhCanhnNjhaMHZsWjcyczVVOHpoWWlRMWM4STZHaU94OVpCUXpkV0NkRzhLX2NvZU9JQnNFZ0QzMmhTQQ?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Apple (AAPL) Picks Core Foldable Glass Supplier For iPhone Duo
- Summary: Apple (AAPL) Picks Core Foldable Glass Supplier For iPhone Duo
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOYmt6MzR0X1VRdEVBYVF2Y1drN3B0RlpXRUtmOW9CX0ZFbE5kYUJXV0oxczZUckthVWxMTW1JeVM5bkZLaVE1QjhZSi1kazRpWUEyUHEySFFoZ21URmNfYVVtQ0Q0NEIwZTdldkpmOVc3akt0XzVxaXVvbFZ6d0ZmUzdxOFlPZkVvYUlRaUFtVU5CRTZ4S0E?oc=5>

### Apple adds face unlock to iPhone Duo in new software beta (AAPL:NASDAQ)
- Summary: Apple adds face unlock to iPhone Duo in new software beta (AAPL:NASDAQ)
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNekw4czk1V0dBR21SMWtoS1ozbkVuWUhPTTR5cEtWTmNTd3JrdHM3UWg5RWItekxCMnJVcUhrZXBDTkJ3aDdPdktucTRUYWtjazFCV1p4a0xyMzBsS3NrMXdvOGlmaEViOGM4MTd4MmZQOW9sN0JTbmQxY3pyRjlTUjk2eXBCa0QwWFR0N1REdHhMMmRfb0x3anhnWQ?oc=5>

### Apple to stand trial in France over iPhone repair restrictions: report (AAPL:NASDAQ)
- Summary: Apple to stand trial in France over iPhone repair restrictions: report (AAPL:NASDAQ)
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxPZ0xRQ0RCX3RmbzdqVjRpTzAwSFZ0bTRGeTlCUzh5QXRpSlZRT0NWT3Y5YmhFU1AtdHA1ZmM1eGxDczBsdVFNUDYyd085VVJPaHFCRGZPZlZMWDZFX3hQM0p4M1UyQlZOYnlfRGY1eFNnbHFDSWdtUkN6TWE2R2VjQjlIZ09GODAxcDBmRVNUVTI1ME9xMks3WUo1U19nZ1I0ZEJQXzJ1R3VkRlU?oc=5>

### Apple (AAPL) Heads To French Trial In June 2027 Over iPhone Repairs
- Summary: Apple (AAPL) Heads To French Trial In June 2027 Over iPhone Repairs
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxNanM1bVhuU1dILWpuWnI0VFNfeTVDOW5ZNnNOdERKalBvSXpaOHdvUWlLUmRpc09ieXRCeUlXcWwwU0N3c0N5NXMtdHBHYUE2ejlLZGNNb180eDh4Y0hfd0Y4QV9zY1JGRFJ4STlKSjhMVWc2bXBvNmJhT2x2VDEtZ3dCNXJHbUNQa2tLX3I5N0Ewdm8zZW5wMVBsai1sOXNWWDFIN014bzA2VUMwNHU2Q2F5OERyVnh1U205d9IBwgFBVV95cUxPNjIydEQzdWR2V2NxRzFGRktPdG5jNkFpTW1UaVJUX2hCLTY1akVCVnpyNGViWW9pdTBXd1JMNHBOLWdILWtIek9sTW0zQW5WcHhKV09CWVRudzlSZ3pSSzRuZC14allOa0ZfaG5UTHVrWU9yOVoxZUVKUVlLb2NOU29RaDh5aTZlSk9Ub1lYSW9sa2ZKYW1vaDNVZlpjNEpMMWxNU0djYjJzVDhqVGpPTGw3VFBIUmZ0bHA1MTgzS1dCdw?oc=5>

### Apple Inc. $AAPL Stock Sold by Loring Wolcott & Coolidge Fiduciary Advisors LLP MA
- Summary: Apple Inc. $AAPL Stock Sold by Loring Wolcott & Coolidge Fiduciary Advisors LLP MA
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxNSVpRTXc5WDRsakZNVk9xLTRpYlptUXZJblQzcDhWS1JpdTFoSnB5eVJUZm1HRFdKQWdtOC0zTFVwdDVtam5vQU54N2tYUFlwSzZHRmhZODBXZ1psREZlbTVBbGlKVGVIdXFfblcyOFVQWDEwMFl4aWZaMkNsNTJ3bnJ3MWJmQ1NJc2FpSV9LUEdYVk5IUmhMOVJSLUpVQ0VuaVpHOW1jU3o1Nm9HNGZIM3FQWks0N2pRUzRKMG11UHhUeE5uTjFvUS11dUNLZUl3LWU1Yll3?oc=5>

### Apple Inc. $AAPL Stock Sold by Slow Capital Inc.
- Summary: Apple Inc. $AAPL Stock Sold by Slow Capital Inc.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPZTcwQkk1LS1MS2o4TUl5MlpKU1Q5TktoSmRRcmJqZ0VzZFpDSXNfc0szSFlmanVXYllOQU0yaTZoVXp0ZjFRTGg2WTdCcy1NeVhYVDZBZTJkQ0dfTkdWTnZ3a01IdXplTURXSWppbzU0b0M1SllHM0VxUk1Nd2loTGJGRzRvOTBUUi12SklYMFBsWmRJWlpsSHdFMG9WTURpUFBxLUxhSGJNUQ?oc=5>

### Apple Inc. $AAPL Stock: Orange Investment Advisors Inc. Reduces Stake
- Summary: Apple Inc. $AAPL Stock: Orange Investment Advisors Inc. Reduces Stake
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxQMTEzaElkaDNuSjEtVVpkTVVBWTlBbzZueElXVzZPbWdhazF2UnhBbWRiWVJiZENpckFYWWpuamhtdDlCSTZrSDUyc3E5Q1E1Z0lEWkF5NXJERTA4amVXWEFUcnhmYUxudWRCNG9uVk1ZenJMVXhJVlBZQ01ZUUQ1cm14WVpQTjdseTlPSmlORkVLVVJVRnY5NDd4dGhnelNaSlgwLVZaMld6ZENYenUtakRCZ1NQMjJkS1BtNk8waHU3Rk94?oc=5>

### Apple Inc. $AAPL Stock Sold by Nadler Financial Group Inc.
- Summary: Apple Inc. $AAPL Stock Sold by Nadler Financial Group Inc.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxON3BPQndiREdNOFVXNzdjeWhndTVfSHpsTDJBSExkSncwUy1JNm1ja183bmVyMXU1ZjJQdVJOWFBYZjB6VzEzY1lqVUpZcnFiYUpDcDhla3BnOV9sNzY2TWlkUDBYdjFqRHNTZDFUdVlFQXJyMk5BOUpRYnNxOUNETXZESGV4a0ItdWctRGtYM0wwSEV1Y2N3bHh0LUZYRUNVejlvM015QUlGQk55dlVvbjI0UVc0X3c?oc=5>

### Apple Inc. $AAPL Stock Sold by B.O.S.S. Retirement Advisors LLC
- Summary: Apple Inc. $AAPL Stock Sold by B.O.S.S. Retirement Advisors LLC
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxOdU5mOHNySXJMdGZnbDFJY2llUzBXS2J5OWVBS0licnFRYVBiaFhwTVEyX3Z3bzZTMUxFUWhjMXMyQkRTVjFFc3pheE9pMS1DNmxRNWYySDVzS3hyTjVFRVpKaGt3X2lBek9RQlN2ZUlyVm9kQWg1Y3IzMmc2LUVrN1FHSmZWMXFFNG9yVTV0TzExblBQTDFwWE1IODhzN3lGU3F1bWhRUXUySHNBcGhlemVUY21ELURTdEE?oc=5>

### AAPL Stock Posted Best Week In 4 Months Amid Nvidia Disruption: Apple Reportedly Plans Smart Glasses To Rival Meta Next Year
- Summary: Apple’s stock surged after announcing plans to launch smart glasses competing with Meta, marking its best week in four months amid Nvidia’s market disruption.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPaTZ2ZWQ2QTBxMk1iWTJ4ZXBGc3hpUDRHMDVVdFdMaGtkWVVkcEtzM2djWFpZQ1ZxTnYtUHFhMHFIbjFSSjhPSXVDWWsxdXlvQzQ1RDliaVNNUzR5QzZLWEl0UW9ROGx5RnZVdko4LWYzbWNqWEJORkJDTEVmY3ZObDgyaHNmZzRHaWpQN2ZCaDFQM05ja21J?oc=5>

### A $1,999 Sellout. What China Renaissance Sees in Apple (AAPL)
- Summary: China Renaissance's $1,999 sellout view on Apple.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPUVhYalN0S3o2VVRpNWZPTU9oWEZJZnlRNi1VU1pTY3VzUXFueTh3Um9IUWIzdjY4OW9EU3kwVG5QblI5MzcxUVg2Y3J3QW5KM3RuZGh3UmRJYTRBWVR0Ql9iZVAzb2JucTM5Qi1IQkl1bHNLQXpDeFltVzhqQm9mTXFneG5GSi1vQ25oSGY0VnBrSEI5a1hWb1d3VDU?oc=5>

### Apple users are about to lose something they've had for 28 years
- Summary: Apple is discontinuing a 28‑year‑old feature, affecting long‑time users.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPZkdNTVM1eXVEN0xUVTJrVzZJdWJ1X3doMmY5TEx4M3pMQ19BNTVHMS1BSjZ1SUhJQUNLOTkzdTZiX3VzVll3V1IzaDdaNk1SYW43eUs2NEhCWHNFTXRyRWpnNlFUajVQaURMeE50dnJ2d2Y3WlBmLUpQN1FhcjhTY1Nra0NzX0lLYnp5a3pjb2J0RmZ1amdGVUZ3?oc=5>

## RISKS

### Apple(AAPL.US) Director Sells US$31.77 Million in Common Stock
- Summary: A director sold $31.77M in Apple shares, possibly signaling insider concerns.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPcjBvOVFKU0RhSk5mZUNBYUo5Z3lHU3NUdEVOV0NBel8wVkJhX29TY2I3MWhVR3dFclVfM0JLOFNEdXNIblA1VV84b1VxOFlsZnJsaTFBYVlhZnRNeW1weU1fZ3pXYk5MOThWeXZLUGJMNkt5dS14T2JZZGZtbnUtaXNRTHhNbV9HSWo2ei1kRmNUUE00ZnN0emIySVVQVm8?oc=5>

### An Apple (AAPL) director gave away 50,000 shares the same day he sold stock.
- Summary: A director gave away 50,000 shares while selling, raising potential governance concerns.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPeXo2bXM2UVlsdURDYTdkaUx1U1YyOFBtRzhmSnhYaFdSZVhQR0ZZeGE3cWNaWTU4dWNNdUVSd0FpU1VaYkc5U09iaWhlSmV1ZDRDa19nWWRONklwT1BuSFY0Z2dZeUFkclNQSVlMN3RjOXpfY3BhZUZUUno1RnRBVkxjUk5yX21xOU9WMmtGOVYyRkUzdGhXT2d5TzZQQzZMSzF4NUhB?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AAPL** | **39.25** | **45.70** | **30.09** | **11.70** | **5,121,867,513,856.00 USD** | **32.25** |
| MSFT | 26.53 | 8.02 | 18.69 | 18.80 | 3,774,660,476,928.00 USD | 3.78 |
| GOOGL | 14.75 | 5.26 | 18.20 | 24.70 | 3,472,317,218,816.00 USD | -0.39 |
| SONY | 19.90 | 2.88 | 0.30 | 10.30 | 155,439,529,984.00 USD | -6.98 |

Peers fetched as_of: 2026-11-18; AAPL reuses existing data (market data as_of: 2026-11-18); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-02
- Next expected earnings: 2027-01-28 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-18

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-11-03
- Revenue (latest available single quarter): 62,900,000,000.00 USD; period 2018-07-01/2018-09-29; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 29,789,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/320193/000032019326000026/aapl-20260926.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMioAFBVV95cUxOZEhVR1p4SVhoeEFLSTkwSUVoLW5RRG9JRmZxX1k5NVVpbExYRU1WTGw5clM4d2FKNllFMTlROVlVT25HQmdkRHpVZUJqMWptSlhkSk9RdmF4LTlDMlhQazFDU3ZlelhMRkJPMTJkOEl0UHYxZHpOY3lYSG1lU2piV0tzM2lvZXdmaDJTU0RueExWYmNJWU1uQU4tWW83Q1lZ?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxQNW4yb1NFai1nR3RoRlg0QThXbnpkRTlTQ1BrWG51Wmhrd3dCRnpUWWVSNG55c2k2anJTMUJDNnlSbks2WEpxWk0welhkSzZicklodTdMT0dOSWRqSTNVNjM5WjBYVUkySzJ5Tzh5clJ6b1JxNm9YTkdqRlBYcnN6bV9MTC1taUR5QXd1Y29VRnhCanhnNjhaMHZsWjcyczVVOHpoWWlRMWM4STZHaU94OVpCUXpkV0NkRzhLX2NvZU9JQnNFZ0QzMmhTQQ?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOYmt6MzR0X1VRdEVBYVF2Y1drN3B0RlpXRUtmOW9CX0ZFbE5kYUJXV0oxczZUckthVWxMTW1JeVM5bkZLaVE1QjhZSi1kazRpWUEyUHEySFFoZ21URmNfYVVtQ0Q0NEIwZTdldkpmOVc3akt0XzVxaXVvbFZ6d0ZmUzdxOFlPZkVvYUlRaUFtVU5CRTZ4S0E?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNekw4czk1V0dBR21SMWtoS1ozbkVuWUhPTTR5cEtWTmNTd3JrdHM3UWg5RWItekxCMnJVcUhrZXBDTkJ3aDdPdktucTRUYWtjazFCV1p4a0xyMzBsS3NrMXdvOGlmaEViOGM4MTd4MmZQOW9sN0JTbmQxY3pyRjlTUjk2eXBCa0QwWFR0N1REdHhMMmRfb0x3anhnWQ?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxPZ0xRQ0RCX3RmbzdqVjRpTzAwSFZ0bTRGeTlCUzh5QXRpSlZRT0NWT3Y5YmhFU1AtdHA1ZmM1eGxDczBsdVFNUDYyd085VVJPaHFCRGZPZlZMWDZFX3hQM0p4M1UyQlZOYnlfRGY1eFNnbHFDSWdtUkN6TWE2R2VjQjlIZ09GODAxcDBmRVNUVTI1ME9xMks3WUo1U19nZ1I0ZEJQXzJ1R3VkRlU?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxNanM1bVhuU1dILWpuWnI0VFNfeTVDOW5ZNnNOdERKalBvSXpaOHdvUWlLUmRpc09ieXRCeUlXcWwwU0N3c0N5NXMtdHBHYUE2ejlLZGNNb180eDh4Y0hfd0Y4QV9zY1JGRFJ4STlKSjhMVWc2bXBvNmJhT2x2VDEtZ3dCNXJHbUNQa2tLX3I5N0Ewdm8zZW5wMVBsai1sOXNWWDFIN014bzA2VUMwNHU2Q2F5OERyVnh1U205d9IBwgFBVV95cUxPNjIydEQzdWR2V2NxRzFGRktPdG5jNkFpTW1UaVJUX2hCLTY1akVCVnpyNGViWW9pdTBXd1JMNHBOLWdILWtIek9sTW0zQW5WcHhKV09CWVRudzlSZ3pSSzRuZC14allOa0ZfaG5UTHVrWU9yOVoxZUVKUVlLb2NOU29RaDh5aTZlSk9Ub1lYSW9sa2ZKYW1vaDNVZlpjNEpMMWxNU0djYjJzVDhqVGpPTGw3VFBIUmZ0bHA1MTgzS1dCdw?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxNSVpRTXc5WDRsakZNVk9xLTRpYlptUXZJblQzcDhWS1JpdTFoSnB5eVJUZm1HRFdKQWdtOC0zTFVwdDVtam5vQU54N2tYUFlwSzZHRmhZODBXZ1psREZlbTVBbGlKVGVIdXFfblcyOFVQWDEwMFl4aWZaMkNsNTJ3bnJ3MWJmQ1NJc2FpSV9LUEdYVk5IUmhMOVJSLUpVQ0VuaVpHOW1jU3o1Nm9HNGZIM3FQWks0N2pRUzRKMG11UHhUeE5uTjFvUS11dUNLZUl3LWU1Yll3?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPZTcwQkk1LS1MS2o4TUl5MlpKU1Q5TktoSmRRcmJqZ0VzZFpDSXNfc0szSFlmanVXYllOQU0yaTZoVXp0ZjFRTGg2WTdCcy1NeVhYVDZBZTJkQ0dfTkdWTnZ3a01IdXplTURXSWppbzU0b0M1SllHM0VxUk1Nd2loTGJGRzRvOTBUUi12SklYMFBsWmRJWlpsSHdFMG9WTURpUFBxLUxhSGJNUQ?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxQMTEzaElkaDNuSjEtVVpkTVVBWTlBbzZueElXVzZPbWdhazF2UnhBbWRiWVJiZENpckFYWWpuamhtdDlCSTZrSDUyc3E5Q1E1Z0lEWkF5NXJERTA4amVXWEFUcnhmYUxudWRCNG9uVk1ZenJMVXhJVlBZQ01ZUUQ1cm14WVpQTjdseTlPSmlORkVLVVJVRnY5NDd4dGhnelNaSlgwLVZaMld6ZENYenUtakRCZ1NQMjJkS1BtNk8waHU3Rk94?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxON3BPQndiREdNOFVXNzdjeWhndTVfSHpsTDJBSExkSncwUy1JNm1ja183bmVyMXU1ZjJQdVJOWFBYZjB6VzEzY1lqVUpZcnFiYUpDcDhla3BnOV9sNzY2TWlkUDBYdjFqRHNTZDFUdVlFQXJyMk5BOUpRYnNxOUNETXZESGV4a0ItdWctRGtYM0wwSEV1Y2N3bHh0LUZYRUNVejlvM015QUlGQk55dlVvbjI0UVc0X3c?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxOdU5mOHNySXJMdGZnbDFJY2llUzBXS2J5OWVBS0licnFRYVBiaFhwTVEyX3Z3bzZTMUxFUWhjMXMyQkRTVjFFc3pheE9pMS1DNmxRNWYySDVzS3hyTjVFRVpKaGt3X2lBek9RQlN2ZUlyVm9kQWg1Y3IzMmc2LUVrN1FHSmZWMXFFNG9yVTV0TzExblBQTDFwWE1IODhzN3lGU3F1bWhRUXUySHNBcGhlemVUY21ELURTdEE?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPaTZ2ZWQ2QTBxMk1iWTJ4ZXBGc3hpUDRHMDVVdFdMaGtkWVVkcEtzM2djWFpZQ1ZxTnYtUHFhMHFIbjFSSjhPSXVDWWsxdXlvQzQ1RDliaVNNUzR5QzZLWEl0UW9ROGx5RnZVdko4LWYzbWNqWEJORkJDTEVmY3ZObDgyaHNmZzRHaWpQN2ZCaDFQM05ja21J?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPUVhYalN0S3o2VVRpNWZPTU9oWEZJZnlRNi1VU1pTY3VzUXFueTh3Um9IUWIzdjY4OW9EU3kwVG5QblI5MzcxUVg2Y3J3QW5KM3RuZGh3UmRJYTRBWVR0Ql9iZVAzb2JucTM5Qi1IQkl1bHNLQXpDeFltVzhqQm9mTXFneG5GSi1vQ25oSGY0VnBrSEI5a1hWb1d3VDU?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPZkdNTVM1eXVEN0xUVTJrVzZJdWJ1X3doMmY5TEx4M3pMQ19BNTVHMS1BSjZ1SUhJQUNLOTkzdTZiX3VzVll3V1IzaDdaNk1SYW43eUs2NEhCWHNFTXRyRWpnNlFUajVQaURMeE50dnJ2d2Y3WlBmLUpQN1FhcjhTY1Nra0NzX0lLYnp5a3pjb2J0RmZ1amdGVUZ3?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPcjBvOVFKU0RhSk5mZUNBYUo5Z3lHU3NUdEVOV0NBel8wVkJhX29TY2I3MWhVR3dFclVfM0JLOFNEdXNIblA1VV84b1VxOFlsZnJsaTFBYVlhZnRNeW1weU1fZ3pXYk5MOThWeXZLUGJMNkt5dS14T2JZZGZtbnUtaXNRTHhNbV9HSWo2ei1kRmNUUE00ZnN0emIySVVQVm8?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPeXo2bXM2UVlsdURDYTdkaUx1U1YyOFBtRzhmSnhYaFdSZVhQR0ZZeGE3cWNaWTU4dWNNdUVSd0FpU1VaYkc5U09iaWhlSmV1ZDRDa19nWWRONklwT1BuSFY0Z2dZeUFkclNQSVlMN3RjOXpfY3BhZUZUUno1RnRBVkxjUk5yX21xOU9WMmtGOVYyRkUzdGhXT2d5TzZQQzZMSzF4NUhB?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
