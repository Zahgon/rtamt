import operator
from rtamt.syntax.ast.visitor.abstract_ast_visitor import AbstractAstVisitor
from rtamt.semantics.abstract_online_interpreter import AbstractOnlineInterpreter, AbstractOnlineUpdateVisitor, AbstractOnlineResetVisitor
from rtamt.semantics.discrete_time_interpreter import DiscreteTimeInterpreter
from rtamt.exception.exception import RTAMTException

class AbstractDiscreteTimeOnlineInterpreter(AbstractOnlineInterpreter, DiscreteTimeInterpreter):

    def __init__(self):
        pass

    def update(self, timestamp, dataset):
        pass

    def reset(self):
        pass

    def set_variable_to_ast_from_dataset(self, dataset):
        pass

    @property
    def update_counter(self):
        pass

    @update_counter.setter
    def update_counter(self, update_counter):
        pass

class DiscreteTimeOnlineUpdateVisitor(AbstractOnlineUpdateVisitor):

    def visitVariable(self, node, online_operator_dict, var_object_dict):
        pass

    def visitConstant(self, node, online_operator_dict, var_object_dict):
        pass

def discrete_time_online_interpreter_factory(AstVisitor):
    pass