from rtamt.semantics.iastl.dense_time.offline.interpreter import IAStlOutputRobustnessDenseTimeOfflineInterpreter, IAStlInputRobustnessDenseTimeOfflineInterpreter, IAStlInputVacuityDenseTimeOfflineInterpreter, IAStlOutputVacuityDenseTimeOfflineInterpreter
from rtamt.semantics.iastl.dense_time.online.interpreter import IAStlOutputRobustnessDenseTimeOnlineInterpreter, IAStlInputRobustnessDenseTimeOnlineInterpreter, IAStlOutputVacuityDenseTimeOnlineInterpreter, IAStlInputVacuityDenseTimeOnlineInterpreter
from rtamt.pastifier.stl.pastifier import StlPastifier
from rtamt.spec.abstract_specification import AbstractOfflineSpecification, AbstractOnlineSpecification, AbstractOfflineOnlineSpecification
from rtamt.syntax.ast.parser.stl.specification_parser import StlAst
from rtamt.semantics.stl.dense_time.offline.interpreter import StlDenseTimeOfflineInterpreter
from rtamt.semantics.stl.dense_time.online.interpreter import StlDenseTimeOnlineInterpreter
from rtamt.semantics.enumerations.options import *

def StlDenseTimeSpecification(semantics=Semantics.STANDARD, language=Language.PYTHON):
    """
    A class used as a container for STL continuous time specifications
       Inherits STLSpecification

    Attributes:
    """
    pass

def StlDenseTimeOfflineSpecification():
    pass

def StlDenseTimeOnlineSpecification():
    pass