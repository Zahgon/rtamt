from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    pass

class LtlLexer(Lexer):
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
    channelNames = [u'DEFAULT_TOKEN_CHANNEL', u'HIDDEN']
    modeNames = ['DEFAULT_MODE']
    literalNames = ['<INVALID>', "'-'", "'+'", "'*'", "'/'", "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "':'", "','", "'.'", "'@'", "'abs'", "'sqrt'", "'exp'", "'pow'", "'log'", "'ln'", "'s'", "'ms'", "'us'", "'ns'", "'ps'", "'topic'", "'import'", "'input'", "'output'", "'internal'", "'const'", "'real'", "'float'", "'long'", "'complex'", "'int'", "'bool'", "'assertion'", "'specification'", "'from'", "'xor'", "'rise'", "'fall'", "'=='", "'!=='", "'>='", "'<='", "'>'", "'<'", "'='"]
    symbolicNames = ['<INVALID>', 'MINUS', 'PLUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACK', 'RBRACK', 'SEMICOLON', 'COLON', 'COMMA', 'DOT', 'AT', 'ABS', 'SQRT', 'EXP', 'POW', 'LOG', 'LN', 'SEC', 'MSEC', 'USEC', 'NSEC', 'PSEC', 'ROS_Topic', 'Import', 'Input', 'Output', 'Internal', 'Constant', 'DomainTypeReal', 'DomainTypeFloat', 'DomainTypeLong', 'DomainTypeComplex', 'DomainTypeInt', 'DomainTypeBool', 'Assertion', 'Specification', 'From', 'NotOperator', 'OrOperator', 'AndOperator', 'IffOperator', 'ImpliesOperator', 'XorOperator', 'RiseOperator', 'FallOperator', 'AlwaysOperator', 'EventuallyOperator', 'UntilOperator', 'UnlessOperator', 'HistoricallyOperator', 'OnceOperator', 'SinceOperator', 'NextOperator', 'PreviousOperator', 'StrongNextOperator', 'StrongPreviousOperator', 'EqualOperator', 'NotEqualOperator', 'GreaterOrEqualOperator', 'LesserOrEqualOperator', 'GreaterOperator', 'LesserOperator', 'EQUAL', 'BooleanLiteral', 'TRUE', 'FALSE', 'IntegerLiteral', 'RealLiteral', 'Identifier', 'LINE_TERMINATOR', 'WHITESPACE', 'COMMENT', 'LINE_COMMENT']
    ruleNames = ['MINUS', 'PLUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACK', 'RBRACK', 'SEMICOLON', 'COLON', 'COMMA', 'DOT', 'AT', 'ABS', 'SQRT', 'EXP', 'POW', 'LOG', 'LN', 'SEC', 'MSEC', 'USEC', 'NSEC', 'PSEC', 'ROS_Topic', 'Import', 'Input', 'Output', 'Internal', 'Constant', 'DomainTypeReal', 'DomainTypeFloat', 'DomainTypeLong', 'DomainTypeComplex', 'DomainTypeInt', 'DomainTypeBool', 'Assertion', 'Specification', 'From', 'NotOperator', 'OrOperator', 'AndOperator', 'IffOperator', 'ImpliesOperator', 'XorOperator', 'RiseOperator', 'FallOperator', 'AlwaysOperator', 'EventuallyOperator', 'UntilOperator', 'UnlessOperator', 'HistoricallyOperator', 'OnceOperator', 'SinceOperator', 'NextOperator', 'PreviousOperator', 'StrongNextOperator', 'StrongPreviousOperator', 'EqualOperator', 'NotEqualOperator', 'GreaterOrEqualOperator', 'LesserOrEqualOperator', 'GreaterOperator', 'LesserOperator', 'EQUAL', 'BooleanLiteral', 'TRUE', 'FALSE', 'IntegerLiteral', 'DecimalNumeral', 'Digits', 'Digit', 'NonZeroDigit', 'DigitsAndUnderscores', 'DigitOrUnderscore', 'Underscores', 'HexNumeral', 'HexDigits', 'HexDigit', 'HexDigitsAndUnderscores', 'HexDigitOrUnderscore', 'BinaryNumeral', 'BinaryDigits', 'BinaryDigit', 'BinaryDigitsAndUnderscores', 'BinaryDigitOrUnderscore', 'RealLiteral', 'DecimalRealLiteral', 'ExponentPart', 'ExponentIndicator', 'SignedInteger', 'Sign', 'Identifier', 'IdentifierStart', 'IdentifierPart', 'LetterOrUnderscore', 'Letter', 'LINE_TERMINATOR', 'WHITESPACE', 'COMMENT', 'LINE_COMMENT']
    grammarFileName = 'LtlLexer.g4'

    def __init__(self, input=None, output: TextIO=sys.stdout):
        pass