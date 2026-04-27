from __future__ import print_function
from antlr4 import *
from io import StringIO

def serializedATN():
    pass

class StlLexer(Lexer):
    atn = ATNDeserializer().deserialize(serializedATN())
    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]
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
    SEC = 20
    MSEC = 21
    USEC = 22
    NSEC = 23
    PSEC = 24
    ROS_Topic = 25
    Import = 26
    Input = 27
    Output = 28
    Internal = 29
    Constant = 30
    DomainTypeReal = 31
    DomainTypeFloat = 32
    DomainTypeLong = 33
    DomainTypeComplex = 34
    DomainTypeInt = 35
    DomainTypeBool = 36
    Assertion = 37
    Specification = 38
    From = 39
    NotOperator = 40
    OrOperator = 41
    AndOperator = 42
    IffOperator = 43
    ImpliesOperator = 44
    XorOperator = 45
    RiseOperator = 46
    FallOperator = 47
    AlwaysOperator = 48
    EventuallyOperator = 49
    UntilOperator = 50
    UnlessOperator = 51
    HistoricallyOperator = 52
    OnceOperator = 53
    SinceOperator = 54
    NextOperator = 55
    PreviousOperator = 56
    StrongNextOperator = 57
    StrongPreviousOperator = 58
    EqualOperator = 59
    NotEqualOperator = 60
    GreaterOrEqualOperator = 61
    LesserOrEqualOperator = 62
    GreaterOperator = 63
    LesserOperator = 64
    EQUAL = 65
    BooleanLiteral = 66
    TRUE = 67
    FALSE = 68
    IntegerLiteral = 69
    RealLiteral = 70
    Identifier = 71
    LINE_TERMINATOR = 72
    WHITESPACE = 73
    COMMENT = 74
    LINE_COMMENT = 75
    modeNames = [u'DEFAULT_MODE']
    literalNames = [u'<INVALID>', u"'-'", u"'+'", u"'*'", u"'/'", u"'('", u"')'", u"'{'", u"'}'", u"'['", u"']'", u"';'", u"':'", u"','", u"'.'", u"'@'", u"'abs'", u"'sqrt'", u"'exp'", u"'pow'", u"'s'", u"'ms'", u"'us'", u"'ns'", u"'ps'", u"'topic'", u"'import'", u"'input'", u"'output'", u"'internal'", u"'const'", u"'real'", u"'float'", u"'long'", u"'complex'", u"'int'", u"'bool'", u"'assertion'", u"'specification'", u"'from'", u"'xor'", u"'rise'", u"'fall'", u"'=='", u"'!=='", u"'>='", u"'<='", u"'>'", u"'<'", u"'='"]
    symbolicNames = [u'<INVALID>', u'MINUS', u'PLUS', u'TIMES', u'DIVIDE', u'LPAREN', u'RPAREN', u'LBRACE', u'RBRACE', u'LBRACK', u'RBRACK', u'SEMICOLON', u'COLON', u'COMMA', u'DOT', u'AT', u'ABS', u'SQRT', u'EXP', u'POW', u'SEC', u'MSEC', u'USEC', u'NSEC', u'PSEC', u'ROS_Topic', u'Import', u'Input', u'Output', u'Internal', u'Constant', u'DomainTypeReal', u'DomainTypeFloat', u'DomainTypeLong', u'DomainTypeComplex', u'DomainTypeInt', u'DomainTypeBool', u'Assertion', u'Specification', u'From', u'NotOperator', u'OrOperator', u'AndOperator', u'IffOperator', u'ImpliesOperator', u'XorOperator', u'RiseOperator', u'FallOperator', u'AlwaysOperator', u'EventuallyOperator', u'UntilOperator', u'UnlessOperator', u'HistoricallyOperator', u'OnceOperator', u'SinceOperator', u'NextOperator', u'PreviousOperator', u'StrongNextOperator', u'StrongPreviousOperator', u'EqualOperator', u'NotEqualOperator', u'GreaterOrEqualOperator', u'LesserOrEqualOperator', u'GreaterOperator', u'LesserOperator', u'EQUAL', u'BooleanLiteral', u'TRUE', u'FALSE', u'IntegerLiteral', u'RealLiteral', u'Identifier', u'LINE_TERMINATOR', u'WHITESPACE', u'COMMENT', u'LINE_COMMENT']
    ruleNames = [u'MINUS', u'PLUS', u'TIMES', u'DIVIDE', u'LPAREN', u'RPAREN', u'LBRACE', u'RBRACE', u'LBRACK', u'RBRACK', u'SEMICOLON', u'COLON', u'COMMA', u'DOT', u'AT', u'ABS', u'SQRT', u'EXP', u'POW', u'SEC', u'MSEC', u'USEC', u'NSEC', u'PSEC', u'ROS_Topic', u'Import', u'Input', u'Output', u'Internal', u'Constant', u'DomainTypeReal', u'DomainTypeFloat', u'DomainTypeLong', u'DomainTypeComplex', u'DomainTypeInt', u'DomainTypeBool', u'Assertion', u'Specification', u'From', u'NotOperator', u'OrOperator', u'AndOperator', u'IffOperator', u'ImpliesOperator', u'XorOperator', u'RiseOperator', u'FallOperator', u'AlwaysOperator', u'EventuallyOperator', u'UntilOperator', u'UnlessOperator', u'HistoricallyOperator', u'OnceOperator', u'SinceOperator', u'NextOperator', u'PreviousOperator', u'StrongNextOperator', u'StrongPreviousOperator', u'EqualOperator', u'NotEqualOperator', u'GreaterOrEqualOperator', u'LesserOrEqualOperator', u'GreaterOperator', u'LesserOperator', u'EQUAL', u'BooleanLiteral', u'TRUE', u'FALSE', u'IntegerLiteral', u'DecimalNumeral', u'Digits', u'Digit', u'NonZeroDigit', u'DigitsAndUnderscores', u'DigitOrUnderscore', u'Underscores', u'HexNumeral', u'HexDigits', u'HexDigit', u'HexDigitsAndUnderscores', u'HexDigitOrUnderscore', u'BinaryNumeral', u'BinaryDigits', u'BinaryDigit', u'BinaryDigitsAndUnderscores', u'BinaryDigitOrUnderscore', u'RealLiteral', u'DecimalRealLiteral', u'ExponentPart', u'ExponentIndicator', u'SignedInteger', u'Sign', u'Identifier', u'IdentifierStart', u'IdentifierPart', u'LetterOrUnderscore', u'Letter', u'LINE_TERMINATOR', u'WHITESPACE', u'COMMENT', u'LINE_COMMENT']
    grammarFileName = u'StlLexer.g4'

    def __init__(self, input=None):
        pass