from unittest.mock import MagicMock, patch

from pydantic import ValidationError
from pytest import fixture, raises

from app.core.schemas import EmailSchema
from app.worker.tasks.emails import send_email

mock_adapter = MagicMock()

message = EmailSchema(
    **{"to": "some@email.com", "subject": "subject", "content": "content"}
)


@fixture(autouse=True)
def mock_get_active_adapter():
    with patch("app.worker.tasks.emails.get_active_adapter", return_value=mock_adapter):
        yield


def test_task_send_email_validates_payload():
    with raises(ValidationError):
        send_email({})


def test_task_send_email_calls_adapter():
    send_email(message)
    mock_adapter.send.assert_called_once_with(message)
