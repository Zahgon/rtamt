"""
Created on Sun Jul 21 22:30:09 2019

@author: NickovicD
"""
from rtamt.syntax.node.leaf_node import LeafNode

class Constant(LeafNode):
    """A class for storing STL real-valued Constant nodes
                Inherits Node

    Attributes:
        val : double
    """

    def __init__(self, val):
        """Constructor for Const node

        Parameters:
            val : double
        """
        pass

    @property
    def val(self):
        """Getter for val"""
        pass

    @val.setter
    def val(self, val):
        """Setter for child"""
        pass