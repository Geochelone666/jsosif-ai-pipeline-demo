"""Audit flags identify suspicious news classifications without changing evidence."""
from copy import deepcopy

from news_decision_audit import audit_decisions, decision_flags


def item(headline, sentiment, event, method='ai', confidence=.9):
    return {'headline': headline, 'sentiment': sentiment, 'event_type': event,
            'extraction_method': method, 'confidence': confidence}


def test_archived_stock_move_in_risks_is_flagged_not_rewritten():
    headline = 'Apple (AAPL) Stock Sinks As Market Gains: What You Should Know'
    data = {
        'risks': [item(headline, 'negative', 'market_move')],
        'tailwinds': [], 'headwinds': [], 'catalysts': [],
        'unclassified': [item('Unknown forecast', 'unknown', 'unknown')],
    }
    original = deepcopy(data)
    result = audit_decisions(data)
    assert result['flag_count'] == 1
    assert result['by_reason']['short_term_price_move_in_structural_risks'] == 1
    assert result['flags'][0]['headline'] == headline
    assert data == original
    assert result['reviewed_classified_items'] == 1


def test_low_self_reported_confidence_is_review_hint_not_reclassification():
    data = {
        'tailwinds': [item('Confirmed improvement', 'positive', 'earnings', confidence=.6)],
        'headwinds': [], 'catalysts': [], 'risks': [],
    }
    result = audit_decisions(data)
    assert result['by_reason'] == {'low_uncalibrated_model_confidence': 1}
    assert data['tailwinds'][0]['confidence'] == .6


def test_conflicting_category_and_sentiment_is_reviewable():
    reasons = decision_flags('tailwinds', item('Loss', 'negative', 'earnings'))
    assert reasons == ['negative_sentiment_in_tailwinds']
    reasons = decision_flags('headwinds', item('Gain', 'positive', 'earnings'))
    assert reasons == ['positive_sentiment_in_headwinds']


def test_rule_heuristic_confidence_is_not_confused_with_calibrated_ai():
    data = {
        'tailwinds': [item('Known rise', 'positive', 'market_move', method='rule', confidence=.8)],
        'headwinds': [], 'catalysts': [], 'risks': [],
    }
    assert audit_decisions(data)['flag_count'] == 0


def test_empty_snapshot_and_invalid_classified_item_are_handled():
    assert audit_decisions({})['flag_count'] == 0
    data = {'tailwinds': [None]}
    result = audit_decisions(data)
    assert result['flag_count'] == 1
    assert result['flags'][0]['reason'] == 'invalid_classified_item'


def test_ambiguous_event_type_can_be_flagged_without_guessing():
    assert decision_flags('headwinds', item('An unclear story', 'negative', 'unknown')) == [
        'directional_claim_without_event_type']
