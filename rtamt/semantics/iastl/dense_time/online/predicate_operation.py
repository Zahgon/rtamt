from rtamt.semantics.stl.dense_time.online.predicate_operation import PredicateOperation as StlPredicateOperation
from rtamt.semantics.enumerations.options import Semantics

class PredicateOperation(StlPredicateOperation):

    def __init__(self, comparison_op, semantics, in_vars, out_vars):
        pass

    def update(self, sample_left, sample_right):
        pass

    def update_final(self, sample_left, sample_right):
        pass