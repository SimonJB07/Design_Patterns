from Controller.main_error_checker import ErrorChecker
from View.view_file_location import ViewFileLocation


class Director(object):
    def __init__(self, d):
        self.__bid = d

    def set_builder(self, diagram):
        self.__bid = diagram

    def file_reader(self, input_file_name):
        ErrorChecker.error_type(str, input_file_name, "FILE NAME DON\'T LOAD: data type is not corrected")
        ErrorChecker.error_name(ViewFileLocation.input_location(), input_file_name, "ERROR: INPUT FILE IS NOT FIND")
        counter = 0
        with open(input_file_name, 'r') as diagram_file:
            for line in diagram_file:
                if '--' or '..' or 'class' in line:
                    if 'class' in line:
                        self.__bid.set_class(line, counter)
                    elif ('--' or '..') in line:
                        self.__bid.set_relationship(line, counter)
                    elif ':' in line:
                        self.__bid.set_attributes(line, counter)
                    elif '(' in line:
                        self.__bid.set_methods(line, counter)
                    elif '}' in line:
                        counter += 1
