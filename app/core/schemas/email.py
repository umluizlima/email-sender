from pydantic import BaseModel, constr, EmailStr, Field

from app.settings import settings


class EmailSchema(BaseModel):
    to: EmailStr
    from_: EmailStr = settings.DEFAULT_EMAIL_ADDRESS
    subject: constr(max_length=78)
    content: str
    content_type: str = "text/plain"

    class Config:
        fields = {"from_": "from"}
