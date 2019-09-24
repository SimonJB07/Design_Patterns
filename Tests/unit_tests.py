import unittest

from Model.concrete_python import BuilderDiagramPython
from Model.format_data import FormatData
from View.view_file_location import ViewFileLocation


class TestSetUp(unittest.TestCase):
    """unit test that cover some part of the program

    """

    def test_check_relationship(self):
        print('Test 1')
        result = BuilderDiagramPython.set_relationship(BuilderDiagramPython(), 'DiagramModel--TestModel', None)
        self.assertEqual(result, 'test_model: TestModel')

    def test_check_string(self):
        print('Test 2')
        result = FormatData.clear_up_data('String')
        self.assertEqual(result, 'str ')

    def test_reverse_word(self):
        print('Test 3')
        result = FormatData.reverse_words('DiagramModel Good')
        self.assertEqual(result, 'Good DiagramModel')

    def test_set_attribute(self):
        print('Test 4')
        result = BuilderDiagramPython.set_attributes('int count_students:')
        self.assertEqual(result, 'count_students: int')

    def test_set_methods(self):
        print('Test 5')
        result = BuilderDiagramPython.set_methods('void get_name( String name )')
        self.assertEqual(result, ' get_name(  name )')

    def test_set_method_two(self):
        print('Test 6')
        result = BuilderDiagramPython.set_methods('void set_number_student()')
        self.assertEqual(result, ' set_number_student()')

    def test_set_class(self):
        print('Test 7')
        result = BuilderDiagramPython.set_class('classDiagramModel{')
        self.assertEqual(result, 'DiagramModel')

    def test_set_attribute_clean_up(self):
        print('Test 8')
        result = BuilderDiagramPython.attribute_clean("Stringdata_name:")
        self.assertEqual(result, "data_name: str")

    def test_location_input(self):
        print('Test 9')
        result = ViewFileLocation.input_location()
        self.assertEqual(result, '../Data/ClassDiagram.txt')

    def test_location_input_error(self):
        print('Test 9')
        self.failureException(ViewFileLocation.input_location())
        self.setUp()
