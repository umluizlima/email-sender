from enum import Enum

from pydantic import BaseModel, constr, EmailStr, Field


class ContentType(str, Enum):
    TEXT_PLAIN = "text/plain"
    TEXT_HTML = "text/html"


class BaseEmailSchema(BaseModel):
    to_email: EmailStr = Field(alias="to")
    from_email: EmailStr = Field(default=None, alias="from")


class EmailSchema(BaseEmailSchema):
    subject: constr(max_length=78)
    content: str
    content_type: ContentType = ContentType.TEXT_HTML
