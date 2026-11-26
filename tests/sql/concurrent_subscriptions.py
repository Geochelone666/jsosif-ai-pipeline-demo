"""Run after subscription_authority.sql, on the same disposable test database."""
from concurrent.futures import ThreadPoolExecutor
import subprocess
import uuid


def update(_):
    sql = f"""
    set role authenticated;
    select set_config('request.jwt.claim.sub','00000000-0000-0000-0000-000000000001',false);
    select public.save_my_subscription(public.get_my_subscription()->'preferences',3,'{uuid.uuid4()}');
    """
    return subprocess.run(['psql', '-X', '-v', 'ON_ERROR_STOP=1'], input=sql, text=True, capture_output=True)


with ThreadPoolExecutor(max_workers=2) as executor:
    results = list(executor.map(update, range(2)))
assert sum(result.returncode == 0 for result in results) == 1, 'Expected exactly one accepted update'
assert any('Subscription version conflict' in result.stderr for result in results), 'Expected explicit conflict'
print('Concurrent updates: one committed, one stale writer rejected')


def security_request(ticker):
    sql = f"""
    set role authenticated;
    select set_config('request.jwt.claim.sub','00000000-0000-0000-0000-000000000001',false);
    select public.request_security('{ticker}','XNAS','Concurrent request');
    """
    return subprocess.run(['psql', '-X', '-v', 'ON_ERROR_STOP=1'], input=sql, text=True, capture_output=True)


# SQL fixture leaves 19 open requests. Two simultaneous new listings must not
# both consume the last slot; retries of the winner remain available at capacity.
with ThreadPoolExecutor(max_workers=2) as executor:
    results = list(executor.map(security_request, ['RACEA', 'RACEB']))
assert sum(result.returncode == 0 for result in results) == 1, 'Outstanding quota raced'
assert any('At most 20 outstanding requests' in result.stderr for result in results)
winner = ['RACEA', 'RACEB'][next(i for i, result in enumerate(results) if result.returncode == 0)]
with ThreadPoolExecutor(max_workers=2) as executor:
    results = list(executor.map(security_request, [winner, winner]))
assert all(result.returncode == 0 for result in results), 'Duplicate retry failed at capacity'
assert results[0].stdout == results[1].stdout, 'Concurrent retries returned different identities'
print('Concurrent security requests: quota preserved; duplicate retries keep one identity')
