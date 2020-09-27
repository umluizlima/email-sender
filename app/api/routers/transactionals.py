from fastapi import APIRouter, Depends
from starlette.status import HTTP_202_ACCEPTED

from app.core.schemas import TransactionalSchema
from app.core.tasks import Task

from ..dependencies import api_key_checker, tasks_producer

router = APIRouter()


@router.post("/transactionals", status_code=HTTP_202_ACCEPTED)
def send_transactional(message: TransactionalSchema, producer=Depends(tasks_producer)):
    producer.send_task(Task.SEND_TRANSACTIONAL, args=[message.dict(by_alias=True)])


def configure(app, settings):
    app.include_router(
        router,
        tags=["transactionals"],
        prefix="/api/v1",
        dependencies=[Depends(api_key_checker)],
    )
