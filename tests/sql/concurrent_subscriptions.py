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
