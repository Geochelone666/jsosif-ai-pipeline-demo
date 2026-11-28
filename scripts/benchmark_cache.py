"""Exact-batch benchmark capture cache with durable, local adapter-call budgets."""
import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
from importlib.metadata import version
import json
import os
from pathlib import Path
import sqlite3
import stat
import time
import uuid

import benchmark_prices as prices
from shared_research_pack import ROOT, canonical, digest, exact_date, timestamp

POSITIVE_TTL = 3600
NEGATIVE_TTL = 300
UNCERTAIN_COOLDOWN = 300
ADAPTER_CONTRACT = 'benchmark-prices-v1'


class CacheError(ValueError): pass
class BudgetExceeded(CacheError): pass
class RetryDeferred(CacheError): pass


def utc_now(clock):
    value = clock()
    if not isinstance(value, datetime) or value.utcoffset() is None:
        raise CacheError('Expected a zoned clock')
    return value.astimezone(timezone.utc)


@contextmanager
def lock(path, timeout):
    fd = os.open(path, os.O_RDWR | os.O_CREAT | os.O_NOFOLLOW, 0o600)
    try:
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1 or info.st_uid != os.getuid():
            raise CacheError('Unsafe cache lock')
        deadline = time.monotonic()+timeout
        while True:
            try:
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB); break
            except BlockingIOError:
                if time.monotonic() >= deadline: raise RetryDeferred('Cache lock is busy') from None
                time.sleep(min(0.025, max(0, deadline-time.monotonic())))
        yield
    finally:
        os.close(fd)


def prepare(root, daily_limit, timeout):
    root = Path(root)
    if root.resolve().is_relative_to(ROOT) or root.is_symlink():
        raise CacheError('Cache must be a dedicated directory outside the repository')
    created = False
    try:
        root.mkdir(mode=0o700, parents=False); created = True
    except FileExistsError: pass
    info = root.stat()
    if not stat.S_ISDIR(info.st_mode) or info.st_uid != os.getuid() or stat.S_IMODE(info.st_mode) & 0o077:
        raise CacheError('Cache must be an owner-only directory')
    path = root/'state.sqlite3'
    if not created and not path.exists():
        raise CacheError('Cache state is missing; refusing to reset its budget')
    with lock(root/'state.lock', timeout):
        if created:
            fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY | os.O_NOFOLLOW, 0o600); os.close(fd)
            with sqlite3.connect(path) as db:
                db.executescript('''
                    PRAGMA user_version=1;
                    CREATE TABLE settings (id INTEGER PRIMARY KEY CHECK(id=1), daily_limit INTEGER NOT NULL,
                                           last_seen TEXT NOT NULL);
                    CREATE TABLE attempts (id TEXT PRIMARY KEY, cache_key TEXT NOT NULL, day TEXT NOT NULL,
                        reserved_at TEXT NOT NULL, units INTEGER NOT NULL CHECK(units BETWEEN 1 AND 59),
                        finished_at TEXT, capture_id TEXT);
                    CREATE INDEX attempts_day ON attempts(day);
                    CREATE INDEX attempts_key ON attempts(cache_key);
                    CREATE TABLE entries (cache_key TEXT PRIMARY KEY, identity TEXT NOT NULL,
                                          capture TEXT NOT NULL, attempt_id TEXT NOT NULL);
                ''')
                db.execute('INSERT INTO settings VALUES (1, ?, ?)',(daily_limit, '1970-01-01T00:00:00+00:00'))
        info = path.lstat()
        if (not stat.S_ISREG(info.st_mode) or info.st_nlink != 1 or info.st_uid != os.getuid()
                or stat.S_IMODE(info.st_mode) & 0o077):
            raise CacheError('Unsafe cache database')
    return root


@contextmanager
def state(root, daily_limit, timeout):
    with lock(root/'state.lock', timeout):
        path = root/'state.sqlite3'
        if path.is_symlink() or not path.is_file(): raise CacheError('Cache state is missing or unsafe')
        # rw prevents sqlite from silently recreating a missing budget database.
        db = sqlite3.connect(path.resolve().as_uri()+'?mode=rw', uri=True, timeout=timeout)
        try:
            db.execute('PRAGMA synchronous=FULL')
            db.execute('BEGIN IMMEDIATE')
            if db.execute('PRAGMA user_version').fetchone() != (1,) or db.execute('PRAGMA quick_check').fetchall() != [('ok',)]:
                raise CacheError('Cache state failed integrity validation')
            settings = db.execute('SELECT id,daily_limit,last_seen FROM settings').fetchall()
            if (len(settings) != 1 or settings[0][:2] != (1,daily_limit)
                    or timestamp(settings[0][2]) != settings[0][2]):
                raise CacheError('Cache policy differs or is corrupt; refusing a budget reset')
            yield db, settings[0][2]
            db.commit()
        except BaseException:
            db.rollback(); raise
        finally: db.close()


def request_identity(symbols, start, end, injected):
    prices.window(start,end)
    if (not isinstance(symbols,(list,tuple)) or not symbols
            or any(not isinstance(s,str) or s not in prices.allowed_symbols() for s in symbols)):
        raise CacheError('Expected supported stocks or configured candidates')
    return dict(schema_version=1, provider='yfinance', adapter_contract=ADAPTER_CONTRACT,
                provider_version='injected' if injected else version('yfinance'),
                capture_mode='injected_fetcher' if injected else 'provider', symbols=sorted(set(symbols)),
                start=start, end=end, interval='1d', adjustment_basis='adjusted_close')


def ttl(capture):
    for row in capture['series']:
        dates = {cell['observed_on'] for cell in row['observations'] if cell['value'] is not None}
        if row['status'] != 'observed' or not {capture['start'],capture['end']} <= dates:
            return NEGATIVE_TTL
    return POSITIVE_TTL


def cached_value(entry, identity, key, now, db):
    try:
        if len(entry[1].encode()) > prices.MAX_BYTES or entry[0] != canonical(identity): return None
        value = prices.validate_capture(json.loads(entry[1]))
        if (value['start'] != identity['start'] or value['end'] != identity['end']
                or value['capture_mode'] != identity['capture_mode']
                or [r['symbol'] for r in value['series']] != identity['symbols']): return None
        if identity['capture_mode']=='provider' and any(r['status']!='unavailable' and
                r['provider_version']!=identity['provider_version'] for r in value['series']): return None
        attempt = db.execute('SELECT cache_key,finished_at,capture_id FROM attempts WHERE id=?',(entry[2],)).fetchone()
        if attempt != (key,value['finished_at'],value['capture_id']): return None
        age = (now-datetime.fromisoformat(value['finished_at'])).total_seconds()
        return value if 0 <= age < ttl(value) else None
    except (ValueError,TypeError,KeyError,AttributeError,OverflowError): return None


def collect(symbols, *, start, end, cache_dir, daily_limit=20, fetcher=None, clock=None, lock_timeout=5):
    if type(daily_limit) is not int or not 1 <= daily_limit <= 1000:
        raise CacheError('Daily limit must be an integer between 1 and 1000')
    if type(lock_timeout) not in (int,float) or not 0 <= lock_timeout <= 30:
        raise CacheError('Lock timeout must be between 0 and 30 seconds')
    identity = request_identity(symbols,start,end,fetcher is not None); key = digest(identity)
    clock = clock or (lambda: datetime.now(timezone.utc))
    if exact_date(end) >= utc_now(clock).date(): raise CacheError('Expected a completed past window')
    root = prepare(cache_dir,daily_limit,lock_timeout)
    with lock(root/(key+'.lock'),lock_timeout):
        with state(root,daily_limit,lock_timeout) as (db,last_seen):
            now = utc_now(clock)
            if now < datetime.fromisoformat(last_seen): raise CacheError('Clock moved backwards')
            if exact_date(end) >= now.date(): raise CacheError('Expected a completed past window')
            db.execute('UPDATE settings SET last_seen=? WHERE id=1',(now.isoformat(),))
            day = now.date().isoformat()
            used = db.execute('SELECT COALESCE(SUM(units),0) FROM attempts WHERE day=?',(day,)).fetchone()[0]
            if type(used) is not int or not 0 <= used <= daily_limit: raise CacheError('Invalid budget state')
            entry = db.execute('''SELECT CASE WHEN length(CAST(identity AS BLOB))<=8192 THEN identity END,
                CASE WHEN length(CAST(capture AS BLOB))<=? THEN capture END, attempt_id
                FROM entries WHERE cache_key=?''',(prices.MAX_BYTES,key)).fetchone()
            saved = cached_value(entry,identity,key,now,db) if entry else None
            if saved is not None:
                return saved, dict(cache_key=key,cache_hit=True,accessed_at=now.isoformat(),capture_id=saved['capture_id'],
                                   budget_day=day,reserved_units=0,daily_reserved_units=used,daily_limit=daily_limit,ttl_seconds=ttl(saved))
            pending = db.execute('SELECT reserved_at FROM attempts WHERE cache_key=? AND finished_at IS NULL',(key,)).fetchall()
            for (reserved,) in pending:
                if not timestamp(reserved) or timestamp(reserved)!=reserved: raise CacheError('Invalid reservation timestamp')
                if (now-datetime.fromisoformat(reserved)).total_seconds() < UNCERTAIN_COOLDOWN:
                    raise RetryDeferred('An unfinished capture is in its retry cooldown')
            units = len(identity['symbols'])
            if used+units > daily_limit: raise BudgetExceeded('Daily adapter-call budget exhausted')
            attempt_id = uuid.uuid4().hex
            db.execute('INSERT INTO attempts VALUES (?,?,?,?,?,NULL,NULL)',(attempt_id,key,day,now.isoformat(),units))
        # Reservation is committed before any provider call. A crash never refunds it.
        value = prices.capture(identity['symbols'],start=start,end=end,fetcher=fetcher,clock=clock)
        # Preserve insertion order as well as values: the normal bundle writer
        # must produce identical bytes on a subsequent cache hit.
        raw = json.dumps(value,ensure_ascii=False,separators=(',',':'),allow_nan=False)
        if len(raw.encode()) > prices.MAX_BYTES: raise CacheError('Captured evidence exceeds cache size limit')
        with state(root,daily_limit,lock_timeout) as (db,last_seen):
            finished = datetime.fromisoformat(value['finished_at'])
            if finished < now: raise CacheError('Capture finished before reservation')
            db.execute('UPDATE settings SET last_seen=? WHERE id=1',(max(datetime.fromisoformat(last_seen),finished).isoformat(),))
            changed = db.execute('UPDATE attempts SET finished_at=?,capture_id=? WHERE id=? AND finished_at IS NULL',
                                 (value['finished_at'],value['capture_id'],attempt_id)).rowcount
            if changed != 1: raise CacheError('Capture reservation changed unexpectedly')
            db.execute('INSERT OR REPLACE INTO entries VALUES (?,?,?,?)',(key,canonical(identity),raw,attempt_id))
            used = db.execute('SELECT COALESCE(SUM(units),0) FROM attempts WHERE day=?',(day,)).fetchone()[0]
        return value, dict(cache_key=key,cache_hit=False,accessed_at=value['finished_at'],capture_id=value['capture_id'],
                           budget_day=day,reserved_units=units,daily_reserved_units=used,daily_limit=daily_limit,ttl_seconds=ttl(value))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--symbols',nargs='+',required=True)
    parser.add_argument('--start',required=True); parser.add_argument('--end',required=True)
    parser.add_argument('--cache',type=Path,required=True); parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--daily-limit',type=int,default=20)
    args = parser.parse_args()
    try:
        output,cache = args.output.resolve(),args.cache.resolve()
        if (args.output.exists() or args.output.is_symlink() or not args.output.parent.is_dir()
                or output.is_relative_to(ROOT) or output.is_relative_to(cache) or cache.is_relative_to(output)):
            raise CacheError('Expected new output outside repository and cache')
        value,receipt = collect(args.symbols,start=args.start,end=args.end,cache_dir=args.cache,daily_limit=args.daily_limit)
        prices.write_bundle(value,args.output)
    except (OSError,sqlite3.Error,ValueError,TypeError,KeyError,AttributeError):
        parser.error('Capture unavailable; inspect cache integrity/policy, retry cooldown, quota, inputs and output path')
    # Operational receipt is distinct from the unmodified retained price evidence.
    print(json.dumps(receipt,sort_keys=True))


if __name__ == '__main__': main()
