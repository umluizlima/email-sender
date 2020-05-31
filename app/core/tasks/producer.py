from functools import lru_cache

from app.settings import settings

from .base import get_celery_app


@lru_cache
def get_tasks_producer():
    return get_celery_app("producer", settings)
