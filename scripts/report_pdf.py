#!/usr/bin/env python3
"""Generate a clean, readable PDF version of the ticker intelligence report.

Reads the same JSON snapshots as regenerate_report.py and renders a
print-friendly PDF with reportlab:
  - clear section headings, tidy tables, sensible font sizes
  - sources rendered as blue clickable hyperlinks (no raw long URLs)

Usage: python scripts/report_pdf.py --ticker ACN
Output: reports/<TICKER>-intelligence-<YYYYMMDD>.pdf
"""
import html as html_lib
import json
import re
import sys
import urllib.parse
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate,
                                Paragraph, Spacer, Table, TableStyle,
                                KeepTogether)

from data_utils import DATA, REPORTS, ticker_arg, ticker_file, as_of_date, number
from metric_interpretation import build_interpretation_section

TICKER = ticker_arg()
AS_OF = as_of_date().isoformat()
STAMP = AS_OF.replace('-', '')

NAVY = colors.HexColor('#1F3A5F')
LINK_BLUE = colors.HexColor('#1155CC')
LIGHT_GREY = colors.HexColor('#F2F4F7')
MID_GREY = colors.HexColor('#D9DEE6')
DARK = colors.HexColor('#1A1A1A')
MUTED = colors.HexColor('#5A6472')


def esc(text):
    return html_lib.escape('' if text is None else str(text), quote=False)


def esc_url(url):
    return url.replace('&', '&amp;').replace('"', '&quot;')


def link(url, text):
    """Blue clickable hyperlink; never shows the raw URL."""
    if not url:
        return esc(text)
    return f'<a href="{esc_url(url)}" color="#1155CC"><u>{esc(text)}</u></a>'


def domain_of(url):
    try:
        netloc = urllib.parse.urlparse(url).netloc.lower()
        return netloc[4:] if netloc.startswith('www.') else netloc
    except Exception:
        return 'link'


def source_label(item, fallback_n):
    """Short human-readable label for a source hyperlink."""
    pub = (item.get('source') or '').strip()
    if pub:
        return pub
    urls = item.get('sources') or ([item.get('url')] if item.get('url') else [])
    if urls:
        return domain_of(urls[0])
    return f'Source {fallback_n}'


def primary_url(item):
    urls = item.get('sources') or ([item.get('url')] if item.get('url') else [])
    return urls[0] if urls else ''


def read_snapshot(name):
    return json.loads((DATA / ticker_file(TICKER, name)).read_text(encoding='utf-8'))


quant = read_snapshot('quant.json')
q = quant['metrics']
ai = read_snapshot('ai-intel.json')
rss = read_snapshot('rss-items.json')
peers_doc = read_snapshot('comparables.json')
earnings = read_snapshot('earnings.json')
macro = json.loads((DATA / 'fred.json').read_text(encoding='utf-8'))
edgar = read_snapshot('edgar.json')
info = read_snapshot('info.json')

link_by_headline = {it['headline']: it['link'] for it in rss if it.get('link')}


def fmt(v, d=4):
    v = number(v)
    return 'N/A' if v is None else f'{v:.{d}f}'


# ---------------------------------------------------------------- styles
styles = {}
styles['title'] = ParagraphStyle('Title2', fontName='Helvetica-Bold', fontSize=20,
                                 leading=24, textColor=NAVY, spaceAfter=4)
styles['subtitle'] = ParagraphStyle('Subtitle2', fontName='Helvetica', fontSize=10,
                                    leading=14, textColor=MUTED, spaceAfter=2)
styles['h1'] = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=13,
                              leading=16, textColor=NAVY, spaceBefore=16,
                              spaceAfter=8, keepWithNext=True)
styles['h2'] = ParagraphStyle('H2', fontName='Helvetica-Bold', fontSize=11,
                              leading=14, textColor=DARK, spaceBefore=10,
                              spaceAfter=6, keepWithNext=True)
styles['body'] = ParagraphStyle('Body', fontName='Helvetica', fontSize=10,
                                 leading=14, textColor=DARK, spaceAfter=6)
styles['small'] = ParagraphStyle('Small', fontName='Helvetica', fontSize=9,
                                 leading=12.5, textColor=MUTED, spaceAfter=4)
styles['bullet'] = ParagraphStyle('Bullet', parent=styles['body'], leftIndent=14,
                                   bulletIndent=4, spaceAfter=4)
styles['cell'] = ParagraphStyle('Cell', fontName='Helvetica', fontSize=9,
                                leading=11.5, textColor=DARK)
styles['cell_b'] = ParagraphStyle('CellB', parent=styles['cell'],
                                   fontName='Helvetica-Bold')
styles['cell_r'] = ParagraphStyle('CellR', parent=styles['cell'], alignment=2)
styles['cell_br'] = ParagraphStyle('CellBR', parent=styles['cell_b'], alignment=2)
styles['head_cell'] = ParagraphStyle('HeadCell', fontName='Helvetica-Bold',
                                      fontSize=9, leading=11.5,
                                      textColor=colors.white)
styles['foot'] = ParagraphStyle('Foot', fontName='Helvetica', fontSize=8,
                                 leading=10, textColor=colors.white)


def p(text, style='body'):
    return Paragraph(text, styles[style])


def styled_table(header, rows, col_widths, right_cols=()):
    """Header + rows as a tidy bordered table with zebra striping."""
    data = [[Paragraph(f'<b>{esc(c)}</b>', styles['head_cell']) for c in header]]
    for r in rows:
        cells = []
        for i, c in enumerate(r):
            st = 'cell_br' if (i in right_cols and str(c).startswith('<b>')) else \
                 'cell_r' if i in right_cols else \
                 'cell_b' if str(c).startswith('<b>') else 'cell'
            cells.append(Paragraph(str(c), styles[st]))
        data.append(cells)
    t = Table(data, colWidths=col_widths, repeatRows=1)
    style_cmds = [
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, MID_GREY),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]
    for i in range(1, len(data)):
        if i % 2 == 0:
            style_cmds.append(('BACKGROUND', (0, i), (-1, i), LIGHT_GREY))
    t.setStyle(TableStyle(style_cmds))
    return t


story = []
W = A4[0] - 4 * cm  # usable width with 2cm margins

# ---------------------------------------------------------------- title block
story.append(p(f'{esc(TICKER)} Intelligence Report', 'title'))
story.append(p(f'Report as_of: <b>{esc(AS_OF)}</b> &nbsp;|&nbsp; '
               f'Market data as_of: <b>{esc(quant.get("as_of") or "N/A")}</b> &nbsp;|&nbsp; '
               f'Market data fetched (UTC): <b>{esc(quant.get("fetched_at", "N/A"))}</b>',
               'subtitle'))
company = esc(info.get('longName') or TICKER)
story.append(p(f'{company} &nbsp;|&nbsp; {esc(info.get("sector") or "N/A")} '
               f'&nbsp;/&nbsp; {esc(info.get("industry") or "N/A")}',
               'subtitle'))
story.append(p('AI status: <b>%s</b> &nbsp;|&nbsp; AI model: <b>gemini-3.5-flash-lite</b> '
               '(Google News RSS headlines &rarr; AI extraction and classification)'
               % esc('N/A: ' + ai['error'] if ai.get('error') else 'Available'),
               'small'))
story.append(p('Snapshot note: the report-date daily bar may be intraday until the US '
               'market closes; its Close field is provisional. News, peers, earnings, '
               'EDGAR and macro sections reuse their existing snapshots.',
               'small'))
story.append(Spacer(1, 6))

# ---------------------------------------------------------------- quantitative
story.append(p('Quantitative', 'h1'))
quant_rows = [
    ('Close', fmt(q.get('Close'))),
    ('Return 1D (%)', fmt(q.get('Return 1D (%)'))),
    ('Return 1W (%)', fmt(q.get('Return 1W (%)'))),
    ('Return 1M (%)', fmt(q.get('Return 1M (%)'))),
    ('Return YTD (%)', fmt(q.get('Return YTD (%)'))),
    ('Return 1Y (%)', fmt(q.get('Return 1Y (%)'))),
    ('Annualized volatility (%)', fmt(q.get('Annualized volatility (%)'))),
    ('Beta vs SPY', fmt(q.get('Beta vs SPY'))),
    ('Max drawdown (%)', fmt(q.get('Max drawdown (%)'))),
    ('Sharpe (rf=0)', fmt(q.get('Sharpe (rf=0)'))),
    ('P/E (trailing)', fmt(q.get('P/E (trailing)'), 2)),
    ('P/B', fmt(q.get('P/B'), 2)),
    ('EV/EBITDA', fmt(q.get('EV/EBITDA'), 2)),
    ('Revenue growth (%)', fmt(q.get('Revenue growth (%)'), 2)),
    ('MA50', fmt(q.get('MA50'))),
    ('Close vs MA50 (%)', fmt(q.get('Close vs MA50 (%)'))),
    ('MA200', fmt(q.get('MA200'))),
    ('Close vs MA200 (%)', fmt(q.get('Close vs MA200 (%)'))),
    ('RSI (14, Wilder)', fmt(q.get('RSI (14, Wilder)'))),
    ('MACD (12,26)', fmt(q.get('MACD (12,26)'))),
    ('MACD signal (9)', fmt(q.get('MACD signal (9)'))),
    ('MACD histogram', fmt(q.get('MACD histogram'))),
]
story.append(styled_table(['Metric', 'Value'],
                          [[f'<b>{esc(m)}</b>', v] for m, v in quant_rows],
                          [W * 0.62, W * 0.38], right_cols=(1,)))
story.append(p('Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq '
               'fallback if unavailable). 1Y return uses the last trading day on or '
               'before the one-year boundary.',
               'small'))

# ---------------------------------------------------------------- how to read
interp = build_interpretation_section(q)
m = re.search(r'## (.+)\n\n(.+?)\n\n((?:- .+\n?)+)', interp, re.S)
if m:
    story.append(p(esc(m.group(1)), 'h1'))
    story.append(p(esc(m.group(2).strip()), 'small'))
    for line in m.group(3).strip().splitlines():
        bm = re.match(r'- \*\*(.+?)\*\*:\s*(.*)$', line)
        if bm:
            story.append(Paragraph(f'<bullet>&bull;</bullet><b>{esc(bm.group(1))}</b>: '
                                   f'{esc(bm.group(2))}', styles['bullet']))
        else:
            story.append(p(esc(line), 'bullet'))

# ---------------------------------------------------------------- AI sections
AI_SECTIONS = (('tailwinds', 'Tailwinds'), ('headwinds', 'Headwinds'),
               ('catalysts', 'Catalysts'), ('risks', 'Risks'))


def item_sources_text(it, n):
    urls = list(dict.fromkeys([u for u in it.get('sources', []) if u]))
    hb = link_by_headline.get(it.get('headline'), '')
    if hb and hb not in urls:
        urls.append(hb)
    if not urls:
        return ''
    parts = []
    for j, u in enumerate(urls, 1):
        label = (it.get('source') or '').strip() or domain_of(u)
        parts.append(link(u, f'{label}' if len(urls) == 1 else f'{label} [{j}]'))
    return 'Sources: ' + ', '.join(parts)


for key, title in AI_SECTIONS:
    story.append(p(title, 'h1'))
    items = ai.get(key) or []
    if not items:
        story.append(p(esc(('N/A: ' + ai['error']) if ai.get('error')
                           else 'No items in this run'),
                         'small'))
        continue
    for n, it in enumerate(items, 1):
        block = [p(f'<b>{n}. {esc(it.get("headline", "N/A"))}</b>', 'body')]
        if it.get('summary') and it['summary'] != it.get('headline'):
            block.append(p(esc(it['summary']), 'body'))
        meta = (f"Date: <b>{esc(it.get('date', 'N/A'))}</b> &nbsp;|&nbsp; "
                f"Impact: <b>{esc(it.get('impact', 'N/A'))}</b> &nbsp;|&nbsp; "
                f"Horizon: <b>{esc(it.get('horizon', 'N/A'))}</b> &nbsp;|&nbsp; "
                f"Confidence: <b>{esc(it.get('confidence', 'N/A'))}</b>")
        block.append(p(meta, 'small'))
        srcs = item_sources_text(it, n)
        if srcs:
            block.append(p(srcs, 'small'))
        story.append(KeepTogether(block))
        story.append(Spacer(1, 4))

# ---------------------------------------------------------------- peers
story.append(p('Peer Comparables', 'h1'))
peers = peers_doc.get('peers') or []
if peers:
    growth = number(q.get('Revenue growth (%)'))
    ret = number(q.get('Return 1Y (%)'))
    me = {'ticker': TICKER, 'pe': q.get('P/E (trailing)'), 'pb': q.get('P/B'),
          'ev_ebitda': q.get('EV/EBITDA'),
          'revenue_growth': growth / 100 if growth is not None else None,
          'mktcap': info.get('marketCap'),
          'ret_1y': ret / 100 if ret is not None else None, 'currency': info.get('currency')}


    def pfmt(v, pct=False):
        v = number(v)
        return 'N/A' if v is None else f'{v * (100 if pct else 1):,.2f}'


    def mcap_fmt(v):
        # Compact billions for the PDF column (e.g. 138.04B); avoids wrapping.
        v = number(v)
        if v is None:
            return 'N/A'
        return f'{v / 1e9:,.2f}B'


    def bold(s):
        return f'<b>{s}</b>'


    prows = []
    for row in [me] + peers:
        is_me = row['ticker'] == TICKER
        cells = [row['ticker'], pfmt(row.get('pe')), pfmt(row.get('pb')),
                 pfmt(row.get('ev_ebitda')), pfmt(row.get('revenue_growth'), True),
                 mcap_fmt(row.get('mktcap')) + ' ' + esc(row.get('currency') or '?'), pfmt(row.get('ret_1y'), True)]
        prows.append([bold(c) if is_me else c for c in cells])
    cw = [W * 0.14, W * 0.12, W * 0.12, W * 0.14, W * 0.18, W * 0.16, W * 0.14]
    story.append(styled_table(
        ['Ticker', 'P/E', 'P/B', 'EV/EBITDA', 'Rev growth (%)',
         'Mkt cap (local)', '1Y ret (%)'],
        prows, cw, right_cols=(1, 2, 3, 4, 5, 6)))
    story.append(p(f'Peers fetched as_of: {esc(peers_doc.get("as_of", "N/A"))}; '
                   f'{esc(TICKER)} reuses existing data. Fundamentals are yfinance '
                   'info snapshots; missing values are not interpolated.', 'small'))
else:
    story.append(p('No peer data in this run.', 'small'))

# ---------------------------------------------------------------- earnings
story.append(p('Earnings Calendar', 'h1'))
story.append(p(f'Last reported earnings: <b>{esc(earnings.get("last_earnings") or "N/A")}</b><br/>'
               f'Next expected earnings: <b>{esc(earnings.get("next_earnings") or "N/A")}</b> '
               '(yfinance; expected dates may change)',
               'body'))

# ---------------------------------------------------------------- macro
story.append(p('Macro (FRED)', 'h1'))
if not macro.get('available'):
    story.append(p('N/A: no FRED API key configured; skipped', 'small'))
else:
    mrows = []
    for row in macro['indicators']:
        v = number(row.get('value'))
        mrows.append([esc(row.get('name', 'N/A')), esc(row.get('series_id', 'N/A')),
                      'N/A' if v is None else f'{v:,.3f}',
                      esc(row.get('date') or 'N/A')])
    story.append(styled_table(['Metric', 'Series', 'Latest value', 'Obs. date'],
                              mrows, [W * 0.44, W * 0.18, W * 0.2, W * 0.18],
                              right_cols=(2,)))
    story.append(p(f'Fetched as_of: {esc(macro.get("as_of", "N/A"))}', 'small'))

# ---------------------------------------------------------------- EDGAR
story.append(p('Latest Filing (EDGAR)', 'h1'))
filing = edgar.get('latest_filing') or {}


def amount(d):
    if not d:
        return 'N/A'
    v = number(d.get('value'))
    val = 'N/A' if v is None else f'{v:,.2f}'
    return (f'{val} {esc(d.get("unit", "N/A"))}; period {esc(d.get("period", "N/A"))}; '
            f'fiscal {esc(d.get("fiscal_year", "N/A"))}/{esc(d.get("fiscal_period", "N/A"))}')


story.append(p(f'Form: <b>{esc(filing.get("form", "N/A"))}</b> &nbsp;|&nbsp; '
               f'Filing date: <b>{esc(filing.get("filing_date", "N/A"))}</b><br/>'
               f'Revenue (latest quarter): {amount(edgar.get("revenue"))}<br/>'
               f'Net income (latest quarter): {amount(edgar.get("net_income"))}<br/>'
               f'SEC filing: {link(filing.get("url", ""), "Open on SEC EDGAR") if filing.get("url") else "N/A"}',
               'body'))
story.append(p('SEC requests use the demo placeholder contact email. Financial values '
               'use directly reported periods of approximately three months, without '
               'deriving quarters from cumulative values.',
               'small'))

# ---------------------------------------------------------------- sources
all_sources = []
seen = set()
for sec, _ in AI_SECTIONS:
    for it in ai.get(sec) or []:
        for u in it.get('sources', []) or []:
            if u and u not in seen:
                seen.add(u)
                all_sources.append((u, (it.get('source') or '').strip() or domain_of(u)))
        hb = link_by_headline.get(it.get('headline'), '')
        if hb and hb not in seen:
            seen.add(hb)
            all_sources.append((hb, (it.get('source') or '').strip() or domain_of(hb)))
story.append(p('Sources', 'h1'))
if all_sources:
    for n, (u, label) in enumerate(all_sources, 1):
        story.append(Paragraph(f'<bullet>&bull;</bullet>[{n}] {link(u, label)} '
                               f'<font color="#8A94A3">({esc(domain_of(u))})</font>',
                               styles['bullet']))
else:
    story.append(p('No sources in this run.', 'small'))
story.append(p('API documentation: '
               f'{link("https://www.sec.gov/search-filings/edgar-application-programming-interfaces", "SEC EDGAR APIs")}'
               ' &nbsp;|&nbsp; '
               f'{link("https://fred.stlouisfed.org/docs/api/fred/series_observations.html", "FRED observations")}',
               'small'))

# ---------------------------------------------------------------- disclaimer
story.append(p('Demo notes and limitations', 'h1'))
story.append(p('Multi-ticker local demo; AI items require human spot checks; RSS '
               'coverage is not guaranteed. Missing market data or fundamentals are '
               'marked N/A; no numbers are fabricated.',
               'small'))
story.append(p('<b>This report is not investment advice.</b>', 'body'))


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(colors.white)
    canvas.rect(0, 0, A4[0], 1.4 * cm, stroke=0, fill=1)
    canvas.setFillColor(MUTED)
    canvas.drawString(2 * cm, 0.65 * cm,
                      'JSOSIF Intelligence Demo \u2014 Not investment advice')
    canvas.drawRightString(A4[0] - 2 * cm, 0.65 * cm, f'Page {doc.page}')
    canvas.restoreState()


OUT = REPORTS / f'{TICKER}-intelligence-{STAMP}.pdf'
doc = BaseDocTemplate(str(OUT), pagesize=A4,
                      leftMargin=2 * cm, rightMargin=2 * cm,
                      topMargin=2 * cm, bottomMargin=2 * cm,
                      title=f'{TICKER} Intelligence Report {AS_OF}',
                      author='JSOSIF AI Pipeline')
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='main')
doc.addPageTemplates([PageTemplate(id='page', frames=[frame], onPage=footer)])
doc.build(story)
print(f'PDF written: {OUT} ({OUT.stat().st_size / 1024:.1f} KB)')

