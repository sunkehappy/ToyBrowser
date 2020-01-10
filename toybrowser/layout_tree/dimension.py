from .edge_size import EdgeSize
from .rect import Rect


class Dimension:
    def __init__(self, content, padding=None, border=None, margin=None):
        if not content:
            content = Rect()
        if not padding:
            padding = EdgeSize()
        if not border:
            border = EdgeSize()
        if not margin:
            margin = EdgeSize()

        self.content = content
        self.padding = padding
        self.border = border
        self.margin = margin

    def __eq__(self, other):
        if other is None:
            return False
        return self.content == other.content and self.padding == other.padding and \
               self.border == other.border and self.margin == other.margin

    def __str__(self):
        return "Dimension(content:{}, padding:{}, border:{}, margin:{})".format(
            self.content, self.padding, self.border, self.margin)

    def __repr__(self):
        return self.__str__()
