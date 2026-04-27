from rtamt.syntax.node.binary_node import BinaryNode

class Disjunction(BinaryNode):
    """A class for storing STL Or nodes
        Inherits TemporalNode
    """

    def __init__(self, child1, child2):
        """Constructor for Or node

        Parameters:
            child1 : stl.Node
            child2 : stl.Node
        """
        pass