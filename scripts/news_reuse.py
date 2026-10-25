"""Reuse successful *identical* news classifications from a verified prior report.

Require:
  - prior ready report, matching ticker and age <= 2 report days
  - intact archived report hashes and separately hashed RSS + AI source files
  - exact headline, original publication string and link match
  - successful original RSS extraction without outstanding unknown items

This cache is not model-generated truth, and it is NOT a cross-ticker semantic
search. A changed article date/link or tampered evidence requires new analysis.
"""
from datetime import date
from pathlib import Path

from report_store import digest, read_json, resolve_file, verified_report_files


CATEGORIES = ('tailwinds', 'headwinds', 'catalysts', 'risks', 'irrelevant')
REUSABLE_FIELDS = ('summary', 'impact', 'horizon', 'confidence', 'event_type', 'sentiment')


def _verified_sources(root, entry):
    verified = verified_report_files(root, entry)
    saved = entry.get('source_sha256')
    if not isinstance(saved, dict):
        return None
    folder = Path(entry['json']).parent / 'sources'
    ticker = entry['ticker'].lower()
    result = {}
    for label in ('rss-items', 'ai-intel'):
        if not isinstance(saved.get(label), str) or len(saved[label]) != 64:
            return None
        path = resolve_file(root, (folder / (ticker + '-' + label + '.json')).as_posix())
        if digest(path) != saved[label]:
            return None
        result[label] = read_json(path)
    if not isinstance(result['rss-items'], list) or not isinstance(result['ai-intel'], dict):
        return None
    return result


def prior_decisions(root, reports, ticker, business_date, max_age_days=2):
    """Find the newest audited eligible prior snapshot or return no cache."""
    today = date.fromisoformat(business_date)
    if type(max_age_days) is not int or not 1 <= max_age_days <= 7:
        raise ValueError('Cache max age must be 1..7 days')
    candidates = []
    for entry in reports:
        if (entry.get('ticker') != ticker or entry.get('quality') != 'ready'
                or entry.get('advisory')):
            continue
        try:
            age = (today - date.fromisoformat(entry['as_of'])).days
        except (TypeError, ValueError, KeyError):
            continue
        if 1 <= age <= max_age_days:
            candidates.append(entry)
    candidates.sort(key=lambda entry: (entry['as_of'], entry.get('generated_at', '')), reverse=True)
    for entry in candidates:
        try:
            sources = _verified_sources(root, entry)
        except (OSError, KeyError, TypeError, ValueError, AttributeError):
            continue
        if sources is None:
            continue
        ai, rss = sources['ai-intel'], sources['rss-items']
        if (ai.get('ticker') != ticker or ai.get('as_of') != entry['as_of']
                or ai.get('error')
                or (ai.get('fetch_status') or {}).get('status') != 'ok'):
            continue
        if (ai.get('extraction_stats') or {}).get('unknown', 1) != 0:
            continue
        originals = {}
        for item in rss:
            if (not isinstance(item, dict) or
                    not all(isinstance(item.get(k), str) and item[k]
                            for k in ('headline', 'pubDate', 'link'))):
                continue
            originals.setdefault(item['headline'], set()).add(
                (item['headline'], item['pubDate'], item['link']))
        choices = []
        for category in CATEGORIES:
            for decision in ai.get(category, []):
                if not isinstance(decision, dict):
                    continue
                title = decision.get('headline')
                matching = originals.get(title, ())
                if len(matching) != 1:
                    continue  # Ambiguous RSS identity: never reuse.
                if category == 'irrelevant':
                    if not isinstance(decision.get('reason'), str) or not decision['reason'].strip():
                        continue
                    compact = {'reason': decision['reason']}
                else:
                    if decision.get('extraction_method') != 'ai':
                        continue  # New deterministic rules always run from scratch.
                    if any(field not in decision for field in REUSABLE_FIELDS):
                        continue
                    compact = {field: decision[field] for field in REUSABLE_FIELDS}
                headline, pub_date, link = next(iter(matching))
                choices.append({'headline': headline, 'pubDate': pub_date, 'link': link,
                                'category': category, 'decision': compact})
        if choices:
            return {'ticker': ticker, 'source_report_id': entry['report_id'],
                    'source_as_of': entry['as_of'], 'items': choices}
    return None
