from fastapi import FastAPI

from .routers import emails_router

api = FastAPI()
api.include_router(emails_router, tags=["emails"])
