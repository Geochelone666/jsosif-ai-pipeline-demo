import unittest
from ai_extract import extract, KEYS, MODEL, _parse_gemini_json


def news(headline):
    return dict(headline=headline, source='RSS source', link='https://example.com/news', pubDate='Fri, 02 Oct 2026 12:00:00 GMT')


def ai_item(headline, **kw):
    item = dict(headline=headline, summary='AI summary.', impact='medium',
                horizon='short', confidence=0.7, event_type='earnings',
                sentiment='neutral')
    item.update(kw)
    return item


def ai_payload(ticker, items_by_key, top_ticker='present'):
    payload = {k: list(items_by_key.get(k, [])) for k in KEYS}
    if top_ticker == 'present':
        payload['ticker'] = ticker
    elif top_ticker is not None:
        payload['ticker'] = top_ticker
    return payload


class ExtractionTests(unittest.TestCase):
    def test_rules_do_not_call_ai(self):
        def forbidden(*args):
            self.fail('clear news called AI')
        data = extract([news('Nvidia stock jumps after earnings')], 'NVDA', forbidden)
        item = data['tailwinds'][0]
        self.assertEqual((item['event_type'], item['sentiment'], item['extraction_method']), ('earnings', 'positive', 'rule'))
        self.assertEqual(item['companies'], ['NVDA'])

    def test_ambiguity_and_rss_authority(self):
        headline = 'Could Nvidia stock jump after earnings?'
        def ai(items, ticker):
            self.assertEqual(len(items), 1)
            return dict(ticker=ticker, **{k: [dict(headline=headline, summary='Uncertain earnings reaction.', date='2099-01-01', source='invented', sources=['https://invented'], impact='low', horizon='short', confidence=.5, event_type='earnings', sentiment='neutral')] if k == 'catalysts' else [] for k in KEYS})
        data = extract([news(headline), news(headline), news('Nvidia stock gains')], 'NVDA', ai)
        item = data['catalysts'][0]
        self.assertEqual(item['date'], '2026-10-02')
        self.assertEqual(item['source'], 'RSS source')
        self.assertEqual(item['sources'], ['https://example.com/news'])
        self.assertEqual(data['extraction_stats'], dict(unique_headlines=2, rule=1, ai=1, unknown=0))

    def test_ai_failure_preserves_rules(self):
        def failed(*args):
            raise RuntimeError('quota')
        data = extract([news('Nvidia stock gains'), news('Will Nvidia rise?')], 'NVDA', failed)
        self.assertEqual(len(data['tailwinds']), 1)
        self.assertEqual(data['unclassified'][0]['extraction_method'], 'unknown')
        self.assertIn('quota', data['error'])
        self.assertTrue(MODEL.endswith('flash-lite'))

    def test_conflicting_signals_and_boundaries(self):
        data = extract([news('Nvidia earnings rise but stock falls'), news('Pineapple stock gains')], 'AAPL')
        self.assertEqual(data['extraction_stats']['rule'], 0)
        self.assertEqual(data['unclassified'][1]['companies'], [])

    # --- Lenient Gemini payload handling (regressions for 2026-10-08 failures) ---

    def test_list_wrapped_payload_unwrapped(self):
        # ACN: Gemini returned [{...}] instead of {...}
        headline = 'Will Nvidia rise?'
        def ai(items, ticker):
            return [ai_payload(ticker, {'catalysts': [ai_item(headline)]})]
        data = extract([news(headline)], 'NVDA', ai)
        self.assertNotIn('error', data)
        self.assertEqual(len(data['catalysts']), 1)
        self.assertIn('unwrapped single-element list', data['ai_notes'][0])

    def test_singular_category_names_mapped(self):
        # ENB/V: Gemini returned "tailwind" instead of "tailwinds"
        headline = 'Will Nvidia rise?'
        def ai(items, ticker):
            return {'ticker': ticker, 'tailwind': [ai_item(headline)],
                    'headwinds': [], 'catalysts': [], 'risks': []}
        data = extract([news(headline)], 'NVDA', ai)
        self.assertNotIn('error', data)
        self.assertEqual(len(data['tailwinds']), 1)

    def test_item_level_ticker_fallback(self):
        # J: top-level ticker missing, items carry it
        headline = 'Will Nvidia rise?'
        def ai(items, ticker):
            item = ai_item(headline, ticker='NVDA')
            return ai_payload(ticker, {'catalysts': [item]}, top_ticker=None)
        data = extract([news(headline)], 'NVDA', ai)
        self.assertNotIn('error', data)
        self.assertEqual(len(data['catalysts']), 1)

    def test_wrong_ticker_still_rejected(self):
        headline = 'Will Nvidia rise?'
        def ai(items, ticker):
            return ai_payload(ticker, {'catalysts': [ai_item(headline)]}, top_ticker='MSFT')
        data = extract([news(headline)], 'NVDA', ai)
        self.assertIn('different ticker', data['error'])
        self.assertEqual(data['extraction_stats']['ai'], 0)

    def test_duplicate_headline_across_categories_kept_once(self):
        # CNQ.TO: same headline in two categories must not nuke the batch
        headline = 'Will Nvidia rise?'
        def ai(items, ticker):
            item = ai_item(headline)
            return ai_payload(ticker, {'tailwinds': [item], 'catalysts': [dict(item)]})
        data = extract([news(headline)], 'NVDA', ai)
        self.assertNotIn('error', data)
        total = sum(len(data[k]) for k in KEYS)
        self.assertEqual(total, 1)
        self.assertEqual(len(data['ai_skipped']), 1)
        self.assertEqual(data['ai_skipped'][0]['reason'], 'duplicate headline')

    def test_reworded_headline_fuzzy_matched(self):
        # VRTX: Gemini dropped leading "Why " from the headline
        pending = 'Why Vertex Pharmaceuticals (VRTX) Dipped More Than Broader Market Today'
        returned = 'Vertex Pharmaceuticals (VRTX) Dipped More Than Broader Market Today'
        def ai(items, ticker):
            return ai_payload(ticker, {'headwinds': [ai_item(returned)]})
        data = extract([news(pending)], 'VRTX', ai)
        self.assertNotIn('error', data)
        self.assertEqual(len(data['headwinds']), 1)
        self.assertEqual(data['headwinds'][0]['headline'], pending)

    def test_past_horizon_normalized(self):
        # NTR.TO: Gemini returned horizon "past"
        headline = 'Will Nvidia rise?'
        def ai(items, ticker):
            return ai_payload(ticker, {'catalysts': [ai_item(headline, horizon='past')]})
        data = extract([news(headline)], 'NVDA', ai)
        self.assertNotIn('error', data)
        self.assertEqual(data['catalysts'][0]['horizon'], 'short')

    def test_invalid_field_value_skips_item_only(self):
        good = 'Will Nvidia rise?'
        bad = 'Could Nvidia fall?'
        def ai(items, ticker):
            return ai_payload(ticker, {'catalysts': [
                ai_item(good),
                ai_item(bad, impact='extreme'),  # not a real impact level
            ]})
        data = extract([news(good), news(bad)], 'NVDA', ai)
        self.assertNotIn('error', data)
        self.assertEqual(len(data['catalysts']), 1)
        self.assertEqual(data['catalysts'][0]['headline'], good)
        self.assertEqual(len(data['ai_skipped']), 1)
        # skipped headline stays in pending -> unclassified audit trail
        self.assertEqual(data['unclassified'][0]['headline'], bad)

    def test_unmatched_headline_skipped_not_fatal(self):
        real = 'Will Nvidia rise?'
        def ai(items, ticker):
            return ai_payload(ticker, {'catalysts': [
                ai_item(real),
                ai_item('Totally invented headline about nothing'),
            ]})
        data = extract([news(real)], 'NVDA', ai)
        self.assertNotIn('error', data)
        self.assertEqual(len(data['catalysts']), 1)
        self.assertEqual(data['ai_skipped'][0]['reason'], 'no matching pending headline')

    def test_missing_category_defaults_to_empty(self):
        headline = 'Will Nvidia rise?'
        def ai(items, ticker):
            return {'ticker': ticker, 'catalysts': [ai_item(headline)]}
        data = extract([news(headline)], 'NVDA', ai)
        self.assertNotIn('error', data)
        self.assertEqual(len(data['catalysts']), 1)

    def test_fenced_json_parses(self):
        text = '```json\n{"ticker": "NVDA", "ok": true}\n```'
        self.assertEqual(_parse_gemini_json(text), {"ticker": "NVDA", "ok": True})
        text2 = '```\n{"a": 1}\n```'
        self.assertEqual(_parse_gemini_json(text2), {"a": 1})
        self.assertEqual(_parse_gemini_json('{"a": 1}'), {"a": 1})


if __name__ == '__main__':
    unittest.main()
