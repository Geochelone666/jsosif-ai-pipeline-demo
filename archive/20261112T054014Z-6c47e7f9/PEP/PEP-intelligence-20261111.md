# PEP Intelligence Report

- ticker: **PEP**
- Report as_of: **2026-11-11**
- Market data as_of: **2026-11-11**
- Quant sources: https://finance.yahoo.com/quote/PEP/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/PEP/key-statistics/
- AI analysis snapshot as_of: **2026-11-11**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-12T05:48:14.929821+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 14, 'rule': 2, 'ai': 8, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261111T043601Z-d14951e6/PEP** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 14 unique headlines; 10 named publishers; 0 exact duplicates; 14 HTTPS source links; largest publisher share 21.43%; oldest publication 2026-11-05

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 143.9400 |
| Return 1D (%) | 0.2298 |
| Return 1W (%) | 1.0673 |
| Return 1M (%) | 14.2653 |
| Return YTD (%) | 3.3456 |
| Return 1Y (%) | 3.2344 |
| Annualized volatility (%) | 21.5751 |
| Beta vs SPY | -0.1962 |
| Max drawdown (%) | -25.2176 |
| Sharpe (rf=0) | 0.2552 |
| Downside deviation (rf=0, %) | 14.3032 |
| Sortino (rf=0) | 0.3850 |
| Historical VaR 95% (1D, %) | 2.1996 |
| Historical ES 95% (1D, %) | 2.6412 |
| Correlation vs SPY | -0.1249 |
| Tracking error vs SPY (%) | 26.9804 |
| P/E (trailing) | 18.11 |
| P/B | 8.81 |
| EV/EBITDA | 12.37 |
| Revenue growth (%) | 5.60 |
| Forward P/E (estimate) | 16.69 |
| Gross margin (%) | 54.33 |
| Operating margin (%) | 16.05 |
| Return on equity (%) | 52.19 |
| Free cash flow yield (%) | 4.61 |
| MA50 | 133.4353 |
| Close vs MA50 (%) | 7.8725 |
| MA200 | 143.6958 |
| Close vs MA200 (%) | 0.1700 |
| RSI (14, Wilder) | 66.3032 |
| MACD (12,26) | 3.1372 |
| MACD signal (9) | 2.3289 |
| MACD histogram | 0.8083 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'PEP': 280, 'SPY': 280}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 143.9400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.2298 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.0673 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 14.2653 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 3.3456 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 3.2344 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 21.5751 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.3032 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.3850 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.1996 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.6412 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1249 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.9804 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1962 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -25.2176 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2552 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.6939 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.3270 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 16.0460 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 52.1870 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.6108 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 18.1057 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 66.3032 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.8083 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 7.8725 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 0.1700 -> Slightly above the moving-average trend level.

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

### PepsiCo (PEP) Cuts 1,000 Jobs as North American Sales Struggle
- Summary: Job cuts amid sales decline signal operational challenges.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxOYnZMM0Z1REtrT1JJaFhBdWR6OW1pUG1SS3M5OFYzR0NUQUY2YlU2clg5WU1IamxjRXdibEVmZk1xRlIwSHVCcnJJTWxlMXZjQTQ0WUduTG9PdnNpUWNmVFg1NWg1UGtlWVdNZVV1MW1pSnN0MGFySVBtYXFEY3FjYTQ0d2QteVlpcGFTTVhPVUJRTU0?oc=5>

## CATALYSTS

### PepsiCo Has Raised Its Dividend 54 Straight Years, but $1,000 in Coca-Cola Finished $1,296 Ahead Over the Past Decade
- Summary: PepsiCo Has Raised Its Dividend 54 Straight Years, but $1,000 in Coca-Cola Finished $1,296 Ahead Over the Past Decade
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxPREZNWVpQWFR3bmZjcUZJQTAwQUdTa1hCQnVpaEJuN19xMjNfMmVhSW1xNjI0U2JXRnA5LXlySjB0bDNvak5ZX0ZzU2t4U0J0bkNJUHZBZEJNdmVqSVFLVUZqZTRTZnM2WVdaN1JuS1psaWJ1WHZic05Vc1Njc05CT2RoTXF4SjZ1Sk5OVXdZZXVhRWxiU0ljb1c4Um1GdEVKR3dhLUpxd3hvQWQ0TlVpcmh2VkRLNEE3MGRrSFZtY0Q3VjVZRzdud3JqTDZDbnQ3eW5kYXFZbklnVjEtLW5tdEhxVGV3SlVqUmhveg?oc=5>

### PepsiCo (PEP) Could Be 29% Undervalued Following Its KFC Deal Renewal
- Summary: Speculation that PepsiCo may be undervalued after renewing its KFC franchise agreement.
- Date: 2026-11-06 | Impact: low | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOTTZVbW1pRWl3aU9seF8zT2ZCZ2hrUFcwXzltSUNOUlYxSmJvWWp2V2l3cF9veVdfVTU5Q3V1VTNNYWtmem5GWHo2bzUwRTJRa2xBX2FTRDBrX2xNUGJQQWktcWJ0SVdMYW9xOWRyM2RsNWU4SmNoMXV1dnZNaDlQVmN6N1Z3MHZLeEtSZXNJbU5ObnNoSkliblphQmJFdw?oc=5>

### Learn Why The Bull Case For PepsiCo (PEP) Could Change Following KFC Deal Renewal
- Summary: KFC deal renewal may alter PepsiCo’s bullish outlook.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxQamxqV0M3YXdmNS1FOENuc3ExX1VQT29XaWRXZmZEYkJVdE0zampyUWRnZWFDay1jcTQta3VDeUI5SGprNGNjbFhoVE9xTmZ0VEFIMG1zdjhiM040Y2JpVWN4NDd1OTBXVW5RV05JY0ZkZDFoUkxWWllKNTdkUmZwYnQzWTJscXVKTGoxUHFGLUtpUnpUSUVpd2IwX1FxVEtQb2VhTkZyWmpPaGJnSjc2UXZIWU1YMnR5WnVGYXh6YmVkem1JQ2Jsbm9WbzRqcllIMzhfWNIB2gFBVV95cUxOR3lTd2U0eXVlZE5IOWkwdFB2blNOVkNEZ2JWWlc2a3F3T21zMjhuWTZCN3BiZHRzWkwwRUluZ1VibS05cW1JOVZ4U0FXT3RXUTVVdWxsbm4tQkFWU0RRNWtHcHlrLW9JbkpQU3ZyUFVpem5YSk1fd09hT1YzMi16dVZnUWQtLVB3RDRGWHpTbFprRDR2ZFhvdXFLVlZydzdSTG9pY19aajM4bVVhNEFBbFJhV0RvM0plVmFMT1VOM3AzY19UNDgzVGJ3WE9WM29pTlhTbTVQbUY1UQ?oc=5>

### KFC pairs chicken tenders with Doritos on select menus as PepsiCo renews its drink deal in 8 countries.
- Summary: PepsiCo renews its drink partnership with KFC in eight countries, pairing drinks with new menu items.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxNMWdkU0gzZGtHMzFwQUxfZ1VrRjdfQXctbnlleE1JMkJGQ1lFeWZfVUZrOTVLbmhTYW5DVklLVEU3MUVJdWxKRXQzdDVsOFRPenRRWFByM211SWQ5TzhuRFlvdmJiRWc5WXZTUElWZzVRbzg0N0dGVTlzU3V6OW5peDZkUTlPTlRCaDBFZGxUWmZHSVIwT2Mzd0J4TFoyZHptSzJ4R09nZndHeWRpUGJj?oc=5>

### PepsiCo reshapes North American business with 1,000 job reductions (PEP:NASDAQ)
- Summary: PepsiCo cuts 1,000 jobs in North America, signaling a workforce reduction strategy.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNbFFHVHlsLWJnOWIta3lIQnBNdE9DVkhZbVJkM0NJbHFIUlpTeVJoSzhNODZadFI4WGNabEdxd29LeUh4ZEdFTmZRdU91Nm5hbGl2SlJHMWdVU2lSc3d5Mno3dlZILTRxSTVDMlNOVHBxTjJpU0ppUk9GNndIaTZIT0FmQ0dWRnFDU3l4VDhmUFlJZ2p3NjZLM053SGhFN29EVHhBTFRn?oc=5>

## RISKS

### PepsiCo Stock Outlook: Is Wall Street Bullish or Bearish?
- Summary: Analysts debate PepsiCo's future market sentiment.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQdEdUQURjRnlZNzNUZGhaVEMwVC01RFFab0xTb1ZaZ2l0d0tzUDJ1NDNiMWxPQ3BJSDV4cllLM0U2MFo5R3pWREc0TUxveHU0QmJSQ2g2THRPZ0xKNkhxelVVQUxKbmRQdGZuVG5vNFBDR2UwWmFZd0hWN1pjbXlsd1FjZDlhUUJ1QzVNcDBOUVlTc0hId0MwX0FhY21aMHM?oc=5>

### PepsiCo (PEP) Stock Could Be Below Fair Value On Cash Flow
- Summary: Speculation that PepsiCo's stock may be undervalued based on cash flow.
- Date: 2026-11-11 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxQa1FBd3lLTDU1OE1vQzByRlphSWJZY05HS1ptZGpfZEgyMVJMQlVTMUt3LUVvWjRTYXpIbWUzMEdSN3BqUjJVdjBOb0J4X1ByMHpaZWxrX041NVFRalVPMnNvUXFoOG1qV1k2NXVPc1BubFRLcElDUGROTUdreldNSm5OOHd4anhIaGZKSmU3ZWZGUkc5TmZtWkpad3psdmZLMWRua3pFYTBnUzV0Uy0wUGo4Y2pEcGk0TzBmaWI5am53NENacFJHaGYtdFd3ZE3SAdQBQVVfeXFMT1BUY2dJbXFWeXBrbWIxV3Rlb0o2SWFtRkhYRGx2Y21rc2tGU3l2S1ZmVEpfaW0tb0QyLXdpSFdfdkpKWnU3UjlEMTZ3TkFiT2NRM19CVHlCa2dMRmlrQ2JMQ0tGbVVvYkRiaUpLZDh0UWxpWVlnblhhdTBfeEV4NXdPc1FHQUxZV2dtXzVURWpOcjJIY01jQkxHRUpmZmw0QzlWdk8xb2Z0bkFma3lNOWZySnFzZ2sxMEhhWkxRUlRZV2ZnZHVFeVh4UWx2VnE5el9qOEY?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **PEP** | **18.11** | **8.81** | **12.37** | **5.60** | **196,152,967,168.00 USD** | **3.23** |
| KO | 28.78 | 11.23 | 25.67 | 7.40 | 419,736,616,960.00 USD | 39.87 |
| MNST | 41.27 | 9.03 | 28.62 | 16.70 | 88,871,043,072.00 USD | 26.27 |
| KDP | 34.46 | 2.05 | 17.12 | 70.60 | 52,056,272,896.00 USD | 47.66 |

Peers fetched as_of: 2026-11-11; PEP reuses existing data (market data as_of: 2026-11-11); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-08
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
- Filing date: 2026-10-08
- Revenue (latest available single quarter): 25,274,000,000.00 USD; period 2026-06-14/2026-09-05; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 3,048,000,000.00 USD; period 2026-06-14/2026-09-05; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/77476/000007747626000048/pep-20260905.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMitwFBVV95cUxQQ3VwYVByV2d1Q1NMb0xtaVFxSkoyNWtRdXZxQXZrR25OUEw0UEdFZ0VnRGRMRjFnd1pXVUpBVVdwdC03M0YxanRJVGJYSjVCcDNPTm5EVXpJZDJJN3N1Ym54U2lPdnhuclRCcXlFMXhvdDZSR3FFVzdqeG1INmZuaWZGQ0RxWTJpRllSMmZsbTZxdDZMWDhGb19kM3VpTVpPYi1xbnY5d1ByVjdtTlZkSHk1QkZsd0k?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxQVlhoS2hVbXB4TFlVMVRsUGtjVWdJOFpLVVNFalQyN3RYazBFUHNrT212ZHZwR09za2ZIWUcwYnZ2S3BJVGt0SHU3elZCZlN5RTdxbE0xcUxqUzRTdUlQU2tGTG5JV3ozdkRRUTExMndOX1IzMW5QdDBsRjYta2lCRl82NzVCMXd3QkxXTzlaQjZjY3duQkNHU2JHSWMzcl9WNjJQU1FUaTRoVGxfQkE?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxOYnZMM0Z1REtrT1JJaFhBdWR6OW1pUG1SS3M5OFYzR0NUQUY2YlU2clg5WU1IamxjRXdibEVmZk1xRlIwSHVCcnJJTWxlMXZjQTQ0WUduTG9PdnNpUWNmVFg1NWg1UGtlWVdNZVV1MW1pSnN0MGFySVBtYXFEY3FjYTQ0d2QteVlpcGFTTVhPVUJRTU0?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxPREZNWVpQWFR3bmZjcUZJQTAwQUdTa1hCQnVpaEJuN19xMjNfMmVhSW1xNjI0U2JXRnA5LXlySjB0bDNvak5ZX0ZzU2t4U0J0bkNJUHZBZEJNdmVqSVFLVUZqZTRTZnM2WVdaN1JuS1psaWJ1WHZic05Vc1Njc05CT2RoTXF4SjZ1Sk5OVXdZZXVhRWxiU0ljb1c4Um1GdEVKR3dhLUpxd3hvQWQ0TlVpcmh2VkRLNEE3MGRrSFZtY0Q3VjVZRzdud3JqTDZDbnQ3eW5kYXFZbklnVjEtLW5tdEhxVGV3SlVqUmhveg?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOTTZVbW1pRWl3aU9seF8zT2ZCZ2hrUFcwXzltSUNOUlYxSmJvWWp2V2l3cF9veVdfVTU5Q3V1VTNNYWtmem5GWHo2bzUwRTJRa2xBX2FTRDBrX2xNUGJQQWktcWJ0SVdMYW9xOWRyM2RsNWU4SmNoMXV1dnZNaDlQVmN6N1Z3MHZLeEtSZXNJbU5ObnNoSkliblphQmJFdw?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxQamxqV0M3YXdmNS1FOENuc3ExX1VQT29XaWRXZmZEYkJVdE0zampyUWRnZWFDay1jcTQta3VDeUI5SGprNGNjbFhoVE9xTmZ0VEFIMG1zdjhiM040Y2JpVWN4NDd1OTBXVW5RV05JY0ZkZDFoUkxWWllKNTdkUmZwYnQzWTJscXVKTGoxUHFGLUtpUnpUSUVpd2IwX1FxVEtQb2VhTkZyWmpPaGJnSjc2UXZIWU1YMnR5WnVGYXh6YmVkem1JQ2Jsbm9WbzRqcllIMzhfWNIB2gFBVV95cUxOR3lTd2U0eXVlZE5IOWkwdFB2blNOVkNEZ2JWWlc2a3F3T21zMjhuWTZCN3BiZHRzWkwwRUluZ1VibS05cW1JOVZ4U0FXT3RXUTVVdWxsbm4tQkFWU0RRNWtHcHlrLW9JbkpQU3ZyUFVpem5YSk1fd09hT1YzMi16dVZnUWQtLVB3RDRGWHpTbFprRDR2ZFhvdXFLVlZydzdSTG9pY19aajM4bVVhNEFBbFJhV0RvM0plVmFMT1VOM3AzY19UNDgzVGJ3WE9WM29pTlhTbTVQbUY1UQ?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxNMWdkU0gzZGtHMzFwQUxfZ1VrRjdfQXctbnlleE1JMkJGQ1lFeWZfVUZrOTVLbmhTYW5DVklLVEU3MUVJdWxKRXQzdDVsOFRPenRRWFByM211SWQ5TzhuRFlvdmJiRWc5WXZTUElWZzVRbzg0N0dGVTlzU3V6OW5peDZkUTlPTlRCaDBFZGxUWmZHSVIwT2Mzd0J4TFoyZHptSzJ4R09nZndHeWRpUGJj?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNbFFHVHlsLWJnOWIta3lIQnBNdE9DVkhZbVJkM0NJbHFIUlpTeVJoSzhNODZadFI4WGNabEdxd29LeUh4ZEdFTmZRdU91Nm5hbGl2SlJHMWdVU2lSc3d5Mno3dlZILTRxSTVDMlNOVHBxTjJpU0ppUk9GNndIaTZIT0FmQ0dWRnFDU3l4VDhmUFlJZ2p3NjZLM053SGhFN29EVHhBTFRn?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQdEdUQURjRnlZNzNUZGhaVEMwVC01RFFab0xTb1ZaZ2l0d0tzUDJ1NDNiMWxPQ3BJSDV4cllLM0U2MFo5R3pWREc0TUxveHU0QmJSQ2g2THRPZ0xKNkhxelVVQUxKbmRQdGZuVG5vNFBDR2UwWmFZd0hWN1pjbXlsd1FjZDlhUUJ1QzVNcDBOUVlTc0hId0MwX0FhY21aMHM?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxQa1FBd3lLTDU1OE1vQzByRlphSWJZY05HS1ptZGpfZEgyMVJMQlVTMUt3LUVvWjRTYXpIbWUzMEdSN3BqUjJVdjBOb0J4X1ByMHpaZWxrX041NVFRalVPMnNvUXFoOG1qV1k2NXVPc1BubFRLcElDUGROTUdreldNSm5OOHd4anhIaGZKSmU3ZWZGUkc5TmZtWkpad3psdmZLMWRua3pFYTBnUzV0Uy0wUGo4Y2pEcGk0TzBmaWI5am53NENacFJHaGYtdFd3ZE3SAdQBQVVfeXFMT1BUY2dJbXFWeXBrbWIxV3Rlb0o2SWFtRkhYRGx2Y21rc2tGU3l2S1ZmVEpfaW0tb0QyLXdpSFdfdkpKWnU3UjlEMTZ3TkFiT2NRM19CVHlCa2dMRmlrQ2JMQ0tGbVVvYkRiaUpLZDh0UWxpWVlnblhhdTBfeEV4NXdPc1FHQUxZV2dtXzVURWpOcjJIY01jQkxHRUpmZmw0QzlWdk8xb2Z0bkFma3lNOWZySnFzZ2sxMEhhWkxRUlRZV2ZnZHVFeVh4UWx2VnE5el9qOEY?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
