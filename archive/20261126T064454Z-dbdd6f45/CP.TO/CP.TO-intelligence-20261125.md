# CP.TO Intelligence Report

- ticker: **CP.TO**
- Report as_of: **2026-11-25**
- Market data as_of: **2026-11-25**
- Quant sources: https://finance.yahoo.com/quote/CP.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CP.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-26T07:09:37.100633+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 16, 'rule': 0, 'ai': 10, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261125T065354Z-0b3565c6/CP.TO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **3**; {'low_uncalibrated_model_confidence': 1, 'short_term_price_move_in_structural_risks': 2}
- RSS source audit (metadata only, not article fact-checking): 16 unique headlines; 8 named publishers; 0 exact duplicates; 16 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-11-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 132.4600 |
| Return 1D (%) | -0.0226 |
| Return 1W (%) | -0.8459 |
| Return 1M (%) | 5.5290 |
| Return YTD (%) | 31.9288 |
| Return 1Y (%) | 32.3953 |
| Annualized volatility (%) | 22.0512 |
| Beta vs SPY | 0.3385 |
| Max drawdown (%) | -11.9692 |
| Sharpe (rf=0) | 1.3881 |
| Downside deviation (rf=0, %) | 14.5271 |
| Sortino (rf=0) | 2.1070 |
| Historical VaR 95% (1D, %) | 1.8632 |
| Historical ES 95% (1D, %) | 2.9374 |
| Correlation vs SPY | 0.2286 |
| Tracking error vs SPY (%) | 23.8108 |
| P/E (trailing) | 30.59 |
| P/B | 2.52 |
| EV/EBITDA | 16.77 |
| Revenue growth (%) | 15.20 |
| Forward P/E (estimate) | 22.43 |
| Gross margin (%) | 52.76 |
| Operating margin (%) | 39.78 |
| Return on equity (%) | 8.27 |
| Free cash flow yield (%) | 2.38 |
| MA50 | 126.2499 |
| Close vs MA50 (%) | 4.9189 |
| MA200 | 121.6823 |
| Close vs MA200 (%) | 8.8572 |
| RSI (14, Wilder) | 56.9294 |
| MACD (12,26) | 1.6174 |
| MACD signal (9) | 1.9822 |
| MACD histogram | -0.3648 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CP.TO': 289, 'SPY': 290}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 132.4600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.0226 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.8459 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 5.5290 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 31.9288 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 32.3953 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 22.0512 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.5271 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.1070 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.8632 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.9374 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2286 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.8108 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3385 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -11.9692 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.3881 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 22.4321 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 52.7640 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 39.7760 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 8.2680 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.3785 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 30.5912 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 56.9294 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.3648 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 4.9189 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 8.8572 -> Clearly above the moving-average trend level.

## TAILWINDS

### Canadian Pacific Kansas City (TSX:CP) Stock Looks Fully Priced Following Its 48% Run
- Summary: Stock appears fully priced after a 48% rally.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQX3gyVkdfTVJNOUlla2VlOFVqVG94Smw4YmpFcFBYRUxoQVhrRExDbU9KSFhOOEtlXzhUVFk5dEJ3b0NfRWdGWl9lUU5qVzgyZTVLN3R6WHpNREpSOTlwQU1SQWF3NnM0SC1rdFg1WEp6RlBtaUZSWlhzRFc4c1ZLUU9LbkdZYUpBcFRPLVNZemg3UVRfY0FwSnU1MDBsdw?oc=5>

### S&P upgrades CPKC to A- on diversified growth, Mexico-US corridor
- Summary: S&P raises CPKC rating to A- citing diversified growth and Mexico-US corridor expansion.
- Date: 2026-11-25 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPU2dwamdiVGlFRXhBSThvR3NuRG9YcUYwTk9SbjQybERNRDBGelRCc1JPYm85Tjc2SDJUQWtUVHpvVktIUEpqTzNLWHp4WkJaWENoZ1Z4Z0d0NUtQWUNoTkZLbmh4Q0ZHeGRDZG5ZVzdRSFlMNDJIWkxTZ2hCTm53TEhXRGVKbHQ4cTdOakl3OEZLTGNkOTkzR2RyOVByZW1r?oc=5>

### Canadian Pacific Kansas City merger review gains support: Can CP stock recover from recent weakness?
- Summary: Merger review gains support, suggesting potential positive impact on CP stock.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxNcjhlaHEzYmZPZ2daaDlhZ19VMnZ3MTB4TVU4MWVJWHo1S09DUWQxTTZPUHExaWJkeFcxVjVCZVJLXzhnd0hHbW9IWjhRMktjT3NZZmt1ckpwdkFaSllkeFRyQUZCNTItbTVGdDZBRTNDR2Z0OUVPclRCSUJsWlNDWGEtZ1NsdERwd0dtNXRKYno?oc=5>

### Is Freight Volume Growth Altering The Investment Case For CPKC Stock?
- Summary: Freight volume growth may strengthen CPKC's investment case.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxOeTd0VzF1YlRqYWRxdDk2VGRjZkxCSDFXd1lkd3BqNnMtUTZqTnE5YTJGUHJROTdzNWZSeFQ2Nmdvc1NyeEc4ZTBnM2dfay1yeDlORFZDa0dfTEg5Ym9FSFNIbnh0WDlXdGg0NE5vT21URVRJM0xxQVplLWdIVzZwUXhfajRqV2puZnREYnY3d29SbEMxdGlEc1l6cnpFRGRmcng1VlV0RzBWUQ?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### S&P upgrades Canadian Pacific Kansas City to A- on cross-border growth momentum
- Summary: S&P raises CP.TO rating to A- citing cross-border growth momentum.
- Date: 2026-11-24 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxPc2dCRS1WQWhHM2lzaWVzMFkzb0ZkODhIWEl4aEtqMHpxMVp5MzZkVFhia3BPVnJvSTc0ZUxyUVFTMGxhOHl1czRxQWNaWTNuejFZSHJiZWtvNlVtQ3BPdUU4YVQ1Q0QxWHNZcndFakRzY1puektnbXlSQ3lyMEdNTHd1M2pRbk5Na1JmTFdaaXcwNzZlN3hTTjlsODNlanMzLVZ0MmZydDM5VkhJMmZLTm8zZFZpLTNqMjdHQ3dteVcxWFA3dGd2ZWVGYVluZw?oc=5>

### Canadian Pacific Kansas City Sees Strongest Quarter as Grain and Intermodal Volumes Surge
- Summary: CP reports strongest quarter with grain and intermodal volume surge.
- Date: 2026-11-22 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPMnFGZ01ldmhDeVFRT1RrX2Y2Y3U4dFMwQXF5cGFQTG5EbW5TRmM5ZjUxeGVsdXcwSlpYS0gwYU1saXQwM1VNbWM4eWZwOHpEUTBObk91Q3ZuaVY1YmsxWUhNeThmOHduc3hEclhoX0lQdDJhRGhfNHBSOXlfbGxzQjJhSkNtRmFvNmExUTV2eXYwR05KMElzbmpqZ216Zzg?oc=5>

### CPKC's President and CEO Keith Creel to address the 2026 UBS Global Industrials and Transportation Conference
- Summary: CP CEO Keith Creel to speak at 2026 UBS conference.
- Date: 2026-11-18 | Impact: low | Horizon: medium | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOeVpuekFWZ3BEZUNNZnk5OUhyZXFKQjRqVWhhd05GQ20zNFA2ZUJaR1dCend4YUN0cHNFMi1qUHNVMkdJQ3g2OGVBQTlQZU9FLURWbmtKZUdYNEcwdTk1NmtrR3M0Z1FkZU1Pd0MwQkRKbFJhOEpxMFVCYzI1ZEMxemNaaVdHaWpOR3pCNUZWcnM1YTFocWRDejI3X2x5TWM?oc=5>

## RISKS

### Canadian Pacific Kansas City reports volume surge: CP faces an upside barrier
- Summary: Volume surge noted, but an upside barrier limits upside potential.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxOQWo0V2NnWEotVDAzUGJxWkc2YkxkUWoycFB5LTVvMDVFZ1hCeVFUVWg0Z1BGMFA0Nlg1eklEMi1QYTFkN2hodjhOa0lha2hPSmtjSG5oQkR4SVBQMFhlaTRoTmY3NHNGVWR5c3hlcW9yTXdRVGxmMlMwaU5PaU1ub1VIbmtpTXR5QkE?oc=5>

### Can CP avoid deeper losses amid ongoing selling pressure and key support at C$121.82?
- Summary: CP may face deeper losses; support at C$121.82.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxQTHRtOGxpM2JFVm16UHZ5T1BRQUlGVHctMWFKS3lpemZtTDlXYjJ5Z3AxSWJqQldSZjl6V1ZFRFVjSFl1dy1LVHlxLV9OQkNwSF9RdFJSMUpBXzZyNHQ1eEU2Q3VDbk50dUY1MkdHaW4teThJRnRPdllTVkpGSHlpZ2RLdk9oeTMzWkxxb3pn?oc=5>

### Canadian Pacific Kansas City stock outlook: Price consolidates below C$134.63 resistance
- Summary: CP stock consolidates below C$134.63 resistance.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxQaGpBSDBnSEZBUE9BWDljcnFndWkxNWJLcm5oVDBOQjFEbkFqaDEzZnlYLVh3WXVaTlBhcWdYMU5OdXJ2NVZnTF9BeGo5ZGJCUVloMUJjTWRGUVJFbzlRVXk0ejl5MHRISU05elZMbTVqYUhqbFdlU0dMY2dHN2ZKN2dCOG52TEt0ZGc?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CP.TO** | **30.59** | **2.52** | **16.77** | **15.20** | **115,181,232,128.00 CAD** | **32.40** |
| CNR.TO | 22.66 | 4.92 | 13.93 | 14.60 | 107,742,101,504.00 CAD | 40.76 |
| UNP | 23.27 | 8.05 | 15.46 | 15.30 | 177,312,448,512.00 USD | 32.97 |
| NSC | 27.37 | 4.38 | 15.35 | 13.60 | 73,339,600,896.00 USD | 14.87 |

Peers fetched as_of: 2026-11-25; CP.TO reuses existing data (market data as_of: 2026-11-25); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-28
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
- Filing date: 2026-10-29
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: https://www.sec.gov/Archives/edgar/data/16875/000001687526000033/cp-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMingFBVV95cUxQX3gyVkdfTVJNOUlla2VlOFVqVG94Smw4YmpFcFBYRUxoQVhrRExDbU9KSFhOOEtlXzhUVFk5dEJ3b0NfRWdGWl9lUU5qVzgyZTVLN3R6WHpNREpSOTlwQU1SQWF3NnM0SC1rdFg1WEp6RlBtaUZSWlhzRFc4c1ZLUU9LbkdZYUpBcFRPLVNZemg3UVRfY0FwSnU1MDBsdw?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPU2dwamdiVGlFRXhBSThvR3NuRG9YcUYwTk9SbjQybERNRDBGelRCc1JPYm85Tjc2SDJUQWtUVHpvVktIUEpqTzNLWHp4WkJaWENoZ1Z4Z0d0NUtQWUNoTkZLbmh4Q0ZHeGRDZG5ZVzdRSFlMNDJIWkxTZ2hCTm53TEhXRGVKbHQ4cTdOakl3OEZLTGNkOTkzR2RyOVByZW1r?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxNcjhlaHEzYmZPZ2daaDlhZ19VMnZ3MTB4TVU4MWVJWHo1S09DUWQxTTZPUHExaWJkeFcxVjVCZVJLXzhnd0hHbW9IWjhRMktjT3NZZmt1ckpwdkFaSllkeFRyQUZCNTItbTVGdDZBRTNDR2Z0OUVPclRCSUJsWlNDWGEtZ1NsdERwd0dtNXRKYno?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxOeTd0VzF1YlRqYWRxdDk2VGRjZkxCSDFXd1lkd3BqNnMtUTZqTnE5YTJGUHJROTdzNWZSeFQ2Nmdvc1NyeEc4ZTBnM2dfay1yeDlORFZDa0dfTEg5Ym9FSFNIbnh0WDlXdGg0NE5vT21URVRJM0xxQVplLWdIVzZwUXhfajRqV2puZnREYnY3d29SbEMxdGlEc1l6cnpFRGRmcng1VlV0RzBWUQ?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxPc2dCRS1WQWhHM2lzaWVzMFkzb0ZkODhIWEl4aEtqMHpxMVp5MzZkVFhia3BPVnJvSTc0ZUxyUVFTMGxhOHl1czRxQWNaWTNuejFZSHJiZWtvNlVtQ3BPdUU4YVQ1Q0QxWHNZcndFakRzY1puektnbXlSQ3lyMEdNTHd1M2pRbk5Na1JmTFdaaXcwNzZlN3hTTjlsODNlanMzLVZ0MmZydDM5VkhJMmZLTm8zZFZpLTNqMjdHQ3dteVcxWFA3dGd2ZWVGYVluZw?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPMnFGZ01ldmhDeVFRT1RrX2Y2Y3U4dFMwQXF5cGFQTG5EbW5TRmM5ZjUxeGVsdXcwSlpYS0gwYU1saXQwM1VNbWM4eWZwOHpEUTBObk91Q3ZuaVY1YmsxWUhNeThmOHduc3hEclhoX0lQdDJhRGhfNHBSOXlfbGxzQjJhSkNtRmFvNmExUTV2eXYwR05KMElzbmpqZ216Zzg?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOeVpuekFWZ3BEZUNNZnk5OUhyZXFKQjRqVWhhd05GQ20zNFA2ZUJaR1dCend4YUN0cHNFMi1qUHNVMkdJQ3g2OGVBQTlQZU9FLURWbmtKZUdYNEcwdTk1NmtrR3M0Z1FkZU1Pd0MwQkRKbFJhOEpxMFVCYzI1ZEMxemNaaVdHaWpOR3pCNUZWcnM1YTFocWRDejI3X2x5TWM?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxOQWo0V2NnWEotVDAzUGJxWkc2YkxkUWoycFB5LTVvMDVFZ1hCeVFUVWg0Z1BGMFA0Nlg1eklEMi1QYTFkN2hodjhOa0lha2hPSmtjSG5oQkR4SVBQMFhlaTRoTmY3NHNGVWR5c3hlcW9yTXdRVGxmMlMwaU5PaU1ub1VIbmtpTXR5QkE?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxQTHRtOGxpM2JFVm16UHZ5T1BRQUlGVHctMWFKS3lpemZtTDlXYjJ5Z3AxSWJqQldSZjl6V1ZFRFVjSFl1dy1LVHlxLV9OQkNwSF9RdFJSMUpBXzZyNHQ1eEU2Q3VDbk50dUY1MkdHaW4teThJRnRPdllTVkpGSHlpZ2RLdk9oeTMzWkxxb3pn?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxQaGpBSDBnSEZBUE9BWDljcnFndWkxNWJLcm5oVDBOQjFEbkFqaDEzZnlYLVh3WXVaTlBhcWdYMU5OdXJ2NVZnTF9BeGo5ZGJCUVloMUJjTWRGUVJFbzlRVXk0ejl5MHRISU05elZMbTVqYUhqbFdlU0dMY2dHN2ZKN2dCOG52TEt0ZGc?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
