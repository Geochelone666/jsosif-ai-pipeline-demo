"""Make one bounded AI smoke request without logging credentials or response bodies."""
import json
import os

from gemini_provider import GeminiError
from groq_provider import GroqError
from ai_provider import generate_json, model as configured_model


def probe():
    model = configured_model()
    if not model:
        raise ValueError('Configure GEMINI_MODEL for a model enabled in this project')
    envelope = generate_json('Return exactly this JSON object: {"status":"ok"}',
                             model=model, attempts=1)
    try:
        payload = json.loads(envelope['text'])
    except (KeyError, TypeError, ValueError):
        raise GeminiError('The smoke response did not satisfy the JSON contract') from None
    if payload != {'status': 'ok'}:
        raise GeminiError('The smoke response did not satisfy the JSON contract')
    return {'status': 'ok', 'model': model, 'usage': envelope.get('usage', {})}


if __name__ == '__main__':
    try:
        print(json.dumps(probe()))
    except (ValueError, GeminiError, GroqError) as exc:
        raise SystemExit(str(exc)) from None
