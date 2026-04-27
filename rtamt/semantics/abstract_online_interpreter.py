from abc import abstractmethod
from rtamt.syntax.node.ltl.variable import Variable
from rtamt.syntax.node.ltl.constant import Constant
from rtamt.syntax.ast.visitor.abstract_ast_visitor import AbstractAstVisitor
from rtamt.semantics.abstract_interpreter import AbstractInterpreter

class AbstractOnlineInterpreter(AbstractInterpreter):

    def __init__(self):
        pass

    def reset(self):
        pass

    def set_ast(self, ast):
        pass

    @abstractmethod
    def update(self, *args, **kargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

class AbstractOnlineResetVisitor(AbstractAstVisitor):

    def visitBinary(self, node, online_operator_dict):
        pass

    def visitUnary(self, node, online_operator_dict):
        pass

    def visitLeaf(self, node, online_operator_dict):
        pass

class AbstractOnlineUpdateVisitor(AbstractAstVisitor):

    def __init__(self):
        pass

    def visitSpec(self, node, online_operator_dict, var_object_dict):
        pass

    def visitBinary(self, node, online_operator_dict, var_object_dict):
        pass

    def visitUnary(self, node, online_operator_dict, var_object_dict):
        pass

    def visitLeaf(self, node, online_operator_dict, var_object_dict):
        pass