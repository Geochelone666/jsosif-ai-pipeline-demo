"""Deterministic source-diversity/freshness statistics for RSS headlines.

This is evidence about fetched *headlines*, not verification of article claims.
No external requests are made; malformed metadata is counted, never inferred.
"""
from collections import Counter
from datetime import date, timezone
from email.utils import parsedate_to_datetime
from urllib.parse import urlsplit


def audit_rss(items, as_of):
    cutoff = date.fromisoformat(as_of)
    distinct = {}
    valid_items = 0
    for item in items:
        if isinstance(item, dict):
            headline = item.get('headline')
            if isinstance(headline, str) and headline.strip():
                valid_items += 1
                distinct.setdefault(headline, item)
    publishers = Counter()
    dates = []
    https_links = 0
    unknown_publishers = 0
    invalid_dates = 0
    future_dates = 0
    for item in distinct.values():
        publisher = item.get('source')
        if isinstance(publisher, str) and publisher.strip():
            publishers[publisher.strip().casefold()] += 1
        else:
            unknown_publishers += 1
        url = item.get('link')
        try:
            parsed = urlsplit(url) if isinstance(url, str) else None
            if parsed and parsed.scheme == 'https' and parsed.hostname:
                https_links += 1
        except ValueError:
            pass
        try:
            timestamp = parsedate_to_datetime(item.get('pubDate', ''))
            if timestamp.tzinfo is None:
                timestamp = timestamp.replace(tzinfo=timezone.utc)
            published = timestamp.astimezone(timezone.utc).date()
        except (TypeError, ValueError, OverflowError, AttributeError):
            invalid_dates += 1
            continue
        dates.append(published)
        if published > cutoff:
            future_dates += 1
    n = len(distinct)
    known = sum(publishers.values())
    dominant = max(publishers.values(), default=0)
    hhi = sum((count / known) ** 2 for count in publishers.values()) if known else None
    return {
        'raw_items': len(items),
        'unique_headlines': n,
        'duplicates_excluded': valid_items - n,
        'invalid_headline_items': len(items) - valid_items,
        'unique_publishers': len(publishers),
        'unknown_publisher_headlines': unknown_publishers,
        'largest_publisher_share_pct': round(dominant / known * 100, 2) if known else None,
        'publisher_hhi': round(hhi, 4) if hhi is not None else None,
        'https_link_headlines': https_links,
        'missing_or_insecure_link_headlines': n - https_links,
        'invalid_publication_dates': invalid_dates,
        'future_publication_dates': future_dates,
        'oldest_publication_date': min(dates).isoformat() if dates else None,
        'newest_publication_date': max(dates).isoformat() if dates else None,
        'oldest_headline_age_days': (cutoff - min(dates)).days if dates else None,
    }
