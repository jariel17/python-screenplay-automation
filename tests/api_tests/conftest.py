from uuid import uuid4

import pytest

from screenplay.abilities.call_api import CallAPI
from screenplay.actor import Actor
from screenplay.tasks.register_user import RegisterUser

BASE_URL = "http://localhost:8000"


@pytest.fixture
def actor():
    return Actor("Tester").can(CallAPI(BASE_URL))

@pytest.fixture
def random_user():
    username = f"user_{uuid4().hex[:6]}"
    return {
        "username": username,
        "email": f"{username}@example.com",
        "password": "123456"
    }
@pytest.fixture
def registered_user(actor, random_user):
    actor.attempts_to(RegisterUser({"user": random_user}))
    return random_user
