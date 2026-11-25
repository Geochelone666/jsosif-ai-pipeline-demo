# MCO Intelligence Report

- ticker: **MCO**
- Report as_of: **2026-11-24**
- Market data as_of: **2026-11-24**
- Quant sources: https://finance.yahoo.com/quote/MCO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MCO/key-statistics/
- AI analysis snapshot as_of: **2026-11-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-25T07:14:05.303669+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 18, 'rule': 5, 'ai': 8, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261124T081701Z-6c335e3d/MCO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 18 unique headlines; 9 named publishers; 1 exact duplicates; 18 HTTPS source links; largest publisher share 38.89%; oldest publication 2026-11-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 485.4000 |
| Return 1D (%) | 1.0009 |
| Return 1W (%) | 0.4236 |
| Return 1M (%) | 0.6230 |
| Return YTD (%) | -4.1383 |
| Return 1Y (%) | 2.2892 |
| Annualized volatility (%) | 28.9901 |
| Beta vs SPY | 0.5467 |
| Max drawdown (%) | -23.6059 |
| Sharpe (rf=0) | 0.2234 |
| Downside deviation (rf=0, %) | 20.6710 |
| Sortino (rf=0) | 0.3133 |
| Historical VaR 95% (1D, %) | 2.4795 |
| Historical ES 95% (1D, %) | 3.9934 |
| Correlation vs SPY | 0.2820 |
| Tracking error vs SPY (%) | 28.6273 |
| P/E (trailing) | 29.62 |
| P/B | 25.61 |
| EV/EBITDA | 22.19 |
| Revenue growth (%) | 0.80 |
| Forward P/E (estimate) | 26.10 |
| Gross margin (%) | 74.63 |
| Operating margin (%) | 46.04 |
| Return on equity (%) | 76.74 |
| Free cash flow yield (%) | 3.03 |
| MA50 | 478.1540 |
| Close vs MA50 (%) | 1.5154 |
| MA200 | 464.3279 |
| Close vs MA200 (%) | 4.5382 |
| RSI (14, Wilder) | 48.5016 |
| MACD (12,26) | -0.7624 |
| MACD signal (9) | 3.4216 |
| MACD histogram | -4.1840 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MCO': 289, 'SPY': 289}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 485.4000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.0009 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.4236 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 0.6230 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -4.1383 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 2.2892 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 28.9901 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 20.6710 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.3133 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.4795 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.9934 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2820 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 28.6273 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5467 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -23.6059 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2234 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 26.0996 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.6330 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 46.0370 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 76.7410 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 3.0284 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 29.6156 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 48.5016 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -4.1840 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 1.5154 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 4.5382 -> Slightly above the moving-average trend level.

## TAILWINDS

### What Is Driving Fresh Interest in Moody's (NYSE:MCO) This Week?
- Summary: Investors show renewed interest in MCO, indicating potential upside.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNcEFwZm85empqS3FNTE9FN05YbnN3OWs2SUk2bUlfMTRMZklET1RoT010eFpEZjhVU2tyaDJMNjE4ZENOTFhQVVhTdWIwekJ1Z2oxbVVhdDVNck1ldWZrVGZqTDRrdU5ZYTdIQndNWGpwckJqNXByakl0T2RWWExjTmdETjJjQXdvcjNFN0hVY1J5UjNScXdxUVhfVkloX3gyenk0VV9B?oc=5>

### Moody's Corporation $MCO Holdings Boosted by Public Sector Pension Investment Board
- Summary: Pension board increased holdings in Moody's, signaling confidence and potential share price support.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxPbjh5SGRwd1BmVmdXSUtTVlRSVHRYQ1FpMGdrV3RmMnBmbWllTGZOQ3BIWGF4Z2V2Y3R6OUVGOFgxZHg1WWRCd1RJSHNHQzdmbFR2bFFiVXQzeXBTR2hWRkl3YjFWQ3lnckk2RnA3ZXQyaXJkeFB0M2htdnhFQU5fOVJLRkZ1V1BGdGFCSWRjb2t4V0JoMGE1bS02SEFIWExqUmNscWZOVkY4dFlnYVdORDF3WmRIVHZ3NC11dmEyTndmLTIzZE1iNUdNOHZ2bnJKMnRDb1NmX1BQdw?oc=5>

## HEADWINDS

### Moody's (NYSE:MCO) Stock Breaks Below 50 Day Moving Average - Here's What Happened
- Summary: Stock fell below 50‑day MA, signaling short‑term weakness.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxNUUZXS09ONmNKTFM5YU96Vm9mTXRxX3ZxVmxSOEFiQzZMWFNsQmx5NWR4VGtCOHliWWQ1cWl5WW5BQnFNNVpJN1FFNUhhczNCaV9uTlhGQWlLRHVkNUZlUTFjV3ZxV0Uwak5fSHpNQTlrMEFiNllDMGFZcWF3ak9RbjRIUUNhdjVxSU1aazRseHBfbkNrS0hjUHZ6cFpFZ1N0SWlEVHdCUEpNaVcwa0dfTk5mQzZxbEZaTnRSN3RxZ1d1Wi1wRmJfaTNtSWdDZklwU3c?oc=5>

### 7,018,315 Moody's Corporation $MCO Shares Sold by State Street Corp
- Summary: Large share sale may pressure price and signal concern.
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxOVTFsRk1FOHJWVm5rN1c2Y19EMWVrRjJUOWRqYlZobUZhaFdxSDd2ejlmQ1hXWjZOSnFmUUxLQVdZaW11MUR4eUw2b1d2M1l0eWI1M2NYbDdwTGd1R0Z6OGdzcDBUZEVUTTVqVGtCOU1SaUhHdjFuOV96VGNZV0M4UjhZaHJPeDVGOEw3R1pXTDBhN09LNkl2TmNWZkVUM1JNRXJPT3VPRHdXU2daaXFyX3ozMW9LRU0tYWJLZFNtaHcyQQ?oc=5>

### What Triggered Moody's (NYSE:MCO) Shares to Plunge More Than 7% on November 17?
- Summary: Shares fell over 7% on Nov 17, indicating a significant market decline.
- Date: 2026-11-18 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxObGw4Q0FJQjBUelJLYlBiOUhOSnlPOVpoNG9xU0p2YU82bTZwQkRBdndHalJlUWFrdkNKVjN3emMzLTlvV2wyazJ5SDVBU1FOR2E2cnVCT0hhQ2tqb0lVNzk1NFExWUE4VmNKdnY2TFNYcXZmTUlMTkVZLTI5YTNCb1JsaTUwaUV5R241UFZNajNTM1FEUGg4SUpqd3N0NFFneEhvSURwWHh1SEk?oc=5>

## CATALYSTS

### Moody's Corporation $MCO Stock Bought by First Trust Advisors LP
- Summary: Moody's Corporation $MCO Stock Bought by First Trust Advisors LP
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxOUF95TFhmN2dTajBJdXZwaXQxczVwOXVIUG03bWVzRFNDLXhXWFh5dFNLVVFpTnJQdVQtVFdKWUUybHh5dmtoUXJ3eVJoTVpRNDU5QkRPUnozMHBSUUhwZDNSTldwdDdCc1pfbHBmTlVEWHZKNUpNYURrcU8xeGlSakViZXFwVlZZakF2eVM0R1hqV05kZXdtdEctNGt6akhwSUhWTFMyRzYyRVQ3ZTE1dUtHd2VqOVE5Q1laRHBZMFM?oc=5>

### Moody's Corporation (NYSE:MCO) Stock Now Rated "Moderate Buy" by Sell-Side Analysts
- Summary: Moody's Corporation (NYSE:MCO) Stock Now Rated "Moderate Buy" by Sell-Side Analysts
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxNWFdsOEgtTXh6am5DOEZDZDhYeHhBTFpQVjBicW9mS18tTWljQUt1Rk9VV1pmSldqX1Zlc2k5M0dibl91UlNLRHBvcHpucW9rOG1qRVZweVlmbmVkUzRvaFlpMUp6VDNiOFNHTEh6VDdnNC1LMmswWXByN2xnbG5vSVpEYXdjN3BxMV84OUt1Uk1CUlZUSm12OFlpd1B4Q3RqTVFYOEIxaVdLMW1SNVAtQzh5ajNZWmhSc1NtbEdiNEJkUGgtY3ItNkhINnZVNjJTZzFKdVBIWi0yZw?oc=5>

### Moody's Corporation (NYSE:MCO) Passed Our Checks, And It's About To Pay A US$1.03 Dividend
- Summary: Moody's Corporation (NYSE:MCO) Passed Our Checks, And It's About To Pay A US$1.03 Dividend
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxQN05SbThuc2dURTRDSTNRUF9IX0JGcE5wT3d0bkJzakZaYVhzRVYtVVRpc2thVTRZOGZpMmc2VldpQzZ1eEh4Q3U1U1dHSG1rUVdDR3F0aDhJZXZ6SE1remctNTdramUxelRGbmZGX0V5aFpjNThvQ3Q3VDZJb0p1alZWYUdHWUNJdGlMS2txckpoMkxxelhPalNLSzRKVGJEcUYwZEtkcFl2OFUzMzVLVjgydHUzNjJQdVVCenprUlQtQlhPRDY3M0NabkdBa0hzSXpNdw?oc=5>

### Moody's Corporation $MCO Stock: Voya Investment Management LLC Increases Stake
- Summary: Moody's Corporation $MCO Stock: Voya Investment Management LLC Increases Stake
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxQVkRHZXZvWklQYnM3SFd1VXlUTUpuRlk2OVA2VEU4RDgxdmpTeWM2V0tIQ2xDVkdDZmFvWXh2RzdsVVNqOG5iYjJYbzlrYml5U0NQbTFhdGJSMTZ2NWtrZkMzZGhVenVWbW5fMV9aaTFyMjVxWnNic29lWjUwYl9YN0pzVWduTFlGc1MxRVlfTUtXTXAtSG1POVRIMFBzV20zMGpFc1FNLVhRUnlUSS1jdTdTMklyX1dmT3RyNWpLTFFDT1pHallTS1U0OHplakJ5OWc?oc=5>

### Moody's Corporation $MCO Shares Sold by Aberdeen Group plc
- Summary: Moody's Corporation $MCO Shares Sold by Aberdeen Group plc
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxPOHpKM3k4UWNxLXdtUDFkQjVGd1F0ejBWOTlweUwwMnMtTGl2dWs3d1drU0s4UERlbW1XdlNQX0gxcXFzdEVNR2lFa1JTTGNWdi1VZDAtXzdGMXhRWUlzTkJ5YXN5WjBERC0wbUU0MzVka3oxM1ZjdWctamJ2eDRoTFBLcGgyQVE0RXh5SGU4MUJyRVE4NmNFLTltOThoNmt0bVR3blFiSkVfN1dWRFlKb25zaUE1bkR0?oc=5>

### Moody's Embeds Connected Intelligence in the Platforms Where Customers Build With AI
- Summary: Moody’s adds Connected Intelligence to its AI platforms, enhancing customer build capabilities.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxNX184T1YzY0pSc29zeDVmcFgzaDYyT0hFcTNMNXFFcDMtOVVLNEh1bGhMU3JZRV9kTVhJSV9QTWVKRndkaHpTUXZuak1NdUZDZS1ITGVPemd4RzRSa2E1ODlvVUxFb0Z4bTRGNkdfOW1zNFlBWWhna2NocWJkQTRWY2E4OExYb3hIUk5jVERlWFFvbHlaUG1YZjV1SGhKQlVkN0s2S2VvWVpTZEpoX2NtQlZjWXA?oc=5>

### Moody's Ratings Gain From AI Infrastructure and Private Credit Growth
- Summary: Moody’s ratings improve due to AI infrastructure and private credit growth, boosting market perception.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxQTkJMNE9uWENURzJjM1g3OVFfY01Cc3pOYUItckFDZWo5TFRKSE9KVThPOU5KLWlfSnNTV1NPYmJyb3dUSVJuRUYtTGVEdEFDS0JoWnA1ZUtoWC15N0praV9jTWZlb3ZmT3l2Q3R5MGNaSFc5WWljWWJNa3RQVGNpbUEzeFAtZnlpcHRPRmlOWWtPTTRXaDdmSE9seUlGUG9BLWpzNw?oc=5>

### Moody’s Sees AI Infrastructure and Private Credit Fueling Growth as Private Markets Demand More Ratings
- Summary: MCO forecasts growth driven by AI infrastructure and private credit demand.
- Date: 2026-11-18 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi-gFBVV95cUxOVnR0cVdKZFd4dUphRjl2Wkp4QkVDczZJUGVhQTdmb0JPVFZyU2VBX0I2R2tzTUZmYVE1VGFHLWxxVHRSd2kzejg5UWQ3ZVpzX1RIVE85bGxiRjNnYUJFdUtsN2dFRGNNdjVpVXR0ZGs0bzZQeHppdGtYSnQwMDhfWkg4NnNvOE91dmNwWWE5bXljbjdUN2ptcjRvdU9ORGNhWjlVaDdMSnNmcjNqYVBxdUlyOFUtZEFFWnhGUkhjTUpKNnpsRkZYY0RkandTcnZ0aGRUZk1RY01XRlhDM2dhRHZ6QnNHV3d2OEMxSUF1Vjk0WFdWSlN0REtn?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MCO** | **29.62** | **25.61** | **22.19** | **0.80** | **83,694,649,344.00 USD** | **2.29** |
| SPGI | 27.19 | 6.69 | 17.68 | 6.80 | 131,953,786,880.00 USD | -0.79 |
| MSCI | 33.52 | -15.07 | 25.74 | 12.40 | 45,325,279,232.00 USD | 15.53 |
| FDS | 22.01 | 5.65 | 13.98 | 6.30 | 11,307,195,392.00 USD | 20.13 |

Peers fetched as_of: 2026-11-24; MCO reuses existing data (market data as_of: 2026-11-24); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-02-17 (yfinance; expected dates may change)

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
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 1,142,100,000.00 USD; period 2019-01-01/2019-03-31; fiscal year/reporting period 2019/Q1
- Net income (latest available single quarter): 734,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1059556/000162828026066731/mco-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMipgFBVV95cUxNcEFwZm85empqS3FNTE9FN05YbnN3OWs2SUk2bUlfMTRMZklET1RoT010eFpEZjhVU2tyaDJMNjE4ZENOTFhQVVhTdWIwekJ1Z2oxbVVhdDVNck1ldWZrVGZqTDRrdU5ZYTdIQndNWGpwckJqNXByakl0T2RWWExjTmdETjJjQXdvcjNFN0hVY1J5UjNScXdxUVhfVkloX3gyenk0VV9B?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxPbjh5SGRwd1BmVmdXSUtTVlRSVHRYQ1FpMGdrV3RmMnBmbWllTGZOQ3BIWGF4Z2V2Y3R6OUVGOFgxZHg1WWRCd1RJSHNHQzdmbFR2bFFiVXQzeXBTR2hWRkl3YjFWQ3lnckk2RnA3ZXQyaXJkeFB0M2htdnhFQU5fOVJLRkZ1V1BGdGFCSWRjb2t4V0JoMGE1bS02SEFIWExqUmNscWZOVkY4dFlnYVdORDF3WmRIVHZ3NC11dmEyTndmLTIzZE1iNUdNOHZ2bnJKMnRDb1NmX1BQdw?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxNUUZXS09ONmNKTFM5YU96Vm9mTXRxX3ZxVmxSOEFiQzZMWFNsQmx5NWR4VGtCOHliWWQ1cWl5WW5BQnFNNVpJN1FFNUhhczNCaV9uTlhGQWlLRHVkNUZlUTFjV3ZxV0Uwak5fSHpNQTlrMEFiNllDMGFZcWF3ak9RbjRIUUNhdjVxSU1aazRseHBfbkNrS0hjUHZ6cFpFZ1N0SWlEVHdCUEpNaVcwa0dfTk5mQzZxbEZaTnRSN3RxZ1d1Wi1wRmJfaTNtSWdDZklwU3c?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxOVTFsRk1FOHJWVm5rN1c2Y19EMWVrRjJUOWRqYlZobUZhaFdxSDd2ejlmQ1hXWjZOSnFmUUxLQVdZaW11MUR4eUw2b1d2M1l0eWI1M2NYbDdwTGd1R0Z6OGdzcDBUZEVUTTVqVGtCOU1SaUhHdjFuOV96VGNZV0M4UjhZaHJPeDVGOEw3R1pXTDBhN09LNkl2TmNWZkVUM1JNRXJPT3VPRHdXU2daaXFyX3ozMW9LRU0tYWJLZFNtaHcyQQ?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxObGw4Q0FJQjBUelJLYlBiOUhOSnlPOVpoNG9xU0p2YU82bTZwQkRBdndHalJlUWFrdkNKVjN3emMzLTlvV2wyazJ5SDVBU1FOR2E2cnVCT0hhQ2tqb0lVNzk1NFExWUE4VmNKdnY2TFNYcXZmTUlMTkVZLTI5YTNCb1JsaTUwaUV5R241UFZNajNTM1FEUGg4SUpqd3N0NFFneEhvSURwWHh1SEk?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxOUF95TFhmN2dTajBJdXZwaXQxczVwOXVIUG03bWVzRFNDLXhXWFh5dFNLVVFpTnJQdVQtVFdKWUUybHh5dmtoUXJ3eVJoTVpRNDU5QkRPUnozMHBSUUhwZDNSTldwdDdCc1pfbHBmTlVEWHZKNUpNYURrcU8xeGlSakViZXFwVlZZakF2eVM0R1hqV05kZXdtdEctNGt6akhwSUhWTFMyRzYyRVQ3ZTE1dUtHd2VqOVE5Q1laRHBZMFM?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxNWFdsOEgtTXh6am5DOEZDZDhYeHhBTFpQVjBicW9mS18tTWljQUt1Rk9VV1pmSldqX1Zlc2k5M0dibl91UlNLRHBvcHpucW9rOG1qRVZweVlmbmVkUzRvaFlpMUp6VDNiOFNHTEh6VDdnNC1LMmswWXByN2xnbG5vSVpEYXdjN3BxMV84OUt1Uk1CUlZUSm12OFlpd1B4Q3RqTVFYOEIxaVdLMW1SNVAtQzh5ajNZWmhSc1NtbEdiNEJkUGgtY3ItNkhINnZVNjJTZzFKdVBIWi0yZw?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxQN05SbThuc2dURTRDSTNRUF9IX0JGcE5wT3d0bkJzakZaYVhzRVYtVVRpc2thVTRZOGZpMmc2VldpQzZ1eEh4Q3U1U1dHSG1rUVdDR3F0aDhJZXZ6SE1remctNTdramUxelRGbmZGX0V5aFpjNThvQ3Q3VDZJb0p1alZWYUdHWUNJdGlMS2txckpoMkxxelhPalNLSzRKVGJEcUYwZEtkcFl2OFUzMzVLVjgydHUzNjJQdVVCenprUlQtQlhPRDY3M0NabkdBa0hzSXpNdw?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxQVkRHZXZvWklQYnM3SFd1VXlUTUpuRlk2OVA2VEU4RDgxdmpTeWM2V0tIQ2xDVkdDZmFvWXh2RzdsVVNqOG5iYjJYbzlrYml5U0NQbTFhdGJSMTZ2NWtrZkMzZGhVenVWbW5fMV9aaTFyMjVxWnNic29lWjUwYl9YN0pzVWduTFlGc1MxRVlfTUtXTXAtSG1POVRIMFBzV20zMGpFc1FNLVhRUnlUSS1jdTdTMklyX1dmT3RyNWpLTFFDT1pHallTS1U0OHplakJ5OWc?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxPOHpKM3k4UWNxLXdtUDFkQjVGd1F0ejBWOTlweUwwMnMtTGl2dWs3d1drU0s4UERlbW1XdlNQX0gxcXFzdEVNR2lFa1JTTGNWdi1VZDAtXzdGMXhRWUlzTkJ5YXN5WjBERC0wbUU0MzVka3oxM1ZjdWctamJ2eDRoTFBLcGgyQVE0RXh5SGU4MUJyRVE4NmNFLTltOThoNmt0bVR3blFiSkVfN1dWRFlKb25zaUE1bkR0?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxNX184T1YzY0pSc29zeDVmcFgzaDYyT0hFcTNMNXFFcDMtOVVLNEh1bGhMU3JZRV9kTVhJSV9QTWVKRndkaHpTUXZuak1NdUZDZS1ITGVPemd4RzRSa2E1ODlvVUxFb0Z4bTRGNkdfOW1zNFlBWWhna2NocWJkQTRWY2E4OExYb3hIUk5jVERlWFFvbHlaUG1YZjV1SGhKQlVkN0s2S2VvWVpTZEpoX2NtQlZjWXA?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxQTkJMNE9uWENURzJjM1g3OVFfY01Cc3pOYUItckFDZWo5TFRKSE9KVThPOU5KLWlfSnNTV1NPYmJyb3dUSVJuRUYtTGVEdEFDS0JoWnA1ZUtoWC15N0praV9jTWZlb3ZmT3l2Q3R5MGNaSFc5WWljWWJNa3RQVGNpbUEzeFAtZnlpcHRPRmlOWWtPTTRXaDdmSE9seUlGUG9BLWpzNw?oc=5
- https://news.google.com/rss/articles/CBMi-gFBVV95cUxOVnR0cVdKZFd4dUphRjl2Wkp4QkVDczZJUGVhQTdmb0JPVFZyU2VBX0I2R2tzTUZmYVE1VGFHLWxxVHRSd2kzejg5UWQ3ZVpzX1RIVE85bGxiRjNnYUJFdUtsN2dFRGNNdjVpVXR0ZGs0bzZQeHppdGtYSnQwMDhfWkg4NnNvOE91dmNwWWE5bXljbjdUN2ptcjRvdU9ORGNhWjlVaDdMSnNmcjNqYVBxdUlyOFUtZEFFWnhGUkhjTUpKNnpsRkZYY0RkandTcnZ0aGRUZk1RY01XRlhDM2dhRHZ6QnNHV3d2OEMxSUF1Vjk0WFdWSlN0REtn?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
