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
from time import monotonic
import uuid

from data_utils import ROOT, DATA, REPORTS, SUPPORTED
from report_store import read_json, write_json, digest, persist, verified_report_files, report_advisory
from snapshot_contract import validate_snapshot
from subscriptions import load, research_tickers
from gemini_provider import quota_day
from ticker_priority import fair_order


def quota_plan(tickers, index, rpd, *, attempts=3, used_requests=0):
    """Conservative rotation: reserve retries instead of bursting past a daily quota."""
    if type(rpd) is not int or rpd < 1:
        raise ValueError('GEMINI_RPD must be the actual positive project quota')
    if type(used_requests) is not int or used_requests < 0 or type(attempts) is not int or attempts < 1:
        raise ValueError('Request counts and retry reserve must be valid nonnegative integers')
    daily = max(1, int(rpd * .8))
    full_day_capacity = daily // attempts
    if full_day_capacity < 1:
        raise ValueError('Configured quota cannot cover one ticker and its retry reserve')
    remaining = max(0, daily - used_requests)
    capacity = remaining // attempts
    latest = {ticker: max((r['generated_at'] for r in index['reports'] if r['ticker'] == ticker and
                          r.get('quality') != 'historical'),
                          default='') for ticker in tickers}
    ordered = sorted(tickers, key=lambda ticker: (latest[ticker], ticker))
    return ordered[:capacity], {'project_rpd': rpd, 'local_daily_budget': daily,
                                'used_requests_today': used_requests, 'remaining_requests': remaining,
                                'max_attempts_per_ticker': attempts,
                                'tickers_per_day': min(capacity, len(tickers)),
                                'full_rotation_days': math.ceil(len(tickers) / full_day_capacity)}


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
        entry['source_sha256'] = {}
        for name in ('quant', 'info', 'ai-intel', 'rss-items', 'comparables', 'earnings', 'edgar'):
            target = sources / f'{ticker.lower()}-{name}.json'
            shutil.copy2(DATA / target.name, target)
            entry['source_sha256'][name] = digest(target)
        shutil.copy2(DATA / 'fred.json', sources)
        entry['source_sha256']['fred'] = digest(sources / 'fred.json')
    except Exception:
        shutil.rmtree(destination)
        raise
    return entry


def ai_budget(tickers, index, root, now, mode='auto'):
    """AI quota never suppresses market collection for another holding."""
    if mode == 'off':
        return [], {'reason': 'AI analysis disabled by configuration'}
    from ai_provider import provider
    if provider() == 'groq':
        from groq_provider import settings, GroqError
        if not (os.environ.get('GROQ_API_KEY') or os.environ.get('Grop_ai_API')):
            return [], {'reason': 'Groq API credentials are not configured'}
        try:
            settings()
        except GroqError as exc:
            return [], {'reason': str(exc)}
        from ai_provider import model as configured_model
        from groq_provider import settings as groq_settings
        selected_model = configured_model()
        caps = groq_settings()
        usage = read_json(Path(root) / 'state/api-usage.json', {})
        usage = usage if isinstance(usage, dict) else {}
        day = now.astimezone(timezone.utc).date().isoformat()
        spent = usage.get('groq:' + selected_model + ':' + day, {})
        spent = spent if isinstance(spent, dict) else {}
        requests = max(0, spent.get('requests', 0)) if type(spent.get('requests', 0)) is int else 0
        tokens = max(0, spent.get('tokens', 0)) if type(spent.get('tokens', 0)) is int else 0
        return list(tickers), {'reason': 'Groq enforces durable per-model request/token application budgets',
                               'provider': 'groq', 'model': selected_model, 'quota_day_utc': day,
                               'request_cap': caps['RPD'], 'token_cap': caps['TPD'],
                               'used_requests': requests, 'used_tokens': tokens,
                               'remaining_requests': max(0, caps['RPD'] - requests),
                               'remaining_tokens': max(0, caps['TPD'] - tokens),
                               'selected_tickers': list(tickers)}
    if os.environ.get('GEMINI_CLI'):
        return list(tickers), {'reason': 'Configured Gemini CLI', 'selected_tickers': list(tickers)}
    if not (os.environ.get('GEMINI_API_KEY') or os.environ.get('GOOGLE_API_KEY')):
        return [], {'reason': 'AI API credentials are not configured'}
    try:
        rpd = int(os.environ.get('GEMINI_RPD', '0'))
        rpm = int(os.environ.get('GEMINI_RPM', '0'))
        if rpm < 1:
            raise ValueError('GEMINI_RPM must be positive')
        model = os.environ.get('GEMINI_MODEL', 'gemini-3.5-flash-lite')
        usage = read_json(Path(root) / 'state/api-usage.json', {})
        selected, plan = quota_plan(tickers, index, rpd,
                                   used_requests=usage.get(model + ':' + quota_day(now), 0))
    except (TypeError, ValueError):
        return [], {'reason': 'Configure positive GEMINI_RPD and GEMINI_RPM project quotas'}
    plan['selected_tickers'] = selected
    plan['reason'] = ('AI daily budget is insufficient for all holdings'
                      if len(selected) < len(tickers) else 'AI budget reserved for all holdings')
    return selected, plan



def reusable_reports(root, index, tickers, business_date):
    """Only intact, ready same-day reports can satisfy an explicit resume."""
    reusable = {}
    for entry in index.get('reports', []):
        if (entry.get('ticker') not in tickers or entry.get('as_of') != business_date
                or entry.get('quality') != 'ready' or entry.get('advisory')):
            continue
        try:
            verified_report_files(root, entry)
            if report_advisory(root, entry):
                continue
        except (ValueError, OSError, KeyError, TypeError):
            continue
        ticker = entry['ticker']
        if ticker not in reusable or entry['generated_at'] > reusable[ticker]['generated_at']:
            reusable[ticker] = entry
    return reusable

def refresh(root, *, config=None, now=None, business_date=None, force=False,
            interval_days=1, ai_mode='auto', stage_timeout=600, persist_git=False, scheduled=False,
            resume=False, time_budget_seconds=None):
    from datetime import date, time
    from zoneinfo import ZoneInfo

    started_at = monotonic()
    if force and resume:
        raise ValueError('Choose resume or force, not both')
    if time_budget_seconds is not None and (isinstance(time_budget_seconds, bool)
            or not math.isfinite(time_budget_seconds) or time_budget_seconds <= 0):
        raise ValueError('Time budget must be a positive finite number')
    def remaining():
        return None if time_budget_seconds is None else time_budget_seconds - (monotonic() - started_at)

    def run_stage(command, **kwargs):
        budget = remaining()
        if budget is not None and budget <= 0:
            raise subprocess.TimeoutExpired(command, time_budget_seconds)
        return subprocess.run(command, timeout=min(stage_timeout, budget) if budget is not None else stage_timeout,
                              **kwargs)

    now = now or datetime.now(timezone.utc)
    business_date = business_date or now.astimezone(ZoneInfo('America/Toronto')).date().isoformat()
    report_date = date.fromisoformat(business_date)
    if report_date > now.astimezone(ZoneInfo('America/Toronto')).date():
        raise ValueError('Business date must not be in the future')
    if not 1 <= interval_days <= 30 or stage_timeout < 1:
        raise ValueError('Invalid interval or stage timeout')
    root = Path(root)
    root.mkdir(parents=True, exist_ok=True)
    index = read_json(root / 'index.json', {'reports': []})
    def checkpoint():
        write_json(root / 'index.json', index)
        persist(root, git=persist_git)

    previous = index.get('last_attempt', {})
    evening = datetime.combine(report_date, time(19), tzinfo=ZoneInfo('America/Toronto'))
    try:
        previous_at = datetime.fromisoformat(previous.get('at', ''))
        replaces_intraday_test = (scheduled and previous.get('business_date') == business_date
                                  and previous_at.tzinfo is not None
                                  and previous_at < evening <= now)
    except (ValueError, TypeError):
        replaces_intraday_test = False
    if not force and not resume and not replaces_intraday_test and previous.get('business_date') == business_date:
        print('Daily run already attempted; use --resume to recover outstanding reports or --force to recompute all')
        return {'status': 'skipped', 'publish': False, 'failed': False}
    last = index.get('last_complete_business_date')
    if last and not force and not resume and not replaces_intraday_test and (report_date - date.fromisoformat(last)).days < interval_days:
        print('Refresh interval not elapsed; archive retained')
        return {'status': 'skipped', 'publish': False, 'failed': False}
    tickers = research_tickers(load(config)) if config else list(SUPPORTED)
    if not tickers:
        return {'status': 'skipped', 'publish': False, 'failed': False}
    reused = reusable_reports(root, index, tickers, business_date) if resume else {}
    pending = [ticker for ticker in tickers if ticker not in reused]
    policy = os.environ.get('JSOSIF_FAIR_RESEARCH_PRIORITY') == '1'
    processing_order = fair_order(pending, index.get('reports', []), business_date) if policy else pending
    selected, plan = ai_budget(pending, index, root, now, ai_mode)
    plan['processing_order'] = processing_order
    plan['priority_policy'] = 'least_recently_ready_then_date_rotation' if policy else 'configured_ticker_order'
    index['refresh_plan'] = plan
    run_id = now.strftime('%Y%m%dT%H%M%SZ') + '-' + uuid.uuid4().hex[:8]
    attempt = {'run_id': run_id, 'at': now.isoformat(), 'business_date': business_date,
               'status': 'running', 'expected_tickers': tickers, 'successful_tickers': sorted(reused),
               'reused_tickers': sorted(reused), 'workflow_run_id': os.environ.get('GITHUB_RUN_ID'),
               'degraded_tickers': [], 'failed_tickers': [], 'failures': [],
               'ai_selected_tickers': selected, 'ai_deferred_tickers': sorted(set(pending)-set(selected)),
               'stage_seconds': {}}
    index['last_attempt'] = attempt
    checkpoint()
    env = dict(os.environ, REPORT_AS_OF=business_date)
    env['JSOSIF_PERSIST_API_USAGE'] = '1' if persist_git else '0'
    env['JSOSIF_API_USAGE_PATH'] = str(root.resolve() / 'state/api-usage.json')
    env['JSOSIF_SEC_CACHE'] = str(root.resolve() / 'state/sec-tickers.json')
    env['JSOSIF_PRICE_CACHE'] = str(root.resolve() / 'state/price-cache')
    env['JSOSIF_PRICE_CACHE_BATCH_START'] = str(now.timestamp())
    DATA.mkdir(exist_ok=True); REPORTS.mkdir(exist_ok=True)
    try:
        if pending:
            run_stage([sys.executable, str(ROOT / 'scripts/fred.py')], cwd=ROOT, env=env, check=True)
    except (subprocess.SubprocessError, OSError):
        attempt.update(status='partial' if reused else 'failed', failed_tickers=pending,
                       pending_tickers=pending,
                       failures=[{'stage': 'fred', 'category': 'shared_prerequisite_failed'}])
        attempt['finished_at'] = datetime.now(timezone.utc).isoformat()
        if remaining() is not None and remaining() <= 0:
            attempt.update(status='interrupted', interruption_reason='time_budget_exhausted')
        checkpoint()
        return {'status': attempt['status'], 'publish': True, 'failed': True}
    groq_budget_closed = False
    for ticker in processing_order:
        if remaining() is not None and remaining() <= 0:
            break
        attempt['current_ticker'] = ticker
        attempt['last_progress_at'] = datetime.now(timezone.utc).isoformat()
        checkpoint()
        stage = 'preflight'
        timings = attempt['stage_seconds'][ticker] = {}
        try:
            allow_ai = ticker in selected and not groq_budget_closed
            ticker_env = dict(env, JSOSIF_AI_ENABLED='1' if allow_ai else '0',
                              JSOSIF_AI_UNAVAILABLE_REASON=(
                                  'Groq application daily budget exhausted earlier in this run'
                                  if groq_budget_closed else plan['reason']))
            if (os.environ.get('JSOSIF_NEWS_REUSE_ENABLED') == '1' and
                    ai_mode != 'off' and ticker in selected):
                from news_reuse import prior_decisions
                cached = prior_decisions(root, index.get('reports', []), ticker, business_date)
                if cached:
                    cache_path = DATA / f'{ticker.lower()}-news-reuse.json'
                    write_json(cache_path, cached)
                    ticker_env['JSOSIF_NEWS_REUSE_PATH'] = str(cache_path)
                    attempt.setdefault('news_cache_candidates', {})[ticker] = len(cached['items'])
            for stage in ('quant', 'ai_extract', 'comparables', 'earnings', 'edgar', 'regenerate_report', 'report_pdf'):
                # Never use the demo SEC contact identity for a production request.
                if stage == 'edgar' and not (os.environ.get('SEC_USER_AGENT') or os.environ.get('GMAIL_USER')):
                    write_json(DATA / f'{ticker.lower()}-edgar.json', {
                        'ticker': ticker, 'cik': None, 'latest_filing': None, 'revenue': None,
                        'net_income': None, 'error': 'SEC source unavailable: configure SEC_USER_AGENT'})
                    continue
                started = monotonic()
                try:
                    run_stage([sys.executable, str(ROOT / 'scripts' / f'{stage}.py'), '--ticker', ticker],
                              cwd=ROOT, env=ticker_env, check=True)
                finally:
                    timings[stage] = round(monotonic() - started, 3)
                    print(f'Research stage: {ticker} {stage} {timings[stage]}s', flush=True)
                if (stage == 'ai_extract' and allow_ai and plan.get('provider') == 'groq'):
                    ai_result = read_json(DATA / f'{ticker.lower()}-ai-intel.json', {})
                    failure = ai_result.get('error', '') if isinstance(ai_result, dict) else ''
                    if isinstance(failure, str) and 'Groq application daily budget exhausted' in failure:
                        groq_budget_closed = True
                        attempt['ai_budget_closed_after'] = ticker
                        attempt['ai_budget_closed_reason'] = 'local_daily_budget_exhausted'
                        print(f'{ticker}: local Groq daily budget exhausted; suppressing further AI calls '
                              'while still collecting market/news snapshots', flush=True)
            stage = 'archive'
            entry = archive(root, ticker, report_date.strftime('%Y%m%d'), run_id,
                            datetime.now(timezone.utc).isoformat())
            index['reports'].append(entry)
            attempt['successful_tickers'].append(ticker)
            if entry['quality'] != 'ready':
                attempt['degraded_tickers'].append(ticker)
        except (subprocess.SubprocessError, ValueError, OSError, KeyError) as exc:
            attempt['failed_tickers'].append(ticker)
            attempt['failures'].append({'ticker': ticker, 'stage': stage,
                                        'category': 'timeout' if isinstance(exc, subprocess.TimeoutExpired) else 'stage_failed'})
            print(f'{ticker}: refresh failed; previous versions retained', file=sys.stderr)
        checkpoint()
        completed = len(attempt['successful_tickers']) + len(attempt['failed_tickers'])
        if os.environ.get('GITHUB_ACTIONS') == 'true':
            print('::notice title=Research progress::' + json.dumps({
                'completed': completed, 'total': len(tickers),
                'degraded': len(attempt['degraded_tickers']), 'failed': len(attempt['failed_tickers'])}), flush=True)
    outstanding = set(tickers) - set(attempt['successful_tickers'])
    budget_expired = remaining() is not None and remaining() <= 0 and bool(outstanding)
    attempt['pending_tickers'] = sorted(outstanding | set(attempt['degraded_tickers']))
    attempt.pop('current_ticker', None)
    if budget_expired:
        attempt['status'] = 'interrupted'
        attempt['interruption_reason'] = 'time_budget_exhausted'
    elif attempt['failed_tickers']:
        attempt['status'] = 'partial' if attempt['successful_tickers'] else 'failed'
    else:
        attempt['status'] = 'degraded' if attempt['degraded_tickers'] else 'complete'
        index['last_complete_refresh'] = now.isoformat()
        index['last_complete_business_date'] = business_date
    attempt['finished_at'] = datetime.now(timezone.utc).isoformat()
    checkpoint()
    return {'status': attempt['status'], 'publish': True, 'failed': bool(attempt['failed_tickers']) or budget_expired}


def main():
    import fcntl
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--store', type=Path, required=True)
    parser.add_argument('--config', type=Path)
    parser.add_argument('--interval-days', type=int, default=1)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--force', action='store_true')
    mode.add_argument('--resume', action='store_true', help='Reuse verified ready reports for the same business date')
    parser.add_argument('--time-budget-seconds', type=float)
    parser.add_argument('--business-date')
    parser.add_argument('--ai-mode', choices=('auto', 'off'), default='auto')
    parser.add_argument('--stage-timeout', type=int, default=600)
    parser.add_argument('--persist-git', action='store_true')
    parser.add_argument('--scheduled', action='store_true', help='Preserve the evening slot after an earlier manual test')
    args = parser.parse_args()
    lock_dir = ROOT / 'logs'
    lock_dir.mkdir(exist_ok=True)
    with (lock_dir / 'refresh.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        result = refresh(args.store, config=args.config, business_date=args.business_date,
                         force=args.force, interval_days=args.interval_days,
                         ai_mode=args.ai_mode, stage_timeout=args.stage_timeout, persist_git=args.persist_git,
                         scheduled=args.scheduled, resume=args.resume,
                         time_budget_seconds=args.time_budget_seconds)
    if os.environ.get('GITHUB_OUTPUT'):
        with open(os.environ['GITHUB_OUTPUT'], 'a', encoding='utf-8') as output:
            output.write('publish=' + str(result['publish']).lower() + '\n')
            output.write('status=' + result['status'] + '\n')
    print(json.dumps(result))
    if result['failed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
