from unittest.mock import MagicMock

from pytest import fixture
from starlette.status import (
    HTTP_202_ACCEPTED,
    HTTP_405_METHOD_NOT_ALLOWED,
    HTTP_422_UNPROCESSABLE_ENTITY,
)

from app.api import api
from app.core.adapters import SendgridAdapter
from app.core.schemas import EmailSchema


message_dict = {
    "from": "from@email.com",
    "to": "to@email.com",
    "subject": "subject",
    "content": "content",
    "content_type": "text/html",
}

message = EmailSchema(**message_dict)


@fixture(scope="function")
def send_response(client):
    SendgridAdapter.send = MagicMock()
    yield client.post("/emails", json=message_dict)
    SendgridAdapter.send.assert_called_once_with(message)


def test_send_email_endpoint_should_accept_post(send_response):
    assert send_response.status_code != HTTP_405_METHOD_NOT_ALLOWED


def test_send_email_should_validate_input(client):
    response = client.post("/emails", json={})
    assert response.status_code == HTTP_422_UNPROCESSABLE_ENTITY


def test_send_email_should_return_status_202(send_response):
    assert send_response.status_code == HTTP_202_ACCEPTED
