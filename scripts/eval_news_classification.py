#!/usr/bin/env python3
"""Evaluate classification with *independently human-labeled* news headlines.

No model requests or network calls. Missing predictions are abstentions, never
evidence that the model has correctly identified a neutral event.
"""
import argparse
from collections import Counter
import json
from pathlib import Path

LABELS = ('tailwinds', 'headwinds', 'catalysts', 'risks', 'irrelevant')
ABSTAIN = 'abstain'
UNVERIFIABLE = 'insufficient_evidence'
GOLD_LABELS = (*LABELS, UNVERIFIABLE)


def load_gold(path):
    rows = json.loads(Path(path).read_text(encoding='utf-8'))
    if not isinstance(rows, list) or not rows:
        raise ValueError('Gold labels must be a nonempty JSON list')
    used = set()
    for row in rows:
        if not isinstance(row, dict) or row.get('label') not in GOLD_LABELS:
            raise ValueError('Each gold item must have a human-selected valid label')
        if not all(isinstance(row.get(k), str) and row[k].strip()
                   for k in ('ticker', 'headline', 'pubDate')):
            raise ValueError('Gold items require ticker, headline and publication date')
        key = (row['ticker'], row['headline'], row['pubDate'])
        if key in used:
            raise ValueError('Duplicate gold headline identity: ' + repr(key))
        used.add(key)
    return rows


def rule_predictions(rows):
    from ai_extract import classify_rule
    output = {}
    for row in rows:
        category, record = classify_rule(row, row['ticker'])
        output[(row['ticker'], row['headline'], row['pubDate'])] = (
            category if record['extraction_method'] == 'rule' else ABSTAIN)
    return output


def snapshot_predictions(rows, snapshots, *, only_model_items=False):
    """Score only headlines actually present in the saved, dated AI snapshots."""
    loaded = {}
    for path in snapshots:
        snap = json.loads(Path(path).read_text(encoding='utf-8'))
        ticker, as_of = snap.get('ticker'), snap.get('as_of')
        if not isinstance(ticker, str) or not isinstance(as_of, str):
            raise ValueError('AI source snapshot must specify ticker and as_of')
        if (ticker, as_of) in loaded:
            raise ValueError('Duplicate AI snapshot for ticker/date')
        decisions = {}
        for category in (*LABELS, 'unclassified'):
            for item in snap.get(category, []):
                headline = item.get('headline') if isinstance(item, dict) else None
                if not isinstance(headline, str):
                    continue
                if only_model_items and item.get('extraction_method') != 'ai':
                    continue
                if headline in decisions:
                    raise ValueError('AI snapshot has duplicate headline decisions')
                decisions[headline] = category if category in LABELS else ABSTAIN
        loaded[(ticker, as_of)] = decisions
    predictions, eligible = {}, []
    for row in rows:
        anchor = row.get('as_of')
        if not anchor:
            raise ValueError('Snapshot scoring needs as_of on every human gold label')
        lookup = loaded.get((row['ticker'], anchor))
        if lookup is None:
            continue
        key = (row['ticker'], row['headline'], row['pubDate'])
        if only_model_items and row['headline'] not in lookup:
            continue
        eligible.append(row)
        predictions[key] = lookup.get(row['headline'], ABSTAIN)
    return eligible, predictions


def score(rows, predictions):
    """Selective precision and coverage must be read together; no auto-100%."""
    counts = Counter()
    confusion = Counter()
    per_label = {label: Counter() for label in GOLD_LABELS}
    for row in rows:
        key = (row['ticker'], row['headline'], row['pubDate'])
        actual = row['label']
        predicted = predictions.get(key, ABSTAIN)
        if predicted not in (*LABELS, ABSTAIN):
            raise ValueError('Invalid prediction: ' + repr(predicted))
        counts['total'] += 1
        confusion[(actual, predicted)] += 1
        per_label[actual]['total'] += 1
        if predicted == ABSTAIN:
            counts['abstained'] += 1
            per_label[actual]['abstained'] += 1
            if actual == UNVERIFIABLE:
                counts['correct_abstentions_on_insufficient_evidence'] += 1
        else:
            counts['covered'] += 1
            per_label[actual]['covered'] += 1
            if predicted == actual:
                counts['correct'] += 1
                per_label[actual]['correct'] += 1
            else:
                counts['wrong'] += 1
                if actual == 'irrelevant':
                    counts['false_company_event_on_irrelevant'] += 1
                if actual == UNVERIFIABLE:
                    counts['false_decisions_on_insufficient_evidence'] += 1
    return {
        'sample_size': counts['total'],
        'coverage': counts['covered'] / counts['total'] if counts['total'] else None,
        'selective_precision': counts['correct'] / counts['covered'] if counts['covered'] else None,
        'correct': counts['correct'], 'wrong': counts['wrong'],
        'correct_abstentions_on_insufficient_evidence': counts['correct_abstentions_on_insufficient_evidence'],
        'false_decisions_on_insufficient_evidence': counts['false_decisions_on_insufficient_evidence'],
        'abstained': counts['abstained'],
        'false_company_event_on_irrelevant': counts['false_company_event_on_irrelevant'],
        'by_human_label': {key: dict(value) for key, value in per_label.items()},
        'confusion': [{'human': actual, 'prediction': predicted, 'count': count}
                      for (actual, predicted), count in sorted(confusion.items())],
        'warning': 'Scores apply ONLY to the provided human-labeled sample; model-generated labels are not ground truth',
    }


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--gold', required=True, type=Path,
                        help='Private independently reviewed JSON labels (never publish member data)')
    parser.add_argument('--snapshots', type=Path, nargs='*',
                        help='Optional saved AI source snapshots: no provider requests')
    args = parser.parse_args(argv)
    gold = load_gold(args.gold)
    output = {'rules': score(gold, rule_predictions(gold))}
    if args.snapshots:
        eligible, predictions = snapshot_predictions(gold, args.snapshots)
        output['observed_pipeline'] = score(eligible, predictions)
        rules_for_eligible = rule_predictions(eligible)
        candidate_rows = [
            row for row in eligible
            if rules_for_eligible[(row['ticker'], row['headline'], row['pubDate'])] == ABSTAIN
        ]
        output['ai_candidate_subset'] = score(candidate_rows, predictions)
        output['caution'] = ('AI candidates are selected by rule abstention; compare '
                             'model performance within that subset, not directly to rule precision.')
    print(json.dumps(output, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
