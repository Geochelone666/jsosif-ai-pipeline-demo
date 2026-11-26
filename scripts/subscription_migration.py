"""Prepare an offline, private, rollback-by-default legacy subscription import review."""
import argparse
from copy import deepcopy
import hashlib
import json
import os
from pathlib import Path
import uuid

from subscriptions import import_members_csv, validate

MAX_BYTES = 2 * 1024 * 1024
PREFERENCE_FIELDS = {'name', 'enabled', 'timezone', 'send_weekday', 'send_time',
                     'groups', 'tickers', 'delivery_start_date', 'content_preferences'}
CONTENT_FIELDS = {'sector_brief', 'macro_overview', 'news_catalysts'}


def read_private_json(path):
    with Path(path).open('rb') as stream:
        raw = stream.read(MAX_BYTES + 1)
    if len(raw) > MAX_BYTES:
        raise ValueError('Input exceeds review size limit')
    return json.loads(raw)


def prepare_plan(config, identities, expected_revision):
    """No network or database access. Actual Auth identity is rechecked by SQL."""
    config = deepcopy(validate(config))
    if set(config) - {'groups', 'members', 'allow_degraded', 'max_report_age_days'}:
        raise ValueError('Unsupported policy fields require explicit review')
    if type(expected_revision) is not int or not 1 <= expected_revision < 2**63 - 1:
        raise ValueError('Expected settings revision must be a positive bigint')
    if not config['members'] or len(config['members']) > 10000:
        raise ValueError('Expected a nonempty bounded roster')
    if not isinstance(identities, list) or len(identities) != len(config['members']):
        raise ValueError('Identity map must cover the complete roster exactly once')
    identity_by_id = {}; user_ids = set()
    for item in identities:
        if not isinstance(item, dict) or set(item) != {'member_id', 'user_id', 'email', 'approved'}:
            raise ValueError('Identity entries require member_id, user_id, email and explicit approved boolean')
        member_id, email = item['member_id'], item['email']
        if not isinstance(member_id, str) or not isinstance(email, str) or type(item['approved']) is not bool:
            raise ValueError('Invalid reviewed identity fields')
        try:
            user_id = str(uuid.UUID(item['user_id']))
        except (ValueError, TypeError, AttributeError):
            raise ValueError('Invalid Auth UUID') from None
        if member_id in identity_by_id or user_id in user_ids:
            raise ValueError('Duplicate member or Auth identity')
        identity_by_id[member_id] = dict(item, user_id=user_id)
        user_ids.add(user_id)
    rows = []
    for member in config['members']:
        identity = identity_by_id.pop(member['id'], None)
        if identity is None or identity['email'].lower() != member['email'].lower():
            raise ValueError('Reviewed identity does not match the legacy member')
        # Legacy spreadsheet feedback/scheduling hints have no backend equivalent.
        # Never silently discard a nonempty field or reinterpret prose as booleans.
        if any(value not in ('', None) for key, value in member.items()
               if key not in PREFERENCE_FIELDS | {'id', 'email'}):
            raise ValueError('Unmapped member fields require explicit review')
        preferences = {key: deepcopy(value) for key, value in member.items() if key in PREFERENCE_FIELDS}
        preferences.setdefault('tickers', [])
        if preferences.get('content_preferences') in ('', None):
            preferences.pop('content_preferences', None)
        content = preferences.get('content_preferences', {})
        if (not isinstance(content, dict) or set(content) - CONTENT_FIELDS or
                any(type(value) is not bool for value in content.values())):
            raise ValueError('Content preferences require supported boolean fields')
        if (not 1 <= len(preferences['name'].strip()) <= 200 or
                any(ord(c) < 32 or ord(c) == 127 for c in preferences['name']) or
                len(preferences['groups']) > 20 or len(preferences['tickers']) > 100):
            raise ValueError('Member preferences exceed backend limits')
        rows.append({'member_id': member['id'], 'user_id': identity['user_id'],
                     'expected_email': member['email'], 'approved': identity['approved'],
                     'preferences': preferences})
    if identity_by_id:
        raise ValueError('Identity map includes unknown members')
    policy = {key: deepcopy(value) for key, value in config.items() if key != 'members'}
    policy.setdefault('allow_degraded', False)
    policy.setdefault('max_report_age_days', 4)
    return {'schema_version': 1, 'mode': 'fresh-authority-import-review',
            'expected_revision': expected_revision, 'policy': policy,
            'members': sorted(rows, key=lambda row: row['member_id'])}


def review_sql(plan):
    payload = json.dumps(plan, ensure_ascii=False, sort_keys=True, allow_nan=False)
    # A generated delimiter avoids SQL interpolation, including quotes/backslashes.
    tag = '$migration_' + hashlib.sha256(payload.encode()).hexdigest()[:20] + '$'
    assert tag not in payload
    return """-- PRIVATE REVIEW ONLY. Contains member identities. Never commit or publish.
-- Fresh authority import only, after schema/catalogue migrations and read-only inventory.
-- This script defaults to ROLLBACK. COMMIT requires separately authorized execution.
begin;
set local lock_timeout = '5s';
set local statement_timeout = '30s';
create temporary table migration_review_plan (document jsonb) on commit drop;
insert into migration_review_plan values (""" + tag + payload + tag + """::jsonb);
do $apply_review$
declare
 plan jsonb; member jsonb; policy jsonb; actual_revision bigint;
 identity_email text; confirmed timestamptz; uid uuid;
begin
 select document into strict plan from migration_review_plan;
 select revision into strict actual_revision from subscription_private.settings where singleton for update;
 if actual_revision <> (plan->>'expected_revision')::bigint then
  raise exception 'Settings revision changed; rebuild the reviewed plan';
 end if;
 -- Block all member writes while checking fresh-install preconditions.
 lock table subscription_private.members in share row exclusive mode;
 lock table subscription_private.approved_members in share row exclusive mode;
 if exists(select 1 from subscription_private.members) or
    exists(select 1 from subscription_private.requests) or
    exists(select 1 from subscription_private.security_requests) then
  raise exception 'Authority is already in use; fresh import refused';
 end if;
 if exists(select 1 from subscription_private.approved_members a where not exists(
     select 1 from jsonb_array_elements(plan->'members') m
     where (m->>'user_id')::uuid=a.user_id and (m->>'approved')::boolean)) then
  raise exception 'Existing approvals conflict with the reviewed map';
 end if;
 policy := plan->'policy';
 if exists(select 1 from jsonb_each(policy->'groups') g,
     jsonb_array_elements_text(g.value->'tickers') t
     where not exists(select 1 from subscription_private.securities s where s.ticker=t.value)) then
  raise exception 'Reviewed group includes an inactive security';
 end if;
 -- Recheck actual Auth rows; offline mapping alone is never verification evidence.
 for member in select value from jsonb_array_elements(plan->'members') loop
  uid := (member->>'user_id')::uuid;
  select email, email_confirmed_at into identity_email, confirmed from auth.users where id=uid for share;
  if not found or confirmed is null or identity_email is null or
     lower(identity_email) <> lower(member->>'expected_email') then
   raise exception 'Verified Auth identity does not match the reviewed map';
  end if;
  if exists(select 1 from jsonb_array_elements_text(member->'preferences'->'tickers') t
       where not exists(select 1 from subscription_private.securities s where s.ticker=t.value)) then
   raise exception 'Reviewed member includes an inactive security';
  end if;
 end loop;
 update subscription_private.settings set config=policy,revision=revision+1 where singleton;
 for member in select value from jsonb_array_elements(plan->'members') loop
  uid := (member->>'user_id')::uuid;
  if (member->>'approved')::boolean then
   insert into subscription_private.approved_members(user_id) values(uid) on conflict(user_id) do nothing;
  end if;
  insert into subscription_private.members(user_id,member_id,version,preferences)
   values(uid,member->>'member_id',1,member->'preferences');
 end loop;
end $apply_review$;
-- Counts only: do not print private preferences, identities or service snapshots.
select count(*) as imported_members,
       count(*) filter(where (preferences->>'enabled')::boolean) as participating_members
from subscription_private.members;
rollback;
"""


def write_review(path, sql):
    """New file only; refuse overwrite/symlinks, and set owner-only permissions."""
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, 'w', encoding='utf-8') as stream:
        stream.write(sql)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, required=True, help='Private legacy JSON configuration')
    parser.add_argument('--members-csv', type=Path, help='Optional legacy CSV, overriding the JSON roster')
    parser.add_argument('--identities', type=Path, required=True, help='Reviewed legacy member/Auth UUID map')
    parser.add_argument('--expected-revision', type=int, required=True)
    parser.add_argument('--output', type=Path, required=True, help='New private SQL review file; never executed')
    args = parser.parse_args()
    try:
        config = read_private_json(args.config)
        if args.members_csv:
            with args.members_csv.open('rb') as stream:
                raw = stream.read(MAX_BYTES + 1)
            if len(raw) > MAX_BYTES:
                raise ValueError('CSV exceeds limit')
            config = import_members_csv(config, raw.decode('utf-8-sig'))
        plan = prepare_plan(config, read_private_json(args.identities), args.expected_revision)
        sql = review_sql(plan)
        write_review(args.output, sql)
    except (ValueError, TypeError, KeyError, OSError):
        parser.error('Review generation failed: check private input schemas, mapping, revision and a new output path')
    print(f'Private rollback-only review created: {len(plan["members"])} members; no database connection made')


if __name__ == '__main__':
    main()
