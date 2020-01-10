from .box_type import BoxType


class LayoutBox:
    def __init__(self, dimension=None, box_type=BoxType.Block, children=()):
        self.dimension = dimension
        self.box_type = box_type
        self.children = children

    def get_inline_container(self):
        

    def __eq__(self, other):
        if other is None:
            return False
        return self.dimension == other.dimension and self.box_type == other.box_type\
               and self.children == other.children

    def __str__(self):
        return "LayoutBox(dimension:{}, box_type:{}, children:{})".format(self.dimension, self.box_type, self.children)

    def __repr__(self):
        return self.__str__()
