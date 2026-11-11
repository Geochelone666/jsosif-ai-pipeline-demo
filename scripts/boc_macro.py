"""Bounded Bank of Canada Valet USD/CAD observations with shared date-keyed caching."""
import argparse
from datetime import date,datetime,timezone
from email.utils import parsedate_to_datetime
import fcntl
import hashlib
import json
import math
from pathlib import Path
from urllib.error import HTTPError,URLError
from urllib.request import Request

from credential_http import urlopen
from report_store import write_json

SERIES='FXUSDCAD'
SOURCE='https://www.bankofcanada.ca/valet/docs'
MAX_BYTES=2*1024*1024


def parse(payload,start,end,retrieved_at):
    if (not isinstance(payload,dict) or not isinstance(payload.get('seriesDetail'),dict) or
            SERIES not in payload['seriesDetail'] or not isinstance(payload.get('observations'),list)):
        raise ValueError('Invalid Valet envelope')
    result=[];seen=set()
    for item in payload['observations']:
        if not isinstance(item,dict):raise ValueError('Invalid observation')
        stamp=item.get('d');observed=date.fromisoformat(stamp)
        if observed.isoformat()!=stamp or not start<=observed<=end or stamp in seen:
            raise ValueError('Invalid observation date')
        seen.add(stamp)
        cell=item.get(SERIES,{})
        if not isinstance(cell,dict):raise ValueError('Invalid exchange-rate cell')
        raw=cell.get('v');value=None
        if raw not in (None,'','.'):
            if isinstance(raw,bool):raise ValueError('Invalid exchange rate')
            value=float(raw)
            if not math.isfinite(value) or value<=0:raise ValueError('Invalid exchange rate')
        result.append({'observed_on':stamp,'value':value,'status':'observed' if value is not None else 'missing'})
    return {'schema_version':1,'provider':'Bank of Canada Valet','series_id':SERIES,
            'unit':'CAD per USD','base_currency':'USD','quote_currency':'CAD',
            'source_url':SOURCE,'start':start.isoformat(),'end':end.isoformat(),
            'retrieved_at':retrieved_at.isoformat(),'publication_time':None,
            'status':'observed' if any(r['value'] is not None for r in result) else 'missing',
            'observations':sorted(result,key=lambda r:r['observed_on'])}


def collect(start,end,*,cache_dir,now=None,opener=None):
    start=date.fromisoformat(start);end=date.fromisoformat(end)
    now=now or datetime.now(timezone.utc)
    if now.utcoffset() is None or start>end or (end-start).days>3660 or end>now.date():
        raise ValueError('Expected a bounded nonfuture observation window and zoned clock')
    identity={'schema_version':1,'series_id':SERIES,'start':start.isoformat(),'end':end.isoformat()}
    key=hashlib.sha256(json.dumps(identity,sort_keys=True).encode()).hexdigest()
    root=Path(cache_dir);root.mkdir(parents=True,exist_ok=True)
    path=root/(key+'.json')
    with (root/(key+'.lock')).open('a') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX)
        try:
            saved=json.loads(path.read_text())
            age=(now-datetime.fromisoformat(saved['retrieved_at'])).total_seconds()
            ttl=saved.get('retry_seconds',60) if saved['status']=='unavailable' else 3600
            if type(ttl) not in (int,float) or not math.isfinite(ttl) or ttl<60:raise ValueError('Invalid cache TTL')
            if saved.get('identity')==identity and 0<=age<ttl:
                original=saved['raw']
                checksum=hashlib.sha256(json.dumps(original,sort_keys=True,allow_nan=False).encode()).hexdigest()
                if checksum==saved['raw_sha256']:
                    if saved['status']=='unavailable':
                        category=saved['result']['category']
                        if category not in ('RATE_LIMIT','SOURCE_UNAVAILABLE','NETWORK_ERROR','DATA_VALIDATION_ERROR'):
                            raise ValueError('Invalid cached failure')
                        return {**identity,'provider':'Bank of Canada Valet','status':'unavailable','category':category,
                                'source_url':SOURCE,'retrieved_at':saved['retrieved_at'],'observations':[],
                                'cache_hit':True,'raw_sha256':None}
                    return dict(parse(original,start,end,datetime.fromisoformat(saved['retrieved_at'])),cache_hit=True,
                                raw_sha256=checksum)
        except (OSError,ValueError,KeyError,TypeError,AttributeError,OverflowError):pass
        category=None;raw=None;retry_seconds=60
        try:
            req=Request('https://www.bankofcanada.ca/valet/observations/'+SERIES+'/json?start_date='+start.isoformat()+'&end_date='+end.isoformat(),
                        headers={'User-Agent':'JSOSIF/2.0','Accept':'application/json'})
            with (opener or urlopen)(req,timeout=30) as response:
                data=response.read(MAX_BYTES+1)
            if len(data)>MAX_BYTES:raise ValueError('Response exceeds limit')
            raw=json.loads(data)
            result=parse(raw,start,end,now)
        except HTTPError as error:
            category='RATE_LIMIT' if error.code==429 else 'SOURCE_UNAVAILABLE'
            retry=(error.headers or {}).get('Retry-After','')
            try:
                delay=int(retry) if retry.isdigit() else (parsedate_to_datetime(retry)-now).total_seconds()
                if math.isfinite(delay):retry_seconds=max(60,delay)
            except (ValueError,TypeError,OverflowError):pass
        except (OSError,URLError):category='NETWORK_ERROR'
        except (ValueError,KeyError,TypeError,AttributeError,OverflowError):category='DATA_VALIDATION_ERROR'
        if category:
            raw=None
            result={**identity,'provider':'Bank of Canada Valet','status':'unavailable','category':category,
                    'source_url':SOURCE,'retrieved_at':now.isoformat(),'observations':[]}
        checksum=hashlib.sha256(json.dumps(raw,sort_keys=True,allow_nan=False).encode()).hexdigest()
        envelope={**identity,'identity':identity,'status':result['status'],'raw':raw,'raw_sha256':checksum,
                  'retrieved_at':now.isoformat(),'result':result,'retry_seconds':retry_seconds}
        # Cache write failures must not turn a successful provider observation into a failed source.
        try:write_json(path,envelope)
        except OSError:pass
        return dict(result,cache_hit=False,raw_sha256=checksum if raw is not None else None)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--start',required=True);parser.add_argument('--end',required=True)
    parser.add_argument('--cache',type=Path,required=True);parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();result=collect(args.start,args.end,cache_dir=args.cache)
    write_json(args.output,result)
    print('Bank of Canada observations: '+result['status']+'; count='+str(len(result['observations'])))
    if result['status']=='unavailable':raise SystemExit(1)


if __name__=='__main__':main()
