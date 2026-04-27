from abc import ABCMeta
import logging
import importlib
from antlr4 import *
from antlr4.InputStream import InputStream
from antlr4.error.ErrorListener import ErrorListener
from rtamt.syntax.ast.parser.stl.parser_visitor import StlAstParserVisitor
from rtamt.exception.exception import RTAMTException

class AbstractAst:
    """An abstract class for AST parser

    Attributes:
        name : String

        modular_spec : String - specification text
        spec : String - specification text

        vars : set(String) - set of variable names
        free_vars : set(String) - set of free variable names

        var_subspec_dict : dict(String, AbstractNode) - dictionary that maps variable names to the AST
        var_object_dict : dict(String, double) - dictionary that maps variable names to their value
        modules : dict(String,String) - dictionary that maps module paths to module names
        var_type_dict : dict(String, String) - dictionary that maps var names to var types
        var_io_dict : dict(String, String) - dictionary that maps var names to var io signature
        const_type_dict : dict(String, String) - dictionary mapping const var names to var types
        const_val_dict : dict(String, String) - dictionary mapping const var names to var vals encoded as strings

        ast : Node - pointer to the specification parse tree

    Methods
        parse - parse the specification

        declare_var - declare variable in spec
        declare_const - declare const variable in spec
        add_sub_spec - add sub spec

    """
    __metaclass__ = ABCMeta

    def __init__(self, antrlLexerType, antrlParserType, parserErrorListenerType=None):
        pass

    def parse(self):
        pass

    @property
    def out_var(self):
        pass

    @out_var.setter
    def out_var(self, out_var):
        pass

    @property
    def out_var_field(self):
        pass

    @out_var_field.setter
    def out_var_field(self, out_var_field):
        pass

    @property
    def spec(self):
        pass

    @spec.setter
    def spec(self, spec):
        pass

    @property
    def specs(self):
        pass

    @specs.setter
    def specs(self, specs):
        pass

    @property
    def name(self):
        pass

    @name.setter
    def name(self, name):
        pass

    @property
    def free_vars(self):
        pass

    @free_vars.setter
    def free_vars(self, free_vars):
        pass

    @property
    def vars(self):
        pass

    @vars.setter
    def vars(self, vars):
        pass

    @property
    def modules(self):
        pass

    @modules.setter
    def modules(self, modules):
        pass

    def add_var(self, var):
        pass

    def get_value(self, phi_name):
        pass

    def add_sub_spec(self, sub_spec):
        pass

    def create_var_from_name(self, var_name):
        pass

    def declare_var(self, var_name, var_type):
        pass

    def declare_const(self, const_name, const_type, const_val):
        pass

    def import_module(self, from_name, module_name):
        pass

    def set_var_topic(self, var_name, var_topic):
        pass

    def set_var_io_type(self, var_name, var_iotype):
        pass

    def add_input_var(self, input_var):
        pass

    def remove_input_var(self, var):
        pass

    def add_output_var(self, output_var):
        pass

    def remove_output_var(self, var):
        pass

def ast_factory(AstParserVisitor):
    pass