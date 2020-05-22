from unittest.mock import patch

from pytest import raises
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content

from app.core.adapters import SendgridAdapter
from app.core.schemas import EmailSchema
from app.settings import Settings

settings = Settings(
    DEFAULT_EMAIL_ADDRESS="some@email.com", SENDGRID_API_KEY="some_api_key",
)

message = EmailSchema(
    **{
        "from": "from@email.com",
        "to": "to@email.com",
        "content": "content",
        "subject": "subject",
    }
)


@patch("sendgrid.SendGridAPIClient.__init__", return_value=None)
def test_sendgrid_client_gets_initialized_with_api_key(mock_client_init):
    SendgridAdapter(settings=settings)
    mock_client_init.assert_called_once_with(api_key=settings.SENDGRID_API_KEY)


@patch("sendgrid.SendGridAPIClient.send")
def test_adapter_send_calls_client_send(mock_client_send):
    adapter = SendgridAdapter(settings=settings)
    adapter.send(message)
    mock_client_send.assert_called_once()


@patch("sendgrid.SendGridAPIClient.send")
def test_adapter_send_throws_exception_on_invalid_message(mock_client_send):
    adapter = SendgridAdapter(settings=settings)
    with raises(Exception):
        adapter.send({})
