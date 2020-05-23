from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware


def configure(app, settings):
    if settings.ENV != "dev":
        app.add_middleware(HTTPSRedirectMiddleware)
