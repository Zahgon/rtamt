import operator
from rtamt.syntax.node.ltl.variable import Variable
from rtamt.syntax.node.ltl.constant import Constant
from rtamt.syntax.ast.visitor.abstract_ast_visitor import AbstractAstVisitor
from rtamt.semantics.abstract_online_interpreter import AbstractOnlineInterpreter, AbstractOnlineUpdateVisitor
from rtamt.semantics.dense_time_interpreter import DenseTimeInterpreter
from rtamt.exception.exception import RTAMTException

class AbstractDenseTimeOnlineInterpreter(AbstractOnlineInterpreter, DenseTimeInterpreter):

    def __init__(self):
        pass

    def update(self, dataset):
        pass

    def update_final(self, dataset):
        pass

    def set_variable_to_ast_from_dataset(self, dataset):
        pass

class DenseTimeOnlineUpdateVisitor(AbstractOnlineUpdateVisitor):

    def visitVariable(self, node, online_operator_dict, var_object_dict):
        pass

    def visitConstant(self, node, online_operator_dict, var_object_dict):
        pass

class DenseTimeOnlineUpdateFinalVisitor(AbstractAstVisitor):

    def visitSpec(self, node, online_operator_dict, var_object_dict):
        pass

    def visitBinary(self, node, online_operator_dict, var_object_dict):
        pass

    def visitUnary(self, node, online_operator_dict, var_object_dict):
        pass

    def visitLeaf(self, node, online_operator_dict, var_object_dict):
        pass

    def visitVariable(self, node, online_operator_dict, var_object_dict):
        pass

    def visitConstant(self, node, online_operator_dict, var_object_dict):
        pass

def dense_time_online_interpreter_factory(AstVisitor):
    pass