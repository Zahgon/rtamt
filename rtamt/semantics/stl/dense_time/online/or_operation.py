from rtamt.semantics.abstract_dense_time_online_operation import AbstractDenseTimeOnlineOperation
import rtamt.semantics.stl.dense_time.online.intersection as intersect

class OrOperation(AbstractDenseTimeOnlineOperation):

    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample_left, sample_right, *args, **kargs):
        pass

    def update_final(self, sample_left, sample_right, *args, **kargs):
        pass