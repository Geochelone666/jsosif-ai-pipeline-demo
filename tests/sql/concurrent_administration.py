"""Run after subscription_authority.sql and concurrent_subscriptions.py in a disposable DB."""
from concurrent.futures import ThreadPoolExecutor
import json
import os
import subprocess
import time
import uuid

USER='00000000-0000-0000-0000-000000000001'
ADMIN='00000000-0000-0000-0000-000000000004'
CMD=['psql','-X','-q','-A','-t','-v','ON_ERROR_STOP=1']


def run(source, *, success=None):
    result=subprocess.run(CMD,input=source,text=True,capture_output=True,timeout=15)
    if success is not None:assert (result.returncode==0)==success,result.stderr
    return result


def scalar(source):return run(source,success=True).stdout.strip()


def as_user(user,source):
    return f"set role authenticated;select set_config('request.jwt.claim.sub','{user}',false);"+source


def admin_change(version,send_time,request_id,approved=True):
    prefs=f"(select preferences||'{{\"send_time\":\"{send_time}\"}}'::jsonb from subscription_private.members where user_id='{USER}')"
    # Preferences for the synthetic test are captured with the fixture operator,
    # then passed as a literal by the authenticated administrator.
    value=scalar('select '+prefs+';') if send_time else 'null'
    argument="'"+value.replace("'","''")+"'::jsonb" if send_time else 'null'
    return as_user(ADMIN,f"select public.correct_admin_subscription('{USER}',{argument},{str(approved).lower()},{version},true,'{request_id}','Concurrent correction','{ADMIN}');")


run(f"insert into auth.users values('{ADMIN}','admin@example.com',now());insert into subscription_private.administrators(user_id) values('{ADMIN}');",success=True)
version=int(scalar(f"select version from subscription_private.members where user_id='{USER}'"))
sources=[admin_change(version,'10:00',str(uuid.uuid4())) for _ in range(2)]
with ThreadPoolExecutor(max_workers=2) as pool:results=list(pool.map(run,sources))
assert sum(r.returncode==0 for r in results)==1,'Competing administrators both overwrote the member'
assert any('Member state changed' in r.stderr for r in results)
assert scalar('select count(*) from subscription_private.administration_changes')=='1'
version+=1
same=admin_change(version,'11:00',str(uuid.uuid4()))
with ThreadPoolExecutor(max_workers=2) as pool:results=list(pool.map(run,[same,same]))
assert all(r.returncode==0 for r in results) and results[0].stdout==results[1].stdout
assert scalar('select count(*) from subscription_private.administration_changes')=='2'
version+=1
prefs=json.loads(scalar(f"select preferences from subscription_private.members where user_id='{USER}'"))
prefs['send_time']='13:00'
literal=json.dumps(prefs).replace("'","''")
member=as_user(USER,f"select public.save_my_subscription('{literal}',{version},'{uuid.uuid4()}');")
with ThreadPoolExecutor(max_workers=2) as pool:
    results=list(pool.map(run,[admin_change(version,'12:00',str(uuid.uuid4())),member]))
assert sum(r.returncode==0 for r in results)==1,'Member/admin version check raced'
version+=1
assert int(scalar(f"select version from subscription_private.members where user_id='{USER}'"))==version

# Force a member save to pass its initial approval check, then wait on the shared
# settings lock while an administrator revokes approval in the holding transaction.
holder=subprocess.Popen(CMD,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,bufsize=1)
pending=None
retry=None
try:
    holder.stdin.write("begin;set local statement_timeout='10s';do $$ begin perform 1 from subscription_private.settings where singleton for update;end $$;select 'READY';\n")
    holder.stdin.flush()
    assert holder.stdout.readline().strip()=='READY'
    pending=subprocess.Popen(CMD,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,
                             env={**os.environ,'PGAPPNAME':'synthetic-queued-member'})
    pending.stdin.write(as_user(USER,f"select public.save_my_subscription('{literal}',{version},'{uuid.uuid4()}');")+'\n')
    pending.stdin.close();pending.stdin=None
    original={'name':'Example','enabled':True,'timezone':'America/Toronto','send_weekday':1,
              'send_time':'09:00','groups':[],'tickers':['CSCO']}
    original_json=json.dumps(original)
    retry=subprocess.Popen(CMD,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,
                           env={**os.environ,'PGAPPNAME':'synthetic-queued-member-retry'})
    retry.stdin.write(as_user(USER,f"select public.save_my_subscription('{original_json}',0,'10000000-0000-0000-0000-000000000001');")+'\n')
    retry.stdin.close();retry.stdin=None
    deadline=time.monotonic()+5
    while time.monotonic()<deadline:
        waiting=scalar("select count(*) from pg_stat_activity where application_name like 'synthetic-queued-member%' and wait_event_type='Lock'")
        if waiting=='2':break
        time.sleep(.02)
    else:raise AssertionError('Member did not wait on the shared settings lock')
    revoke=as_user(ADMIN,f"select public.correct_admin_subscription('{USER}',null,false,{version},true,'{uuid.uuid4()}','Revoke while member waits','{ADMIN}');")
    holder.stdin.write(revoke+'commit;\n');holder.stdin.close();holder.stdin=None
    holder_out,holder_error=holder.communicate(timeout=10)
    assert holder.returncode==0,holder_error
    for process in (pending,retry):
        out,error=process.communicate(timeout=10)
        assert process.returncode!=0 and 'team approval required' in error.lower(),error
    assert int(scalar(f"select version from subscription_private.members where user_id='{USER}'"))==version+1
    assert scalar(f"select count(*) from subscription_private.approved_members where user_id='{USER}'")=='0'
    assert scalar(f"select member_id from subscription_private.members where user_id='{USER}'")=='legacy-member-001'
finally:
    for process in (holder,pending,retry):
        if process is not None and process.poll() is None:
            process.kill();process.communicate()
print('Concurrent administration: one writer wins; exact retry has one audit event; queued member save and replay denied after revocation')
