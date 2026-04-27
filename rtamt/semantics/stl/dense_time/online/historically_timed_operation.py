from rtamt.semantics.abstract_dense_time_online_operation import AbstractDenseTimeOnlineOperation
import rtamt.semantics.stl.dense_time.online.intersection as intersect

class HistoricallyTimedOperation(AbstractDenseTimeOnlineOperation):

    def __init__(self, begin, end):
        pass

    def reset(self):
        pass

    def update(self, sample, *args, **kargs):
        pass

    def update_final(self, sample, *args, **kargs):
        pass