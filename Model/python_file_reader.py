from Controller.main_error_checker import ErrorChecker
from Model.Components.attributes import Attributes
from Model.Components.class_names import ClassName
from Model.Components.methods import Method
from Model.builder_abstract_diagram import BuilderAbstractDiagram
from Model.Components.relationship import Relationship
from View.view_file_location import ViewFileLocation
from Model.format_data import FormatData


# Concrete Builder
class BuilderPythonDiagramFileReader(BuilderAbstractDiagram):

    def file_reader(self, input_file_name):
        overall_reader_file = []
        ErrorChecker.error_type(str, input_file_name, "FILE NAME DON\'T LOAD: data type is not corrected")
        ErrorChecker.error_name(ViewFileLocation.input_location(), input_file_name, "ERROR: INPUT FILE IS NOT FIND")

        from Controller.main_controller import MainController
        with open(input_file_name, 'r') as diagram_file:
            for line in diagram_file:
                if ('--' or '..') in line:
                    self.data.set_relationship(line)
                elif 'class' in line:
                    self.data.set_class(line)
                elif ':' in line:
                    self.data.set_attributes(line)
                elif '(' in line:
                    self.data.set_methods(line)
                elif '}' in line:
                    pass
                temp_line = line.replace('\n', '').replace(' ', '')
                overall_reader_file.append(temp_line)
            if MainController.pass_validate_data(overall_reader_file):
                MainController.pass_set_up(overall_reader_file)
            else:
                print('ERROR: FILE DON\'T LOADED')

    def set_class(self, clsname):
        class_name = ClassName()
        # ErrorChecker.error_type(str, clsname, "ERROR: SETUP CLASS NAME: data type is not corrected")
        try:
            python_class_name = clsname.replace("class", '').replace('{', '')
            class_name.name = python_class_name
            return class_name
        except Exception as e:
            print("PYTHON CLASS NAME ERROR: ")
            print(e)

    def set_relationship(self, relation):
        relationship = Relationship()
        # ErrorChecker.error_type(str, relation, "SETUP RELATIONSHIP: data type is not corrected")
        try:
            rel_value = relation.replace("--", ": ")
            relationship.rel = FormatData.format_relationship(rel_value)
            return relationship
        except Exception as e:
            print("RELATIONSHIP VALUE ERROR: ")
            print(e)

    def set_attributes(self, att):
        attribute = Attributes()
        # ErrorChecker.error_type(str,  att, "ATTRIBUTE NAME: datatype not corrected ")
        try:
            attribute.att = self.attribute_clean(att)
            return attribute
        except Exception as e:
            print("ATTRIBUTE NAME ERROR: ")
            print(e)

    def attribute_clean(self, att_data):
        temp_att = FormatData.clear_up_data(att_data)
        format_attribute = FormatData.reverse_words(temp_att)
        return format_attribute

    def set_methods(self, met):
        method = Method()
        # ErrorChecker.error_type(str, met , "SETUP METHOD NAME: data type is not corrected")
        try:
            method.method = self.method_clean(met)
            return method
        except Exception as e:
            print("METHOD NAME ERROR: ")
            print(e)

    def method_clean(self, method_data):
        print(method_data)
        temp_met = method_data.replace('void', '')
        return FormatData.clear_up_data(temp_met).replace('str ', '')

