from Model.relationships import Relationships
from Model.class_name import ClassName
from Model.attributes import Attribute
from Model.method import Method
from Controller.main_error_checker import ErrorChecker


class SetUp(object):
    """The class's docstring
    """
    def __init__(self):
        self.full_class_dict = {}
        self.relationship_list = []
        self.attribute_list = []
        self.method_list = []
        self.final_uml_list = []
        self.overall_content = []

    def pass_to_file_handler(self):
        from Controller.main_controller import MainController
        MainController.write_name(self.final_uml_list)

    def set_over_string(self, overall_file):
        """This checks to see if there is a class dict
        """
        ErrorChecker.error_type(list, overall_file, "SETUP OVER STRING: datatype not corrected")
        try:
            self.set_string(overall_file)
        except Exception as e:
            print("OVER STRING ERROR: This don'ts work ")
            print(e)

    def set_string(self, overall_file):
        for line in overall_file:
            if ('--' or '..') in line:
                self.relationship_list.append(Relationships.error_check_relationship(line))
            elif 'class' in line:
                self.full_class_dict['class_name_key'] = ClassName.set_up_class_name(line)
            elif ':' in line:
                self.attribute_list.append(Attribute.error_check_attribute(line))
            elif '(' in line:
                self.method_list.append(Method.error_check_method(line))
            elif '}' in line:
                self.set_keys_value()
                self.pass_data()
        self.pass_to_file_handler()

    def set_keys_value(self):
        self.full_class_dict['relationship_key'] = self.relationship_list
        self.full_class_dict['attributes_key'] = self.attribute_list
        self.full_class_dict['methods_key'] = self.method_list

    def pass_data(self):
        self.overall_content = self.full_class_dict
        temp_dict = self.full_class_dict.copy()
        self.final_uml_list.append(temp_dict)
        self.clean_data()

    def clean_data(self):
        self.full_class_dict.clear()
        self.full_class_dict = {}
        self.attribute_list = []
        self.method_list = []
        self.relationship_list = []
