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
    selected = model()
    requested_model = kwargs.pop('model', selected)
    if provider() != 'groq':
        from gemini_provider import generate_json as generate
        return generate(prompt, model=requested_model, **kwargs)

    from groq_provider import generate_json as generate, GroqError
    try:
        return generate(prompt, model=requested_model, **kwargs)
    except GroqError as exc:
        # Never mask remote 429s, permission failures, transport or schema errors.
        # A backup is optional and only used for a definite local daily budget cap.
        backup = os.environ.get('GROQ_FALLBACK_MODEL', '').strip()
        if exc.budget_kind not in ('requests', 'tokens') or not backup:
            raise
        supported = {'openai/gpt-oss-20b', 'openai/gpt-oss-120b', 'qwen/qwen3.8-27b'}
        if backup not in supported or backup == requested_model:
            raise GroqError('GROQ_FALLBACK_MODEL must name another supported strict-schema model') from None
        return generate(prompt, model=backup, **kwargs)
