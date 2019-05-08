from Controller.main_error_checker import ErrorChecker
from Model.format_data import FormatData


class Methods:

    @staticmethod
    def set_up_method_name(method_name):
        """this removes the String from the method attributes
        """
        ErrorChecker.error_type(str, method_name, "SETUP METHOD NAME: data type is not corrected")
        try:
            temp_met = method_name.replace('void', '')
            format_method = FormatData.clear_up_data(temp_met).replace('str ', '')
            return format_method
        except Exception as e:
            print("METHOD NAME ERROR: ")
            print(e)
