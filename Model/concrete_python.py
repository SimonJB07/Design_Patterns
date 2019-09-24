from Model.error_checker import ErrorChecker
from Model.Components.attributes import Attributes
from Model.Components.class_names import ClassName
from Model.Components.methods import Method
from Model.abstract_builder import Builder
from Model.Components.relationship import Relationship
from Model.format_data import FormatData


# Concrete Builder
class BuilderDiagramPython(Builder):

    def check_class(self, key, value, no):
        if no <= 0:
            self.data.dict['diagram'][key].append(value)
        else:
            self.data.dict['diagram' + '_1'][key].append(value)

    def set_class(self, clsname, counter):
        cla_key = 'Cla'
        class_name = ClassName()
        ErrorChecker.error_type(str, clsname, "ERROR: SETUP CLASS NAME: data type is not corrected")
        try:
            python_class_name = clsname.replace("class", '').replace('{', '').replace('\n', '')
            class_name.name = python_class_name.replace(" ", "")
            BuilderDiagramPython.check_class(self, cla_key, class_name.name, counter)
        except Exception as e:
            print("PYTHON CLASS NAME ERROR: ")
            print(e)

    def set_relationship(self, relation, counter):
        rel_key = "Rel"
        relationship = Relationship()
        ErrorChecker.error_type(str, relation, "SETUP RELATIONSHIP: data type is not corrected")
        try:
            rel_value = relation.replace("-- ", "").replace('\n', '')
            relationship.rel = FormatData.format_relationship(rel_value)
            BuilderDiagramPython.check_class(self, rel_key, relationship.rel, counter)
        except Exception as e:
            print("RELATIONSHIP VALUE ERROR: ")
            print(e)

    def set_attributes(self, att, counter):
        att_key = "Att"
        attribute = Attributes()
        ErrorChecker.error_type(str, att, "ATTRIBUTE NAME: datatype not corrected ")
        try:
            attribute.att = self.attribute_clean(att).replace('\n', '')
            BuilderDiagramPython.check_class(self, att_key, attribute.att, counter)
        except Exception as e:
            print("ATTRIBUTE NAME ERROR: ")
            print(e)

    @staticmethod
    def attribute_clean(att_data):
        temp_att = FormatData.clear_up_data(att_data).replace(":", "")
        format_attribute = FormatData.reverse_words(temp_att).replace(" ", ": ")
        return format_attribute

    def set_methods(self, met, counter):
        met_key = "Met"
        method = Method()
        ErrorChecker.error_type(str, met, "SETUP METHOD NAME: data type is not corrected")
        try:
            method.method = self.method_clean(met).replace('\n', '')
            BuilderDiagramPython.check_class(self, met_key, method.method, counter)
        except Exception as e:
            print("METHOD NAME ERROR: ")
            print(e)

    @staticmethod
    def method_clean(method_data):
        temp_met = method_data.replace('void', '').replace(":", "")
        return FormatData.clear_up_data(temp_met).replace('str ', '').replace(" ", "")

    def specification(self, output):
        with open(output, "w") as f:
            BuilderDiagramPython.specification_total(self, "diagram", f)
            print("", file=f)
            BuilderDiagramPython.specification_total(self, "diagram_1", f)

    def specification_total(self, diagram, f):
            for item in self.data.dict[diagram].items():
                self.specification_class(item, f)
                self.specification_relationship(item, f)
                self.specification_attributes(item, f)
                self.specification_methods(item, f)

    @staticmethod
    def specification_class(item, f):
        if item[0] == 'Cla':
            for c in item[1]:
                print(f'class {c}(object):', file=f)
            print(f"    def __init__(self):", file=f)

    @staticmethod
    def specification_relationship(item, f):
        if item[0] == 'Rel':
            for r in item[1]:
                if not item[1]:
                    pass
                else:
                    print(f"        self.{r}", file=f)

    @staticmethod
    def specification_attributes(item, f):
        if item[0] == 'Att':
            for a in item[1]:
                print(f"        self.{a}", file=f)
            print(f"", file=f)

    @staticmethod
    def specification_methods(item, f):
        if item[0] == 'Met':
            for m in item[1]:
                print(f"    @staticmethod", file=f)
                print(f"    def {m}:", file=f)
                print(f"        pass\n", file=f)
