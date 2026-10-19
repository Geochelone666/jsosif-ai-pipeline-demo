"""Portable Gemini REST client. Keys stay in headers; errors exclude response bodies."""
import json
import os
import re
import time
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
from urllib.error import HTTPError, URLError
from urllib.request import Request
from credential_http import urlopen


class GeminiError(RuntimeError):
    pass


def quota_day(now=None):
    return (now or datetime.now(ZoneInfo('America/Los_Angeles'))).astimezone(
        ZoneInfo('America/Los_Angeles')).date().isoformat()


def reserve_request(model):
    """Enforce a configured project budget before every attempt, including retries."""
    path = os.environ.get('JSOSIF_API_USAGE_PATH')
    if not path:
        return  # Standalone client can use provider-side quotas.
    from report_store import read_json, write_json
    try:
        rpd = int(os.environ.get('GEMINI_RPD', '0'))
        rpm = int(os.environ.get('GEMINI_RPM', '0'))
    except ValueError:
        raise GeminiError('Configure numeric GEMINI_RPD and GEMINI_RPM') from None
    if rpd < 1 or rpm < 1:
        raise GeminiError('Configure actual project GEMINI_RPD and GEMINI_RPM')
    day = quota_day()
    usage = read_json(Path(path), {})
    key = model + ':' + day
    used = usage.get(key, 0)
    # Leave 20% of published quota for other consumers; this is a local cap.
    if used >= max(1, int(rpd * .8)):
        raise GeminiError('Configured daily request budget exhausted; resume after quota reset')
    last = usage.get('last_request_at', 0)
    time.sleep(max(0, 60 / rpm - (time.time() - last)))
    usage[key] = used + 1
    usage['last_request_at'] = time.time()
    write_json(Path(path), usage)
    if os.environ.get('JSOSIF_PERSIST_API_USAGE') == '1':
        from report_store import persist
        persist(Path(path).resolve().parents[1], git=True)


def generate_json(prompt, model='gemini-3.5-flash-lite', *, attempts=3,
                  opener=urlopen, sleep=time.sleep):
    key = os.environ.get('GEMINI_API_KEY') or os.environ.get('GOOGLE_API_KEY')
    if not key:
        raise GeminiError('Gemini API key is not configured')
    if not re.fullmatch(r'[a-zA-Z0-9._-]+', model):
        raise GeminiError('Invalid Gemini model identifier')
    body = json.dumps({'contents': [{'parts': [{'text': prompt}]}],
                       'generationConfig': {'responseMimeType': 'application/json'}}).encode()
    request = Request(f'https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent',
                      data=body, headers={'Content-Type': 'application/json', 'x-goog-api-key': key})
    for attempt in range(attempts):
        reserve_request(model)
        try:
            with opener(request, timeout=180) as response:
                payload = json.load(response)
            text = ''.join(part.get('text', '') for candidate in payload.get('candidates', [])[:1]
                           for part in candidate.get('content', {}).get('parts', [])
                           if not part.get('thought'))
            if not text:
                raise GeminiError('Gemini returned no usable content')
            return {'text': text, 'model': model, 'usage': payload.get('usageMetadata', {})}
        except HTTPError as exc:
            if exc.code not in (429, 500, 502, 503, 504) or attempt + 1 == attempts:
                raise GeminiError(f'Gemini HTTP {exc.code}') from None
            retry = exc.headers.get('Retry-After', '') if exc.headers else ''
            sleep(min(120, max(2 ** (attempt + 1), int(retry) if retry.isdigit() else 0)))
        except (URLError, TimeoutError, OSError):
            if attempt + 1 == attempts:
                raise GeminiError('Gemini connection failed') from None
            sleep(2 ** (attempt + 1))
    raise GeminiError('Gemini request failed')
