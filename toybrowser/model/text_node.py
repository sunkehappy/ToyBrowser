from toybrowser.model import node, node_type


class TextNode(node.Node):
    def __init__(self, text):
        super(TextNode, self).__init__((), node_type.NodeType.Text)
        self.text = text
