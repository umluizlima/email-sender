from fastapi import APIRouter, Depends
from starlette.status import HTTP_202_ACCEPTED

from app.core.adapters import BaseAdapter, get_active_adapter
from app.core.schemas import EmailSchema

router = APIRouter()


@router.post("/emails", status_code=HTTP_202_ACCEPTED)
def send(message: EmailSchema, adapter: BaseAdapter = Depends(get_active_adapter)):
    print(adapter)
    return adapter.send(message)
