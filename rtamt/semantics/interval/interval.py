import logging

class Interval(object):
    """A class for storing integer intervals

        Attributes
        --------------
        begin : int
            beginning of the interval
        end : int
            end of the interval

        Methods
        --------------
        begin, end
            Getter for begin and end
            The object is immutable - the setter issues a warning message and does nothing
        """

    def __init__(self, begin, end, begin_unit='', end_unit=''):
        """Constructor for Interval
        Parameters:
            begin : int
                Beginning of the interval
            end : int
                End of the interval
        """
        pass

    @property
    def begin(self):
        """Getter for begin"""
        pass

    @begin.setter
    def begin(self, begin):
        pass

    @property
    def end(self):
        """Getter for end"""
        pass

    @end.setter
    def end(self, end):
        pass

    @property
    def begin_unit(self):
        """Getter for begin_unit"""
        pass

    @begin_unit.setter
    def begin_unit(self, begin_unit):
        pass

    @property
    def end_unit(self):
        """Getter for end_unit"""
        pass

    @end_unit.setter
    def end_unit(self, end_unit):
        pass