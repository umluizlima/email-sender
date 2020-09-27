from enum import Enum
from typing import Dict

from pydantic import Field

from .email import BaseEmailSchema


class Transactional(str, Enum):
    ACCESS_CODE = ("ACCESS_CODE", "access_code.html")

    def __new__(cls, value: str, template: str):
        obj = str.__new__(cls)
        obj._value_ = value
        obj.template = template
        return obj


class TransactionalSchema(BaseEmailSchema):
    transactional_type: Transactional = Field(alias="type")
    transactional_data: Dict = Field({}, alias="data")

    class Config:
        use_enum_values = True
