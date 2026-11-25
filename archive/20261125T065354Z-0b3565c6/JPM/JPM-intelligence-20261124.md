# JPM Intelligence Report

- ticker: **JPM**
- Report as_of: **2026-11-24**
- Market data as_of: **2026-11-24**
- Quant sources: https://finance.yahoo.com/quote/JPM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/JPM/key-statistics/
- AI analysis snapshot as_of: **2026-11-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-25T07:11:20.076988+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 3, 'ai': 17, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261124T081701Z-6c335e3d/JPM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'directional_claim_without_event_type': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 11 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 16.67%; oldest publication 2026-11-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 317.1000 |
| Return 1D (%) | 0.1390 |
| Return 1W (%) | -3.8974 |
| Return 1M (%) | -4.3670 |
| Return YTD (%) | 0.3064 |
| Return 1Y (%) | 8.4588 |
| Annualized volatility (%) | 23.1601 |
| Beta vs SPY | 0.7696 |
| Max drawdown (%) | -15.4717 |
| Sharpe (rf=0) | 0.4677 |
| Downside deviation (rf=0, %) | 16.7432 |
| Sortino (rf=0) | 0.6470 |
| Historical VaR 95% (1D, %) | 2.4552 |
| Historical ES 95% (1D, %) | 3.3659 |
| Correlation vs SPY | 0.4969 |
| Tracking error vs SPY (%) | 20.3912 |
| P/E (trailing) | 13.30 |
| P/B | 2.40 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 10.20 |
| Forward P/E (estimate) | 12.40 |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 44.79 |
| Return on equity (%) | 18.01 |
| Free cash flow yield (%) | N/A |
| MA50 | 335.5005 |
| Close vs MA50 (%) | -5.4845 |
| MA200 | 322.8744 |
| Close vs MA200 (%) | -1.7884 |
| RSI (14, Wilder) | 37.3025 |
| MACD (12,26) | -5.3808 |
| MACD signal (9) | -2.4597 |
| MACD histogram | -2.9211 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'JPM': 289, 'SPY': 289}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 317.1000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.1390 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -3.8974 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -4.3670 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 0.3064 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 8.4588 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 23.1601 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.7432 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.6470 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.4552 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.3659 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4969 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 20.3912 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.7696 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.4717 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.4677 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 12.3998 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 44.7880 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 18.0130 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 13.3012 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 37.3025 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -2.9211 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -5.4845 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -1.7884 -> Slightly below the moving-average trend level.

## TAILWINDS

### JPMorgan Chase (JPM) Stock Still Looks Like A Bargain On Its 122% Run
- Summary: Stock appears undervalued, suggesting potential upside.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPQzVkNFFCMi1sUzRfQkxuRzdhLWRjaGw2N3N6ZEY3OU9EX0JLLUNRQktEekxYM1JmUlc3TWFGaXZFY0ZlbjNtdHoyVTc4WTdyaDl1eVFkVUlacXFSMHYwNWxNYjlVUTM3WHBjbVBiUnFRRlJoTWlWamF1UlROZVkzbGpwMTlLLUh6V0hJa1dZVlNqdVdER2xFOS1Xbw?oc=5>

### JPMorgan Chase (JPM) Stock Looks Undervalued On Current Profitability
- Summary: Current profitability indicates undervaluation, hinting at upside potential.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxQcS1nNGNZX3pxWV81MlpaVnZhRmtwQ1JJWW92ZWJSczNJN1BRUDdWZmRNTEc1Q2ZBZVdiTFJ0SjhzYmludWtMSWR6VldxMXNJQzh2Nm1BXzVqUlRJQm5Cb0tNSkNOR3lZcVk4RTNWdGk1eThZQkZxUV9jUWoxaHNFVkFPMkFWYmphc1AyX1NpeGZ4QXNqWlRZVERmUVI2Q1pTNDl0VTNYQlNIYlBkUEh6U0c2Vkw4ZlpCT0JUMVd3S01JSGRadmtjRmhERdIBywFBVV95cUxQcS1nNGNZX3pxWV81MlpaVnZhRmtwQ1JJWW92ZWJSczNJN1BRUDdWZmRNTEc1Q2ZBZVdiTFJ0SjhzYmludWtMSWR6VldxMXNJQzh2Nm1BXzVqUlRJQm5Cb0tNSkNOR3lZcVk4RTNWdGk1eThZQkZxUV9jUWoxaHNFVkFPMkFWYmphc1AyX1NpeGZ4QXNqWlRZVERmUVI2Q1pTNDl0VTNYQlNIYlBkUEh6U0c2Vkw4ZlpCT0JUMVd3S01JSGRadmtjRmhERQ?oc=5>

### JPMorgan, HSBC, StoneX complete first digital gold trade in London (JPM:NYSE)
- Summary: First digital gold trade in London involving JPMorgan, HSBC, and StoneX, marking a new product launch.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxQWnZJeTlaTFFpSS0xZXlZSENJVTM5Z3Q0Wm52NF9ia2RfZ3c1YTViNzBQSE1TUWs2amFWVXl3VjFFVmRmWk8tS0hIVFRWTG02a2hSTmJTSmVjZHU5STZJSHhmNFM1VnV4enBoTUlKajdMdGNsRUhUVWpuZFFzUi0zS3otSEdVeEVCUEZQU0VWNXlTSFhwcm9ueTJfMVpZTnQ4Tng2cg?oc=5>

### JPMorgan Chase Financial Company LLC Declares Quarterly Coupon on Alerian MLP Index ETN
- Summary: JPMorgan Chase LLC declares a quarterly coupon on its Alerian MLP Index ETN, providing dividend income to investors.
- Date: 2026-11-20 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxQOW1jbmc1R3N5QkszczFMYURJNjdMN2NSdE82bXdpaWJhMUFfZ3U0SzEwcVlFdFBlR0Nzdlp1QXdCYXdheXJQcmRVSGFBeGRnd1NxWFBFa2IwTXNwTGNQa0FwQldJV0FaamdiVjBJbjZMdHJtRlE0dW5xSnJsNWNBRmNrUnI4TTdNd2trRUo2cjAzTWEweDcwbXgzR3FnTmRTS3RCMmtfdkw1ODZSelZUd3JKRHZSeVk?oc=5>

### Bank of America vs. JPMorgan Chase: Which Financial Stock Is a Better Buy for 2027?
- Summary: Analyst comparison of Bank of America and JPMorgan Chase stocks for 2027 investment prospects.
- Date: 2026-11-17 | Impact: low | Horizon: long | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxNcmNqS0ZTT0JxeUJCUE54SVh5VU55VGtLSXBEallvX2dURVFJT19wZFAxSFZDVV90d2JMMzBkVnBxd1JCQTJ2a0o2OWxfMHpkZ2tkcjF6ME9kUUVnS1NWRV82UUVabi1QLTlKdUkzbFFjZHNBQm41SWs1NS1yS0xLQjA5WHFlUTluVmE4NXl0NFBsU2NkSVk0R2d2TFhYbnNkSlBSa3FrVGlDZkk3N3VLbEF3el90bExNcTlMZmNoY3hlTGI3UkJGNUhoSWJEUQ?oc=5>

## HEADWINDS

### JPMorgan Stock Slides: What's Going On?
- Summary: JPM stock is declining, raising concerns about its short-term performance.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPY25wTkZqdFZDWF93OFdXcFRsSmJWM0oybzR3b3N1OHZ1bURYVjlFZkoySHhQVkxrNjluVTBqQzNIQ2pGWGQwN0ZheXhvbk8yT18xQzYtaDhnSVJYTVA4VVQ4eUNkZDFzNDc5TW1fMXZsMzRGR0FnelpUaVZLeEhkNnpPd2RVLTNncEY4SGluTVA5dE5IbnF3aFFFdFFSQQ?oc=5>

### Third-party vendors of JPMorgan Chase, Visa, Mastercard reportedly faced cyberattacks (JPM:NYSE)
- Summary: Cyberattacks on third‑party vendors threaten JPM operations.
- Date: 2026-11-19 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxNS1daVEN0SlZtVGhOUjZxSTI3TmhybWJYN3dIMkdOVUtYck1LQjhyRUNsMkdhMXo5dWFtUWRxUnVROFloQzI1Y3ZNRWpURFZwakNWM041ekhjTTc2c0JJN1FjRDdST3E4OUdWSk1SdERfWW00aUp6QVl0Q1dHTnNYMFlXQ3JNd0szM2hvSGpyOXM2dlFfR2NwV1VpVXRaS21FLUxzQ19DOHJkNXpNV3V2Uw?oc=5>

### JPMorgan Chase edges higher as cyberattack disclosure raises customer data risk concerns
- Summary: Cyberattack disclosure increases customer data risk, dampening sentiment.
- Date: 2026-11-24 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxQWEdfWVV6RTE5SDJtR1U4LUVZMmZSRUFmM1VjNjZwUmNkQ1JOUmkzeUt5djJNTHlHV3NMYWs3bWFnZEkya0RXSWdiandkRjk0NmFDUDNVdTYtblB6VjA5ZHh1M3FOVm5qelZ5cGNJMWlJY1U3anpERTVfajNTaThnendBM3h6bVYxLXJQcTdzQWltdw?oc=5>

### JPM: SEC Form FWP filed by JP Morgan Chase & Co.
- Summary: JPMorgan filed a SEC Form FWP, indicating regulatory reporting activity.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxQTjRqU0J1WTJrSWh6U2FPNEZIbWptV1BKU0o2QkEzQVlmOHRmZmtIaUcwVTNSQXBUTFBzTldqY1JuVld5NjlxaDcwNWEtVXJhdkZqSXpBbkFnSFVXTnlFUDEyY1NfSzluVG1lOEZXZ0UwUDJValBzaEMyZzhDM2NlRkhVR1pBcWdWVHJj?oc=5>

### JPMorgan Chase announces CFO transition, confirms resolving 'technical issue' (JPM:NYSE)
- Summary: JPMorgan Chase announces CFO transition amid resolving a technical issue, indicating internal changes.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxNbUgxQkh0ZkRTNW9FNlV6TElsVVdudTRKcG9GYlVrYnF4dFNsMVB1LU0wdGVobGxYLTFuSWtSOEVhZThSYy11Q3lJUmRZYWF3V2I3cndtb3plS25NMmtleUxNR21DcFRwajZqR0E1bXFYS253VjVwTUNMRnJyeUtjb3F2Ulpzd3BnVWY1MHdkR2xncGRxMndDQ0prcll2VE5ndlBPVGpFakZIdmlUTU9RRkxB?oc=5>

## CATALYSTS

### JPMorgan Chase (JPM) Receives a Rating Update from a Top Analyst
- Summary: JPMorgan Chase (JPM) Receives a Rating Update from a Top Analyst
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3wFBVV95cUxOWjcyUFpnWTZMQVFNdFcwaUhIak9LQnczREtpTjNLLTlYblJvZWp2ZFhWWS02VDdmZTFKMHVDcFFkaEk2S2RwYlFLVzV0ODkyUnNQeS1oeG52T0lSWXVnQk5rR3R1bThpYWVzVG1Dc0s3NkNhRmtHMzJBTUVyRHFyYzZ2dEJXcHVZRk5JVzdkeWN3ZDhyUU9HSWlUdjBZQTVaNTNIR1ZLcV9yM28tRUZmUmJ2UmRHeHBlaldQRXIzdnU4WnFnMy14RTFoNG5IWWJGM3ozNE01b3RISk8wM1RB?oc=5>

### JPMorgan Chase Earned a Profit in Both 2008 and 2009. History Says That's the Bank to Own If a Recession Hits.
- Summary: JPMorgan Chase Earned a Profit in Both 2008 and 2009. History Says That's the Bank to Own If a Recession Hits.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi5AFBVV95cUxPNVpZTXlfNmdZbGJIeVl5Zk9ySEJGME9WelVkbDU2NFA3NWtlQW83TWJDZVB4cGViWHktZnBFdlMwU3RVczdYY1oweU9zQ0ozMUhsNFV2VzF3bWJGaXRNUVQ3ZWFJZEZmZW9fdHQ1R01yNWFjYmVLY2RGZ1Q2RnZPU3N6M1BORVlRN2RKTXE1TXlleEF0aEp5b2h5NDJIM3UwZmVqZVZtYjBkMTZuS19mZFNIVWdEY25MN3VWeTcwU1FpaGRMakE4a19ONjRBYllZZ2pmUTB3dkt2MEJoZS1XMERXdWU?oc=5>

### JPMorgan Chase & Co. $JPM Stock: Cibc World Market Inc. Cuts Position
- Summary: JPMorgan Chase & Co. $JPM Stock: Cibc World Market Inc. Cuts Position
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxOVG1uRXlnZExYY3JUM3hUbzM5SVdzbmZncnJyZEZZWXUwd1JWZ01hWE0wckVPYVlKNGpRMUxMWmw0cGs5eXc2dnZUd3I3SUtVSDN1U3dod1J6WFhtclVZczBUYk9hcDV2Z0JoTzIwWS1XcW5aeng4R3V4dWh5UmlRaWtmMlZMZkI1bWVCQ2I2d1lVb0R5dS1jdmNWMEdGVWpVTndnRnBhVGxpOWRpRzNaMGR2MFVNUkQ1OThrbU1nVHVlUQ?oc=5>

### Investors Heavily Search JPMorgan Chase & Co. (JPM): Here is What You Need to Know
- Summary: Search interest spikes for JPM, indicating heightened investor attention.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxOTi1Qa21zWU1iRlVjR0ZvUTNYYnNHQjNucnBpWFZlYU5MSmZuTkxJZ3c5ZGFlRWJRODl1cWs2dzBNLUMxNlhpckotWmNua3NQMlN2OVdCTXVUMGQyN3R5SExOM2RpOUJ0QURHeUFYN2dpeWxBUVowZ21Sc2lpcTh2d1lfRGl1YXpETGE2cjR1NHBvUmJIa0hBSURUY0dmUFpDZVVOMFZvRQ?oc=5>

### JP Morgan Chase & (JPM): Auto-callable note tied to lowest of three indices, due 2029
- Summary: New auto-callable note linked to three indices, maturing 2029.
- Date: 2026-11-20 | Impact: low | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxQMzdFRGdmS3hBaDZSZ0xKRW5sZmJkVDdqbEVtTVJrblZveHlpbVRlZzc1OWhDSVBsNlVNQUxmM0x3dUpScmVfNTRqT2hncFpZU1U2U0Vnc3g5TEVjLXlreHcwdkFUWVhibktJa0xKWm0zZWw0ZHRUemV5aEgzdVpqVjZnWXJUMHBHalRJ?oc=5>

### JPMorgan's bond fund will leave the NYSE on Dec. 16
- Summary: JPM bond fund delisting from NYSE scheduled for December 16.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxQX1dLNXlUSHBhdVg2NGoxcFQtSEtoc3lQSWpFNm1UVDM0LTItbVBfajBHY0ZzdS1kcTJFU3RuYTk4SDRrdXBkbzNpaG14QUJNTWhmUE1pdGphVUF1d2xnOE5NT0h6Q2lXb1FQakYwTWFJWnBoTTNyRDQ3N3FUTzNPeGRfVnluc0t3bDJuOXpidVZlMHJhLTBuV0dQNEsxWkxESWVjQXRMY3kyOUVaTkZ2SGl0Z1V0bE5iZVdV?oc=5>

### J.P. Morgan Private Bank expanding in Dallas to tap alternative assets sector (JPM:NYSE)
- Summary: J.P. Morgan Private Bank expands in Dallas to access alternative assets, enhancing service offerings.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxOX2NlWVZVUWYtQlN4aWJGak9XaXNkTXNSVXZRTWxpbHFCTFBMcXBTUHF2MjVkNFhLMmpERFpua0NYVGNBS2FZREJGRk41b09rcGp2c0EwUmdpOGZyaVhSTDlnd0ozVVVRUk0zdnNpR2R6YkdlM2hjSHFZSVcySFFpS21DSVV0WURYd3Q1cnVqZWRmOUtHbm1hQkpDVloxWWx2VkJZTTMxME05Z2lPdTlJVVl5UTI?oc=5>

## RISKS

### Visa, Mastercard, JPMorgan Hit By Reported Data Leak, Payment Information Not Affected
- Summary: Data leak reported affecting JPMorgan, Visa, Mastercard; payment data safe.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNemtoLTNrQVB1M1loZGQyaUtzUkdiZDVHNDBkRF8waURYakthUVpueGRSUTZGMnc1VVlscGVLeEtZRl93V1hXNzR5VkhNcmg2SUtyOXBQQWlJZnFnU2FwYzZlNktrM3NReXJCVEtaYTV1b0g2ZHVZUFVZY3FPMHlfRWVrNHVVeTZKWWt3QnM2LW45ZVU3QmxzelF4SmRRYUE?oc=5>

### JP Morgan Chase & (JPM): JPMorgan notes tied to S&P 500 and Russell 2000 due December 2030
- Summary: Notes due 2030 tied to indices pose long‑term risk.
- Date: 2026-11-24 | Impact: medium | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxQcXdGNmdTNlI4aTVBeThaeVpuU2Z2UTNhb0VfZngwc1cwYmNUVnN1eEJhWVBjd0RaSWxTY1kwVXl2NnJyQzlBbjhwclg1a1Z5ZEViZUFNWnljbC13Q0dBN29zWXVaVW1GWF8zdmxzUnd6ZEJRVThEUVR4Z0hNMDhaVDNlSEJ4S3d5emQw?oc=5>

### JPMorgan Chase (JPM) Says Vendor Cyberattack Exposed Customer Data
- Summary: Vendor cyberattack exposed customer data, posing significant security risk to JPMorgan Chase.
- Date: 2026-11-22 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxPZVF5aFBkb2l0THVYcnNDTVZ1RmJlWlREZHRqS2xBQlBkNXRvUXNyMWVGVTRxTmViWGZjVzFMbnRXNnRGR2JOYWNJQ0hvUEZPdi1rMzlIcnh5dGJ5Y2M4bUZYYktKS0k3ZVJDVVpIX0w2UFZQSEtLY0sxcXdIQmFVdG5TNThINDU2UFhSZXNBWWl5UTdqbThGQUdIYlItcUpmdDFaM1JKSmtwWjNVUWctSGZKanZBaHJhOTJUa3hDaUo3VDdITjYxWHh30gHKAUFVX3lxTE9lUXloUGRvaXRMdVhyc0NNVnVGYmVaVERkdGpLbEFCUGQ1dG9Rc3IxZUZVNHFOZWJYZmNXMUxudFc2dEZHYk5hY0lDSG9QRk92LWszOUhyeHl0YnljYzhtRlhiS0pLSTdlUkNVWkhfTDZQVlBIS0tjSzFxd0hCYVV0blM1OEg0NTZQWFJlc0FZaXlRN2ptOEZBR0hiUi1xSmZ0MVozUkpKa3BaM1VRZy1IZkpqdkFocmE5MlRreENpSjdUN0hONjFYeHc?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **JPM** | **13.30** | **2.40** | **N/A** | **10.20** | **842,093,821,952.00 USD** | **8.46** |
| BAC | 11.59 | 1.24 | N/A | 3.40 | 335,074,164,736.00 USD | -4.50 |
| C | 11.10 | 0.98 | N/A | 8.00 | 188,445,032,448.00 USD | 16.57 |
| WFC | 11.45 | 1.54 | N/A | 0.40 | 243,720,241,152.00 USD | -1.94 |

Peers fetched as_of: 2026-11-24; JPM reuses existing data (market data as_of: 2026-11-24); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-13
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

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
- Filing date: 2026-11-03
- Revenue (latest available single quarter): 24,246,000,000.00 USD; period 2014-07-01/2014-09-30; fiscal year/reporting period 2014/Q3
- Net income (latest available single quarter): 15,305,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/19617/000162828026069523/jpm-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimwFBVV95cUxPQzVkNFFCMi1sUzRfQkxuRzdhLWRjaGw2N3N6ZEY3OU9EX0JLLUNRQktEekxYM1JmUlc3TWFGaXZFY0ZlbjNtdHoyVTc4WTdyaDl1eVFkVUlacXFSMHYwNWxNYjlVUTM3WHBjbVBiUnFRRlJoTWlWamF1UlROZVkzbGpwMTlLLUh6V0hJa1dZVlNqdVdER2xFOS1Xbw?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxQcS1nNGNZX3pxWV81MlpaVnZhRmtwQ1JJWW92ZWJSczNJN1BRUDdWZmRNTEc1Q2ZBZVdiTFJ0SjhzYmludWtMSWR6VldxMXNJQzh2Nm1BXzVqUlRJQm5Cb0tNSkNOR3lZcVk4RTNWdGk1eThZQkZxUV9jUWoxaHNFVkFPMkFWYmphc1AyX1NpeGZ4QXNqWlRZVERmUVI2Q1pTNDl0VTNYQlNIYlBkUEh6U0c2Vkw4ZlpCT0JUMVd3S01JSGRadmtjRmhERdIBywFBVV95cUxQcS1nNGNZX3pxWV81MlpaVnZhRmtwQ1JJWW92ZWJSczNJN1BRUDdWZmRNTEc1Q2ZBZVdiTFJ0SjhzYmludWtMSWR6VldxMXNJQzh2Nm1BXzVqUlRJQm5Cb0tNSkNOR3lZcVk4RTNWdGk1eThZQkZxUV9jUWoxaHNFVkFPMkFWYmphc1AyX1NpeGZ4QXNqWlRZVERmUVI2Q1pTNDl0VTNYQlNIYlBkUEh6U0c2Vkw4ZlpCT0JUMVd3S01JSGRadmtjRmhERQ?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxQWnZJeTlaTFFpSS0xZXlZSENJVTM5Z3Q0Wm52NF9ia2RfZ3c1YTViNzBQSE1TUWs2amFWVXl3VjFFVmRmWk8tS0hIVFRWTG02a2hSTmJTSmVjZHU5STZJSHhmNFM1VnV4enBoTUlKajdMdGNsRUhUVWpuZFFzUi0zS3otSEdVeEVCUEZQU0VWNXlTSFhwcm9ueTJfMVpZTnQ4Tng2cg?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxQOW1jbmc1R3N5QkszczFMYURJNjdMN2NSdE82bXdpaWJhMUFfZ3U0SzEwcVlFdFBlR0Nzdlp1QXdCYXdheXJQcmRVSGFBeGRnd1NxWFBFa2IwTXNwTGNQa0FwQldJV0FaamdiVjBJbjZMdHJtRlE0dW5xSnJsNWNBRmNrUnI4TTdNd2trRUo2cjAzTWEweDcwbXgzR3FnTmRTS3RCMmtfdkw1ODZSelZUd3JKRHZSeVk?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxNcmNqS0ZTT0JxeUJCUE54SVh5VU55VGtLSXBEallvX2dURVFJT19wZFAxSFZDVV90d2JMMzBkVnBxd1JCQTJ2a0o2OWxfMHpkZ2tkcjF6ME9kUUVnS1NWRV82UUVabi1QLTlKdUkzbFFjZHNBQm41SWs1NS1yS0xLQjA5WHFlUTluVmE4NXl0NFBsU2NkSVk0R2d2TFhYbnNkSlBSa3FrVGlDZkk3N3VLbEF3el90bExNcTlMZmNoY3hlTGI3UkJGNUhoSWJEUQ?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPY25wTkZqdFZDWF93OFdXcFRsSmJWM0oybzR3b3N1OHZ1bURYVjlFZkoySHhQVkxrNjluVTBqQzNIQ2pGWGQwN0ZheXhvbk8yT18xQzYtaDhnSVJYTVA4VVQ4eUNkZDFzNDc5TW1fMXZsMzRGR0FnelpUaVZLeEhkNnpPd2RVLTNncEY4SGluTVA5dE5IbnF3aFFFdFFSQQ?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNS1daVEN0SlZtVGhOUjZxSTI3TmhybWJYN3dIMkdOVUtYck1LQjhyRUNsMkdhMXo5dWFtUWRxUnVROFloQzI1Y3ZNRWpURFZwakNWM041ekhjTTc2c0JJN1FjRDdST3E4OUdWSk1SdERfWW00aUp6QVl0Q1dHTnNYMFlXQ3JNd0szM2hvSGpyOXM2dlFfR2NwV1VpVXRaS21FLUxzQ19DOHJkNXpNV3V2Uw?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxQWEdfWVV6RTE5SDJtR1U4LUVZMmZSRUFmM1VjNjZwUmNkQ1JOUmkzeUt5djJNTHlHV3NMYWs3bWFnZEkya0RXSWdiandkRjk0NmFDUDNVdTYtblB6VjA5ZHh1M3FOVm5qelZ5cGNJMWlJY1U3anpERTVfajNTaThnendBM3h6bVYxLXJQcTdzQWltdw?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxQTjRqU0J1WTJrSWh6U2FPNEZIbWptV1BKU0o2QkEzQVlmOHRmZmtIaUcwVTNSQXBUTFBzTldqY1JuVld5NjlxaDcwNWEtVXJhdkZqSXpBbkFnSFVXTnlFUDEyY1NfSzluVG1lOEZXZ0UwUDJValBzaEMyZzhDM2NlRkhVR1pBcWdWVHJj?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxNbUgxQkh0ZkRTNW9FNlV6TElsVVdudTRKcG9GYlVrYnF4dFNsMVB1LU0wdGVobGxYLTFuSWtSOEVhZThSYy11Q3lJUmRZYWF3V2I3cndtb3plS25NMmtleUxNR21DcFRwajZqR0E1bXFYS253VjVwTUNMRnJyeUtjb3F2Ulpzd3BnVWY1MHdkR2xncGRxMndDQ0prcll2VE5ndlBPVGpFakZIdmlUTU9RRkxB?oc=5
- https://news.google.com/rss/articles/CBMi3wFBVV95cUxOWjcyUFpnWTZMQVFNdFcwaUhIak9LQnczREtpTjNLLTlYblJvZWp2ZFhWWS02VDdmZTFKMHVDcFFkaEk2S2RwYlFLVzV0ODkyUnNQeS1oeG52T0lSWXVnQk5rR3R1bThpYWVzVG1Dc0s3NkNhRmtHMzJBTUVyRHFyYzZ2dEJXcHVZRk5JVzdkeWN3ZDhyUU9HSWlUdjBZQTVaNTNIR1ZLcV9yM28tRUZmUmJ2UmRHeHBlaldQRXIzdnU4WnFnMy14RTFoNG5IWWJGM3ozNE01b3RISk8wM1RB?oc=5
- https://news.google.com/rss/articles/CBMi5AFBVV95cUxPNVpZTXlfNmdZbGJIeVl5Zk9ySEJGME9WelVkbDU2NFA3NWtlQW83TWJDZVB4cGViWHktZnBFdlMwU3RVczdYY1oweU9zQ0ozMUhsNFV2VzF3bWJGaXRNUVQ3ZWFJZEZmZW9fdHQ1R01yNWFjYmVLY2RGZ1Q2RnZPU3N6M1BORVlRN2RKTXE1TXlleEF0aEp5b2h5NDJIM3UwZmVqZVZtYjBkMTZuS19mZFNIVWdEY25MN3VWeTcwU1FpaGRMakE4a19ONjRBYllZZ2pmUTB3dkt2MEJoZS1XMERXdWU?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxOVG1uRXlnZExYY3JUM3hUbzM5SVdzbmZncnJyZEZZWXUwd1JWZ01hWE0wckVPYVlKNGpRMUxMWmw0cGs5eXc2dnZUd3I3SUtVSDN1U3dod1J6WFhtclVZczBUYk9hcDV2Z0JoTzIwWS1XcW5aeng4R3V4dWh5UmlRaWtmMlZMZkI1bWVCQ2I2d1lVb0R5dS1jdmNWMEdGVWpVTndnRnBhVGxpOWRpRzNaMGR2MFVNUkQ1OThrbU1nVHVlUQ?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxOTi1Qa21zWU1iRlVjR0ZvUTNYYnNHQjNucnBpWFZlYU5MSmZuTkxJZ3c5ZGFlRWJRODl1cWs2dzBNLUMxNlhpckotWmNua3NQMlN2OVdCTXVUMGQyN3R5SExOM2RpOUJ0QURHeUFYN2dpeWxBUVowZ21Sc2lpcTh2d1lfRGl1YXpETGE2cjR1NHBvUmJIa0hBSURUY0dmUFpDZVVOMFZvRQ?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxQMzdFRGdmS3hBaDZSZ0xKRW5sZmJkVDdqbEVtTVJrblZveHlpbVRlZzc1OWhDSVBsNlVNQUxmM0x3dUpScmVfNTRqT2hncFpZU1U2U0Vnc3g5TEVjLXlreHcwdkFUWVhibktJa0xKWm0zZWw0ZHRUemV5aEgzdVpqVjZnWXJUMHBHalRJ?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxQX1dLNXlUSHBhdVg2NGoxcFQtSEtoc3lQSWpFNm1UVDM0LTItbVBfajBHY0ZzdS1kcTJFU3RuYTk4SDRrdXBkbzNpaG14QUJNTWhmUE1pdGphVUF1d2xnOE5NT0h6Q2lXb1FQakYwTWFJWnBoTTNyRDQ3N3FUTzNPeGRfVnluc0t3bDJuOXpidVZlMHJhLTBuV0dQNEsxWkxESWVjQXRMY3kyOUVaTkZ2SGl0Z1V0bE5iZVdV?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxOX2NlWVZVUWYtQlN4aWJGak9XaXNkTXNSVXZRTWxpbHFCTFBMcXBTUHF2MjVkNFhLMmpERFpua0NYVGNBS2FZREJGRk41b09rcGp2c0EwUmdpOGZyaVhSTDlnd0ozVVVRUk0zdnNpR2R6YkdlM2hjSHFZSVcySFFpS21DSVV0WURYd3Q1cnVqZWRmOUtHbm1hQkpDVloxWWx2VkJZTTMxME05Z2lPdTlJVVl5UTI?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNemtoLTNrQVB1M1loZGQyaUtzUkdiZDVHNDBkRF8waURYakthUVpueGRSUTZGMnc1VVlscGVLeEtZRl93V1hXNzR5VkhNcmg2SUtyOXBQQWlJZnFnU2FwYzZlNktrM3NReXJCVEtaYTV1b0g2ZHVZUFVZY3FPMHlfRWVrNHVVeTZKWWt3QnM2LW45ZVU3QmxzelF4SmRRYUE?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxQcXdGNmdTNlI4aTVBeThaeVpuU2Z2UTNhb0VfZngwc1cwYmNUVnN1eEJhWVBjd0RaSWxTY1kwVXl2NnJyQzlBbjhwclg1a1Z5ZEViZUFNWnljbC13Q0dBN29zWXVaVW1GWF8zdmxzUnd6ZEJRVThEUVR4Z0hNMDhaVDNlSEJ4S3d5emQw?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxPZVF5aFBkb2l0THVYcnNDTVZ1RmJlWlREZHRqS2xBQlBkNXRvUXNyMWVGVTRxTmViWGZjVzFMbnRXNnRGR2JOYWNJQ0hvUEZPdi1rMzlIcnh5dGJ5Y2M4bUZYYktKS0k3ZVJDVVpIX0w2UFZQSEtLY0sxcXdIQmFVdG5TNThINDU2UFhSZXNBWWl5UTdqbThGQUdIYlItcUpmdDFaM1JKSmtwWjNVUWctSGZKanZBaHJhOTJUa3hDaUo3VDdITjYxWHh30gHKAUFVX3lxTE9lUXloUGRvaXRMdVhyc0NNVnVGYmVaVERkdGpLbEFCUGQ1dG9Rc3IxZUZVNHFOZWJYZmNXMUxudFc2dEZHYk5hY0lDSG9QRk92LWszOUhyeHl0YnljYzhtRlhiS0pLSTdlUkNVWkhfTDZQVlBIS0tjSzFxd0hCYVV0blM1OEg0NTZQWFJlc0FZaXlRN2ptOEZBR0hiUi1xSmZ0MVozUkpKa3BaM1VRZy1IZkpqdkFocmE5MlRreENpSjdUN0hONjFYeHc?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
