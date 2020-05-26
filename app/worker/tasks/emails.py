from pydantic import validate_arguments

from app.core.adapters import get_active_adapter
from app.core.schemas import EmailSchema

from .. import worker


@worker.task
@validate_arguments
def send_email(message: EmailSchema):
    adapter = get_active_adapter()
    return adapter.send(message)
