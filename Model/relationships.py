from Controller.main_error_checker import ErrorChecker
from Model.format_data import FormatData


class Relationships:

    @staticmethod
    def error_check_relationship(relationship_value):
        """this method converts diagram to workable class
        """
        ErrorChecker.error_type(str, relationship_value, "SETUP RELATIONSHIP: data type is not corrected")
        try:
            rel_value = relationship_value.replace("--", ": ")
            return FormatData.format_relationship(rel_value)
        except Exception as e:
            print("RELATIONSHIP VALUE ERROR: ")
            print(e)

    @staticmethod
    def relationship_print(value, output):
        s = "self"
        print(f"    def __inti__({s}):", file=output)
        for relationship in value:
            print(f"        {s}.{relationship}", file=output)


