class DiagramModel(object):
    def __init__(self):
        self.diagram_model: TestModel
        self.data_name: str
        self.id_number: list
        self.count_students: int

    @staticmethod
    def get_id():
        pass

    @staticmethod
    def get_name(name):
        pass

    @staticmethod
    def set_number_student():
        pass


class TestModel(object):
    def __init__(self):
        self.data_students_name: str
        self.last_name_student: list
        self.count_student: dict

    @staticmethod
    def get_last_name():
        pass

    @staticmethod
    def get_count_students(name):
        pass

