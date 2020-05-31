import sentry_sdk
from sentry_sdk.integrations.celery import CeleryIntegration

from app.settings import Environment


def configure(app, settings):
    if settings.SENTRY_DSN and settings.ENV != Environment.DEVELOPMENT:
        sentry_sdk.init(settings.SENTRY_DSN, integrations=[CeleryIntegration()])
