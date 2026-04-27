from rtamt.syntax.ast.visitor.ltl.ast_visitor import LtlAstVisitor
from rtamt.exception.exception import RTAMTException
from rtamt.explanation.ltl.discrete_time.explanations import *

class LTLExplainer(LtlAstVisitor):

    def __init__(self):
        pass

    def explain(self, spec):
        pass

    def visitConstant(self, element, args):
        pass

    def visitPredicate(self, element, args):
        pass

    def visitVariable(self, element, args):
        pass

    def visitAddition(self, element, args):
        pass

    def visitMultiplication(self, element, args):
        pass

    def visitSubtraction(self, element, args):
        pass

    def visitDivision(self, element, args):
        pass

    def visitAbs(self, element, args):
        pass

    def visitSqrt(self, element, args):
        pass

    def visitExp(self, element, args):
        pass

    def visitPow(self, element, args):
        pass

    def visitRise(self, element, args):
        pass

    def visitFall(self, element, args):
        pass

    def visitNot(self, element, args):
        pass

    def visitAnd(self, element, args):
        pass

    def visitOr(self, element, args):
        pass

    def visitImplies(self, element, args):
        pass

    def visitIff(self, element, args):
        pass

    def visitXor(self, element, args):
        pass

    def visitEventually(self, element, args):
        pass

    def visitAlways(self, element, args):
        pass

    def visitUntil(self, element, args):
        pass

    def visitOnce(self, element, args):
        pass

    def visitPrevious(self, element, args):
        pass

    def visitStrongPrevious(self, element, args):
        pass

    def visitNext(self, element, args):
        pass

    def visitStrongNext(self, element, args):
        pass

    def visitHistorically(self, element, args):
        pass

    def visitSince(self, element, args):
        pass

    def visitDefault(self, element):
        pass