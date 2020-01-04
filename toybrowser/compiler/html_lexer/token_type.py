from enum import Enum


class TokenType(Enum):
    EOF = "EOF"
    IDENTIFIER = "IDENTIFIER"

    # <> and </>
    L_START_ANGLE_BRACKETS = "<"
    L_END_ANGLE_BRACKETS = "</"
    R_ANGLE_BRACKETS = ">"
    EQUAL = "="
