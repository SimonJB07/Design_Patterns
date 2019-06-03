from abc import ABCMeta, abstractmethod


class BuilderAbstractDiagram(metaclass=ABCMeta):

    def __init__(self, data=None):
        self.data = data

    def reset(self):
        return self.data

    def results(self):
        return self.data

    @abstractmethod
    def set_class(self):
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
