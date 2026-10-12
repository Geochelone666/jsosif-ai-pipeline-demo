#!/usr/bin/env python3
"""Fetch Google News RSS for the selected ticker, then rule-first extraction with Flash-Lite fallback."""
from email.utils import parsedate_to_datetime
import html
import http.client
import json
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

CLI = "/home/hatch/workspace/skills/google-ai-studio/bin/gemini-call.py"


class RSSFetchError(Exception):
    """Carries fetch diagnostics so callers can persist a graceful failure."""

    def __init__(self, category, retryable, attempts, detail):
        self.category = category
        self.retryable = retryable
        self.attempts = attempts
        self.detail = detail
        explanations = {
            'dns_or_connection': '域名解析或网络连接失败，无法访问 news.google.com',
            'timeout': '连接超时，未能及时从 news.google.com 获取新闻',
            'http_error': 'news.google.com 返回 HTTP 错误，暂时限流、服务异常或请求被拒绝',
            'malformed_xml': 'news.google.com 返回的 XML 格式损坏，无法解析新闻',
        }
        super().__init__(
            f'RSS 源不可用（{explanations[category]}），{attempts} 次尝试后放弃。'
            '本轮新闻分析跳过，量化指标不受影响。')


def rss_url(query):
    q = urllib.parse.quote(query)
    return f"https://news.google.com/rss/search?q={q}&hl=en-US&gl=US&ceid=US:en"


def rss_status(url, attempts, items=0, error=None):
    return dict(stage='rss_fetch', status='failed' if error else 'ok',
                category=error.category if error else None,
                retryable=error.retryable if error else False,
                attempts=attempts, url=url, items=items)


def fetch_rss(query, n=25, max_attempts=3, sleep=time.sleep):
    """Return (item list, status); retry transient failures after 0.5, 1, ... seconds."""
    if not isinstance(max_attempts, int) or isinstance(max_attempts, bool) or max_attempts < 1:
        raise ValueError('max_attempts must be a positive integer')
    url = rss_url(query)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    for attempt in range(1, max_attempts + 1):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                xml = r.read()
            root = ET.fromstring(xml)
            break
        except (OSError, http.client.HTTPException, ET.ParseError) as exc:
            if isinstance(exc, urllib.error.HTTPError):
                category = 'http_error'
                retryable = exc.code == 429 or 500 <= exc.code <= 599
            elif isinstance(exc, ET.ParseError):
                category, retryable = 'malformed_xml', False
            elif isinstance(getattr(exc, 'reason', exc), TimeoutError):
                category, retryable = 'timeout', True
            else:
                category, retryable = 'dns_or_connection', True
            if not retryable or attempt == max_attempts:
                raise RSSFetchError(category, retryable, attempt, str(exc)) from exc
            sleep(0.5 * 2 ** (attempt - 1))
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
    return items, rss_status(url, attempt, len(items))


KEYS = ('tailwinds', 'headwinds', 'catalysts', 'risks')
MODEL = 'gemini-3.5-flash-lite'
ALIASES = {
    'NVDA': ('nvidia', '英伟达', '輝達'), 'MSFT': ('microsoft', '微软', '微軟', 'azure'), 'AAPL': ('apple', '苹果', '蘋果'),
    'GOOGL': ('alphabet', 'google', 'goog', '谷歌'), 'AMZN': ('amazon', 'amazon.com', 'aws', '亚马逊', '亞馬遜'), 'TSLA': ('tesla', '特斯拉'),
}
from universe import COMPANIES
ALIASES.update({ticker: (name.lower(),) for ticker, name in COMPANIES.items()})
# Specific corporate events precede generic earnings/market vocabulary.
EVENTS = {
    'acquisition': r'acquisition|acquir(?:e[sd]?|ing)|merger|takeover|buyout|收购|并购',
    'stock_split': r'stock splits?|share splits?|splits? (?:into|its)|spin[ -]?offs?|spins? off|拆分|拆股|分拆',
    'buyback': r'buy[ -]?backs?|repurchases?|share repurchase authorization|回购',
    'dividend': r'dividends?|派息|股息',
    'guidance': r'guidance|outlook|forecast|指引|展望',
    'lawsuit': r'lawsuits?|sues?|suing|antitrust|litigation|court|liability|诉讼|反垄断',
    'product': r'launch(?:es|ed|ing)?|unveils?|release|iphone|robotaxi|fsd|推出|发布',
    'partnership': r'deals?|partnership|signs|agreement|contract|合作|协议',
    'analyst': r'analysts?|price target|upgrad(?:e[sd]?|ing)|downgrad(?:e[sd]?|ing)|conviction list|tactical ideas|top .*pick|fair value|valued|评级|目标价|fair value boost',
    'workforce': r'layoffs?|job cuts|裁员',
    'earnings': r'(?:beats?|miss(?:es)?|tops?|exceeds?) .{0,25}estimates?|earnings|revenue|profits?|quarterly results|deliver(?:ies|ed)|delivery numbers|registrations|财报|营收|利润',
    'ownership': r'(?:stock|shares) (?:sold|purchased|bought) by|(?:sells?|buys?) \$[\d,]+ in|insider (?:sale|purchase)|持股|增持|减持',
    'calendar': r'mark your calendars?|scheduled (?:for|on)',
    'risk': r'flags? .*risk|approval risks?|accounts receivable|memory chip crunch',
    'market_move': r'stock|shares|premarket|market cap|股价|股票',
}
POSITIVE = r'jump(?:s|ed|ing)?|gain(?:s|ed|ing)?|climb(?:s|ed|ing)?|pop(?:s|ped)?|higher|surge(?:s|d)?|rall(?:y|ies|ied)|ris(?:e[sn]?|ing)|up|record highs?|all.time highs?|upgrad(?:e[sd]?|ing)|wins?|green light|bullish|better.than.expected|conviction list|top .*pick|optimism|best quarter|上涨|大涨|上调|超预期'
NEGATIVE = r'fall(?:s|ing)?|fell|slip(?:s|ped)?|drop(?:s|ped)?|tumbl(?:ing|es?)|sink(?:s|ing)?|sank|slide[sd]?|down|lower(?:s|ed)?|downgrad(?:e[sd]?|ing)|worst|pressure|threat|warnings?|doubts|lawsuit|antitrust|layoffs?|post.ipo low|selloff|retreats?|下跌|下调|不及预期'


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
                 if any(re.search((r'\b' + re.escape(name) + r'\b') if name.isascii() else re.escape(name), text)
                        for name in (*names, symbol.lower()))]
    event = next((name for name, pattern in EVENTS.items()
                  if re.search(r'(?<![a-z0-9])(?:' + pattern + r')(?![a-z0-9])', text)), 'unknown')
    if event == 'unknown' and re.search(r'\b(?:falls?|rises?|gains?|drops?)\s+\d+(?:\.\d+)?%', text):
        event = 'market_move'
    # A competitor's price move is not a target-company price move.
    other_subject = False
    if event == 'market_move' and not text.startswith('stocks making'):
        subject = re.split(r'\b(?:stock|shares)\b', text, maxsplit=1)[0]
        other_subject = not any(re.search(r'\b'+re.escape(name)+r'\b', subject) if name.isascii() else name in subject for name in (*ALIASES.get(ticker, ()), ticker.lower()))
    # A factual lead remains classifiable when followed by a commentary question.
    # Leading questions and conditional claims remain AI candidates.
    lead = re.split(r"[.!]\s+(?=[A-Z])|:\s+(?=(?:Is|What's|What is))|\s[-–—]\s+(?=(?:What|Still|Here))", headline)[0].lower()
    pos = bool(re.search(r'\b(?:' + POSITIVE + r')\b', lead))
    neg = bool(re.search(r'\b(?:' + NEGATIVE + r')\b', lead))
    pos = pos or any(word in lead for word in ('上涨', '大涨', '上调', '超预期'))
    neg = neg or any(word in lead for word in ('下跌', '下调', '不及预期'))
    # Evaluate forecasts within the lead, without treating calendar month May as speculation.
    speculation_text = re.sub(r'\b(?:in|since|during|of) may\b', '', lead)
    ambiguous = bool(re.search(r'\?|\b(?:could|may|might|prediction|predicts|predicted|will|expected to)\b', speculation_text))
    # Calendar May and relational expressions are not directional signals.
    if re.search(r'\b(?:falls? (?:just )?shy|near(?:ly)? .*high|back at .*record)\b', lead):
        ambiguous = True
    sentiment = ('positive' if pos else 'negative') if pos != neg and not ambiguous else 'unknown'
    # Earnings beats/misses and guidance/rating revisions require event-local verbs.
    if not ambiguous:
        if event == 'earnings':
            beat = bool(re.search(r'\b(?:beats?|tops?|exceeds?)\b.{0,35}\b(?:estimates?|expectations?|consensus)\b', lead))
            miss = bool(re.search(r'\b(?:miss(?:es)?|below)\b.{0,35}\b(?:estimates?|expectations?|consensus)\b', lead))
            if beat != miss:
                sentiment = 'unknown' if (beat and neg) or (miss and pos) else 'positive' if beat else 'negative'
        elif event in ('guidance', 'analyst'):
            raised = bool(re.search(r'\b(?:rais(?:e[sd]?|ing)|boost(?:s|ed)?|hik(?:e[sd]?|ing)|upgrad(?:e[sd]?|ing))\b', lead))
            cut = bool(re.search(r'\b(?:cuts?|lower(?:s|ed)?|slash(?:es|ed)?|downgrad(?:e[sd]?|ing))\b', lead))
            if raised != cut and not (pos and neg):
                sentiment = 'positive' if raised else 'negative'
        if sentiment == 'unknown' and not pos and not neg and event in ('dividend', 'acquisition', 'partnership', 'product', 'buyback', 'stock_split', 'earnings', 'ownership', 'calendar', 'analyst'):
            sentiment = 'neutral'
    if not ambiguous and not (pos and neg) and event == 'risk':
        sentiment = 'negative'
    if not ambiguous and event == 'market_move' and text.startswith('stocks making the biggest moves'):
        sentiment = 'neutral'
    method = 'rule' if event != 'unknown' and sentiment != 'unknown' and ticker in companies and not other_subject and metadata(item)['date'] else 'unknown'
    category = 'tailwinds' if sentiment == 'positive' else 'headwinds' if sentiment == 'negative' else 'catalysts'
    # Announcements are discrete catalysts even when a market reaction is included.
    if event in ('product', 'buyback', 'stock_split', 'dividend', 'acquisition', 'ownership', 'calendar') and sentiment != 'negative':
        category = 'catalysts'
    if event == 'analyst' and not re.search(r'\b(?:upgrad(?:e[sd]?|ing)|downgrad(?:e[sd]?|ing)|rais(?:e[sd]?|ing)|lower(?:s|ed)?|top .*pick|conviction list)\b', lead):
        category = 'catalysts'
    if event == 'risk':
        category = 'risks'
    if sentiment == 'negative' and event == 'lawsuit' and re.search(r'\b(?:lawsuits?|sues?|suing|antitrust|litigation|court)\b', lead):
        category = 'risks'
    result = {'headline': headline, 'summary': headline, 'impact': 'medium',
              'horizon': 'short', 'confidence': 0.8 if method == 'rule' else 0.0,
              'companies': companies, 'event_type': event, 'sentiment': sentiment,
              'extraction_method': method, **metadata(item)}
    return category, result


# Lenient normalization for Gemini output. Gemini is mostly right but drifts:
# singular category names, list-wrapped payloads, reworded headlines, and
# non-canonical impact/horizon words. Normalize what we can; skip single
# items we cannot; fail the whole AI batch only on structural breakage.
def _norm_text(s):
    return ' '.join(str(s).lower().split())

_LEADING_QUESTION_WORDS = ('why ', 'how ', 'what ', 'when ', 'where ',
                           'is ', 'are ', 'was ', 'were ', 'will ',
                           'would ', 'could ', 'should ', 'can ', 'do ',
                           'does ', 'did ')

def _strip_leading_question(s):
    for q in _LEADING_QUESTION_WORDS:
        if s.startswith(q):
            return s[len(q):]
    return s

_IMPACT_MAP = {
    'high': 'high', 'major': 'high', 'severe': 'high', 'significant': 'high',
    'medium': 'medium', 'moderate': 'medium',
    'low': 'low', 'minor': 'low', 'minimal': 'low', 'negligible': 'low',
}
_HORIZON_MAP = {
    'short': 'short', 'near-term': 'short', 'near term': 'short',
    'immediate': 'short', 'past': 'short',
    'medium': 'medium', 'medium-term': 'medium', 'medium term': 'medium',
    'mid-term': 'medium', 'mid term': 'medium',
    'long': 'long', 'long-term': 'long', 'long term': 'long',
}
_VALID_SENTIMENTS = ('positive', 'negative', 'neutral', 'unknown')


def _normalize_ai_payload(extracted, ticker):
    """Leniently normalize Gemini's payload. Returns (payload, notes).

    Raises ValueError only on structural breakage (wrong shape, ticker
    mismatch); per-item problems are left for the caller to skip.
    """
    notes = []
    if isinstance(extracted, list):
        if len(extracted) == 1 and isinstance(extracted[0], dict):
            notes.append('unwrapped single-element list payload')
            extracted = extracted[0]
        else:
            raise ValueError('AI returned a list instead of an object')
    if not isinstance(extracted, dict):
        raise ValueError('AI returned a non-object payload')
    top_ticker = extracted.get('ticker')
    if isinstance(top_ticker, str) and top_ticker.strip():
        if top_ticker.strip().lower() != ticker.lower():
            raise ValueError('Gemini returned a different ticker')
    payload = {}
    for key in KEYS:
        val = extracted.get(key)
        if val is None:
            singular = key[:-1]
            if singular in extracted:
                notes.append(f'mapped singular category {singular!r} -> {key!r}')
                val = extracted[singular]
        if val is None:
            payload[key] = []
        elif isinstance(val, list):
            payload[key] = val
        else:
            notes.append(f'category {key!r} was not a list; ignored')
            payload[key] = []
    if not (isinstance(top_ticker, str) and top_ticker.strip()):
        item_tickers = {str(it.get('ticker')).strip().lower()
                        for items in payload.values() for it in items
                        if isinstance(it, dict) and it.get('ticker')}
        bad = {t for t in item_tickers if t != ticker.lower()}
        if bad:
            raise ValueError('Gemini returned a different ticker')
        if item_tickers:
            notes.append('ticker verified from item-level fields')
    return payload, notes


def _build_headline_index(pending):
    """Map normalized headline forms to the exact pending headline."""
    index = {}
    for it in pending:
        exact = it['headline']
        normed = _norm_text(exact)
        for form in {normed, _strip_leading_question(normed)}:
            index.setdefault(form, exact)
    return index


def _match_pending_headline(headline, by_headline, index):
    """Match a Gemini-returned headline to a pending RSS headline.

    Returns the exact pending headline or None. Tiered: exact, normalized,
    normalized minus leading question word, then a conservative fuzzy match.
    """
    if headline in by_headline:
        return headline
    import difflib
    normed = _norm_text(headline)
    if normed in index:
        return index[normed]
    stripped = _strip_leading_question(normed)
    if stripped in index:
        return index[stripped]
    close = difflib.get_close_matches(normed, list(index), n=1, cutoff=0.92)
    return index[close[0]] if close else None


def _parse_gemini_json(text):
    """Parse Gemini's JSON payload, tolerating markdown code fences."""
    t = str(text).strip()
    if t.startswith('```'):
        lines = t.split('\n')
        if lines and lines[0].startswith('```'):
            lines = lines[1:]
        while lines and lines[-1].strip().startswith('```'):
            lines = lines[:-1]
        t = '\n'.join(lines).strip()
    return json.loads(t)


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
            payload, notes = _normalize_ai_payload(extracted, ticker)
            by_headline = {it['headline']: it for it in pending}
            index = _build_headline_index(pending)
            staged = {k: [] for k in KEYS}
            used = set()
            skipped = []
            for key in KEYS:
                for result in payload[key]:
                    headline = result.get('headline') if isinstance(result, dict) else None
                    if not isinstance(headline, str):
                        skipped.append({'headline': None, 'reason': 'not a dict or missing headline', 'category': key})
                        continue
                    matched = _match_pending_headline(headline, by_headline, index)
                    if matched is None:
                        skipped.append({'headline': headline, 'reason': 'no matching pending headline', 'category': key})
                        continue
                    if matched in used:
                        skipped.append({'headline': headline, 'reason': 'duplicate headline', 'category': key})
                        continue
                    fields = ('summary', 'impact', 'horizon', 'confidence', 'event_type', 'sentiment')
                    if not all(field in result for field in fields):
                        skipped.append({'headline': headline, 'reason': 'incomplete item', 'category': key})
                        continue
                    impact = _IMPACT_MAP.get(_norm_text(result['impact']))
                    horizon = _HORIZON_MAP.get(_norm_text(result['horizon']))
                    sentiment = _norm_text(result['sentiment'])
                    event_type = _norm_text(result['event_type'])
                    confidence = result['confidence']
                    if (impact is None or horizon is None
                            or sentiment not in _VALID_SENTIMENTS
                            or event_type not in (*EVENTS, 'unknown')
                            or isinstance(confidence, bool)
                            or not isinstance(confidence, (int, float))
                            or not 0 <= confidence <= 1):
                        skipped.append({'headline': headline, 'reason': 'invalid field value', 'category': key})
                        continue
                    base = classify_rule(by_headline[matched], ticker)[1]
                    base.update({'summary': result['summary'], 'impact': impact,
                                 'horizon': horizon, 'confidence': confidence,
                                 'event_type': event_type, 'sentiment': sentiment})
                    base['extraction_method'] = 'ai'
                    staged[key].append(base)
                    used.add(matched)
            for key in KEYS:
                data[key].extend(staged[key])
            if notes:
                data['ai_notes'] = notes
            if skipped:
                data['ai_skipped'] = skipped
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
    from data_utils import DATA, save, ticker_file
    prompt = (
        f'Classify relevant {ticker} news into tailwinds, headwinds, catalysts, risks. '
        'Return JSON with ticker and those four arrays. Skip irrelevant news. '
        'Each item: headline copied exactly, summary grounded only in headline, '
        'impact high/medium/low, horizon short/medium/long, confidence 0-1, '
        'event_type from ' + ', '.join(EVENTS) + ', or unknown; '
        'sentiment positive/negative/neutral/unknown. Do not infer facts absent from headlines. '
        'News: ' + json.dumps(items)
    )
    path = DATA / ticker_file(ticker, 'ai-prompt.txt')
    path.write_text(prompt, encoding='utf-8')
    last_call = DATA / '.last-ai-call'
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
    # Persist the raw stdout before parsing so malformed payloads stay debuggable.
    save(ticker_file(ticker, 'ai-envelope-raw.json'),
         {'stdout': res.stdout, 'stderr': (res.stderr or '')[:500],
          'returncode': res.returncode})
    try:
        envelope = json.loads(res.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f'Gemini envelope not JSON: {exc}')
    try:
        result = _parse_gemini_json(envelope['text'])
    except (KeyError, TypeError, json.JSONDecodeError) as exc:
        head = str(envelope.get('text') if isinstance(envelope, dict) else '')[:200]
        raise RuntimeError(f'Gemini payload not JSON: {exc}; text head: {head!r}')
    save(ticker_file(ticker, 'ai-envelope.json'), envelope)
    return result


def main():
    from data_utils import save, ticker_arg, ticker_file
    ticker = ticker_arg()
    query = f'{COMPANIES[ticker]} {ticker} stock'
    try:
        items, fetch_status = fetch_rss(query, 25)
    except RSSFetchError as exc:
        items = []
        data = extract([], ticker)
        data['error'] = str(exc)
        fetch_status = rss_status(rss_url(query), exc.attempts, error=exc)
        fetch_status['detail'] = exc.detail
        print(str(exc), file=sys.stderr)
    else:
        data = extract(items, ticker, call_gemini)
    data['fetch_status'] = fetch_status
    save(ticker_file(ticker, 'rss-items.json'), items)
    save(ticker_file(ticker, 'ai-intel.json'), data)
    print('Extraction: ' + json.dumps(data['extraction_stats']), flush=True)


if __name__ == '__main__':
    main()
