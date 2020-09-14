from enum import Enum

from celery import Celery

from app.settings import Settings


class Task(str, Enum):
    SEND_EMAIL = "SEND_EMAIL"


def get_celery_app(name: str, settings: Settings, **kwargs):
    return Celery(name, broker=settings.BROKER_URL, **kwargs)
