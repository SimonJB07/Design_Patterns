class Relationship:
    def __init__(self):
        self.__relationship = None

    @property
    def relationship(self):
        return self.__relationship

    @relationship.setter
    def rel(self, rel):
        self.__relationship = rel
