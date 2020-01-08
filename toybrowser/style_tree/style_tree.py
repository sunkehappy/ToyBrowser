from .styled_node import StyledNode


class StyleTree:
    def matched_rule_for_node(self):

    def style_for_node(self, node, css_rules):
        css_map = {}
        rules = self.matched_rule_for_node(node, css_rules)

    def build_tree(self, root, css_rules):
        css_map = self.style_for_node(root, css_rules)
        children = [map(StyleTree.build_tree, root.children)]
        styled_node = StyledNode(root, css_map, children)
        return styled_node
