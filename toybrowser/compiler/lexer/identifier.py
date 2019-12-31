from .token import Token
from .token_type import TokenType


class Identifier(Token):
    keyword_dic = {
        "html": TokenType.KW_HTML,
        "head": TokenType.KW_HEAD,
    }

    def __init__(self, name):
        super(Identifier, self).__init__(TokenType.IDENTIFIER)
        self.name = name

    @classmethod
    def is_keyword(cls, string):
        return string in cls.keyword_dic

    @classmethod
    def keyword_type(cls, string):
        return cls.keyword_dic[string]
