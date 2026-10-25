"""Offline PDF structural preflight for research reports and archived sources.

This inspects pages, extractable content, expected metrics and external links.
Passing it is NOT a pixel-level proof against clipping or overlapping text.
"""
import argparse
import json
from pathlib import Path
from urllib.parse import urlsplit

from pypdf import PdfReader
from pypdf.errors import PdfReadError

from fundamental_context import FUNDAMENTAL_KEYS
from risk_extensions import RISK_KEYS


HEADINGS = ('Intelligence Report', 'Quantitative', 'Tailwinds', 'Headwinds',
            'Catalysts', 'Risks', 'Peer Comparables', 'Sources',
            'Research notes and limitations')


class PdfQualityError(ValueError):
    pass


def _safe_public_link(url):
    if not isinstance(url, str) or len(url) > 4096 or any(ord(c) < 32 for c in url):
        return False
    try:
        parsed = urlsplit(url)
        return (parsed.scheme == 'https' and bool(parsed.hostname)
                and parsed.username is None and parsed.password is None)
    except ValueError:
        return False


def inspect_pdf(path, *, ticker=None, as_of=None, max_pages=40):
    path = Path(path)
    if not path.is_file() or path.stat().st_size < 500:
        raise PdfQualityError('PDF missing or too small to be a complete report')
    try:
        pdf = PdfReader(path, strict=False)
        if pdf.is_encrypted:
            raise PdfQualityError('Research PDF must not require a password')
        pages = pdf.pages
        if not 1 <= len(pages) <= max_pages:
            raise PdfQualityError(f'Unexpected PDF page count: {len(pages)}')
        extracted, links = [], 0
        for position, page in enumerate(pages, 1):
            width = float(page.mediabox.width)
            height = float(page.mediabox.height)
            if abs(width - 595.28) > 5 or abs(height - 841.89) > 5:
                raise PdfQualityError(f'Page {position}: expected A4 portrait')
            text = page.extract_text() or ''
            if len(text.strip()) < 40:
                raise PdfQualityError(f'Page {position}: little or no extractable text')
            extracted.append(text)
            for annot_ref in page.get('/Annots', []):
                annot = annot_ref.get_object()
                action = annot.get('/A')
                if not action:
                    continue
                if action.get('/S') != '/URI' or not _safe_public_link(str(action.get('/URI', ''))):
                    raise PdfQualityError(f'Page {position}: unsafe or non-HTTPS link action')
                links += 1
    except PdfQualityError:
        raise
    except (PdfReadError, OSError, ValueError, TypeError, KeyError, IndexError, AttributeError) as exc:
        raise PdfQualityError(f'Unreadable or damaged PDF: {type(exc).__name__}') from None
    text = ' '.join(' '.join(extracted).split())
    required = (*HEADINGS, *RISK_KEYS, *FUNDAMENTAL_KEYS)
    if ticker:
        required += (ticker + ' Intelligence Report',)
    if as_of:
        required += (as_of,)
    missing = [label for label in required if ' '.join(label.split()) not in text]
    if missing:
        raise PdfQualityError('PDF omitted expected content: ' + ', '.join(missing[:10]))
    if not links:
        raise PdfQualityError('PDF contains no clickable research/source documentation links')
    return {'pages': len(pages), 'bytes': path.stat().st_size,
            'text_characters': len(text), 'https_links': links,
            'required_labels': len(required)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pdf', required=True, type=Path)
    parser.add_argument('--ticker')
    parser.add_argument('--as-of')
    args = parser.parse_args()
    print(json.dumps(inspect_pdf(args.pdf, ticker=args.ticker, as_of=args.as_of)))


if __name__ == '__main__':
    main()
