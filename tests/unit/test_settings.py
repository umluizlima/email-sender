from app.settings import Settings


def test_default_email_address_is_set_from_env(monkeypatch):
    expected = "some@email.com"
    monkeypatch.setenv("DEFAULT_EMAIL_ADDRESS", expected)
    assert Settings().DEFAULT_EMAIL_ADDRESS == expected


def test_default_email_address_has_default_value(monkeypatch):
    monkeypatch.delenv("DEFAULT_EMAIL_ADDRESS", raising=False)
    assert Settings().DEFAULT_EMAIL_ADDRESS == "address@domain.com"
