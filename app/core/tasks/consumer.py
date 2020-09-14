from app.settings import Settings

from .base import get_celery_app


def get_tasks_consumer(settings: Settings, **kwargs):
    return get_celery_app("consumer", settings, **kwargs)
