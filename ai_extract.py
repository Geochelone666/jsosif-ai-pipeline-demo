#!/usr/bin/env python3
"""Fetch Google News RSS for NVDA, then Gemini (plain, no grounding) structured extraction."""
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
        items.append({
            "headline": headline,
            "source": source,
            "link": it.findtext("link") or "",
            "pubDate": it.findtext("pubDate") or "",
        })
    return items


def main():
    items = fetch_rss("NVDA stock", 25)
    print(f"RSS items: {len(items)}", flush=True)
    with open("rss-items.json", "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=1)

    lines = "\n".join(
        f"- [{it['pubDate']}] ({it['source']}) {it['headline']}" for it in items
    )
    prompt = (
        "You are a financial research assistant for a student investment fund. "
        "Below are recent news headlines about NVIDIA (NVDA).\n\n"
        "Classify each item into tailwinds (positive), headwinds (negative), "
        "catalysts (upcoming events), or risks. Then summarize.\n\n"
        "Rules:\n"
        "- Output ONLY valid JSON, no markdown fences, no commentary.\n"
        "- Every item: headline, summary (1-2 sentences, in Chinese), date from pubDate "
        "(YYYY-MM-DD), impact high|medium|low, horizon short|medium|long, confidence 0-1.\n"
        "- Skip duplicates and irrelevant items.\n\n"
        "Schema:\n"
        '{"ticker":"NVDA","as_of":"2026-10-03","tailwinds":[],"headwinds":[],'
        '"catalysts":[],"risks":[]}\n'
        "Each element: "
        '{"headline":str,"summary":str,"date":str,"impact":str,"horizon":str,"confidence":float}\n\n'
        f"Headlines:\n{lines}"
    )
    with open("/tmp/nvda-ai-prompt.txt", "w", encoding="utf-8") as f:
        f.write(prompt)

    res = subprocess.run(
        [CLI, "--model", "gemini-3.5-flash-lite", "--json-output",
         "--prompt", "@/tmp/nvda-ai-prompt.txt"],
        capture_output=True, text=True, timeout=180,
    )
    print("CLI rc:", res.returncode, flush=True)
    if res.returncode != 0:
        print("STDERR:", res.stderr[:600])
        raise SystemExit(1)
    env = json.loads(res.stdout)
    with open("ai-envelope.json", "w", encoding="utf-8") as f:
        json.dump(env, f, ensure_ascii=False, indent=1)
    data = json.loads(env["text"])
    for k in ("ticker", "as_of", "tailwinds", "headwinds", "catalysts", "risks"):
        assert k in data, f"missing key {k}"
    with open("ai-intel.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    n = sum(len(data[k]) for k in ("tailwinds", "headwinds", "catalysts", "risks"))
    print(f"AI extraction OK: {n} items")


if __name__ == "__main__":
    main()
