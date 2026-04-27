"""
Created on Mon Sep 23 2019

@author: Dejan Nickovic
"""
from abc import ABCMeta

class AbstractNode:
    """
    Abstract Node: tree-like data structure containing
    arbitrary specifications
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    def add_child(self, child):
        pass

    def accept(self, visitor):
        """accept: recursive function needed to implement node visitors
        Inputs:
        visitor - Visitor object
        """
        pass

    @property
    def interpreter(self):
        """Getter for the online_interpreter"""
        pass

    @interpreter.setter
    def interpreter(self, interpreter):
        """Setter for the online_interpreter"""
        pass

    @property
    def name(self):
        """Getter for the name"""
        pass

    @name.setter
    def name(self, name):
        """Setter for the name"""
        pass

    @property
    def node(self):
        """Getter for the node"""
        pass

    @node.setter
    def node(self, node):
        """Setter for the horizon"""
        pass

    @property
    def children(self):
        pass

    @children.setter
    def children(self, children):
        pass

    @property
    def in_vars(self):
        """Getter for the in_vars"""
        pass

    @in_vars.setter
    def in_vars(self, in_vars):
        """Setter for the in_vars"""
        pass

    @property
    def out_vars(self):
        """Getter for the out_vars"""
        pass

    @out_vars.setter
    def out_vars(self, out_vars):
        """Setter for the out_vars"""
        pass

    def __repr__(self):
        """Returns representation of the object"""
        pass