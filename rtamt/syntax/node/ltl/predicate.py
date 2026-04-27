from rtamt.syntax.node.binary_node import BinaryNode

class Predicate(BinaryNode):
    """A class for storing STL real-valued Variable nodes
                Inherits Node

    Attributes:
        child1 : Node
        child2 : Node
        operator : OperatorType (LEQ, GEQ, LESS, GREATER, EQ or NEQ)
    """

    def __init__(self, child1, child2, operator):
        """Constructor for Predicate node

        Parameters:
            var : String
            field : String
            io_type : IOType enumeration (INPUT, OUTPUT or UNKNOWN)
            operator : OperatorType (LEQ, GEQ, LESS, GREATER, EQ or NEQ)
        """
        pass

    @property
    def operator(self):
        """Getter for operator"""
        pass

    @operator.setter
    def operator(self, operator):
        """Setter for operator"""
        pass