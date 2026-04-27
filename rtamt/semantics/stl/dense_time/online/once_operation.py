from rtamt.semantics.abstract_dense_time_online_operation import AbstractDenseTimeOnlineOperation

class OnceOperation(AbstractDenseTimeOnlineOperation):

    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample, *args, **kargs):
        pass

    def update_final(self, sample, *args, **kargs):
        pass