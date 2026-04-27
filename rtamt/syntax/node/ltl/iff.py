from rtamt.syntax.node.binary_node import BinaryNode

class Iff(BinaryNode):
    """A class for storing STL Iff nodes
        Inherits TemporalNode
    """

    def __init__(self, child1, child2):
        """Constructor for Iff node

        Parameters:
            child1 : stl.Node
            child2 : stl.Node
        """
        pass