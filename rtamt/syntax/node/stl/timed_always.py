"""
Created on Sun Jul 21 22:24:09 2019

@author: NickovicD
"""
from rtamt.semantics.interval.interval import Interval
from rtamt.syntax.node.unary_node import UnaryNode

class TimedAlways(UnaryNode, Interval):
    """A class for storing STL Always nodes
        Inherits TemporalNode
    """

    def __init__(self, child, interval, is_pure_python=True):
        """Constructor for Always

        Parameters:
            child : stl.Node
            bound : Interval
        """
        pass