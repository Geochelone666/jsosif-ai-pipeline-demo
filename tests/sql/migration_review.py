"""Synthetic migration review checks; run only in a fresh disposable PostgreSQL DB."""
import json
from pathlib import Path
import subprocess

from subscription_migration import prepare_plan, review_sql


def sql(source, *, success=True):
    result = subprocess.run(['psql', '-X', '-A', '-t', '-v', 'ON_ERROR_STOP=1'],
                            input=source, capture_output=True, text=True)
    assert (result.returncode == 0) == success, 'Unexpected synthetic migration outcome: ' + result.stderr
    return result.stdout.strip()


sql("""
do $$ begin
 if not exists(select 1 from pg_roles where rolname='anon') then create role anon; end if;
 if not exists(select 1 from pg_roles where rolname='authenticated') then create role authenticated; end if;
 if not exists(select 1 from pg_roles where rolname='service_role') then create role service_role bypassrls; end if;
end $$;
create schema auth;
create table auth.users(id uuid primary key,email text,email_confirmed_at timestamptz);
create function auth.uid() returns uuid language sql stable as $$
 select nullif(current_setting('request.jwt.claim.sub',true),'')::uuid
$$;
grant usage on schema auth to authenticated;
grant execute on function auth.uid() to authenticated;
""")
for path in sorted(Path('supabase/migrations').glob('*.sql')):
    sql(path.read_text())
sql(Path('supabase/seed_securities.sql').read_text())
sql("""insert into auth.users values
 ('00000000-0000-0000-0000-000000000001','one@example.com',now()),
 ('00000000-0000-0000-0000-000000000002','two@example.com',now());""")
config = {'groups': {'tech': {'name': 'Technology', 'tickers': ['CSCO']}}, 'members': []}
identities = []
for n in (1, 2):
    config['members'].append({'id': f'legacy-{n}', 'name': "Quoted ' \\ $apply_review$ ; -- name",
                             'email': ['one@example.com', 'two@example.com'][n-1],
                             'enabled': False, 'timezone': 'America/Toronto', 'send_time': '09:00',
                             'send_weekday': 1, 'groups': ['tech'], 'tickers': ['CSCO'],
                             'delivery_start_date': '2026-12-01'})
    identities.append({'member_id': f'legacy-{n}', 'user_id': f'00000000-0000-0000-0000-{n:012}',
                       'email': config['members'][-1]['email'], 'approved': n == 1})
plan = prepare_plan(config, identities, 1)
review = review_sql(plan)
sql(review)
assert sql('select count(*) from subscription_private.members;') == '0'
assert sql('select count(*) from subscription_private.approved_members;') == '0'
assert sql('select revision from subscription_private.settings;') == '1'

# Guards fail atomically before import; restored values belong only to this fixture.
for mutation, restoration in [
    ("update auth.users set email_confirmed_at=null", "update auth.users set email_confirmed_at=now()"),
    ("update auth.users set email='mismatch@example.com' where email='one@example.com'",
     "update auth.users set email='one@example.com' where email='mismatch@example.com'"),
    ("update subscription_private.settings set revision=2", "update subscription_private.settings set revision=1"),
    ("delete from subscription_private.securities where ticker='CSCO'", "insert into subscription_private.securities values('CSCO')"),
    ("insert into subscription_private.approved_members(user_id) values('00000000-0000-0000-0000-000000000002')",
     "delete from subscription_private.approved_members where user_id='00000000-0000-0000-0000-000000000002'"),
]:
    sql(mutation); sql(review, success=False); sql(restoration)
    assert sql('select count(*) from subscription_private.members;') == '0'
    assert sql('select revision from subscription_private.settings;') == '1'

# Only the synthetic test changes the last ROLLBACK to COMMIT.
sql(review.removesuffix('rollback;\n') + 'commit;\n')
rows = json.loads(sql("select jsonb_agg(jsonb_build_object('id',member_id,'preferences',preferences) order by member_id) from subscription_private.members;"))
assert [row['id'] for row in rows] == ['legacy-1', 'legacy-2']
assert all(row['preferences']['enabled'] is False for row in rows)
assert rows[0]['preferences']['name'] == config['members'][0]['name']
snapshot = json.loads(sql('select public.subscription_snapshot();'))
assert snapshot['revision'] == '2'
assert [m['id'] for m in snapshot['config']['members']] == ['legacy-1']
assert snapshot['config']['members'][0]['delivery_start_date'] == '2026-12-01'
sql(review, success=False)  # Retry refuses stale revision without replacing preferences.
sql(review_sql(prepare_plan(config, identities, 2)), success=False)  # Even a fresh revision cannot overwrite.
assert sql('select count(*) from subscription_private.members;') == '2'
assert sql('select revision from subscription_private.settings;') == '2'
print('Migration review: rollback default, Auth/catalogue/revision guards, exact legacy IDs, opt-outs and non-overwrite passed')
