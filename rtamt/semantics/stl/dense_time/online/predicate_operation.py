from rtamt.semantics.abstract_dense_time_online_operation import AbstractDenseTimeOnlineOperation
from rtamt.semantics.enumerations.comp_oper import StlComparisonOperator
from rtamt.semantics.arithmetic.dense_time.online.subtraction_operation import SubtractionOperation
from rtamt.exception.exception import RTAMTException

class PredicateOperation(AbstractDenseTimeOnlineOperation):

    def __init__(self, comparison_op):
        pass

    def reset(self):
        pass

    def update(self, sample_left, sample_right, *args, **kargs):
        pass

    def update_final(self, node, sample_left, sample_right, *args, **kargs):
        pass

    def sat(self, sample_left, sample_right, *args, **kargs):
        pass

    def sat_final(self, sample_left, sample_right, *args, **kargs):
        pass