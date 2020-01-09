from .styled_node import StyledNode


class StyleTreeConstructor:
    def match_simple_selector(self, node, selector):
        if selector.tag_name and selector.tag_name != node.tag_name:
            return False
        if selector.id and selector.id != node.id():
            return False
        if selector.classes and node.classes() != selector.classes:
            return False
        return True

    def check_match_rule_for_node(self, node, css_rule):
        rule_map_list = []
        for selector in css_rule.selectors:
            if self.match_simple_selector(node, selector):
                rule_map_list.append((selector.specificity(), css_rule))
        return rule_map_list

    def matched_rule_for_node(self, node, css_rules):
        rule_map_list = []
        for css_rule in css_rules:
            rule_map_list.extend(self.check_match_rule_for_node(node, css_rule))
        return rule_map_list

    def style_for_node(self, node, css_rules):
        rules = self.matched_rule_for_node(node, css_rules)
        rules.sort(key=lambda x: x[0])
        values = {}
        for rule in rules:
            for declaration in rule[1].declarations:
                values[declaration.name] = declaration.value
        return values

    def build_tree(self, root, css_rules):
        css_map = self.style_for_node(root, css_rules)
        children = [map(StyleTreeConstructor.build_tree, root.children)]
        styled_node = StyledNode(root, css_map, children)
        return styled_node
