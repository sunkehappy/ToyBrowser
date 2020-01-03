from .node import Node
from .node_type import NodeType


class ElementNode(Node):
    def __init__(self, children=(), tag_name="", attributes=None):
        super(ElementNode, self).__init__(children, NodeType.Element)

        if attributes is None:
            attributes = {}
        self.tag_name = tag_name
        self.attributes = attributes

    def __eq__(self, other):
        if other is None:
            return False
        eq = super(ElementNode, self).__eq__(other)
        return eq and self.tag_name == other.tag_name and self.attributes == other.attributes

    def __str__(self):
        return "tag:{}, attributes:{}, children:{}".format(self.tag_name, self.attributes, self.children)

    def __repr__(self):
        return "tag:{}, attributes:{}, children:{}".format(self.tag_name, self.attributes, self.children)
