from rtamt.semantics.iastl.discrete_time.offline.interpreter import IAStlOutputRobustnessDiscreteTimeOfflineInterpreter, IAStlInputVacuityDiscreteTimeOfflineInterpreter, IAStlInputRobustnessDiscreteTimeOfflineInterpreter, IAStlOutputVacuityDiscreteTimeOfflineInterpreter
from rtamt.semantics.stl.discrete_time.online.interpreter import StlDiscreteTimeOnlineInterpreter
from rtamt.spec.abstract_specification import AbstractOfflineSpecification, AbstractOnlineSpecification, AbstractOfflineOnlineSpecification
from rtamt.syntax.ast.parser.stl.specification_parser import StlAst
from rtamt.semantics.stl.discrete_time.offline.interpreter import StlDiscreteTimeOfflineInterpreter
from rtamt.semantics.iastl.discrete_time.online.interpreter import IAStlOutputRobustnessDiscreteTimeOnlineInterpreter, IAStlInputVacuityDiscreteTimeOnlineInterpreter, IAStlInputRobustnessDiscreteTimeOnlineInterpreter, IAStlOutputVacuityDiscreteTimeOnlineInterpreter
from rtamt.semantics.enumerations.options import *
from rtamt.pastifier.stl.pastifier import StlPastifier

def IASTLDiscreteTimeSpecification(semantics=Semantics.STANDARD, language=Language.PYTHON):
    """
    A class used as a container for STL continuous time specifications
       Inherits STLSpecification

    Attributes:
    """
    pass

def IAStlOutputRobustnessDiscreteTimeOfflineSpecification():
    pass

def IAStlInputVacuityDiscreteTimeOfflineSpecification():
    pass

def IAStlInputRobustnessDiscreteTimeOfflineSpecification():
    pass

def IAStlOutputVacuityDiscreteTimeOfflineSpecification():
    pass

def IAStlOutputRobustnessDiscreteTimeOnlineSpecification():
    pass

def IAStlInputVacuityDiscreteTimeOnlineSpecification():
    pass

def IAStlInputRobustnessDiscreteTimeOnlineSpecification():
    pass

def IAStlOutputVacuityDiscreteTimeOnlineSpecification():
    pass