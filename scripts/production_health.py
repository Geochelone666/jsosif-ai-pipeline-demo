#!/usr/bin/env python3
"""Read-only daily research health report, with deterministic failure categories.

Only aggregates public report/source evidence. Never reads subscriptions,
delivery state, member addresses, environment secrets or email bodies.
"""
import argparse
from collections import Counter
from datetime import datetime, timezone
import json
from pathlib import Path

from report_store import read_json, resolve_file, verified_report_files


def failure_reason(snapshot, ai):
    """Classify root cause using persisted error signals, not guessed HTTP state."""
    statuses = snapshot.get('source_status') or {}
    if statuses.get('market') != 'ok':
        return 'market_source_invalid'
    if not isinstance(ai, dict):
        return 'news_source_unavailable'
    fetch = ai.get('fetch_status') or {}
    if fetch.get('status') not in (None, 'ok'):
        return 'rss_fetch_failed'
    error = str(ai.get('error') or '').lower()
    if 'groq application daily budget exhausted' in error:
        return 'groq_daily_tokens' if 'token' in error else (
            'groq_daily_requests' if 'requests' in error else 'groq_daily_budget')
    if 'ai unavailable' in error or 'api credentials' in error:
        return 'ai_provider_unavailable'
    if error:
        return 'news_processing_error'
    statistics = ai.get('extraction_stats') or {}
    if statistics.get('unknown', 0):
        return 'unresolved_news_classification'
    if statuses.get('news') != 'ok':
        return 'news_evidence_invalid'
    return 'other_degraded_evidence'


def build_health(store):
    root = Path(store)
    index = read_json(root / 'index.json', {})
    if not isinstance(index, dict):
        raise ValueError('Invalid report store index')
    attempt = index.get('last_attempt') or {}
    if not isinstance(attempt, dict) or not attempt.get('run_id'):
        raise ValueError('No recorded production attempt')
    date = attempt.get('business_date')
    expected = attempt.get('expected_tickers') or []
    if not isinstance(expected, list) or not all(isinstance(t, str) for t in expected):
        raise ValueError('Invalid expected ticker roster')
    run_id = attempt['run_id']
    reports = index.get('reports') or []
    by_ticker = {}
    for entry in reports:
        ticker = entry.get('ticker')
        if ticker not in expected or entry.get('as_of') != date:
            continue
        # Reused ready versions on the same report date are considered only
        # when no fresh report was generated in this particular run.
        is_current = entry.get('report_id', '').startswith(run_id + '/')
        prior = by_ticker.get(ticker)
        if prior is None or (is_current, entry.get('generated_at', '')) > (
                prior['report_id'].startswith(run_id + '/'), prior.get('generated_at', '')):
            by_ticker[ticker] = entry
    errors, fail_reasons, rows = Counter(), Counter(), []
    classified = Counter()
    observed_publishers = 0
    reused_decisions = 0
    review_flags = 0
    for ticker in expected:
        entry = by_ticker.get(ticker)
        if entry is None:
            errors['missing_report'] += 1
            rows.append({'ticker': ticker, 'quality': 'missing', 'reason': 'missing_report'})
            continue
        try:
            files = verified_report_files(root, entry)
            snapshot = read_json(files['json'], {})
            location = (Path(entry['json']).parent / 'sources' /
                        (ticker.lower() + '-ai-intel.json')).as_posix()
            ai = read_json(resolve_file(root, location), {})
            if not isinstance(snapshot, dict):
                raise ValueError('invalid snapshot')
            if not isinstance(ai, dict):
                raise ValueError('invalid ai source')
        except (OSError, ValueError, KeyError, TypeError, AttributeError):
            errors['archive_integrity'] += 1
            rows.append({'ticker': ticker, 'quality': 'unverified',
                         'reason': 'archive_integrity'})
            continue
        stats = ai.get('extraction_stats') or {}
        for field in ('rule', 'ai', 'unknown', 'irrelevant'):
            value = stats.get(field, 0)
            if type(value) is int and value >= 0:
                classified[field] += value
        rss = ai.get('rss_audit') or {}
        count = rss.get('unique_publishers') if isinstance(rss, dict) else None
        if type(count) is int and count >= 0:
            observed_publishers += count
        reuse = ai.get('ai_reuse') or {}
        count = reuse.get('reused_headlines') if isinstance(reuse, dict) else None
        if type(count) is int and count >= 0:
            reused_decisions += count
        review = ai.get('decision_audit') or {}
        count = review.get('flag_count') if isinstance(review, dict) else None
        if type(count) is int and count >= 0:
            review_flags += count
        quality = entry.get('quality')
        reason = None if quality == 'ready' else failure_reason(snapshot, ai)
        if reason:
            fail_reasons[reason] += 1
        rows.append({'ticker': ticker, 'quality': quality, 'reason': reason})
    total = len(expected)
    ready = sum(row['quality'] == 'ready' for row in rows)
    return {
        'business_date': date, 'run_id': run_id,
        'status': attempt.get('status'), 'expected': total, 'ready': ready,
        'degraded_or_unverified': total - ready,
        'strict_release_eligible': attempt.get('status') == 'complete' and ready == total and total > 0,
        'failure_reasons': dict(sorted(fail_reasons.items())),
        'integrity_errors': dict(sorted(errors.items())),
        'classification_totals': dict(classified),
        'sum_named_publishers_per_ticker': observed_publishers,
        'verified_ai_decisions_reused': reused_decisions,
        'nonblocking_decision_review_flags': review_flags,
        'ticker_status': rows,
        'ai_budget_closed_after': attempt.get('ai_budget_closed_after'),
        'refresh_priority_policy': (index.get('refresh_plan') or {}).get('priority_policy'),
        'observed_at_utc': datetime.now(timezone.utc).isoformat(),
        'limitations': ('Classification counts and model confidence are not independently validated '
                        'accuracy rates; sums of publishers across tickers are not unique publishers. '
                        'Historical report archives are immutable.'),
    }


def markdown(health):
    lines = [
        '## Research production evidence health',
        f"Business date: **{health['business_date']}**; status: **{health['status']}**",
        f"Ready: **{health['ready']}/{health['expected']}**; "
        f"strict eligible: **{health['strict_release_eligible']}**",
        'Failure categories: ' + json.dumps(health['failure_reasons'], sort_keys=True),
        'Archive integrity: ' + json.dumps(health['integrity_errors'], sort_keys=True),
        'Classification counts: ' + json.dumps(health['classification_totals'], sort_keys=True),
        f"Previously verified AI decisions reused: {health['verified_ai_decisions_reused']}",
        f"Nonblocking review flags: {health['nonblocking_decision_review_flags']}",
        'These numbers describe evidence completeness, not prediction accuracy.',
    ]
    for row in health['ticker_status']:
        if row['quality'] != 'ready':
            lines.append(f"- {row['ticker']}: {row['quality']} / {row['reason']}")
    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--store', required=True, type=Path)
    parser.add_argument('--json-out', type=Path)
    parser.add_argument('--append-summary', type=Path)
    args = parser.parse_args()
    health = build_health(args.store)
    payload = json.dumps(health, indent=2, ensure_ascii=False, allow_nan=False) + '\n'
    print(payload)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(payload, encoding='utf-8')
    if args.append_summary:
        with args.append_summary.open('a', encoding='utf-8') as stream:
            stream.write('\n' + markdown(health))


if __name__ == '__main__':
    main()
