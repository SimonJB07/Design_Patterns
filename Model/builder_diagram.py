from abc import ABCMeta, abstractmethod


# Abstract Builder
class BuilderDiagram(metaclass=ABCMeta):

    def __init__(self):
        self.data = {}

    # def reset(self):
    # return self.data = None

    def results(self):
        return self.data

    @abstractmethod
    def set_class(self, clsname):
        pass

    @abstractmethod
    def set_relationship(self, rel):
        pass

    @abstractmethod
    def set_attributes(self, att):
        pass

    @abstractmethod
    def set_methods(self, met):
        pass
