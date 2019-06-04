class ClassName:
    def __init__(self):
        self.__class_name = None

    @property
    def name(self):
        return self.__class_name

    @name.setter
    def name(self, cls):
        self.__class_name = cls
