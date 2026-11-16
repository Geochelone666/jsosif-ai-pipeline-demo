"""Private administrator inspect -> offline review -> explicit apply workflow."""
import argparse
import json
import os
from pathlib import Path
import re
import uuid
from urllib.error import URLError
from urllib.request import Request

from credential_http import urlopen
from subscription_migration import PREFERENCE_FIELDS, read_private_json, write_review

MAX_BYTES = 2 * 1024 * 1024
RPC = 'correct_admin_subscription'


def project_url(value):
    if not isinstance(value, str) or not re.fullmatch(r'https://[a-z0-9-]+\.supabase\.co', value):
        raise ValueError('Invalid project URL')
    return value


def identifier(value):
    if not isinstance(value, str) or str(uuid.UUID(value)) != value:
        raise ValueError('Expected a canonical UUID')
    return value


def rpc(name, arguments, *, opener=None, env=None):
    env = os.environ if env is None else env
    base = project_url(env.get('SUBSCRIPTIONS_SUPABASE_URL'))
    key = env.get('SUBSCRIPTIONS_PUBLISHABLE_KEY', '')
    token = env.get('SUBSCRIPTIONS_ADMIN_TOKEN', '')
    if not re.fullmatch(r'sb_publishable_[A-Za-z0-9_-]+', key) or not token or any(c.isspace() for c in token):
        raise ValueError('Verified administrator session and publishable configuration required')
    if name not in ('get_admin_subscription', 'get_admin_subscription_history', RPC):
        raise ValueError('Unknown administrator operation')
    request = Request(base + '/rest/v1/rpc/' + name,
                      data=json.dumps(arguments, allow_nan=False).encode(), method='POST',
                      headers={'apikey': key, 'Authorization': 'Bearer ' + token,
                               'Content-Type': 'application/json'})
    try:
        with (opener or urlopen)(request, timeout=20) as response:
            raw = response.read(MAX_BYTES + 1)
        if len(raw) > MAX_BYTES:
            raise ValueError('Response exceeds limit')
        return json.loads(raw)
    except (OSError, URLError, ValueError):
        raise ValueError('Administrator request failed; no success confirmed') from None


def inspect_account(user_id, *, call=rpc, env=None):
    env = os.environ if env is None else env
    identifier(user_id)
    current = call('get_admin_subscription', {'p_user_id': user_id})
    if (not isinstance(current, dict) or current.get('user_id') != user_id or
            type(current.get('version')) is not int or current['version'] < 0 or
            type(current.get('approved')) is not bool):
        raise ValueError('Invalid inspection')
    identifier(current.get('operator_id'))
    history = call('get_admin_subscription_history', {'p_user_id': user_id})
    if not isinstance(history, list) or len(history) > 50:
        raise ValueError('Invalid review history')
    return {'schema_version': 1, 'project_url': project_url(env.get('SUBSCRIPTIONS_SUPABASE_URL')),
            'subscription': current, 'recent_history': history}


def prepare(inspection, *, preferences=None, approval='keep', reason):
    if (not isinstance(inspection, dict) or type(inspection.get('schema_version')) is not int or
            inspection['schema_version'] != 1):
        raise ValueError('Invalid inspection schema')
    current = inspection['subscription']
    if approval not in ('keep', 'approve', 'revoke') or type(current.get('approved')) is not bool:
        raise ValueError('Explicit approval state required')
    approved = current['approved'] if approval == 'keep' else approval == 'approve'
    if preferences is not None and (not isinstance(preferences, dict) or set(preferences) - PREFERENCE_FIELDS):
        raise ValueError('Only supported preferences may be corrected')
    if preferences is None and approved == current['approved']:
        raise ValueError('No correction requested')
    plan = {'schema_version': 1, 'project_url': inspection['project_url'], 'rpc': RPC,
            'arguments': {'p_user_id': current['user_id'], 'p_preferences': preferences,
                          'p_approved': approved, 'p_expected_version': current['version'],
                          'p_expected_approved': current['approved'], 'p_request_id': str(uuid.uuid4()),
                          'p_reason': reason.strip(), 'p_expected_actor': current['operator_id']}}
    validate_plan(plan)
    return plan


def validate_plan(plan):
    if (not isinstance(plan, dict) or set(plan) != {'schema_version', 'project_url', 'rpc', 'arguments'} or
            type(plan['schema_version']) is not int or plan['schema_version'] != 1 or plan['rpc'] != RPC):
        raise ValueError('Invalid administrator review plan')
    project_url(plan['project_url'])
    args = plan['arguments']
    if not isinstance(args, dict) or set(args) != {'p_user_id', 'p_preferences', 'p_approved',
            'p_expected_version', 'p_expected_approved', 'p_request_id', 'p_reason', 'p_expected_actor'}:
        raise ValueError('Invalid correction fields')
    for key in ('p_user_id', 'p_expected_actor', 'p_request_id'):
        identifier(args[key])
    if (type(args['p_expected_version']) is not int or not 0 <= args['p_expected_version'] < 2**63-1 or
            type(args['p_approved']) is not bool or type(args['p_expected_approved']) is not bool or
            not isinstance(args['p_reason'], str) or not 1 <= len(args['p_reason'].strip()) <= 1000 or
            any(ord(c) < 32 or ord(c) == 127 for c in args['p_reason'])):
        raise ValueError('Invalid expected state or reason')
    prefs = args['p_preferences']
    if prefs is not None and (not isinstance(prefs, dict) or set(prefs) - PREFERENCE_FIELDS):
        raise ValueError('Invalid preference fields')
    return plan


def apply(plan, receipt, *, call=rpc, env=None):
    env = os.environ if env is None else env
    validate_plan(plan)
    if project_url(env.get('SUBSCRIPTIONS_SUPABASE_URL')) != plan['project_url']:
        raise ValueError('Review belongs to another project')
    args = plan['arguments']
    # Reserve a private receipt before dispatch. An interruption/lost response
    # leaves an explicit unconfirmed record and the original retry plan intact.
    fd = os.open(receipt, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, 'w', encoding='utf-8') as stream:
        json.dump({'status': 'unconfirmed', 'request_id': args['p_request_id']}, stream)
        stream.flush(); os.fsync(stream.fileno())
        result = call(RPC, args)
        if (not isinstance(result, dict) or result.get('request_id') != args['p_request_id'] or
                result.get('user_id') != args['p_user_id'] or result.get('operator_id') != args['p_expected_actor'] or
                type(result.get('version')) is not int or result['version'] < args['p_expected_version'] or
                result.get('approved') is not args['p_approved']):
            raise ValueError('Invalid correction response; no success confirmed')
        stream.seek(0); stream.truncate()
        json.dump({'status': 'confirmed', 'result': result}, stream, ensure_ascii=False, indent=2)
        stream.write('\n'); stream.flush(); os.fsync(stream.fileno())
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    inspect = sub.add_parser('inspect', help='Read one target and up to 50 private audit events')
    inspect.add_argument('--user-id', required=True); inspect.add_argument('--output', type=Path, required=True)
    review = sub.add_parser('prepare', help='Generate a private review plan offline; no network or mutation')
    review.add_argument('--inspection', type=Path, required=True)
    review.add_argument('--preferences', type=Path)
    review.add_argument('--approval', choices=('keep', 'approve', 'revoke'), default='keep')
    review.add_argument('--reason-file', type=Path, required=True)
    review.add_argument('--output', type=Path, required=True)
    execute = sub.add_parser('apply', help='Execute exactly one explicitly authorized reviewed plan')
    execute.add_argument('--plan', type=Path, required=True)
    execute.add_argument('--receipt', type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.command == 'inspect':
            write_review(args.output, json.dumps(inspect_account(args.user_id), ensure_ascii=False, indent=2)+'\n')
        elif args.command == 'prepare':
            with args.reason_file.open('rb') as stream:
                raw = stream.read(4097)
            if len(raw) > 4096:
                raise ValueError('Reason exceeds limit')
            plan = prepare(read_private_json(args.inspection),
                           preferences=read_private_json(args.preferences) if args.preferences else None,
                           approval=args.approval, reason=raw.decode('utf-8'))
            write_review(args.output, json.dumps(plan, ensure_ascii=False, indent=2)+'\n')
        else:
            apply(read_private_json(args.plan), args.receipt)
    except (ValueError, TypeError, KeyError, OSError, AttributeError):
        parser.error('Operation failed; no success confirmed. Keep the original plan and retry its same request ID if the outcome is uncertain. Check private inputs and authorization without publishing them.')
    print('Private administrator '+args.command+' completed; output saved locally')


if __name__ == '__main__':
    main()
