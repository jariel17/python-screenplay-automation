from uuid import uuid4

from screenplay.abilities.call_api import CallAPI
from screenplay.actor import Actor
from screenplay.assertions.matchers import equals_to
from screenplay.assertions.see_that import SeeThat
from screenplay.questions.response_status import ResponseStatus
from screenplay.tasks.register_user import RegisterUser

BASE_URL = "http://localhost:8000"

def test_user_can_login():
    actor = Actor("Ariel").can(CallAPI(BASE_URL))

    username = f"ariel_{uuid4().hex[:6]}"
    email = f"{username}@example.com"

    actor.attempts_to(
        RegisterUser({"user": {"username": username, "email": email, "password": "123456"}})
    )

    actor.should(SeeThat(ResponseStatus(), equals_to(201)))
