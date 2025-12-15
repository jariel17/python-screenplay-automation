from screenplay.assertions.matchers import equals_to
from screenplay.assertions.see_that import SeeThat
from screenplay.questions.response_status import ResponseStatus
from screenplay.tasks.login_user import LoginUser

BASE_URL = "http://localhost:8000"

def test_user_can_login(actor, registered_user):
    credentials = {
        "user": {
            "email": registered_user["email"],
            "password": registered_user["password"]
        }
    }
    actor.attempts_to(LoginUser(credentials))
    actor.should(SeeThat(ResponseStatus(), equals_to(202)))

def test_user_cannont_login_with_wrong_password(actor, registered_user):
    credentials = {
        "user": {
            "email": registered_user["email"],
            "password": "ww"
        }
    }
    actor.attempts_to(LoginUser(credentials))
    actor.should(SeeThat(ResponseStatus(), equals_to(400)))

