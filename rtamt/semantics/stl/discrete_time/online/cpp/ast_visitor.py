from rtamt.syntax.ast.visitor.stl.ast_visitor import StlAstVisitor
from rtamt.semantics.enumerations.comp_op import StlComparisonOperator as CompOp
from rtamt.lib.rtamt_stl_library_wrapper.stl_combinatorial_binary_node import CombinatorialBinaryOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_comp_op import StlComparisonOperator
from rtamt.lib.rtamt_stl_library_wrapper.stl_not_node import NotOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_addition_node import AdditionOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_predicate_node import PredicateOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_multiplication_node import MultiplicationOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_subtraction_node import SubtractionOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_division_node import DivisionOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_and_node import AndOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_or_node import OrOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_implies_node import ImpliesOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_iff_node import IffOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_xor_node import XorOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_since_node import SinceOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_abs_node import AbsOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_exp_node import ExpOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_pow_node import PowOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_sqrt_node import SqrtOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_rise_node import RiseOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_fall_node import FallOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_once_node import OnceOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_historically_node import HistoricallyOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_always_node import AlwaysOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_eventually_node import EventuallyOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_previous_node import PreviousOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_constant_node import ConstantOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_once_bounded_node import OnceBoundedOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_historically_bounded_node import HistoricallyBoundedOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_since_bounded_node import SinceBoundedOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_precedes_bounded_node import PrecedesBoundedOperation
from rtamt.exception.exception import RTAMTException

class StlDiscreteTimeOnlineAstVisitorCpp(StlAstVisitor):

    def visitPredicate(self, node, *args, **kwargs):
        pass

    def visitAbs(self, node, *args, **kwargs):
        pass

    def visitPow(self, node, *args, **kwargs):
        pass

    def visitExp(self, node, *args, **kwargs):
        pass

    def visitSqrt(self, node, *args, **kwargs):
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

    def op_cpp(self, op):
        pass