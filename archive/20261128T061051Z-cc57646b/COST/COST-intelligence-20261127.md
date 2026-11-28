# COST Intelligence Report

- ticker: **COST**
- Report as_of: **2026-11-27**
- Market data as_of: **2026-11-27**
- Quant sources: https://finance.yahoo.com/quote/COST/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/COST/key-statistics/
- AI analysis snapshot as_of: **2026-11-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-28T06:18:52.287193+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 6, 'ai': 10, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261127T063646Z-c0c26981/COST** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 15 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-11-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 1097.8101 |
| Return 1D (%) | 1.0121 |
| Return 1W (%) | 2.4044 |
| Return 1M (%) | 13.9284 |
| Return YTD (%) | 31.6542 |
| Return 1Y (%) | 24.9980 |
| Annualized volatility (%) | 20.3577 |
| Beta vs SPY | -0.1633 |
| Max drawdown (%) | -18.1993 |
| Sharpe (rf=0) | 1.1777 |
| Downside deviation (rf=0, %) | 13.6200 |
| Sortino (rf=0) | 1.7603 |
| Historical VaR 95% (1D, %) | 2.0836 |
| Historical ES 95% (1D, %) | 2.7374 |
| Correlation vs SPY | -0.1205 |
| Tracking error vs SPY (%) | 26.7171 |
| P/E (trailing) | 52.88 |
| P/B | 13.59 |
| EV/EBITDA | 33.51 |
| Revenue growth (%) | 11.10 |
| Forward P/E (estimate) | 43.84 |
| Gross margin (%) | 12.77 |
| Operating margin (%) | 3.80 |
| Return on equity (%) | 28.40 |
| Free cash flow yield (%) | 1.39 |
| MA50 | 975.6472 |
| Close vs MA50 (%) | 12.5212 |
| MA200 | 952.2892 |
| Close vs MA200 (%) | 15.2812 |
| RSI (14, Wilder) | 72.4453 |
| MACD (12,26) | 32.4009 |
| MACD signal (9) | 32.5565 |
| MACD histogram | -0.1557 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'COST': 291, 'SPY': 291}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 1097.8101 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.0121 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.4044 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 13.9284 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 31.6542 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 24.9980 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 20.3577 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 13.6200 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.7603 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0836 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.7374 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1205 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.7171 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1633 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -18.1993 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1777 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 43.8362 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 12.7660 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 3.7970 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 28.4020 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.3881 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 52.8810 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 72.4453 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.1557 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 12.5212 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 15.2812 -> Clearly above the moving-average trend level.

## TAILWINDS

### Costco Wholesale (NASDAQ:COST) Stock Jumps 1% - Still a Buy?
- Summary: Costco Wholesale (NASDAQ:COST) Stock Jumps 1% - Still a Buy?
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxQNUpvT1E4Wnk2MnJZbGFIeGVtLTM4ZmcxSkFGWnNTTFZlVG5PSTZWZEJoS2hMekNJQ0pDcVFLNzhRQ2xiN2FqRWNReVVPbjNmYzdjOUFoOG1HdXVuV1Z5QkRTWm9SYlpMTmsyRkhYZ2xuMGpscmZkckRZdVpwSTZjLWtSelVWcjE1V3d5N2d5UnBqQTQwX2h1V1NYWjVJMzJSbjlmR19idllJcE90SmlHSDNXckc?oc=5>

## HEADWINDS

### Costco stock edges lower as inflation adds risk to interest rate outlook
- Summary: Costco stock edges lower as inflation adds risk to interest rate outlook
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxNUl9hbXVSSnBMcFlNR3BMengxejMwSUpmYll5Mkh4TEctb1VOSFZJX2tURDEzV1FTQi1sOW1mNFhkTWR1bDRKVXpvUFQyaG9oODZQWllRZTdhWnlKVFJTUEtVZWRuT0JjTjhtYkdzTUdVTHVac2dLalgtandCWGdqbDBpSHRtMk50?oc=5>

### Costco share price slips while investors weigh effects of special dividend on capital return sentiment
- Summary: Costco share price slips while investors weigh effects of special dividend on capital return sentiment
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNZDE3eXY3WWJseGp6UEZfM3E5ZEhvX2ZfaVZJVEtQNFVQTzV3UDkyaGNGWWNPV2dsU1B3S00wWm5WSjZvdTFwbEZpQTNEU1l2YllSWmowZF80QTN3WkxpUTNyUnkxdlVOQk9PdmI3S09ERWxrVkVlS3o4OUdWUXU3TU5pb2ZFaG5pVS1Z?oc=5>

### Costco Wholesale (COST) Options Flow Turns Bearish: A Smart-Money Check on the Stock, Nov 20
- Summary: Bearish options flow suggests negative sentiment toward Costco stock.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxPX2Rwd0c3M29jTmN3NGNpWUFJbmxOdkpoU2pkMDZiV1phTVpROENBZUJLMDdBcThyN0VZUEwxdlN2MFIyMHNPSDF6X0RTMzE4c0dqMDdOWWRMZHFSdVZ3cXpOMkEtZWZMNGJZZEx1OEJBNlR6NTE1Sllwcmw4LXFWbWgtd2NnemdOR3VtZ1JUOTNHd1RQT2M5SUlwS2xiVG9rNHlWR01GYTNjdUg1c2d5UTVZRE5HZ0U?oc=5>

## CATALYSTS

### Costco Hasn't Split Its Stock Since 2000. Here's Why 2027 Could Be the Year.
- Summary: Costco Hasn't Split Its Stock Since 2000. Here's Why 2027 Could Be the Year.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxOZVlsSnhuTWFlV0hwclBxbFRPbkVlcVlyVk9hb1E2bkVsTEs2SDdwMHhqWUUwZXI5WDB6cVlyY1FTX2xLQ3Jvd0hnNGRIZHI2eU5aYXR1cHNMbTV4U25BdWJ1NnNycE9rZGxMNFFMQTQ0LXdWNVEta1NXSlkwM1c2UUNIeE5Wdkp4ZjBvX3Y5T3Z2LUVhcFZEc0Y4amVvSjJvUzdxQVFsekVWd2hoVlRhWk5aWGxjZUtz?oc=5>

### Costco (COST) Lifts Dividend After Strong 2026 Results And $7.5 Billion 2027 Plan
- Summary: Costco (COST) Lifts Dividend After Strong 2026 Results And $7.5 Billion 2027 Plan
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQaldob3FsZloyeUJwWGFqekxrWkVVX2pFM1ZiNjdaX0ZKTXo1Rzl2c1kzRzNrM013RzdrOUVIV1NBeVJ6MHlHT3ZqdGE1ejhBdS1zU2lhbHlsOTR3bXg3aUxHZW9zOGs0YzRfTWxHeS1kX2pFZWE2OGVhSHFSNkhKMTUyTDBJQkVObFdiVjVIbHd3ZlZpVEJLemlJeG53N2s?oc=5>

### Costco Absorbs Its $30 Special Dividend and Stays Near Records, With $1,090.46 Next
- Summary: Costco Absorbs Its $30 Special Dividend and Stays Near Records, With $1,090.46 Next
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi-AFBVV95cUxNM2VFY0dIRVcxdVhpdFpHRV9JWXZDUnI1U3NyYUEwVkFFUlJ5ZDN5M3NfakpQdU1MOWYtSmNNWXBOREY0Qi0wTllXdWgzZVBHX0JRa0M0SENxOUxaYlZwdTJ5N2ZrcHRYUFpEaFJFSmhxbGhJVVhVX3kwcUNoZ3ZER0RfSnEwYTFKbnNoLUZsbGJoeUwzanY2cHFWU3BzNWpXd0NiUFg5X212TFNkMDItTjlBYVZxSzRPd2FqcjRVNlJyM1EyZ19YSDVNUUY3WHJkUkEwUW5Oa0RWSUhVOHk2WUpMVmtXcVd0ekpjeTRQTDdEdW1QdG8zag?oc=5>

### What Happens To Costco Stock If Its Cash Pile Runs Down?
- Summary: Analyzes potential price impact of cash depletion.
- Date: 2026-11-24 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxQdE44SDRNZ19hUGp2ckZ5VjJwTGZkOHVSR203WGZwUFhLWUp5ZVQ0NzBSc3EzWTQtVU9vLTFoLTN1ajJrTE91MkkwYXNjQmpvM3ZGNTlnX1J5Q2d2TGp4RU5sdVl0SklxV0pzOW9SRmkwN2dzUUZENnhqYVVieWJNX1Fib2owOUF1S0NSRl9SWmo1RVE1QUtSNlhxcWRTaXJENVQ4RW5UUk9GUzNKbG5GbzNMTGNEVlk?oc=5>

### Why is Costco Wholesale stock climbing today?
- Summary: Explains factors behind today's price rise.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxQZFBLVEpPdDJ6ZlhBczUydzZvUWFaMVctWVJLN29tS1BBRHY3T1BrblNZUVRPcEhtUTBpT3pfOE5sSENSbmsyQWZ4TlVkU0V1dHhUcVR4bzNUVXZCaWJkTV9jb2s3MDRGZGdkcTZGUkxoYkdEWmhUQU5MQm5ybHdQZTBZSUliV2xQblhNOC14eUJ1NXh6NUI5MTRlS2lIeld1T0hRdUUxYjhZdw?oc=5>

### Costco Wholesale (COST) Could Be 27% Overvalued After Its $30 Special Dividend
- Summary: Highlights overvaluation risk post-special dividend.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPekNEZ3lzY0RJTDRta3FyTm9lajJXSnl6eUNDZlo2YzNxbGc4ckV4Ymt3U1c2b0gxVUh2VTBMaThLaHZGdU1FbHVubG1Kb19Gd0lvN3U2b2VoUnFxdnphTjViandrNEQ5T01JZTRKeXlMSjZCNGNFRkRxdGZ5SURReWlwRkJTNVZlSlpCU0cwR3U5V2c5WlhNSDdGQQ?oc=5>

### Costco Wholesale Corporation (COST) Is a Trending Stock: Facts to Know Before Betting on It
- Summary: Provides general info for potential investors.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxNRnYzc2pVVUVaSEd0ek5wY3duY2EtbXJ6enE3SnhkZ0tJclNVUGZaekpxWXZnR2NIVkNCUW5RN003MV9hMDhFYUxXeVlYZTJlNlpMbVpLTVM1Z1ZCOTNqNEF0YXNuajQwLVN2SVdhQTlScUVvREVPVmxPTWVUYnBrYXc4OUpsOFBZdXlyZzJxaTlnUUpDQl9oTm13NC1WdVJ5T1RGd0J6dktjeHM?oc=5>

### What's Going on with Costco Shares on Friday?
- Summary: Analysts discuss potential short-term price movement for Costco shares.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxONmNEVDZFWXVmYWlkOHpmc1VSMFRtNlVwdlRSSGxvcGFxVnVrZzhaMnpHcmphM21RRjRyQ3U2YnhvdzAyeEVtYnRLSVVWeTFlU3AyT19kNmxqaFFiVk5wNXZjVkdUaFhEZVd0LW9sYXZMR25seUlwdDFPYTViNk5keDNLTDEyY0xUNG5adml3NEVkTHBicklzcXZsYWFScDl6cTFV?oc=5>

### Costco (COST) Rises Yet Lags Behind Market: Some Facts Worth Knowing
- Summary: Costco’s share price increased but remains below overall market gains.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigAFBVV95cUxNU2ZSQWl5THpqSVoxNWNvMjNvbFhHcVA2bWFFZ3FoRkNiVlE4QWVCNkdpSlc1Q2RmbmxTUkQtQl9vTUhCc2tEanlJRlBCM2JQT2pjYmc1SWJhbFc4U0EwZk9OenpxVDMtWThSOVB6SWxVSGp6bnprUUd4TWFpMF9rag?oc=5>

## RISKS

### Costco Wholesale (NASDAQ: COST) stock price forecast: Wall Street weighs valuation risks
- Summary: Wall Street analysts highlight valuation concerns for Costco stock.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxNVlN1YlRDRWNDNzc3OVhrU3JYR2xFYjdSOHdleDlRcDZRbGZGQ3R6cW5yYXdsTEtEbzJWMWRZMFdNc0h3dDc0RlBLZTkxb3FSRVloOEZEQWZaYkVQZVdvT2VjVkFDRFdqR0ZPSDl2bWRmbk0wQ2RBZXhhN2N6SE0tRUxWTXFockgzVDVmNTNBNnRzbXc?oc=5>

### Will Costco Do a Stock Split Before the End of 2026?
- Summary: Speculation about a potential stock split by Costco before 2026.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxOZ2NuQTRMd3FVRXB2OTJ4M0FlejNIUC0ycGhVTjlTaHZPQXFCYkJnVXRhRGVIdGIxV3IxZExEOWZEYjJYUWI2TGZudEcwRTZJTVNRcENjdHFSdEJEWE5ZY0NTbk5PTEJkeG9valdzcXZGOVBZV2tKZm16Rk1sOVN3MXFrSXl2NWZXRVFqZWpOWG8xQlhPamQ4blF3eXp1bUdOdW14WWVsWUEtZDYweC1vQ3Z6OE9pN184VmJVem9iMDZmNnRmeHFqblZQbm41WmtmRlE?oc=5>

### 12 Big Funds Bought Costco Wholesale Last Quarter, While 7 Sold. Who’s Right?
- Summary: Large funds’ buying and selling activity in Costco shares last quarter.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxNRmJSekZTQkdueHp4RTJrMWd4WnAwdEVMQ2ZpVnpkaV85aVZRQUN6ZW5wZHo2WDcweDhwVVBJdXZhT29rUlVmTFAwc2VZUkladmEtYWNHdzVQYnBRMWduZVJjbVJVV3FCaVhmWGhTbDJmcC1HZUstQURzaEhWZkg2b0dFMFlObDdNdkxpZGdKcGhiSmRDaHcwTnEwQkZZelJB?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **COST** | **52.88** | **13.59** | **33.51** | **11.10** | **486,471,860,224.00 USD** | **25.00** |
| WMT | 48.24 | 10.76 | 23.21 | 5.20 | 1,059,459,104,768.00 USD | 23.05 |
| TGT | 15.98 | 4.24 | 10.43 | 7.10 | 77,858,070,528.00 USD | 98.16 |
| BJ | 21.99 | 5.78 | 14.97 | 17.50 | 12,693,111,808.00 USD | 10.73 |

Peers fetched as_of: 2026-11-27; COST reuses existing data (market data as_of: 2026-11-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-24
- Next expected earnings: 2026-12-10 (yfinance; expected dates may change)

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
- Filing date: 2026-10-07
- Revenue (latest available single quarter): 69,597,000,000.00 USD; period 2025-11-24/2026-02-15; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): 2,192,000,000.00 USD; period 2026-02-16/2026-05-10; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/909832/000090983226000093/cost-20260830.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMitAFBVV95cUxQNUpvT1E4Wnk2MnJZbGFIeGVtLTM4ZmcxSkFGWnNTTFZlVG5PSTZWZEJoS2hMekNJQ0pDcVFLNzhRQ2xiN2FqRWNReVVPbjNmYzdjOUFoOG1HdXVuV1Z5QkRTWm9SYlpMTmsyRkhYZ2xuMGpscmZkckRZdVpwSTZjLWtSelVWcjE1V3d5N2d5UnBqQTQwX2h1V1NYWjVJMzJSbjlmR19idllJcE90SmlHSDNXckc?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxNUl9hbXVSSnBMcFlNR3BMengxejMwSUpmYll5Mkh4TEctb1VOSFZJX2tURDEzV1FTQi1sOW1mNFhkTWR1bDRKVXpvUFQyaG9oODZQWllRZTdhWnlKVFJTUEtVZWRuT0JjTjhtYkdzTUdVTHVac2dLalgtandCWGdqbDBpSHRtMk50?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNZDE3eXY3WWJseGp6UEZfM3E5ZEhvX2ZfaVZJVEtQNFVQTzV3UDkyaGNGWWNPV2dsU1B3S00wWm5WSjZvdTFwbEZpQTNEU1l2YllSWmowZF80QTN3WkxpUTNyUnkxdlVOQk9PdmI3S09ERWxrVkVlS3o4OUdWUXU3TU5pb2ZFaG5pVS1Z?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxPX2Rwd0c3M29jTmN3NGNpWUFJbmxOdkpoU2pkMDZiV1phTVpROENBZUJLMDdBcThyN0VZUEwxdlN2MFIyMHNPSDF6X0RTMzE4c0dqMDdOWWRMZHFSdVZ3cXpOMkEtZWZMNGJZZEx1OEJBNlR6NTE1Sllwcmw4LXFWbWgtd2NnemdOR3VtZ1JUOTNHd1RQT2M5SUlwS2xiVG9rNHlWR01GYTNjdUg1c2d5UTVZRE5HZ0U?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxOZVlsSnhuTWFlV0hwclBxbFRPbkVlcVlyVk9hb1E2bkVsTEs2SDdwMHhqWUUwZXI5WDB6cVlyY1FTX2xLQ3Jvd0hnNGRIZHI2eU5aYXR1cHNMbTV4U25BdWJ1NnNycE9rZGxMNFFMQTQ0LXdWNVEta1NXSlkwM1c2UUNIeE5Wdkp4ZjBvX3Y5T3Z2LUVhcFZEc0Y4amVvSjJvUzdxQVFsekVWd2hoVlRhWk5aWGxjZUtz?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQaldob3FsZloyeUJwWGFqekxrWkVVX2pFM1ZiNjdaX0ZKTXo1Rzl2c1kzRzNrM013RzdrOUVIV1NBeVJ6MHlHT3ZqdGE1ejhBdS1zU2lhbHlsOTR3bXg3aUxHZW9zOGs0YzRfTWxHeS1kX2pFZWE2OGVhSHFSNkhKMTUyTDBJQkVObFdiVjVIbHd3ZlZpVEJLemlJeG53N2s?oc=5
- https://news.google.com/rss/articles/CBMi-AFBVV95cUxNM2VFY0dIRVcxdVhpdFpHRV9JWXZDUnI1U3NyYUEwVkFFUlJ5ZDN5M3NfakpQdU1MOWYtSmNNWXBOREY0Qi0wTllXdWgzZVBHX0JRa0M0SENxOUxaYlZwdTJ5N2ZrcHRYUFpEaFJFSmhxbGhJVVhVX3kwcUNoZ3ZER0RfSnEwYTFKbnNoLUZsbGJoeUwzanY2cHFWU3BzNWpXd0NiUFg5X212TFNkMDItTjlBYVZxSzRPd2FqcjRVNlJyM1EyZ19YSDVNUUY3WHJkUkEwUW5Oa0RWSUhVOHk2WUpMVmtXcVd0ekpjeTRQTDdEdW1QdG8zag?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxQdE44SDRNZ19hUGp2ckZ5VjJwTGZkOHVSR203WGZwUFhLWUp5ZVQ0NzBSc3EzWTQtVU9vLTFoLTN1ajJrTE91MkkwYXNjQmpvM3ZGNTlnX1J5Q2d2TGp4RU5sdVl0SklxV0pzOW9SRmkwN2dzUUZENnhqYVVieWJNX1Fib2owOUF1S0NSRl9SWmo1RVE1QUtSNlhxcWRTaXJENVQ4RW5UUk9GUzNKbG5GbzNMTGNEVlk?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxQZFBLVEpPdDJ6ZlhBczUydzZvUWFaMVctWVJLN29tS1BBRHY3T1BrblNZUVRPcEhtUTBpT3pfOE5sSENSbmsyQWZ4TlVkU0V1dHhUcVR4bzNUVXZCaWJkTV9jb2s3MDRGZGdkcTZGUkxoYkdEWmhUQU5MQm5ybHdQZTBZSUliV2xQblhNOC14eUJ1NXh6NUI5MTRlS2lIeld1T0hRdUUxYjhZdw?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPekNEZ3lzY0RJTDRta3FyTm9lajJXSnl6eUNDZlo2YzNxbGc4ckV4Ymt3U1c2b0gxVUh2VTBMaThLaHZGdU1FbHVubG1Kb19Gd0lvN3U2b2VoUnFxdnphTjViandrNEQ5T01JZTRKeXlMSjZCNGNFRkRxdGZ5SURReWlwRkJTNVZlSlpCU0cwR3U5V2c5WlhNSDdGQQ?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxNRnYzc2pVVUVaSEd0ek5wY3duY2EtbXJ6enE3SnhkZ0tJclNVUGZaekpxWXZnR2NIVkNCUW5RN003MV9hMDhFYUxXeVlYZTJlNlpMbVpLTVM1Z1ZCOTNqNEF0YXNuajQwLVN2SVdhQTlScUVvREVPVmxPTWVUYnBrYXc4OUpsOFBZdXlyZzJxaTlnUUpDQl9oTm13NC1WdVJ5T1RGd0J6dktjeHM?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxONmNEVDZFWXVmYWlkOHpmc1VSMFRtNlVwdlRSSGxvcGFxVnVrZzhaMnpHcmphM21RRjRyQ3U2YnhvdzAyeEVtYnRLSVVWeTFlU3AyT19kNmxqaFFiVk5wNXZjVkdUaFhEZVd0LW9sYXZMR25seUlwdDFPYTViNk5keDNLTDEyY0xUNG5adml3NEVkTHBicklzcXZsYWFScDl6cTFV?oc=5
- https://news.google.com/rss/articles/CBMigAFBVV95cUxNU2ZSQWl5THpqSVoxNWNvMjNvbFhHcVA2bWFFZ3FoRkNiVlE4QWVCNkdpSlc1Q2RmbmxTUkQtQl9vTUhCc2tEanlJRlBCM2JQT2pjYmc1SWJhbFc4U0EwZk9OenpxVDMtWThSOVB6SWxVSGp6bnprUUd4TWFpMF9rag?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxNVlN1YlRDRWNDNzc3OVhrU3JYR2xFYjdSOHdleDlRcDZRbGZGQ3R6cW5yYXdsTEtEbzJWMWRZMFdNc0h3dDc0RlBLZTkxb3FSRVloOEZEQWZaYkVQZVdvT2VjVkFDRFdqR0ZPSDl2bWRmbk0wQ2RBZXhhN2N6SE0tRUxWTXFockgzVDVmNTNBNnRzbXc?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxOZ2NuQTRMd3FVRXB2OTJ4M0FlejNIUC0ycGhVTjlTaHZPQXFCYkJnVXRhRGVIdGIxV3IxZExEOWZEYjJYUWI2TGZudEcwRTZJTVNRcENjdHFSdEJEWE5ZY0NTbk5PTEJkeG9valdzcXZGOVBZV2tKZm16Rk1sOVN3MXFrSXl2NWZXRVFqZWpOWG8xQlhPamQ4blF3eXp1bUdOdW14WWVsWUEtZDYweC1vQ3Z6OE9pN184VmJVem9iMDZmNnRmeHFqblZQbm41WmtmRlE?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxNRmJSekZTQkdueHp4RTJrMWd4WnAwdEVMQ2ZpVnpkaV85aVZRQUN6ZW5wZHo2WDcweDhwVVBJdXZhT29rUlVmTFAwc2VZUkladmEtYWNHdzVQYnBRMWduZVJjbVJVV3FCaVhmWGhTbDJmcC1HZUstQURzaEhWZkg2b0dFMFlObDdNdkxpZGdKcGhiSmRDaHcwTnEwQkZZelJB?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
