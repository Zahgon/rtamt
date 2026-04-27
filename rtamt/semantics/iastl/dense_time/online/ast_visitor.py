from rtamt.semantics.stl.dense_time.online.ast_visitor import StlDenseTimeOnlineAstVisitor
from rtamt.semantics.iastl.dense_time.online.predicate_operation import PredicateOperation
from rtamt.semantics.enumerations.options import Semantics

class IAStlOutputRobustnessDenseTimeOnlineAstVisitor(StlDenseTimeOnlineAstVisitor):

    def visitPredicate(self, node, *args, **kwargs):
        pass

class IAStlInputVacuityDenseTimeOnlineAstVisitor(StlDenseTimeOnlineAstVisitor):

    def visitPredicate(self, node, *args, **kwargs):
        pass

class IAStlOutputVacuityDenseTimeOnlineAstVisitor(StlDenseTimeOnlineAstVisitor):

    def visitPredicate(self, node, *args, **kwargs):
        pass

class IAStlInputRobustnessDenseTimeOnlineAstVisitor(StlDenseTimeOnlineAstVisitor):

    def visitPredicate(self, node, *args, **kwargs):
        pass