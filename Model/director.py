from Model.diagram import Diagram


class Director(object):
    __builder = None

    def set_builder(self, diagram):
        self.__bid = diagram

    def contuctor(self):
        diagram = Diagram()
        self.__bid.set_class(self)
        diagram.set_class(self)
        self.__bid.set_relationship(self)
        diagram.set_relationship(self)
        self.__bid.set_methods(self)
        diagram.set_methods(self)
        self.__bid.set_attributes(self)
        diagram.set_attributes(self)

