from Controller.main_error_checker import ErrorChecker
from Model.replace_value import Replace

import re


class FormatData:

    @staticmethod
    def clear_up_data(data):
        """this converts to a class diagram str
        """
        ErrorChecker.error_type(str, data, "SETUP CLEAR UP DATA: data type is not corrected  ")
        try:
            clean_data = data.replace('String', Replace.STRING.value) \
                .replace('int', Replace.INT.value) \
                .replace('Float', Replace.FLOAT.value) \
                .replace('Boolean', Replace.BOOLEAN.value) \
                .replace('List', Replace.LIST.value) \
                .replace('Tuple', Replace.TUPLE.value) \
                .replace('Dict', Replace.DICT.value)
            return clean_data
        except Exception as e:
            print("VALUE ERROR: ")
            print(e)

    @staticmethod
    def format_relationship(data):
        for word in data.split():
            str = data.replace(" ", "").replace(word, "")
            if ':' not in word:
                word = re.findall('[A-Z][^A-Z]*', word)
                add_line = word[0] + "_" + word[1]
                lower_case = add_line.lower()
                string_all = lower_case + ': ' + str.replace("_", '')
                return string_all

    @staticmethod
    def reverse_words(word):
        """this reverse words in a string
        """
        ErrorChecker.error_type(str, word, "SETUP REVERSE WORD: data type is not corrected ")
        return ' '.join(reversed(word.split()))


