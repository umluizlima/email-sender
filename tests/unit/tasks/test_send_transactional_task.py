from unittest.mock import MagicMock

from pydantic import ValidationError
from pytest import fixture, raises

from app.core.schemas import TransactionalSchema
from app.core.tasks import Task
from app.worker.tasks.send_transactional import SendTransactionalTask

mock_tasks_producer = MagicMock()
mock_transactional_service = MagicMock()


@fixture
def send_transactional_task():
    mock_tasks_producer.reset_mock()
    mock_transactional_service.reset_mock()
    return SendTransactionalTask(mock_tasks_producer, mock_transactional_service)


def test_task_send_transactional_validates_payload(send_transactional_task):
    with raises(ValidationError):
        send_transactional_task.run({})


def test_task_send_transactional_calls_service(
    transactional_message, send_transactional_task
):
    send_transactional_task.run(transactional_message)

    mock_transactional_service.build_email.assert_called_once_with(
        transactional_message
    )


def test_task_send_transactional_calls_producer(
    transactional_message, email_message, send_transactional_task
):
    mock_transactional_service.build_email.return_value = email_message

    send_transactional_task.run(transactional_message)

    mock_tasks_producer.send_task.assert_called_once_with(
        Task.SEND_EMAIL, args=[email_message.dict(by_alias=True)]
    )
