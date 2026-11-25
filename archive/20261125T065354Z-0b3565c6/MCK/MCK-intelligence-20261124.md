# MCK Intelligence Report

- ticker: **MCK**
- Report as_of: **2026-11-24**
- Market data as_of: **2026-11-24**
- Quant sources: https://finance.yahoo.com/quote/MCK/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MCK/key-statistics/
- AI analysis snapshot as_of: **2026-11-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-25T07:12:47.871487+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 12, 'rule': 1, 'ai': 11, 'unknown': 0})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261124T081701Z-6c335e3d/MCK** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 12 unique headlines; 7 named publishers; 0 exact duplicates; 12 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-11-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 1078.0900 |
| Return 1D (%) | 2.8300 |
| Return 1W (%) | -1.2440 |
| Return 1M (%) | 7.7260 |
| Return YTD (%) | 31.8225 |
| Return 1Y (%) | 24.3762 |
| Annualized volatility (%) | 31.9141 |
| Beta vs SPY | -0.1890 |
| Max drawdown (%) | -27.1691 |
| Sharpe (rf=0) | 0.8412 |
| Downside deviation (rf=0, %) | 18.5128 |
| Sortino (rf=0) | 1.4501 |
| Historical VaR 95% (1D, %) | 2.5988 |
| Historical ES 95% (1D, %) | 3.6083 |
| Correlation vs SPY | -0.0886 |
| Tracking error vs SPY (%) | 36.4239 |
| P/E (trailing) | 27.81 |
| P/B | -31.36 |
| EV/EBITDA | 18.09 |
| Revenue growth (%) | 7.60 |
| Forward P/E (estimate) | 20.55 |
| Gross margin (%) | 3.65 |
| Operating margin (%) | 1.59 |
| Return on equity (%) | N/A |
| Free cash flow yield (%) | 5.95 |
| MA50 | 980.6432 |
| Close vs MA50 (%) | 9.9370 |
| MA200 | 879.8141 |
| Close vs MA200 (%) | 22.5361 |
| RSI (14, Wilder) | 60.3366 |
| MACD (12,26) | 26.3664 |
| MACD signal (9) | 31.7266 |
| MACD histogram | -5.3602 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MCK': 289, 'SPY': 289}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 1078.0900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.8300 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.2440 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 7.7260 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 31.8225 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 24.3762 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 31.9141 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 18.5128 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.4501 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.5988 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.6083 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.0886 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 36.4239 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1890 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.1691 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.8412 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 20.5517 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 3.6530 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 1.5900 -> No interpretation rule is available for this metric.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 5.9472 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 27.8073 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 60.3366 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -5.3602 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 9.9370 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 22.5361 -> Clearly above the moving-average trend level.

## TAILWINDS

### McKesson (MCK) Stock Still Sits Below Fair Value On Raised EPS Guidance
- Summary: McKesson (MCK) Stock Still Sits Below Fair Value On Raised EPS Guidance
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxQdW1BVTFCeUdGb29fYWRnQnRiQ0Qyd1NramlSQzFBazJmTmhGSXozaUhHcnEzUGRnR0FFYTZMVnkzVnVGZjNKeG8xa1BLY0lRV1BwTmw3YnREeWJiNHhhX2V0Snk5QUlzUng3RzhCX0E5ZEdqeXV1UEwwbGVJYmd0U2NGNVZGRXpIX203N2EzRUMyMzZxSGM3OXJ1cUJaZWYwcGZQc0M4MA?oc=5>

### McKesson (MCK) Expands In Oncology And Multispecialty Care
- Summary: McKesson expands its oncology and multispecialty care services, indicating growth potential.
- Date: 2026-11-21 | Impact: high | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxPbHhHbkthcWZpaHZCbXlvbkZMMElSZTNlbzQ2VHpnOUVzVjRKUkx3MmNzWnB0bG1vTGZMc3VLeE5ybUNubDUyX2VRcDN1YXg5M3h0dlNhS19Fc2tjRklpcGY1Z2phdmFWdVR3c0tWUWlCNVJxTFdwNVJ3MzhCSWhFTFE0LTRDa1hJOE1TcnZieWxXZ01Jc3ZlU1F3MGd2bmxxcDFwNnZwLUV0MVozNTlWRjBfcU5ESEtqa2ZWYmluY9IBxAFBVV95cUxNWFpiaHQwMUpyb2dBb0lldG9yZHNXdU5OVUZRUVZOVzdvbTJiemxxc1FYdzNpZW1vbHhlZkwtbFdIUFdXUU9mTVg1RG0zbDlBQkJIQ29abnRLQlpINm9JbDJDbFZMNXNYa3V2MlhzbXFpS1VqeEtMSVY2Zk1PbXZiVFhCNVM2MDJ1VUt5b0owU3pNVmpNdVZ4STN6cnVnTUl0cDJPNW4zcWxkNDJOMlA1aXVUbXJVcVJ6Z29DMWRkTm9IaW4z?oc=5>

### Do Wall Street Analysts Like McKesson Stock?
- Summary: Wall Street analysts discuss McKesson’s stock performance and potential upside.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxOc1h0YnprSHlCSXBvX3ZJYV8xTUhNMDlPRTFVSElBQ01pY01Jb3ozWFhkUll0MDlsNndoa05nWTBjYzBpV1pWSHBzZ2VLYU83N040WmFYZDhRZTU3akFoRVFLQWwxTnpEeExpLU5VTTlFenJxRU84dF9rYnZuS2VYMzA2eUdDMHN0QlV1Uko3b0VkUS1SdS16LVlqLXNIZkVWNHc?oc=5>

### Here's How Much $1000 Invested In McKesson 15 Years Ago Would Be Worth Today
- Summary: Illustrates long-term growth of McKesson shares over 15 years.
- Date: 2026-11-24 | Impact: low | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxNME94U1VmRERqTVVKQmJGcEFhZ3BlZE1ONVUxN1RhNmdRMkxvTlZfcHdOQ2NNRlYzZWlkUHR1bnBjc3YxeWg4VE5TR2R0Q25CVFVvamJxRkJzSldoWFFja2tYSHQ2NmwtYlNmaEJYdnZkSWFYYXZMbWhjN3BiTDdkSkdmRzNXOXRxbk5PUENCMmZtRU5EZ3NoLTMzLUp2NG5pZ0ltSHcwNDFoelBFWjFCRXQ2SE80NG1a?oc=5>

### Here's Why You Should Add McKesson Stock to Your Portfolio Now
- Summary: Recommends adding McKesson to portfolio due to favorable outlook.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3gFBVV95cUxOYlpDbXo3OEVzQm5ySUoyTkhsTjFyTFZ6UjZzWGxjWXJfME1neS1IaXh1M2ViU2s3UzlUZUxzV1FBWTZ2ZFlCeU1EUnlSTXdVSUtqQ2ozTnN5QU5LdmE4VTg1Sk9fYkpUYzl6bndZak54VWplMDdQc25BU0ZqcVhtRU1IOTJIZXVlQzFfM24zbVphcW1kMW5PNVdEc2U3cE5vOG1IWU5GcHFsTUJQZ3lvbWVYLWo3Mndqd2RMcTlEZ1AxQjVvTHF2LTZXWDF1YnVNNEZKUHhkdUpibjlWTlE?oc=5>

### Earnings Beat Might Change The Case For Investing In McKesson Stock (MCK)
- Summary: Earnings beat could alter investment considerations for McKesson.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQdHRfb1NHc3hXd29ncm9RR2t2MnM3aWlFUW5XYmF4UVpqS29aVEtmSWJsMjIxbmUzZmFxT2xmS1Q3b21yVHRlQ1ZNWDFzaWdaNFZ5eWZramdiU2tVTDRYd1JRS1RKYVBubzhYWlE0eHVhcnAzSC1abUF4SmpfWlRtNTJkQ3h2ZzNzbXBZVlJjaElON2RtY0dJ?oc=5>

### The Early Signs Before McKesson Stock’s 44% Rise
- Summary: Highlights indicators preceding a significant rise in McKesson shares.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxQV0gweEJOR1MxRUw2d2RIcV9pN1Rfb1NzR1prc002enNVY2k5Z3lNMlA3R2Z5bE0yRzF3aUVaNXIzVW1vM200OV8tVHdqOHVRRWp3SVV6NXNKUkl3UU5ydGZFc0x6alJrMG9LUHVtZ0lyU1JCaHFuTDVKOVJpSTliYkpuc21hVzlCT24xeDZ0dmhuZTlSWG50cmczQXR0TUNabHpjckhkbUhWdw?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Two Deals and a Higher Target: UBS’s Call on McKesson (MCK)
- Summary: UBS raises its target price for McKesson, citing two deals that could boost earnings and shareholder value.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxOV01GZTdJWVdxdDl5OGpKZkZmRE0xWDREM3ZlTWJrQlJSZm40cXRPelZWeWdIMUcxSlhqQ0FKSklfbjRUVThFMVlSdUNnc3FoeW40Rm1iMGNad1lkTUtoUXFqY2VDZjhvMXhKcEJkWFZCOWdvd0ZXOTQyMHVqcFVGaEFB?oc=5>

### Brokers Suggest Investing in McKesson (MCK): Read This Before Placing a Bet
- Summary: Brokerages recommend buying McKesson shares, highlighting potential upside and favorable market conditions.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOd0FmakpWMUFBR2Zhd0NkMkszOFl2YzJGNWZkcnhRdHVhTXFUQ2xvNUI0QWs1dDhMdVJBelZOQkJfZnZBdjBRQjNQOXBZMHBfZnRod3ZjUUNoazg3T1hWak5lNFl6WEE5ZW5HSTFwbEZzWkN2bXNSNzRKRmVqY2Q1YkM1eGhZOEJEbTNwWmZ5TG0yOHpEcWMwU3JYejFOYVktTGktZXBB?oc=5>

### McKesson (MCK) Dropped, So What Is Driving Attention Now?
- Summary: McKesson’s stock fell, prompting analysis of underlying factors influencing investor focus.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxQMWM4YWNWVThOUEk1MGlBYmhMYjgxdk10UnUtQjcxNEJmeldDN3ZuZEM2SjJfeVphcFRmQ2ZVRlNiRWI0NW4wQ3h1Z05GOWdqV2pIQ2NEUkxwWWNBcWwtUFNRaDBRdmJWQ29Nd19Lci16RlN1TlVvaENRbTNBTlNucTBZOEpSalBaSWd0ZjNsM0k?oc=5>

### Should Stronger Oncology Earnings Require Action From McKesson (MCK) Investors?
- Summary: Investors evaluate the implications of improved oncology earnings for McKesson’s future strategy.
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxNYkN6X0RsRXNOWTRkbmhhSHRsZWh6ZTFtNjIxYkJXc0ZpRC00Z1dCOHk0TW5VQWc5enEtRElJZnMtaTR6V2l0eHprZ196R0pobW4zZktaVFFWMmJESk1nM2FrYWRVMWsxRE1RemNETE5oanlfYjV0alowNmJDSmJHSUhRY29jTzQ4NzVsMS1NX0duZ19Sem1EWmZJQ3NMcjd2OXNfWHFYWHEyM0dVS1BsU2UzZ0hMX25ZUnZDU0RKWkgzamF5ek1yNkRn0gHKAUFVX3lxTE1iQ3pfRGxFc05ZNGRuaGFIdGxlaHplMW02MjFiQldzRmlELTRnV0I4eTRNblVBZzl6cS1ESUlmcy1pNHpXaXR4emtnX3pHSmhtbjNmS1pUUVYyYkRKTWczYWthZFUxazFETVF6Y0RMTmhqeV9iNXRqWjA2YkNKYkdJSFFjb2NPNDg3NWwxLU1fR25nX1J6bURaZklDc0xyN3Y5c19YcVhYcTIzR1VLUGxTZTNnSExfbllSdkNTREpaSDNqYXl6TXI2RGc?oc=5>

## RISKS

### The Open Question In McKesson’s Two New Deals
- Summary: Uncertainty surrounding two new deals involving McKesson.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxPaHZXNjNxNWpfZE5PY1NnVTF4NTVMNm41NE92d0RwcFN4MmlRa2E0eGJvaWlYX0d2R3UxRjhaUFUzX3o1YUs0ZDlnZDg3N0lnbXVXQnhYYUJjN2VJTGV0SGVNb1VBdXFseVdLcUlJNFk5RVpDX0dRNHNfTnJySnVTMV9KcENuZDhzUUFjRWtWNDJGdVNscGtYX2ZtUmJxVW91c1pPZTRTUQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MCK** | **27.81** | **-31.36** | **18.09** | **7.60** | **124,472,672,256.00 USD** | **24.38** |
| COR | 19.48 | 18.13 | 12.79 | 5.50 | 66,728,443,904.00 USD | -5.32 |
| CAH | 36.18 | -21.45 | 15.58 | 5.50 | 64,637,366,272.00 USD | 33.66 |
| CNC | 22.11 | 1.43 | 5.10 | 0.20 | 31,857,625,088.00 USD | 68.59 |

Peers fetched as_of: 2026-11-24; MCK reuses existing data (market data as_of: 2026-11-24); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-04
- Next expected earnings: 2027-02-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-24

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

- https://news.google.com/rss/articles/CBMipwFBVV95cUxQdW1BVTFCeUdGb29fYWRnQnRiQ0Qyd1NramlSQzFBazJmTmhGSXozaUhHcnEzUGRnR0FFYTZMVnkzVnVGZjNKeG8xa1BLY0lRV1BwTmw3YnREeWJiNHhhX2V0Snk5QUlzUng3RzhCX0E5ZEdqeXV1UEwwbGVJYmd0U2NGNVZGRXpIX203N2EzRUMyMzZxSGM3OXJ1cUJaZWYwcGZQc0M4MA?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxPbHhHbkthcWZpaHZCbXlvbkZMMElSZTNlbzQ2VHpnOUVzVjRKUkx3MmNzWnB0bG1vTGZMc3VLeE5ybUNubDUyX2VRcDN1YXg5M3h0dlNhS19Fc2tjRklpcGY1Z2phdmFWdVR3c0tWUWlCNVJxTFdwNVJ3MzhCSWhFTFE0LTRDa1hJOE1TcnZieWxXZ01Jc3ZlU1F3MGd2bmxxcDFwNnZwLUV0MVozNTlWRjBfcU5ESEtqa2ZWYmluY9IBxAFBVV95cUxNWFpiaHQwMUpyb2dBb0lldG9yZHNXdU5OVUZRUVZOVzdvbTJiemxxc1FYdzNpZW1vbHhlZkwtbFdIUFdXUU9mTVg1RG0zbDlBQkJIQ29abnRLQlpINm9JbDJDbFZMNXNYa3V2MlhzbXFpS1VqeEtMSVY2Zk1PbXZiVFhCNVM2MDJ1VUt5b0owU3pNVmpNdVZ4STN6cnVnTUl0cDJPNW4zcWxkNDJOMlA1aXVUbXJVcVJ6Z29DMWRkTm9IaW4z?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOc1h0YnprSHlCSXBvX3ZJYV8xTUhNMDlPRTFVSElBQ01pY01Jb3ozWFhkUll0MDlsNndoa05nWTBjYzBpV1pWSHBzZ2VLYU83N040WmFYZDhRZTU3akFoRVFLQWwxTnpEeExpLU5VTTlFenJxRU84dF9rYnZuS2VYMzA2eUdDMHN0QlV1Uko3b0VkUS1SdS16LVlqLXNIZkVWNHc?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxNME94U1VmRERqTVVKQmJGcEFhZ3BlZE1ONVUxN1RhNmdRMkxvTlZfcHdOQ2NNRlYzZWlkUHR1bnBjc3YxeWg4VE5TR2R0Q25CVFVvamJxRkJzSldoWFFja2tYSHQ2NmwtYlNmaEJYdnZkSWFYYXZMbWhjN3BiTDdkSkdmRzNXOXRxbk5PUENCMmZtRU5EZ3NoLTMzLUp2NG5pZ0ltSHcwNDFoelBFWjFCRXQ2SE80NG1a?oc=5
- https://news.google.com/rss/articles/CBMi3gFBVV95cUxOYlpDbXo3OEVzQm5ySUoyTkhsTjFyTFZ6UjZzWGxjWXJfME1neS1IaXh1M2ViU2s3UzlUZUxzV1FBWTZ2ZFlCeU1EUnlSTXdVSUtqQ2ozTnN5QU5LdmE4VTg1Sk9fYkpUYzl6bndZak54VWplMDdQc25BU0ZqcVhtRU1IOTJIZXVlQzFfM24zbVphcW1kMW5PNVdEc2U3cE5vOG1IWU5GcHFsTUJQZ3lvbWVYLWo3Mndqd2RMcTlEZ1AxQjVvTHF2LTZXWDF1YnVNNEZKUHhkdUpibjlWTlE?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQdHRfb1NHc3hXd29ncm9RR2t2MnM3aWlFUW5XYmF4UVpqS29aVEtmSWJsMjIxbmUzZmFxT2xmS1Q3b21yVHRlQ1ZNWDFzaWdaNFZ5eWZramdiU2tVTDRYd1JRS1RKYVBubzhYWlE0eHVhcnAzSC1abUF4SmpfWlRtNTJkQ3h2ZzNzbXBZVlJjaElON2RtY0dJ?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxQV0gweEJOR1MxRUw2d2RIcV9pN1Rfb1NzR1prc002enNVY2k5Z3lNMlA3R2Z5bE0yRzF3aUVaNXIzVW1vM200OV8tVHdqOHVRRWp3SVV6NXNKUkl3UU5ydGZFc0x6alJrMG9LUHVtZ0lyU1JCaHFuTDVKOVJpSTliYkpuc21hVzlCT24xeDZ0dmhuZTlSWG50cmczQXR0TUNabHpjckhkbUhWdw?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxOV01GZTdJWVdxdDl5OGpKZkZmRE0xWDREM3ZlTWJrQlJSZm40cXRPelZWeWdIMUcxSlhqQ0FKSklfbjRUVThFMVlSdUNnc3FoeW40Rm1iMGNad1lkTUtoUXFqY2VDZjhvMXhKcEJkWFZCOWdvd0ZXOTQyMHVqcFVGaEFB?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOd0FmakpWMUFBR2Zhd0NkMkszOFl2YzJGNWZkcnhRdHVhTXFUQ2xvNUI0QWs1dDhMdVJBelZOQkJfZnZBdjBRQjNQOXBZMHBfZnRod3ZjUUNoazg3T1hWak5lNFl6WEE5ZW5HSTFwbEZzWkN2bXNSNzRKRmVqY2Q1YkM1eGhZOEJEbTNwWmZ5TG0yOHpEcWMwU3JYejFOYVktTGktZXBB?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxQMWM4YWNWVThOUEk1MGlBYmhMYjgxdk10UnUtQjcxNEJmeldDN3ZuZEM2SjJfeVphcFRmQ2ZVRlNiRWI0NW4wQ3h1Z05GOWdqV2pIQ2NEUkxwWWNBcWwtUFNRaDBRdmJWQ29Nd19Lci16RlN1TlVvaENRbTNBTlNucTBZOEpSalBaSWd0ZjNsM0k?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxNYkN6X0RsRXNOWTRkbmhhSHRsZWh6ZTFtNjIxYkJXc0ZpRC00Z1dCOHk0TW5VQWc5enEtRElJZnMtaTR6V2l0eHprZ196R0pobW4zZktaVFFWMmJESk1nM2FrYWRVMWsxRE1RemNETE5oanlfYjV0alowNmJDSmJHSUhRY29jTzQ4NzVsMS1NX0duZ19Sem1EWmZJQ3NMcjd2OXNfWHFYWHEyM0dVS1BsU2UzZ0hMX25ZUnZDU0RKWkgzamF5ek1yNkRn0gHKAUFVX3lxTE1iQ3pfRGxFc05ZNGRuaGFIdGxlaHplMW02MjFiQldzRmlELTRnV0I4eTRNblVBZzl6cS1ESUlmcy1pNHpXaXR4emtnX3pHSmhtbjNmS1pUUVYyYkRKTWczYWthZFUxazFETVF6Y0RMTmhqeV9iNXRqWjA2YkNKYkdJSFFjb2NPNDg3NWwxLU1fR25nX1J6bURaZklDc0xyN3Y5c19YcVhYcTIzR1VLUGxTZTNnSExfbllSdkNTREpaSDNqYXl6TXI2RGc?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPaHZXNjNxNWpfZE5PY1NnVTF4NTVMNm41NE92d0RwcFN4MmlRa2E0eGJvaWlYX0d2R3UxRjhaUFUzX3o1YUs0ZDlnZDg3N0lnbXVXQnhYYUJjN2VJTGV0SGVNb1VBdXFseVdLcUlJNFk5RVpDX0dRNHNfTnJySnVTMV9KcENuZDhzUUFjRWtWNDJGdVNscGtYX2ZtUmJxVW91c1pPZTRTUQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
