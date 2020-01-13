from .layout_box import LayoutBox
from .box_type import BoxType


class LayoutTreeConstructor:

    def build_tree(self, styled_node):
        root = LayoutBox(styled_node, box_type=styled_node.display())
        for child in styled_node.children:
            if child.display() == BoxType.Block:
                root.children.append(LayoutBox(child, box_type=child.display()))
            elif child.display() == BoxType.Inline:
                return root.get_inline_container().children.append(LayoutBox(child, box_type=child.display()))