from unittest.mock import patch

from pytest import fixture, raises

from app.core.adapters import MailjetAdapter
from app.settings import EmailService


@fixture
def settings(settings):
    settings.EMAIL_SERVICE = EmailService.MAILJET
    return settings


@patch("app.core.adapters.mailjet.Client.__init__", return_value=None)
def test_mailjet_client_gets_initialized_with_parameters(mock_client_init, settings):
    MailjetAdapter(settings=settings)
    mock_client_init.assert_called_once_with(
        auth=(settings.MAILJET_API_KEY, settings.MAILJET_API_SECRET), version="v3.1"
    )


@patch("app.core.adapters.mailjet.Client")
def test_adapter_send_throws_exception_on_invalid_message(mock_client_send, settings):
    adapter = MailjetAdapter(settings=settings)
    with raises(Exception):
        adapter.send({})
