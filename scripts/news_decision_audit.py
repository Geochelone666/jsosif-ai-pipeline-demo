"""Flag internally inconsistent classified headlines for review, without rewriting them.

No model call, invented confidence, automatic reclassification or quality-gate
bypass. A flag is a heuristic concern, not proof of misclassification.
"""
from collections import Counter

SECTIONS = ('tailwinds', 'headwinds', 'catalysts', 'risks')


def decision_flags(category, item):
    """Return review reasons supported by existing, explicit classification data."""
    if not isinstance(item, dict):
        return ['invalid_classified_item']
    event = item.get('event_type')
    sentiment = item.get('sentiment')
    method = item.get('extraction_method')
    confidence = item.get('confidence')
    reasons = []
    if category == 'tailwinds' and sentiment == 'negative':
        reasons.append('negative_sentiment_in_tailwinds')
    if category == 'headwinds' and sentiment == 'positive':
        reasons.append('positive_sentiment_in_headwinds')
    if category == 'risks' and event == 'market_move':
        reasons.append('short_term_price_move_in_structural_risks')
    if category in ('tailwinds', 'headwinds') and event == 'unknown':
        reasons.append('directional_claim_without_event_type')
    if method == 'ai' and type(confidence) in (int, float) and 0 <= confidence < 0.7:
        reasons.append('low_uncalibrated_model_confidence')
    return reasons


def audit_decisions(ai):
    issues, summary = [], Counter()
    reviewed = 0
    for section in SECTIONS:
        for item in ai.get(section, []) or []:
            reviewed += 1
            for reason in decision_flags(section, item):
                summary[reason] += 1
                issues.append({
                    'headline': item.get('headline') if isinstance(item, dict) else None,
                    'category': section,
                    'reason': reason,
                    'method': item.get('extraction_method') if isinstance(item, dict) else None,
                })
    return {'reviewed_classified_items': reviewed,
            'flag_count': len(issues),
            'flagged_headlines': len({(x['category'], x['headline']) for x in issues}),
            'by_reason': dict(sorted(summary.items())),
            'flags': issues[:50],
            'note': 'Flags are heuristic review priorities only; no category was changed and confidence is not calibrated.'}
