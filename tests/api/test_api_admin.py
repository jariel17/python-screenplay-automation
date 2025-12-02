import pytest
from screenplay.actors.actor import Actor
from screenplay.abilities.call_api import CallAPI
from screenplay.questions.response_status import ResponseStatus
from screenplay.tasks.register_user import RegisterUser
from screenplay.tasks.login_user import LoginUser
from screenplay.questions.response_status import ResponseStatus

BASE_URL ="http://localhost:8000"

@pytest.mark.api
def test_admin_register_and_login():
    admin = Actor("Admin")
    admin.can(CallAPI(BASE_URL))

    