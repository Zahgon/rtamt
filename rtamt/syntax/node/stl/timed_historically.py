from rtamt.semantics.interval.interval import Interval
from rtamt.syntax.node.unary_node import UnaryNode

class TimedHistorically(UnaryNode, Interval):

    def __init__(self, child, interval, is_pure_python=True):
        pass