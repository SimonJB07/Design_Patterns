class Method:
    def __init__(self):
        self.__method = None

    @property
    def methods(self):
        return self.__method

    @methods.setter
    def method(self, met):
        self.__method = met
