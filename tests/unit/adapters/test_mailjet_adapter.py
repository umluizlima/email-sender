from unittest.mock import patch

from pytest import raises

from app.core.adapters import MailjetAdapter
from app.core.schemas import EmailSchema
from app.settings import Settings

settings = Settings(
    _env_file=None,
    DEFAULT_EMAIL_ADDRESS="some@email.com",
    MAILJET_API_KEY="some_api_key",
    MAILJET_API_SECRET="some_api_secret",
)

message = EmailSchema(
    **{
        "from": "from@email.com",
        "to": "to@email.com",
        "content": "content",
        "subject": "subject",
    }
)


@patch("app.core.adapters.mailjet.Client.__init__", return_value=None)
def test_mailjet_client_gets_initialized_with_parameters(mock_client_init):
    MailjetAdapter(settings=settings)
    mock_client_init.assert_called_once_with(
        auth=(settings.MAILJET_API_KEY, settings.MAILJET_API_SECRET), version="v3.1"
    )


@patch("app.core.adapters.mailjet.Client")
def test_adapter_send_throws_exception_on_invalid_message(mock_client_send):
    adapter = MailjetAdapter(settings=settings)
    with raises(Exception):
        adapter.send({})
