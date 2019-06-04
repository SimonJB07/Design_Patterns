from Model.director import Director
from View.view_file_location import ViewFileLocation
# from Tests.main_test_file import MainTests
from Model.validate_data import ValidateData
from Model.python_file_reader import BuilderPythonDiagramFileReader


class MainController:

    @staticmethod
    def main():
        try:
            MainController.read_data()
            # MainController.get_doctest()
            # MainController.get_unittest()
            print("fucking work")
            python_diagram = BuilderPythonDiagramFileReader()
            dirt = Director()
            dirt.set_builder(python_diagram)
            python = dirt.contuctor()
            python.specification()
        except Exception as e:
                print("MAIN ERROR: python or director")
                print(e)


    @staticmethod
    def read_data():
        BuilderPythonDiagramFileReader.file_reader(BuilderPythonDiagramFileReader(), ViewFileLocation().input_location())

    @staticmethod
    def get_unittest():
        pass
        # return MainTests.unit_test()

    @staticmethod
    def get_doctest():
        pass
        # return MainTests.doc_tests()

    @staticmethod
    def pass_set_up(output):
        pass# SetUpDiagram.set_over_string(SetUpDiagram(), output)

    @staticmethod
    def pass_validate_data(output):
        return ValidateData.validate_test_loader(output)
