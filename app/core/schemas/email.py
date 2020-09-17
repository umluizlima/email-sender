from enum import Enum
from typing import Optional

from pydantic import BaseModel, constr, EmailStr


class ContentType(str, Enum):
    TEXT_PLAIN = "text/plain"
    TEXT_HTML = "text/html"


class EmailSchema(BaseModel):
    to: EmailStr
    from_: Optional[EmailStr]
    subject: constr(max_length=78)
    content: str
    content_type: ContentType = ContentType.TEXT_HTML

    class Config:
        allow_population_by_field_name = True
        fields = {"from_": "from"}
