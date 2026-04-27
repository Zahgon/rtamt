from rtamt.syntax.ast.visitor.abstract_ast_visitor import AbstractAstVisitor
from rtamt.semantics.abstract_offline_interpreter import AbstractOfflineInterpreter
from rtamt.semantics.dense_time_interpreter import DenseTimeInterpreter
from rtamt.exception.exception import RTAMTException

class AbstractDenseTimeOfflineInterpreter(AbstractOfflineInterpreter, DenseTimeInterpreter):

    def __init__(self):
        pass

    def evaluate(self, dataset):
        pass

def dense_time_offline_interpreter_factory(AstVisitor):
    pass