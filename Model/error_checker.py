class ErrorChecker:

    @staticmethod
    def error_type(type_class, value_to_check, error_message):
        if type_class == type(value_to_check):
            pass
        else:
            print(error_message)
            print(type(value_to_check))

    @staticmethod
    def error_name(file_path, value, error_message):
        if file_path == value:
            pass
        else:
            print(error_message)
