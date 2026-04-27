"""
Created on Mon Sep 23 2019

@author: Dejan Nickovic
"""
from abc import ABCMeta
from rtamt.exception.exception import RTAMTException

class AbstractInterpreter(object):
    """
    Abstract Operation: template for any monitoring operation
    """
    __metaclass__ = ABCMeta
    NOT_IMPLEMENTED = 'You should implement this.'

    def exist_ast(self):
        pass

    def set_ast(self, ast):
        pass