from pydantic.error_wrappers import ValidationError
from pytest import raises

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


def test_to_field_is_required(message_dict):
    del message_dict["to"]
    with raises(ValidationError):
        EmailSchema(**message_dict)


def test_to_field_must_be_email_address(message_dict):
    for address in invalid_email_addresses:
        message_dict["to"] = address
        with raises(ValidationError):
            EmailSchema(**message_dict)


def test_from_field_has_default_value(message_dict):
    del message_dict["from"]
    assert EmailSchema(**message_dict).from_ == settings.DEFAULT_EMAIL_ADDRESS


def test_from_field_must_be_email_address(message_dict):
    for address in invalid_email_addresses:
        message_dict["from"] = address
        with raises(ValidationError):
            EmailSchema(**message_dict)


def test_subject_field_is_required(message_dict):
    del message_dict["subject"]
    with raises(ValidationError):
        EmailSchema(**message_dict)


def test_subject_field_max_length_is_78(message_dict):
    message_dict["subject"] = 79 * "a"
    with raises(ValidationError):
        EmailSchema(**message_dict)


def test_content_field_is_required(message_dict):
    del message_dict["content"]
    with raises(ValidationError):
        EmailSchema(**message_dict)


def test_content_type_field_has_default_value(message_dict):
    assert EmailSchema(**message_dict).content_type == "text/html"
