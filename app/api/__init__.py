from fastapi import FastAPI

from ..settings import settings
from . import https, sentry, routers

sentry.configure()

api = FastAPI()
https.configure(api)
routers.configure(api, settings)
