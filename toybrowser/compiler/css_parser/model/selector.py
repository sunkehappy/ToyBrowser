class Selector:
    def __init__(self, id=None, classes=(), tag_name=None):
        self.id = id
        self.classes = classes
        self.tag_name = tag_name

    def __eq__(self, other):
        if other is None:
            return False
        return self.id == other.id and self.classes == other.classes and self.tag_name == other.tag_name

    def __str__(self):
        if self.id:
            return "Selector(id: {})".format(self.id)
        elif self.classes:
            return "Selector(classes: {})".format(self.classes)
        else:
            return "Selector(tag_name: {})".format(self.tag_name)

    def __repr__(self):
        return self.__str__()
