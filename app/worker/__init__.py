from celery import Celery

from app.settings import settings

worker = Celery("worker", broker=settings.BROKER_URL, include=["app.worker.tasks"])
worker.conf.update(broker_pool_limit=settings.BROKER_POOL_LIMIT)
