class Node:
    def __init__(self, children=(), node_type=None):
        self.children = children
        self.node_type = node_type

    def __eq__(self, other):
        if other is None:
            return False
        eq = self.node_type == other.node_type
        eq = eq and len(self.children) == len(other.children)
        for i in range(len(self.children)):
            eq = eq and self.children[i] == other.children[i]
            if not eq:
                break
        return eq
