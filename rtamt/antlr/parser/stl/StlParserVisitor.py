from antlr4 import *
if __name__ is not None and '.' in __name__:
    from .StlParser import StlParser
else:
    from StlParser import StlParser

class StlParserVisitor(ParseTreeVisitor):

    def visitInterval(self, ctx: StlParser.IntervalContext):
        pass

    def visitIntervalTimeLiteral(self, ctx: StlParser.IntervalTimeLiteralContext):
        pass

    def visitConstantTimeLiteral(self, ctx: StlParser.ConstantTimeLiteralContext):
        pass

    def visitUnit(self, ctx: StlParser.UnitContext):
        pass

    def visitExprNot(self, ctx: StlParser.ExprNotContext):
        pass

    def visitExprNext(self, ctx: StlParser.ExprNextContext):
        pass

    def visitExprAddSub(self, ctx: StlParser.ExprAddSubContext):
        pass

    def visitExprUnless(self, ctx: StlParser.ExprUnlessContext):
        pass

    def visitExprFall(self, ctx: StlParser.ExprFallContext):
        pass

    def visitExprPredicate(self, ctx: StlParser.ExprPredicateContext):
        pass

    def visitExprRise(self, ctx: StlParser.ExprRiseContext):
        pass

    def visitExprOr(self, ctx: StlParser.ExprOrContext):
        pass

    def visitExprLog(self, ctx: StlParser.ExprLogContext):
        pass

    def visitExprId(self, ctx: StlParser.ExprIdContext):
        pass

    def visitExprSince(self, ctx: StlParser.ExprSinceContext):
        pass

    def visitExprParen(self, ctx: StlParser.ExprParenContext):
        pass

    def visitExprIff(self, ctx: StlParser.ExprIffContext):
        pass

    def visitExpreOnce(self, ctx: StlParser.ExpreOnceContext):
        pass

    def visitExprEv(self, ctx: StlParser.ExprEvContext):
        pass

    def visitExprStrongPrevious(self, ctx: StlParser.ExprStrongPreviousContext):
        pass

    def visitExprImplies(self, ctx: StlParser.ExprImpliesContext):
        pass

    def visitExprUntil(self, ctx: StlParser.ExprUntilContext):
        pass

    def visitExprStrongNext(self, ctx: StlParser.ExprStrongNextContext):
        pass

    def visitExprAbs(self, ctx: StlParser.ExprAbsContext):
        pass

    def visitExprAnd(self, ctx: StlParser.ExprAndContext):
        pass

    def visitExprPow(self, ctx: StlParser.ExprPowContext):
        pass

    def visitExprPrevious(self, ctx: StlParser.ExprPreviousContext):
        pass

    def visitExprHist(self, ctx: StlParser.ExprHistContext):
        pass

    def visitExprNegate(self, ctx: StlParser.ExprNegateContext):
        pass

    def visitExprXor(self, ctx: StlParser.ExprXorContext):
        pass

    def visitExprLn(self, ctx: StlParser.ExprLnContext):
        pass

    def visitExprExp(self, ctx: StlParser.ExprExpContext):
        pass

    def visitExprAlways(self, ctx: StlParser.ExprAlwaysContext):
        pass

    def visitExprLiteral(self, ctx: StlParser.ExprLiteralContext):
        pass

    def visitExprMultDiv(self, ctx: StlParser.ExprMultDivContext):
        pass

    def visitExprSqrt(self, ctx: StlParser.ExprSqrtContext):
        pass

    def visitSpecification_file(self, ctx: StlParser.Specification_fileContext):
        pass

    def visitSpecification(self, ctx: StlParser.SpecificationContext):
        pass

    def visitSpecificationId(self, ctx: StlParser.SpecificationIdContext):
        pass

    def visitModImport(self, ctx: StlParser.ModImportContext):
        pass

    def visitAssertion(self, ctx: StlParser.AssertionContext):
        pass

    def visitDeclVariable(self, ctx: StlParser.DeclVariableContext):
        pass

    def visitDeclConstant(self, ctx: StlParser.DeclConstantContext):
        pass

    def visitAnnotation(self, ctx: StlParser.AnnotationContext):
        pass

    def visitRosTopic(self, ctx: StlParser.RosTopicContext):
        pass

    def visitVariableDeclaration(self, ctx: StlParser.VariableDeclarationContext):
        pass

    def visitConstantDeclaration(self, ctx: StlParser.ConstantDeclarationContext):
        pass

    def visitAsgnLiteral(self, ctx: StlParser.AsgnLiteralContext):
        pass

    def visitAsgnExpr(self, ctx: StlParser.AsgnExprContext):
        pass

    def visitDomainType(self, ctx: StlParser.DomainTypeContext):
        pass

    def visitIoType(self, ctx: StlParser.IoTypeContext):
        pass

    def visitMult(self, ctx: StlParser.MultContext):
        pass

    def visitDiv(self, ctx: StlParser.DivContext):
        pass

    def visitPlus(self, ctx: StlParser.PlusContext):
        pass

    def visitMinus(self, ctx: StlParser.MinusContext):
        pass

    def visitLeq(self, ctx: StlParser.LeqContext):
        pass

    def visitGeq(self, ctx: StlParser.GeqContext):
        pass

    def visitLess(self, ctx: StlParser.LessContext):
        pass

    def visitGreater(self, ctx: StlParser.GreaterContext):
        pass

    def visitEq(self, ctx: StlParser.EqContext):
        pass

    def visitNeq(self, ctx: StlParser.NeqContext):
        pass

    def visitLiteral(self, ctx: StlParser.LiteralContext):
        pass
del StlParser