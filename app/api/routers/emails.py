from fastapi import APIRouter, Depends
from starlette.status import HTTP_202_ACCEPTED

from app.core.schemas import EmailSchema
from app.core.tasks import get_tasks_producer, Task

router = APIRouter()


@router.post("/emails", status_code=HTTP_202_ACCEPTED)
def send(message: EmailSchema, producer=Depends(get_tasks_producer)):
    producer.send_task(Task.SEND_EMAIL, args=[message.dict()])
