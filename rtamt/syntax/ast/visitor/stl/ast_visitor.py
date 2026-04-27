from rtamt.exception.exception import RTAMTException
from rtamt.syntax.node.stl.timed_precedes import TimedPrecedes
from rtamt.syntax.ast.visitor.ltl.ast_visitor import LtlAstVisitor
from rtamt.syntax.node.stl.timed_since import TimedSince
from rtamt.syntax.node.stl.timed_once import TimedOnce
from rtamt.syntax.node.stl.timed_historically import TimedHistorically
from rtamt.syntax.node.stl.timed_eventually import TimedEventually
from rtamt.syntax.node.stl.timed_always import TimedAlways
from rtamt.syntax.node.stl.timed_until import TimedUntil

class StlAstVisitor(LtlAstVisitor):

    def visit(self, node, *args, **kwargs):
        pass

    def visitTimedPrecedes(self, node, *args, **kwargs):
        pass

    def visitTimedOnce(self, node, *args, **kwargs):
        pass

    def visitTimedHistorically(self, node, *args, **kwargs):
        pass

    def visitTimedSince(self, node, *args, **kwargs):
        pass

    def visitTimedPrecedes(self, node, *args, **kwargs):
        pass

    def visitTimedAlways(self, node, *args, **kwargs):
        pass

    def visitTimedEventually(self, node, *args, **kwargs):
        pass

    def visitTimedUntil(self, node, *args, **kwargs):
        pass

    def raise_exception(self, text):
        pass