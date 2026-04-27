from rtamt.syntax.ast.visitor.stl.ast_visitor import StlAstVisitor
from rtamt.explanation.ltl.discrete_time.explainer import LTLExplainer
from rtamt.explanation.stl.discrete_time.explanations import *
from rtamt.exception.exception import RTAMTException

class STLExplainer(LTLExplainer, StlAstVisitor):

    def __init__(self):
        pass

    def visit(self, element, args):
        pass

    def explain(self, spec):
        pass

    def visitTimedEventually(self, element, args):
        pass

    def visitTimedAlways(self, element, args):
        pass

    def visitTimedUntil(self, element, args):
        pass

    def visitTimedOnce(self, element, args):
        pass

    def visitTimedHistorically(self, element, args):
        pass

    def visitTimedSince(self, element, args):
        pass

    def visitTimedPrecedes(self, element, args):
        pass

    def visitDefault(self, element):
        pass