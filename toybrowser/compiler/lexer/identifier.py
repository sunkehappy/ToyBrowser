from .token import Token
from .token_type import TokenType


class Identifier(Token):
    keyword_dic = {
        "html": TokenType.KW_HTML,
        "head": TokenType.KW_HEAD,
        "body": TokenType.KW_BODY,
        "h1": TokenType.KW_H1,
        "div": TokenType.KW_DIV,
        "p": TokenType.KW_P,
        "em": TokenType.KW_EM,
    }

    def __init__(self, name):
        super(Identifier, self).__init__(TokenType.IDENTIFIER)
        self.name = name

    def __str__(self):
        return "Identifier({})".format(self.name)

    def __repr__(self):
        return "Identifier({})".format(self.name)

    def __eq__(self, other):
        return super(Identifier, self).__eq__(other) and self.name == other.name

    @classmethod
    def is_keyword(cls, string):
        return string.lower() in cls.keyword_dic

    @classmethod
    def keyword_type(cls, string):
        return cls.keyword_dic[string.lower()]
