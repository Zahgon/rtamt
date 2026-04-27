from abc import ABCMeta
from rtamt.syntax.node.binary_node import BinaryNode
from rtamt.syntax.node.unary_node import UnaryNode
from rtamt.syntax.node.leaf_node import LeafNode
from rtamt.exception.exception import RTAMTException

class AbstractAstVisitor(object):
    __metaclass__ = ABCMeta

    def visitChildren(self, node, *args, **kwargs):
        pass

    def visit(self, node, *args, **kwargs):
        pass

    def visitAst(self, ast, *args, **kwargs):
        pass

    def visitSpec(self, node, *args, **kwargs):
        pass

    def visitBinary(self, node, *args, **kwargs):
        pass

    def visitUnary(self, node, *args, **kwargs):
        pass

    def visitLeaf(self, node, *args, **kwargs):
        pass