from pydantic.error_wrappers import ValidationError
from pytest import raises

from app.core.schemas import TransactionalSchema, TransactionalType


def test_transactional_type_field_is_required(transactional_message_dict):
    del transactional_message_dict["type"]
    with raises(ValidationError):
        TransactionalSchema(**transactional_message_dict)


def test_transactional_type_field_is_enum(transactional_message_dict):
    transactional_message_dict["type"] = TransactionalType.ACCESS_CODE.value + "a"
    with raises(ValidationError):
        TransactionalSchema(**transactional_message_dict)


def test_transactional_data_field_is_optional(transactional_message_dict):
    del transactional_message_dict["data"]
    assert (
        TransactionalSchema(**transactional_message_dict).transactional_data is not None
    )


def test_transactional_data_field_has_default_value(transactional_message_dict):
    assert isinstance(
        TransactionalSchema(**transactional_message_dict).transactional_data, dict
    )
