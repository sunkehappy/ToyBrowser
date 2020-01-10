from toybrowser.compiler.html_lexer.lexer import Lexer
from toybrowser.compiler.html_lexer.token import Token
from toybrowser.compiler.html_lexer.token_type import TokenType
from unittest import TestCase, TestSuite, TextTestRunner


class LexerTest(TestCase):
    def setUp(self) -> None:
        self.html_file = open("../../resources/sample.html")
        self.lexer = Lexer()

    def tearDown(self) -> None:
        self.html_file.close()

    def testHTML(self):
        self.lexer.init_with_content(self.html_file.readlines())

        # test <html>
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.L_START_ANGLE_BRACKETS))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.IDENTIFIER, "html"))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.R_ANGLE_BRACKETS))

        # test <body>
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.L_START_ANGLE_BRACKETS))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.IDENTIFIER, "body"))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.R_ANGLE_BRACKETS))

        # test <h1>
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.L_START_ANGLE_BRACKETS))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.IDENTIFIER, "h1"))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.R_ANGLE_BRACKETS))

        # test "Title" in <h1></h1>
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.IDENTIFIER, "Title"))

        # test </h1>
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.L_END_ANGLE_BRACKETS))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.IDENTIFIER, "h1"))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.R_ANGLE_BRACKETS))

        # test <div id="hello-world">
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.L_START_ANGLE_BRACKETS))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.IDENTIFIER, "div"))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.IDENTIFIER, "id"))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.EQUAL))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.IDENTIFIER, "hello-world"))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.R_ANGLE_BRACKETS))

        # test <p>Hello <em>world</em>!</p>
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.L_START_ANGLE_BRACKETS))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.IDENTIFIER, "p"))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.R_ANGLE_BRACKETS))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.IDENTIFIER, "Hello world!"))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.L_END_ANGLE_BRACKETS))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.IDENTIFIER, "p"))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.R_ANGLE_BRACKETS))

        # test </div>
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.L_END_ANGLE_BRACKETS))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.IDENTIFIER, "div"))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.R_ANGLE_BRACKETS))

        # test <div class="author">
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.L_START_ANGLE_BRACKETS))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.IDENTIFIER, "div"))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.IDENTIFIER, "class"))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.EQUAL))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.IDENTIFIER, "author"))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.R_ANGLE_BRACKETS))

        # test string in above div
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.IDENTIFIER, "From a happy toy browser."))

        # test </div>
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.L_END_ANGLE_BRACKETS))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.IDENTIFIER, "div"))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.R_ANGLE_BRACKETS))

        # test </body>
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.L_END_ANGLE_BRACKETS))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.IDENTIFIER, "body"))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.R_ANGLE_BRACKETS))

        # test </html>
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.L_END_ANGLE_BRACKETS))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.IDENTIFIER, "html"))
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.R_ANGLE_BRACKETS))

        # test EOF
        self.assertEqual(self.lexer.get_next_token(), Token(TokenType.EOF))


if __name__ == '__main__':
    suite = TestSuite()
    suite.addTest(LexerTest('testHTML'))
    # 执行测试
    runner = TextTestRunner()
    runner.run(suite)
