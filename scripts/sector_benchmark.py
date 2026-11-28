"""Validated, sector-scoped projections of retained candidate benchmark evidence."""
from datetime import timedelta

import benchmark_review as benchmarks
from shared_research_pack import canonical, exact_date

TITLE = 'Candidate benchmark comparison'
LIMITATIONS = (
    'Saved archive returns remain unaligned. Separate candidate comparisons are on page 5; no sector return is inferred.',
    'Industry KPIs, verified events and approved sector benchmarks remain missing; delivery readiness is false.',
)


def project(review, *, sector_id, name, tickers, candidates, as_of):
    benchmarks.validate(review)
    cutoff = exact_date(as_of)
    capture = review['capture']
    if exact_date(capture['end']) > cutoff:
        raise ValueError('Candidate observations extend beyond the sector cutoff')
    group = next((g for g in review['configuration'] if g['id'] == sector_id), None)
    if (group is None or group['name'] != name or group['tickers'] != sorted(tickers)
            or canonical(group['benchmark_candidates']) != canonical(candidates)):
        raise ValueError('Candidate taxonomy differs from sector coverage')
    pairs = next(g['pairs'] for g in review['groups'] if g['id'] == sector_id)
    available = sum(p['result']['status'] == 'available' for p in pairs)
    within = exact_date(capture['start']) >= cutoff-timedelta(days=6)
    return dict(review_id=review['review_id'],capture_id=capture['capture_id'],configuration_id=review['configuration_id'],
                start=capture['start'],end=capture['end'],retrieved_at=capture['finished_at'],
                capture_mode=capture['capture_mode'],within_review_window=within,
                available_pairs=available,missing_pairs=len(pairs)-available,pairs=pairs,
                delivery_ready=False,point_in_time_eligible=False)


def verify(brief, review):
    expected = project(review,sector_id=brief['sector_id'],name=brief['name'],
                       tickers=[s['ticker'] for s in brief['stocks']],candidates=brief['benchmark_candidates'],as_of=brief['as_of'])
    if (type(brief.get('schema_version')) is not int or brief['schema_version'] != 2
            or canonical(brief.get('relative_performance')) != canonical(expected)
            or brief['delivery_ready'] is not False):
        raise ValueError('Sector benchmark projection differs from retained evidence')
    return expected


def period_label(projection):
    return 'Within archive review window' if projection['within_review_window'] else 'OUTSIDE archive review window - not this week\'s return'


def mode_label(projection):
    return 'SYNTHETIC FIXTURE - not provider observations' if projection['capture_mode']=='injected_fetcher' else 'Retrospective provider capture'


def number(value):
    if value is None:return 'N/A'
    return f'{value:.3f}' if abs(value)<10000 else f'{value:.3e}'


def gap(result):
    if result['status']=='available':return 'Available'
    reason=result['reason']
    if reason=='Stock series was not captured':return 'S0'
    if reason=='Candidate benchmark series was not captured':return 'B0'
    if reason.startswith(('Stock series:', 'Candidate benchmark series:')):return 'DATA'
    if reason=='Exact observation endpoints are unavailable':return 'END'
    if reason=='Currency conversion evidence is required':return 'FX'
    if reason=='Candidate currency differs from configured currency':return 'CCY'
    return 'OTHER'


def table_rows(projection):
    return [[p['stock'],p['benchmark'],p['result'].get('currency','-'),number(p['result']['stock_return_pct']),
             number(p['result']['benchmark_return_pct']),number(p['result']['relative_return_pp']),gap(p['result'])]
            for p in projection['pairs']]
