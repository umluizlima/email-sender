from app.settings import Settings


def test_default_email_address_is_set_from_env(monkeypatch):
    expected = "some@email.com"
    monkeypatch.setenv("DEFAULT_EMAIL_ADDRESS", expected)
    assert Settings(_env_file=None).DEFAULT_EMAIL_ADDRESS == expected


def test_default_email_address_has_default_value(monkeypatch):
    monkeypatch.delenv("DEFAULT_EMAIL_ADDRESS", raising=False)
    assert isinstance(Settings(_env_file=None).SENDGRID_API_KEY, str)
