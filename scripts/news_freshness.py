"""Publication-age disclosures for classified RSS headlines.

Publication age is not the event's true occurrence time or ongoing materiality.
These labels affect presentation only, never quality readiness or classification.
"""
from datetime import date


RSS_WINDOW_DAYS = 7
TRANSIENT_EVENTS = {'market_move': 2, 'ownership': 3}
DEFAULT_HEADLINE_DAYS = 7


def publication_freshness(publication_date, report_date, event_type='unknown'):
    """Return a bounded age and an editorial recency label without guessing dates."""
    try:
        published = date.fromisoformat(publication_date)
        report = date.fromisoformat(report_date)
    except (TypeError, ValueError):
        return {'age_days': None, 'label': 'unknown_publication_date',
                'presentation_window_days': None}
    age = (report - published).days
    if age < 0:
        label = 'future_dated'
    elif age > RSS_WINDOW_DAYS:
        label = 'outside_rss_window'
    else:
        display_days = TRANSIENT_EVENTS.get(event_type, DEFAULT_HEADLINE_DAYS)
        label = 'current_window' if age <= display_days else 'historical_context'
    return {'age_days': age, 'label': label,
            'presentation_window_days': TRANSIENT_EVENTS.get(event_type, DEFAULT_HEADLINE_DAYS)}


def annotate_news_publication_age(ai, as_of):
    """Attach derived metadata to the saved AI result; retain every story as evidence."""
    categories = ('tailwinds', 'headwinds', 'catalysts', 'risks', 'unclassified')
    counts = {'current_window': 0, 'historical_context': 0,
              'outside_rss_window': 0, 'future_dated': 0,
              'unknown_publication_date': 0}
    for category in categories:
        for item in ai.get(category, []):
            if not isinstance(item, dict):
                continue
            result = publication_freshness(item.get('date'), as_of, item.get('event_type'))
            item['publication_freshness'] = result
            counts[result['label']] += 1
    ai['publication_freshness_summary'] = {
        'reference_date': as_of, 'rss_window_days': RSS_WINDOW_DAYS,
        'classified_or_unresolved_counts': counts,
        'method': 'publication date relative to report business date; labels are editorial and do not certify event materiality',
    }
    return ai
