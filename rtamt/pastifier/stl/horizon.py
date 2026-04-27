from rtamt.syntax.ast.visitor.stl.ast_visitor import StlAstVisitor
from rtamt.pastifier.ltl.horizon import LtlHorizon
from rtamt.exception.exception import RTAMTException

class StlHorizon(LtlHorizon, StlAstVisitor):

    def __init__(self):
        pass

    def visit(self, node, *args, **kwargs):
        pass

    def visitTimedEventually(self, node, *args, **kwargs):
        pass

    def visitTimedAlways(self, node, *args, **kwargs):
        pass

    def visitTimedUntil(self, node, *args, **kwargs):
        pass

    def visitTimedOnce(self, node, *args, **kwargs):
        pass

    def visitTimedHistorically(self, node, *args, **kwargs):
        pass

    def visitTimedSince(self, node, *args, **kwargs):
        pass

    def visitTimedPrecedes(self, node, *args, **kwargs):
        pass

    def visitDefault(self, node):
        pass