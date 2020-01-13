from .box_type import BoxType


class LayoutBox:
    def __init__(self, styled_node=None, dimension=None, box_type=BoxType.Block, children=()):
        self.styled_node = styled_node
        self.dimension = dimension
        self.box_type = box_type
        self.children = children

    def get_inline_container(self):
        if self.box_type == BoxType.Inline or self.box_type == BoxType.Anonymous:
            return self
        elif self.box_type == BoxType.Anonymous:
            if self.children[-1].box_type != BoxType.Anonymous:
                self.children.append(LayoutBox(box_type=BoxType.Anonymous))
            return self.children[-1]

    def __eq__(self, other):
        if other is None:
            return False
        return self.dimension == other.dimension and self.box_type == other.box_type\
               and self.children == other.children

    def __str__(self):
        return "LayoutBox(dimension:{}, box_type:{}, children:{})".format(self.dimension, self.box_type, self.children)

    def __repr__(self):
        return self.__str__()
