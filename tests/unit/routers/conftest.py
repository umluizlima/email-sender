from unittest.mock import MagicMock

from pytest import fixture
from starlette.testclient import TestClient

from app.api import api
from app.api.dependencies import tasks_producer
from app.settings import Settings, get_settings

mock_producer = MagicMock()


def get_settings_override():
    return Settings(_env_file=None)


def tasks_producer_override():
    return mock_producer


@fixture
def producer():
    return mock_producer


@fixture
def client(settings):
    client = TestClient(api)
    api.dependency_overrides[get_settings] = get_settings_override
    api.dependency_overrides[tasks_producer] = tasks_producer_override
    yield client
    api.dependency_overrides = {}
