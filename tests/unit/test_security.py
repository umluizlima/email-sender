from fastapi import HTTPException
from pytest import fixture, raises

from app.api.security import ApiKeyChecker
from app.settings import Settings

settings = Settings(_env_file=None, API_KEY="some-secret-key")


@fixture
def checker():
    return ApiKeyChecker(settings=settings)


def test_checker_throws_exception_for_invalid_key(checker):
    with raises(HTTPException):
        checker(f"not-quite-{settings.API_KEY}")


def test_checker_passes_for_valid_key(checker):
    checker(settings.API_KEY)
