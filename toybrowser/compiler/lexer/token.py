class Token:
    def __init__(self, token_type=None):
        self.type = token_type

    def __eq__(self, other):
        return self.type == other.type

    def __str__(self):
        return "Token({})".format(self.type.value)

    def __repr__(self):
        return "Token({})".format(self.type.value)
