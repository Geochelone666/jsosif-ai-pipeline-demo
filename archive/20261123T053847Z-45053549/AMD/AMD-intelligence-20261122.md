# AMD Intelligence Report

- ticker: **AMD**
- Report as_of: **2026-11-22**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/AMD/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMD/key-statistics/
- AI analysis snapshot as_of: **2026-11-22**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-23T05:52:38.603818+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 5, 'ai': 8, 'unknown': 0, 'irrelevant': 10})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261122T045655Z-f5ef568d/AMD** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 15 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 34.78%; oldest publication 2026-11-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 424.3900 |
| Return 1D (%) | -13.2464 |
| Return 1W (%) | -20.5351 |
| Return 1M (%) | -20.6362 |
| Return YTD (%) | 98.1649 |
| Return 1Y (%) | 105.9946 |
| Annualized volatility (%) | 74.7962 |
| Beta vs SPY | 3.4249 |
| Max drawdown (%) | -37.7290 |
| Sharpe (rf=0) | 1.3448 |
| Downside deviation (rf=0, %) | 49.5199 |
| Sortino (rf=0) | 2.0313 |
| Historical VaR 95% (1D, %) | 6.9676 |
| Historical ES 95% (1D, %) | 10.1271 |
| Correlation vs SPY | 0.6546 |
| Tracking error vs SPY (%) | 66.3253 |
| P/E (trailing) | 90.68 |
| P/B | 10.18 |
| EV/EBITDA | 61.88 |
| Revenue growth (%) | 44.70 |
| Forward P/E (estimate) | 24.06 |
| Gross margin (%) | 56.00 |
| Operating margin (%) | 17.82 |
| Return on equity (%) | 11.96 |
| Free cash flow yield (%) | 1.05 |
| MA50 | 553.0976 |
| Close vs MA50 (%) | -23.2703 |
| MA200 | 429.7861 |
| Close vs MA200 (%) | -1.2555 |
| RSI (14, Wilder) | 38.4158 |
| MACD (12,26) | -16.2917 |
| MACD signal (9) | -12.8229 |
| MACD histogram | -3.4688 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMD': 287, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 424.3900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -13.2464 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -20.5351 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -20.6362 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 98.1649 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 105.9946 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 74.7962 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 49.5199 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.0313 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 6.9676 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 10.1271 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6546 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 66.3253 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.4249 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -37.7290 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.3448 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 24.0608 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 56.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 17.8210 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 11.9600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.0474 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 90.6816 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 38.4158 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.4688 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -23.2703 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -1.2555 -> Slightly below the moving-average trend level.

## TAILWINDS

### AMD’s Data Center Sales Jumped 97%. Is the Stock a Buy?
- Summary: AMD’s Data Center Sales Jumped 97%. Is the Stock a Buy?
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOeGVYdV9Ga0hQQzdiZ0NxZ1l4Nk1aZ2stV0N3M0RvLVY0U2FKM1M4b1BfVnMzSWk0Wm5LRkJIN3ItSkJoVV9Ia2UyM2t6QUloOFctcXJ4ajViTWpNUUl4V2V4YTZzUGdfLUkyN2NIQ1paeFVlcThHcEFveEduaDlueFdjSDd1RGcyYkpCVWMxM2N1UXZtWVlBaw?oc=5>

## HEADWINDS

### AMD Stock Drops After Short Report Says It Isn’t an Nvidia Replacement
- Summary: AMD Stock Drops After Short Report Says It Isn’t an Nvidia Replacement
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTE5vOE1LWHU3SlUwbnlZRHlYTUpYZEJzTUJYRlMwdjVaRXdiTXg3NHJKSEVNcTNOVTVOLXFac0xDUUU2dy1OM0tFcERGUG1BSV9hX0Z0Wk41bTdEbW1fNmFMNjh2cEVyeE1ldHFvQ2hoMHUtVTExT0ZPb2Y2V09Kdw?oc=5>

### AMD Just Plunged Almost 8%, Lost $67 Billion and Kept Falling After Hours. A Short Seller Says It Shares Nvidia's China Risk
- Summary: AMD Just Plunged Almost 8%, Lost $67 Billion and Kept Falling After Hours. A Short Seller Says It Shares Nvidia's China Risk
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi9gFBVV95cUxOU3NlNDNwUFBXX0xaNk5jdlIyaTRtM2RySWJfWmljWm9fTHJZeXlxWmQwN0xMbVQ4WFJqYzhKaXRDQ3lINmJ4TmVuZm9xc3R3dFloTkZLU3l0RE1EQ2M0ZE1jRndwdG90TGxBN3ZPbE9KajBzX2YtRnFVOGMyd1hET2R5anVlRllBblNCQ0p4NnFOT3NzSnZTMGpzb3plOEQ4QmNjQndRQUZJTjN2b1NWTTBWUGhORm0tOGJBYnozQnZReGpRSlZnOVJiWVg0YWlKcDFFbXFIbnFXaWxGR3FVX0VKMDFhb2tKeDBpSUowRmlMbDhnZFE?oc=5>

### AMD Stock Gets Crushed by Anthropic’s Drop and a Short Report. It’s No Time to Panic.
- Summary: AMD Stock Gets Crushed by Anthropic’s Drop and a Short Report. It’s No Time to Panic.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMif0FVX3lxTE1BRXFaZEE0NmhQSWZGQ0FWbHQ2WFd2MTlSUmtIcEUtTXR4dWFGSTY2ZVAxMjI2RzdCcmpSUmxrdUM2NEJfY2ZsZFc5Sko5aEJyaXdob0xZZ3NhWVVSSXU2U0p4RXd4Ri1SNzJxWXpVOG5RU05MNTVCX096Zm5rTkU?oc=5>

### Why Is AMD Stock Falling on Friday?
- Summary: Investors concerned about recent performance and market conditions, leading to a decline in AMD shares.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPakd6RUtYYTBuV2dfQVE4SWpBendrV1B4UmdxOUt4R2djNzVkbWo5VV9qTmZ5YjRHaUJwSXhHb0dZMG5RMTJGQVNhcWZyT1prN3JFdFBWN1JWQ0twS3RDc3ZDVjVWbDltUVZWOURuTHZ6V1MxRkhGN3NCZ1V2N1NRX0FPUnRPamJOVU1EYnVRWkRXR2N2TWZUdnJ4WQ?oc=5>

### AMD shares slide after short-seller warns China ties could invite US scrutiny
- Summary: Short-seller warns China ties may attract US scrutiny, causing AMD shares to fall.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPUHBtWGJlV3dPYm9YWFZNRGxhYlVDN1EwUktRdlNQRUZLYnNiU0FCdDFyVUFnVWN5WHV0TlRyZjBwT2tPbGRIc3U0blVjVVFjcHdrSDZFcHZ0VnN4OHRhR0t0ZDNTUEZQdjRmaU1mNkc3ZlV6alhLZnl2SmdmYk1fUm5Zc1NPencwWlRkYWpRZlNEd0FL?oc=5>

## CATALYSTS

### Advanced Micro Devices, Inc. $AMD Stock Sold by Cvfg LLC
- Summary: Advanced Micro Devices, Inc. $AMD Stock Sold by Cvfg LLC
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxQTThjYUJqeU1jTE9RWGVhUUw3TXJmakYycVl0Qzljd1lDaml6dFJKN1c0UGswU0lueVByd1JWWWRGREk2NHR4Rmh6MWFqLXh6Sk1VOG43WlFLSG5VRExyYXJ6eVRtNjBLM25Oek1VREpiVXRSV19NTlprNjZwZ1FPYmNSV0VQQVlXNEpacUlVdFRjT2dZdUlKLUhnUFc1dGNZVTh1c3NTX3Vzd0t3LUg2ZlJjNnE?oc=5>

### Why Is Advanced Micro Devices Stock Rising Today?
- Summary: Explores reasons behind AMD's recent price increase.
- Date: 2026-11-18 | Impact: low | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPUkNPRlQ0VWdjd0dOeVdRWVVDZlUwOTg0YkFDRE9UXzJHOWFuVEVFMmIwU2xOSl9Ibi1vMTFPX0liLU80SzdaeVdWLTgtamhuSS1nMlV6QjZBMVN2N1ZjN2xqYmR3NHlWYm5kY1l6a0lQUGo1UVdycjNhbzV5cmZjYlRGNGxvTVpDRXpRMGpRWkxkaVA1bm9KcTBBaTg4QQ?oc=5>

### AMD Shares Slump After Shortseller Raises China Concerns
- Summary: Shortseller’s China concerns triggered a sharp decline in AMD shares.
- Date: 2026-11-19 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxPbkp6di1ZYkMzQlhjTmkxbHFwNzIzLWMyc3NKXzBqSV9hZ05wODRRYUhjYl9pSmIyNENPaHpXWmlScUpaYXhfT3AyQ1hKYVhWZnhHRVp1a0g2dkVGWmpYa2lXdmdjaE1TUTQwbFlyNjJVNjVkRmlIbWt3WHhWYjNJWXNGSG9RcFkwYUFRZzdYMVNpQXVnZllfU0ZlZEc0QnFsQ1RnWk9tUmc5d2luUVVSaWRKMA?oc=5>

### Why AMD Stock Was Plunging on Thursday
- Summary: AMD shares fell sharply on Thursday, prompting concerns about valuation.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxOX3BLVnZVVDhkQ1I2LTdZRjZJdHBWU2dKVTlOS2U5bmNaTms4SUY1WndRRmF0TDcyN0VuanVjcFhyQnRyWVlOMGQzS21rSnJCUnRoalZqc3M5N3lwSGQ5S2hjN1BMV3BYTlhNcDBvZlZ1X1dfT2JqMmpXN05fYzJJWm5wTERHME1s?oc=5>

## RISKS

### Advanced Micro Devices (AMD) Faces Firmware Allegations And Class Action Scrutiny
- Summary: AMD faces firmware allegations and class‑action scrutiny, potentially impacting operations and reputation.
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNX0RaMHU5SVFZX1JpOHYzRVBPOGxQYTF6UFlwbUU3aG9YWWNKdENRZ3VSVXdUaW14TElpcldNTzY5SXhQdm5OTnNQdG40TFpXLTFYeFo0dzV5Qy0tLXpqYmJTc2xXMTdUMlVXLWpnbUdSZjh6WUFiMXFFVllpWWdtcHhWR2RxMENBVnNfOXhpLTVoTTlxMGJESUxOWjFGUQ?oc=5>

### AMD dives on short seller report of alleged China exposure
- Summary: Short seller claims AMD has China exposure, causing stock drop.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNamxpaV9pd09BZHBwY2dkTF9NMUttWDFlQS16Q2MwOFl3d3VxX1BrR0J4aEtlQXM2TG5XUlN0eXBfMExna25BSzNOdTUxNG1DdG5ZQ2NNaWtqTjJpTnQ3S25xeXpBSzk5cWp4MUExWmk3RE1GWExWalJINFNOX3FjYWphSHFsOVR1SHppYkxvU0Uyek5zU2hCcUMzZ9IBoAFBVV95cUxNelFseGlBTTJCNTlhVlhxSzVvTjd4Y29iNzkxUE9USXk5YnQ3bEVNWl9yRmpnOHVhYzhyLUp3WXQtQjRoSmVDMUVqcDR5bFBMQmxuUzJ1VnRVaTloYTlMQnhnZTZ6QU9ybDdGSzJpWjhOTjRYT3ZyVk5LSmd6a3dKbTMyU3hNckEyeU5YVHhiNmV1N0VTaDh0emN1bDJPYjZW?oc=5>

### AMD Gained From Nvidia’s China Scandal. Now a Short Seller Says AMD Has a China Problem Too.
- Summary: Short seller alleges AMD faces China issues after Nvidia scandal.
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNM2UyYnM1anhCMjQ0bTNQYXVwLWRhMHVoOFRWZU5kUXRvbksxQUM2UW5vYTBkX0U4RXZZVUlySTZ6UEV3SEp0OTM4UmVudnk0dUFtZm1aTTR2b001MnJmdnJZVFBzaTFmOU1hcTljTDktZm5OampyVklMUmJkYzliWVJHSXhoM3MxYmFtN3l0RzU4X1kydWNCQkhhc2g?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMD** | **90.68** | **10.18** | **61.88** | **44.70** | **702,393,286,656.00 USD** | **105.99** |
| NVDA | 13.48 | 11.35 | 12.19 | 103.20 | 3,031,172,907,008.00 USD | -30.34 |
| INTC | N/A | 2.37 | 14.91 | 20.90 | 272,553,181,184.00 USD | 52.53 |
| AVGO | 38.88 | 14.58 | 28.48 | 85.50 | 1,453,140,738,048.00 USD | -11.58 |

Peers fetched as_of: 2026-11-22; AMD reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-03
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-22

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 1,584,000,000.00 USD; period 2017-07-02/2017-09-30; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 2,428,000,000.00 USD; period 2026-06-28/2026-09-26; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimAFBVV95cUxOeGVYdV9Ga0hQQzdiZ0NxZ1l4Nk1aZ2stV0N3M0RvLVY0U2FKM1M4b1BfVnMzSWk0Wm5LRkJIN3ItSkJoVV9Ia2UyM2t6QUloOFctcXJ4ajViTWpNUUl4V2V4YTZzUGdfLUkyN2NIQ1paeFVlcThHcEFveEduaDlueFdjSDd1RGcyYkpCVWMxM2N1UXZtWVlBaw?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTE5vOE1LWHU3SlUwbnlZRHlYTUpYZEJzTUJYRlMwdjVaRXdiTXg3NHJKSEVNcTNOVTVOLXFac0xDUUU2dy1OM0tFcERGUG1BSV9hX0Z0Wk41bTdEbW1fNmFMNjh2cEVyeE1ldHFvQ2hoMHUtVTExT0ZPb2Y2V09Kdw?oc=5
- https://news.google.com/rss/articles/CBMi9gFBVV95cUxOU3NlNDNwUFBXX0xaNk5jdlIyaTRtM2RySWJfWmljWm9fTHJZeXlxWmQwN0xMbVQ4WFJqYzhKaXRDQ3lINmJ4TmVuZm9xc3R3dFloTkZLU3l0RE1EQ2M0ZE1jRndwdG90TGxBN3ZPbE9KajBzX2YtRnFVOGMyd1hET2R5anVlRllBblNCQ0p4NnFOT3NzSnZTMGpzb3plOEQ4QmNjQndRQUZJTjN2b1NWTTBWUGhORm0tOGJBYnozQnZReGpRSlZnOVJiWVg0YWlKcDFFbXFIbnFXaWxGR3FVX0VKMDFhb2tKeDBpSUowRmlMbDhnZFE?oc=5
- https://news.google.com/rss/articles/CBMif0FVX3lxTE1BRXFaZEE0NmhQSWZGQ0FWbHQ2WFd2MTlSUmtIcEUtTXR4dWFGSTY2ZVAxMjI2RzdCcmpSUmxrdUM2NEJfY2ZsZFc5Sko5aEJyaXdob0xZZ3NhWVVSSXU2U0p4RXd4Ri1SNzJxWXpVOG5RU05MNTVCX096Zm5rTkU?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPakd6RUtYYTBuV2dfQVE4SWpBendrV1B4UmdxOUt4R2djNzVkbWo5VV9qTmZ5YjRHaUJwSXhHb0dZMG5RMTJGQVNhcWZyT1prN3JFdFBWN1JWQ0twS3RDc3ZDVjVWbDltUVZWOURuTHZ6V1MxRkhGN3NCZ1V2N1NRX0FPUnRPamJOVU1EYnVRWkRXR2N2TWZUdnJ4WQ?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPUHBtWGJlV3dPYm9YWFZNRGxhYlVDN1EwUktRdlNQRUZLYnNiU0FCdDFyVUFnVWN5WHV0TlRyZjBwT2tPbGRIc3U0blVjVVFjcHdrSDZFcHZ0VnN4OHRhR0t0ZDNTUEZQdjRmaU1mNkc3ZlV6alhLZnl2SmdmYk1fUm5Zc1NPencwWlRkYWpRZlNEd0FL?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxQTThjYUJqeU1jTE9RWGVhUUw3TXJmakYycVl0Qzljd1lDaml6dFJKN1c0UGswU0lueVByd1JWWWRGREk2NHR4Rmh6MWFqLXh6Sk1VOG43WlFLSG5VRExyYXJ6eVRtNjBLM25Oek1VREpiVXRSV19NTlprNjZwZ1FPYmNSV0VQQVlXNEpacUlVdFRjT2dZdUlKLUhnUFc1dGNZVTh1c3NTX3Vzd0t3LUg2ZlJjNnE?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPUkNPRlQ0VWdjd0dOeVdRWVVDZlUwOTg0YkFDRE9UXzJHOWFuVEVFMmIwU2xOSl9Ibi1vMTFPX0liLU80SzdaeVdWLTgtamhuSS1nMlV6QjZBMVN2N1ZjN2xqYmR3NHlWYm5kY1l6a0lQUGo1UVdycjNhbzV5cmZjYlRGNGxvTVpDRXpRMGpRWkxkaVA1bm9KcTBBaTg4QQ?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxPbkp6di1ZYkMzQlhjTmkxbHFwNzIzLWMyc3NKXzBqSV9hZ05wODRRYUhjYl9pSmIyNENPaHpXWmlScUpaYXhfT3AyQ1hKYVhWZnhHRVp1a0g2dkVGWmpYa2lXdmdjaE1TUTQwbFlyNjJVNjVkRmlIbWt3WHhWYjNJWXNGSG9RcFkwYUFRZzdYMVNpQXVnZllfU0ZlZEc0QnFsQ1RnWk9tUmc5d2luUVVSaWRKMA?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxOX3BLVnZVVDhkQ1I2LTdZRjZJdHBWU2dKVTlOS2U5bmNaTms4SUY1WndRRmF0TDcyN0VuanVjcFhyQnRyWVlOMGQzS21rSnJCUnRoalZqc3M5N3lwSGQ5S2hjN1BMV3BYTlhNcDBvZlZ1X1dfT2JqMmpXN05fYzJJWm5wTERHME1s?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOX3QtQTdQeGVTWk5haDNFU010WGQ5aGp6ODFMY2g5NHhRalcyUGF1anNoNUo3c0hxZWxJUTRrOFdGWHhNb0lHU2RHbmdUMFB2emVGM21wOTUxUWtfdGdiTUhYZDcyN0hKRXpBWDZMMVdhNTZRSU9tSTR3eG5JUmFheVZCSUhYUHlicFdKMEwyekg1bXNvUkZsQThFM3Q?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxNX0RaMHU5SVFZX1JpOHYzRVBPOGxQYTF6UFlwbUU3aG9YWWNKdENRZ3VSVXdUaW14TElpcldNTzY5SXhQdm5OTnNQdG40TFpXLTFYeFo0dzV5Qy0tLXpqYmJTc2xXMTdUMlVXLWpnbUdSZjh6WUFiMXFFVllpWWdtcHhWR2RxMENBVnNfOXhpLTVoTTlxMGJESUxOWjFGUQ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNamxpaV9pd09BZHBwY2dkTF9NMUttWDFlQS16Q2MwOFl3d3VxX1BrR0J4aEtlQXM2TG5XUlN0eXBfMExna25BSzNOdTUxNG1DdG5ZQ2NNaWtqTjJpTnQ3S25xeXpBSzk5cWp4MUExWmk3RE1GWExWalJINFNOX3FjYWphSHFsOVR1SHppYkxvU0Uyek5zU2hCcUMzZ9IBoAFBVV95cUxNelFseGlBTTJCNTlhVlhxSzVvTjd4Y29iNzkxUE9USXk5YnQ3bEVNWl9yRmpnOHVhYzhyLUp3WXQtQjRoSmVDMUVqcDR5bFBMQmxuUzJ1VnRVaTloYTlMQnhnZTZ6QU9ybDdGSzJpWjhOTjRYT3ZyVk5LSmd6a3dKbTMyU3hNckEyeU5YVHhiNmV1N0VTaDh0emN1bDJPYjZW?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNM2UyYnM1anhCMjQ0bTNQYXVwLWRhMHVoOFRWZU5kUXRvbksxQUM2UW5vYTBkX0U4RXZZVUlySTZ6UEV3SEp0OTM4UmVudnk0dUFtZm1aTTR2b001MnJmdnJZVFBzaTFmOU1hcTljTDktZm5OampyVklMUmJkYzliWVJHSXhoM3MxYmFtN3l0RzU4X1kydWNCQkhhc2g?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
