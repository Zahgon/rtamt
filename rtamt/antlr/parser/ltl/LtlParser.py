from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    pass

class LtlParser(Parser):
    grammarFileName = 'LtlParser.g4'
    atn = ATNDeserializer().deserialize(serializedATN())
    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]
    sharedContextCache = PredictionContextCache()
    literalNames = ['<INVALID>', "'-'", "'+'", "'*'", "'/'", "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "':'", "','", "'.'", "'@'", "'abs'", "'sqrt'", "'exp'", "'pow'", "'log'", "'ln'", "'s'", "'ms'", "'us'", "'ns'", "'ps'", "'topic'", "'import'", "'input'", "'output'", "'internal'", "'const'", "'real'", "'float'", "'long'", "'complex'", "'int'", "'bool'", "'assertion'", "'specification'", "'from'", '<INVALID>', '<INVALID>', '<INVALID>', '<INVALID>', '<INVALID>', "'xor'", "'rise'", "'fall'", '<INVALID>', '<INVALID>', '<INVALID>', '<INVALID>', '<INVALID>', '<INVALID>', '<INVALID>', '<INVALID>', '<INVALID>', '<INVALID>', '<INVALID>', "'=='", "'!=='", "'>='", "'<='", "'>'", "'<'", "'='"]
    symbolicNames = ['<INVALID>', 'MINUS', 'PLUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACK', 'RBRACK', 'SEMICOLON', 'COLON', 'COMMA', 'DOT', 'AT', 'ABS', 'SQRT', 'EXP', 'POW', 'LOG', 'LN', 'SEC', 'MSEC', 'USEC', 'NSEC', 'PSEC', 'ROS_Topic', 'Import', 'Input', 'Output', 'Internal', 'Constant', 'DomainTypeReal', 'DomainTypeFloat', 'DomainTypeLong', 'DomainTypeComplex', 'DomainTypeInt', 'DomainTypeBool', 'Assertion', 'Specification', 'From', 'NotOperator', 'OrOperator', 'AndOperator', 'IffOperator', 'ImpliesOperator', 'XorOperator', 'RiseOperator', 'FallOperator', 'AlwaysOperator', 'EventuallyOperator', 'UntilOperator', 'UnlessOperator', 'HistoricallyOperator', 'OnceOperator', 'SinceOperator', 'NextOperator', 'PreviousOperator', 'StrongNextOperator', 'StrongPreviousOperator', 'EqualOperator', 'NotEqualOperator', 'GreaterOrEqualOperator', 'LesserOrEqualOperator', 'GreaterOperator', 'LesserOperator', 'EQUAL', 'BooleanLiteral', 'TRUE', 'FALSE', 'IntegerLiteral', 'RealLiteral', 'Identifier', 'LINE_TERMINATOR', 'WHITESPACE', 'COMMENT', 'LINE_COMMENT']
    RULE_specification_file = 0
    RULE_specification = 1
    RULE_spec = 2
    RULE_modimport = 3
    RULE_assertion = 4
    RULE_declaration = 5
    RULE_annotation = 6
    RULE_annotation_type = 7
    RULE_variableDeclaration = 8
    RULE_constantDeclaration = 9
    RULE_assignment = 10
    RULE_domainType = 11
    RULE_ioType = 12
    RULE_expression = 13
    RULE_multdivOp = 14
    RULE_addsubOp = 15
    RULE_comparisonOp = 16
    RULE_literal = 17
    ruleNames = ['specification_file', 'specification', 'spec', 'modimport', 'assertion', 'declaration', 'annotation', 'annotation_type', 'variableDeclaration', 'constantDeclaration', 'assignment', 'domainType', 'ioType', 'expression', 'multdivOp', 'addsubOp', 'comparisonOp', 'literal']
    EOF = Token.EOF
    MINUS = 1
    PLUS = 2
    TIMES = 3
    DIVIDE = 4
    LPAREN = 5
    RPAREN = 6
    LBRACE = 7
    RBRACE = 8
    LBRACK = 9
    RBRACK = 10
    SEMICOLON = 11
    COLON = 12
    COMMA = 13
    DOT = 14
    AT = 15
    ABS = 16
    SQRT = 17
    EXP = 18
    POW = 19
    LOG = 20
    LN = 21
    SEC = 22
    MSEC = 23
    USEC = 24
    NSEC = 25
    PSEC = 26
    ROS_Topic = 27
    Import = 28
    Input = 29
    Output = 30
    Internal = 31
    Constant = 32
    DomainTypeReal = 33
    DomainTypeFloat = 34
    DomainTypeLong = 35
    DomainTypeComplex = 36
    DomainTypeInt = 37
    DomainTypeBool = 38
    Assertion = 39
    Specification = 40
    From = 41
    NotOperator = 42
    OrOperator = 43
    AndOperator = 44
    IffOperator = 45
    ImpliesOperator = 46
    XorOperator = 47
    RiseOperator = 48
    FallOperator = 49
    AlwaysOperator = 50
    EventuallyOperator = 51
    UntilOperator = 52
    UnlessOperator = 53
    HistoricallyOperator = 54
    OnceOperator = 55
    SinceOperator = 56
    NextOperator = 57
    PreviousOperator = 58
    StrongNextOperator = 59
    StrongPreviousOperator = 60
    EqualOperator = 61
    NotEqualOperator = 62
    GreaterOrEqualOperator = 63
    LesserOrEqualOperator = 64
    GreaterOperator = 65
    LesserOperator = 66
    EQUAL = 67
    BooleanLiteral = 68
    TRUE = 69
    FALSE = 70
    IntegerLiteral = 71
    RealLiteral = 72
    Identifier = 73
    LINE_TERMINATOR = 74
    WHITESPACE = 75
    COMMENT = 76
    LINE_COMMENT = 77

    def __init__(self, input: TokenStream, output: TextIO=sys.stdout):
        pass

    class Specification_fileContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            pass

        def specification(self):
            pass

        def EOF(self):
            pass

        def getRuleIndex(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    def specification_file(self):
        pass

    class SpecificationContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            pass

        def spec(self):
            pass

        def modimport(self, i: int=None):
            pass

        def declaration(self, i: int=None):
            pass

        def annotation(self, i: int=None):
            pass

        def assertion(self, i: int=None):
            pass

        def getRuleIndex(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    def specification(self):
        pass

    class SpecContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            pass

        def getRuleIndex(self):
            pass

        def copyFrom(self, ctx: ParserRuleContext):
            pass

    class SpecificationIdContext(SpecContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def Specification(self):
            pass

        def Identifier(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    def spec(self):
        pass

    class ModimportContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            pass

        def getRuleIndex(self):
            pass

        def copyFrom(self, ctx: ParserRuleContext):
            pass

    class ModImportContext(ModimportContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def From(self):
            pass

        def Identifier(self, i: int=None):
            pass

        def Import(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    def modimport(self):
        pass

    class AssertionContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            pass

        def expression(self):
            pass

        def SEMICOLON(self):
            pass

        def Identifier(self):
            pass

        def EQUAL(self):
            pass

        def getRuleIndex(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    def assertion(self):
        pass

    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            pass

        def getRuleIndex(self):
            pass

        def copyFrom(self, ctx: ParserRuleContext):
            pass

    class DeclVariableContext(DeclarationContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def variableDeclaration(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class DeclConstantContext(DeclarationContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def constantDeclaration(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    def declaration(self):
        pass

    class AnnotationContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            pass

        def AT(self):
            pass

        def annotation_type(self):
            pass

        def getRuleIndex(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    def annotation(self):
        pass

    class Annotation_typeContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            pass

        def getRuleIndex(self):
            pass

        def copyFrom(self, ctx: ParserRuleContext):
            pass

    class RosTopicContext(Annotation_typeContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def ROS_Topic(self):
            pass

        def LPAREN(self):
            pass

        def Identifier(self, i: int=None):
            pass

        def COMMA(self):
            pass

        def RPAREN(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    def annotation_type(self):
        pass

    class VariableDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            pass

        def domainType(self):
            pass

        def Identifier(self):
            pass

        def ioType(self):
            pass

        def assignment(self):
            pass

        def getRuleIndex(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    def variableDeclaration(self):
        pass

    class ConstantDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            pass

        def Constant(self):
            pass

        def domainType(self):
            pass

        def Identifier(self):
            pass

        def EQUAL(self):
            pass

        def literal(self):
            pass

        def getRuleIndex(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    def constantDeclaration(self):
        pass

    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            pass

        def getRuleIndex(self):
            pass

        def copyFrom(self, ctx: ParserRuleContext):
            pass

    class AsgnExprContext(AssignmentContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def EQUAL(self):
            pass

        def expression(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class AsgnLiteralContext(AssignmentContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def EQUAL(self):
            pass

        def literal(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    def assignment(self):
        pass

    class DomainTypeContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            pass

        def DomainTypeFloat(self):
            pass

        def DomainTypeInt(self):
            pass

        def DomainTypeLong(self):
            pass

        def DomainTypeComplex(self):
            pass

        def Identifier(self):
            pass

        def getRuleIndex(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    def domainType(self):
        pass

    class IoTypeContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            pass

        def Input(self):
            pass

        def Output(self):
            pass

        def getRuleIndex(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    def ioType(self):
        pass

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            pass

        def getRuleIndex(self):
            pass

        def copyFrom(self, ctx: ParserRuleContext):
            pass

    class ExprNotContext(ExpressionContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def NotOperator(self):
            pass

        def expression(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class ExprNextContext(ExpressionContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def NextOperator(self):
            pass

        def expression(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class ExprAddSubContext(ExpressionContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def expression(self, i: int=None):
            pass

        def addsubOp(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class ExprUnlessContext(ExpressionContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def expression(self, i: int=None):
            pass

        def UnlessOperator(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class ExprFallContext(ExpressionContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def FallOperator(self):
            pass

        def LPAREN(self):
            pass

        def expression(self):
            pass

        def RPAREN(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class ExprPredicateContext(ExpressionContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def expression(self, i: int=None):
            pass

        def comparisonOp(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class ExprRiseContext(ExpressionContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def RiseOperator(self):
            pass

        def LPAREN(self):
            pass

        def expression(self):
            pass

        def RPAREN(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class ExprOrContext(ExpressionContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def expression(self, i: int=None):
            pass

        def OrOperator(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class ExprLogContext(ExpressionContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def LOG(self):
            pass

        def LPAREN(self):
            pass

        def expression(self, i: int=None):
            pass

        def COMMA(self):
            pass

        def RPAREN(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class ExprIdContext(ExpressionContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def Identifier(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class ExprSinceContext(ExpressionContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def expression(self, i: int=None):
            pass

        def SinceOperator(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class ExprParenContext(ExpressionContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def LPAREN(self):
            pass

        def expression(self):
            pass

        def RPAREN(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class ExprIffContext(ExpressionContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def expression(self, i: int=None):
            pass

        def IffOperator(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class ExpreOnceContext(ExpressionContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def OnceOperator(self):
            pass

        def expression(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class ExprEvContext(ExpressionContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def EventuallyOperator(self):
            pass

        def expression(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class ExprStrongPreviousContext(ExpressionContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def StrongPreviousOperator(self):
            pass

        def expression(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class ExprImpliesContext(ExpressionContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def expression(self, i: int=None):
            pass

        def ImpliesOperator(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class ExprUntilContext(ExpressionContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def expression(self, i: int=None):
            pass

        def UntilOperator(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class ExprStrongNextContext(ExpressionContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def StrongNextOperator(self):
            pass

        def expression(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class ExprAbsContext(ExpressionContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def ABS(self):
            pass

        def LPAREN(self):
            pass

        def expression(self):
            pass

        def RPAREN(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class ExprAndContext(ExpressionContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def expression(self, i: int=None):
            pass

        def AndOperator(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class ExprPowContext(ExpressionContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def POW(self):
            pass

        def LPAREN(self):
            pass

        def expression(self, i: int=None):
            pass

        def COMMA(self):
            pass

        def RPAREN(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class ExprPreviousContext(ExpressionContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def PreviousOperator(self):
            pass

        def expression(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class ExprHistContext(ExpressionContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def HistoricallyOperator(self):
            pass

        def expression(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class ExprNegateContext(ExpressionContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def MINUS(self):
            pass

        def expression(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class ExprXorContext(ExpressionContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def expression(self, i: int=None):
            pass

        def XorOperator(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class ExprLnContext(ExpressionContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def LN(self):
            pass

        def LPAREN(self):
            pass

        def expression(self):
            pass

        def RPAREN(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class ExprExpContext(ExpressionContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def EXP(self):
            pass

        def LPAREN(self):
            pass

        def expression(self):
            pass

        def RPAREN(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class ExprAlwaysContext(ExpressionContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def AlwaysOperator(self):
            pass

        def expression(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class ExprLiteralContext(ExpressionContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def literal(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class ExprMultDivContext(ExpressionContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def expression(self, i: int=None):
            pass

        def multdivOp(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class ExprSqrtContext(ExpressionContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def SQRT(self):
            pass

        def LPAREN(self):
            pass

        def expression(self):
            pass

        def RPAREN(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    def expression(self, _p: int=0):
        pass

    class MultdivOpContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            pass

        def getRuleIndex(self):
            pass

        def copyFrom(self, ctx: ParserRuleContext):
            pass

    class DivContext(MultdivOpContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def DIVIDE(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class MultContext(MultdivOpContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def TIMES(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    def multdivOp(self):
        pass

    class AddsubOpContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            pass

        def getRuleIndex(self):
            pass

        def copyFrom(self, ctx: ParserRuleContext):
            pass

    class PlusContext(AddsubOpContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def PLUS(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class MinusContext(AddsubOpContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def MINUS(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    def addsubOp(self):
        pass

    class ComparisonOpContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            pass

        def getRuleIndex(self):
            pass

        def copyFrom(self, ctx: ParserRuleContext):
            pass

    class GeqContext(ComparisonOpContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def GreaterOrEqualOperator(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class LeqContext(ComparisonOpContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def LesserOrEqualOperator(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class GreaterContext(ComparisonOpContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def GreaterOperator(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class NeqContext(ComparisonOpContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def NotEqualOperator(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class EqContext(ComparisonOpContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def EqualOperator(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    class LessContext(ComparisonOpContext):

        def __init__(self, parser, ctx: ParserRuleContext):
            pass

        def LesserOperator(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    def comparisonOp(self):
        pass

    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            pass

        def IntegerLiteral(self):
            pass

        def RealLiteral(self):
            pass

        def getRuleIndex(self):
            pass

        def enterRule(self, listener: ParseTreeListener):
            pass

        def exitRule(self, listener: ParseTreeListener):
            pass

        def accept(self, visitor: ParseTreeVisitor):
            pass

    def literal(self):
        pass

    def sempred(self, localctx: RuleContext, ruleIndex: int, predIndex: int):
        pass

    def expression_sempred(self, localctx: ExpressionContext, predIndex: int):
        pass