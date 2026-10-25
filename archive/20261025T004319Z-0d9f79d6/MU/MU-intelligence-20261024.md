# MU Intelligence Report

- ticker: **MU**
- Report as_of: **2026-10-24**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/MU/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MU/key-statistics/
- AI analysis snapshot as_of: **2026-10-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-25T01:18:11.595294+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 1, 'ai': 9, 'unknown': 0, 'irrelevant': 12})
- AI model(s) actually used: **openai/gpt-oss-20b**
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 8 named publishers; 3 exact duplicates; 22 HTTPS source links; largest publisher share 59.09%; oldest publication 2026-10-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 877.5500 |
| Return 1D (%) | 2.4589 |
| Return 1W (%) | -0.1468 |
| Return 1M (%) | -18.1169 |
| Return YTD (%) | 207.6949 |
| Return 1Y (%) | 325.0141 |
| Annualized volatility (%) | 81.4133 |
| Beta vs SPY | 3.3658 |
| Max drawdown (%) | -39.0954 |
| Sharpe (rf=0) | 2.1890 |
| Downside deviation (rf=0, %) | 48.9009 |
| Sortino (rf=0) | 3.6444 |
| Historical VaR 95% (1D, %) | 7.0055 |
| Historical ES 95% (1D, %) | 9.5345 |
| Correlation vs SPY | 0.5270 |
| Tracking error vs SPY (%) | 75.4775 |
| P/E (trailing) | 11.81 |
| P/B | 7.17 |
| EV/EBITDA | 8.77 |
| Revenue growth (%) | 379.30 |
| Forward P/E (estimate) | 4.24 |
| Gross margin (%) | 80.72 |
| Operating margin (%) | 80.68 |
| Return on equity (%) | 88.26 |
| Free cash flow yield (%) | 2.93 |
| MA50 | 982.5951 |
| Close vs MA50 (%) | -10.6906 |
| MA200 | 731.8925 |
| Close vs MA200 (%) | 19.9015 |
| RSI (14, Wilder) | 38.1774 |
| MACD (12,26) | -35.3737 |
| MACD signal (9) | -18.3192 |
| MACD histogram | -17.0545 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MU': 267, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 877.5500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.4589 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.1468 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -18.1169 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 207.6949 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 325.0141 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 81.4133 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 48.9009 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 3.6444 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 7.0055 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 9.5345 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5270 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 75.4775 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.3658 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -39.0954 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 2.1890 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 4.2415 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 80.7160 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 80.6780 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 88.2600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.9349 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 11.8061 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 38.1774 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -17.0545 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -10.6906 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 19.9015 -> Clearly above the moving-average trend level.

## TAILWINDS

### Micron leads memory stock rebound candidates after sharp selloff
- Summary: Micron's strong position in memory stocks may drive a rebound after recent selloff.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxOMV81S05Vc2lFdTl0Tno0RlFDbFJBYTZJOTZMSHlNQ0VfSlZEZExzMkhrX1NydlhkUHE4UV9jb2NRUG01Y2F1Z1JTSnZmWmhuaG9WTTltMFZjeElrTk82Y0N6T0VIa1ZPcnFJa29TSklGRkZDQzFlelJubUswbDBVTjNYZlpYaG5VNTM0d1FCeHNRYzBYVEV1VnNEbFRwdzhlRWw4Y0xHUm8tbnVNQ0pUVldQMGhndHZod1lUYU1IbGMwbV9h?oc=5>

### Micron’s Taiwan Unit Reached a Deal With the Taichung Union. Here’s What to Know.
- Summary: Micron’s Taiwan unit finalized a labor agreement with the Taichung Union, potentially improving workforce stability and operational efficiency.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNNVd3V3FmWXh1R28xWTN4T21iT1JUWGRCaG1UT1lzZHYtM3FBejhyd0ZPMmVZQzVZQ2x1eUJNR0h2Q2RiMk1qQ3ZlbFM4VGxlNDltWkp5a1I5YmYtMlpST0I3Ums3RndmemowSndyd2pBaVZBX3NIZURZdmRFamU2TW9EWHFxUUlZSFNaWk93TTlJMmc0QXhQVU5ZSnM?oc=5>

### Micron Is Up 221% in 2026 and Seagate Is Up 155%: Take Profits, or Hold On for the Ride?
- Summary: Micron’s stock surged 221% in 2026, indicating strong investor confidence and potential upside.
- Date: 2026-10-21 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPMXBJbEtncUUybHhIV0FmYjQtV0JzaEwyOXhxV1N6eVhma0FtakplY19KdkFQZkNaWUwycXVJZmg2TXdaNkFET1hVcklRcDBUYWt4STNFcHJHN0wtUU41aGdBU05YVm5pNk9LRXdjb3c4amN1N012c01kaW56MTVOdVBFQkl0d0o4MEJaVndKdk1SQjYxVFp3?oc=5>

## HEADWINDS

### Micron Technology (MU) Stock Is Down 24% From Its Peak. History Says $10,000 Invested Right Now Could Be Worth This Much by 2030
- Summary: Micron Technology (MU) Stock Is Down 24% From Its Peak. History Says $10,000 Invested Right Now Could Be Worth This Much by 2030
- Date: 2026-10-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNNGROMk1zSFJob2UzMTZxY3VMY255UklfZnlDejZnZDVxMGZJbGUwUnhxM3dzTEVjMlY3aGhEM2RFb2RZOWNMOXRrVFY0dllCQ3pfT21WZTB6NTZnQnBkbktGQkUyaEJ0c2hPT1pVWjV3TkpwOHZibXNzLU9FQk93OV9JU3B0MjRjdzd2ME51cmRhQXlUQ3gwOFRmMUM?oc=5>

### Micron (MU) Falls More Steeply Than Broader Market: What Investors Need to Know
- Summary: Micron’s decline outpaced the broader market, signaling potential downside risk for investors.
- Date: 2026-10-22 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQajkybmNzZ3ZoWFlBRkVmdHBON0ZXUzZ6d2l2bkJ0REU3S01TS0F3MDNLaERyRWhwTmtCTkV2ampCOUtFdlJySlRsWndic3J5NFFuZDJKdTRuYnhWYUxWLUZxeVoxNGYtRTUyS0FKV2FoNEx2LUwtazI2MWNXWEtuSnhZM185S2h3YVBUQ29jZVlwSUZ5MmlkTg?oc=5>

## CATALYSTS

### 3 big reasons Micron and other chip stocks fell hard on Thursday
- Summary: Micron stock fell sharply due to market-wide chip sell‑off, citing supply concerns and weak earnings outlook.
- Date: 2026-10-22 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQOGZPNEpMdnlfTHU5OFFIbXZBM0VtWlJyWWhJTDNHWWRoUlBWLTdSR28zOXFrOU9GNG1Db2VhQ1VNVEZweFFJYlEtZTVnUTduQkR2bkRRdWJVQnhEZ3FzS3B5cTJ2c05tRTNLOExzY3BuVHV0MW9aRUlqMVhUTHExcDJHUkppaXloLVZta0hNMjhrSy1vOURaM3E3WUZaVENCRFRYamY5a1dYNHdNUTFYQw?oc=5>

### Why Micron Stock Dropped on Thursday
- Summary: Micron shares declined amid broader chip sector downturn and investor worries over future demand.
- Date: 2026-10-22 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPNUJTTHZMRXZtaXhGU3pzdjhvek43SkFTb3VGVjhfMVhpV3ZXdDdkZTZ0LUFnUWRXQXRlYTNEb1RNSlc2R2ozNmw5ZkZoWGt4bkNwSldmTlg5R0NHVl9faWlPTkFCYklrTDh4WHpPQnRJOHlCQkNXczN1R2Z2ejNLRmstTWVZbWlTbU10RHlwelcwZW9RNUxmUDZ3cFJCNEE?oc=5>

### Micron stock gets stunning $3,000 call despite 6% plunge
- Summary: Micron shares fell 6% but still hit a $3,000 target, reflecting mixed investor sentiment.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxObloxQW9TSXVqOFExT2w5akpqeWNBTkJlbm5NdTdPbkFRV3cxbC1UenB3ak9vYS0wUnQ2bUt2NHd0RTZHaWZ1TmwxZnQ3dkMtQ1NIU3JsSXFuNmpaVkhqWERISTFScGFHRWt1WHU2NG91bHFCdjM1Q0tSUHpzR0N0bWFjaTFuMm9vOHoyNmwwVXdzQUZuQnJsSkpnOWJUZw?oc=5>

### Micron (MU) Stock Looks Fully Valued After A Critical Minerals Deal
- Summary: Critical minerals deal could boost Micron's supply chain and valuation.
- Date: 2026-10-22 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNUEdGRmdiWk0xMkVvSG9zT1ZZWVBMR0JQNUt6Vkk2OXpIVjRFeWVrTXdCSm9DT0lWQXluSnhtaXhYR0ZVbXR4NUNLclluWnRGTVVodkJnWGUyQnNiTFRMZVZOaTN0TXhGU1AzQ0Z4dWZ1Y1o4dTFIWVRHcVVQZVZZWmVsZkZsOW9rSVRxS20zckxIekI1VmtJ?oc=5>

### Stock Split Watch: Is Micron Next?
- Summary: Potential stock split may increase liquidity and attract investors.
- Date: 2026-10-23 | Impact: low | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMigAFBVV95cUxNdUxMSlJOQWRGYWR2RnFwZ0RWZUVhdW5LR0ZpYlFOenVpQ0lsYjN2dHhTTG9hR3Z5NFliMnlvNmJPbHJ6OHhLV254andDMnBTQjNma19XUm1FakJwcml2Y0lrTnhmTzhZVTludXk4ZGlxY2VuWDRYTlAyVTZaLTl4Uw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MU** | **11.81** | **7.17** | **8.77** | **379.30** | **992,880,427,008.00 USD** | **325.01** |
| WDC | 12.09 | 13.46 | 19.84 | 55.50 | 128,643,678,208.00 USD | 173.87 |
| STX | 45.36 | 65.99 | 32.23 | 48.50 | 143,369,011,200.00 USD | 180.11 |
| NXPI | 20.06 | 5.20 | 13.29 | 19.50 | 59,238,408,192.00 USD | 8.31 |

Peers fetched as_of: 2026-10-24; MU reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-30
- Next expected earnings: 2026-12-23 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-24

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-10-09
- Revenue (latest available single quarter): 8,440,000,000.00 USD; period 2018-06-01/2018-08-30; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 28,243,000,000.00 USD; period 2026-02-27/2026-05-28; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/723125/000072312526000023/mu-20260903.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMixAFBVV95cUxOMV81S05Vc2lFdTl0Tno0RlFDbFJBYTZJOTZMSHlNQ0VfSlZEZExzMkhrX1NydlhkUHE4UV9jb2NRUG01Y2F1Z1JTSnZmWmhuaG9WTTltMFZjeElrTk82Y0N6T0VIa1ZPcnFJa29TSklGRkZDQzFlelJubUswbDBVTjNYZlpYaG5VNTM0d1FCeHNRYzBYVEV1VnNEbFRwdzhlRWw4Y0xHUm8tbnVNQ0pUVldQMGhndHZod1lUYU1IbGMwbV9h?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNNVd3V3FmWXh1R28xWTN4T21iT1JUWGRCaG1UT1lzZHYtM3FBejhyd0ZPMmVZQzVZQ2x1eUJNR0h2Q2RiMk1qQ3ZlbFM4VGxlNDltWkp5a1I5YmYtMlpST0I3Ums3RndmemowSndyd2pBaVZBX3NIZURZdmRFamU2TW9EWHFxUUlZSFNaWk93TTlJMmc0QXhQVU5ZSnM?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPMXBJbEtncUUybHhIV0FmYjQtV0JzaEwyOXhxV1N6eVhma0FtakplY19KdkFQZkNaWUwycXVJZmg2TXdaNkFET1hVcklRcDBUYWt4STNFcHJHN0wtUU41aGdBU05YVm5pNk9LRXdjb3c4amN1N012c01kaW56MTVOdVBFQkl0d0o4MEJaVndKdk1SQjYxVFp3?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNNGROMk1zSFJob2UzMTZxY3VMY255UklfZnlDejZnZDVxMGZJbGUwUnhxM3dzTEVjMlY3aGhEM2RFb2RZOWNMOXRrVFY0dllCQ3pfT21WZTB6NTZnQnBkbktGQkUyaEJ0c2hPT1pVWjV3TkpwOHZibXNzLU9FQk93OV9JU3B0MjRjdzd2ME51cmRhQXlUQ3gwOFRmMUM?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQajkybmNzZ3ZoWFlBRkVmdHBON0ZXUzZ6d2l2bkJ0REU3S01TS0F3MDNLaERyRWhwTmtCTkV2ampCOUtFdlJySlRsWndic3J5NFFuZDJKdTRuYnhWYUxWLUZxeVoxNGYtRTUyS0FKV2FoNEx2LUwtazI2MWNXWEtuSnhZM185S2h3YVBUQ29jZVlwSUZ5MmlkTg?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxQOGZPNEpMdnlfTHU5OFFIbXZBM0VtWlJyWWhJTDNHWWRoUlBWLTdSR28zOXFrOU9GNG1Db2VhQ1VNVEZweFFJYlEtZTVnUTduQkR2bkRRdWJVQnhEZ3FzS3B5cTJ2c05tRTNLOExzY3BuVHV0MW9aRUlqMVhUTHExcDJHUkppaXloLVZta0hNMjhrSy1vOURaM3E3WUZaVENCRFRYamY5a1dYNHdNUTFYQw?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPNUJTTHZMRXZtaXhGU3pzdjhvek43SkFTb3VGVjhfMVhpV3ZXdDdkZTZ0LUFnUWRXQXRlYTNEb1RNSlc2R2ozNmw5ZkZoWGt4bkNwSldmTlg5R0NHVl9faWlPTkFCYklrTDh4WHpPQnRJOHlCQkNXczN1R2Z2ejNLRmstTWVZbWlTbU10RHlwelcwZW9RNUxmUDZ3cFJCNEE?oc=5
- https://news.google.com/rss/articles/CBMihgFBVV95cUxQOVI4dmd6RkFUUTZ6SHp3RGlSMjN0OGhFcGhWQUZRMXhoSVNpeS1sM09wN3pUbHRWaTAtN1N3V1RxcGRhOTFRVi1JOXFwYS1tbEJhaFRwbF85ejUxQ3g3TzAtcjVrR25zUzJ4ZmpOeFc0S1VpQjVuRnJHSkVlNWl0OUZ6VG4zUQ?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxObloxQW9TSXVqOFExT2w5akpqeWNBTkJlbm5NdTdPbkFRV3cxbC1UenB3ak9vYS0wUnQ2bUt2NHd0RTZHaWZ1TmwxZnQ3dkMtQ1NIU3JsSXFuNmpaVkhqWERISTFScGFHRWt1WHU2NG91bHFCdjM1Q0tSUHpzR0N0bWFjaTFuMm9vOHoyNmwwVXdzQUZuQnJsSkpnOWJUZw?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNUEdGRmdiWk0xMkVvSG9zT1ZZWVBMR0JQNUt6Vkk2OXpIVjRFeWVrTXdCSm9DT0lWQXluSnhtaXhYR0ZVbXR4NUNLclluWnRGTVVodkJnWGUyQnNiTFRMZVZOaTN0TXhGU1AzQ0Z4dWZ1Y1o4dTFIWVRHcVVQZVZZWmVsZkZsOW9rSVRxS20zckxIekI1VmtJ?oc=5
- https://news.google.com/rss/articles/CBMigAFBVV95cUxNdUxMSlJOQWRGYWR2RnFwZ0RWZUVhdW5LR0ZpYlFOenVpQ0lsYjN2dHhTTG9hR3Z5NFliMnlvNmJPbHJ6OHhLV254andDMnBTQjNma19XUm1FakJwcml2Y0lrTnhmTzhZVTludXk4ZGlxY2VuWDRYTlAyVTZaLTl4Uw?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNNEJqTE9aVU8yN2w5QTJOUWtqc1JPQ184V2VVTUQtenJ0MlJaOGN3S2lYUTNHaEk1VGhmUGFOVHhrTkpFb0lwd1JnUkZZMFFfN2pVdHNaem1zcnNNblVlaHRkOVI3dGZFVUlwaUJFYzRISWtnZUJLcjNxbGE2T1RkVTB1WHM5b0l5Sk91eTFoU3BhYjYxR3lfcXZ3?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
