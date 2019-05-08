from Controller.main_error_checker import ErrorChecker
from View.view_file_location import ViewFileLocation


class FileReader:

    @staticmethod
    def file_reader(input_file_name):
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
                temp_line = line.replace('\n', '').replace(' ', '')
                overall_reader_file.append(temp_line)
            if MainController.pass_validate_data(overall_reader_file):
                MainController.pass_set_up(overall_reader_file)
            else:
                print('ERROR: FILE DON\'T LOADED')

