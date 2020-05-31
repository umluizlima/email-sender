from enum import Enum

from celery import Celery
from pydantic import BaseSettings


class Task(str, Enum):
    SEND_EMAIL = "SEND_EMAIL"


def get_celery_app(name: str, settings: BaseSettings, **kwargs):
    return Celery(name, broker=settings.BROKER_URL, **kwargs)
