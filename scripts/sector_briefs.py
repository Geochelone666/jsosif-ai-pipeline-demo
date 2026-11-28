"""Build eight offline, retrospective sector brief drafts from verified archives."""
import argparse
from datetime import timedelta
import hashlib
import json
from pathlib import Path
from tempfile import TemporaryDirectory

from shared_research_pack import build, digest, exact_date, validate_pack

SECTIONS = (
    'Coverage and source dates', 'Relative performance', 'Macro drivers',
    'Peer valuation snapshot', 'Industry KPIs and missing evidence',
    'Regulation and next-week events', 'Risks and limitations',
)
LIMITATIONS = (
    'Retrospective archive reconstruction; not current market data or point-in-time backtest evidence.',
    'Research groups are configurable product defaults, not a formal industry classification.',
    'Provider industry labels and peer candidates do not establish economic comparability.',
    'Saved returns lack aligned endpoints and adjustment evidence; no sector or benchmark return is calculated.',
    'Peer fiscal periods and valuation bases may differ. Native currencies are not converted or aggregated.',
    'Publication dates and historical vintages are unavailable. A report date is not a freshness guarantee.',
    'Industry KPIs, verified events and sector-relative performance are missing; delivery readiness is false.',
    'For analyst research preparation only; not investment advice.',
)


def one(rows, subject, metric):
    matches = [r for r in rows if r['subject'] == subject and r['metric'] == metric]
    if len(matches) > 1:
        raise ValueError('Ambiguous metric within a report context')
    return matches[0]['id'] if matches else None


def assemble(pack, *, benchmark_review=None):
    """Build deterministic evidence projections; never infer facts from prose or peers."""
    validate_pack(pack)
    entities = {r['id']: r for r in pack['entities']}
    observations = {r['id']: r for r in pack['observations']}
    sources = {r['id']: r for r in pack['sources']}
    reports = {r['ticker']: r for r in pack['reports']}
    if len(reports) != len(pack['reports']):
        raise ValueError('Duplicate report ticker')
    cutoff = exact_date(pack['as_of'])
    start = cutoff - timedelta(days=6)
    seen = set()
    result = []
    for sector in sorted(pack['sectors'], key=lambda r: r['id']):
        if (sector['id'] not in entities or entities[sector['id']]['kind'] != 'sector'
                or not sector['tickers'] or len(set(sector['tickers'])) != len(sector['tickers'])
                or seen.intersection(sector['tickers'])):
            raise ValueError('Invalid sector coverage identity')
        seen.update(sector['tickers'])
        stocks = []
        used_obs = set(pack['additional_macro_observations'])
        used_sources = set()
        for ticker in sorted(sector['tickers']):
            report = reports.get(ticker)
            if report is None:
                stocks.append({'ticker': ticker, 'status': 'missing_report', 'report_id': None,
                               'industry': None, 'metrics': {}, 'peers': [], 'peer_count': 0})
                continue
            rows = [observations[k] for k in report['observation_ids']]
            if any(r['context_date'] != report['as_of'] for r in rows):
                raise ValueError('Evidence context does not match its report')
            subject = 'stock:' + ticker
            metrics = {r['metric']: one(rows, subject, r['metric']) for r in rows
                       if r['subject'] == subject and r['metric'].startswith(('stock.', 'sec.'))}
            peer_ids = sorted(set(report['peer_ids']))
            peers = []
            for peer_id in peer_ids[:5]:
                if entities[peer_id]['kind'] != 'stock' or peer_id == subject:
                    raise ValueError('Invalid peer identity')
                peers.append({'ticker': entities[peer_id]['ticker'], 'metrics': {
                    metric: one(rows, peer_id, metric)
                    for metric in ('peer.pe', 'peer.pb', 'peer.ev_ebitda', 'peer.mktcap', 'peer.ret_1y')
                }})
            selected = set(metrics.values())
            selected.update(k for p in peers for k in p['metrics'].values() if k)
            selected.update(r['id'] for r in rows if entities[r['subject']]['kind'] == 'macro')
            used_obs.update(selected)
            used_sources.add(report['snapshot_source_id'])
            industry = entities[report['industry_id']]['name'] if report['industry_id'] else None
            for relation in pack['relationships']:
                if (relation['subject'] == subject and relation['context_date'] == report['as_of']
                        and relation['predicate'] in ('provider_industry', 'provider_peer_candidate')):
                    used_sources.add(relation['source_id'])
            stocks.append({'ticker': ticker, 'status': 'archived', 'report_id': report['report_id'],
                           'report_date': report['as_of'], 'quality': report['quality'],
                           'in_review_window': start <= exact_date(report['as_of']) <= cutoff,
                           'report_age_days': (cutoff - exact_date(report['as_of'])).days,
                           'industry': industry, 'metrics': metrics, 'peers': peers,
                           'peer_count': len(peer_ids), 'snapshot_source_id': report['snapshot_source_id']})
        for relation in pack['relationships']:
            if relation['object'] == sector['id'] or relation['subject'] == sector['id']:
                used_sources.add(relation['source_id'])
        for key in used_obs:
            used_sources.update(s for s in (observations[key]['source_id'], observations[key]['currency_source_id']) if s)
        macro = []
        for subject in sorted({observations[k]['subject'] for k in used_obs
                               if entities[observations[k]['subject']]['kind'] == 'macro'}):
            candidates = [observations[k] for k in used_obs if observations[k]['subject'] == subject]
            usable = [r for r in candidates if r['status'] == 'observed']
            latest = max((r['observed_on'] for r in usable), default=None)
            latest_rows = [r for r in usable if r['observed_on'] == latest]
            distinct = {(r['value'], r['unit']) for r in latest_rows}
            status = 'missing' if not distinct else ('observed' if len(distinct) == 1 else 'conflicting')
            value, unit = next(iter(distinct)) if status == 'observed' else (None, None)
            macro.append({'subject': subject, 'status': status, 'observed_on': latest,
                          'value': value, 'unit': unit,
                          'observation_ids': sorted(r['id'] for r in candidates)})
        payload = {
            'schema_version': 1, 'dataset_id': pack['dataset_id'], 'sector_id': sector['id'],
            'name': sector['name'], 'as_of': pack['as_of'], 'review_start': start.isoformat(),
            'status': 'draft_incomplete_evidence', 'delivery_ready': False,
            'temporal_scope': pack['temporal_scope'], 'sections': list(SECTIONS),
            'stocks': stocks, 'macro': macro,
            'benchmark_candidates': sector['benchmark_candidates'], 'relative_performance': None,
            'kpi_topics': sector['kpi_topics'], 'kpi_observations': [], 'events': [],
            'missing_evidence': ['validated_benchmark_returns', 'industry_kpis', 'verified_events',
                                 'publication_times_and_vintages'],
            'observations': [observations[k] for k in sorted(used_obs)],
            'sources': [sources[k] for k in sorted(used_sources)], 'limitations': list(LIMITATIONS),
        }
        if benchmark_review is not None:
            from sector_benchmark import project, LIMITATIONS as benchmark_limitations
            projection = project(benchmark_review,sector_id=sector['id'],name=sector['name'],
                                 tickers=sector['tickers'],candidates=sector['benchmark_candidates'],as_of=pack['as_of'])
            payload['schema_version'] = 2
            payload['relative_performance'] = projection
            payload['limitations'][3] = benchmark_limitations[0]
            payload['limitations'][6] = benchmark_limitations[1]
            payload['missing_evidence'][0] = 'approved_sector_benchmarks'
            if projection['missing_pairs']: payload['missing_evidence'].append('candidate_pair_gaps')
            if not projection['within_review_window']: payload['missing_evidence'].append('candidate_window_outside_review')
        result.append({'brief_id': digest(payload), **payload})
    if len(result) != 8:
        raise ValueError('Eight sector drafts are required')
    return result


def cell(brief, identity):
    """Never display an incomplete number as an established metric."""
    row = next((r for r in brief['observations'] if r['id'] == identity), None)
    if row is None or row['status'] != 'observed':
        return 'N/A'
    value = f"{row['value']:,.2f}" if abs(row['value']) < 1e12 else f"{row['value']:.3e}"
    return value


def write_bundle(pack, output, *, benchmark_review=None):
    """Reserve a new directory; publish its completion manifest only after all checks."""
    from sector_brief_pdf import render, inspect
    output = Path(output)
    briefs = assemble(pack, benchmark_review=benchmark_review)
    output.mkdir(parents=False, exist_ok=False)
    # A failure leaves no completed manifest, never overwrites a user's directory,
    # and removes only our TemporaryDirectory, not the reserved parent.
    with TemporaryDirectory(prefix='.building-', dir=output) as temp:
        stage = Path(temp)
        entries = []
        benchmark_reference = None
        if benchmark_review is not None:
            evidence = stage / 'benchmark-review.json'
            evidence.write_text(json.dumps(benchmark_review,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
            if evidence.stat().st_size > 8 * 1024 * 1024:
                raise ValueError('Benchmark evidence exceeds bundle size limit')
            benchmark_reference = {'json':evidence.name,'review_id':benchmark_review['review_id'],
                                   'sha256':hashlib.sha256(evidence.read_bytes()).hexdigest()}
        for brief in briefs:
            stem = brief['sector_id'].removeprefix('sector:') + '-' + brief['as_of']
            if Path(stem).name != stem or '/' in stem or '\\' in stem or '..' in stem:
                raise ValueError('Unsafe sector output identity')
            sidecar = stage / (stem + '.json')
            sidecar.write_text(json.dumps(brief, ensure_ascii=False, indent=2, allow_nan=False) + '\n')
            pdf = stage / (stem + '.pdf')
            if benchmark_review is None: render(brief, pdf, sidecar.name)
            else: render(brief, pdf, sidecar.name, benchmark_review=benchmark_review)
            check = inspect(pdf, brief)
            entries.append({'sector_id': brief['sector_id'], 'brief_id': brief['brief_id'],
                            'pdf': pdf.name, 'json': sidecar.name, 'validation': check,
                            'sha256': {p.suffix[1:]: hashlib.sha256(p.read_bytes()).hexdigest()
                                       for p in (pdf, sidecar)}})
        manifest = {'schema_version': 1, 'dataset_id': pack['dataset_id'], 'as_of': pack['as_of'],
                    'status': 'draft_incomplete_evidence', 'delivery_ready': False, 'briefs': entries}
        if benchmark_reference is not None:
            manifest.update(schema_version=2,benchmark_review=benchmark_reference)
        # Exclusive writes also detect a concurrently inserted file. No implicit merge.
        for path in sorted(stage.iterdir()):
            with (output / path.name).open('xb') as stream:
                stream.write(path.read_bytes())
        with (output / 'manifest.json').open('x') as stream:
            stream.write(json.dumps(manifest, indent=2) + '\n')
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--store', type=Path, required=True)
    parser.add_argument('--as-of', required=True)
    parser.add_argument('--boc-capture', type=Path)
    parser.add_argument('--benchmark-review', type=Path, help='Optional validated candidate review bundle; adds a fifth page')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.output.resolve().is_relative_to(args.store.resolve()):
            raise ValueError('Output must not alter the report archive')
        benchmark = None
        if args.benchmark_review is not None:
            from benchmark_review import load_bundle
            if args.output.resolve().is_relative_to(args.benchmark_review.resolve()):
                raise ValueError('Output must not alter benchmark evidence')
            benchmark = load_bundle(args.benchmark_review)
        pack = build(args.store, as_of=args.as_of, boc_capture=args.boc_capture)
        result = write_bundle(pack, args.output, benchmark_review=benchmark)
    except (OSError, ValueError, TypeError, KeyError, AttributeError):
        parser.error('Brief build failed; check archive integrity and use a new output directory')
    print(f"Built {len(result['briefs'])} sector drafts; delivery readiness remains false")


if __name__ == '__main__':
    main()
