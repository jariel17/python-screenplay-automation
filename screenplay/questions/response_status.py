from screenplay.questions.base_question import Question

class ResponseStatus(Question):
    def answered_by(self, actor):
        response = actor.recall("last_response")
        return response.status_code