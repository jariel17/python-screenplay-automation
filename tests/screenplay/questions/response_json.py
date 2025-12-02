from screenplay.questions.base_question import Question

class ResponseJsonField(Question):
    def __init__(self, field):
        self.field = field

    def answered_by(self, actor):
        response = actor.recall("last_response")
        body = response.json()
        return body.get(self.field)
