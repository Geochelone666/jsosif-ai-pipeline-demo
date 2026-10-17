"""Refresh configured holdings and publish immutable report/source versions."""
import argparse
from datetime import datetime, timedelta, timezone
import json
import math
import os
from pathlib import Path
import shutil
import subprocess
import sys
import uuid

from data_utils import ROOT, DATA, REPORTS, SUPPORTED
from report_store import read_json, write_json, digest
from snapshot_contract import validate_snapshot
from subscriptions import load, tickers_for


def quota_plan(tickers, index, rpd, *, attempts=3):
    """Conservative rotation: reserve retries instead of bursting past a daily quota."""
    if rpd < 1:
        raise ValueError('GEMINI_RPD must be the actual positive project quota')
    daily = max(1, int(rpd * .8))
    capacity = daily // attempts
    if capacity < 1:
        raise ValueError('Configured quota cannot cover one ticker and its retry reserve')
    latest = {ticker: max((r['generated_at'] for r in index['reports'] if r['ticker'] == ticker),
                          default='') for ticker in tickers}
    ordered = sorted(tickers, key=lambda ticker: (latest[ticker], ticker))
    return ordered[:capacity], {'project_rpd': rpd, 'local_daily_budget': daily,
                                'max_attempts_per_ticker': attempts,
                                'tickers_per_day': min(capacity, len(tickers)),
                                'full_rotation_days': math.ceil(len(tickers) / capacity)}


def archive(root, ticker, stamp, run_id, generated_at):
    root = Path(root)
    snapshot = json.loads((REPORTS / f'{ticker}-intelligence-{stamp}.json').read_text())
    errors = validate_snapshot(snapshot)
    if errors or snapshot['identity']['ticker'] != ticker or snapshot['identity']['report_stamp'] != stamp:
        raise ValueError('Report does not satisfy the snapshot contract')
    destination = root / 'archive' / run_id / ticker
    if destination.exists():
        raise ValueError('Report version already exists')
    destination.mkdir(parents=True)
    entry = dict(report_id=f'{run_id}/{ticker}', ticker=ticker, generated_at=generated_at,
                 as_of=snapshot['identity']['as_of'], quality=snapshot['quality'],
                 market_as_of=snapshot['freshness']['market_data_as_of'],
                 news_as_of=snapshot['freshness']['ai_snapshot_as_of'], sha256={})
    try:
        for kind in ('md', 'json', 'pdf'):
            source = REPORTS / f'{ticker}-intelligence-{stamp}.{kind}'
            if kind == 'pdf' and not source.read_bytes().startswith(b'%PDF-'):
                raise ValueError('Invalid PDF')
            target = destination / source.name
            shutil.copy2(source, target)
            entry[kind] = target.relative_to(root).as_posix()
            entry['sha256'][kind] = digest(target)
        # Only explicit public data inputs, never credentials, prompts or raw stderr.
        sources = destination / 'sources'
        sources.mkdir()
        for name in ('quant', 'info', 'ai-intel', 'rss-items', 'comparables', 'earnings', 'edgar'):
            shutil.copy2(DATA / f'{ticker.lower()}-{name}.json', sources)
        shutil.copy2(DATA / 'fred.json', sources)
    except Exception:
        shutil.rmtree(destination)
        raise
    return entry


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--store', type=Path, required=True)
    parser.add_argument('--config', type=Path)
    parser.add_argument('--interval-days', type=int, default=1)
    parser.add_argument('--force', action='store_true')
    args = parser.parse_args()
    if not 1 <= args.interval_days <= 30:
        parser.error('interval-days must be 1 to 30')
    now = datetime.now(timezone.utc)
    args.store.mkdir(parents=True, exist_ok=True)
    index = read_json(args.store / 'index.json', {'reports': []})
    last = index.get('last_complete_refresh')
    if last and not args.force and (now.date() - datetime.fromisoformat(last).date()).days < args.interval_days:
        print('Refresh interval not elapsed; archive retained')
        return
    tickers = tickers_for(load(args.config)) if args.config else list(SUPPORTED)
    if not tickers:
        print('No active subscriptions; no API calls')
        return
    if not os.environ.get('GEMINI_CLI') and not (os.environ.get('GEMINI_API_KEY') or os.environ.get('GOOGLE_API_KEY')):
        parser.error('Configure GEMINI_API_KEY (or explicitly configure GEMINI_CLI) before refreshing')
    if not os.environ.get('SEC_USER_AGENT'):
        parser.error('Configure SEC_USER_AGENT with your organization and contact email')
    if not os.environ.get('GEMINI_CLI'):
        try:
            rpd, rpm = int(os.environ.get('GEMINI_RPD', '0')), int(os.environ.get('GEMINI_RPM', '0'))
            if rpm < 1:
                raise ValueError('GEMINI_RPM must be the actual positive project quota')
            tickers, plan = quota_plan(tickers, index, rpd)
        except ValueError as exc:
            parser.error(str(exc))
        index['refresh_plan'] = plan
        print('Quota plan:', json.dumps(plan))
        write_json(args.store / 'index.json', index)
    # Freeze the business date for every stage even if a job crosses UTC midnight.
    env = dict(os.environ, REPORT_AS_OF=now.date().isoformat())
    env['JSOSIF_API_USAGE_PATH'] = str(args.store.resolve() / 'state/api-usage.json')
    env['JSOSIF_SEC_CACHE'] = str(args.store.resolve() / 'state/sec-tickers.json')
    env['JSOSIF_PRICE_CACHE'] = str(args.store.resolve() / 'state/price-cache')
    DATA.mkdir(exist_ok=True); REPORTS.mkdir(exist_ok=True)
    subprocess.run([sys.executable, str(ROOT / 'scripts/fred.py')], cwd=ROOT, env=env, check=True)
    run_id = now.strftime('%Y%m%dT%H%M%SZ') + '-' + uuid.uuid4().hex[:8]
    failures = []
    for ticker in tickers:
        try:
            for stage in ('quant', 'ai_extract', 'comparables', 'earnings', 'edgar', 'regenerate_report', 'report_pdf'):
                subprocess.run([sys.executable, str(ROOT / 'scripts' / f'{stage}.py'), '--ticker', ticker],
                               cwd=ROOT, env=env, check=True)
            entry = archive(args.store, ticker, now.strftime('%Y%m%d'), run_id, now.isoformat())
            index['reports'].append(entry)
            write_json(args.store / 'index.json', index)
        except (subprocess.CalledProcessError, ValueError, OSError, KeyError):
            failures.append(ticker)
            print(f'{ticker}: refresh failed; previous versions retained', file=sys.stderr)
    if not failures:
        index['last_complete_refresh'] = now.isoformat()
    index['last_attempt'] = {'at': now.isoformat(), 'failed_tickers': failures}
    write_json(args.store / 'index.json', index)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
