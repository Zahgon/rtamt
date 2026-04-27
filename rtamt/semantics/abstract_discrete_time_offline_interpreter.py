from rtamt.syntax.ast.visitor.abstract_ast_visitor import AbstractAstVisitor
from rtamt.semantics.abstract_offline_interpreter import AbstractOfflineInterpreter
from rtamt.semantics.discrete_time_interpreter import DiscreteTimeInterpreter
from rtamt.exception.exception import RTAMTException

class AbstractDiscreteTimeOfflineInterpreter(AbstractOfflineInterpreter, DiscreteTimeInterpreter):

    def __init__(self):
        pass

    def evaluate(self, dataset):
        pass

    def set_variable_to_ast_from_dataset(self, dataset):
        pass

def discrete_time_offline_interpreter_factory(AstVisitor):
    pass