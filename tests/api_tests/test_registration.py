from screenplay.actor import Actor
from screenplay.abilities.call_api import CallAPI
from screenplay.tasks.register_user import RegisterUser
from screenplay.tasks.login_user import LoginUser
from screenplay.questions.response_status import ResponseStatus
from screenplay.assertions.see_that import SeeThat
from screenplay.assertions.matchers import equals_to
from uuid import uuid4

BASE_URL ="http://localhost:8000"

def test_user_can_login():
    actor = Actor("Ariel").can(CallAPI(BASE_URL))

    username = f"ariel_{uuid4().hex[:6]}"
    email = f"{username}@example.com"

    actor.attempts_to(
        RegisterUser({
            "user": {
                "username": username,
                "email": email, 
                "password":"123456"
                }
            })
    )

    actor.should(
        SeeThat(ResponseStatus(), equals_to(201))
    )
