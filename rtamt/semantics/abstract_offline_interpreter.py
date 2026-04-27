from abc import abstractmethod
from rtamt.semantics.abstract_interpreter import AbstractInterpreter

class AbstractOfflineInterpreter(AbstractInterpreter):

    def __init__(self):
        pass

    @abstractmethod
    def evaluate(self, dataset):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

    def visitSpec(self, node, *args, **kwargs):
        pass