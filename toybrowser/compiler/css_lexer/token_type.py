from enum import Enum


class TokenType(Enum):
    EOF = "EOF"
    IDENTIFIER = "IDENTIFIER"

    # The # and . used in CSS
    KW_SHARP = "#"
    KW_DOT = "."

    # The {}
    L_BRACE = "{"
    R_BRACE = "}"

    COMMA = ","
    COLON = ":"
    SEMICOLON = ";"
