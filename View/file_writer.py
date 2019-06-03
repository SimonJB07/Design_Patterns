from View.view_file_location import ViewFileLocation
from Controller.main_error_checker import ErrorChecker
from Controller.director import Director


class FileWriter:
    """The class's docstring"""

    def file_writer(self, overall_content):
        """this writes to a file using dict as kes
        and having the values as the print outs
        the loop steps though each key in dict
        """
        output_file_name = ViewFileLocation.output_location()

        ErrorChecker.error_type(str, output_file_name, "FILE NAME: datatype not corrected")
        ErrorChecker.error_type(list, overall_content, "OVERALL DATA: datatype not corrected")
        ErrorChecker.error_name(ViewFileLocation.output_location(), output_file_name, "FILE IS NOT NAMED CORRECTLY")



