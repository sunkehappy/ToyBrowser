class EdgeSize:
    def __init__(self, top=0, right=0, bottom=0, left=0, horizontal=0, vertical=0, total=0):
        if total:
            top = right = bottom = left = total
        if vertical:
            top = bottom = vertical
        if horizontal:
            right = left = horizontal
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left

    def __eq__(self, other):
        if other is None:
            return False
        return self.top == other.top and self.right == other.right and \
               self.bottom == other.bottom and self.left == other.left

    def __str__(self):
        return "EdgeSize({}, {}, {}, {})".format(self.top, self.right, self.bottom, self.left)

    def __repr__(self):
        return self.__str__()
