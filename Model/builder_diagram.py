from abc import ABCMeta, abstractmethod
from Model.diagram import Diagram


class BuilderDiagram(metaclass=ABCMeta):

    def __init__(self):
        self.data = Diagram()

    def results(self):
        return self.data

    @abstractmethod
    def set_class_name(self):
        pass

    @abstractmethod
    def set_relationship(self):
        pass

    @abstractmethod
    def set_attributes(self):
        pass

    @abstractmethod
    def set_methods(self):
        pass
