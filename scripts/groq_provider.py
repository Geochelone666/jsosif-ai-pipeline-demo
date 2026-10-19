"""Groq JSON client with durable application budgets and bounded retries.

Local caps are application policy, not a statement of an account's Groq limits.
"""
import json
import os
import time
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

DEFAULT_MODEL = 'llama-3.1-8b-instant'


class GroqError(RuntimeError):
    pass


def settings():
    defaults = {'RPD': 100, 'RPM': 10, 'TPD': 100000, 'TPM': 5000}
    try:
        caps = {name: int(os.environ.get('GROQ_' + name) or value)
                for name, value in defaults.items()}
        if min(caps.values()) < 1:
            raise ValueError
    except ValueError:
        raise GroqError('Groq application budgets must be positive integers') from None
    return caps


def _save(path, ledger):
    if not path:
        return
    from report_store import write_json, persist
    write_json(Path(path), ledger)
    if os.environ.get('JSOSIF_PERSIST_API_USAGE') == '1':
        persist(Path(path).resolve().parents[1], git=True)


def _reserve(model, tokens, sleep):
    from report_store import read_json
    path = os.environ.get('JSOSIF_API_USAGE_PATH')
    ledger = read_json(Path(path), {}) if path else {}
    caps = settings()
    now = time.time()
    day = datetime.fromtimestamp(now, timezone.utc).date().isoformat()
    key = 'groq:' + model + ':' + day
    state = ledger.setdefault(key, {'requests': 0, 'tokens': 0})
    if state['requests'] >= caps['RPD'] or state['tokens'] + tokens > caps['TPD']:
        raise GroqError('Groq application daily budget exhausted')
    if tokens > caps['TPM']:
        raise GroqError('Groq prompt exceeds application per-minute token budget')
    # Space reservations conservatively, including failed/retried requests.
    delay = max(0, ledger.get('groq_next_request_at', 0) - now)
    if delay > 120:
        raise GroqError('Groq retry deferred by server or application pacing')
    if delay:
        sleep(delay)
    state['requests'] += 1
    state['tokens'] += tokens
    ledger['groq_next_request_at'] = time.time() + max(60 / caps['RPM'], 60 * tokens / caps['TPM'])
    _save(path, ledger)  # Persist before HTTP; a crash must not erase a reservation.
    return path, ledger, key


def _retry_delay(headers, fallback):
    value = headers.get('retry-after', '') if headers else ''
    try:
        return max(0, float(value))
    except ValueError:
        try:
            return max(0, parsedate_to_datetime(value).timestamp() - time.time())
        except (ValueError, TypeError, OverflowError):
            return fallback


def generate_json(prompt, model=DEFAULT_MODEL, *, attempts=3, opener=urlopen, sleep=time.sleep):
    key = os.environ.get('GROQ_API_KEY') or os.environ.get('Grop_ai_API')
    if not key:
        raise GroqError('Groq API key is not configured')
    # A byte bound intentionally overestimates input tokens; output is bounded too.
    reserved = len(prompt.encode('utf-8')) + 1800
    body = json.dumps({'model': model, 'messages': [
        {'role': 'system', 'content': 'Return a valid JSON object only.'},
        {'role': 'user', 'content': prompt}], 'temperature': 0,
        'response_format': {'type': 'json_object'}, 'max_completion_tokens': 1600}).encode()
    request = Request('https://api.groq.com/openai/v1/chat/completions', data=body,
                      headers={'Authorization': 'Bearer ' + key, 'Content-Type': 'application/json'})
    for attempt in range(attempts):
        path, ledger, slot = _reserve(model, reserved, sleep)
        try:
            with opener(request, timeout=60) as response:
                payload = json.load(response)
            text = payload.get('choices', [{}])[0].get('message', {}).get('content')
            if not isinstance(text, str) or not text.strip():
                raise GroqError('Groq returned no usable content')
            usage = payload.get('usage', {})
            actual = usage.get('total_tokens')
            if isinstance(actual, int) and actual >= 0:
                ledger[slot]['tokens'] += actual - reserved
                _save(path, ledger)
            return {'text': text, 'model': model, 'usage': {
                k: usage[k] for k in ('prompt_tokens', 'completion_tokens', 'total_tokens') if k in usage}}
        except HTTPError as exc:
            retry = exc.code in (408, 409, 429) or exc.code >= 500
            delay = _retry_delay(exc.headers, 2 ** (attempt + 1))
            if retry:
                ledger['groq_next_request_at'] = max(ledger.get('groq_next_request_at', 0), time.time() + delay)
                _save(path, ledger)
            if not retry or attempt + 1 == attempts or delay > 120:
                raise GroqError(f'Groq HTTP {exc.code}; check account limits and retry guidance') from None
            sleep(delay)
        except (URLError, TimeoutError, OSError):
            if attempt + 1 == attempts:
                raise GroqError('Groq connection failed') from None
            sleep(2 ** (attempt + 1))
        except (ValueError, KeyError, IndexError, TypeError):
            raise GroqError('Groq returned an invalid response') from None
    raise GroqError('Groq request failed')
