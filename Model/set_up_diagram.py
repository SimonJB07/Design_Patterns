from Model.builder_python_diagram import BuilderPythonDiagram
from Controller.main_error_checker import ErrorChecker


class SetUpDiagram(object):
    """The class's docstring
    """
    def __init__(self):
        self.overall_content = []

    def set_over_string(self, overall_file):
        """This checks to see if there is a class dict
        """
        ErrorChecker.error_type(list, overall_file, "SETUP OVER STRING: datatype not corrected")
        try:
            self.set_string(overall_file)
            print(overall_file)
        except Exception as e:
            print("OVER STRING ERROR: This dont's work ")
            print(e)

    def set_string(self, overall_file):
        for line in overall_file:
            if ('--' or '..') in line:
                BuilderPythonDiagram.data = (line)

            elif 'class' in line:
                BuilderPythonDiagram.set_class = line
            elif ':' in line:
                BuilderPythonDiagram.set_attributes = line
            elif '(' in line:
                BuilderPythonDiagram.set_methods = line
            elif '}' in line:
                pass


