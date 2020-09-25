from pytest import fixture

from app.core.schemas import EmailSchema, TransactionalSchema
from app.settings import Settings


@fixture
def settings():
    return Settings(_env_file=None)


@fixture
def email_message_dict():
    return {
        "from": "from@test.com",
        "to": "to@test.com",
        "subject": "Testing",
        "content": "This is a test",
    }


@fixture
def email_message(email_message_dict):
    return EmailSchema(**email_message_dict)


@fixture
def transactional_message_dict():
    return {
        "from": "from@test.com",
        "to": "to@test.com",
        "type": "ABC",
        "data": {},
    }


@fixture
def transactional_message(transactional_message_dict):
    return TransactionalSchema(**transactional_message_dict)
