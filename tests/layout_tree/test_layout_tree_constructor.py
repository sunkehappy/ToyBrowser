from toybrowser.compiler.html_lexer.lexer import Lexer as HtmlLexer
from toybrowser.compiler.html_parser.parser import Parser as HtmlParser
from toybrowser.compiler.html_parser.model.element_node import ElementNode
from toybrowser.compiler.html_parser.model.text_node import TextNode
from toybrowser.compiler.css_lexer.lexer import Lexer as CssLexer
from toybrowser.compiler.css_parser.parser import Parser as CssParser
from toybrowser.style_tree.style_tree_constructor import StyleTreeConstructor
from toybrowser.style_tree.styled_node import StyledNode
from toybrowser.layout_tree.layout_box import LayoutBox
from toybrowser.compiler.css_parser.model.color import Color
from unittest import TestCase, TestSuite, TextTestRunner


class LexerTest(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test(self):
        html_file = open("../resources/sample.html")
        html_lexer = HtmlLexer(html_file.readlines())
        html_parser = HtmlParser(html_lexer)
        html_file.close()

        css_file = open("../resources/sample.css")
        css_lexer = CssLexer(css_file.readlines())
        css_parser = CssParser(css_lexer)
        css_file.close()

        root = html_parser.parse()
        css_rules = css_parser.parse()
        style_tree_constructor = StyleTreeConstructor()

        text_node = TextNode("Hello world!")
        p = ElementNode(children=[text_node], tag_name="p")
        p_styled_node = StyledNode(p)
        attributes = {
            "id": "hello-world",
        }
        div1 = ElementNode([p], "div", attributes)
        div1_styled_node = StyledNode(div1, {
            "color": ["red"]
        }, [p_styled_node])

        text_node = TextNode("Title")
        h1 = ElementNode([text_node], "h1")
        h1_styled_node = StyledNode(h1, {
            "margin": ["auto"],
            "color": Color(hex_str="#cc0000")
        })

        text_node = TextNode("From a happy toy browser.")
        attributes = {
            "class": "author",
        }
        div2 = ElementNode([text_node], "div", attributes)
        div2_styled_node = StyledNode(div2, {
            "margin-bottom": ["20px"],
            "padding": ["10px"]
        })

        body = ElementNode([h1, div1, div2], "body")
        body_styled_node = StyledNode(body, children=[h1_styled_node, div1_styled_node, div2_styled_node])
        html = ElementNode([body], "html")
        style_tree = StyledNode(html, children=[body_styled_node])

        self.assertEqual(style_tree_constructor.build_tree(root, css_rules), style_tree)


if __name__ == '__main__':
    suite = TestSuite()
    suite.addTest(LexerTest('test'))
    # 执行测试
    runner = TextTestRunner()
    runner.run(suite)
