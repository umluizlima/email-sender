from unittest.mock import MagicMock

from pytest import fixture
from starlette.testclient import TestClient

from app.api import api
from app.api.security import ApiKeyChecker, api_key_checker
from app.core.adapters import ActiveAdapter, get_active_adapter
from app.settings import EmailService, Settings

mock_adapter = MagicMock()


def get_active_adapter_override():
    return mock_adapter


@fixture
def adapter():
    return mock_adapter


@fixture
def settings():
    return Settings(_env_file=None, API_KEY="secret-api-key")


@fixture
def client(settings):
    client = TestClient(api)
    api.dependency_overrides[api_key_checker] = ApiKeyChecker(settings)
    api.dependency_overrides[get_active_adapter] = get_active_adapter_override
    yield client
    api.dependency_overrides = {}
