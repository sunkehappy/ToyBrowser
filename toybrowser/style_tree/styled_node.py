from ..layout_tree.box_type import BoxType


class StyledNode:
    def __init__(self, node, css_map=None, children=()):
        if css_map is None:
            css_map = {}
        if not children:
            children = ()
        self.node = node
        self.css_map=css_map
        self.children = children

    def display(self):
        display_value = self.css_map.get("display", None)
        if display_value == "block":
            return BoxType.Block
        elif display_value == "inline":
            return BoxType.Inline
        else:
            raise Exception("unexpected display value:{}".format(display_value))

    def __eq__(self, other):
        if other is None:
            return False
        return self.node == other.node and self.css_map == other.css_map and self.children == other.children

    def __str__(self):
        return "StyledNode(node:{}\ncss_map:{}\nchildren:{})".format(self.node, self.css_map, self.children)

    def __repr__(self):
        return self.__str__()
