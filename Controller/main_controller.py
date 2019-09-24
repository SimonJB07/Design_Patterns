from View.view_file_location import ViewFileLocation
from Model.facade_diagram_model import Facade


class MainController:

    @staticmethod
    def main():
        try:
            # MainController.get_doctest()
            # MainController.get_unittest()
            Facade.model_facade(ViewFileLocation().input_location(), ViewFileLocation.output_location())
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

