from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture(autouse=True)
def isolated_activities(monkeypatch):
    monkeypatch.setattr(app_module, "activities", deepcopy(app_module.activities))


@pytest.fixture
def client():
    return TestClient(app_module.app)
