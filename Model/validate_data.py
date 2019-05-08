from Controller.main_error_checker import ErrorChecker


class ValidateData:
    """This just handles the data
    and checks to see if it is all there
    and load correctly

     """

    @classmethod
    def validate_test_loader(cls, test_data):
        """if the data load correctly
        """
        cls.start = False
        cls.class_counter = 0
        cls.relationship_counter = 0
        cls.methods_counter = 0
        cls.attribute_counter = 0
        cls.class_braced = 0
        cls.end = False

        ErrorChecker.error_type(list, test_data, "VALIDATE TEST LOADER: data type is not corrected")
        try:
            for check_line in test_data:
                if '@startuml' == check_line:
                    cls.start = True
                elif 'class' in check_line:
                    cls.class_counter += 1
                elif '--' in check_line:
                    cls.relationship_counter += 1
                elif ':' in check_line:
                    cls.attribute_counter += 1
                elif '(' in check_line:
                    cls.methods_counter += 1
                elif '}' == check_line:
                    cls.class_braced += 1
                elif '@enduml' == check_line:
                    cls.end = True
        except Exception as e:
            print("ERROR: VALIDATE TEST LOADER CONTENT")
            print(e)
        finally:
            return cls.start and cls.end and cls.class_counter == cls.class_braced and cls.relationship_counter


