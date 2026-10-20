#!/usr/bin/env python3
"""Fetch Google News RSS for the selected ticker, then rule-first extraction with Flash-Lite fallback."""
from email.utils import parsedate_to_datetime
from datetime import date, timedelta, datetime, timezone
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

CLI = None  # Use the portable REST provider unless GEMINI_CLI is explicitly set.


class RSSFetchError(Exception):
    """Carries fetch diagnostics so callers can persist a graceful failure."""

    def __init__(self, category, retryable, attempts, detail):
        self.category = category
        self.retryable = retryable
        self.attempts = attempts
        self.detail = detail
        explanations = {
            'dns_or_connection': 'DNS resolution or network connection failed, cannot reach news.google.com',
            'timeout': 'Connection timed out, failed to fetch news from news.google.com in time',
            'http_error': 'news.google.com returned an HTTP error (rate limited, service error, or request rejected)',
            'malformed_xml': 'news.google.com returned malformed XML, cannot parse news',
        }
        super().__init__(
            f'RSS source unavailable ({explanations[category]}), gave up after {attempts} attempts. '
            'Skipping news analysis for this round; quantitative metrics unaffected.')


def rss_url(query):
    q = urllib.parse.quote(query)
    return f"https://news.google.com/rss/search?q={q}&hl=en-US&gl=US&ceid=US:en"


def rss_status(url, attempts, items=0, error=None):
    return dict(stage='rss_fetch', status='failed' if error else 'ok',
                category=error.category if error else None,
                retryable=error.retryable if error else False,
                attempts=attempts, url=url, items=items)


def fetch_rss(query, n=25, max_attempts=3, sleep=time.sleep, timeout=30,
              as_of=None, window_days=None):
    """Return (item list, status); retry transient failures after 0.5, 1, ... seconds."""
    if not isinstance(max_attempts, int) or isinstance(max_attempts, bool) or max_attempts < 1:
        raise ValueError('max_attempts must be a positive integer')
    cutoff = date.fromisoformat(as_of) if as_of else date.today()
    earliest = cutoff - timedelta(days=window_days) if window_days else None
    url = rss_url(query)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    for attempt in range(1, max_attempts + 1):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                xml = r.read()
            root = ET.fromstring(xml)
            if root.tag != 'rss' or root.find('channel') is None:
                raise ET.ParseError('Expected an RSS channel, not an error page')
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
            published = parsedate_to_datetime(pub_date).astimezone(timezone.utc).date()
            if published > cutoff or (earliest and published < earliest):
                continue
        except (ValueError, TypeError, OverflowError):
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
    'NVDA': ('nvidia',), 'MSFT': ('microsoft', 'azure'), 'AAPL': ('apple',),
    'GOOGL': ('alphabet', 'google', 'goog'), 'AMZN': ('amazon', 'amazon.com', 'aws'), 'TSLA': ('tesla',),
}
from universe import COMPANIES
ALIASES.update({ticker: (name.lower(),) for ticker, name in COMPANIES.items()})
ALIASES['J'] = ('jacobs solutions', 'jacobs')
# Specific corporate events precede generic earnings/market vocabulary.
EVENTS = {
    'acquisition': r'acquisition|acquir(?:e[sd]?|ing)|merger|takeover|buyout',
    'stock_split': r'stock splits?|share splits?|splits? (?:into|its)|spin[ -]?offs?|spins? off',
    'buyback': r'buy[ -]?backs?|repurchases?|share repurchase authorization',
    'dividend': r'dividends?',
    'guidance': r'guidance|outlook|forecast',
    'lawsuit': r'lawsuits?|sues?|suing|antitrust|litigation|court|liability',
    'product': r'launch(?:es|ed|ing)?|unveils?|release|iphone|robotaxi|fsd',
    'partnership': r'deals?|partnership|signs|agreement|contract',
    'analyst': r'analysts?|price target|upgrad(?:e[sd]?|ing)|downgrad(?:e[sd]?|ing)|conviction list|tactical ideas|top .*pick|fair value|valued|fair value boost',
    'workforce': r'layoffs?|job cuts',
    'earnings': r'(?:beats?|miss(?:es)?|tops?|exceeds?) .{0,25}estimates?|earnings|revenue|profits?|quarterly results|deliver(?:ies|ed)|delivery numbers|registrations',
    'ownership': r'(?:stock|shares) (?:sold|purchased|bought) by|(?:sells?|buys?) \$[\d,]+ in|insider (?:sale|purchase)',
    'calendar': r'mark your calendars?|scheduled (?:for|on)',
    'risk': r'flags? .*risk|approval risks?|accounts receivable|memory chip crunch',
    'market_move': r'stock|shares|premarket|market cap',
}
POSITIVE = r'jump(?:s|ed|ing)?|gain(?:s|ed|ing)?|climb(?:s|ed|ing)?|pop(?:s|ped)?|higher|surge(?:s|d)?|rall(?:y|ies|ied)|ris(?:e[sn]?|ing)|up|record highs?|all.time highs?|upgrad(?:e[sd]?|ing)|wins?|green light|bullish|better.than.expected|conviction list|top .*pick|optimism|best quarter'
NEGATIVE = r'fall(?:s|ing)?|fell|slip(?:s|ped)?|drop(?:s|ped)?|tumbl(?:ing|es?)|sink(?:s|ing)?|sank|slide[sd]?|down|lower(?:s|ed)?|downgrad(?:e[sd]?|ing)|worst|pressure|threat|warnings?|doubts|lawsuit|antitrust|layoffs?|post.ipo low|selloff|retreats?'


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
    def mentions(symbol, names):
        named = any(re.search(r'\b' + re.escape(name) + r'\b', text) for name in names)
        # A one-letter ticker is ambiguous in prose (notably J&J versus Jacobs).
        coded = (bool(re.search(r'\$' + re.escape(symbol) + r'\b|\(' + re.escape(symbol) + r'\)', headline))
                 if len(symbol) == 1 else bool(re.search(r'\b' + re.escape(symbol.lower()) + r'\b', text)))
        return named or coded

    companies = [symbol for symbol, names in ALIASES.items() if mentions(symbol, names)]
    event = next((name for name, pattern in EVENTS.items()
                  if re.search(r'(?<![a-z0-9])(?:' + pattern + r')(?![a-z0-9])', text)), 'unknown')
    if event == 'unknown' and re.search(r'\b(?:falls?|rises?|gains?|drops?)\s+\d+(?:\.\d+)?%', text):
        event = 'market_move'
    # A competitor's event is not a target-company event.
    other_subject = False
    if not (event == 'market_move' and text.startswith('stocks making')):
        # Only unambiguous target-led statements qualify for automatic rules.
        # A mention such as "Visa rival Mastercard wins ..." is not Visa's event.
        names = list(ALIASES.get(ticker, ()))
        if len(ticker) > 1:
            names.append(ticker.lower())
        target = r'(?:' + '|'.join(re.escape(name) for name in names) + r')\b'
        code = r'(?:\$' + re.escape(ticker.lower()) + r'\b|\(' + re.escape(ticker.lower()) + r'\))'
        lead_target = re.match(r'^\s*(?:' + target + '|' + code + r')', text)
        other_subject = not lead_target or bool(re.match(
            r"\s*(?:\([A-Za-z0-9.$:-]+\)\s*)?(?:['’]s\s+)?(?:rival|competitor|peer|supplier|customer|partner|and|versus|vs)\b|\s*:",
            text[lead_target.end():] if lead_target else ''))
    # A factual lead remains classifiable when followed by a commentary question.
    # Leading questions and conditional claims remain AI candidates.
    lead = re.split(r"[.!]\s+(?=[A-Z])|:\s+(?=(?:Is|What's|What is))|\s[-–—]\s+(?=(?:What|Still|Here))", headline)[0].lower()
    pos = bool(re.search(r'\b(?:' + POSITIVE + r')\b', lead))
    neg = bool(re.search(r'\b(?:' + NEGATIVE + r')\b', lead))
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
            raise ValueError('AI returned a different ticker')
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
            raise ValueError('AI returned a different ticker')
        if item_tickers:
            notes.append('ticker verified from item-level fields')
    payload['irrelevant'] = extracted.get('irrelevant', []) if isinstance(extracted.get('irrelevant', []), list) else []
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


def extract(items, ticker, call_ai=None, as_of=None):
    data = {'ticker': ticker, 'as_of': as_of or date.today().isoformat(), **{k: [] for k in KEYS}}
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
                    if (not isinstance(result['summary'], str) or not result['summary'].strip()
                            or impact is None or horizon is None
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
            irrelevant = []
            for result in payload['irrelevant']:
                if not isinstance(result, dict) or not isinstance(result.get('headline'), str):
                    continue
                matched = _match_pending_headline(result['headline'], by_headline, index)
                reason = result.get('reason')
                if matched is not None and matched not in used and isinstance(reason, str) and reason.strip():
                    irrelevant.append({'headline': matched, 'reason': reason.strip()})
                    used.add(matched)
            if irrelevant:
                data['irrelevant'] = irrelevant
            if notes:
                data['ai_notes'] = notes
            if skipped:
                data['ai_skipped'] = skipped
            pending = [it for it in pending if it['headline'] not in used]
        except Exception as exc:
            # HTTP and CLI transports expose safe messages; never include OS paths.
            detail = type(exc).__name__ if isinstance(exc, OSError) else str(exc)
            data['error'] = f'AI unavailable: {detail}'
            from groq_provider import GroqError
            from report_store import StorePushError
            if isinstance(exc, GroqError):
                data['failure'] = {'type': 'provider', 'status': exc.code, 'code': exc.provider_code}
            elif isinstance(exc, StorePushError):
                data['failure'] = {'type': 'store', 'code': exc.category}
            else:
                data['failure'] = {'type': 'analysis', 'code': type(exc).__name__}
    # Preserve unresolved headlines for audit, without inventing report classifications.
    data['unclassified'] = [classify_rule(it, ticker)[1] for it in pending]
    data['extraction_stats'] = {
        'unique_headlines': len(seen),
        **{method: sum(it['extraction_method'] == method for k in (*KEYS, 'unclassified') for it in data[k])
           for method in ('rule', 'ai', 'unknown')},
    }
    if data.get('irrelevant'):
        data['extraction_stats']['irrelevant'] = len(data['irrelevant'])
    return data


def classification_schema(ticker):
    fields = {'headline': {'type': 'string'}, 'summary': {'type': 'string'},
              'impact': {'type': 'string', 'enum': ['high', 'medium', 'low']},
              'horizon': {'type': 'string', 'enum': ['short', 'medium', 'long']},
              'confidence': {'type': 'number'},
              'event_type': {'type': 'string', 'enum': [*EVENTS, 'unknown']},
              'sentiment': {'type': 'string', 'enum': ['positive', 'negative', 'neutral', 'unknown']}}
    item = {'type': 'object', 'properties': fields, 'required': list(fields), 'additionalProperties': False}
    irrelevant = {'type': 'object', 'properties': {'headline': {'type': 'string'}, 'reason': {'type': 'string'}},
                  'required': ['headline', 'reason'], 'additionalProperties': False}
    properties = {'ticker': {'type': 'string', 'enum': [ticker]},
                  **{name: {'type': 'array', 'items': {'$ref': '#/$defs/news_item'}} for name in KEYS},
                  'irrelevant': {'type': 'array', 'items': {'$ref': '#/$defs/irrelevant_item'}}}
    return {'type': 'object', 'properties': properties, 'required': list(properties), 'additionalProperties': False,
            '$defs': {'news_item': item, 'irrelevant_item': irrelevant}}


def call_gemini(items, ticker):
    from ai_provider import provider
    if provider() == 'groq' and len(items) > 5:
        combined = {'ticker': ticker, **{name: [] for name in (*KEYS, 'irrelevant')}}
        for offset in range(0, len(items), 5):
            result, _ = _normalize_ai_payload(call_gemini(items[offset:offset + 5], ticker), ticker)
            for name in (*KEYS, 'irrelevant'):
                combined[name].extend(result.get(name, []))
        return combined
    import os
    import time
    from data_utils import DATA, save, ticker_file
    prompt = (
        f'Target company: {COMPANIES.get(ticker, ticker)} ({ticker}). '
        f'Use ticker exactly {ticker}, not another listing. '
        'Classify only facts grounded in supplied headlines; do not infer article content or listing prices. '
        'Copy headlines exactly. Summaries must be at most 35 words. Confidence must be 0-1. '
        'A competitor event is not a target-company event. '
        'Put each irrelevant headline in irrelevant with a brief reason. Do not force relevance. '
        'Return the required JSON object. News: ' +
        json.dumps([{'headline': item.get('headline', item.get('title', ''))} for item in items])
    )
    if provider() != 'groq':
        prompt += ' Output JSON schema: ' + json.dumps(classification_schema(ticker))
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
    from ai_provider import provider
    cli = os.environ.get('GEMINI_CLI') if provider() == 'gemini' else None
    if not cli:
        from ai_provider import generate_json
        envelope = generate_json(prompt, schema=classification_schema(ticker)) if provider() == 'groq' else generate_json(prompt)
        save(ticker_file(ticker, 'ai-envelope.json'), envelope)
        return _parse_gemini_json(envelope['text'])
    res = subprocess.run(
        [cli, '--model', os.environ.get('GEMINI_MODEL', MODEL),
         '--json-output', '--prompt', '@' + str(path)],
        capture_output=True, text=True, timeout=180,
    )
    if res.returncode:
        raise RuntimeError(f'Gemini CLI exited with status {res.returncode}')
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
        raise RuntimeError('Gemini payload was not valid JSON') from None
    save(ticker_file(ticker, 'ai-envelope.json'), envelope)
    return result


def main():
    from data_utils import save, ticker_arg, ticker_file, as_of_date
    import os
    ticker = ticker_arg()
    as_of = as_of_date().isoformat()
    query = f'{COMPANIES[ticker]} {ticker} stock'
    rss_options = {}
    for option in ('max_attempts', 'timeout'):
        env_name = 'JSOSIF_RSS_' + option.upper()
        if env_name in os.environ:
            rss_options[option] = int(os.environ[env_name])
    try:
        items, fetch_status = fetch_rss(
            query, int(os.environ.get('JSOSIF_RSS_COUNT', '25')),
            as_of=as_of, window_days=7, **rss_options)
    except RSSFetchError as exc:
        items = []
        data = extract([], ticker, as_of=as_of)
        data['error'] = str(exc)
        fetch_status = rss_status(rss_url(query), exc.attempts, error=exc)
        fetch_status['detail'] = exc.detail
        print(str(exc), file=sys.stderr)
    else:
        enabled = os.environ.get('JSOSIF_AI_ENABLED', '1') == '1'
        data = extract(items, ticker, call_gemini if enabled else None, as_of=as_of)
        if not enabled and items:
            data['error'] = os.environ.get('JSOSIF_AI_UNAVAILABLE_REASON', 'AI analysis is disabled for this run')
    data['fetched_at'] = datetime.now(timezone.utc).isoformat()
    from ai_provider import model
    data['model'] = (model()
                     if os.environ.get('JSOSIF_AI_ENABLED', '1') == '1' else 'rules-only')
    data['fetch_status'] = fetch_status
    save(ticker_file(ticker, 'rss-items.json'), items)
    save(ticker_file(ticker, 'ai-intel.json'), data)
    print('Extraction: ' + json.dumps(data['extraction_stats']), flush=True)


if __name__ == '__main__':
    main()

