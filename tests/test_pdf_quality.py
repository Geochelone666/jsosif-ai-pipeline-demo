"""Safety and completeness checks for emitted research PDFs."""
from pathlib import Path

import pytest
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate

from pdf_quality import PdfQualityError, _safe_public_link, inspect_pdf
from fundamental_context import FUNDAMENTAL_KEYS
from risk_extensions import RISK_KEYS


def fixture_pdf(path, *, pagesize=A4, include_required=True, include_link=True):
    styles = getSampleStyleSheet()
    story = []
    if include_required:
        headings = [
            'AAPL Intelligence Report', 'Report as_of: 2026-10-24',
            'Quantitative', 'Tailwinds', 'Headwinds', 'Catalysts',
            'Risks', 'Peer Comparables', 'Sources', 'Research notes and limitations',
            *RISK_KEYS, *FUNDAMENTAL_KEYS,
        ]
    else:
        headings = ['AAPL Intelligence Report', 'Only partial report']
    for value in headings:
        story.append(Paragraph(value, styles['Normal']))
    if include_link:
        story.append(Paragraph('<link href="https://www.sec.gov/search-filings">SEC source</link>',
                               styles['Normal']))
    SimpleDocTemplate(str(path), pagesize=pagesize).build(story)


def test_complete_offline_report_pdf_is_parseable_and_has_sources(tmp_path):
    filename = tmp_path / 'healthy.pdf'
    fixture_pdf(filename)
    result = inspect_pdf(filename, ticker='AAPL', as_of='2026-10-24')
    assert result['pages'] >= 1
    assert result['https_links'] == 1
    assert result['text_characters'] > 100
    assert result['required_labels'] >= 20


def test_wrong_page_geometry_is_rejected(tmp_path):
    filename = tmp_path / 'letter.pdf'
    fixture_pdf(filename, pagesize=letter)
    with pytest.raises(PdfQualityError, match='A4 portrait'):
        inspect_pdf(filename)


def test_missing_required_content_fails_closed(tmp_path):
    filename = tmp_path / 'incomplete.pdf'
    fixture_pdf(filename, include_required=False)
    with pytest.raises(PdfQualityError, match='omitted expected content'):
        inspect_pdf(filename)


def test_pdf_needs_clickable_documentation(tmp_path):
    filename = tmp_path / 'unlinked.pdf'
    fixture_pdf(filename, include_link=False)
    with pytest.raises(PdfQualityError, match='no clickable'):
        inspect_pdf(filename)


def test_malformed_pdf_is_rejected(tmp_path):
    filename = tmp_path / 'bad.pdf'
    filename.write_bytes(b'%PDF-' + b'not a PDF' * 100)
    with pytest.raises(PdfQualityError, match='Unreadable|damaged|Unexpected'):
        inspect_pdf(filename)


@pytest.mark.parametrize('url', [
    'javascript:alert(1)', 'file:///etc/passwd', 'http://unsecured.example.com',
    'https://user:pass@example.com', 'data:text/plain,abc', '',
    'https://example.com/unsafe\nheader',
])
def test_unsafe_links_are_not_embedded(url):
    assert not _safe_public_link(url)


def test_regular_https_source_link_is_valid():
    assert _safe_public_link('https://www.sec.gov/Archives/edgar/data/1/file.html?a=1&b=2')
