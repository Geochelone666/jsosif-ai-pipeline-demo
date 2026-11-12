# CAT Intelligence Report

- ticker: **CAT**
- Report as_of: **2026-11-11**
- Market data as_of: **2026-11-11**
- Quant sources: https://finance.yahoo.com/quote/CAT/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CAT/key-statistics/
- AI analysis snapshot as_of: **2026-11-11**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-12T05:55:50.143786+00:00**
- AI status: **Partial: 1 headline remains unclassified and excluded from research conclusions**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 3, 'ai': 11, 'unknown': 1, 'irrelevant': 10})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **13** exact headline/source/date matches; prior report **20261111T043601Z-d14951e6/CAT** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 15 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 16.0%; oldest publication 2026-11-06

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 601.6100 |
| Return 1D (%) | 2.9150 |
| Return 1W (%) | 1.7436 |
| Return 1M (%) | -24.6642 |
| Return YTD (%) | 5.9099 |
| Return 1Y (%) | 6.8311 |
| Annualized volatility (%) | 41.4988 |
| Beta vs SPY | 1.8352 |
| Max drawdown (%) | -47.7898 |
| Sharpe (rf=0) | 0.3669 |
| Downside deviation (rf=0, %) | 29.3250 |
| Sortino (rf=0) | 0.5192 |
| Historical VaR 95% (1D, %) | 4.2437 |
| Historical ES 95% (1D, %) | 5.7878 |
| Correlation vs SPY | 0.6071 |
| Tracking error vs SPY (%) | 34.9118 |
| P/E (trailing) | 22.94 |
| P/B | 12.81 |
| EV/EBITDA | 18.49 |
| Revenue growth (%) | 17.30 |
| Forward P/E (estimate) | 18.66 |
| Gross margin (%) | 29.54 |
| Operating margin (%) | 18.76 |
| Return on equity (%) | 56.14 |
| Free cash flow yield (%) | 1.44 |
| MA50 | 747.1158 |
| Close vs MA50 (%) | -19.4757 |
| MA200 | 804.8429 |
| Close vs MA200 (%) | -25.2513 |
| RSI (14, Wilder) | 35.4884 |
| MACD (12,26) | -52.1496 |
| MACD signal (9) | -48.5480 |
| MACD histogram | -3.6016 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CAT': 280, 'SPY': 280}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 601.6100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.9150 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.7436 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -24.6642 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 5.9099 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 6.8311 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 41.4988 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 29.3250 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.5192 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.2437 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.7878 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6071 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 34.9118 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.8352 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -47.7898 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3669 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 18.6563 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 29.5420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 18.7610 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 56.1350 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.4433 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 22.9447 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 35.4884 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.6016 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -19.4757 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -25.2513 -> Clearly below the moving-average trend level.

## TAILWINDS

### Caterpillar stock rallies as Anthropic generator order and record results boost sentiment
- Summary: Caterpillar stock rallies as Anthropic generator order and record results boost sentiment
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNX2JxV0djQ3diY0o5amlwWW5xMVhnTS1MSXhENGQxel9JY00tNThkamk0TUh0bUZMYTdkcm9vNWJJY25kWFRGX1RUV3l1VllzMjc3bVhlMm5hdWJMU1YxTndLQndrSFItQWRxeU05RlN2N0paZDNPVktRTlRUcHdHWktNdmJJdGhhNlFXbFFNYjFnbC02VUxxdEVKOXA?oc=5>

### Caterpillar Stock Jumps 7% on Anthropic's $3.4 Billion Deal, With $628.70 Next
- Summary: Caterpillar Stock Jumps 7% on Anthropic's $3.4 Billion Deal, With $628.70 Next
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi-gFBVV95cUxQZ3N5d2hOR2ZJLTYzX2NKUGYzVnRqZ0c5RWJNMUFobWR1Z2xCdlRiaXNpNjBzZWp3U0tRWmF3aTZSZUZPMmxzSTMzcmk3dTRsVGdudmFpSkhjU3MtVmFVcXNza2N6UmExQzJJRGxnMnNvSWQtdklRYnJLYU9JQXNMTVJ1VmRmY2JKOWZBZ3AtWUxlM1V3akpVUTNOV3JjUGpVTzJVdzV0TnNlUk1MQXFSazhNX3NxV0RHcE9NTnNRN2Vfd28zSXpmNUVuYnpIOHJlaktoLVlDd3dDOGJKR1VGUXhvRkRBdGJUbUd6clJkS0FyOHlLYzUyNU93?oc=5>

## HEADWINDS

### Caterpillar Stock Sinks 10% in a Week Despite Record Backlog: Is It a Buy?
- Summary: Caterpillar Stock Sinks 10% in a Week Despite Record Backlog: Is It a Buy?
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQejZtY3VabmQ4VHhlRU9zZ1owV3F5dkpmSWEtYzFGR0dQLTVKcGtvMUloR1QyejZoSHFGdk80Q1EwU1Z6WUlyZWFIc0xvRUJfNm5KWXBFSGV1MjFyUjdXLUp4TVhXelBraEI5QVREMVBQdTFPVzE5WUZ3X19yaENmbUdSaTNWSFNuOXhabU1yMnVnd3ljejkwdkp4OWtVZw?oc=5>

### Michael Burry Cashes In On Caterpillar Puts After 4X Gain — Is CAT Stock Still Overvalued?
- Summary: Burry’s puts suggest bearish sentiment.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNWlFPd3JLaXpOZVZXUHJYOF9tOVFIS3lJUFNjSi1maUZnRFNCN3hNWjRpSXI0a0lla05ibDhiYWlDbXRlUnF6WmtHUzhmVFhDUGZ1WWxCeXNvTXE1TGNNTDl5WjdmVFlyb0RGbG1EM3BWeWIxY0gtbnVhTlNTQkZvQVBwOXpTQ3RzQ1BnZUJObWtzejhHVFlDWDY5RXVhMVNZTkt0cQ?oc=5>

### Caterpillar Inc Stock (CAT) Opened Down by 3.21% on Nov 10: What Investors Need To Know
- Summary: Opening decline indicates short‑term downside pressure.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxNQlM1U25JV09KYWxJRkU1cTV4RFFOZmUyS3FHNlhSYmlOSldQM1hxZ0pZZFJfNDlLQzFXbkstaHRuSTBQR3llNEM2WUNfaGV1bmV4TTBmN1JaNVI2elZieHZqZzNXeFBfc2ZwcURndkdRVW52YlRkUlBhdnRHMnA3a0J5MUlZajh0OEE?oc=5>

## CATALYSTS

### Caterpillar Stocks Jump 6.61% as Anthropic Takes Over $3.4 Billion Generator Order
- Summary: Caterpillar’s stock surged after Anthropic secured a $3.4B generator contract, signaling a significant product win.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPeHNqTHAxVnZNSjZwbkNvYVRQSGpZTjFfUUhyOGRvVmswVl9Fb2NqaWtSQzc4bWFjb25fZzl3VmhyS0lhV2pHdkNYM3JTdHd4RVEyMkdRa0xPOUdBaFFEXzdDWFVnd1ZMSmtmUURSOTkzaEUtYTEtOVNGNGEzR2VfbG12ci1YeWlENXRDcmlialo5UUQwWW9RYg?oc=5>

### Michael Burry trims Caterpillar bearish bet after puts nearly quadruple (CAT:NYSE)
- Summary: Analyst Michael Burry reduced bearish position after significant put activity.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxNenhDZnVjT3I5TWg4b2pELVpBZUl0OXRHTTZFdWs0bVotNmRhcnF0QlpUcmJoR0s1U1I3M0JidEtvU0Rqemh6VXBRZ2NsV3lYOFdIMUViMVJkZlUyZ1BZWk5scTNhc090YlVFUjhsY095c3c5Wl9ZbDB3S3dPRW9vS3ZIdzg0SUVCeFhIQ1ByZUpQUmxaY3M5QUprb0w1RDktbTZTTTdHZkpKV09UZUE?oc=5>

### Caterpillar Inc Stock (CAT) Moved Up by 6.33% on Nov 9: Facts Behind the Movement
- Summary: CAT shares rose 6.33% on Nov 9, reflecting positive market sentiment and potential underlying catalysts.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxPYWhHMi1yN2MyUnhlZmlPdFdLOTNjeURLWFlFWEc1THo3Y2JRUllZVWNIcG5PbVU2SVVIWXFQb3c5WHJxTnpPT2tmYVNxSzZXb3QyME91X2lmdXVUOHl0eW91UFA5WXBtN0dPSWlIbHVybkU2ZENISENkMTJ4WUJwaGtfMXMwbTVaRmc?oc=5>

### A Look at Caterpillar Inc (CAT) After 7.2% Gain -- GF Value $504
- Summary: CAT experienced a 7.2% gain, boosting its GF value to $504 and indicating strong investor confidence.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxNTnRjQmJITUVpQkcyejM3NEppdUJyRldHaXJfOUZiZEd0RElCXzgyMGRYb0FQUzBnOFRaU0J2NEUwZUFXRW43Nkl0MElPOXBwQVVWN2hMMzg4SDRZaDNwVmxEWllHSDg4VmZmREc4ak9YRS0wQ0k1Z3JkSjlhckEwOG9mZ1ZHT0c3RVpvLUJseHg1em12eFVCRnE3M015UXNIWHIwVXV4WHAxV0l4RnVOVW1R?oc=5>

### Why Is Caterpillar (CAT) In Focus After A $3.4 Billion AI Power Order?
- Summary: A $3.4B AI power order boosts Caterpillar’s product pipeline and revenue prospects.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxPd1dlc2g0VjBPM0lPNTVkc0Nsa05jQ1hfd0ZiQklZVXBURW9hczBiaHFGSkF5M2NuWDBRa3podnlnbHgwby0xRDNsUDJFLTMwcjBwdzlPeFRYY1VnZHJSQkxXYlBQNk85MGF5SUtvaG42TnFSQVBVbVdKMjNJNmNrX1hGbkNHQXRseldEZllaWVVFY1Z0aDF0QklZVzRtMngyNDg0bW1tZFVDcC1WSzY4aWJiUVNaU0lkZmNsYmQzMDZoUlllYW44N2dEa9IB0AFBVV95cUxPX3NlWS1va3VicDZxUnNCWUhxRENldXhydUl5SXhzdjN0VHdRVFl4NkZqS21STWsyeEtxZ1J0REkyMXJUV29WNTNBN2l6M195dDE1WFYwd3ByUFd6eVowclRFdjdKMFZlWVo2VFBOWDJRNUUtYzJlYzVjM1NTOUhKTUNLeEJHQzFTTDQzZy1LQnBhMGl0MXdlaDlXLW5PbkpIMjlLUVZYUUlpeE1ZMHhYTEFBMGswUHBhWGhpMjhrYXdIRi1OSEtTc3A4Q082aElr?oc=5>

### Terex, Titan International, Caterpillar, AGCO, and AeroVironment shares skyrocket, what you need to know
- Summary: Caterpillar shares surged, indicating strong market sentiment and potential upside.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikwJBVV95cUxNakgxTXNwMlRFcVNOWmJTanY0MnBsR05CeWdnMVE0YjR1RWx5aFYyM0YxV1dLU2czNUdqWjg5WFV3NTVaUjl2OXFYeWZXcVMtejVBV3N0UWtjT0YxbjFMMEEyQWFwZzF0SFNfSHZmY2NCMzNBNUJLTmwxeU5VZlVrdGRyeHZ1R1ZKUHN6NjNqTXpncHNGY1pCUHJmWkctM2I1MlJGM05VbVd0eVhPTFI2Umx1TGt1bWgxOXpvS1hYM292ZzllQ1Y1QUZSUDA3SGtZbVlhWEZXQjA3WFNUdTVnSkxOUHR6QTRJOHN6NHQya0tBM1ZoN0IwRnBtWFFwMUw0Z0syLWwtZ1NzaVM0emFoNXdQWQ?oc=5>

### Caterpillar stock support and resistance levels after 5.8% rebound
- Summary: Technical analysis shows key support/resistance levels post-rebound.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxNZkE4aGxDRDhTaU1ZMUhLdHduaXpUaW5HV1daM2hKTElfN3JDT0RvYU9lNU1iX3dVSGd2SXhNNEJLa1d1by02LUozVlg0YmhDRFpnMG1Lb21Bc3BMNnRYaW1iS0VtbUdYRzVZVlpsNTNteFpBX0hIM1o3SWljcXNUYUVNZkg0MHhtekVPd3hlWVBmbTdTZVN4S0RHUEdoSFE4RUxNNlk3ekJCandNdHM5ZFQ4RW5EenBZcTgwNDdLOF9sLWE3?oc=5>

### Is The Market Underpricing Caterpillar Stock?
- Summary: Questioning whether Caterpillar’s stock is undervalued by the market.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPSzZUOTVXRk5ObmpOb3Nqdld4NC0tMC0weUdJYy1vWXpDUVBfeFNVakJRMHhFaUpIRUdhNjZ2OUZ1Snl3aDk1b3gtSmVLY1NwQWloZWRjNENCaEhnMHJpR0pkNFZDVDRzYXlaaUExaTFKc2NDM3RyS3VidGZtTmFrbDlkOGRWcWVfWUhzanVicm14eTdKZGFNZ3NjNUxwYVU1R0Ficg?oc=5>

### Michael Burry just made a big move on Caterpillar stock
- Summary: Michael Burry has increased his stake in Caterpillar, signaling confidence in the company.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxPNjNSWWZwMzh1LUlsNXBWZzNKM3pDWGhHT1RVX0FKSGNHY1dRakNoVmlDUmJvSDFvbjl1aExGYl9CNHBmNlEzSmw3a2xia3FVNHduanYzdDRVczJFUEthMlRQXzNmTDJWVHEyc3pQX2hWQVpwMVg3WEtzWlp2Vk1JOGNyR0M?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CAT** | **22.94** | **12.81** | **18.49** | **17.30** | **275,293,241,344.00 USD** | **6.83** |
| DE | 38.22 | 6.66 | 28.40 | 4.90 | 186,513,375,232.00 USD | 46.38 |
| CNH | 59.48 | 1.98 | 18.73 | -1.00 | 20,057,022,464.00 USD | 27.64 |
| CMI | 19.33 | 4.76 | 12.77 | 13.50 | 63,502,704,640.00 USD | -1.26 |

Peers fetched as_of: 2026-11-11; CAT reuses existing data (market data as_of: 2026-11-11); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-29
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-11

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 20,682,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 1,141,000,000.00 USD; period 2011-07-01/2011-09-30; fiscal year/reporting period 2011/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/18230/000001823026000057/cat-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMinAFBVV95cUxNX2JxV0djQ3diY0o5amlwWW5xMVhnTS1MSXhENGQxel9JY00tNThkamk0TUh0bUZMYTdkcm9vNWJJY25kWFRGX1RUV3l1VllzMjc3bVhlMm5hdWJMU1YxTndLQndrSFItQWRxeU05RlN2N0paZDNPVktRTlRUcHdHWktNdmJJdGhhNlFXbFFNYjFnbC02VUxxdEVKOXA?oc=5
- https://news.google.com/rss/articles/CBMi-gFBVV95cUxQZ3N5d2hOR2ZJLTYzX2NKUGYzVnRqZ0c5RWJNMUFobWR1Z2xCdlRiaXNpNjBzZWp3U0tRWmF3aTZSZUZPMmxzSTMzcmk3dTRsVGdudmFpSkhjU3MtVmFVcXNza2N6UmExQzJJRGxnMnNvSWQtdklRYnJLYU9JQXNMTVJ1VmRmY2JKOWZBZ3AtWUxlM1V3akpVUTNOV3JjUGpVTzJVdzV0TnNlUk1MQXFSazhNX3NxV0RHcE9NTnNRN2Vfd28zSXpmNUVuYnpIOHJlaktoLVlDd3dDOGJKR1VGUXhvRkRBdGJUbUd6clJkS0FyOHlLYzUyNU93?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQejZtY3VabmQ4VHhlRU9zZ1owV3F5dkpmSWEtYzFGR0dQLTVKcGtvMUloR1QyejZoSHFGdk80Q1EwU1Z6WUlyZWFIc0xvRUJfNm5KWXBFSGV1MjFyUjdXLUp4TVhXelBraEI5QVREMVBQdTFPVzE5WUZ3X19yaENmbUdSaTNWSFNuOXhabU1yMnVnd3ljejkwdkp4OWtVZw?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNWlFPd3JLaXpOZVZXUHJYOF9tOVFIS3lJUFNjSi1maUZnRFNCN3hNWjRpSXI0a0lla05ibDhiYWlDbXRlUnF6WmtHUzhmVFhDUGZ1WWxCeXNvTXE1TGNNTDl5WjdmVFlyb0RGbG1EM3BWeWIxY0gtbnVhTlNTQkZvQVBwOXpTQ3RzQ1BnZUJObWtzejhHVFlDWDY5RXVhMVNZTkt0cQ?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxNQlM1U25JV09KYWxJRkU1cTV4RFFOZmUyS3FHNlhSYmlOSldQM1hxZ0pZZFJfNDlLQzFXbkstaHRuSTBQR3llNEM2WUNfaGV1bmV4TTBmN1JaNVI2elZieHZqZzNXeFBfc2ZwcURndkdRVW52YlRkUlBhdnRHMnA3a0J5MUlZajh0OEE?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPeHNqTHAxVnZNSjZwbkNvYVRQSGpZTjFfUUhyOGRvVmswVl9Fb2NqaWtSQzc4bWFjb25fZzl3VmhyS0lhV2pHdkNYM3JTdHd4RVEyMkdRa0xPOUdBaFFEXzdDWFVnd1ZMSmtmUURSOTkzaEUtYTEtOVNGNGEzR2VfbG12ci1YeWlENXRDcmlialo5UUQwWW9RYg?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxNenhDZnVjT3I5TWg4b2pELVpBZUl0OXRHTTZFdWs0bVotNmRhcnF0QlpUcmJoR0s1U1I3M0JidEtvU0Rqemh6VXBRZ2NsV3lYOFdIMUViMVJkZlUyZ1BZWk5scTNhc090YlVFUjhsY095c3c5Wl9ZbDB3S3dPRW9vS3ZIdzg0SUVCeFhIQ1ByZUpQUmxaY3M5QUprb0w1RDktbTZTTTdHZkpKV09UZUE?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxPYWhHMi1yN2MyUnhlZmlPdFdLOTNjeURLWFlFWEc1THo3Y2JRUllZVWNIcG5PbVU2SVVIWXFQb3c5WHJxTnpPT2tmYVNxSzZXb3QyME91X2lmdXVUOHl0eW91UFA5WXBtN0dPSWlIbHVybkU2ZENISENkMTJ4WUJwaGtfMXMwbTVaRmc?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxNTnRjQmJITUVpQkcyejM3NEppdUJyRldHaXJfOUZiZEd0RElCXzgyMGRYb0FQUzBnOFRaU0J2NEUwZUFXRW43Nkl0MElPOXBwQVVWN2hMMzg4SDRZaDNwVmxEWllHSDg4VmZmREc4ak9YRS0wQ0k1Z3JkSjlhckEwOG9mZ1ZHT0c3RVpvLUJseHg1em12eFVCRnE3M015UXNIWHIwVXV4WHAxV0l4RnVOVW1R?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxPd1dlc2g0VjBPM0lPNTVkc0Nsa05jQ1hfd0ZiQklZVXBURW9hczBiaHFGSkF5M2NuWDBRa3podnlnbHgwby0xRDNsUDJFLTMwcjBwdzlPeFRYY1VnZHJSQkxXYlBQNk85MGF5SUtvaG42TnFSQVBVbVdKMjNJNmNrX1hGbkNHQXRseldEZllaWVVFY1Z0aDF0QklZVzRtMngyNDg0bW1tZFVDcC1WSzY4aWJiUVNaU0lkZmNsYmQzMDZoUlllYW44N2dEa9IB0AFBVV95cUxPX3NlWS1va3VicDZxUnNCWUhxRENldXhydUl5SXhzdjN0VHdRVFl4NkZqS21STWsyeEtxZ1J0REkyMXJUV29WNTNBN2l6M195dDE1WFYwd3ByUFd6eVowclRFdjdKMFZlWVo2VFBOWDJRNUUtYzJlYzVjM1NTOUhKTUNLeEJHQzFTTDQzZy1LQnBhMGl0MXdlaDlXLW5PbkpIMjlLUVZYUUlpeE1ZMHhYTEFBMGswUHBhWGhpMjhrYXdIRi1OSEtTc3A4Q082aElr?oc=5
- https://news.google.com/rss/articles/CBMikwJBVV95cUxNakgxTXNwMlRFcVNOWmJTanY0MnBsR05CeWdnMVE0YjR1RWx5aFYyM0YxV1dLU2czNUdqWjg5WFV3NTVaUjl2OXFYeWZXcVMtejVBV3N0UWtjT0YxbjFMMEEyQWFwZzF0SFNfSHZmY2NCMzNBNUJLTmwxeU5VZlVrdGRyeHZ1R1ZKUHN6NjNqTXpncHNGY1pCUHJmWkctM2I1MlJGM05VbVd0eVhPTFI2Umx1TGt1bWgxOXpvS1hYM292ZzllQ1Y1QUZSUDA3SGtZbVlhWEZXQjA3WFNUdTVnSkxOUHR6QTRJOHN6NHQya0tBM1ZoN0IwRnBtWFFwMUw0Z0syLWwtZ1NzaVM0emFoNXdQWQ?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxNZkE4aGxDRDhTaU1ZMUhLdHduaXpUaW5HV1daM2hKTElfN3JDT0RvYU9lNU1iX3dVSGd2SXhNNEJLa1d1by02LUozVlg0YmhDRFpnMG1Lb21Bc3BMNnRYaW1iS0VtbUdYRzVZVlpsNTNteFpBX0hIM1o3SWljcXNUYUVNZkg0MHhtekVPd3hlWVBmbTdTZVN4S0RHUEdoSFE4RUxNNlk3ekJCandNdHM5ZFQ4RW5EenBZcTgwNDdLOF9sLWE3?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPSzZUOTVXRk5ObmpOb3Nqdld4NC0tMC0weUdJYy1vWXpDUVBfeFNVakJRMHhFaUpIRUdhNjZ2OUZ1Snl3aDk1b3gtSmVLY1NwQWloZWRjNENCaEhnMHJpR0pkNFZDVDRzYXlaaUExaTFKc2NDM3RyS3VidGZtTmFrbDlkOGRWcWVfWUhzanVicm14eTdKZGFNZ3NjNUxwYVU1R0Ficg?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxPNjNSWWZwMzh1LUlsNXBWZzNKM3pDWGhHT1RVX0FKSGNHY1dRakNoVmlDUmJvSDFvbjl1aExGYl9CNHBmNlEzSmw3a2xia3FVNHduanYzdDRVczJFUEthMlRQXzNmTDJWVHEyc3pQX2hWQVpwMVg3WEtzWlp2Vk1JOGNyR0M?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
