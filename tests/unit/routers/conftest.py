from pytest import fixture
from starlette.testclient import TestClient

from app.api import api


@fixture
def client():
    return TestClient(api)
