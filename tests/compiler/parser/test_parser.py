from toybrowser.compiler.lexer.lexer import Lexer
from toybrowser.compiler.parser.parser import Parser
from toybrowser.compiler.parser.model.text_node import TextNode
from toybrowser.compiler.parser.model.element_node import ElementNode
from unittest import TestCase, TestSuite, TextTestRunner


class LexerTest(TestCase):
    def setUp(self) -> None:
        self.file = open("../../resources/sample.html")
        lexer = Lexer(self.file.readlines())
        self.parser = Parser(lexer)

    def tearDown(self) -> None:
        self.file.close()

    def test(self):
        text_node = TextNode("world")
        em = ElementNode(children=[text_node], tag_name="em")
        text_node1 = TextNode("Hello ")
        text_node2 = TextNode("!")
        p = ElementNode(children=[text_node1, em, text_node2], tag_name="p")
        attributes = {
            "id": "main",
            "class": "test",
        }
        div = ElementNode([p], "div", attributes)
        text_node = TextNode("Title")
        h1 = ElementNode([text_node], "h1")
        body = ElementNode([h1, div], "body")
        html = ElementNode([body], "html")

        self.assertEqual(html, self.parser.parse())


if __name__ == '__main__':
    suite = TestSuite()
    suite.addTest(LexerTest('test'))
    # 执行测试
    runner = TextTestRunner()
    runner.run(suite)
