from Controller.main_error_checker import ErrorChecker
from Model.Components.attributes import Attributes
from Model.Components.class_names import ClassName
from Model.Components.methods import Method
from Model.builder_diagram import BuilderDiagram
from Model.Components.relationship import Relationship

from Model.format_data import FormatData


# Concrete Builder
class BuilderPythonDiagramFileReader(BuilderDiagram):

    def __instancecheck__(self, instance):
        self.__uml_list = []
        self.__class_dict = {}
        self.__class_relationship = []
        self.__attribute_list = []
        self.__method_list = []

    def add_overall_content(self, key, value):
        self.data[key] = value

    def add_class(self, key, value):
        self.data[key] = value


    def add_relationship(self, key, value):
        self.data[key] = value

    def add_methods(self, key, value):
        self.__method_list[key] = value

    def add_attributes(self, key, value):
        self.data[key] = value




    def set_class(self, clsname):
        class_name = ClassName()
        # ErrorChecker.error_type(str, clsname, "ERROR: SETUP CLASS NAME: data type is not corrected")
        try:
            python_class_name = clsname.replace("class", '').replace('{', '').replace('\n', '')
            class_name.name = python_class_name
            self.add_class("Class Name", class_name.name)
        except Exception as e:
            print("PYTHON CLASS NAME ERROR: ")
            print(e)

    def set_relationship(self, relation):
        relationship = Relationship()
        # ErrorChecker.error_type(str, relation, "SETUP RELATIONSHIP: data type is not corrected")
        try:
            # print(relation)
            rel_value = relation.replace("--", ": ").replace('\n', '')
            relationship.rel = FormatData.format_relationship(rel_value)
            self.add_value("Relationships:", relationship.rel)
        except Exception as e:
            print("RELATIONSHIP VALUE ERROR: ")
            print(e)

    def set_attributes(self, att):
        att_key = "Attributes:"
        attribute = Attributes()
        # ErrorChecker.error_type(str,  att, "ATTRIBUTE NAME: datatype not corrected ")
        try:
            # print(att)
            attribute.att = self.attribute_clean(att).replace('\n', '')
            self.data.setdefault(att_key, [])
            self.data[att_key].append(attribute.att)
        except Exception as e:
            print("ATTRIBUTE NAME ERROR: ")
            print(e)

    def attribute_clean(self, att_data):
        temp_att = FormatData.reverse_words(att_data)
        format_attribute = FormatData.clear_up_data(temp_att)

        return format_attribute

    def set_methods(self, met):
        met_key = "Methods:"
        method = Method()
        ErrorChecker.error_type(str, met , "SETUP METHOD NAME: data type is not corrected")
        try:
            method.method = self.method_clean(met).replace('\n', '')
            self.data.setdefault(met_key, [])
            self.data[met_key].append(method.method)
        except Exception as e:
            print("METHOD NAME ERROR: ")
            print(e)

    def method_clean(self, method_data):
        # meth = filter(lambda x: x['void'], method_data)
        temp_met = method_data.replace('void', '')
        return FormatData.clear_up_data(temp_met).replace('str ', '')

