from pydantic import validate_arguments

from app.core.adapters import get_active_adapter
from app.core.schemas import EmailSchema
from app.core.tasks import Task

from .base import BaseTask


class SendEmailTask(BaseTask):
    name = Task.SEND_EMAIL

    def __init__(self):
        self.adapter = get_active_adapter()

    @validate_arguments
    def run(self, message: EmailSchema):
        try:
            return self.adapter.send(message)
        except Exception as exc:
            self.retry(exc=exc)
