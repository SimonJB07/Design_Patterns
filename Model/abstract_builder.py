
from abc import ABCMeta, abstractmethod


# Abstract Builder
class Builder(metaclass=ABCMeta):

    def __init__(self):
        self.data = {}

    def reset(self):
        self.data = None

    def get_results(self):
        return self.data

    @abstractmethod
    def set_class(self, cls, counter):
        pass

    @abstractmethod
    def set_relationship(self, rel, counter):
        pass

    @abstractmethod
    def set_attributes(self, att, counter):
        pass

    @abstractmethod
    def set_methods(self, met, counter):
        pass

    @abstractmethod
    def specification(self, output):
        pass
