from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone,timedelta
import io,json
import pytest
from boc_macro import collect,parse
from datetime import date

NOW=datetime(2026,11,7,tzinfo=timezone.utc)
PAYLOAD={'seriesDetail':{'FXUSDCAD':{'label':'US dollar'}},'observations':[
 {'d':'2026-11-02','FXUSDCAD':{'v':'1.4'}},{'d':'2026-11-03','FXUSDCAD':{'v':'.'}}]}


def test_realistic_envelope_retains_units_dates_and_missing_values(tmp_path):
 def opener(req,timeout):
  assert req.full_url.endswith('start_date=2026-11-02&end_date=2026-11-06') and timeout==30
  return io.BytesIO(json.dumps(PAYLOAD).encode())
 result=collect('2026-11-02','2026-11-06',cache_dir=tmp_path,now=NOW,opener=opener)
 assert result['unit']=='CAD per USD' and result['observations'][0]['value']==1.4
 assert result['observations'][1]['value'] is None and result['publication_time'] is None
 assert result['source_url'].startswith('https://www.bankofcanada.ca/')


def test_shared_cache_serializes_concurrent_requests_and_refetches_corruption(tmp_path):
 calls=[]
 def opener(*args,**kwargs):calls.append(1);return io.BytesIO(json.dumps(PAYLOAD).encode())
 def run(_):return collect('2026-11-02','2026-11-06',cache_dir=tmp_path,now=NOW,opener=opener)
 with ThreadPoolExecutor(max_workers=2) as pool:results=list(pool.map(run,range(2)))
 assert len(calls)==1 and sum(r['cache_hit'] for r in results)==1
 next(tmp_path.glob('*.json')).write_text('{broken')
 assert not run(0)['cache_hit'] and len(calls)==2


def test_network_failure_is_sanitized_and_backed_off(tmp_path):
 calls=[]
 def opener(*args,**kwargs):calls.append(1);raise OSError('synthetic private response')
 def run(now):return collect('2026-11-02','2026-11-06',cache_dir=tmp_path,now=now,opener=opener)
 assert run(NOW)['category']=='NETWORK_ERROR'
 assert run(NOW+timedelta(seconds=30))['cache_hit'] and len(calls)==1
 assert not run(NOW+timedelta(seconds=61))['cache_hit'] and len(calls)==2
 assert 'synthetic private' not in next(tmp_path.glob('*.json')).read_text()


@pytest.mark.parametrize('value',['nan','inf','0','-1',True])
def test_invalid_exchange_rates_cannot_become_observations(value):
 data=json.loads(json.dumps(PAYLOAD));data['observations'][0]['FXUSDCAD']['v']=value
 with pytest.raises(ValueError):parse(data,date(2026,11,2),date(2026,11,6),NOW)


def test_future_and_duplicate_dates_rejected():
 for rows in [[PAYLOAD['observations'][0]]*2,[{'d':'2026-11-08','FXUSDCAD':{'v':'1.4'}}]]:
  with pytest.raises(ValueError):parse(dict(PAYLOAD,observations=rows),date(2026,11,2),date(2026,11,6),NOW)


def test_retry_after_is_respected_and_cached_failure_fields_cannot_be_injected(tmp_path):
 from urllib.error import HTTPError
 calls=[]
 def opener(*args,**kwargs):
  calls.append(1);raise HTTPError('https://example.invalid',429,'rate limit',{'Retry-After':'300'},None)
 collect('2026-11-02','2026-11-06',cache_dir=tmp_path,now=NOW,opener=opener)
 file=next(tmp_path.glob('*.json'));cached=json.loads(file.read_text());cached['result']['private']='secret';file.write_text(json.dumps(cached))
 result=collect('2026-11-02','2026-11-06',cache_dir=tmp_path,now=NOW+timedelta(seconds=120),opener=opener)
 assert result['cache_hit'] and len(calls)==1 and 'private' not in result
