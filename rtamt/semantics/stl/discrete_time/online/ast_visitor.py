from rtamt.semantics.stl.discrete_time.online.strong_previous_operation import StrongPreviousOperation
from rtamt.semantics.stl.discrete_time.online.variable_operation import VariableOperation
from rtamt.syntax.ast.visitor.stl.ast_visitor import StlAstVisitor
from rtamt.semantics.arithmetic.discrete_time.online.addition_operation import AdditionOperation
from rtamt.semantics.arithmetic.discrete_time.online.multiplication_operation import MultiplicationOperation
from rtamt.semantics.arithmetic.discrete_time.online.subtraction_operation import SubtractionOperation
from rtamt.semantics.arithmetic.discrete_time.online.division_operation import DivisionOperation
from rtamt.semantics.arithmetic.discrete_time.online.abs_operation import AbsOperation
from rtamt.semantics.arithmetic.discrete_time.online.sqrt_operation import SqrtOperation
from rtamt.semantics.arithmetic.discrete_time.online.exp_operation import ExpOperation
from rtamt.semantics.arithmetic.discrete_time.online.pow_operation import PowOperation
from rtamt.semantics.arithmetic.discrete_time.online.negate_operation import NegateOperation
from rtamt.semantics.arithmetic.discrete_time.online.log_operation import LogOperation
from rtamt.semantics.arithmetic.discrete_time.online.ln_operation import LnOperation
from rtamt.semantics.stl.discrete_time.online.predicate_operation import PredicateOperation
from rtamt.semantics.stl.discrete_time.online.and_operation import AndOperation
from rtamt.semantics.stl.discrete_time.online.or_operation import OrOperation
from rtamt.semantics.stl.discrete_time.online.implies_operation import ImpliesOperation
from rtamt.semantics.stl.discrete_time.online.iff_operation import IffOperation
from rtamt.semantics.stl.discrete_time.online.xor_operation import XorOperation
from rtamt.semantics.stl.discrete_time.online.since_operation import SinceOperation
from rtamt.semantics.stl.discrete_time.online.not_operation import NotOperation
from rtamt.semantics.stl.discrete_time.online.rise_operation import RiseOperation
from rtamt.semantics.stl.discrete_time.online.fall_operation import FallOperation
from rtamt.semantics.stl.discrete_time.online.once_operation import OnceOperation
from rtamt.semantics.stl.discrete_time.online.historically_operation import HistoricallyOperation
from rtamt.semantics.stl.discrete_time.online.previous_operation import PreviousOperation
from rtamt.semantics.stl.discrete_time.online.once_timed_operation import OnceTimedOperation
from rtamt.semantics.stl.discrete_time.online.historically_timed_operation import HistoricallyTimedOperation
from rtamt.semantics.stl.discrete_time.online.since_timed_operation import SinceTimedOperation
from rtamt.semantics.stl.discrete_time.online.precedes_timed_operation import PrecedesTimedOperation
from rtamt.exception.exception import RTAMTException

class StlDiscreteTimeOnlineAstVisitor(StlAstVisitor):

    def visitVariable(self, node, *args, **kwargs):
        pass

    def visitPredicate(self, node, *args, **kwargs):
        pass

    def visitAbs(self, node, *args, **kwargs):
        pass

    def visitSqrt(self, node, *args, **kwargs):
        pass

    def visitExp(self, node, *args, **kwargs):
        pass

    def visitPow(self, node, *args, **kwargs):
        pass

    def visitAddition(self, node, *args, **kwargs):
        pass

    def visitSubtraction(self, node, *args, **kwargs):
        pass

    def visitMultiplication(self, node, *args, **kwargs):
        pass

    def visitDivision(self, node, *args, **kwargs):
        pass

    def visitLog(self, node, *args, **kwargs):
        pass

    def visitLn(self, node, *args, **kwargs):
        pass

    def visitNegate(self, node, *args, **kwargs):
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

    def visitHistorically(self, node, *args, **kwargs):
        pass

    def visitSince(self, node, *args, **kwargs):
        pass

    def visitRise(self, node, *args, **kwargs):
        pass

    def visitFall(self, node, *args, **kwargs):
        pass

    def visitPrevious(self, node, *args, **kwargs):
        pass

    def visitStrongPrevious(self, node, *args, **kwargs):
        pass

    def visitNext(self, node, *args, **kwargs):
        pass

    def visitStrongNext(self, node, *args, **kwargs):
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