import pytest

from screenplay.abilities.call_api import CallAPI
from screenplay.actor import Actor

BASE_URL = "http://localhost:8000"


@pytest.fixture
def actor():
    return Actor("Ariel").can(CallAPI(BASE_URL))
