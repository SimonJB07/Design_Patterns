from View.view_file_location import ViewFileLocation
from Controller.main_error_checker import ErrorChecker


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

        from Controller.main_controller import MainController
        with open(output_file_name, "w") as output_file:
            for item in overall_content:
                file_output = dict(item)
                print(f"", file=output_file)
                for k, v in file_output.items():
                    if 'class_name_key' in k:
                        MainController.class_print(v, output_file)
                    elif 'relationship_key' in k:
                        MainController.relationship_print(v, output_file)
                    elif 'attributes_key' in k:
                        MainController.attribute_print(v, output_file)
                    elif 'methods_key' in k:
                        MainController.methods_print(v, output_file)



