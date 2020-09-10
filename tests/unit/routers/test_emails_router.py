from pytest import fixture
from starlette.status import (
    HTTP_202_ACCEPTED,
    HTTP_403_FORBIDDEN,
    HTTP_405_METHOD_NOT_ALLOWED,
    HTTP_422_UNPROCESSABLE_ENTITY,
)


@fixture(scope="function")
def send_response(producer, client, message, message_dict, settings):
    producer.reset_mock()
    yield client.post(
        "/api/v1/emails",
        json=message_dict,
        headers={"x-api-key": settings.API_KEY.get_secret_value()},
    )
    producer.send_task.assert_called_once_with("SEND_EMAIL", args=[message.dict()])


def test_send_email_endpoint_should_accept_post(send_response):
    assert send_response.status_code != HTTP_405_METHOD_NOT_ALLOWED


def test_send_email_should_return_status_202(send_response):
    assert send_response.status_code == HTTP_202_ACCEPTED


def test_send_email_should_validate_input(client, settings):
    response = client.post(
        "/api/v1/emails",
        json={},
        headers={"x-api-key": settings.API_KEY.get_secret_value()},
    )
    assert response.status_code == HTTP_422_UNPROCESSABLE_ENTITY


def test_send_email_should_return_status_403_if_not_authorized(client, settings):
    response = client.post(
        "/api/v1/emails",
        json={},
        headers={"x-api-key": f"not-quite-{settings.API_KEY.get_secret_value()}"},
    )
    assert response.status_code == HTTP_403_FORBIDDEN
