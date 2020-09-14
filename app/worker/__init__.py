from app.core.tasks import get_tasks_consumer
from app.settings import get_settings

from . import extensions, tasks

settings = get_settings()

worker = get_tasks_consumer(settings)
worker.conf.update(broker_pool_limit=settings.BROKER_POOL_LIMIT)

extensions.configure(worker, settings)
tasks.configure(worker, settings)
