from fastapi import Security, HTTPException
from fastapi.security.api_key import APIKeyHeader
from pydantic import BaseSettings

from starlette.status import HTTP_403_FORBIDDEN

from app.settings import settings


API_KEY_HEADER = APIKeyHeader(name="x-api-key")


class ApiKeyChecker:
    def __init__(self, settings=settings):
        self.settings = settings

    def __call__(self, api_key: str = Security(API_KEY_HEADER)):
        if api_key != self.settings.API_KEY:
            raise HTTPException(
                status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
            )


api_key_checker = ApiKeyChecker()
