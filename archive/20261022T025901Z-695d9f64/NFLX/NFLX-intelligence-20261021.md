# NFLX Intelligence Report

- ticker: **NFLX**
- Report as_of: **2026-10-21**
- Market data as_of: **2026-10-21**
- Quant sources: https://finance.yahoo.com/quote/NFLX/history/, https://finance.yahoo.com/quote/NFLX/key-statistics/
- AI analysis snapshot as_of: **2026-10-21**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-22T04:18:14.696031+00:00**
- AI status: **N/A: AI unavailable: Groq application daily budget exhausted**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 17, 'ai': 0, 'unknown': 7})

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 65.0400 |
| Return 1D (%) | -5.3137 |
| Return 1W (%) | -7.8362 |
| Return 1M (%) | -11.3413 |
| Return YTD (%) | -30.6314 |
| Return 1Y (%) | -47.6054 |
| Annualized volatility (%) | 36.9541 |
| Beta vs SPY | N/A |
| Max drawdown (%) | -47.6054 |
| Sharpe (rf=0) | -1.5695 |
| P/E (trailing) | 18.80 |
| P/B | 9.18 |
| EV/EBITDA | 17.29 |
| Revenue growth (%) | 11.80 |
| MA50 | 74.6590 |
| Close vs MA50 (%) | -12.8839 |
| MA200 | 82.5174 |
| Close vs MA200 (%) | -21.1803 |
| RSI (14, Wilder) | 32.6116 |
| MACD (12,26) | -1.5134 |
| MACD signal (9) | -1.4542 |
| MACD histogram | -0.0593 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NFLX': 265}.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 65.0400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -5.3137 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -7.8362 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -11.3413 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -30.6314 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -47.6054 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 36.9541 -> Moderate annualized volatility.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -47.6054 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -1.5695 -> Negative risk-adjusted return.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 18.7977 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 32.6116 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.0593 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -12.8839 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -21.1803 -> Clearly below the moving-average trend level.

## TAILWINDS

### Netflix Beats Q3 Earnings Estimates But Braces Wall Street for 2026 Ad Sales Whiff
- Summary: Netflix Beats Q3 Earnings Estimates But Braces Wall Street for 2026 Ad Sales Whiff
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxQV2xrakJTS3dXNzdZd3JzWWpodUd4Z1A3SlVoalJkQWMzTUpOYU9yNXBFMm5IN3p3RHdBbk9QZWZxbVUxSnBXRXFzUlk2bFozTUtnVEtpT3RIQUU5c3RqamYzd0ZRcVFvMlZZTjhwT09fM0k2U0gzdmlDWVRuUlBiRm9KY0JLajBfYmVJV2p3R01fQk9aa1FYUVBVNjRBbVpYajVJM3VaX1RDZ040bkZ5b0tLSjhDY2YtV1RtZ3hpWXlwYjJW?oc=5>

## HEADWINDS

### Netflix stock sinks as Wall Street lowers price targets following Q4 revenue forecast miss
- Summary: Netflix stock sinks as Wall Street lowers price targets following Q4 revenue forecast miss
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7gFBVV95cUxQNEJkYUJaMXNVbEhiRTVINEhQZEptTkdWWFpkQkhDc2hDMkREQVRteGxITEZGVlYwcnZzSUdmd1ltclFkM2hBTnp2OGVWSVJEaWlub29QdHVMVC15eTRISWRPUGZLT3NaS2FiZHhwNGxtOExtUDBQUUpHejhDOFRmQ2pFQXhKRUNuN1JnM3RiR281VjlfT1ZvS1IxX2FWZ0tZQ3VjMTAzRERHQnowczhMNGJRUU1YeUFPdGNxVDNOWFFrZ0FOckdkNDdZNDFwaXhtaF81VXhJSzRLb1hVVW5JVks2Q09vVVViQ3dVN21n?oc=5>

### NFLX Stock Tumbles Overnight: Co-CEO Wants Netflix To Be Last Service Customers 'Ever Cancel', Says Live Events 'Drive New Membership'
- Summary: NFLX Stock Tumbles Overnight: Co-CEO Wants Netflix To Be Last Service Customers 'Ever Cancel', Says Live Events 'Drive New Membership'
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAJBVV95cUxPQnY4ektENzU5YW9wNHZrZDdlSXh6SS1jUFo0ZVNvNVJKWF9hTEY2MThtcmo4T0xDQ3JWN0hBSnZrZXRFUThnWjB4Q3hsMzhBMzlaN05zZDRUckNRVzV0T3MxS2gydFNUS3BLbWhqak85VFNKRU4wdVNxQjdqdE5FemJHb1ZfazZWWHNRb3paZnpnZ2hfZERqMlMxMGN1aWlDeDhobXB4SE52ZHBycWN5NXZaWnpDRmpGWVczN2R5UUlmQUhmVXhTbXFuTXdKSFNlMlc0YWV6MkxxVUM0anlHOEtCRklKUzVKSjhDb05CU2tROFlVZlk5ZTV1eTF0aS1GMGMtZGJtTEpvVi0ydEFRYTY0RlVUT2JuYnd2QQ?oc=5>

### Netflix stock sinks as revenue forecast falls short of estimates
- Summary: Netflix stock sinks as revenue forecast falls short of estimates
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxNbTQ0NzBnVm9FdEw4NEV5N19lemFsUTg0cFJRekVXb3RnbzdRTElIOGM1MjFZRDhtb3QwdnllRTRSdFlpS0dVTkVLdHRCLUMzSzJhS01USWFzR01ldE5YNGRQbDYwN29zMnkzUS1fTVhDUnVrMGN4c2FmUXBXSHNpODNtelpfZlFsSjdrSmIwaFZlcUdIcW1XM1dTWEN0RVlIeFNDQWxYdEJ5UlRhcVhQUGxRZk42U3IxLUFIakFmX1JlNXdXcGo0?oc=5>

### NFLX Stock Slips More Than 6% Premarket: Morningstar Sees 'Best Buying Opportunity' For Netflix Amid Negative Sentiment
- Summary: NFLX Stock Slips More Than 6% Premarket: Morningstar Sees 'Best Buying Opportunity' For Netflix Amid Negative Sentiment
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNYXVuTzRUeVNQZHhoTUpSZzg5aEE4VnhPYWh5YVQ4UmplQ1B4T1ktSDN5aHpMVFY2cm01QnRGS2FWWWxSMmlOTmYxS2kyaWVCZHdDZ0Q0NC1Bd1JGWG54cVdBdDktWnJKMEJZVldCOGRaUVhCQkdNYjBMTVNxakdjYjRyZFVSRUNrX3BrbERTUXJmdw?oc=5>

### Netflix (NASDAQ:NFLX) Stock Price Target Lowered at Guggenheim
- Summary: Netflix (NASDAQ:NFLX) Stock Price Target Lowered at Guggenheim
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxQVEtlRE5HTzFEOFlEdTZXOTVKejFTMTlBQWxxY3I2MzJnV1lBT0R3U0QxbGZ3cV9rXzdDeHA4aE1JQ20tcGs4Q3lZSlM3SXNlWUU3MENHR0tpbTdLWlhVclUyN1VqTzVRdi1zZDdSTjZxZEhkR0tKN01qcTE2RHBXZ1FsdUV6RVBFZUE3UHczTlgzZTJxTXVkakpqVFd1bVVzRmlYMTVNeDczTHRfYUNWTWViMXM2SlpJZ2FrNnJBbw?oc=5>

### Netflix has 2 problems behind the stock slide — and they aren't YouTube, co-CEO Ted Sarandos says
- Summary: Netflix has 2 problems behind the stock slide — and they aren't YouTube, co-CEO Ted Sarandos says
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7wFBVV95cUxOSmVJUnB4azRpbkpPRmxaNmVSRjlld0Y3TUpvcEx0Q3kydjNVTE13VEdaTHBCRGhQYWhVa1lTUlhFR3FUX1lJZ05QZUtDaUt2b2h4OTA1bHp2U0ZPQ2VYNHhEU1RqWkF6NUR6Q2FUOGZ2RTdmdE1GYnBBLUxkT0wzaXA5V2tidExCeC1Id1pwTVY2WjBKQUZnYzdUSkw5eDh6d2hkbExyVVEzeklrY3JDZW9vUjE2Uk11Q2JTX1pxTmsyNEtZWGpLVnoyeEc0d193QW53QkQzd0RFckRtWjJQcmhYSFNkeVA5OXdlSFhmMA?oc=5>

### Netflix Is Down 38% Since Completing Its 10-For-1 Stock Split. Here's Why the Sell-Off Is Worsening After Its Latest Earnings.
- Summary: Netflix Is Down 38% Since Completing Its 10-For-1 Stock Split. Here's Why the Sell-Off Is Worsening After Its Latest Earnings.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNQ1k4SFhQUlM5MnZqME9sbV84SGFydm1OMzEwOXdNbjlraXVVV3hKSXBOa1dSeVY4SnA2QlotbmVMeC1iTlVBZnd2Y1RnWkVubXhRemRRYWV5YnJVMTBOWU9YdENqYjlfU0pka1dhTVYyN1Via0pSTjIyeHdLZHh2ZGRpbVhqYnF0VUNYU1pOTlg4TmJkaU9uMGdZSkVRQQ?oc=5>

### NFLX Stock Heads For 26-Month Low After Needham Downgrade, Wall Street Price Target Cuts — YouTube Threat Grows, Content Problem ‘Seems Clear’
- Summary: NFLX Stock Heads For 26-Month Low After Needham Downgrade, Wall Street Price Target Cuts — YouTube Threat Grows, Content Problem ‘Seems Clear’
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOSTNsWGs5VllLU09RdWlFcGkySkh6UTRaTUVCRFplcm5GamFZQnFhVFhvQnJzU3JMQkRFT3NuVjJCNThrX0s5X0pYeW9TT1p4RWNpUGtja0hNYy1nUXhUZjlCYklKN3RjNzhpS3NtN2F2dVVOY0R2OXhLNXF0UUp2VkNrdVVxMVVQeHR1cFdnOEx5Q2dn?oc=5>

### Netflix Stock Drops Over 6% Following Expected Revenue Numbers
- Summary: Netflix Stock Drops Over 6% Following Expected Revenue Numbers
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxORFVyZ3JGNEJIdWMyYndUX1d5MTZwX1h2VmxmakJ0TEphU0RVLUt3RHJRMlBlQ1QtLU12eFV6eE5GN0JSdWRIWXJVNl9NX0JqVlJBVDZyZEN6akdUb1pReWk4TUpiWmNuakdkVVVmaUVCR0tFc3lfTC1uTmNTYUd5SzBUUVgtcVA4bHZrMkpjY2E3VG4tV3c?oc=5>

### Netflix Stock Sinks To 52-Week Low - Here's Why
- Summary: Netflix Stock Sinks To 52-Week Low - Here's Why
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxPOEdDM0lRcERUWnQ3Zi0xU192cXRTSUlfRnotLTRFSU1BTGZSa0R5bDQyUTBnaDRENkhpU2NtTmJ1LW9aZUVzWjVhYlNaU1FnMG0weDJFOTY0dWZKX3dBWnc5OGZlTmFURHhpZ09fcVBaMzRVbkVab1BEM1lZWjRGWGF4eWtvRUQxemwzdTNpaDBZMlJlcno4QVhPUElyWGtvYlV6Ny1EV3U?oc=5>

### Netflix (NASDAQ:NFLX) Stock Price Target Lowered at JPMorgan Chase & Co.
- Summary: Netflix (NASDAQ:NFLX) Stock Price Target Lowered at JPMorgan Chase & Co.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxOQjd4OUpISFIzdUZNUUVQY3JoZ2ZDcEdWZ3RGUS14SGNoVlBXdVNwcWJmc0taamtQXzR2Q3p1U1NhaWlsVzJmblNmTF80aWlHeXEyakNFRGZRXy11NDdTb243M2pVNDBSU0VhRDJZeExvQUZmVExJaU9KUlpzWXpycXpFWUN1M0dyOXJZb19xOVpDRzh6UmphTmRCSWJfZkRNTk1FUGUwclE1Mmh4UWRIY3p3UzhEMVZCYmhxaEFPR1BGMzBsMk1qcw?oc=5>

## CATALYSTS

### Netflix's profit rose 44% to $3.7 billion in Q3.
- Summary: Netflix's profit rose 44% to $3.7 billion in Q3.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNQXN6amJnWXBNeGZ6WmxaQW1jUVRNN2ZvTm5iX0ZvMEh1X2VFQ1pSTUJ2MHJwY2pFbHpkUnZyVlhtVVpSX1VqcDk5TmNGM1FyaEZkNWZZVV92WGZGV0d3YVp0MmtrOW5Ja2pBZGdnZm5YeFlwcUJ0UlVIREhHNVdJS015MDU1TnAwWjJKVWFWNEo0aFZudy0wMHk4aUNhSXc?oc=5>

### Netflix Q3 Earnings Are Today. Here’s What to Expect from NFLX Stock
- Summary: Netflix Q3 Earnings Are Today. Here’s What to Expect from NFLX Stock
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPSVlUODVLMUgtQngtWjBhMS1RdlNrQmtybk15RWJGbV96Y0tJWjNCQXRPUHdMVmhHajcwN1oxTHFVOE11TTE1c1FOQ2hKZXNiZmpkQ3ozWTVKS3NVVll2RXAxclhpWUh4YjYxeXB1RWRWQkh1b3kzYzBFemJuaWJXN3JBTkd1M0ZLcDBnaE4zTjBrWTZ3c1NUd2NmOXc?oc=5>

### Netflix Revenue Growth Slows as It Overhauls Programming Units
- Summary: Netflix Revenue Growth Slows as It Overhauls Programming Units
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxPWEliUElBYzE0WlcxV2VLNkZJSlFYcDJlZXBLeDZxOTZKNmlkMGRlQ003RWRjdE1YUVpZakxYaHZsY2YyVnAwYkhFSmhaUEZzWXJlalBHNFRSb2RhbUk3ZkhMRWJTNmZLaXhLX1NPRFk1Nks4TzNKNEpwUktvYWdKOE5Bb01QeUlVbGM0ZVhuTnNoNFBRd0RxdTd3Zjc4cVd4T1NrcXVaYlF4TWd2dnc?oc=5>

### NFLX Stock Flat Overnight: Netflix's ‘Largest Content Deal’ With Brazil Media Giant Globo Fails To Sway Retail Ahead Of Earnings
- Summary: NFLX Stock Flat Overnight: Netflix's ‘Largest Content Deal’ With Brazil Media Giant Globo Fails To Sway Retail Ahead Of Earnings
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxNd3JSQU1waGFseE0tTlZyUDd1eWpEbDJCbm9HajJ3bmxxT1poZkNCWlRrc3RmWnlaZDMtR2hwMlNuYzBacWQ2REtQNHc2SHF6d2NmQ21pUzBoVE9DTUhDWEV4dzJlYmRxX0I0NTZucGhhWlQ0U2t1NGZoSGpiVEs1akwzSGhzRHZ0WkMyUGtmMl84ZFlJSDZ0LWQ3UVJOdFM3?oc=5>

### Netflix Q3 earnings: Streamer is facing an 'attention scarcity' issue
- Summary: Netflix Q3 earnings: Streamer is facing an 'attention scarcity' issue
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxPQ2ZHMjlTcktrVGZtUmpXbFBvLTlFRm9hcjZzM3VjQnNKTUhFZzVRZjNhZE1DN2VTRktZaGIzMnlyTzUzRFkyZ1Q2aEh3ODNmc2Vqc1RPWVJfRmJudWtIU210bXl6NUVzTVJWZnJmZUtYZ0tvaUpHRWxmX0hBY2loRml5dnpSZWo0MEFiUV9NbmFhcF9xYVl2MFBRT3hqYk9CVFQySFNqbl92Yi0zNF9nVE5ZZw?oc=5>

## RISKS

N/A: AI unavailable: Groq application daily budget exhausted

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NFLX** | **18.80** | **9.18** | **17.29** | **11.80** | **270,822,637,568.00 USD** | **-47.61** |
| DIS | 23.01 | 1.76 | 11.48 | 6.80 | 193,095,401,472.00 USD | -0.74 |
| WBD | N/A | 2.36 | 13.79 | -11.20 | 77,595,885,568.00 USD | N/A |
| CMCSA | 7.12 | 0.87 | 4.73 | -1.20 | 78,353,899,520.00 USD | -17.18 |

Peers fetched as_of: 2026-10-21; NFLX reuses existing data (market data as_of: 2026-10-21); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-20
- Next expected earnings: 2027-01-19 (yfinance; expected dates may change)

## MACRO (FRED)

N/A: no FRED API key configured; skipped

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 12,874,176,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 3,663,927,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMixAFBVV95cUxQV2xrakJTS3dXNzdZd3JzWWpodUd4Z1A3SlVoalJkQWMzTUpOYU9yNXBFMm5IN3p3RHdBbk9QZWZxbVUxSnBXRXFzUlk2bFozTUtnVEtpT3RIQUU5c3RqamYzd0ZRcVFvMlZZTjhwT09fM0k2U0gzdmlDWVRuUlBiRm9KY0JLajBfYmVJV2p3R01fQk9aa1FYUVBVNjRBbVpYajVJM3VaX1RDZ040bkZ5b0tLSjhDY2YtV1RtZ3hpWXlwYjJW?oc=5
- https://news.google.com/rss/articles/CBMi7gFBVV95cUxQNEJkYUJaMXNVbEhiRTVINEhQZEptTkdWWFpkQkhDc2hDMkREQVRteGxITEZGVlYwcnZzSUdmd1ltclFkM2hBTnp2OGVWSVJEaWlub29QdHVMVC15eTRISWRPUGZLT3NaS2FiZHhwNGxtOExtUDBQUUpHejhDOFRmQ2pFQXhKRUNuN1JnM3RiR281VjlfT1ZvS1IxX2FWZ0tZQ3VjMTAzRERHQnowczhMNGJRUU1YeUFPdGNxVDNOWFFrZ0FOckdkNDdZNDFwaXhtaF81VXhJSzRLb1hVVW5JVks2Q09vVVViQ3dVN21n?oc=5
- https://news.google.com/rss/articles/CBMinAJBVV95cUxPQnY4ektENzU5YW9wNHZrZDdlSXh6SS1jUFo0ZVNvNVJKWF9hTEY2MThtcmo4T0xDQ3JWN0hBSnZrZXRFUThnWjB4Q3hsMzhBMzlaN05zZDRUckNRVzV0T3MxS2gydFNUS3BLbWhqak85VFNKRU4wdVNxQjdqdE5FemJHb1ZfazZWWHNRb3paZnpnZ2hfZERqMlMxMGN1aWlDeDhobXB4SE52ZHBycWN5NXZaWnpDRmpGWVczN2R5UUlmQUhmVXhTbXFuTXdKSFNlMlc0YWV6MkxxVUM0anlHOEtCRklKUzVKSjhDb05CU2tROFlVZlk5ZTV1eTF0aS1GMGMtZGJtTEpvVi0ydEFRYTY0RlVUT2JuYnd2QQ?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxNbTQ0NzBnVm9FdEw4NEV5N19lemFsUTg0cFJRekVXb3RnbzdRTElIOGM1MjFZRDhtb3QwdnllRTRSdFlpS0dVTkVLdHRCLUMzSzJhS01USWFzR01ldE5YNGRQbDYwN29zMnkzUS1fTVhDUnVrMGN4c2FmUXBXSHNpODNtelpfZlFsSjdrSmIwaFZlcUdIcW1XM1dTWEN0RVlIeFNDQWxYdEJ5UlRhcVhQUGxRZk42U3IxLUFIakFmX1JlNXdXcGo0?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNYXVuTzRUeVNQZHhoTUpSZzg5aEE4VnhPYWh5YVQ4UmplQ1B4T1ktSDN5aHpMVFY2cm01QnRGS2FWWWxSMmlOTmYxS2kyaWVCZHdDZ0Q0NC1Bd1JGWG54cVdBdDktWnJKMEJZVldCOGRaUVhCQkdNYjBMTVNxakdjYjRyZFVSRUNrX3BrbERTUXJmdw?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxQVEtlRE5HTzFEOFlEdTZXOTVKejFTMTlBQWxxY3I2MzJnV1lBT0R3U0QxbGZ3cV9rXzdDeHA4aE1JQ20tcGs4Q3lZSlM3SXNlWUU3MENHR0tpbTdLWlhVclUyN1VqTzVRdi1zZDdSTjZxZEhkR0tKN01qcTE2RHBXZ1FsdUV6RVBFZUE3UHczTlgzZTJxTXVkakpqVFd1bVVzRmlYMTVNeDczTHRfYUNWTWViMXM2SlpJZ2FrNnJBbw?oc=5
- https://news.google.com/rss/articles/CBMi7wFBVV95cUxOSmVJUnB4azRpbkpPRmxaNmVSRjlld0Y3TUpvcEx0Q3kydjNVTE13VEdaTHBCRGhQYWhVa1lTUlhFR3FUX1lJZ05QZUtDaUt2b2h4OTA1bHp2U0ZPQ2VYNHhEU1RqWkF6NUR6Q2FUOGZ2RTdmdE1GYnBBLUxkT0wzaXA5V2tidExCeC1Id1pwTVY2WjBKQUZnYzdUSkw5eDh6d2hkbExyVVEzeklrY3JDZW9vUjE2Uk11Q2JTX1pxTmsyNEtZWGpLVnoyeEc0d193QW53QkQzd0RFckRtWjJQcmhYSFNkeVA5OXdlSFhmMA?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxNQ1k4SFhQUlM5MnZqME9sbV84SGFydm1OMzEwOXdNbjlraXVVV3hKSXBOa1dSeVY4SnA2QlotbmVMeC1iTlVBZnd2Y1RnWkVubXhRemRRYWV5YnJVMTBOWU9YdENqYjlfU0pka1dhTVYyN1Via0pSTjIyeHdLZHh2ZGRpbVhqYnF0VUNYU1pOTlg4TmJkaU9uMGdZSkVRQQ?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOSTNsWGs5VllLU09RdWlFcGkySkh6UTRaTUVCRFplcm5GamFZQnFhVFhvQnJzU3JMQkRFT3NuVjJCNThrX0s5X0pYeW9TT1p4RWNpUGtja0hNYy1nUXhUZjlCYklKN3RjNzhpS3NtN2F2dVVOY0R2OXhLNXF0UUp2VkNrdVVxMVVQeHR1cFdnOEx5Q2dn?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxORFVyZ3JGNEJIdWMyYndUX1d5MTZwX1h2VmxmakJ0TEphU0RVLUt3RHJRMlBlQ1QtLU12eFV6eE5GN0JSdWRIWXJVNl9NX0JqVlJBVDZyZEN6akdUb1pReWk4TUpiWmNuakdkVVVmaUVCR0tFc3lfTC1uTmNTYUd5SzBUUVgtcVA4bHZrMkpjY2E3VG4tV3c?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxPOEdDM0lRcERUWnQ3Zi0xU192cXRTSUlfRnotLTRFSU1BTGZSa0R5bDQyUTBnaDRENkhpU2NtTmJ1LW9aZUVzWjVhYlNaU1FnMG0weDJFOTY0dWZKX3dBWnc5OGZlTmFURHhpZ09fcVBaMzRVbkVab1BEM1lZWjRGWGF4eWtvRUQxemwzdTNpaDBZMlJlcno4QVhPUElyWGtvYlV6Ny1EV3U?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxOQjd4OUpISFIzdUZNUUVQY3JoZ2ZDcEdWZ3RGUS14SGNoVlBXdVNwcWJmc0taamtQXzR2Q3p1U1NhaWlsVzJmblNmTF80aWlHeXEyakNFRGZRXy11NDdTb243M2pVNDBSU0VhRDJZeExvQUZmVExJaU9KUlpzWXpycXpFWUN1M0dyOXJZb19xOVpDRzh6UmphTmRCSWJfZkRNTk1FUGUwclE1Mmh4UWRIY3p3UzhEMVZCYmhxaEFPR1BGMzBsMk1qcw?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNQXN6amJnWXBNeGZ6WmxaQW1jUVRNN2ZvTm5iX0ZvMEh1X2VFQ1pSTUJ2MHJwY2pFbHpkUnZyVlhtVVpSX1VqcDk5TmNGM1FyaEZkNWZZVV92WGZGV0d3YVp0MmtrOW5Ja2pBZGdnZm5YeFlwcUJ0UlVIREhHNVdJS015MDU1TnAwWjJKVWFWNEo0aFZudy0wMHk4aUNhSXc?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPSVlUODVLMUgtQngtWjBhMS1RdlNrQmtybk15RWJGbV96Y0tJWjNCQXRPUHdMVmhHajcwN1oxTHFVOE11TTE1c1FOQ2hKZXNiZmpkQ3ozWTVKS3NVVll2RXAxclhpWUh4YjYxeXB1RWRWQkh1b3kzYzBFemJuaWJXN3JBTkd1M0ZLcDBnaE4zTjBrWTZ3c1NUd2NmOXc?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxPWEliUElBYzE0WlcxV2VLNkZJSlFYcDJlZXBLeDZxOTZKNmlkMGRlQ003RWRjdE1YUVpZakxYaHZsY2YyVnAwYkhFSmhaUEZzWXJlalBHNFRSb2RhbUk3ZkhMRWJTNmZLaXhLX1NPRFk1Nks4TzNKNEpwUktvYWdKOE5Bb01QeUlVbGM0ZVhuTnNoNFBRd0RxdTd3Zjc4cVd4T1NrcXVaYlF4TWd2dnc?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxNd3JSQU1waGFseE0tTlZyUDd1eWpEbDJCbm9HajJ3bmxxT1poZkNCWlRrc3RmWnlaZDMtR2hwMlNuYzBacWQ2REtQNHc2SHF6d2NmQ21pUzBoVE9DTUhDWEV4dzJlYmRxX0I0NTZucGhhWlQ0U2t1NGZoSGpiVEs1akwzSGhzRHZ0WkMyUGtmMl84ZFlJSDZ0LWQ3UVJOdFM3?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxPQ2ZHMjlTcktrVGZtUmpXbFBvLTlFRm9hcjZzM3VjQnNKTUhFZzVRZjNhZE1DN2VTRktZaGIzMnlyTzUzRFkyZ1Q2aEh3ODNmc2Vqc1RPWVJfRmJudWtIU210bXl6NUVzTVJWZnJmZUtYZ0tvaUpHRWxmX0hBY2loRml5dnpSZWo0MEFiUV9NbmFhcF9xYVl2MFBRT3hqYk9CVFQySFNqbl92Yi0zNF9nVE5ZZw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
