from toybrowser.compiler.css_lexer.lexer import Lexer
from toybrowser.compiler.css_parser.parser import Parser
from toybrowser.compiler.css_parser.model.css_rule import CSSRule
from toybrowser.compiler.css_parser.model.selector import Selector
from toybrowser.compiler.css_parser.model.declaration import Declaration
from toybrowser.compiler.css_parser.model.color import Color
from unittest import TestCase, TestSuite, TextTestRunner


class LexerTest(TestCase):
    def setUp(self) -> None:
        self.file = open("../../resources/sample.css")
        lexer = Lexer(self.file.readlines())
        self.parser = Parser(lexer)

    def tearDown(self) -> None:
        self.file.close()

    def test(self):
        selectors = [Selector(tag_name="h1"), Selector(tag_name="h2"), Selector(tag_name="h3")]
        declarations = [Declaration("margin", ["auto"]), Declaration("color", Color(hex_str="#cc0000"))]
        rules = [CSSRule(selectors, declarations)]

        selectors = [Selector(tag_name="div.note")]
        declarations = [Declaration("margin-bottom", ["20px"]), Declaration("padding", ["10px"])]
        rules.append(CSSRule(selectors, declarations))

        selectors = [Selector(id="answer")]
        declarations = [Declaration("display", ["none"])]
        rules.append(CSSRule(selectors, declarations))

        self.assertEqual(rules, self.parser.parse())


if __name__ == '__main__':
    suite = TestSuite()
    suite.addTest(LexerTest('test'))
    # 执行测试
    runner = TextTestRunner()
    runner.run(suite)
