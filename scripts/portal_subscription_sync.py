"""Safely stage confirmed website subscribers for a *reviewed* roster sync.

This is deliberately not called by production workflows. The public website
must first pass identity, consent, durable-store and ticker freshness acceptance.
Private data stays in the runner's temporary files; never commit it to Git.
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from copy import deepcopy
from pathlib import Path

from subscriptions import import_members_csv, validate, write_private_config
from universe import SUPPORTED

OFFICIAL_EXPORT = 'https://www.jsosif.com/api/portal/export'
MAX_EXPORT_BYTES = 2_000_000
MAX_SUBSCRIBERS = 2000
REQUIRED = ('id', 'name', 'email', 'timezone', 'send_time')


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    """Do not forward the private export token to another hostname."""

    def redirect_request(self, request, fp, code, msg, headers, newurl):
        return None


def fetch_export(url, token, timeout=20):
    if url != OFFICIAL_EXPORT:
        raise ValueError('Portal export must use the verified official HTTPS endpoint')
    if not isinstance(token, str) or not token:
        raise ValueError('Portal export token is missing')
    request = urllib.request.Request(url, headers={'X-Portal-Export-Token': token})
    opener = urllib.request.build_opener(_NoRedirect())
    try:
        with opener.open(request, timeout=timeout) as response:
            if response.status != 200:
                raise ValueError('Portal export did not return HTTP 200')
            payload = response.read(MAX_EXPORT_BYTES + 1)
    except (urllib.error.URLError, OSError) as exc:
        raise ValueError('Secure portal export failed; inspect the server without printing the token') from None
    if len(payload) > MAX_EXPORT_BYTES:
        raise ValueError('Portal export exceeds size limit')
    try:
        result = json.loads(payload.decode('utf-8'))
    except (ValueError, UnicodeError):
        raise ValueError('Portal export must be valid UTF-8 JSON') from None
    if not isinstance(result, dict) or not isinstance(result.get('members'), list):
        raise ValueError('Portal export is missing its members list')
    if len(result['members']) > MAX_SUBSCRIBERS:
        raise ValueError('Portal export exceeds subscriber limit')
    return result


def normalize_member(member, supported=None):
    supported = set(SUPPORTED if supported is None else supported)
    if not isinstance(member, dict):
        raise ValueError('Invalid portal member record')
    for field in REQUIRED:
        if not isinstance(member.get(field), str) or not member[field].strip():
            raise ValueError(f'Invalid portal member field: {field}')
    if not member['id'].startswith('portal-'):
        raise ValueError('Portal member needs a stable portal-prefixed ID')
    if type(member.get('enabled')) is not bool:
        raise ValueError('Portal member enabled must be a boolean')
    if type(member.get('send_weekday')) is not int or not 0 <= member['send_weekday'] <= 6:
        raise ValueError('Portal weekday must be an integer from 0 to 6')
    requested = member.get('tickers')
    if not isinstance(requested, list) or any(not isinstance(t, str) or not t.strip() for t in requested):
        raise ValueError('Portal tickers must be a list of nonempty strings')
    requested = list(dict.fromkeys(t.strip().upper() for t in requested))
    accepted = [t for t in requested if t in supported]
    return ({
        'id': member['id'], 'name': member['name'], 'email': member['email'],
        'groups': [], 'tickers': accepted,
        'enabled': member['enabled'], 'timezone': member['timezone'],
        'send_weekday': member['send_weekday'], 'send_time': member['send_time'],
    }, len(requested) - len(accepted))


def merge(existing_config, portal_members, *, supported=None):
    """Return a validated new configuration, or fail without modifying input.

    - Do not overwrite manual member data on an email collision.
    - Only a *matching stable portal ID* is allowed to update portal settings.
    - A subscriber with no currently supported ticker is kept pending, not
      silently turned into an invalid active group.
    """
    base = validate(deepcopy(existing_config))
    members = list(base['members'])
    by_email = {m['email'].casefold(): m for m in members}
    by_id = {m['id']: m for m in members}
    accepted = 0
    pending = 0
    unsupported = 0
    seen_email = set()
    for record in portal_members:
        member, dropped = normalize_member(record, supported)
        key = member['email'].casefold()
        if key in seen_email:
            raise ValueError('Duplicate email addresses in portal export')
        seen_email.add(key)
        unsupported += dropped
        old = by_email.get(key)
        if not member['tickers']:
            if old:
                raise ValueError('An existing portal subscription has no supported ticker; review required')
            pending += 1
            continue
        id_owner = by_id.get(member['id'])
        if old and (not old['id'].startswith('portal-') or old['id'] != member['id']):
            raise ValueError('Portal and privately managed member identities conflict')
        if id_owner and id_owner['email'].casefold() != key:
            raise ValueError('Portal member ID belongs to a different email')
        if old:
            members[members.index(old)] = member
        else:
            members.append(member)
        by_email[key] = member
        by_id[member['id']] = member
        accepted += 1
    base['members'] = members
    return validate(base), {'accepted': accepted, 'pending': pending, 'unsupported_tickers': unsupported}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', type=Path, help='Private output outside the public repository')
    parser.add_argument('--url', default=OFFICIAL_EXPORT)
    args = parser.parse_args(argv)
    token = os.environ.get('SUBSCRIPTION_PORTAL_EXPORT_TOKEN', '')
    if not token:
        parser.error('Missing portal export token')
    try:
        export = fetch_export(args.url, token)
        raw_json = os.environ.get('SUBSCRIPTIONS_JSON', '').strip()
        raw_csv = os.environ.get('MEMBERS_CSV', '').strip()
        existing = json.loads(raw_json) if raw_json else {'groups': {}, 'members': []}
        if raw_csv:
            existing = import_members_csv(existing, raw_csv)
        staged, counts = merge(existing, export['members'])
        write_private_config(args.output, staged)
    except (ValueError, OSError, TypeError):
        print('Portal sync staging failed; no private roster was replaced', file=sys.stderr)
        raise SystemExit(2) from None
    print(f"Staged {counts['accepted']} portal member(s); "
          f"{counts['pending']} awaiting a supported ticker; "
          f"{counts['unsupported_tickers']} unsupported symbol request(s). "
          'No production secrets or member email addresses were changed.')


if __name__ == '__main__':
    main()
