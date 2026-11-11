# TSM Intelligence Report

- ticker: **TSM**
- Report as_of: **2026-11-10**
- Market data as_of: **2026-11-10**
- Quant sources: https://finance.yahoo.com/quote/TSM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TSM/key-statistics/
- AI analysis snapshot as_of: **2026-11-10**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-11T04:50:15.804749+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 3, 'ai': 16, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261110T055129Z-abd33250/TSM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'directional_claim_without_event_type': 1, 'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 16 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 28.0%; oldest publication 2026-11-09

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 396.4800 |
| Return 1D (%) | 2.0225 |
| Return 1W (%) | -2.0553 |
| Return 1M (%) | -12.5367 |
| Return YTD (%) | 31.4941 |
| Return 1Y (%) | 35.6983 |
| Annualized volatility (%) | 41.6385 |
| Beta vs SPY | 2.1495 |
| Max drawdown (%) | -27.3158 |
| Sharpe (rf=0) | 0.9446 |
| Downside deviation (rf=0, %) | 28.7144 |
| Sortino (rf=0) | 1.3697 |
| Historical VaR 95% (1D, %) | 4.2423 |
| Historical ES 95% (1D, %) | 5.7594 |
| Correlation vs SPY | 0.7057 |
| Tracking error vs SPY (%) | 33.4247 |
| P/E (trailing) | 25.19 |
| P/B | 75.67 |
| EV/EBITDA | 3.67 |
| Revenue growth (%) | 50.90 |
| Forward P/E (estimate) | 16.95 |
| Gross margin (%) | 65.85 |
| Operating margin (%) | 58.66 |
| Return on equity (%) | 41.85 |
| Free cash flow yield (%) | N/A |
| MA50 | 430.4612 |
| Close vs MA50 (%) | -7.8941 |
| MA200 | 400.6428 |
| Close vs MA200 (%) | -1.0390 |
| RSI (14, Wilder) | 44.0698 |
| MACD (12,26) | -14.4955 |
| MACD signal (9) | -11.1913 |
| MACD histogram | -3.3042 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TSM': 279, 'SPY': 279}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 396.4800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.0225 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.0553 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -12.5367 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 31.4941 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 35.6983 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 41.6385 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 28.7144 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.3697 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.2423 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.7594 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.7057 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 33.4247 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.1495 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.3158 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9446 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.9542 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 65.8460 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 58.6550 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 41.8550 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 25.1893 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 44.0698 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.3042 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -7.8941 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -1.0390 -> Slightly below the moving-average trend level.

## TAILWINDS

### TSMC Stocks Rise 1.64% After October Sales Jump 59.7% to a Record
- Summary: TSMC Stocks Rise 1.64% After October Sales Jump 59.7% to a Record
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxNZWRRUzluaGY2SldjRmZEc3hoNWlCLXFfUW5KRlNSSVJrUU5HTWtKZ0VJQ2wwdmcyTmI4SENBS1NoU1hjaHBmaEd5bldjWHZwOXRkLVZycEMtTnFDNmJVcm1mcHNmbUE0amZBd3dXSXBrREVmemVrTm02b0ZJN3F1STZfS3BodEFMUzVBMzZ0QjFGNFpWWFh0aEpTOVlKc094Ny13Q3Bka1FjYWUwcVZYalFGQ2s1YzlncTZNZ3o0Zzg?oc=5>

### TSMC Stocks Rise 1.64% After October Sales Jump 59.7% to a Recor
- Summary: TSMC Stocks Rise 1.64% After October Sales Jump 59.7% to a Recor
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNZ005S3JHLXVpN3VIcklQdnJBWWhCZWhVVFE5WGF2MS1HMGRPVXljYkF3dG9mYXNSbjBVV1hIa2t1Q2RzSnBRWUNpODdjMDhlSmd5eDg3anVfWS0wV2ZzZ1NmUUpmZV9sVlpmVTAxc2l0bFdUT1dfT2laVTk4TkR6S3J3TWMxMkc2LTB0dGpRX3RvYUowQ3Vkc2U2cEVYRndUUUE?oc=5>

### TSMC (NYSE:TSM) Stock Rises as Sales Surge 60% and $1 Billion OpenAI, Anthropic Investment Plan Emerges
- Summary: TSMC (NYSE:TSM) Stock Rises as Sales Surge 60% and $1 Billion OpenAI, Anthropic Investment Plan Emerges
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTE1TX0dnVFNvcHhXQ3kxbHYtUFdxZ2hRQWMtbU5qek5jNWFGdEVCZE55WUg0aEZPN3RNeTJXUHotMlYxUE9tVFNMaDYxMnNHU3VnM0JjWW44UU94eG5TQXFNLUp6VXdudlA1ZlR6NHA0eHBYY3h1bjNYUF9XaWhDZw?oc=5>

### Taiwan Semiconductor Sales Jump 60% In October As AI Boom Continues
- Summary: TSM reports a 60% sales increase in October driven by AI demand.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNdXVPN1FxVkpoWXdpeG9DdDJyNEl5aUlMWF8yZVM2aG1SNkdTbUFMNnQwQWFMMjhkNjJkOVdjb19IQTRtQzJBZ085alZEdjVpLTFMek9haGlValNDZzFTR3lfNnpmc1BPRk44N2RuWHR1dE03SWdTMXhHVGRSQm1ONkJpSkJVZmhvRzdLUEQwdUx4VHUzbnpN?oc=5>

### TSMC to invest up to $1 billion in Anthropic, OpenAI
- Summary: TSM plans a $1B investment in Anthropic and OpenAI to support AI chip development.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPY2I3VHRfaEF6T19qN28tZEVhN0piNERjTFpJRVlDMFdTLXJUZTlNdGJXblVLTVpEY0QzUVdvay1IazlCNTBmbGFWQ3NlNkIxRzBZSTIwSEJGUnJKTjl2YkZrUVdLVzB3T1V2WkRhRVAzcmVCVFJ6RjRfUEJveDZnWTlFYTBRZl9sMFlIUGZZaXlibmc?oc=5>

### TSMC Is at the Center of an AI Boom That Flipped 25 Years of U.S. Trade. Is the Stock a Buy?
- Summary: AI boom positions TSMC as a key player, boosting demand for its chips.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxPVVlBamVBWGZsQi0wcmNOQnJiU1JFOTgxbnNtYlZaS2tYSkRRT3E3TDVmTVQ4SHQyaUZhZFQ3MlBmWV9tSnNTUWNLemFrNWtBRWFESWFNT3A3WWozbUhKN3VKRmVwZ3B2UkhSWXNiOUFQNnZfYVlEWmFzVkZLbTVOQ2RsZkQ1NDlwQl9BOGY2b0twUmFTaWpEeF91a3ltSm1JbDdrZHBIVFVWMDcwdzIyWXpBSU5zZ2I5ZkdGaEV4XzNuU09vRjBXNW9IV2o?oc=5>

### What Does Taiwan Semiconductor Manufacturing (TSM) AI Revenue Surge Mean For Investors?
- Summary: TSM's AI revenue surge signals strong product demand, boosting investor confidence.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxPdHZ6QnVWUlEtOE5fb0dnOGRMbEttQ1FIM0dTdy1CZzloTk1Tc0RaNm40VTB1YjR1bmpnVmRFelE5RjlyeGJQQl9lY2s5SThnZ1d2QmRHbnM0cHVFTnZCcXh6QzRqZVN0TFoyOGVpSExjYm56czYydkdZLV9YX1RYYWdBY1hMRWlTQVhWR2MxQmp1clVoTW93b2J6NVdTZEdjdGZMc041NldwODR4?oc=5>

### Taiwan Semiconductor Manufacturing (TSM) executive Yuan bought 43 shares for $3,032 at $70.50
- Summary: Insider purchase by executive Yuan indicates confidence in TSM's prospects.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNYlJiS2Q1OF9KcnZtZUxVdm85U3BMLXBnMmYyS2pOUVpaWllZUVZSamxOdTY2eXFUa1pWYkxYQXhLQTNXTmRQR21iejJ0NFdWblNZRDBiaHFRdlRPLXZET3JJNElCZHpGa0F5NEJxTHExLXlZeV9rZklfMUtndkRkandTQmNhdTdTVVh3R3Z5eVgwLWoyaGxQTA?oc=5>

### Taiwan Semiconductor Manufacturing (TSM) executive Chuang bought 48 shares for $3,384 at $70.50
- Summary: Insider purchase by executive Chuang signals management confidence.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQOXlCU0M2TFhqbDZSTVZkN2UxaXY3NXNoSVhvUUtxV3o1TjJYOWNpWnFhMFV3T3JMbE1WeVE1VWsxSWJFdk00YkJrOS1ob0xSaEtMemdDZW4wdTRzQ1padkRTVVRVd1V5eTMxcnRIbnpFQWlQSmVDbFRFV0NLZEZXNVlUVXZMNFlwMS14eDVrMVhmNnNlYzVJRjh6dk5FZw?oc=5>

### Wedbush Has a Strong Message for TSMC Stock Fans
- Summary: Wedbush analyst endorses TSMC, suggesting positive outlook.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxORk9oU1JVdGlRMFByRzFoVC1yU2d2TjlIMUVmdnVIRXY3am53NkdfaF9LNTloYWtSUUQyS0JvakxRU1lXNTBnbTkyR0I2OE9IUHJsbGFNRl8wX0RGdktPQjdvRlliek05TUVpa0JwTjNJSXpZUDdEY21FNDM4MHl6UWpzeTB1OWluSXpwZmpQVFVLRWZ3RmI4N2VLZDBwenc?oc=5>

## HEADWINDS

### Taiwan Semiconductor Manufacturing (TSM) Stock Could Be 7% Undervalued Despite Fab Expansion Plans
- Summary: Analysts suggest TSMC may be undervalued, indicating potential downside risk.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxNclhidVc5Z2VTNE9uZzRCcldGRDUzLXcyc1otalhRaExZNHR2cVRPNk03Z052ekExdUt1QzgxWGkya1NHcElYeWowOXRESHM1UFlsZUx3Yi14bUFHcHp3bVJuTlJPUDlzZFZjYV9URFR6b19NQVRtYUhMdFNobGIwWWFJb1JwODdWM1h6ZjQ4RS1obDRfNUkxdHdGUDdFR0JqbkhnX2ZzVUtRTml2Nmc?oc=5>

## CATALYSTS

### TSMC earmarks up to $1bn to buy Anthropic and OpenAI shares
- Summary: TSMC invests in AI firms, strengthening its AI ecosystem presence.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxOX3lnNU1VVFk4T18zOEhrOVBOalRYV3BNSV9qZDhkQzZoZTdKSk4tU2lNMEd5eXc4NXlTckpIYmZvaHlfeXZ5MVI3amtRdDQyckdnTHNCWmQ5anB4YW1ZT3l6NDVNUGhnOFpQQ254SS1VUjhXckNPMzJfMFhyalh3VE8wMmZfeW4tSnZHdWN2UUVUN2J4RHEyNjBmc3pkT1BfUzlsY1lVN2ZWZ3FCdE9SZHlzU244SVBoQkpXcXBVbnNrckRt?oc=5>

### Taiwan Semiconductor Manufacturing (TSM) CFO Huang bought 30 shares for $2,115 at $70.50
- Summary: Insider purchase signals confidence in TSMC's prospects.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQOWxRYmU0Y2tka0Jhck5VN2psUVlscUZ2bmtZQVR2ZHZhc1VKZmVfQmdDemVTbTdnUHNzcS1pRGJuNlhQRVR1YnFVLVdhYi1JQUlVcHRTWFVZc29jUGZjUzRCNjNEcVRVMG43Q0xRQVZQSDJzTUZRam1wbU1ZTlNQLWhJazZrdkNDeTFwSEh5TFlEWVhMMmtMTWFGeUdhUQ?oc=5>

### Taiwan Semiconductor Manufacturing (TSM) executive Lin bought 50 shares for $3,525 at $70.50
- Summary: Executive share purchase indicates management confidence.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPVzMycFlnUjVmcWNZakVSRjJmMnJVTXQzMEFDdGJYMnlYRlAtSGhiZ0VwZ3ktcDd6QUlUWHNOaEVfOERsMXh0dWYtWGgtMS10Wld3SHV6R1RoOExRMEdrZkQ1czhwSkVDbXFMX1c5dGI5aUZuYzhPRkwtVVRZUUplZ2kyaVdES3hSanVrRUl4WGFqVm11aDV2Qmhn?oc=5>

### Taiwan Semiconductor Manufacturing (TSM) COO Zhang bought 65 shares for $4,583 at $70.50
- Summary: TSM COO Zhang purchased 65 shares at $70.50, indicating insider confidence.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxPdVhGMHJxSmRrQW5HSWdxS2sxOHRQd2R6Wmd3TldJOWhMbWt1QUp4MkZfM3NqTUxBR0xZNUNaQUVxRmxpVjRzeHVXRVpPTU0wd3MyN0Faa3J2RTIyTXlDVDhQZnQ3ejM1aDZ0UE0ycHBCd3NUNFdMZGpUaEc3UHZzOXkzaDhZQ3F4TnV5RE4xY3BqRm5jSVpMcERKcEpESnpMZllqTkdPdw?oc=5>

### Taiwan Semiconductor Manufacturing (TSM) executive Chen bought 48 shares for $3,384 at $70.50
- Summary: TSM executive Chen bought 48 shares at $70.50, showing insider interest.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOZmpMSExKY3duZF9LbGtCMVVNYzFUV2hILTR2MEh5eG41ZmtfT1FPUkJQTlpxdVpoeThnbzV6azdXVnppNWRmTzFBVnNud05ZOU5MY3ZHS1VLQk1uQy1SWUR1VEtoQlRjSEEwRG8ybUFUd3pPcjY3emEzUGNOZzZqUXczeThIamJWTHBvOG9qRFdpOGRzRHJtN0F0UHM?oc=5>

### Taiwan Semiconductor Manufacturing (TSM) executive Hwang bought 41 shares for $2,891 at $70.50
- Summary: TSM executive Hwang purchased 41 shares at $70.50, reflecting insider activity.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOM3M1NHQyXzhFT0pEcnc0eWFPaTlKbURhQWRvZHZTU0ZNVzZla0ZrWmJXMXVBeldiY0tuc0c5cHNzVUFGMEtpNmxkem1nYlc4ZG85ZUpLU3dwR3V1TnpzeWVIY2MwTnFmOEVzNXhDLUtpaVU2czVPcWs5SGw0NjhKWHNiVnR5M2VSdFVWVmcxQ3ZnOHVjbFRxWUR3aXI?oc=5>

### Taiwan Semiconductor's October sales offer up 'strong start' to quarter, Wedbush says (TSM:NYSE)
- Summary: Wedbush reports TSM's October sales suggest a strong quarter start, indicating positive outlook.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxNNC1ndEJPQjN3V0RWSTJCaXlPWV94TUY1RzFjemY5S1R6c2FNYXdCTHFZc0ozdlFjellvbWxrMU9BaGFRZk83RVZLZXVZTHBTblYwamxab0h4X3drLV9YdEo0UXowa2g0bjFlMVhhUjRYSjRjUkZ1OHZOcEc2S1VYU3I1VEI4UldwUW9uT2dpcDhWWDNSQklDR3dSUHRUS1FrVEZTOTBMcXFaUjZVZmlhUkZ2Z3VkdzN5Nmkw?oc=5>

## RISKS

### What Is Going on With Taiwan Semiconductor Stock on Monday?
- Summary: Inquiry about TSM stock movement on Monday.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxNdlVNUlBPLXliejk5cW53UXNqT0FxZTBBUnQ1ZlhjS2dldDZGSjl2QUsyT3BGY2Q3OGRkUWw3VmV1TFgxVU05eGdJRXZRckQ0ZXU0di1nMGdoYzhJX3YzWGxVcGIxbm9FR0Z2bEpQenM4bkhsNkcydFVCLUtOeHVMd1htQ0ZuV185SVV4bTgzM2l5YjlONURuc0FyWHN2NFpyS2hSdDJyMm8yRE5TWGVZcg?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TSM** | **25.19** | **75.67** | **3.67** | **50.90** | **2,056,333,295,616.00 USD** | **35.70** |
| UMC | 14.19 | 2.59 | -0.29 | 25.60 | 37,717,221,376.00 USD | 105.98 |
| GFS | 116.06 | 1.90 | 10.90 | 12.50 | 22,643,568,640.00 USD | 17.79 |
| INTC | N/A | 2.69 | 16.81 | 20.90 | 308,960,952,320.00 USD | 51.18 |

Peers fetched as_of: 2026-11-10; TSM reuses existing data (market data as_of: 2026-11-10); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-10

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMiwAFBVV95cUxNZWRRUzluaGY2SldjRmZEc3hoNWlCLXFfUW5KRlNSSVJrUU5HTWtKZ0VJQ2wwdmcyTmI4SENBS1NoU1hjaHBmaEd5bldjWHZwOXRkLVZycEMtTnFDNmJVcm1mcHNmbUE0amZBd3dXSXBrREVmemVrTm02b0ZJN3F1STZfS3BodEFMUzVBMzZ0QjFGNFpWWFh0aEpTOVlKc094Ny13Q3Bka1FjYWUwcVZYalFGQ2s1YzlncTZNZ3o0Zzg?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNZ005S3JHLXVpN3VIcklQdnJBWWhCZWhVVFE5WGF2MS1HMGRPVXljYkF3dG9mYXNSbjBVV1hIa2t1Q2RzSnBRWUNpODdjMDhlSmd5eDg3anVfWS0wV2ZzZ1NmUUpmZV9sVlpmVTAxc2l0bFdUT1dfT2laVTk4TkR6S3J3TWMxMkc2LTB0dGpRX3RvYUowQ3Vkc2U2cEVYRndUUUE?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTE1TX0dnVFNvcHhXQ3kxbHYtUFdxZ2hRQWMtbU5qek5jNWFGdEVCZE55WUg0aEZPN3RNeTJXUHotMlYxUE9tVFNMaDYxMnNHU3VnM0JjWW44UU94eG5TQXFNLUp6VXdudlA1ZlR6NHA0eHBYY3h1bjNYUF9XaWhDZw?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNdXVPN1FxVkpoWXdpeG9DdDJyNEl5aUlMWF8yZVM2aG1SNkdTbUFMNnQwQWFMMjhkNjJkOVdjb19IQTRtQzJBZ085alZEdjVpLTFMek9haGlValNDZzFTR3lfNnpmc1BPRk44N2RuWHR1dE03SWdTMXhHVGRSQm1ONkJpSkJVZmhvRzdLUEQwdUx4VHUzbnpN?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPY2I3VHRfaEF6T19qN28tZEVhN0piNERjTFpJRVlDMFdTLXJUZTlNdGJXblVLTVpEY0QzUVdvay1IazlCNTBmbGFWQ3NlNkIxRzBZSTIwSEJGUnJKTjl2YkZrUVdLVzB3T1V2WkRhRVAzcmVCVFJ6RjRfUEJveDZnWTlFYTBRZl9sMFlIUGZZaXlibmc?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxPVVlBamVBWGZsQi0wcmNOQnJiU1JFOTgxbnNtYlZaS2tYSkRRT3E3TDVmTVQ4SHQyaUZhZFQ3MlBmWV9tSnNTUWNLemFrNWtBRWFESWFNT3A3WWozbUhKN3VKRmVwZ3B2UkhSWXNiOUFQNnZfYVlEWmFzVkZLbTVOQ2RsZkQ1NDlwQl9BOGY2b0twUmFTaWpEeF91a3ltSm1JbDdrZHBIVFVWMDcwdzIyWXpBSU5zZ2I5ZkdGaEV4XzNuU09vRjBXNW9IV2o?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxPdHZ6QnVWUlEtOE5fb0dnOGRMbEttQ1FIM0dTdy1CZzloTk1Tc0RaNm40VTB1YjR1bmpnVmRFelE5RjlyeGJQQl9lY2s5SThnZ1d2QmRHbnM0cHVFTnZCcXh6QzRqZVN0TFoyOGVpSExjYm56czYydkdZLV9YX1RYYWdBY1hMRWlTQVhWR2MxQmp1clVoTW93b2J6NVdTZEdjdGZMc041NldwODR4?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNYlJiS2Q1OF9KcnZtZUxVdm85U3BMLXBnMmYyS2pOUVpaWllZUVZSamxOdTY2eXFUa1pWYkxYQXhLQTNXTmRQR21iejJ0NFdWblNZRDBiaHFRdlRPLXZET3JJNElCZHpGa0F5NEJxTHExLXlZeV9rZklfMUtndkRkandTQmNhdTdTVVh3R3Z5eVgwLWoyaGxQTA?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQOXlCU0M2TFhqbDZSTVZkN2UxaXY3NXNoSVhvUUtxV3o1TjJYOWNpWnFhMFV3T3JMbE1WeVE1VWsxSWJFdk00YkJrOS1ob0xSaEtMemdDZW4wdTRzQ1padkRTVVRVd1V5eTMxcnRIbnpFQWlQSmVDbFRFV0NLZEZXNVlUVXZMNFlwMS14eDVrMVhmNnNlYzVJRjh6dk5FZw?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxORk9oU1JVdGlRMFByRzFoVC1yU2d2TjlIMUVmdnVIRXY3am53NkdfaF9LNTloYWtSUUQyS0JvakxRU1lXNTBnbTkyR0I2OE9IUHJsbGFNRl8wX0RGdktPQjdvRlliek05TUVpa0JwTjNJSXpZUDdEY21FNDM4MHl6UWpzeTB1OWluSXpwZmpQVFVLRWZ3RmI4N2VLZDBwenc?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxNclhidVc5Z2VTNE9uZzRCcldGRDUzLXcyc1otalhRaExZNHR2cVRPNk03Z052ekExdUt1QzgxWGkya1NHcElYeWowOXRESHM1UFlsZUx3Yi14bUFHcHp3bVJuTlJPUDlzZFZjYV9URFR6b19NQVRtYUhMdFNobGIwWWFJb1JwODdWM1h6ZjQ4RS1obDRfNUkxdHdGUDdFR0JqbkhnX2ZzVUtRTml2Nmc?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxOX3lnNU1VVFk4T18zOEhrOVBOalRYV3BNSV9qZDhkQzZoZTdKSk4tU2lNMEd5eXc4NXlTckpIYmZvaHlfeXZ5MVI3amtRdDQyckdnTHNCWmQ5anB4YW1ZT3l6NDVNUGhnOFpQQ254SS1VUjhXckNPMzJfMFhyalh3VE8wMmZfeW4tSnZHdWN2UUVUN2J4RHEyNjBmc3pkT1BfUzlsY1lVN2ZWZ3FCdE9SZHlzU244SVBoQkpXcXBVbnNrckRt?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQOWxRYmU0Y2tka0Jhck5VN2psUVlscUZ2bmtZQVR2ZHZhc1VKZmVfQmdDemVTbTdnUHNzcS1pRGJuNlhQRVR1YnFVLVdhYi1JQUlVcHRTWFVZc29jUGZjUzRCNjNEcVRVMG43Q0xRQVZQSDJzTUZRam1wbU1ZTlNQLWhJazZrdkNDeTFwSEh5TFlEWVhMMmtMTWFGeUdhUQ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPVzMycFlnUjVmcWNZakVSRjJmMnJVTXQzMEFDdGJYMnlYRlAtSGhiZ0VwZ3ktcDd6QUlUWHNOaEVfOERsMXh0dWYtWGgtMS10Wld3SHV6R1RoOExRMEdrZkQ1czhwSkVDbXFMX1c5dGI5aUZuYzhPRkwtVVRZUUplZ2kyaVdES3hSanVrRUl4WGFqVm11aDV2Qmhn?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPdVhGMHJxSmRrQW5HSWdxS2sxOHRQd2R6Wmd3TldJOWhMbWt1QUp4MkZfM3NqTUxBR0xZNUNaQUVxRmxpVjRzeHVXRVpPTU0wd3MyN0Faa3J2RTIyTXlDVDhQZnQ3ejM1aDZ0UE0ycHBCd3NUNFdMZGpUaEc3UHZzOXkzaDhZQ3F4TnV5RE4xY3BqRm5jSVpMcERKcEpESnpMZllqTkdPdw?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOZmpMSExKY3duZF9LbGtCMVVNYzFUV2hILTR2MEh5eG41ZmtfT1FPUkJQTlpxdVpoeThnbzV6azdXVnppNWRmTzFBVnNud05ZOU5MY3ZHS1VLQk1uQy1SWUR1VEtoQlRjSEEwRG8ybUFUd3pPcjY3emEzUGNOZzZqUXczeThIamJWTHBvOG9qRFdpOGRzRHJtN0F0UHM?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOM3M1NHQyXzhFT0pEcnc0eWFPaTlKbURhQWRvZHZTU0ZNVzZla0ZrWmJXMXVBeldiY0tuc0c5cHNzVUFGMEtpNmxkem1nYlc4ZG85ZUpLU3dwR3V1TnpzeWVIY2MwTnFmOEVzNXhDLUtpaVU2czVPcWs5SGw0NjhKWHNiVnR5M2VSdFVWVmcxQ3ZnOHVjbFRxWUR3aXI?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxNNC1ndEJPQjN3V0RWSTJCaXlPWV94TUY1RzFjemY5S1R6c2FNYXdCTHFZc0ozdlFjellvbWxrMU9BaGFRZk83RVZLZXVZTHBTblYwamxab0h4X3drLV9YdEo0UXowa2g0bjFlMVhhUjRYSjRjUkZ1OHZOcEc2S1VYU3I1VEI4UldwUW9uT2dpcDhWWDNSQklDR3dSUHRUS1FrVEZTOTBMcXFaUjZVZmlhUkZ2Z3VkdzN5Nmkw?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNdlVNUlBPLXliejk5cW53UXNqT0FxZTBBUnQ1ZlhjS2dldDZGSjl2QUsyT3BGY2Q3OGRkUWw3VmV1TFgxVU05eGdJRXZRckQ0ZXU0di1nMGdoYzhJX3YzWGxVcGIxbm9FR0Z2bEpQenM4bkhsNkcydFVCLUtOeHVMd1htQ0ZuV185SVV4bTgzM2l5YjlONURuc0FyWHN2NFpyS2hSdDJyMm8yRE5TWGVZcg?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
