from Controller.main_error_checker import ErrorChecker
from Model.format_data import FormatData


class Method:
    def __init__(self):
        self.__met = None

    @property
    def method(self):
        return self.__met

    @method.setter
    def method(self, method):
        self.__met = method

    @staticmethod
    def error_check_method(method_name):
        """this removes the String from the method attributes
        """
        ErrorChecker.error_type(str, method_name, "SETUP METHOD NAME: data type is not corrected")
        try:
            return Method.method_clean(method_name)
        except Exception as e:
            print("METHOD NAME ERROR: ")
            print(e)

    @staticmethod
    def method_clean(method_data):
        temp_met = method_data.replace('void', '')
        return FormatData.clear_up_data(temp_met).replace('str ', '')

    @staticmethod
    def methods_print(value, output):
        stat = "staticmethod"
        for methods in value:
            print(f"    @{stat}", file=output)
            print(f"    def {methods}:", file=output)
            print(f"        pass\n", file=output)
