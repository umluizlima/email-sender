from app.core.tasks import get_tasks_consumer
from app.settings import settings

from . import extensions

worker = get_tasks_consumer(settings, include=["app.worker.tasks"])
worker.conf.update(broker_pool_limit=settings.BROKER_POOL_LIMIT)

extensions.configure(worker, settings)
