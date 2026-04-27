from rtamt.semantics.abstract_online_operation import AbstractOnlineOperation
from rtamt.semantics.enumerations.comp_oper import StlComparisonOperator
from rtamt.exception.exception import RTAMTException

class PredicateOperation(AbstractOnlineOperation):

    def __init__(self, comparison_op):
        pass

    def reset(self):
        pass

    def update(self, sample_left, sample_right):
        pass

    def sat(self, sample_left, sample_right):
        pass