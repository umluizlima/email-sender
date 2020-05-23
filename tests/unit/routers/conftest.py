from pytest import fixture
from starlette.testclient import TestClient

from app.api import api
from app.api.security import ApiKeyChecker, api_key_checker
from app.settings import Settings


@fixture
def settings():
    return Settings(API_KEY="secret-api-key")


@fixture
def client(settings):
    client = TestClient(api)
    api.dependency_overrides[api_key_checker] = ApiKeyChecker(settings)
    return client
