from pydantic import validate_arguments

from app.core.adapters import BaseAdapter, get_adapter
from app.core.schemas import EmailSchema
from app.core.tasks import Task
from app.settings import Settings

from .base import BaseTask


class SendEmailTask(BaseTask):
    name = Task.SEND_EMAIL

    def __init__(self, adapter: BaseAdapter):
        self.adapter = adapter

    @validate_arguments
    def run(self, message: EmailSchema):
        try:
            return self.adapter.send(message)
        except Exception as exc:
            self.retry(exc=exc)


def configure(settings: Settings):
    adapter = get_adapter(settings)
    return SendEmailTask(adapter)
