"""Fail-closed, authenticated access to the team's Supabase subscription snapshot."""
from datetime import datetime, timezone
import hashlib
import json
import os
import re
from urllib.error import URLError
from urllib.request import Request

from credential_http import urlopen
from subscriptions import validate

MAX_BYTES = 2 * 1024 * 1024


def fingerprint(config):
    return hashlib.sha256(json.dumps(config, sort_keys=True, separators=(',', ':'),
                                     ensure_ascii=False, allow_nan=False).encode()).hexdigest()


def fetch_snapshot(*, opener=None, now=None):
    base = os.environ.get('SUBSCRIPTIONS_SUPABASE_URL', '').rstrip('/')
    key = os.environ.get('SUBSCRIPTIONS_SERVICE_KEY', '')
    if not re.fullmatch(r'https://[a-z0-9-]+\.supabase\.co', base) or not key:
        raise ValueError('Configure the subscription authority URL and server credential')
    request = Request(base + '/rest/v1/rpc/subscription_snapshot', data=b'{}',
                      headers={'apikey': key, 'Authorization': 'Bearer ' + key,
                               'Content-Type': 'application/json'}, method='POST')
    try:
        with (opener or urlopen)(request, timeout=20) as response:
            raw = response.read(MAX_BYTES + 1)
        if len(raw) > MAX_BYTES:
            raise ValueError('Snapshot exceeds size limit')
        envelope = json.loads(raw)
        if (type(envelope.get('schema_version')) is not int or envelope['schema_version'] != 1 or
                not isinstance(envelope.get('revision'), str) or
                not re.fullmatch(r'[1-9][0-9]*', envelope['revision'])):
            raise ValueError('Invalid snapshot schema')
        generated = datetime.fromisoformat(envelope['generated_at'].replace('Z', '+00:00'))
        now = now or datetime.now(timezone.utc)
        if generated.tzinfo is None or not -30 <= (now - generated).total_seconds() <= 300:
            raise ValueError('Snapshot timestamp is stale or invalid')
        config = validate(envelope['config'])
        if '_subscription_authority' in config:
            raise ValueError('Reserved authority metadata')
        digest = fingerprint(config)
    except (OSError, URLError, ValueError, KeyError, TypeError, AttributeError):
        # Neither provider response bodies nor member values belong in logs.
        raise ValueError('Subscription authority unavailable or snapshot invalid; delivery blocked') from None
    return dict(config, _subscription_authority={
        'revision': envelope['revision'], 'sha256': digest, 'generated_at': envelope['generated_at']})


def assert_current(config):
    """Check immediately before reservation; changes require a fresh sender run.

    This cannot retract a submission already in flight. No stale fallback is used.
    """
    metadata = config.get('_subscription_authority')
    if not metadata:
        if os.environ.get('SUBSCRIPTIONS_BACKEND', 'legacy') == 'supabase':
            raise ValueError('Sender requires an authoritative subscription snapshot')
        return
    original = {k: v for k, v in config.items() if k != '_subscription_authority'}
    if not isinstance(metadata, dict) or metadata.get('sha256') != fingerprint(original):
        raise ValueError('Subscription snapshot was modified')
    current = fetch_snapshot()['_subscription_authority']
    if any(metadata.get(k) != current[k] for k in ('revision', 'sha256')):
        raise ValueError('Subscriptions changed; reload before sending')
