from fastapi import FastAPI

from ..settings import get_settings
from . import extensions, routers

settings = get_settings()

api = FastAPI(title="email-sender")

extensions.configure(api, settings)
routers.configure(api, settings)
