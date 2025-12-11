import logging

from requests.exceptions import JSONDecodeError

from screenplay.abilities.call_api import CallAPI
from screenplay.tasks.base_task import Task

logger = logging.getLogger(__name__)


class LoginUser(Task):
    def __init__(self, credentials):
        self.credentials = credentials

    def perform_as(self, actor):
        api = actor.ability_to(CallAPI)
        response = api.post("/api/users/login", json=self.credentials)
        actor.remember("last_response", response)
        try:
            data = response.json()
            token = data["user"]["token"]
            actor.remember("token", token)
        except (KeyError, JSONDecodeError):
            logger.warning("LoginUser: token not found in response")
        return response
