from Model.builder_abstract_diagram import BuilderAbstractDiagram
from Model.diagram import Diagram
from Controller.main_error_checker import ErrorChecker
from Model.format_data import FormatData


class BuilderPythonDiagram(BuilderAbstractDiagram):
    def __init__(self):
        super().__init__(Diagram())

    def set_class(self):
        python_class_name = ""
        # ErrorChecker.error_type(str, self.data.__class, "ERROR: SETUP CLASS NAME: data type is not corrected")
        try:
            self.data.__class = python_class_name.replace("class", '').replace('{', '')
            self.data.set_class(python_class_name)
        except Exception as e:
            print("PYTHON CLASS NAME ERROR: ")
            print(e)

    def set_relationship(self):
        # ErrorChecker.error_type(str, self.data.__relationship, "SETUP RELATIONSHIP: data type is not corrected")
        try:
            rel_value = ""
            self.data.__relationship = rel_value.replace("--", ": ")
            self.data.set_relationship(FormatData.format_relationship(rel_value))
        except Exception as e:
            print("RELATIONSHIP VALUE ERROR: ")
            print(e)

    def set_attributes(self):
        # ErrorChecker.error_type(str,  self.data.set_attributes(), "ATTRIBUTE NAME: datatype not corrected ")
        try:
            BuilderPythonDiagram.attribute_clean(self.data.set_attributes())
        except Exception as e:
            print("ATTRIBUTE NAME ERROR: ")
            print(e)

    @staticmethod
    def attribute_clean(att_data):
        temp_att = FormatData.clear_up_data(att_data)
        format_attribute = FormatData.reverse_words(temp_att)
        return format_attribute

    def set_methods(self):
        # ErrorChecker.error_type(str, self.data.set_methods() , "SETUP METHOD NAME: data type is not corrected")
        try:
            BuilderPythonDiagram.method_clean(self.data.set_methods())
        except Exception as e:
            print("METHOD NAME ERROR: ")
            print(e)

    @staticmethod
    def method_clean(method_data):
        temp_met = method_data.replace('void', '')
        return FormatData.clear_up_data(temp_met).replace('str ', '')

