import sentry_sdk
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

from app.settings import Environment


def configure(app, settings):
    if settings.SENTRY_DSN and settings.ENV != Environment.DEVELOPMENT:
        sentry_sdk.init(settings.SENTRY_DSN)
        app.add_middleware(SentryAsgiMiddleware)
