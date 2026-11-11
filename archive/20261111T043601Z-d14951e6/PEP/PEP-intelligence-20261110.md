# PEP Intelligence Report

- ticker: **PEP**
- Report as_of: **2026-11-10**
- Market data as_of: **2026-11-10**
- Quant sources: https://finance.yahoo.com/quote/PEP/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/PEP/key-statistics/
- AI analysis snapshot as_of: **2026-11-10**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-11T04:46:11.976554+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 7, 'ai': 7, 'unknown': 0, 'irrelevant': 10})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **12** exact headline/source/date matches; prior report **20261110T055129Z-abd33250/PEP** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 10 named publishers; 0 exact duplicates; 24 HTTPS source links; largest publisher share 41.67%; oldest publication 2026-11-05

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 143.6100 |
| Return 1D (%) | 1.2193 |
| Return 1W (%) | 4.6186 |
| Return 1M (%) | 14.0033 |
| Return YTD (%) | 3.1087 |
| Return 1Y (%) | 4.7742 |
| Annualized volatility (%) | 21.6415 |
| Beta vs SPY | -0.1977 |
| Max drawdown (%) | -25.2176 |
| Sharpe (rf=0) | 0.3238 |
| Downside deviation (rf=0, %) | 14.3032 |
| Sortino (rf=0) | 0.4899 |
| Historical VaR 95% (1D, %) | 2.1996 |
| Historical ES 95% (1D, %) | 2.6412 |
| Correlation vs SPY | -0.1249 |
| Tracking error vs SPY (%) | 27.0023 |
| P/E (trailing) | 17.84 |
| P/B | 8.79 |
| EV/EBITDA | 12.34 |
| Revenue growth (%) | 5.60 |
| Forward P/E (estimate) | 16.62 |
| Gross margin (%) | 54.33 |
| Operating margin (%) | 16.88 |
| Return on equity (%) | 52.19 |
| Free cash flow yield (%) | 4.62 |
| MA50 | 133.3227 |
| Close vs MA50 (%) | 7.7161 |
| MA200 | 143.6980 |
| Close vs MA200 (%) | -0.0612 |
| RSI (14, Wilder) | 65.8292 |
| MACD (12,26) | 2.9873 |
| MACD signal (9) | 2.1268 |
| MACD histogram | 0.8605 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'PEP': 279, 'SPY': 279}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 143.6100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.2193 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 4.6186 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 14.0033 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 3.1087 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 4.7742 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 21.6415 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.3032 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4899 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.1996 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.6412 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1249 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 27.0023 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1977 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -25.2176 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3238 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.6238 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.3270 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 16.8830 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 52.1870 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.6214 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 17.8397 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 65.8292 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.8605 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 7.7161 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -0.0612 -> Slightly below the moving-average trend level.

## TAILWINDS

### PepsiCo (NASDAQ:PEP) Stock Price Up 1.2% - Here's What Happened
- Summary: PepsiCo (NASDAQ:PEP) Stock Price Up 1.2% - Here's What Happened
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxQQ3VwYVByV2d1Q1NMb0xtaVFxSkoyNWtRdXZxQXZrR25OUEw0UEdFZ0VnRGRMRjFnd1pXVUpBVVdwdC03M0YxanRJVGJYSjVCcDNPTm5EVXpJZDJJN3N1Ym54U2lPdnhuclRCcXlFMXhvdDZSR3FFVzdqeG1INmZuaWZGQ0RxWTJpRllSMmZsbTZxdDZMWDhGb19kM3VpTVpPYi1xbnY5d1ByVjdtTlZkSHk1QkZsd0k?oc=5>

### Do PepsiCo’s Dividends Make Up For A Lagging Stock?
- Summary: Analysis questions if dividends offset a lagging stock, suggesting potential positive impact.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxQVlhoS2hVbXB4TFlVMVRsUGtjVWdJOFpLVVNFalQyN3RYazBFUHNrT212ZHZwR09za2ZIWUcwYnZ2S3BJVGt0SHU3elZCZlN5RTdxbE0xcUxqUzRTdUlQU2tGTG5JV3ozdkRRUTExMndOX1IzMW5QdDBsRjYta2lCRl82NzVCMXd3QkxXTzlaQjZjY3duQkNHU2JHSWMzcl9WNjJQU1FUaTRoVGxfQkE?oc=5>

## HEADWINDS

### PepsiCo, Inc. $PEP Holdings Decreased by Boston Trust Walden Corp
- Summary: Major holder reduced holdings, indicating possible negative sentiment.
- Date: 2026-11-05 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxOUndwU1dpZG1sdjNpRmRRUmhyNG9ZNW5PZDdheHBGWGM0RHJ4WThHS1pOUU9GR0VUUEd3bHJqb0ZuTlFvclIwZjh2Mi1DeWdkTmNqcDlZdHVvUE05MUsyRkNGNjY3b2xCUDd4SHRHRVNWOW9FaXBHVHhqOWFxc2xCYlpHdUM5d09DUnFsbHZkSldOcWh2V2xKemFfRVk1MjhsNTBfZHViNlVhS3FVYVhuLTZGcmlqUFY3VDJlTDA4LWM?oc=5>

### PepsiCo (PEP) Cuts 1,000 Jobs as North American Sales Struggle
- Summary: Job cuts amid sales decline signal operational challenges.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxOYnZMM0Z1REtrT1JJaFhBdWR6OW1pUG1SS3M5OFYzR0NUQUY2YlU2clg5WU1IamxjRXdibEVmZk1xRlIwSHVCcnJJTWxlMXZjQTQ0WUduTG9PdnNpUWNmVFg1NWg1UGtlWVdNZVV1MW1pSnN0MGFySVBtYXFEY3FjYTQ0d2QteVlpcGFTTVhPVUJRTU0?oc=5>

## CATALYSTS

### PepsiCo Has Raised Its Dividend 54 Straight Years, but $1,000 in Coca-Cola Finished $1,296 Ahead Over the Past Decade
- Summary: PepsiCo Has Raised Its Dividend 54 Straight Years, but $1,000 in Coca-Cola Finished $1,296 Ahead Over the Past Decade
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxPREZNWVpQWFR3bmZjcUZJQTAwQUdTa1hCQnVpaEJuN19xMjNfMmVhSW1xNjI0U2JXRnA5LXlySjB0bDNvak5ZX0ZzU2t4U0J0bkNJUHZBZEJNdmVqSVFLVUZqZTRTZnM2WVdaN1JuS1psaWJ1WHZic05Vc1Njc05CT2RoTXF4SjZ1Sk5OVXdZZXVhRWxiU0ljb1c4Um1GdEVKR3dhLUpxd3hvQWQ0TlVpcmh2VkRLNEE3MGRrSFZtY0Q3VjVZRzdud3JqTDZDbnQ3eW5kYXFZbklnVjEtLW5tdEhxVGV3SlVqUmhveg?oc=5>

### PepsiCo, Inc. $PEP Stock Sold by Welch & Forbes LLC
- Summary: PepsiCo, Inc. $PEP Stock Sold by Welch & Forbes LLC
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxNZDg4clZrc3dLNHI0R0hJcGg4cDUtUmtNM2hYREo2YVRkWG10Z25jTmgzYzI2cGNRNzUzTXZFYUV3UWs5MkN3T2dBUEt2ZjRpN2RxVnlmQXdNZ05LVmNwYTB5YnRGUThmNGRKUDdWdXBqZ1o2S3UyRjlGbFJlYVNZeWRSVEozZmpqb1g2MXhMSWlYaHZiYTJxYWpaeU1LLUdTcFNBTEVsMlMxQkU?oc=5>

### PepsiCo Extends KFC Beverage Partnership Across Eight International Markets
- Summary: PepsiCo Extends KFC Beverage Partnership Across Eight International Markets
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxOaFJTajBVaXltQzNFcXlnSVl2V1Z5R0hVcDJPVjVHYUhibVhHR3UwRV9hOXV6MzN3bFZhazE2Z0Y2c0dHVVJsUHFPaGpvcFlHbjMzMk5tUmRZMDFERFV3ODZXVzRqNVZlb2diU2lnR0dGenY3RzJYTmc3ZHBvdGtadWZ5SjZBUVZGUjRaamxkMjlLOG5SYWJORWxiWlZOSGVTcmRBWm1fX2g?oc=5>

### PepsiCo, Inc. $PEP Stock Sold by Brighton Jones LLC
- Summary: PepsiCo, Inc. $PEP Stock Sold by Brighton Jones LLC
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxQcXF2dHM3ZUtuTWJzeXpuTElqbzM1YXZQeXl2eXVxTzBLSFhyN1lRMXJTZHVtLU1nclZ6Qkp0ajJ5dnZnS3F1YVdSTFFVRmZiQkctaHgzY0VkZUFBUXVHamxBendUUV84bHktcXo0SkJhdGk1QVUyR0dzbEVjNElKQTZiQnZSYTJ6djYzSF9KU0VPQkhqR3pQalY5aEV1Wm1sa2duYTVpa0VjdVNFd1E?oc=5>

### PepsiCo, Inc. $PEP Stock: Lindsell Train Ltd Reduces Stake
- Summary: PepsiCo, Inc. $PEP Stock: Lindsell Train Ltd Reduces Stake
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxQeGY2TmxKcm1TWXpkcDA0NDMwS0xmMzd4WmxsdURQVTFxT2lZOXF3Z1JvMEhyc2g1aGZvQ09rRHFPZGhiQUpTWG81MHcwd2ptRGp6bzdUd0NPaWZYUHJfUjE5em05NXN3V1lLSHBlVFdydlAxX3hnRlZoa3RNQVkzaEVjVllQZ19aZXBzSkFnRHNlT2pnU3AwZG56WFZhMldUZWZvMENGN3VPd1Z2S1B1TTYzckQ4Zw?oc=5>

### PepsiCo, Inc. $PEP Shares Purchased by Kestra Advisory Services LLC
- Summary: PepsiCo, Inc. $PEP Shares Purchased by Kestra Advisory Services LLC
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxQY3UwclhpOC1JcmVTRU0zM3doSWx6bFR3QlhCc0lPMjF4Z0VBSkRVV3BJR2swTU1QMHE0WnI4Q2tva2MzSldTZjI0VXBVd0ZoR2RqQ1lCVm52bWZUNnhiVG5TUnliLXE4TzhKS1RmNlFkWW1LUFQ0eWxFN0hhTW5DMEp3MFFzN25pUUhXYWFNVW9wU1NOZ2szb0lzZG52RlkyT2ZPdXo2UzFNMFY4RXU5Mk12ZTlrR0w5X0tGOGt4Vk5MRDA?oc=5>

### PepsiCo (PEP) Could Be 29% Undervalued Following Its KFC Deal Renewal
- Summary: Speculation that PepsiCo may be undervalued after renewing its KFC franchise agreement.
- Date: 2026-11-06 | Impact: low | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOTTZVbW1pRWl3aU9seF8zT2ZCZ2hrUFcwXzltSUNOUlYxSmJvWWp2V2l3cF9veVdfVTU5Q3V1VTNNYWtmem5GWHo2bzUwRTJRa2xBX2FTRDBrX2xNUGJQQWktcWJ0SVdMYW9xOWRyM2RsNWU4SmNoMXV1dnZNaDlQVmN6N1Z3MHZLeEtSZXNJbU5ObnNoSkliblphQmJFdw?oc=5>

### KFC pairs chicken tenders with Doritos on select menus as PepsiCo renews its drink deal in 8 countries.
- Summary: PepsiCo renews its drink partnership with KFC in eight countries, pairing drinks with new menu items.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxNMWdkU0gzZGtHMzFwQUxfZ1VrRjdfQXctbnlleE1JMkJGQ1lFeWZfVUZrOTVLbmhTYW5DVklLVEU3MUVJdWxKRXQzdDVsOFRPenRRWFByM211SWQ5TzhuRFlvdmJiRWc5WXZTUElWZzVRbzg0N0dGVTlzU3V6OW5peDZkUTlPTlRCaDBFZGxUWmZHSVIwT2Mzd0J4TFoyZHptSzJ4R09nZndHeWRpUGJj?oc=5>

### Learn Why The Bull Case For PepsiCo (PEP) Could Change Following KFC Deal Renewal
- Summary: KFC deal renewal may alter PepsiCo’s bullish outlook.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxQamxqV0M3YXdmNS1FOENuc3ExX1VQT29XaWRXZmZEYkJVdE0zampyUWRnZWFDay1jcTQta3VDeUI5SGprNGNjbFhoVE9xTmZ0VEFIMG1zdjhiM040Y2JpVWN4NDd1OTBXVW5RV05JY0ZkZDFoUkxWWllKNTdkUmZwYnQzWTJscXVKTGoxUHFGLUtpUnpUSUVpd2IwX1FxVEtQb2VhTkZyWmpPaGJnSjc2UXZIWU1YMnR5WnVGYXh6YmVkem1JQ2Jsbm9WbzRqcllIMzhfWNIB2gFBVV95cUxOR3lTd2U0eXVlZE5IOWkwdFB2blNOVkNEZ2JWWlc2a3F3T21zMjhuWTZCN3BiZHRzWkwwRUluZ1VibS05cW1JOVZ4U0FXT3RXUTVVdWxsbm4tQkFWU0RRNWtHcHlrLW9JbkpQU3ZyUFVpem5YSk1fd09hT1YzMi16dVZnUWQtLVB3RDRGWHpTbFprRDR2ZFhvdXFLVlZydzdSTG9pY19aajM4bVVhNEFBbFJhV0RvM0plVmFMT1VOM3AzY19UNDgzVGJ3WE9WM29pTlhTbTVQbUY1UQ?oc=5>

## RISKS

### PepsiCo reshapes North American business with 1,000 job reductions (PEP:NASDAQ)
- Summary: PepsiCo cuts 1,000 jobs in North America, signaling cost-cutting and potential operational impact.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNbFFHVHlsLWJnOWIta3lIQnBNdE9DVkhZbVJkM0NJbHFIUlpTeVJoSzhNODZadFI4WGNabEdxd29LeUh4ZEdFTmZRdU91Nm5hbGl2SlJHMWdVU2lSc3d5Mno3dlZILTRxSTVDMlNOVHBxTjJpU0ppUk9GNndIaTZIT0FmQ0dWRnFDU3l4VDhmUFlJZ2p3NjZLM053SGhFN29EVHhBTFRn?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **PEP** | **17.84** | **8.79** | **12.34** | **5.60** | **195,703,259,136.00 USD** | **4.77** |
| KO | 28.59 | 11.16 | 25.51 | 7.40 | 416,897,368,064.00 USD | 41.08 |
| MNST | 41.60 | 9.02 | 28.58 | 16.70 | 88,753,594,368.00 USD | 29.49 |
| KDP | 33.27 | 2.01 | 17.44 | 70.60 | 51,158,048,768.00 USD | 48.50 |

Peers fetched as_of: 2026-11-10; PEP reuses existing data (market data as_of: 2026-11-10); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-08
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

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
- Filing date: 2026-10-08
- Revenue (latest available single quarter): 25,274,000,000.00 USD; period 2026-06-14/2026-09-05; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 3,048,000,000.00 USD; period 2026-06-14/2026-09-05; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/77476/000007747626000048/pep-20260905.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMitwFBVV95cUxQQ3VwYVByV2d1Q1NMb0xtaVFxSkoyNWtRdXZxQXZrR25OUEw0UEdFZ0VnRGRMRjFnd1pXVUpBVVdwdC03M0YxanRJVGJYSjVCcDNPTm5EVXpJZDJJN3N1Ym54U2lPdnhuclRCcXlFMXhvdDZSR3FFVzdqeG1INmZuaWZGQ0RxWTJpRllSMmZsbTZxdDZMWDhGb19kM3VpTVpPYi1xbnY5d1ByVjdtTlZkSHk1QkZsd0k?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxQVlhoS2hVbXB4TFlVMVRsUGtjVWdJOFpLVVNFalQyN3RYazBFUHNrT212ZHZwR09za2ZIWUcwYnZ2S3BJVGt0SHU3elZCZlN5RTdxbE0xcUxqUzRTdUlQU2tGTG5JV3ozdkRRUTExMndOX1IzMW5QdDBsRjYta2lCRl82NzVCMXd3QkxXTzlaQjZjY3duQkNHU2JHSWMzcl9WNjJQU1FUaTRoVGxfQkE?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxOUndwU1dpZG1sdjNpRmRRUmhyNG9ZNW5PZDdheHBGWGM0RHJ4WThHS1pOUU9GR0VUUEd3bHJqb0ZuTlFvclIwZjh2Mi1DeWdkTmNqcDlZdHVvUE05MUsyRkNGNjY3b2xCUDd4SHRHRVNWOW9FaXBHVHhqOWFxc2xCYlpHdUM5d09DUnFsbHZkSldOcWh2V2xKemFfRVk1MjhsNTBfZHViNlVhS3FVYVhuLTZGcmlqUFY3VDJlTDA4LWM?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxOYnZMM0Z1REtrT1JJaFhBdWR6OW1pUG1SS3M5OFYzR0NUQUY2YlU2clg5WU1IamxjRXdibEVmZk1xRlIwSHVCcnJJTWxlMXZjQTQ0WUduTG9PdnNpUWNmVFg1NWg1UGtlWVdNZVV1MW1pSnN0MGFySVBtYXFEY3FjYTQ0d2QteVlpcGFTTVhPVUJRTU0?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxPREZNWVpQWFR3bmZjcUZJQTAwQUdTa1hCQnVpaEJuN19xMjNfMmVhSW1xNjI0U2JXRnA5LXlySjB0bDNvak5ZX0ZzU2t4U0J0bkNJUHZBZEJNdmVqSVFLVUZqZTRTZnM2WVdaN1JuS1psaWJ1WHZic05Vc1Njc05CT2RoTXF4SjZ1Sk5OVXdZZXVhRWxiU0ljb1c4Um1GdEVKR3dhLUpxd3hvQWQ0TlVpcmh2VkRLNEE3MGRrSFZtY0Q3VjVZRzdud3JqTDZDbnQ3eW5kYXFZbklnVjEtLW5tdEhxVGV3SlVqUmhveg?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxNZDg4clZrc3dLNHI0R0hJcGg4cDUtUmtNM2hYREo2YVRkWG10Z25jTmgzYzI2cGNRNzUzTXZFYUV3UWs5MkN3T2dBUEt2ZjRpN2RxVnlmQXdNZ05LVmNwYTB5YnRGUThmNGRKUDdWdXBqZ1o2S3UyRjlGbFJlYVNZeWRSVEozZmpqb1g2MXhMSWlYaHZiYTJxYWpaeU1LLUdTcFNBTEVsMlMxQkU?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxOaFJTajBVaXltQzNFcXlnSVl2V1Z5R0hVcDJPVjVHYUhibVhHR3UwRV9hOXV6MzN3bFZhazE2Z0Y2c0dHVVJsUHFPaGpvcFlHbjMzMk5tUmRZMDFERFV3ODZXVzRqNVZlb2diU2lnR0dGenY3RzJYTmc3ZHBvdGtadWZ5SjZBUVZGUjRaamxkMjlLOG5SYWJORWxiWlZOSGVTcmRBWm1fX2g?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxQcXF2dHM3ZUtuTWJzeXpuTElqbzM1YXZQeXl2eXVxTzBLSFhyN1lRMXJTZHVtLU1nclZ6Qkp0ajJ5dnZnS3F1YVdSTFFVRmZiQkctaHgzY0VkZUFBUXVHamxBendUUV84bHktcXo0SkJhdGk1QVUyR0dzbEVjNElKQTZiQnZSYTJ6djYzSF9KU0VPQkhqR3pQalY5aEV1Wm1sa2duYTVpa0VjdVNFd1E?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxQeGY2TmxKcm1TWXpkcDA0NDMwS0xmMzd4WmxsdURQVTFxT2lZOXF3Z1JvMEhyc2g1aGZvQ09rRHFPZGhiQUpTWG81MHcwd2ptRGp6bzdUd0NPaWZYUHJfUjE5em05NXN3V1lLSHBlVFdydlAxX3hnRlZoa3RNQVkzaEVjVllQZ19aZXBzSkFnRHNlT2pnU3AwZG56WFZhMldUZWZvMENGN3VPd1Z2S1B1TTYzckQ4Zw?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxQY3UwclhpOC1JcmVTRU0zM3doSWx6bFR3QlhCc0lPMjF4Z0VBSkRVV3BJR2swTU1QMHE0WnI4Q2tva2MzSldTZjI0VXBVd0ZoR2RqQ1lCVm52bWZUNnhiVG5TUnliLXE4TzhKS1RmNlFkWW1LUFQ0eWxFN0hhTW5DMEp3MFFzN25pUUhXYWFNVW9wU1NOZ2szb0lzZG52RlkyT2ZPdXo2UzFNMFY4RXU5Mk12ZTlrR0w5X0tGOGt4Vk5MRDA?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOTTZVbW1pRWl3aU9seF8zT2ZCZ2hrUFcwXzltSUNOUlYxSmJvWWp2V2l3cF9veVdfVTU5Q3V1VTNNYWtmem5GWHo2bzUwRTJRa2xBX2FTRDBrX2xNUGJQQWktcWJ0SVdMYW9xOWRyM2RsNWU4SmNoMXV1dnZNaDlQVmN6N1Z3MHZLeEtSZXNJbU5ObnNoSkliblphQmJFdw?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxNMWdkU0gzZGtHMzFwQUxfZ1VrRjdfQXctbnlleE1JMkJGQ1lFeWZfVUZrOTVLbmhTYW5DVklLVEU3MUVJdWxKRXQzdDVsOFRPenRRWFByM211SWQ5TzhuRFlvdmJiRWc5WXZTUElWZzVRbzg0N0dGVTlzU3V6OW5peDZkUTlPTlRCaDBFZGxUWmZHSVIwT2Mzd0J4TFoyZHptSzJ4R09nZndHeWRpUGJj?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxQamxqV0M3YXdmNS1FOENuc3ExX1VQT29XaWRXZmZEYkJVdE0zampyUWRnZWFDay1jcTQta3VDeUI5SGprNGNjbFhoVE9xTmZ0VEFIMG1zdjhiM040Y2JpVWN4NDd1OTBXVW5RV05JY0ZkZDFoUkxWWllKNTdkUmZwYnQzWTJscXVKTGoxUHFGLUtpUnpUSUVpd2IwX1FxVEtQb2VhTkZyWmpPaGJnSjc2UXZIWU1YMnR5WnVGYXh6YmVkem1JQ2Jsbm9WbzRqcllIMzhfWNIB2gFBVV95cUxOR3lTd2U0eXVlZE5IOWkwdFB2blNOVkNEZ2JWWlc2a3F3T21zMjhuWTZCN3BiZHRzWkwwRUluZ1VibS05cW1JOVZ4U0FXT3RXUTVVdWxsbm4tQkFWU0RRNWtHcHlrLW9JbkpQU3ZyUFVpem5YSk1fd09hT1YzMi16dVZnUWQtLVB3RDRGWHpTbFprRDR2ZFhvdXFLVlZydzdSTG9pY19aajM4bVVhNEFBbFJhV0RvM0plVmFMT1VOM3AzY19UNDgzVGJ3WE9WM29pTlhTbTVQbUY1UQ?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNbFFHVHlsLWJnOWIta3lIQnBNdE9DVkhZbVJkM0NJbHFIUlpTeVJoSzhNODZadFI4WGNabEdxd29LeUh4ZEdFTmZRdU91Nm5hbGl2SlJHMWdVU2lSc3d5Mno3dlZILTRxSTVDMlNOVHBxTjJpU0ppUk9GNndIaTZIT0FmQ0dWRnFDU3l4VDhmUFlJZ2p3NjZLM053SGhFN29EVHhBTFRn?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
