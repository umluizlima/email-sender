from pydantic import validate_arguments

from app.core.adapters import get_active_adapter
from app.core.schemas import EmailSchema
from app.core.tasks import Task

from .. import worker


@worker.task(name=Task.SEND_EMAIL)
@validate_arguments
def send_email(message: EmailSchema):
    adapter = get_active_adapter()
    return adapter.send(message)
