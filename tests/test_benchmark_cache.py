from datetime import datetime, timedelta, timezone
import json
import multiprocessing
import os
from pathlib import Path
import sqlite3
import sys
import time

import pytest

import benchmark_cache as cache
import benchmark_prices as prices
from shared_research_pack import canonical, digest

NOW = datetime(2025,10,10,12,tzinfo=timezone.utc)
START,END = '2025-10-01','2025-10-08'


def provider(symbol,start,end):
    return dict(symbol=symbol,currency='USD',exchange_timezone='America/New_York',exchange_name='SYNTHETIC',
                instrument_type='ETF' if symbol=='XLK' else 'EQUITY',provider_version='synthetic-test',
                observations=[dict(observed_on=start,value=100),dict(observed_on=end,value=105)])


def collect(root,symbols=('CSCO','XLK'),**kwargs):
    return cache.collect(list(symbols),start=START,end=END,cache_dir=root,
                         **dict(dict(fetcher=provider,clock=lambda:NOW,daily_limit=4),**kwargs))


def state(root,sql,args=()):
    with sqlite3.connect(root/'state.sqlite3') as db:
        return db.execute(sql,args).fetchall()


def test_same_batch_reuses_exact_evidence_and_never_updates_retrieval_time(tmp_path):
    calls=[]
    def fetch(s,a,b): calls.append(s); return provider(s,a,b)
    root=tmp_path/'cache'
    first,a=collect(root,fetcher=fetch)
    second,b=collect(root,('XLK','CSCO','CSCO'),fetcher=fetch,clock=lambda:NOW+timedelta(seconds=30))
    assert calls==['CSCO','XLK'] and first==second
    assert a['reserved_units']==2 and b['reserved_units']==0 and b['cache_hit']
    assert a['daily_reserved_units']==b['daily_reserved_units']==2
    assert b['accessed_at']!=second['finished_at']
    assert (root.stat().st_mode&0o777)==0o700
    assert ((root/'state.sqlite3').stat().st_mode&0o777)==0o600


def test_daily_quota_is_shared_across_keys_and_cannot_be_increased_by_caller(tmp_path):
    root=tmp_path/'cache'; collect(root,daily_limit=2)
    with pytest.raises(cache.BudgetExceeded): collect(root,('JPM',),daily_limit=2)
    with pytest.raises(cache.CacheError,match='policy'): collect(root,daily_limit=3)
    assert state(root,'SELECT SUM(units) FROM attempts')==[(2,)]
    assert collect(root,daily_limit=2)[1]['cache_hit']


@pytest.mark.parametrize('seconds,hit',[(3599,True),(3600,False)])
def test_positive_expiry_boundary(tmp_path,seconds,hit):
    root=tmp_path/'cache'; original,_=collect(root)
    value,receipt=collect(root,clock=lambda:NOW+timedelta(seconds=seconds))
    assert receipt['cache_hit'] is hit
    assert (value['capture_id']==original['capture_id']) is hit
    assert receipt['daily_reserved_units']==(2 if hit else 4)


@pytest.mark.parametrize('mode',['exception','missing','incomplete','invalid'])
def test_negative_cache_prevents_failure_retry_storm_and_keeps_good_series(tmp_path,mode):
    calls=[]
    def fetch(s,a,b):
        calls.append(s); raw=provider(s,a,b)
        if s=='CSCO':
            if mode=='exception': raise ValueError('PRIVATE=must-not-persist')
            if mode=='missing': raw['observations']=[]
            if mode=='incomplete': raw['observations'].pop()
            if mode=='invalid': raw['currency']='BAD-CURRENCY'
        return raw
    root=tmp_path/'cache'; first,a=collect(root,fetcher=fetch)
    second,b=collect(root,fetcher=fetch,clock=lambda:NOW+timedelta(seconds=299))
    assert first==second and b['cache_hit'] and a['ttl_seconds']==300
    assert first['series'][1]['status']=='observed' and calls==['CSCO','XLK']
    assert 'PRIVATE' not in (root/'state.sqlite3').read_bytes().decode('latin1')
    _,c=collect(root,fetcher=fetch,clock=lambda:NOW+timedelta(seconds=300))
    assert not c['cache_hit'] and c['daily_reserved_units']==4 and len(calls)==4


def test_new_utc_day_has_own_quota_and_retains_prior_reservations(tmp_path):
    root=tmp_path/'cache'; collect(root,daily_limit=2)
    _,receipt=collect(root,daily_limit=2,clock=lambda:NOW+timedelta(days=1))
    assert receipt['daily_reserved_units']==2
    assert state(root,'SELECT day,SUM(units) FROM attempts GROUP BY day ORDER BY day')==[('2025-10-10',2),('2025-10-11',2)]
    with pytest.raises(cache.CacheError,match='backwards'): collect(root,daily_limit=2)


@pytest.mark.parametrize('change',['symbols','window','contract','version','mode'])
def test_cache_identity_separates_semantically_different_requests(change,monkeypatch):
    first=cache.request_identity(['CSCO','XLK'],START,END,False)
    symbols,start,end,injected=['CSCO','XLK'],START,END,False
    if change=='symbols': symbols=['CSCO']
    if change=='window': start='2025-10-02'
    if change=='contract': monkeypatch.setattr(cache,'ADAPTER_CONTRACT','next-contract')
    if change=='version': monkeypatch.setattr(cache,'version',lambda _: 'new-provider-version')
    if change=='mode': injected=True
    assert digest(first)!=digest(cache.request_identity(symbols,start,end,injected))


@pytest.mark.parametrize('damage',['json','identity','hash','oversize','reference','rehash_window'])
def test_invalid_entry_recovers_only_by_spending_new_budget(tmp_path,damage):
    root=tmp_path/'cache'; collect(root)
    if damage=='json': state(root,'UPDATE entries SET capture=?',('{',))
    if damage=='identity': state(root,'UPDATE entries SET identity=?',('{}',))
    if damage=='oversize': state(root,'UPDATE entries SET capture=?',(' '* (prices.MAX_BYTES+1),))
    if damage=='reference': state(root,'UPDATE entries SET attempt_id=?',('unbound',))
    if damage in ('hash','rehash_window'):
        value=json.loads(state(root,'SELECT capture FROM entries')[0][0]); value['start']='2025-09-30'
        if damage=='rehash_window': value['capture_id']=digest({k:v for k,v in value.items() if k!='capture_id'})
        state(root,'UPDATE entries SET capture=?',(canonical(value),))
    _,receipt=collect(root)
    assert not receipt['cache_hit'] and receipt['daily_reserved_units']==4
    assert state(root,'SELECT COUNT(*) FROM attempts')==[(2,)]


def test_corrupt_entry_at_exhausted_budget_never_triggers_provider(tmp_path):
    root=tmp_path/'cache'; collect(root,daily_limit=2)
    state(root,'UPDATE entries SET capture=?',('{',))
    calls=[]
    with pytest.raises(cache.BudgetExceeded): collect(root,daily_limit=2,fetcher=lambda *args:calls.append(args))
    assert calls==[] and state(root,'SELECT SUM(units) FROM attempts')==[(2,)]


@pytest.mark.parametrize('damage',['missing_file','garbage','empty_file','missing_settings','missing_attempts','wrong_version'])
def test_budget_corruption_fails_closed_without_reset(tmp_path,damage):
    root=tmp_path/'cache'; collect(root)
    db=root/'state.sqlite3'
    if damage=='missing_file': db.unlink()
    if damage=='garbage': db.write_bytes(b'BROKEN')
    if damage=='empty_file': db.write_bytes(b'')
    if damage=='missing_settings': state(root,'DELETE FROM settings')
    if damage=='missing_attempts': state(root,'DROP TABLE attempts')
    if damage=='wrong_version': state(root,'PRAGMA user_version=9')
    before=db.read_bytes() if db.exists() else None; calls=[]
    with pytest.raises((cache.CacheError,sqlite3.Error)):
        collect(root,fetcher=lambda *args:calls.append(args))
    assert calls==[] and (db.read_bytes() if db.exists() else None)==before


def test_crash_reservation_is_durable_and_cooldown_does_not_refund(tmp_path):
    root=tmp_path/'cache'
    def crash(*args): raise KeyboardInterrupt()
    with pytest.raises(KeyboardInterrupt): collect(root,fetcher=crash)
    assert state(root,'SELECT units,finished_at FROM attempts')==[(2,None)]
    with pytest.raises(cache.RetryDeferred): collect(root,clock=lambda:NOW+timedelta(seconds=299))
    _,receipt=collect(root,clock=lambda:NOW+timedelta(seconds=300))
    assert receipt['daily_reserved_units']==4 and not receipt['cache_hit']
    assert state(root,'SELECT COUNT(*) FROM attempts WHERE finished_at IS NULL')==[(1,)]


def worker(root,symbols,gate,queue,crash=False):
    gate.wait()
    def fetch(s,a,b):
        if crash: os._exit(17)
        time.sleep(0.08)
        return provider(s,a,b)
    try:
        _,receipt=collect(Path(root),symbols,fetcher=fetch,daily_limit=2,lock_timeout=3)
        queue.put(('ok',receipt))
    except Exception as error: queue.put((type(error).__name__,None))


@pytest.mark.parametrize('same_key',[True,False])
def test_concurrent_processes_deduplicate_or_compete_for_one_budget(tmp_path,same_key):
    root=tmp_path/'cache'; cache.prepare(root,2,1)
    ctx=multiprocessing.get_context('fork'); gate=ctx.Event(); queue=ctx.Queue()
    sets=[('CSCO','XLK'),('XLK','CSCO') if same_key else ('JPM','CSCO')]
    children=[ctx.Process(target=worker,args=(str(root),symbols,gate,queue)) for symbols in sets]
    for p in children:p.start()
    gate.set()
    try:
        results=[queue.get(timeout=10) for _ in children]
        for p in children: p.join(5); assert p.exitcode==0
        if same_key:
            assert sorted(r[1]['cache_hit'] for r in results)==[False,True]
        else: assert sorted(r[0] for r in results)==['BudgetExceeded','ok']
        assert state(root,'SELECT COUNT(*),SUM(units) FROM attempts')==[(1,2)]
    finally:
        for p in children:
            if p.is_alive():p.terminate();p.join()


def test_abrupt_process_death_retains_reservation_and_releases_lock(tmp_path):
    root=tmp_path/'cache'; cache.prepare(root,2,1)
    ctx=multiprocessing.get_context('fork'); gate=ctx.Event(); queue=ctx.Queue()
    child=ctx.Process(target=worker,args=(str(root),('CSCO','XLK'),gate,queue,True))
    child.start();gate.set();child.join(5)
    try:
        assert child.exitcode==17
        with pytest.raises(cache.RetryDeferred): collect(root,daily_limit=2)
        with pytest.raises(cache.BudgetExceeded): collect(root,daily_limit=2,clock=lambda:NOW+timedelta(seconds=300))
        assert state(root,'SELECT units,finished_at FROM attempts')==[(2,None)]
    finally:
        if child.is_alive():child.terminate();child.join()


def test_busy_lock_times_out_without_spending_budget(tmp_path):
    root=tmp_path/'cache'; cache.prepare(root,4,1)
    key=digest(cache.request_identity(['CSCO','XLK'],START,END,True))
    with cache.lock(root/(key+'.lock'),0):
        with pytest.raises(cache.RetryDeferred,match='busy'): collect(root,lock_timeout=0)
    assert state(root,'SELECT COUNT(*) FROM attempts')==[(0,)]


@pytest.mark.parametrize('kind',['root','database','lock'])
def test_symlink_cache_paths_are_rejected(tmp_path,kind):
    root=tmp_path/'cache'; cache.prepare(root,4,1)
    if kind=='root':
        link=tmp_path/'link';link.symlink_to(root,target_is_directory=True);root=link
    elif kind=='database':
        path=root/'state.sqlite3'; path.rename(tmp_path/'outside.db');path.symlink_to(tmp_path/'outside.db')
    else:
        path=root/'state.lock';path.unlink();(tmp_path/'outside.lock').touch();path.symlink_to(tmp_path/'outside.lock')
    with pytest.raises((cache.CacheError,OSError)):collect(root)


def test_cli_output_guard_precedes_any_cache_or_provider_mutation(tmp_path,monkeypatch):
    root=tmp_path/'cache'
    monkeypatch.setattr(sys,'argv',['benchmark_cache.py','--symbols','CSCO','--start',START,'--end',END,
                                  '--cache',str(root),'--output',str(tmp_path)])
    monkeypatch.setattr(cache,'collect',lambda *a,**kw:pytest.fail('Collection started before output guard'))
    with pytest.raises(SystemExit) as error:cache.main()
    assert error.value.code==2 and not root.exists()


@pytest.mark.parametrize('kw',[dict(daily_limit=True),dict(daily_limit=0),dict(daily_limit=1001),
                              dict(lock_timeout=float('nan')),dict(lock_timeout=31),dict(clock=lambda:NOW.replace(tzinfo=None))])
def test_invalid_policy_and_clock_rejected_before_state_creation(tmp_path,kw):
    with pytest.raises(cache.CacheError):collect(tmp_path/'cache',**kw)
    assert not (tmp_path/'cache').exists()


def test_cache_bundle_bytes_remain_compatible_with_existing_review(tmp_path):
    import benchmark_review as review
    root=tmp_path/'cache';first,_=collect(root);second,_=collect(root)
    prices.write_bundle(first,tmp_path/'first');prices.write_bundle(second,tmp_path/'second')
    assert {p.name:p.read_bytes() for p in (tmp_path/'first').iterdir()}=={p.name:p.read_bytes() for p in (tmp_path/'second').iterdir()}
    assert review.build(prices.load_bundle(tmp_path/'first'))==review.build(prices.load_bundle(tmp_path/'second'))


def test_midnight_crossing_receipt_names_the_reservation_day(tmp_path):
    moments=iter(datetime(2025,10,10,23,59,56,tzinfo=timezone.utc)+timedelta(seconds=n*2) for n in range(10))
    _,receipt=collect(tmp_path/'cache',clock=lambda:next(moments))
    assert receipt['budget_day']=='2025-10-10' and receipt['accessed_at'].startswith('2025-10-11')
    assert state(tmp_path/'cache','SELECT day,SUM(units) FROM attempts GROUP BY day')==[('2025-10-10',2)]


def test_failed_cache_commit_keeps_reservation_without_claiming_success(tmp_path,monkeypatch):
    from contextlib import contextmanager
    root=tmp_path/'cache'; original=cache.state; calls=0
    @contextmanager
    def fail_second(*args):
        nonlocal calls
        calls+=1
        if calls==2:raise sqlite3.OperationalError('synthetic disk failure')
        with original(*args) as result:yield result
    monkeypatch.setattr(cache,'state',fail_second)
    with pytest.raises(sqlite3.OperationalError):collect(root)
    assert state(root,'SELECT units,finished_at FROM attempts')==[(2,None)]
    assert state(root,'SELECT COUNT(*) FROM entries')==[(0,)]
