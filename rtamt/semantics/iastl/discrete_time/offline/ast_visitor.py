from rtamt.semantics.stl.discrete_time.offline.ast_visitor import StlDiscreteTimeOfflineAstVisitor
from rtamt.semantics.enumerations.comp_op import StlComparisonOperator

class IAStlDiscreteTimeOfflineAstVisitor(StlDiscreteTimeOfflineAstVisitor):

    def visitPredicate(self, node, *args, **kwargs):
        pass

class IAStlOutputRobustnessDiscreteTimeOfflineAstVisitor(IAStlDiscreteTimeOfflineAstVisitor):

    def visitPredicate(self, node, *args, **kwargs):
        pass

class IAStlInputRobustnessDiscreteTimeOfflineAstVisitor(IAStlDiscreteTimeOfflineAstVisitor):

    def visitPredicate(self, node, *args, **kwargs):
        pass

class IAStlInputVacuityDiscreteTimeOfflineAstVisitor(IAStlDiscreteTimeOfflineAstVisitor):

    def visitPredicate(self, node, *args, **kwargs):
        pass

class IAStlOutputVacuityDiscreteTimeOfflineAstVisitor(IAStlDiscreteTimeOfflineAstVisitor):

    def visitPredicate(self, node, *args, **kwargs):
        pass