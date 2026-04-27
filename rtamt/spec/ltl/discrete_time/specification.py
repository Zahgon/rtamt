import logging
import importlib
from rtamt.explanation.ltl.discrete_time.explainer import LTLExplainer
from rtamt.spec.abstract_specification import AbstractSpecification
from rtamt.syntax.ast.parser.ltl.specification_parser import LtlAstParserVisitor
from rtamt.exception.exception import RTAMTException
from rtamt.interpreter.ltl.online_interpreter import LtlInterpreter
from rtamt.reset.ltl.reset import LTLReset
from rtamt.semantics.enumerations.options import *

class LTLDiscreteTimeSpecification(AbstractSpecification):
    """A class used as a container for STL specifications

    Attributes:
        name : String

        vars : set(String) - set of variable names
        free_vars : set(String) - set of free variable names

        sampling_period : int - size of the sampling period


        var_object_dict : dict(String,AbstractNode) - dictionary that maps variable names to their Node instances
        modules : dict(String,String) - dictionary that maps module paths to module names

        top : AbstractNode - pointer to the specification parse tree

        online_interpreter : AbstractInterpreter - pointer to the object that implements the monitoring algorithm

        update_counter : int
        previous_time : float
        sampling_violation_counter : int

    """

    def __init__(self, semantics=Semantics.STANDARD, language=Language.PYTHON):
        """Constructor for STL Specification"""
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

    def import_module(self, from_name, module_name):
        pass

    def declare_const(self, const_name, const_type, const_val):
        pass

    def declare_var(self, var_name, var_type):
        pass

    def set_var_topic(self, var_name, var_topic):
        pass

    def create_var_from_name(self, var_name):
        pass

    @property
    def semantics(self):
        pass

    @semantics.setter
    def semantics(self, semantics):
        pass

    @property
    def in_vars(self):
        pass

    @in_vars.setter
    def in_vars(self, in_vars):
        pass

    @property
    def out_vars(self):
        pass

    @out_vars.setter
    def out_vars(self, out_vars):
        pass

    def parse(self):
        pass

    def pastify(self):
        pass

    def explain(self):
        pass

    def update(self, timestamp, list_inputs):
        pass

    def evaluate(self, *args, **kargs):
        pass

    def reset(self):
        pass