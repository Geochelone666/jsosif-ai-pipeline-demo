"""Select one provider explicitly; credentials never cross provider endpoints."""
import os


def provider():
    value = os.environ.get('AI_PROVIDER', '').strip().lower()
    if not value:
        value = 'groq' if (os.environ.get('GROQ_API_KEY') or os.environ.get('Grop_ai_API')) else 'gemini'
    if value not in ('groq', 'gemini'):
        raise ValueError('AI_PROVIDER must be groq or gemini')
    return value


def model():
    return (os.environ.get('GROQ_MODEL') or 'openai/gpt-oss-20b') if provider() == 'groq' else (
        os.environ.get('GEMINI_MODEL') or 'gemini-3.5-flash-lite')


def generate_json(prompt, **kwargs):
    if provider() == 'groq':
        from groq_provider import generate_json as generate
    else:
        from gemini_provider import generate_json as generate
    return generate(prompt, model=kwargs.pop('model', model()), **kwargs)
