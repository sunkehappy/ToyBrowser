from toybrowser.compiler.lexer.lexer import Lexer
from toybrowser.compiler.lexer.token import Token
from toybrowser.compiler.lexer.identifier import Identifier
from toybrowser.compiler.lexer.token_type import TokenType
from unittest import TestCase, TestSuite, TextTestRunner


class LexerTest(TestCase):
    def setUp(self) -> None:
        self.file = open("sample.html")
        self.lexer = Lexer(self.file.readlines())

    def tearDown(self) -> None:
        self.file.close()

    def test(self):
        # test <html>
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.L_ANGLE_BRACKETS))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.KW_HTML))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.R_ANGLE_BRACKETS))

        # test <body>
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.L_ANGLE_BRACKETS))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.KW_BODY))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.R_ANGLE_BRACKETS))

        # test <h1>
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.L_ANGLE_BRACKETS))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.KW_H1))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.R_ANGLE_BRACKETS))

        # test "Title" in <h1></h1>
        self.assertEqual(self.lexer.get_next_token(), Identifier("Title"))

        # test </h1>
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.L_ANGLE_BRACKETS))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.SLASH))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.KW_H1))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.R_ANGLE_BRACKETS))


if __name__ == '__main__':
    suite = TestSuite()
    suite.addTest(LexerTest('test'))
    # 执行测试
    runner = TextTestRunner()
    runner.run(suite)
