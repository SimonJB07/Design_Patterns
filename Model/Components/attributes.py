class Attributes:
    def __init__(self):
        self.__attribute = None

    @property
    def attribute(self):
        return self.__attribute

    @attribute.setter
    def att(self, att):
        self.__attribute = att
