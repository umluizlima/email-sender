from fastapi import Depends

from app.core.tasks import get_tasks_producer
from app.settings import Settings, get_settings


def tasks_producer(settings: Settings = Depends(get_settings)):
    return get_tasks_producer(settings)
