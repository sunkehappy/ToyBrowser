class StyledNode:
    def __init__(self, node, css_map=None, children=()):
        if css_map is None:
            css_map = {}
        self.node = node
        self.cssMap=css_map
        self.children = children
