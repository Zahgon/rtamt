import os
from abc import ABCMeta
from rtamt.semantics.abstract_discrete_time_online_interpreter import AbstractDiscreteTimeOnlineInterpreter
from rtamt.semantics.abstract_dense_time_online_interpreter import AbstractDenseTimeOnlineInterpreter
from rtamt.semantics.abstract_discrete_time_offline_interpreter import AbstractDiscreteTimeOfflineInterpreter
from rtamt.semantics.abstract_dense_time_offline_interpreter import AbstractDenseTimeOfflineInterpreter
from rtamt.semantics.discrete_time_interpreter import DiscreteTimeInterpreter
from rtamt.exception.exception import RTAMTException
from antlr4 import *
from antlr4.InputStream import InputStream
from antlr4.error.ErrorListener import ErrorListener

class AbstractSpecification(object):
    __metaclass__ = ABCMeta

    def __init__(self, ast):
        pass

    @property
    def name(self):
        pass

    @name.setter
    def name(self, name):
        pass

    @property
    def spec(self):
        pass

    @spec.setter
    def spec(self, spec):
        pass

    def add_var(self, var):
        pass

    def get_value(self, phi_name):
        pass

    def add_sub_spec(self, sub_spec):
        pass

    def set_var_io_type(self, var, io_type):
        pass

    def declare_var(self, var_name, var_type):
        pass

    def declare_const(self, const_name, const_type, const_val):
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
    def var_topic_dict(self):
        pass

    @var_topic_dict.setter
    def var_topic_dict(self, var_topic_dict):
        pass

    @property
    def var_object_dict(self):
        pass

    @var_object_dict.setter
    def var_object_dict(self, var_object_dict):
        pass

    @property
    def phi_name_to_node_dict(self):
        pass

    @phi_name_to_node_dict.setter
    def phi_name_to_node_dict(self, phi_name_to_node_dict):
        pass

    @property
    def free_vars(self):
        pass

    @free_vars.setter
    def free_vars(self, free_vars):
        pass

    def modules(self, modules):
        pass

    def import_module(self, from_name, module_name):
        pass

    def set_var_topic(self, var_name, var_topic):
        pass

    def spec_print(self):
        pass

    def parse(self):
        pass

    def set_sampling_period(self, sampling_period=int(1), unit='s', tolerance=float(0.1)):
        pass

    def get_sampling_frequency(self):
        pass

    @property
    def sampling_violation_counter(self):
        pass

    @property
    def sampling_tolerance(self):
        pass

    @property
    def publish_var(self):
        pass

    @publish_var.setter
    def publish_var(self, publish_var):
        pass

    @property
    def publish_var_field(self):
        pass

    @publish_var_field.setter
    def publish_var_field(self, publish_var_field):
        pass

    def add_input_var(self, input_var):
        pass

    def remove_input_var(self, var):
        pass

    def add_output_var(self, output_var):
        pass

    def remove_output_var(self, var):
        pass

    def add_op(self, op):
        pass

    def get_spec_from_file(self, path):
        """Opens a text file and returns its content as a string
        Parameters:
            path : String - path to the filename
        Returns
            out : String - file content
        """
        pass

class DiscreteTimeOfflineInterpreter(object):
    pass

class AbstractOfflineSpecification(AbstractSpecification):

    def __init__(self, ast, offlineInterpreter, explainer=None):
        pass

    def explain(self):
        pass

    def evaluate(self, *args, **kwargs):
        pass

class AbstractOnlineSpecification(AbstractSpecification):

    def __init__(self, ast, onlineInterpreter, pastifier=None):
        pass

    def pastify(self):
        pass

    def update(self, *args, **kwargs):
        pass

    def final_update(self, *args, **kwargs):
        pass

    def reset(self):
        pass

class AbstractOfflineOnlineSpecification(AbstractOfflineSpecification, AbstractOnlineSpecification):

    def __init__(self, ast, offlineInterpreter, onlineInterpreter, pastifier=None):
        pass