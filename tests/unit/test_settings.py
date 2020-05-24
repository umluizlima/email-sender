from pydantic import ValidationError
from pytest import raises

from app.settings import EmailService, Settings


def test_api_key_is_set_from_env(monkeypatch):
    expected = "this_is_an_api_key"
    monkeypatch.setenv("API_KEY", expected)
    assert Settings(_env_file=None).API_KEY == expected


def test_api_key_has_default_value(monkeypatch):
    monkeypatch.delenv("API_KEY", raising=False)
    assert isinstance(Settings(_env_file=None).API_KEY, str)


def test_default_email_address_is_set_from_env(monkeypatch):
    expected = "some@email.com"
    monkeypatch.setenv("DEFAULT_EMAIL_ADDRESS", expected)
    assert Settings(_env_file=None).DEFAULT_EMAIL_ADDRESS == expected


def test_default_email_address_has_default_value(monkeypatch):
    monkeypatch.delenv("DEFAULT_EMAIL_ADDRESS", raising=False)
    assert isinstance(Settings(_env_file=None).SENDGRID_API_KEY, str)


def test_sendgrid_api_key_is_set_from_env(monkeypatch):
    expected = "this_is_an_api_key"
    monkeypatch.setenv("SENDGRID_API_KEY", expected)
    assert Settings(_env_file=None).SENDGRID_API_KEY == expected


def test_sendgrid_api_key_has_default_value(monkeypatch):
    monkeypatch.delenv("SENDGRID_API_KEY", raising=False)
    assert isinstance(Settings(_env_file=None).SENDGRID_API_KEY, str)


def test_email_service_is_set_from_env(monkeypatch):
    expected = EmailService.SENDGRID.value
    monkeypatch.setenv("EMAIL_SERVICE", expected)
    assert Settings(_env_file=None).EMAIL_SERVICE == expected


def test_email_service_must_exist(monkeypatch):
    expected = "some-service-that-is-not-mapped"
    monkeypatch.setenv("EMAIL_SERVICE", expected)
    with raises(ValidationError):
        Settings(_env_file=None)


def test_email_service_has_default_value(monkeypatch):
    monkeypatch.delenv("EMAIL_SERVICE", raising=False)
    assert isinstance(Settings(_env_file=None).EMAIL_SERVICE, EmailService)
