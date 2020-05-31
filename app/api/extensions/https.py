from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

from app.settings import Environment


def configure(app, settings):
    if settings.ENV != Environment.DEVELOPMENT:
        app.add_middleware(HTTPSRedirectMiddleware)
