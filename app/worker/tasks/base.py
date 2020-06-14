from celery import Task


class BaseTask(Task):
    default_retry_delay = 10
    max_retries = 3
    pass
