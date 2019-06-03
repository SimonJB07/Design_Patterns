from Model.file_reader import FileReader
from View.view_file_location import ViewFileLocation
# from Tests.main_test_file import MainTests
from Model.set_up_diagram import SetUpDiagram
from Model.validate_data import ValidateData


class MainController:

    @staticmethod
    def main():
        try:
            MainController.read_data()
            MainController.get_doctest()
            MainController.get_unittest()
        except Exception as e:
            print("MAIN ERROR: main_controller.py error")
            print(e)

    @staticmethod
    def read_data():
        FileReader.file_reader(ViewFileLocation().input_location())

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
        SetUpDiagram.set_over_string(SetUpDiagram(), output)

    @staticmethod
    def pass_validate_data(output):
        return ValidateData.validate_test_loader(output)

