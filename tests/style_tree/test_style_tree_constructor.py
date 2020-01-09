from toybrowser.compiler.html_lexer.lexer import Lexer as HtmlLexer
from toybrowser.compiler.html_parser.parser import Parser as HtmlParser
from toybrowser.compiler.html_parser.model.element_node import ElementNode
from toybrowser.compiler.html_parser.model.text_node import TextNode
from toybrowser.compiler.css_lexer.lexer import Lexer as CssLexer
from toybrowser.compiler.css_parser.parser import Parser as CssParser
from toybrowser.style_tree.style_tree_constructor import StyleTreeConstructor
from toybrowser.style_tree.styled_node import StyledNode
from unittest import TestCase, TestSuite, TextTestRunner


class LexerTest(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test(self):
        html_file = open("../../resources/sample.html")
        html_lexer = HtmlLexer(html_file.readlines())
        html_parser = HtmlParser(html_lexer)
        html_file.close()

        css_file = open("../../resources/sample.css")
        css_lexer = CssLexer(css_file.readlines())
        css_parser = CssParser(css_lexer)
        css_file.close()

        root = html_parser.parse()
        css_rules = css_parser.parse()
        style_tree_constructor = StyleTreeConstructor()

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

        style_tree = StyledNode()

        self.assertEqual(style_tree_constructor.build_tree(root, css_rules), style_tree)


if __name__ == '__main__':
    suite = TestSuite()
    suite.addTest(LexerTest('test'))
    # 执行测试
    runner = TextTestRunner()
    runner.run(suite)
