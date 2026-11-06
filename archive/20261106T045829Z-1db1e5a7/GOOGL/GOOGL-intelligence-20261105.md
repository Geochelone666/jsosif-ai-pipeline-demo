# GOOGL Intelligence Report

- ticker: **GOOGL**
- Report as_of: **2026-11-05**
- Market data as_of: **2026-11-05**
- Quant sources: https://finance.yahoo.com/quote/GOOGL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/GOOGL/key-statistics/
- AI analysis snapshot as_of: **2026-11-05**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-06T05:20:47.747731+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 4, 'ai': 16, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261105T045846Z-bde0a1fe/GOOGL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **7**; {'directional_claim_without_event_type': 2, 'low_uncalibrated_model_confidence': 5}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 7 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 54.17%; oldest publication 2026-10-29

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 282.5700 |
| Return 1D (%) | -2.2012 |
| Return 1W (%) | -0.4404 |
| Return 1M (%) | -18.4432 |
| Return YTD (%) | -9.5464 |
| Return 1Y (%) | -0.3535 |
| Annualized volatility (%) | 33.8127 |
| Beta vs SPY | 1.3140 |
| Max drawdown (%) | -30.6204 |
| Sharpe (rf=0) | 0.1589 |
| Downside deviation (rf=0, %) | 23.7787 |
| Sortino (rf=0) | 0.2259 |
| Historical VaR 95% (1D, %) | 2.9365 |
| Historical ES 95% (1D, %) | 4.7232 |
| Correlation vs SPY | 0.5283 |
| Tracking error vs SPY (%) | 29.0251 |
| P/E (trailing) | 14.76 |
| P/B | 5.27 |
| EV/EBITDA | 18.20 |
| Revenue growth (%) | 24.70 |
| Forward P/E (estimate) | 18.24 |
| Gross margin (%) | 60.86 |
| Operating margin (%) | 31.80 |
| Return on equity (%) | 44.29 |
| Free cash flow yield (%) | -0.03 |
| MA50 | 334.0192 |
| Close vs MA50 (%) | -15.4031 |
| MA200 | 339.4420 |
| Close vs MA200 (%) | -16.7546 |
| RSI (14, Wilder) | 27.9871 |
| MACD (12,26) | -16.5392 |
| MACD signal (9) | -11.8278 |
| MACD histogram | -4.7115 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'GOOGL': 276, 'SPY': 276}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 282.5700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.2012 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.4404 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -18.4432 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -9.5464 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -0.3535 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 33.8127 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 23.7787 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.2259 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9365 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.7232 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5283 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 29.0251 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.3140 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -30.6204 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1589 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 18.2381 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 60.8570 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 31.8050 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 44.2860 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: -0.0335 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 14.7556 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 27.9871 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -4.7115 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -15.4031 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -16.7546 -> Clearly below the moving-average trend level.

## TAILWINDS

### Reddit (RDDT) vs. Alphabet (GOOGL): Which Stock Offers More Upside, According to Analysts?
- Summary: Analysts compare potential upside between Reddit and Alphabet, suggesting Alphabet may offer stronger growth prospects.
- Date: 2026-11-03 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxPMkN4cGVFZGYxM29fRzlMVjhyQ1AzYUs0ckl4dG42cXRxWDVFaDk3enV1eGRiczNua3lXQTVwYjhuYzJXWTlBYTdGa2V2RW5Sa1IxcEhJYzBaTVNHaG13U29BcGZFNUdaR2tvVnViWGRrVzhmeXljaTQ5U1NZTER4WWZpOEVHeHVpSkNSaW9oZTk0ZjZxUDRCSFAwS2U3eHo1WGtuZmJpbW0yNU5OVTlfalI0WVR2Z0xVMnQ3TQ?oc=5>

### Why Alphabet Stock Popped on Wednesday
- Summary: Analyzes factors contributing to Alphabet's price jump on Wednesday, including earnings expectations and market dynamics.
- Date: 2026-11-04 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxOYlJpNTBiZjlSRFh0LTc3cThFWW5GWXlQUFdTVDJQQkZWYWRwVnYxQXh4T1ZnY1FnM0JxY2Joc2ltWGJlVDJWVmRpWEVySHU5WFpLeFhiRENVVHhOUUI4SjA1SXl2dTBZRGFKVENzZldSLXc3WUR3c05aRXFWeE9URnpsTkp5d1Yy?oc=5>

### Marc Chaikin Sees Alphabet (GOOGL) as a Conglomerate Hiding Three World-Class Businesses
- Summary: Analyst views Alphabet as a conglomerate with hidden top-tier businesses.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOZGUwTUFsMVZQeEZPSnFCZ3dnMDZNTVNFeGVXelVQN1ZtcFo3SnY2dzdmSHhIM2J2OGgwRXZScGYxajZuSDNQd3ZvTGdrMDU5QWNEdWhXM0hnb1lPMmNoQ3ZST0lTcnVDRllVRnpwWG9VdWxxQ1I5R0w5Q3BsZ0NaMkJ1b0FRc05nZnRWdFRhdFBBYVg3aEkwSWd4NlktZw?oc=5>

### Alphabet: The Advertising Phenomenon Investors Always Miss (NASDAQ:GOOG)
- Summary: Highlights Alphabet’s advertising strength as a growth driver.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNYi1ibllMYTF5RnA0OWpuZEMwdkQxNGRlM09ZVmpIX0t0NTZIdGVnQzdrUWZJMTBLTG5mUGQxRXVNT0dDeU4xRXZPT2NZSEFZMUhtZk1aVjNRRldNVU1Gd2JYMXVWcXpzbVdmc3hIZFZKbXJOZHBCTDBPV1RnYndIV1UwQjFnSnNmek4zSkwxSzcwZWZYQU9FdW9OV1FYWVU?oc=5>

### 2027 Is Alphabet's Proving Year: Hold With GOOY (NASDAQ:GOOGL)
- Summary: Suggests 2027 will be a strong year for Alphabet.
- Date: 2026-11-05 | Impact: medium | Horizon: long | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxPbDlWbXZQTlZVRk15MmRxbHp4TnBuNUw3YXFhN3NyRTdKam1GSHR1Uk9Pa3dRNkpMWkRBLUl1eXlGM3hqVzAweUN6SWc1YlBCVlRGVnpVZlVuRHN6amNzcmdScUw5M0p5ckZheG1BODkyMkJ1TTk2X0pyN2dINXllV2ZEcXBUelBELXAxZC1vYw?oc=5>

## HEADWINDS

### GOOGL Stock Is Down 10% YTD. Alphabet’s Historic Selloff Could Be a Buying Opportunity.
- Summary: GOOGL Stock Is Down 10% YTD. Alphabet’s Historic Selloff Could Be a Buying Opportunity.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNbl9XRDh5Y0hMVXdFZUpUZ3ExTDRzV0Z6dHYtTWhRQVdrU3l1Z085NFRsYkVocDBWX0xfZzltd25VdW5idENwc1hFNXd0SjFiWTRmY3VEcHBzUjFqdmFzcjQ0RkR6WTRfUGJ3SzdvZUN0SGNwVnROdUtzSC1LeEpKeFJRNzJoMEp1cFZweS1SbWNCdw?oc=5>

### GOOGL Q3 deep dive: AI investment drives revenue growth but profit falls short of expectations
- Summary: GOOGL Q3 deep dive: AI investment drives revenue growth but profit falls short of expectations
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxPZURicFRzOTd2YnRheVByVFd3c3h5eDFlbHFPVmV3ZEZPbW1adG1NaElwdU1kcU5RM25tWjBZb1lqMktlTy1JalcxWXY4ek1QUGxrOVVES2RSN0JMcXVMRmxpOVpENlcyeTFHa3I0VUxEb2g2U2tCMjhjZV9McHRocVNDU2pEbTlkUFJfblF2WQ?oc=5>

### Alphabet loses $475 billion in market value, the biggest drop in its history
- Summary: Alphabet's market value fell $475B, the largest decline in its history, indicating significant investor sell‑off and market uncertainty.
- Date: 2026-10-30 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxOb0pfRGxYakdFTWU5eXlYYTd5cGVuVmpzMDFiMDBuX2ZOQVB5aFV1Qmk1dEhXQWwtSVNtU2ZOSTNfVDMxS2NoMUpTbmJ3a0hYOGtvOGJldXlkU3k2N3djaVhDMUNGN0g5Q1J2SzRXMkhXbzI3MUxqd2t5SEszX0JEZWZPUmRSd3VZQmYyZzZZeDNvY0hKaExMcnNTbHhzeTItckpZaEJmbWxodHVla2FKTTN4cmdFY2VjWk96cjdwLUtjX3FMRmZwLVp3SHJiX2xNajBR?oc=5>

### Why Did Alphabet (GOOGL) Shares Fall After Its $500 Billion Value Wipeout?
- Summary: Shares dropped after a $500B market value wipeout, reflecting investor concerns.
- Date: 2026-11-01 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQcWljZDdUS0l6cHpEVmtJYWlLNm5IdFN0RnV6ZmhuLThjODQ4aXhiQl95UE1Pa3ptY1pGRUVrQm5EWVh0SzN5aEVaUF9rUjVBU1YyZHhtMlBRem45b01lY3IwdFZkdmNxWU9LcWVEQTZTM2hjcWVrdmJaRDZDaFlzUWFHVlBNNjBSS0tJQ1MyMk8wazVMLVRCTFJB?oc=5>

### Good News Or Bad? Wall Street Lowers The Revenue Bar For Google Search
- Summary: Revenue expectations lowered, negative outlook.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxOWXFmV3NncXdwZnhIbTZmUGJOM2hWUkhHeVdySTRlY3hnRjVVMzk5bVYyN2R1Mk8xbm0xanV0TGVxMFN5UW9haTZhcFpaQXpIc2o1SDBqTThOOVlsMmJKMzVxMTBZRXFnVlZLbTREdW1PeTczbV9CQzExZDBSY2dwakh3d0gyQWRCQzVCY0VydFVkajRfbGliejB4aERfbHV3ckJTM3h5aUZlcmFFc3NMS05zdU1vaFlSdXZv?oc=5>

### Alphabet: Search Disruption Vs. The Rise Of Carbon
- Summary: Search disruption threatens Alphabet amid growing carbon focus.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPTWFweTVyMV9zZjhXMnVna0dsaWppNUVEMmpCNjlTVjJJcFljd3ExUjZwRlpTT3lrRmxmTGFFYWEyZE1NWUNFQVV1UjJfSTB1enlPUERnYnE5eXM2V2txMUhrdXFUelR6SGFUNndiWjM5WDlVMTFwMV92SW8xLUVRa3Y5cHpxSGpUVlRfYW55OVpBdGM?oc=5>

### Has Alphabet (GOOGL) Fallen Far Enough To Back Its Cash Flow Value?
- Summary: Questioning if Alphabet's valuation supports its cash flow value.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQckEtTjZnazV2YS1qTjQxNkxzaXZOU2pjYmZ5S29qRzB5QlJ6Y04wcE9MYzE0c250WjQydHNkeUVDS1Q4RGRTaUFrUkphdFVGYWlqcHNibXNkVFo3QUpKVWZKX29LZTF4NE1INVU1ZkVONnQ3MzVzWXhrQzJ2VVBrZUVkTmVRT0VETVdhUnhWZW9uWFhVaThnbkRJeXEyZw?oc=5>

### Alphabet: Investors Are Making The Same Mistake They Did With Microsoft (NASDAQ:GOOG)
- Summary: Warns investors about potential pitfalls similar to Microsoft.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxPaWlPYks3MTZ2OWRHU05kZVZhWGpfTzJjVzVPck9lZ29GLVRLUENaa2RZQ0ttVHh2WXhiN19LRUJ0eWp2eEVVQnhlbVdEV1YxT3VleDlfQVdZRGZEbmR5Y1J6bnp5clhxc1ZpREJsYnFQcjdEYTlZY1hERE1obDdvSHNjOTEzMUZtTDhscjUtNXNHd3B1YVV3NUxNNkFDYUhWakN1cEFlLUd2WEdQTVZHRQ?oc=5>

### Alphabet: The AI Reckoning Starts Here (NASDAQ:GOOG)
- Summary: Indicates challenges from AI developments for Alphabet.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxPR2NRSjltdlRpOWhqWTUwZ1dwV3FRbUZBZWZqbVhhTWt4NnR6XzVNa2dBS3NSZzVENDFpWlRKT1dRWjVOX05ISVRDU1FpbjBhdVhKanlXSFpXbF9uMkxjUlMtanpCb0hXSWRGZ1FkbmFGQnRLMHVoaHB6TlRzbjVxNGJtOTg?oc=5>

## CATALYSTS

### Google stock gets shredded after earnings—here's 2 reasons why investors hated the quarter
- Summary: Google stock gets shredded after earnings—here's 2 reasons why investors hated the quarter
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi5wFBVV95cUxObUdnZkYxXzBTRmhYR29adzI1M0oxMjZMU1VhX2F0cFpEdkFGNnd3Sk42Y21QZXVNLXA5NTJiQmlXZUpFVWhFNlptbjQyYWR0a09jRUZCZGdoVDJnTGlrOWthVE5qaXhCQkI4a0tWVzV1bTg4dGx6b3YwbUtWUk03UDRjdlh3Nlppd3FiVTgwVUlNSXdfaWdKR0hpTnJuVS1CRENOTGhSN05RbXlpaFdaZG5uOC1HMU1zTWJ1MnFjN1hVUEpubGpnaEZoQmRMdVBzSG1Wcmk2NGdHTmpWWkdxYS1scW54elU?oc=5>

### Alphabet (GOOGL) Stock Sees Fair Value Cut After Q3 Miss And Higher AI Spending
- Summary: Alphabet (GOOGL) Stock Sees Fair Value Cut After Q3 Miss And Higher AI Spending
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNM2lKdjlTOWxfNDNhTEk0bEhYWUVMUHE4bnpEVHdzakFsX3A3NHRwcGdpd1pBRHVxRkdESzg5cTc3X0hUZ3ZkM212UVA5c3JQQk43T0NxTXJCSUpPRERFLU1GX1V3ajc5MGV4a1ZiZS1KZmZFcHFhbGxVak93VXZLcWs0N1Y5RTlhbkxBYkg3eGVnOU5tYVYtZGdTVQ?oc=5>

### Why Alphabet (GOOGL) shares are sliding today
- Summary: Alphabet shares fell today, reflecting market concerns and negative sentiment.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPQmJ1N3ZZWXo3VXA4TXZrRmJXMVdzU1dOUmJVNFpfenJzQ2VxVXJsX2xhSzJvNTRwU0pJNTN1LWsxSmZ6S2RXYkhVQXdwelZzbFdpcm1IUjRFS2E3NmUtZ2JxckRmdHRlZ1FKNVhsZDAxeGdMbTRpOXNIcm9iaWdJQUJ0ZzdhU0xvU3ROUlVwbEhwRFZ3cEozaWxCQ2FPX3M?oc=5>

### Alphabet: Cheapest Hyperscaler By A Margin (NASDAQ:GOOG)
- Summary: Highlights Alphabet’s cost advantage in hyperscaler market.
- Date: 2026-11-05 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxPQjFUZl9WVGNOMjFocVBIdEtCRHc4Zkx2VWxtRkZiQ1Vic2FrTWNUZUEtNXpNTjNRU0lmSTB4R0JPMVhoYmcxR0U0MXdxckw0eW9FeURQRVZKUkJEWXBxSVVMUVhNU2lmY2tpM3ZnbzVUN05PRmRxQm5GaGVrUm80azVMS29NTmVaMWc?oc=5>

### Investors Heavily Search Alphabet Inc. (GOOG): Here is What You Need to Know
- Summary: Provides overview of investor interest and key points about Alphabet.
- Date: 2026-11-02 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPQ3JjS2p6X012anh4STM1VWFFZ3NmVGZKdVY2ZG1OX3pYY1lidFJnSVNwMHBCOHpGQ3RPZm5DQ3RfeGtualZVenE0Z2liVERnNnlmZl9SQXBlazdwaUx0UmJybVhDNkNhSUpzVFptMXlUbEkyVWZCQ04ydnhqZ0xCRTJVT1d3bDB3bnA2Vk9mM2tkU2dQODFFaVRYNEkxTmRXRmNMUg?oc=5>

### What's Going on with Alphabet Stock? 3 Things Investors Should Know
- Summary: Summarizes three key factors affecting Alphabet stock.
- Date: 2026-11-02 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPaDh0YmZUaTVRLUZENzJXVER4ODlodzRKYjAyTW9HVHJsOUhiRFdWUm1MTzhubnowRHBwdUplUjBuRWdzVmpjc05Nd2EwRVlCTW9GZUo4SFpHWUdwUHkzNWt6SW1ZVG0tc0NNOG9CblhvY2d1N0xYNkkxUzJvRkl5cElkak9OSmE2eFM2UVREV2xtYjVEQk1LWA?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **GOOGL** | **14.76** | **5.27** | **18.20** | **24.70** | **3,473,915,510,784.00 USD** | **-0.35** |
| META | 21.49 | 5.68 | 13.59 | 26.10 | 1,547,088,560,128.00 USD | -4.53 |
| MSFT | 29.00 | 8.46 | 19.69 | 18.80 | 3,979,920,277,504.00 USD | 6.54 |
| AMZN | 21.50 | 4.58 | 16.35 | 12.10 | 2,813,686,448,128.00 USD | 4.00 |

Peers fetched as_of: 2026-11-05; GOOGL reuses existing data (market data as_of: 2026-11-05); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-28
- Next expected earnings: 2027-02-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-05

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-29
- Revenue (latest available single quarter): 127,577,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 26,468,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000084/goog-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMivAFBVV95cUxPMkN4cGVFZGYxM29fRzlMVjhyQ1AzYUs0ckl4dG42cXRxWDVFaDk3enV1eGRiczNua3lXQTVwYjhuYzJXWTlBYTdGa2V2RW5Sa1IxcEhJYzBaTVNHaG13U29BcGZFNUdaR2tvVnViWGRrVzhmeXljaTQ5U1NZTER4WWZpOEVHeHVpSkNSaW9oZTk0ZjZxUDRCSFAwS2U3eHo1WGtuZmJpbW0yNU5OVTlfalI0WVR2Z0xVMnQ3TQ?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxOYlJpNTBiZjlSRFh0LTc3cThFWW5GWXlQUFdTVDJQQkZWYWRwVnYxQXh4T1ZnY1FnM0JxY2Joc2ltWGJlVDJWVmRpWEVySHU5WFpLeFhiRENVVHhOUUI4SjA1SXl2dTBZRGFKVENzZldSLXc3WUR3c05aRXFWeE9URnpsTkp5d1Yy?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOZGUwTUFsMVZQeEZPSnFCZ3dnMDZNTVNFeGVXelVQN1ZtcFo3SnY2dzdmSHhIM2J2OGgwRXZScGYxajZuSDNQd3ZvTGdrMDU5QWNEdWhXM0hnb1lPMmNoQ3ZST0lTcnVDRllVRnpwWG9VdWxxQ1I5R0w5Q3BsZ0NaMkJ1b0FRc05nZnRWdFRhdFBBYVg3aEkwSWd4NlktZw?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNYi1ibllMYTF5RnA0OWpuZEMwdkQxNGRlM09ZVmpIX0t0NTZIdGVnQzdrUWZJMTBLTG5mUGQxRXVNT0dDeU4xRXZPT2NZSEFZMUhtZk1aVjNRRldNVU1Gd2JYMXVWcXpzbVdmc3hIZFZKbXJOZHBCTDBPV1RnYndIV1UwQjFnSnNmek4zSkwxSzcwZWZYQU9FdW9OV1FYWVU?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxPbDlWbXZQTlZVRk15MmRxbHp4TnBuNUw3YXFhN3NyRTdKam1GSHR1Uk9Pa3dRNkpMWkRBLUl1eXlGM3hqVzAweUN6SWc1YlBCVlRGVnpVZlVuRHN6amNzcmdScUw5M0p5ckZheG1BODkyMkJ1TTk2X0pyN2dINXllV2ZEcXBUelBELXAxZC1vYw?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNbl9XRDh5Y0hMVXdFZUpUZ3ExTDRzV0Z6dHYtTWhRQVdrU3l1Z085NFRsYkVocDBWX0xfZzltd25VdW5idENwc1hFNXd0SjFiWTRmY3VEcHBzUjFqdmFzcjQ0RkR6WTRfUGJ3SzdvZUN0SGNwVnROdUtzSC1LeEpKeFJRNzJoMEp1cFZweS1SbWNCdw?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxPZURicFRzOTd2YnRheVByVFd3c3h5eDFlbHFPVmV3ZEZPbW1adG1NaElwdU1kcU5RM25tWjBZb1lqMktlTy1JalcxWXY4ek1QUGxrOVVES2RSN0JMcXVMRmxpOVpENlcyeTFHa3I0VUxEb2g2U2tCMjhjZV9McHRocVNDU2pEbTlkUFJfblF2WQ?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxOb0pfRGxYakdFTWU5eXlYYTd5cGVuVmpzMDFiMDBuX2ZOQVB5aFV1Qmk1dEhXQWwtSVNtU2ZOSTNfVDMxS2NoMUpTbmJ3a0hYOGtvOGJldXlkU3k2N3djaVhDMUNGN0g5Q1J2SzRXMkhXbzI3MUxqd2t5SEszX0JEZWZPUmRSd3VZQmYyZzZZeDNvY0hKaExMcnNTbHhzeTItckpZaEJmbWxodHVla2FKTTN4cmdFY2VjWk96cjdwLUtjX3FMRmZwLVp3SHJiX2xNajBR?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQcWljZDdUS0l6cHpEVmtJYWlLNm5IdFN0RnV6ZmhuLThjODQ4aXhiQl95UE1Pa3ptY1pGRUVrQm5EWVh0SzN5aEVaUF9rUjVBU1YyZHhtMlBRem45b01lY3IwdFZkdmNxWU9LcWVEQTZTM2hjcWVrdmJaRDZDaFlzUWFHVlBNNjBSS0tJQ1MyMk8wazVMLVRCTFJB?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxOWXFmV3NncXdwZnhIbTZmUGJOM2hWUkhHeVdySTRlY3hnRjVVMzk5bVYyN2R1Mk8xbm0xanV0TGVxMFN5UW9haTZhcFpaQXpIc2o1SDBqTThOOVlsMmJKMzVxMTBZRXFnVlZLbTREdW1PeTczbV9CQzExZDBSY2dwakh3d0gyQWRCQzVCY0VydFVkajRfbGliejB4aERfbHV3ckJTM3h5aUZlcmFFc3NMS05zdU1vaFlSdXZv?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPTWFweTVyMV9zZjhXMnVna0dsaWppNUVEMmpCNjlTVjJJcFljd3ExUjZwRlpTT3lrRmxmTGFFYWEyZE1NWUNFQVV1UjJfSTB1enlPUERnYnE5eXM2V2txMUhrdXFUelR6SGFUNndiWjM5WDlVMTFwMV92SW8xLUVRa3Y5cHpxSGpUVlRfYW55OVpBdGM?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQckEtTjZnazV2YS1qTjQxNkxzaXZOU2pjYmZ5S29qRzB5QlJ6Y04wcE9MYzE0c250WjQydHNkeUVDS1Q4RGRTaUFrUkphdFVGYWlqcHNibXNkVFo3QUpKVWZKX29LZTF4NE1INVU1ZkVONnQ3MzVzWXhrQzJ2VVBrZUVkTmVRT0VETVdhUnhWZW9uWFhVaThnbkRJeXEyZw?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxPaWlPYks3MTZ2OWRHU05kZVZhWGpfTzJjVzVPck9lZ29GLVRLUENaa2RZQ0ttVHh2WXhiN19LRUJ0eWp2eEVVQnhlbVdEV1YxT3VleDlfQVdZRGZEbmR5Y1J6bnp5clhxc1ZpREJsYnFQcjdEYTlZY1hERE1obDdvSHNjOTEzMUZtTDhscjUtNXNHd3B1YVV3NUxNNkFDYUhWakN1cEFlLUd2WEdQTVZHRQ?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxPR2NRSjltdlRpOWhqWTUwZ1dwV3FRbUZBZWZqbVhhTWt4NnR6XzVNa2dBS3NSZzVENDFpWlRKT1dRWjVOX05ISVRDU1FpbjBhdVhKanlXSFpXbF9uMkxjUlMtanpCb0hXSWRGZ1FkbmFGQnRLMHVoaHB6TlRzbjVxNGJtOTg?oc=5
- https://news.google.com/rss/articles/CBMi5wFBVV95cUxObUdnZkYxXzBTRmhYR29adzI1M0oxMjZMU1VhX2F0cFpEdkFGNnd3Sk42Y21QZXVNLXA5NTJiQmlXZUpFVWhFNlptbjQyYWR0a09jRUZCZGdoVDJnTGlrOWthVE5qaXhCQkI4a0tWVzV1bTg4dGx6b3YwbUtWUk03UDRjdlh3Nlppd3FiVTgwVUlNSXdfaWdKR0hpTnJuVS1CRENOTGhSN05RbXlpaFdaZG5uOC1HMU1zTWJ1MnFjN1hVUEpubGpnaEZoQmRMdVBzSG1Wcmk2NGdHTmpWWkdxYS1scW54elU?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNM2lKdjlTOWxfNDNhTEk0bEhYWUVMUHE4bnpEVHdzakFsX3A3NHRwcGdpd1pBRHVxRkdESzg5cTc3X0hUZ3ZkM212UVA5c3JQQk43T0NxTXJCSUpPRERFLU1GX1V3ajc5MGV4a1ZiZS1KZmZFcHFhbGxVak93VXZLcWs0N1Y5RTlhbkxBYkg3eGVnOU5tYVYtZGdTVQ?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPQmJ1N3ZZWXo3VXA4TXZrRmJXMVdzU1dOUmJVNFpfenJzQ2VxVXJsX2xhSzJvNTRwU0pJNTN1LWsxSmZ6S2RXYkhVQXdwelZzbFdpcm1IUjRFS2E3NmUtZ2JxckRmdHRlZ1FKNVhsZDAxeGdMbTRpOXNIcm9iaWdJQUJ0ZzdhU0xvU3ROUlVwbEhwRFZ3cEozaWxCQ2FPX3M?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxPQjFUZl9WVGNOMjFocVBIdEtCRHc4Zkx2VWxtRkZiQ1Vic2FrTWNUZUEtNXpNTjNRU0lmSTB4R0JPMVhoYmcxR0U0MXdxckw0eW9FeURQRVZKUkJEWXBxSVVMUVhNU2lmY2tpM3ZnbzVUN05PRmRxQm5GaGVrUm80azVMS29NTmVaMWc?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPQ3JjS2p6X012anh4STM1VWFFZ3NmVGZKdVY2ZG1OX3pYY1lidFJnSVNwMHBCOHpGQ3RPZm5DQ3RfeGtualZVenE0Z2liVERnNnlmZl9SQXBlazdwaUx0UmJybVhDNkNhSUpzVFptMXlUbEkyVWZCQ04ydnhqZ0xCRTJVT1d3bDB3bnA2Vk9mM2tkU2dQODFFaVRYNEkxTmRXRmNMUg?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPaDh0YmZUaTVRLUZENzJXVER4ODlodzRKYjAyTW9HVHJsOUhiRFdWUm1MTzhubnowRHBwdUplUjBuRWdzVmpjc05Nd2EwRVlCTW9GZUo4SFpHWUdwUHkzNWt6SW1ZVG0tc0NNOG9CblhvY2d1N0xYNkkxUzJvRkl5cElkak9OSmE2eFM2UVREV2xtYjVEQk1LWA?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
