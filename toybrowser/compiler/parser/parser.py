from toybrowser.compiler.lexer.lexer import Lexer
from toybrowser.compiler.lexer.token_type import TokenType
from toybrowser.compiler.parser.model.node import Node


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

    def document(self, node: Node):
        while self.current_token.type != TokenType.EOF:

