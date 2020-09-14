from unittest.mock import MagicMock

from pydantic import ValidationError
from pytest import raises

from app.worker.tasks.send_email import SendEmailTask

mock_adapter = MagicMock()


def test_task_send_email_validates_payload():
    with raises(ValidationError):
        SendEmailTask(mock_adapter).run({})


def test_task_send_email_calls_adapter(message):
    SendEmailTask(mock_adapter).run(message)
    mock_adapter.send.assert_called_once_with(message)
