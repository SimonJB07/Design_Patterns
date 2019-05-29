from Controller.main_error_checker import ErrorChecker


class ClassName:
    def __init__(self):
        self.__shape = None

    @property
    def shape(self):
        return self.__shape

    @shape.setter
    def shape(self, shape):
        self.__shape = shape

    @staticmethod
    def set_up_class_name(python_class_name):
        """this returns the class name
        """
        ErrorChecker.error_type(str, python_class_name, "ERROR: SETUP CLASS NAME: data type is not corrected")
        try:
            class_name = python_class_name.replace("class", '').replace('{', '')
            return class_name
        except Exception as e:
            print("PYTHON CLASS NAME ERROR: ")
            print(e)

    @staticmethod
    def class_print(value, output):
        print(f"class {value}:", file=output)
