"""Render and verify a standalone retrospective news review draft."""
import argparse
from copy import deepcopy
import hashlib
from html import escape
from io import BytesIO
import json
import os
from pathlib import Path
import re
import unicodedata

from pypdf import PdfReader
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Spacer, PageBreak, Paragraph
from reportlab.pdfgen.canvas import Canvas

import news_evidence as evidence
from news_freshness import publication_freshness
from report_store import resolve_file
from sector_brief_pdf import para, table, TEAL, MUTED
from shared_research_pack import digest, exact_date, timestamp, teams, ROOT
from universe import SUPPORTED

MAX_JSON = 8 * 1024 * 1024
MAX_PDF = 20 * 1024 * 1024
HEADINGS = ('News evidence snapshot', 'Publication chronology / 1',
            'Publication chronology / 2', 'Stock coverage and source gaps')
LIMITATIONS = [
    'Retrospective draft, not current news intelligence. No provider refresh or model inference.',
    'Publication time is RSS metadata, not a verified event date. No event calendar is inferred.',
    'Saved predictions may be wrong or conflicting. No importance ranking or investment recommendation.',
    'Eight latest dated identities at or before the cutoff are shown; future and undated evidence stays in JSON.',
    'Exact duplicate identities do not establish independent corroboration. Full per-stock context stays in JSON.',
    'PDF display uses ASCII normalization and marked shortening; original headlines and URLs stay in JSON.',
    'Checksums establish consistency, not publisher authentication or point-in-time backtest eligibility.',
    'Incomplete draft only. Delivery readiness is false; private preview opt-in does not authorize sending.',
]
SCOPED_LIMITATIONS = LIMITATIONS + [
    'Filtered by archived report references for the requested stocks, not inferred headline relevance.',
    'The eight-story cap is chronological across this scope; it does not guarantee a story for every requested stock.',
]


def normalize_tickers(tickers):
    if (not isinstance(tickers, (list, tuple)) or not tickers or
            any(not isinstance(t, str) or t not in SUPPORTED for t in tickers)):
        raise ValueError('News scope requires nonempty supported stock symbols')
    return sorted(set(tickers))


def artifact_stem(value):
    return 'news-review-' + value['as_of'] + ('-' + value['review_id'][:16] if value['schema_version'] == 2 else '')


def fingerprint(value):
    return isinstance(value, str) and bool(re.fullmatch('[0-9a-f]{64}', value))


def count(value):
    return type(value) is int and value >= 0


def registry(rows, prefix):
    if not isinstance(rows, list) or any(not isinstance(r, dict) or not isinstance(r.get('id'), str)
            or not r['id'].startswith(prefix) or not fingerprint(r['id'][len(prefix):]) for r in rows):
        raise ValueError('Invalid news registry')
    result = {r['id']: r for r in rows}
    if len(result) != len(rows):
        raise ValueError('Duplicate news identity')
    return result


def validate_evidence(value):
    """Validate retained evidence and derived fields, not publisher authenticity."""
    scoped = isinstance(value, dict) and value.get('schema_version') == 2
    keys = {'index_id', 'schema_version', 'kind', 'as_of', 'status', 'delivery_ready', 'temporal_scope',
            'sectors', 'missing_reports', 'reports', 'articles', 'sources', 'limitations'}
    if scoped:
        keys |= {'scope_tickers', 'parent_index_id'}
    if (not isinstance(value, dict) or set(value) != keys
            or value.get('index_id') != digest({k:v for k,v in value.items() if k != 'index_id'})
            or type(value.get('schema_version')) is not int or value['schema_version'] not in (1, 2)
            or value.get('kind') != ('scoped_news_evidence_index' if scoped else 'news_evidence_index')
            or value.get('status') != 'draft_incomplete_evidence'
            or value.get('delivery_ready') is not False
            or value.get('temporal_scope') != 'retrospective_reconstruction_not_point_in_time'
            or value.get('limitations') != evidence.LIMITATIONS):
        raise ValueError('Invalid news evidence contract')
    cutoff = exact_date(value['as_of'])
    configured = [{'id': t['id'], 'name': t['name'], 'tickers': t['tickers']}
                  for t in teams(ROOT / 'config/research_teams.json')]
    universe = set(SUPPORTED)
    if scoped:
        if value['scope_tickers'] != normalize_tickers(value['scope_tickers']) or not fingerprint(value['parent_index_id']):
            raise ValueError('Invalid news evidence scope')
        universe = set(value['scope_tickers'])
        configured = [dict(t, tickers=sorted(set(t['tickers']) & universe)) for t in configured if set(t['tickers']) & universe]
    if value['sectors'] != configured:
        raise ValueError('News taxonomy mismatch')
    articles = registry(value['articles'], 'article:')
    sources = registry(value['sources'], 'source:')
    for s in sources.values():
        if (set(s) != {'id', 'kind', 'sha256', 'integrity'} or not fingerprint(s['sha256'])
                or s['id'] != 'source:' + digest({k:v for k,v in s.items() if k != 'id'})
                or s['kind'] not in ('rss-items', 'ai-intel')
                or s['integrity'] not in ('archived_expected_hash', 'observed_hash_only')):
            raise ValueError('Invalid news source')
    for a in articles.values():
        if (set(a) != {'id', 'headline', 'publisher', 'published_at', 'publication_status', 'url',
                'link_status', 'event_date', 'point_in_time_eligible', 'publication_age'}
                or not evidence.text(a['headline'], 2000)
                or a['publisher'] is not None and not evidence.text(a['publisher'], 300)
                or a['event_date'] is not None or a['point_in_time_eligible'] is not False):
            raise ValueError('Invalid article claim')
        stamp = a['published_at']
        if stamp is not None:
            if timestamp(stamp) != stamp or a['publication_status'] != 'parsed_utc_not_independently_verified':
                raise ValueError('Invalid publication timestamp')
        elif a['publication_status'] not in ('invalid_or_missing', 'timezone_missing'):
            raise ValueError('Invalid missing publication status')
        if (a['publication_age'] != publication_freshness(stamp[:10] if stamp else None, value['as_of'])
                or a['url'] is not None and (evidence.public_link(a['url']) != a['url'] or
                    a['link_status'] != 'retained_https_reference')
                or a['url'] is None and a['link_status'] != 'missing_or_rejected'):
            raise ValueError('Invalid article metadata')
    tickers, report_ids, used_articles, used_sources = set(), set(), set(), set()
    if not isinstance(value['reports'], list) or len(value['reports']) > len(SUPPORTED):
        raise ValueError('Invalid report coverage')
    allowed_flags = {'negative_sentiment_in_tailwinds', 'positive_sentiment_in_headwinds',
        'short_term_price_move_in_structural_risks', 'directional_claim_without_event_type',
        'low_uncalibrated_model_confidence', 'missing_or_invalid_event_type',
        'missing_or_invalid_sentiment', 'missing_or_invalid_extraction_method',
        'saved_date_not_confirmed_by_utc_publication'}
    for r in value['reports']:
        if not isinstance(r, dict) or set(r) != {'ticker', 'report_id', 'as_of', 'generated_at', 'snapshot_sha256',
                'archived_quality', 'sector_ids', 'rss_source_id', 'ai_source_id', 'rss_status', 'ai_status',
                'raw_rss_rows', 'invalid_rss_rows', 'unmatched_decisions', 'unmatched_decisions_by_category',
                'malformed_decisions', 'references'}:
            raise ValueError('Invalid news report fields')
        ticker = r['ticker']
        if (ticker not in universe or ticker in tickers or not evidence.text(r['report_id'], 300)
                or r['report_id'] in report_ids or exact_date(r['as_of']) > cutoff
                or not timestamp(r['generated_at']) or timestamp(r['generated_at']) != r['generated_at'] or not fingerprint(r['snapshot_sha256'])
                or r['sector_ids'] != [s['id'] for s in configured if ticker in s['tickers']]):
            raise ValueError('Invalid news report lineage')
        tickers.add(ticker); report_ids.add(r['report_id'])
        for field, kind in (('rss_source_id', 'rss-items'), ('ai_source_id', 'ai-intel')):
            key = r[field]
            if key is not None:
                if key not in sources or sources[key]['kind'] != kind:
                    raise ValueError('Missing news source reference')
                used_sources.add(key)
        if (r['rss_status'] not in ('available', 'missing', 'invalid_shape')
                or r['ai_status'] not in ('available', 'missing', 'invalid_shape', 'identity_mismatch')
                or (r['rss_status'] == 'missing') != (r['rss_source_id'] is None)
                or (r['ai_status'] == 'missing') != (r['ai_source_id'] is None)
                or any(not count(r[k]) for k in ('raw_rss_rows', 'invalid_rss_rows', 'unmatched_decisions', 'malformed_decisions'))
                or r['raw_rss_rows'] > 500
                or not isinstance(r['references'], list) or len(r['references']) > 500
                or not isinstance(r['unmatched_decisions_by_category'], dict)
                or any(k not in evidence.CATEGORIES or not count(v) for k,v in r['unmatched_decisions_by_category'].items())
                or sum(r['unmatched_decisions_by_category'].values()) != r['unmatched_decisions']):
            raise ValueError('Invalid news coverage counts')
        seen = set(); occurrences = 0
        for ref in r['references']:
            if not isinstance(ref, dict) or set(ref) != {'article_id', 'rss_occurrences', 'saved_decision_occurrences',
                    'saved_decisions', 'decision_status', 'publication_age_at_report', 'future_relative_to_report'}:
                raise ValueError('Invalid news reference fields')
            key = ref['article_id']
            if key not in articles or key in seen or not count(ref['rss_occurrences']) or ref['rss_occurrences'] == 0:
                raise ValueError('Invalid news article reference')
            seen.add(key); used_articles.add(key); occurrences += ref['rss_occurrences']
            stamp = articles[key]['published_at']
            saved = ref['saved_decisions']
            if not isinstance(saved, list) or len(saved) > 1000 or len({digest(d) for d in saved}) != len(saved):
                raise ValueError('Invalid saved predictions')
            for d in saved:
                if (set(d) != {'category', 'event_type', 'sentiment', 'method', 'saved_date', 'review_flags'}
                        or d['category'] not in evidence.CATEGORIES or d['event_type'] not in evidence.EVENTS | {None}
                        or d['sentiment'] not in {'positive', 'negative', 'neutral', 'unknown', None}
                        or d['method'] not in {'rule', 'ai', 'unknown', None}
                        or not isinstance(d['review_flags'], list) or any(f not in allowed_flags for f in d['review_flags'])):
                    raise ValueError('Invalid saved prediction metadata')
                if d['saved_date'] is not None:
                    exact_date(d['saved_date'])
            if (not count(ref['saved_decision_occurrences']) or ref['saved_decision_occurrences'] < len(saved)
                    or not saved and ref['saved_decision_occurrences'] != 0
                    or saved and r['ai_status'] != 'available'
                    or ref['decision_status'] != ('missing' if not saved else 'conflicting' if len(saved) > 1 else 'single_saved_prediction')
                    or ref['publication_age_at_report'] != publication_freshness(stamp[:10] if stamp else None, r['as_of'])
                    or ref['future_relative_to_report'] is not bool(stamp and stamp[:10] > r['as_of'])):
                raise ValueError('Invalid prediction summary')
        if (occurrences + r['invalid_rss_rows'] != r['raw_rss_rows'] or r['rss_status'] != 'available' and occurrences
                or sum(ref['saved_decision_occurrences'] for ref in r['references']) + r['unmatched_decisions'] + r['malformed_decisions'] > 1000):
            raise ValueError('Invalid RSS accounting')
    if (value['missing_reports'] != sorted(universe - tickers)
            or used_articles != set(articles) or used_sources != set(sources)):
        raise ValueError('Unreferenced news evidence or coverage mismatch')
    return value


def derived(index):
    refs = [ref for r in index['reports'] for ref in r['references']]
    ordered = sorted((a for a in index['articles'] if a['published_at'] and a['published_at'][:10] <= index['as_of']),
                     key=lambda a: (a['published_at'], a['id']), reverse=True)
    return {'selected_article_ids': [a['id'] for a in ordered[:8]],
        'summary': {'stocks': len(index['reports']), 'articles': len(index['articles']), 'references': len(refs),
            'sources': len(index['sources']), 'missing_predictions': sum(r['decision_status'] == 'missing' for r in refs),
            'conflicting_predictions': sum(r['decision_status'] == 'conflicting' for r in refs),
            'unmatched_predictions': sum(r['unmatched_decisions'] for r in index['reports']),
            'undated_articles': sum(a['published_at'] is None for a in index['articles']),
            'future_articles': sum(a['publication_age']['label'] == 'future_dated' for a in index['articles'])},
        'report_versions': {r['ticker']: {k:r[k] for k in ('report_id', 'as_of', 'snapshot_sha256')}
                            for r in index['reports']}}


def assemble(index, *, parent_review_id=None):
    validate_evidence(index)
    scoped = index['schema_version'] == 2
    if scoped and not fingerprint(parent_review_id):
        raise ValueError('Scoped review requires parent identity')
    payload = {'schema_version': 2 if scoped else 1, 'kind': 'news_review', 'as_of': index['as_of'],
        'status': 'draft_incomplete_evidence', 'delivery_ready': False, 'evidence': index,
        **derived(index), 'limitations': SCOPED_LIMITATIONS if scoped else LIMITATIONS}
    if scoped:
        payload['scope'] = {'mode': 'selected_stocks', 'tickers': index['scope_tickers'], 'parent_review_id': parent_review_id}
    return {'review_id': digest(payload), **payload}


def validate_review(value):
    scoped = isinstance(value, dict) and value.get('schema_version') == 2
    keys = {'review_id', 'schema_version', 'kind', 'as_of', 'status', 'delivery_ready', 'evidence',
            'selected_article_ids', 'summary', 'report_versions', 'limitations'} | ({'scope'} if scoped else set())
    if (not isinstance(value, dict) or set(value) != keys
            or type(value['schema_version']) is not int or value['schema_version'] not in (1, 2)
            or value['kind'] != 'news_review' or value['status'] != 'draft_incomplete_evidence'
            or value['delivery_ready'] is not False or value['limitations'] != (SCOPED_LIMITATIONS if scoped else LIMITATIONS)
            or value['review_id'] != digest({k:v for k,v in value.items() if k != 'review_id'})):
        raise ValueError('Invalid news review contract')
    validate_evidence(value['evidence'])
    if value['evidence']['schema_version'] != value['schema_version']:
        raise ValueError('News review and evidence scope versions disagree')
    if scoped:
        scope = value['scope']
        if (not isinstance(scope, dict) or set(scope) != {'mode', 'tickers', 'parent_review_id'}
                or scope['mode'] != 'selected_stocks' or scope['tickers'] != value['evidence']['scope_tickers']
                or not fingerprint(scope['parent_review_id'])):
            raise ValueError('News review scope disagrees with evidence')
    if value['as_of'] != value['evidence']['as_of'] or any(value[k] != v for k,v in derived(value['evidence']).items()):
        raise ValueError('News review differs from retained evidence')
    return value


def scope_review(value, tickers):
    """Project verified retained evidence without re-reading the archive or inferring relevance."""
    validate_review(value)
    tickers = normalize_tickers(tickers)
    if value['schema_version'] == 2 and not set(tickers) <= set(value['scope']['tickers']):
        raise ValueError('Cannot widen a previously scoped news review')
    index = deepcopy(value['evidence'])
    parent = index['index_id']
    index['reports'] = [r for r in index['reports'] if r['ticker'] in tickers]
    article_ids = {ref['article_id'] for r in index['reports'] for ref in r['references']}
    source_ids = {r[k] for r in index['reports'] for k in ('rss_source_id', 'ai_source_id') if r[k]}
    index['articles'] = [a for a in index['articles'] if a['id'] in article_ids]
    index['sources'] = [s for s in index['sources'] if s['id'] in source_ids]
    index['sectors'] = [dict(s, tickers=sorted(set(s['tickers']) & set(tickers)))
                        for s in index['sectors'] if set(s['tickers']) & set(tickers)]
    index.update(schema_version=2, kind='scoped_news_evidence_index', scope_tickers=tickers,
                 parent_index_id=parent, missing_reports=sorted(set(tickers) - {r['ticker'] for r in index['reports']}))
    index['index_id'] = digest({k:v for k,v in index.items() if k != 'index_id'})
    return validate_review(assemble(index, parent_review_id=value['review_id']))


def scoped_attachment(loaded, tickers):
    value = scope_review(loaded['review'], tickers)
    raw = render(value); inspect_pdf(raw, value)
    if len(raw) > MAX_PDF:
        raise ValueError('Scoped news PDF exceeds size limit')
    return {'review_id': value['review_id'], 'as_of': value['as_of'], 'report_versions': value['report_versions'],
            'filename': artifact_stem(value) + '.pdf', 'sha256': hashlib.sha256(raw).hexdigest(),
            'bytes': raw, 'scope': value['scope']}


def display(value, limit=240):
    text = str(value).replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')
    text = text.replace('\u2013', '-').replace('\u2014', '-').replace('\u2026', '...')
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode().strip()
    return (text[:limit] + ' [shortened]' if len(text) > limit else text) or '[See original text in JSON]'


def render(value):
    out = BytesIO(); index = value['evidence']; summary = value['summary']
    def header(title):
        return [para('JSOSIF / NEWS REVIEW', size=10, bold=True, color=TEAL), para(title, size=21, bold=True),
                para('Cutoff ' + value['as_of'] + ' | Draft - incomplete evidence', size=9, color=MUTED)] + (
                    [para(f"Selected-stock scope: {len(value['scope']['tickers'])} requested stocks", size=8, color=TEAL)]
                    if value['schema_version'] == 2 else [])
    def footer(canvas, doc):
        canvas.saveState(); canvas.setStrokeColor(TEAL); canvas.line(44, 39, A4[0]-44, 39)
        canvas.setFont('Helvetica', 8); canvas.setFillColor(MUTED)
        canvas.drawString(44, 26, 'JSOSIF | Retrospective draft | Not investment advice')
        canvas.drawRightString(A4[0]-44, 26, f'{doc.page} / 4'); canvas.restoreState()
    story = header(HEADINGS[0])
    story += [para('A sourced headline review for analyst preparation. Article text and claims have not been '
                   'independently verified. Publication chronology is not an event calendar.'),
        table(['Archived stocks', 'Exact RSS identities', 'Report references', 'Source versions'],
              [[summary[k] for k in ('stocks', 'articles', 'references', 'sources')]], [.25]*4), Spacer(1, 15),
        para('Evidence requiring review', size=13, bold=True),
        table(['Review gap', 'Count'], [['No exact saved prediction', summary['missing_predictions']],
            ['Conflicting saved predictions', summary['conflicting_predictions']],
            ['Unmatched saved prediction rows', summary['unmatched_predictions']],
            ['Undated / future article metadata', f"{summary['undated_articles']} / {summary['future_articles']}"]], [.75, .25]),
        Spacer(1, 12), para('Reading this draft', size=13, bold=True)]
    story += [para(line, size=9) for line in value['limitations']]
    story += [para('Evidence index SHA-256: ' + index['index_id'], size=7),
              para('Review SHA-256: ' + value['review_id'], size=7), PageBreak()]
    articles = {a['id']: a for a in index['articles']}
    for page in (1, 2):
        story += header(HEADINGS[page])
        story += [para(f"Showing up to eight dated identities, newest first; {len(value['selected_article_ids'])} selected "
                       f"from {summary['articles']} retained identities. Full original text and all stock contexts are in JSON.", size=8)]
        selected = value['selected_article_ids'][(page-1)*4:page*4]
        if not selected:
            story += [Spacer(1, 30), para('No additional eligible dated headlines', size=14, bold=True),
                      para('Missing and future publication metadata remains in the evidence companion. No substitute headline is inferred.')]
        for key in selected:
            a = articles[key]
            context = [(r['ticker'], ref) for r in index['reports'] for ref in r['references'] if ref['article_id'] == key]
            labels = {'missing': 'no exact prediction', 'conflicting': 'conflicting predictions', 'single_saved_prediction': 'saved prediction'}
            predictions = '; '.join(t + ': ' + labels[ref['decision_status']] +
                (' / ' + ', '.join(d['category'] for d in ref['saved_decisions']) if ref['saved_decisions'] else '') for t, ref in context)
            story += [Spacer(1, 8), para(display(a['headline']), size=11, bold=True),
                      para(display(a['publisher'] or 'Publisher unknown', 70) + ' | ' + a['published_at'] +
                           ' | age ' + str(a['publication_age']['age_days']) + ' days', size=8, color=MUTED),
                      para('Saved predictions: ' + display(predictions, 180), size=8),
                      para('Evidence: ' + key.removeprefix('article:'), size=7)]
            story.append(Paragraph('<link href="' + escape(a['url'], quote=True) + '">Archived RSS reference</link>'
                if a['url'] else 'Source link unavailable or rejected', ParagraphStyle('link', fontName='Helvetica',
                    fontSize=8, leading=10, textColor=TEAL, spaceAfter=4)))
        story.append(PageBreak())
    story += header(HEADINGS[3])
    story += [para('Counts: unique references / missing exact prediction / conflicting prediction. '
                   '* means RSS source missing or malformed. A dash means no selected stock report.', size=8)]
    rows = {r['ticker']: r for r in index['reports']}
    def cells(ticker):
        r = rows.get(ticker)
        if r is None:
            return [ticker, '-']
        refs = r['references']
        return [ticker + ('*' if r['rss_status'] != 'available' else ''),
                f"{len(refs)} / {sum(x['decision_status'] == 'missing' for x in refs)} / {sum(x['decision_status'] == 'conflicting' for x in refs)}"]
    tickers = value['scope']['tickers'] if value['schema_version'] == 2 else sorted(SUPPORTED)
    middle = (len(tickers)+1)//2
    story += [table(['Stock', 'References / gaps', 'Stock', 'References / gaps'],
        [cells(tickers[i]) + (cells(tickers[i+middle]) if i+middle < len(tickers) else ['', '']) for i in range(middle)],
        [.16, .34, .16, .34], size=7),
        para('All source hashes, report versions, original headlines, URLs and prediction flags are retained in '
             + artifact_stem(value) + '.json. Hashes are not provider signatures.', size=8)]
    doc = SimpleDocTemplate(out, pagesize=A4, leftMargin=44, rightMargin=44, topMargin=36, bottomMargin=54,
                            title='JSOSIF News Review - ' + value['as_of'], author='JSOSIF')
    doc.build(story, onFirstPage=footer, onLaterPages=footer,
              canvasmaker=lambda *a, **kw: Canvas(*a, **{**kw, 'invariant': 1}))
    return out.getvalue()


def inspect_pdf(raw, value):
    reader = PdfReader(BytesIO(raw))
    if reader.is_encrypted or len(reader.pages) != 4:
        raise ValueError('News draft must fit four pages')
    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ''
        if HEADINGS[i] not in text or 'Draft - incomplete evidence' not in text or value['as_of'] not in text or f'{i+1} / 4' not in text:
            raise ValueError('Missing news draft identity')
        if value['schema_version'] == 2 and 'Selected-stock scope:' not in text:
            raise ValueError('Missing news scope disclosure')
    for i, key in enumerate(value['selected_article_ids']):
        if key.removeprefix('article:') not in (reader.pages[1+i//4].extract_text() or ''):
            raise ValueError('Missing selected news evidence reference')
    return {'pages': 4, 'bytes': len(raw), 'visual_review_required': True}


def write_bundle(value, output, *, store):
    validate_review(value)
    output = Path(output)
    if output.resolve().is_relative_to(Path(store).resolve()) or output.resolve().is_relative_to(ROOT):
        raise ValueError('Output must be outside repository and archive')
    raw_pdf = render(value); check = inspect_pdf(raw_pdf, value)
    raw_json = (json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + '\n').encode()
    if len(raw_json) > MAX_JSON or len(raw_pdf) > MAX_PDF:
        raise ValueError('News artifact exceeds bundle limit')
    stem = artifact_stem(value)
    manifest = {'schema_version': value['schema_version'], 'kind': 'news_review', 'review_id': value['review_id'],
        'as_of': value['as_of'], 'status': value['status'], 'delivery_ready': False,
        'pdf': stem+'.pdf', 'json': stem+'.json', 'validation': check,
        'sha256': {'pdf': hashlib.sha256(raw_pdf).hexdigest(), 'json': hashlib.sha256(raw_json).hexdigest()}}
    private = value['schema_version'] == 2
    output.mkdir(mode=0o700 if private else 0o777, parents=False, exist_ok=False)
    for name, raw in ((manifest['pdf'], raw_pdf), (manifest['json'], raw_json),
                      ('manifest.json', (json.dumps(manifest, indent=2)+'\n').encode())):
        if private:
            fd = os.open(output/name, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
            with os.fdopen(fd, 'wb') as stream:
                stream.write(raw)
        else:
            with (output/name).open('xb') as stream:
                stream.write(raw)
    return manifest


def load_bundle(root):
    if root is None:
        return None
    def read(name, limit):
        return evidence.read_bytes(resolve_file(root, name), limit)
    manifest = json.loads(read('manifest.json', 2*1024*1024))
    if (type(manifest.get('schema_version')) is not int or manifest['schema_version'] not in (1, 2)
            or manifest.get('kind') != 'news_review' or manifest.get('status') != 'draft_incomplete_evidence'
            or manifest.get('delivery_ready') is not False or not fingerprint(manifest.get('review_id'))):
        raise ValueError('Invalid news draft manifest')
    exact_date(manifest['as_of']); loaded = {}
    for kind, limit in (('json', MAX_JSON), ('pdf', MAX_PDF)):
        if manifest[kind] != artifact_stem(manifest) + '.' + kind:
            raise ValueError('Invalid news filename')
        raw = read(manifest[kind], limit)
        if hashlib.sha256(raw).hexdigest() != manifest['sha256'][kind]:
            raise ValueError('News artifact checksum mismatch')
        loaded[kind] = raw
    value = validate_review(json.loads(loaded['json']))
    if any(value[k] != manifest[k] for k in ('schema_version', 'review_id', 'as_of', 'status', 'delivery_ready')):
        raise ValueError('News manifest and companion disagree')
    inspect_pdf(loaded['pdf'], value)
    return {'review_id': value['review_id'], 'as_of': value['as_of'], 'report_versions': value['report_versions'],
            'filename': manifest['pdf'], 'sha256': manifest['sha256']['pdf'], 'bytes': loaded['pdf'], 'review': value}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--store', type=Path, required=True); parser.add_argument('--as-of', required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--tickers', nargs='+', help='Optional supported stock scope; produces a private bundle')
    args = parser.parse_args()
    try:
        value = assemble(evidence.build(args.store, as_of=args.as_of))
        if args.tickers is not None:
            value = scope_review(value, args.tickers)
        write_bundle(value, args.output, store=args.store)
    except (OSError, ValueError, TypeError, KeyError, AttributeError):
        parser.error('News draft failed; verify archive and use a new output directory')
    print('Built standalone news review draft; no refresh or send')


if __name__ == '__main__':
    main()
