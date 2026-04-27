from rtamt.syntax.ast.visitor.stl.ast_visitor import StlAstVisitor
from rtamt.semantics.interval.interval import Interval
from rtamt.pastifier.ltl.pastifier import LtlPastifier
from rtamt.syntax.node.stl.timed_precedes import TimedPrecedes
from rtamt.syntax.node.stl.timed_historically import TimedHistorically
from rtamt.syntax.node.stl.timed_once import TimedOnce
from rtamt.syntax.node.stl.timed_since import TimedSince
from rtamt.syntax.node.ltl.predicate import Predicate
from rtamt.syntax.node.ltl.variable import Variable
from rtamt.syntax.node.ltl.neg import Neg
from rtamt.syntax.node.ltl.conjunction import Conjunction
from rtamt.syntax.node.ltl.disjunction import Disjunction
from rtamt.syntax.node.ltl.implies import Implies
from rtamt.syntax.node.ltl.iff import Iff
from rtamt.syntax.node.ltl.strong_previous import StrongPrevious
from rtamt.syntax.node.ltl.xor import Xor
from rtamt.syntax.node.ltl.once import Once
from rtamt.syntax.node.ltl.historically import Historically
from rtamt.syntax.node.ltl.since import Since
from rtamt.syntax.node.arithmetic.addition import Addition
from rtamt.syntax.node.arithmetic.subtraction import Subtraction
from rtamt.syntax.node.arithmetic.multiplication import Multiplication
from rtamt.syntax.node.arithmetic.division import Division
from rtamt.syntax.node.arithmetic.abs import Abs
from rtamt.syntax.node.arithmetic.sqrt import Sqrt
from rtamt.syntax.node.arithmetic.exp import Exp
from rtamt.syntax.node.arithmetic.pow import Pow
from rtamt.syntax.node.ltl.fall import Fall
from rtamt.syntax.node.ltl.rise import Rise
from rtamt.syntax.node.ltl.constant import Constant
from rtamt.syntax.node.ltl.previous import Previous
from rtamt.exception.exception import RTAMTException
from rtamt.pastifier.stl.horizon import StlHorizon

class StlPastifier(LtlPastifier, StlAstVisitor):

    def __init__(self):
        pass

    def pastify(self, ast):
        pass

    def visit(self, node, *args, **kwargs):
        pass

    def visitVariable(self, node, *args, **kwargs):
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

    def visitConstant(self, node, *args, **kwargs):
        pass

    def visitPredicate(self, node, *args, **kwargs):
        pass

    def visitVariable(self, node, *args, **kwargs):
        pass

    def visitAddition(self, node, *args, **kwargs):
        pass

    def visitMultiplication(self, node, *args, **kwargs):
        pass

    def visitSubtraction(self, node, *args, **kwargs):
        pass

    def visitDivision(self, node, *args, **kwargs):
        pass

    def visitAbs(self, node, *args, **kwargs):
        pass

    def visitSqrt(self, node, *args, **kwargs):
        pass

    def visitExp(self, node, *args, **kwargs):
        pass

    def visitPow(self, node, *args, **kwargs):
        pass

    def visitRise(self, node, *args, **kwargs):
        pass

    def visitFall(self, node, *args, **kwargs):
        pass

    def visitNot(self, node, *args, **kwargs):
        pass

    def visitAnd(self, node, *args, **kwargs):
        pass

    def visitOr(self, node, *args, **kwargs):
        pass

    def visitImplies(self, node, *args, **kwargs):
        pass

    def visitIff(self, node, *args, **kwargs):
        pass

    def visitXor(self, node, *args, **kwargs):
        pass

    def visitEventually(self, node, *args, **kwargs):
        pass

    def visitAlways(self, node, *args, **kwargs):
        pass

    def visitUntil(self, node, *args, **kwargs):
        pass

    def visitOnce(self, node, *args, **kwargs):
        pass

    def visitPrevious(self, node, *args, **kwargs):
        pass

    def visitStrongPrevious(self, node, *args, **kwargs):
        pass

    def visitNext(self, node, *args, **kwargs):
        pass

    def visitStrongNext(self, node, *args, **kwargs):
        pass

    def visitHistorically(self, node, *args, **kwargs):
        pass

    def visitSince(self, node, *args, **kwargs):
        pass

    def visitDefault(self, node):
        pass