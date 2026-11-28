# DIS Intelligence Report

- ticker: **DIS**
- Report as_of: **2026-11-27**
- Market data as_of: **2026-11-27**
- Quant sources: https://finance.yahoo.com/quote/DIS/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/DIS/key-statistics/
- AI analysis snapshot as_of: **2026-11-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-28T06:20:19.758005+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 1, 'ai': 13, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **14** exact headline/source/date matches; prior report **20261127T063646Z-c0c26981/DIS** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 2}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 14 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 17.39%; oldest publication 2026-11-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 127.2400 |
| Return 1D (%) | 1.3057 |
| Return 1W (%) | 7.8488 |
| Return 1M (%) | 15.4314 |
| Return YTD (%) | 12.6966 |
| Return 1Y (%) | 24.8017 |
| Annualized volatility (%) | 26.6431 |
| Beta vs SPY | 0.5292 |
| Max drawdown (%) | -20.2451 |
| Sharpe (rf=0) | 0.9332 |
| Downside deviation (rf=0, %) | 17.5460 |
| Sortino (rf=0) | 1.4171 |
| Historical VaR 95% (1D, %) | 2.3432 |
| Historical ES 95% (1D, %) | 3.3566 |
| Correlation vs SPY | 0.2984 |
| Tracking error vs SPY (%) | 26.3946 |
| P/E (trailing) | 22.60 |
| P/B | 1.98 |
| EV/EBITDA | 11.78 |
| Revenue growth (%) | 15.50 |
| Forward P/E (estimate) | 14.88 |
| Gross margin (%) | 38.02 |
| Operating margin (%) | 16.57 |
| Return on equity (%) | 9.13 |
| Free cash flow yield (%) | 3.43 |
| MA50 | 111.9520 |
| Close vs MA50 (%) | 13.6559 |
| MA200 | 104.0144 |
| Close vs MA200 (%) | 22.3292 |
| RSI (14, Wilder) | 70.9118 |
| MACD (12,26) | 3.4265 |
| MACD signal (9) | 2.9340 |
| MACD histogram | 0.4924 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'DIS': 291, 'SPY': 291}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 127.2400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.3057 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 7.8488 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 15.4314 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 12.6966 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 24.8017 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 26.6431 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 17.5460 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.4171 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.3432 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.3566 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2984 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.3946 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5292 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -20.2451 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9332 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 14.8777 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 38.0230 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 16.5650 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.1270 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 3.4286 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 22.6004 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 70.9118 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.4924 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 13.6559 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 22.3292 -> Clearly above the moving-average trend level.

## TAILWINDS

### DIS Stock Breaks Above $125 For First Time Since 2022: Disney Retail Bulls Are Talking About A ‘Santa Claus Rally’
- Summary: DIS Stock Breaks Above $125 For First Time Since 2022: Disney Retail Bulls Are Talking About A ‘Santa Claus Rally’
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigAJBVV95cUxQejhseVRieXB1N3dMQU1NTmdQR0l4ZTRkd1ZsMEhKSUQ3ZFJtQkFoRmhrMms3WnRRZ3U3RFdkLTNBTXZmM3YyTFgtR2czTi1mdmlaUlVqZkQwcWR2XzdkSlpORkZqRVdFUGd0VThnSk1uVHdSME5ESVJOT25PSnlIeDBvblc5d2FUYzFfVWFLenBraHpvZFQ1WkF3ekxWVDBMOW1WdnFVaTE5Ql9fejdzNVI1YjNfZHE1QlN0MUo0dDRLUnJ3NEJBaEVxOUZONHlVMTlsNVY0VU5RZ1U1am1aNl95ODFrS2JpTlpSSHE2OW1SUDhFLWtDSjZQclVTbGUw?oc=5>

### Disney Stock Hits 52-Week High: What's Happening?
- Summary: Disney shares reach a 52‑week peak, indicating strong investor confidence.
- Date: 2026-11-25 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxOOHcyQU1Vd05lbmZJbkJTSEpJcTdGVDN2WDdhQ2I0anBXUU01eEN2RDBjcXhvcmZQY2l6cml0bnFwQWhiTTRnSTdMR0N2aFBJbWo0bmlGcjJPWS16SHB2Rmk0UkktWDEtcTRzOWw3MU01TEZXZnZkSFo3T0lxNjYxUHdwOWFVZGhiQ3EyMUttMzlHUkZGSnpOZW9jWGRuMlE2ckt4dUtGV1pyYjg?oc=5>

### Disney Just Made a 52-Week High While Netflix Is Down 36.2% This Year. Here’s the Better Buy Now.
- Summary: Disney’s stock reached a 52‑week high, outperforming Netflix, suggesting a bullish trend for investors.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxQUElRSDRiaTVrUVNDRGpOTW9oN3Y4X1ZSWjV4c2IyclotejJvc2RCc09KRjEyYkoyNnZ1Y08zMVBaY3hpVVQyVVBINnk1U1BrQXllSE9RRC1CTTI4QlVZbDYxSFhFZno4LVFqb1V5VFZfUUE0RXBZVFV2dG5xLVNwWUZ4b0N3RW5jVzJjbWtYbHd1RjhCa1l5aHcybGhianlJcldVOUFuYzN6dWt5VFdTc292SVBRMGN3QlJhbDE3bjVPSExhbFpodFIycVRNcU9lRUtN?oc=5>

### Walt Disney (DIS) Plans To Merge Hulu Into Disney+ By December 2026
- Summary: Planned merger of Hulu into Disney+ by Dec 2026.
- Date: 2026-11-23 | Impact: medium | Horizon: long | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOOUt0eEthdFhwMWlYRFQ3R0drQVhsTzU3S1lHZ05IaVY5XzZmRXZSVS1heERXRGhTenJUTzEzZjFqX1BrcF9mVUNuYTByb3RVSjlLSXF3XzlNTU5CTTVQeklja2xFckhUSmIxZlFMbl9qVlh6ZFBNd0Y0Rld5Yk9pWkJTWlFQVUhqaFJicjZBUUhDdEZRMXBHYmtSaw?oc=5>

## HEADWINDS

### Disney Stops Reporting Streaming Profit. Should You Worry?
- Summary: Disney ceases streaming profit reporting.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxNTy1FUDdSVTVGYWN4OHZXTkxUT3NIRm41b2F1LWVIUHNwNFBVd1hJTlpmQUpodjB2ckFPVU5vY196UzJzNHQ5M3VMWWRlLXI5d2F2X2V6YnYzSlBwSS02ejhEd0hDNk1MZ3RWNXg5ajcwTnduNFd6cVpGV3VURVJleUlFdERVZzY5aXNKVnBiYkpfNy1NVE43VXA4RENVUG1mQjIzeC1DN09CeHJ4M1lqSFJsZ096ODg?oc=5>

### What Could Derail Disney Stock?
- Summary: Potential risks that could negatively impact Disney’s stock performance.
- Date: 2026-11-20 | Impact: high | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOMFZaMHd3UjJfY3VxSTR5YWJxc1h3bzJJRENFbTdRUkluM1pTeEVxSTAtTVNSUmNQZ04zZzRITHo5N0JucmpzTDM1UEVEbFdaU1pwSGd0TDdCd05LQlFtNVI3Y0pQSnhCMC1LMXVSajc3NWtxYVZxdm1pRExtem44OXJ2NU1IcHNYWXUtTURvdVZaLVo5?oc=5>

### Court blocks FCC move on ABC licenses in free speech ruling for Disney (DIS:NYSE)
- Summary: Court blocks FCC action affecting Disney’s ABC licenses, limiting regulatory changes.
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxOR09HOHFJR3lVYWxYM2puRVptUzBnNDJKNXltaEdhZHBZLTYwNk5CNDlRU0d5VzZ5d2tYMTJPRjk0SDNnck03U3RWRmFJdlBRa0RTZjFfU2FxQ09sdkU1YUZMb3hIdjdpb1U5Q0d6ZzFJNUl0VVA4ZGdPd3dLcHBIRHFLeklsVFZISkJEREU2MWlQZ2s0cWlJbTEtS0lRekFzdTJYTzVxMW91ZkRk?oc=5>

### Disney (DIS) officer Sonia Coleman proposes selling 3,759 shares valued at about $472,000.
- Summary: Insider proposes selling shares, potential negative signal.
- Date: 2026-11-27 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQeTFPUC1JWUoybHNFNUdyNVdFdDFGaGVpcUNMeGpJWnI1MTZlUmJ0bWdKdW1JWmZVZDFkaGhJU2ZYMDRaeVNqRGhvckZrdHh2SUhvUW1QTmg2ODAtR3FPb3pRR1ptUEZjeFZISGhKNEcwUFRLWV9jR1h5eFk0NEpOVHZhS1NTelJDN2ZnbHpUSTlKYi1E?oc=5>

## CATALYSTS

### Walt Disney (DIS) Lifts Dividend On Strong Earnings, Is The Stock Still Cheap?
- Summary: Disney raises its dividend following robust earnings, signaling shareholder value enhancement.
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPU2FOLXhZdG9kUG9WTGFsZ0dGRGhFdndkT3VZUk1WUV9BcVV4X1lhODNkazl4SXdOMjFHam1VWnlTVzVyNk5vWjhvNl81UlFXWVhWNEM1ZlRFOXVtZUt1clh3UENSTUVZUWc0ZnlXeU1SUGtCTkJHQ2hCV0JvTThMSzNyMGR5SW0zeDNsZEdXSC1ockw1bFlPNnJEbw?oc=5>

### Disney Just Boosted Its Dividend by 33%. That Gives DIS Stock Investors a Real Reason to Stick Around.
- Summary: Disney increased dividend by 33%.
- Date: 2026-11-20 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi2wFBVV95cUxPSlowejN5VDB0OWxkUnJIMmhHclNmWWNaM3M5SE9FTFJHb09JYnRiQjNZSWxha3JrUUw4SFQ3UXhJQkhBbDJMYkg1dEw2Ym1IdG1tZDIwTWZicVhfLW0zQlVzanVGaUppNm54SlphanNyZ3ZEanhPQ0hhc2Y2Q0lQWGFlUVgtZEhPOXB5ODQ4ejI2QlV3TktSZFZZdVFGV1ZnaURiSU1HdklOc0tpYjBVb1Y0aUV2cjhOeE9SU0R2Zi13czNYemVkSFI3RW0zWnliYUR3MjFJYmp5QUk?oc=5>

### Disney Is Up 10% in 2026 and Just Hit a 52-Week High: Take Profits, or Buy More?
- Summary: Shares surged 10% in 2026, reaching a 52‑week high, prompting a debate on taking profits or buying more.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxNZjJTZ3hzSzBKSnRlakdVeDBsRFpoVTFKWDB5V0tHRkFFajNheERBVEpESVpTODBOWm5KeGFCak1jTjhqTENJRHluVW5nQ0RDVG1qRUhKR0o2SHRwWHNiRVJHajctM2U2TVlmWmlldlFnSzhtTnRFamwwdjc3aFZjQ3Z6OUNjajJkWnhEQWo4TkNVTS0tN3ZNSHF2bEhlMFVsQ2JLYVdTX2d6Z3ZDMHZISlBzano2UQ?oc=5>

### Walt Disney (DIS) Could Be 4% Undervalued On Its FCC Court Win
- Summary: Disney may be undervalued by 4% following its FCC court victory, suggesting a potential upside.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxQUnBJazEtcUQxVm10Y3VncXFpUks3SmNyTUJ0a09rRG9pRG1fVVlfMU5NYlJkc29FTjNVV3hxWG5laUlzbmhLV0FIRjI1SG11cWxpd0JqNDJ6NlZZdWlkY2VGTk44YU5uRDducTdWRWhZazhLcUF4UTZLQThfN1ZqY3pjX2xrZ2M3WGlpOHRkMnJpOEp6eWU4bUtVTkM1NXlZU2Q5RU0tSjNJRk1VSjRfaHFQbVVXWUFwX1pjNWpELTbSAcYBQVVfeXFMUHNSYjREMGFHOFhqZHZ4T0s4bkZKazJBWlh5SDc1ZUh1ZXdXc0I3amkwa3FyT2dzVTRubXZOc2lfVVpqRmp3NUNqaVowS1hoUmxXaDRFN0dyWGt0eGNEU3BJYVV4UUpJNHM0TTl4cS0xRFdMTDd4SlRpdFpBdmxTLWd5eE1zRDhmZjN4X3o4b1pMWm9iRWl5S3gzSGc1dE9YOVVwUDVUX0x0Rmt4cE82VW5Rc1pLUThLbjIxWW1mVjdRbDduYkd3?oc=5>

### Disney: Economic Outlook Clashes With Disney Goals (NYSE:DIS)
- Summary: Disney’s economic outlook conflicts with its stated goals, indicating potential challenges ahead.
- Date: 2026-11-23 | Impact: medium | Horizon: medium | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQSnBqVXZUdi1CY0cxV0JwLS1IOTQ3UW5sUjlNUXV3TlpBRzdENkVNdEJsaDVaUGNuWTVPbFh3cWxHNm5BeWMtUjNVSWxkaWQ5ckdQYTZ5eHRjTkc0WF9vTF9jampzMFVsY19OczRWRHFCTzhva1ZnbkxsQlg3LWo0QWN5dUdpRWdvN1NmV1RXaXJ2dmpy?oc=5>

### Disney: Even After Its 26% Rally, I Am Still Calling It A Strong Buy (NYSE:DIS)
- Summary: Analyst maintains strong buy rating after rally.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxQNVFmdkRSTXNKTzltTGNrZ3J5Q0tLWmdBbjVvSXRuM1A4TWswV09qR0M5QXNMdUtPakFfNFdiNnZ1QTMyRUdaY1FvXzRtLUMtTW9BMFBfQzJvT0tha2Z6UTQ1Ymd0WUlGZE93YmJxLUdreHZsTHJKR2xjSXhvWlJHcGdTaHNFVTVhSmEwTmtJVnA5aTUtMS1WNml4aXpnU2tYakU4VlJTdHRGUFBBUmtHZGZnNHM?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **DIS** | **22.60** | **1.98** | **11.78** | **15.50** | **217,329,696,768.00 USD** | **24.80** |
| NFLX | 17.61 | 8.54 | 16.26 | 11.80 | 250,198,441,984.00 USD | -42.59 |
| WBD | N/A | 2.36 | 13.79 | -11.20 | 77,595,885,568.00 USD | N/A |
| PSKY | N/A | 0.93 | 7.95 | 0.90 | 10,992,190,464.00 USD | N/A |

Peers fetched as_of: 2026-11-27; DIS reuses existing data (market data as_of: 2026-11-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-17
- Next expected earnings: 2027-02-01 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-27

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-11-17
- Revenue (latest available single quarter): 25,248,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 2,638,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1744489/000174448926000066/dis-20261003.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMigAJBVV95cUxQejhseVRieXB1N3dMQU1NTmdQR0l4ZTRkd1ZsMEhKSUQ3ZFJtQkFoRmhrMms3WnRRZ3U3RFdkLTNBTXZmM3YyTFgtR2czTi1mdmlaUlVqZkQwcWR2XzdkSlpORkZqRVdFUGd0VThnSk1uVHdSME5ESVJOT25PSnlIeDBvblc5d2FUYzFfVWFLenBraHpvZFQ1WkF3ekxWVDBMOW1WdnFVaTE5Ql9fejdzNVI1YjNfZHE1QlN0MUo0dDRLUnJ3NEJBaEVxOUZONHlVMTlsNVY0VU5RZ1U1am1aNl95ODFrS2JpTlpSSHE2OW1SUDhFLWtDSjZQclVTbGUw?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxOOHcyQU1Vd05lbmZJbkJTSEpJcTdGVDN2WDdhQ2I0anBXUU01eEN2RDBjcXhvcmZQY2l6cml0bnFwQWhiTTRnSTdMR0N2aFBJbWo0bmlGcjJPWS16SHB2Rmk0UkktWDEtcTRzOWw3MU01TEZXZnZkSFo3T0lxNjYxUHdwOWFVZGhiQ3EyMUttMzlHUkZGSnpOZW9jWGRuMlE2ckt4dUtGV1pyYjg?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxQUElRSDRiaTVrUVNDRGpOTW9oN3Y4X1ZSWjV4c2IyclotejJvc2RCc09KRjEyYkoyNnZ1Y08zMVBaY3hpVVQyVVBINnk1U1BrQXllSE9RRC1CTTI4QlVZbDYxSFhFZno4LVFqb1V5VFZfUUE0RXBZVFV2dG5xLVNwWUZ4b0N3RW5jVzJjbWtYbHd1RjhCa1l5aHcybGhianlJcldVOUFuYzN6dWt5VFdTc292SVBRMGN3QlJhbDE3bjVPSExhbFpodFIycVRNcU9lRUtN?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOOUt0eEthdFhwMWlYRFQ3R0drQVhsTzU3S1lHZ05IaVY5XzZmRXZSVS1heERXRGhTenJUTzEzZjFqX1BrcF9mVUNuYTByb3RVSjlLSXF3XzlNTU5CTTVQeklja2xFckhUSmIxZlFMbl9qVlh6ZFBNd0Y0Rld5Yk9pWkJTWlFQVUhqaFJicjZBUUhDdEZRMXBHYmtSaw?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxNTy1FUDdSVTVGYWN4OHZXTkxUT3NIRm41b2F1LWVIUHNwNFBVd1hJTlpmQUpodjB2ckFPVU5vY196UzJzNHQ5M3VMWWRlLXI5d2F2X2V6YnYzSlBwSS02ejhEd0hDNk1MZ3RWNXg5ajcwTnduNFd6cVpGV3VURVJleUlFdERVZzY5aXNKVnBiYkpfNy1NVE43VXA4RENVUG1mQjIzeC1DN09CeHJ4M1lqSFJsZ096ODg?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOMFZaMHd3UjJfY3VxSTR5YWJxc1h3bzJJRENFbTdRUkluM1pTeEVxSTAtTVNSUmNQZ04zZzRITHo5N0JucmpzTDM1UEVEbFdaU1pwSGd0TDdCd05LQlFtNVI3Y0pQSnhCMC1LMXVSajc3NWtxYVZxdm1pRExtem44OXJ2NU1IcHNYWXUtTURvdVZaLVo5?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxOR09HOHFJR3lVYWxYM2puRVptUzBnNDJKNXltaEdhZHBZLTYwNk5CNDlRU0d5VzZ5d2tYMTJPRjk0SDNnck03U3RWRmFJdlBRa0RTZjFfU2FxQ09sdkU1YUZMb3hIdjdpb1U5Q0d6ZzFJNUl0VVA4ZGdPd3dLcHBIRHFLeklsVFZISkJEREU2MWlQZ2s0cWlJbTEtS0lRekFzdTJYTzVxMW91ZkRk?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQeTFPUC1JWUoybHNFNUdyNVdFdDFGaGVpcUNMeGpJWnI1MTZlUmJ0bWdKdW1JWmZVZDFkaGhJU2ZYMDRaeVNqRGhvckZrdHh2SUhvUW1QTmg2ODAtR3FPb3pRR1ptUEZjeFZISGhKNEcwUFRLWV9jR1h5eFk0NEpOVHZhS1NTelJDN2ZnbHpUSTlKYi1E?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPU2FOLXhZdG9kUG9WTGFsZ0dGRGhFdndkT3VZUk1WUV9BcVV4X1lhODNkazl4SXdOMjFHam1VWnlTVzVyNk5vWjhvNl81UlFXWVhWNEM1ZlRFOXVtZUt1clh3UENSTUVZUWc0ZnlXeU1SUGtCTkJHQ2hCV0JvTThMSzNyMGR5SW0zeDNsZEdXSC1ockw1bFlPNnJEbw?oc=5
- https://news.google.com/rss/articles/CBMi2wFBVV95cUxPSlowejN5VDB0OWxkUnJIMmhHclNmWWNaM3M5SE9FTFJHb09JYnRiQjNZSWxha3JrUUw4SFQ3UXhJQkhBbDJMYkg1dEw2Ym1IdG1tZDIwTWZicVhfLW0zQlVzanVGaUppNm54SlphanNyZ3ZEanhPQ0hhc2Y2Q0lQWGFlUVgtZEhPOXB5ODQ4ejI2QlV3TktSZFZZdVFGV1ZnaURiSU1HdklOc0tpYjBVb1Y0aUV2cjhOeE9SU0R2Zi13czNYemVkSFI3RW0zWnliYUR3MjFJYmp5QUk?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxNZjJTZ3hzSzBKSnRlakdVeDBsRFpoVTFKWDB5V0tHRkFFajNheERBVEpESVpTODBOWm5KeGFCak1jTjhqTENJRHluVW5nQ0RDVG1qRUhKR0o2SHRwWHNiRVJHajctM2U2TVlmWmlldlFnSzhtTnRFamwwdjc3aFZjQ3Z6OUNjajJkWnhEQWo4TkNVTS0tN3ZNSHF2bEhlMFVsQ2JLYVdTX2d6Z3ZDMHZISlBzano2UQ?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxQUnBJazEtcUQxVm10Y3VncXFpUks3SmNyTUJ0a09rRG9pRG1fVVlfMU5NYlJkc29FTjNVV3hxWG5laUlzbmhLV0FIRjI1SG11cWxpd0JqNDJ6NlZZdWlkY2VGTk44YU5uRDducTdWRWhZazhLcUF4UTZLQThfN1ZqY3pjX2xrZ2M3WGlpOHRkMnJpOEp6eWU4bUtVTkM1NXlZU2Q5RU0tSjNJRk1VSjRfaHFQbVVXWUFwX1pjNWpELTbSAcYBQVVfeXFMUHNSYjREMGFHOFhqZHZ4T0s4bkZKazJBWlh5SDc1ZUh1ZXdXc0I3amkwa3FyT2dzVTRubXZOc2lfVVpqRmp3NUNqaVowS1hoUmxXaDRFN0dyWGt0eGNEU3BJYVV4UUpJNHM0TTl4cS0xRFdMTDd4SlRpdFpBdmxTLWd5eE1zRDhmZjN4X3o4b1pMWm9iRWl5S3gzSGc1dE9YOVVwUDVUX0x0Rmt4cE82VW5Rc1pLUThLbjIxWW1mVjdRbDduYkd3?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQSnBqVXZUdi1CY0cxV0JwLS1IOTQ3UW5sUjlNUXV3TlpBRzdENkVNdEJsaDVaUGNuWTVPbFh3cWxHNm5BeWMtUjNVSWxkaWQ5ckdQYTZ5eHRjTkc0WF9vTF9jampzMFVsY19OczRWRHFCTzhva1ZnbkxsQlg3LWo0QWN5dUdpRWdvN1NmV1RXaXJ2dmpy?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxQNVFmdkRSTXNKTzltTGNrZ3J5Q0tLWmdBbjVvSXRuM1A4TWswV09qR0M5QXNMdUtPakFfNFdiNnZ1QTMyRUdaY1FvXzRtLUMtTW9BMFBfQzJvT0tha2Z6UTQ1Ymd0WUlGZE93YmJxLUdreHZsTHJKR2xjSXhvWlJHcGdTaHNFVTVhSmEwTmtJVnA5aTUtMS1WNml4aXpnU2tYakU4VlJTdHRGUFBBUmtHZGZnNHM?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
