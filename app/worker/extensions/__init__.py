from . import sentry


def configure(app, settings):
    for extension in [sentry]:
        extension.configure(app, settings)
