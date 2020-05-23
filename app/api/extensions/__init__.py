from . import https, sentry


def configure(app, settings):
    for extension in [https, sentry]:
        extension.configure(app, settings)
