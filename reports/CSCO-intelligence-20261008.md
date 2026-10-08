# CSCO Intelligence Demo

- ticker: **CSCO**
- Report as_of: **2026-10-08**
- Market data as_of: **2026-10-07**
- Quant sources: https://finance.yahoo.com/quote/CSCO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CSCO/key-statistics/
- AI analysis snapshot as_of: **2026-10-03** (retained; this run refreshes market data only)
- Snapshot note: the report-date daily bar may be intraday until the US market closes; its Close field is provisional. News, peers, earnings, EDGAR and macro sections reuse their existing snapshots.
- Market data fetched_at (UTC): **2026-10-08T04:10:39.246366+00:00**
- AI status: **Available**
- AI model: **gemini-3.5-flash-lite** (25 Google News RSS headlines -> AI extraction and classification; free-tier grounding unavailable, using RSS + AI)

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 117.3900 |
| Return 1D (%) | -0.4663 |
| Return 1W (%) | 9.4909 |
| Return 1M (%) | 7.9167 |
| Return YTD (%) | 55.2165 |
| Return 1Y (%) | 73.3052 |
| Annualized volatility (%) | 34.9248 |
| Beta vs SPY | 1.0631 |
| Max drawdown (%) | -17.8245 |
| Sharpe (rf=0) | 1.7569 |
| P/E (trailing) | 35.47 |
| P/B | 9.21 |
| EV/EBITDA | 25.76 |
| Revenue growth (%) | 17.60 |
| MA50 | 111.7754 |
| Close vs MA50 (%) | 5.0231 |
| MA200 | 97.5488 |
| Close vs MA200 (%) | 20.3398 |
| RSI (14, Wilder) | 66.7806 |
| MACD (12,26) | 0.9263 |
| MACD signal (9) | -0.4219 |
| MACD histogram | 1.3482 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CSCO': 255, 'SPY': 255}.

## TAILWINDS

### Cisco Systems (NASDAQ:CSCO) Stock Price Up 1% - Here's Why
- Summary: Cisco Systems (NASDAQ:CSCO) Stock Price Up 1% - Here's Why
- Date: 2026-10-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxORVczVmpoclNNRHg0aTZMYXZFR0JJUHQzOUQ3NDc1Q1Q0aXd5YUtpX1g5QTh0LURLVm5YMEl2Q0x0V1QtOGsyR3FpZmRsV2ZNNS1WME5oblFaRExhMVlZcThlcV9fd3FXa2JPY0dHUS1XbW1uQjdIX2N2ZlVLT3MyckF1YXBPNjM5a215RFRvTTJ0WkJqLWtoS09IeDVtY1lCMXBiQWZ1VXZadDRaZExCbC13?oc=5>

### Cisco Systems (CSCO) Stock Dips While Market Gains: Key Facts
- Summary: Cisco Systems (CSCO) Stock Dips While Market Gains: Key Facts
- Date: 2026-07-14 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNUnlZcjlNZTZoWHQ3QnRsTG81VHhyeDRxTzhvVWpDQ3hpcFJnbF9iU2trdlJaeW1hVEZvY1NjSUtGQno5V3hDeUo2WUlEcEMwSzlWWV9wV3VYZGRmUnZJVnJmZWF6eTlkOXlOc29IbnFxeXlSbzRHR2VWVmxWdy1XbDJhcy0wVHNOWEVYdjBUSl9naXQ5V1ZPTDJ3?oc=5>

### Cisco Systems (NASDAQ:CSCO) Shares Climb 3.2% - Time to Buy?
- Summary: Cisco Systems shares climbed 3.2%.
- Date: 2026-10-02 | Impact: medium | Horizon: short | Confidence: 1.0
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxQbFJ6T3BQV284elcxSVEyZ1BZQnRNVnlSVkZNc2RNeHdXYVlMMldPbGpPLXRaTEJoM0d0NTV2X2hPZzFUb0hXX2tJLUFNdTZQUzg1WHI1Z09ibHd3REY0ckpmbFk1Z1AzUUp3WVNJSFlqUkl4X0xoSzJMeTVyOE5FblY1NU5sMkVhZ2I1SkNjZEQ1ZEdDR256bDF3THQ1aEtuWm9OWWhWaVgybzUyelVHcTB0cw?oc=5>

### Cisco Systems Inc Stock (CSCO) Moved Up by 3.21% on Oct 2: What Signal Does It Send?
- Summary: Cisco Systems Inc stock moved up by 3.21% on Oct 2.
- Date: 2026-10-02 | Impact: medium | Horizon: short | Confidence: 1.0
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNTldKZUI3NlRyWERZenNLalZxM296Z2gxMm1iR284X2NKTTBiLWdVZ29nWTV2dEdxOTgxSHc3YS1QVmlCRW8xbjdzNlFMTTRwUEgtOEtxLTVBYkRwYkVsVHM4MUsydWZlLUFCWHRJX24ySEdmdEt6OWswa1Y5TTg0b1B5cnEwaDhIdGlN?oc=5>

### Cisco Systems (NASDAQ:CSCO) Stock Lifted to "Strong-Buy" by Zacks Research
- Summary: Zacks Research lifted Cisco Systems stock to Strong-Buy.
- Date: 2026-10-02 | Impact: high | Horizon: medium | Confidence: 1.0
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxQNWdxbjEza2hzaWRfdjRUdXZIdDFBTF9DZWJoUnByTzJNYUFWUW56V3JMMWZ4aXZBOHEwcTcwQ3kwLVpqbHM5TUVSMXJaTmRnM2lwU1U2VThicmZYVHVZTXdscEVUOHFmRnlGR2ZsQ0lvblRCbHZVWDUyRmJsbjd5VUN4cXcyWU1RdGtkX3BYWUVHcnVfcTNSRTJsQjdNdFppQi1oVkVBd19uN3ZaNVBtT2JuMXRNcGdVdjFaYnZwWmltSUlBdmZZa3lVd2E?oc=5>

## HEADWINDS

### Why Cisco (CSCO) Stock Is Down Today
- Summary: Why Cisco (CSCO) Stock Is Down Today
- Date: 2026-08-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQMFFjemo5UF9NcVlfazJ5ZzlGSTNhV2hDRWZQYVNTNFA3U2ZnUFhZWWVLWlhLenZGUXhWSEstZW10ZEI1QXgxY0pFRWdxdzEweUR6VHpDdW9wYUNmT0dfZXctR1VWT09ieDdYYmwySHhuX1dRSm9NWTNDVXhxbU5WV0FaT1FqQUtiakFtLWQxMHRTaFBQ?oc=5>

### Cisco Systems Falls 3.9% as Recent Insider Selling and Profit-Taking Weigh on Shares
- Summary: Cisco Systems Falls 3.9% as Recent Insider Selling and Profit-Taking Weigh on Shares
- Date: 2026-09-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxQSll0cTlhbk9uV0dCZ3hKdFhUVXpoRDI1R0V0TkNUR1pQZFV4RU94SVp5N0J2SFRmY1FWYzc3Mjd0eFl2a28tNURMNUNiX0NVemNPREczd1BWcmlid2NQZTUtQjZpZ1IwUGFhRDVoWFlVMFRTVllqVWU2TV9YYjVHQ3NTZmwwUnpZX2ZadlVRc1ZYUk92cHpJbTVsT3B2TEppVFNTUTQ2QllNc1QwZ0NId3pBOUNjVkh0SWI0?oc=5>

### Cisco Systems Inc Stock (CSCO) Moved Down by 3.32% on Sep 22: Facts Behind the Movement
- Summary: Cisco Systems Inc Stock (CSCO) Moved Down by 3.32% on Sep 22: Facts Behind the Movement
- Date: 2026-09-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxPWHlDRG1UREhHX04wb0R6ajh4Y2RRNUFTazdFNjdSYVNGdXRmb01aMTFRSlJqaVI3SndQZkk1YndYV29DRksxYTNfVEN1Wmp1SGhUMm5kcHcwa3FpekRycGJZcUtjZnlaNFJnTmRJVlFPTEozMi14OXk5YmhkUGxTVFI4MnRpOGN6RUZ3?oc=5>

### Cisco Systems (NASDAQ:CSCO) Downgraded by Wall Street Zen to "Hold"
- Summary: Cisco Systems (NASDAQ:CSCO) Downgraded by Wall Street Zen to "Hold"
- Date: 2026-10-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxOTzc2TVEwcWM4SlNqSkRKZFNHeGN1dUpEQmZOdG12OE1oaUxrajhxTFVLd29LUTdYeHo4d0tFeGVBZlZpQVZ2eFNGRmtmVi1UUU5tMGZPSG1reHFPRmVsd0FXWlhFTko3MFg4REc3OXk4LTIySVNRYk5PdUMweXRDOERMdzhKdkFaTVFQdFVXYWtJREV1a05xRzl3TkpQQVUwRGpiU0N6Tm1ENDdZbEdEVjBmSTc4R1c1WUQzOThBOG1oeE0?oc=5>

### Cisco Drops 10% Post Q4 Earnings: Buy, Sell or Hold the Stock?
- Summary: Cisco drops 10% post Q4 earnings.
- Date: 2026-08-19 | Impact: high | Horizon: short | Confidence: 1.0
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxNWDgtc19aaVZscm0xaDJadTE0cFFBYVo3VnVWUXdhcExJV0RkS1Vqb3FEUUU3UkpZZW96N2tXNkRxTUdnZDQzX2J6N0Z6OE1oZXIyWHVHeW9kUVFabE1GSmYzNjRtMGRvSTNtS0FaclI1SXNNbzl3RXVkem42bkZ3Zmw5QmhJRE83a0F3TzRZb0k?oc=5>

## CATALYSTS

### Cisco stock sinks 5% after Piper Sandler cuts price target on growth concerns
- Summary: Cisco stock sinks 5% after Piper Sandler cuts price target on growth concerns
- Date: 2026-09-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigAFBVV95cUxQNzdLX0Z1bHBINVp0ejU0bGlZc2tuemRSWjhyOTdXbW1idFNndDVNOFdwRk1LdEpHRGZtYmNSd01UUmlJLThtbEZaVElSb3N6QlFnRDdyUEttanlrOGY2NXIxLVVUYXlBMUhYeW1nbVBjMkFYMTFfdGFDdW1WakxPb9IBhgFBVV95cUxNcGxZWEtwQ216d08wX3IyRThWQzRpbUxtYWNGd3BmOVcyQkx0T3E4ZGJjZ1pLeFJpTERfSE0xaEFhaVFpMThENnVWLUdSMUJSY3NWQ2xIZmlpc3AxZnBkSjNaVnJHRTJDR1lpemhzMFdEazhleXRhV0xRMHFxbDcyRGZCMUhzdw?oc=5>

### Cisco Stock Falls as Piper Sandler Cuts Price Target - Cisco Systems (NASDAQ:CSCO)
- Summary: Cisco Stock Falls as Piper Sandler Cuts Price Target - Cisco Systems (NASDAQ:CSCO)
- Date: 2026-09-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxPNU5hT2JabE12Y2pvWXYtd1RLMG5rbjRYX1pXYlJLOWpGTlkta3JyUDktRVJ4NWhZTk9YeDc3NTAzb0lxenFBQ1VLM2h4LS1xbHpGX1BqSnoxQmpzZWFreW11RFFhbXNKM2FGb2tvRWZPbUx5NjVYejZrd1EycXdzam1kZWtBb3IwUmpNWHhieUxXbk13M3ZabU5XMGNhb0FEcE4ta3FtNDNQazE0SVRiYzdDaw?oc=5>

### Cisco (CSCO) Stock Looks Fairly Valued After Strong AI News
- Summary: Cisco (CSCO) Stock Looks Fairly Valued After Strong AI News
- Date: 2026-08-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNWHFseTN1V2FUdkVZZ3JnZlZJdjdkQUxmRVppMG04LTU2WGZyVzVXY2ROTGREOXBzaHV5ajNUM1hKc2JzcHdKM3FSLWpsMXdZZ2dHa2lyTDdVMGRWMGpLYUpPR2ZKTXFPR296M0VEX1ZzSi0tcG5jZlQtTmFNdVg1RHJVeEMxQmhROUJOQm9lTGxwdDNXTWhkaERn?oc=5>

### Cisco Systems, Inc. $CSCO Stock Purchased by CX Institutional
- Summary: Cisco Systems, Inc. $CSCO Stock Purchased by CX Institutional
- Date: 2026-10-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxPVVB1SDFmTzlETkwyUmlGbU9iVFhjYzdEdHVwRGpaX3FnLTF0TUlQem9ieEttWlJYN0tKVzFkRW9qbDRfYXJYQ2oybVBLZi1yeHpkNzMxanhOQWJ0UFhDa0RmVnFOYVk3RWRZbnBsZ1N1MW9CX2dTQVh4YjlyMEotWlc5MXJHYVN3Z1VsVnRfb29QMnJWeVBKZndmSzdpTzhBV19KZFlSd1RCY1FxVUxlajRUZ1RQNGNuR1hv?oc=5>

### Cisco (CSCO) Stock Fair Value Edges Higher After AI Networking Order Strength
- Summary: Cisco (CSCO) Stock Fair Value Edges Higher After AI Networking Order Strength
- Date: 2026-07-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOc3d3LS1yYXVOV1hSd3hIaWNNcndpRXBSUk1LYUxDbFQ2eVMxanY4cDBWQ25ac204WWhUOVJiX05UWDNWQ1J1WTRncnd1OGlBYjBqZVVvUDhCUi1kZ2tWMncyaTVleHVoZkE5Y19TVEc1Ym5zeGZ0LUpHYVZxMWZnMHNnak13SmIwZ3ZZZmFmUkJXZl9NUktj?oc=5>

### Cisco Systems, Inc. $CSCO Stock Bought by Versant Capital Management Inc
- Summary: Cisco Systems, Inc. $CSCO Stock Bought by Versant Capital Management Inc
- Date: 2026-10-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxOY1Y1T1ZoMEo2WGNMRXJ3N2FaSmRDMDRPaXE3UWFJVDVXcUNqcXV2UTRyR196QkEyUzJIU29UeWJiOTE1VExMWVNCNVFjdVlEalREVm9qcXRoQlI4SVlWV2NucjJtRm1VSW1tZUppOF8zZTIxQnBpUTFfdmtIa1E5b2dnTEZRQzVQUGp2bmtmQmZPdFFTT1JFQTloMVBHUEJMZk9JelJpZVdseWEtQ21aQ1E5RWk0X3kxQWZacE43X1pRUGVZcG04Y3d3?oc=5>

### Here’s How Much Traders Expect Cisco Stock to Move After Earnings
- Summary: Here’s How Much Traders Expect Cisco Stock to Move After Earnings
- Date: 2026-08-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxNLS15cDdfVTEwdm9kLWNzT0FFd0FnekREczdQNkR2eHdHTUlBNVBFYVJIc0s2WWVMOV9LUC1RNUVFbVdBdFB6clUxYXo4SVJ6bTlQZEd1enZ3aHlkSk81Z1NleTZZS0JJaHZLdWxQV3hodHF4R3NuT3FsN2g3bkdGSG9KcUFWSlZFdFI1QWNLSDZKRTVpNWJOYlJyYXJxV1ZoZUZiT2Iwd2RhcnBPNWxUbkZPOURxak92YlVJ?oc=5>

### Cisco (CSCO) Stock Looks About Right As Security Deal Talk Grows
- Summary: Cisco (CSCO) Stock Looks About Right As Security Deal Talk Grows
- Date: 2026-07-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPNk9oOTNWQ0dVMm9FUGFmVGRvOUY4UHBNMDdJTkdXcEp4RHlhUzRER3BhcXMxSC1Lc1JWdlJCMWd5UWdkb2JVMkppVjItYnRIV0JIcktxN3YzX09SVl9FcUpMUXVVYm81Vk9qVXZIS29WcFhSWXdGRUFrWXVSR3hhaTBYVi1WUG9SRmhzMkJmaVlPNDB2c1dHcWowajA?oc=5>

### Is Sovereign AI Partnership Altering The Investment Case For Cisco (CSCO)?
- Summary: Sovereign AI partnership is altering the investment case for Cisco.
- Date: 2026-10-03 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxNNEc4MWpxbTllNHRETlNfTk82R05venplU3RiSXhDV2swSlZIS0lvdXJCUHNjYWtmOWxjNjB6OGFyMGJJeWRHUWI3X1NwMm9CU3o1V25yN0VsWTBXbTVIa2tHNTBIWDF3UG13WEZIVGZvbHd1VFUtZHZCbVdxdjBiOVRjdm5zMjhoc0ZEZEwtRE9nUVhWTloyS3EwbWhMQnVKekROT2VVRDlxNU9aUmdTcUEtaHFYMEFjNFRhbjRuTEhSazVGVjJN0gHMAUFVX3lxTE5DcjUxQW80OVlucXhmb0hyYU5YU1lpVFNsQlRYVHdzWFpzdEFqTy1zS3l0aTYwM0M3RTVPMVpPY0x0NUNXbTRpZWVEWFJlcWtxSVl4WG1kTTJEMy1USGdCX09Db3I3aGVWb2xqQVlfMVg4NUtVcHJCNzdobVd1V2NJQ2J6Y0NBb2IwM3pJNUVxWS1EX01kdTA0eGtPLWJrMUVBN3VMLXNyeWZndEhxTkl0VWNqenBQUE1EYk9YOVRfTEc0M1Jub2JKc011eA?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (USD) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CSCO** | **35.47** | **9.21** | **25.76** | **17.60** | **462,820,278,272.00** | **73.31** |

Peers fetched as_of: 2026-10-08; CSCO reuses existing data (market data as_of: 2026-10-07); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-12
- Next expected earnings: 2026-11-12 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-03

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment Rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index | CPIAUCSL | 334.13 | 2026-08-01 |
| Federal Funds Effective Rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-09-02
- Revenue (latest available single quarter): 12,844,000,000.00 USD; period 2018-04-29/2018-07-28; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 3,373,000,000.00 USD; period 2026-01-25/2026-04-25; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/858877/000085887726000132/csco-20260725.htm

SEC requests use the demo placeholder contact email contact@example.com. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMisgFBVV95cUxORVczVmpoclNNRHg0aTZMYXZFR0JJUHQzOUQ3NDc1Q1Q0aXd5YUtpX1g5QTh0LURLVm5YMEl2Q0x0V1QtOGsyR3FpZmRsV2ZNNS1WME5oblFaRExhMVlZcThlcV9fd3FXa2JPY0dHUS1XbW1uQjdIX2N2ZlVLT3MyckF1YXBPNjM5a215RFRvTTJ0WkJqLWtoS09IeDVtY1lCMXBiQWZ1VXZadDRaZExCbC13?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNUnlZcjlNZTZoWHQ3QnRsTG81VHhyeDRxTzhvVWpDQ3hpcFJnbF9iU2trdlJaeW1hVEZvY1NjSUtGQno5V3hDeUo2WUlEcEMwSzlWWV9wV3VYZGRmUnZJVnJmZWF6eTlkOXlOc29IbnFxeXlSbzRHR2VWVmxWdy1XbDJhcy0wVHNOWEVYdjBUSl9naXQ5V1ZPTDJ3?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxQbFJ6T3BQV284elcxSVEyZ1BZQnRNVnlSVkZNc2RNeHdXYVlMMldPbGpPLXRaTEJoM0d0NTV2X2hPZzFUb0hXX2tJLUFNdTZQUzg1WHI1Z09ibHd3REY0ckpmbFk1Z1AzUUp3WVNJSFlqUkl4X0xoSzJMeTVyOE5FblY1NU5sMkVhZ2I1SkNjZEQ1ZEdDR256bDF3THQ1aEtuWm9OWWhWaVgybzUyelVHcTB0cw?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNTldKZUI3NlRyWERZenNLalZxM296Z2gxMm1iR284X2NKTTBiLWdVZ29nWTV2dEdxOTgxSHc3YS1QVmlCRW8xbjdzNlFMTTRwUEgtOEtxLTVBYkRwYkVsVHM4MUsydWZlLUFCWHRJX24ySEdmdEt6OWswa1Y5TTg0b1B5cnEwaDhIdGlN?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxQNWdxbjEza2hzaWRfdjRUdXZIdDFBTF9DZWJoUnByTzJNYUFWUW56V3JMMWZ4aXZBOHEwcTcwQ3kwLVpqbHM5TUVSMXJaTmRnM2lwU1U2VThicmZYVHVZTXdscEVUOHFmRnlGR2ZsQ0lvblRCbHZVWDUyRmJsbjd5VUN4cXcyWU1RdGtkX3BYWUVHcnVfcTNSRTJsQjdNdFppQi1oVkVBd19uN3ZaNVBtT2JuMXRNcGdVdjFaYnZwWmltSUlBdmZZa3lVd2E?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQMFFjemo5UF9NcVlfazJ5ZzlGSTNhV2hDRWZQYVNTNFA3U2ZnUFhZWWVLWlhLenZGUXhWSEstZW10ZEI1QXgxY0pFRWdxdzEweUR6VHpDdW9wYUNmT0dfZXctR1VWT09ieDdYYmwySHhuX1dRSm9NWTNDVXhxbU5WV0FaT1FqQUtiakFtLWQxMHRTaFBQ?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxQSll0cTlhbk9uV0dCZ3hKdFhUVXpoRDI1R0V0TkNUR1pQZFV4RU94SVp5N0J2SFRmY1FWYzc3Mjd0eFl2a28tNURMNUNiX0NVemNPREczd1BWcmlid2NQZTUtQjZpZ1IwUGFhRDVoWFlVMFRTVllqVWU2TV9YYjVHQ3NTZmwwUnpZX2ZadlVRc1ZYUk92cHpJbTVsT3B2TEppVFNTUTQ2QllNc1QwZ0NId3pBOUNjVkh0SWI0?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxPWHlDRG1UREhHX04wb0R6ajh4Y2RRNUFTazdFNjdSYVNGdXRmb01aMTFRSlJqaVI3SndQZkk1YndYV29DRksxYTNfVEN1Wmp1SGhUMm5kcHcwa3FpekRycGJZcUtjZnlaNFJnTmRJVlFPTEozMi14OXk5YmhkUGxTVFI4MnRpOGN6RUZ3?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxOTzc2TVEwcWM4SlNqSkRKZFNHeGN1dUpEQmZOdG12OE1oaUxrajhxTFVLd29LUTdYeHo4d0tFeGVBZlZpQVZ2eFNGRmtmVi1UUU5tMGZPSG1reHFPRmVsd0FXWlhFTko3MFg4REc3OXk4LTIySVNRYk5PdUMweXRDOERMdzhKdkFaTVFQdFVXYWtJREV1a05xRzl3TkpQQVUwRGpiU0N6Tm1ENDdZbEdEVjBmSTc4R1c1WUQzOThBOG1oeE0?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxNWDgtc19aaVZscm0xaDJadTE0cFFBYVo3VnVWUXdhcExJV0RkS1Vqb3FEUUU3UkpZZW96N2tXNkRxTUdnZDQzX2J6N0Z6OE1oZXIyWHVHeW9kUVFabE1GSmYzNjRtMGRvSTNtS0FaclI1SXNNbzl3RXVkem42bkZ3Zmw5QmhJRE83a0F3TzRZb0k?oc=5
- https://news.google.com/rss/articles/CBMigAFBVV95cUxQNzdLX0Z1bHBINVp0ejU0bGlZc2tuemRSWjhyOTdXbW1idFNndDVNOFdwRk1LdEpHRGZtYmNSd01UUmlJLThtbEZaVElSb3N6QlFnRDdyUEttanlrOGY2NXIxLVVUYXlBMUhYeW1nbVBjMkFYMTFfdGFDdW1WakxPb9IBhgFBVV95cUxNcGxZWEtwQ216d08wX3IyRThWQzRpbUxtYWNGd3BmOVcyQkx0T3E4ZGJjZ1pLeFJpTERfSE0xaEFhaVFpMThENnVWLUdSMUJSY3NWQ2xIZmlpc3AxZnBkSjNaVnJHRTJDR1lpemhzMFdEazhleXRhV0xRMHFxbDcyRGZCMUhzdw?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxPNU5hT2JabE12Y2pvWXYtd1RLMG5rbjRYX1pXYlJLOWpGTlkta3JyUDktRVJ4NWhZTk9YeDc3NTAzb0lxenFBQ1VLM2h4LS1xbHpGX1BqSnoxQmpzZWFreW11RFFhbXNKM2FGb2tvRWZPbUx5NjVYejZrd1EycXdzam1kZWtBb3IwUmpNWHhieUxXbk13M3ZabU5XMGNhb0FEcE4ta3FtNDNQazE0SVRiYzdDaw?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNWHFseTN1V2FUdkVZZ3JnZlZJdjdkQUxmRVppMG04LTU2WGZyVzVXY2ROTGREOXBzaHV5ajNUM1hKc2JzcHdKM3FSLWpsMXdZZ2dHa2lyTDdVMGRWMGpLYUpPR2ZKTXFPR296M0VEX1ZzSi0tcG5jZlQtTmFNdVg1RHJVeEMxQmhROUJOQm9lTGxwdDNXTWhkaERn?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxPVVB1SDFmTzlETkwyUmlGbU9iVFhjYzdEdHVwRGpaX3FnLTF0TUlQem9ieEttWlJYN0tKVzFkRW9qbDRfYXJYQ2oybVBLZi1yeHpkNzMxanhOQWJ0UFhDa0RmVnFOYVk3RWRZbnBsZ1N1MW9CX2dTQVh4YjlyMEotWlc5MXJHYVN3Z1VsVnRfb29QMnJWeVBKZndmSzdpTzhBV19KZFlSd1RCY1FxVUxlajRUZ1RQNGNuR1hv?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOc3d3LS1yYXVOV1hSd3hIaWNNcndpRXBSUk1LYUxDbFQ2eVMxanY4cDBWQ25ac204WWhUOVJiX05UWDNWQ1J1WTRncnd1OGlBYjBqZVVvUDhCUi1kZ2tWMncyaTVleHVoZkE5Y19TVEc1Ym5zeGZ0LUpHYVZxMWZnMHNnak13SmIwZ3ZZZmFmUkJXZl9NUktj?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxOY1Y1T1ZoMEo2WGNMRXJ3N2FaSmRDMDRPaXE3UWFJVDVXcUNqcXV2UTRyR196QkEyUzJIU29UeWJiOTE1VExMWVNCNVFjdVlEalREVm9qcXRoQlI4SVlWV2NucjJtRm1VSW1tZUppOF8zZTIxQnBpUTFfdmtIa1E5b2dnTEZRQzVQUGp2bmtmQmZPdFFTT1JFQTloMVBHUEJMZk9JelJpZVdseWEtQ21aQ1E5RWk0X3kxQWZacE43X1pRUGVZcG04Y3d3?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxNLS15cDdfVTEwdm9kLWNzT0FFd0FnekREczdQNkR2eHdHTUlBNVBFYVJIc0s2WWVMOV9LUC1RNUVFbVdBdFB6clUxYXo4SVJ6bTlQZEd1enZ3aHlkSk81Z1NleTZZS0JJaHZLdWxQV3hodHF4R3NuT3FsN2g3bkdGSG9KcUFWSlZFdFI1QWNLSDZKRTVpNWJOYlJyYXJxV1ZoZUZiT2Iwd2RhcnBPNWxUbkZPOURxak92YlVJ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPNk9oOTNWQ0dVMm9FUGFmVGRvOUY4UHBNMDdJTkdXcEp4RHlhUzRER3BhcXMxSC1Lc1JWdlJCMWd5UWdkb2JVMkppVjItYnRIV0JIcktxN3YzX09SVl9FcUpMUXVVYm81Vk9qVXZIS29WcFhSWXdGRUFrWXVSR3hhaTBYVi1WUG9SRmhzMkJmaVlPNDB2c1dHcWowajA?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxNNEc4MWpxbTllNHRETlNfTk82R05venplU3RiSXhDV2swSlZIS0lvdXJCUHNjYWtmOWxjNjB6OGFyMGJJeWRHUWI3X1NwMm9CU3o1V25yN0VsWTBXbTVIa2tHNTBIWDF3UG13WEZIVGZvbHd1VFUtZHZCbVdxdjBiOVRjdm5zMjhoc0ZEZEwtRE9nUVhWTloyS3EwbWhMQnVKekROT2VVRDlxNU9aUmdTcUEtaHFYMEFjNFRhbjRuTEhSazVGVjJN0gHMAUFVX3lxTE5DcjUxQW80OVlucXhmb0hyYU5YU1lpVFNsQlRYVHdzWFpzdEFqTy1zS3l0aTYwM0M3RTVPMVpPY0x0NUNXbTRpZWVEWFJlcWtxSVl4WG1kTTJEMy1USGdCX09Db3I3aGVWb2xqQVlfMVg4NUtVcHJCNzdobVd1V2NJQ2J6Y0NBb2IwM3pJNUVxWS1EX01kdTA0eGtPLWJrMUVBN3VMLXNyeWZndEhxTkl0VWNqenBQUE1EYk9YOVRfTEc0M1Jub2JKc011eA?oc=5

## Demo notes and limitations

- Multi-ticker local demo; AI items require human spot checks; RSS coverage is not guaranteed.
- Free-tier Gemini grounding (google_search tool) returned 429; the demo uses Google News RSS + plain-text AI extraction.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
