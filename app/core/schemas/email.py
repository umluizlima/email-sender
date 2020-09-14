from typing import Optional

from pydantic import BaseModel, constr, EmailStr


class EmailSchema(BaseModel):
    to: EmailStr
    from_: Optional[EmailStr]
    subject: constr(max_length=78)
    content: str
    content_type: Optional[str] = "text/html"

    class Config:
        allow_population_by_field_name = True
        fields = {"from_": "from"}
