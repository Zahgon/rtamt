"""
Created on Sun Jul 21 22:24:09 2019

@author: NickovicD
"""
from rtamt.syntax.node.binary_node import BinaryNode

class Conjunction(BinaryNode):
    """A class for storing STL Conjunction nodes
        Inherits TemporalNode
    """

    def __init__(self, child1, child2):
        """Constructor for Conjunction node

            Parameters:
                child1 : stl.Node
                child2 : stl.Node
        """
        pass