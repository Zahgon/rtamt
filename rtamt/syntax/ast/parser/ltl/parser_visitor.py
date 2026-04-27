import logging
import operator
from antlr4 import *
from rtamt.antlr.parser.ltl.LtlParserVisitor import LtlParserVisitor
from rtamt.syntax.node.ltl.variable import Variable
from rtamt.syntax.node.ltl.predicate import Predicate
from rtamt.syntax.node.ltl.previous import Previous
from rtamt.syntax.node.ltl.next import Next
from rtamt.syntax.node.ltl.neg import Neg
from rtamt.syntax.node.ltl.until import Until
from rtamt.syntax.node.ltl.conjunction import Conjunction
from rtamt.syntax.node.ltl.disjunction import Disjunction
from rtamt.syntax.node.ltl.implies import Implies
from rtamt.syntax.node.ltl.iff import Iff
from rtamt.syntax.node.ltl.strong_next import StrongNext
from rtamt.syntax.node.ltl.strong_previous import StrongPrevious
from rtamt.syntax.node.ltl.xor import Xor
from rtamt.syntax.node.ltl.always import Always
from rtamt.syntax.node.ltl.eventually import Eventually
from rtamt.syntax.node.ltl.once import Once
from rtamt.syntax.node.ltl.historically import Historically
from rtamt.syntax.node.ltl.since import Since
from rtamt.syntax.node.arithmetic.abs import Abs
from rtamt.syntax.node.arithmetic.sqrt import Sqrt
from rtamt.syntax.node.arithmetic.exp import Exp
from rtamt.syntax.node.arithmetic.pow import Pow
from rtamt.syntax.node.arithmetic.log import Log
from rtamt.syntax.node.arithmetic.ln import Ln
from rtamt.syntax.node.arithmetic.addition import Addition
from rtamt.syntax.node.arithmetic.subtraction import Subtraction
from rtamt.syntax.node.arithmetic.negate import Negate
from rtamt.syntax.node.arithmetic.multiplication import Multiplication
from rtamt.syntax.node.arithmetic.division import Division
from rtamt.syntax.node.ltl.fall import Fall
from rtamt.syntax.node.ltl.rise import Rise
from rtamt.syntax.node.ltl.constant import Constant
from rtamt.exception.exception import RTAMTException

class LtlAstParserVisitor(LtlParserVisitor):

    def visitExprPredicate(self, ctx):
        pass

    def visitExprId(self, ctx):
        pass

    def visitVariableDeclaration(self, ctx):
        pass

    def visitConstantDeclaration(self, ctx):
        pass

    def visitRosTopic(self, ctx):
        pass

    def visitModImport(self, ctx):
        pass

    def visitExprAddSub(self, ctx):
        pass

    def visitExprNegate(self, ctx):
        pass

    def visitExprMultDiv(self, ctx):
        pass

    def visitExprAbs(self, ctx):
        pass

    def visitExprSqrt(self, ctx):
        pass

    def visitExprExp(self, ctx):
        pass

    def visitExprPow(self, ctx):
        pass

    def visitExprLog(self, ctx):
        pass

    def visitExprLn(self, ctx):
        pass

    def visitExprNot(self, ctx):
        pass

    def visitExprRise(self, ctx):
        pass

    def visitExprLiteral(self, ctx):
        pass

    def visitExprFall(self, ctx):
        pass

    def visitExprAnd(self, ctx):
        pass

    def visitExprOr(self, ctx):
        pass

    def visitExprImplies(self, ctx):
        pass

    def visitExprIff(self, ctx):
        pass

    def visitExprXor(self, ctx):
        pass

    def visitExprAlways(self, ctx):
        pass

    def visitExprEv(self, ctx):
        pass

    def visitExprPrevious(self, ctx):
        pass

    def visitExprStrongPrevious(self, ctx):
        pass

    def visitExprNext(self, ctx):
        pass

    def visitExprStrongNext(self, ctx):
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

    def visitExprParen(self, ctx):
        pass

    def visitExpr(self, ctx):
        pass

    def visitAssertion(self, ctx):
        pass

    def visitSpecification_file(self, ctx):
        pass

    def visitSpecification(self, ctx):
        pass

    def visitSpecificationId(self, ctx):
        pass

    def str_to_op_type(self, input):
        pass