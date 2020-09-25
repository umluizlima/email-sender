from typing import Dict

from pydantic import Field

from .email import BaseEmailSchema


class TransactionalSchema(BaseEmailSchema):
    transactional_type: str = Field(alias="type")
    transactional_data: Dict = Field({}, alias="data")
