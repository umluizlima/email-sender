from pytest import fixture

from app.core.schemas import EmailSchema
from app.settings import Settings


@fixture
def settings():
    return Settings(_env_file=None)


@fixture
def message_dict():
    return {
        "from": "from@test.com",
        "to": "to@test.com",
        "subject": "Testing",
        "content": "This is a test",
    }


@fixture
def message(message_dict):
    return EmailSchema(**message_dict)
