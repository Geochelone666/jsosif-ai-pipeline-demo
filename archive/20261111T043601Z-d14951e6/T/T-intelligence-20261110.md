# T Intelligence Report

- ticker: **T**
- Report as_of: **2026-11-10**
- Market data as_of: **2026-11-10**
- Quant sources: https://finance.yahoo.com/quote/T/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/T/key-statistics/
- AI analysis snapshot as_of: **2026-11-10**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-11T04:48:25.466922+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 1, 'ai': 14, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261110T055129Z-abd33250/T** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 13 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 21.74%; oldest publication 2026-11-05

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 21.9400 |
| Return 1D (%) | 0.6422 |
| Return 1W (%) | 2.5713 |
| Return 1M (%) | -1.0821 |
| Return YTD (%) | -7.4605 |
| Return 1Y (%) | -7.4232 |
| Annualized volatility (%) | 28.7085 |
| Beta vs SPY | -0.3576 |
| Max drawdown (%) | -28.8854 |
| Sharpe (rf=0) | -0.1248 |
| Downside deviation (rf=0, %) | 21.9799 |
| Sortino (rf=0) | -0.1630 |
| Historical VaR 95% (1D, %) | 2.8546 |
| Historical ES 95% (1D, %) | 4.6484 |
| Correlation vs SPY | -0.1703 |
| Tracking error vs SPY (%) | 33.8339 |
| P/E (trailing) | 11.67 |
| P/B | 1.39 |
| EV/EBITDA | 7.31 |
| Revenue growth (%) | 5.30 |
| Forward P/E (estimate) | 8.45 |
| Gross margin (%) | 59.74 |
| Operating margin (%) | 24.65 |
| Return on equity (%) | 11.61 |
| Free cash flow yield (%) | 8.09 |
| MA50 | 23.6375 |
| Close vs MA50 (%) | -7.1813 |
| MA200 | 24.4089 |
| Close vs MA200 (%) | -10.1146 |
| RSI (14, Wilder) | 45.4900 |
| MACD (12,26) | -0.5298 |
| MACD signal (9) | -0.6743 |
| MACD histogram | 0.1446 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'T': 279, 'SPY': 279}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 21.9400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.6422 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.5713 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -1.0821 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -7.4605 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -7.4232 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 28.7085 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.9799 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.1630 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8546 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.6484 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1703 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 33.8339 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.3576 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.8854 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.1248 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 8.4521 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 59.7420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 24.6520 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 11.6130 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 8.0933 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 11.6702 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 45.4900 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.1446 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -7.1813 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -10.1146 -> Clearly below the moving-average trend level.

## TAILWINDS

### Is AT&T Stock Stronger Than It Looks?
- Summary: Analysts question AT&T's stock strength, suggesting potential undervaluation.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOV205OXl5UnNZZlVDUUZVNmFvdEVoUnFPYW10RTZROUtpOUpvb211dkVUQ2pMMlkzU0RSSkgtUklLUnc3aXI1Y1VtaTNOX1pVRGtURTBKQ0dvRlVqemhDMk0yYWNqVU5ZWHFxalRrUU9EX29tWlZZVHBFV24zdm5adnBldzNPYXppdWVjTnJqM2ZQREItNWM5OQ?oc=5>

### AT&T (T) Stock Could Be 35% Undervalued On Customer Care Reshoring
- Summary: AT&T may be undervalued due to customer care reshoring, suggesting potential upside.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxQQzhTeVNGUjkyM281M1NQTHlScngzUDV2cWNyeWVzT3BQdXRTQ09VX2NYa1VhQW9GVDQ3T09kWGJiZVl0ZnhrMkNFa3E4M2h4SU5NWW5jMmJ5blptQkFxU05NTUtCenZEaXJCRlMtWGczZTAzRklsOTBoVUNHSXB6MUx2RGFTN1psVS1iVG41czg3NGg0TGpxU1NVb3NfVmJPSXp4N2FaMFhKeW5OYk9HWHQySzZ6UDDSAbwBQVVfeXFMTnA5RjlVYmhQQnpVdmlQRzlHZmktblFqa2tyTEM3TkYzLUdYdVVfMlNyNTZUZlNzZjd3T0NkcUZ6ZUJicUlYZXVUYW5kWWdKbkxsTEptbktWRm83bExWaG5zSWQ5V1ZYYmtQcDlHVElveHJoQTVyUjNqb3p2SkwwSnE2R3A4aHVOcXlVR3ZqVTRqbUdDYjVHWmxvNXV6ak1JQkNHV1VEZmFCOXlfZWZLMVJVVFFTTUlvb201Wmw?oc=5>

## HEADWINDS

### 'Big Short' Investor Steve Eisman Says AT&T, Verizon and T-Mobile Are 'Uninvestable' as Elon Musk Targets US Wireless Market
- Summary: Investor Steve Eisman deems AT&T uninvestable amid Musk's market entry, signaling negative outlook.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOdE9zdjg3TERlenVnUzQ2MkpLTTRtSUU0LTBadHZvQmJyN3hTZWdOQVhuc2tVNnhzRzItUzYxS19NUkJnZFhIYjVGSHpwMDJ1dmNDRDhTZC1SY2lSWTNDdE1SVDBtbmJoVWx3VFdqSDVLNDI1NmEybmI5ZU03a01aMC1fbDZHanNqY0c3Yl9nSUYtblVDQUFYc0xPQUM?oc=5>

### AT&T, T-Mobile Are Reportedly Ready To Boot Boost Mobile If SpaceX Buys It
- Summary: AT&T and T-Mobile may remove Boost Mobile if SpaceX acquires it, indicating potential market disruption.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxNOTBicHN0a1hkd3pjMGFKUjBpWVNMMTJmc2FGdjZRODBwd1VqcjZTTzVuSXFsd3duOEFhM2htVUlfX2lrbWcyUE9DN2xnMFlzVWlPNlhTbWNNOXlkQkw5eUh0d3U5UHlkM3ZXRVVRbGJCcUtwU3MxcThiWHc2V0FtU0t5NmZVQlhEYzJnWnNfV250aV9zUVJXNFIzQ3FiVEp3YXpPMnJERnhGYVdoSGJHWjQzMWFyVVNhTEFyUVNHSmZ3VUMwaWlHRnlEV09MSGVabVhhZmZPUnBOUQ?oc=5>

### Why AT&T Stock Slumped in October
- Summary: AT&T stock fell sharply in October, indicating negative market sentiment.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxNcm8tYWtGY1RKVEpGcGc3THl3dXNvOTRQN0xoTXNBdnJwUmswMVg0d180VjlELTRFeFd2ejhvR1M5cE5QeUF3WDAwLTJpbFZQaFRuRG1NdkVON0drcGpFbjNvVU9uTngxU05FcmdWU2cwbDE0dS01MXRZSUdBZk9rSzJlRXdIRVE?oc=5>

### AT&T Stock Falls 11.8% in a Year: Should You Buy the Dip?
- Summary: AT&T shares dropped 11.8% over the year, raising concerns about valuation.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNeVJqakhwY213N3laR2tsVk5Zam5UbFBhUWVqNEVILTRjdVlEUFJrQ21qV2RwUHNBVmZwQmNZT25JbHo2eFoxUnBGd01Ob1JpWEQzZzBsejJzcjE2X2F3MmJoM2Rpdm5mZ0l1azhKQnZpVnJaN09SdHJVWHUwbVRIaFMwRjhFNFlLY3hj?oc=5>

## CATALYSTS

### AT&T Inc. $T Stock Bought by Vestor Capital LLC
- Summary: AT&T Inc. $T Stock Bought by Vestor Capital LLC
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQVGdGNGU4RU5IRWF6VDMtS0ZQeklodGF1VHdUeHV4eC1XVkdZY3NoRmZROFBZVlZrelkydFNYZHNYRlJzRUprT2VGaVFVTXFPWFN0OURNZUd4cnlaSmx6MXI4Tk55REtaeXRrNVF5aWVhbDZKX3lHeDRraVdPOVpvakNCRGtJblROUmw0ZmdidXF6MkFpbV9qSzJXQk1ZaW1lNktPNmJTNmE?oc=5>

### Is AT&T (T) Undervalued As Its Satellite Handoff Opens A New Coverage Question?
- Summary: AT&T’s satellite handoff raises coverage concerns, potentially affecting valuation.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQMENnU1dvSXNRUjl6S1hnVUZJT0oxRUphNUxqYTBFcHRjQmE0R1ROYVRfdDh6di1jT0Y0bWpYUk1LbU9uczBEMEhkNERQRW1TMUFLQUppSnNSSXBVSjUxNldYUGhSeEowcGtJSXA1clpvODV3R1BrcWdQMVIzSG9yREthclI4c3JwVUZxS2o1V043Xzg4cWluQXhGUnRERm8?oc=5>

### TELUS Faces Q3 Challenges Amid Strategic Shift; AT&T (T) Dividen
- Summary: AT&T announced a dividend amid TELUS’s Q3 challenges.
- Date: 2026-11-07 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxNSTNSUU9EenFtcnVyRHdYNm5mMXU3MDUwcEJaT3FnaWhSRElpSjVwV1NsQUphRmN4SV9GLTk4cXJFNnFtc1c2dGF0cG91aXFCdXVSc044UWhJdDBPN2VIak5NWXptZHRraUJvRGVvdVVtUF90S2NPejRnWExXNHlLVEp4dF9wMXh5WWdVV2RRVXNDZlZ3cWREOGNyRnJhUTFoeTlhQ2NCSmduNk0zWlFFSlJnZlVjbDhXbnZZZXJhcjlMdw?oc=5>

### AT&T (T) Stock May Be 34% Below Fair Value After Care Reshoring Plan
- Summary: AT&T's care reshoring plan may boost valuation, indicating potential upside.
- Date: 2026-11-10 | Impact: high | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMic0FVX3lxTE5fSVJiZi0zX1JoRHd2YTJFNENVSVBFQ1pZOTIyT1h1ZFA3TjdNWmt3LTM3am1wSjFNNjBhZTZRamlZckdaQ1hRSUNwNXp3ZnNERkZhc3cyVHJrcDBaY1otN05pRm54VEJYQ2dCMndCWmhXTU0?oc=5>

### How Investors Are Reacting To AT&T (T) Satellite Phone Handoff
- Summary: Investors react to AT&T's satellite phone handoff, indicating market sentiment on the transition.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxPMndVTWxGVVhEX19hREV1aDRrb2RHS3ZxMzFIa2ZNeXBOcjkxbUVOZm9qRUlKaDZHeXMtSEdFZ3B2QTlGXzVtdXRhaGNTSndNOUxDaTZNdGxXWDI3cXRNVmhCcEl2WS1WbTZOckgzYkhETzNCSmxUTnhhYldrWTJHRkh0LVdtdXVRZzJrcWJtaTRlVll1cEU0RWtNNEpGTGgxYjVtUEZDeFFHZ1F4T1FwaEF1YXhDUdIBuwFBVV95cUxNbGVjdUJJcXVDU01lN1NpOUVST1RjZVI3OHRrWDh0UDZvWFYwa3hoSUVvMlBlWWdSUEcyRkc3dnNFU1I0S2h3eGR0R0hadXBVTnJONm5SeEdqTFZGM0JoOVVlSV82eGYwU2xzMzBIaHExNmVhZk9hM3Q4RkplM2cxbExNS3YxbXlJVFREaVhLTVU4N3ViTTloQmxYX1hUN3BBMC1ISURNNXA1d3FYWWczSUJhUzBzM1JIODRZ?oc=5>

### AT&T Inc. $T Stock: International Assets Investment Management LLC Decreases Stake
- Summary: International Assets Investment Management LLC reduces its AT&T stake, signaling a shift in institutional ownership.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxNRm54U3l0bWhOVW9VMS1ZTG9RS0I4X3NNc2cxOEtxOVI4NWRLOXpUOHEyTmU1WmZmMmVnS2QyQ2VjQmZkUkpvaXZoNklzeFhvZWZxWVIzaGJnc3loUzRacEY2ZXB3cmVYOTdUUGhaZ3BNUlBGWkdOdjI3VjRKWXl2TG9qN0s3eWV1UTU2WW1WZTFkVWNfdWNmRXc2aUVWb2RST1pyTzJ4RUZuOElPSUFJUVlWWXhnMkVsT1ZpTGh1QzRkdk90MHRkemNFUHoyOVJVVWlYZGV3?oc=5>

### Fund Update: 1,886,214 AT&T (T) shares added to Cullen Capital Management, LLC portfolio
- Summary: Cullen Capital Management adds 1.9 million AT&T shares, reflecting increased institutional investment.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxQdzJFdmlkdDREMU83VlFHRU80c0FlNmwwcDBjanhiRmczSmFTc2dxemdpV0xocm1yeGRmSlYyWW8xREZVOVdCeGJjQW5YdFd1aHdPdkU3T2RJSVIydnJpM2FJMTV6MDBpYVdDcnJ3LVZSMG1SaTdHZGxxTkFxSU13SmhiT19fTUc0TjdtcUYza0pzNG16QUJTWkltOVN4VmFLeGd3TVNWdkxVem9NUTg0YTdEenB3ZnFVUGduNUpmMXB0ajQwLUtLUWJuQlN1TkxB?oc=5>

### AT&T Inc. $T Stock Holdings Decreased by International Assets Investment Management LLC
- Summary: International Assets Investment Management LLC reduces its AT&T stake, signaling a shift in institutional ownership.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi3gFBVV95cUxNWngzbGdtalpYRlpjU2w5cUtsTldiLUZMVVcxZElOODVZdkpNc0pJSlYzc0dqc0MyQ0h3enlmbHpJNWZBdDBDRXFRLUNMUjJtSXNRSVJiVjJfT2JhMkF4MS1JY0psQVBFekRwcHgtU3FsSDRyQ1RYWmxibUZvVlV1Y0d1d2RyNUplRElTOUtfaWlFdUNYZ3JlUERyZjI0N19NUTBKY0luTS1YT3I0UmUxU0xZV0xEdmR0Qk5WYnF1R3lmSzlQYUx0Sk1SYnprUXduSFBZOG5SckxTYmpEZ1E?oc=5>

### AT&T Inc. $T Stock Position Lifted by Alps Advisors Inc.
- Summary: Alps Advisors increased its stake in AT&T, signaling confidence in the company’s prospects.
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxNelZ5NTR5S09hQVlkZ2Y3dFdHNG93ZkFOc3ZGckt0UU5VdTVCRGpnT0JYam13bGJveUxMR090anM3RVdmcWNCOV8tSkstWGhPc2dUamVuWWtXeC0xd0JfZ3hkeXRDY2piVzFvVmwwaFlmdUwyckFHVnpDejY4My16YzhzS1NwNTV5OFlRWGpvQ0VoSXlqTHhWazR1TkhTY2xkMlhRbkZjQzhGakZPMFRDbFB5cw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **T** | **11.67** | **1.39** | **7.31** | **5.30** | **147,798,228,992.00 USD** | **-7.42** |
| VZ | 11.81 | 1.81 | 7.37 | 1.50 | 191,936,348,160.00 USD | 23.94 |
| TMUS | 16.30 | 3.19 | 8.27 | 7.40 | 179,101,810,688.00 USD | -16.14 |
| BCE | 11.70 | 1.35 | 7.38 | 2.20 | 20,179,857,408.00 USD | -0.61 |

Peers fetched as_of: 2026-11-10; T reuses existing data (market data as_of: 2026-11-10); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-10

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 32,322,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 891,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/732717/000073271726000372/t-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimAFBVV95cUxOV205OXl5UnNZZlVDUUZVNmFvdEVoUnFPYW10RTZROUtpOUpvb211dkVUQ2pMMlkzU0RSSkgtUklLUnc3aXI1Y1VtaTNOX1pVRGtURTBKQ0dvRlVqemhDMk0yYWNqVU5ZWHFxalRrUU9EX29tWlZZVHBFV24zdm5adnBldzNPYXppdWVjTnJqM2ZQREItNWM5OQ?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxQQzhTeVNGUjkyM281M1NQTHlScngzUDV2cWNyeWVzT3BQdXRTQ09VX2NYa1VhQW9GVDQ3T09kWGJiZVl0ZnhrMkNFa3E4M2h4SU5NWW5jMmJ5blptQkFxU05NTUtCenZEaXJCRlMtWGczZTAzRklsOTBoVUNHSXB6MUx2RGFTN1psVS1iVG41czg3NGg0TGpxU1NVb3NfVmJPSXp4N2FaMFhKeW5OYk9HWHQySzZ6UDDSAbwBQVVfeXFMTnA5RjlVYmhQQnpVdmlQRzlHZmktblFqa2tyTEM3TkYzLUdYdVVfMlNyNTZUZlNzZjd3T0NkcUZ6ZUJicUlYZXVUYW5kWWdKbkxsTEptbktWRm83bExWaG5zSWQ5V1ZYYmtQcDlHVElveHJoQTVyUjNqb3p2SkwwSnE2R3A4aHVOcXlVR3ZqVTRqbUdDYjVHWmxvNXV6ak1JQkNHV1VEZmFCOXlfZWZLMVJVVFFTTUlvb201Wmw?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOdE9zdjg3TERlenVnUzQ2MkpLTTRtSUU0LTBadHZvQmJyN3hTZWdOQVhuc2tVNnhzRzItUzYxS19NUkJnZFhIYjVGSHpwMDJ1dmNDRDhTZC1SY2lSWTNDdE1SVDBtbmJoVWx3VFdqSDVLNDI1NmEybmI5ZU03a01aMC1fbDZHanNqY0c3Yl9nSUYtblVDQUFYc0xPQUM?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxNOTBicHN0a1hkd3pjMGFKUjBpWVNMMTJmc2FGdjZRODBwd1VqcjZTTzVuSXFsd3duOEFhM2htVUlfX2lrbWcyUE9DN2xnMFlzVWlPNlhTbWNNOXlkQkw5eUh0d3U5UHlkM3ZXRVVRbGJCcUtwU3MxcThiWHc2V0FtU0t5NmZVQlhEYzJnWnNfV250aV9zUVJXNFIzQ3FiVEp3YXpPMnJERnhGYVdoSGJHWjQzMWFyVVNhTEFyUVNHSmZ3VUMwaWlHRnlEV09MSGVabVhhZmZPUnBOUQ?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxNcm8tYWtGY1RKVEpGcGc3THl3dXNvOTRQN0xoTXNBdnJwUmswMVg0d180VjlELTRFeFd2ejhvR1M5cE5QeUF3WDAwLTJpbFZQaFRuRG1NdkVON0drcGpFbjNvVU9uTngxU05FcmdWU2cwbDE0dS01MXRZSUdBZk9rSzJlRXdIRVE?oc=5
- https://news.google.com/rss/articles/CBMie0FVX3lxTFB2YXVlREQ3R0NieWVFMkRISThWcE5kRFRqcXVfdjVzUy0zenpJNVo4eFQ2Wmt5Q1Q1N002cVZ6MTUyU2JLYk9tQVg0bFM3d0VNU013Y180allLd1ZPeHE1OUtOeURuc0xrV0N5S3h4M2pmRGxwMURMV1JlOA?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNeVJqakhwY213N3laR2tsVk5Zam5UbFBhUWVqNEVILTRjdVlEUFJrQ21qV2RwUHNBVmZwQmNZT25JbHo2eFoxUnBGd01Ob1JpWEQzZzBsejJzcjE2X2F3MmJoM2Rpdm5mZ0l1azhKQnZpVnJaN09SdHJVWHUwbVRIaFMwRjhFNFlLY3hj?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQVGdGNGU4RU5IRWF6VDMtS0ZQeklodGF1VHdUeHV4eC1XVkdZY3NoRmZROFBZVlZrelkydFNYZHNYRlJzRUprT2VGaVFVTXFPWFN0OURNZUd4cnlaSmx6MXI4Tk55REtaeXRrNVF5aWVhbDZKX3lHeDRraVdPOVpvakNCRGtJblROUmw0ZmdidXF6MkFpbV9qSzJXQk1ZaW1lNktPNmJTNmE?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQMENnU1dvSXNRUjl6S1hnVUZJT0oxRUphNUxqYTBFcHRjQmE0R1ROYVRfdDh6di1jT0Y0bWpYUk1LbU9uczBEMEhkNERQRW1TMUFLQUppSnNSSXBVSjUxNldYUGhSeEowcGtJSXA1clpvODV3R1BrcWdQMVIzSG9yREthclI4c3JwVUZxS2o1V043Xzg4cWluQXhGUnRERm8?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxNSTNSUU9EenFtcnVyRHdYNm5mMXU3MDUwcEJaT3FnaWhSRElpSjVwV1NsQUphRmN4SV9GLTk4cXJFNnFtc1c2dGF0cG91aXFCdXVSc044UWhJdDBPN2VIak5NWXptZHRraUJvRGVvdVVtUF90S2NPejRnWExXNHlLVEp4dF9wMXh5WWdVV2RRVXNDZlZ3cWREOGNyRnJhUTFoeTlhQ2NCSmduNk0zWlFFSlJnZlVjbDhXbnZZZXJhcjlMdw?oc=5
- https://news.google.com/rss/articles/CBMic0FVX3lxTE5fSVJiZi0zX1JoRHd2YTJFNENVSVBFQ1pZOTIyT1h1ZFA3TjdNWmt3LTM3am1wSjFNNjBhZTZRamlZckdaQ1hRSUNwNXp3ZnNERkZhc3cyVHJrcDBaY1otN05pRm54VEJYQ2dCMndCWmhXTU0?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxPMndVTWxGVVhEX19hREV1aDRrb2RHS3ZxMzFIa2ZNeXBOcjkxbUVOZm9qRUlKaDZHeXMtSEdFZ3B2QTlGXzVtdXRhaGNTSndNOUxDaTZNdGxXWDI3cXRNVmhCcEl2WS1WbTZOckgzYkhETzNCSmxUTnhhYldrWTJHRkh0LVdtdXVRZzJrcWJtaTRlVll1cEU0RWtNNEpGTGgxYjVtUEZDeFFHZ1F4T1FwaEF1YXhDUdIBuwFBVV95cUxNbGVjdUJJcXVDU01lN1NpOUVST1RjZVI3OHRrWDh0UDZvWFYwa3hoSUVvMlBlWWdSUEcyRkc3dnNFU1I0S2h3eGR0R0hadXBVTnJONm5SeEdqTFZGM0JoOVVlSV82eGYwU2xzMzBIaHExNmVhZk9hM3Q4RkplM2cxbExNS3YxbXlJVFREaVhLTVU4N3ViTTloQmxYX1hUN3BBMC1ISURNNXA1d3FYWWczSUJhUzBzM1JIODRZ?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxNRm54U3l0bWhOVW9VMS1ZTG9RS0I4X3NNc2cxOEtxOVI4NWRLOXpUOHEyTmU1WmZmMmVnS2QyQ2VjQmZkUkpvaXZoNklzeFhvZWZxWVIzaGJnc3loUzRacEY2ZXB3cmVYOTdUUGhaZ3BNUlBGWkdOdjI3VjRKWXl2TG9qN0s3eWV1UTU2WW1WZTFkVWNfdWNmRXc2aUVWb2RST1pyTzJ4RUZuOElPSUFJUVlWWXhnMkVsT1ZpTGh1QzRkdk90MHRkemNFUHoyOVJVVWlYZGV3?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxQdzJFdmlkdDREMU83VlFHRU80c0FlNmwwcDBjanhiRmczSmFTc2dxemdpV0xocm1yeGRmSlYyWW8xREZVOVdCeGJjQW5YdFd1aHdPdkU3T2RJSVIydnJpM2FJMTV6MDBpYVdDcnJ3LVZSMG1SaTdHZGxxTkFxSU13SmhiT19fTUc0TjdtcUYza0pzNG16QUJTWkltOVN4VmFLeGd3TVNWdkxVem9NUTg0YTdEenB3ZnFVUGduNUpmMXB0ajQwLUtLUWJuQlN1TkxB?oc=5
- https://news.google.com/rss/articles/CBMi3gFBVV95cUxNWngzbGdtalpYRlpjU2w5cUtsTldiLUZMVVcxZElOODVZdkpNc0pJSlYzc0dqc0MyQ0h3enlmbHpJNWZBdDBDRXFRLUNMUjJtSXNRSVJiVjJfT2JhMkF4MS1JY0psQVBFekRwcHgtU3FsSDRyQ1RYWmxibUZvVlV1Y0d1d2RyNUplRElTOUtfaWlFdUNYZ3JlUERyZjI0N19NUTBKY0luTS1YT3I0UmUxU0xZV0xEdmR0Qk5WYnF1R3lmSzlQYUx0Sk1SYnprUXduSFBZOG5SckxTYmpEZ1E?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxNelZ5NTR5S09hQVlkZ2Y3dFdHNG93ZkFOc3ZGckt0UU5VdTVCRGpnT0JYam13bGJveUxMR090anM3RVdmcWNCOV8tSkstWGhPc2dUamVuWWtXeC0xd0JfZ3hkeXRDY2piVzFvVmwwaFlmdUwyckFHVnpDejY4My16YzhzS1NwNTV5OFlRWGpvQ0VoSXlqTHhWazR1TkhTY2xkMlhRbkZjQzhGakZPMFRDbFB5cw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
