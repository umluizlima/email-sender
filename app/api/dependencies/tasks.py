from fastapi import Depends

from app.settings import get_settings, Settings
from app.core.tasks import get_tasks_producer


def tasks_producer(settings: Settings = Depends(get_settings)):
    return get_tasks_producer(settings)
