from pydantic.error_wrappers import ValidationError
from pytest import fixture, raises

from app.core.schemas import EmailSchema
from app.settings import settings

invalid_email_addresses = [
    "plainaddress",
    "#@%^%#$@#$@#.com",
    "@example.com",
    "email.example.com",
    "email@example@example.com",
    ".email@example.com",
    "email.@example.com",
    "email..email@example.com",
    "email@example.com (Joe Smith)",
    "email@example",
    "email@-example.com",
    "email@111.222.333.44444",
    "email@example..com",
    "Abc..123@example.com",
]


@fixture
def email():
    return {
        "to": "address@domain.com",
        "from": "address@domain.com",
        "subject": "subject",
        "content": "content",
    }


def test_to_field_is_required(email):
    del email["to"]
    with raises(ValidationError):
        EmailSchema(**email)


def test_to_field_must_be_email_address(email):
    for address in invalid_email_addresses:
        email["to"] = address
        with raises(ValidationError):
            EmailSchema(**email)


def test_from_field_has_default_value(email, monkeypatch):
    del email["from"]
    assert EmailSchema(**email).from_ == settings.DEFAULT_EMAIL_ADDRESS


def test_from_field_must_be_email_address(email):
    for address in invalid_email_addresses:
        email["from"] = address
        with raises(ValidationError):
            EmailSchema(**email)


def test_subject_field_is_required(email):
    del email["subject"]
    with raises(ValidationError):
        EmailSchema(**email)


def test_subject_field_max_length_is_78(email):
    email["subject"] = 79 * "a"
    with raises(ValidationError):
        EmailSchema(**email)


def test_content_field_is_required(email):
    del email["content"]
    with raises(ValidationError):
        EmailSchema(**email)


def test_content_type_field_has_default_value(email):
    assert EmailSchema(**email).content_type == "text/plain"
