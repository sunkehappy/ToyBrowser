from toybrowser.compiler.lexer.lexer import Lexer
from toybrowser.compiler.lexer.token_type import TokenType
from toybrowser.compiler.parser.model.element_node import ElementNode
from .model.text_node import TextNode


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
        root = self.parse_single_node()
        assert self.current_token.type == TokenType.EOF
        return root

    def parse_attributes(self):
        result = {}
        while self.current_token.type != TokenType.R_ANGLE_BRACKETS:
            key = self.current_token.name
            self.eat(TokenType.IDENTIFIER)
            self.eat(TokenType.EQUAL)
            value = self.current_token.name
            self.eat(TokenType.IDENTIFIER)
            result[key] = value
        return result

    def parse_single_node(self):
        self.eat(TokenType.L_START_ANGLE_BRACKETS)
        current_tag_type = self.current_token.type
        self.eat(current_tag_type)

        attributes = self.parse_attributes()

        self.eat(TokenType.R_ANGLE_BRACKETS)

        nodes = []
        while self.current_token.type != TokenType.L_END_ANGLE_BRACKETS:
            if self.current_token.type == TokenType.L_START_ANGLE_BRACKETS:
                nodes.append(self.parse_single_node())
            elif self.current_token.type == TokenType.IDENTIFIER:
                token_name = self.current_token.name
                self.eat(TokenType.IDENTIFIER)
                nodes.append(TextNode(token_name))
        self.eat(TokenType.L_END_ANGLE_BRACKETS)
        self.eat(current_tag_type)
        self.eat(TokenType.R_ANGLE_BRACKETS)
        return ElementNode(nodes, current_tag_type.value, attributes)
