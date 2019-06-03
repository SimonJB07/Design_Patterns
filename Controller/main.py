from Controller.main_controller import MainController
from Model.file_reader import FileReader
from Model.builder_python_diagram import BuilderPythonDiagram
from Controller.director import Director

if __name__ == '__main__':
    # MainController.main()

    file_reader = FileReader()
    print(file_reader.file_reader())
    # diagram = BuilderPythonDiagram()
    # dir = Director(diagram)
    # dir.contuctor()
    # diagram.results().specification()

