class Director(object):

    def __init__(self, diagram):
        self.__bid = diagram

    def contuctor(self):
        self.__bid.set_classname()
        self.__bid.set_relationship()
        self.__bid.set_methods()
        self.__bid.set_attributes()

