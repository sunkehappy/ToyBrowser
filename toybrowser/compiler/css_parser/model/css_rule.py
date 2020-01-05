class CSSRule:
    def __init__(self, selectors=(), declarations=()):
        self.selectors = selectors
        self.declarations = declarations

    def __eq__(self, other):
        if other is None:
            return False
        selectors_equal = self.selectors == other.selectors
        declarations_equal = self.declarations == other.declarations
        return selectors_equal and declarations_equal

    def __str__(self):
        return "CSSRule:\nselectors:{}\ndeclarations:{}".format(self.selectors, self.declarations)

    def __repr__(self):
        return self.__str__()
