# JSOSIF v3 Regression Gold Labels
# Source: GPT-5.6 Sol analysis, 2026-10-05
# Chat: https://chatgpt.com/c/6ac447b2-9538-83e9-b2b1-4cdcf960128d
#
# These 8 were disagreements between v2 rules and historical AI.
# GPT adjudicated each. Use as regression fixtures for v3.

import json

GOLD_LABELS = [
    {
        "id": "v3-gold-01",
        "ticker": "NVDA",
        "headline": "Nvidia stock hits new all-time high, market cap at $5.7 trillion",
        "gold_category": "tailwinds",
        "confidence": "low",
        "note": "Ideally market_move/sentiment; price action is outcome not catalyst",
        "secondary": None,
    },
    {
        "id": "v3-gold-02",
        "ticker": "GOOGL",
        "headline": "GOOGL Stock Rises After Gemini 4 Argon Launch, But JPMorgan Says Google Must Rec",
        "gold_category": "catalysts",
        "confidence": "high",
        "note": "Product launch is primary catalyst; JPMorgan warning is secondary",
        "secondary": "risks",
    },
    {
        "id": "v3-gold-03",
        "ticker": "AMZN",
        "headline": "Amazon Stock Pops Up 1.8% as AWS Chief Pledges $1 Billion Fund to Ease AI",
        "gold_category": "catalysts",
        "confidence": "high",
        "note": "Discrete corporate event, not structural tailwind",
        "secondary": None,
    },
    {
        "id": "v3-gold-04",
        "ticker": "AMZN",
        "headline": "Amazon Signs 20 Year Nuclear Power Deal",
        "gold_category": "tailwinds",
        "confidence": "high",
        "note": "20-year agreement = structural development",
        "secondary": None,
    },
    {
        "id": "v3-gold-05",
        "ticker": "AMZN",
        "headline": "Synopsys Stock Rallies After AI Deals With OpenAI and Amazon",
        "gold_category": "SKIP",
        "confidence": "high",
        "note": "Subject is Synopsys, Amazon is counterparty. Entity relevance gate should filter.",
        "secondary": "SECONDARY_RELEVANCE",
    },
    {
        "id": "v3-gold-06",
        "ticker": "TSLA",
        "headline": "TSLA Stock Slips Overnight: Gary Black Says SpaceX Can't Afford Tesla",
        "gold_category": "risks",
        "confidence": "high",
        "note": "Analyst concern = uncertainty/risk, not observed structural headwind",
        "secondary": None,
    },
    {
        "id": "v3-gold-07",
        "ticker": "TSLA",
        "headline": "Tesla Doubles EU Registrations In May But BYD Still Leads",
        "gold_category": "headwinds",
        "confidence": "low",
        "note": "Mixed; competitive position matters more than absolute growth",
        "secondary": "tailwinds",
    },
    {
        "id": "v3-gold-08",
        "ticker": "TSLA",
        "headline": "TSLA Stock Rises Overnight: JPMorgan Says Tesla-SpaceX Merger Looks 'Coherent'",
        "gold_category": "risks",
        "confidence": "medium",
        "note": "Speculative M&A (analyst hypothetical), not confirmed transaction",
        "secondary": None,
    },
]

if __name__ == "__main__":
    print(json.dumps(GOLD_LABELS, ensure_ascii=False, indent=2))
