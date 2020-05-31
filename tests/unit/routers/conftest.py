from unittest.mock import MagicMock

from pytest import fixture
from starlette.testclient import TestClient

from app.api import api
from app.api.security import ApiKeyChecker, api_key_checker
from app.core.tasks import get_tasks_producer

mock_producer = MagicMock()


def get_tasks_producer_override():
    return mock_producer


@fixture
def producer():
    return mock_producer


@fixture
def client(settings):
    client = TestClient(api)
    api.dependency_overrides[api_key_checker] = ApiKeyChecker(settings)
    api.dependency_overrides[get_tasks_producer] = get_tasks_producer_override
    yield client
    api.dependency_overrides = {}
