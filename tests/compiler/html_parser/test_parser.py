from toybrowser.compiler.html_lexer.lexer import Lexer
from toybrowser.compiler.html_parser.parser import Parser
from toybrowser.compiler.html_parser.model.text_node import TextNode
from toybrowser.compiler.html_parser.model.element_node import ElementNode
from unittest import TestCase, TestSuite, TextTestRunner


class LexerTest(TestCase):
    def setUp(self) -> None:
        self.file = open("../../resources/sample.html")
        lexer = Lexer(self.file.readlines())
        self.parser = Parser(lexer)

    def tearDown(self) -> None:
        self.file.close()

    def test(self):
        text_node = TextNode("Hello world!")
        p = ElementNode(children=[text_node], tag_name="p")
        attributes = {
            "id": "hello-world",
        }
        div1 = ElementNode([p], "div", attributes)

        text_node = TextNode("Title")
        h1 = ElementNode([text_node], "h1")

        text_node = TextNode("From a happy toy browser.")
        attributes = {
            "class": "author",
        }
        div2 = ElementNode([text_node], "div", attributes)

        body = ElementNode([h1, div1, div2], "body")
        html = ElementNode([body], "html")

        self.assertEqual(html, self.parser.parse())


if __name__ == '__main__':
    suite = TestSuite()
    suite.addTest(LexerTest('test'))
    # 执行测试
    runner = TextTestRunner()
    runner.run(suite)
