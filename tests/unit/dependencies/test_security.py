from fastapi import HTTPException
from pytest import raises

from app.api.dependencies import api_key_checker


def test_checker_throws_exception_for_invalid_key(settings):
    with raises(HTTPException):
        api_key_checker(f"not-quite-{settings.API_KEY.get_secret_value()}", settings)


def test_checker_passes_for_valid_key(settings):
    api_key_checker(settings.API_KEY.get_secret_value(), settings)
