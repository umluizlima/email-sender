from fastapi import APIRouter
from starlette.status import HTTP_202_ACCEPTED

from app.core.adapters import SendgridAdapter
from app.core.schemas import EmailSchema

router = APIRouter()


@router.post("/emails", status_code=HTTP_202_ACCEPTED)
def send(message: EmailSchema):
    return SendgridAdapter().send(message)
