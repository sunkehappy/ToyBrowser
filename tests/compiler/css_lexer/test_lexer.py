from toybrowser.compiler.css_lexer.lexer import Lexer
from toybrowser.compiler.css_lexer.token import Token
from toybrowser.compiler.css_lexer.token_type import TokenType
from unittest import TestCase, TestSuite, TextTestRunner


class LexerTest(TestCase):
    def setUp(self) -> None:
        self.css_file = open("../../resources/sample.css")
        self.lexer = Lexer()

    def tearDown(self) -> None:
        self.css_file.close()

    def testCSS(self):
        self.lexer.init_with_content(self.css_file.readlines())

        # Test h1, h2, h3 { margin: auto; color: #cc0000; }
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.IDENTIFIER, "h1"))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.COMMA))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.IDENTIFIER, "h2"))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.COMMA))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.IDENTIFIER, "h3"))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.L_BRACE))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.IDENTIFIER, "margin"))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.COLON))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.IDENTIFIER, "auto"))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.SEMICOLON))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.IDENTIFIER, "color"))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.COLON))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.KW_SHARP))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.IDENTIFIER, "cc0000"))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.SEMICOLON))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.R_BRACE))

        # Test .author { margin-bottom: 20px; padding: 10px; }
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.KW_DOT))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.IDENTIFIER, "author"))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.L_BRACE))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.IDENTIFIER, "margin-bottom"))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.COLON))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.IDENTIFIER, "20px"))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.SEMICOLON))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.IDENTIFIER, "padding"))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.COLON))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.IDENTIFIER, "10px"))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.SEMICOLON))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.R_BRACE))

        # Test #hello-world { color: red; }
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.KW_SHARP))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.IDENTIFIER, "hello-world"))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.L_BRACE))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.IDENTIFIER, "color"))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.COLON))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.IDENTIFIER, "red"))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.SEMICOLON))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.R_BRACE))

        # test EOF
        # self.assertEqual(self.lexer.get_next_token(), Token(TokenType.EOF))


if __name__ == '__main__':
    suite = TestSuite()
    suite.addTest(LexerTest('testCSS'))
    # 执行测试
    runner = TextTestRunner()
    runner.run(suite)
