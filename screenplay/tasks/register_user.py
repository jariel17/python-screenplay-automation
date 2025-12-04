from screenplay.abilities.call_api import CallAPI
from screenplay.tasks.base_task import Task

class RegisterUser(Task):
    def __init__(self, user_data):
        self.user_data = user_data
    
    def perform_as(self, actor):
        api = actor.ability_to(CallAPI)
        response = api.post("/api/users", json=self.user_data)
        actor.remember("last_response", response)
        return response