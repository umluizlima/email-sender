from celery import Celery
from pydantic import BaseSettings


def get_celery_app(name: str, settings: BaseSettings, **kwargs):
    return Celery(name, broker=settings.BROKER_URL, **kwargs)
