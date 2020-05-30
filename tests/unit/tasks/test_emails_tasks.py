from unittest.mock import MagicMock, patch

from pydantic import ValidationError
from pytest import fixture, raises

from app.worker.tasks.emails import send_email

mock_adapter = MagicMock()


@fixture(autouse=True)
def mock_get_active_adapter():
    with patch("app.worker.tasks.emails.get_active_adapter", return_value=mock_adapter):
        yield


def test_task_send_email_validates_payload():
    with raises(ValidationError):
        send_email({})


def test_task_send_email_calls_adapter(message):
    send_email(message)
    mock_adapter.send.assert_called_once_with(message)
