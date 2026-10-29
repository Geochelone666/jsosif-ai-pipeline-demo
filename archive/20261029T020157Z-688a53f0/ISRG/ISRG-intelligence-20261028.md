# ISRG Intelligence Report

- ticker: **ISRG**
- Report as_of: **2026-10-28**
- Market data as_of: **2026-10-28**
- Quant sources: https://finance.yahoo.com/quote/ISRG/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ISRG/key-statistics/
- AI analysis snapshot as_of: **2026-10-28**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-29T02:18:34.484744+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 4, 'ai': 9, 'unknown': 0, 'irrelevant': 11})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **13** exact headline/source/date matches; prior report **20261028T015717Z-533e470c/ISRG** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 10 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 29.17%; oldest publication 2026-10-21

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 444.1800 |
| Return 1D (%) | -0.3813 |
| Return 1W (%) | 3.7513 |
| Return 1M (%) | 7.0855 |
| Return YTD (%) | -21.5729 |
| Return 1Y (%) | -18.5574 |
| Annualized volatility (%) | 33.9787 |
| Beta vs SPY | 0.8773 |
| Max drawdown (%) | -43.9960 |
| Sharpe (rf=0) | -0.4342 |
| Downside deviation (rf=0, %) | 25.6409 |
| Sortino (rf=0) | -0.5753 |
| Historical VaR 95% (1D, %) | 2.8853 |
| Historical ES 95% (1D, %) | 5.0452 |
| Correlation vs SPY | 0.3280 |
| Tracking error vs SPY (%) | 32.1370 |
| P/E (trailing) | 53.71 |
| P/B | 9.63 |
| EV/EBITDA | 33.57 |
| Revenue growth (%) | 21.70 |
| Forward P/E (estimate) | 35.67 |
| Gross margin (%) | 66.64 |
| Operating margin (%) | 33.29 |
| Return on equity (%) | 17.93 |
| Free cash flow yield (%) | 2.19 |
| MA50 | 399.3718 |
| Close vs MA50 (%) | 11.2197 |
| MA200 | 434.2000 |
| Close vs MA200 (%) | 2.2985 |
| RSI (14, Wilder) | 64.2523 |
| MACD (12,26) | 13.6432 |
| MACD signal (9) | 12.6243 |
| MACD histogram | 1.0189 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ISRG': 270, 'SPY': 270}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 444.1800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.3813 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 3.7513 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 7.0855 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -21.5729 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -18.5574 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 33.9787 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 25.6409 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.5753 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8853 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.0452 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3280 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.1370 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.8773 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -43.9960 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.4342 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 35.6716 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 66.6420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 33.2860 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 17.9320 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.1889 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 53.7098 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 64.2523 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.0189 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 11.2197 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 2.2985 -> Slightly above the moving-average trend level.

## TAILWINDS

### Intuitive Surgical (ISRG) Could Be 24% Above Fair Value As Earnings Split The Market
- Summary: Earnings suggest ISRG may be undervalued, indicating potential upside.
- Date: 2026-10-27 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxNSGxRNkt3UTdSSmFBX2wzamstRjdPamFrWHVmdmtQZ3R1bGRtUVRPWUFDRkJDSHFJQUpENzdzc2x0bUkyek1TWUN1TkNrY0ROdUI1QkdpMDdtWENqWUcxZjR3V2JQM1NqODlOTTkwMXdhSVRxV3NnMkJEYm1DZTF1bTlsci1sZkFuMzJjWjROa1AyZGZLOVVrSGJRd012azA4VWpxWm81cnhRM0g5RU1wblVWa1lMR3pqeXdsd1FYa3FHNGQyYmtiWWRMVlRlZkNKeF9TWjFR0gHbAUFVX3lxTE9kRDlUbzNEbmFlU0REd1E2bkFyQ3YxNzRScjlGbDYtR1NiSnh2TDJEcWdTelFpRXl6bkt6eFlzc0xxT011S2wzM191WU5wTEdfNGF4TnNTSGNxa1dLUlVHSURMNG13b3JZc0RDQzJtNlpLcDlyVUJZRVZ3MzZaQnJtZmEzeWFFd3NYSFluSE4yNXdDdFNMR2xpUTh6VEtDS1Y5YUhlbEpSQXZPZ2gtM0lEdUVCMGRTU1k2MEZyaWUxQk9pdmgyTU5LdEJpU3ZieWJsUkc1RXd2enhNaw?oc=5>

### Intuitive Surgical (ISRG) Receives a Buy from RBC Capital
- Summary: RBC Capital upgrades Intuitive Surgical to a buy, signaling confidence in its future prospects.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxQcGdkZjdsWlVmbExNZzAtbXNQc1dfdFp4S1FYaXNRZnlLVXhIZXIwckhIem5YZnBpd1l5YS12Tk9ET0xsMmRKWWRFTmExSDB2V3FIQkJKSll2dm01TnZYTzcwXzJLMDFQMHljS3NWVGJ4RC1tRGhYejctc296TmRyenJYenp2dVFOTjNndkdjWkhGa0lCcDBSejdHejNTc1V5NURBTmFkVEpGejY5VGEzLXBvT2N6TW1mQW1xc2dTYjFEQU81ZEhVNWFCVTJ3WkljY1hoWmM3UQ?oc=5>

## HEADWINDS

### Intuitive Surgical stock drops after Q3 beat (ISRG:NASDAQ)
- Summary: Intuitive Surgical stock drops after Q3 beat (ISRG:NASDAQ)
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxOaHNmbUs4MTcwdVdmcVQ5cTFraThfY0xXTFdpbzkwMVU2R050cTdVRndfR05uSTMwYXltanJHOFhRcXFsLTBweGpGY0txS2l6MDQ3STc4U2xTMzFDN2NXTVlZRExDbldkRnVaa1pUZUp5dlZ2d2UtdkdNMU9Oc3d5dlJ3?oc=5>

## CATALYSTS

### Intuitive Surgical (ISRG) Stock Faces A Q3 Earnings Valuation Reality Check
- Summary: Intuitive Surgical (ISRG) Stock Faces A Q3 Earnings Valuation Reality Check
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQU0JGbU5VQ1dmVmRnVi1URXY3VWpxT3otdU9LUzRhRm9xZUlzbGlzR3VGSFB6VDI1WHk3SlNsa2x2MjFrbVduQ2R3SVY3bVIwdUg1Z2VyQ3ZxaUVkN0dEMVlTUzhQUlV2TjVfNjVnLXE5WjNvY0FPbnA1MHNqRHNMR2UxSDhnYUM5SXZTdHZwdmhlY3lGSUgwYjZXU0dZdlI4Zmc?oc=5>

### Intuitive Surgical (ISRG) Insider Sale: SVP Chief Human Resource
- Summary: Intuitive Surgical (ISRG) Insider Sale: SVP Chief Human Resource
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi6wFBVV95cUxQamx6UHcwVVd0Uno3aVhvcHc4c291YWl0N08wZlViSnFfYTRMTmFPa1VVcnlRd0lpREg4QVd2MXlHeDNNanpqQTF0eEdnTWVia3FoRUEwXzkwWFFFWGpDUFB3UGlWWmFCZC1Zd0FUZjdTcVlCcFRQSTFFdktYTmRMNW81SVhISmZVaHAxSWhSUnJMNUx2Wm5jckFhOGNsM2l4WG9LSXZOOXNXR2ExQnhQLWhrSjB0cEczQzlHYk5OaTRnSjJWcTB6Mzhtb2dKWl82d0hBVW85YTdGNEdrV0VGeVFtZkt0aEJHbDNR?oc=5>

### Intuitive Surgical, Inc. 2026 Q3 - Results - Earnings Call Presentation (NASDAQ:ISRG) 2026-10-23
- Summary: Intuitive Surgical, Inc. 2026 Q3 - Results - Earnings Call Presentation (NASDAQ:ISRG) 2026-10-23
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPTmpjcE5OT1pBOXJ4aGFzZkhja3VhUi1TcV9tNEI0cUd1TVVUeHF1ZzlNczhHWUplMkZqQXhHNDBELVdXTVZXU24yaHRVRTVPa0JTQW9tZnRadXN1MGNVTWhrQU5zUFcwZ2JaRVZNbFNQcHhNdkpJX0tNRTRhRzNUNUJON2pzY01DQ2ZUMVRlZkVGMmNTdmFMZFRuM1hpelpWVDRzUHdGQjBRZw?oc=5>

### Intuitive Surgical (ISRG) Shares Dip Despite Strong Q3 Results o
- Summary: Shares fell after Q3 earnings, despite strong results, indicating market concerns about future growth.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxPVElCY21walNRbE1pRW15Wkx4ZnlZelNFamRpbC04cEdlTVBzejFYdGVqU2V5THhCOUFfSjBmTUk1NGR3RWVQQm80ZGxHb3F2TzYza2swN1RrSDdybllxbE9CSHF2aWtYbnl5czZDTnhmRllQeTllMWo0MVZ3cmVEelJ5ZjJ6dWFiQi1teFJ3aVlFZHJmclpOSEJuSE12cjdLakdWeVphZXV0cWZZZHFQRnowVy1zeDdQ?oc=5>

### Intuitive Surgical (ISRG) Stock Looks Reasonable After Mixed Q3 Results
- Summary: Mixed Q3 results prompt a reassessment of ISRG’s valuation, suggesting a reasonable price target for investors.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxOdDRpdU9FbjgxbEJxbHVOSy1wTE9UazRNSG1Nc3AwaXRSTUJQR2lISUhyNzltWUZ6MWpFRXlRVWZkMk5uc2xZYnNkSXEzWUFoZUh0MEdiZTVwVVoxU190cmk5WGNUMlRyUTZxLXBIaTNDSUhybG9JRzFmcU5ibDNNenZRc1N0UUJCNmhwMXIwZFV3alpRalFpSmtjTkVfdFYtMUl5YWNFbXZUek5WMWlvZmFkb3ZyenhLMDlxSVkxck1JeDNMXzY3dE9nRWpMd2tGTEN4V0pB0gHbAUFVX3lxTFBEcm1NRjkyem5SRk52RVN6dUdBNHhDRXBXWnZNUzJJU0NadVNZWFFVR3ZMdGwyWVcwVENFd3N3RHB1bVlDV3FNMGRtT28yeUdHSjNzcC1mT0NfV3VEWFowbTE2WVpOUlFValduNnRBT0F4UFgydWNfQXpwVUVLVTZGc2Zvckh6ZDJJc1Yxeng4eUFiVkNiaHZDNlZDUzlKNWhzNmdydlpsc2JUc2lXRDM4bEFMLTNZSkJ6MWdHNHRHZllTN29rLU40T3c4bGNrekNaWG5TLUR2UEMwdw?oc=5>

### Intuitive Surgical Q3: The Best Way To Grow May Be To Charge Less (NASDAQ:ISRG)
- Summary: Intuitive Surgical reports Q3 results, suggesting growth strategy may involve pricing adjustments to boost revenue.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxNYkxpeXRwTS1ZRVhrQzVyN01NUW56cWk5Sk9IUWkxMkRmRmRtdGp2QjQtZF9NVk1vTWJJMlZtY2Jla3V1Q3B0Ul9WeTRGeWxDVkNoaGVmOFZTZ0RZemxiTk5iR1IxVzRsRmdjeE5EYXlEWVBiSG1JdUJLVk0yMkhOZTVlRmtfTTZxSGZ5Q01pMWRRYkpocHMzcWlsN1daT1I5b0ZBMlBoWWw?oc=5>

### An EVP sold 61 shares per sale under a trading plan at Intuitive Surgical (ISRG).
- Summary: EVP sold 61 shares under a trading plan, indicating insider activity.
- Date: 2026-10-28 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxNN2ZfRVV6SE1yX3g4WGw4a1kxdmZMTmZuWlAxRnd0ak5kd0k5TnQtWGlCU0E0UW1Hb2JtWTY3Slk3UmVzTGFoZVNwVEF3V1N5OUdLOWxwY0p3VWlyTkYxVWZUWnBOdXpneERzRXg0VHM5dUllZEFKZ3VjemVBRnl5T3JoZmJnQmtTRnpiTEN6eFZCc3N0WDYwV05TRkgzd3A4R3YwR1NfWnlhZ0wzZTNXQUhfck9lNVk?oc=5>

### Intuitive Surgical Insider Sold Shares Worth $1,834,124, According to a Recent SEC Filing
- Summary: Insider sold shares worth $1.8M, reflecting ownership change.
- Date: 2026-10-26 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxNWXBYLXU5eHRVeFphS2NhSXpOdXlfc2tldkhQZXRNVlMzTUFSM1VjNGRhU3lRbnJoZ2x6NUg0SVFwaV80cnVpcnlUVW56SGxrT2dQZkJjT1c1ZzNtcl9aVlBSQlJiM1UtQWdiOFBzNlVpSHpycVpfY1NCSlE0N2lsbUJUZGtmNGVSUWs2YzdmeVNLTGQySlliZktyX0NzVThMRTRtTDFFY3NwN25GbEFCdg?oc=5>

### After selling 20,095 shares, Intuitive Surgical (ISRG) director Gary S. Guthart's trust holds 1,204,530.
- Summary: Director sold 20,095 shares; trust retains 1.2M shares, showing insider ownership shift.
- Date: 2026-10-26 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxPYkxQbk01d3gxbjRyR1F1aVpZODJ5Z1F3NFNPRUhFbnBjeWZ3Q3lONHctSXY1bE5hWGhlV0c5MEVoTXpMR01xRENuMHp4SHdnQlZJd0s5TTItaFh2R1F4TndKRjNPd1RjdVRVRzM5bHBfUkNvU2RCV1laS0lhUzRKSjFLbjRhQnpaOWpmVFpzWVVIbDNEaTEtM3pYUlFOeG9LY0hmV2hmTXl1X052MTRsOGhQWGpycWs?oc=5>

## RISKS

### Robotics Titan Hammered On Elevated Buy-Side Views
- Summary: Elevated buy-side expectations lead to a sharp decline in ISRG shares, indicating potential downside risk.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPbFQ1cWh6R3FnQ3BUZWJlMHNqazZUeExEN1RkQUMzeDBPcHgyOGxfZHI2eV82RkxQcWVXV2h2MDVOcWZaeGNEOEZDN29GcmdLTDR2S1lMaHpoTDFGQ1VjYTBxS010bkZGbmV1aGxmSW5tcFEyUTFzb3FrQno2aE5WV1JDMHlaU2FndDVRNHZYYkZ1alV3eWQ4RHEyb0ZCWnEtZlJmaDl3?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ISRG** | **53.71** | **9.63** | **33.57** | **21.70** | **156,919,037,952.00 USD** | **-18.56** |
| MDT | 23.29 | 2.42 | 13.56 | 13.70 | 121,236,692,992.00 USD | 5.03 |
| SYK | 31.50 | 4.86 | 17.43 | 9.40 | 116,606,205,952.00 USD | -18.24 |
| BSX | 18.21 | 2.60 | 13.59 | 7.50 | 61,490,810,880.00 USD | -57.98 |

Peers fetched as_of: 2026-10-28; ISRG reuses existing data (market data as_of: 2026-10-28); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-20
- Next expected earnings: 2027-01-21 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-28

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 3,048,700,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 522,800,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1035267/000103526726000071/isrg-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi1gFBVV95cUxNSGxRNkt3UTdSSmFBX2wzamstRjdPamFrWHVmdmtQZ3R1bGRtUVRPWUFDRkJDSHFJQUpENzdzc2x0bUkyek1TWUN1TkNrY0ROdUI1QkdpMDdtWENqWUcxZjR3V2JQM1NqODlOTTkwMXdhSVRxV3NnMkJEYm1DZTF1bTlsci1sZkFuMzJjWjROa1AyZGZLOVVrSGJRd012azA4VWpxWm81cnhRM0g5RU1wblVWa1lMR3pqeXdsd1FYa3FHNGQyYmtiWWRMVlRlZkNKeF9TWjFR0gHbAUFVX3lxTE9kRDlUbzNEbmFlU0REd1E2bkFyQ3YxNzRScjlGbDYtR1NiSnh2TDJEcWdTelFpRXl6bkt6eFlzc0xxT011S2wzM191WU5wTEdfNGF4TnNTSGNxa1dLUlVHSURMNG13b3JZc0RDQzJtNlpLcDlyVUJZRVZ3MzZaQnJtZmEzeWFFd3NYSFluSE4yNXdDdFNMR2xpUTh6VEtDS1Y5YUhlbEpSQXZPZ2gtM0lEdUVCMGRTU1k2MEZyaWUxQk9pdmgyTU5LdEJpU3ZieWJsUkc1RXd2enhNaw?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxQcGdkZjdsWlVmbExNZzAtbXNQc1dfdFp4S1FYaXNRZnlLVXhIZXIwckhIem5YZnBpd1l5YS12Tk9ET0xsMmRKWWRFTmExSDB2V3FIQkJKSll2dm01TnZYTzcwXzJLMDFQMHljS3NWVGJ4RC1tRGhYejctc296TmRyenJYenp2dVFOTjNndkdjWkhGa0lCcDBSejdHejNTc1V5NURBTmFkVEpGejY5VGEzLXBvT2N6TW1mQW1xc2dTYjFEQU81ZEhVNWFCVTJ3WkljY1hoWmM3UQ?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxOaHNmbUs4MTcwdVdmcVQ5cTFraThfY0xXTFdpbzkwMVU2R050cTdVRndfR05uSTMwYXltanJHOFhRcXFsLTBweGpGY0txS2l6MDQ3STc4U2xTMzFDN2NXTVlZRExDbldkRnVaa1pUZUp5dlZ2d2UtdkdNMU9Oc3d5dlJ3?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQU0JGbU5VQ1dmVmRnVi1URXY3VWpxT3otdU9LUzRhRm9xZUlzbGlzR3VGSFB6VDI1WHk3SlNsa2x2MjFrbVduQ2R3SVY3bVIwdUg1Z2VyQ3ZxaUVkN0dEMVlTUzhQUlV2TjVfNjVnLXE5WjNvY0FPbnA1MHNqRHNMR2UxSDhnYUM5SXZTdHZwdmhlY3lGSUgwYjZXU0dZdlI4Zmc?oc=5
- https://news.google.com/rss/articles/CBMi6wFBVV95cUxQamx6UHcwVVd0Uno3aVhvcHc4c291YWl0N08wZlViSnFfYTRMTmFPa1VVcnlRd0lpREg4QVd2MXlHeDNNanpqQTF0eEdnTWVia3FoRUEwXzkwWFFFWGpDUFB3UGlWWmFCZC1Zd0FUZjdTcVlCcFRQSTFFdktYTmRMNW81SVhISmZVaHAxSWhSUnJMNUx2Wm5jckFhOGNsM2l4WG9LSXZOOXNXR2ExQnhQLWhrSjB0cEczQzlHYk5OaTRnSjJWcTB6Mzhtb2dKWl82d0hBVW85YTdGNEdrV0VGeVFtZkt0aEJHbDNR?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPTmpjcE5OT1pBOXJ4aGFzZkhja3VhUi1TcV9tNEI0cUd1TVVUeHF1ZzlNczhHWUplMkZqQXhHNDBELVdXTVZXU24yaHRVRTVPa0JTQW9tZnRadXN1MGNVTWhrQU5zUFcwZ2JaRVZNbFNQcHhNdkpJX0tNRTRhRzNUNUJON2pzY01DQ2ZUMVRlZkVGMmNTdmFMZFRuM1hpelpWVDRzUHdGQjBRZw?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxPVElCY21walNRbE1pRW15Wkx4ZnlZelNFamRpbC04cEdlTVBzejFYdGVqU2V5THhCOUFfSjBmTUk1NGR3RWVQQm80ZGxHb3F2TzYza2swN1RrSDdybllxbE9CSHF2aWtYbnl5czZDTnhmRllQeTllMWo0MVZ3cmVEelJ5ZjJ6dWFiQi1teFJ3aVlFZHJmclpOSEJuSE12cjdLakdWeVphZXV0cWZZZHFQRnowVy1zeDdQ?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxOdDRpdU9FbjgxbEJxbHVOSy1wTE9UazRNSG1Nc3AwaXRSTUJQR2lISUhyNzltWUZ6MWpFRXlRVWZkMk5uc2xZYnNkSXEzWUFoZUh0MEdiZTVwVVoxU190cmk5WGNUMlRyUTZxLXBIaTNDSUhybG9JRzFmcU5ibDNNenZRc1N0UUJCNmhwMXIwZFV3alpRalFpSmtjTkVfdFYtMUl5YWNFbXZUek5WMWlvZmFkb3ZyenhLMDlxSVkxck1JeDNMXzY3dE9nRWpMd2tGTEN4V0pB0gHbAUFVX3lxTFBEcm1NRjkyem5SRk52RVN6dUdBNHhDRXBXWnZNUzJJU0NadVNZWFFVR3ZMdGwyWVcwVENFd3N3RHB1bVlDV3FNMGRtT28yeUdHSjNzcC1mT0NfV3VEWFowbTE2WVpOUlFValduNnRBT0F4UFgydWNfQXpwVUVLVTZGc2Zvckh6ZDJJc1Yxeng4eUFiVkNiaHZDNlZDUzlKNWhzNmdydlpsc2JUc2lXRDM4bEFMLTNZSkJ6MWdHNHRHZllTN29rLU40T3c4bGNrekNaWG5TLUR2UEMwdw?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxNYkxpeXRwTS1ZRVhrQzVyN01NUW56cWk5Sk9IUWkxMkRmRmRtdGp2QjQtZF9NVk1vTWJJMlZtY2Jla3V1Q3B0Ul9WeTRGeWxDVkNoaGVmOFZTZ0RZemxiTk5iR1IxVzRsRmdjeE5EYXlEWVBiSG1JdUJLVk0yMkhOZTVlRmtfTTZxSGZ5Q01pMWRRYkpocHMzcWlsN1daT1I5b0ZBMlBoWWw?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxNN2ZfRVV6SE1yX3g4WGw4a1kxdmZMTmZuWlAxRnd0ak5kd0k5TnQtWGlCU0E0UW1Hb2JtWTY3Slk3UmVzTGFoZVNwVEF3V1N5OUdLOWxwY0p3VWlyTkYxVWZUWnBOdXpneERzRXg0VHM5dUllZEFKZ3VjemVBRnl5T3JoZmJnQmtTRnpiTEN6eFZCc3N0WDYwV05TRkgzd3A4R3YwR1NfWnlhZ0wzZTNXQUhfck9lNVk?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNWXBYLXU5eHRVeFphS2NhSXpOdXlfc2tldkhQZXRNVlMzTUFSM1VjNGRhU3lRbnJoZ2x6NUg0SVFwaV80cnVpcnlUVW56SGxrT2dQZkJjT1c1ZzNtcl9aVlBSQlJiM1UtQWdiOFBzNlVpSHpycVpfY1NCSlE0N2lsbUJUZGtmNGVSUWs2YzdmeVNLTGQySlliZktyX0NzVThMRTRtTDFFY3NwN25GbEFCdg?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxPYkxQbk01d3gxbjRyR1F1aVpZODJ5Z1F3NFNPRUhFbnBjeWZ3Q3lONHctSXY1bE5hWGhlV0c5MEVoTXpMR01xRENuMHp4SHdnQlZJd0s5TTItaFh2R1F4TndKRjNPd1RjdVRVRzM5bHBfUkNvU2RCV1laS0lhUzRKSjFLbjRhQnpaOWpmVFpzWVVIbDNEaTEtM3pYUlFOeG9LY0hmV2hmTXl1X052MTRsOGhQWGpycWs?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPbFQ1cWh6R3FnQ3BUZWJlMHNqazZUeExEN1RkQUMzeDBPcHgyOGxfZHI2eV82RkxQcWVXV2h2MDVOcWZaeGNEOEZDN29GcmdLTDR2S1lMaHpoTDFGQ1VjYTBxS010bkZGbmV1aGxmSW5tcFEyUTFzb3FrQno2aE5WV1JDMHlaU2FndDVRNHZYYkZ1alV3eWQ4RHEyb0ZCWnEtZlJmaDl3?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
