from Model.director import Director
from Model.concrete_python import BuilderDiagramPython


# Facade Pattern
class Facade:

    @staticmethod
    def model_facade(data_in, data_out):
        diagram = BuilderDiagramPython()
        Director().set_builder(diagram)
        Director().construct(data_in)
        return diagram.specification(data_out)

