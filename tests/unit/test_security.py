from fastapi import HTTPException
from pytest import fixture, raises

from app.api.security import ApiKeyChecker


@fixture
def checker(settings):
    return ApiKeyChecker(settings=settings)


def test_checker_throws_exception_for_invalid_key(checker, settings):
    with raises(HTTPException):
        checker(f"not-quite-{settings.API_KEY.get_secret_value()}")


def test_checker_passes_for_valid_key(checker, settings):
    checker(settings.API_KEY.get_secret_value())
