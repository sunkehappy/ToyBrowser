from .layout_box import LayoutBox
from .display_type import DisplayType


class LayoutTreeConstructor:
    def build_tree(self, style_tree):
        root = LayoutBox(box_type=style_tree.display())
        for styled_node in style_tree.children:
            if styled_node.display() == DisplayType.Flex:
                root.children.append(self.build_tree(styled_node))
            elif styled_node.display() == DisplayType.InlineFlex:
                root.get_inline_container().children.append(self.build_tree(styled_node))

