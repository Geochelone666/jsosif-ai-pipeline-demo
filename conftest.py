"""Offline regressions must not inherit live credentials or deployment settings."""
import pytest


@pytest.fixture(autouse=True)
def isolated_provider_environment(monkeypatch):
    # Individual tests explicitly supply synthetic bindings. Real credentials are
    # exercised separately by check_integrations.py, never by the offline suite.
    names = ('AI_PROVIDER', 'GROQ_API_KEY', 'Grop_ai_API', 'GROQ_MODEL',
             'GEMINI_API_KEY', 'GOOGLE_API_KEY', 'GEMINI_MODEL', 'GEMINI_CLI',
             'GEMINI_RPD', 'GEMINI_RPM', 'GROQ_RPD', 'GROQ_RPM', 'GROQ_TPD', 'GROQ_TPM',
             'GMAIL_USER', 'GMAIL_APP_PASSWORD', 'JSOSIF_APPROVED_SEND',
             'GITHUB_OUTPUT', 'GITHUB_STEP_SUMMARY', 'SUBSCRIPTIONS_JSON', 'MEMBERS_CSV',
             'JSOSIF_API_USAGE_PATH', 'JSOSIF_PERSIST_API_USAGE')
    for name in names:
        monkeypatch.delenv(name, raising=False)
