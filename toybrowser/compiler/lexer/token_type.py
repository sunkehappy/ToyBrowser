from enum import Enum


class TokenType(Enum):
    EOF = "EOF"

    IDENTIFIER = "IDENTIFIER"


    # 关键字
    KW_ID = "id"
    KW_CLASS = "class"
    KW_HTML = "html"
    KW_HEAD = "head"
    KW_BODY = "body"
    KW_H1 = "h1"

    # <>
    L_ANGLE_BRACKETS = "<"
    R_ANGLE_BRACKETS = ">"

    # /
    SLASH = "/"
