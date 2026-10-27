# TSM Intelligence Report

- ticker: **TSM**
- Report as_of: **2026-10-26**
- Market data as_of: **2026-10-26**
- Quant sources: https://finance.yahoo.com/quote/TSM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TSM/key-statistics/
- AI analysis snapshot as_of: **2026-10-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-27T02:10:55.087709+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 21, 'rule': 4, 'ai': 10, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **10** exact headline/source/date matches; prior report **20261026T005504Z-6368ad31/TSM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 21 unique headlines; 7 named publishers; 4 exact duplicates; 21 HTTPS source links; largest publisher share 42.86%; oldest publication 2026-10-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 424.3700 |
| Return 1D (%) | 1.4002 |
| Return 1W (%) | 0.9876 |
| Return 1M (%) | -5.8232 |
| Return YTD (%) | 40.7439 |
| Return 1Y (%) | 45.3965 |
| Annualized volatility (%) | 39.2038 |
| Beta vs SPY | 2.1388 |
| Max drawdown (%) | -21.5466 |
| Sharpe (rf=0) | 1.1295 |
| Downside deviation (rf=0, %) | 26.0886 |
| Sortino (rf=0) | 1.6973 |
| Historical VaR 95% (1D, %) | 4.1447 |
| Historical ES 95% (1D, %) | 5.1216 |
| Correlation vs SPY | 0.6937 |
| Tracking error vs SPY (%) | 31.7324 |
| P/E (trailing) | 27.50 |
| P/B | 80.99 |
| EV/EBITDA | 3.99 |
| Revenue growth (%) | 50.90 |
| Forward P/E (estimate) | 18.15 |
| Gross margin (%) | 65.85 |
| Operating margin (%) | 58.66 |
| Return on equity (%) | 41.85 |
| Free cash flow yield (%) | N/A |
| MA50 | 433.6080 |
| Close vs MA50 (%) | -2.1305 |
| MA200 | 396.5948 |
| Close vs MA200 (%) | 7.0034 |
| RSI (14, Wilder) | 44.6049 |
| MACD (12,26) | -5.9652 |
| MACD signal (9) | -2.0949 |
| MACD histogram | -3.8703 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TSM': 268, 'SPY': 268}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 424.3700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.4002 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.9876 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -5.8232 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 40.7439 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 45.3965 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 39.2038 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.0886 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.6973 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.1447 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1216 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6937 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.7324 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.1388 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -21.5466 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1295 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 18.1469 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 65.8460 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 58.6550 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 41.8550 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 27.5029 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 44.6049 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.8703 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -2.1305 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 7.0034 -> Clearly above the moving-average trend level.

## TAILWINDS

### TSMC Debunks Irrational AI Fears As Pricing Power Expands (Rating Upgrade) (NYSE:TSM)
- Summary: TSMC Debunks Irrational AI Fears As Pricing Power Expands (Rating Upgrade) (NYSE:TSM)
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxPaVhFdlg4SFFKQ0sxVVcyMnNvdGxFYVNKOVRpMFRXNnhjV0txOGphTHR1Q2N5S0hRbUVoMWhKcE12Qlh4MEFjb2hKWDR0dUREb3Ywb1p4ZWFLcW8tQVRxdC1Xd2ZwVlRQRXpLS1MwUURibmxDYk14Slc3UV83NlNLLUl5ZVJGUUJWa0VKTl9RaFlUR3ZjNGpBSl9JX21kbFo5VVRVaEYzckRGZnVUYVhtVTZ1cw?oc=5>

### Taiwan Semiconductor Will Transition Into an Indispensible Utility of Global Computing Within 5 Years
- Summary: TSMC plans to become essential global computing utility within five years, driven by AI and data center demand.
- Date: 2026-10-23 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi3gFBVV95cUxQblNIRms1YWZKSjN1WENrYkttcUlzeDkwaVkyR0VBSFpDWlFtTktTSU1NNDM4YnJxRzJvTm9pbnEzZFV2UWxlYTRsa3BHMGNPZ1VkMVcyNW0zQm5BellRM0RMczZCZzVpeE5LYVFsVXZjeVVCSzRZWWY2ZU5zeDg4OG5uMC1yWlVidjFRU1VaMlh0T3VnSDNCdm1SbmVST0pRVTc5emJLN2wwU3JhQVM5TjJjdUs4d25QdWR5bjBzaHBGYlY3UTNOYjJWWlJoemxQTHR3XzQyY0NQczJMZFE?oc=5>

### Moody’s upgrades TSMC rating to Aa2 on booming AI demand and market dominance
- Summary: Moody’s raises TSMC’s rating to Aa2, citing AI demand and market dominance.
- Date: 2026-10-21 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQLVc5LUhMMkVUc0VSU2ZYUnVDUXQ1a0dPWE90a25OR3ZMdGVjLVNkQWlIN1JPck9mZUdIR1FTNHBQNk1KcV9MUHgyYUlocV82VlI2cGd2Zm5IU0tEZmNLTkNoU0dnVE1tVGpNUDlzVmR3cGZRdy12d2xkZ2lyWmtpRUZMNmxKNnBMTG51dElNVVoxRDh0eXB2dHRMYw?oc=5>

### TSMC Explores Rare Earth Alternatives To Protect Chip Production From China Controls
- Summary: TSMC seeks rare earth substitutes to reduce dependence on China, strengthening supply chain resilience.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOLXZraEZSc3pROFZjRTdkbkpJT0ZlRmY4eTlaVDQ3MFE4dmJ2ZU5LcnBJTTFpX0tDcGNUQTFZYUE1SVJBdzhvblhWSkxCa01LWmxkRF9ERV92NVo3Nk0wNi1mVDNrWlRMTmxRTUN0MlFFemJKRG94MGVlS2VkVlFacGk0YV9jTTNXdS1vM1pHZmRWTk9OZVhORWZjQ3FkU0U?oc=5>

### Taiwan Semiconductor Is Set to Cash in on AI. Here's What a $5,000 Investment Could Be Worth by 2030.
- Summary: TSMC’s AI focus could boost long‑term returns.
- Date: 2026-10-25 | Impact: high | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQYmpiWURNZUxWWjYwaFlnNjZWajVPTmhHekpuLS04TmNwRGgzTHlXbmhSZUROQ0R5U1NaUGs0b1NmR0N4VnZHbEFqT3BaNzVzVG9zQ2lkX0hiLU9pMktNQUxTT2Zhd1RRTHN0aU1iRkdmUVhtQy1RT29FVEJFVS0yaW1uNUhPQ0VDTkRaUjhvaGdWMlZZVHZPMw?oc=5>

## HEADWINDS

### Taiwan Semiconductor (TSMC) Posted Record Profit and the Stock Still Fell. Here's What the Market Is Worried About.
- Summary: Taiwan Semiconductor (TSMC) Posted Record Profit and the Stock Still Fell. Here's What the Market Is Worried About.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPUC14clR2aXF2cVFkUGpJWjYzNEFKYTlWQVBySmdMdUY4Y3QtQmNXbVlaVjVyWEpuNjNzbXlCRER4WVRyeFFwWGFHcXJPOFA3UGc5R1pNb05CX3V6ZkM4VWRibmdaRG9GN3NXbVBDTkZYZ1J2eUJSSkd5OWlza05OSnQ4TUE0VTNyOXhNTGtiSkRxd05xTmhB?oc=5>

### Intel and TSMC Are Vying for Chip Fabrication Supremacy. 1 Offers Superior Value.
- Summary: Intense competition may pressure TSMC’s market share.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQQnZxbWxFZzlVSmEzOGNXYnpRUDVyX3ZSTF9KYkI4d2JmVmdsbzlITUMyUG5zUDQ0UWdwcWw5c1hlako2MUJtbmp1VFYxWFg3cHhTMjl2OXprazhTUHpvOUI1VTJqaFBMUGh0bXZTRXRtZ0tJNFZmVjNNZV8wYzlsYTFvMXJ1WTUzNWRtWktwNGQtT0pxRmU2WnNwYXQ1NEE?oc=5>

### Taiwan Semiconductor Manufacturing (TSM) Stock Looks Pricey Against Cash Flow
- Summary: Valuation concerns relative to cash flow.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxORldEaFpNSnljQTZVWGtRUmV3X0R2QTZQTE9pNm0yWDlremFDNV85cHVhRnlZTy02c2Zkd0dsTTE0Zkx4LWJibjZVR0RHWlhZdy1WcHRVZ2dHQlpHOWxGWEVHUnlJRU5mcFVhU1FnWXk5TzB4ZFdMYjkzRDctYjJ0d0tYeGxfbHlBU1ducHNRZEFOYkwzZy1TTXRGNjRkcDlZZTUwcDNLdlZXSGFsb3c?oc=5>

## CATALYSTS

### Taiwan Semiconductor Manufacturing Company Ltd. $TSM Stock: Provident Investment Management Inc. Lowers Position
- Summary: Taiwan Semiconductor Manufacturing Company Ltd. $TSM Stock: Provident Investment Management Inc. Lowers Position
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi_gFBVV95cUxPUkM2VlRySDB4OGhrb1YxMFRzcDFNa3hpRjZ6SU96UzBjWGZ2WndERk9kSnhhb2g2TXh5V0dKZFpPM2FaUVFjMlRJT0tHcFRiVFNVUlJWYUV1aWJ5RzhWU2VCUWVkUEd5YWY0SnBYMEI4ZzFXck11NEYtRnZkRkNNVU9NbnhMRUFEVVlMb3pKZURwNVFfMDAyWC1QMmc1RWNpNFMtby1hWFRJcXVlSThEQkZSMFJlNG9EMHdzNTd2cGQxam1obUlHYzhrZUd3VGdRbkc4aVl4dmdveWpLcHZUMy1WblFGSDVSNENNZ29Ldl8xeGVLSlJvNHRxTENQZw?oc=5>

### Taiwan Semiconductor Manufacturing Company Ltd. $TSM Shares Acquired by Loring Wolcott & Coolidge Fiduciary Advisors LLP MA
- Summary: Taiwan Semiconductor Manufacturing Company Ltd. $TSM Shares Acquired by Loring Wolcott & Coolidge Fiduciary Advisors LLP MA
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAJBVV95cUxPcjNuRjZuSG1Xd2tDNzRNVm9DaDI4eExXM19NbHhkZjh5OGRZYXFFWnZmQlhOX0F0cFQxckljNFhETW9TaXBHWkoyNzBaY25kLVVDZG9TbldoY1dsOEl4c1ZfWGx4OXpPcDQyQmd0X2pETWdHQ1BFaXJnTVZoZGxyZzVQZEhNU2pHNkZOLVNrUHBDTVdTUU9lMnNkTFpfNi0wR2lZeFk1ai1sU3VYbmFJSEpYUlVpcDJhYm1UNUprTGcxNng3VmtXOURFVkl3cnlqTnEtaVRBMlBQUnVhOGNlbWMtUHZWQWRIR3hEcVh4MUNkUDE5eFhYU1d2S0s2RUFEa18zOXFRSGh5Mlkz?oc=5>

### What's Going On With Taiwan Semiconductor Stock Friday?
- Summary: Inquiry about TSM stock performance on Friday.
- Date: 2026-10-23 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxQV1hWNFFIMUw3cmE2SlhnZUJYcXgtaGVjYV96SjJDWjBaV1JWUlJxNWw1WGR0VTNreXRaS09MTGxCdWMzc3dfa0tsd09FdE5LeVA0aWdMQmV4eFRqMjNXM21kNmRHVnlFb2Y2OEVjTy1tVVVMVUJ1dkxDaFc0SlhkRmZZMGJNN1hDYl8tSlc5eVkxdDFjQ1d1b19KaUtOc1ZhSjl4bnJZS2o0Q3Vi?oc=5>

### Taiwan Semiconductor Manufacturing (TSM) Draws Fund Managers Leaving Firms To Invest Personally
- Summary: TSM attracts fund managers who are investing their own money in the company.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxQNWwxM1BhNzBha1B4WGV1WDllaDBXMVByYW9peGwxSmE0WWotQ09qQWlhc3RFMS1TTkhIbDBEcXZGZ2FIRXVlX3Q1UkRDUTJXbjlZNFI0YXcwTVV1OWZXVUhBYTk5bnlqWVJXQUlCUzlxSGVPaVg5UFV3WjVzbnZTV0l3VTNmSG1YbXVNNUdtTnB5cVEtWVRJcFlSbTEzTUNIWUpfcWZKMU1tdzd5alE?oc=5>

### This Company Behind the World’s AI Chips Could Be a Huge Winner
- Summary: TSM may become a major AI chip supplier, enhancing its market position.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxQbldrdE92SjNYOC1XekxDRkJsZEJYa0hFNnBjN3NHSncwUnJPR0EwX1F4TmJjNUFTR1BJMFZCWHRteG1nVk13eGpJNUxYeHlSZzVIN0paZW43YWNCc3B2aVVaWTJ4N3k2NU80ZjUwa3ZYRUJxQXItajVaQmFjTXMtX2M1UHBjOFNIMFNPanIwcFhKZk5qZzRFUlQ5V0NGUE5IUi11MEdRN0cyUQ?oc=5>

### TSMC (TSM) Stock Forecast: June Revenue Up 68%, Q2 Earnings Tomorrow; Is $438 the Next Stop?
- Summary: TSMC forecasts 68% revenue growth for June and upcoming Q2 earnings, suggesting a potential price target of $438.
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxNZ1JnUDhUX2U1ZXlyTk1ZZlJZQUlCanB0VnhQVTE2RktleVdTd2Z5a2JxS25KZGJuYTIzc1duU2lvVkZXMU16WlVSRzB3a2tkQW11czBQUF80VFdJX1pQM2tBelY1akNLaEZlbXF3QVJ5eVNKNGM2TWh1S3ByREV5TDBmUmRTT05kSDNxMXhaZVhDSEhOYXc4WjRJVm9CN0xaLTVQbW1RLWR5WXhzb1RhZ0dFRFdCM3ltVmx3dy1VQ3JqSFlnMjU0ejFGN2V1cWNa?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TSM** | **27.50** | **80.99** | **3.99** | **50.90** | **2,200,983,830,528.00 USD** | **45.40** |
| UMC | 19.37 | 3.52 | -0.33 | 17.00 | 48,101,687,296.00 USD | 158.85 |
| GFS | 35.16 | 2.09 | 12.15 | 5.80 | 25,083,838,464.00 USD | 27.91 |
| INTC | N/A | 5.21 | 29.26 | 25.40 | 478,233,919,488.00 USD | 136.34 |

Peers fetched as_of: 2026-10-26; TSM reuses existing data (market data as_of: 2026-10-26); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-26

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: N/A
- Filing date: N/A
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: N/A

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiswFBVV95cUxPaVhFdlg4SFFKQ0sxVVcyMnNvdGxFYVNKOVRpMFRXNnhjV0txOGphTHR1Q2N5S0hRbUVoMWhKcE12Qlh4MEFjb2hKWDR0dUREb3Ywb1p4ZWFLcW8tQVRxdC1Xd2ZwVlRQRXpLS1MwUURibmxDYk14Slc3UV83NlNLLUl5ZVJGUUJWa0VKTl9RaFlUR3ZjNGpBSl9JX21kbFo5VVRVaEYzckRGZnVUYVhtVTZ1cw?oc=5
- https://news.google.com/rss/articles/CBMi3gFBVV95cUxQblNIRms1YWZKSjN1WENrYkttcUlzeDkwaVkyR0VBSFpDWlFtTktTSU1NNDM4YnJxRzJvTm9pbnEzZFV2UWxlYTRsa3BHMGNPZ1VkMVcyNW0zQm5BellRM0RMczZCZzVpeE5LYVFsVXZjeVVCSzRZWWY2ZU5zeDg4OG5uMC1yWlVidjFRU1VaMlh0T3VnSDNCdm1SbmVST0pRVTc5emJLN2wwU3JhQVM5TjJjdUs4d25QdWR5bjBzaHBGYlY3UTNOYjJWWlJoemxQTHR3XzQyY0NQczJMZFE?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQLVc5LUhMMkVUc0VSU2ZYUnVDUXQ1a0dPWE90a25OR3ZMdGVjLVNkQWlIN1JPck9mZUdIR1FTNHBQNk1KcV9MUHgyYUlocV82VlI2cGd2Zm5IU0tEZmNLTkNoU0dnVE1tVGpNUDlzVmR3cGZRdy12d2xkZ2lyWmtpRUZMNmxKNnBMTG51dElNVVoxRDh0eXB2dHRMYw?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOLXZraEZSc3pROFZjRTdkbkpJT0ZlRmY4eTlaVDQ3MFE4dmJ2ZU5LcnBJTTFpX0tDcGNUQTFZYUE1SVJBdzhvblhWSkxCa01LWmxkRF9ERV92NVo3Nk0wNi1mVDNrWlRMTmxRTUN0MlFFemJKRG94MGVlS2VkVlFacGk0YV9jTTNXdS1vM1pHZmRWTk9OZVhORWZjQ3FkU0U?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQYmpiWURNZUxWWjYwaFlnNjZWajVPTmhHekpuLS04TmNwRGgzTHlXbmhSZUROQ0R5U1NaUGs0b1NmR0N4VnZHbEFqT3BaNzVzVG9zQ2lkX0hiLU9pMktNQUxTT2Zhd1RRTHN0aU1iRkdmUVhtQy1RT29FVEJFVS0yaW1uNUhPQ0VDTkRaUjhvaGdWMlZZVHZPMw?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPUC14clR2aXF2cVFkUGpJWjYzNEFKYTlWQVBySmdMdUY4Y3QtQmNXbVlaVjVyWEpuNjNzbXlCRER4WVRyeFFwWGFHcXJPOFA3UGc5R1pNb05CX3V6ZkM4VWRibmdaRG9GN3NXbVBDTkZYZ1J2eUJSSkd5OWlza05OSnQ4TUE0VTNyOXhNTGtiSkRxd05xTmhB?oc=5
- https://news.google.com/rss/articles/CBMioAJBVV95cUxOTFdKNmpUR3BlVVlPSEtxNV80Z1BSa3FXZ0RYMExXU2JieDNhV0xqcVM4RXNUNmRNZk43TldnT1VaYlp3ZDFHQnctR3FWbFFVd1hVNDNDUW1rMVFWWVUzQmdZT09GdFlmZExPSUp6N2g2M3VkVnhlZFBtU1M2dGpuZ0ZFWkVKX1h0YUJfVmZxTDNrZXJLZlFCT3NqbjNZS2JBMExBaU93NVNwc05iZmhBb0ZDdVc5LXdMSkFfMDF5d2dQU2p4d3pFTlZYSUhkdGt4bnpmV3JmdXBfaHVBNDFMZ2xTaXFPcG54dElpRlprV3pZMGRzLUU0bU5UTEdxTnh1UU9NbkZidVhLVXpFUFA3N1N1RFJiSjI3ellBS0FHX3g?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQQnZxbWxFZzlVSmEzOGNXYnpRUDVyX3ZSTF9KYkI4d2JmVmdsbzlITUMyUG5zUDQ0UWdwcWw5c1hlako2MUJtbmp1VFYxWFg3cHhTMjl2OXprazhTUHpvOUI1VTJqaFBMUGh0bXZTRXRtZ0tJNFZmVjNNZV8wYzlsYTFvMXJ1WTUzNWRtWktwNGQtT0pxRmU2WnNwYXQ1NEE?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNWUVWd0NpUkZTdTZPSFZKSXBvLWIxMlNnZnNqam9qVFMwNHc1OWgxdk1KMGpDZHJzektLUjZQdXduQnZuQ1ZacnE3WWZ2dnNtVGs5WTdYcWRzcUZmQTNnZTZOcUNjOXNBZkNPckNQRzZVMHYzUThfaEJQblE2UGpjWnU5cDBFTnN1VmRpcXMxb3NSbUNo?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxORldEaFpNSnljQTZVWGtRUmV3X0R2QTZQTE9pNm0yWDlremFDNV85cHVhRnlZTy02c2Zkd0dsTTE0Zkx4LWJibjZVR0RHWlhZdy1WcHRVZ2dHQlpHOWxGWEVHUnlJRU5mcFVhU1FnWXk5TzB4ZFdMYjkzRDctYjJ0d0tYeGxfbHlBU1ducHNRZEFOYkwzZy1TTXRGNjRkcDlZZTUwcDNLdlZXSGFsb3c?oc=5
- https://news.google.com/rss/articles/CBMi_gFBVV95cUxPUkM2VlRySDB4OGhrb1YxMFRzcDFNa3hpRjZ6SU96UzBjWGZ2WndERk9kSnhhb2g2TXh5V0dKZFpPM2FaUVFjMlRJT0tHcFRiVFNVUlJWYUV1aWJ5RzhWU2VCUWVkUEd5YWY0SnBYMEI4ZzFXck11NEYtRnZkRkNNVU9NbnhMRUFEVVlMb3pKZURwNVFfMDAyWC1QMmc1RWNpNFMtby1hWFRJcXVlSThEQkZSMFJlNG9EMHdzNTd2cGQxam1obUlHYzhrZUd3VGdRbkc4aVl4dmdveWpLcHZUMy1WblFGSDVSNENNZ29Ldl8xeGVLSlJvNHRxTENQZw?oc=5
- https://news.google.com/rss/articles/CBMijAJBVV95cUxPcjNuRjZuSG1Xd2tDNzRNVm9DaDI4eExXM19NbHhkZjh5OGRZYXFFWnZmQlhOX0F0cFQxckljNFhETW9TaXBHWkoyNzBaY25kLVVDZG9TbldoY1dsOEl4c1ZfWGx4OXpPcDQyQmd0X2pETWdHQ1BFaXJnTVZoZGxyZzVQZEhNU2pHNkZOLVNrUHBDTVdTUU9lMnNkTFpfNi0wR2lZeFk1ai1sU3VYbmFJSEpYUlVpcDJhYm1UNUprTGcxNng3VmtXOURFVkl3cnlqTnEtaVRBMlBQUnVhOGNlbWMtUHZWQWRIR3hEcVh4MUNkUDE5eFhYU1d2S0s2RUFEa18zOXFRSGh5Mlkz?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxQV1hWNFFIMUw3cmE2SlhnZUJYcXgtaGVjYV96SjJDWjBaV1JWUlJxNWw1WGR0VTNreXRaS09MTGxCdWMzc3dfa0tsd09FdE5LeVA0aWdMQmV4eFRqMjNXM21kNmRHVnlFb2Y2OEVjTy1tVVVMVUJ1dkxDaFc0SlhkRmZZMGJNN1hDYl8tSlc5eVkxdDFjQ1d1b19KaUtOc1ZhSjl4bnJZS2o0Q3Vi?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxQNWwxM1BhNzBha1B4WGV1WDllaDBXMVByYW9peGwxSmE0WWotQ09qQWlhc3RFMS1TTkhIbDBEcXZGZ2FIRXVlX3Q1UkRDUTJXbjlZNFI0YXcwTVV1OWZXVUhBYTk5bnlqWVJXQUlCUzlxSGVPaVg5UFV3WjVzbnZTV0l3VTNmSG1YbXVNNUdtTnB5cVEtWVRJcFlSbTEzTUNIWUpfcWZKMU1tdzd5alE?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxQbldrdE92SjNYOC1XekxDRkJsZEJYa0hFNnBjN3NHSncwUnJPR0EwX1F4TmJjNUFTR1BJMFZCWHRteG1nVk13eGpJNUxYeHlSZzVIN0paZW43YWNCc3B2aVVaWTJ4N3k2NU80ZjUwa3ZYRUJxQXItajVaQmFjTXMtX2M1UHBjOFNIMFNPanIwcFhKZk5qZzRFUlQ5V0NGUE5IUi11MEdRN0cyUQ?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxNZ1JnUDhUX2U1ZXlyTk1ZZlJZQUlCanB0VnhQVTE2RktleVdTd2Z5a2JxS25KZGJuYTIzc1duU2lvVkZXMU16WlVSRzB3a2tkQW11czBQUF80VFdJX1pQM2tBelY1akNLaEZlbXF3QVJ5eVNKNGM2TWh1S3ByREV5TDBmUmRTT05kSDNxMXhaZVhDSEhOYXc4WjRJVm9CN0xaLTVQbW1RLWR5WXhzb1RhZ0dFRFdCM3ltVmx3dy1VQ3JqSFlnMjU0ejFGN2V1cWNa?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
