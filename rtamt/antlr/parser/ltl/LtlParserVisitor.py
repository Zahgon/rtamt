from antlr4 import *
if __name__ is not None and '.' in __name__:
    from .LtlParser import LtlParser
else:
    from LtlParser import LtlParser

class LtlParserVisitor(ParseTreeVisitor):

    def visitSpecification_file(self, ctx: LtlParser.Specification_fileContext):
        pass

    def visitSpecification(self, ctx: LtlParser.SpecificationContext):
        pass

    def visitSpecificationId(self, ctx: LtlParser.SpecificationIdContext):
        pass

    def visitModImport(self, ctx: LtlParser.ModImportContext):
        pass

    def visitAssertion(self, ctx: LtlParser.AssertionContext):
        pass

    def visitDeclVariable(self, ctx: LtlParser.DeclVariableContext):
        pass

    def visitDeclConstant(self, ctx: LtlParser.DeclConstantContext):
        pass

    def visitAnnotation(self, ctx: LtlParser.AnnotationContext):
        pass

    def visitRosTopic(self, ctx: LtlParser.RosTopicContext):
        pass

    def visitVariableDeclaration(self, ctx: LtlParser.VariableDeclarationContext):
        pass

    def visitConstantDeclaration(self, ctx: LtlParser.ConstantDeclarationContext):
        pass

    def visitAsgnLiteral(self, ctx: LtlParser.AsgnLiteralContext):
        pass

    def visitAsgnExpr(self, ctx: LtlParser.AsgnExprContext):
        pass

    def visitDomainType(self, ctx: LtlParser.DomainTypeContext):
        pass

    def visitIoType(self, ctx: LtlParser.IoTypeContext):
        pass

    def visitExprNot(self, ctx: LtlParser.ExprNotContext):
        pass

    def visitExprNext(self, ctx: LtlParser.ExprNextContext):
        pass

    def visitExprAddSub(self, ctx: LtlParser.ExprAddSubContext):
        pass

    def visitExprUnless(self, ctx: LtlParser.ExprUnlessContext):
        pass

    def visitExprFall(self, ctx: LtlParser.ExprFallContext):
        pass

    def visitExprPredicate(self, ctx: LtlParser.ExprPredicateContext):
        pass

    def visitExprRise(self, ctx: LtlParser.ExprRiseContext):
        pass

    def visitExprOr(self, ctx: LtlParser.ExprOrContext):
        pass

    def visitExprLog(self, ctx: LtlParser.ExprLogContext):
        pass

    def visitExprId(self, ctx: LtlParser.ExprIdContext):
        pass

    def visitExprSince(self, ctx: LtlParser.ExprSinceContext):
        pass

    def visitExprParen(self, ctx: LtlParser.ExprParenContext):
        pass

    def visitExprIff(self, ctx: LtlParser.ExprIffContext):
        pass

    def visitExpreOnce(self, ctx: LtlParser.ExpreOnceContext):
        pass

    def visitExprEv(self, ctx: LtlParser.ExprEvContext):
        pass

    def visitExprStrongPrevious(self, ctx: LtlParser.ExprStrongPreviousContext):
        pass

    def visitExprImplies(self, ctx: LtlParser.ExprImpliesContext):
        pass

    def visitExprUntil(self, ctx: LtlParser.ExprUntilContext):
        pass

    def visitExprStrongNext(self, ctx: LtlParser.ExprStrongNextContext):
        pass

    def visitExprAbs(self, ctx: LtlParser.ExprAbsContext):
        pass

    def visitExprAnd(self, ctx: LtlParser.ExprAndContext):
        pass

    def visitExprPow(self, ctx: LtlParser.ExprPowContext):
        pass

    def visitExprPrevious(self, ctx: LtlParser.ExprPreviousContext):
        pass

    def visitExprHist(self, ctx: LtlParser.ExprHistContext):
        pass

    def visitExprNegate(self, ctx: LtlParser.ExprNegateContext):
        pass

    def visitExprXor(self, ctx: LtlParser.ExprXorContext):
        pass

    def visitExprLn(self, ctx: LtlParser.ExprLnContext):
        pass

    def visitExprExp(self, ctx: LtlParser.ExprExpContext):
        pass

    def visitExprAlways(self, ctx: LtlParser.ExprAlwaysContext):
        pass

    def visitExprLiteral(self, ctx: LtlParser.ExprLiteralContext):
        pass

    def visitExprMultDiv(self, ctx: LtlParser.ExprMultDivContext):
        pass

    def visitExprSqrt(self, ctx: LtlParser.ExprSqrtContext):
        pass

    def visitMult(self, ctx: LtlParser.MultContext):
        pass

    def visitDiv(self, ctx: LtlParser.DivContext):
        pass

    def visitPlus(self, ctx: LtlParser.PlusContext):
        pass

    def visitMinus(self, ctx: LtlParser.MinusContext):
        pass

    def visitLeq(self, ctx: LtlParser.LeqContext):
        pass

    def visitGeq(self, ctx: LtlParser.GeqContext):
        pass

    def visitLess(self, ctx: LtlParser.LessContext):
        pass

    def visitGreater(self, ctx: LtlParser.GreaterContext):
        pass

    def visitEq(self, ctx: LtlParser.EqContext):
        pass

    def visitNeq(self, ctx: LtlParser.NeqContext):
        pass

    def visitLiteral(self, ctx: LtlParser.LiteralContext):
        pass
del LtlParser