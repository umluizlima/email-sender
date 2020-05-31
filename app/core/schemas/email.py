from typing import Optional

from pydantic import BaseModel, constr, EmailStr

from app.settings import settings


class EmailSchema(BaseModel):
    to: EmailStr
    from_: Optional[EmailStr] = settings.DEFAULT_EMAIL_ADDRESS
    subject: constr(max_length=78)
    content: str
    content_type: Optional[str] = "text/html"

    class Config:
        fields = {"from_": "from"}
