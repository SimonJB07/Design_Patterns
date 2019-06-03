class Diagram:
    def __init__(self):
        self.__classname = ""
        self.__relationship = list()
        self.__attributes = list()
        self.__methods = list()

    def set_class(self, classname):
        self.__classname = classname

    def set_relationship(self, relation):
        self.__relationship.append(relation)

    def set_attributes(self, attrib):
        self.__attributes.append(attrib)

    def set_methods(self, method):
        self.__methods.append(method)

    def specification_class(self):
        print(f"class {self.__classname}:")

    def specification_relationship(self):
        print(f"        self.{self.__relationship[0]}")

    def specification_attributes(self):
        print(f"        self.{self.__attributes[0]}")

    def specification_methods(self):
        print(f"    @staticmethod")
        print(f"    def {self.__methods[0]}:")
        print(f"        pass\n")

    def specification(self):
        Diagram.specification_class(self)
        Diagram.specification_relationship(self)
        Diagram.specification_attributes(self)
        Diagram.specification_methods(self)

