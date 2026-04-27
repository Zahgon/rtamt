from rtamt.semantics.stl.discrete_time.online.ast_visitor import StlDiscreteTimeOnlineAstVisitor
from rtamt.semantics.iastl.discrete_time.online.predicate_operation import PredicateOperation
from rtamt.semantics.enumerations.options import Semantics

class IAStlDiscreteTimeOnlineAstVisitor(StlDiscreteTimeOnlineAstVisitor):

    def visitPredicate(self, node, *args, **kwargs):
        pass

class IAStlOutputRobustnessDiscreteTimeOnlineAstVisitor(StlDiscreteTimeOnlineAstVisitor):

    def visitPredicate(self, node, *args, **kwargs):
        pass

class IAStlInputVacuityDiscreteTimeOnlineAstVisitor(StlDiscreteTimeOnlineAstVisitor):

    def visitPredicate(self, node, *args, **kwargs):
        pass

class IAStlOutputVacuityDiscreteTimeOnlineAstVisitor(StlDiscreteTimeOnlineAstVisitor):

    def visitPredicate(self, node, *args, **kwargs):
        pass

class IAStlInputRobustnessDiscreteTimeOnlineAstVisitor(StlDiscreteTimeOnlineAstVisitor):

    def visitPredicate(self, node, *args, **kwargs):
        pass