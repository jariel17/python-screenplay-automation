class Actor:
    def __init__(self, name):
        self.name = name
        self.abilities = {}
        self.memory = {}

    def __repr__(self):
        abilities_list = [ability.__class__.__name__ for ability in self.abilities.values()]
        return f"Actor(name={self.name!r}, abilities={abilities_list})"

    def can(self, ability):
        self.abilities[type(ability)] = ability
        return self

    def ability_to(self, ability_type):
        if ability_type not in self.abilities:
            raise ValueError(
                f"Actor '{self.name}' does not have the ability '{ability_type.__name__}'. "
                f"Available abilities: {[a.__name__ for a in self.abilities.keys()]}"
            )
        return self.abilities[ability_type]

    def attempts_to(self, *tasks):
        results = []
        for task in tasks:
            results.append(task.perform_as(self))
        return results[0] if len(results) == 1 else results

    def remember(self, key, value):
        self.memory[key] = value

    def recall(self, key):
        return self.memory.get(key)

    def should(self, *assertions):
        for assertion in assertions:
            assertion.evaluate_as(self)
