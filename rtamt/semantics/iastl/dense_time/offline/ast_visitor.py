from rtamt.semantics.enumerations.comp_oper import StlComparisonOperator
from rtamt.semantics.stl.dense_time.offline.ast_visitor import StlDenseTimeOfflineAstVisitor, subtraction_operation

class IAStlDenseTimeOfflineAstVisitor(StlDenseTimeOfflineAstVisitor):

    def visitPredicate(self, node, *args, **kwargs):
        pass

class IAStlOutputRobustnessDenseTimeOfflineAstVisitor(IAStlDenseTimeOfflineAstVisitor):

    def visitPredicate(self, node, *args, **kwargs):
        pass

class IAStlInputRobustnessDenseTimeOfflineAstVisitor(IAStlDenseTimeOfflineAstVisitor):

    def visitPredicate(self, node, *args, **kwargs):
        pass

class IAStlInputVacuityDenseTimeOfflineAstVisitor(IAStlDenseTimeOfflineAstVisitor):

    def visitPredicate(self, node, *args, **kwargs):
        pass

class IAStlOutputVacuityDenseTimeOfflineAstVisitor(IAStlDenseTimeOfflineAstVisitor):

    def visitPredicate(self, node, *args, **kwargs):
        pass