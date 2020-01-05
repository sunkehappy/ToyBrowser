from .token_type import TokenType


class Token:
    def __init__(self, token_type=None, value=""):
        self.type = token_type
        self.value = value

    def __eq__(self, other):
        return self.type == other.type and self.value == other.value

    def __str__(self):
        if self.value:
            return "Token({}, {})".format(self.type.name, self.value)
        else:
            return "Token({})".format(self.type.name)

    def __repr__(self):
        return self.__str__()
