import sentry_sdk

from ..settings import settings


def configure(settings=settings):
    if settings.SENTRY_DSN:
        sentry_sdk.init(settings.SENTRY_DSN)
