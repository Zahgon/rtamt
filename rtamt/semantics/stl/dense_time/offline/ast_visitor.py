import math
import operator
from collections import deque
import rtamt.semantics.stl.dense_time.offline.intersection as intersect
from rtamt.syntax.ast.visitor.stl.ast_visitor import StlAstVisitor
from rtamt.semantics.enumerations.comp_oper import StlComparisonOperator
from rtamt.exception.exception import RTAMTException

def subtraction_operation(sample_left, sample_right):
    pass

def and_operation(sample_left, sample_right):
    pass

def since_operation(sample_left, sample_right):
    pass

def once_timed_operation(sample, begin, end):
    pass

def historically_timed_operation(sample, begin, end):
    pass

def since_timed_operation(sample_left, sample_right, begin, end):
    pass

def always_timed_operation(sample, begin, end):
    pass

def eventually_timed_operation(sample, begin, end):
    pass

def until_operation(sample_left, sample_right):
    pass

def until_timed_operation(sample_left, sample_right, begin, end):
    pass

class StlDenseTimeOfflineAstVisitor(StlAstVisitor):

    def visit(self, node, *args, **kwargs):
        pass

    def visitPredicate(self, node, *args, **kwargs):
        pass

    def visitVariable(self, node, *args, **kwargs):
        pass

    def visitAbs(self, node, *args, **kwargs):
        pass

    def visitSqrt(self, node, *args, **kwargs):
        pass

    def visitExp(self, node, *args, **kwargs):
        pass

    def visitPow(self, node, *args, **kwargs):
        pass

    def visitLog(self, node, *args, **kwargs):
        pass

    def visitLn(self, node, *args, **kwargs):
        pass

    def visitAddition(self, node, *args, **kwargs):
        pass

    def visitSubtraction(self, node, *args, **kwargs):
        pass

    def visitMultiplication(self, node, *args, **kwargs):
        pass

    def visitDivision(self, node, *args, **kwargs):
        pass

    def visitNot(self, node, *args, **kwargs):
        pass

    def visitNegate(self, node, *args, **kwargs):
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

    def visitHistorically(self, node, *args, **kwargs):
        pass

    def visitSince(self, node, *args, **kwargs):
        pass

    def visitRise(self, node, *args, **kwargs):
        pass

    def visitFall(self, node, *args, **kwargs):
        pass

    def visitConstant(self, node, *args, **kwargs):
        pass

    def visitPrevious(self, node, *args, **kwargs):
        pass

    def visitNext(self, node, *args, **kwargs):
        pass

    def visitTimedPrecedes(self, node, *args, **kwargs):
        pass

    def visitTimedOnce(self, node, *args, **kwargs):
        pass

    def visitTimedHistorically(self, node, *args, **kwargs):
        pass

    def visitTimedSince(self, node, *args, **kwargs):
        pass

    def visitTimedAlways(self, node, *args, **kwargs):
        pass

    def visitTimedEventually(self, node, *args, **kwargs):
        pass

    def visitTimedUntil(self, node, *args, **kwargs):
        pass