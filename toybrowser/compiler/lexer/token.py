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

    keyword_dic = {
        "html": TokenType.KW_HTML,
        "head": TokenType.KW_HEAD,
        "body": TokenType.KW_BODY,
        "h1": TokenType.KW_H1,
        "div": TokenType.KW_DIV,
        "p": TokenType.KW_P,
        "em": TokenType.KW_EM,
    }

    @classmethod
    def is_keyword(cls, string):
        return string.lower() in cls.keyword_dic

    @classmethod
    def keyword_type(cls, string):
        return cls.keyword_dic[string.lower()]