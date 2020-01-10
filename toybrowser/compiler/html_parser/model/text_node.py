from toybrowser.compiler.html_parser.model import node, node_type


class TextNode(node.Node):
    def __init__(self, text):
        super(TextNode, self).__init__((), node_type.NodeType.Text)
        self.text = text

    def __eq__(self, other):
        if other is None:
            return False
        eq = super(TextNode, self).__eq__(other)
        return eq and self.text == other.text

    def __str__(self):
        return "TextNode(text:{}, node_type{}, children:{})\n".format(self.text, self.node_type, self.children)

    def __repr__(self):
        return self.__str__()
