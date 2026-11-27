"""Build a retrospective RSS evidence index; never fetch, classify or send news."""
import argparse
from collections import Counter
from datetime import timezone
from email.utils import parsedate_to_datetime
import hashlib
import html
import json
from pathlib import Path
import re
from urllib.parse import urlsplit, urlunsplit

from news_decision_audit import decision_flags
from news_freshness import publication_freshness
from report_store import resolve_file, verified_report_files
from shared_research_pack import canonical, digest, exact_date, teams, timestamp, ROOT
from universe import SUPPORTED

MAX_SOURCE_BYTES = 2 * 1024 * 1024
MAX_INDEX_BYTES = 32 * 1024 * 1024
CATEGORIES = ('tailwinds', 'headwinds', 'catalysts', 'risks', 'unclassified', 'irrelevant')
EVENTS = {'unknown', 'acquisition', 'stock_split', 'buyback', 'dividend', 'guidance',
          'lawsuit', 'product', 'partnership', 'analyst', 'workforce', 'earnings',
          'ownership', 'calendar', 'risk', 'market_move'}
LIMITATIONS = [
    'Retrospective archive evidence only; no live refresh or claim of current completeness.',
    'RSS publication timestamps are publisher metadata, not verified event occurrence or scheduled event dates.',
    'Saved classifications are historical predictions, not verified claims, recommendations or calibrated probabilities.',
    'Exact RSS identities deduplicate references, not syndicated stories, independent corroboration or real-world events.',
    'Unmatched, conflicting, missing and invalid evidence remains explicit; no new inference or reclassification.',
    'Source checksums prove local consistency, not publisher authenticity. No point-in-time backtest eligibility.',
    'Draft evidence index only; no standalone newsletter, member attachment, production send or delivery readiness.',
]


def read_bytes(path, limit):
    with Path(path).open('rb') as stream:
        raw = stream.read(limit + 1)
    if len(raw) > limit:
        raise ValueError('News evidence input exceeds size limit')
    return raw


def text(value, limit):
    return value if isinstance(value, str) and 0 < len(value) <= limit and value.strip() and not any(
        ord(c) < 32 or 127 <= ord(c) <= 159 for c in value) else None


def publication(value):
    if text(value, 160) is None:
        return None, 'invalid_or_missing'
    try:
        parsed = parsedate_to_datetime(value)
        if parsed.utcoffset() is None:
            return None, 'timezone_missing'
        return parsed.astimezone(timezone.utc).isoformat(), 'parsed_utc_not_independently_verified'
    except (ValueError, TypeError, OverflowError, AttributeError):
        return None, 'invalid_or_missing'


def public_link(value):
    """Do not propagate credentials, arbitrary query strings or local targets."""
    if text(value, 4096) is None or re.search(r'[\s<>"\\]', value):
        return None
    try:
        u = urlsplit(value)
        host = u.hostname or ''
        if (u.scheme != 'https' or u.username or u.password or u.port not in (None, 443)
                or not re.fullmatch(r'[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,63}', host)
                or host.endswith(('.localhost', '.local', '.internal')) or u.fragment):
            return None
        if host == 'news.google.com':
            if not re.fullmatch(r'/rss/articles/[A-Za-z0-9_-]+', u.path) or u.query not in ('', 'oc=5'):
                return None
        elif u.query:
            return None
        return urlunsplit(('https', host, u.path, '', ''))
    except ValueError:
        return None


def rss_identity(item, *, decision=False):
    if not isinstance(item, dict) or text(item.get('headline'), 2000) is None:
        return None
    fields = {'headline': item['headline'], 'source': item.get('source'),
              'pubDate': item.get('pubDate'), 'link': item.get('url' if decision else 'link')}
    # Preserve missing metadata as null, but reject structured/oversized values.
    for key, limit in (('source', 300), ('pubDate', 160), ('link', 4096)):
        value = fields[key]
        if value is not None and (not isinstance(value, str) or len(value) > limit):
            return None
    return fields


def read_source(root, entry, kind):
    relative = (Path(entry['json']).parent / 'sources' / (entry['ticker'].lower() + '-' + kind + '.json')).as_posix()
    expected = entry.get('source_sha256', {}).get(kind)
    try:
        path = resolve_file(root, relative)
    except ValueError:
        if expected is not None:
            raise ValueError('Tracked news source missing or outside archive') from None
        return None, None
    raw = read_bytes(path, MAX_SOURCE_BYTES)
    actual = hashlib.sha256(raw).hexdigest()
    if expected is not None and actual != expected:
        raise ValueError('News source changed after archive verification')
    source = {'kind': kind, 'sha256': actual, 'integrity': 'archived_expected_hash' if expected else 'observed_hash_only'}
    try:
        value = json.loads(raw)
    except ValueError:
        value = None
    return value, {'id': 'source:' + digest(source), **source}


def saved_decision(category, item, article):
    flags = decision_flags(category, item)
    def enum(name, allowed):
        value = item.get(name)
        if not isinstance(value, str) or value not in allowed:
            flags.append('missing_or_invalid_' + name)
            return None
        return value
    event = enum('event_type', EVENTS)
    sentiment = enum('sentiment', {'positive', 'negative', 'neutral', 'unknown'})
    method = enum('extraction_method', {'rule', 'ai', 'unknown'})
    day = item.get('date')
    try:
        exact_date(day)
    except (ValueError, TypeError):
        day = None
    published = article['published_at']
    if day is None or published is None or day != published[:10]:
        flags.append('saved_date_not_confirmed_by_utc_publication')
    return {'category': category, 'event_type': event, 'sentiment': sentiment, 'method': method,
            'saved_date': day, 'review_flags': sorted(set(flags))}


def build(root, *, as_of, teams_path=None):
    exact_date(as_of)
    root = Path(root)
    configured = teams(teams_path or ROOT / 'config/research_teams.json')
    index = json.loads(read_bytes(root / 'index.json', MAX_INDEX_BYTES))
    if not isinstance(index, dict) or not isinstance(index.get('reports'), list):
        raise ValueError('Archive index required')
    latest, used = {}, set()
    for entry in index['reports']:
        if not isinstance(entry, dict) or not isinstance(entry.get('ticker'), str):
            raise ValueError('Invalid archive identity')
        exact_date(entry.get('as_of'))
        generated = timestamp(entry.get('generated_at'))
        report_id = text(entry.get('report_id'), 300)
        if not generated or not report_id or report_id in used:
            raise ValueError('Ambiguous archive version')
        used.add(report_id)
        ticker = entry['ticker']
        if ticker not in SUPPORTED or entry['as_of'] > as_of:
            continue
        key = (entry['as_of'], generated, report_id)
        if ticker not in latest or key > latest[ticker][0]:
            latest[ticker] = (key, entry)
    articles, sources, reports = {}, {}, []
    for ticker, (_, entry) in sorted(latest.items()):
        verified_report_files(root, entry)
        rss, rss_source = read_source(root, entry, 'rss-items')
        ai, ai_source = read_source(root, entry, 'ai-intel')
        for source in (rss_source, ai_source):
            if source:
                sources[source['id']] = source
        valid_rss = isinstance(rss, list)
        if valid_rss and len(rss) > 500:
            raise ValueError('Too many archived RSS rows')
        counts, selected, invalid = Counter(), {}, 0
        for item in rss if valid_rss else []:
            identity = rss_identity(item)
            if identity is None:
                invalid += 1
                continue
            article_id = 'article:' + digest(identity)
            counts[article_id] += 1
            stamp, stamp_status = publication(identity['pubDate'])
            link = public_link(identity['link'])
            article = {'id': article_id, 'headline': identity['headline'],
                       'publisher': text(identity['source'], 300), 'published_at': stamp,
                       'publication_status': stamp_status, 'url': link,
                       'link_status': 'retained_https_reference' if link else 'missing_or_rejected',
                       'event_date': None, 'point_in_time_eligible': False,
                       'publication_age': publication_freshness(stamp[:10] if stamp else None, as_of)}
            articles[article_id] = article
            selected[article_id] = article
        ai_status = ('missing' if ai_source is None else 'invalid_shape' if not isinstance(ai, dict) else
                     'identity_mismatch' if ai.get('ticker') != ticker or ai.get('as_of') != entry['as_of'] else 'available')
        decisions, unmatched, malformed = {}, Counter(), 0
        if ai_status == 'available':
            rows = []
            for category in CATEGORIES:
                values = ai.get(category, [])
                if not isinstance(values, list):
                    raise ValueError('Invalid saved news category')
                rows.extend((category, item) for item in values)
            if len(rows) > 1000:
                raise ValueError('Too many archived decisions')
            for category, item in rows:
                identity = rss_identity(item, decision=True)
                if identity is None:
                    malformed += 1
                    continue
                article_id = 'article:' + digest(identity)
                if article_id not in selected:
                    unmatched[category] += 1
                    continue
                projected = saved_decision(category, item, selected[article_id])
                decisions.setdefault(article_id, []).append(projected)
        references = []
        for article_id, article in sorted(selected.items()):
            saved = decisions.get(article_id, [])
            distinct = sorted({canonical(d): d for d in saved}.values(), key=canonical)
            references.append({'article_id': article_id, 'rss_occurrences': counts[article_id],
                'saved_decision_occurrences': len(saved), 'saved_decisions': distinct,
                'decision_status': 'missing' if not saved else 'conflicting' if len(distinct) > 1 else 'single_saved_prediction',
                'publication_age_at_report': publication_freshness(
                    article['published_at'][:10] if article['published_at'] else None, entry['as_of']),
                'future_relative_to_report': bool(article['published_at'] and article['published_at'][:10] > entry['as_of'])})
        reports.append({'ticker': ticker, 'report_id': entry['report_id'], 'as_of': entry['as_of'],
            'generated_at': timestamp(entry['generated_at']), 'snapshot_sha256': entry['sha256']['json'],
            'archived_quality': entry['quality'], 'sector_ids': [t['id'] for t in configured if ticker in t['tickers']],
            'rss_source_id': rss_source['id'] if rss_source else None, 'ai_source_id': ai_source['id'] if ai_source else None,
            'rss_status': 'available' if valid_rss else 'missing' if rss_source is None else 'invalid_shape',
            'ai_status': ai_status, 'raw_rss_rows': len(rss) if valid_rss else 0,
            'invalid_rss_rows': invalid, 'unmatched_decisions': sum(unmatched.values()),
            'unmatched_decisions_by_category': dict(sorted(unmatched.items())), 'malformed_decisions': malformed,
            'references': references})
    payload = {'schema_version': 1, 'kind': 'news_evidence_index', 'as_of': as_of,
        'status': 'draft_incomplete_evidence', 'delivery_ready': False,
        'temporal_scope': 'retrospective_reconstruction_not_point_in_time',
        'sectors': [{'id': t['id'], 'name': t['name'], 'tickers': t['tickers']} for t in configured],
        'missing_reports': sorted(set(SUPPORTED) - set(latest)), 'reports': reports,
        'articles': sorted(articles.values(), key=lambda r: r['id']),
        'sources': sorted(sources.values(), key=lambda r: r['id']), 'limitations': LIMITATIONS}
    return {'index_id': digest(payload), **payload}


def escape(value):
    return re.sub(r'([\\`*_{}\[\]()#+.!|~-])', r'\\\1', html.escape(str(value), quote=True))


def markdown(value):
    lines = ['# News evidence review', '', 'Cutoff: ' + value['as_of'] + ' | Retrospective draft | Delivery readiness: false', '']
    lines += [escape(s) for s in value['limitations']]
    lines += ['', '## Archive coverage', '', '| Stock | Report date | RSS | Unique references | Missing / conflicting decisions |',
              '| --- | --- | --- | --- | --- |']
    for r in value['reports']:
        missing = sum(x['decision_status'] == 'missing' for x in r['references'])
        conflicts = sum(x['decision_status'] == 'conflicting' for x in r['references'])
        lines.append(f"| {r['ticker']} | {r['as_of']} | {r['rss_status']} | {len(r['references'])} | {missing} / {conflicts} |")
    # Bounded human review only; JSON preserves every article and per-report decision.
    ordered = sorted(value['articles'], key=lambda a: (a['published_at'] or '', a['id']), reverse=True)
    lines += ['', '## Publication chronology', '', f'Showing {min(100, len(ordered))} of {len(ordered)} exact RSS identities, newest first. '
              'Future metadata stays flagged; missing dates sort last. This is not an event calendar or importance ranking.', '']
    for a in ordered[:100]:
        context = [(r['ticker'], ref) for r in value['reports'] for ref in r['references'] if ref['article_id'] == a['id']]
        tickers = [ticker for ticker, _ in context]
        predictions = '; '.join(ticker + ': ' + ref['decision_status'] + ' [' + ', '.join(
            d['category'] + '/' + (d['event_type'] or 'event unavailable') for d in ref['saved_decisions']) + ']'
            for ticker, ref in context)
        lines += ['### ' + escape(a['headline']), '',
            escape(', '.join(tickers) + ' | ' + (a['publisher'] or 'publisher unavailable') + ' | ' +
                   (a['published_at'] or 'publication time unavailable') + ' | ' + a['publication_age']['label']), '',
            ('[Archived RSS reference](<' + a['url'] + '>)' if a['url'] else 'Source link missing or rejected.'), '',
            'Saved predictions, not verified events: ' + escape(predictions), '',
            'Evidence ID: `' + a['id'] + '`', '']
    lines += ['## Full evidence', '', 'All article identities, source hashes, report references, saved decisions and gaps are in news-evidence.json.', '',
              'Index SHA-256: `' + value['index_id'] + '`', '']
    return '\n'.join(lines)


def write_bundle(value, output, *, store):
    output = Path(output)
    if output.resolve().is_relative_to(Path(store).resolve()) or output.resolve().is_relative_to(ROOT):
        raise ValueError('Output must be outside source repository and report store')
    raw = {'news-evidence.json': (json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + '\n').encode(),
           'news-review.md': markdown(value).encode()}
    manifest = {'schema_version': 1, 'kind': value['kind'], 'index_id': value['index_id'],
                'as_of': value['as_of'], 'delivery_ready': False,
                'sha256': {name: hashlib.sha256(content).hexdigest() for name, content in raw.items()}}
    output.mkdir(parents=False, exist_ok=False)
    for name, content in (*raw.items(), ('manifest.json', (json.dumps(manifest, indent=2) + '\n').encode())):
        with (output / name).open('xb') as stream:
            stream.write(content)
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--store', type=Path, required=True)
    parser.add_argument('--as-of', required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    try:
        value = build(args.store, as_of=args.as_of)
        write_bundle(value, args.output, store=args.store)
    except (OSError, ValueError, KeyError, TypeError, AttributeError):
        parser.error('News evidence build failed; check archive integrity and a new output directory')
    print(f"News evidence: {len(value['reports'])} reports, {len(value['articles'])} RSS identities; retrospective draft only")


if __name__ == '__main__':
    main()
