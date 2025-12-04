def equals_to(expected):
    def matcher(actual):
        assert actual == expected, f"Expected {expected}, but got {actual}"

    return matcher


def is_not_none():
    def matcher(actual):
        assert actual is not None, "Expected value to not be None"

    return matcher
