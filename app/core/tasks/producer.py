from app.settings import Settings

from .base import get_celery_app


def get_tasks_producer(settings: Settings, **kwargs):
    return get_celery_app("producer", settings, **kwargs)
