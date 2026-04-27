from rtamt.semantics.interval.interval import Interval
from rtamt.syntax.node.unary_node import UnaryNode

class TimedEventually(UnaryNode, Interval):
    """A class for storing STL Eventually nodes
            Inherits TemporalNode
    """

    def __init__(self, child, interval, is_pure_python=True):
        """Constructor for Eventually node

        Parameters:
            child : stl.Node
            bound : Interval
        """
        pass