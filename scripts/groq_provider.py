"""Groq JSON client with durable application budgets and bounded retries.

Local caps are application policy, not a statement of an account's Groq limits.
"""
import json
import math
import os
import time
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request
from credential_http import urlopen

DEFAULT_MODEL = 'openai/gpt-oss-20b'
MODEL_CANDIDATES = (DEFAULT_MODEL, 'llama-3.1-8b-instant', 'llama-3.3-70b-versatile',
                    'openai/gpt-oss-120b', 'qwen/qwen3-32b',
                    'meta-llama/llama-4-scout-17b-16e-instruct')


def available_models(*, opener=urlopen):
    key = os.environ.get('GROQ_API_KEY') or os.environ.get('Grop_ai_API')
    if not key:
        raise GroqError('Groq API key is not configured')
    request = Request('https://api.groq.com/openai/v1/models',
                      headers={'Authorization': 'Bearer ' + key, 'User-Agent': 'JSOSIF/1.0'})
    with opener(request, timeout=60) as response:
        payload = json.load(response)
    enabled = {entry.get('id') for entry in payload.get('data', []) if isinstance(entry, dict)}
    return [model for model in MODEL_CANDIDATES if model in enabled]


class GroqError(RuntimeError):
    def __init__(self, message, *, status=None, provider_code=None):
        super().__init__(message)
        self.code = status
        self.provider_code = provider_code


def error_code(response):
    """Return a known diagnostic code, never raw error content or credentials."""
    try:
        raw = response.read(8192)
        if b'error code: 1010' in raw.lower():
            return 'edge_policy_1010'
        error = json.loads(raw).get('error', {})
        code = error.get('code') or error.get('type')
        allowed = {'invalid_api_key', 'insufficient_permissions', 'permission_denied',
                   'model_not_found', 'rate_limit_exceeded', 'unsupported_country_region_territory',
                   'access_denied', 'json_validate_failed', 'invalid_request_error', 'json_schema_unsupported'}
        return code if isinstance(code, str) and code in allowed else None
    except (OSError, ValueError, TypeError, AttributeError):
        return None


def settings():
    defaults = {'RPD': 200, 'RPM': 10, 'TPD': 200000, 'TPM': 5000}
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


def reconcile_usage(path, ledger):
    # The remote reservation already covers this call. Keep the actual usage
    # locally; the next reservation or ticker checkpoint pushes it durably.
    # A crash in between retains the conservative remote upper bound.
    if path:
        from report_store import write_json
        write_json(Path(path), ledger)


def minute_slot(events, start, tokens, caps):
    """Reserve against a rolling minute, including differently sized requests."""
    at = start
    while True:
        active = [event for event in events if event['at'] > at - 60]
        if len(active) < caps['RPM'] and sum(event['tokens'] for event in active) + tokens <= caps['TPM']:
            return at, active
        at = min(event['at'] for event in active) + 60


def _reserve(model, tokens, sleep):
    from report_store import read_json
    path = os.environ.get('JSOSIF_API_USAGE_PATH')
    ledger = read_json(Path(path), {}) if path else {}
    caps = settings()
    now = time.time()
    if tokens > caps['TPM']:
        raise GroqError('Groq prompt exceeds application per-minute token budget')
    # Determine the UTC application day after waiting: pacing may cross midnight.
    at, recent = minute_slot(ledger.get('groq_recent_requests', []),
                             max(now, ledger.get('groq_next_request_at', 0)), tokens, caps)
    delay = max(0, at - now)
    if delay > 120:
        raise GroqError('Groq retry deferred by server or application pacing')
    next_day = datetime.fromtimestamp(now + delay, timezone.utc).date().isoformat()
    pending = ledger.get('groq:' + model + ':' + next_day, {})
    if pending.get('requests', 0) >= caps['RPD'] or pending.get('tokens', 0) + tokens > caps['TPD']:
        raise GroqError('Groq application daily budget exhausted')
    if delay:
        sleep(delay)
    at = max(at, time.time())
    day = datetime.fromtimestamp(at, timezone.utc).date().isoformat()
    key = 'groq:' + model + ':' + day
    state = ledger.setdefault(key, {'requests': 0, 'tokens': 0})
    if state['requests'] >= caps['RPD'] or state['tokens'] + tokens > caps['TPD']:
        raise GroqError('Groq application daily budget exhausted')
    state['requests'] += 1
    state['tokens'] += tokens
    event = {'at': at, 'tokens': tokens}
    ledger['groq_recent_requests'] = [e for e in recent if e['at'] > at - 60] + [event]
    _save(path, ledger)  # Persist before HTTP; a crash must not erase a reservation.
    return path, ledger, key, event


def _retry_delay(headers, fallback):
    value = headers.get('retry-after', '') if headers else ''
    try:
        delay = float(value)
        return max(0, delay) if math.isfinite(delay) else fallback
    except ValueError:
        try:
            return max(0, parsedate_to_datetime(value).timestamp() - time.time())
        except (ValueError, TypeError, OverflowError):
            return fallback


def generate_json(prompt, model=DEFAULT_MODEL, *, attempts=3, opener=urlopen, sleep=time.sleep, schema=None):
    key = os.environ.get('GROQ_API_KEY') or os.environ.get('Grop_ai_API')
    if not key:
        raise GroqError('Groq API key is not configured')
    # A byte bound intentionally overestimates input tokens; output is bounded too.
    reserved = len(prompt.encode('utf-8')) + 1800 + (len(json.dumps(schema, separators=(',', ':')).encode('utf-8')) if schema else 0)
    payload = {'model': model, 'messages': [
        {'role': 'system', 'content': 'Return a valid JSON object only.'},
        {'role': 'user', 'content': prompt}], 'temperature': 0,
        'response_format': {'type': 'json_object'}, 'max_completion_tokens': 1600}
    if model.startswith('openai/gpt-oss-'):
        payload['reasoning_effort'] = 'low'
    if schema is not None:
        payload['response_format'] = {'type': 'json_schema', 'json_schema': {
            'name': 'news_classification', 'strict': True, 'schema': schema}}
    body = json.dumps(payload).encode()
    request = Request('https://api.groq.com/openai/v1/chat/completions', data=body,
                      headers={'Authorization': 'Bearer ' + key, 'Content-Type': 'application/json',
                               'User-Agent': 'JSOSIF/1.0'})
    for attempt in range(attempts):
        path, ledger, slot, reservation = _reserve(model, reserved, sleep)
        try:
            with opener(request, timeout=60) as response:
                payload = json.load(response)
        except HTTPError as exc:
            retry = exc.code in (408, 409, 429) or exc.code >= 500
            delay = _retry_delay(exc.headers, 2 ** (attempt + 1))
            if retry:
                ledger['groq_next_request_at'] = max(ledger.get('groq_next_request_at', 0), time.time() + delay)
                _save(path, ledger)
            if not retry or attempt + 1 == attempts or delay > 120:
                raise GroqError(f'Groq HTTP {exc.code}; check account limits and retry guidance',
                                status=exc.code, provider_code=error_code(exc)) from None
            sleep(delay)
            continue
        except (URLError, TimeoutError, OSError):
            if attempt + 1 == attempts:
                raise GroqError('Groq connection failed') from None
            sleep(2 ** (attempt + 1))
            continue
        except (ValueError, KeyError, IndexError, TypeError):
            raise GroqError('Groq returned an invalid response') from None
        try:
            text = payload.get('choices', [{}])[0].get('message', {}).get('content')
            usage = payload.get('usage', {})
            actual = usage.get('total_tokens')
            if not isinstance(text, str) or not text.strip():
                raise GroqError('Groq returned no usable content')
            safe_usage = {k: usage[k] for k in ('prompt_tokens', 'completion_tokens', 'total_tokens')
                          if type(usage.get(k)) is int and usage[k] >= 0}
        except (AttributeError, KeyError, IndexError, TypeError):
            raise GroqError('Groq returned an invalid response') from None
        if type(actual) is int and actual >= 0:
            ledger[slot]['tokens'] += actual - reserved
            reservation['tokens'] = actual
            # Persistence failures are not transport failures and must not retry HTTP.
            reconcile_usage(path, ledger)
        return {'text': text, 'model': model, 'usage': safe_usage}
    raise GroqError('Groq request failed')
