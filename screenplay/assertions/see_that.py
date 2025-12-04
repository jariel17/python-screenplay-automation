class SeeThat:
    def __init__(self, question, matcher):
        self.question = question
        self.matcher = matcher

    def evaluate_as(self, actor):
        actual = self.question.answered_by(actor)
        self.matcher(actual)
