"""Four-page review layout for deterministic sector brief drafts."""
from html import escape
from pathlib import Path

from pypdf import PdfReader
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.pdfgen.canvas import Canvas

from sector_briefs import cell

NAVY = colors.HexColor('#18334B')
TEAL = colors.HexColor('#087E8B')
MUTED = colors.HexColor('#536575')
WIDTH = A4[0] - 88
PAGE_TITLES = ('Coverage and source dates', 'Macro and evidence gaps',
               'Peer valuation snapshot', 'Sources and limitations')


def text(value):
    return str(value).replace('\u2013', '-').replace('\u2014', '-').replace('\u2011', '-').replace('\u2019', "'")


def para(value, *, size=9, bold=False, color=NAVY):
    return Paragraph(escape(text(value)).replace('\n', '<br/>'), ParagraphStyle('body', fontName='Helvetica-Bold' if bold else 'Helvetica',
                     fontSize=size, leading=size * 1.35, textColor=color, spaceAfter=7))


def table(headers, rows, widths, *, size=8):
    body = [[para(h, size=size, bold=True, color=colors.white) for h in headers]]
    body += [[para(c, size=size) for c in row] for row in rows]
    result = Table(body, colWidths=[WIDTH * w for w in widths], repeatRows=1, hAlign='LEFT')
    result.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor('#F0F5F8'), colors.white]),
        ('LEFTPADDING', (0, 0), (-1, -1), 6), ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 5), ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('LINEBELOW', (0, 0), (-1, 0), 1, TEAL),
    ]))
    return result


def render(brief, path, sidecar_name):
    observations = {o['id']: o for o in brief['observations']}
    source_alias = {s['id']: 'S' + str(i + 1).zfill(2) for i, s in enumerate(brief['sources'])}

    def source_for(identity):
        row = observations.get(identity)
        return source_alias.get(row['source_id'], '-') if row else '-'

    def stamp(identity):
        return (observations.get(identity) or {}).get('observed_on') or 'unknown'

    def footer(canvas, doc):
        canvas.saveState()
        canvas.setStrokeColor(TEAL)
        canvas.line(44, 39, A4[0] - 44, 39)
        canvas.setFont('Helvetica', 8)
        canvas.setFillColor(MUTED)
        canvas.drawString(44, 26, 'JSOSIF | Retrospective draft | Not investment advice')
        canvas.drawRightString(A4[0] - 44, 26, f'{doc.page} / 4')
        canvas.restoreState()

    def heading(title):
        return [para('JSOSIF / SECTOR WEEKLY BRIEF', size=9, bold=True, color=TEAL),
                para(brief['name'], size=22, bold=True), para(title, size=13, bold=True),
                para('Cutoff ' + brief['as_of'] + ' | Draft - incomplete evidence', size=9, color=MUTED)]

    story = heading(PAGE_TITLES[0])
    archived = [s for s in brief['stocks'] if s['status'] == 'archived']
    story += [para(f"{len(archived)} / {len(brief['stocks'])} stocks have archived reports. "
                   f"Review window: {brief['review_start']} to {brief['as_of']}. This window does not define return endpoints."),
              para('Each stock belongs to this configurable research group. Industry labels below are provider labels, '
                   'not an independently validated classification. Historical quality is preserved.')]
    rows = []
    for stock in brief['stocks']:
        m = stock['metrics']; close = m.get('stock.Close'); observation = observations.get(close, {})
        report = (stock.get('report_date', 'missing') + '\n' + stock.get('quality', 'missing'))
        if stock.get('in_review_window') is False:
            report += '\nOutside review window'
        value = cell(brief, close)
        if value != 'N/A':
            value += ' ' + (observation.get('currency') or '')
        rows.append([stock['ticker'], stock['industry'] or 'Unavailable', report,
                     value + '\n' + stamp(close) + ' / ' + source_for(close)])
    story += [table(['Stock', 'Provider industry', 'Report / quality', 'Saved close / date / source'],
                    rows, [.12, .30, .24, .34]), Spacer(1, 10),
              para('Coverage is not delivery readiness. No aggregate sector return, investment conclusion or '
                   'freshness upgrade is inferred from these archived values.', color=MUTED), PageBreak()]

    story += heading(PAGE_TITLES[1])
    story += [para('Macro drivers - observations only', size=12, bold=True),
              para('Latest dated value present in selected evidence; no causal sector attribution. Conflicting values '
                   'at the same latest date remain unavailable. Older observations are not refreshed.')]
    rows = []
    for row in brief['macro']:
        value = f"{row['value']:,.3f}" if row['status'] == 'observed' else 'N/A (' + row['status'] + ')'
        references = sorted({source_for(k) for k in row['observation_ids']})
        rows.append([row['subject'].removeprefix('macro:'), value, row['unit'] or '-',
                     row['observed_on'] or 'unknown', ', '.join(references)])
    story += [table(['Series', 'Value', 'Unit', 'Observed on', 'Sources'],
                    rows or [['Unavailable', 'N/A', '-', '-', '-']], [.25, .17, .23, .20, .15])]
    story += [Spacer(1, 12), para('Relative performance', size=12, bold=True),
              para('Unavailable. Proposed benchmark candidates: ' +
                   ', '.join(b['ticker'] + ' (' + b['currency'] + ')' for b in brief['benchmark_candidates']) +
                   '. Listings, aligned calendars, adjustment bases and currency comparability require validation.'),
              para('Industry KPIs and missing evidence', size=12, bold=True)]
    for topic in brief['kpi_topics']:
        story.append(para(topic + ': not collected; applicability must be checked for each issuer.'))
    story += [para('Regulation and next-week events', size=12, bold=True),
              para('Unavailable. No verified event feed, event timestamp or regulatory source is present in this '
                   'package. This means evidence is missing, not that no events exist.'), PageBreak()]

    story += heading(PAGE_TITLES[2])
    story += [para('Provider-selected candidates; P/E ratios shown where available. Alphabetical order is not a ranking. '
                   'Financial periods and valuation bases are unaligned; no cheap/expensive conclusion is implied.'),
              para('Full P/B, EV/EBITDA, market-cap and saved-return evidence, dates and units are in the companion JSON. '
                   'A missing ratio is not zero. No peer is invented to reach a minimum count.')]
    rows = []
    for stock in brief['stocks']:
        peers = []
        for peer in stock['peers']:
            key = peer['metrics'].get('peer.pe')
            peers.append(peer['ticker'] + '\nP/E ' + cell(brief, key) + '\n' + stamp(key) + ' / ' + source_for(key))
        peers += ['Unavailable'] * (5 - len(peers))
        rows.append([stock['ticker'] + '\n' + str(stock['peer_count']) + ' candidates', *peers])
    story += [table(['Covered stock', 'Candidate 1', 'Candidate 2', 'Candidate 3', 'Candidate 4', 'Candidate 5'],
                    rows, [.15, .17, .17, .17, .17, .17], size=7), Spacer(1, 10),
              para('At most five candidates are displayed per stock. Additional candidates, if present, are disclosed '
                   'by the total count. Candidate selection is deterministic alphabetical truncation, not analyst endorsement.',
                   color=MUTED), PageBreak()]

    story += heading(PAGE_TITLES[3])
    story += [para('Evidence ledger', size=12, bold=True),
              para('References below bind displayed metrics to source bytes. Hashes are abbreviated for print; '
                   'the companion JSON retains full SHA-256, observation IDs, source integrity labels, dates and limitations.')]
    rows = []
    for stock in archived:
        relevant = {stock['snapshot_source_id']}
        keys = list(stock['metrics'].values()) + [k for p in stock['peers'] for k in p['metrics'].values() if k]
        for key in keys:
            row = observations[key]
            relevant.update(k for k in (row['source_id'], row['currency_source_id']) if k)
        refs = [source_alias[s['id']] + ' ' + s['kind'] + ' ' + s['sha256'][:10]
                for s in brief['sources'] if s['id'] in relevant]
        rows.append([stock['ticker'], '; '.join(refs)])
    global_sources = [source_alias[s['id']] + ' ' + s['kind'] + ' ' + s['sha256'][:10]
                      for s in brief['sources'] if s['kind'] in ('fred', 'boc', 'research_configuration')]
    rows.append(['Shared', '; '.join(global_sources) or 'Unavailable'])
    story += [table(['Stock / scope', 'Source reference, kind and SHA-256 prefix'], rows, [.15, .85], size=7),
              Spacer(1, 8), para('Risks and limitations', size=11, bold=True)]
    for limitation in brief['limitations']:
        story.append(para(limitation, size=8))
    story += [para('Public attribution: Yahoo Finance; FRED; SEC EDGAR; Bank of Canada Valet. '
                   'Exact public URLs are recorded in each source entry.', size=8),
              para('Companion: ' + sidecar_name, size=8),
              para('Dataset SHA-256: ' + brief['dataset_id'], size=7)]
    doc = SimpleDocTemplate(str(path), pagesize=A4, leftMargin=44, rightMargin=44,
                            topMargin=36, bottomMargin=54, title=brief['name'] + ' - Sector Weekly Brief',
                            author='JSOSIF', pageCompression=1)
    doc.build(story, onFirstPage=footer, onLaterPages=footer,
              canvasmaker=lambda *args, **kwargs: Canvas(*args, **{**kwargs, 'invariant': 1}))


def inspect(path, brief):
    reader = PdfReader(path)
    if reader.is_encrypted or len(reader.pages) != 4:
        raise ValueError('Sector draft must fit its four-page review layout')
    extracted = []
    for i, page in enumerate(reader.pages):
        content = page.extract_text() or ''
        if PAGE_TITLES[i] not in content or 'Draft - incomplete evidence' not in content:
            raise ValueError('Missing section heading or draft label')
        if f'{i + 1} / 4' not in content:
            raise ValueError('Invalid page footer')
        extracted.append(content)
    if any(s['ticker'] not in extracted[0] or s['ticker'] not in extracted[2] for s in brief['stocks']):
        raise ValueError('Missing covered stock')
    if any(section not in '\n'.join(extracted) for section in brief['sections']):
        raise ValueError('Missing weekly template section')
    return {'pages': 4, 'bytes': Path(path).stat().st_size, 'text_characters': sum(map(len, extracted)),
            'visual_review_required': True}
