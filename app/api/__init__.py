from fastapi import FastAPI, Depends

from .routers import emails_router
from .security import api_key_checker

api = FastAPI()
api.include_router(
    emails_router, tags=["emails"], dependencies=[Depends(api_key_checker)]
)
