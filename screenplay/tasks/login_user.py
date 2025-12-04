from screenplay.abilities.call_api import CallAPI
from screenplay.tasks.base_task import Task


class LoginUser(Task):
    def __init__(self, credentials):
        self.credentials = credentials

    def perform_as(self, actor):
        api = actor.ability_to(CallAPI)
        response = api.post("/api/users/login", json=self.credentials)
        actor.remember("last_response", response)
        return response
