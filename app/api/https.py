from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

from ..settings import settings


def configure(app, settings=settings):
    if settings.ENV != "dev":
        app.add_middleware(HTTPSRedirectMiddleware)
