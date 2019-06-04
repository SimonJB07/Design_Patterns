from Model.diagram import Diagram


class Director(object):

    def __init__(self):
        self.__bid = None

    def set_builder(self, diagram):
        self.__bid = diagram

    def contuctor(self, input_file_name):
        #self.__bid.set_class(self)
        #self.__bid.set_relationship(self)
        #self.__bid.set_methods(self)
        #self.__bid.set_attributes(self)

        # def file_reader(self, ):
            overall_reader_file = []
            # ErrorChecker.error_type(str, input_file_name, "FILE NAME DON\'T LOAD: data type is not corrected")
            # ErrorChecker.error_name(ViewFileLocation.input_location(), input_file_name, "ERROR: INPUT FILE IS NOT FIND")

            from Controller.main_controller import MainController
            with open(input_file_name, 'r') as diagram_file:
                for line in diagram_file:
                    if ('--' or '..') in line:
                        self.__bid.set_relationship(line)
                    elif 'class' in line:
                        self.__bid.set_class(line)
                    elif ':' in line:
                        self.__bid.set_attributes(line)
                    elif '(' in line:
                        self.__bid.set_methods(line)
                    elif '}' in line:
                        pass
                    temp_line = line.replace('\n', '').replace(' ', '')
                    overall_reader_file.append(temp_line)
                if MainController.pass_validate_data(overall_reader_file):
                    MainController.pass_set_up(overall_reader_file)
                else:
                    print('ERROR: FILE DON\'T LOADED')
                # print(overall_reader_file)


