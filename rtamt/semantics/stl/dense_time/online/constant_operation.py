from rtamt.semantics.abstract_dense_time_online_operation import AbstractDenseTimeOnlineOperation

class ConstantOperation(AbstractDenseTimeOnlineOperation):

    def __init__(self, val):
        pass

    def update(self, *args, **kargs):
        pass

    def update_final(self, *args, **kargs):
        pass