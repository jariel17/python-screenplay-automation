from tests.screenplay.actor import Actor
from screenplay.abilities.call_api import CallAPI
from screenplay.tasks.register_user import RegisterUser
from screenplay.tasks.login_user import LoginUser
from screenplay.questions.response_status import ResponseStatus
from screenplay.assertions.see_that import SeeThat
from screenplay.assertions.matchers import equals_to

BASE_URL ="http://localhost:8000"

def test_user_can_login():
    actor = Actor("Ariel").can(CallAPI(BASE_URL))

    actor.attempts_to(
        RegisterUser({"user": {"username": "ariel"}, "email": "ariel@example.com", "password":"123456"}),
        LoginUser({"user":{"email":"ariel@example.com", "password":"123456"}})
    )

    actor.should(
        SeeThat(ResponseStatus(), equals_to(200))
    )
