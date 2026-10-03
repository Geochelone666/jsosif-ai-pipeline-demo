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


def main():
    import os
    import time
    from data_utils import ROOT, save, ticker_arg, ticker_file
    ticker = ticker_arg()
    keys = ('tailwinds', 'headwinds', 'catalysts', 'risks')
    data = {'ticker': ticker, 'as_of': '2026-10-03', **{k: [] for k in keys}}
    items = []
    try:
        items = fetch_rss(f"{ticker} stock", 25)
        save(ticker_file(ticker, 'rss-items.json'), items)
        prompt = (
            f"Analyze these {ticker} news headlines for a student investment fund. "
            "Output only valid JSON in English. Do not invent facts or dates; skip duplicates and irrelevant items. "
            "Classify into tailwinds, headwinds, catalysts, risks. Each item must have headline (copied exactly), "
            "summary (1-2 sentences), date (YYYY-MM-DD from pubDate), impact (high/medium/low), "
            "horizon (short/medium/long), confidence (0-1). Schema: "
            + json.dumps(data) + " Headlines: " + json.dumps(items)
        )
        prompt_path = ROOT / ticker_file(ticker, 'ai-prompt.txt')
        prompt_path.write_text(prompt, encoding='utf-8')
        last_call = ROOT / '.last-ai-call'
        for attempt in range(2):
            delay = max(0, 20 - (time.time() - float(last_call.read_text()))) if last_call.exists() else 0
            if delay:
                time.sleep(delay)
            last_call.write_text(str(time.time()))
            res = subprocess.run(
                [os.environ.get('GEMINI_CLI', CLI), '--model', 'gemini-3.5-flash-lite',
                 '--json-output', '--prompt', '@' + str(prompt_path)],
                capture_output=True, text=True, timeout=180,
            )
            if res.returncode == 0:
                env = json.loads(res.stdout)
                extracted = json.loads(env['text'])
                assert extracted['ticker'] == ticker
                for key in keys:
                    assert isinstance(extracted[key], list)
                    for item in extracted[key]:
                        assert all(field in item for field in ('headline', 'summary', 'date', 'impact', 'horizon', 'confidence'))
                        assert item['headline'] in {it['headline'] for it in items}
                source_dates = {it["headline"]: parsedate_to_datetime(it["pubDate"]).date().isoformat() for it in items}
                for key in keys:
                    for item in extracted[key]:
                        item["date"] = source_dates[item["headline"]]
                data = extracted
                save(ticker_file(ticker, 'ai-envelope.json'), env)
                break
            if attempt == 0:
                print('AI request failed; retrying after 90 seconds', flush=True)
                time.sleep(90)
            else:
                raise RuntimeError('Gemini failed twice; AI unavailable')
    except Exception as exc:
        data = {'ticker': ticker, 'as_of': '2026-10-03', **{k: [] for k in keys}, 'error': str(exc)}
        print(f'AI N/A: {exc}', flush=True)
    save(ticker_file(ticker, 'rss-items.json'), items)
    save(ticker_file(ticker, 'ai-intel.json'), data)
    print(f"AI extraction: {sum(len(data[k]) for k in keys)} items", flush=True)


if __name__ == '__main__':
    main()
