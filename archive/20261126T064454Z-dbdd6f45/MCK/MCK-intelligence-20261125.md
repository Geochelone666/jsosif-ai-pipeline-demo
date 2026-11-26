# MCK Intelligence Report

- ticker: **MCK**
- Report as_of: **2026-11-25**
- Market data as_of: **2026-11-25**
- Quant sources: https://finance.yahoo.com/quote/MCK/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MCK/key-statistics/
- AI analysis snapshot as_of: **2026-11-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-26T06:49:45.986718+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 14, 'rule': 1, 'ai': 9, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261125T065354Z-0b3565c6/MCK** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 14 unique headlines; 10 named publishers; 0 exact duplicates; 14 HTTPS source links; largest publisher share 21.43%; oldest publication 2026-11-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 1077.3199 |
| Return 1D (%) | -0.0714 |
| Return 1W (%) | -0.6557 |
| Return 1M (%) | 7.6491 |
| Return YTD (%) | 31.7284 |
| Return 1Y (%) | 21.6221 |
| Annualized volatility (%) | 31.8455 |
| Beta vs SPY | -0.1980 |
| Max drawdown (%) | -27.1691 |
| Sharpe (rf=0) | 0.7716 |
| Downside deviation (rf=0, %) | 18.5129 |
| Sortino (rf=0) | 1.3273 |
| Historical VaR 95% (1D, %) | 2.5988 |
| Historical ES 95% (1D, %) | 3.6083 |
| Correlation vs SPY | -0.0928 |
| Tracking error vs SPY (%) | 36.4048 |
| P/E (trailing) | 27.79 |
| P/B | -31.33 |
| EV/EBITDA | 18.08 |
| Revenue growth (%) | 7.60 |
| Forward P/E (estimate) | 20.50 |
| Gross margin (%) | 3.65 |
| Operating margin (%) | 1.59 |
| Return on equity (%) | N/A |
| Free cash flow yield (%) | 5.95 |
| MA50 | 984.4438 |
| Close vs MA50 (%) | 9.4344 |
| MA200 | 880.5387 |
| Close vs MA200 (%) | 22.3478 |
| RSI (14, Wilder) | 60.0906 |
| MACD (12,26) | 25.1912 |
| MACD signal (9) | 30.4196 |
| MACD histogram | -5.2283 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MCK': 290, 'SPY': 290}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 1077.3199 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.0714 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.6557 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 7.6491 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 31.7284 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 21.6221 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 31.8455 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 18.5129 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.3273 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.5988 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.6083 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.0928 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 36.4048 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1980 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.1691 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.7716 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 20.5001 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 3.6530 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 1.5900 -> No interpretation rule is available for this metric.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 5.9514 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 27.7875 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 60.0906 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -5.2283 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 9.4344 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 22.3478 -> Clearly above the moving-average trend level.

## TAILWINDS

### McKesson (MCK) Stock Still Sits Below Fair Value On Raised EPS Guidance
- Summary: McKesson (MCK) Stock Still Sits Below Fair Value On Raised EPS Guidance
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQOUVrbFZVZkNmN3hvUk95azRidjJTMzc1TUwyUjNLR2FSSGNPbUxFVzdnek1uU0NDOURtd00wUmEwaDBXal90MnBTbnlxdjJFdDVsR1c4MWV4a3ktb2N5cC1wRmxXNGw2bWR6MWVUYWVxTTNwRmd6dUpmTThpVDZqTkJFRVJWeVpmLWR0amdLSDFqS2xmRzBMQUZB?oc=5>

### Here's Why You Should Add McKesson Stock to Your Portfolio Now
- Summary: Recommends adding McKesson to portfolio due to favorable outlook.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3gFBVV95cUxOYlpDbXo3OEVzQm5ySUoyTkhsTjFyTFZ6UjZzWGxjWXJfME1neS1IaXh1M2ViU2s3UzlUZUxzV1FBWTZ2ZFlCeU1EUnlSTXdVSUtqQ2ozTnN5QU5LdmE4VTg1Sk9fYkpUYzl6bndZak54VWplMDdQc25BU0ZqcVhtRU1IOTJIZXVlQzFfM24zbVphcW1kMW5PNVdEc2U3cE5vOG1IWU5GcHFsTUJQZ3lvbWVYLWo3Mndqd2RMcTlEZ1AxQjVvTHF2LTZXWDF1YnVNNEZKUHhkdUpibjlWTlE?oc=5>

### Do Wall Street Analysts Like McKesson Stock?
- Summary: Wall Street analysts discuss McKesson’s stock performance and potential upside.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxOc1h0YnprSHlCSXBvX3ZJYV8xTUhNMDlPRTFVSElBQ01pY01Jb3ozWFhkUll0MDlsNndoa05nWTBjYzBpV1pWSHBzZ2VLYU83N040WmFYZDhRZTU3akFoRVFLQWwxTnpEeExpLU5VTTlFenJxRU84dF9rYnZuS2VYMzA2eUdDMHN0QlV1Uko3b0VkUS1SdS16LVlqLXNIZkVWNHc?oc=5>

### Here's How Much $1000 Invested In McKesson 15 Years Ago Would Be Worth Today
- Summary: Illustrates long-term growth of McKesson shares over 15 years.
- Date: 2026-11-24 | Impact: low | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxNME94U1VmRERqTVVKQmJGcEFhZ3BlZE1ONVUxN1RhNmdRMkxvTlZfcHdOQ2NNRlYzZWlkUHR1bnBjc3YxeWg4VE5TR2R0Q25CVFVvamJxRkJzSldoWFFja2tYSHQ2NmwtYlNmaEJYdnZkSWFYYXZMbWhjN3BiTDdkSkdmRzNXOXRxbk5PUENCMmZtRU5EZ3NoLTMzLUp2NG5pZ0ltSHcwNDFoelBFWjFCRXQ2SE80NG1a?oc=5>

### The Early Signs Before McKesson Stock’s 44% Rise
- Summary: Highlights indicators preceding a significant rise in McKesson shares.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxQV0gweEJOR1MxRUw2d2RIcV9pN1Rfb1NzR1prc002enNVY2k5Z3lNMlA3R2Z5bE0yRzF3aUVaNXIzVW1vM200OV8tVHdqOHVRRWp3SVV6NXNKUkl3UU5ydGZFc0x6alJrMG9LUHVtZ0lyU1JCaHFuTDVKOVJpSTliYkpuc21hVzlCT24xeDZ0dmhuZTlSWG50cmczQXR0TUNabHpjckhkbUhWdw?oc=5>

### McKesson (MCK) Expands In Oncology And Multispecialty Care
- Summary: McKesson expands its oncology and multispecialty care services, indicating growth potential.
- Date: 2026-11-21 | Impact: high | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxPbHhHbkthcWZpaHZCbXlvbkZMMElSZTNlbzQ2VHpnOUVzVjRKUkx3MmNzWnB0bG1vTGZMc3VLeE5ybUNubDUyX2VRcDN1YXg5M3h0dlNhS19Fc2tjRklpcGY1Z2phdmFWdVR3c0tWUWlCNVJxTFdwNVJ3MzhCSWhFTFE0LTRDa1hJOE1TcnZieWxXZ01Jc3ZlU1F3MGd2bmxxcDFwNnZwLUV0MVozNTlWRjBfcU5ESEtqa2ZWYmluY9IBxAFBVV95cUxNWFpiaHQwMUpyb2dBb0lldG9yZHNXdU5OVUZRUVZOVzdvbTJiemxxc1FYdzNpZW1vbHhlZkwtbFdIUFdXUU9mTVg1RG0zbDlBQkJIQ29abnRLQlpINm9JbDJDbFZMNXNYa3V2MlhzbXFpS1VqeEtMSVY2Zk1PbXZiVFhCNVM2MDJ1VUt5b0owU3pNVmpNdVZ4STN6cnVnTUl0cDJPNW4zcWxkNDJOMlA1aXVUbXJVcVJ6Z29DMWRkTm9IaW4z?oc=5>

### Two Deals and a Higher Target: UBS’s Call on McKesson (MCK)
- Summary: UBS raises target price for McKesson, citing two deals that could boost revenue.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxQdG1zMDh1d1doZEFIWG9aa281cWdxa1Fhb05zcHlSOHBFNnpFVjRDVG93SWVPSm5XYXlQVEE4bll2UHZrOVB1MjdSdjZtRUpFcVQ2M256Q1BqVjFNZmpkVThtZ3FJMVJhNS1Vbk9fX0s5cnRSR0o1bjk0R0pEQWt0R3ZB?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### McKesson (MCK) Dropped, So What Is Driving Attention Now?
- Summary: McKesson’s stock fell, prompting analysis of underlying factors influencing investor focus.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxQMWM4YWNWVThOUEk1MGlBYmhMYjgxdk10UnUtQjcxNEJmeldDN3ZuZEM2SjJfeVphcFRmQ2ZVRlNiRWI0NW4wQ3h1Z05GOWdqV2pIQ2NEUkxwWWNBcWwtUFNRaDBRdmJWQ29Nd19Lci16RlN1TlVvaENRbTNBTlNucTBZOEpSalBaSWd0ZjNsM0k?oc=5>

### Brokers Suggest Investing in McKesson (MCK): Read This Before Placing a Bet
- Summary: Brokerages recommend buying McKesson shares, highlighting potential upside and favorable market conditions.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOd0FmakpWMUFBR2Zhd0NkMkszOFl2YzJGNWZkcnhRdHVhTXFUQ2xvNUI0QWs1dDhMdVJBelZOQkJfZnZBdjBRQjNQOXBZMHBfZnRod3ZjUUNoazg3T1hWak5lNFl6WEE5ZW5HSTFwbEZzWkN2bXNSNzRKRmVqY2Q1YkM1eGhZOEJEbTNwWmZ5TG0yOHpEcWMwU3JYejFOYVktTGktZXBB?oc=5>

### Should Stronger Oncology Earnings Require Action From McKesson (MCK) Investors?
- Summary: Investors debate whether improved oncology earnings warrant strategic action.
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxOUlFDTE9CeW1vRGdkSTYtT29CUUdETjRxMkRtTHJuYTVQMlRzeE9zd3BJQWFnWkJ3X0JKbmVJUjBuNHZxYS1UNzk3Z3JUeDBDU3ZXd3BTLTA5Z2d1MUtjRGNITkp0QVpJU08xNEVRazAyTEVTaFFlcG95VDVVZWtYblkwTTdSdjNxZlhOZjB6cU5LVnlhYWUzZlR6WUlmMlpNM28xdXZyMG9naUJGVkRhcnZoZ2hpVFNiZjVjblZLTnlnTDFh0gHKAUFVX3lxTE1iQ3pfRGxFc05ZNGRuaGFIdGxlaHplMW02MjFiQldzRmlELTRnV0I4eTRNblVBZzl6cS1ESUlmcy1pNHpXaXR4emtnX3pHSmhtbjNmS1pUUVYyYkRKTWczYWthZFUxazFETVF6Y0RMTmhqeV9iNXRqWjA2YkNKYkdJSFFjb2NPNDg3NWwxLU1fR25nX1J6bURaZklDc0xyN3Y5c19YcVhYcTIzR1VLUGxTZTNnSExfbllSdkNTREpaSDNqYXl6TXI2RGc?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MCK** | **27.79** | **-31.33** | **18.08** | **7.60** | **124,383,764,480.00 USD** | **21.62** |
| COR | 19.72 | 18.35 | 12.93 | 5.50 | 67,562,356,736.00 USD | -4.78 |
| CAH | 36.60 | -21.70 | 15.75 | 5.50 | 65,390,870,528.00 USD | 33.62 |
| CNC | 22.25 | 1.44 | 5.14 | 0.20 | 32,050,700,288.00 USD | 63.24 |

Peers fetched as_of: 2026-11-25; MCK reuses existing data (market data as_of: 2026-11-25); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-04
- Next expected earnings: 2027-02-03 (yfinance; expected dates may change)

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
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 29,980,000,000.00 USD; period 2011-04-01/2011-06-30; fiscal year/reporting period 2011/Q1
- Net income (latest available single quarter): 1,218,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2027/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/927653/000092765326000281/mck-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimgFBVV95cUxQOUVrbFZVZkNmN3hvUk95azRidjJTMzc1TUwyUjNLR2FSSGNPbUxFVzdnek1uU0NDOURtd00wUmEwaDBXal90MnBTbnlxdjJFdDVsR1c4MWV4a3ktb2N5cC1wRmxXNGw2bWR6MWVUYWVxTTNwRmd6dUpmTThpVDZqTkJFRVJWeVpmLWR0amdLSDFqS2xmRzBMQUZB?oc=5
- https://news.google.com/rss/articles/CBMi3gFBVV95cUxOYlpDbXo3OEVzQm5ySUoyTkhsTjFyTFZ6UjZzWGxjWXJfME1neS1IaXh1M2ViU2s3UzlUZUxzV1FBWTZ2ZFlCeU1EUnlSTXdVSUtqQ2ozTnN5QU5LdmE4VTg1Sk9fYkpUYzl6bndZak54VWplMDdQc25BU0ZqcVhtRU1IOTJIZXVlQzFfM24zbVphcW1kMW5PNVdEc2U3cE5vOG1IWU5GcHFsTUJQZ3lvbWVYLWo3Mndqd2RMcTlEZ1AxQjVvTHF2LTZXWDF1YnVNNEZKUHhkdUpibjlWTlE?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOc1h0YnprSHlCSXBvX3ZJYV8xTUhNMDlPRTFVSElBQ01pY01Jb3ozWFhkUll0MDlsNndoa05nWTBjYzBpV1pWSHBzZ2VLYU83N040WmFYZDhRZTU3akFoRVFLQWwxTnpEeExpLU5VTTlFenJxRU84dF9rYnZuS2VYMzA2eUdDMHN0QlV1Uko3b0VkUS1SdS16LVlqLXNIZkVWNHc?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxNME94U1VmRERqTVVKQmJGcEFhZ3BlZE1ONVUxN1RhNmdRMkxvTlZfcHdOQ2NNRlYzZWlkUHR1bnBjc3YxeWg4VE5TR2R0Q25CVFVvamJxRkJzSldoWFFja2tYSHQ2NmwtYlNmaEJYdnZkSWFYYXZMbWhjN3BiTDdkSkdmRzNXOXRxbk5PUENCMmZtRU5EZ3NoLTMzLUp2NG5pZ0ltSHcwNDFoelBFWjFCRXQ2SE80NG1a?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxQV0gweEJOR1MxRUw2d2RIcV9pN1Rfb1NzR1prc002enNVY2k5Z3lNMlA3R2Z5bE0yRzF3aUVaNXIzVW1vM200OV8tVHdqOHVRRWp3SVV6NXNKUkl3UU5ydGZFc0x6alJrMG9LUHVtZ0lyU1JCaHFuTDVKOVJpSTliYkpuc21hVzlCT24xeDZ0dmhuZTlSWG50cmczQXR0TUNabHpjckhkbUhWdw?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxPbHhHbkthcWZpaHZCbXlvbkZMMElSZTNlbzQ2VHpnOUVzVjRKUkx3MmNzWnB0bG1vTGZMc3VLeE5ybUNubDUyX2VRcDN1YXg5M3h0dlNhS19Fc2tjRklpcGY1Z2phdmFWdVR3c0tWUWlCNVJxTFdwNVJ3MzhCSWhFTFE0LTRDa1hJOE1TcnZieWxXZ01Jc3ZlU1F3MGd2bmxxcDFwNnZwLUV0MVozNTlWRjBfcU5ESEtqa2ZWYmluY9IBxAFBVV95cUxNWFpiaHQwMUpyb2dBb0lldG9yZHNXdU5OVUZRUVZOVzdvbTJiemxxc1FYdzNpZW1vbHhlZkwtbFdIUFdXUU9mTVg1RG0zbDlBQkJIQ29abnRLQlpINm9JbDJDbFZMNXNYa3V2MlhzbXFpS1VqeEtMSVY2Zk1PbXZiVFhCNVM2MDJ1VUt5b0owU3pNVmpNdVZ4STN6cnVnTUl0cDJPNW4zcWxkNDJOMlA1aXVUbXJVcVJ6Z29DMWRkTm9IaW4z?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxQdG1zMDh1d1doZEFIWG9aa281cWdxa1Fhb05zcHlSOHBFNnpFVjRDVG93SWVPSm5XYXlQVEE4bll2UHZrOVB1MjdSdjZtRUpFcVQ2M256Q1BqVjFNZmpkVThtZ3FJMVJhNS1Vbk9fX0s5cnRSR0o1bjk0R0pEQWt0R3ZB?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxQMWM4YWNWVThOUEk1MGlBYmhMYjgxdk10UnUtQjcxNEJmeldDN3ZuZEM2SjJfeVphcFRmQ2ZVRlNiRWI0NW4wQ3h1Z05GOWdqV2pIQ2NEUkxwWWNBcWwtUFNRaDBRdmJWQ29Nd19Lci16RlN1TlVvaENRbTNBTlNucTBZOEpSalBaSWd0ZjNsM0k?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOd0FmakpWMUFBR2Zhd0NkMkszOFl2YzJGNWZkcnhRdHVhTXFUQ2xvNUI0QWs1dDhMdVJBelZOQkJfZnZBdjBRQjNQOXBZMHBfZnRod3ZjUUNoazg3T1hWak5lNFl6WEE5ZW5HSTFwbEZzWkN2bXNSNzRKRmVqY2Q1YkM1eGhZOEJEbTNwWmZ5TG0yOHpEcWMwU3JYejFOYVktTGktZXBB?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxOUlFDTE9CeW1vRGdkSTYtT29CUUdETjRxMkRtTHJuYTVQMlRzeE9zd3BJQWFnWkJ3X0JKbmVJUjBuNHZxYS1UNzk3Z3JUeDBDU3ZXd3BTLTA5Z2d1MUtjRGNITkp0QVpJU08xNEVRazAyTEVTaFFlcG95VDVVZWtYblkwTTdSdjNxZlhOZjB6cU5LVnlhYWUzZlR6WUlmMlpNM28xdXZyMG9naUJGVkRhcnZoZ2hpVFNiZjVjblZLTnlnTDFh0gHKAUFVX3lxTE1iQ3pfRGxFc05ZNGRuaGFIdGxlaHplMW02MjFiQldzRmlELTRnV0I4eTRNblVBZzl6cS1ESUlmcy1pNHpXaXR4emtnX3pHSmhtbjNmS1pUUVYyYkRKTWczYWthZFUxazFETVF6Y0RMTmhqeV9iNXRqWjA2YkNKYkdJSFFjb2NPNDg3NWwxLU1fR25nX1J6bURaZklDc0xyN3Y5c19YcVhYcTIzR1VLUGxTZTNnSExfbllSdkNTREpaSDNqYXl6TXI2RGc?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
