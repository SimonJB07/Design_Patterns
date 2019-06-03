from Controller.main_error_checker import ErrorChecker
from View.view_file_location import ViewFileLocation
from Model.format_data import FormatData


class FileReader:

    def __init__(self):
        self.__classname = ""
        self.__relationship = list()
        self.__attributes = list()
        self.__methods = list()

    def file_reader(self, input_file_name):
        """this takes in a string and loops thought to
        get a list of strings
        it also checks the input and validates the data at the
        end before passing the data
        """
        overall_reader_file = []
        ErrorChecker.error_type(str, input_file_name, "FILE NAME DON\'T LOAD: data type is not corrected")
        ErrorChecker.error_name(ViewFileLocation.input_location(), input_file_name, "ERROR: INPUT FILE IS NOT FIND")

        from Controller.main_controller import MainController
        with open(input_file_name, 'r') as diagram_file:
            for line in diagram_file:
                if ('--' or '..') in line:
                    self.__relationship.append(line)
                    print(self.__relationship)
                elif 'class' in line:
                    FileReader.set_class(self, line)
                elif ':' in line:
                    self.__attributes.append(line)
                elif '(' in line:
                    self.__methods(line)
                elif '}' in line:
                    pass
                temp_line = line.replace('\n', '').replace(' ', '')
                overall_reader_file.append(temp_line)
            if MainController.pass_validate_data(overall_reader_file):
                MainController.pass_set_up(overall_reader_file)
            else:
                print('ERROR: FILE DON\'T LOADED')

    def set_class(self, class_name):
        python_class_name = ""
        # ErrorChecker.error_type(str, self.data.__class, "ERROR: SETUP CLASS NAME: data type is not corrected")
        try:
            class_name = python_class_name.replace("class", '').replace('{', '')
            self.__classname = python_class_name
            print(python_class_name)
        except Exception as e:
            print("PYTHON CLASS NAME ERROR: ")
            print(e)

    def set_relationship(self, relationship):
        # ErrorChecker.error_type(str, self.data.__relationship, "SETUP RELATIONSHIP: data type is not corrected")
        try:
            rel_value = ""
            relationship = rel_value.replace("--", ": ")
            self.data.set_relationship(FormatData.format_relationship(rel_value))
        except Exception as e:
            print("RELATIONSHIP VALUE ERROR: ")
            print(e)

    def set_attributes(self, attribute):
        # ErrorChecker.error_type(str,  self.data.set_attributes(), "ATTRIBUTE NAME: datatype not corrected ")
        try:
            FileReader.attribute_clean(attribute)
        except Exception as e:
            print("ATTRIBUTE NAME ERROR: ")
            print(e)

    def attribute_clean(self, att_data):
        temp_att = FormatData.clear_up_data(att_data)
        format_attribute = FormatData.reverse_words(temp_att)
        return format_attribute

    def set_methods(self, methods):
        # ErrorChecker.error_type(str, self.data.set_methods() , "SETUP METHOD NAME: data type is not corrected")
        try:
            FileReader.method_clean(methods)
        except Exception as e:
            print("METHOD NAME ERROR: ")
            print(e)

    def method_clean(self, method_data):
        temp_met = method_data.replace('void', '')
        return FormatData.clear_up_data(temp_met).replace('str ', '')

