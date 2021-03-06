from toybrowser.compiler.html_lexer.token import Token
from toybrowser.compiler.html_lexer.token_type import TokenType


class Lexer:
    def __init__(self, lines=()):
        self.init_with_content(lines)

    def init_with_content(self, lines):
        self.lines = lines
        self.text = lines[0] if len(lines) > 0 else ""
        self.init_variables()

    def init_variables(self):
        self.pos = 0
        self.line_number = 0
        self.column_number = 0
        # String in angle or out of angle are parsed using different rules.
        self.in_angle = False

    def get_current_char(self):
        if self.line_number >= len(self.lines):
            return None
        return self.text[self.pos]

    def advance(self, step=1):
        self.pos += step
        self.column_number += step
        if self.pos >= len(self.text):
            self.pos = 0
            self.line_number += 1
            self.column_number = 0
            if self.line_number < len(self.lines):
                self.text = self.lines[self.line_number]

    def get_next_token(self):
        self.eat_space()
        # Can be added in future version.
        # self.eat_comment()

        current_char = self.get_current_char()
        if not current_char:
            return Token(TokenType.EOF)
        elif current_char == '<':
            self.advance()
            self.in_angle = True
            if self.get_current_char() == '/':
                self.advance()
                return Token(TokenType.L_END_ANGLE_BRACKETS)
            else:
                return Token(TokenType.L_START_ANGLE_BRACKETS)
        elif current_char == '>':
            self.advance()
            self.in_angle = False
            return Token(TokenType.R_ANGLE_BRACKETS)
        elif current_char == '=':
            self.advance()
            return Token(TokenType.EQUAL)
        elif current_char == '"':
            return self.parse_string_in_quote()
        else:
            if self.in_angle:
                return self.parse_identifier_and_keyword()
            else:
                return self.parse_string_between_tag()

    def parse_identifier_and_keyword(self):
        current_char = self.get_current_char()
        result = ""
        while current_char and current_char.isalnum():
            result += current_char
            self.advance()
            current_char = self.get_current_char()
        return Token(TokenType.IDENTIFIER, result)

    def eat_space(self):
        while self.get_current_char() and self.get_current_char().isspace():
            self.advance()

    def parse_string_in_quote(self):
        # Eat left "
        self.advance()
        result = ""
        current_char = self.get_current_char()
        while current_char and current_char != '"':
            result += current_char
            self.advance()
            current_char = self.get_current_char()
        if current_char != '"':
            raise Exception("Unclosed string in quote")
        # Eat right "
        self.advance()
        # TODO string should be id or class name.
        return Token(TokenType.IDENTIFIER, result)

    def parse_string_between_tag(self):
        result = ""
        current_char = self.get_current_char()
        while current_char and current_char != '<':
            result += current_char
            self.advance()
            current_char = self.get_current_char()
        if current_char != '<':
            raise Exception("Unclosed string in quote")
        return Token(TokenType.IDENTIFIER, result.strip())
