from .token_type import TokenType


class Token:
    def __init__(self, token_type=None, value=""):
        self.type = token_type
        self.value = value

    def __eq__(self, other):
        return self.type == other.type and self.value == other.value

    def __str__(self):
        return "Token({}, {})".format(self.type.value, self.value)

    def __repr__(self):
        return "Token({}, {})".format(self.type.value, self.value)
