import sentry_sdk
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware


def configure(app, settings):
    if settings.SENTRY_DSN:
        sentry_sdk.init(settings.SENTRY_DSN)
        app.add_middleware(SentryAsgiMiddleware)
