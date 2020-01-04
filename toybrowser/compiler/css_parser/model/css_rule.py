class CSSRule:
    def __init__(self, selectors=(), declarations=()):
        self.selectors = selectors
        self.declarations = declarations
