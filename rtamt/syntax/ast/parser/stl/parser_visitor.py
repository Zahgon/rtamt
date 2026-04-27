from decimal import Decimal
from fractions import Fraction
from rtamt.antlr.parser.stl.StlParserVisitor import StlParserVisitor
from rtamt.syntax.ast.parser.ltl.parser_visitor import LtlAstParserVisitor
from rtamt.semantics.interval.interval import Interval
from rtamt.syntax.node.ltl.disjunction import Disjunction
from rtamt.syntax.node.ltl.always import Always
from rtamt.syntax.node.ltl.eventually import Eventually
from rtamt.syntax.node.ltl.once import Once
from rtamt.syntax.node.ltl.historically import Historically
from rtamt.syntax.node.ltl.since import Since
from rtamt.syntax.node.ltl.until import Until
from rtamt.syntax.node.stl.timed_always import TimedAlways
from rtamt.syntax.node.stl.timed_eventually import TimedEventually
from rtamt.syntax.node.stl.timed_historically import TimedHistorically
from rtamt.syntax.node.stl.timed_once import TimedOnce
from rtamt.syntax.node.stl.timed_since import TimedSince
from rtamt.syntax.node.stl.timed_until import TimedUntil
from rtamt.exception.exception import RTAMTException

class StlAstParserVisitor(LtlAstParserVisitor, StlParserVisitor):

    def __init__(self):
        pass

    def visitExprAlways(self, ctx):
        pass

    def visitExprEv(self, ctx):
        pass

    def visitExpreOnce(self, ctx):
        pass

    def visitExprHist(self, ctx):
        pass

    def visitExprSince(self, ctx):
        pass

    def visitExprUntil(self, ctx):
        pass

    def visitExprUnless(self, ctx):
        pass

    def visitConstantTimeLiteral(self, ctx):
        pass

    def visitIntervalTimeLiteral(self, ctx):
        pass

    def visitInterval(self, ctx):
        pass

    def get_sampling_period(self):
        pass

    @property
    def unit(self):
        pass

    @unit.setter
    def unit(self, unit):
        pass