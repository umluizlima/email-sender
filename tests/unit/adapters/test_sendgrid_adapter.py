from unittest.mock import patch

from pytest import fixture, raises

from app.core.adapters import SendgridAdapter
from app.settings import EmailService


@fixture
def settings(settings):
    settings.EMAIL_SERVICE = EmailService.SENDGRID
    return settings


@patch("app.core.adapters.sendgrid.SendGridAPIClient.__init__", return_value=None)
def test_sendgrid_client_gets_initialized_with_api_key(mock_client_init, settings):
    SendgridAdapter(settings=settings)
    mock_client_init.assert_called_once_with(
        api_key=settings.SENDGRID_API_KEY.get_secret_value()
    )


@patch("app.core.adapters.sendgrid.SendGridAPIClient.send")
def test_adapter_send_calls_client_send(mock_client_send, message, settings):
    adapter = SendgridAdapter(settings=settings)
    adapter.send(message)
    mock_client_send.assert_called_once()


@patch("app.core.adapters.sendgrid.SendGridAPIClient.send")
def test_adapter_send_throws_exception_on_invalid_message(mock_client_send, settings):
    adapter = SendgridAdapter(settings=settings)
    with raises(Exception):
        adapter.send({})
