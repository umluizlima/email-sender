from fastapi import Depends, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from starlette.status import HTTP_403_FORBIDDEN

from app.settings import Settings, get_settings

API_KEY_HEADER = APIKeyHeader(name="x-api-key")


def api_key_checker(
    api_key: str = Security(API_KEY_HEADER), settings: Settings = Depends(get_settings),
):
    if api_key != settings.API_KEY.get_secret_value():
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )
