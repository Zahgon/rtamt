from fractions import Fraction
from rtamt.semantics.time_interpreter import TimeInterpreter
from rtamt.exception.exception import RTAMTException

class DiscreteTimeInterpreter(TimeInterpreter):

    def __init__(self):
        pass

    @property
    def sampling_period(self):
        pass

    @sampling_period.setter
    def sampling_period(self, sampling_period):
        pass

    @property
    def sampling_tolerance(self):
        pass

    @sampling_tolerance.setter
    def sampling_tolerance(self, sampling_tolerance):
        pass

    @property
    def sampling_period_unit(self):
        pass

    @sampling_period_unit.setter
    def sampling_period_unit(self, sampling_period_unit):
        pass

    @property
    def sampling_violation_counter(self):
        pass

    @sampling_violation_counter.setter
    def sampling_violation_counter(self, sampling_violation_counter):
        pass

    def set_sampling_period(self, sampling_period=int(1), unit='s', tolerance=float(0.1)):
        pass

    def get_sampling_period(self):
        pass

    def get_sampling_frequency(self):
        pass

    def dataset_check(self, dataset):
        pass

    def update_sampling_violation_counter(self, duration):
        pass

    def time_unit_transformer(self, node):
        pass