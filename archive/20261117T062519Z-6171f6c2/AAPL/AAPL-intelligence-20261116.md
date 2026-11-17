# AAPL Intelligence Report

- ticker: **AAPL**
- Report as_of: **2026-11-16**
- Market data as_of: **2026-11-16**
- Quant sources: https://finance.yahoo.com/quote/AAPL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AAPL/key-statistics/
- AI analysis snapshot as_of: **2026-11-16**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-17T06:46:28.207986+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 5, 'ai': 14, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **11** exact headline/source/date matches; prior report **20261116T043911Z-b81cfeb4/AAPL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **6**; {'directional_claim_without_event_type': 4, 'low_uncalibrated_model_confidence': 2}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 10 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 32.0%; oldest publication 2026-11-09

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 352.7800 |
| Return 1D (%) | -0.9796 |
| Return 1W (%) | 0.6724 |
| Return 1M (%) | 2.7916 |
| Return YTD (%) | 30.2174 |
| Return 1Y (%) | 29.9545 |
| Annualized volatility (%) | 24.9292 |
| Beta vs SPY | 0.6134 |
| Max drawdown (%) | -13.7985 |
| Sharpe (rf=0) | 1.2588 |
| Downside deviation (rf=0, %) | 16.9047 |
| Sortino (rf=0) | 1.8563 |
| Historical VaR 95% (1D, %) | 2.0102 |
| Historical ES 95% (1D, %) | 3.4742 |
| Correlation vs SPY | 0.3388 |
| Tracking error vs SPY (%) | 24.0514 |
| P/E (trailing) | 39.29 |
| P/B | 45.74 |
| EV/EBITDA | 30.12 |
| Revenue growth (%) | 11.70 |
| Forward P/E (estimate) | 33.37 |
| Gross margin (%) | 48.79 |
| Operating margin (%) | 33.01 |
| Return on equity (%) | 142.26 |
| Free cash flow yield (%) | 2.06 |
| MA50 | 339.4508 |
| Close vs MA50 (%) | 3.9267 |
| MA200 | 301.2456 |
| Close vs MA200 (%) | 17.1071 |
| RSI (14, Wilder) | 57.2284 |
| MACD (12,26) | 4.2072 |
| MACD signal (9) | 3.4734 |
| MACD histogram | 0.7338 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AAPL': 283, 'SPY': 283}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 352.7800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.9796 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.6724 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 2.7916 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 30.2174 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 29.9545 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 24.9292 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.9047 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.8563 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0102 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.4742 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3388 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.0514 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.6134 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -13.7985 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.2588 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 33.3708 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 48.7860 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 33.0100 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 142.2570 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.0610 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 39.2851 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 57.2284 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.7338 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 3.9267 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 17.1071 -> Clearly above the moving-average trend level.

## TAILWINDS

### Apple Stock Called ‘Safe Haven,’ Hits Record High
- Summary: Apple Stock Called ‘Safe Haven,’ Hits Record High
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxQSjNua2NKRWx2ckNtazhaanloVXE0b3padGZlSnlfSDBXLURWYmM4Tm9xUWlmaWxqaXJsN3JQekh6YmtWcEFPRGJBVGYzdDFDVTdsYWpMSUhuSERxbGhFaWM3LWVvV2RvRGZocmwxLWlTWFhIemg0V0piMTJOVGpzUk5CeTRjQmR4YmdTaXVOSF9feUk?oc=5>

### Apple Shares (AAPL) Look Expensive Heading into 2027
- Summary: Analysis of Apple shares’ valuation approaching 2027.
- Date: 2026-11-11 | Impact: low | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOM2lsenhVYnFXTUNRUHVQUkVxVEVMUDNwSzdFcDNnNWNRU3F2dDVGTHh2Zkh1N2laS1FtZHdzb2hQN3B6bHhrcUUxa2VFOWxzY1NlZTVwRFB5YkE4MGxjUHBueG1WQjRjUExnanJaZGZFSTQzX1Y0YTU3bmJ6UGNZYjNyaVdPenFDZHVhU0JlMUZySFBONHVDU2wxNnNIUQ?oc=5>

### Apple Inc. (AAPL) Rallied 15% as Investors Reassessed Its Growth: What’s Next for the Stock?
- Summary: Apple shares surged 15% after investors reassessed growth prospects.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQOTluMHhsdUl2LXpHekdlOUZIWmFHQ0t5M3c1LTJaNm9uUU9ENHJlQ25BNzN6SFJaaXd5NVE0SlJtMEl2UHBhNnllV0JXVS1GRGhJWUdEMjBxT1RhRDBwTmo1R2hnNTZpOVpPb3Z4YVl0My0tQTc0NTZMZzZKTnpGOHlNYXUtd252c3NSOE9vMFhybUc4?oc=5>

### Apple Is the World’s Largest Company, and Nvidia Is Second. Here’s What $10,000 Invested in Each Today Could Be Worth by the End of Next Year.
- Summary: Apple remains largest company; comparison with Nvidia.
- Date: 2026-11-13 | Impact: low | Horizon: long | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi_gFBVV95cUxNWVJhZDJfcFlqSnN2N25TRHpLazhkbE9GRFBWODJkaGVYd3FNZzRjR0prczZNcGdVV2djMVo5bHM0ZFd2djIzYlFkVFBQUk9KYjBuSFpVTExPQjRPT2pSd2Y4TFJlaE5wUHhBdDZUbnZUQXpGNG9lY2hkdWxDVnZ4aDl2bmxtVnI0WWZDaHUybEV3RU9GaGdhSWhGMG9JWnk5NkZCazk4d01uTlRBLVNnRGptVEotdXRFS05oY0tuV3U0d2gtaHFLaVJ0cU5mdWdvVFlBaE05Mng3WXZJdDJTTDZfRng2a3lNTTczbGtYY18wSzJwbGtTelpocm1JZw?oc=5>

### Apple: The Business Got Better, The Stock Got Much More Expensive (NASDAQ:AAPL)
- Summary: Business improvement and higher stock price signal positive momentum.
- Date: 2026-11-14 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOc2xKSXl6YWFyMmtDeE1OcmZpLUNDUTh4cGxTZGt0TkhTd2VMWFVsR2J1ZGdJc1hOWVZvUFBrbW9ZMzlZZ19HUVducENSWjgtQzFOdG1MU1ZBcDU4MVhyM2Izc1RJclFyblhRQV9XNDNvUmwtMHA0ZllBZTlSQ2U0VFBpU294Y3N6ZXdtMzRCc2o4SkZvcEtNaklnYjY?oc=5>

### Drama Notable Only By Its Absence: Why Investors Love Apple (NASDAQ:AAPL)
- Summary: Exploration of investor sentiment toward Apple amid market calm.
- Date: 2026-11-12 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxNWDQtTm5fUUhEZ1R2UnlWV3NrZnF0alhzalJBWFloTG5ucFJRZldRdTc5T2p2ZUI1X0Q5U0JlcHF3VEtWOFRFUnlDSzR2cTlER09HQWNUX2gwTWRtS2ZXLXQtNEJ2a1hGOXhsb0ZQS2l3MmNpeF81U3hmLW0zMnBoWUtLT29KUGI2YTJBdDJZZkZOOEthYXFhamYzSUJseTcw?oc=5>

### Apple: Deserves Costco's Multiple (Rating Upgrade) (NASDAQ:AAPL)
- Summary: Analysis of Apple’s valuation relative to Costco with a rating upgrade.
- Date: 2026-11-12 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxNX1Q3Q0ppRGVaRnZnZmo0ekF1V3FUZkh0YTEwVXhYX2REUGIteGNjaTl2a2szb21zQkd3eEdMOHdlYlhhNFMzeVlIbWQwbFk1VFdHckxmQW9qcExZSlQ2S1UtTGJleWZEQ28yRHF5OGZUbVZQOGs3UHRtT3pVSDNVSTZzdVVicEFkV0VhOXBMczA?oc=5>

### Apple (AAPL) Stock: $348.51, Down 0.62% Nov 10
- Summary: Current Apple stock price and recent decline.
- Date: 2026-11-11 | Impact: low | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOMUpaWVdPaHVGd2dQLXBWZHo0TXpUYWthUWxrUnYzNHg4TzRGWWZaVEl6dEpFaEQ0M3F0VmtqeTZ5YkpMNkthTDUtbWg5bXNZMXpLRnJBUUNzRHQwM09CVF9YSURjYjlGem9lOS1WVHhoZjRuLURYdUFEYWpndWtnOGhOY0dkX3JPT3FzcWtVZXdpM3ZDQzZEOGJSZkRaVHc?oc=5>

### Apple targets June 2027 unveiling for AI smart glasses: report (AAPL:NASDAQ)
- Summary: Apple plans to unveil AI smart glasses in June 2027.
- Date: 2026-11-16 | Impact: medium | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOZEhVR1p4SVhoeEFLSTkwSUVoLW5RRG9JRmZxX1k5NVVpbExYRU1WTGw5clM4d2FKNllFMTlROVlVT25HQmdkRHpVZUJqMWptSlhkSk9RdmF4LTlDMlhQazFDU3ZlelhMRkJPMTJkOEl0UHYxZHpOY3lYSG1lU2piV0tzM2lvZXdmaDJTU0RueExWYmNJWU1uQU4tWW83Q1lZ?oc=5>

## HEADWINDS

### Whale Rock Capital takes new stake in Microsoft, exits Apple, among Q3 moves (HPE:NYSE)
- Summary: Shareholder exit may signal reduced confidence.
- Date: 2026-11-13 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxQNmtUVU1paUZxR04yTGZRcktMTkRzLWRoY1o3YVFJX24xSGpzalloc2FoZEhYZGZqMDdiQkU0QVNNOGJ5WDE2dVI4Y21lWFJSQ0RKRzc1dWtKbDBidkh2T2ZhZFc4ZVhLRlZxdXZEcTJ4d2xUS1VCZFdPVkV6aUMtdkx2aERlWGstU1lwOEo4Sm5FazNHVFRzeHFESkpLOENiNEtMQWtNX2Z5TEtiU3M4ZmVn?oc=5>

## CATALYSTS

### Apple (AAPL) Picks Core Foldable Glass Supplier For iPhone Duo
- Summary: Apple (AAPL) Picks Core Foldable Glass Supplier For iPhone Duo
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOYmt6MzR0X1VRdEVBYVF2Y1drN3B0RlpXRUtmOW9CX0ZFbE5kYUJXV0oxczZUckthVWxMTW1JeVM5bkZLaVE1QjhZSi1kazRpWUEyUHEySFFoZ21URmNfYVVtQ0Q0NEIwZTdldkpmOVc3akt0XzVxaXVvbFZ6d0ZmUzdxOFlPZkVvYUlRaUFtVU5CRTZ4S0E?oc=5>

### Apple (AAPL) Stock Gets Fair Value Bump As Analysts Debate Margins And iPhone Demand
- Summary: Apple (AAPL) Stock Gets Fair Value Bump As Analysts Debate Margins And iPhone Demand
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNZHZNT19NWVNzc0ZrNmpzYlVESDQ1RFZyRTd4SlU5Q000TnJBUzlUTEhKdHRodWpjdmtjMkxMQW5GV0FveDhRaWU3MDluZUYxTnp4R1RsQTZSM3duU2F4aWxSZWJJNXlwc09PVjRFaDRUX051YmFPRnRRY3VoUkRFcS1aMjVtYno3SFUyTFVaTlFmTU5Ca2c?oc=5>

### Apple adds face unlock to iPhone Duo in new software beta (AAPL:NASDAQ)
- Summary: Apple adds face unlock to iPhone Duo in new software beta (AAPL:NASDAQ)
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNekw4czk1V0dBR21SMWtoS1ozbkVuWUhPTTR5cEtWTmNTd3JrdHM3UWg5RWItekxCMnJVcUhrZXBDTkJ3aDdPdktucTRUYWtjazFCV1p4a0xyMzBsS3NrMXdvOGlmaEViOGM4MTd4MmZQOW9sN0JTbmQxY3pyRjlTUjk2eXBCa0QwWFR0N1REdHhMMmRfb0x3anhnWQ?oc=5>

### Apple Inc. $AAPL Stock Acquired by One Wealth Capital Management LLC
- Summary: Apple Inc. $AAPL Stock Acquired by One Wealth Capital Management LLC
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxNMmszLVZpbk1hTFowUEJDOURpTDBNVzV0V0dDaVI3SzUyU1dIU2pUUzU1NDJrSXhMd2V2TXlnTThqdmVOMWg1enlPajJYNkhsVENFOHBDUDU1MzROYWtFdHdMNDEyUEl2dFJqXzh1d21wTlZGSTBpZ1hVUS1TVEg1bjJTSnA2b1c0dnhmSXpneTQwRDBpcDRnbk5uUVdqeTdCdm9CT21zUFJfdWd3TUpBcFNGNkZyeXVwRTlwcWVJSjBiWmV0TVE?oc=5>

### A $1,999 Sellout. What China Renaissance Sees in Apple (AAPL)
- Summary: China Renaissance's $1,999 sellout view on Apple.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPUVhYalN0S3o2VVRpNWZPTU9oWEZJZnlRNi1VU1pTY3VzUXFueTh3Um9IUWIzdjY4OW9EU3kwVG5QblI5MzcxUVg2Y3J3QW5KM3RuZGh3UmRJYTRBWVR0Ql9iZVAzb2JucTM5Qi1IQkl1bHNLQXpDeFltVzhqQm9mTXFneG5GSi1vQ25oSGY0VnBrSEI5a1hWb1d3VDU?oc=5>

### Apple (AAPL) Puts Tim Cook At The Center Of A Surprise CEO Search
- Summary: Apple announces a surprise CEO search, placing Tim Cook at the center of the process, signaling potential leadership changes.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxQZ2pUMi1tNld3R2xsYWtXRlNIck5ST3gyZVNBUE5tcE04d1Q5SWdJeUJaSjVVNm9kWHpVX3huOWQtTHFGbWxLNUY4TGsxMkFNX1BtUXdndVUxTnpDajhkdm5FMXROeXRIdDhCN05aQ3NiQXBqeEYtT21KRThBemZKSnhwVk1kZmxGVVhTZ053?oc=5>

### AAPL Stock Posted Best Week In 4 Months Amid Nvidia Disruption: Apple Reportedly Plans Smart Glasses To Rival Meta Next Year
- Summary: Apple’s stock surged after announcing plans to launch smart glasses competing with Meta, marking its best week in four months amid Nvidia’s market disruption.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPaTZ2ZWQ2QTBxMk1iWTJ4ZXBGc3hpUDRHMDVVdFdMaGtkWVVkcEtzM2djWFpZQ1ZxTnYtUHFhMHFIbjFSSjhPSXVDWWsxdXlvQzQ1RDliaVNNUzR5QzZLWEl0UW9ROGx5RnZVdko4LWYzbWNqWEJORkJDTEVmY3ZObDgyaHNmZzRHaWpQN2ZCaDFQM05ja21J?oc=5>

### Apple: A Downgrade To Hold Would Be A Wise Move Before Q1 (NASDAQ:AAPL)
- Summary: Analyst downgrade to hold before Q1.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxORm15ODNFbGlFdjBNa1A3aHlFZUJNTFNvNm5vZmJuYXBpa3BGUjZnU2g3aktoclI4bTBMOGFuVmo1cklSY25JTTdKLW45cC13ZmwzZHhLT1Btbm55MkRBUFpENkctWWdVY2tNZFJ0MXNxZ1RDeW9EdFF5LTdpU1FYbHBpbXk2Yy1kUE1YZjJZTENweU1xdnhzQVowTkp0QQ?oc=5>

## RISKS

### Is Apple Stock a Buy Right Now?
- Summary: Question reflects uncertainty about valuation.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTE9ZZzd4WHdhQ2gyRU5BckJfY21JTWhSdXYyZC1sZGlmb0FyZEZUSzVDeWVkbUloU19hR2ItYVhiaXBodGVIUVZTODZtQ1lkdWV1RVlOcDhZOFpJR1Z6bld4TG1YN3BPTUY3ZXhLeGlEaUFOTzNmN3FNbjI3VDVYdw?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AAPL** | **39.29** | **45.74** | **30.12** | **11.70** | **5,126,663,176,192.00 USD** | **29.95** |
| MSFT | 27.03 | 8.18 | 19.04 | 18.80 | 3,846,694,502,400.00 USD | 2.37 |
| GOOGL | 14.82 | 5.29 | 18.28 | 24.70 | 3,488,053,460,992.00 USD | 2.91 |
| SONY | 20.18 | 2.92 | 0.30 | 10.30 | 157,595,992,064.00 USD | -10.23 |

Peers fetched as_of: 2026-11-16; AAPL reuses existing data (market data as_of: 2026-11-16); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-02
- Next expected earnings: 2027-01-28 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-16

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-11-03
- Revenue (latest available single quarter): 62,900,000,000.00 USD; period 2018-07-01/2018-09-29; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 29,789,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/320193/000032019326000026/aapl-20260926.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMikwFBVV95cUxQSjNua2NKRWx2ckNtazhaanloVXE0b3padGZlSnlfSDBXLURWYmM4Tm9xUWlmaWxqaXJsN3JQekh6YmtWcEFPRGJBVGYzdDFDVTdsYWpMSUhuSERxbGhFaWM3LWVvV2RvRGZocmwxLWlTWFhIemg0V0piMTJOVGpzUk5CeTRjQmR4YmdTaXVOSF9feUk?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOM2lsenhVYnFXTUNRUHVQUkVxVEVMUDNwSzdFcDNnNWNRU3F2dDVGTHh2Zkh1N2laS1FtZHdzb2hQN3B6bHhrcUUxa2VFOWxzY1NlZTVwRFB5YkE4MGxjUHBueG1WQjRjUExnanJaZGZFSTQzX1Y0YTU3bmJ6UGNZYjNyaVdPenFDZHVhU0JlMUZySFBONHVDU2wxNnNIUQ?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQOTluMHhsdUl2LXpHekdlOUZIWmFHQ0t5M3c1LTJaNm9uUU9ENHJlQ25BNzN6SFJaaXd5NVE0SlJtMEl2UHBhNnllV0JXVS1GRGhJWUdEMjBxT1RhRDBwTmo1R2hnNTZpOVpPb3Z4YVl0My0tQTc0NTZMZzZKTnpGOHlNYXUtd252c3NSOE9vMFhybUc4?oc=5
- https://news.google.com/rss/articles/CBMi_gFBVV95cUxNWVJhZDJfcFlqSnN2N25TRHpLazhkbE9GRFBWODJkaGVYd3FNZzRjR0prczZNcGdVV2djMVo5bHM0ZFd2djIzYlFkVFBQUk9KYjBuSFpVTExPQjRPT2pSd2Y4TFJlaE5wUHhBdDZUbnZUQXpGNG9lY2hkdWxDVnZ4aDl2bmxtVnI0WWZDaHUybEV3RU9GaGdhSWhGMG9JWnk5NkZCazk4d01uTlRBLVNnRGptVEotdXRFS05oY0tuV3U0d2gtaHFLaVJ0cU5mdWdvVFlBaE05Mng3WXZJdDJTTDZfRng2a3lNTTczbGtYY18wSzJwbGtTelpocm1JZw?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOc2xKSXl6YWFyMmtDeE1OcmZpLUNDUTh4cGxTZGt0TkhTd2VMWFVsR2J1ZGdJc1hOWVZvUFBrbW9ZMzlZZ19HUVducENSWjgtQzFOdG1MU1ZBcDU4MVhyM2Izc1RJclFyblhRQV9XNDNvUmwtMHA0ZllBZTlSQ2U0VFBpU294Y3N6ZXdtMzRCc2o4SkZvcEtNaklnYjY?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxNWDQtTm5fUUhEZ1R2UnlWV3NrZnF0alhzalJBWFloTG5ucFJRZldRdTc5T2p2ZUI1X0Q5U0JlcHF3VEtWOFRFUnlDSzR2cTlER09HQWNUX2gwTWRtS2ZXLXQtNEJ2a1hGOXhsb0ZQS2l3MmNpeF81U3hmLW0zMnBoWUtLT29KUGI2YTJBdDJZZkZOOEthYXFhamYzSUJseTcw?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxNX1Q3Q0ppRGVaRnZnZmo0ekF1V3FUZkh0YTEwVXhYX2REUGIteGNjaTl2a2szb21zQkd3eEdMOHdlYlhhNFMzeVlIbWQwbFk1VFdHckxmQW9qcExZSlQ2S1UtTGJleWZEQ28yRHF5OGZUbVZQOGs3UHRtT3pVSDNVSTZzdVVicEFkV0VhOXBMczA?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOMUpaWVdPaHVGd2dQLXBWZHo0TXpUYWthUWxrUnYzNHg4TzRGWWZaVEl6dEpFaEQ0M3F0VmtqeTZ5YkpMNkthTDUtbWg5bXNZMXpLRnJBUUNzRHQwM09CVF9YSURjYjlGem9lOS1WVHhoZjRuLURYdUFEYWpndWtnOGhOY0dkX3JPT3FzcWtVZXdpM3ZDQzZEOGJSZkRaVHc?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOZEhVR1p4SVhoeEFLSTkwSUVoLW5RRG9JRmZxX1k5NVVpbExYRU1WTGw5clM4d2FKNllFMTlROVlVT25HQmdkRHpVZUJqMWptSlhkSk9RdmF4LTlDMlhQazFDU3ZlelhMRkJPMTJkOEl0UHYxZHpOY3lYSG1lU2piV0tzM2lvZXdmaDJTU0RueExWYmNJWU1uQU4tWW83Q1lZ?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxQNmtUVU1paUZxR04yTGZRcktMTkRzLWRoY1o3YVFJX24xSGpzalloc2FoZEhYZGZqMDdiQkU0QVNNOGJ5WDE2dVI4Y21lWFJSQ0RKRzc1dWtKbDBidkh2T2ZhZFc4ZVhLRlZxdXZEcTJ4d2xUS1VCZFdPVkV6aUMtdkx2aERlWGstU1lwOEo4Sm5FazNHVFRzeHFESkpLOENiNEtMQWtNX2Z5TEtiU3M4ZmVn?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOYmt6MzR0X1VRdEVBYVF2Y1drN3B0RlpXRUtmOW9CX0ZFbE5kYUJXV0oxczZUckthVWxMTW1JeVM5bkZLaVE1QjhZSi1kazRpWUEyUHEySFFoZ21URmNfYVVtQ0Q0NEIwZTdldkpmOVc3akt0XzVxaXVvbFZ6d0ZmUzdxOFlPZkVvYUlRaUFtVU5CRTZ4S0E?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNZHZNT19NWVNzc0ZrNmpzYlVESDQ1RFZyRTd4SlU5Q000TnJBUzlUTEhKdHRodWpjdmtjMkxMQW5GV0FveDhRaWU3MDluZUYxTnp4R1RsQTZSM3duU2F4aWxSZWJJNXlwc09PVjRFaDRUX051YmFPRnRRY3VoUkRFcS1aMjVtYno3SFUyTFVaTlFmTU5Ca2c?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNekw4czk1V0dBR21SMWtoS1ozbkVuWUhPTTR5cEtWTmNTd3JrdHM3UWg5RWItekxCMnJVcUhrZXBDTkJ3aDdPdktucTRUYWtjazFCV1p4a0xyMzBsS3NrMXdvOGlmaEViOGM4MTd4MmZQOW9sN0JTbmQxY3pyRjlTUjk2eXBCa0QwWFR0N1REdHhMMmRfb0x3anhnWQ?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxNMmszLVZpbk1hTFowUEJDOURpTDBNVzV0V0dDaVI3SzUyU1dIU2pUUzU1NDJrSXhMd2V2TXlnTThqdmVOMWg1enlPajJYNkhsVENFOHBDUDU1MzROYWtFdHdMNDEyUEl2dFJqXzh1d21wTlZGSTBpZ1hVUS1TVEg1bjJTSnA2b1c0dnhmSXpneTQwRDBpcDRnbk5uUVdqeTdCdm9CT21zUFJfdWd3TUpBcFNGNkZyeXVwRTlwcWVJSjBiWmV0TVE?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPUVhYalN0S3o2VVRpNWZPTU9oWEZJZnlRNi1VU1pTY3VzUXFueTh3Um9IUWIzdjY4OW9EU3kwVG5QblI5MzcxUVg2Y3J3QW5KM3RuZGh3UmRJYTRBWVR0Ql9iZVAzb2JucTM5Qi1IQkl1bHNLQXpDeFltVzhqQm9mTXFneG5GSi1vQ25oSGY0VnBrSEI5a1hWb1d3VDU?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxQZ2pUMi1tNld3R2xsYWtXRlNIck5ST3gyZVNBUE5tcE04d1Q5SWdJeUJaSjVVNm9kWHpVX3huOWQtTHFGbWxLNUY4TGsxMkFNX1BtUXdndVUxTnpDajhkdm5FMXROeXRIdDhCN05aQ3NiQXBqeEYtT21KRThBemZKSnhwVk1kZmxGVVhTZ053?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPaTZ2ZWQ2QTBxMk1iWTJ4ZXBGc3hpUDRHMDVVdFdMaGtkWVVkcEtzM2djWFpZQ1ZxTnYtUHFhMHFIbjFSSjhPSXVDWWsxdXlvQzQ1RDliaVNNUzR5QzZLWEl0UW9ROGx5RnZVdko4LWYzbWNqWEJORkJDTEVmY3ZObDgyaHNmZzRHaWpQN2ZCaDFQM05ja21J?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxORm15ODNFbGlFdjBNa1A3aHlFZUJNTFNvNm5vZmJuYXBpa3BGUjZnU2g3aktoclI4bTBMOGFuVmo1cklSY25JTTdKLW45cC13ZmwzZHhLT1Btbm55MkRBUFpENkctWWdVY2tNZFJ0MXNxZ1RDeW9EdFF5LTdpU1FYbHBpbXk2Yy1kUE1YZjJZTENweU1xdnhzQVowTkp0QQ?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTE9ZZzd4WHdhQ2gyRU5BckJfY21JTWhSdXYyZC1sZGlmb0FyZEZUSzVDeWVkbUloU19hR2ItYVhiaXBodGVIUVZTODZtQ1lkdWV1RVlOcDhZOFpJR1Z6bld4TG1YN3BPTUY3ZXhLeGlEaUFOTzNmN3FNbjI3VDVYdw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
