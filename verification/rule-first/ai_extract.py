#!/usr/bin/env python3
"""Fetch Google News RSS for the selected ticker, then Gemini (plain, no grounding) structured extraction."""
from email.utils import parsedate_to_datetime
import html
import json
import subprocess
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

CLI = "/home/hatch/workspace/skills/google-ai-studio/bin/gemini-call.py"


def fetch_rss(query, n=25):
    q = urllib.parse.quote(query)
    url = f"https://news.google.com/rss/search?q={q}&hl=en-US&gl=US&ceid=US:en"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        xml = r.read()
    root = ET.fromstring(xml)
    items = []
    for it in root.iter("item"):
        if len(items) >= n:
            break
        title = html.unescape(it.findtext("title") or "")
        if " - " in title:
            headline, source = title.rsplit(" - ", 1)
        else:
            headline, source = title, ""
        pub_date = it.findtext("pubDate") or ""
        try:
            if parsedate_to_datetime(pub_date).date().isoformat() > "2026-10-03":
                continue
        except (ValueError, TypeError):
            continue
        items.append({
            "headline": headline,
            "source": source,
            "link": it.findtext("link") or "",
            "pubDate": it.findtext("pubDate") or "",
        })
    return items


KEYS = ('tailwinds', 'headwinds', 'catalysts', 'risks')
MODEL = 'gemini-3.5-flash-lite'
ALIASES = {
    'NVDA': ('nvidia',), 'MSFT': ('microsoft',), 'AAPL': ('apple',),
    'GOOGL': ('alphabet', 'google'), 'AMZN': ('amazon', 'aws'), 'TSLA': ('tesla',),
}
EVENTS = {
    'earnings': r'earnings|revenue|profits?|quarterly results|deliveries|delivery numbers',
    'acquisition': r'acquisition|acquires?|merger|takeover|buyout',
    'guidance': r'guidance|outlook|forecast',
    'lawsuit': r'lawsuit|sues?|suing|antitrust|litigation|court|liability',
    'dividend': r'dividends?', 'buyback': r'buyback|repurchase',
    'product': r'launch|unveils?|release|iphone|robotaxi|fsd',
    'partnership': r'deal|partnership|signs|agreement|contract',
    'analyst': r'analyst|price target|upgrades?|downgrades?|conviction list|tactical ideas|top .*pick|fair value|valued',
    'workforce': r'layoffs?|job cuts',
    'stock_split': r'stock split',
    'market_move': r'stock|shares|premarket|market cap',
}
POSITIVE = r'jumps?|gains?|climbs?|pops?|higher|surges?|rall(?:y|ies)|record high|all.time high|upgrades?|wins?|green light|bullish|better.than.expected|buyback|repurchase|conviction list|top .*pick'
NEGATIVE = r'falls?|slips?|drops?|tumbling|lowers?|downgrades?|worst|pressure|threat|warnings?|doubts|lawsuit|antitrust|layoffs?|post.ipo low'


def metadata(item):
    try:
        date = parsedate_to_datetime(item.get('pubDate', '')).date().isoformat()
    except (ValueError, TypeError, OverflowError):
        date = ''
    return {'date': date, 'source': item.get('source', ''),
            'pubDate': item.get('pubDate', ''), 'url': item.get('link', ''),
            'sources': [item['link']] if item.get('link') else []}


def classify_rule(item, ticker):
    import re
    headline = item['headline']
    text = headline.lower()
    companies = [symbol for symbol, names in ALIASES.items()
                 if any(re.search(r'\b' + re.escape(name) + r'\b', text)
                        for name in (*names, symbol.lower()))]
    event = next((name for name, pattern in EVENTS.items()
                  if re.search(r'\b(?:' + pattern + r')\b', text)), 'unknown')
    pos = bool(re.search(r'\b(?:' + POSITIVE + r')\b', text))
    neg = bool(re.search(r'\b(?:' + NEGATIVE + r')\b', text))
    # Questions, conditional predictions and conflicting signals need interpretation.
    ambiguous = bool(re.search(r'\?|\b(?:could|may|might|prediction|predicts|will|expected to)\b', text))
    sentiment = ('positive' if pos else 'negative') if pos != neg and not ambiguous else 'unknown'
    if sentiment == 'unknown' and not ambiguous and not pos and not neg and event in ('dividend', 'acquisition', 'partnership', 'product'):
        sentiment = 'neutral'
    method = 'rule' if event != 'unknown' and sentiment != 'unknown' and ticker in companies and metadata(item)['date'] else 'unknown'
    category = 'tailwinds' if sentiment == 'positive' else 'headwinds' if sentiment == 'negative' else 'catalysts'
    if sentiment == 'negative' and event == 'lawsuit':
        category = 'risks'
    result = {'headline': headline, 'summary': headline, 'impact': 'medium',
              'horizon': 'short', 'confidence': 0.8 if method == 'rule' else 0.0,
              'companies': companies, 'event_type': event, 'sentiment': sentiment,
              'extraction_method': method, **metadata(item)}
    return category, result


def extract(items, ticker, call_ai=None):
    data = {'ticker': ticker, 'as_of': '2026-10-03', **{k: [] for k in KEYS}}
    pending = []
    seen = set()
    for item in items:
        if item['headline'] in seen:
            continue
        seen.add(item['headline'])
        category, result = classify_rule(item, ticker)
        if result['extraction_method'] == 'rule':
            data[category].append(result)
        else:
            pending.append(item)
    if pending and call_ai:
        try:
            extracted = call_ai(pending, ticker)
            if extracted.get('ticker') != ticker:
                raise ValueError('Gemini returned a different ticker')
            by_headline = {it['headline']: it for it in pending}
            staged = {k: [] for k in KEYS}
            used = set()
            for key in KEYS:
                if not isinstance(extracted.get(key), list):
                    raise ValueError('Invalid category')
                for result in extracted[key]:
                    headline = result['headline']
                    if headline not in by_headline or headline in used:
                        raise ValueError('Unknown or duplicate headline')
                    if not all(field in result for field in ('summary', 'impact', 'horizon', 'confidence', 'event_type', 'sentiment')):
                        raise ValueError('Incomplete Gemini item')
                    if result['impact'] not in ('high', 'medium', 'low') or result['horizon'] not in ('short', 'medium', 'long'):
                        raise ValueError('Invalid impact/horizon')
                    confidence = result['confidence']
                    if isinstance(confidence, bool) or not isinstance(confidence, (int, float)) or not 0 <= confidence <= 1:
                        raise ValueError('Invalid confidence')
                    if result['event_type'] not in (*EVENTS, 'unknown') or result['sentiment'] not in ('positive', 'negative', 'neutral', 'unknown'):
                        raise ValueError('Invalid event/sentiment')
                    base = classify_rule(by_headline[headline], ticker)[1]
                    base.update({field: result[field] for field in ('summary', 'impact', 'horizon', 'confidence', 'event_type', 'sentiment')})
                    base['extraction_method'] = 'ai'
                    staged[key].append(base)
                    used.add(headline)
            for key in KEYS:
                data[key].extend(staged[key])
            pending = [it for it in pending if it['headline'] not in used]
        except Exception as exc:
            data['error'] = f'AI unavailable: {exc}'
    # Preserve unresolved headlines for audit, without inventing report classifications.
    data['unclassified'] = [classify_rule(it, ticker)[1] for it in pending]
    data['extraction_stats'] = {
        'unique_headlines': len(seen),
        **{method: sum(it['extraction_method'] == method for k in (*KEYS, 'unclassified') for it in data[k])
           for method in ('rule', 'ai', 'unknown')},
    }
    return data


def call_gemini(items, ticker):
    import os
    import time
    from data_utils import ROOT, save, ticker_file
    prompt = (
        f'Classify relevant {ticker} news into tailwinds, headwinds, catalysts, risks. '
        'Return JSON with ticker and those four arrays. Skip irrelevant news. '
        'Each item: headline copied exactly, summary grounded only in headline, '
        'impact high/medium/low, horizon short/medium/long, confidence 0-1, '
        'event_type from ' + ', '.join(EVENTS) + ', or unknown; '
        'sentiment positive/negative/neutral/unknown. Do not infer facts absent from headlines. '
        'News: ' + json.dumps(items)
    )
    path = ROOT / ticker_file(ticker, 'ai-prompt.txt')
    path.write_text(prompt, encoding='utf-8')
    last_call = ROOT / '.last-ai-call'
    try:
        delay = max(0, 20 - (time.time() - float(last_call.read_text())))
    except (OSError, ValueError):
        delay = 0
    if delay:
        time.sleep(delay)
    last_call.write_text(str(time.time()))
    res = subprocess.run(
        [os.environ.get('GEMINI_CLI', CLI), '--model', MODEL,
         '--json-output', '--prompt', '@' + str(path)],
        capture_output=True, text=True, timeout=180,
    )
    if res.returncode:
        raise RuntimeError(f'Gemini exit {res.returncode}: {res.stderr.strip()[:500]}')
    envelope = json.loads(res.stdout)
    result = json.loads(envelope['text'])
    save(ticker_file(ticker, 'ai-envelope.json'), envelope)
    return result


def main():
    from data_utils import save, ticker_arg, ticker_file
    ticker = ticker_arg()
    items = []
    try:
        items = fetch_rss(f'{ticker} stock', 25)
        data = extract(items, ticker, call_gemini)
    except Exception as exc:
        data = extract(items, ticker)
        data['error'] = str(exc)
    save(ticker_file(ticker, 'rss-items.json'), items)
    save(ticker_file(ticker, 'ai-intel.json'), data)
    print('Extraction: ' + json.dumps(data['extraction_stats']), flush=True)


if __name__ == '__main__':
    main()
