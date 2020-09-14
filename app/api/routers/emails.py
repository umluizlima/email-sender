from fastapi import APIRouter, Depends
from starlette.status import HTTP_202_ACCEPTED

from app.core.schemas import EmailSchema
from app.core.tasks import Task

from ..dependencies import tasks_producer

router = APIRouter()


@router.post("/emails", status_code=HTTP_202_ACCEPTED)
def send(message: EmailSchema, producer=Depends(tasks_producer)):
    producer.send_task(Task.SEND_EMAIL, args=[message.dict()])
