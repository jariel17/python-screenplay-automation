import pytest
from screenplay.actor import Actor
from screenplay.abilities.call_api import CallAPI

BASE_URL = "http://localhost:8000"

@pytest.fixture
def actor():
    return Actor("Ariel").can(
        CallAPI(BASE_URL)
    )