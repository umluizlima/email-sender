from pydantic import validate_arguments

from app.core.schemas import EmailSchema, TransactionalSchema
from app.core.services import TemplateService, TransactionalService
from app.core.tasks import get_tasks_producer, Task
from app.settings import Settings

from .base import BaseTask


class SendTransactionalTask(BaseTask):
    name = Task.SEND_TRANSACTIONAL

    def __init__(self, tasks_producer, transactional_service: TransactionalService):
        self.tasks_producer = tasks_producer
        self.transactional_service = transactional_service

    @validate_arguments
    def run(self, message: TransactionalSchema):
        try:
            return self.tasks_producer.send_task(
                Task.SEND_EMAIL,
                args=[
                    self.transactional_service.build_email(message).dict(by_alias=True)
                ],
            )
        except Exception as exc:
            self.retry(exc=exc)


def configure(settings: Settings):
    tasks_producer = get_tasks_producer(settings)
    template_service = TemplateService(settings)
    transactional_service = TransactionalService(settings, template_service)
    return SendTransactionalTask(tasks_producer, transactional_service)
