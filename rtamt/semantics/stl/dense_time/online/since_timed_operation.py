from rtamt.semantics.abstract_dense_time_online_operation import AbstractDenseTimeOnlineOperation
from rtamt.semantics.stl.dense_time.online.since_operation import SinceOperation
from rtamt.semantics.stl.dense_time.online.once_timed_operation import OnceTimedOperation
from rtamt.semantics.stl.dense_time.online.historically_timed_operation import HistoricallyTimedOperation
from rtamt.semantics.stl.dense_time.online.and_operation import AndOperation

class SinceTimedOperation(AbstractDenseTimeOnlineOperation):

    def __init__(self, begin, end):
        pass

    def reset(self):
        pass

    def update(self, sample_left, sample_right, *args, **kargs):
        pass

    def update_final(self, sample_left, sample_right, *args, **kargs):
        pass