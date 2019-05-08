from cmd import Cmd
from Controller.main_controller import MainController


class TestData(Cmd):
    """
    single command processor checking areas of the programme
    """

    def __init__(self):
        Cmd.__init__(self)
        self.prompt = ">>> "
        self.my_data = MainController.get_file_data()
        self.my_unit_test = MainController.get_unit_test()

    def do_unit_test(self, line):
        """
        Syntax: enter data [the_data]
        Data this can load data to txt file
        :param data: a string representing a class name
        :return: None
        """
        print(self.my_unit_test)

    def do_relationship(self, relationship):
        """
        Syntax: relationship [the_name]
        Greet the relationship between class
        :param the_data: a string representing relationships
        :return: None
        """
        relationship = self.class_relationship
        if relationship:
            print(relationship)
        else:
            print(self.my_data)

    def do_class_name(self):
        """
        Syntax: class_name [ class names ]
        :param: a string representing a class names
        :return: None
        """
        print(self.my_data)

    def do_run_main(self, line):
        # MainController.write_name()
        MainController.read_data()
        # MainController.get_file_data()

    @staticmethod
    def do_quit():
        """
        Syntax: quiting
        close programme
        :param None
        :return: None
        """
        print("Quitting, data entry")
        return True

    @staticmethod
    def help_quit():
        print("\n".join(['Quit from my CMD', ':return: True']))

    do_q = do_quit
    """
    Syntax: quiting 
    close programme
    :param None
    :return: None
    """
    do_rel = do_relationship
    """
    Syntax: relationship [the_name]
    Greet the relationship between class
    :param the_data: a string representing relationships
    :return: None
    """
    do_cls = do_class_name
    """
     Syntax: class_name [ class names ]
     :param: a string representing a class names
     :return: None
     """


if __name__ == '__main__':
    test = TestData()
    test.cmdloop()
