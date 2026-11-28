"""Offline CI acceptance; retain public synthetic evidence, never the cache DB."""
import argparse
from datetime import datetime, timedelta
import hashlib
import json
from pathlib import Path
import sqlite3

import benchmark_cache as cache
import benchmark_prices as prices
import benchmark_review as review


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cache',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    args.output.mkdir(parents=False,exist_ok=False)
    fixture=prices.load_bundle(Path(__file__).parent/'fixtures/benchmark_prices_synthetic')
    rows={r['symbol']:r for r in fixture['series']};calls=[]
    now=datetime.fromisoformat(fixture['finished_at'])
    def fetch(symbol,start,end):
        calls.append(symbol)
        assert (start,end)==(fixture['start'],fixture['end'])
        return rows[symbol]
    kwargs=dict(start=fixture['start'],end=fixture['end'],cache_dir=args.cache,daily_limit=2)
    first,a=cache.collect(['CSCO','XLK'],fetcher=fetch,clock=lambda:now,**kwargs)
    def deny(*args): raise AssertionError('Cache hit or exhausted budget called provider')
    second,b=cache.collect(['XLK','CSCO','CSCO'],fetcher=deny,clock=lambda:now+timedelta(seconds=30),**kwargs)
    assert calls==['CSCO','XLK'] and first==second==fixture and b['cache_hit']
    try: cache.collect(['JPM'],fetcher=deny,clock=lambda:now+timedelta(seconds=31),**kwargs)
    except cache.BudgetExceeded: pass
    else: raise AssertionError('Exhausted budget did not block a new key')
    prices.write_bundle(first,args.output/'first');prices.write_bundle(second,args.output/'second')
    def hashes(root):return {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(root.iterdir())}
    assert hashes(args.output/'first')==hashes(args.output/'second')
    review.write_bundle(review.build(second),args.output/'review')
    with sqlite3.connect(args.cache/'state.sqlite3') as db:
        reservations=db.execute('SELECT day,units,finished_at,capture_id FROM attempts').fetchall()
    assert len(reservations)==1 and reservations[0][1]==2
    result=dict(status='passed',evidence_mode='synthetic_fixture',adapter_calls=calls,first=a,second=b,
                retained_capture_unchanged=True,bundle_bytes_identical=True,quota_blocked_new_key=True,
                reservation_count=1,reserved_units=2,sha256=hashes(args.output/'first'))
    (args.output/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print('Synthetic cache acceptance passed: 2 adapter calls, cache hit reused exact evidence, quota retained')


if __name__=='__main__':main()
