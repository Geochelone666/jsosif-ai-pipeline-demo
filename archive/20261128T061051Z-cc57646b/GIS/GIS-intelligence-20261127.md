# GIS Intelligence Report

- ticker: **GIS**
- Report as_of: **2026-11-27**
- Market data as_of: **2026-11-27**
- Quant sources: https://finance.yahoo.com/quote/GIS/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/GIS/key-statistics/
- AI analysis snapshot as_of: **2026-11-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-28T06:21:35.450843+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 12, 'rule': 2, 'ai': 8, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261126T064454Z-dbdd6f45/GIS** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 12 unique headlines; 6 named publishers; 0 exact duplicates; 12 HTTPS source links; largest publisher share 50.0%; oldest publication 2026-11-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 35.8500 |
| Return 1D (%) | -1.1035 |
| Return 1W (%) | 0.3078 |
| Return 1M (%) | 7.1108 |
| Return YTD (%) | -17.5841 |
| Return 1Y (%) | -18.7548 |
| Annualized volatility (%) | 31.3189 |
| Beta vs SPY | -0.4211 |
| Max drawdown (%) | -33.2524 |
| Sharpe (rf=0) | -0.5252 |
| Downside deviation (rf=0, %) | 21.6496 |
| Sortino (rf=0) | -0.7598 |
| Historical VaR 95% (1D, %) | 2.9986 |
| Historical ES 95% (1D, %) | 3.8866 |
| Correlation vs SPY | -0.2020 |
| Tracking error vs SPY (%) | 37.3706 |
| P/E (trailing) | N/A |
| P/B | 2.57 |
| EV/EBITDA | 9.48 |
| Revenue growth (%) | -2.80 |
| Forward P/E (estimate) | 11.41 |
| Gross margin (%) | 33.73 |
| Operating margin (%) | 15.62 |
| Return on equity (%) | -10.49 |
| Free cash flow yield (%) | 6.80 |
| MA50 | 33.7775 |
| Close vs MA50 (%) | 6.1357 |
| MA200 | 35.4442 |
| Close vs MA200 (%) | 1.1449 |
| RSI (14, Wilder) | 56.7969 |
| MACD (12,26) | 0.4611 |
| MACD signal (9) | 0.3437 |
| MACD histogram | 0.1174 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'GIS': 291, 'SPY': 291}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 35.8500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.1035 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.3078 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 7.1108 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -17.5841 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -18.7548 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 31.3189 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.6496 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.7598 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9986 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.8866 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.2020 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.3706 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.4211 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -33.2524 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.5252 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 11.4051 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 33.7280 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 15.6240 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: -10.4950 -> Adjusted price fell over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 6.7956 -> No interpretation rule is available for this metric.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 56.7969 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.1174 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 6.1357 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 1.1449 -> Slightly above the moving-average trend level.

## TAILWINDS

### Here's How Much $2,500 in General Mills Stock Could Pay You in Dividends in 2027
- Summary: Projected dividend payout for $2,500 investment in 2027.
- Date: 2026-11-21 | Impact: medium | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxQQlFNQW5Nd3h4VVRMTGR2M3V3SDg0RHVTQUpKa1FqcTNVRGtiOGxMTC0wRVVNNDU1UzhxaXJoZUFCVHhoN1RnLXN0VDF0N0NwVnBEZmpkRFItbmhWOUZWU1FOamUtS0M5blJkN0JaV2hSNU5HNDdHbHkxQlNSZkFYZnF5V21fTi1sRWk1dG1yckdXYTBiSW1KdFlVSkNVX0hwdGxIa0NUQU83eFM3RXJFaXB5TjJyOGJXNkFQUVdSYUhHTXM?oc=5>

### General Mills (GIS) is Suddenly Drawing Wall Street’s Attention
- Summary: Wall Street shows renewed interest in General Mills stock.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOMGJ2RGZIMlVrUGM0TGxWV0F2STRMb3l3aEFnZDc2VGxsSXZkc2RwOWc1MWlsT2Y4QUlHU1dSbW1USHNuWkROUjEtcWZwd1BxX1FiZXRYN1lad284R2RwS1JELVQ4QjR2M2J1TjJPSUg5dlRJVHRGdERUcGZKYklyb2JsclQyTncyRnZGQTFfQ09yaDhSWG1QUmh0NUpRSUtW?oc=5>

### General Mills (NYSE:GIS) Stock Purchase Reported by Rep. Harriet M. Hageman
- Summary: A U.S. Representative purchased General Mills shares, indicating support.
- Date: 2026-11-25 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxOa1hDOXZqLV81Z2lyMGduVUM2c1ZsZWEwV3h0OXQ3bGZzXzdHc3lGc21KaEp3OTllMTJITFJVUkEzV3EzMTZXbmZLb3ZkNWJJSDZabkpQNlV4NFZ2Uk0zZTdFc3hXV0dsOVR2Q3k2d1RWdk5lOVh0MWJ6NjhpSEN3ZUdCUE91b3NBcXh1OTJndjJvR2NKWEpZSGp1cTlVUzRGdkpZcnI3cHBRMWhLUXBQLUYyV21BZXJnOFNFUWwxbC13VGY3aDJOd2hxT0RkV2M?oc=5>

### Air Products and Chemicals or General Mills: The One Dividend Stock I’d Hold for the Next 10 Years
- Summary: Article compares General Mills dividend to Air Products, suggesting long-term hold.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPeTFTdU02RmRrT1FuVXB5TDd3RThDbm90S01sdl9TRGttQjNwbmtmMGxIVDV4S3BVWFJUTXBHYm9BeUxOTEdpUkZnM2pBRjRZM1VrMGNkLXZaVFR3aEdBSGNSWlpmUmdsOThiNlNRUHJqZU54TXNpSXBmVmNUTjJtakU0UXkycC0xenljZ3o4MFNUMDhKLS1MMlc0MG9YbHRreXhJ?oc=5>

### General Mills vs. Kraft Heinz: Which Food Dividend Is Better for Retirees?
- Summary: Comparison of General Mills and Kraft Heinz dividends for retirees.
- Date: 2026-11-22 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPZXcwemduV1dHbnVZLXVQcFVvNWRlRndfOXZPb294dHVWaEdKaWREb2lORXgxTlR5TzNwODl4MXd0YVZPS2tqUUhlT21PNmo3WDZJbEpLMks4d0pzdC1VamhvU2FZYUhsMDNrSHVrX2tsWHQ3S213NXoxYVVkYWRONHhpbGtpd20zVk9OUlVhc0h6bHQxaTdqUQ?oc=5>

### Can international Häagen-Dazs review support General Mills stock?
- Summary: Examines if Häagen-Dazs review could boost General Mills shares.
- Date: 2026-11-20 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxNWmZlSU9IWFpoYXZld2ZMSVlhaWJ3djdtdEFMcWZlVG55SmFIRmxNbHAybHF1dnFTZjFKMmN4SURzMXd1VUh6a3EzSmpfUmJGX1ItMzQyaHhLRWNEV1hFdDhjVld6LTItM2hCYXEyZEpPU3cyTFhFYzlnMEc5MC13SWpMWGtDQXl5SWJoc1VR?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### General Mills (GIS) Stock Looks Fairly Valued On Sales Today
- Summary: General Mills (GIS) Stock Looks Fairly Valued On Sales Today
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPVWhIWDdadjV1RXVtckYyWkRaa3FwLU56RUY0c1ZfLTNqVnZTLUZQNVJzUHlFWFhhSk81RVNIM2R3dExvN0VrcklMMVZiRFNCYWJuUEdzZ2dHaFY5alI3S2dsa1NreDNNVTJnS05lXzhVQlUyU1pOU3BtQ0dNX1ZKS3k3NGdDWE5YaWZSRERCQ0tCZEVJa0FsMWpn?oc=5>

### General Mills (NYSE:GIS) Stock Purchased by Rep. Harriet M. Hageman
- Summary: General Mills (NYSE:GIS) Stock Purchased by Rep. Harriet M. Hageman
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxPRDVRMGd2Sm5IM3hqVGxtZEFvbXZrbU05RE1Sbkhtb2FJM0Y2YmlEcjJWM052bmNrV0s1cFk5YkdYdTZwT0tOZ1RoTlNXMEx5OWNzRm1wWU9UVG8tMG02cWRkTFNyc2pqRmMwMEg3aXNZTmJSR0Rtd2w5VFlQNW9fRFlpT281aTFKUjR5a0N2ZzJwdWtLZmNjSG5EeHc4ZG1Pd2tROTZLX2ZlbHJITll2bTRaXzV1ME5TeFJaY1ZiT2x2WndZ?oc=5>

### General Mills (GIS) Unveils New Trix And Restructuring, Is The Stock Fully Priced?
- Summary: Launch of new Trix cereal and restructuring plans announced.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOemZmMU1udzZlUVJlT1VxSHNXT2haa3d1bHBEZnB0Z3N3VVQ5QVJOb1NFTHRrbXc4UUZQb2huWnAxQTJBU2ZrYWhyZWgzZFVyd0FBNmY4Y0hFOEVpdEhYSmJ5UVlDcW1WSDlvZ0JEblJES0VkUUlTOUlsRVRkQkYyQ2dIWEZyaW9MdmV1X1F1ZjZoVGJ5ODR2MmdSRQ?oc=5>

## RISKS

### How Operating Reorganization Will Impact General Mills (GIS) Investors
- Summary: General Mills’ operating reorganization may affect investor outlook, potentially altering financial performance and market perception.
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxObVRwSkFzd3Y1Z282MkowT1hNNmh6VzNraXdkNGpTNWtYN1g0TGxYVW5vTzMtU2pGOW9XYUw2Z0tOWDBvSi15WUNKMDU2WGY4WHJZUVZvczhITjVTVHA3dWRzNWswMEVPZmFIQjdZdjlsVldBc2pYZVdNZzZoUHFXUno5ZUhBOWMxeW5aOEo0bnZWU0Zyd1hfZ2taMmNwaDV4a2xPel9vR3g5bUMwUzZuMzhzeS1fTWxDcml4akhjV1JpcGllM3I5OVFDZTBISzg3OWxBM2F4TUk4QdIB3wFBVV95cUxPZEk5TmhKX3BnTll4bEFwVThvQlNSNENscnNFYVRlR2ZhTFREdGVoZ0stbDBveFE3b1JCU0lqRVhZZTFVWkZkSUtuQnVqNTdjYzFST05rSEREbXB4MV9ZOXdwR0t1azFPLWJ4N1ZfREd6WUZUek8xNmNZck96NEpmSXFmSnNKUnRpME9CWUhSbUNxOXBwczZHOXBLX2U1eXluVV85aHRkQnlIaTBFMWpPSFdjcmxzdlJFQ2x2d0V3OHdhLUFZTG5WRUxPdmZaZzhLYk5TeU9tMkRVRklPMjc0?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **GIS** | **N/A** | **2.57** | **9.48** | **-2.80** | **19,168,532,480.00 USD** | **-18.75** |
| KHC | N/A | 0.87 | 8.81 | -2.00 | 31,359,629,312.00 USD | 10.56 |
| CPB | 18.45 | 1.87 | 8.99 | -7.90 | 7,225,777,152.00 USD | -14.96 |
| SJM | 59.28 | 2.36 | 9.40 | -2.00 | 13,567,848,448.00 USD | 27.82 |

Peers fetched as_of: 2026-11-27; GIS reuses existing data (market data as_of: 2026-11-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-23
- Next expected earnings: 2026-12-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-27

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-09-23
- Revenue (latest available single quarter): 4,389,500,000.00 USD; period 2026-06-01/2026-08-30; fiscal year/reporting period 2027/Q1
- Net income (latest available single quarter): 397,000,000.00 USD; period 2026-06-01/2026-08-30; fiscal year/reporting period 2027/Q1
- SEC link: https://www.sec.gov/Archives/edgar/data/40704/000162828026063201/gis-20260830.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiwwFBVV95cUxQQlFNQW5Nd3h4VVRMTGR2M3V3SDg0RHVTQUpKa1FqcTNVRGtiOGxMTC0wRVVNNDU1UzhxaXJoZUFCVHhoN1RnLXN0VDF0N0NwVnBEZmpkRFItbmhWOUZWU1FOamUtS0M5blJkN0JaV2hSNU5HNDdHbHkxQlNSZkFYZnF5V21fTi1sRWk1dG1yckdXYTBiSW1KdFlVSkNVX0hwdGxIa0NUQU83eFM3RXJFaXB5TjJyOGJXNkFQUVdSYUhHTXM?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOMGJ2RGZIMlVrUGM0TGxWV0F2STRMb3l3aEFnZDc2VGxsSXZkc2RwOWc1MWlsT2Y4QUlHU1dSbW1USHNuWkROUjEtcWZwd1BxX1FiZXRYN1lad284R2RwS1JELVQ4QjR2M2J1TjJPSUg5dlRJVHRGdERUcGZKYklyb2JsclQyTncyRnZGQTFfQ09yaDhSWG1QUmh0NUpRSUtW?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxOa1hDOXZqLV81Z2lyMGduVUM2c1ZsZWEwV3h0OXQ3bGZzXzdHc3lGc21KaEp3OTllMTJITFJVUkEzV3EzMTZXbmZLb3ZkNWJJSDZabkpQNlV4NFZ2Uk0zZTdFc3hXV0dsOVR2Q3k2d1RWdk5lOVh0MWJ6NjhpSEN3ZUdCUE91b3NBcXh1OTJndjJvR2NKWEpZSGp1cTlVUzRGdkpZcnI3cHBRMWhLUXBQLUYyV21BZXJnOFNFUWwxbC13VGY3aDJOd2hxT0RkV2M?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPeTFTdU02RmRrT1FuVXB5TDd3RThDbm90S01sdl9TRGttQjNwbmtmMGxIVDV4S3BVWFJUTXBHYm9BeUxOTEdpUkZnM2pBRjRZM1VrMGNkLXZaVFR3aEdBSGNSWlpmUmdsOThiNlNRUHJqZU54TXNpSXBmVmNUTjJtakU0UXkycC0xenljZ3o4MFNUMDhKLS1MMlc0MG9YbHRreXhJ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPZXcwemduV1dHbnVZLXVQcFVvNWRlRndfOXZPb294dHVWaEdKaWREb2lORXgxTlR5TzNwODl4MXd0YVZPS2tqUUhlT21PNmo3WDZJbEpLMks4d0pzdC1VamhvU2FZYUhsMDNrSHVrX2tsWHQ3S213NXoxYVVkYWRONHhpbGtpd20zVk9OUlVhc0h6bHQxaTdqUQ?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxNWmZlSU9IWFpoYXZld2ZMSVlhaWJ3djdtdEFMcWZlVG55SmFIRmxNbHAybHF1dnFTZjFKMmN4SURzMXd1VUh6a3EzSmpfUmJGX1ItMzQyaHhLRWNEV1hFdDhjVld6LTItM2hCYXEyZEpPU3cyTFhFYzlnMEc5MC13SWpMWGtDQXl5SWJoc1VR?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPVWhIWDdadjV1RXVtckYyWkRaa3FwLU56RUY0c1ZfLTNqVnZTLUZQNVJzUHlFWFhhSk81RVNIM2R3dExvN0VrcklMMVZiRFNCYWJuUEdzZ2dHaFY5alI3S2dsa1NreDNNVTJnS05lXzhVQlUyU1pOU3BtQ0dNX1ZKS3k3NGdDWE5YaWZSRERCQ0tCZEVJa0FsMWpn?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxPRDVRMGd2Sm5IM3hqVGxtZEFvbXZrbU05RE1Sbkhtb2FJM0Y2YmlEcjJWM052bmNrV0s1cFk5YkdYdTZwT0tOZ1RoTlNXMEx5OWNzRm1wWU9UVG8tMG02cWRkTFNyc2pqRmMwMEg3aXNZTmJSR0Rtd2w5VFlQNW9fRFlpT281aTFKUjR5a0N2ZzJwdWtLZmNjSG5EeHc4ZG1Pd2tROTZLX2ZlbHJITll2bTRaXzV1ME5TeFJaY1ZiT2x2WndZ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOemZmMU1udzZlUVJlT1VxSHNXT2haa3d1bHBEZnB0Z3N3VVQ5QVJOb1NFTHRrbXc4UUZQb2huWnAxQTJBU2ZrYWhyZWgzZFVyd0FBNmY4Y0hFOEVpdEhYSmJ5UVlDcW1WSDlvZ0JEblJES0VkUUlTOUlsRVRkQkYyQ2dIWEZyaW9MdmV1X1F1ZjZoVGJ5ODR2MmdSRQ?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxObVRwSkFzd3Y1Z282MkowT1hNNmh6VzNraXdkNGpTNWtYN1g0TGxYVW5vTzMtU2pGOW9XYUw2Z0tOWDBvSi15WUNKMDU2WGY4WHJZUVZvczhITjVTVHA3dWRzNWswMEVPZmFIQjdZdjlsVldBc2pYZVdNZzZoUHFXUno5ZUhBOWMxeW5aOEo0bnZWU0Zyd1hfZ2taMmNwaDV4a2xPel9vR3g5bUMwUzZuMzhzeS1fTWxDcml4akhjV1JpcGllM3I5OVFDZTBISzg3OWxBM2F4TUk4QdIB3wFBVV95cUxPZEk5TmhKX3BnTll4bEFwVThvQlNSNENscnNFYVRlR2ZhTFREdGVoZ0stbDBveFE3b1JCU0lqRVhZZTFVWkZkSUtuQnVqNTdjYzFST05rSEREbXB4MV9ZOXdwR0t1azFPLWJ4N1ZfREd6WUZUek8xNmNZck96NEpmSXFmSnNKUnRpME9CWUhSbUNxOXBwczZHOXBLX2U1eXluVV85aHRkQnlIaTBFMWpPSFdjcmxzdlJFQ2x2d0V3OHdhLUFZTG5WRUxPdmZaZzhLYk5TeU9tMkRVRklPMjc0?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
