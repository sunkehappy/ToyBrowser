class Declaration:
    def __init__(self, name="", value=None):
        self.name = name
        self.value = value

    def __eq__(self, other):
        if other is None:
            return False
        return self.name == other.name and self.value == other.value

    def __str__(self):
        return "Declaration(name={}, value={})".format(self.name, self.value)

    def __repr__(self):
        return "Declaration(name={}, value={})".format(self.name, self.value)
