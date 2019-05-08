from View.file_reader import FileReader
from View.file_writer import FileWriter
from View.view_file_location import ViewFileLocation
from Tests.main_test_file import MainTests
from Model.set_up_diagram import SetUp
from Model.class_name import ClassName
from Model.relationships import Relationships
from Model.attributes import Attribute
from Model.method import Method
from Model.validate_data import ValidateData


class MainController:

    @staticmethod
    def main():
        try:
            MainController.read_data()
            MainController.get_doctest()
            MainController.get_unittest()
        except Exception as e:
            print("MAIN ERROR: main.py error")
            print(e)


    @staticmethod
    def read_data():
        FileReader.file_reader(ViewFileLocation().input_location())

    @staticmethod
    def write_name(data):
        return FileWriter.file_writer(data)

    @staticmethod
    def pickle_write_call():
        import pickle
        with open('data.pickle', 'wb') as f:
            pickle.dump(SetUp().final_uml_list, f)
        with open('data.pickle', 'rb') as f:
            data = pickle.load(f)
            print(data)

    @staticmethod
    def get_unittest():
        return MainTests.unit_test()

    @staticmethod
    def get_doctest():
        return MainTests.doc_tests()

    @staticmethod
    def class_print(value, output_file):
        ClassName.class_print(value, output_file)

    @staticmethod
    def relationship_print(value, output):
        Relationships.relationship_print(value, output)

    @staticmethod
    def attribute_print(value, output):
        Attribute.attribute_print(value, output)

    @staticmethod
    def methods_print(value, output):
        Method.methods_print(value, output)

    @staticmethod
    def pass_set_up(output):
        SetUp.set_over_string(SetUp(), output)

    @staticmethod
    def pass_validate_data(output):
        return ValidateData.validate_test_loader(output)

