from rtamt.syntax.node.leaf_node import LeafNode
from rtamt.semantics.enumerations.io_type import StlIOType

class Variable(LeafNode):
    """A class for storing STL real-valued Variable nodes
            Inherits Node
        """

    def __init__(self, var, field=None, iotype='output'):
        """Constructor for Variable node

        Parameters:
            var : String
            field : String
        """
        pass

    @property
    def var(self):
        """Getter for var"""
        pass

    @var.setter
    def var(self, var):
        """Setter for var"""
        pass

    @property
    def field(self):
        """Getter for field"""
        pass

    @field.setter
    def field(self, field):
        """Setter for field"""
        pass

    @property
    def io_type(self):
        """Getter for io_type"""
        pass

    @io_type.setter
    def io_type(self, io_type):
        """Setter for io_type"""
        pass