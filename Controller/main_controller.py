from Model.director import Director
from View.view_file_location import ViewFileLocation

# from Tests.main_test_file import MainTests
from Model.validate_data import ValidateData
from Model.builder_diagram_python import BuilderDiagramPython


class MainController:

    @staticmethod
    def main():
        try:
            # MainController.get_doctest()
            # MainController.get_unittest()
            diagram = BuilderDiagramPython()
            dir = Director(diagram)
            dir.file_reader(ViewFileLocation().input_location())
            diagram.specification()
        except Exception as e:
                print("MAIN ERROR: python or director")
                print(e)

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
