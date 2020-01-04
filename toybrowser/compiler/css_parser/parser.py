from toybrowser.compiler.css_lexer.lexer import Lexer
from toybrowser.compiler.css_lexer.token_type import TokenType
from .model.selector import Selector
from .model.declaration import Declaration
from .model.css_rule import CSSRule


class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.current_token = lexer. get_next_token()

    def error(self, reason: str):
        raise Exception("解析出错：{0}. 行号：{1}，列号：{2}".format(
            reason, self.lexer.line_number, self.lexer.column_number
        ))

    def eat(self, type: TokenType):
        if self.current_token.type != type:
            self.error("期望类型：{0}，实际类型：{1}。".format(
                type, self.current_token.type
            ))
        else:
            self.current_token = self.lexer.get_next_token()

    def parse(self):
        rules = []
        while self.current_token.type != TokenType.EOF:
            rules.append(self.parse_CSS_rule())
        return rules

    def parse_single_selector(self):
        if self.current_token.type == TokenType.KW_SHARP:
            self.eat(TokenType.KW_SHARP)
            value = self.current_token.value
            self.eat(self.current_token.type)
            return Selector(id=value)
        elif self.current_token.type == TokenType.KW_DOT:
            self.eat(TokenType.KW_DOT)
            value = self.current_token.value
            self.eat(self.current_token.type)
            return Selector(classes=value)
        else:
            value = self.current_token.value
            self.eat(self.current_token.type)
            return Selector(tag_name=value)

    def parse_selectors(self):
        selectors = []
        while self.current_token.type != TokenType.L_BRACE:
            selectors.append(self.parse_single_selector())
            if self.current_token.type == TokenType.COMMA:
                self.eat(TokenType.COMMA)
        return selectors

    def parse_declarations(self):
        declarations = []
        while self.current_token.type != TokenType.R_BRACE:
            declarations.append(self.parse_single_declaration())
        return declarations

    def parse_single_declaration(self):
        name = self.current_token.value
        self.eat(TokenType.IDENTIFIER)
        self.eat(TokenType.COLON)
        value = self.current_token.value
        self.eat(TokenType.IDENTIFIER)
        self.eat(TokenType.SEMICOLON)
        return Declaration(name, value)

    def parse_CSS_rule(self):
        selectors = self.parse_selectors()
        declarations = self.parse_declarations()
        return CSSRule(selectors, declarations)
